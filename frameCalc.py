def should_save_by_frame(frame_number, interval):
    return frame_number % interval == 0

def should_save_by_time(frame_number, fps, seconds):
    frame_interval = int(fps * seconds)
    return frame_interval > 0 and frame_number % frame_interval == 0
