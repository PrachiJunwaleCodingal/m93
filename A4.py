# Program to merge two files into a third file

with open('demo.txt') as fp:
	data1 = fp.read()

with open('food.txt') as fp:
	data2 = fp.read()

data1 += "\n"
data1 += data2
print("Merging two files....to see result open MergedFile.txt")
with open ('MergedFile.txt', 'w') as fp:
	fp.write(data1)
