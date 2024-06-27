# def print_list(n):
#     for i in list(range(0,n)):
#         print(i)
#
# print_list(10)
# print('Hello')
# print('----------------')
# ##
# num = 1
# while num <= 100:
#     print(num)
#     num += 1

# def multi(m):
#     for n in range(1, 10):
#         print(f'{m} * {n} = {m*n:2d}')
# multi(3)

import calendar
import tkinter as tk

c = calendar.TextCalendar()
m = c.formatmonth(2021, 3)

root = tk.Tk()
t = tk.Text(root, height=7, width=20)
t.insert(tk.END, m)
t.pack()
tk.mainloop()
