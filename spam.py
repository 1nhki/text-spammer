import keyboard
import time
many = input(" many :")     #input how many text that want to send
text = input("text:")       #input text

for a in range (3, 0, -1):  #3 second before spam deploy
    print (a)
    time.sleep(1)
    if a == 1 :
        print ("===GO===")
        
for i in range (int(many)) :            #loops
    time.sleep(0.3)                 #delay
    keyboard.write(text)                        #typing text
    keyboard.press_and_release('enter')         #and enter
    
    if keyboard.is_pressed('f8'):       #break funtion just in case
        break
