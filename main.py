import sysinfo

print("- [1] System Info")
print("- [2] Log Checker")
print("- [3] Task List")
print("- [0] Exit")
user_select = input("Please select number: ")
while(user_select!= '0'):
    if user_select == '1':
        print("Calling show_sysinfo()... ")
        sysinfo.show_sysinfo()
    print("- [1] System Info")
    print("- [2] Log Checker")
    print("- [3] Task List")
    print("- [0] Exit")
    user_select = input("Please select number: ")
