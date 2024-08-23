# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 19:40:04 2024

@author: lanphuong
"""

print ("Nhập số giờ, phút, giây: ")
gio = float(input("Giờ: "))
phut = float(input("Phút: "))    
giay = float(input("Giây: "))

if gio == phut == giay == 0:
    print ("Số giây không hợp lệ")
else:
    sogiay = gio * 60 * 60 + phut * 60 + giay
    print ("Số giây được đổi ra là: ", sogiay)


            
            

  
    
    