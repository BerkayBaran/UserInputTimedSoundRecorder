# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 07:01:51 2022

@author: berka
"""

#input timed soundrecorder

from pynput import keyboard
import sounddevice
from scipy.io.wavfile import write
import shutil
import os

print("Please press Enter to record, press Space to exit.")
def on_press(key):
    
    if key == keyboard.Key.space:
        return False
    try:
        a = key.char  
    except:
        a = key.name  
        
    if a in ['enter']:      
        while True:
            try:
                a =  int(input("How many seconds of recording will it be? "))
                break
            except:
                input("Invalid input.")
                
        def record_sound(seconds, file):
            print("Recording")
            recording = sounddevice.rec((seconds * 44100), samplerate= 44100, channels=2)
            sounddevice.wait()
            write(file, 44100, recording)
        
        notallowed = set(r'\/:*?"<>|')
        
        while True:
            
            soundname = input("Enter The Sound Name ")
            
            if soundname and notallowed.issuperset(soundname):
                print("Invalid characters entered!")
            else:
                break
        
        record_sound(int(a),  soundname + '.wav')
        homeDir = os.environ["HOMEPATH"]
        sourcepath= os.path.dirname(__file__)
        sourcefiles = os.listdir(sourcepath)
        destinationpath = homeDir+'/OneDrive/Masaüstü/'
        for file in sourcefiles:
            if file.endswith('.wav'):
                shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpath,file))
              
        print("Recording Finished and saved to desktop. To record again press Enter or Space to exit.")

listener = keyboard.Listener(on_press=on_press)
listener.start()  # start to listen on a separate thread
listener.join()  # remove if main thread is polling self.keys

