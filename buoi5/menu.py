# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 12:19:24 2024

@author: lanphuong
"""

mon_an = {
    1: "Hủ tiếu",
    2: "Cháo lòng",
    3: "Bánh canh",
    4: "Bún riêu",
    5: "Phở bò"
}

print("========== MENU ============ ")
print("1. Hủ tiếu")
print("2. Cháo lòng")
print("3. Bánh canh")
print("4. Bún riêu")
print("5. Phở bò")
print("============================== ")
lua_chon = int(input("Mời bạn chọn món ăn (nhập số): "))
if 1 <= lua_chon <= 5:
    print(f"Bạn đã chọn: {mon_an[lua_chon]}")
    
