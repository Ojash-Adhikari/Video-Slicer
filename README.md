# Video Frame Slicer

_Simple tool to slice a video into image frames._

![Frames sample](https://via.placeholder.com/600x120.png?text=Video+Frame+Slicer)

Video Frame Slicer loads a video file, extracts frames, and saves selected frames into the `frames/` directory. You can save frames every N frames or every N seconds. A progress bar shows processing status.

## Features

- Save frames by frame count (every N frames)
- Save frames by time interval (every N seconds — converted to frames using FPS)
- Lightweight: only `opencv-python` and `tqdm` required
- Output saved to the `frames/` folder with readable filenames

## Project Structure

- `main.py` — Entry point, controls the flow
- `videoloader.py` — Loads the video file
- `frameInput.py` — Handles user input
- `frameCalc.py` — Converts seconds↔frames and decision logic
- `slicer.py` — Reads video and extracts frames
- `store.py` — Saves frames to disk
- `frames/` — Output directory for saved frames

## Installation

Requires Python 3.8+.

Install dependencies:

```sh
pip install opencv-python tqdm
```

## Usage

Run the program and follow prompts:

```sh
python main.py
```

Example interaction:

```
Enter path to video file: sample.mp4
Do you want to save frames based on seconds (y/n): y
Save frame every how many seconds? 2
```

Saved frames example:

- `frames/frame_0.jpg`
- `frames/frame_60.jpg`
- `frames/frame_120.jpg`

## How it works

1. User provides a video path.
2. Video is opened with OpenCV; FPS and frame count are read.
3. User chooses frame-based or time-based slicing.
4. The slicer iterates frames and saves matching frames using `store.py`.
5. `tqdm` displays a progress bar during processing.

## Possible Extensions

- Save frames with timestamps instead of frame numbers
- Add a simple GUI (Tkinter or web UI)
- Batch processing for multiple videos
- Export metadata (CSV) with saved frame timestamps

## License

MIT — feel free to learn, modify, and extend.

---

