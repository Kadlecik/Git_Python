text_data = "ahoj Kámo"

file = open("test1.txt", "w")
file.write(text_data)
file.close()


file = open("test1.txt", "r")
file_data = file.read()
file.close()

print(file_data)