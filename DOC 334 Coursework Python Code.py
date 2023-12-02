import random
import sys

# Function created for the filteration
def search(list, item):
    for i in range(len(list)):
        if list[i] == item:
            return "NO"
    return "OK"

# Getting user input values

print("          Welcome to a simple percolation program")
print("          =======================================")
print()


command = sys.argv
if len(command) == 2:
    column = int(command[1].split("x")[0])
    row = int(command[1].split("x")[1])    

# Checking if the entered values are compatible to form the grid
if column >= 10 or column <= 2:
    print("Invalid inputs. Default column and row values will be taken as 5x5")
    column = 5
    row = 5
    
if row >= 10 or row <= 2:
    print("Invalid inputs. Default column and row values will be taken as 5x5")
    column = 5
    row = 5

if column == "" or row == "":
    print("Invalid inputs. Default column and row values will be taken as 5x5")
    column = int(5)
    row = int(5)

# Creating lists
values = []
finalgrid = []
resPList = []

# Getting random values and spaces to be inserted in the grid
for b in range(11,100):
    values.append(b)

for o in range(1,10):
        values.append("  ")

for a in range(0,row):
    rowlist = []

    for t in range(0,column):
        rowlist.append(random.choice(values))

    finalgrid.append(rowlist)

# Filteration process of the column in the grid
for y in range(column):
    resP = "OK"
    for z in finalgrid:
        if (z[y] == "  "):
            resP = "NO"
    resPList.append(resP)

finalgrid.append(resPList)

# Printing out the grid
for x in finalgrid:
    for xy in x:
        print("|",xy,"|", end="")
    print("")

# Creating a text file for the output 
with open('Course Work Text File.txt', 'w') as fp:
    fp.write("Percolation program")
    fp.write('\n')
    fp.write('\n')
    for k in finalgrid:
        for num in k:            
            fp.write(f'{num}  ')
        fp.write('\n')

# Creating a html file for the output 
with open('Course Work HTML File.html', 'w') as fp:
    fp.write("Percolation program")
    fp.write('<br>')
    fp.write('<br>')
    fp.write('<table style="border:1px solid black;" cellpadding="5">')

    for l in finalgrid:
        fp.write('<tr>')
        for val in l:
            fp.write('<td style="border:1px solid black">')
            fp.write(f'{val}')        
            fp.write('</td>')
        fp.write('</tr>')
    fp.write('</table>')
