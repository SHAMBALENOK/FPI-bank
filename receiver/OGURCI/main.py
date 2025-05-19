import mediapipe as mp
import face_recognition

mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils
face_detection = mp_face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.3)

# Load the jpg files into numpy arrays
biden_image = face_recognition.load_image_file("biden.jpg")
obama_image = face_recognition.load_image_file("obama.jpg")
unknown_image = face_recognition.load_image_file("obama2.jpg")
unknown1_image = face_recognition.load_image_file("bababoy1.jpg")
unknown2_image = face_recognition.load_image_file("bababoy2.jpg")
unknown3_image = face_recognition.load_image_file("bababoy3.jpg")

# Get the face encodings for each face in each image file
# Since there could be more than one face in each image, it returns a list of encodings.
# But since I know each image only has one face, I only care about the first encoding in each image, so I grab index 0.
try:
    biden_face_encoding = face_recognition.face_encodings(biden_image)[0]
    obama_face_encoding = face_recognition.face_encodings(obama_image)[0]
    unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]
    unknown1_face_encoding = face_recognition.face_encodings(unknown1_image)[0]
    unknown2_face_encoding = face_recognition.face_encodings(unknown2_image)[0]
    unknown3_face_encoding = face_recognition.face_encodings(unknown3_image)[0]
except IndexError:
    print("I wasn't able to locate any faces in at least one of the images. Check the image files. Aborting...")
    quit()

known_faces = [
    biden_face_encoding,
    obama_face_encoding,
    unknown_face_encoding,
    unknown1_face_encoding,
    unknown2_face_encoding
]


def f():
    img = face_recognition.load_image_file("new_img.png")
    img_encoding = face_recognition.face_encodings(img)[0]
    # results is an array of True/False telling if the unknown face matched anyone in the known_faces array
    results = face_recognition.compare_faces(known_faces, img_encoding)

    print(F"Is the unknown face a picture of ...? {format(results[2])}")


# def recognition_send(piddi, name):
#     a = f"Is the unknown face a picture of {name}? {format(results[piddi])}"
#     return a
