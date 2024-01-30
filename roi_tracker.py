#! /usr/bin/env python3
import cv2

tracker_types = ['BOOSTING', 'MIL','KCF', 'TLD', 'MEDIANFLOW', 'GOTURN', 'MOSSE', 'CSRT']
tracker_type = tracker_types[7] # CSRT

if tracker_type == 'BOOSTING':
    tracker = cv2.TrackerBoosting_create()
if tracker_type == 'MIL':
    tracker = cv2.TrackerMIL_create() 
if tracker_type == 'KCF':
    tracker = cv2.TrackerKCF_create() 
if tracker_type == 'TLD':
    tracker = cv2.TrackerTLD_create() 
if tracker_type == 'MEDIANFLOW':
    tracker = cv2.TrackerMedianFlow_create() 
if tracker_type == 'GOTURN':
    tracker = cv2.TrackerGOTURN_create()
if tracker_type == 'MOSSE':
    tracker = cv2.TrackerMOSSE_create()
if tracker_type == "CSRT":
    tracker = cv2.TrackerCSRT_create()

# Get the video file and read it
video = cv2.VideoCapture("input.mp4")
ret, frame = video.read()
if not ret:
    print('cannot read the video')

frame_height, frame_width = frame.shape[:2]
# Resize the video for a more convinient view
frame = cv2.resize(frame, (frame_width//4, frame_height//4))
# Initialize video writer to save the results
output = cv2.VideoWriter((tracker_type+'.avi'), 
                         cv2.VideoWriter_fourcc(*'XVID'), 60.0, 
                         (frame_width//4, frame_height//4), True)

# Select the bounding box in the first frame
bbox = cv2.selectROI(frame, False)
ret = tracker.init(frame, bbox)

frame_cnt = 1.0 # total num of frames
tr_cnt = 0.0 # num of missed frames

# Start tracking
while True:
    ret, frame = video.read()
    frame = cv2.resize(frame, (frame_width//4, frame_height//4))
    if not ret:
        print('something went wrong')
        break

    # Start timer
    timer = cv2.getTickCount()
    frame_cnt += 1.0

    # Update tracker
    ret, bbox = tracker.update(frame)

    # Calculate Frames per second (FPS)
    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)
    
    # Draw bounding box of tracker -----------------------------------------------
    if ret:
        p1 = (int(bbox[0]), int(bbox[1]))
        p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
        cv2.rectangle(frame, p1, p2, (255,0,0), 2, 1)
    else:
        # Tracking failure
        tr_cnt +=1.0
        cv2.putText(frame, "Tracking failure detected", (100,80), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.75,(0,0,255),2)
        
    # Display tracker info on frame
    cv2.putText(frame, tracker_type + " Tracker", (100,20), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2)
    cv2.putText(frame, "FPS : " + str(int(fps)), (100,50), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2)
    cv2.putText(frame, "SR : " + str(100*(frame_cnt-tr_cnt)/frame_cnt), (100,70),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (50,170,50), 2)
    
    cv2.imshow("Tracking", frame)
    output.write(frame)
    k = cv2.waitKey(1) & 0xff
    if k == 27 : break

video.release()
output.release()
cv2.destroyAllWindows()
