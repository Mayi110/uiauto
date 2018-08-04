# -*- coding=utf-8 -*-


class DBServer(object):
    """数据库服务器配置"""
    # 注意：测试服务器用于 UI 自动化测试服务器
    HOST = '120.26.4.163'
    DOMAIN = 'dev.herely.us'
    # PG
    PG_PROTOCOL = 'postgresql://'
    PG_USERNAME = 'postgres'
    PG_PASSWORD = '_postgres_'
    ORIGINAL_DB_NAME = 'postgres'
    HERELY_DB_NAME = 'herely_db'
    DB_PORT = '5433'
    UIAUTO_DB_DSN = ''.join([PG_PROTOCOL, PG_USERNAME, ':', PG_PASSWORD, '@',
                             HOST, ':', DB_PORT, '/', HERELY_DB_NAME])


class Colors(object):
    """颜色配置"""
    # 骚粉
    HEADER = '\033[95m'
    # 直男蓝
    OKBLUE = '\033[94m'
    # 原谅绿
    OKGREEN = '\033[92m'
    # 飙车黄
    WARNING = '\033[93m'
    # 血腥红
    FAIL = '\033[91m'
    # 正常白
    ENDC = '\033[0m'
    # 加粗白
    BOLD = '\033[1m'
    # 下划线白
    UNDERLINE = '\033[4m'

    @staticmethod
    def debug(color, *text):
        text = ''.join([str(t) for t in text])
        print(color + text)


class Email(object):
    """电子邮件配置"""
    EMAIL_TIGER = 'tiger.huang@herely.us'
    EMAIL_CARSON = 'carson.pan@herely.us'
    EMAIL_SIMON = 'simon.cai@herely.us'
    EMAIL_DOBBY = 'dobby.luo@herely.us'


class PublicXpath(object):
    # 空间列表的第一张空间图片
    xpath_space_list = '//*[@id="main"]/space-space/div/div[2]'
    # 立即预订按钮
    xpath_startup_booking = '//*[@id="spaceDetailWrap"]/a'
    # 请选择按钮（弹出开始时间）
    xpath_select_time = '//*[@id="main"]/space-order-calendar/div[1]/div[1]/div'
    # 开始时间确定按钮
    xpath_start_time = '//*[@id="main"]/div[2]/div[1]/a[2]'
    # 结束时间确定按钮
    xpath_end_time = '//*[@id="main"]/div[3]/div[1]/a[2]'
    # 现在预定按钮
    xpath_launched_booking = '//*[@id="main"]/space-order-calendar/div[2]/button'
    # 银联支付按钮
    xpath_startup_unionpay = '//*[@id="main"]/space-order-payment/div[3]/button[2]'
    # 银联卡号输入框
    xpath_unionpay_input_field = '//*[@id="cardNumber"]'
    # 银联页面下一步按钮
    xpath_unionpay_next_step = '//*[@id="main-container"]/div[1]/div/div[3]/div[4]/div/a'
    # 银联页面免费获取按钮
    xpath_unionpay_free_sms = '//*[@id="sendCode"]/a'


class WechatApp(object):
    # 微信公众号自动以菜单配置
    WECHAT_PUBILC_HERELY_INDEPENDENT = "//*[contains(@text, '独立空间')]"
    WECHAT_PUBILC_HERELY_QUICKPFFICE = "//*[contains(@text, '移动办公')]"
    WECHAT_PUBILC_HERELY_USERINFO = "//*[contains(@text, '个人中心')]"

    # 微信小程序配置
