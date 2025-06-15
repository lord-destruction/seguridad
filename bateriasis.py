# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 18:51:48 2020

@author: lord-drestuction
"""

import psutil

from plyer import notification
import time

battery = psutil.sensors_battery()
while (True):
    percent = battery.percent
    notification.notify(
    title="Battery Percentage",
    message=str(percent)+"% Battery remaining",
    timeout=10       
    )
    time.sleep(60*60)
    continue
