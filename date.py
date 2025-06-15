from datetime import timedelta
from pathlib import Path


u = Path('/proc/uptime').read_text().split()[0]
t = timedelta(seconds = float(u))
print (str(t).split('.')[0])
