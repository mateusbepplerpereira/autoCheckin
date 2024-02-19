from datetime import datetime
import time
from dotenv import dotenv_values
import tkinter as tk
from tkinter import messagebox

from autoCheckin import startAutoCheckin

env_values = dotenv_values("./config/.env")

def checkin():
    resultado = messagebox.askquestion("Lembrete!", "Realizar Checkin. Deseja executar o bot?")
    if resultado == 'yes':
        startAutoCheckin(env_values)
        
    time.sleep(5)

def timer():
    hr1 = "07:50"
    hr2 = "09:50"
    hr3 = "15:50"
    while True:
        timeNow = datetime.now().strftime("%H:%M")
        if timeNow == hr1 or timeNow == hr2 or timeNow == hr3:
            checkin()
        else:
            time.sleep(10)


timer()

# print("Teste")