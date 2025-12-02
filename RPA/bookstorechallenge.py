from robocorp.tasks import task
from robocorp import browser 
from RPA.Excel.Files import Files 
from RPA.HTTP import HTTP 
from RPA.PDF import PDF 
import os
@task
def findbook():
    openpage()
    search()
    titles = collectbookdata()
    prices = collectbookprices()
    exportexcel(titles, prices)
    highlightunderprice(prices, x=15.0)
    highlightcheapest(prices)
    print(titles)
    print(prices)

def openpage():
    browser.goto("https://www.suomalainen.com")
    page=browser.page()
    page.wait_for_selector("button:text('Hyväksy kaikki')", timeout=3000)
    page.click("button:text('Hyväksy kaikki')")
def search():
    page = browser.page()
    page.wait_for_selector("#header-nav-search")
    page.fill("#header-nav-search", "Andrzej Sapkowski")
    page.click("button[type='submit']")
    page.wait_for_selector("p.ais-hit--title")
def collectbookdata():
    page=browser.page()
    locator_titles=page.locator("p.ais-hit--title").all()
    book_titles=[]
    for loc in locator_titles:
        book_titles.append(loc.text_content())
    return book_titles
def collectbookprices():
    page=browser.page()
    locator_prices=page.locator("p.price.ais-hit--price").all()
    book_prices=[]
    for loc in locator_prices:
            raw = loc.text_content().replace("€", "").replace(",", ".").strip()
            book_prices.append(float(raw))
    return book_prices
def exportexcel(titles, prices):
    excel=Files()
    excel.create_workbook(path="./output/librarybooks.xlsx",fmt="xlsx",sheet_name="Books")
    excel.append_rows_to_worksheet([["Title","Price"]],name="Books")
    for t,p in zip(titles,prices):
        excel.append_rows_to_worksheet([[t,p]],name="Books")
    excel.auto_size_columns("a",width=50)
    excel.save_workbook()
    excel.close_workbook()
def highlightcheapest(prices):
    excel = Files()
    excel.open_workbook(path="./output/librarybooks.xlsx")
    cheapest = min(prices)
    for idx, price in enumerate(prices):
        if price == cheapest:
            row = idx + 2
            excel.set_styles(f"A{row}:B{row}", cell_fill="#ff1616", bold=True)
    excel.save_workbook()
    excel.close_workbook()
def highlightunderprice(prices, x=15.0):
    excel = Files()
    excel.open_workbook(path="./output/librarybooks.xlsx")
    for idx, price in enumerate(prices):
            if price < x:
                row = idx + 2
                excel.set_styles(f"A{row}:B{row}", cell_fill="#FFF2CC", bold=True)
    excel.save_workbook()
    excel.close_workbook()
                            