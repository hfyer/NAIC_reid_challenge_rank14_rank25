# Experiment-Four-Fold

### Experiment baseline
```yml
INPUT:
  PIXEL_MEAN: [0.485, 0.456, 0.406]
  PIXEL_STD: [0.229, -0.224, -0.225]
SOLVER:
  OPTIMIZER_NAME: 'SGD'
  MAX_EPOCHS: 80
  BASE_LR: 0.005
  CENTER_LR: 0.5
  CENTER_LOSS_WEIGHT: 0.0005
  MARGIN: 1.0
  STEPS: [50, 70]
```
| experiment | split1(mAP/Rank-1) |   split2  |   split3  |   split4  | avg |
|:----------:|:------------------:|:---------:|:---------:|:---------:|:---:|
|  baseline  |      83.6/93.8     | 82.2/92.3 | 80.9/91.8 | 84.2/93.7 |  -  |

### Experiment 001
```yml
INPUT:
  PIXEL_STD: [0.229, 0.224, 0.225]
```  
| experiment | split1(mAP/Rank-1) |   split2  |   split3  |   split4  |     avg     | result |
|:----------:|:------------------:|:---------:|:---------:|:---------:|:-----------:|:------:|
|  baseline  |      83.6/93.8     | 82.2/92.3 | 80.9/91.8 | 84.2/93.7 | 82.73/92.90 |    -   |
|     001    |      82.5/92.8     | 81.3/93.0 | 80.8/92.2 | 83.6/93.9 | 82.05/92.97 |    -   |


### Experiment Margin
```yml
INPUT:
  PIXEL_MEAN: [0.485, 0.456, 0.406]
  PIXEL_STD: [0.229, -0.224, -0.225]
SOLVER:
  OPTIMIZER_NAME: 'SGD'
  MAX_EPOCHS: 80
  BASE_LR: 0.005
  CENTER_LR: 0.5
  CENTER_LOSS_WEIGHT: 0.0005
  MARGIN: ???
  STEPS: [50, 70]
```
|       experiment      | split1(mAP/Rank-1) |   split2  |   split3  |   split4  |     avg     | result |
|:---------------------:|:------------------:|:---------:|:---------:|:---------:|:-----------:|:------:|
|  (margin=1.0)baseline |      83.6/93.8     | 82.2/92.3 | 80.9/91.8 | 84.2/93.7 | 82.73/92.90 |    -   |
| (margin=1.5)margin001 |      83.6/94.1     | 82.4/92.3 | 81.1/91.5 | 85.0/94.8 | 83.03/93.18 | better |
| (margin=2.0)margin002 |      84.2/93.7     | 82.3/92.2 | 82.1/92.1 | 85.1/94.8 | 83.42/93.20 | better |
| (margin=3.0)margin003 |      84.4/94.1     | 82.5/92.6 | 81.7/92.0 | 84.8/93.6 | 83.35/93.01 | better |
| (margin=5.0)margin004 |      85.0/94.1     | 82.8/92.7 | 82.6/92.7 | 85.6/93.9 | 84.00/93.35 | better |
|  (margin=10)margin005 |      85.2/94.3     | 83.1/92.7 | 83.1/93.0 | 86.4/94.8 | 84.45/93.70 | better |



### Experiment Center loss weight  
```yml
INPUT:
  PIXEL_MEAN: [0.485, 0.456, 0.406]
  PIXEL_STD: [0.229, -0.224, -0.225]
SOLVER:
  OPTIMIZER_NAME: 'SGD'
  MAX_EPOCHS: 80
  BASE_LR: 0.005
  CENTER_LR: 0.5
  CENTER_LOSS_WEIGHT: ???
  MARGIN: 1.0
  STEPS: [50, 70]
```

|     experiment    | split1(mAP/Rank-1) |   split2  |   split3  |   split4  |     avg     |   result  |
|:-----------------:|:------------------:|:---------:|:---------:|:---------:|:-----------:|:---------:|
|   (cw=1e-4)cw001  |      84.4/94.7     | 82.3/93.1 | 81.8/92.8 | 84.5/93.9 | 83.25/93.63 |   better  |
|   (cw=2e-4)cw002  |      84.0/93.7     | 82.5/93.5 | 80.8/92.0 | 84.8/94.8 | 83.03/93.50 |   better  |
|   (cw=3e-4)cw003  |      84.2/94.3     | 82.0/92.3 | 81.1/92.1 | 84.7/94.0 | 83.00/93.18 |   better  |
|   (cw=4e-4)cw004  |      83.7/93.7     | 82.0/91.9 | 81.4/92.5 | 85.2/94.5 | 83.08/93.15 |   better  |
| (cw=5e-4)baseline |      83.6/93.8     | 82.2/92.3 | 80.9/91.8 | 84.2/93.7 | 82.73/92.90 |     -     |
|   (cw=5e-4)cw005  |      83.6/93.1     | 81.3/91.1 | 80.8/91.4 | 84.5/94.3 | 82.55/92.48 |   worse   |
|   (cw=6e-4)cw006  |      83.8/93.4     | 81.7/92.2 | 80.8/90.9 | 84.9/94.6 | 82.80/92.78 |   worse   |
|   (cw=7e-4)cw007  |      83.3/93.2     | 81.7/92.3 | 80.7/91.2 | 84.1/93.4 | 82.45/92.53 |           |
|   (cw=8e-4)cw008  |      83.2/93.4     | 81.5/91.7 | 80.4/91.2 | 83.9/94.2 | 82.25/92.63 |           |
|   (cw=9e-4)cw009  |      83.4/92.8     | 81.4/92.3 | 80.2/90.9 | 84.5/94.0 | 82.38/92.50 |           |
|   (cw=1e-3)cw010  |      83.4/93.1     | 81.2/91.6 | 80.7/91.7 | 84.5/94.8 | 82.45/92.80 |           |
|  (cw=9e-5)mcw001  |      85.4/94.4     | 83.3/93.4 | 83.1/93.4 | 85.9/94.8 | 84.43/94.00 | MARGIN=10 |
|  (cw=8e-5)mcw002  |      84.8/93.5     | 83.5/92.7 | 83.7/92.8 | 86.2/96.0 | 84.55/93.75 |           |
|  (cw=7e-5)mcw003  |      85.1/94.5     | 82.9/92.8 | 82.9/93.4 | 85.5/94.3 | 84.10/93.75 |           |
|  (cw=6e-5)mcw004  |      85.3/94.7     | 83.5/93.0 | 83.2/92.8 | 85.3/94.3 | 84.33/93.70 |           |
|  (cw=5e-5)mcw005  |      85.2/94.4     | 83.4/93.0 | 83.0/93.7 | 86.3/95.3 | 84.48/94.10 |           |
|  (cw=4e-5)mcw006  |      85.4/94.7     | 83.1/93.1 | 83.0/93.4 | 85.2/94.2 | 84.18/93.85 |           |
|  (cw=3e-5)mcw007  |      85.1/94.1     | 83.8/93.5 | 82.8/92.5 | 85.4/94.2 | 84.28/93.58 |           |
|  (cw=2e-5)mcw008  |      85.0/94.1     | 82.9/92.4 | 83.2/93.4 | 85.7/94.8 | 84.20/93.68 |           |









### Learning rate  
```yml
INPUT:
  PIXEL_MEAN: [0.485, 0.456, 0.406]
  PIXEL_STD: [0.229, -0.224, -0.225]
SOLVER:
  OPTIMIZER_NAME: 'SGD'
  MAX_EPOCHS: 80
  BASE_LR: ???
  CENTER_LR: 0.5
  CENTER_LOSS_WEIGHT: 5e-4
  MARGIN: 1.0
  STEPS: [50, 70]
```

|     experiment    | split1(mAP/Rank-1) |   split2  |   split3  |   split4  |     avg     | result |
|:-----------------:|:------------------:|:---------:|:---------:|:---------:|:-----------:|:------:|
|   (lr=1e-3)lr001  |      82.4/92.7     | 79.7/90.8 | 78.9/90.7 | 83.0/93.4 | 81.05/91.90 |  worse |
|   (lr=2e-3)lr002  |      83.0/93.5     | 80.9/91.5 | 80.0/91.7 | 84.0/93.9 | 81.98/92.65 |  worse |
|   (lr=3e-3)lr003  |      83.6/94.0     | 81.5/92.6 | 80.7/91.2 | 84.3/94.0 | 82.53/92.95 |  worse |
|   (lr=4e-3)lr004  |      84.1/94.2     | 81.9/91.5 | 80.5/90.7 | 84.5/94.5 | 82.75/92.73 |  worse |
| (lr=5e-3)baseline |      83.6/93.8     | 82.2/92.3 | 80.9/91.8 | 84.2/93.7 | 82.73/92.90 |    -   |
|   (lr=6e-3)lr005  |      84.1/94.0     | 81.7/92.4 | 81.2/92.0 | 85.4/94.5 | 83.10/93.23 | better |
|   (lr=7e-3)lr006  |      84.3/93.8     | 82.3/92.6 | 81.9/92.4 | 85.4/94.9 | 83.48/93.43 | better |
|   (lr=8e-3)lr007  |      84.5/93.8     | 83.0/93.5 | 81.3/92.7 | 84.8/94.3 | 83.40/93.58 | better |
|   (lr=9e-3)lr008  |      84.4/94.1     | 81.9/91.9 | 81.1/91.7 | 85.2/94.8 | 83.15/93.13 | better |
|   (lr=1e-2)lr009  |      84.0/93.8     | 82.3/92.3 | 81.4/92.1 | 84.9/94.6 | 83.15/93.20 | better |




### RandomPatch Prob  
```yml
INPUT:
  PIXEL_MEAN: [0.485, 0.456, 0.406]
  PIXEL_STD: [0.229, -0.224, -0.225]
  RANDOM_PATCH_PROB: ???
SOLVER:
  OPTIMIZER_NAME: 'SGD'
  MAX_EPOCHS: 80
  BASE_LR: 5e-3
  CENTER_LR: 0.5
  CENTER_LOSS_WEIGHT: 5e-4
  MARGIN: 1.0
  STEPS: [50, 70]
```
|      experiment     | split1(mAP/Rank-1) |   split2  |   split3  |   split4  |     avg     | result |
|:-------------------:|:------------------:|:---------:|:---------:|:---------:|:-----------:|:------:|
| (prob=0.10)patch001 |      82.9/93.4     | 81.5/92.6 | 80.3/91.4 | 82.7/92.6 | 81.85/92.50 |  worse |
| (prob=0.15)patch002 |      83.2/92.8     | 81.4/91.6 | 81.2/92.5 | 83.8/93.6 | 82.40/92.63 |  worse |
| (prob=0.20)patch003 |      83.5/93.8     | 81.9/91.6 | 80.8/91.5 | 84.3/94.3 | 82.63/92.80 |  worse |
| (prob=0.25)patch004 |      83.8/93.5     | 81.4/92.3 | 81.6/92.5 | 84.6/94.2 | 82.85/93.13 | better |
| (prob=0.30)baseline |      83.6/93.8     | 82.2/92.3 | 80.9/91.8 | 84.2/93.7 | 82.73/92.90 |    -   |
| (prob=0.35)patch005 |      84.1/94.7     | 81.9/92.2 | 81.5/92.8 | 85.1/94.5 | 83.15/93.55 | better |
| (prob=0.40)patch006 |      83.7/93.4     | 82.2/93.0 | 81.4/91.8 | 84.9/94.6 | 83.05/93.20 | better |
| (prob=0.45)patch007 |      83.4/92.5     | 81.6/91.2 | 81.4/92.0 | 85.5/94.8 | 82.98/92.63 |   ???  |
| (prob=0.50)patch008 |      84.4/94.5     | 82.4/93.0 | 81.6/92.4 | 85.1/94.6 | 83.45/93.63 | better |


### RandomPatch Area
```yml
INPUT:
  PIXEL_MEAN: [0.485, 0.456, 0.406]
  PIXEL_STD: [0.229, -0.224, -0.225]
  RANDOM_PATCH_PROB: ???
SOLVER:
  OPTIMIZER_NAME: 'SGD'
  MAX_EPOCHS: 80
  BASE_LR: 5e-3
  CENTER_LR: 0.5
  CENTER_LOSS_WEIGHT: 1e-4
  MARGIN: 10.0
  STEPS: [50, 70]
```
|    experiment    | split1(mAP/Rank-1) |   split2  |   split3  |   split4  |     avg     | result |
|:----------------:|:------------------:|:---------:|:---------:|:---------:|:-----------:|:------:|
| (area=0.10)pa001 |      84.6/94.5     | 83.1/92.6 | 82.8/92.2 | 84.7/93.9 | 83.80/93.30 |        |
| (area=0.15)pa002 |      85.3/94.4     | 82.9/91.9 | 83.2/93.2 | 85.7/94.6 | 84.28/93.53 |        |
| (area=0.20)pa003 |      84.7/94.1     | 83.3/92.7 | 83.5/93.5 | 85.6/94.2 | 84.28/93.63 |        |
| (area=0.25)pa004 |      85.1/94.4     | 82.8/92.0 | 83.2/93.2 | 86.4/95.3 | 84.38/93.73 |        |
| (area=0.30)pa005 |      85.1/93.1     | 82.8/92.3 | 83.0/93.1 | 86.0/94.6 | 84.23/93.28 |        |
| (area=0.35)pa006 |      85.2/94.3     | 83.1/92.4 | 82.7/92.7 | 86.3/94.8 | 84.33/93.55 |        |
| (area=0.40)pa007 |      84.6/93.2     | 82.2/91.6 | 82.1/92.0 | 85.8/94.8 | 83.68/92.90 |        |
| (area=0.45)pa008 |      84.3/94.0     | 81.4/92.2 | 81.9/92.4 | 85.3/94.6 | 83.23/93.30 |        |
| (area=0.50)pa009 |                    |           | 81.4/91.8 |           |      -      |        |



### CenterLossLR
```yml
INPUT:
  PIXEL_MEAN: [0.485, 0.456, 0.406]
  PIXEL_STD: [0.229, -0.224, -0.225]
  RANDOM_PATCH_PROB: 0.3
SOLVER:
  OPTIMIZER_NAME: 'SGD'
  MAX_EPOCHS: 80
  BASE_LR: 5e-3
  CENTER_LR: ????
  CENTER_LOSS_WEIGHT: 1e-4
  MARGIN: 10.0
  STEPS: [50, 70]
```

|   experiment  | split1(mAP/Rank-1) |   split2  |   split3  |   split4  |     avg     | result |
|:-------------:|:------------------:|:---------:|:---------:|:---------:|:-----------:|:------:|
| (lr=0.1)cl001 |      85.6/94.3     | 83.7/93.3 | 83.1/93.8 | 85.8/94.3 | 84.55/93.93 |        |
| (lr=0.2)cl002 |      84.6/94.0     | 83.4/92.8 | 83.1/93.1 | 85.7/94.3 | 84.20/93.55 |        |
| (lr=0.3)cl003 |      85.0/94.3     | 82.7/92.4 | 83.1/93.1 | 86.2/95.7 | 84.25/93.88 |        |
| (lr=0.4)cl004 |      85.7/95.1     | 83.3/93.1 | 83.3/93.5 | 85.0/94.2 | 84.33/93.98 |        |
| (lr=0.5)cl005 |      85.6/95.3     | 83.2/92.6 | 83.2/93.4 | 85.7/94.5 | 84.43/93.95 |        |
| (lr=0.6)cl006 |      85.1/94.5     | 83.3/93.1 | 83.0/94.0 | 86.2/95.1 | 84.40/94.18 |        |
| (lr=0.7)cl007 |      85.1/94.5     | 82.7/92.7 | 83.6/93.7 | 85.9/94.3 | 84.33/93.80 |        |
| (lr=0.8)cl008 |      85.2/93.8     | 83.1/93.0 | 83.4/93.2 | 86.3/94.6 | 84.50/93.65 |        |
| (lr=0.9)cl009 |                    |           | 82.8/92.8 |           |             |        |





