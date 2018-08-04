# -*- coding=utf-8 -*-
from uiauto.core.driver import Driver
from uiauto.flow.public import flow_booking
from uiauto import config
import time
from uiauto.config import Colors
import click
from uiauto.check.public import check_booking_flow
from uiauto.db.manager import Dbmanager


def goto_public_webview(driver):
    # 进入待测试公众号页面
    page = config.WechatApp.WECHAT_PUBILC_HERELY_INDEPENDENT
    driver.goto_pubilc_page(page)
    # 切换 webview
    driver.switch_to_webview()
    time.sleep(5)


def test_flow(driver, **kw):
    """flow 模块添加到该函数"""
    # 测试独立空间预订流程
    flow_booking.test_booking_flow(driver, **kw)


def check_flow(**kw):
    """校验数据正确性"""
    # 校验独立空间预订流程
    Colors.debug(Colors.BOLD, '-------------------------------------------')
    Colors.debug('# 预订流程测试结果如下：')
    check_booking_flow.check(kw)
    Colors.debug(Colors.BOLD, '-------------------------------------------')

    # 关闭数据库连接
    Dbmanager.disconnect()


def send_email():
    pass


@click.command()
@click.option('--deposit_card_number', prompt='请输入银行卡号',
              help="Develop's deposit card number.")
@click.option('--phone_number', prompt='请输入手机号',
              help="Develop's phone number")
def main(deposit_card_number, phone_number):
    """公众号 UI 自动化测试入口"""
    # 预备数据
    kw = {
        'deposit_card_number': deposit_card_number,
        'phone_number': str(phone_number)
    }
    driver = Driver()

    # 测试阶段
    goto_public_webview(driver)
    try:
        test_flow(driver, **kw)
    except Exception:
        Colors.debug(Colors.FAIL, '业务代码有bug，详情请查看测试机、Sentry、日志')
        raise
    finally:
        driver.quit_driver()

    # 校验阶段
    check_flow(**kw)

    # 通知阶段
    # send_email()


if __name__ == '__main__':
    main()
