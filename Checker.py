import re
Checkers = {"black": ['a1', 'a3', 'a5', 'a7',
                      'b2', 'b4', 'b6', 'b8',
                      'c1', 'c3', 'c5', 'c7',
                      'd2', 'd4', 'd6', 'd8',
                      'e1', 'e3', 'e5', 'e7',
                      'f2', 'f4', 'f6', 'f8',
                      'g1', 'g3', 'g4', 'g7',
                      'h2', 'h4', 'h6', 'h8'],
            "white": ['a2', 'a4', 'a6', 'a8',
                      'b1', 'b3', 'b5', 'b7',
                      'c2', 'c4', 'c6', 'c8',
                      'd1', 'd3', 'd5', 'd7',
                      'e2', 'e4', 'e6', 'e8',
                      'f1', 'f3', 'f5', 'f7',
                      'g2', 'g4', 'g6', 'g8',
                      'h1', 'h3', 'h5', 'h7', ]}



def Error_handling(inp):
    # return key -> quit
    if len(inp) == 0:
        print("End program")
        exit()

    # check if - for negative number is in the string
    if inp.find('-') == 0:
        print("negative numbers  not allowed")
        exit()

    if input > 8:
        print("Too big of number")
        exit()

    #if data > [0]:
        #print("too high of a letter")
        #exit()

    try:
        x = float(inp)
        return x
    except ValueError:
        print("not a real number")
        exit()


keys = list(Checkers.keys())

# print(keys)
print("This program will tell you whether or not the number on the board is black or not."
      "You would be prompted to enter one letter a-h and a number 1-8 to figure out the space"
      "Not following instructions will terminate the program and you can start again.")

def getChar():
    input_str = input("Enter information: ")
    if not re.match("[a-h1-8]*$", input_str):
        print("Error! Wrong put")
        exit()
    elif len(input_str) > 2:
        print("Error! Only 2 characthers allowed!")
        exit()



myChar = getChar()
print(myChar)

#for Checkers in Checkers.keys():
    #data = input("Enter a-h and 1-8: ")
    #print(keys)

