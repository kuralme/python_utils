
"""
Calculate the Intersection over Union (IoU) between two bounding boxes.
"""

import json
import cv2

def calculate_iou(bbox1, bbox2):
    x1 = max(bbox1[0], bbox2[0])
    y1 = max(bbox1[1], bbox2[1])
    x2 = min(bbox1[0] + bbox1[2], bbox2[0] + bbox2[2])
    y2 = min(bbox1[1] + bbox1[3], bbox2[1] + bbox2[3])
    intersection = max(0, x2 - x1) * max(0, y2 - y1)
    area1 = bbox1[2] * bbox1[3]
    area2 = bbox2[2] * bbox2[3]
    iou = intersection / float(area1 + area2 - intersection)
    return iou

# Load the ground truth annotations from a JSON file
with open('ground_truth_annotations.json', 'r') as f:
    ground_truth = json.load(f)

# Load the tracking results from a JSON file
with open('tracking_results.json', 'r') as f:
    tracking_results = json.load(f)

# Set the IoU threshold for a successful track
iou_threshold = 0.5

# Loop over each frame in the tracking results
for frame_idx, frame_data in tracking_results.items():

    # Load the corresponding image
    image = cv2.imread(frame_data['image_path'])

    # Loop over each tracked object in the frame
    for obj_idx, obj_data in frame_data['objects'].items():

        # Get the tracked bounding box coordinates
        bbox = obj_data['bbox']

        # Loop over each ground truth object in the frame
        for gt_obj in ground_truth[frame_idx]:

            # Get the ground truth bounding box coordinates
            gt_bbox = gt_obj['bbox']

            # Calculate the IoU between the tracked and ground truth bounding boxes
            iou = calculate_iou(bbox, gt_bbox)

            # If the IoU is greater than the threshold, the track is successful
            if iou > iou_threshold:
                print('Frame {}, Object {}: Successful track with IoU {:.2f}'.format(frame_idx, obj_idx, iou))
            else:
                print('Frame {}, Object {}: Failed track with IoU {:.2f}'.format(frame_idx, obj_idx, iou))

