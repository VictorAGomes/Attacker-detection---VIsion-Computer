# Intruder Detection - Computer Vision Project

This is a computer vision project developed in Python to detect intruders in a video using a YOLO (You Only Look Once) object detection model. When an intruder is detected within a predefined area, a sound alarm is activated.

## Dependencies

To run this project, make sure you have the following libraries installed:

- OpenCV (`cv2`)
- Ultralytics (`ultralytics`)
- Pygame (`pygame`)

You can install the dependencies using the following pip command:

```
pip install opencv-python ultralytics pygame
```

## Instructions

1. Download the video you want to analyze and save it in the same folder as this script.
2. Run the Python script `main.py`.
3. The program will start analyzing the video, detecting intruders within the defined area.
4. When an intruder is detected, a sound alarm will be activated.

To terminate the program, press the `q` key while the video window is in focus.

## Notes

- Make sure you have the necessary files for the sound alarm in the same folder as this script.
- The intruder detection area can be adjusted by modifying the values in the `area` list.
- The input video file is specified in the line `video = cv2.VideoCapture('ex01.mp4')`. Replace `'ex01.mp4'` with the path to your video file.

This project was developed as part of a study in computer vision. If you have any questions or need further assistance, feel free to ask.
