from robocorp.tasks import task
from robocorp import browser 
from RPA.Excel.Files import Files 
from RPA.HTTP import HTTP 
from RPA.PDF import PDF 
import os

@task
def bookstore_data():
    open_website()
    titles=collect_data()
    prices=collect_prices()
    export_excel(titles, prices)
def open_website():
    browser.goto("https://fspacheco.github.io/rpa-challenge/bookstore.html")
def collect_data():
    page=browser.page()
    locator_titles=page.locator("div.book-title").all()
    book_titles=[]
    for loc in locator_titles:
         book_titles.append(loc.text_content())
    return book_titles
def collect_prices():
    page=browser.page()
    locator_prices=page.locator("div.book-price").all()
    book_prices=[]
    for loc in locator_prices:
         book_prices.append(float(loc.text_content().replace("$","")))
    return book_prices
def export_excel(titles, prices):
    excel=Files()
    os.makedirs("./output", exist_ok=True)
    excel.create_workbook(path="./output/books.xlsx",fmt="xlsx",sheet_name="Books")
    excel.append_rows_to_worksheet([["Title","Price"]],name="Books")
    for t,p in zip(titles,prices):
        excel.append_rows_to_worksheet([[t,p]],name="Books")
    excel.auto_size_columns("a",width=50)
    excel.save_workbook()
    excel.close_workbook()
def find_biggest_len(a_list):
    biggest=0
    for item in a_list:
        if len(item)>biggest:
            biggest=len(item)
    return biggest

