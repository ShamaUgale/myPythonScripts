li= [1,0,4,2,3,5,6]

new_list = []

while li:
    minimum = li[0] 
    for x in data_list: 
        if x < minimum:
            minimum = x
    new_list.append(minimum)
    data_list.remove(minimum)    

print new_list


for i in range(len(li)):
    for j in range(i + 1, len(li)):

        if li[i] > li[j]:
           li[i], li[j] = li[j], li[i]

print li


def maxLengthSubList(arr, sum):