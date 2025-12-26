from videoloader import load_video
from frameInput import (
    get_yes_no,
    get_frame_interval,
    get_second_interval,
)
from slicer import slice_video

def main():
    video_path = input("Enter path to video file: ")
    cap = load_video(video_path)

    use_seconds = get_yes_no("Do you want to save frames based on seconds")

    if use_seconds:
        seconds = get_second_interval()
        slice_video(cap, use_seconds=True, interval=None, seconds=seconds)
    else:
        interval = get_frame_interval()
        slice_video(cap, use_seconds=False, interval=interval)

    print("Frames saved successfully!")

if __name__ == "__main__":
    main()
