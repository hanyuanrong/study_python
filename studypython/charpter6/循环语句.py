'''
food_list=["康师傅方便面","酸奶","雪糕","康师傅方便面"]
for name  in food_list:
    print(name)

# whie 循环语句
number=len(food_list)
i=0
while i<number:
    print(food_list[i])
    i +=1

# food_list1=["康师傅方便面","酸奶","雪糕","康师傅方便面"]
# food_list2=["啤酒","饮料","矿泉水"]
# food_list3=["花生","瓜子","火腿肠"]
# food_list4=[food_list1,food_list2,food_list3]
# print(food_list4)
#
# for item in food_list4:
#     print(item)
#     for name in item:
#         print(name)

food_list4=[['康师傅方便面', '酸奶', '雪糕', '康师傅方便面'], ['啤酒', '饮料', '矿泉水'], ['花生', '瓜子', '火腿肠']]
for item in food_list4:
    print(item)
    for name in item:
        print(name)

# enumerate枚举，列举，参数为可遍历/可迭代的对象，多用于在for循环中计数，可以同时获得索引和值。
food_list1=["康师傅方便面","酸奶","雪糕","康师傅方便面"]
for i,value in enumerate(food_list1):
    print(i,value)
    print(f'第{i+1}个元素的值是{value}')
'''

food_list4=[['康师傅方便面', '酸奶', '雪糕', '康师傅方便面'], ['啤酒', '饮料', '矿泉水'], ['花生', '瓜子', '火腿肠']]
for i, value in enumerate(food_list4):
    print(f'第{i+1}个元素的值是{value}')
    for j,name in enumerate(value):
        print(f'第{j+1}个元素的值是{name}')



