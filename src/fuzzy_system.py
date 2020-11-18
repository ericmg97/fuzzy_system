from fuzzy_rule import FuzzyRule
from fuzzy_variable import InputVariable, OutputVariable

class InferenceSys:

	def __init__(self, in_vars, out_vars):
		self.input_vars = {}
		for var in in_vars:
			self.input_vars[var.name] = var
		
		self.output_vars = {}
		for var in out_vars:
			self.output_vars[var.name] = var

		self.rules = []

	def add_rule(self, antecedent_clauses, consequent_clauses):
		new_rule = FuzzyRule()

		for var_name, set_name in antecedent_clauses.items():
			var = self.input_vars[var_name]
			f_set = var.sets[set_name]
			
			new_rule.add_antecedent_clause(f_set)

		for var_name, set_name in consequent_clauses.items():
			var = self.output_vars[var_name]
			f_set = var.sets[set_name]

			new_rule.add_consequent_clause(var, f_set)

		# Añadir la nueva regla
		self.rules.append(new_rule)

	def execute(self, input_values, inference_method = "Mamdani", def_method = "COA"):
		# Fusificar la entrada
		for input_name, input_value in input_values.items():
			self.input_vars[input_name].fuzzify(input_value)

		# Evaluar las reglas
		for rule in self.rules:
			rule.evaluate(inference_method)

		# Defusificar la salida
		output = {}
		for output_var_name, output_var in self.output_vars.items():
			output[output_var_name] = output_var.defuzzify(def_method)

		return output