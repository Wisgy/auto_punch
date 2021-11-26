#此脚本需挂在学校虚拟机中一直执行
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# 只需修改下面三项即可 学号 密码 打卡网址
username = "username"
password = "password"
url1 = "https://weixine.ustc.edu.cn/2020/home"

# 下面是每次填报的时候几个需要填写的地方，F12找到这些位置的 full XPath
login="/html/body/div[1]/div/div[3]/div[2]/a"
userxpath="/html/body/div/div/div[3]/form/div[1]"
reportid="report-submit-btn-a24"

# 模拟登陆打卡
def do_login(driver):
    #选择登录界面
    driver.find_element(By.XPATH,login).click()#统一身份认证登录
    time.sleep(1)
    #登录界面
    new=driver.current_window_handle
    driver.switch_to.window(new)
    driver.find_element(By.NAME,'username').send_keys(username,Keys.TAB,password)#学号密码
    driver.find_element(By.ID,"login").click()  # 点击登录
    time.sleep(1)
    #进入打卡页面
    new = driver.current_window_handle
    driver.switch_to.window(new)
    driver.find_element(By.ID,reportid).click()#确认上报

if __name__ == '__main__':
    while(1):
        # 模拟浏览器打开网站
        try:
            driver = webdriver.Firefox()
            driver.get(url1)
            # 登录并打卡
            do_login(driver)
            driver.close()
            driver.quit()
            print("打卡成功")
            time.sleep(86400)#间隔一天打卡
        except Exception:
            print("打卡失败")#重新打卡
            time.sleep(1)