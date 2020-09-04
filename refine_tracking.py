import numpy as np
import cv2
import os.path as osp
import os

DATA_ROOT = './'
TRACKING_PATH = osp.join(DATA_ROOT, 'tracking')
DETECTION_PATH = osp.join(DATA_ROOT, 'detections')
REFINED_PATH = osp.join(DATA_ROOT, 'tracking_refined')

img_height = 1200
img_width = 1920

with open('list.txt') as f:
  SESSIONS = [line.strip() for line in f.readlines()]

def max_IoU(ref_box, box_list):

  ov_x1 = np.maximum(ref_box[0], box_list[:, 0])
  ov_y1 = np.maximum(ref_box[1], box_list[:, 1])
  ov_x2 = np.minimum(ref_box[0]+ref_box[2], box_list[:, 0]+box_list[:, 2])
  ov_y2 = np.minimum(ref_box[1]+ref_box[3], box_list[:, 1]+box_list[:, 3])

  ov_w = np.clip((ov_x2-ov_x1), 0, float('inf'))
  ov_h = np.clip((ov_y2-ov_y1), 0, float('inf'))
  ov_area = np.multiply(ov_w , ov_h)


  union_x1 = np.maximum(0, np.minimum(ref_box[0], box_list[:, 0]))
  union_y1 = np.maximum(0, np.minimum(ref_box[1], box_list[:, 1]))
  union_x2 = np.minimum(np.maximum(ref_box[0]+ref_box[2], box_list[:, 0]+box_list[:, 2]), img_width)
  union_y2 = np.minimum(np.maximum(ref_box[1]+ref_box[3], box_list[:, 1]+box_list[:, 3]), img_height)

  union_w = np.clip((union_x2-union_x1), 0, float('inf'))
  union_h = np.clip((union_y2-union_y1), 0, float('inf'))
  union_area = np.multiply(union_w , union_h)

  IoU = np.divide(ov_area, union_area)
  #print(IoU)
  selected_idx = np.argmax(IoU)
  selected_idx_iou = np.amax(IoU)

  return box_list[selected_idx], selected_idx_iou, selected_idx
  '''
  print('ov_area:\n', ov_area)
  print('ov_w:\n', ov_x2-ov_x1)
  print('ov_w:\n', ov_w)
  print('ov_h:\n', ov_y2-ov_y1)
  print('ov_h:\n', ov_h)
  print('union_area:\n', union_area)
  print('union_w:\n', union_x2-union_x1)
  print('union_w:\n', union_w)
  print('union_h:\n', union_y2-union_y1)
  print('union_h:\n', union_h)
  '''
  #print('IoU',   IoU)




for sess, session in enumerate(SESSIONS):
  print('Processing ',session, ' ',  sess, '/', len(SESSIONS))
  tracking_txt_path = osp.join(TRACKING_PATH,'%s.txt' % session)

  tracking_results = np.loadtxt(tracking_txt_path, delimiter=',')

  detection_txt_path = osp.join(DETECTION_PATH,'%s.txt' % session)

  detection_results = np.loadtxt(detection_txt_path, delimiter=',')

  results = []
  for i , tracker  in enumerate(tracking_results):
     fid = tracker[0]
     box = tracker[2:6]

     detection_index = np.where(detection_results[:,0] == fid)[0]
     detection_box = detection_results[detection_index, 2:6] #Nx4
     #print(fid, detection_box)

     if len(detection_index) != 0:
        refined_box, max_iou, selected_idx = max_IoU(box, detection_box)
        if max_iou < 0.5:
          continue
        tracker[2:6] = refined_box
     results.append(tracker)
     #break

  output_file = osp.join(REFINED_PATH, '%s.txt' % session)
  f = open(output_file, 'w')
  for row in results:
    print('%d,%d,%.2f,%.2f,%.2f,%.2f,1,-1,-1,-1' % (row[0], row[1], row[2], row[3], row[4], row[5]),file=f)
