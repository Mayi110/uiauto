# -*- coding=utf-8 -*-
from uiauto.check.public import check_booking_flow
from uiauto import config


def test_booking_flow(driver, **kw):
    """
    独立空间预订流程（切换到 webview 后的后续操作）
    测试流程：点击自定义菜单［独立空间］按钮开始 --> 点击银联支付页面获取验证码按钮
    """

    # 清除测试者的订单数据
    check_booking_flow.prepare(kw)

    # 点击空间列表的第一张空间图片
    driver.click_element_by_xpath(config.PublicXpath.xpath_space_list)
    # 点击立即预订按钮
    driver.click_element_by_xpath(config.PublicXpath.xpath_startup_booking)
    # 点击请选择按钮（弹出开始时间）
    driver.click_element_by_xpath(config.PublicXpath.xpath_select_time)
    # 点击开始时间确定按钮
    driver.click_element_by_xpath(config.PublicXpath.xpath_start_time,
                                  is_sleep=False)
    # 点击结束时间确定按钮
    driver.click_element_by_xpath(config.PublicXpath.xpath_end_time,
                                  is_sleep=False)
    # 点击现在预定按钮
    driver.click_element_by_xpath(config.PublicXpath.xpath_launched_booking,
                                  is_sleep=False)
    # 来回切换
    driver.switch_round()
    # 点击银联支付按钮
    driver.click_element_by_xpath(config.PublicXpath.xpath_startup_unionpay)

    # 来回切换
    driver.switch_round()
    # 输入银联卡号
    driver.input_field(config.PublicXpath.xpath_unionpay_input_field,
                       message=kw['deposit_card_number'])
    # 点击下一步按钮
    driver.click_element_by_xpath(config.PublicXpath.xpath_unionpay_next_step)
    # 点击免费获取按钮
    driver.click_element_by_xpath(config.PublicXpath.xpath_unionpay_free_sms)
