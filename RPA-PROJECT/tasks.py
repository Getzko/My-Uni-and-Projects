from robocorp.tasks import task

@task
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