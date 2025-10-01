import psutil
import time

while True:
    time.sleep(1)
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage >= 75:
        print("Cpu usage is to high!")   
    print("CPU Usage:", cpu_usage)
    memory_usage = psutil.virtual_memory().percent
    if memory_usage >= 80:
        print("memory at critical limit!")
    print("memory usage:", memory_usage)
    disk_usage = psutil.disk_usage('C:').percent
    if disk_usage >= 60:
        print("You better clean your hard drive sir!")
    print("disk usage:", disk_usage)
