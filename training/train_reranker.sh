#!/bin/bash

set -e
set -x

source ../paths.sh

if [ $# -ge 5 ]; then
    output_dir=$1
    device=$2
    model_path=$3
    reranker_feats=$4
    moses_path=$5
else
    echo "Please specify the paths to the input_file and output rerdirectory"
    echo "Usage: `basename $0` <output_dir> <gpu-device-num(e.g: 0)> <path to model_file/dir> <features, e.g 'eo' or 'eolm'> <path-to-moses>"   >&2
fi


FAIRSEQPY=$SOFTWARE_DIR/fairseq-py
NBEST_RERANKER=$SOFTWARE_DIR/nbest-reranker
beam=12
nbest=$beam
threads=12

## setting model paths
if [[ -d "$model_path" ]]; then
    models=`ls $model_path/*.pt | tr '\n' ' ' | sed "s| \([^$]\)| --path \1|g"`
    echo $models
elif [[ -f "$model_path" ]]; then
    models=$model_path
elif [[ ! -e "$model_path" ]]; then
    echo "Model path not found: $model_path"
fi

###############
# training
###############

TRAIN_DIR=$output_dir/training/
mkdir -p $TRAIN_DIR
echo "[weight]" > $TRAIN_DIR/rerank_config.ini
echo "F0= 0.5" >> $TRAIN_DIR/rerank_config.ini
echo "EditOps0= 0.2 0.2 0.2" >> $TRAIN_DIR/rerank_config.ini
if [ $reranker_feats == "eolm" ]; then
    echo "LM0= 0.5" >> $TRAIN_DIR/rerank_config.ini
    echo "WordPenalty0= -1" >> $TRAIN_DIR/rerank_config.ini
fi

if [ $reranker_feats == "eo" ]; then
    featstring="EditOps(name='EditOps0')"
elif [ $reranker_feats == "eolm" ]; then
    LM_PATH=$MODEL_DIR/lm/94Bcclm.trie
    if [ ! -f $LM_PATH ]; then
        mkdir -p $MODEL_DIR/lm
        curl -L -o $MODEL_DIR/lm/94Bcclm.trie https://tinyurl.com/yb4jutxq/lm/94Bcclm.trie
    fi
    featstring="EditOps(name='EditOps0'), LM('LM0', '$MODEL_DIR/lm/94Bcclm.trie', normalize=False), WordPenalty(name='WordPenalty0')"
fi


$SCRIPTS_DIR/apply_bpe.py -c models/bpe_model/train.bpe.model < processed/dev.input.txt > $output_dir/dev.input.bpe.txt

CUDA_VISIBLE_DEVICES=$device python3.5 $FAIRSEQPY/generate.py --no-progress-bar --path $models --beam $beam --nbest $beam --interactive --workers $threads processed/bin < $output_dir/dev.input.bpe.txt > $output_dir/dev.output.bpe.nbest.txt

# reformating the nbest file
$SCRIPTS_DIR/nbest_reformat.py -i $output_dir/dev.output.bpe.nbest.txt --debpe > $output_dir/dev.output.tok.nbest.reformat.txt

# augmenting the dev nbest
$NBEST_RERANKER/augmenter.py -s processed/dev.input.txt -i $output_dir/dev.output.tok.nbest.reformat.txt -o $output_dir/dev.output.tok.nbest.reformat.augmented.txt -f "$featstring"

# training the nbest to obtain the weights
$NBEST_RERANKER/train.py -i $output_dir/dev.output.tok.nbest.reformat.augmented.txt -r processed/dev.m2 -c $TRAIN_DIR/rerank_config.ini --threads 12 --tuning-metric m2 --predictable-seed -o $TRAIN_DIR --moses-dir $moses_path --no-add-weight

cp $TRAIN_DIR/weights.txt $output_dir/weights.txt

