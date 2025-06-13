list = [11,12,23,43,43,7,7,7,90]
print(set(list))

max_freq = 0
max_freq_element = 0

#n^2 soln:

# for i in range(0, len(list)):
#     count = 1
#     for j in range(i +1  , len(list)):
#         if list[i] == list[j]:
#             count += 1
#     #  j loop ends over here
#     if max_freq < count:
#         max_freq = count
#         max_freq_element = list[i]

#n solution:

freq_map = {
}

for i in range(len(list)):
    if list[i] not in freq_map:
        freq_map[list[i]] = 1
    else:
        freq_map[list[i]] += 1

print(freq_map)

for key in freq_map:
    if freq_map[key] > max_freq:
        max_freq = freq_map[key]
        max_freq_element = key

print(max_freq_element)

