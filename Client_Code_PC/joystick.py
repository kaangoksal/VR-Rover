import pygame
import time
import socket
import sys
import json

pygame.display.init()
pygame.joystick.init()
pygame.joystick.Joystick(0).init()

HOST, PORT = "192.168.8.174", 5005
data = " ".join(sys.argv[1:])




# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


# Prints the joystick's name
JoyName = pygame.joystick.Joystick(0).get_name()
print "Name of the joystick:"
print JoyName
# Gets the number of axes
JoyAx = pygame.joystick.Joystick(0).get_numaxes()
print "Number of axis:"
print JoyAx

sock.connect((HOST, PORT))

# Prints the values for axis0
while True:
        pygame.event.pump()
        #print pygame.joystick.Joystick(0).get_axis(0)
        #print pygame.joystick.Joystick(0).get_axis(1)
        #print pygame.joystick.Joystick(0).get_axis(2) #one
        #print pygame.joystick.Joystick(0).get_axis(3)
        #print pygame.joystick.Joystick(0).get_axis(4)
        #print pygame.joystick.Joystick(0).get_axis(5) #one
        rightwheel = ((pygame.joystick.Joystick(0).get_axis(5) * 100) + 100)/2
        leftwheel = ((pygame.joystick.Joystick(0).get_axis(2) * 100) + 100)/2
        
        if rightwheel > 10 or leftwheel > 10:
           
            print "leftwheel" + str(leftwheel)
            print "rightwheel" + str(rightwheel)
            dictlocal =  {'leftmotor': leftwheel, 'rightmotor': rightwheel}
            returnstring = json.dumps(dictlocal, sort_keys=True, indent=4, separators=(',', ': '))
	    print returnstring
            sock.sendall(returnstring + "\n")
        time.sleep(0.05)



