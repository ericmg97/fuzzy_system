class FuzzyRule():

	def __init__(self):
		self._antecedent = []
		self._consequent = {}

	def add_antecedent_clause(self, f_set):
		self._antecedent.append(f_set)

	def add_consequent_clause(self, var, f_set):
		self._consequent[var] = f_set

	def evaluate(self, method):
		rule_min = 1
		for ante_clause in self._antecedent:
			rule_min = min(ante_clause.last_degree_value, rule_min)

		for consequent_clause in self._consequent.items():
			c_var = consequent_clause[0]
			c_set = consequent_clause[1]
			
			if method == "Mamdani":
			    c_var.add_rule_contribution(c_set.min_operator(rule_min))
			