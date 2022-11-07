#this tool is used to resend a messege to the place where you place your pointer continously

import pyautogui as auto
import time as t

def loopContent():
    auto.typewrite("your text messege here")
    auto.press("enter")
    #you can write 10 and 11 as many times with different messeges but remember to write the messege you want to send seperately must be put seperaately


    #for delay we use time.sleep()
    t.sleep(1) #waits 1 sec to re type the same message


#uncomment what you need 

for i in range(0,10): #the end value is the value of your total number of times you send the messege
    loopContent()

#for infinite unstopped until you stop the program
while True:
    loopContent()

#once you are done with it you can press ctrl+c to end the program in the terminal