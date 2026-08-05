#1 count positive, negative and zeros in given list

list1=[1,4,67,0,-34,56,92,0,-56,7,-82]
pos=0
neg=0
zero=0
for item in list1:
    if item == 0:
        zero+=1
    elif item>0:
        pos+=1
    else:
        neg+=1
print("positive count:", pos)
print("negative count:", neg)
print("zero count:", zero)

#2 return prime numbers only 

list2 = [2,56,23,57,79,34,66,89,83]
prime_list = []
for item in list2:
    for i in range(1,item):
        if item%i == 0:
            break
        else:
            prime_list.append(item)
print("Prime numbers in givem list: ",prime_list) 

#3 return palindrome numbers only

list3=[121,45,23232,643,123456,56565,37842]
p_list=[]
for item in list3:
    string = str(item)
    if string == string[::-1]:
        p_list.append(item)
print("Palindrome Numbers: ",p_list)

#4  search and return index

list_4=[122,333,532,67,12,782,547,111,739]
val = int(input("enter a number you want to find: "))
if val in list_4:
    print("value found on index: ",list_4.index(val))
else:
    print("Value not found")

#5 take 2 lists and check for list 2 but not in list 1 then append that in that 

list_1 = [23,56,22,66,48,29,51,67]
list_2 = [45,64,66,12,23,51,85,92]
for item in list_2:
    if item not in list_1:
        list_1.append(item)
print(list_1)

#6 in given list append all elements which are on even index
ul_list = [12,33,69,257,269,18,27,92,81,25]
length = len(ul_list)
for i in range(length-1,-1,-1):
    if i%2==0:
        ul_list.pop(i)
print(ul_list)


#7 add value at given index

a = (10,20,30,40,50,70)
val = 60
index = 5
a = a[:index] + (val,) + a[index:]
print(a)

#8 add value at last or append given value

c = (10,20,30,40,50,60)
val = 70
c = c + (val,)
print(c)

#9 update value at given index

b = (10,20,30,100,50,60,70)
val = 40
index = 3
b = b[:index] + (val,) + b[index+1:]
print(b)

#10 find value and update with given value

d = (12,23,34,45,66,67,78)
val = 66
update = 56
for value in d:
    if value == val:
        d=d[:d.index(value)] + (update,) + d[d.index(value)+1:]
print(d)

#11 delete at given index 

s = (1,2,3,4,5,6,3)
index = 3
s = s[:index] + s[index+1:]
print(s)

#12 find and delete 

t = (1,2,3,4,5,6,3)
val = 3
for value in t:
    if value == val:
        t = t[:t.index(value)] + t[t.index(value)+1:]
print(t)