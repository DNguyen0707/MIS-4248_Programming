# import packages
import pyautogui
import PySimpleGUI as sg
import subprocess
from datetime import datetime
import time
from pathlib import Path
import pynput

#common input
username = 'root'
password = 'm@xwe11W@sRite'
zDrive = ''
usrDrive = '/usr/bollard-base/config/'


def run(RightIP = 'google.com', LeftIP = 'bing.com', SN = '000000-000000'):
    sg.set_options(font=('Arial Bold', 16))
    
    #open winscp, the logo WinSCP should be at 329,217
    subprocess.Popen([r'C:\Program Files (x86)\WinSCP\WinSCP.exe'])
    
    #popup warning
    sg.popup_no_buttons('Make sure WinSCP is within the box in the background and DO NOT move it')
    
    #click back to winscp
    time.sleep(1)
    pyautogui.click(616, 358)
    time.sleep(1)
    
    #do right side
    rightSide(RightIP, SN)
    
    #do left side
    leftSide(LeftIP, SN)
    
    #check the files
    sg.popup_no_buttons('Verify Primary file has those information in the boxes. Close the window after done reading', title='Collect Data', text_color='#F7F6F2', keep_on_top=True, image=r"Z:\05. Manufacturing\60. Uncontrolled\Troubleshoot\Phat\MIS\727-4248\col6.png")
    sg.popup_no_buttons('Verify Secondary file has those information in the boxes. Close the window after done reading', title='Collect Data', text_color='#F7F6F2', keep_on_top=True, image=r"Z:\05. Manufacturing\60. Uncontrolled\Troubleshoot\Phat\MIS\727-4248\col7.png")

    return True

def rightSide(RIP, SerialN):
    
    #lock mouse
    mouse_listener = pynput.mouse.Listener(suppress=True)
    mouse_listener.start()
    
    #login (change to tab if possible)
    pyautogui.click(581, 389)  # click to the new site
    time.sleep(1)
    pyautogui.click(862, 481)  # click to the host
    time.sleep(1)
    pyautogui.write(RIP)  # enter ip right
    time.sleep(1)
    pyautogui.click(833, 529)  # enter user
    time.sleep(1)
    pyautogui.write(username)
    time.sleep(1)
    pyautogui.click(1004, 529)  # enter pass
    time.sleep(1)
    pyautogui.write(password, interval=0.1)
    time.sleep(1)
    pyautogui.click(913, 716) #login
    time.sleep(1)
    pyautogui.click(704, 740) #update
    time.sleep(1)
    
    #make it so it auto click the folder
    #double click address bar
    #click on the address
    pyautogui.hotkey('Ctrl', 'a') #ctrl+a
    time.sleep(1)
    pyautogui.hotkey('Backspace') #delete
    time.sleep(1)
    pyautogui.write(zDrive)
    pyautogui.write(SerialN)
    #ok or enter

    #finding the other folder
    #double click address bar
    #click on the address
    pyautogui.hotkey('Ctrl', 'a') #ctrl+a
    time.sleep(1)
    pyautogui.hotkey('Backspace') #delete
    time.sleep(1)
    pyautogui.write(usrDrive)
    time.sleep(1)
    #ok or enter
    
    #download
    pyautogui.hotkey('Ctrl', 'a')
    time.sleep(1)
    pyautogui.click(889, 347)  # Click Download
    time.sleep(1)
    pyautogui.click(878, 615)  # Ok
    time.sleep(1)
    
    #unlock mouse
    mouse_listener.start()
    
    return True

def leftSide(LIP, SerialN):
    
    #lock mouse
    mouse_listener = pynput.mouse.Listener(suppress=True)
    mouse_listener.start()
    
    #login (change to tab if possible)
    pyautogui.click(527, 297)  # click to the new site
    time.sleep(1)
    pyautogui.click(862, 481)  # click to the host
    time.sleep(1)
    pyautogui.write(LIP)  # enter ip right
    time.sleep(1)
    pyautogui.click(833, 529)  # enter user
    time.sleep(1)
    pyautogui.write(username)
    time.sleep(1)
    pyautogui.click(1004, 529)  # enter pass
    time.sleep(1)
    pyautogui.write(password, interval=0.1)
    time.sleep(1)
    pyautogui.click(913, 716) #login
    time.sleep(1)
    pyautogui.click(704, 740) #update
    time.sleep(1)
    
    #make it so it auto click the folder
    #double click address bar
    #click on the address
    pyautogui.hotkey('Ctrl', 'a') #ctrl+a
    time.sleep(1)
    pyautogui.hotkey('Backspace') #delete
    time.sleep(1)
    pyautogui.write(zDrive)
    pyautogui.write(SerialN)
    #ok or enter

    #finding the other folder
    #double click address bar
    #click on the address
    pyautogui.hotkey('Ctrl', 'a') #ctrl+a
    time.sleep(1)
    pyautogui.hotkey('Backspace') #delete
    time.sleep(1)
    pyautogui.write(usrDrive)
    time.sleep(1)
    #ok or enter
    
    #download
    pyautogui.hotkey('Ctrl', 'a')
    time.sleep(1)
    pyautogui.click(889, 347)  # Click Download
    time.sleep(1)
    pyautogui.click(878, 615)  # Ok
    time.sleep(1)
    pyautogui.click(785, 633)  # Yes Overwrite
    time.sleep(1)
    pyautogui.click(785, 633)  # Yes Overwrite
    time.sleep(1)

    #unlock mouse
    mouse_listener.start()
    
    return True

if __name__ == "__main__":
    print("Debug Mode")
    run()