
import concurrent.futures
import time

start = time.perf_counter()

def do_something(sec):
    print(f'Sleeping {sec} second(s)...')
    time.sleep(sec)
    return f'Done Sleeping...{sec}'

with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    results = executor.map(do_something, secs)

    # for result in results:
    #     print(result)


    # results = [ executor.submit(do_something, sec) for sec in secs ]

    # for f in concurrent.futures.as_completed(results):
    #     print(f.result())

finish = time.perf_counter()

print(f'Finished in {round(finish - start, 2)} second(s)')
