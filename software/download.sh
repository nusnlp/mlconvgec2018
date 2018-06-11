COMMIT=ceb2f1200c9e5b8bf42a1033e7638d3e8586609a
echo "Downloading Fairseq from https://github.com/shamilcm/fairseq-py (rev:$COMMIT)"
wget https://github.com/shamilcm/fairseq-py/archive/$COMMIT.zip
unzip $COMMIT.zip
rm $COMMIT.zip
mv fairseq-py-$COMMIT fairseq-py

COMMIT=b9453d5a211fc8f90fb25a584b39d4784f8de716
echo "Downloading n-best reranker from https://github.com/nusnlp/nbest-reranker (rev: $COMMIT)"
wget https://github.com/nusnlp/nbest-reranker/archive/$COMMIT.zip
unzip $COMMIT.zip
rm $COMMIT.zip
mv nbest-reranker-$COMMIT nbest-reranker
#git clone https://github.com/nusnlp/nbest-reranker/

echo "Downloading Subword NMT from https://github.com/rsennrich/subword-nmt (rev: ec5c7b009c409e72b5ef65a77c1a846546f14847)"
wget https://github.com/rsennrich/subword-nmt/archive/ec5c7b009c409e72b5ef65a77c1a846546f14847.zip
unzip ec5c7b009c409e72b5ef65a77c1a846546f14847.zip
rm ec5c7b009c409e72b5ef65a77c1a846546f14847.zip
mv subword-nmt-ec5c7b009c409e72b5ef65a77c1a846546f14847 subword-nmt
