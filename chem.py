import random

var1pos1 = int(5)
var1pos2 = int(0)
var1pos3 = int(1)
var1pos4 = int(0)

var2pos1 = int(12)
var2pos2 = int(0)
var2pos3 = int(0)
var2pos4 = int(2)

var3pos1 = int(0)
var3pos2 = int(2)
var3pos3 = int(2)
var3pos4 = int(1)

var4pos1 = int(0)
var4pos2 = int(0)
var4pos3 = int(0)
var4pos4 = int(0)

co1 = int(1)
co2 = int(1)
co3 = int(1)
co4 = int(1)

flag = False
count = int(0)

while flag != True:
    answer1 = random.randint(1, 10)
    answer2 = random.randint(1, 10)
    answer3 = random.randint(1, 10)
    answer4 = random.randint(1, 10)
    first1 = int((answer1 * (co1 * var1pos1)) + (answer2 * (co2 * var1pos2)))
    first2 = int((answer1 * (co1 * var2pos1)) + (answer2 * (co2 * var2pos2)))
    first3 = int((answer1 * (co1 * var3pos1)) + (answer2 * (co2 * var3pos2)))
    first4 = int((answer1 * (co1 * var4pos1)) + (answer2 * (co2 * var4pos2)))
    second1 = int((answer3 * (co3 * var1pos3)) + (answer4 * (co4 * var1pos4)))
    second2 = int((answer3 * (co3 * var2pos3)) + (answer4 * (co4 * var2pos4)))
    second3 = int((answer3 * (co3 * var3pos3)) + (answer4 * (co4 * var3pos4)))
    second4 = int((answer3 * (co3 * var4pos3)) + (answer4 * (co4 * var4pos4)))
    if first1 != second1:
        flag = False
        count += 1
    elif first2 != second2:
        flag = False
        count += 1
    elif first3 != second3:
        flag = False
        count += 1
    elif first4 != second4:
        flag = False
        count += 1
    else:
        print("answer 1 = " + str(answer1))
        print("answer 2 = " + str(answer2))
        print("answer 3 = " + str(answer3))
        print("answer 4 = " + str(answer4))
        print("Found after " + str(count) + " attempts!")
        flag = True
