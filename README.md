# MultiChoice
MultiChoice is a framework for generating formatted user input queries on the terminal. Especially multiple choice questions.

## Class: MultiChoice
`MultiChoice(query, options, required=True, strict=True)`

MultiChoice: Generates multiple choice questions.

`__call__(self)`
- Return: String. Returns the user selection.

`__init__(self, query, options, required=True, strict=True)`
- Param query: String.
    Question for the user.
- Param options: Tuple of Strings.
    Options presented to the user as a numbered sequence.
    The user may enter an answer as text or one of the numbers.
- Param required: Bool. Default=True:
    True: Repeats question until answered.
    False: Accepts null input as an empty string.
- Param strict: Bool. Default=True
    True: Answer must be in the options tuple. Not case-sensitive.
    False: Accepts any answer.

 
## Class: Question
`Question(query, required=True)`

Question: Generates fill in the blank style questions.

`__call__(self)`
- Return: String. Returns the user selection.

`__init__(self, query, required=True)`
- Param query: String.
    Question for the user.
- Param required: Bool. Default=True:
    True: Repeats question until answered.
    False: Accepts null input as an empty string.


## Class: TrueFalse
`TrueFalse(query, required=True, strict=True)`

TrueFalse: Generates True or False style questions.

`__call__(self)`
- Return: String. Returns the user selection.

`__init__(self, query, required=True, strict=True)`
- Param query: String.
    Question for the user.
- Param required: Bool. Default=True:
    True: Repeats question until answered.
    False: Accepts null input as an empty string.
- Param strict: Bool. Default=True
    True: Answer must be in the options tuple. Not case-sensitive.
    False: Accepts any answer.
