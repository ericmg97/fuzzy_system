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

class InputVariable(Variable):

	def __init__(self, name, min_val, max_val):
		super().__init__(name, min_val, max_val)

	def fuzzify(self, value):
		for _, f_set in self.sets.items():
			f_set.last_degree_value = f_set[value]

class OutputVariable(Variable):
    def __init__(self, name, min_val, max_val):
        super().__init__(name, min_val, max_val)
        self._output_distribution = FuzzySet(min_val, max_val)
    
    def add_rule_contribution(self, rule_consequence):
        self._output_distribution = self._output_distribution.union(rule_consequence)
    
    def defuzzify(self, def_method):
        return self._output_distribution.defuzzify(def_method)