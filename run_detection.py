import os

def main():
	f = open('list.txt','r')
	vids = [line.strip() for line in f.readlines()]

	for vid in vids:
		command = 'CUDA_VISIBLE_DEVICES=0 python Detectron.pytorch/tools/infer_simple.py --dataset coco --cfg Detectron.pytorch/e2e_mask_rcnn_X-101-64x4d-FPN_1x.yaml --load_detectron weights/maskrcnn_coco_resnext.pkl --image_dir images/%s --output_dir detections/%s.txt ' % (vid,vid)
		os.system(command)
		print('Video %s done' % vid)
	f.close()

if __name__ == '__main__':
	main()
