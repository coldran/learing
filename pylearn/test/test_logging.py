import logging
logging.basicConfig(level=logging.INFO)

s = '0'
n = int(s)
logging.info('n = %d' % n)

try:
    print(10 / n)
except Exception as e:
    logging.exception(e)
    

print('end')
