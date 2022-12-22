data = open('LotsOfNumbers.txt')

dataString = data.read()
#print(dataString)

# make the data into a list
dataList = dataString.split("\n")
#print(dataList)
# cast str to int

for i in range(0, len(dataList),1):
    dataList[i] = int(dataList[i]) # Cast this element into in


#print(dataList)

len(dataList)     # indiviual numbers
print(len(dataList))
print("Number of integers")

sum(dataList)       # Added totak
print(sum(dataList))
print("Total sum of integers")

Lots_len = len(dataList)
Lots_sum = sum(dataList)
# Getting the average

print(Lots_sum / Lots_len)
print("Average of integers")

#Note to Blanche would like to see an example using Def to create and average to make the code look cleaner, was having trouble getting the functions to work. Thank you!
