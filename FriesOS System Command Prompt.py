# Please dont edit line 2
# Fries-Byte made this, open-source

inuser = input("Name the Operating System:~$ ")
print("hosting Server...")
print("server loaded!")
print("                                                                                                                 ")
print("FriesOS Operating System [Version 1.0]")
print("(c)Fries-Byte in GitHub 2024")
while 1 == 1:
    serverip = input(inuser+ "@serverhost.test:~$ ")
    
    if serverip == "cfile":
        cfile = input("FileName:~$ ")
        infile = input("FileText:~$ ")
        
    if serverip == "cfile2":
        cfile2 = input("FileName:~$ ")
        infile2 = input("FileText:~$ ")
    

    if serverip == "file -load":
        print(cfile)
        print(cfile2)
    
    if serverip == "info -s":
        print("server name: "+inuser)
        print("server ip: "+serverip)
        print("server state: perfect")
    
    if serverip == "textfile -load":
        print(infile)
        print(infile2)
    
    if serverip == "name .server":
        print(inuser+"/")
        
    if serverip == "state -net":
        print("Network State: Offline")
    
    
    if serverip == "cd":
        print(inuser+"@serverhost.test/Server/Storage/Files/.Useagefiles.")
        print(".. is an inaccessable place")
        pickcd = input("Where do you wish to go?:~$ ")
    
        if pickcd == "Server":
         print("successfully moved!")
    
        if pickcd == "Storage":
           print("successfully moved!")
    
        if pickcd == "Files":
           print("successfully moved!")
    
        if pickcd == "Useagefiles":
            print("DIRECTORY'S BLOCKED")
