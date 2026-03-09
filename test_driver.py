from selenium import webdriver
from utils.driver_manager import get_driver  # 假设你的函数叫这个

try:
    driver = get_driver()  # 或直接 webdriver.Chrome()
    driver.get("https://www.example.com")
    print("页面标题:", driver.title)
    driver.quit()
except Exception as e:
    print("启动浏览器失败:", type(e).__name__, str(e))