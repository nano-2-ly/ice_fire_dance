import sounddevice as sd
import numpy as np
from pynput.keyboard import Key, Controller
keyboard = Controller()
fs = 4400                           
duration = 5 # seconds
while(1):
    myrecording = sd.rec(10 , samplerate=fs, channels=1, dtype='float64')
    # I would like to read myrecording into a stream at this point. 
    #print("Recording Audio")
    sd.wait()
    #print("Audio recording complete , Play Audio")
    #print(myrecording)
    for i in myrecording:
        if i>0.1:
            print("!")
            keyboard.press(Key.space)
            keyboard.release(Key.space)
            break
plt.plot(myrecording)
plt.show()