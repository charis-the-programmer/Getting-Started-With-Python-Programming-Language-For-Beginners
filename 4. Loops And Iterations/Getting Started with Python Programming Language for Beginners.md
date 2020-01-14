# Getting Started with Python Programming Language for Beginners

This tutorial is designed for software programmers who need to learn Python programming language from scratch.  So before we get started let’s take a brief look at what Python is and what it has to offer.  

## What is Python & Why Learn It?

Python is a general-purpose interpreted, interactive, object-oriented, and high-level programming language. Python is a great language for the beginner-level programmers because it uses English keywords and it has fewer syntactical constructions than other languages. Python’s simple, easy to learn syntax emphasizes readability and therefore reduces the cost of program maintenance. 

**Python is Interpreted:** Python is processed at runtime by the interpreter. You do not need to compile your program before executing it. Since there is no compilation step, the edit-test-debug cycle is incredibly fast. Debugging Python programs is easy.

**Python is Interactive:** Python comes with a prompt which can be used to interact with the interpreter directly to write your programs, as well as interactive testing and debugging of snippets of code.

**Python is Object-Oriented:** Python supports Object-Oriented style or technique of programming that encapsulates code within objects. It also supports functional and structured programming methods.
Programmers often fall in love with Python because of the increased productivity it provides. 

Python's features include:

**A broad standard library:** Python supports modules and packages, which encourages program modularity and code reuse. The Python interpreter and the extensive standard library are available in source or binary form without charge for all major platforms, and can be freely distributed.

**Dynamic Semantics:** It provides very high-level dynamic data types and supports dynamic type checking. It combines its built in data structures with dynamic typing and dynamic binding which makes it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing components together.  It supports automatic garbage collection.

**Databases and GUI Programming:** Python provides interfaces to all major commercial databases. Python supports GUI applications that can be created and ported to many system calls, libraries, and windows systems. 
Portable: Python is available on a wide variety of platforms and has the same interface on all platforms e.g. including Windows, Linux and Mac OS X. We will understand how to set up our Python environment in the section on Downloading and Installing Python.

## Python Frameworks

Most developers use frameworks to create code and develop applications. The framework provides a defined structure to the developers so that you can focus on the core logic of the application rather than on other elements. There are generally two types of frameworks namely: Full Stack and Non Full Stack

### Full-Stack Frameworks

These are frameworks that provide complete support to developers, including necessary elements such as form validation, form generators, and template layouts. Some of the common full-stack frameworks are:

#### Django

Django, developed by Django Software Foundation, is a full-stack Python web framework. It is an open source and free-to-use framework, released officially in July 2005. It helps developers to create complex code and applications in an easier way, and requires much less time compared to other frameworks. It follows the principle of DRY (don’t repeat yourself) and a model-view-template architectural pattern. Django is widely used by most of the renowned companies such as Instagram, Pinterest, Disqus, Mozilla, The Washington Times, and Bitbucket. For more information about Django visit <a href="https://www.djangoproject.com/">https://www.djangoproject.com/</a>

#### Web2py

Web2py, developed by Massimo De Pierro, is a cross-platform web application framework written in Python programming language. It is an open source and free-to-use Python web framework, released in September 2007. It enables users to create dynamic web content in Python. The Web2py framework comes with a code editor, debugger, and deployment tool with which you can develop and debug code, as well as test and maintain applications. It incorporates a ticketing system, which issues a ticket to the user whenever an error occurs. This ticket helps the user to track the status of the error. For more information about Web2py visit <a href="http://www.web2py.com/">http://www.web2py.com/</a>

#### TurboGears 

TurboGears, developed by KevinDangoor and Mark Ramm, is a fullstack web application framework. It is a data-driven, open source and free-to-use Python web framework. With the help of components such as WebOb, SQLAlchemy, Genshi, and Repoze, you can easily developapplications that require database connectivity much faster as compared to other existing frameworks. For more information about TurboGears visit <a href="http://www.turbogears.org/">http://www.turbogears.org/</a> 

### Non-Full- Stack Frameworks

The non-full-stack frameworks do not provide additional functionalities and features to the users. Developers need to add a lot of code and other things manually. Some commonly used Python frameworks are:

#### Bottle 

Bottle, developed by Marcel Hellkemp, is a microframework. It is an easy-to-use lightweight framework generally used to build small web applications. It creates a single source file of every project or application. It has no other dependency than Python Standard Library. For more information about Bottle visit <a href="https://bottlepy.org/docs/dev/">https://bottlepy.org/docs/dev/</a>

#### Flask 

Flask, developed by Armin Ronacher, is a powerful Python web application framework. It is generally termed a microframework because it does not have the following elements: 
<ul>
<li>No database abstraction layer</li>
<li>No form validation</li>
<li>Specific tools and libraries</li> 
</ul>

For more information about Flask visit <a href="http://flask.pocoo.org/">http://flask.pocoo.org/</a>

#### CherryPy

CherryPy is an open source object-oriented Python framework. RemiDelon is known as the founder of the CherryPy project. The CherryPy framework is widely implemented by developers to create Python web applications. It has its own multi-threaded web server. For more information about CherryPy visit <a href="https://cherrypy.org/">https://cherrypy.org/</a>

Next we will go on to talk about what has been an interesting topic in the recent years among the coding community: which Python version is the best one to use:

## Python 3 vs. Python 2.7

Python 2.0 was first released in 2000. Its latest version, 2.7, was released in 2010. Python 3.0 was released in 2008. Its newest version, 3.8.1, was released in 2019.

Let’s take a look at some of the major differences between Python 2 vs. Python 3

**1. PYTHON 2 IS LEGACY, PYTHON 3 IS THE FUTURE.**

 Python 2 has been the most popular version for over a decade and a half, hence it is still entrenched in the software at certain companies. However, the version that is becoming obsolete and more companies are moving from Python 2 to 3.

**2. PYTHON 2 AND PYTHON 3 HAVE DIFFERENT (SOMETIMES INCOMPATIBLE) LIBRARIES**

Since Python 3 is the future, many of today's developers are creating libraries strictly for use with Python 3. Similarly, many older libraries built for Python 2 are not forwards-compatible.

**3. THERE IS BETTER UNICODE SUPPORT IN PYTHON 3**

In Python 3, text strings are Unicode by default. In Python 2, strings are stored as ASCII by default. This is important because Unicode is more versatile than ASCII. Unicode strings can store foreign language letters, Roman letters and numerals, symbols, emojis, etc., offering you more choices.

**4. PYTHON 3 HAS IMPROVED INTEGER DIVISION**

In Python 2, if you write a number without any digits after the decimal point, it rounds your calculation down to the nearest whole number. For example, if you type 5 /2, the result will be 2 due to rounding. However, in Python 3, the expression 5 / 2 will return the expected result of 2.5. Python 3 syntax is be more intuitive

**5. THE TWO VERSIONS HAVE DIFFERENT PRINT STATEMENT SYNTAXES**
 
Essentially, in Python 3, the print statement has been replaced with a print () function. For example, in Python 2 it is print “hello” but in Python 3 it is print (“hello”). 

**Conclusion**

Now, in 2020, it’s more of a no-brainer: Python 3 is the clear winner for new learners more notably because python 2.x is no longer being maintained. Further reading on this topic is available at <a href="https://www.djangoproject.com/">https://www.djangoproject.com/</a>

## Downloading and Installing Python

In this Python installation guide, you’ll see step by step how to set up a working Python 3 distribution on Windows, macOS, Linux, iOS, and Android. So let’s get started!

### Windows

**Step 1: Download the Python 3 Installer**

Open a browser window and navigate to the Download page for Windows at python.org. Click on the link for the Latest Python 3 Release - Python 3.x.x. (As of this writing, the latest is Python 3.8.5.)Select either Windows x86-64 executable installer for 64-bit or for 32-bit. 

**Step 2: Run the Installer**

Simply run the installer by double-clicking on the downloaded file. A dialog should appear. Ensure that the Install launcher for all users (recommended) and the Add Python 3.7 to PATH checkboxes at the bottom are checked. Then just click Install Now. Python should now be installed.

#### Veryifing

To try to verify installation,
Navigate to the directory Python was installed. Double-click the icon/file python.exe. A pop-up window will appear of the Python Interactive Prompt.

### Linux

There is a very good chance your Linux distribution has Python installed already, but it probably won’t be the latest version, and it may be Python 2 instead of Python 3. To upgrade to Python 3 on Linux go to and proceed to install.

### macOS / Mac OS X

While current versions of macOS (previously known as “Mac OS X”) include a version of Python 2, it is likely out of date by a few months. To upgrade to Python 3 go to and proceed to install.

## Installing a Python IDE (PyCharm)

PyCharm is a cross-platform editor developed by JetBrains. Pycharm provides all the tools you need for productive Python development.

**Step 1)** To download PyCharm visit the website <a href="https://www.jetbrains.com/pycharm/download/">https://www.jetbrains.com/pycharm/download/</a> and Click the "DOWNLOAD" link under the Community Section.

**Step 2)** Once the download is complete, run the exe for install PyCharm. The setup wizardshould have started. Click “Next”.

**Step 3)** On the next screen, Change the installation path if required. Click “Next”.

**Step 4)** On the next screen, you can create a desktop shortcut if you want and click on “Next”. Basic Python Syntax

**Step 5)** Choose the start menu folder. Keep selected JetBrains and click on “Install”.

**Step 6)** Wait for the installation to finish.

**Step 7)** Once installation finished, you should receive a message screen that PyCharm is installed. If you want to go ahead and run it, click the “Run PyCharm Community Edition” box first and click “Finish”.

### Visual Studio Code (Alternative to PyCharm)

Python 3 can be used in Visual Studio Code using the Python extension, which turns VS Code into a great lightweight Python IDE. You may find it to be a productive alternative to PyCharm. <a href="https://code.visualstudio.com/download">https://code.visualstudio.com/download</a>
There are other great IDEs out there which you can try out and find the one you are most comfortable with. Now that were done setting up or environment let’s begin writing some Python Code. 

## Basic Python Syntax

### Your First Python Program  

We will run the programs in different modes of programming.

#### Interactive Mode Programming:

Open your terminal or command prompt and type in the word "python" and press Enter, this will invoke the python interpreter and brings back the following prompt:
Type the following text at the Python prompt and press the Enter:

<code>
print("Hello, World!")
</code>

This produces the following result:

Hello, World!

#### Script Mode Programming

Write a simple program in a file and name it hello.py. Note: All Python files must have a .py extension. 

<code>print("Hello, Python!")
</code>

In your command prompt or terminal, run the program as follows

<code>python hello.py</code>

This produces the following result:

Hello, Python!

#### Python Keywords 

There are reserved words in python which cannot be used as a constant or variable names/ identifiers. All the Python keywords contain lowercase letters only. The following list shows the Python keywords. 

<table>
<tr>
    <td>False</td> <td>class</td>  <td>return</td> <td>is</td> <td>finally</td>
</tr>
<tr>    
    <td>None</td> <td>if</td> <td>for</td> <td>lambda</td> <td>continue</td>
</tr>
<tr>    
    <td>True</td> <td>def</td> <td>from</td> <td>while</td> <td>nonlocal</td>
</tr>
<tr>
    <td>and</td> <td>del</td> <td>global</td> <td>not</td> <td>with</td> 
</tr>
<tr>
<td>as</td> <td>elif</td> <td>try</td> <td>or</td> <td>yield</td> 
</tr>
<tr>    
<td>assert</td> <td>else</td> <td>import</td> <td>pass</td> <td>break</td>
</tr>
<tr>    
 <td>except</td> <td>in</td> <td>raise</td>
</tr>
<table>
    
#### Lines and Indentation

Python provides no braces to indicate blocks of code for class and function definitions or flow control. Blocks of code are denoted by line indentation, which is rigidly enforced. The number of spaces in the indentation is variable, but all statements within the block must be indented the same amount. For example: 

<code>if True:
	print( "True")
else:
	print( "False")
</code>
Thus, in Python all the continuous lines indented with same number of spaces would form a block. The following example has various statement blocks: Note: Do not try to understand the logic at this point of time. Just make sure you understood various blocks even if they are without braces.

#### Multi-Line Statements

Statements in Python typically end with a new line. Python does, however, allow the use of the line continuation character (\) to denote that the line should continue. For example:

<code>total  = 	item_one + \ <br>              item_two + \ <br>              item_three</code>

Statements contained within the [], {}, or () brackets do not need to use the line
continuation character. For example:

`days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']`

#### Quotation in Python

Python accepts single ('), double (") and triple (''' or """) quotes to denote string literals, as long as the same type of quote starts and ends the string.

The triple quotes are used to span the string across multiple lines. For example, all
the following are legal:

<code>word = 'word'
sentence = "This is a sentence."
paragraph = """This is a paragraph. It is
made up of multiple lines and sentences."""
</code>

#### Comments in Python

A hash sign (#) that is not inside a string literal begins a comment. All characters after the # and up to the end of the physical line are part of the comment and the Python interpreter ignores them.

<code>#First comment
print "Hello, Python!"; # second comment
This produces the following result:
You can type a comment on the same line after a statement or expression:
You can comment multiple lines as follows:
</code>

#### Waiting for the User

The following line of the program displays the prompt, the statement saying “Press the enter key to exit”, and waits for the user to take action:

<code>input("Press the enter key to exit.")
</code>

Once the user presses the key, the program ends. This is a nice trick to keep a console
window open until the user is done with an application.

## Chapter 1: Variables and Expressions
### Variables 

A variable is a named place in the memory where a programmer can store data and later retrieve the data using the variable "name".A programmer gets to choose the names of the variables and can change the contents of a variable in a later statement

**Sample Code**

<code>X = 12.2
y = 14
x = 100
</code>
    
Python variables have the following naming rules:
<ul>
    <li>must start with a letter or underscore _</li>
    <li>may consist of letters, numbers and underscores</li>
    <li>they are case sensitive</li> 
</ul>

for example some good variable names are: <br>
`spam eggs spam23 _speed_`<br>

and some bad examples are<br>
`23spam sign var.12`<br>

`spam Spam and SPAM` are 3 different variables 

**Example 01**

<code>hours = 35.0
rate = 12.50
pay  = hours * rate
print(pay)
</code>
    
### Constants 
 
Fixed values such as numbers letters and strings are called constants because they do not change
examples of numeric constants are: 123, 3.14 
a string constant uses single quotes (') or double quotes (") for example: 'Hello World' 

### Assignment Statements

We can assign a value to a variable using the assignment statement (=)
An assignment statement consists of an expression on the right hand side and a variable to store the result.

**Example 02** 

`x = 12 * 4`<br>

the result will give x being assigned the value 48. Another example

```x = 0.6
x = 1.2 * x * ( 1 - x)
``` 
<br>

The result will give x being assigned the value 0.228

### Numeric Expressions

<table >
    <th>Operator</th> <th> Operation</th>
    <tr>
        <td>+</td> <td>Addition</td>
    </tr>
    <tr>
        <td>-</td><td>Subtraction</td>
    </tr>
    <tr>
        <td>*</td><td>Multiplication</td>
    </tr>
    <tr>
        <td>/</td><td>Division</td>
    </tr>
    <tr>
        <td>**</td><td>Power</td>
    </tr>
    <tr>
        <td>%</td><td>Remainder</td>
    </tr>
</table>

**Example 03**

<code>x = 2
x = x + 2
print(x)
</code>

Result: 4

<code>y = 45 * 21
print(y)
</code>

Result: 945

<code>z = y/100
print(z)
</code>

Result: 9.45

<code>j = 23
k = j%5
print(k)
</code>

Result: 3

<code>print(4**3)
</code>

Result: 64

##### Operator Order of Precendence Rules

Highest precedence rule to lowest precedence rule:
<ol>
<li>Parentheses are always respected first</li> 
<li>Exponentiation (raises to a power) second</li>
<li>Multiplication, Division, and Remainder third</li>
<li>Addition and Subtraction last</li>
</ol>
In Python variables, literals and constants have a type. Some operations are prohibited such as adding a number to a string. We can ask python what type a particular variable is by using the type() function

**Example 04**

<code>w = "hello"
print(type(w))
</code>
    
Result: <class'str'>

<code>r = 1
print(type(r))
</code>

Result: <class'int'>

There are two main types of numbers: <br>
**Integers** which are whole numbers for example -14, -2, 0, 1, 100, 401233 <br>
**Floating Point Numbers** which have decimal parts -2.5, 0.0, 98.6, 14.0 <br>
Every other number types are variations of float and integer type

### Type Conversions

**Numeric Conversions**

When you put an integer and a floating point in an expression, the integer is implicitly converted to a float.
We can control this with the built-in functions int() and float() for example

**Example 05**

<code>print(float(99) + 100)</code>

Result: 199.0

Integer Division produces a floating point result

<code>print(10/2)</code>

Result: 5.0

**String Conversions**

We can also use int() and float() to convert strings and integers. Note: You will get an error if the string does not contain numeric characters

**Example 06**

<code>v = '123'
print(type(v))</code>

Result: <class'str'>

<code>w = int(v)
print(type(v))</code>

Result: <class'int'>


## Chapter 2: Conditional Statements

Conditional statements help to specify actions taken in anticipation of conditions occurring while execution of the program which is effectively  decision making. When we need to determine which action to take and which statements to execute expressions which produce TRUE or FALSE as outcome are evaluated. Python programming language provides following types of decision making statements.


### If Statement

It consists of a boolean expression followed by one or more statements

**Example 01**

<code>x = 5
if x < 10:
    print("Smaller")
if x > 20:
    print("Bigger")
print("End")
</code>
    
**Output:**
Smaller <br>
End


### Comparison Operators

Comparison Operators only look at the variables but do not change the contents of these variables
Boolean Expressions using comparison operators evaluate to either True / False

<table >
    <th>Sign</th> <th>Meaning</th>
    <tr>
        <td> < </td> <td>Less than</td>
    </tr>
    <tr>
        <td> <= </td><td>Less than or Equal to</td>
    </tr>
    <tr>
        <td>==</td><td>Equal to</td>
    </tr>
    <tr>
        <td>>= </td><td>Greater than or Equal To</td>
    </tr>
    <tr>
        <td>> </td><td>Greater than</td>
    </tr>
    <tr>
        <td>!= </td><td>Not equal</td>
    </tr>
</table>
 
 
### If...Else Statement

An if statement can be followed by an optional else statement, which
executes when the boolean expression is FALSE. 

**Example 02**

<code>x = 4
if x > 2:
    print("Bigger")
else:
print("Smaller")
print("Done")
    
</code>
    
**Output:** <br>
Bigger <br>
Done

### elif Statement

The elif statement allows you to check multiple expressions for TRUE and execute a block of code as soon as one of the conditions evaluates to TRUE.

**Example 03**

<code>x=0
if x < 2 :
    print("Small")
elif x < 10 :
    print("Medium")
else:
    print("Large")
print("Done")
</code>

**Output:** <br>
Small <br>
Done

### Try/Except Structure

If you have some suspicious code that may raise an exception, you can defend your program by placing the suspicious code in a try: block. After the try:block, include an except: statement, followed by a block of code which handles the problem as elegantly as possible.

**Example 04**

<code>str1 = "Hello John"
try:
    str2 = int(str1)
except: 
    str2 = -1
print("First ", str2)
str1 = "123"
try:
    str2 = int(str1)
except: 
    str2 = -1
print("Second ", str2)
</code>

**Output:** <br>
First -1 <br>
Second 123

**Explanation**

The suspicious code in the above program is attempting to convert a string into an integer.
When the first conversion fails - the except clause is executed and the program continues. When the second conversioon succeeds the except clause is skipped and the program countinues.  


## Chapter 3: Using and Building Functions

A function is a block of organized, reusable code that is used to perform a single, related action. Functions provide better modularity for your application and a high degree of code reusing.

### Defining a Function

Defining a function only gives it a name, specifies the parameters that are to be included in the function and structures the blocks of code.

**Example 01** 

<code>def thing():
    print("Hello")
    print("Fun")
</code>    
    
### Calling a Function
Once the basic structure of a function is finalized, you can execute it by calling it from another function or directly from the Python prompt. Following is the example to call the thing() function:

<code>thing()
print("Hey")
thing()
</code>

**Output:** <br>
Hello <br>
Fun<br>
Hey<br>
Hello<br>
Fun

### Arguments

An argument is a value we pass into the function as its input when we call the function. We can use arguments to direct the function to do different kinds of work when we call it at different times. We put the arguments in parentheses after the name of the function

A parameter is a variable which we use in the function definition. It is a "handle" that allows the code in the function to access the arguments for a particular function invocation.

**Example 02**

<code>def greet(lang):
    if lang == "es":
        print("Hola")
    elif lang == "fr":
        print("Bonjour")
    else:
        print("Hello")
</code>


Calling the function and passing in the argument <i>"en"</i> as shown below:

<code>greet("en")</code>

will produce the following result

**Output:**
Hello

Calling the function and passing in the argument <i>"es"</i> as shown below:

<code>greet("es")</code>

will produce the following result

**Output:**
Hola

And finally calling the function and passing in the argument <i>"fr"</i> as shown below:

<code>greet("fr")</code>

will produce the following result

**Output:**
Bonjour


### Return Values 

Often a function will take arguments, do some computation and return a value to be used as the value of the function all in the calling expression. The return keyword is used for this.

**Example 03**

<code>def greet():
    return "Hello "
   
    
print(greet(), "Glenn")
print(greet(), "Sally")
</code>

**Output:**

Hello Glenn <br>
Hello Sally

### Multiple Parameters/ Arguments

We can define more than one parameter in the function definition. We simplyadd more arguments when we call the function. We match the number and order of arguments and parameters

**Example 04**

<code>def add(a, b):
    sum = a + b
    return sum
    
x = add(5, 6)
print(x)
</code>

**Output:**

11

## Chapter 4: Loops and Iterations

There may be a situation when you need to execute a block of code several number of times. A loop statement allows us to execute a statement or group of statements multiple times. Python programming language provides following types of loops to handle looping requirements.

Loops (repeated steps) have iteration variables that change each time through a loop. Often these iteration variables go through a sequence of numbers. 

### While Loop

A while loop statement in Python programming language repeatedly executes a
target statement as long as a given condition is true.

**Example 01**

<code>n = 5
while n > 0:
    print(n)
    n = n - 1
print("TakeOff")
print(n)
</code>

**Output**

5 <br>
4 <br>
3 <br>
2 <br>
1 <br>
TakeOff! <br>
0 

### The Infinite Loop

A loop becomes infinite loop if a condition never becomes FALSE. You must use
caution when using while loops because of the possibility that this condition never resolves to a FALSE value. This results in a loop that never ends hence infinite loop.


**Example 02**

<code>n = 5
while n > 0:
    print("Eat")
    print("Work")
print("Sleep")
</code>

### Breaking out of a Loop

The break statement ends the current loop and jumps to the statement immediately following the loop. 

**Example 03**

<code>while True:
    line = input(">")
    if line == "done":
        break
     print(line)
print("Done!")
</code>

Entering the input say <i>"hello there"</i> will produce the following result:

**Output:**

hello there

Entering another input say <i>"finished"</i> will produce the following result:

**Output:**

finished

And finally entering the input <i>"done"</i> will produce break out the the following result:

**Output:**

Done!

### Finishing an Iteration with Countinue

The continue statement ends the current iteration and jumps to the top of the loop and starts the next iteration

**Example 03**

<code>while True:
    line = input(">")
    if line[0] == "#":
        continue
    if line == "done":
        break
     print(line)
print("Done!")
</code>

Entering the input say <i>"hi there"</i> will produce the following result:

**Output:**

hi there

Entering another input say <i>"# don't print this"</i> will produce the following result:

**Output:**


Entering another input say <i>"print this!"</i> will produce the following result:

**Output:**

print this!

And finally entering another input say <i>"done"</i> will produce the following result:

**Output:**

Done!

### For Loop

It has the ability to iterate over the items of any sequence, such as a list or a string.

If a sequence contains an expression list, it is evaluated first. Then, the first item in the sequence is assigned to the iterating variable. Next, the statements block is executed. Each item in the list is assigned to the iterating variable, and the statement(s) block is executed until the entire sequence is exhausted.

**Example 04 a**

<code>for i in [5,4,3,2,1]:
    print(i)
print("Blastoff")
</code>

**Output 04 a: **

5 <br>
4 <br>
3 <br>
2 <br>
1 <br>
Blastoff

**Program 04 b:**

<code>friends = ["John", "Sally", "Patel"]
for friend in friends:
    print("Happy New Year:", friend)
print("Done")
</code>

**Output 04 b: **

The iteration variable "iterates" through the sequence (ordered set)
The block (body) of code is executed once for each value in the sequence
The iteration variable moves through all the values in the sequence

### Pass Statement

It is used when a statement is required syntactically but you do not want any
command or code to execute.The pass statement is a null operation; nothing happens when it executes.The pass is also useful in places where your code will eventually go, but has not been written yet.

**Example 05**

<code>for letter in 'Python':
    if letter == 'h':
        pass
        print('This is pass block')
    print('Current Letter :', letter)
print("Good bye!")
</code>

**Output:**

Current Letter : P
Current Letter : y
Current Letter : t
This is pass block
Current Letter : h
Current Letter : o
Current Letter : n
Good bye!


### Nested Loops

Python programming language allows to use one loop inside another loop. 

The following program uses a nested for loop to find the prime numbers from 2 to
100:

**Example 06**

<code>i = 2
while(i < 100):
    j = 2
    while(j <= (i/j)):
        if not(i%j): break
        j = j + 1
    if (j > i/j) : print(i, " is prime")
    i = i + 1
    
print("Good bye!")
</code>

**Output:**

2 is prime
3 is prime
5 is prime
7 is prime
11 is prime
13 is prime
17 is prime
19 is prime
23 is prime
29 is prime
31 is prime
37 is prime
41 is prime
43 is prime
47 is prime
53 is prime
59 is prime
61 is prime
67 is prime
71 is prime
73 is prime
79 is prime
83 is prime
89 is prime
97 is prime
Good bye!


## Further Steps 

Now,with this we have reached the end of our Introduction to  Python Tutorial. Congratulations for having gotten this far, you are well on you way to becoming an Advanced Python Developer!!! 


## References

<ul>

<li> Python Tutorials Point - <br>
    
<a href="https://www.tutorialspoint.com/">https://www.tutorialspoint.com/</a> </li>

<br>

<li> Python Documentation - <br>
    
<a href="https://www.tutorialspoint.com/">https://www.tutorialspoint.com/</a> </li>

<br>

<li>Code Repository - <br>
    
<a href="https://github.com/shumbaashley/Getting-Started-With-Python-Programming-Language-For-Beginners">https://github.com/shumbaashley/Getting-Started-With-Python-Programming-Language-For-Beginners</a> </li>

<br>
</ul>
