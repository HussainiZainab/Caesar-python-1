import math
from turtle import*


##Law of Cosine

def myTriangle ():
    firstSide = int(input("Please give me the first side length: "))
    secondSide = int(input("Please give me the second aide length: "))
    firstAngle = int(input("Please give me one angle: "))


    thirdSide = (pow(firstSide,2) + pow(secondSide,2)) - ((2)*(firstSide)*(secondSide)*(math.cos(math.radians(firstAngle))))
    thirdSide1 = pow(thirdSide,0.5)

    secondAngle = math.acos(((pow(secondSide,2)) - (pow(firstSide,2)) - (pow(thirdSide1,2)))/ ((-2)*(firstSide)*(thirdSide1)))
    secondAngle1 = math.degrees(secondAngle)

    thirdAngle = 180 - secondAngle1 - firstAngle

    ## TURTLE DRAWING ##
    zainab = Turtle()
    zainab.goto(0,0)
    zainab.down()
    zainab.forward(firstSide)
    zainab.left(180-thirdAngle)
    zainab.forward(secondSide)
    zainab.left(180-firstAngle)
    zainab.forward(thirdSide1)

    
    ##print ("thirdSide1")
    ##print ("thirdAngle")
    ##print ("secondAngle")

if __name__=="__main__":
    myTriangle()



    
