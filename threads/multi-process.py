import math
import multiprocessing as mp
import time


results_a = []
results_b = []
results_c = []

def calc_a(nuumbers):
    for i in nuumbers:
        results_a.append(math.sqrt(i**2))

def calc_b(nuumbers):
    for i in nuumbers:
        results_a.append(math.sqrt(i**3))

def calc_c(nuumbers):
    for i in nuumbers:
        results_a.append(math.sqrt(i**5))


if __name__ == "__main__":
    number_list = list(range(5000000))

    
    
    start = time.time()
    calc_a(number_list)
    calc_b(number_list)
    calc_c(number_list)
    end = time.time()

    print(f"Time to complete in sync: {end - start}")

    p1 = mp.Process(target=calc_a, args=(number_list,))
    p2 = mp.Process(target=calc_b, args=(number_list,))
    p3 = mp.Process(target=calc_c, args=(number_list,))

    start = time.time()
    p1.start()
    p2.start()
    p3.start()
    end = time.time()

    print(f"Time to complete in multi-process: {end - start}")