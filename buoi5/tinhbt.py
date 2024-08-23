# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 23:49:31 2024

@author: lanphuong
"""

import math

a = float(input("Nhập a: "))
b = float(input("Nhập b: "))

tu1 = math.sqrt(a) - math.sqrt(b)
mau1 = math.pow(a, 0.25) - math.pow(b, 0.25)
pso1 = tu1 / mau1

tu2 = math.sqrt(a) + math.pow(a*b, 0.25)
mau2 = math.pow(a, 0.25) + math.pow(b, 0.25)
pso2 = tu2 / mau2

ketqua = pso1 - pso2

print("Kết quả của biểu thức là:", round (ketqua, 3))

