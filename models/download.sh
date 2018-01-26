lm.trie

mkdir -p mlconv mlconv_embed
for model_name in  mlconv mlconv_embed ; do
    for i in {1..4}; do
        curl -L -o $model_name/model$i.pt https://tinyurl.com/yb4jutxq/$model_name/model$i.pt
    done
done

mkdir -p bpe_model
curl -L -o bpe_model/train.bpe.model https://tinyurl.com/yb4jutxq/bpe_model/train.bpe.model

# downloading vocab files
mkdir -p data_bin
curl -L -o data_bin/dict.src.txt https://tinyurl.com/yb4jutxq/data_bin/dict.src.txt
curl -L -o data_bin/dict.trg.txt https://tinyurl.com/yb4jutxq/data_bin/dict.trg.txt

# download reranker weights
mkdir -p reranker_weights
for reranker_weight_file in mlconv_4ens_eo.weights.txt  mlconv_embed_4ens_eo_lm.weights.txt  mlconv_embed_4ens_eo.weights.txt ; do
    curl -L -o reranker_weights/$reranker_weight_file https://tinyurl.com/yb4jutxq/reranker_weights/$reranker_weight_file
done

# downloading embeddings
echo "Downloading word embeddings (170MB)..."
mkdir -p embeddings
curl -L -o embeddings/wiki_model.vec https://tinyurl.com/yb4jutxq/embeddings/wiki_model.vec

# downloading large language model
echo "Downloading large language model (>100G)..."
mkdir -p lm
curl -L -o lm/94Bcclm.trie https://tinyurl.com/yb4jutxq/lm/94Bcclm.trie



