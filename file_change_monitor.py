# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 12:34:05 2020

@author: KOTIRMA
"""

import os
import shutil
import time

path = "C:/Users/kotirma/PythonTest/autosave.docx"

last_modification_time = os.path.getmtime(path)

print(f"Observing {path} ctrl+C to stop")

while True:
    current_time = time.strftime("%H_%M_%S", time.localtime())
    path2 = f"C:/Users/kotirma/PythonTest/autosave_{current_time}.docx"
    if os.path.getmtime(path) == last_modification_time:        
        time.sleep(10)
    else:
        shutil.copyfile(path,path2)
        last_modification_time = os.path.getmtime(path)
        print("File copied and renamed")        
        time.sleep(10)
    
#https://github.com/scopatz/w3g



