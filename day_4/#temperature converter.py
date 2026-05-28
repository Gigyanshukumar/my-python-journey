                              #Temperature converter

var1 = "Temperature converter"
print(var1.center(70))

print()                       #space

temp_cel = float(input("Temperature in celcius: "))          #temperature in celcius
                                                             
                                                             
cels_to_fahr = temp_cel * 9/5 + 32        #converting celcius to fahrenhite                                                                                   into fahrenhite

print()                            #space

print(f"Temperature in fahrenheit: {cels_to_fahr} °F")
