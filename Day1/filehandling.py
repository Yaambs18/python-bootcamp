import os
create = input("Want to create a file(Y/N): ")
if create=='Y':
    f = open("Myfile.txt", "w+")
    f.write("Yansh 22-03-2001")
    f.close()
    read_f = input("Want to read file(Y/N): ")
    if read_f=='Y':
        with open("Myfile.txt", mode='r+') as file:
            content = file.read()
            print(content)
    update = input("Want to update file(Y/N): ")
    if update=='Y':
        file1 = open("Myfile.txt",'w+')
        content1 = content.replace("Yansh", "Bhardwaj")
        content2 = content1.replace("2001", "")
        content3 = int(content[-4:])+10
        updated_content = content2 + str(content3)
        file1.write(updated_content)
        file1.close()
    read_again = input("Want to read again file(Y/N): ")
    if read_again=='Y':
        file2 = open("Myfile.txt",'r')
        new_content = file2.read()
        print(new_content)
        file2.close()
    d = input("Want to delete file Y/N: ")
    if d == 'Y':
        os.remove("Myfile.txt")
    