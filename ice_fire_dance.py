import sounddevice as sd
import numpy as np
from pynput.keyboard import Key, Controller
import time

keyboard = Controller()
fs = 44100                               
duration = 5 # seconds
while(1): 
    myrecording = sd.rec(4410 , samplerate=fs, channels=1, dtype='float64')
    # I would like to read myrecording into a stream at this point. 
    #print("Recording Audio")
    sd.wait()
    #print("Audio recording complete , Play Audio")
    #print(myrecording)
    keyboard.press(Key.down)
    
    for i in myrecording:
        if i>0.1 :      
            #print("!")
            keyboard.release(Key.down)
            #time.sleep(1)
            keyboard.press(Key.space)
            

            keyboard.release(Key.space)
            time.sleep(0.1) 
            break               
plt.plot(myrecording)
plt.show() 