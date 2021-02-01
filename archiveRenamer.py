import os

# for renaming rom archives to delete either 
# certain strings in names
# OR
# entire files that contain certain strings

# rename certain files

rootdir = 'D:/Games/Xbox/Emulated/genesis/all_genesis'
target = " 3"
for filename in os.listdir(rootdir):
    if target in filename:    
        filepath = os.path.join(rootdir, filename)
        newfilepath = os.path.join(rootdir, filename.replace(target, " iii"))
        os.rename(filepath, newfilepath)
'''
# delete files that contain
my_dir = "D:/Games/Xbox/Emulated/genesis/all_genesis" # enter the dir name
for fname in os.listdir(my_dir):
    if "(Brazil)" in fname:
        os.remove(os.path.join(my_dir, fname))
'''

