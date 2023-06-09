# Jhanvi's python notes

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

- Break stops the loop

- Continue skips the next statements and goes to the next itiration of the loop

- - -

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
    ```
    - eg: string1 = "Hello world"
        string1[4:6] = 'o '
    ```
    
- String functions
    - Length = len(string)
    - Capitalize = string.capitalize()
    - Find = string.find(findstring,start,stop)
    ```
    eg. string = "Hi jaanu, this is python speaking, wassup?"
    findstring = "jaanu"
    ```
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
    - sort = list.sort() `THIS IS IN ASCENDING ORDER`
    - sort reverse = list.sort(reverse = True) `THIS IS IN DESCENDING ORDER`

- Tuples
    - Methods in tuples
        - max() = tuple.max()
        - min() = tuple.min()
        - index() = tuple.index(value)  
        ```
        eg: tuple1 = (1,2,3,4,5,6)
        tuple1.index(4) = 3
        ```
        - list to tuple
            - tuple(list)

# DICTIONARIES -

- Dictionaries
    - definition of a dictionary
        - eg `variable = {<key>:<value>,<key>:<value>,...}`
    ```
    eg: dict = {'name':'jaanu','age':20,'city':'kolkata'}
        dict[2] = kolkata
        d1 = {5 : "number", "a":string, (1,2): "tuple"}
        for key in d1:
            print(key,":",d1[key])
    ```
- Dictionary operations
    - Adding key values = `<dictionary name>[<key>] = <value>`
    - Delete a key value pair = `del <dictionary>[<key>]`
    ```
        eg: dict = {'name':'jaanu','age':20,'city':'kolkata'}
        - del dict['age']
        - dict = {'name':'jannu','city':'kolkata'}
    ```
    - To check if key exists in dictionary = `<value> in <dictionary>`

- Dictionary operations
    - len() = Length of the dictionary (how many key:value pairs)
    - clear() = clears the entire dictionary
    - get() = returns the value of the given key, `eg:dict.get('key')`
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
```
    [16  12]  18  13  14  17
    12  16  [18  13]  14  17
    12  [16  13]  18  14  17
    12  13  16  [18  14]  17
    12  13  [16  14]  18  17
    12  13  14  16  [18  17]
    [12  13  14  16  17  18]
```
- INSERTION SORT
    - Insertion sort is a sorting algorithm that works on lists.
```
    16  12  18  13  14  17
    12  16  18  13  14  17
    12  13  16  18  14  17
    12  13  14  16  18  17
    12  13  14  16  17  18
```

# FUNCTIONS -

### Definition:
- Functions are pieces of code that are made so as to reduce repeating lines of statements inside a program.
- A function is a subprogram that acts on data and often returns a value.

- Used to reduce repeating blocks of code in a program.

- Function creation:
```
def {Function_name} (Parameters):
    STATEMENTS...
```
- Calling a function / Invoking a function / Using a function:
```
{Function_name}()

{Function_name}(parameters)
```
- Passing parameters
    - Literals: 

        `{Function_name}(6.63*10^-34) #planck's constant`

    - Variables:

        `{Function_name}(h) #planck's constant: h = 6.63*10^-34`

    - Input from User:

        `inp = int(input("Enter a value: "))`

        `{Function_name}(inp)`


- Calling functions
    - Normal calling

        `{Function_name}(param)`
    - Inside other statements

        `print({Function_name}(param))`
    - Inside expressions

        `x = a + {Function_name}(param)`

- Types of functions:
    - Built-in Functions
    - Module defined functions
    - User defined functions

#### ***NOTE:*** type() -> returns the data type of a given variable mentioned in its parameter
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
    - def -> Function header for defining functions inside python

- Function name:
    - follows the same rules as variable names.

- Indentation
```
eg: this is a line of python code
        this is an indented line
    
def {Function_name}(param):
    statements...
```
# FLOW OF EXECUTION 
#### Invalid representation:
```
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


CODE EXECUTION:
1) creates a variable x with the value 5
2) creates a variable y with the value 10
3) creates a variable sum with the value of x + y
4) displays the value of the variable sum
5) creates a variable p with the value of (runs the function sum)

THIS IS ABSOLUTELY WRONG!
```
#### Correct representation:
```
23 def sum(x,y):
24     z = x + y
25     return z
26 p = sum(x,y)
27 print(p)

#code execution flow is: 23,26,23,24,25,26,27
```
# Parameters:
```
eg: def something(x,y,z):
        statements...

x - 1
y - 2
z - 3
```
### Calling parameters:
```
something(15,20,25)
```
- Are literals are passed
```
something(2,x,y)
```
- literals + Variables passed
```
something(x,y,z)
```
- All variables are passed

### Defining function parameters:
```
def something(x=0,y=0,z=0):
```
# returning values - 

- Single return
- Multiple return

- Three things that can be returned in a python return:
    - A literal
        `return 4`

    - A variable
	  `return h`

    - An expression
	  `return a + b`

- Functions can also not return any value.
```
def somemthing():
	print("something here")
```
# Scope of variables
- Global scope
- Variables defined in the top level statement are called the global scope variables.
- These variables can be accessed throughout the entire program.
```
eg:

x = 4
y = 5
z = int(input("Enter a value: "))
a = x + y + z
```
- Local scope
- Variables that are defined inside a flow control statement and can only be accessed inside the statement itself.
```
eg:
if(condition):
	s = "something"

print(s) #this will give an error "variable not defined"
```

- Scope of variables inside functions:
- LEGB rule
	- Local environment
	- Enclosed environment
	- Global environment
	- Built-in environment

- Local environment
```
eg:
def hi():
	hey = "hi" #Local environment variable
```
- Global environment
```
eg:
s = "hi jaanu"

def hi():
	print("hi" + s) #This will return an error

- to solve this, we do:

s = "hi jaanu"

def hi(s):
	print("hi" + s)

-- OR --

s = "hi jaanu"

def hi():
	global s #Global environment variable
	print("hi" + s)
```
- Enclosed environment
```
eg: if(condition):
	statements...

eg: 
if(a>b):
	s = "something" #Enclosed environment variable
```

- built-in environment
- Any variables defined inside a builtin library or a external module are called built in environment variables.
```
QUESTION:
s = 15

def something():
    s = 10
    print(s)

something()
print(s)

#output:
10
15
```

- Mutability and Immutability of variables in function and parameters

- Mutable parameters:
    - These parameter operations are performed on the same memory address

- Immutable parameters:
    - These parameter operations are performed on a copy of the created memory object

## TYPE LIBRARIES NOTES

# File Handling

- Types:
    - Text file
    - Binary file

- Text file
- Regular text files: .txt , .rtf, etc..
- Delimited text files: a,b,c,etc... 
    - delimiter: anything that separates 2 values in a file
    - Types of delimited files:
        - TSV (Tab Separated Values) - the data is separated by a "{TAB_SPACE}" 
        - CSV (Comma Separated Values) - the data is separated by a , (comma)

    eg: TSV file -
    Jannu   Sudeshna    Chandana    so,on...

    eg: CSV file - 
    Jannu,Sudeshna,Chandana,so,on...

- Binary file
- are 0s and 1s
- Python allows us to write and read in binary

- Reading and Writing data in python

- File system:
    - Working directory
    - Main directory (Hard drive/SSD/etc...)

    eg: path: "I:\2023 v1.0\J_prep\J_prep"
    working dir -> J_prep
    main dir -> I:

- Opening a file in python:
    - `open()`
    - format: {file_variable} = open({path_to_file})
    eg:
    file -> C:\Home\Desktop\keys.txt
    variable = open("C:\Home\Desktop\keys.txt")
    - this is an example of Object Oriented Programming (OOPs)
    
    variable = open("keys.txt")

    - Absolute path: from main dir to working dir and file name included
    - Relative path: only file name included


- Opening modes:
- Types of opening modes:
    - read mode
    - write mode
    - readwrite mode
    - read binary
    - write binary
    - readwrite binary
    - append

- Access modes:
    1. read mode - only reads data from the file
    open("file_name",'r')
    r -> read mode

    2. write mode - only writes data into the file
    open("file_name",'w')
    w -> write mode

    3. Readwrite mode - can do both read and writing to the file
    open("file_name",'r+')
    r+ -> read permission + write permission

    4. Read binary mode - only reads binary data.
    open("file_name",'rb')
    rb -> read in binary

    5. Write binary mode - only writing binary data.
    open("file_name",'wb')
    wb -> write in binary

    6. Readwrite binary - can do both reading and writing of binary files
    open("file_name",'r+b')
    r+b -> read permission + write permission in binary

    7. append mode
    open("file_name",'a')
    a -> append data to the file
    writes data onto a file
        - a+ - read data from a file

``` 
eg:
# to open a python file
var = open("names.txt",'r')
print(var)
```

- Closing opened files
- done using the `.close()` function
eg:
var.close() -> close the var variable/file

```
eg:
var = open("names.txt",'r')
print(var)
var.close()
```

- Reading data from files
- Types:
    - Read 
    read()
    format: {file_var}.read()

    eg:
    jannu hi this is python from a file
    read() -> jannu hi this is python from a file
    read(8) -> jannu hi

    - Readline
    readline()
    format: {file_var}.readline()

    eg:
    jannu hi this is python from a file
    readline() -> jannu hi this is python from a file

    eg:
    jannu hi this is python from a file
    this is another line in the file
    this is the third line
    this is the last line, trust me

    readline(2) ->  jannu hi this is python from a file\n <- EOL character (End Of Line)
                    this is another line in the file\n

    - Readlines
    readlines()

    This reads all the lines that are there in the file.

- Write data to files
- Types:
    - Write
    write()
    format: {file_var}.write(strings)

    eg:
    write("hi there")
    file -> hi there

    - Writelines
    writelines(["string 1","string 2"])
    format: {file_var}.writelines([LIST OF STRING HERE])

    eg:
    writelines(["hi there jaanu","this is a list of strings"])
    file -> hi there jaanu
            this is a list of strings

- Append data to files
    same as write function but adds the data to the end of the file.

- Flush function
    this is used when there is a lot of data to be written at the same time.
    this is to be used after completing all the write functions.
    
    {file_var}.flush()






