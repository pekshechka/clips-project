#!/usr/bin/bash

# rus vectors
# https://rusvectores.org/ru/models/

# word to vec
!wget http://vectors.nlpl.eu/repository/20/182.zip
!unzip 182.zip
!mkdir w2v
!mv meta.json model.bin model.txt README w2v


# fast text
!wget http://vectors.nlpl.eu/repository/20/181.zip
!unzip 181.zip
!mkdir ft
!mv meta.json model.model model.model.vectors_ngrams.npy model.model.vectors.npy model.model.vectors_vocab.npy README ft
