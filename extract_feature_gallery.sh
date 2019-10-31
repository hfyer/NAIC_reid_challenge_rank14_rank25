python tools/extract_feature_gallery.py \
  --config_file='configs/softmax_triplet_with_center.yml' \
  MODEL.DEVICE_ID "('1')" \
  DATASETS.NAMES "('dukemtmc')" \
  DATASETS.ROOT_DIR "('../train_split/split2')" \
  MODEL.PRETRAIN_CHOICE "('self')" \
  MODEL.PRETRAIN_PATH "('exps/Experiment1/se_resnet101_model_120.pth')" \
  OUTPUT_DIR "('./exps/test')"
