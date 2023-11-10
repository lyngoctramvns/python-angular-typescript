# !, -, and number at the beginning of a variable is not valid
name = "Dave"
print("This variable is " + name)

# operators

# 1. Assignment Operator: =
# 2. Arithmatic Operator: +, -, *, /, //(floor division), round(24/5), %, **, +=, -=, /= (divide to decimal numbers)
# 3. Comparison Operators: ==, ===, !=, >, <, >=, <=, not, and, or

# Data types

# String data type
stringData = "Tram"
print(type(stringData))
print(isinstance(stringData, str))

# Constructor function
pizza = str("Pepperoni")
print(pizza)
print(type(pizza))
print(isinstance(pizza, str))

#Concatenate
stringFirst = "Ngoc"
stringSecond = "Tram"
fullname = stringFirst + " " + stringSecond
print(fullname)

#multiple lines
multiple = '''
This is a new line
And then enter
New again

'''
print(multiple)

#Using single quote or double quote in string
specialCharacters = 'I\'m saying ' + "\"To you right now\""
print(specialCharacters)
print(specialCharacters.lower())
print(specialCharacters.upper())
print(len(specialCharacters))

# get a range of index value
print(specialCharacters[1:-1]) #From the first to the last character
print(specialCharacters[1:]) # Get index all the way to the end

#Boolean data type
myvalue = True
wrongVal = bool(False)
print(type(wrongVal))
print(type(myvalue))

#Numeric  data type
myNumber = 9
print(myNumber)

#Operators

## Asignment operator
## Arithmatic operator: +, -, *, /, %, **(to the power of), +=, -=, *=, /=
test1 = round(24/5)
test2 = 42
test2 += 1
print(test1,test2)
## Comparison operator: ==, ===, !=, >=, <=, not, and, or

print(42=='42')
x = True
print(not x)

## condition if-else

if x != False:
    print('This value is %s' % x) # print(f'This value is {x}')
    print('Another way', x)
    output = 'Third way ' + str(x)
    print(output)
else:
    print('No')

## Ternary Operators
y = 15
print("Right on!") if y > 10 else print("Not today!")

# User Inputs
