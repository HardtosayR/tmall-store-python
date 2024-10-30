import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# 配置 ChromeDriver 路径
DRIVER_PATH = "D:\\ChromeDriver\\chromedriver-win32\\chromedriver-win32\\chromedriver.exe"
SHOP_URL = 'https://shop59996859.taobao.com/?spm=a230r.7195193.1997079397.28.591551f0oWOTfE'

def init_driver(driver_path):
    """初始化 Chrome WebDriver，并设置参数"""
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_argument("--disable-blink-features")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--headless")  # 可选，若不需要无头模式可以注释掉
    service = Service(executable_path=driver_path)
    return webdriver.Chrome(service=service, options=options)

def get_shop_name(driver, url):
    """打开页面并获取店铺名称"""
    driver.get(url)
    time.sleep(8)  # 根据需要调整等待时间
    try:
        shop_name = driver.find_element(By.CLASS_NAME, 'shopName--qijIco3R').text
        print(f"店铺名称: {shop_name}")
    except Exception as e:
        print("未找到店铺名称，可能需要调整选择器。", e)

def main():
    driver = init_driver(DRIVER_PATH)
    try:
        get_shop_name(driver, SHOP_URL)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
