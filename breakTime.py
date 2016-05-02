import webbrowser
import time

#a counter
counter = 0

print ("Hello " + time.ctime())
while (counter < 2):
    time.sleep()
    webbrowser.open("http://www.youtube.com")
    counter = counter + 1
print ("Bye " + time.ctime())
