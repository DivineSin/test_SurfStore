import os
import time

download_time = []
for i in range(25):
    t1 = time.time()
    os.system("time python3 ../hw5-cse224_fa18_hw5_bty/client.py ../hw5-cse224_fa18_hw5_bty/config.txt download 60000_{} ./download_60k".format(i))
    t2 = time.time()
    download_time.append(t2-t1)

print(download_time)
