import cv2
from torch import hub  # Hub contains other models like FasterRCNN

camera_ip = "rtsp://username:password@IP/port"
stream = cv2.VideoCapture(camera_ip)

model = torch.hub.load("ultralytics/yolov5", "yolov5s", pretrained=True)
