# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 11:47:37 2022

@author: Tiffany Bohorquez
"""

import os 
from tkinter import filedialog
import tkinter as tk

d = tk.filedialog.askdirectory()  
os.chdir(d)

for i in os.listdir(d): 
    re = input("Please enter new name for file "+i + ":")
    os.rename(os.path.join(d,i), os.path.join(d,re))
    
root = tk.Tk()
root.mainloop()

 


            

