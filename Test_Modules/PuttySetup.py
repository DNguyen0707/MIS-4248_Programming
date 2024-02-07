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
setup = '/usr/bollard-base/utils/setup-ronin.sh'
hiddenWIFI = ''
hiddenSSID = ''
hiddenPASS = ''



def run(RightSN = '000000', LeftSN = '000000', RightIP = 'google.com', LeftIP = 'bing.com'):
    
    sg.set_options(font=('Arial Bold', 16))
    sg.popup_ok('Turn On the Power Supply. Press the Power On Button on Both Carrier. Verify Both Carrier have LED1 on.')
    
    #do right side
    rightSide(RightSN, RightIP)
    
    #do left side
    leftSide(LeftSN, LeftIP)

    return True




def rightSide(RSN, RIP):
    #lock mouse
    mouse_listener = pynput.mouse.Listener(suppress=True)
    mouse_listener.start()  
    
    #phase 1
    while True:
        #open putty and type IP address
        subprocess.Popen([r'C:\Program Files\PuTTY\putty.exe'])
        time.sleep(1)
        pyautogui.click(740, 390)
        pyautogui.write(RIP, interval=0.1)
        time.sleep(1)
        pyautogui.press('enter') 
        
        #unlock mouse
        mouse_listener.stop()
        
        #Check if the window popup actually show up
        result = sg.popup_yes_no('Is this screen showing?', image=r"Z:\05. Manufacturing\60. Uncontrolled\Troubleshoot\Phat\MIS\727-4248\done.png") #add screenshot of warning popup
        if result == 'Yes':
            break
        else: 
            sg.popup_ok('Close Putty and click ok')
    
    #phase 2
    #lock mouse
    mouse_listener = pynput.mouse.Listener(suppress=True)
    mouse_listener.start()
    
    #run thru putty
    # pyautogui.hotkey("alt", "tab", interval=0.2) #switch back to putty
    time.sleep(1)
    pyautogui.press('tab') # tab to go to the Accept button
    time.sleep(1)
    pyautogui.press('enter') #accept
    time.sleep(1)
    pyautogui.click(384, 428) #focus on SSH screen
    time.sleep(1)
    pyautogui.write(username)  # login
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.write(password, interval=0.1)  # passwords
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.write(setup, interval=0.1)  # /user/...
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(8)
    pyautogui.write('y')  # Yes to continue
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.write(RSN)  # Set serial
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.write('1')  # For dual
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.write('1')  # for primary
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.write('11')  # for Pacific time
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    date = datetime.now().strftime('%H:%M:%S %m/%d/%y')
    pyautogui.write(date, interval=0.1)  # for time format
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.write('n')  # for not connect to the existing wlan
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(10)
    
    #unlock mouse
    mouse_listener.stop()
    
    #ask for SSID and pass
    global hiddenSSID
    hiddenSSID = sg.popup_get_text("Enter the ssid:", title='SSID', image=r"Z:\05. Manufacturing\60. Uncontrolled\Troubleshoot\Phat\MIS\727-4248\ssidpass.png")
    global hiddenPASS
    hiddenPASS = sg.popup_get_text("Enter the passwords:", title='Passwords', image=r"Z:\05. Manufacturing\60. Uncontrolled\Troubleshoot\Phat\MIS\727-4248\ssidpass.png")

    #debug
    print(hiddenSSID)
    print(hiddenPASS)
    
    return True

def leftSide(LSN, LIP):
    
    #lock mouse
    mouse_listener = pynput.mouse.Listener(suppress=True)
    mouse_listener.start() 
    
    #phase 1
    while True:
        #open putty and type IP address
        subprocess.Popen([r'C:\Program Files\PuTTY\putty.exe'])
        time.sleep(1)
        pyautogui.click(740, 390)
        pyautogui.write(LIP, interval=0.1)
        time.sleep(1)
        pyautogui.press('enter') 
        
        #unlock mouse
        mouse_listener.stop()
        
        #Check if the window popup actually show up
        result = sg.popup_yes_no('Is this screen showing?', image=r"Z:\05. Manufacturing\60. Uncontrolled\Troubleshoot\Phat\MIS\727-4248\done.png") #add screenshot of warning popup
        if result == 'No':
            sg.popup_ok('Close Putty and click ok')
            continue

            
        #phrase 2
        #lock mouse
        mouse_listener = pynput.mouse.Listener(suppress=True)
        mouse_listener.start()
        
        #run thru putty
        pyautogui.press('tab') # tab to go to the Accept button
        time.sleep(1)
        pyautogui.press('enter') #accept
        time.sleep(1)
        pyautogui.click(384, 428) #focus on SSH screen
        time.sleep(1)
        pyautogui.write(username)  # login
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.write(password, interval=0.1)  # passwords
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.write(setup, interval=0.1)  # /user/...
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(8)
        pyautogui.write('y')  # Yes to continue
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.write(LSN)  # Set serial
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.write('1')  # For dual
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.write('2')  # for secondary
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.write('11')  # for Pacific time
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)
        date = datetime.now().strftime('%H:%M:%S %m/%d/%y')
        pyautogui.write(date, interval=0.1)  # for time format
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.write('y')  # for connect to primary
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(2)
        
        #unlock mouse
        mouse_listener.stop()
        
        #phrase 3
        instruction = [
            [sg.Text('Click to run auto-connect'), sg.Button("Connect")],
            [sg.Text('If the connection failed, click Connect to run again')]
        ]
        
        picture = [
            [sg.Image(filename = 'C:/Users/dain/Documents/Github/MIS-4248_Programming/Resources/putty2.PNG', key='IMAGE1')],
        ]
        
        layout = [
            [sg.Column(picture)],
            [sg.Column(instruction)],
            [sg.Button("Pass"), sg.Button("Fail")]
        ]

        window = sg.Window('Auto-Connect', layout, size=(725,700), enable_close_attempted_event=True)
        
        hiddenWIFI = 'bruh'
        
        while True:
            event, values = window.read()
            
           
            if event == sg.WIN_CLOSED:
                return False
            elif event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT:
                return False
            elif event == "Fail":
                return False
            elif event == "Pass":
                window.close()
                break
            elif event == "Connect":
                 #lock mouse
                mouse_listener = pynput.mouse.Listener(suppress=True)
                mouse_listener.start()
                
                # turn everything off first
                pyautogui.hotkey("alt", "tab", interval=0.2) #switch back to putty
                time.sleep(1)
                pyautogui.write('agent off')  # for agent off
                time.sleep(1)
                pyautogui.press('enter')
                time.sleep(1)
                pyautogui.write('disable wifi')  # for disable Wi-Fi
                time.sleep(1)
                pyautogui.press('enter')
                time.sleep(1)
                pyautogui.write('agent on')  # for agent on
                time.sleep(1)
                pyautogui.press('enter')
                time.sleep(1)
                pyautogui.write('enable wifi')  # for enable Wi-Fi on
                time.sleep(1)
                pyautogui.press('enter')
                time.sleep(1)
                pyautogui.write('scan wifi')  # for scan Wi-Fi on
                time.sleep(1)
                pyautogui.press('enter')
                time.sleep(3)
                pyautogui.write('services')  # for services on
                time.sleep(1)
                pyautogui.press('enter')
                time.sleep(1)
                
                #check for hidden wifi
                if hiddenWIFI == 'bruh':
                    #unlock mouse
                    mouse_listener.stop()  
                    hiddenWIFI = sg.popup_get_text('After displaying available access points chose primary bollard network'
                                               '\n"hidden" SSID (blank) and copy the hash (2nd column) to clipboard that should have word "_hidden_"')
                    #lock mouse again
                    mouse_listener = pynput.mouse.Listener(suppress=True)
                    mouse_listener.start()
                    pyautogui.hotkey("alt", "tab", interval=0.2) #switch back to putty
                    
                pyautogui.write('connect ')  # connect Wi-Fi
                pyautogui.write(hiddenWIFI, interval=0.1)
                time.sleep(1)
                pyautogui.press('enter')
                time.sleep(1)
                pyautogui.write(hiddenSSID, interval=0.1)  # enter ssid
                time.sleep(1)
                pyautogui.press('enter')
                time.sleep(1)
                pyautogui.write(hiddenPASS, interval=0.1)  # enter passwords
                time.sleep(1)
                pyautogui.press('enter')
                time.sleep(10)
                mouse_listener.stop()
        break    
        
    #once done
    pyautogui.write('exit')  # for exit
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    return True


if __name__ == "__main__":
    print("Debug Mode")
    run()