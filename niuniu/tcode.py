#! /usr/bin/env python
#coding=utf-8
import os
import xlrd

class GetTcode():
    def __init__(self):
        workbook=xlrd.open_workbook(os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))),'niuniu/tcode.xlsx'))
        self.sheet_pf=workbook.sheet_by_name('16pf')
        print(os.path.dirname(__file__))
        print(os.path.abspath(os.path.dirname(__file__)))
        print(os.path.join(os.path.abspath(os.path.dirname(__file__)),'tcode.xlsx'))
    def tcode_pf(self,str,num):
        d={'a':1,'b':2,'c':3,'e':4,'f':5,'g':6,'h':7,'i':8,'l':9,'m':10,'n':11,'o':12,'q1':13,'q2':14,'q3':15,'q4':16}
        col_num=d[str]
        cell_value=self.sheet_pf.cell_value(num+1,col_num)
        return int(cell_value)
    
if __name__ == '__main__':
    re=GetTcode().tcode_pf('c',3)
    print(re)