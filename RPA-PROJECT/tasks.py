from robocorp.tasks import task
from robocorp import windows
<<<<<<< Updated upstream
from RPA.Desktop.Windows import Desktop
import json
desktop = windows.desktop()
desktop2=Desktop()


@task
def main():
    open_ltspice()
    extract_voltage()
    get_components()

def json_function():
    with open("strings.json") as f:
        d=json.load(f)

def open_ltspice():
    desktop.windows_run(r"C:\apps\ltsipce\LTspice.exe")
    ltspice = windows.find_window('regex:.*LTspice')

    ltspice.send_keys("{Ctrl}o") #open a new file

    #CHANGE THE NEXT 2 LINES SO IT OPENS FROM THE JSON FILE LATER

    ltspice.find("path:1|1|1|4|1|1|2|5").click()#click on Downloads (where the circuit file is located on ur PC so: C:\Users\katie\Downloads for example)
    ltspice.find("path:1|1|1|4|2|1|4|3|1").click()#click on the file
    ltspice.find("path:1|5").click()#click open

    ltspice.set_window_pos(0,0,desktop.width/2,desktop.height)

    ltspice.send_keys("{Alt}{R}")

    ltspice.send_keys("{Ctrl}l")#opens the output log
    ltspice.find("automationid:1178").click() #clicks on the text
    desktop.send_keys("{Ctrl}a")#select all text
    desktop.send_keys("{Ctrl}c")#copies the text
    ltspice.find("automationid:1178").click() #clicks on the text
    ltspice.find("name:Close").click()#this is the path for the x button to close the log window


=======
import time
import os
from robocorp.tasks import task
from RPA.Desktop.Windows import Desktop
desktop2=Desktop()
circuit = r"C:\Users\USER\Documents\LTspice\pmos-switch-circuit-A.asc"
desktop = windows.Desktop()
@task
def main():
    desktop.windows_run(r"C:\Users\USER\AppData\Local\Programs\ADI\LTspice\LTspice.exe")
    open_circuit(circuit)
    run_simulation()
    time.sleep(2)
    screenshot()
    copylog()
    extract_voltage()
def open_circuit(circuit):
    lt = windows.find_window("name:LTspice", search_depth=1)
    lt.send_keys('{Ctrl}o')
    dlg = windows.find_window("regex:.*Open.*", search_depth=2)
    dlg.send_keys( circuit )
    time.sleep(0.1)
    dlg.send_keys('{Enter}')
def run_simulation():
    lt = windows.find_window("name:LTspice - [pmos-switch-circuit-A.asc]", search_depth=1)
    lt.send_keys('{ALT}{R}')
    time.sleep(3)
    lt.send_keys('{CTRL}{L}')
def screenshot():
    lt = windows.find_window("name:LTspice - pmos-switch-circuit-A.asc", search_depth=1)
    lt.screenshot("screenshot.png")
def copylog():
    log_win = windows.find_window("regex:.*SPICE Output Log.*", search_depth=2)
    log_win.send_keys('{Ctrl}a')
    time.sleep(0.1)
    log_win.send_keys('{Ctrl}c')
    time.sleep(0.1)
>>>>>>> Stashed changes

def extract_voltage():
    desktop = windows.Desktop()
    raw_text=desktop2.get_clipboard_value()
<<<<<<< Updated upstream
    row=raw_text.split("\n")[16]
    voltage_string=row.split(" ")[1]
    voltage=voltage_string.split("=")[1]
    print(voltage)

def get_components():
    #if voltage is within approved voltage, this function runs
    BOM_dictionary={}
    desktop=windows.Desktop()
    ltspice = windows.find_window('regex:.*LTspice')

    ltspice.find("name:View").click()
    ltspice.find("name:Bill of Materials").mouse_hover()
    ltspice.find("Paste to clipboard").click()
    bom=desktop2.get_clipboard_value()

    desktop.windows_run('notepad.exe')
    note = windows.find_window("regex:.*Untitled") #CHANGE THIS LATER SO IT OPENS FROM THE JSON FILE
    note.send_keys(bom)
    note.send_keys("{Ctrl}s")

    
    #EXTRACTING THE FIRST PART INFORMATION IN THE LIST
    bom_line_M1=bom.split("\n")[3] #splits the string by new lines and saves the first part information line
    bom_M1=bom_line_M1.split("\t") #splits the first part line by tabs

    #EXTRACTING THE SECOND MATERIAL IN THE LIST
    bom_line_Q1=bom.split("\n")[4] 
    bom_Q1=bom_line_Q1.split("\t") 

    #EXTRACTING THE THIRD MATERIAL IN THE LIST
    bom_line_R1=bom.split("\n")[5] 
    bom_R1=bom_line_R1.split("\t")

    #EXTRACTING THE FOURTH MATERIAL IN THE LIST
    bom_line_R2=bom.split("\n")[6] 
    bom_R2=bom_line_R2.split("\t")
    
    #EXTRACTING THE FIFTH MATERIAL IN THE LIST
    bom_line_R3=bom.split("\n")[7] 
    bom_R3=bom_line_R3.split("\t")

    BOM_dictionary={
                bom_M1[0]:{"Manufacturer:":bom_M1[1],"Part Number:":bom_M1[2]},
                bom_Q1[0]:{"Manufacturer:":bom_Q1[1],"Part Number:":bom_Q1[2]},
                bom_R1[0]:{"Manufacturer:":bom_R1[1],"Part Number:":bom_R1[2]},
                bom_R2[0]:{"Manufacturer:":bom_R2[1],"Part Number:":bom_R2[2]},
                bom_R3[0]:{"Manufacturer:":bom_R3[1],"Part Number:":bom_R3[2]}
    }
    print(BOM_dictionary)
    





=======
    raw_text.split("\n")
    line=raw_text.split("\t")
    voltage=line[3]
    desktop.windows_run('notepad.exe')
    note = windows.find_window("regex:.*Notepad", search_depth=3)
    note.send_keys(voltage)
>>>>>>> Stashed changes
