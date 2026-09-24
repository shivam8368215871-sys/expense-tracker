url = "/home/shivam/Documents/vscode/python projects/data.csv"                                  #URL Of The File


def add_expences():                                                                             #For Addding New Expences

    name_of_expence = input("enter your expence name: \n")                                      #For Entering The Expence Name
    try:                                    
        ammount = float(input("enter your expence ammount: \n")) 
    except ValueError:
        print("Please enter a vaild ammount")                                 

    try:                                                                                        #Error Handling For Try

        with open( url , 'a') as file:                                                          #Opening The File
            exp = file.write(f"{name_of_expence},${ammount} \n")                                #Writing The Name Of Expence And Ammount

    except FileNotFoundError:                                                                   #Except Block For Error Handling

        print(f"{url} not found")                                                               #Print Statement In Case Try wont Work

    finally:                                                                                    
        file.close()                                                                           #Closing The File Inside The URL

def display_expenses():

    try:
        with open(url, "r") as file:
            content = file.read()
            if not content.strip():
                print("No expenses recorded yet.")
            else:
                print(content)
                
    except FileNotFoundError:
        print("No expense data file found yet. Add an expense first!\n")
 
def delete_expense():
   
    try:
        with open(url, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("No expense file found to delete from.\n")
        return

    if not lines:
        print("The expense file is currently empty.\n")
        return

    target_name = input("Enter the name of the expense to delete: ").strip().lower()
    
    updated_lines = []
    found = False

    for line in lines:
        if not line.strip():
            continue
            
        name, amount = line.strip().split(",")
        
        if name.strip().lower() == target_name:
            found = True
            print(f"Successfully deleted: {name} ({amount})")
        else:
          
            updated_lines.append(line)

    if found:
        with open(url, "w") as file:
            file.writelines(updated_lines)
    else:
        print(f"Expense named '{target_name}' not found.\n")
