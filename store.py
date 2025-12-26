import cv2
import os

def save_frame(frame, frame_number, output_dir="frames"):
    os.makedirs(output_dir, exist_ok=True)
    filename = f"frame_{frame_number}.jpg"
    path = os.path.join(output_dir, filename)
    cv2.imwrite(path, frame)