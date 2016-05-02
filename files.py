import os


#get file names
#rename files

def rename ():
    fileNames = os.listdir(r"C:\Users\100520618\Desktop\python\prank")
    
    os.chdir(r"C:\Users\100520618\Desktop\python\prank")

    #loop for changing the names 
    for name in fileNames:
        print (name + " ")
        os.rename(name, name.translate(None, "1234567890"))
        print (name + "\n")
        
    os.chdir(r"C:\Users\100520618\Desktop\python")
rename()
