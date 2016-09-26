with open ('data')as f:
    ls = f.readlines()
    data = ls[0].strip()
    word = ls[1].strip()
length = len(word)
counter = 0
print data
print word
for i in range(len(data)-length+1):
    if data[i:(i+length)] == word:
        counter+=1
print counter

