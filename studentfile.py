



def add_student():
    print("add")

def search_student():
    print("search")
    
def main():    
    option_1 = "1. Add a new Student"
    option_2 = "2. Search for a Student"
    
    print("XYZ college - Student Management System \n{} \n{}".format(option_1, option_2))
    user_choice = input("Choose 1 or 2: ")
    
    if user_choice == "1":
        print("\nyou chose: {}".format(option_1))
        add_student()
        
    elif user_choice == "2":
        print("\nyou chose: {}".format(option_1))
        search_student()
        
    else:
        print("\nChoice not valid\n")    
    
      
main()