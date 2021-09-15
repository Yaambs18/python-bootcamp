import zipfile

f = open("file_one.txt", 'w+')
f.write("This is file one")
f.close()

f = open("file_two.txt", 'w+')
f.write("This is file two")
f.close()

comp_file = zipfile.ZipFile('compress.zip', 'w')
comp_file.write('file_one.txt', compress_type=zipfile.ZIP_DEFLATED)
comp_file.write('file_two.txt', compress_type=zipfile.ZIP_DEFLATED)
comp_file.close()

zip_obj = zipfile.ZipFile('compress.zip', 'r')
zip_obj.extractall("extracted_file")

# zipping entire folder using shutil module

import shutil

dir_to_zip = '/home/yaambs18/Desktop/extracted_file'

new_zip_file = "shutil_zip"

shutil.make_archive(new_zip_file, 'zip', dir_to_zip)
shutil.unpack_archive('shutil_zip.zip','new unzip shutil','zip')
