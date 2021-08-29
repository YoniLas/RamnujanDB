import mpmath
FILTER_TOL = 15
CONSTS = []

class ContinousFractionFRGenerator(object):
    def __init__(self, fr_list):
        self.fr_list = load_from_db()

    @staticmethod
    def generate_fr():
        pass

class ContinousFraction(object):
    def __init__(self, a_formula, b_formula):
        self.a_formula = a_formula
        self.b_formula = b_formula
        self.values = dict()

    def calculate(self, n):
        calculated_value = 0
        self.values(n, calculated_value)
        return calculated_value

    def __str__(self):
        return


def get_fr():
    return [(an, bn)]

def check_int_null_vector(constant, continous_fraction):
    cr_value = continous_fraction.calculate(n=FILTER_TOL)
    return mpmath.pslq([constant, 1, -cr_value*constant, cr_value], tol=10**(-FILTER_TOL))

def push_to_db(constant, mobious_tranform, continous_fraction):
    pass

def main():
    fr_list = get_fr()
    first_const = CONSTS[0]
    for fr in fr_list:
        vector = check_int_null_vector(first_const, fr)
        if vector:
            push_to_db(first_const, vector, fr)
    pass


if __name__ == '__main__':
    main()