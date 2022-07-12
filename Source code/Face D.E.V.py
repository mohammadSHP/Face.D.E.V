
print ('Please wait...')


import cv2
from retinaface import RetinaFace
from deepface import DeepFace
import tkinter as tk
from tkinter import filedialog
from tkinter.constants import X


# Define for getting path
def path_getter():
 
  #selection window
  root = tk.Tk()
  root.withdraw()
  X = str(filedialog.askopenfilenames())

  #Start with new image
  X = X.replace("/", "\\\\" )
  X = X.replace('(', '')
  X = X.replace(')', '')
  X = X.replace(',', '')
  X = X.replace("'", '')
  print ('your selected path is: ', X)
  return X


# Define of face detection
def face_det():
  #Face Detection
  Z = path_getter()
  img_path = cv2.imread(Z)
  obj = RetinaFace.detect_faces(img_path)

  for key in obj.keys():
    identity = obj[key]
    facial_area = identity["facial_area"]
    landmarks = identity["landmarks"]

    #Creat facial frame
    facial_rect = cv2.rectangle(img_path, (facial_area[2], facial_area[3]), (facial_area[0], facial_area[1]), (0, 0, 255), 1)
    facial_img = img_path[facial_area[1]: facial_area[3], facial_area[0]: facial_area[2]]
    
  #Show the facial area with frame (press "Esc" to exit!)
  while True:
    cv2.imshow ("Face Detected <Press 'Esc' to continue...>", facial_rect)
    k = cv2.waitKey(5)
    if k == 27:

      # De-allocate any associated memory usage 
      cv2.destroyAllWindows()  
      break
  what()


# Define of face extraction
def face_ext():
  
  #The counter
  count = 1
  
  #Extract and save each facese with diffrent name
  Z = path_getter()
  img_path = cv2.imread(Z)
  faces = RetinaFace.extract_faces(img_path, align = True)
  for face in faces:
    new_image = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
    Z = Z.replace('.jpg', '')
    save_path = Z + 'No ' + str(count) + ".jpg"
    cv2.imwrite(save_path, new_image)
    print ('Extract & Save successfully ' + str(count))
    count += 1
  what()


# Define of face verification
def face_ver ():
  try:
    img_ver1 = path_getter()
  except:
    img_ver1 = input ('Please enter the name you want to verify here: ')
  
  try:
    img_ver2 = path_getter()
  except:

    img_ver2 = input ('Please enter the name you want to verify here: ')
    
  try:
    ver_ans = DeepFace.verify(img1_path = img_ver1, img2_path = img_ver2, model_name = 'ArcFace', detector_backend = 'retinaface')
  except:
      print ('Verification failed! Make sure you selected the correct file.')
      face_ver()

  if ver_ans.get('verified') == True:
    print ('Verification confirmed!')
  else:
    print ('Verification failed!')
  what()


def what():
  face_in = input ('\nHello! what do you want? \n Press "d" for face detection \n Press "e" for face extraction \n Press "v" for face verification.\n')
  if face_in == 'd':
    face_det()
  elif face_in == 'e':
    face_ext()
  elif face_in == 'v':
    face_ver()
  else:
    what()

what()
face_det()
face_ext()
face_ver()
