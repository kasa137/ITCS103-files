import os
#import AGRABIOSO KRISTIN ANGELA - dream
while True:
    os.system("clear")
    print("*====== DREAM FILE MANAGER ======*")
    print("# 1. Read inspring message       #")
    print("# 2. Add a new inspiring message #")
    print("# 3. Rewrite the entire file     #")
    print("# 4. Exit                        #")
    print("*================================*")
    
    iww = " "
    ins = ""
    #iww = ins
    #add = ""

    enter = eval(input("choose an optin above --->  "))
    
    iw = []
    
    if enter == 1:

         os.system("clear")
         print("~~~~~~~~~~* Inspiring Message *~~~~~~~~~~ ")
         #\n
         #def inwr == {
         
         #"*===========================================================================================*",
         #" Dream Big: I want to become a skilled programmer who builds systems that help people.",
         #" Stay Curious: I will keep learning even when things get difficult.",
         #" Embrace Failure: Every error is a step closer to success.",
         #" Create Impact: I want my code to solve real-world problems.",
         #" Be Consistent: Small progress every day leads to big results.",
         #" Believe in Yourself: I am capable of learning and growing.Someday we will be free.",
         #"*===========================================================================================*"}
         #print(iw)  
              
         print("*===========================================================================================*")
         print("# Dream Big: I want to become a skilled programmer who builds systems that help people.     #")
         print("# Stay Curious: I will keep learning even when things get difficult.                        #")
         print("# Embrace Failure: Every error is a step closer to success.                                 #")
         print("# Create Impact: I want my code to solve real-world problems.                               #")
         print("# Be Consistent: Small progress every day leads to big results.                             #")
         print("# Believe in Yourself: I am capable of learning and growing.Someday we will be free.        #")
         print("*===========================================================================================*")
         print("~~~~~* added inspiring words *~~~~~")
         #add = iw.append(ins)
         #print(add)
         #ins = add 
         iww = ins
         print(iww)
     
         ent = input("enter y to exit --->  ").lower()
         if ent == "y":
              continue
          
         else:
             break
    elif enter == 2 :
        os.system("clear")
        print("~~~~~~~* Add Inspiring message *~~~~~~~\n")
        ins = input("Enter your new Inspiring line :  ")
        
        #add = iw.append(ins)
        #ins = add
        iww = ins
        
        print("\nYour Inspiring has been added! ")
        
        ent = input("\nenter y to exit --->  ").lower()
        if ent == "y":
             continue
          
        else:
            break
    elif enter == 3:
        os.system("clear")
        print("Warning : This will overwrite the file.")
        unak = input("\n Type YES to continue : ").upper()
        if unak == "YES" :
            ts = input("\nWrite your new set of inspiring message :\n  ")
            print("File has been overwritten.")
            
        else :
            continue
        #print("File has been overwritten.")
    else:
        break

        
        
        
        
        
         
        
                     