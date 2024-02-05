# MIS-4248 Programming

### Notes
- Create a txt file that save the operator name, program date, ip address of left and right carrier. Do this in Setup.py
- Keep left first then right

## Test steps

### General Setup
- Keep the same

### Test Setup
- Add back/next button to change photos, keep the same window if possible

### Recover win & VNC Right (and Left) carrier
- Keep the same set up picture
- Make sure to have a window that let you click start to boot up the recovery-window
- Add button for VNC automation, wait till VNC boot up, and let user add IP address, then button to click next
    - somehow make it so that the pc can just hijack the mouse completely and not let the user control it
    - Make sure to have a way to ESC
- Show the same disassemble image and move to left if click "pass"
- In the same .py but show 2 different windows
- Show the window that tell the op to turn on both carrier and click pass if led on

### Putty Setup - Right (and Left) 
- Remove telling op to go into file. Open the file itself
- Remove telling op to input IP address because already done it in last step
- Make a window that let the op start the automation themselves for right and left
    - Add for SSID and Password in the same window
    - Screenshot the new terminal instead of using the old one
- For left bollard:
    - Ask for the hidden wifi once (add a paste button)
    - Allows the user to click restart the automation if fail to connect to right bollard
    - Skip "services" since the address will always be the same
    - Remember to add "exit" for left bollard

### Collect Report
- Create new window showing both left and right
- Automatically know where the folder is at
- Double click local address bar (far right corner) and type the folder address in
- Connect into the carrier before copying
    - Save the address and type it in once connected into the carrier
- Popup the picture telling op to check the .conf file
- Click pass if all the file is right
    - Shut off WinSCP afterward


### Disassemble DUTs
- Keep the same

### Final Test Result
- Keep the same