# -*- coding: UTF-8 -*-
import time
from appium import webdriver
from appium.options.android import UiAutomator2Options


def start_app():
    desire_caps = {
        # 通过adb devices获取,此处是模拟器所以填写的是ip和port
        "deviceName": "127.0.0.1:21503",
        # 被测系统决定是Android还是ios
        "platformName": "Android",
        # 系统版本:通过查看被测的系统的设置确定
        # "platformVersion": "9",
        # 包名需进入APP安装包路径通过命令查看:aapt dump badging jinritoutiao.apk |findstr package
        "appPackage": "com.ss.android.article.news",
        # activity名:需进入app安装包路径通过命令查看:aapt dump badging jinritoutiao.apk |findstr activity
        "appActivity": "com.ss.android.article.news.activity.MainActivity",
        # 在此会话前不要重置应用程序
        "noReset": True,
        # 解决输入中文的问题,否则不能用sendkeys输入中文
        "unicodeKeyboard": True,
        "automationName": "UIAutomator2"
    }
    appium_server_url = 'http://localhost:4723'
    driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(desire_caps))
    time.sleep(5)
    driver.quit()


if __name__ == '__main__':
    start_app()
