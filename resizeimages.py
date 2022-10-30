import numpy as np
import cv2

for i in range(6562): #cycles through all the frames of the animation
    number = str(i+1).rjust(3,"0") #changes i to 001, 002,003, ect because thats how the frames are numbered
    print(number)
    img = cv2.imread(r"C:\Users\username\Documents\python_stuff\bad apple\bad_apple_"+number+".png") #access the images (you will have to change the path if you want to do this yourself)
    resized = cv2.resize(img, (20,15)) #resize them, im using 20x15
    cv2.imwrite("resized_"+number+".png", resized) # creates the images
    # so i kinda forgot to put them into a seperate folder so they all appeared in the same directory.. oops xD

