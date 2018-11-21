# A Multilayer Convolutional Encoder-Decoder Neural Network for Grammatical Error Correction

Code and model files for the [paper](https://www.aaai.org/ocs/index.php/AAAI/AAAI18/paper/viewFile/17308/16137): "A Multilayer Convolutional Encoder-Decoder Neural Network for Grammatical Error Correction" (In AAAI-18). If you use any part of this work, make sure you include the following citation:

```
@InProceedings{chollampatt2018mlconv,
  author    = {Chollampatt, Shamil and Ng, Hwee Tou},
  title     = {A Multilayer Convolutional Encoder-Decoder Neural Network for Grammatical Error Correction},
  booktitle = {Proceedings of the Thirty-Second AAAI Conference on Artificial Intelligence},
  month     = {February},
  year      = {2018},
}
```

## Setting Up
1. Clone this repository.
2. Download the pre-requisite software:
    * [Fairseq-py](http://github.com/facebookresearch/fairseq-py)
    * [Subword-NMT](https://github.com/rsennrich/subword-nmt)
    * [N-best Reranker](https://github.com/nusnlp/nbest-reranker/) (Requires [KenLM](https://github.com/kpu/kenlm) Python module)

      **NOTE**: For training and evaluation of the models, we suggest that you download the exact revisions of the above software. Go to `software/` directory and run `download.sh` directory to download the exact revisions of these software.
3. Compile and install Fairseq-py.


## For testing with pre-trained models
1. Go to `data/` directory and run `prepare_test_data.sh` script to download and process CoNLL-2014 test dataset
2. Go to `models/` directory and run `download.sh` to download the required model files
3. For running the system, run the `run.sh` script with the following format
```
./run.sh <input-file> <output-directory> <gpu-device-number> <models-path>
````
`<input-file>`: path to tokenized input data
`<gpu-device-number>`: typically 0,1,2 etc to be used with the environment variable `CUDA_VISIBLE_DEVICES`
`<models-path>`: could be the path to a single model file or a directory having multiple model files alone.

You can also run the script by adding optional arguments for re-ranking
```
./run.sh <input-file> <output-directory> <gpu-device-number> <models-path> <weights-file> <features>
````
 `<weights-file>`: path to trained feature weights for the re-ranker (within `models/reranker_weights`
 `<features>`: use 'eo' for edit operation features, and 'eolm' for both edit operations and language model features.



## For training from scratch

### Data Preparation
1. Update the paths to `NUCLE_TAR` and `LANG8V2` within `prepare_data.sh`
2. Run the script `prepare_data.sh` from within `data/` directory.
   (**NOTE**: To get the exact data you may need to use LangID.py v1.1.6 for language filtering and NLTK v2.0b7 for tokenization. The prepared training data (`data/train.tok.{src,trg}`) will have 2210277 sentence pairs with 26,557,233 source tokens and 30,028,798 target tokens).

### Training
For training, download the version of Fairseq-py 
In the `training/` directory, within the `preprocess.sh` script, place paths to the the training datasets and development datasets. The source and target files must be tokenized.
1. Go to `training/` directory
2. Run `./preprocess.sh` script
3.   
    - To train the models without pre-trainined embeddings use the `train.sh` script.
    - To train the models with pre-trained word embeddings use the `train_embed.sh` script. (**NOTE**: The pre-trained embeddings are trained using Wikipedia data segmented using the released BPE model. If your training data and BPE model are different, we suggest that you pre-train [fastText](https://github.com/facebookresearch/fastText) embeddings on Wikipedia text segmented with your own BPE model and modify the paths within the script accordingly.)
4. To train the re-ranker, you would additionally need to have compiled [Moses](https://github.com/moses-smt/mosesdecoder) software. Run `train_reranker.sh` script with the following arguments:
      ```
      ./train_reranker.sh <output_dir> <gpu-device-number> <models-path> <path-to-moses>
      ```
      `<output-dir>`: directory to store temporary files and final output `weights.txt` file.
5. Run the trained model from within `training/` directory using the script `run_trained_model.py`.

## License
The code and models in this repository are licensed under the GNU General Public License Version 3.
For commercial use of this code and models, separate commercial licensing is also available. Please contact:

* Shamil Chollampatt (shamil@u.nus.edu)
* Hwee Tou Ng (nght@comp.nus.edu.sg)





