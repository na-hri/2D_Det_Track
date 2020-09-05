# 2D_Det_Track
## Introduction
This a PyTorch and Tensorflow respository for 2D detection and tracking.
## Environment
Install the respective environments for detection and tracking.
## Data Preparation
Extract images from videos and put them under ``images/`` and make sure to have the following structure:

```
images
|--201810221516_0_128
   |--*.jpg
|--201807161357_12215_12401
   |--*.jpg
```   
## Usage
### Run 2D detection
```
python run_detection.py
```
### Run 2D tracking
```
python run_tracking.py
```
### Refine tracking results
```
python refine_tracking.py
```
