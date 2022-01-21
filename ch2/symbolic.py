variables = {'x': 1, 'y': 2, 'z': 3}

class Function():

    def __init__(self, expr=''):
        self._expr = expr

    def __str__(self):
        return self._expr

    def is_constant(self):
        return len(self._expr) == 1 and self._expr not in variables

    def is_var(self):
        return self._expr in variables

    def same_var(self, var):
        return self._expr == var

    def set_expr(self, new_expr):
        self._expr = new_expr

    def is_sum(self):
        return self._expr.split()[0] == '+'

    def is_prod(self):
        return self._expr.split()[0] == '*'

    def addend(self):
        return Function(self._expr.split()[1])

    def augend(self):
        return Function(self._expr.split()[2])

    def is_number(self, n=None):
        if n is None:
            return self._expr.isdigit()
        else:
            return str(n) == self._expr

    def make_op(self, op, f1, f2):
        if f1.is_number(0):
            if op == '+':
                self._expr = f2._expr
            if op == '*':
                self._expr = '0'
        elif f2.is_number(0):
            if op == '+':
                self._expr = f1._expr
            if op == '*':
                self._expr = '0'
        elif f1.is_number(1) and op == '*':
            self._expr = f2._expr
        elif f2.is_number(1) and op == '*':
            self._expr = f1._expr
        elif f1.is_number() and f2.is_number():
            if op == '+':
                self._expr = str(int(f1._expr) + int(f2._expr))
            elif op == '*':
                self._expr = str(int(f1._expr) * int(f2._expr))
        else:
            self._expr = op + ' ' + f1._expr + ' ' + f2._expr

    @staticmethod
    def make_sum(f1, f2):
        res = Function()
        res.make_op('+', f1, f2)
        return res

    def multiplier(self):
        return Function(self._expr.split()[1])

    def multiplicand(self):
        return Function(self._expr.split()[2])

    @staticmethod
    def make_prod(f1, f2):
        res = Function()
        res.make_op('*', f1, f2)
        return res

    def diff(self, var):
        deriv = Function()
        if self.is_constant():
            deriv.set_expr('0')
        elif self.is_var():
            if self.same_var(var):
                deriv.set_expr('1')
            else:
                deriv.set_expr('0')
        elif self.is_sum():
            addend = self.addend()
            augend = self.augend()
            deriv = Function.make_sum(addend.diff(var),
                                      augend.diff(var))
        elif self.is_prod():
            multiplier = self.multiplier()
            multiplicand = self.multiplicand()
            deriv = Function.make_sum(
                Function.make_prod(multiplier,
                                   multiplicand.diff(var)),
                Function.make_prod(multiplier.diff(var),
                                   multiplicand)
            )
        else:
            raise Exception('unknown expression')
        return deriv

def main():
    f1 = Function('+ x 3')
    print(f1)
    print(f1.diff('x'))
    f2 = Function('* x y')
    print(f2)
    print(f2.diff('x'))
    # f3 = Function('* * x y + x 3')
    # print(f3)
    # print(f3.diff('x'))

main()
