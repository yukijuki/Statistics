import functools

################################### list iteration ###########################
#list comprehension
arr = ["1","2","3","4","5","6"]

simple_list = [1,2,4,5]
print(arr)
double = [arr[el] for el in simple_list]
print(double)

#list comprehension using if
double = [arr[el] for el in simple_list if el in simple_list]
print(double)

#double list comprehension
text = (("Hi", "Steve!"), ("What's", "up?"))
print([word for sentence in text for word in sentence])


#dict comprehension
stat = [["apple", "banana"],["appl2e", "ban2ana"],["app3le", "banana3"]]
dict_stat = {key: value for (key, value) in stat}
print(dict_stat)



################################## list manipulation ###########################
#(set)discard
arr = {"MAX", "ANNA"}
arr.discard("MAX")
print(arr)

#dict items
arr = {"apple":"red", "banana":"yello2"}
for k, v in arr.items():
    print(k,v)

#index to get an element out of list
arr = ["1","2","3","4","5","6"]

print(arr.index("1"))

#delete list
del(arr[1])
print(arr)



########################### map lambda reduce for faster iteration ###########################

#map (function, argument)
simple = [1,2,3,4]
def multiply(x):
    return x*2

# map = map(multiply, simple)
#or
#lambda map(lambda arugument1, arg2: function), argument)
# map = list(map(lambda x : x*2, simple))
print(map)

simple_list = [1,2,4,5,34]
simple_list2 = [1,2,4,5, 4]

#reduce
transaction = [
    {"sender": "yuki", "amount": 2},
    {},
    {},
    {"sender": "yuki", "amount": 2},
    {"sender": "sho", "amount": 2},
    {"sender": "sho", "amount": 2}
    ]

#基本的なやり方
balance = 0
for tx in transaction:
    if len(tx) > 0 and tx["sender"] == "yuki":
        balance += tx["amount"]
print("normal")
print(balance)

#Reduce的なやり方
#answer = list(map(lambda tx_sum, tx: tx_sum + tx, simple_list, simple_list2))
answer = functools.reduce(lambda tx_sum, tx: tx_sum + tx["amount"] if len(tx) > 0 and tx["sender"] == "yuki" else tx_sum, transaction, 0)
print("reduced")
print(answer)