# @Author  ~ Onwuemenyi Joshua Akachukwu.
"""This programe is a custom file formatter used by myself to format these type of files."""
# importing the OS.
import os
os.system('title Custom File Formatter (By Jhush)')
def intro() -> None : 
   info : str = """\t\tWelcome to a custom File formatter (CFF)..
   \n\tSpecify the folder path where the files are  located."""
   help : str = """ \nFolder should contain files of custom type to afoid Unexpected results.
    \n\tFiles should contain stuffs like ->  1 6G4–42610–31–4D TOP COWLING ASSY\nWith the first tree lines being like follows
    \n\tFIG. 1 TOP COWLING
    \n\ttrue
    \n\t[]"""
   print(info)
   folderPath : str = input('Enter Directory : ')
   Edit(folderPath)

# The edit function is used to format files in a folder which has these custom files!
def Edit(folderPath : str) -> None :
   # requesting for the working folder
   # folderPath : str = input('Enter Directory : ')

   # this creates an list (aray) containing the names of each file in the listed folder (Directory)
   op = os.listdir(folderPath) 

   # this is where each file is passed to the edit line function for editing. see EditLine2 function bellow;
   for file in op :
      firstEdit = editLine2(file, folderPath)
   print("Line editing done!")
   # callFE()
   # print("Done")
   # i = input("Press enter to exit...")

# The editLine2 function is used to formate each file line by line.
# It reads the first line of the file to get the destination file name, the edit number, and exceptions.
# It then processes the remaining lines, checking if the first element is a digit and if it is not in the exceptions list.
# If the conditions are met, it formats the line and writes it to the destination file.
def editLine2(file : str, folderPath : str) -> bool:
    os.chdir(folderPath)
    srcfile = file or 'new.txt'
    desfile = ''
    ednum = ''
    exceptions = []
    with open(srcfile, 'r', encoding='utf-8') as s:
        lines = s.readlines()
    if len(lines) >= 1:
        desfile = lines[0].strip() + '.txt'
        ednum = lines[1].strip()
        exceptions = lines[2].strip().split()
    with open(desfile, 'w', encoding='utf-8') as d:
        for l in lines[3:]:
            c = ''
            t = l.split()
            editNumbers2(t)
            # if ednum and len(t) > 1 and t[0] not in exceptions:
            #     t = editNumbers2(t, 0) or t
            q = t[0].isdigit() if t else False
            if q and len(t) > 2 and t[1] != t[0]:
                for m in t:
                    c += ' ' + m
                c = c.strip()
                c += '\n'
                d.write(c)
                print(c)
            else:
                print(f"'Removed {len(t)} : {t}'")
    os.remove(file)
    return True

# The editNumbers2 function is used to format the numbers in the line.
# based of the value of Limit
#  it checks every item or word in the line and if it finds a digit it checks if it is the first item in the line. And then if the is at the limit it removes it and the rest of the items.
# but if it is just one away from the limit it leaves it and removes the rest of the items.
def editNumbers2(f : list) -> None:
   limit : int = 5
   print(f"from editNumber2 ${f}")
   for i in range(len(f)) :
      # z = type(int(f[i])) == int #this is where the problem lies. Don't know hoe to check int in str without getting error for non int.
      try :
         z = z = type(int(f[i])) == int
      except :
         z = False
      # print(f"from editNumber2 z = {z}")
      if z  and f.index(f[i]) != 0 :
         c = (len(f)) - f.index(f[i])
         # print(f"from editNumber2 c : {c}")
         if c <= limit :
            for i in range(c) :
               f.pop()
         elif c > limit :
            for i in range(c - 1):
               f.pop()   

# this function checks every line in the file and removes every ',' and '.' at the end of each word.
# It also replaces '–' with '-' and formats the line by adding '=' after every white space after the first two words.
# It returns the formatted line.
def finalEdit(line : str) :
   c = line.split()
   v = list()
   for l in c :
      v.append(l.removesuffix(',').removeprefix('.').replace('–', '-'))
   v2 = ''
   for l in v :
      if v.index(l) > 2 :
         v2 += f'={l}'
      else :
         v2 += f' {l}'
   
   return v2.strip()

# This function is used to call the file editor.
# It prompts the user for a file directory, lists the folders in that directory, and processes each file in those folders with the finalEdit function.
# def callFE(filePath : str) -> None :
def callFE() -> None :
   n = 1
   f = ''
   path = input("File Directory For callFE function : ")
   folders = os.listdir(path)
   dc = []
   for folder in folders :
      os.chdir(f"{path}\\{folder}")
      files = os.listdir(f"{path}\\{folder}")
      for file in files :
         dc.append(file)
         gg = []
         with open(f"{str(file)}", '+r', encoding= 'utf-8') as p:
            for l in p :
               gg.append(finalEdit(l))
         print('Files copied and Editied.... Now appending')
   
         os.rename(file, 'OLD.txt')
         curr = dc.pop()
         with open(curr, 'a+', encoding='utf-8') as Newfile :
            if Newfile.writable() :
               for i in gg :
                  Newfile.writelines(f'{i}\n')
            else :
               print('File not writable!')
         os.remove('OLD.txt')
   print('All Processess Done')
# intro()
callFE()
