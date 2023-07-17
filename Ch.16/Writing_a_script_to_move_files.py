import os 
#Target folder is the folder we want to move the files too. 
#Source folder is the folder in which we want to extract the data.

target_folder = r'C:\Users\deanf\.vscode\Ch.16\data' + '\\'
source_folder = r'C:\Users\deanf\OneDrive\Desktop\chapter_16\the_csv_file_format\data' + '\\'

for path, dir, files in os.walk(source_folder):
    if files:
        for file in files:
            if not os.path.isfile(target_folder + file):
                os.rename(path + '\\' + file, target_folder + file)
#The files that I saved migrated over to the correct location finally so hopefully I can actually start to generate data now. 
