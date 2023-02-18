from datetime import *

today = date.today()
yesterday = today - timedelta(1)
tomorrow = today + timedelta(1)

print("Yesterday was: ", yesterday)
print("Today is: ", today)
print("Tomorrow will be: ", tomorrow)