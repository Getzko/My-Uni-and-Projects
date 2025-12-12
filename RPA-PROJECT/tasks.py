from logging import config
from anyio import open_file
from robocorp.tasks import task
from robocorp import browser
from robocorp import windows
from RPA.Desktop.Windows import Desktop
import json
import time

#Place for global variables
desktop = windows.desktop()
desktop2=Desktop()


@task
def main():
    browser.configure(slowmo=500)
    

    open_ltspice()
    
    
    voltage, is_ok=extract_voltage()
    if is_ok:
        component_list=get_components()
    else:
        print("Voltage check failed. Process halted.")

    open_login_odoo(component_list)

def json_function():
    with open("config.json") as f:
        return json.load(f)

def open_ltspice():
    config=json_function()
    desktop.windows_run(config["ltspice"])
    ltspice = windows.find_window('regex:.*LTspice',search_depth=1)
    ltspice.send_keys("{Ctrl}o") #open a new file
    open_file=windows.find_window("regex:.*Open.",search_depth=2)
    open_file.send_keys(config["circuit_a"])
    time.sleep(0.2)
    open_file.send_keys("{Enter}")

    ltspice.set_window_pos(0,0,desktop.width/2,desktop.height)
    ltspice.find("name:Run/Pause").click() #had to change this cuz the alt + r didnt work = the signal panel wasnt showing up
    
    time.sleep(2)
    ltspice.send_keys("{Ctrl}l")#opens the output log
    ltspice.find("automationid:1178").click() #clicks on the text
    desktop.send_keys("{Ctrl}a")#select all text
    desktop.send_keys("{Ctrl}c")#copies the text
    ltspice.find("automationid:1178").click() #clicks on the text
    ltspice.find("name:Close").click()#this is the path for the x button to close the log window

def extract_voltage():
    config=json_function()
    threshold=config["threshold"]
    raw_text=desktop2.get_clipboard_value()
    try:
        row=raw_text.split("\n")[16]
        voltage_string=row.split(" ")[1]
        voltage=float(voltage_string.split("=")[1])
        print(f"Extracted voltage: {voltage}")
        if voltage<=threshold:
            print("Voltage is within approved threshold. Continuing.")
            return voltage, True
        else:
            print("Voltage exceeds approved threshold. Halting process.")
            return voltage, False
    except Exception as e:
        print(f"Error extracting voltage: {e}")
        return None

def get_components():
    #if voltage is within approved voltage, this function runs
    config=json_function()
    BOM_location=config["Bill_of_Materials"]

    BOM_dictionary={}
    ltspice = windows.find_window('regex:.*LTspice')

    ltspice.find("name:View").click()
    ltspice.find("name:Bill of Materials").mouse_hover()
    ltspice.find("Paste to clipboard").click()
    bom=desktop2.get_clipboard_value()

    desktop.windows_run(BOM_location)
    note = windows.find_window("regex:.*BOM_text_file") #CHANGE THIS LATER SO IT OPENS FROM THE JSON FILE
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
                bom_M1[0]:{"Manufacturer:":bom_M1[1],"Part Number:":bom_M1[2],"Name:":bom_M1[3]},
                bom_Q1[0]:{"Manufacturer:":bom_Q1[1],"Part Number:":bom_Q1[2],"Name:":bom_Q1[3]},
                bom_R1[0]:{"Manufacturer:":bom_R1[1],"Part Number:":bom_R1[2],"Name:":bom_R1[3]},
                bom_R2[0]:{"Manufacturer:":bom_R2[1],"Part Number:":bom_R2[2],"Name:":bom_R2[3]},
                bom_R3[0]:{"Manufacturer:":bom_R3[1],"Part Number:":bom_R3[2],"Name:":bom_R3[3]}
    }
    return BOM_dictionary

def open_login_odoo(component_list):
    config=json_function()
    browser.goto(config["odoo_url"])
    page=browser.page()
    page.fill('#login',config["odoo_user"])
    page.fill('#password',config["odoo_pass"])
    time.sleep(1)
    page.click("button:text('Log in')")
    page.wait_for_selector("#result_app_4")
    page.locator("#result_app_4").click() #clicks on "manufacturing"

    page.wait_for_selector("button.fw-normal:nth-child(4) > span:nth-child(1)")
    page.locator("button.fw-normal:nth-child(4) > span:nth-child(1)").click() #clicks on "products" dropdown menu
    page.locator(".o_popover > a:nth-child(1)").click() #clicks on "Products"

    page.locator("button:text('New')").click()
    page.locator("#name_0").fill(config["circuit_a_name"])#gets the first part's name
    page.locator(".o_form_button_save").click()#saves the part

    page.locator(".o_menu_brand").click()#goes back to main page
    page.wait_for_selector("#result_app_4")
    page.locator("#result_app_4").click() #clicks on "manufacturing"
    page.wait_for_selector("button.fw-normal:nth-child(4) > span:nth-child(1)")
    page.locator("button.fw-normal:nth-child(4) > span:nth-child(1)").click() #clicks on "products" dropdown menu
    page.locator("a.o-dropdown-item:nth-child(2)").click()#clicks on "Bill of Materials" 

    page.locator("button:text('New')").click() #clicks on "New"
    page.locator("#product_tmpl_id_0").fill(config["circuit_a_name"])#fills in the circuit name form the json file
    desktop.send_keys("{Enter}")#saves the name


    
    for ref, data in component_list.items():
        print(f"Adding {ref}: {data['Manufacturer:']} {data['Part Number:']}")

        page.locator(".o_field_x2many_list_row_add > a:nth-child(1)").click() #click add new line
        desktop.send_keys(data["Manufacturer:"])#fills in "Manufacturer"
        desktop.send_keys(" ")
        desktop.send_keys(data["Part Number:"])#fills in "Part NUmber"
        desktop.send_keys("{Enter}")
        page.locator(".o_form_button_save").click()#saves the Bill of Materials

    page.locator("button.fw-normal:nth-child(2)").click() #clicks on Operations
    page.locator("a:text('Manufacturing Orders')").click()#clicks on Manufacturing Orders
    page.locator("button:text('New')").click()#clicks on new
    page.locator("#product_id_0").fill(config["circuit_a_name"])#names the new order from the json file
    desktop.send_keys("{Enter}")

    page.locator("#product_qty_0").fill(config["quantity_to_manufacture_A"])#sets the quantity from the json file
    page.locator(".o_form_button_save").click()# saves the order
    page.screenshot(path=".output\manufacturing_order.png") #takes a screenshot of the manufacturing order
    time.sleep(5)

