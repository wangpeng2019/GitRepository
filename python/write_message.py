'''
#10.2.1写入文件
filename='programming.txt'

with open(filename,'a') as file_object:
	file_object.write("he also love find it .\n")
	file_object.write("she love create new games.\n")


#10.3-1
print("Give me two number,and I'll divide them")
print("Input 'q' to quit.")

while True:
	first_number = input("\nFirst number: ")
	if first_number == 'q':
		break
	second_number = input("\nSecond number: ")
	if second_number == 'q':
		break
	try:
		answer = int(first_number)/int(second_number)
	except ZeroDivisionError:
		print("You can't divide by 0!!!")
	else:
		print(answer)
'''
#10.3-2
#FileNotFoundError

def count_words(filename):
	try:
		with open(filename) as f_obj:
			contents=f_obj.read()
	except FileNotFoundError:
		msg = "Sorry,the file " + filename + " does not exist."
		print(msg)
	else:
		#计算文件包含多少个单词
		words = contents.split()
		num_words = len(words)
		print("The file " + filename + " has about " + str(num_words) + " words.")
	
filenames=[r'C:\Users\admin\Desktop\Alice in Wonderland.txt',"alice.txt"]
for filename in filenames:
	count_words(filename)
