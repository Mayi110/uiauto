# -*- coding=utf-8 -*-
from uiauto.db.manager import Dbmanager
from uiauto.config import Colors


def prepare(kw):
    # 看将测试者的订单记录的状态都改成 cancel
    # 避免干扰数据校验
    sql = "UPDATE booking SET status = '{}' \
           WHERE member_phone_number = '{}'" \
           .format('cancel', kw['phone_number'])
    Dbmanager.update(sql)


def check(kw):
    # 查询出自动化测试时生成的订单
    sql = "SELECT * FROM booking \
           WHERE status = '{}' OR status = '{}' \
           AND member_phone_number = '{}'" \
           .format('wait_use', 'in_use', kw['phone_number'])
    booking = Dbmanager.select_one(sql)

    # 查询处订单对应的支付纪录
    sql = "SELECT * FROM payment \
           WHERE booking_id = '{}'" \
           .format(booking[0])
    payment = Dbmanager.select_one(sql)

    # 检验数据是否正确
    if booking:
        Colors.debug(Colors.OKGREEN, '订单数据记录正确')
    else:
        Colors.debug(Colors.FAIL, '订单数据记录不存在')
    if 'unionpay_pre' in payment and 'success' in payment and \
            'pre_auth_trade' in payment:
        Colors.debug(Colors.OKGREEN, '支付数据记录正确')
    else:
        Colors.debug(Colors.FAIL, '订单数据记录错误')
