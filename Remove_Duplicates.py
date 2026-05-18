def remove_duplicates(elements):

    unique_elements=set()
    for num in elements:
        unique_elements.add(num)

    return list(unique_elements)

elements=[]
for i in range(6):
    num=int(input("enter a number : "))
    elements.append(num)

unique_elements_list=remove_duplicates(elements)
for num in unique_elements_list:
    print(num, end=" ")

