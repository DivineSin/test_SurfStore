import os

for i in range(25):
    os.system("dd if=/dev/urandom of=4k/4000_{} bs=1000 count=4".format(i))
