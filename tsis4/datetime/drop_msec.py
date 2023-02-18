from datetime import *

print(datetime.today().replace(microsecond=0))

dt = datetime.today()
dt = dt.strftime("%Y-%m-%d %H:%M:%S ")
print(dt)