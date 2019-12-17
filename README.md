# MultiChoice
A framework for generating well formatted user input queries in the terminal.


### Table of Contents
- API Documentation
    - Question: Fill-in-the-blank
    - TrueFalse: True or False
    - MultiChoice: Multiple Choice
- Developer Log


## API Documentation

### Class: Question
`Question(query)`

Question: Generates fill in the blank style questions.

`__call__(self)`
- Return: String. Returns the user selection.

`__init__(self, query, required=True, cursor='>>>')`
- Param query: String.
    - Question for the user.
- Param required: Optional Bool. Default=True
    - True: Repeats question until answered.
    - False: Accepts null input as an empty string.
- Param cursor: Optional String. Default='>>>' 
    - Indicates user input field.

#### Question Example
```python
from MultiChoice import Question


get_name = Question("What is your name?")  # setup
user = get_name()                          # get input
print(user)                                # print
```
```
What is your name?
>>> Robert
Robert
```

### Class: TrueFalse
`TrueFalse(query)`

TrueFalse: Generates True or False style questions.

`__call__(self)`
- Return: String. Returns the user selection.

`__init__(self, query, required=True, cursor='>>>')`
- Param query: String.
    - Question for the user.
- Param required: Optional Bool. Default=True
    - True: Repeats question until answered.
    - False: Accepts null input as an empty string.
- Param cursor: Optional String. Default='>>>' 
    - Indicates user input field.

#### TrueFalse Example
```python
from MultiChoice import TrueFalse


question = TrueFalse("True or False: Python3 is the best!")
answer = question()
print(answer)
```
```
True or False: Python3 is the best!
1. True
2. False
>>> 1
True
```


### Class: MultiChoice
`MultiChoice(query, options)`

MultiChoice: Generates multiple choice style questions.

`__call__(self)`
- Return: String. Returns the user selection.

`__init__(self, query, options, required=True, strict=True, cursor='>>>')`
- Param query: String.
    - Question for the user.
- Param options: Tuple of Strings.
    - Options presented to the user as a numbered sequence. 
    - Numbers are generated automatically.
    - The user may enter an answer as text or one of the numbers.
- Param required: Optional Bool. Default=True.
    - True: Repeats question until answered.
    - False: Accepts null input as an empty string.
- Param strict: Optional Bool. Default=True.
    - True: Answer must be in the options tuple. Not case-sensitive.
    - False: Accepts any answer.
- Param cursor: Optional String. Default='>>>'
    - Indicates user input field.

#### MultiChoice Example
```python
from MultiChoice import MultiChoice


question = MultiChoice(
    "What is your favorite color?\n"
    "You must choose one of the following:",
    options=("Red", "Orange", "Yellow", "Green", "Blue", "Purple"),
)
answer = question()
print(answer)
```
```
What is your favorite color?
You must choose one of the following:
1. Red
2. Orange
3. Yellow
4. Green
5. Blue
6. Purple
>>> blue
Blue
```


## Developer Log
### MultiChoice v0.3.5
- TrueFalse update, removed strict option - T/F is always strict.

### MultiChoice v0.3.4
- Installer Bug Fixed

### MultiChoice v0.3.3
- Comments Updated

### MultiChoice v0.3.2
- Examples Added

### MultiChoice v0.3.1
- Added Cursor Option

### MultiChoice v0.2 (internal)
- API Updated

### MultiChoice v0.1
- Initial Upload
