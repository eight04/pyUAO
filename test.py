# -*- coding: utf-8 -*-
import uao
uao.register_uao()

u = u"一小段中文測試♥一小段中文测试♥中国の短いテスト♥"
b = b"\xa4\x40\xa4\x70\xac\x71\xa4\xa4\xa4\xe5\xb4\xfa\xb8\xd5\x9d\xde\xa4\x40\xa4\x70\xac\x71\xa4\xa4\xa4\xe5\x84\xf2\x86\x49\x9d\xde\xa4\xa4\x83\xf6\xc7\x55\xb5\x75\xc6\xea\xc7\xc2\xc7\xb5\xc7\xc4\x9d\xde"

assert u.encode("big5-uao") == b
assert b.decode("big5-uao") == u
