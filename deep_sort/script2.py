
import os
      
splits=['s1', 's2']
for split in splits:
	vids = os.listdir('/data/datasets_home/datasets/Honda_Intersection_Dataset/frames/%s' % split)
	for vid in vids:
		command='CUDA_VISIBLE_DEVICES=0 python deep_sort_app.py --sequence_dir=/data/datasets_home/datasets/Honda_Intersection_Dataset/frames/%s/%s --detection_file=/data/datasets_home/datasets/Honda_Intersection_Dataset/frames/%s/%s/%s.npy --output_file=/data/datasets_home/datasets/Honda_Intersection_Dataset/frames/%s/%s/%s.txt --min_confidence=0.3 --nn_budget=100 --display=False' % (split, vid, split, vid, vid, split, vid, vid)
		os.system(command)
		print('Split %s Video %s done' % (split, vid))
