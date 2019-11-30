""" MultiChoice
MultiChoice is a framework for generating formatted user input questions.

Author: Robert Sharp
Date: November 30, 2019
"""


class MultiChoice:
    """ MultiChoice: generates multiple choice questions. """
    cursor = ":> "

    def __init__(self, prompt, options, required=True, strict=True):
        """ Multiple Choice
        :param prompt: String.
            Question, query or prompt for the user.
        :param options: Tuple of Strings.
            Options presented to the user as a numbered sequence.
            The user may enter an answer as text or one of the numbers.
        :param required: Bool. Default=True:
            True: Repeats question until answered.
            False: Accepts null input as an empty string.
        :param strict: Bool. Default=True
            True: Answer must be in the options tuple. Not case-sensitive.
            False: Accepts any answer. """
        self.prompt = prompt
        self.options = options
        self.required = required
        self.strict = strict
        self.data = {
            str(k + 1): v.lower() for k, v in enumerate(self.options)
        }
        self.choice_pack = (
            self.prompt,
            *(f"{k}. {v.title()}" for k, v in self.data.items()),
            self.cursor,
        )

    def _get_answer(self):
        return input('\n'.join(self.choice_pack)).lower()

    def __call__(self):
        """
        :return: String. Returns the user selection.
        """
        selection = self._get_answer()
        if selection in self.data.values():
            return selection.title()
        elif selection in self.data.keys():
            return self.data[selection].title()
        elif selection and not self.strict:
            return selection.title()
        elif not self.required:
            return selection.title()
        else:
            return self()


class FillBlank(MultiChoice):
    """ FillBlank: generates fill-in-the-blank questions. """

    def __init__(self, prompt, required=True):
        """ Fill in the Blank
        :param prompt: String.
            Question, query or prompt for the user.
        :param required: Bool. Default=True:
            True: Repeats question until answered.
            False: Accepts null input as an empty string. """
        super().__init__(
            prompt, options=(), required=required, strict=False)


class TrueFalse(MultiChoice):
    """ TrueFalse generates True or False questions. """

    def __init__(self, prompt, required=True, strict=True):
        """ True or False
        :param prompt: String.
            Question, query or prompt for the user.
        :param required: Bool. Default=True:
            True: Repeats question until answered.
            False: Accepts null input as an empty string.
        :param strict: Bool. Default=True
            True: Answer must be in the options tuple. Not case-sensitive.
            False: Accepts any answer. """
        super().__init__(
            prompt, options=("True", "False"), required=required, strict=strict)
