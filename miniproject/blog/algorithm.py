import face_recognition
import dlib
import cv2
from scipy.spatial import distance


# def viewImage(image, name_of_window):
#     '''
#     show window with the image
#     '''
#     cv2.namedWindow(name_of_window, cv2.WINDOW_NORMAL)
#     cv2.imshow(name_of_window, image)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
#
#
# def showFaceLandmarks(image):
#     '''
#     show face rectangle and face landmarks. Doesn't change the original image.
#     '''
#     image_copy = image.copy()
#     #find face rectangle
#     face_loc = face_recognition.face_locations(image_copy)[0]
#     cv2.rectangle(image_copy, (face_loc[3], face_loc[0]), (face_loc[1], face_loc[2]), (0, 255, 255), 4)
#     #find and match all landmarks
#     face_landmarks = face_recognition.face_landmarks(image_copy)[0]
#     for key in face_landmarks.keys():
#         for i in face_landmarks.get(key):
#             cv2.circle(image_copy, (i[0], i[1]), 4, (0, 0, 255), -1)
#     #show image
#     viewImage(image_copy, 'landmarks')


def is_face_long(face_landmarks):
    """
    returns True if the face width is less than 70 percent of the length.

    """
    threshold = 70
    cheekbones_width = distance.euclidean(face_landmarks.get('chin')[1], face_landmarks.get('chin')[15])
    face_height = distance.euclidean(face_landmarks.get('nose_bridge')[1], face_landmarks.get('chin')[8])

    if cheekbones_width * 100 / 2 / face_height < 70:
        return True
    else:
        return False


def is_triangle(face_landmarks):
    """

    """
    threshold = 38.7
    jaw = distance.euclidean(face_landmarks.get('chin')[4], face_landmarks.get('chin')[12])
    chin_height = distance.euclidean(face_landmarks.get('chin')[8], face_landmarks.get('bottom_lip')[9])
    if chin_height * 100 / jaw > 38.7:
        return True
    else:
        return False


def is_square(face_landmarks):
    """

    """
    threshold = 83
    cheekbones_width = distance.euclidean(face_landmarks.get('chin')[1], face_landmarks.get('chin')[15])
    jaw = distance.euclidean(face_landmarks.get('chin')[4], face_landmarks.get('chin')[12])
    if jaw * 100 / cheekbones_width > 83:
        return True
    else:
        return False


def get_face_landmarks(image):
    i = cv2.imread(image)
    #print(image)
    return face_recognition.face_landmarks(i)[0]


# face_landmarks = face_recognition.face_landmarks(image)[0]
