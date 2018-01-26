lm.trie

mkdir -p mlconv mlconv_embed
for model_name in  mlconv mlconv_embed ; do
    for i in {1..4}; do
        curl -L -o $model_name/model$i.pt http://sterling8.d2.comp.nus.edu.sg/~shamil/mlconvgec2018/models/$model_name/model$i.pt
    done
done

mkdir -p bpe_model
curl -L -o bpe_model/train.bpe.model http://sterling8.d2.comp.nus.edu.sg/~shamil/mlconvgec2018/models/bpe_model/train.bpe.model

# downloading vocab files
mkdir -p data_bin
curl -L -o data_bin/dict.src.txt http://sterling8.d2.comp.nus.edu.sg/~shamil/mlconvgec2018/models/data_bin/dict.src.txt
curl -L -o data_bin/dict.trg.txt http://sterling8.d2.comp.nus.edu.sg/~shamil/mlconvgec2018/models/data_bin/dict.trg.txt

# download reranker weights
mkdir -p reranker_weights
for reranker_weight_file in mlconv_4ens_eo.weights.txt  mlconv_embed_4ens_eo_lm.weights.txt  mlconv_embed_4ens_eo.weights.txt ; do
    curl -L -o reranker_weights/$reranker_weight_file http://sterling8.d2.comp.nus.edu.sg/~shamil/mlconvgec2018/models/reranker_weights/$reranker_weight_file
done

# downloading embeddings
echo "Downloading word embeddings (170MB)..."
mkdir -p embeddings
curl -L -o embeddings/wiki_model.vec http://sterling8.d2.comp.nus.edu.sg/~shamil/mlconvgec2018/models/embeddings/wiki_model.vec

# downloading large language model
echo "Downloading large language model (>100G)..."
mkdir -p lm
curl -L -o lm/94Bcclm.trie http://sterling8.d2.comp.nus.edu.sg/~shamil/mlconvgec2018/models/lm/94Bcclm.trie



