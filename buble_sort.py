lst = [4,2,1,3]

for x in range(len(lst)-1):
    for j in range(len(lst)-x-1):
        print(lst[j], " vs ", lst[j+1])
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]
        print("===total ", lst)


print("===end  ", lst)
