import os
from traceback import print_tb
def ops():
    cmd = 'cls' # for windows
    os.system(cmd)
ops()

def profile():
    first_name = "Ramadhan" #strings
    second_name = "Ibrahim" #strings
    age = 26
    pro = "Cyber Security Engineer | Python Developer," # strings
    study = "Centennial College"
    country = "Toronto, Canada"
    certs = "Two Diplomas in Computer Science and Cyber Security"
    dip_cs = 2 
    dip_sec = 2
    
   

   # maths functions 
    


    print("")
    print("==========================================")
    print("My name is ", first_name,second_name)
    print("I am ", pro)
    print("Am",age, "years" )
    print("Graduated at ",study, "in",country, "with ",certs,)
    print("Studied Diploma in Computer science for ",dip_cs, "years and Cyber security for", dip_sec, "years, that's",dip_cs + dip_sec, "years")

    print("==========================================")

profile()