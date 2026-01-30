from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def before_all(context):
    print(" 自動化測試開始...")
    chrome_options = Options()

    # --- 關鍵設置 ---
    # 如果要在 Jenkins 後台跑，必須取消下面這行的註釋 (去掉 # 號)
    # chrome_options.add_argument("--headless") 

    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")

    # 啟動瀏覽器
    context.driver = webdriver.Chrome(options=chrome_options)

def after_all(context):
    print(" 測試結束，正在關閉瀏覽器...")
    context.driver.quit()
