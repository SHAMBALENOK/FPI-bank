import mediapipe as mp
import face_recognition

mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils
face_detection = mp_face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.3)

# Load the jpg files into numpy arrays
putin_image = face_recognition.load_image_file("putin.png")
pasha_image = face_recognition.load_image_file("pasha.jpg")

# Get the face encodings for each face in each image file
# Since there could be more than one face in each image, it returns a list of encodings.
# But since I know each image only has one face, I only care about the first encoding in each image, so I grab index 0.
try:
    putin_face_encoding = face_recognition.face_encodings(putin_image)[0]
    pasha_face_encoding = face_recognition.face_encodings(pasha_image)[0]
except IndexError:
    print("I wasn't able to locate any faces in at least one of the images. Check the image files. Aborting...")
    quit()

known_faces = [
    putin_face_encoding,
    pasha_face_encoding
]
names_faces = [
    'Владимир Владимирович Путин',
    'Пашуля'
]


def f():
    img = face_recognition.load_image_file("new_img.png")
    img_encoding = face_recognition.face_encodings(img)[0]
    # results is an array of True/False telling if the unknown face matched anyone in the known_faces array
    results = face_recognition.compare_faces(known_faces, img_encoding)

    # for i in range(len(results)):
    #     print(F"Is the unknown face a picture of {names_faces[i]}? {format(results[i])}")
    for i in range(len(results)):
        if results[i]:
            print(f'Это {names_faces[i]}')
            return True, names_faces[i]

    return False, 'неизвестный'
