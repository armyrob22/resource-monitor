import psutil
import time
import logging

logging.basicConfig(
    filename='resource_monitor.log', 
    level=logging.WARNING,
    format= '%(asctime)s, %(levelname)s, %(message)s'
)
while True:
    time.sleep(1)
    cpu_usage = psutil.cpu_percent(interval=1,)
    if cpu_usage >= 75:
        logging.warning("Cpu usage is to high!")
    per_cpu = psutil.cpu_percent(interval=1, percpu=True)   
    print("CPU Usage:", cpu_usage)
    print("Per CPU Usage:", per_cpu)
    memory_usage = psutil.virtual_memory().percent
    if memory_usage >= 75:
        logging.warning("memory at critical limit!")
    print("memory usage:", memory_usage)
    disk_usage = psutil.disk_usage('C:').percent
    if disk_usage >= 75:
        logging.warning("You better clean your hard drive sir!")
    print("disk usage:", disk_usage)
