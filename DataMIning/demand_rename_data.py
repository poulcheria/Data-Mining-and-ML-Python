import pandas as pd
import os

#deleting empty files

path='C:/Users/poulcheria/Desktop/DataMining/Data/demand'

for (dirpath,dirnames,filenames) in os.walk(path):
        for filename in filenames:
            file_folder=dirpath+'/'+filename
            # print(file_folder)
            if os.path.isdir(file_folder): 
                if not os.listdir(file_folder): 
                    print(file_folder)
                    # os.rmdir(dirpath+filename) 
            elif os.path.isfile(file_folder): 
                if os.path.getsize(file_folder) == 0: 
                    print(file_folder)
                    os.remove(file_folder)  
print(path, 'clean over!')

#renaming the files in demand folder to names: 0 to 1095 for easier manipulation

os.chdir(r'C:/Users/poulcheria/Desktop/DataMining/Data/demand/')
print(os.getcwd())
 
for count, f in enumerate(os.listdir()):
    f_name, f_ext = os.path.splitext(f)
    f_name = str(count)
 
    new_name = f'{f_name}{f_ext}'
    os.rename(f, new_name)



