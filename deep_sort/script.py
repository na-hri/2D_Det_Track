import os

splits=['s1','s2']
for split in splits:
	command = 'CUDA_VISIBLE_DEVICES=0 python tools/generate_detections.py --mot_dir /data/datasets_home/datasets/Honda_Intersection_Dataset/frames/%s --output_dir output1/' % split
	os.system(command)
