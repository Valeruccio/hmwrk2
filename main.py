print("Задание 1")

user_list = ['Рамочно-сместительный двигатель', 5, 20.5, None, True]
user_list.append("Маневровый двигатель")

print("---")

for x in user_list:
    print(x)

print("---")

def user_type(x):
 for x in range(len(user_list)):
    print(type(user_list[x]))
 return
user_type(user_list)

print("---")

print("Задание 2")

