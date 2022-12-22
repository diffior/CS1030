# Project 1
# Height to Meters
# Input: 
#    a) number from user (in feet) to convert to meters
#    b) number in inches
# Output: converted values
#

# test input for all digits then convert to integer
# if length (number of characters) entered by user
# is zero, then the only entry is the return/enter key
# so quit
def CheckInput(inp):
    # return key -> quit
    if len(inp) == 0:
        print("End program")
        exit()
    
    # check if - for negative number is in the string
    if inp.find('-') == 0:
        print("negative numbers  not allowed")
        exit()
        
    # convert to a real number, if possible
    try:
        x = float(inp)
        return x
    except ValueError:
        print("not a real number")
        exit()

    
# user input routine
def GetUserFeet():
    inFeet = input("Enter feet: ")
    feet = CheckInput(inFeet)
    return feet

def GetUserInches():
    inInch = input("Enter inches: ")
    inches = CheckInput(inInch)
    if inches > 11:
        print("that's bigger than a foot")
        exit()
    return inches

def CalculateTotalInches(ft, inh):
    ti = ft * 12 + inh
    return ti

def ConvertInchesToCentimeters(totalInches):
    centimeters = totalInches * 2.54
    return centimeters
    
def CalculateMeters(centimeters):
    meters = centimeters / 10
    return meters

    
def CheckError(e):
    if e < 0:
        print("error: ", e)
        exit()

def DisplayAnswers(a,b,c,d,e):
    print("--- answers ---")
    print("Feet:   ", a)
    print("Inches: ", b)
    print("CalculateTotalInches:       ", c)
    print("ConvertInchesToCentimeters: ", d)
    print("CalculateMeters:            ", e)

def main():
    feet = GetUserFeet()
    inches = GetUserInches()
    totalInches = CalculateTotalInches(feet,inches)
    centimeters = ConvertInchesToCentimeters(totalInches)
    meters = CalculateMeters(centimeters)
    DisplayAnswers(feet, inches, totalInches, centimeters, meters)
     
#if __name__ == "__main__":
#    main()

main()