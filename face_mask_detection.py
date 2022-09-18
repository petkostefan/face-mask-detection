import torch
import numpy as np
import cv2
import time

model = torch.hub.load('yolov5', 'custom', path='weights.pt', source='local', force_reload=True)

cap = cv2.VideoCapture(0)

while cap.isOpened():
    start = time.time()
    ret, frame = cap.read()
    results = model(frame, size=480)

    end = time.time()
    fps = 1/(end-start) 
    fps = str(int(fps)) + ' FPS'

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, fps, (7, 40), font, 1, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.imshow('Face mask detection', np.squeeze(results.render()))

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()