import time

start = time.time()

old_list = [str(i) for i in range(10000000)]

new_list = []
for item in old_list:
    new_list.append(int(item))

# print(new_list)
end = time.time() - start
print(end)
