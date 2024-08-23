# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 18:27:57 2024

@author: lanphuong
"""
str1 = ("Đại học Quốc gia,\nKhu phố 6,\nP. Linh Trung,\nQ. Thủ Đức,\nTp. HCM")
str1 = str1.replace(",","")
str1 = str1.replace("P. ","")
str1 = str1.replace("Tp. ","")
str1 = str1.replace("Q. ","")
print(str1)

