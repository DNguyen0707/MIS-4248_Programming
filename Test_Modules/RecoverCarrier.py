# import packages
import pyautogui
import PySimpleGUI as sg
import subprocess
from datetime import datetime
import time
from pathlib import Path
import pynput

#This is recover and VNC

IP = ''

def run():
    sg.set_options(font=('Arial Bold', 16))

    picture = [
        [sg.Image(filename = 'C:/Users/dain/Documents/Github/MIS-4248_Programming/Resources/step1recover.PNG', key='IMAGE1')],
    ]
    
    instruction = [
        [sg.Text('Click to run recovery mode'), sg.Button("Recover")],
        [sg.Text('Click to run TVNC'), sg.Button("TVNC")],
        [sg.Text(size=20)],
        [sg.Text('IP address:'), sg.InputText('192.168.29.',size=(20,1), key="IPbox")],
    ]
    
    layout = [
        [sg.Column(picture)],
        [sg.Column(instruction)],
        [sg.Button("Pass"), sg.Button("Fail"), sg.Exit()]
    ]
    
    window = sg.Window('Recover Carrier', layout, size=(725,700), enable_close_attempted_event=True)
    
    while True:
        event, values = window.read()
        
        # window pressing
        if event == sg.WIN_CLOSED or event == 'Exit':
            return False
        elif event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT:
            return False
        elif event == "Fail":
            return False
        elif event == "Pass":
            IP = values["IPbox"]
            window.close()
            break
        
        # Test pressing
        if event == "Recover":
            # run recover window
            subprocess.Popen([r'Z:\05. Manufacturing\60. Uncontrolled\Troubleshoot\Dai\MIS Program\727-4248 Programming\recovery-windows.bat']) #change address
            time.sleep(6)
            
            # ask if done
            result = sg.popup_yes_no("Does it appear with DONE?", title='Recovery Right Carrier', image=r"Z:\05. Manufacturing\60. Uncontrolled\Troubleshoot\Dai\MIS Program\727-4248 Programming\Resources\done.png") #change address
            
            #if doesnt work first time
            if result == "No" and retry < 1:
                sg.popup_no_buttons('1. Turn Off the Power Supply.\n2. Hold the Recovery button on DUT.\n3. Turn On the Power Supply.\n4. Press the Power On Button on DUT.\n5. Press "Recover" again', title='Solution', text_color='#F7F6F2', keep_on_top=True)

                retry = retry + 1
                continue
            
            #Replace bottom after trying 3 time
            elif result == "No" and retry == 1:
                sg.popup_no_buttons('1. Turn Off the Power Supply.\n2. Replace bottom board (727-4238).\n3. Hold the Recovery button on DUT.\n4. Turn On the Power Supply.\n5. Press the Power On Button on DUT.', title='Solution', text_color='#F7F6F2', keep_on_top=True)
                retry = retry + 1
                continue
            
            #Stop test and go next
            elif result == "No" and retry == 2:
                sg.popup_no_buttons('Turn Off the Power Supply and give the pair to Test Engineer', title='Solution', text_color='#F7F6F2', keep_on_top=True)
                window.close()
                continue #might wanna replace as fail
             
             #if pass
            elif result == "Yes":
                sg.popup_ok('Click TVNC to continue')
                continue

        elif event == "TVNC":
            TVNC()
            continue
    
    #return to main
    print(IP)
    return IP

            
def TVNC():
    #lock mouse
    mouse_listener = pynput.mouse.Listener(suppress=True)
    mouse_listener.start()
            
    #open TVNC
    #subprocess.Popen([r'C:\Program Files\TightVNC\tvnviewer.exe'])
    time.sleep(2)
    pyautogui.click(1103, 432) # click Connect
    time.sleep(2)
    mouse_listener.stop() #unlock mouse
    
    # ask if the menu is on
    result = sg.popup_yes_no('Is this screen showing?', image=r"Z:\05. Manufacturing\60. Uncontrolled\Troubleshoot\Dai\MIS Program\727-4248 Programming\Resources\done.png") #replace image
    
    if result == "Yes":
        #ask for the IP address
        sg.popup_no_buttons('Record the IP address on the side. Close this window AFTER record to continue')  
        
        #lock mouse
        mouse_listener = pynput.mouse.Listener(suppress=True)
        mouse_listener.start()  
        
        #continue clicking
        time.sleep(1)
        pyautogui.press('enter')
        pyautogui.click(740, 260)  
        pyautogui.click(740, 390)  # select program
        pyautogui.click(660, 355)  # install program
        time.sleep(1)
        pyautogui.press('enter')
        
        mouse_listener.stop() #unlock mouse
        
        sg.popup_no_buttons('Ignore All of the Error Messages.'
                                '\nExpect the process to take about 4 minutes.'
                                '\nClose the window when the programming is done/fail.', title='VNC Window', text_color='#F7F6F2', keep_on_top=True)
        
        #Check if good or not
        final = sg.popup_yes_no("Does it pass the programming?")
        if final:
            sg.popup_no_buttons("Write the IP into the text box and click Pass to continue")
            return True
        else:
            return False
        
    else:
        sg.popup_no_buttons('Close TVNC\'s error message and click "TVNC" again')



if __name__ == "__main__":
    print("Debug Mode")
    run()