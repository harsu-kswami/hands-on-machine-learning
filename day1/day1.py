# day 1 of rivision my python at starting 

# print("hello world")


# what we understand 

# input-> take input of any function and give output-> process the input -> give output

# user_text = input("enter your name: ")
# print(user_text)


# store multiple items 
# user_input = "enter your todo: "
# todo1 = input(user_input)
# todo2 = input(user_input)
# todo3 = input(user_input)

# # todos = [todo1, todo2, todo3]
# # print(todos)

# # type of username
# print(type(user_input))



# first create a empty list 
# todos = []

# then keep adding items to the list
# while 2>1:
#     todo = input("enter your todo: ")
#     todos.append(todo)
#     print(todos)


# use while loops
# password = input("enter your password: ")
# count = 0
# while password != "pass123":
#     print("wrong password")
#     password = input("enter your password: ")
#     count += 1
#     if count == 3:
#         print("too many attempts")
#         break

# if password == "pass123":
#     print("welcome user")


    
# day1-4 part \

# todo list program 
# todos = []

# while True:
#     user_action = input("type add , show , or exit: ")
#     user_action  = user_action.strip()   # strip() remove extra spaces for example:- "  add  " -> "add"

#     match user_action:
#         case "add":
#             todo = input("enter your todo:")
#             todos.append(todo)    #append add item to the list for example :- todos = [] -> todos.append("buy milk") -> todos = ["buy milk"]
#         case "show":
#             for item in todos:
#                 print(item)
#         case "edit":
#             number = int(input("enter the nunber of the todo to edit: "))
#             existing_todo = todos[number - 1]
#             print(f"you are editing {existing_todo}")
#             existing_todo = input("enter the new todo: ")
#             todos[number - 1] = existing_todo
#             print("todo updated")
#         case "exit":
#             break
# print("bye!")   



