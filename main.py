import sysinfo
import logcheck

print("- [1] System Info")
print("- [2] Log Checker")
print("- [3] Task List")
print("- [0] Exit")
user_select = input("Please select number: ")
while(user_select!= '0'):
    if user_select == '1':
        print("Calling show_sysinfo()... ")
        sysinfo.show_sysinfo()
    elif user_select == '2':
        print("Caliing check_log()... ")
        logcheck.check_log()
    print("- [1] System Info")
    print("- [2] Log Checker")
    print("- [3] Task List")
    print("- [0] Exit")
    user_select = input("Please select number: ")
