import time
import utils

def execute_job(range_to_print):
    for i in range_to_print:
        print(i)
        time.sleep(5)

    return range_to_print

def summarize_results(a):
    print(a)

def run_query(asd):
    return [i for i in range(asd)]
