def manage_tasks():
  tasks = ["go to the gym" , "wash dishes", "do homework"]
  while True:
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Remove a task by number")
    print("4. Return to main menu")
    choice = input("Choose: ")
    if choice == "1":
      task = input("Enter Task: ")
      tasks.append(task)

    elif choice == "2":
      for task in tasks:
        print(task)

    elif choice == "3":
      num = input("Enter Number: ")
      num = int(num)
      if num>=1 and num<=len(tasks):
        tasks.pop(num-1)
      else:
        print("Invalid number")

    else:
      break
    


