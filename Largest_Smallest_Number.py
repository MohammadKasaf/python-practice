def largest_smallest_number(elements):

    largest=elements[0]
    smallest=elements[0]

    for index in range(len(elements)):

        if smallest>elements[index]:
            smallest=elements[index]

        if largest<elements[index]:
            largest=elements[index]

    return largest,smallest


elem=[]
for i in range(6):
    num=int(input("enter a number :"))
    elem.append(num)
largest,smallest=largest_smallest_number(elem)
print(f"largest number is {largest} and smallest number is {smallest}")