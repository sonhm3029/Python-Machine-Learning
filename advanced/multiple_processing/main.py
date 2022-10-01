"""
Process: An instance of a program(e.g Python interperter)

+ Take advantage of multiple CPUs and cores
+ Separate memory space -> Memory is not shared between processes
+ Great for CPU-bound processing
+ New process is stated independently from other processes
+ Processes are interuptable/killable
+ One GIL for each process -> avoids GIL limitation

- Heavy weight
- Starting a process is slower than starting a thread
- More memory
- IPC (inter-process communication) is more complicated
"""

"""
Threads: An entity within a process that can be scheduled (also known as "leightweight process")
A process can spawn multiple threads

+ All threads within a process share the same memory
+ Leightweight
+ Starting a thread is faster than starting a process
+ Great for I/O-bound tasks

- Threading is limited by GIL: Only one thread at a time
- No effect for CPU-bound tasks
- Not interruptable/killabel
- Careful with race conditions
"""

"""
GIL: Global interperter lock
- A lock that allows only one thread at a time to execute in Python

- Needed in CPython because memory management is not thread-safe

- Avoid:
    - Use multiple processing
    - Use a different, free-threaded Python implementation (Jython, IronPython)
    - Use Python as a wrapper for third-party libraries (C/C++) -> numpy, scipy
"""

from multiprocessing import Process
import os
import time


processes = []
num_processes = os.cpu_count()


print(f"Number of cpus: {num_processes}")
def square_num():
    for i in range(100):
        i*i
        time.sleep(0.1)



if __name__ == "__main__":
    for i in range(num_processes):
        process = Process(target=square_num)
        processes.append(process)

    # Start processes
    for process in processes:
        process.start()

    # Join processes
    for process in processes:
        process.join()
        print('end main')

    