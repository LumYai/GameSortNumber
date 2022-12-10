import random

# a = [0,1,2,3,4,5,6,7,8,9]
# b = [0,1,2,3,4,5,6,7,8,9]

# c = {1,2,3}

# if a == b :
#     print("ok")

# random_number = random.randint(1, 8)
# print(random_number)

# print(c)
print("*** Let's make like for finish ! ***")
print(  "\t"+str(1)+"|"+str(2)+"|"+str(3)+"\n"
        "\t"+str(4)+"|"+str(5)+"|"+str(6)+"\n"
        "\t"+str(7)+"|"+str(8)+"|")
print("___________________________________________")
#-----------------------RandomNumber--------------
finish = [1,2,3,4,5,6,7,8,0]
test = [1,2,3,4,5,6,7,8,0]

number = []

print("*** START ***")

while len(number) != 8 :
    check_equ = 0
    random_number = random.randint(1, 8)
    # ครั้งแรกให้ใส่ไปใน number เลย
    if len(number) == 0 :
        number.append(random_number)
    # ครั้งต่อไปให้ตรวจสอบไม่ให้เลขเหมือนกับก่อนๆหน้า
    else :
        for i in range (len(number)) :
            if random_number == number[i] :
                check_equ = 1
        # ถ้าเลขไม่เท่าให้เติม
        if check_equ == 0 :
            number.append(random_number)
        else :
            check_equ = 0

number.append(0)

print(number)

print(  "\t"+str(number[0])+"|"+str(number[1])+"|"+str(number[2])+"\n"
        "\t"+str(number[3])+"|"+str(number[4])+"|"+str(number[5])+"\n"
        "\t"+str(number[6])+"|"+str(number[7])+"|")
print("___________________________________________")





#-----------------------Game-------------------------
while finish != number :
    
    check_key = 0


    if number[0] == 0 :
        print("Press number ( ",number[1]," , ",number[3]," ) :",end = '')
        key = int(input())
        if str(key) == str(number[1]) :
            key = 1
            check_key = 1
        elif str(key) == str(number[3]) :
            key = 3
            check_key = 1

        if check_key == 1 :
            number[0],number[key] = number[key],number[0]

    elif number[1] == 0 :
        print("Press number ( ",number[0]," , ",number[2]," , ",number[4]," ) :",end = '')
        key = int(input())
        if str(key) == str(number[0])  :
            key = 0
            check_key = 1
        elif str(key) == str(number[2]) :
            key = 2
            check_key = 1
        elif str(key) == str(number[4]) :
            key = 4
            check_key = 1

        if check_key == 1 :
            number[1],number[key] = number[key],number[1]

    elif number[2] == 0 :
        print("Press number ( ",number[1]," , ",number[5]," ) :",end= '')
        key = int(input())
        if str(key) == str(number[1])  :
            key = 1
            check_key = 1
        elif str(key) == str(number[5]) :
            key = 5
            check_key = 1

        if check_key == 1 :
            number[2],number[key] = number[key],number[2]

    elif number[3] == 0 :
        print("Press number ( ",number[0]," , ",number[4]," , ",number[6]," ) :",end = '')
        key = int(input())
        if str(key) == str(number[0]) :
            key = 0
            check_key = 1
        elif str(key) == str(number[4]) :
            key = 4
            check_key = 1
        elif str(key) == str(number[6]) :
            key = 6
            check_key = 1

        if check_key == 1 :
            number[3],number[key] = number[key],number[3]

    elif number[4] == 0 :
        print("Press number ( ",number[1]," , ",number[3]," , ",number[5]," , ",number[7]," ) :",end='')
        key = int(input())
        if str(key) == str(number[1]) :
            key = 1
            check_key = 1
        elif str(key) == str(number[3]) :
            key = 3
            check_key = 1
        elif str(key) == str(number[5]):
            key = 5
            check_key = 1
        elif str(key) == str(number[7]) :
            key = 7
            check_key = 1

        if check_key == 1 :
            number[4],number[key] = number[key],number[4]

    elif number[5] == 0 :
        print("Press number ( ",number[2]," , ",number[4]," , ",number[8]," ) :",end='')
        key = int(input())
        if str(key) == str(number[2]) :
            key = 2
            check_key = 1
        elif str(key) == str(number[4]) :
            key = 4
            check_key = 1
        elif str(key) == str(number[8]) :
            key = 8
            check_key = 1

        if check_key == 1 :
            number[5],number[key] = number[key],number[5]
            
    elif number[6] == 0 :
        print("Press number ( ",number[3]," , ",number[7]," ) :",end='')
        key = int(input())
        if str(key) == str(number[3]) :
            key = 3
            check_key =1
        elif str(key) == str(number[7]) :
            key = 7
            check_key = 1

        if check_key == 1 :
            number[6],number[key] = number[key],number[6]

    elif number[7] == 0 :
        print("Press number ( ",number[6]," , ",number[4]," , ",number[8]," ) :",end= '')
        key = int(input())
        if str(key) == str(number[6]) :
            key = 6
            check_key = 1
        elif str(key) == str(number[4]) :
            key = 4
            check_key = 1
        elif str(key) == str(number[8]) :
            key = 8
            check_key = 1

        if check_key == 1 :
            number[7],number[key] = number[key],number[7]

    else :
        print("Press number ( ",number[5]," , ",number[7]," ) :",end = '')
        
        key = int(input())
        
        if str(key) == str(number[5]) :
            key = 5
            check_key = 1
        elif str(key) == str(number[7]) :
            key = 7
            check_key = 1
        

        if check_key == 1 :
            number[8],number[key] = number[key],number[8]
        
    if check_key == 0 :
        print("!!! Press key again !!!")
    else :
        print(number)

        # print(  "\t"+str(number[0])+"|"+str(number[1])+"|"+str(number[2])+"\n"
        # "\t"+str(number[3])+"|"+str(number[4])+"|"+str(number[5])+"\n"
        # "\t"+str(number[6])+"|"+str(number[7])+"|"+str(number[8])+"\n")

        row = 0

        print("\t",end='')
        for i in range (len(number)) :
            
            if row == 3 :
                print("\n\t",end='')
                row = 0

            if row == 1 or row == 2 :
                print("|",end='') 
            if number[i] != 0 :
                print(number[i],end='')
            else :
                print(" ",end='')

            row += 1

            
            
        
    print()
    # check_key = 0
    print("___________________________________________")


print ("\tFinish!!!!!!!!!!!!!!!!!!")
print ("\tFinish!!!!!!!!!!!!!!!!!!")
print ("\tFinish!!!!!!!!!!!!!!!!!!")



