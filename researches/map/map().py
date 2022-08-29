import time

start = time.time()

old_list = [str(i) for i in range(10000000)]
new_list = list(map(int, old_list))

# print(new_list)
end = time.time() - start
print(end)
