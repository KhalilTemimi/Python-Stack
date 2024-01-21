def countdown (start):
    list= []
    for i in range(start, -1, -1):
        list.append(i)
    return list
countdown_list = countdown(5)
print(countdown_list)


def print_and_return(list):
    print(list[0])
    return(list[1])
secondValue = print_and_return([1,2])
print(secondValue)

def first_and_length(list):
    return(list[0]+len(list))
sum = first_and_length([1,5,8,6,4])
print(sum)

def values_greater_than_second(list):
    if len(list)<2:
        return False
    new_list=[]
    for i in range (len(list)):
        if list[i]>list[1]:
            new_list.append(list[i])
    if len(new_list)>1:
        print(len(new_list))
        return new_list
    else:
        return False
new_list = values_greater_than_second([3,2,5,0,7,1])
print(new_list)

def length_and_value(size,value):
    my_list=[]
    for i in range(size):
        my_list.append(value)
    return my_list
my_list = length_and_value(6,2)
print(my_list)