import os

for i in range(25):
    os.system("dd if=/dev/urandom of=60k/60000_{} bs=1000 count=60".format(i))
