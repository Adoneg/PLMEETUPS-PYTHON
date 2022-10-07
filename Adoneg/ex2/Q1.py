# Q1.
sentence = "All work and no play makes jack a dull boy"
word_list = sentence.split()
print(word_list)
variable_list = ["var1", "var2", "var3", "var4", "var5", "var6", "var7", "var8", "var9", "var10"]
index = 0
for index in range(len(word_list)):
    variable_list[index] = word_list[index]
    print(f"{variable_list[index]}\n")
    index += 1
