import time

waktu = 3

for i in reversed(range(waktu + 1)):
    if i > 0:
        print(i, end='>>>', flush = True)
        time.sleep(1)
        
    else:
        print('Start')