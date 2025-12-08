from robocorp.tasks import task
from robocorp import windows
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



def extract_voltage():
    desktop = windows.Desktop()
    raw_text=desktop2.get_clipboard_value()
    row=raw_text.split("\n")[16]
    print(row)
    voltage_string=row.split(" ")[1]
    voltage=voltage_string.split("=")[1]
    desktop.windows_run('notepad.exe')
    note = windows.find_window("regex:.*Untitled")
    note.send_keys(voltage)






