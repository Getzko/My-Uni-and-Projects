#ltspice automation
from robocorp.tasks import task
from robocorp import windows
import time
import os
'''
desktop = windows.Desktop()
def calc_notes():
    calc=open_calculator()
    calculate(calc,'2+7')
    copy_results(calc)
    notepad=open_notepad()
    paste_results(notepad)
def open_calculator():
    desktop.windows_run("calc.exe")
    calc = windows.find_window("name:Calculator")
    return calc
def calculate(calc,operation):
    calc.send_keys(operation+'=')
def copy_results(app):
    app.send_keys('{Ctrl}c')
def open_notepad():
    desktop.windows_run("notepad.exe")
    notepad = windows.find_window("regex:.*Notepad")
    if notepad is None:
        raise RuntimeError("Could not find Notepad after launching it")
    return notepad
def paste_results(app):
    app.send_keys('{Ctrl}v')
'''
circuit = r"C:\Users\USER\Documents\LTspice\pmos-switch-circuit.asc"
desktop = windows.Desktop()
@task
def main():
    desktop.windows_run(r"C:\Users\USER\AppData\Local\Programs\ADI\LTspice\LTspice.exe")
    open_circuit(circuit)
    run_simulation()
    time.sleep(2)
    screenshot()
    copylog()
def open_circuit(circuit):
    lt = windows.find_window("name:LTspice", search_depth=1)
    lt.send_keys('{Ctrl}o')
    dlg = windows.find_window("regex:.*Open.*", search_depth=2)
    dlg.send_keys( circuit )
    time.sleep(0.1)
    dlg.send_keys('{Enter}')
def run_simulation():
    lt = windows.find_window("name:LTspice - [pmos-switch-circuit.asc]", search_depth=1)
    lt.send_keys('{ALT}{R}')
    time.sleep(1)
    lt.send_keys('{CTRL}{L}')
def screenshot():
    lt = windows.find_window("name:LTspice - pmos-switch-circuit.asc", search_depth=1)
    lt.screenshot("screenshot.png")
def copylog():
    log_win = windows.find_window("regex:.*SPICE Output Log.*", search_depth=3)
    log_win.send_keys('{Ctrl}a')
    time.sleep(0.1)
    log_win.send_keys('{Ctrl}c')
    time.sleep(0.1)
    desktop = windows.Desktop()
    desktop.windows_run('notepad.exe')
    note = windows.find_window("regex:.*Notepad", search_depth=3)
    note.send_keys('{Ctrl}v')