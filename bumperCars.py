##
## Name: Joey Baldwin
## bumper.py
##
## Purpose:
##  Uses the Graphics package to create a simulation of two bumper cars
##
## Certification of Authenticity:
##  I certify that this is entirely my own work.
##
## Sources:
##  http://www.vobarian.com/collisions/2dcollisions2.pdf
##      I used this source to calculate collision with physics.
##      I did this part of the assignment before we were told in class
##      that it wasn't necesary. Still, it gave a very cool result
##
##  http://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/graphics.html
##      I used this source to learn about the color_rgb() function in the
##      graphics package. I could have used a list and randomly selected
##      pre-chosen colors from that list, but I just wanted to try something
##      different
## 
## Output: two circles moving randomly and bouncing of walls and each other 
##
##Pseudocode
##1. import
##    A) graphics All
##    B) time -> sleep
##    C) random -> randint
##2. write functions
##    A) getRandom(moveAmount)
##        1) use randint to find random integer
##        2) return integer
##    B) didCollide(ball1, ball2)
##        1)get centers of both balls
##        2) find the X and Y values of both balls
##        3) get the radius of each ball
##        4) use euclidean distance formula to find distance between center points
##        5) sum the radii
##        6) if/else
##            a) if distance <= sumRadii return True
##            b) else return false
##    C) hitVertical(ball,win)
##        1) get center of ball
##        2) find X value of ball
##        3) get radius of ball
##        4) find width of window
##        5) if/else
##            a) if X <= radius or X >= width-radius return True
##            b) else return false
##    D) hitHorizontal(ball,win)
##        1) get center of ball
##        2) find Y value of ball center
##        3) get radius of ball
##        4) find height of window
##        5) if/else
##            a) if Y <= radius or Y >= height-radius return True
##            b) else return False
##    E) collisionV(listV,ball1,ball2,mass1,mass2)
##        1) use velocity list to find X and Y velocities of both balls
##        2) find the X and Y locations of both balls
##        3) find difference the X's and Y's
##        4) find distance between centers of balls
##        5) find unit normal vector
##        6) find normal scalars
##        7) find tangental scalars
##        8) find tangental velocities after collision
##        9) use collision functions to find normal primes
##        10) find new normal vectors
##        11) find new tangental vectors
##        12) sum the new tangental and normal vectors to find new vectors
##        13) return new velocity list
##    F) main
##        1)create window
##        2) create cars
##        3) generate random X and Y velocities using getRandom() and set in a list
##        4) create loop that moves cars
##            a)sleep
##            b) test collisions
##                1. if didCollide() is True run collisionV() 
##                2. if hitVertical() is True set velocity X to -X for each car
##                3. if hitHorizontal() is True set velocity Y to -Y for each car
##            c) move cars based on velocityList

from graphics import*
from time import sleep
from random import randint

#returns a random number between -moveAmount and +moveAmount
def getRandom(moveAmount):
    return randint(-moveAmount,moveAmount)
    

#returns boolean based on the collision of the two balls
def didCollide(ball1,ball2):
    ball1Center = ball1.getCenter()
    ball2Center = ball2.getCenter()
    ball1X = ball1Center.getX()
    ball1Y = ball1Center.getY()
    ball2X = ball2Center.getX()
    ball2Y = ball2Center.getY()
    ball1Radius = ball1.getRadius()
    ball2Radius = ball2.getRadius()
    distance = (((ball2X-ball1X)**2) + ((ball2Y-ball1Y)**2))**(1/2)
    radius = ball1Radius+ball2Radius
    if distance <= radius:
        answer = True
        randomColor(ball1)
        randomColor(ball2)
    else:
        answer = False
    return answer

#returns True if ball hits a vertical wall, False otherwise
def hitVertical(ball,win):
    ballCenter = ball.getCenter()
    ballX = ballCenter.getX()
    radius = ball.getRadius()
    width = win.getWidth()
    if ballX <= radius or ballX >= width-radius:
        answer = True
        randomColor(ball)
    else:
        answer = False
    return answer
    
#returns True if ball hits a horizontal wall, False otherwise
def hitHorizontal(ball,win):
    ballCenter = ball.getCenter()
    ballY = ballCenter.getY()
    radius = ball.getRadius()
    height = win.getHeight()
    if ballY <= radius or ballY >= height-radius:
        answer = True
        randomColor(ball)
    else:
        answer = False
    return answer

#returns a random color
def randomColor(circle):
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    circle.setFill(color_rgb(r,g,b))
    

#returns list of new velocities
def collisionV(listV,ball1,ball2,mass1,mass2):
    #Velocities of the balls in x and y direction
    v1X = listV[0][0]
    v1Y = listV[0][1]
    v2X = listV[1][0]
    v2Y = listV[1][1]
    #location of ball1 and ball2
    ball1Center = ball1.getCenter()
    ball2Center = ball2.getCenter()
    ball1X = ball1Center.getX()
    ball1Y = ball1Center.getY()
    ball2X = ball2Center.getX()
    ball2Y = ball2Center.getY()
    #find the difference of X's and Y's
    deltaX = ball2X - ball1X
    deltaY = ball2Y - ball1Y
    #finds distance between ball 1 and ball 2
    distance = ((deltaX**2) + (deltaY**2))**(1/2)
    #finds unit normal vector
    unX = deltaX/distance
    unY = deltaY/distance
    #finds unit tangent vector
    utX = -unY
    utY = unX
    #finds normal scalars
    v1n = (unX*v1X)+(unY*v1Y)
    v2n = (unX*v2X)+(unY*v2Y)
    #finds tangent scalars
    v1t = (utX*v1X)+(utY*v1Y)
    v2t = (utX*v2X)+(utY*v2Y)
    #tangental velocities after collision
    v1Prime = v1t
    v2Prime = v2t
    # collision formulas
    v1nPrime = (v1n*(mass1-mass2)+2*mass2*v2n)/(mass1+mass2)
    v2nPrime = (v2n*(mass2-mass1)+2*mass1*v1n)/(mass1+mass2)
    # normal vectors
    v1nPrimeX = v1nPrime * unX
    v1nPrimeY = v1nPrime * unY
    v2nPrimeX = v2nPrime * unX
    v2nPrimeY = v2nPrime * unY
    # tangental vectors
    v1tPrimeX = v1t * utX
    v1tPrimeY = v1t * utY
    v2tPrimeX = v2t * utX
    v2tPrimeY = v2t * utY
    # new velocity vectors
    v1X = v1nPrimeX + v1tPrimeX
    v1Y = v1nPrimeY + v1tPrimeY
    v2X = v2nPrimeX + v2tPrimeX
    v2Y = v2nPrimeY + v2tPrimeY
    return [[v1X,v1Y],[v2X,v2Y]]

def main():
    #create window
    win = GraphWin("Bumper Car Simulation",600,600)
    width = win.getWidth()
    height = win.getHeight()
    # create cars
    radius = 20
    car1 = Circle(Point(radius+30,height/2),radius)
    car2 = Circle(Point(width - (radius+30),height/2),radius)
    randomColor(car1)
    randomColor(car2)
    car1.draw(win)
    car2.draw(win)
    # initial velocities
    v1X = getRandom(15)  
    v1Y = getRandom(15)
    v2X = getRandom(15)
    v2Y = getRandom(15)
    velocityList = [[v1X,v1Y],[v2X,v2Y]]
    # car masses
    car1mass = 1
    car2mass = 1
    # loop that moves cars
    for i in range(500):
        sleep(.04)
        # test if the circles hav hit eachother
        if didCollide(car1,car2):
            velocityList = collisionV(velocityList,car1,car2,car1mass,car2mass)
        if hitVertical(car1,win):
            velocityList[0][0] = -velocityList[0][0]
        if hitVertical(car2,win):
            velocityList[1][0] = -velocityList[1][0]
        if hitHorizontal(car1,win):
            velocityList[0][1] = -velocityList[0][1]
        if hitHorizontal(car2,win):
            velocityList[1][1] = -velocityList[1][1]

        car1.move(velocityList[0][0],velocityList[0][1])
        car2.move(velocityList[1][0],velocityList[1][1])

main()
        
            
    
    
    
    

