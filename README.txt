Project name: Face D.E.V
Date: 12/6/2021
Author: Mohammad Sharifi Pishe

>>> introduction:
This project Detect, Extract, and verify the faces in the picture.

It has three features:
I) Detecting faces in a single image on your system.
II) Extract the faces and save them in front of the main picture.
III) Verification between 2 pictures that include one person's face.

You can use the source code to see how its works.

>>>Built with:
In this app, I use OpenCV as a computer vision library for handling the picture,
RetinaFace is a face detection module and The original implementation is mainly based on mxnet.
Then, its TensorFlow based re-implementation is published by Stanislas Bertrand.
and at the end, I use Deepface to compare and verify persons.

>>> Let's start.
There is three folder here.
I) Project: include an EXE file
II) Source code: include a python code of the project
III) Samples: include some prepared pictures that you can use if you need them.

>>> How to use?
You can run the EXE file without any requirements on your system and easily use it.
You can choose what feature you want to use. Detection, Extraction, or verification.

For Detection, you should choose a picture that includes one or more faces in it.
After selecting the picture, the app starts to detect faces and after a second,
it shows your picture with a frame around the faces.

For Extraction, you should choose a picture that includes one or more faces in it.
After selecting a picture, the app starts to detect faces and save them in that path with a specific name.

For verification, you should choose two pictures that include just one face.
Then the app starts to compare them. If they are the same person, you see this message: 
"Verification confirmed!"
and on the other hand, you see: "Verification failed!"

After using features you can use the other feature.

>>> requirments:
For using source code you need these requirments (They are alos in "requirments.txt"):
deepface==0.0.68
numpy==1.21.4
opencv-python==4.5.2.54
retina-face==0.0.5
retinaface==0.0.6
tensorboard==2.1.1
tensorflow==2.1.0
tensorflow-estimator==2.1.0

