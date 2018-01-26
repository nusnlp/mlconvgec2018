echo "Downloading Fairseq from https://github.com/shamilcm/fairseq-py (rev:90c31cd92055124c427689c00624b1eb84c5688a)"
wget https://github.com/shamilcm/fairseq-py/archive/90c31cd92055124c427689c00624b1eb84c5688a.zip 
unzip 90c31cd92055124c427689c00624b1eb84c5688a.zip
rm 90c31cd92055124c427689c00624b1eb84c5688a.zip
mv fairseq-py-90c31cd92055124c427689c00624b1eb84c5688a fairseq-py

echo "Downloading n-best reranker from https://github.com/nusnlp/nbest-reranker (rev: 454c4adc90d0469ef7b2c71ff8cf849ea8cb67f)"
wget https://github.com/nusnlp/nbest-reranker/archive/454c4adc90d0469ef7b2c71ff8cf849ea8cb67f6.zip
unzip 454c4adc90d0469ef7b2c71ff8cf849ea8cb67f6.zip
rm 454c4adc90d0469ef7b2c71ff8cf849ea8cb67f6.zip
mv nbest-reranker-454c4adc90d0469ef7b2c71ff8cf849ea8cb67f6 nbest-reranker
#git clone https://github.com/nusnlp/nbest-reranker/

echo "Downloading Subword NMT from https://github.com/rsennrich/subword-nmt (rev: ec5c7b009c409e72b5ef65a77c1a846546f14847)"
wget https://github.com/rsennrich/subword-nmt/archive/ec5c7b009c409e72b5ef65a77c1a846546f14847.zip
unzip ec5c7b009c409e72b5ef65a77c1a846546f14847.zip
rm ec5c7b009c409e72b5ef65a77c1a846546f14847.zip
mv subword-nmt-ec5c7b009c409e72b5ef65a77c1a846546f14847 subword-nmt
