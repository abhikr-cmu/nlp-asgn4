# CMU 11-711 Advanced Natural Language Processing Project

#### Team Members : Abhishek Kumar, Deep Karkhanis, Nilay Pande

We have worked on Automatic Code Generation for Python Language. We picked the SOTA **Code generation from natural language with less prior and more monolingual data (TAE)** as the base model and were able to improve its BLEU score by **0.9**

Following are important folders in the repo :
* `screenshots/` folder contain the screenshot of test accuracy we obtained on the CoNaLa dataset for various methods
* `generated_test_outputs/` contain the output of the models on the CoNaLa test
* `our_models/` folder contain our models


Following are our results on CoNaLa dataset and Corpus BLEU

| Method  | Results      | 
| ------- | ------------ |
| Baseline SOTA | 33.41  |
| SOTA + Python Standard Lib + Numpy + Pandas + Torch| 32.09        | 
| SOTA + Python Standard Lib + Numpy + Pandas + Torch + Resample  | 33.3        | 
| **SOTA + Python Standard Lib + Numpy + Pandas + Torch + Resample + Prob Prune + Len Constrain**  | **34.31**        | 
| SOTA + Python Standard Lib + Numpy + Pandas + Torch + Resample + Prob Prune + Len Constrain + Libname  | 32.76        | 


Our best results are with SOTA model bootstrapped with Python standard library, Numpy, Pandas, and PyTorch library. During Sampling we do a probability pruning to stop some examples from getting unfair advantage over others. Moreover, we place a contraint of number of characters (120) in the intent.




# Original Paper
## Code generation from natural language with less prior and more monolingual data (TAE)

Paper published in [ACL 2021](https://aclanthology.org/2021.acl-short.98/)


install the requirments:
```
pip install -r requirements.txt
```

To train model on Django
```
python3 train.py --dataset_name django --save_dir CHECKPOINT_DIR --copy_bt --no_encoder_update --monolingual_ratio 1.0 --early_stopping
``` 
To evaluate the provided Django checkpoint:
```
python3 train.py --dataset_name django --save_dir pretrained_weights/django --copy_bt --no_encoder_update --monolingual_ratio 1.0 --early_stopping --just_evaluate --seed 2
``` 
To train model on CoNaLa
```
python3 train.py --dataset_name conala --save_dir CHECKPOINT_DIR --copy_bt --no_encoder_update --monolingual_ratio 0.5 --epochs 80
``` 
To evaluate the provided CoNaLa chceckpoint:
```
python3 train.py --dataset_name conala --save_dir pretrained_weights/conala --copy_bt --no_encoder_update --monolingual_ratio 0.5 --epochs 80 --just_evaluate --seed 4
```

### Evaluation Results
Here are the evaluation numbers for the provided checkpoints:

| Dataset | Results      | Metric             |
| ------- | ------------ | ------------------ |
| Django  | 81.77        | Exact Match Acc.   |
| CoNaLa  | 33.41        | Corpus BLEU        |
