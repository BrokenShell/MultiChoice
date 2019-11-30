# MultiChoice
MultiChoice is a framework for generating formatted user input questionnaires.


## Class: MultiChoice
`MultiChoice(prompt, options, required=True, strict=True)`

Generates multiple choice questions.

`__call__(self)`
- Return: String. Returns the user selection.

`__init__(self, prompt, options, required=True, strict=True)`
- Param prompt: String.
    Question, query or prompt for the user.
- Param options: Tuple of Strings.
    Options presented to the user as a numbered sequence.
    The user may enter an answer as text or one of the numbers.
- Param required: Bool. Default=True:
    True: Repeats question until answered.
    False: Accepts null input as an empty string.
- Param strict: Bool. Default=True
    True: Answer must be in the options tuple. Not case-sensitive.
    False: Accepts any answer.

 
## Class: FillBlank
`FillBlank(prompt, required=True)`

FillBlank: generates fill-in-the-blank questions.

`__call__(self)`
- Return: String. Returns the user selection.

`__init__(self, prompt, required=True)`
- Param prompt: String.
    Question, query or prompt for the user.
- Param required: Bool. Default=True:
    True: Repeats question until answered.
    False: Accepts null input as an empty string.


## Class: TrueFalse
`TrueFalse(prompt, required=True, strict=True)`

TrueFalse generates True or False questions.

`__call__(self)`
- Return: String. Returns the user selection.

`__init__(self, prompt, required=True, strict=True)`
- Param prompt: String.
    Question, query or prompt for the user.
- Param required: Bool. Default=True:
    True: Repeats question until answered.
    False: Accepts null input as an empty string.
- Param strict: Bool. Default=True
    True: Answer must be in the options tuple. Not case-sensitive.
    False: Accepts any answer.
