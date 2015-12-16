from timeit import default_timer


start = default_timer()
"Stupid test function"
L = [i for i in range(100)]
end = default_timer()
print(end - start)
print L
