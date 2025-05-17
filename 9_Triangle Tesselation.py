# Faisal Altaie
# Computing Science 10
# Henry Wise Wood School
# 2021-2022 semster 1
# November 8th, 2021

# input the height, columns, and row inputs (all as integers)
height = int(input("height? :"))
colomns = int(input("colomns? :"))
rows = int(input("row? :"))

# show what the three triangles would be formed of and show our height list near the top
character = '*'
heightList = []

# this is the for loop (take the range from 1 to height multiplied by 2 and increase by 2 repeatedly)
for h in range(1, height * 2, 2):
    heightList.append(h)

# This is the for loop that takes the range on the row and makes the row -1
for row in range(rows):
    for num in heightList:
        ns = ''

        # if the row is divisible by 2, then it's 0, and if it's not divisible by 2, it will turn to 1
        if row % 2 == 0:
            number = character * num

            # for each column,I t will iterate over from 0 to int(columns)
            for colomn in range(colomns):
                ns += ' ' + number.center(max(heightList))

            print(ns)

        # elif the row is divisible by 2,then it's 0, and if it's not divisible by ,2 it will turn to 1
        elif row % 2 == 1:
            ns = ''
            number = character * num

            # if the number is one, the string is one
            if num == 1:
                numberIfOne = character * num
                ns += str(numberIfOne)

            # If the number is not 1, you must find the middle point
            else:
                numberStart = character * ((num // 2) + 1)
                ns += str(numberStart)

            for colomn in range(colomns):

                # Creating the starting offset triangle
                if colomn == 0:
                    numberStart = character * ((num // 2) + 10)

                    spacesCount = ((((max(heightList) // 2) + 1)) - ((num // 2) + 1))
                    spaces = ' ' * spacesCount
                    ns += spaces

                # creating each middle triangle
                if colomn + 1 != colomns:
                    ns += ' ' + number.center(max(heightList))

                # creating the last offset triangle
                if colomn + 1 == colomns:
                    endCount = (((max(heightList) // 2) + 1)) - (num // 2)
                    spacesEnd = endCount * ' '
                    charactersEnd = (num // 2) * character
                    ns += ' ' + spaces + charactersEnd

            # print the final number string
            print(ns)

