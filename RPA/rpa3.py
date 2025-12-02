from robocorp.tasks import task
from robocorp import browser 
from RPA.Excel.Files import Files 
from RPA.HTTP import HTTP 
from RPA.PDF import PDF
from robocorp import log 
import os

@task

def test_site():
    open_website()
    check_cart()
    check_sort()
    check_search()

def open_website():
    browser.goto("https://fspacheco.github.io/rpa-challenge/kirjakauppa.html")

def check_cart():
    page=browser.page()
    page.locator('#booksContainer > div:nth-child(1) > button').click()
    cart_items=page.locator('#cart-info>span').text_content()
    page.screenshot(path="./output/cart_items.png")
    if cart_items=="1":
        log.console_message("alles gut",'task_name')
    else:
        log.console_message(f'nein nein {cart_items} items in cart, expected 1','task_name')

def check_sort():
    page=browser.page()
    page.locator('#sortSelect').select_option('price')
    _, prices=collect_data()
    if prices == sorted(prices):
        log.console_message("Sorting works",'task_name')
    else:
        log.console_message(f"Sorting broken {prices}\n",'error')

def collect_data():

    page=browser.page()
    locator_titles=page.locator("div.kirjan-nimi").all()
    book_titles=[]
    for loc in locator_titles:
            book_titles.append(loc.text_content())
    locator_prices=page.locator("div.hinta").all()
    book_prices=[]
    for loc in locator_prices:
            book_prices.append(float(loc.text_content().replace("$","").replace(",",".")))
    return book_titles, book_prices

def check_search():
    page=browser.page()
    page.locator('#searchInput').fill('python')
    visible_titles=page.locator('esine:visible').all()
    print(visible_titles)
    visible_titles=[]
    for loc in visible_titles:
        visible_titles.append(loc.locator('kirjan-nimi').text_content())

    print(visible_titles)
    if visible_titles==['Python for Beginners']:
        log.console_message("Search works",'task_name')
    else:
        log.console_message(f"Search broken {visible_titles}\n",'error')









