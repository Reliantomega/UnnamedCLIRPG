

test_list = []
test_list.append("hello")
test_list.append("world")
test_list.append(123)
test_list.append((1, 3))

for i in test_list:
    print(i)

in_var = ""
t_list = []
while in_var != "q":
    in_var = input("input something. type q to quit")
    t_list.append(in_var)

for j in t_list:
    print(j)
