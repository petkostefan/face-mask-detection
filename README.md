# Real-time face mask detection system

This repo is part of the thesis "Real-time face mask detection system". Focus of the thesis is development of a system that detects face masks in real time using modern methods.

## Abstract
Wearing face masks is one of the key measures to combat infectious diseases transmitted by air. The detection of face masks in real time enables easier implementation of these measures. The goal of the paper is to create a system that automatically detects face masks in real time and displays the detection results. To obtain the best results, four models of the YOLO deep learning algorithm were trained on the aggregated MOXA and FMD datasets. The model with the best performance was selected to be implemented in the system. The system was created in Python programming language, along with PyTorch framework and auxiliary libraries. The result is a detection system that achieves a mean average precision of 73%, at a speed of 47 frames per second on an NVIDIA Tesla T4 graphics card.

## Results
All the results are displayed in the table below.

|Model|Optimizer|Epoch|mAP@.5|Precision|Recall|FPS|
|:----|:----|:----|:----|:----|:----|:----|
|YOLOv3|SGD|5|0.70|0.74|0.68|33|
| | |10|**0.73**|0.76|0.72| |
| | |15|0.69|0.75|0.67| |
| | |20|0.70|0.74|0.70| |
| |ADAM|5|0.61|0.66|0.59| |
| | |10|0.64|0.72|0.60| |
| | |15|0.68|0.77|0.61| |
| | |20|0.71|0.74|0.69| |
|YOLOv5|SGD|5|0.54|0.64|0.50|**47**|
| | |10|0.62|0.72|0.58| |
| | |15|0.67|0.72|0.61| |
| | |20|**0.73**|0.73|0.70| |
| |ADAM|5|0.54|0.64|0.50| |
| | |10|0.62|0.72|0.58| |
| | |15|0.67|0.72|0.61| |
| | |20|0.72|0.73|0.70| |

## Usage
1. Clone the repository:

   ```shell
   git clone https://github.com/petkostefan/face-mask-detection.git
   ```
2. Clone the yolov5 repository:

   ```shell
   cd face-mask-detection
   git clone https://github.com/ultralytics/yolov5.git
   ```

3. Install the required dependencies:

   ```shell
   pip install -r yolov5/requirements.txt
   ```
 
 4. Run the face_mask_detection.py file
    ```shell
    python face_mask_detection.py
    ```
  
