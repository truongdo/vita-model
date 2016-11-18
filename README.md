# Introduction #
This is the model that is used in [Vita](https://github.com/truongdq/vita) application.
The models are trained using [CRFSuite](http://www.chokkan.org/software/crfsuite/).

If you want to download the trained model, please contact us at truongdo[at]vais.vn.
The model is quite large and GitHub does not allow me to upload large files.

2 models are available:

1. PoS (Part of speech tagging): models/word_pos.model
2. Word segmentation: models/word_segment.model

## Data ##

1. The training data for word segmentation comes from http://jvnsegmenter.sourceforge.net/.
2. The training data for PoS comes from https://github.com/lupanh/vTools

## Accuracy ##

1. Word segmentation: ~95% F1 (about the same with the [original paper](http://www.aclweb.org/anthology/Y06-1028))
2. PoS: ~89.72% Accuracy
2. Chunking: 86.20% Accuracy

## Training script ##
The script `./run.sh` shows how I trained the model.
