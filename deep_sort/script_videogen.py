import os

splits=['s1', 's2', 's3', 's4']
for split in splits:
	command = 'python generate_videos.py --mot_dir /data/datasets_home/datasets/Honda_Intersection_Dataset/frames/%s --output_dir /data/datasets_home/datasets/Honda_Intersection_Dataset/frames/%s --result_dir /data/datasets_home/datasets/Honda_Intersection_Dataset/frames/%s ' % (split, split, split)
	os.system(command)
