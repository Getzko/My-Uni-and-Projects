# 4/3 EXERCISE FOR RPA THIS IS great
from robocorp.tasks import task
from robocorp import browser
import time

URL_V1 = "https://fspacheco.github.io/rpa-challenge/factory-inventory-system-v1.html"
BATCH_COUNTER = 0
PASSED = 0
FAILED = 0

def gen_batch():
    global BATCH_COUNTER
    BATCH_COUNTER += 1
    return f"BATCH-{BATCH_COUNTER}"

def open_site(url):
    browser.configure(slowmo=50)
    browser.goto(url)
    page = browser.page()
    try:
        page.evaluate("localStorage.clear()")
    except:
        pass
    page.reload()
    page.wait_for_timeout(200)
    return page

def add_item(page, item):
    page.fill("#partName", str(item["name"]))
    page.fill("#quantity", str(item["qty"]))
    page.fill("#batchNumber", str(item["batch"]))
    page.fill("#location", str(item["location"]))
    page.fill("#reorderThreshold", str(item["threshold"]))
    page.click("button:has-text('Add Item')")
    # wait for the row with the batch to appear (or timeout)
    try:
        page.wait_for_selector(f"tbody tr:has-text('{item['batch']}')", timeout=3000)
    except:
        page.wait_for_timeout(300)

def find_row_by_batch(page, batch):
    try:
        locator = page.locator(f"tbody tr:has-text('{batch}')")
        if locator.count() > 0:
            return locator.nth(0)
    except:
        pass
    return None

def count_rows_with_batch(page, batch):
    try:
        rows = page.locator("tbody tr")
        c = 0
        for i in range(rows.count()):
            try:
                if batch in rows.nth(i).text_content():
                    c += 1
            except:
                pass
        return c
    except:
        return 0

def print_pass(version, test):
    global PASSED
    PASSED += 1
    print(f"{version}: PASS - {test}")

def print_fail(version, test, info=""):
    global FAILED
    FAILED += 1
    print(f"{version}: FAIL - {test} {info}")

def test_view_items(page, version, a, b):
    r1 = find_row_by_batch(page, a["batch"])
    r2 = find_row_by_batch(page, b["batch"])
    if r1 and a["name"] in r1.text_content() and r2:
        print_pass(version, "View items in table")
    else:
        print_fail(version, "View items in table", "(items missing)")

def test_add_valid(page, version, item):
    add_item(page, item)
    if find_row_by_batch(page, item["batch"]):
        print_pass(version, "Add item with valid quantities")
    else:
        print_fail(version, "Add item with valid quantities")

def test_batch_unique(page, version, item):
    add_item(page, {"name":"dup-test","qty":"10","batch":item["batch"],"location":"Z","threshold":"1"})
    matches = count_rows_with_batch(page, item["batch"])
    if matches == 1:
        print_pass(version, "Batch numbers must be unique")
    else:
        print_fail(version, "Batch numbers must be unique", f"(found {matches})")

def test_update(page, version, item):
    row = find_row_by_batch(page, item["batch"])
    if not row:
        print_fail(version, "Update quantity", "(row not found)")
        return
    try:
        inp = row.locator("input[id^='updateQty-']")
        inp.fill("500")
        row.locator("button:has-text('Update')").click()
        # wait for update to reflect
        page.wait_for_timeout(300)
    except:
        print_fail(version, "Update quantity", "(edit failed)")
        return
    row2 = find_row_by_batch(page, item["batch"])
    if row2 and "500" in row2.text_content():
        print_pass(version, "Update quantity")
    else:
        print_fail(version, "Update quantity", "(value not updated)")

def test_delete(page, version, item):
    row = find_row_by_batch(page, item["batch"])
    if not row:
        print_fail(version, "Delete item", "(row not found)")
        return
    try:
        page.once("dialog", lambda d: d.accept())
        row.locator("button:has-text('Delete')").click()
        # wait a bit for removal
        page.wait_for_timeout(300)
    except:
        print_fail(version, "Delete item", "(delete failed)")
        return
    if find_row_by_batch(page, item["batch"]) is None:
        print_pass(version, "Delete item")
    else:
        print_fail(version, "Delete item", "(still exists)")

def test_low_stock(page, version, item):
    row = find_row_by_batch(page, item["batch"])
    if not row:
        print_fail(version, "Low stock test", "(row not found)")
        return
    if "LOW STOCK" in row.text_content().upper():
        print_pass(version, "Low stock when qty <= threshold")
    else:
        print_fail(version, "Low stock when qty <= threshold")

def test_not_low_stock(page, version, item):
    row = find_row_by_batch(page, item["batch"])
    if not row:
        print_fail(version, "No low stock test", "(row not found)")
        return
    if "LOW STOCK" not in row.text_content().upper():
        print_pass(version, "No low stock when qty > threshold")
    else:
        print_fail(version, "No low stock when qty > threshold")

def test_dashboard_total(page, version):
    try:
        table_rows = page.locator("tbody tr").count()
    except:
        table_rows = 0
    try:
        ui = page.locator("#totalItems").inner_text().strip()
    except:
        ui = "?"
    if str(table_rows) == ui:
        print_pass(version, "Dashboard total item count")
    else:
        print_fail(version, "Dashboard total item count", f"(UI={ui}, actual={table_rows})")

def test_dashboard_low(page, version):
    rows = page.locator("tbody tr").all()
    actual_low = 0
    for i in range(len(rows)):
        try:
            if "LOW STOCK" in rows[i].text_content().upper():
                actual_low += 1
        except:
            pass
    try:
        ui = page.locator("#lowStockItems").inner_text().strip()
    except:
        ui = "?"
    if str(actual_low) == ui:
        print_pass(version, "Dashboard low stock count")
    else:
        print_fail(version, "Dashboard low stock count", f"(UI={ui}, actual={actual_low})")

def test_search_exact(page, version, item):
    page.fill("#searchInput", "")
    page.fill("#searchInput", item["name"])
    page.wait_for_timeout(200)
    rows = page.locator("tbody tr").count()
    if rows == 1:
        print_pass(version, "Search exact match")
    else:
        print_fail(version, "Search exact match", f"(Found {rows})")

def test_search_partial(page, version, item):
    page.fill("#searchInput", "")
    keyword = item["name"][:3]
    page.fill("#searchInput", keyword)
    page.wait_for_timeout(200)
    rows = page.locator("tbody tr").all()
    found = False
    for r in rows:
        try:
            if item["name"] in r.text_content():
                found = True
                break
        except:
            pass
    if found:
        print_pass(version, "Search partial match")
    else:
        print_fail(version, "Search partial match")

def test_search_case_insensitive(page, version, item):
    page.fill("#searchInput", "")
    page.fill("#searchInput", item["name"].upper())
    page.wait_for_timeout(200)
    rows = page.locator("tbody tr").all()
    found = False
    for r in rows:
        try:
            if item["name"].lower() in r.text_content().lower():
                found = True
                break
        except:
            pass
    if found:
        print_pass(version, "Search case-insensitive")
    else:
        print_fail(version, "Search case-insensitive")

def run_tests_for(url, version):
    page = open_site(url)

    item1 = {"name":"Tubes","qty":"1000","batch":gen_batch(),"location":"Zone A","threshold":"500"}
    item2 = {"name":"wood screws","qty":"10000","batch":gen_batch(),"location":"Zone B","threshold":"5000"}
    item3 = {"name":"wheels","qty":"100","batch":gen_batch(),"location":"Zone C","threshold":"20"}

    add_item(page, item1)
    add_item(page, item2)

    test_view_items(page, version, item1, item2)
    test_add_valid(page, version, item3)
    test_batch_unique(page, version, item3)
    test_update(page, version, item2)
    test_delete(page, version, item1)
    test_low_stock(page, version, item2)
    test_not_low_stock(page, version, item3)
    test_dashboard_total(page, version)
    test_dashboard_low(page, version)
    test_search_exact(page, version, item2)
    test_search_partial(page, version, item1)
    test_search_case_insensitive(page, version, item3)

    print(f"{version}: TEST RUN COMPLETE")

@task
def main():
    global PASSED, FAILED
    PASSED = 0
    FAILED = 0
    run_tests_for(URL_V1, "V1")
    print(f"SUMMARY: Passed: {PASSED} | Failed: {FAILED}")
