import pickle
import time
from os import listdir
from os.path import isfile, join
import re
import cProfile
from random import randint

from memory_profiler import profile

from algos import AVLTree

mypath = "datasets"
onlyfiles = sorted([join(mypath, f) for f in listdir(mypath) if isfile(join(mypath, f))], key=lambda x: int(re.findall(r'\d+', x)[0]))
total_time = 0

@profile()
def profile(data):
    avl = AVLTree()
    for i in data:
        avl.insert(i)

for file_name in onlyfiles:
    stream = open(file_name, "rb")
    key = re.findall(r'\d+', file_name)[0]
    test_array = pickle.load(stream)
    stream.close()
    start_time = time.time()

    profile(test_array)

    end_time = time.time()
    current_total = round(end_time - start_time, 2)
    total_time += current_total
    print(current_total)

