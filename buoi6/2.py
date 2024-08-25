# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 18:27:57 2024

@author: lanphuong
"""
input_string = "Đại học Quốc gia, Khu phố 6, P. Linh Trung, Q. Thủ Đức, Tp. HCM"

substrings = input_string.split(",")
for s in substrings:
    print(s.strip())

