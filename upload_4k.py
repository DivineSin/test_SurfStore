import os

for i in range(25):
    os.system("python3 ../hw5-cse224_fa18_hw5_bty/client.py ../hw5-cse224_fa18_hw5_bty/config.txt upload 4k/4000_{}".format(i))
