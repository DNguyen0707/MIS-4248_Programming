#!/usr/bin/env python3

# import packages
import pyautogui
import PySimpleGUI as sg
import subprocess
from datetime import datetime
import time
from pathlib import Path

#import test module
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
testModule_path = os.path.join(current_dir, "Test_Modules")
sys.path.append("Test_Modules")

sg.set_options(font=('Arial Bold', 16))

image_viewer_column = [
    [sg.Text("Programming Step's Detail:", )],
    [sg.Text(size=(40, 1), key="TOUT")],
    [sg.Image(key="-IMAGE-")],
    [sg.Text('General Requirement: ', size=(27, 1)), sg.Text(key='GR')],
    [sg.Text('Test Setup: ', size=(27, 1)), sg.Text(key='TS')],
    [sg.Text('Recover win & VNC Right Carrier: ', size=(27, 1)), sg.Text(key='T1')],
    [sg.Text('Recover win & VNC Left Carrier: ', size=(27, 1)), sg.Text(key='T2')],
    [sg.Text('Putty Setup Right Carrier Result: ', size=(27, 1)), sg.Text(key='T3')],
    [sg.Text('Putty Setup Left Carrier Result: ', size=(27, 1)), sg.Text(key='T4')],
    [sg.Text('Collect Report Result: ', size=(27, 1)), sg.Text(key='T5')],
    [sg.Text('Disassemble DUTs Result: ', size=(27, 1)), sg.Text(key='T6')],
    [sg.Text('Final Result: ', size=(27, 1)), sg.Text(key='T7')]
]

functional_step_column = [
    [sg.Text('Operator Name: ', size=(22, 1)), sg.Combo(['Phat Huynh', 'Anh Phan', 'Tung Hong','Dai Nguyen'], default_value='', key='operator')],
    [sg.Text('Left Carrier Serial Number: ', size=(22, 1)), sg.InputText(size=(10, 1))],
    [sg.Text('Right Carrier Serial Number: ', size=(22, 1)), sg.InputText(size=(10, 1))],
    [sg.Text('System Serial Number: ', size=(22, 1)), sg.Text(key='-SS-')],
    [sg.Text('Date: ', size=(22, 1)), sg.Text(key='-DT-')], 
]

# Full Layout
layout = [
    [sg.Text('727-4248 CARRIER BOARDS PROGRAMMING TEST', font=('Arial Bold', 20), size=20, expand_x=True, justification='center')],
    [sg.Column(functional_step_column),
     sg.VSeperator(),
     sg.Column(image_viewer_column)],
    [sg.Text('Enter Operator and Serial Number information then Press Start to begin the Test.')],
    [sg.Text('(If you are not in the list of Operator Name, please contact Engineer for training)')],
    [sg.Button("Start"), sg.Exit()]
]

# Create the window
window = sg.Window("727-4248 Programming Test", layout, size=(980, 560), enable_close_attempted_event=True)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT and sg.popup_yes_no('Do you really want to exit?') == 'Yes':
        break
    if event == sg.WIN_CLOSED or event == 'Exit' and sg.popup_yes_no('Do you really want to exit?') == 'Yes':
        break
    if event == "Start":
        # Collect and update info
        snl = values[0]
        snr = values[1]
        carr = snl + '-' + snr
        window['-SS-'].update(carr)
        date = datetime.now().strftime('%H:%M:%S %m/%d/%y')
        window['-DT-'].update(date)
        
        #check for correct information
        if values['operator'] == '':
            sg.popup_no_buttons('Operator name is blank. Please try again by re-running the 727-4248.py', title='Front Page', text_color='#F7F6F2', keep_on_top=True)
            break
        elif snr == '':
            sg.popup_no_buttons('Serial Number of Right Carrier is blank. Please try again by re-running the 727-4248.py', title='Front Page', text_color='#F7F6F2', keep_on_top=True)
            break
        elif snl == '':
            sg.popup_no_buttons('Serial Number of Left Carrier is blank. Please try again by re-running the 727-4248.py', title='Front Page', text_color='#F7F6F2', keep_on_top=True)
            break
        
        #clear board
        window["GR"].update("")
        window["TS"].update("")
        window["T1"].update("")
        window["T2"].update("")
        window["T3"].update("")
        window["T4"].update("")
        window["T5"].update("")
        window["T6"].update("")
        window["T7"].update("")

        
        #import test module
        import Setup
        import RecoverCarrier
        import PuttySetup
        import CollectReport
        import Disassemble
        
        #start setup
        if Setup.run(carr):
            window["GR"].update("Pass")
            window["TS"].update("Pass")
        else:
            sg.popup_ok("Functional Test Failed")
        
        #Recover Right (0) Carrier 
        RightIP = RecoverCarrier.run()
        if RightIP:
            window["T1"].update("Pass")
        else:
            sg.popup_ok("Functional Test Failed")
        
        #Move to the left
        sg.popup_ok("Move on to the the Left Carrier. Close the Window to continue")
        
        #Recover Left (1) Carrier
        LeftIP = RecoverCarrier.run()
        if LeftIP:
            window["T2"].update("Pass")
        else:
            sg.popup_ok("Functional Test Failed")
        
        #Putty Setup for both
        if PuttySetup.run(snr, snl, RightIP, LeftIP):
            window["T3"].update("Pass")
        else:
            sg.popup_ok("Functional Test Failed")
            
        #Collect info in WinSCP
        if CollectReport.run(RightIP, LeftIP, carr):
            window["T5"].update("Pass")
        else:
            sg.popup_ok("Functional Test Failed")
        
        #Disassemble        
        if Disassemble.run():
            window["T6"].update("Pass")
        else:
            sg.popup_ok("Functional Test Failed")
        
        sg.popup_ok("Functional Test Passed")
        window["T7"].update("Pass")