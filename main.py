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
    per_cpu = psutil.cpu_percent(percpu=True)
    cpu_freq = psutil.cpu_freq(percpu=True)
    print("CPU Usage:", cpu_usage)
    print("Per CPU Usage:", per_cpu)
    print("CPU frequency:", cpu_freq)
    memory_usage = psutil.virtual_memory().percent
    if memory_usage >= 75:
        logging.warning("memory at critical limit!")
    print("memory usage:", memory_usage)
    disk_usage = psutil.disk_usage('C:').percent
    if disk_usage >= 75:
        logging.warning("You better clean your hard drive sir!")
    print("disk usage:", disk_usage)
    network = psutil.net_io_counters(pernic=False, nowrap=True)
    print("Network:", network)
    network_addr = psutil.net_if_addrs()
    print("network address's:", network_addr)