INTEGER, PLUS, MINUS, NONE = 'integer', 'plus', 'minus', 'none'

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value
    


class Interpeter:

    def __init__(self, input):
        self._input = input
        self._index = -1
    
    def skip_spaces(self):
        while self._peek() is not None and self._peek().isspace():
            self._index += 1

    def _advance(self):
        self.skip_spaces()        
        c = self._peek()
        self._index += 1
        return c

    def _peek(self):
        if self._index + 1 > len(self._input) - 1:
            return None
        return self._input[self._index + 1]

    def _integer(self, c):
        result = c
        next_char = self._peek()    
        while next_char is not None and next_char.isnumeric():
            c = self._advance()
            result += c
            next_char = self._peek()
        return Token(INTEGER, int(result))

    def _operator(self, c):
        if c == '+':
            return Token(PLUS, '+')
        if c == '-':
            return Token(MINUS, '-')

    def _lexer(self):
        next_char = self._advance()
        if next_char is None:
            return Token(NONE, None)
        
        if next_char.isnumeric():
            return self._integer(next_char)
        else:
            return self._operator(next_char)

    def result(self):
        operand = self._lexer()
        result = operand.value
        while not operand.type == NONE:
            operator = self._lexer()
            operand = self._lexer()

            if operator.type == PLUS:
                result += operand.value
            elif operator.type == MINUS:
                result -= operand.value

        return result


while True:
    print(Interpeter(input('calc> ')).result())