
#
data = [1, 48, 22, 19]
big_index = 0
for j in range(len(data)):
    if data[j] > data[big_index]:
        big_index = j

print(big_index)