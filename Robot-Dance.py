from Myro import *
init("sim")

def slowTurnRight():
    turnRight(.82,1.5)

def fastTurnRight():
    turnRight(2.45,.5)

def fastTwirlRight():
    turnRight(9.8,1)

def slowTwirlRight():
    turnRight(4.9,2)
#def miniTurnRight():

def slowTurnLeft():
    turnLeft(.82,1.5)

def fastTurnLeft():
    turnLeft(2.45,.5)

def fastTwirlLeft():
    turnLeft(9.8,1)

def slowTwirlLeft():
    turnLeft(4.9,2)
#def miniTurnLeft():

def fastFor():
    forward(3.5,.23)

def fastBack():
    backward(3.5,.23)
    

def slowBack():
    backward(2,1.5)
    
def chaCha():
    fastFor()
    fastBack()
    fastTurnRight()
    turnLeft(4.9,.5)
    fastTurnRight
  
def twirlDrop():  
    fastTwirlRight()
    fastTurnRight()
    fastTurnLeft()
    fastTurnLeft()
    fastTurnRight()
    turnLeft(4.9,1)
    fastTwirlLeft()
    fastTurnLeft()
    fastTurnRight()
    fastTurnRight()
    fastTurnLeft()
    
for x in range (0,2):
    fastTurnLeft()
    
#THINK I CAN FLAI
for x in range (0,8):
    for x in range (0,2):
        fastFor()
    for x in range (0,2):
        fastBack()
turnRight(9.8,.5)
for x in range (0,2):
    fastFor()
for x in range (0,2):
    fastBack()
fastTurnLeft()
fastTurnRight()
fastTurnLeft()
turnRight(4.9,1)
fastTurnRight()
fastTurnRight()
for x in range (0,3):
    fastFor()
    fastBack()
slowTwirlRight()
slowTwirlLeft()
slowTwirlRight()
slowTwirlLeft()
slowTwirlRight()
slowTwirlLeft()
for x in range (0,8):
    fastTurnRight()
#i wanna run awaii
for x in range (0,8):
    fastFor()
    fastBack()
    fastFor()
    turnLeft(2.40,2)
turnLeft(2.40,2)

#YUU AND AI #1
for x in range (0,2):    
    for x in range (0,2):
        slowTwirlRight()
    for x in range (0,2):
        slowTwirlLeft()
fastTurnRight()
fastTurnLeft()
fastTurnRight()

chaCha()
chaCha()

#YUUUU AND AI AI AI AI AIII     #2
twirlDrop()
turnRight(1.23,1)
twirlDrop()
fastFor()
slowBack()

    


