from datetime import datetime  # to get today date
import PySimpleGUI as sg  # GUI window
from pathlib import Path  # make folder
import pyautogui as pyautogui  # to screenshot monitor

def run(carr = "000000-000000"):
    #Set font
    sg.set_options(font=('Arial Bold', 14))
    
    #Image Location
    imageREQ = "Z:/05. Manufacturing/60. Uncontrolled/Troubleshoot/Phat/MIS/727-4248/req.png"
    imageSETUP1 = "Z:/05. Manufacturing/60. Uncontrolled/Troubleshoot/Phat/MIS/727-4248/set1.png"
    imageSETUP2 = "Z:/05. Manufacturing/60. Uncontrolled/Troubleshoot/Phat/MIS/727-4248/set2.png"
    imageSETUP3 = "Z:/05. Manufacturing/60. Uncontrolled/Troubleshoot/Phat/MIS/727-4248/set2-1.png"
    imageSETUP4 = "Z:/05. Manufacturing/60. Uncontrolled/Troubleshoot/Phat/MIS/727-4248/set3.png"
    
    Layout = [
        [sg.Image(filename=imageREQ, key="ImageBoard")],
        [sg.Text('Click next when finish reading carefully')],
        [sg.Button("Next"), sg.Button("Back"), sg.Exit()]
    ]

    window = sg.Window('Requirement and Setup', Layout, size=(1000,900), enable_close_attempted_event=True)
    imageNum = 0
    
    while True:
        event, values = window.read()
        
        if event == sg.WIN_CLOSED or event == 'Exit':
            return False
        elif event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT:
            return False
        elif event == "Next":
            match imageNum:
                case 0:
                    window['ImageBoard'].update(filename=imageSETUP1, visible=True)
                    window.refresh()
                    
                    imageNum = 1
                case 1:
                    window['ImageBoard'].update(filename=imageSETUP2, visible=True)
                    window.refresh()
                    imageNum = 2
                case 2:
                    window['ImageBoard'].update(filename=imageSETUP3, visible=True)
                    window.refresh()
                    imageNum = 3
                case 3:
                    window['ImageBoard'].update(filename=imageSETUP4, visible=True)
                    window.refresh()
                    imageNum = 4
                case 4:
                    window.close
                    
                    # Create a folder for that
                    Path("Z:/05. Manufacturing/20. Test/400 records/Test Records/727/727-4251/" + carr).mkdir(parents=True, exist_ok=True)

                    return True
        elif event == "Back":
            match imageNum:
                case 0:
                    sg.popup_no_buttons("You're at the first image")
                    
                case 1:
                    window['ImageBoard'].update(filename=imageREQ, visible=True)
                    window.refresh()
                    imageNum = 0
                    
                case 2:
                    window['ImageBoard'].update(filename=imageSETUP1, visible=True)
                    window.refresh()
                    imageNum = 1
                    
                case 3:
                    window['ImageBoard'].update(filename=imageSETUP2, visible=True)
                    window.refresh()
                    imageNum = 2
                    
                case 4:
                    window['ImageBoard'].update(filename=imageSETUP3, visible=True)
                    window.refresh()
                    imageNum = 3
                    


if __name__ == "__main__":
    print("Debug Mode")
    run()