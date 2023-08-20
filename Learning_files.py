###converts the first letter of each word to uppercase and prints out the converted text.
file = open("input_files/essay.txt",'r')
print(file.read().title())
file.close()

####Write a program that reads the essay.txt file and returns the number of characters contained in the file.
file = open("input_files/essay.txt",'r')
print(len(file.read()))
file.close()

###create a file with name file.txt and write the text snail there.
file = open("input_files/file.txt",'w')
file.write("snail")
file.close()

####1. prompts the user to enter a new member.
####2. adds that member to members.txt at the end of the existing members.
# name = input("Enter name :")
# file = open("input_files/members.txt",'a')
# file.write(name)
# file.close()

####1. generates multiple text files by iterating over the filenames list,
####2. and writes the text Hello  inside each generated text file.
filenames = ['doc.txt', 'report.txt', 'presentation.txt']
for i in filenames:
    f = open(f"input_files/{i}","w")
    f.write("Hello")
    f.close()

#write the items of temperatures each in one line in the file.txt list.
temperatures = [10, 12, 14]
temperatures = [str(i) + '\n' for i in temperatures]
file = open("file.txt", 'w')
file.writelines(temperatures)