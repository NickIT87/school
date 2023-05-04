class KS(object):
    # elementary base functions
    def conjunctor(self, a: bool | int, b: bool | int) -> bool | int:
        return a and b

    def desjunctor(self, a: bool | int, b: bool | int) -> bool | int:
        return a or b

    def invertor(self, a: bool | int) -> bool | int:
        return not a

    # schemes
    def emergency_exit(self, x: bool | int, y: bool | int, z: bool | int) -> bool | int:
        left_side_of_equation = self.conjunctor(self.invertor(self.desjunctor(x, y)), self.conjunctor(x, y))
        right_side_of_equation = self.conjunctor(self.conjunctor(x, self.invertor(y)), z)
        return int(self.desjunctor(left_side_of_equation, right_side_of_equation))
    
    def decoder(self, x: bool | int, y: bool | int) -> bool | int:
        responce = []
        responce.append(int(self.conjunctor(self.invertor(x), self.invertor(y))))
        responce.append(int(self.conjunctor(self.invertor(x), y)))
        responce.append(int(self.conjunctor(x, self.invertor(y))))
        responce.append(int(self.conjunctor(x, y)))
        return responce
    
    def encoder(self, x, y, z, f):
        responce = []
        responce.append(int(self.desjunctor(z, f)))
        responce.append(int(self.desjunctor(y, f)))
        return responce


solver = KS()
print(solver.emergency_exit(1, 0, 1))

print(solver.decoder(1, 1))
print(solver.decoder(1, 0))
print(solver.decoder(0, 1))
print(solver.decoder(0, 0))

print(solver.encoder(0, 0, 0, 1))
print(solver.encoder(0, 0, 1, 0))
print(solver.encoder(0, 1, 0, 0))
print(solver.encoder(1, 0, 0, 0))
