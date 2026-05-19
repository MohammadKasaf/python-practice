
def missing_number(elements):

    flag=1

    while flag<=len(elements):
        if flag not in elements:
            return flag
        flag+=1

    return flag

n=int(input("enter a number : "))
elements=[]
for i in range(n-1):
    elements.append(int(input()))

get_missing_number=missing_number(elements)
print(f"missing number is {get_missing_number}")