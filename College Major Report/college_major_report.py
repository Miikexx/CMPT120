# College Major Report (Week 5 coding exercise)
# Mike Kim
# February 15th, 2022


file = open("major_data.csv")

print("Welcome to the US College Major")
file.readline()
# The total number of people surveyed overall majors (i.e. the sum of the Total column

# Step 1: set up accumulator + empty list
population = 0
total_median = 0
total_surveyed = 0
major_list = []
major_list2 = []
# Step 2:
for line in file:
  population += 1
  line = line.strip().split(",")
  #1
  ppl_surveyed = line[3]
  total_surveyed += int(ppl_surveyed)
  #2
  median_income = line[8]
  total_median += int(median_income)
  avg_median = (total_median//population)

# reset 
file.seek(0)
file.readline()
for line in file:
  line = line.strip().split(",")
  #3
  #The ratio of the major's median income with respect to the average median income
  percentages = "{:.3f}".format(float(int(line[8]))/float(int(avg_median))*100) + "%"
  table_filler = [line[1].title(),line[3],line[8],percentages]
  major_list.append(table_filler)
  
# presentation
print("Total number of people surveyed = ", total_surveyed)
print("Overall average median income = ", avg_median)

print("{:<40} {:<10} {:<10} {:<10}".format('MAJOR','PEOPLE','INCOME','INC/AVG'))

file.seek(0)
file.readline()
x = 0

for i in range(population):
  print("{:<40} {:<10} {:<10} {:<10}"\
  .format(major_list[x][0],major_list[x][1],major_list[x][2],major_list[x][3]))
  x += 1

  
# Part two--------------------
print("-------PART TWO-------")

# Reset
file.seek(0)

# skip header 
file.readline()

# take input
major_input = input("Please enter the name of a major: ").title().strip(".,?!")

# list 
second_category_list = []
flag = False
for line in file:
  line = line.strip().split(",")
  if major_input == line[1].title():
    major_category = line[2]
    previous_income = int(line[8])
    flag = True

if flag == False:
  print(major_input, "was not found in the file.")

else:
  print(major_input, "is in the ", major_category, " category.")
  print ("{:<40} {:<10} {:<10} {:<10}".format('MAJOR','UNEMP','INCOME','INC +/-'))
  # put everything under else
  
file.seek(0)
file.readline()

if flag == True:
  for line in file:
    line = line.strip().split(",")
    if line[2] == major_category:
      percentages2 = "{:.2f}".format(float(line[7])*100) + "%"
      inc_plus = int(line[8]) - previous_income 
      table_filler2 = [line[1].title(),percentages2, line[8],inc_plus]
      major_list2.append(table_filler2)
      
file.seek(0)
file.readline()
x = 0
for i in range(len(major_list2)):
  if i == 0:
    print("{:<40} {:<10} {:<10}"\
  .format(major_list2[x][0],major_list2[x][1],major_list2[x][2]))
  else:
    print("{:<40} {:<10} {:<10} {:<10}"\
    .format(major_list2[x][0],major_list2[x][1],major_list2[x][2],major_list2[x][3]))
  x += 1  


      
      
      





