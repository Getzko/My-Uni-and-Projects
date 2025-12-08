from robocorp.tasks import task
from robocorp import windows
<<<<<<< Updated upstream
from RPA.Desktop.Windows import Desktop
desktop = windows.desktop()
desktop2=Desktop()


@task
def main():
    open_ltspice()
    extract_voltage()



def open_ltspice():
    desktop.windows_run(r"C:\apps\ltsipce\LTspice.exe")
    ltspice = windows.find_window('regex:.*LTspice')

    ltspice.send_keys("{Ctrl}o") #open a new file
    ltspice.find("path:1|1|1|4|1|1|2|5").click()#click on Downloads (where the circuit file is located on my PC)
    ltspice.find("path:1|1|1|4|2|1|4|3|1").click()#click on the file
    ltspice.find("path:1|5").click()#click open

    ltspice.set_window_pos(0,0,desktop.width/2,desktop.height)

    ltspice.send_keys("{Alt}{R}")

    ltspice.send_keys("{Ctrl}l")#opens the output log
    ltspice.find("automationid:1178").click() #clicks on the text
    desktop.send_keys("{Ctrl}a")#select all text
    desktop.send_keys("{Ctrl}c")#copy the text


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
    print(row)
    voltage_string=row.split(" ")[1]
    voltage=voltage_string.split("=")[1]
    desktop.windows_run('notepad.exe')
    note = windows.find_window("regex:.*Untitled")
    note.send_keys(voltage)






=======
    raw_text.split("\n")
    line=raw_text.split("\t")
    voltage=line[3]
    desktop.windows_run('notepad.exe')
    note = windows.find_window("regex:.*Notepad", search_depth=3)
    note.send_keys(voltage)
>>>>>>> Stashed changes
