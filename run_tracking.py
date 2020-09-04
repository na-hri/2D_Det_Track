import os

def main():
	f = open('list.txt','r')
	vids = [line.strip() for line in f.readlines()]

	command = 'CUDA_VISIBLE_DEVICES=0 python deep_sort/tools/generate_detections.py --mot_dir images/ --detection_dir detections --output_dir tracking'
	os.system(command)

	for vid in vids:
		command='CUDA_VISIBLE_DEVICES=0 python deep_sort/deep_sort_app.py --sequence_dir=images/%s --detection_file=tracking/%s.npy --output_file=tracking/%s.txt --min_confidence=0.3 --nn_budget=100 --display=True' % (vid, vid, vid)
		os.system(command)
		print('Video %s done' % vid)


if __name__ == '__main__':
	main()
