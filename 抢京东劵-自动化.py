from selenium import webdriver
import datetime
import time

options = webdriver.ChromeOptions()
options.add_argument('--log-level=3')

# 创建浏览器对象
driver = webdriver.Chrome(chrome_options=options)
# 窗口最大化显示
driver.maximize_window()

url = "https://pro.jd.com/mall/active/TT9s9JigEyqGXyn8VUN9sSzzLq8/index.html"
driver.get(url)
driver.implicitly_wait(10)
time.sleep(1)

# 找到并点击淘宝的登陆按钮
driver.find_element_by_link_text("你好，请登录").click()

print("请在30秒内完成登录")
# 用户扫码登陆
time.sleep(20)

# "立即领取40元优惠券"的css_selector
btn_buy = "['data-cpid='CC4F462FF17611DD74637C66C334FB31_babel','div class'='use_mask','div class'='use_btn']"
#“关闭按钮”的css_selector
btn_close = ".close-button"
#抢购时间，尽量设置的靠前一点，比如提前1分钟，如10：00开奖，那就设置为09：59
time = "2020-11-04 17:59:58"

a = 0
while True:
    print("领取还未开始")
    if datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') > buy_time:
        print("即将开始领取")
        # 找到“立即领取”，点击
        time.sleep(0.0)
        if driver.find_element_by_css_selector(btn_buy):
            while True:
                driver.find_element_by_css_selector(btn_buy).click()
                time.sleep(0.0)
                try:
                    if driver.find_element_by_css_selector(btn_close):
                        time.sleep(0.1)
                        driver.find_element_by_css_selector(btn_close).click()
                    time.sleep(0.1)
                except:
                    print("抢券成功")
                    a=1
                    break
            if a == 1:
                break

    time.sleep(0.5)
