#此脚本需挂在学校虚拟机中一直执行
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# 只需修改下面三项即可 学号 密码 打卡网址
username = "username"
password = "password"
url1 = "https://weixine.ustc.edu.cn/2020/home"
url2 = "https://weixine.ustc.edu.cn/2020/apply/daliy"

# 模拟登录报备
def do_report(driver):
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div[2]/a').click()  # 统一身份认证登录
    # 登录界面
    driver.switch_to.window(driver.current_window_handle)
    driver.find_element(By.NAME, 'username').send_keys(username, Keys.TAB, password)  # 学号密码
    driver.find_element(By.ID, "login").click()  # 点击登录
    time.sleep(2)
    driver.get(url2)
    input1=driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[2]/div[2]/form/div/div[2]/div/label[3]/input')
    ActionChains(driver).move_to_element(input1).click(input1).perform()
    driver.find_element(By.ID,'confirm-report-hook').click()
    driver.find_element(By.XPATH,'//*[@id="report-submit-btn"]').click()
    time.sleep(2)
    input2=driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[2]/div[2]/form/div/div[4]/div/label[2]/i')
    input3=driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div[2]/form/div/div[4]/div/label[5]/i')
    ActionChains(driver).move_to_element(input2).click(input2).perform()
    ActionChains(driver).move_to_element(input3).click(input3).perform()
    driver.find_element(By.XPATH,'//*[@id="report-submit-btn"]').click()

if __name__ == '__main__':
    while(1):
        # 模拟浏览器打开网站
        try:
            driver = webdriver.Firefox()
            driver.get(url1)
            # 登录并打卡
            do_report(driver)
            driver.close()
            driver.quit()
            print("报备成功")
            time.sleep(86396)#间隔一天打卡
        except Exception:
            print("报备失败")#重新打卡
            time.sleep(1)