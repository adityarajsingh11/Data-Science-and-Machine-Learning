## Processes that run in parallel
## When to use Multiprocessing
### CPU-Bound Tasks-Tasks that are heavy on CPU usage (e.g., mathematical computations, data processing).
## Parallel execution- Multiple cores of the CPU

import multiprocessing
import time

def square_number():
    for i in range(5):
        time.sleep(1)
        print(f'Square: {i * i}')

def cube_numbers():
    for i in range(5):
        time.sleep(1)
        print(f'Cube: {i * i * i}')


## create the processes
p1 = multiprocessing.Process(target=square_number)
p2 = multiprocessing.Process(target=cube_numbers)
t = time.time()

if __name__=="__main__":
    ## start the processes
    p1.start()
    p2.start()

    ## wait for the processes to finish
    p1.join()
    p2.join()

    finished_time = time.time()-t
    print(finished_time)