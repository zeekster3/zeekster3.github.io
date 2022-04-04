import math 

def cels_to_fahr(cels):
    fahr = cels * 9/5 + 32
    return fahr

def windchill(temp, speed):
    chill = 35.74 + (0.6215 * temp) - 35.75 * (speed ** 0.16) + 0.4275 * temp * (speed ** 0.16)
    return chill

speeds = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]


start = ''

while start != 'N':
    start = input('Would you like to find the windchill of a temperature? (Y/N) ').upper()
   
    print()
    if start == 'N':
        print('Have a nice day.')
        break
    elif start == 'Y':
        user_temp = float(input('What is the temperature? '))
        
        print()
        user_scale = input('Is this temperature in Fahrenheit(F) or Celsius(C)? ').upper()
        if start == 'Y':
            
            print()
            if user_scale == 'C':
                temp = cels_to_fahr(user_temp)
                for speed in speeds:
                    print(f'At temperature {temp}, and wind speed {speed} mph, the windchill is: {round(windchill(temp, speed), 2)}F')
                
                print()
            elif user_scale == 'F':
                temp = user_temp
                for speed in speeds:
                    print(f'At temperature {temp}, and wind speed {speed} mph, the windchill is: {round(windchill(temp, speed), 2)}F')
                
                print()
            else:
                print('please enter (F) for Fahrenheit, (C) for Celsius: ')
                
                print()
    else:
        print('Please choose (Y) for yes or (N) for no. ')    
    
    

        




    






# print(f'At temperature {temp}, and wind speed {speed} mph, the windchill is: {windchill(temp, speed)}F')