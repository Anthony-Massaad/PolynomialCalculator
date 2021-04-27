class Function:
    def __init__(self, *coeff):
        self._coeff = list(coeff)
        self._function = ""

    def __str__(self) -> str:
        zero_checking = 0
        for i in range(0, len(self._coeff)):
            if self._coeff[i] != 0:
                self._function += str('{:0.1f}'.format(self._coeff[i]))
                if len(self._coeff) - (i + 1) >= 1:
                    self._function += "x^" + str((len(self._coeff) - (i + 1)))
                    break
            zero_checking += 1

        if all(elem == 0 for elem in self._coeff):
            return "0"

        for i in range(zero_checking + 1, len(self._coeff)):
            if self._coeff[i] == 0:
                continue
            elif self._coeff[i] > 0:
                self._function += " + " + str('{:0.1f}'.format(self._coeff[i]))
            elif self._coeff[i] < 0:
                self._function += " - " + str('{:0.1f}'.format(abs(self._coeff[i])))
            if len(self._coeff) - (i + 1) >= 1:
                self._function += "x^" + str(len(self._coeff) - (i + 1))

        return self._function

    def getFunction(self):
        return self._function

    def __repr__(self):
        return 'Function({0})'.format(self._coeff)

    def __add__(self, other):
        if isinstance(other, Function):
            f1 = self._coeff[::-1]
            f2 = other._coeff[::-1]
            added = []
            for i in range(len(f1)):
                try:
                    added.append(f1[i] + f2[i])
                except:
                    if len(f1) < len(f2):
                        added.append(f2[i])
                    else:
                        added.append(f1[i])
            added = added[::-1]
        else:
            added = self._coeff
            added[len(added)-1] += other

        return Function(*added)

    def __sub__(self, other):
        if isinstance(other, Function):
            f1 = self._coeff[::-1]
            f2 = other._coeff[::-1]
            added = []
            for i in range(len(f1)):
                try:
                    added.append(f1[i] - f2[i])
                except:
                    if len(f1) < len(f2):
                        added.append(f2[i] * -1)
                    else:
                        added.append(f1[i] * -1)
            added = added[::-1]
        else:
            added = self._coeff
            added[len(added)-1] -= other

        return Function(*added)


    def __mul__(self, other):
        if isinstance(other, Function):
            final_coeffs = [0] * (len(other._coeff) + len(self._coeff) - 1)
            for d1, coef1 in enumerate(self._coeff):
                for d2, coef2 in enumerate(other._coeff):
                    final_coeffs[d1 + d2] += coef1 * coef2
        else:
            final_coeffs = [0] * (len(self._coeff))
            for i in range(len(self._coeff)):
                final_coeffs[i] = self._coeff[i] * other

        return Function(*final_coeffs)


    def derivative(self):
        derived_coeffs = self._coeff[::-1]
        for i in range(0, len(self._coeff)):
            derived_coeffs[i] = derived_coeffs[i] * i
        if len(self._coeff) != 0:
            derived_coeffs.pop(0)
        derived_coeffs = derived_coeffs[::-1]

        return Function(*derived_coeffs)

    def integrate(self):
        integrated_coeffs = []
        for i in range(len(self._coeff)):
            integrated_coeffs.append(self._coeff[i] / (len(self._coeff) - (i + 1) + 1))
        integrated_coeffs.append(0)
        return Function(*integrated_coeffs)

