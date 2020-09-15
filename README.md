# 2D_Det_Track
## Introduction
This a PyTorch and Tensorflow repository for 2D detection and tracking.
## Environment
Install the respective environments for detection and tracking.
## Setup and Data Preparation
- Download network [weights](https://drive.google.com/drive/folders/1i7ZAcCthN12l9Fk64kChkboq0BKKn9Rz?usp=sharing) and put them under `weights/`. 
- Extract images from videos and put them under ``images/``, and provide the list of videos in `list.txt`. Make sure to have the following directory structure:

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
