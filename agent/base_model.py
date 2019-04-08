import psutil
import time

def cpu_count():
    return psutil.cpu_count()

def cpu_person():
    return psutil.cpu_percent()

def