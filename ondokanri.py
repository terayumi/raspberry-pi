#!/usr/bin/env python
#coding=utf8
import subprocess
import sys
import gspread
import datetime
import time

#out=check_output("sudo utils/tempered 2> /dev/null |awk 'NR==1' | cut -b 29-33",shell=True)



time.sleep(30)
gc=gspread.service_account(filename="/home/pi/workspace/TEMPered/ondokanri-account.json")
sh=gc.open_by_key('1I2XjtT3yRkLtXbEUJgZ0_fyw6s0wuFDNwszUlrOMZG0')
ws=sh.get_worksheet(0)
print('opened')
while True:
    re=subprocess.check_output("sudo /home/pi/workspace/TEMPered/utils/tempered 2>/dev/null",shell=True)
    dt=datetime.datetime.now()
    dt_str=dt.strftime('%Y/%m/%d %H:%M:%S')
    print(re[28:33],re[107:112],dt_str)
    tempe=[re[28:33],re[107:112],dt_str]
    try:
        ws.append_row(tempe)
    except:
        print('network error')
        pass
        
    #ws.update_cell(1,1,1)
    time.sleep(1800)

#a=re.find('°C')
#b=re.rfind('°C')

#print(re[a:a+4])
#print(re[b:b-4])

