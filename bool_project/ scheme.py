class KS(object):
    def conjunctor(self, a: bool | int, b: bool | int) -> bool | int:
        return a and b

    def desjunctor(self, a: bool | int, b: bool | int) -> bool | int:
        return a or b

    def invertor(self, a: bool | int) -> bool | int:
        return not a

    def solve(self, x: bool | int, y: bool | int, z: bool | int) -> bool | int:
        left_side_of_equation = self.conjunctor(self.invertor(self.desjunctor(x, y)), self.conjunctor(x, y))
        right_side_of_equation = self.conjunctor(self.conjunctor(x, self.invertor(y)), z)
        return int(self.desjunctor(left_side_of_equation, right_side_of_equation))
    
solver = KS()
print(solver.solve(1, 0, 1))
print(solver.solve(1, 1, 1))
print(solver.solve(0, 0, 1))
print(solver.solve(1, 0, 0))
print(solver.solve(0, 0, 0))
print(solver.solve(True, False, True))