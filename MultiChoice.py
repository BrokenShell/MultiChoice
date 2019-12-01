""" MultiChoice
A framework for generating well formatted user input queries in the terminal. """


class MultiChoice:
    """ MultiChoice: generates multiple choice style questions. """

    def __init__(self, query, options, required=True, strict=True, cursor=">>>"):
        """ Multiple Choice Questions
        :param query: String.
            Question for the user.
        :param options: Tuple of Strings.
            Options presented to the user as a numbered sequence.
            The user may enter an answer as text or one of the numbers.
        :param required: Bool. Default=True:
            True: Repeats question until answered.
            False: Accepts null input as an empty string.
        :param strict: Bool. Default=True
            True: Answer must be in the options tuple. Not case-sensitive.
            False: Accepts any answer.
        :param cursor: String. Default='>>>' Indicates user input field.
        """
        self.cursor = cursor + ' '
        self.prompt = query
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
        Gets the answer from the user.
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


class Question(MultiChoice):
    """ Question: generates fill in the blank style questions.  """

    def __init__(self, query, required=True, cursor=">>>"):
        """ Fill in the Blank Questions
        :param query: String.
            Question for the user.
        :param required: Bool. Default=True:
            True: Repeats question until answered.
            False: Accepts null input as an empty string.
        :param cursor: String. Default='>>>' Indicates user input field.
        """
        super().__init__(
            query, options=(), required=required, strict=False, cursor=cursor)


class TrueFalse(MultiChoice):
    """ TrueFalse generates True or False style questions. """

    def __init__(self, query, required=True, strict=True, cursor=">>>"):
        """ True or False Questions
        :param query: String.
            Question for the user.
        :param required: Bool. Default=True:
            True: Repeats question until answered.
            False: Accepts null input as an empty string.
        :param strict: Bool. Default=True
            True: Answer must be in the options tuple. Not case-sensitive.
            False: Accepts any answer.
        :param cursor: String. Default='>>>' Indicates user input field.
        """
        super().__init__(
            query, options=("True", "False"),
            required=required, strict=strict, cursor=cursor)
