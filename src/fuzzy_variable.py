from fuzzy_set import FuzzySet

class Variable():

    def __init__(self, name, min_val, max_val):
        self.sets = {}
        self._max_val = max_val
        self._min_val = min_val
        self.name = name

    def add_triangular(self, name, low, mid, high):
        new_set = FuzzySet.create_triangular(
            self._min_val, self._max_val, low, mid, high)
        self.sets[name] = new_set
        return new_set

    def add_trapezoidal(self, name, low, mid1, mid2, high):
        new_set = FuzzySet.create_trapezoidal(
            self._min_val, self._max_val, low, mid1, mid2, high)
        self.sets[name] = new_set
        return new_set