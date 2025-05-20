import cv2
import mediapipe as mp
import numpy as np
import threading
import os
from playsound import playsound
playsound(r"C:\Users\user\Desktop\Project\alarm.wav")


# Eye aspect ratio threshold and consecutive frame count
EYE_AR_THRESH = 0.25
EYE_AR_CONSEC_FRAMES = 30

COUNTER = 0
ALARM_ON = False
ALARM_LOCK = threading.Lock()

# Use absolute path for alarm sound
ALARM_PATH = os.path.abspath("alarm.wav")

def sound_alarm():
    global ALARM_ON
    with ALARM_LOCK:
        try:
            playsound(ALARM_PATH)
        except Exception as e:
            print(f"Alarm failed to play: {e}")
        finally:
            ALARM_ON = False  # Reset alarm flag after sound

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1)

def eye_aspect_ratio(eye_landmarks):
    # Calculate distances between vertical eye landmarks
    A = np.linalg.norm(eye_landmarks[1] - eye_landmarks[5])
    B = np.linalg.norm(eye_landmarks[2] - eye_landmarks[4])
    # Calculate distance between horizontal eye landmarks
    C = np.linalg.norm(eye_landmarks[0] - eye_landmarks[3])
    # EAR formula
    return (A + B) / (2.0 * C)

cap = cv2.VideoCapture(0)

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        h, w = frame.shape[:2]
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(rgb)
        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                mesh_points = np.array(
                    [(int(p.x * w), int(p.y * h)) for p in face_landmarks.landmark]
                )
                # Indices for left and right eyes (MediaPipe Face Mesh)
                left_eye = mesh_points[[33, 160, 158, 133, 153, 144]]
                right_eye = mesh_points[[362, 385, 387, 263, 373, 380]]
                left_ear = eye_aspect_ratio(left_eye)
                right_ear = eye_aspect_ratio(right_eye)
                ear = (left_ear + right_ear) / 2.0

                if ear < EYE_AR_THRESH:
                    COUNTER += 1
                    if COUNTER >= EYE_AR_CONSEC_FRAMES:
                        if not ALARM_ON:
                            ALARM_ON = True
                            threading.Thread(target=sound_alarm, daemon=True).start()
                        cv2.putText(frame, "DROWSINESS DETECTED!", (10, 30),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                else:
                    COUNTER = 0
                    ALARM_ON = False

                cv2.putText(frame, f"EAR: {ear:.2f}", (500, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        cv2.imshow("Drowsiness Detection", frame)
        if cv2.waitKey(1) & 0xFF == 27:  # ESC key to exit
            break
finally:
    cap.release()
    cv2.destroyAllWindows()
