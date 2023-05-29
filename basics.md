# Keywords -
- False
- True
- for
- in
- if
- else
- while
- is
- print
- break
- input
- and
- as
- not
- def
- elif
- or


# Identifiers - 
- Myfile
- apple
-- Should not be a keyword
-- only _ allowed
-- can not start with number

# Literals -
- # Sentence here
- ''' Paragraphs here '''


# Data types -
- Int 
- String
- Boolean
- Float
- Double
- List
- Tuple
- Set
- Dictionary


# Operators -
- Identity operator (not,is,is not)
- Logical operators (and, or)
- Membership operators (in,not in)

# Immutable & Mutable -
- Immutable
    - Num3 = 10
    - Num2 

# Input & Outputs -


# LISTS - 
- list = [1,2,3,4]
- list always is defined inside [] 

# DICTIONARIES - 
- dictionary = {}

# TUPLES -
- tuples = ()

# Expressions -
- Arithmetic
    - O/P is solution of a arithmetic equation
- Relational
    - eg: (a = b + c) == (d = e + f), (a>b) and (b>c)
    - O/P is always True / False
- Logical
    - eg: a == b, a == b and c == d
    - O/P is always True / False

# TYPECASTING -
- Typecasting is changing the datatype of a variable
- eg: int(a)

# FLOW CONTROL -
- Flow control is nothing but, us limiting and allowing only a certain few statements to run only if, a condition is satisfied.

# Statements in flow control -
- Compound statement
- Simple statement
- Empty statement

# IF statements - 
- same as C but without {}

# RANGE -
- range(start,stop,step)
- eg: for i in range(0,len(list),2)

# BREAK & CONTINUE - 

# ==========================================================================================================

# Strings -

- Traversing a string:
    eg: 
    na = "JAANU"

    for i in na: # J,A
        print(i,'~',end=" ") # J~,
        # JAANU 
        # J~ A~ A~ N~ U~

- String Operations
    - String + String (Concatenation)
    - String * value (Multiplication/Replication)

NOTE: In C it is `char ch = "A"` but in python is `ch = 'A'`

- String Slicing
    - string slicing is basically when we take a string and get the values based on the address of the variable.
    - eg: string1 = "Hello world"
        string1[4:6] = 'o '
    
- String functions
    - Length = len(string)
    - Capitalize = string.capitalize()
    - Find = string.find(findstring,start,stop)
        eg. string = "Hi jaanu, this is python speaking, wassup?"
        findstring = "jaanu"
    - All alphabets & numbers = string.isalnum()
    - All alphabets = string.isalpha()
    - All digit = string.isdigit()

# LISTS -

- Lists
    - string = ['j','a','a','n','u']
    - lists = ['jannu','bnmit']

- List operation
    - list.append(value)

- List functions
    - pop = list.pop(index)
    - remove = list.remove(value)
    - clear = list.clear()
    - count = list.count(value)
    - reverse = list.reverse()
    - sort = list.sort() == THIS IS IN ASCENDING ORDER
    - sort reverse = list.sort(reverse = True) == THIS IS IN DESCENDING ORDER

- Tuples
    - Methods in tuples
        - max() = tuple.max()
        - min() = tuple.min()
        - index() = tuple.index(value)
            eg: tuple1 = (1,2,3,4,5,6)
            tuple1.index(4) = 3
        - list to tuple
            - tuple(list)

# DICTIONARIES -

- Dictionaries
    - definition of a dictionary
        - eg variable = {<key>:<value>,<key>:<value>,...}
    
    - eg: dict = {'name':'jaanu','age':20,'city':'kolkata'}
        - dict[2] = kolkata
    - d1 = {5 : "number", "a":string, (1,2): "tuple"}
        for key in d1:
            print(key,":",d1[key])

- Dictionary operations
    - Adding key values = <dictionary name>[<key>] = <value>
    - Delete a key value pair = del <dictionary>[<key>]
        eg: dict = {'name':'jaanu','age':20,'city':'kolkata'}
        - del dict['age']
        - dict = {'name':'jannu','city':'kolkata'}
    - To check if key exists in dictionary
        - <value> in <dictionary>

- Dictionary operations
    - len() = Length of the dictionary (how many key:value pairs)
    - clear() = clears the entire dictionary
    - get() = returns the value of the given key, eg:dict.get('key')
    - items() = returns all the values in the dictionary
    - keys() = returns all the keys in the dictionary
    - update() = adds a dictionary or a key:value pair at the end of an existing dictionary

# SORTING TECHNIQUES

- Types
    - Bubble Sort
    - Insertion Sort

- BUBBLE SORT
    - Bubble sort is a simple sorting algorithm that works on lists.
    - Bubble sort repeatedly swaps adjacent elements if they are in wrong order.

    [16  12]  18  13  14  17
    12  16  [18  13]  14  17
    12  [16  13]  18  14  17
    12  13  16  [18  14]  17
    12  13  [16  14]  18  17
    12  13  14  16  [18  17]
    [12  13  14  16  17  18]

- INSERTION SORT
    - Insertion sort is a sorting algorithm that works on lists.

    16  12  18  13  14  17
    12  16  18  13  14  17
    12  13  16  18  14  17
    12  13  14  16  18  17
    12  13  14  16  17  18


# FUNCTIONS -

-- Definition:
- Functions are pieces of code that are made so as to reduce repeating lines of statements inside a program.
- A function is a subprogram that acts on data and often returns a value.

- Used to reduce repeating blocks of code in a program.

- Function creation:

def {Function_name} (Parameters):
    STATEMENTS...

- Calling a function / Invoking a function / Using a function:

{Function_name}()

- {Function_name}(parameters)

- Passing parameters
    - Literals 
        {Function_name}(6.63*10^-34) #planck's constant
    - Variables
        {Function_name}(h) #planck's constant: h = 6.63*10^-34
    - Input from User
        inp = int(input("Enter a value: "))
        {Function_name}(inp)

- Calling functions
    - Normal calling
        {Function_name}(param)
    - Inside other statements
        print({Function_name}(param))
    - Inside expressions
        x = a + {Function_name}(param)

- Types of functions:
    - Built-in Functions
    - Module defined functions
    - User defined functions

# NOTE: type() -> returns the data type of a given variable mentioned in its parameter
    x = 50
    eg: type(x) -> int

# Definition of functions:

- Structure of a function:
    - Function Header
    - Function Name
    - Parameters
    - Function Body
    - Indentation

- Function header:
    def -> Function header for defining functions inside python

- Function name:
    follows the same rules as variable names.

- Parameters:

- Indentation

eg: this is a line of python code
        this is an indented line
    
def {Function_name}(param):
    statements...

# FLOW OF EXECUTION 
eg:
x = 5
y = 10
sum = x + y
print(sum)
p = sum(x,y) # sum not defined
print(p)
def sum(x,y):
    z = x + y
    return z 

'''
CODE EXECUTION:
1) creates a variable x with the value 5
2) creates a variable y with the value 10
3) creates a variable sum with the value of x + y
4) displays the value of the variable sum
5) creates a variable p with the value of (runs the function sum)

THIS IS ABSOLUTELY WRONG!

'''

def sum(x,y):
    z = x + y
    return z
p = sum(x,y)
print(p)

- #code execution flow is: 23,26,23,24,25,26,27

# Parameters:
eg: def something(x,y,z):
        statements...

x - 1
y - 2
z - 3

-- Calling parameters:
something(15,20,25)
- Are literals are passed

something(2,x,y)
- literals + Variables passed

something(x,y,z)
- All variables are passed

-- Defining function parameters:
def something(x=0,y=0,z=0):

