# import packages
import pyautogui
import PySimpleGUI as sg
import subprocess
from datetime import datetime
import time
from pathlib import Path

def run():
    sg.set_options(font=('Arial Bold', 16))

    sg.popup_no_buttons('Detach the J9 cable for both Primary and Secondary DUTs.'
                            '\nClose the window after done reading', title='Disassemble DUTs', text_color='#F7F6F2', keep_on_top=True, image=r"Z:\05. Manufacturing\60. Uncontrolled\Troubleshoot\Phat\MIS\727-4248\dis.png")
    
    return True

if __name__ == "__main__":
    print("Debug Mode")
    run()