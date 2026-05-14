# Search the type of PC the program is running on
import os

# Global employee list
emp_info = []

#clear screen
def dump():
    print('\n'*49)

# Used to bring header to the top of the page,
#leaving question and response at the bottom for input to remain visible
def half_dump():
    print('\n'*25)

# Export Employee list
def write_file():
  f = open('emp_lst.txt', 'w') # 'a' gives the emp_lst file the ability to append new information
  for emp in emp_info:
    copy_emp = emp[:]  # a copy of emp_info=[]
    copy_emp[4] = str(copy_emp[4]) # converts any int() or float to str()
    write_str = ','.join( copy_emp ) #creates the string lines of copied emp_info=[]
    f.write(write_str) # Saves the copy to the emp_lst.txt file
    f.write('\n')  # Tells the interpreter to flush the output buffer
  f.close() # Closes the file

# Import Employee list
def read_file():
    f = open('emp_lst.txt', 'r') # 'r' means read only
    contents = f.readlines()  # f.readlines means to read line by line
    for line_str in contents:  #Calling the lines in f.readlines
        emp = line_str.split(',')  # telling the system to split each line with commas and create nested lists
        emp[4] = float(emp[4]) # converting emp[4], salary back to a float
        emp_info.append(emp) # adding the list back to global emp_info = []
    f.close()
    return emp_info # sends the nested list

# Main menu
def manage():
    print('\n', '\t'*2, f"{'_'*30: ^0}{'_'*31: >0}",
          '\n', '\t'*2, f"{'Employee Management System': >45}",
          '\n', '\t'*2, f"{'_'*30: ^0}{'_'*31: >0}",
          '\n', '\t\t\tEmployees in list:', len(emp_info),
          '\n', '\t'*2, f"{'-'*30: ^0}{'-'*31: >0}", '\n')
    main =['Add Employee',
           'View All Employees',
           'Search For Employee by SSN',
           'Update An Employee',
           'Import Employee\'s',
           'Export Employee\'s',
           'Exit Employee Management System']
    for i, answer in enumerate (main, start=1):
        print('[', i, ']', answer)

# add employee form after allowing user to decide how many employees to add
def add_new_emp():
    b = 1
    while b <= choice:
        try:
            print('\nPlease enter employee information:\n')
            name = input("Name: ")
            cap_name = name.title()
            ssn = input("SSN: ")
            phone = input("Phone (only 10 digits): ")
            email = input("Email: ")
            wage = float(input("Hourly Wage: $"))
            salary = (wage * 40) * 52
            new_emp = [cap_name, ssn, phone, email, salary] 
            emp_info.append(new_emp)
            b += 1
        except ValueError:
            dump()
            continue

# Designated employee archive print format
def emp_prt_form():
    for i, (name, ssn, phone, email, salary) in enumerate (emp_info, start=1):
        print('[', i, ']', f"{'\t'*4}{'-'*25: <0}{name: ^10}{'-'*25: >0}",
              '\nSSN:', ssn,
              '\nPhone:', f"({phone [:3]}){phone [3:6]}-{phone [6:]}",
              '\nEmail:', email, '\nSalary:', f"${salary:.0f}", '\n',
              f"{'\t'*4}{'-'*30: <0}{'-'*31: >0}")

# Employee search function: should work using any piece of employee info
def find_emp_ssn ():
    ssn = input("Please enter employee SSN: ")
    for i in range(len(emp_info)):
        if ssn == emp_info[i][1]:
            location = i
            break
    return location
    

# Continuous running program starting with
#Main menu and options to chose from.
while True:
    dump() 
    menu_main = manage() # links to def manage() script
    half_dump()
    menu = input('\nPlease choose an option: ')

    # Add employee into management system
    if menu == '1':
        half_dump()
        print('\n\t'*2, f"{'_'*30: ^0}{'_'*31: >0}",
              '\n\t'*2, f"{'New Employee Information': >45}", 
              '\n\t'*2, f"{'_'*30: ^0}{'_'*31: >0}",
              '\n\t\tEmployees in list:', len(emp_info),
              '\n\t'*2, f"{'-'*30: ^0}{'-'*31: >0}", '\n')
        half_dump()
        choice = int(input("\nHow many employee's would you like to add? : "))
        dump()
        add_new_emp()

    # View all employees in the list and choose one to view
    if menu == '2':
        dump()
        print('\n\t'*2, f"{'_'*30: ^0}{'_'*31: >0}",
              '\n\t'*2, f"{'Employee Archive': >45}",  # Header format
              '\n\t'*2, f"{'_'*30: ^0}{'_'*31: >0}",
              '\n\t\tEmployees in list:',len(emp_info),
              '\n\t'*2, f"{'-'*30: ^0}{'-'*31: >0}", '\n')
        again = 'Y'
        while again != 'N':
            try:
                emp_prt_form()  # Designated employee archive print format
                pick = int(input("Choose employee number to view (i.e. [1]):  "))
                emp_idx = pick - 1
                name = emp_info[emp_idx][0]   # named values directly linking to
                ssn = emp_info[emp_idx][1]    # emp_info global list
                phone = emp_info[emp_idx][2]
                email = emp_info[emp_idx][3]
                salary = emp_info[emp_idx][4]
                dump()
                print('[', pick, ']', f"{'\t'*4}{'-'*25: <0}{name: ^10}{'-'*25: >0}",
                      '\nSSN:', ssn,
                      '\nPhone:', f"({phone [:3]}){phone [3:6]}-{phone [6:]}",
                      '\nEmail:', email, '\nSalary:', f"${salary:.0f}", '\n',
                      f"{'\t'*4}{'-'*30: <0}{'-'*31: >0}")
                half_dump()
                again = input("\nWould you like to view another employee? [Y]/[N]: ").capitalize()
                if again == 'Y':
                    continue
                else:
                    again == 'N'
                    break
            except ValueError:
                break
                
    #option to locate employee using SSN
    if menu == '3':
        half_dump()
        print('\n\t'*2, f"{'_'*30: ^0}{'_'*31: >0}", 
              '\n\t', f"{'Employee Search': >45}",    # Header format
              '\n\t'*2, f"{'_'*30: ^0}{'_'*31: >0}",
              '\n\t\tEmployees in list:',len(emp_info), 
              '\n\t'*2, f"{'-'*30: ^0}{'-'*31: >0}", '\n')
        location = find_emp_ssn() #return value linking def find_emp_ssn() script
        if location == -1:
                print('Not found')
        else:
            name = emp_info[location][0]    # named values directly linking to
            ssn = emp_info[location][1]     # emp_info global list
            phone = emp_info[location][2]
            email = emp_info[location][3]
            salary = emp_info[location][4]
            dump()
            print('[', location, ']\n',
                  '\t'*4, f"{'-'*25: <0}{name: ^10}{'-'*25: >0}",
                  '\nSSN:', ssn,
                  '\nPhone:', f"({phone [:3]}){phone [3:6]}-{phone [6:]}",
                  '\nEmail:', email,
                  '\nSalary:', f"${salary:.0f}",
                  '\n', '\t'*4, f"{'-'*30: <0}{'-'*31: >0}")
            half_dump()
            input('\nPress any key for Main Menu')

    # Option to edit searched employee using ssn search function        
    if menu =='4':
        dump()
        print('\n\t'*2, f"{'_'*30: ^0}{'_'*31: >0}", 
              '\n\t'*2, f"{'Edit Employee Information': >45}",   # Header format
              '\n\t'*2 ,f"{'_'*30: ^0}{'_'*31: >0}",   
              '\n\t\tEmployees in list:',len(emp_info), 
              '\n\t'*2, f"{'-'*30: ^0}{'-'*31: >0}", '\n')
        print()
        p = find_emp_ssn() #return value linking def find_emp_ssn() script
        if p == -1:
            print('Employee Not found')
        else:
            name = emp_info[p][0]   # named values directly linking to 
            ssn = emp_info[p][1]    # emp_info global list
            phone = emp_info[p][2]
            email = emp_info[p][3]
            salary = emp_info[p][4]
            finish = 'Y'
            while finish != 'N':
                print('[1]: ', name)      # List options to choose to edit
                print('[2]: ', ssn)
                print('[3]: ', f"({phone [:3]}){phone [3:6]}-{phone [6:]}")
                print('[4]: ', email)
                print('[5]: ', f"${salary:.0f}")
                edit = input('\nPlease choose an option to edit: ')
                if edit == '1':
                    print('\n\t'*2, f"{'-'*25: <0}{name : ^10}{'-'*25: >0}", '\n')
                    name = input('New Name: ').title()
                    emp_info[p][0] = name
                    print('\nThe employee\'s name has been updated to', emp_info[p][0])
                    finish = input('Do you need to edit another section for this employee? [Y]/[N]: ')
                    if finish == 'Y':
                        continue
                    else:
                        break

                if edit == '2':
                    print('\nSSN: ', ssn, '\n')
                    ssn = input('New SSN: ')
                    emp_info[p][1] = ssn
                    print('\nThe employee\'s SSN has been updated to', emp_info[p][1])
                    finish = input('Do you need to edit another section for this employee? [Y]/[N]: ')
                    if finish == 'Y':
                        continue
                    else:
                        break

                if edit == '3':
                    print('\nPhone: ', phone, '\n')
                    phone = input('New phone number: ')
                    emp_info[p][2] = phone
                    print('\nThe employee\'s phone number has been updated to', emp_info[p][2])
                    finish = input('Do you need to edit another section for this employee? [Y]/[N]: ')
                    if finish == 'Y':
                        continue
                    else:
                        break

                if edit == '4':
                    print('Email: ', email, '\n')
                    email = input('New Email: ')
                    emp_info[p][3] = email
                    print('\nEmail: ', emp_info[p][3])
                    print('\nThe employee\'s email has been updated to', emp_info[p][3])
                    finish = input('Do you need to edit another section for this employee? [Y]/[N]: ')
                    if finish == 'Y':
                        continue
                    else:
                        break

                if edit == '5':
                    print('\nSalary:', salary, '\n')
                    wage = float(input("New Hourly Wage: $"))
                    salary = (wage * 40) * 52
                    emp_info[p][4] = salary
                    print('Salary:', emp_info[p][4])
                    print('\nThe employee\'s salary has been updated to', emp_info[p][4])
                    finish = input('Do you need to edit another section for this employee? [Y]/[N]: ')
                    if finish == 'Y':
                        continue
                    else:
                        break
                else:
                    break
                    print('Press any key for the main menu')

    if menu == '5':
        # Import Employee list
        read_file()
        input('Your list of employee\'s have been uploaded. Press any key for Main Menu.')

    if menu == '6':
        # Export Employee list
        write_file()
        input('Your list of employee\'s have been saved. Press any key for Main Menu.')
   
    if menu == '7':
        dump()
        print('\nEmployees in list:', len(emp_info))
        print('\nThank you and have a great day!')
        half_dump()
        print('Press any key to return to Main Menu')




    
           
