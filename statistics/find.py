import pickle

import numpy as np
import os
from sklearn import preprocessing
from tqdm import tqdm
import json


def process_info(info):
    """
    get features and normalizing features.
    Args:
        info:

    Returns:

    """
    feats = []
    imgnames = []
    for i in range(len(info)):
        feats.append(info[i][0].flatten())
        imgnames.append(info[i][1])
    feats = np.array(feats)
    feats = preprocessing.normalize(feats)
    return feats, imgnames


def main():
    query = "395592518.png"

    gallery_info = pickle.load(open('/home/xiangan/reid_features/gallery.feat', 'rb'))
    query_info = pickle.load(open('/home/xiangan/reid_features/query.feat', 'rb'))
    train_info = pickle.load(open('/home/xiangan/reid_features/train.feat', 'rb'))

    gallery_feats, gallery_imgnames = process_info(gallery_info)
    query_feats, query_imgnames = process_info(query_info)
    train_feats, train_imgnames = process_info(train_info)


    print(train_imgnames.index(query))

if __name__ == '__main__':
    main()