from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.common.exceptions import WebDriverException

def get_driver(browser='chrome', headless=False):
    """
    获取浏览器驱动，支持 chrome/firefox/edge
    :param browser: 'chrome', 'firefox', 'edge'
    :param headless: 是否无头模式（默认 False）
    :return: WebDriver 实例
    """
    try:
        if browser.lower() == 'chrome':
            options = ChromeOptions()
            if headless:
                options.add_argument("--headless=new")  # 新版 headless，更稳定
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--disable-gpu")           # Windows 有时需要
            options.add_argument("--window-size=1920,1080") # 推荐代替 maximize_window
            # options.add_argument("--start-maximized")     # 备选

            driver = webdriver.Chrome(options=options)

        elif browser.lower() == 'firefox':
            options = FirefoxOptions()
            if headless:
                options.add_argument("--headless")
            # 可以加更多 firefox 选项

            driver = webdriver.Firefox(options=options)

        elif browser.lower() == 'edge':
            options = EdgeOptions()
            if headless:
                options.add_argument("--headless=new")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")

            driver = webdriver.Edge(options=options)

        else:
            raise ValueError(f"不支持的浏览器类型: {browser}")

        # 统一设置
        driver.implicitly_wait(10)          # 隐式等待 10 秒，推荐
        # driver.maximize_window()          # 如果不用 window-size，可以保留这个
        return driver

    except WebDriverException as e:
        raise RuntimeError(f"浏览器启动失败 ({browser}): {str(e)}") from e
    except Exception as e:
        raise RuntimeError(f"获取驱动时发生未知错误: {str(e)}") from e