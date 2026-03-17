def check_log():
  file_name = input("Please enter file name: /n")
  try: 
    file = open(file_name, 'r')
    for line in file:
      if "ERROR" in line:
        print(line)
    file.close()
  except FileNotFoundError:
    print("Error: file does not exist")



