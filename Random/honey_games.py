__author__ = 'iamrishap'

nl = ['popal', 'magaz', 'rajkumar', 'was', 'kalakaar', 'kaptaan', 'vactive', 'ajeeb', 'tom', 'cigni', 'satc', 'tauji', 'bibi', 'lover', 'livewire']
sl = [81335, 197916, 86758, 57839, 95795, 122907, 55417, 84950, 191867, 194273, 112811, 120042, 101217, 80277, 264769]
el = list(zip(nl, sl))
print(el)
emps = []
from splinter.browser import Browser
from collections import OrderedDict

br = Browser('chrome')

def find_details(emps):
    # id= gross_monthly     "net_monthly"  super_monthly tax_gross_monthly
    # net_annually
    global br
    for emp in emps:
        br.visit('https://www.paycalculator.com.au/#'+ str(int(emp['gross_annually'])) +'|0|2018|9.5|5,250,8,40,50|000000')
        emp['gross_monthly'] = br.find_by_id('gross_monthly').first.value
        emp['net_monthly'] = br.find_by_id('net_monthly').first.value
        emp['super_monthly'] = br.find_by_id('super_monthly').first.value
        emp['tax_gross_monthly'] = br.find_by_id('tax_gross_monthly').first.value
        emp['net_annually'] = br.find_by_id('net_annually').first.value
        emp['super_annually'] = br.find_by_id('super_annually').first.value
        emp['tax_gross_annually'] = br.find_by_id('tax_gross_annually').first.value
        gross_annually = emp['gross_annually']  #.replace(',', '').replace('$', '').replace('[', '').replace(']', '')
        super_annually = emp['super_annually'].replace(',', '').replace('$', '').replace('[', '').replace(']', '')
        emp['CTC'] = int(gross_annually) + int(float(super_annually))
    br.quit()

for e in el:
    emp = OrderedDict()
    emp['name'] = e[0].upper()
    gross_monthly = (e[1] * 100)/950
    gross_annually = gross_monthly * 12
    # emp['gross_monthly'] = gross_monthly
    emp['gross_annually'] = gross_annually
    emps.append(emp)

find_details(emps)
print(emps)