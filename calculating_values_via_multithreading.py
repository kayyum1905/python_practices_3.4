import threading
import time


def sum_nums(*args):
    total = 0
    for n in args:
        total += n
        time.sleep(0.3)
        print('Adding: ', n)
    time.sleep(0.25)
    print('Total Sum is: ', total)


def mult_nums(*args):
    total = 1
    for n in args:
        total *= n
        time.sleep(0.3)
        print('Multiplying:', n)
    time.sleep(0.25)
    print('Total Multiplication is: ', total)

# Our array is below
our_array = [3, 4, 32, 1]

t = time.time()
print('time start: ', time.time())

t1 = threading.Thread(target=sum_nums, args=our_array)
t2 = threading.Thread(target=mult_nums, args=our_array)

t1.start()
t2.start()

t1.join()
t2.join()

print('Calculations finished in: ', time.time()-t)
