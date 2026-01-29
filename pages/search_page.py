from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchPage:
    # Bilibili 的首頁地址
    URL = "https://www.bilibili.com"

    # 定位器 (Locators) - 這些是 Bilibili 頁面上的元素特徵
    # 注意：如果 B站 改版，這裡可能需要更新
    SEARCH_INPUT = (By.CLASS_NAME, "nav-search-input") 
    SEARCH_BUTTON = (By.CLASS_NAME, "nav-search-btn")

    def __init__(self, driver):
        self.driver = driver

    # 動作：打開首頁
    def open(self):
        self.driver.get(self.URL)

    # 動作：輸入關鍵詞
    def input_keyword(self, keyword):
        # 顯式等待：最多等 10 秒，直到輸入框出現
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.SEARCH_INPUT)
        )
        element.clear()
        element.send_keys(keyword)

    # 動作：點擊搜索
    def click_search(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SEARCH_BUTTON)
        )
        element.click()

    # 動作：獲取標題
    def get_title(self):
        return self.driver.title
