#structure of the commands for each pixel is  "particle minecraft:dust" + colour + XandY "~0 0 0 0 0 1 force @a"
#each pixel interval is 0.125 (for particle size 25)
import cv2
import numpy as np
def generatefunc(pathimg,pathfunc,num): #num is the number of the frame its on
    f = open(pathfunc, 'w') #creates the mcfunction file
    img = cv2.imread(pathimg)  #loads the frame (resized version)
    for x in range(20): #cycle through all the pixels in said frame 
        for y in range(15):
            colour = str(img.item(y,x,0)/255)+ " " +str(img.item(y,x,1)/255)+ " " +str(img.item(y,x,2)/255) #accessing all three channels of the pixel via numpy
            pos = "~" + str(1.25 - x*0.125) + " ~" + str(0.9375 - y*0.125) #position of the pixel according to its x and y 
            command = "particle minecraft:dust " + colour +" 0.75 " + pos + " ~-1.5 0 0 0 0 1 force @a" #creates the actual command
            f.write(command)
            f.write("\n")
    f.write("schedule function badapple:badapple_"+str(num+1)+" 1t") #this part makes a frame auto run the next one after a tick
for i in range (6562): #go through all the frames
    number = str(i+1).rjust(3,"0") 
    print(number)
    generatefunc(r"C:\Users\susername\Documents\python_stuff\bad apple resize\resized_"+number+".png",r"C:\Users\username\Documents\python_stuff\functionsmc\badapple_"+str(i)+".mcfunction",i)
#you will need to change the paths if you want to do this yourself.

