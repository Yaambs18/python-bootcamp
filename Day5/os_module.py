import os
import shutil
import send2trash


print(os.getcwd())

print(os.listdir('/home/yaambs18/Desktop/Iedaas Python'))

# shutil.move('Python Crash Course ( PDFDrive.com ).pdf', '/home/yaambs18/Desktop/Iedaas Python')

# os.unlink('/home/yaambs18/Desktop/Python Crash Course ( PDFDrive.com ).pdf')
# os.rmdir('/home/yaambs18/Desktop/')
# shutil.rmtree('/home/yaambs18/Desktop/')   ----> it is not safer to use bcz it deletes file permanently

# send2trash.send2trash('Python Crash Course ( PDFDrive.com ).pdf')

for folder, sub_folders, files in os.walk('/home/yaambs18/Desktop/Iedaas Python'):
    print(f"currently at {folder}")
    print("\n")
    for i in sub_folders:
        print("sub ", i)
    print("/n")
    for j in files:
        print('file ', j)