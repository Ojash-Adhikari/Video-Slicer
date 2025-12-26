Video Frame Slicer (Python)
🎞️ A simple, modular Python tool to extract frames from a video
📌 Project Philosophy
Simple projects are not built from big complicated ideas — they are built from small, focused tasks.
This project started with one very small requirement:
“I need a simple way to slice a video into frames.”
Instead of writing everything in a single file, the project was intentionally broken down into minimal, independent tasks. Each task solves exactly one problem, and together they form a complete solution.
This approach:

Makes the code easier to understand
Keeps files small and readable
Allows features to be added without rewriting everything
Scales naturally as requirements grow

🎯 What This Project Does
This Python program:

Loads a video file
Slices the video into individual frames
Saves frames into a frames/ directory
Allows the user to choose how frames are saved:
📸 Every N frames
⏱ Every N seconds

Displays a progress bar while processing

🧩 Project Structure
textproject/
├── main.py          # Entry point, controls the flow
├── videoloader.py   # Loads the video file
├── frameInput.py    # Handles all user input
├── frameCalc.py     # Frame/time-based decision logic
├── slicer.py        # Reads video and extracts frames
├── store.py         # Saves frames to disk
└── frames/          # Output directory for saved frames (created automatically)
Each file is responsible for one small task only.
🔄 How the Project Works

User provides a video path
Video is loaded using OpenCV
User is asked:
Whether they want to save frames based on seconds (y/n)
The interval (seconds or frame count)

Based on the choice:
Frame-based slicing uses a fixed frame interval
Time-based slicing converts seconds → frames using the video's FPS

Video frames are read one by one
Selected frames are saved into the frames/ folder
A progress bar shows real-time processing status

📦 Requirements
Python Version

Python 3.8 or higher

Python Libraries
Install the required packages with:
Bashpip install opencv-python tqdm





















PackagePurposeopencv-pythonVideo loading and frame extractiontqdmProgress bar for frame processingosFile system handling (built-in)
▶️ How to Run
Bashpython main.py
Example Interaction
textEnter path to video file: sample.mp4
Do you want to save frames based on seconds (y/n): y
Save frame every how many seconds? 2
Frames will be saved as:
frames/frame_0.jpg, frames/frame_60.jpg, frames/frame_120.jpg, ...
🧠 Why This Design Matters

🔹 Each file does one thing well (Single Responsibility Principle)
🔹 Easy to test and debug
🔹 New features can be added without breaking existing logic
🔹 Demonstrates real-world software engineering practices

This project intentionally stays simple, but not simplistic.
🚀 Possible Extensions

Save frames using timestamps instead of frame numbers
Add a GUI version using Tkinter
Resume slicing from the last saved frame
Export metadata (e.g., timestamp, frame number) to CSV
Batch process multiple videos

📄 License
This project is open for learning, experimentation, and extension. Feel free to fork, modify, and share!
(No specific license is applied — public domain / free to use.)