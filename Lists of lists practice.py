list1 = [

    [1, 2, 4],
    [11, 12, 13], 
    [7, 8, 9]
]

def finding_sum(sum):
    sum(len(sublist)for sublist in list1)
    


for row in list1:
    for element in row:
        print(element, end= " ")
    print()