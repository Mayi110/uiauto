# -*- coding=utf-8 -*-
from appium import webdriver
import time
from uiauto.config import Colors


def singleton(cls, *args, **kw):
    """单例类装饰器"""
    instances = {}

    def _singleton(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]

    return _singleton


@singleton
class Driver(object):

    def __init__(self,
                 platformName='Android',
                 platformVersion='5.1',
                 deviceName='C5H9KA9640820877',
                 appPackage='com.tencent.mm',
                 noReset='true',
                 appActivity='.ui.LauncherUI',
                 recreateChromeDriverSessions='true',
                 androidProcess='com.tencent.mm:tools',
                 appium_rest='http://localhost:4723/wd/hub'):

        # platformName：测试手机系统名
        # platformVersion：测试手机系统版本
        # deviceName：测试手机驱动名（根据 chrome://inspect/#devices 页面得知）
        # appPackage：微信进程名（根据测试手机中的调试模式得知）
        # noReset：禁止在启动自动化测试时关闭微信
        # appActivity：微信的开始界面名
        # recreateChromeDriverSessions：自动销毁 appium client session
        # chromeOptions：待测试公众号的进程名（根据测试手机中的调试模式得知）
        # appium_rest: appium server 接口

        self.platformName = platformName
        self.platformVersion = platformVersion
        self.deviceName = deviceName
        self.appPackage = appPackage
        self.noReset = noReset
        self.appActivity = appActivity
        self.recreateChromeDriverSessions = recreateChromeDriverSessions
        self.androidProcess = androidProcess
        self.appium_rest = appium_rest

        # context
        self.native_app = 'NATIVE_APP'
        self.webview = 'WEBVIEW_com.tencent.mm:tools'

        # chromedriver 配置字典
        self.desired_caps = {
            'platformName': platformName,
            'platformVersion': platformVersion,
            'deviceName': deviceName,
            'appPackage': appPackage,
            'noReset': noReset,
            'appActivity': appActivity,
            'recreateChromeDriverSessions': recreateChromeDriverSessions,
            'chromeOptions': {'androidProcess': androidProcess}
        }

        # 配置 chromedriver
        self.driver = webdriver.Remote(self.appium_rest, self.desired_caps)
        self.driver.implicitly_wait(10)

    def goto_pubilc_page(self, page):
        # 以［收藏］为入口，点击进入指定的公众号页面
        self.driver.find_element_by_xpath("//*[@text='我']").click()
        self.driver.find_element_by_xpath("//*[@text='收藏']").click()
        self.driver.find_element_by_xpath(page).click()

    def switch_to_webview(self):
        # 从 native 切换到 webview
        self.driver.switch_to.context(self.webview)
        Colors.debug(Colors.OKBLUE, 'webview 信息：', self.driver.contexts)
        Colors.debug(Colors.OKGREEN, '切换到 webview 成功')

    def switch_round(self):
        # 来回切换
        self.driver.switch_to.context(self.native_app)
        Colors.debug(Colors.OKBLUE, 'webview 信息：', self.driver.contexts)
        self.driver.switch_to.context(self.webview)
        Colors.debug(Colors.OKBLUE, 'webview 信息：', self.driver.contexts)
        Colors.debug(Colors.OKGREEN, '来回切换：成功')

    def click_element_by_xpath(self, xpath, is_sleep=True):
        # 根据 xpath 来获取页面元素，并点击
        if is_sleep:
            time.sleep(5)
        self.driver.find_element_by_xpath(xpath).click()

    def input_field(self, xpath, message, is_sleep=True):
        # 根据 xpath 来获取页面元素，并输入
        if is_sleep:
            time.sleep(5)
        input_field = self.driver.find_element_by_xpath(xpath)
        input_field.clear()
        input_field.send_keys(message)

    def save_final_image(self, directory, filename):
        # 截图
        self.driver.get_screenshot_as_file(directory + filename)

    def quit_driver(self):
        # 销毁 chromedriver
        time.sleep(30)
        try:
            Colors.debug(Colors.OKGREEN, '测试完毕')
            self.driver.quit()
        except Exception:
            pass
