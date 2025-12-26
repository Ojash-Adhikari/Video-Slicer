from frameCalc import should_save_by_frame, should_save_by_time
from store import save_frame
from tqdm import tqdm
import cv2

def slice_video(cap, use_seconds, interval, seconds=None):
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_number = 0

    with tqdm(total=total_frames, desc="Processing video", unit="frame") as pbar:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            if use_seconds:
                if should_save_by_time(frame_number, fps, seconds):
                    save_frame(frame, frame_number)
            else:
                if should_save_by_frame(frame_number, interval):
                    save_frame(frame, frame_number)

            frame_number += 1
            pbar.update(1)

    cap.release()
