# MultiChoice
MultiChoice is a framework for generating formatted user input queries on the terminal.


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
    Question for the user.
- Param required: Optional Bool. Default=True
    True: Repeats question until answered.
    False: Accepts null input as an empty string.
- Param cursor: Optional String. Default='>>>' 
    Indicates user input field.


### Class: TrueFalse
`TrueFalse(query)`

TrueFalse: Generates True or False style questions.

`__call__(self)`
- Return: String. Returns the user selection.

`__init__(self, query, required=True, strict=True, cursor='>>>')`
- Param query: String.
    Question for the user.
- Param required: Optional Bool. Default=True
    True: Repeats question until answered.
    False: Accepts null input as an empty string.
- Param strict: Optional Bool. Default=True
    True: Answer must be in the options tuple. Not case-sensitive.
    False: Accepts any answer.
- Param cursor: Optional String. Default='>>>' 
    Indicates user input field.


### Class: MultiChoice
`MultiChoice(query, options)`

MultiChoice: Generates multiple choice style questions.

`__call__(self)`
- Return: String. Returns the user selection.

`__init__(self, query, options, required=True, strict=True, cursor='>>>')`
- Param query: String.
    Question for the user.
- Param options: Tuple of Strings.
    Options presented to the user as a numbered sequence. 
    Numbers are generated automatically.
    The user may enter an answer as text or one of the numbers.
- Param required: Optional Bool. Default=True
    True: Repeats question until answered.
    False: Accepts null input as an empty string.
- Param strict: Optional Bool. Default=True
    True: Answer must be in the options tuple. Not case-sensitive.
    False: Accepts any answer.
- Param cursor: Optional String. Default='>>>' 
    Indicates user input field.


## Developer Log

### MultiChoice v0.3.1
- Added custom cursor option.
- Documentation update

### MultiChoice v0.2 (internal)
- API update

### MultiChoice v0.1
- Initial Project
