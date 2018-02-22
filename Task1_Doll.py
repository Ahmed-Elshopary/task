# Main call library.....
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from math import *


#############################
def face():
	glColor3d(0.8,0.8,0.2)
	glBegin(GL_POLYGON)
	glVertex2d(.17,.55)
	glVertex2d(.17,.4)
	glVertex2d(-.17,.4)
	glVertex2d(-.17,.55)
	glEnd()
	glColor3d(0.2,0.2,0.2)
	glBegin(GL_POLYGON)
	glVertex2d(.023,.45)
	glVertex2d(.023,.43)
	glVertex2d(-.023,.43)
	glVertex2d(-.023,.45)
	glEnd()
	glColor3d(0.2,0.2,0.2)
	glBegin(GL_POLYGON)
	glVertex2d(.07,.48)
	glVertex2d(.09,.48)
	glVertex2d(.09,.51)
	glVertex2d(.07,.51)
	glEnd()
	glColor3d(0.2,0.2,0.2)
	glBegin(GL_POLYGON)
	glVertex2d(-.07,.48)
	glVertex2d(-.09,.48)
	glVertex2d(-.09,.51)
	glVertex2d(-.07,.51)
	glEnd()
	
	glFlush()
	
def legs():
	glColor3d(.2,.2,.9)
	glBegin(GL_POLYGON)
	
	glVertex2d(.1,-.23)
	glVertex2d(.2,-.23)
	glVertex2d(.2,-.6)
	glVertex2d(.1,-.6)
	
	glEnd()
		
	glColor3d(.2,.2,.9)
	glBegin(GL_POLYGON)
	
	glVertex2d(-.1,-.23)
	glVertex2d(-.2,-.23)
	glVertex2d(-.2,-.6)
	glVertex2d(-.1,-.6)
	
	glEnd()	
	glFlush()
	
def arms():
	glColor3d(.6,.4,.6)
	glBegin(GL_POLYGON)
	glVertex2d(.23,.23)
	glVertex2d(.23,.18)
	glVertex2d(.4,.001)
	glVertex2d(.45,.03)
	glEnd()
	glColor3d(.6,.4,.6)
	glBegin(GL_POLYGON)
	glVertex2d(-.23,.23)
	glVertex2d(-.23,.18)
	glVertex2d(-.4,.001)
	glVertex2d(-.45,.03)
	glEnd()
	glFlush()
	
	
	
def body():
	glColor3d(0.3,0.4,.5)
	glBegin(GL_POLYGON)
	glVertex2d(.23,0.23)
	glVertex2d(.23,-0.23)
	glVertex2d(-.23,-.23)
	glVertex2d(-.23,.23)
	glEnd()
	glFlush()
	
def neck():
	glColor3d(.2,.2,.4)
	glBegin(GL_POLYGON)
	glVertex2d(.05,.4)
	glVertex2d(.05,.23)
	glVertex2d(-.05,.23)
	glVertex2d(-.05,.4)
	glEnd()
	glFlush()
	
def doll():
	glColor(1,1,1,1)
	glClear(GL_COLOR_BUFFER_BIT)
	neck()
	legs()
	body()
	arms()
	face()
	glEnd()
	glFlush()
	
	
	
# Main Function of OpenGl.....
glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB )
glutInitWindowSize(700,700)
glutCreateWindow(b":First Task")
glutDisplayFunc(doll)
glutMainLoop()					
	
###########################













