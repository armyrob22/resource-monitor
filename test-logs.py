#Test logging feature
from dashboard import save_log_entry
import time
import random

services = ['web-server', 'api', 'database']
levels = ['INFO' 'WARNING', 'ERROR']

for i in range(20):
    service = random.choice(services)
    level = random.choice(levels)
    message = f"Test log message {i}"
    save_log_entry(service, level, message)
    time.sleep(0.5)