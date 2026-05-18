# write in file using with()function
with open('demo.txt', 'w') as file:
  file.write("food helps us grow strong and healthy. We eat food every day. Fruits and vegetables are healthy food. Milk makes our bones strong..")
file.close()

# split file into words
with open('demo.txt', 'r') as file:
  data = file.readlines()
  print("Words in this file are....")
  for line in data:
    word = line.split()
    print (word)
file.close()

