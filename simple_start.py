from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions


#去除webdriver一些特征
option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
option.add_argument("--disable-blink-features")
option.add_argument("--disable-blink-features=AutomationControlled")
option.add_argument("--headless")
# 设置Chrome驱动
driver = Chrome(options=option)

# 打开天猫店铺页面
url = 'https://shop59996859.taobao.com/?spm=a230r.7195193.1997079397.28.591551f0oWOTfE'
driver.get(url)

# 等待手动登录
input("请手动登录天猫账号，然后按Enter继续...")

# 等待页面加载完成
time.sleep(8)  # 根据网络速度调整等待时间

# 根据页面结构获取店铺名称（替换成实际的class名称）
try:
    shop_name = driver.find_element(By.CLASS_NAME,'shopName--qijIco3R').text 
    print(f"店铺名称: {shop_name}")
except Exception as e:
    print("未找到店铺名称，可能需要调整选择器。", e)

# 关闭浏览器
driver.quit()
