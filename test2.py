'''MY FILE CREATING PROGRAM'''
'''🎰🎰'''
print("This program allows you to open an existing file and also create a file.")

# file creating function(FCF)
def file(name_of_file, files):
    f = open(name_of_file,"w")
    f.write(files)
    f.close
    
    f = open(name_of_file)
    print(">>> your file has been created. take a look")
    print('\n',f.read())
    f.close
    return ''

def open_file(name_of_file):
        f = open(name_of_file)
        print(f.read())
        return ''


option = input("1. Do you want to create a new file?, Or \n2. Open an existing file,\nplease enter 1 or 2 :")
if option == "1":
# File creation interface
  Name_of_file = input(">>> Name your file:")
  Content = input(">>> Give your file some contents:")
  #calling FCF
  x = file(Name_of_file,Content)
  print(x)
elif option == "2":
  print(">>> Enter name of file you want to open")
  Name_of_file = input(":")
  x = open_file(Name_of_file)
  print(x)
else:
  print(">>> only '1' or '2' allowed.Your input", option, "is invalid.")

print("Endorsed by O.J.A")
