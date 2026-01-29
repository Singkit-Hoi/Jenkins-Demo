from behave import *
from pages.search_page import SearchPage
import time

@given('我打開了 Bilibili 首頁')
def step_open_homepage(context):
    context.page = SearchPage(context.driver)
    context.page.open()

@when('我在搜索框輸入 "{keyword}"')
def step_input_keyword(context, keyword):
    context.page.input_keyword(keyword)

@when('我點擊搜索按鈕')
def step_click_search(context):
    context.page.click_search()
    time.sleep(2)
    windows = context.driver.window_handles
    context.driver.switch_to.window(windows[-1])

@then('頁面標題應該包含 "{text}"')
def step_check_title(context, text):
    time.sleep(2)
    title = context.page.get_title()
    print(f"當前頁面標題是: {title}")
    assert text in title
