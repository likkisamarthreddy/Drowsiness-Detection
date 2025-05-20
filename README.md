🚨 Drowsiness Detection System
Real-time drowsiness detection in action
📖 Project Overview
The Drowsiness Detection System is a cutting-edge computer vision application designed to enhance safety by monitoring a user's eye activity in real-time. Using a webcam, it calculates the Eye Aspect Ratio (EAR) to detect prolonged eye closure, a key indicator of drowsiness. When drowsiness is detected, an alarm sound (alarm.wav) plays to alert the user, making this ideal for applications like driver safety monitoring or workplace alertness tracking. Built with MediaPipe for facial landmark detection, OpenCV for video processing, and playsound for audio alerts, this project combines advanced technology with practical utility.
✨ Key Features

Real-time Monitoring: Tracks eye landmarks to compute the EAR, detecting drowsiness with high accuracy.
Alarm System: Plays an audio alert (alarm.wav) when eyes remain closed for a set period.
Visual Feedback: Displays the EAR value and a bold "DROWSINESS DETECTED!" message on the video feed.
Thread Safety: Uses a threading lock to ensure safe audio playback in a multi-threaded environment.
Error Handling: Manages camera and audio errors gracefully for reliable operation.
Potential Applications: Perfect for driver fatigue detection, workplace safety, or educational focus monitoring.

🛠️ Prerequisites
Before running the project, ensure the following are set up:

Python 3.8+: Download from python.org.
Dependencies:
opencv-python: For video capture and processing.
mediapipe: For facial landmark detection.
numpy: For numerical computations.
playsound: For audio playback (Note: May have compatibility issues on some Windows systems; pygame is a recommended alternative).


Hardware:
A webcam (default camera, index 0).
A valid WAV file named alarm.wav in the project directory (e.g., C:\Users\user\Desktop\Project).



📦 Installation
Follow these steps to set up the project:

Verify Python Installation:Ensure Python 3.8 or higher is installed:
python --version


Install Dependencies:Install required libraries using pip:
pip install opencv-python mediapipe numpy playsound


Prepare Alarm File:Place a valid WAV file named alarm.wav in the project directory. Ensure the file is accessible and not corrupted. Update ALARM_PATH in the code if using a different location.

Save the Script:Save the main script as drowsiness_detection.py in your project directory.


🚀 Usage

Run the Script:Open a terminal in the project directory and execute:
python drowsiness_detection.py


The webcam will activate, displaying a live video feed with the EAR value.
If your eyes remain closed for ~1 second (30 frames at ~30 FPS), the alarm will play, and "DROWSINESS DETECTED!" will appear.
The alarm stops when you open your eyes (EAR ≥ 0.25).
Press ESC to exit the program.


Expected Output:

Video Feed: Shows the webcam feed with the EAR value (top-right) and a red "DROWSINESS DETECTED!" message when triggered.
Alarm: Plays alarm.wav when drowsiness is detected.



📜 License
This project is licensed under the MIT License. Feel free to use, modify, and distribute it as needed.

🙌 Acknowledgments
MediaPipe: For robust facial landmark detection.
OpenCV: For seamless video processing.
Playsound: For audio playback (consider switching to Pygame for enhanced reliability).
Inspiration: Developed to address real-world safety challenges through innovative computer vision solutions.

📬 Contact
For questions or contributions, reach out via GitHub Issues or email (likkisamarthreddy@gmail.com).
