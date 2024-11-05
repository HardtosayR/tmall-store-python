from time import sleep
import random
from selenium import webdriver    
from selenium.webdriver.common.by import By    #元素定位XPATH
from selenium.webdriver.chrome.service import Service  #负责启动和停止chrome webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from anticaptchaofficial.imagecaptcha import *


DRIVER_PATH = "C:\\Program Files (x86)\\chromedriver.exe"
URL = "https://www.tmall.com/"

"""初始化 Chrome WebDriver, 并设置参数"""
def init_driver(driver_path):
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-automation']) #关闭自动化状态显示
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("--disable-blink-features")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument('--disable-gpu') 
    options.add_argument('--no-sandbox')
    options.add_argument('--ignore-certificate-errors')
    # options.add_argument("--headless")   # 可选，若不需要无头模式可以注释掉
    service = Service(executable_path=driver_path)
    return webdriver.Chrome(service=service, options=options)


driver = init_driver(DRIVER_PATH)
# 设置 Chrome DevTools
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
})
driver.set_window_size(1920,1080)   #全屏打开，可见元素


driver.get(URL)
wait = WebDriverWait(driver, 8)  #设置最长等待时长
sleep(2)
""" account = input("输入账号回车确认：")
password = input("输入密码回车确认：") """
account = '18428167476'
password = 'Xch123456'

def login_handler(acc, pwd):
    try:
        login_element = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@class='h']")))
        login_element.click()
    except Exception as e:
        print(f"首页元素未加载或发生错误: {e}")


    try:
        log_account_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='fm-login-id']")))
        """ for char in acc:
            log_account_input.send_keys(char)
            sleep(random.uniform(0.2, 0.7))
        sleep(random.randint(2,4)) """
        log_account_input.send_keys(acc)
        log_password_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='fm-login-password']")))
        """ for char in pwd:
            log_password_input.send_keys(char)
            sleep(random.uniform(0.2, 0.7)) """
        log_password_input.send_keys(pwd)
    except Exception as e:
        print(f"登录界面元素未加载或发生错误: {e}")

login_handler(account, password)



"""滑条模拟"""
sleep(5)


try:
    #切换到iframe上
    iframe = driver.find_element(By.CSS_SELECTOR, "#baxia-dialog-content")
    driver.switch_to.frame(iframe)
    sleep(2)
    #获取滑块元素40x32
    sour = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "span[class*='btn_slide']"))
    )
    #获取滑块条元素420x32
    """ ele = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".nc-lang-cnt"))
    ) """
except Exception as e:
    print(f"验证界面元素未加载或发生错误: {e}")

sleep(2)

print(f"是否可见：{sour.is_displayed()}")
print(f"滑块宽度：{sour.size['width']}")
# ActionChains(driver).drag_and_drop_by_offset(sour, 200, 0).perform()
target_distance = 378

def generate_slow_slide_path(distance):
    path =[]
    current_position = 0

    #前半段较快，模拟加速
    while current_position < distance * 0.6:
        move = random.randint(2, 4)
        path.append(move)
        current_position += move
    
    # 后半段逐渐减速
    while current_position < distance:
        move = random.randint(1, 3)
        path.append(move)
        current_position += move

    # 最后微调，确保达到精确位置
    if current_position > distance:
        path[-1] -= (current_position - distance)
    
    return path

actions = ActionChains(driver)
actions.click_and_hold(sour).perform()

slide_path = generate_slow_slide_path(target_distance)
for move in slide_path:
    actions.move_by_offset(move, 0).perform()
    sleep(random.uniform(0.1, 0.3))  #随机暂停，模拟人类手动滑动

#释放滑块
actions.release().perform()


input("\nEnter to quit browser...\n")
driver.switch_to.default_content()
driver.quit()
