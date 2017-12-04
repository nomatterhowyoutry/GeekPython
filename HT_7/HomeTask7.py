class Calc(object):
    ''' Simplest calc class '''
    last_result = 0 # returns last operation result
    f = open('result.txt', 'w')
    f.write('Start of a Session\n')

    def add(self, x ,y):
        ''' addition '''
        self.last_result = x + y
        self.write('Addition: ' + str(self.last_result))

    def sub(self, x ,y):
        ''' substraction '''
        self.last_result = x - y
        self.write('Substraction: ' + str(self.last_result))

    def mult(self, x ,y):
        ''' multiplication '''
        self.last_result = x * y
        self.write('Multiplication: ' + str(self.last_result))

    def div(self, x ,y):
        ''' division '''
        self.last_result = x / y
        self.write('Division: ' + str(self.last_result))

    def write(self, input):
        self.f.write(input + '\n')

    @staticmethod
    def end():
        Calc().f.write('End of a Session')
        Calc().f.close()

calc = Calc()
calc.add(5,3)
calc.mult(2,3)
calc.sub(10,2)
calc.div(27,9)
Calc.end()