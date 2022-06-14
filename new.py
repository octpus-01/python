import os
import sys
import datetime

head = '#'+'-'*20+'\n' + \
    '#function description:\n' + \
    '#author:octopus\n' + \
    'e-mail:octopus_pierre@163.com\n' + \
    '#'+'-'*20+'\n'
desFile = sys.argv[1]
if os.path.exists(desFile) or not desFile.endswith('.py'):
    print('%s already exist or is not a python file!' % desFile)
    sys.exit()
fp = open(desFile, 'w')
today = str(datetime.date.today())
fp.write('#-*-coding:utf-8-*-\n')
fp.write('#filename:'+desFile+'\n')
fp.write(head)
fp.write('#date:'+today+'\n')
fp.write('#'+'-'*20+'\n')
fp.close()
