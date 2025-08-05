

# name = ("priya", "lakshmi", "nami", "shekar")
# print(name)
# last = input("Enter the new name: ")
# new = (last,)
# pos = int(input("Enter the position to insert the new name: "))
# name = name[:pos-1]+new + name[pos-1:]

# print(name)

# y=input("enter text you want to enter")
# d=open("file.txt","w")
# d.write(y)
# d.close

# try:
#     f=open("file.txt","r")
#     x=f.read()
#     print(x)
#     f.close()
# except FileNotFoundError:
#     print("file not found")

# x=input("enter text you want to enter")
# f=open("file.txt","a")
# f.write(x)
# f.close


def main():
     f1=open("sai.jpeg","rb")
     bytes=f1.read()
     print(f1)


main()


# def main():
#     str=""
#     f=open("myfile.txt","w")
#     print("enter texr @as endchar for line")
#     while str!=@
#     str=input()
#     if str!=@:
#         f.write(str+"\n")
#         f.close()
#         f1=open("myfile.txt","r")
#         s=f1.read()
#         print("file contents are \n",s)
#         f1.close
# # main()
# def main():
#     # Open the file in write mode
#     f = open("myfile.txt", "w")

#     print("Enter text. Use '@' as end character for the line.")
#     while True:
#         # Take input from the user
#         str_input = input()
        
#         # Check if the input is the end character
#         if str_input == "@":
#             break
        
#         # Write the input to the file
#         f.write(str_input + "\n")

#     # Close the file after writing
#     f.close()

#     # Open the file in read mode
#     f1 = open("myfile.txt", "r")

#     # Read the contents of the file
#     file_contents = f1.read()

#     # Print the file contents
#     print("File contents are:\n", file_contents)

#     # Close the file after reading
#     f1.close()

# # Call the main function
# main()
'''
class teacher:
    def setId(self,x):
        self.id=x
    def getId(self):
        return self.id
    def setname(self,n):
        self.name=n
    def getname(self):
        return self.name
    def setaddress(self,addr):
        self.address=addr
    def getaddress(self):
        return self.address
class student(teacher):
    def setmarks(self,m):
        self.marks=m
    def getmarks(self):
        return self.marks
s=student()
s.setId(int(input("enter student ID:")))
s.setname(input("enter name:"))
s.setaddress(input("enter address:"))       
s.setmarks(int(input("enter marks:")))
print("roll num is:",s.getId())
print("name is:",s.getname())
print("address is:",s.getaddress())
print("marks is:",s.getmarks())




'''

















