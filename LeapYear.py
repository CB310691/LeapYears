class Leap_Year_Test : #Creates a Class for the test
    
    def Leap_Years(): #Defining the function
            
        year = input("Enter the year you want to test") #Insert the year
        
        if (year % 4 == 0) and (year % 100 != 0) and (year % 400 != 0): #If the remainder of the year is 0, it is divisible by 4 and therefore a leap year. However if the year is divisible by 100 then the leap year is skipped.
             print("This year is a leap year")
        if (year % 100 == 0) and (year % 400 != 0): #A leap year is skipped every 100 years unless the year is also divisble by 400.
            print("This year is not a leap year")
        if (year % 100 == 0 ) and (year % 400 == 0):
            print ("This year is a leap year") #If the year is divisible by 100 and 400 then the year is a leap year
        if (year % 4 != 0) and (year % 100 != 0) and (year % 400 != 0):
            print("This year is not a leap year")#If the two if statements above do not work, this will output that the year is not a leapyear.
            
    () #closes the function

    Leap_Years() #Calls the function


#Different Tests:
#Typical leap year e.g 2016
#Typiclar non leap year e.g 2017
#Atypical leap year e.g 1600
#Atypical non leap year e.g 1900
