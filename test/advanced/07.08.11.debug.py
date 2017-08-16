# -*- coding: utf-8 -*-
# 调试
import logging
try:
	print('try...')
	r = 10/int('a')
	print('result =', r)
except Exception as e:
	print('except:', e)
	logging.exception(e)
finally:
	print('finally...')
print('END')