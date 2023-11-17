# import packages
import pyautogui
import PySimpleGUI as sg
import subprocess
from datetime import datetime
import time
from pathlib import Path

#This is recover and VNC

def run():
    sg.set_options(font=('Arial Bold', 16))

    picture = [
        
    ]
    
    instruction = [
        
    ]
    
    layout = [
        
    ]
    
    window = sg.Window('Recover Carrier', layout, size=(700,600), enable_close_attempted_event=True)
    
    while True:
        event, values = window.read()
        
        if event == sg.WIN_CLOSED or event == 'Exit':
            return False
        elif event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT:
            return False
        elif event == "Fail":
            return False
        elif event == "Pass":
            window.close()
            break
    
    return True

if __name__ == "__main__":
    print("Debug Mode")
    run()