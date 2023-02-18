from datetime import *
import random

today = datetime.today()
date_1 = today - timedelta(seconds=random.randint(0, 60))

diff = str(today - date_1)
diff = diff[5:]

print("The difference between two times is:", diff)