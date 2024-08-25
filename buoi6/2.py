# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 18:27:57 2024

@author: lanphuong
"""

input_string = "Đại học Quốc gia, Khu phố 6, P. Linh Trung, Q. Thủ Đức, Tp. HCM"
substrings = input_string.split(", ")
substrings_cleaned = [s.replace("P. ","").replace("Tp. ","").replace("Q. ","") for s in substrings]
for s in substrings_cleaned:
    print(s)

