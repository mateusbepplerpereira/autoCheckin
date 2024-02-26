from datetime import datetime
import time
from dotenv import dotenv_values
import tkinter as tk
from tkinter import messagebox

from autoCheckin import startAutoCheckin

env_values = dotenv_values("./config/.env")

def checkin():
    if messagebox.askquestion("Lembrete!", "Realizar Checkin. Deseja executar o bot?") == 'yes':
        startAutoCheckin(env_values)
    time.sleep(5)

def timer():
    hr1 = "07:50"
    hr2 = "09:50"
    hr3 = "15:50"
    while True:
        if env_values['RUN'] == "True":
            timeNow = datetime.now().strftime("%H:%M")
            weekday = datetime.now().weekday()
            days = [5,6]
            if timeNow == hr1 and weekday not in days or timeNow == hr2 and weekday not in days or timeNow == hr3 and weekday not in days and weekday != 4:
                checkin()
            else:
                time.sleep(10)

timer()