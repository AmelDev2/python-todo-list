to_do_list = []

while True:

  user_needs = input("chose one of them 'add', 'view', 'remove' , 'exit' : ").lower()

  if user_needs not in ['add','view','remove','exit']:
    print("not valid!  you should chose only one of them 'add','view','remove','exit' ")
    continue

  if user_needs == "add":
    task = input("Enter a task: ")
    to_do_list.append(task)
    print(f"the tasks {task} added")

  elif user_needs == 'view':

    for i, task in enumerate(to_do_list, 1):
      print(f"{i}- {task}")

  elif user_needs == 'remove':
    remove_task = input("enter the task you wonated to remove it :")  

    if remove_task in to_do_list:
      to_do_list.remove(remove_task)
      print("The task '{remove_task}' has been removed.")
      
    else:
      print(f"The task '{remove_task}' was not found.")


  elif user_needs == 'exit':
    print("Good Bye!")
    break
  else:
    print("Invalid")

