# A Multilayer Convolutional Encoder-Decoder Neural Network for Grammatical Error Correction

Repository containing the code and model files for the paper: "A Multilayer Convolutional Encoder-Decoder Neural Network for Grammatical Error Correction" (AAAI-18).

If you use the code, models, or output files from this work please cite the following paper:

@article{chollampatt2018mlconv,
  author    = {Chollampatt, Shamil and Ng, Hwee Tou},
  title     = {A Multilayer Convolutional Encoder-Decoder Neural Network for Grammatical Error Correction},
  booktitle = {Proceedings of the Thirty-Second AAAI Conference on Artificial Intelligence},
  month     = {February},
  year      = {2018},
}


### Setting Up
1. Clone this repository.
2. Download the pre-requisite software:
    * Fairseq-py (http://github.com/facebookresearch/fairseq-py)
    * Subword-NMT (https://github.com/rsennrich/subword-nmt)
    * N-best Reranker (https://github.com/nusnlp/nbest-reranker/)
  For training models, we suggest that you download the exact revisions of the above software. Refer to `software/download.sh` directory to download the exact revisions of these software.


## For testing with pre-trained models
1. Go to `data/` directory and run `prepare_test_data.sh` script to download and process CoNLL-2014 test dataset
2. Go to `models/` directory and run `download.sh` to download the required model files
3. For running the system, run the `run.sh` script with the following format 
`
./run.sh <input-file> <output-directory> <gpu-device-number> <path-to-model-file/path-to-model-dir>
`
You can also run the script by adding optional arguments for re-ranking
`
./run.sh <input-file> <output-directory> <gpu-device-number> <path-to-model-file/path-to-model-dir> <weights-file> <features>
`
where,
 `<wegihts-file>` is the path to trained feature weights for the re-ranker
 `<features>`: use 'eo' for edit operation features, and 'eolm' for both edit operations and language model features. 


### Downloading and Processing Test Data
1. Go to `data/` directory.
2. Run `prepare_test_data.sh` script to download and process CoNLL-2014 test dataset



## For training from scratch

3. Download the 4 Model files
./run.sh data/test/conll14st-test/conll14st-test.tok.src outputs 0 models/mlconv/model1.pt,models/mlconv/model2.pt,models/mlconv/model3.pt,models/mlconv/model4.pt
./run.sh data/test/conll14st-test/conll14st-test.tok.src outputs 0 models/mlconv
