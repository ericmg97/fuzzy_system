from fuzzy_variable import OutputVariable, InputVariable
from fuzzy_system import InferenceSys
from utils import format_print

temperatura = InputVariable('Temperatura', 0, 150)

temperatura.add_triangular('Fria', 0, 0, 80)
temperatura.add_triangular('Tibia', 70, 90, 110)
temperatura.add_triangular('Caliente', 100, 150, 150)

humedad = InputVariable('Humedad', 0, 100)

humedad.add_triangular('Seco', 0, 0, 40)
humedad.add_trapezoidal('Moderado', 30, 45, 65, 80)
humedad.add_triangular('Humedo', 70, 100, 100)

motor_velocidad = OutputVariable('Velocidad', 0, 100)

motor_velocidad.add_triangular('Lento', 0, 0, 40)
motor_velocidad.add_triangular('Normal', 30, 50, 70)
motor_velocidad.add_triangular('Rapido', 60, 100, 100)

input_vars = [temperatura, humedad]
output_vars = [motor_velocidad]

system = InferenceSys(input_vars, output_vars)

system.add_rule(
		{ 'Temperatura':'Fria',
			'Humedad':'Humedo' },
		{ 'Velocidad':'Lento'})

system.add_rule(
		{ 'Temperatura':'Fria',
			'Humedad':'Moderado' },
		{ 'Velocidad':'Lento'})

system.add_rule(
		{ 'Temperatura':'Tibia',
			'Humedad':'Humedo' },
		{ 'Velocidad':'Lento'})

system.add_rule(
		{ 'Temperatura':'Tibia',
			'Humedad':'Moderado' },
		{ 'Velocidad':'Normal'})

system.add_rule(
		{ 'Temperatura':'Fria',
			'Humedad':'Seco' },
		{ 'Velocidad':'Normal'})

system.add_rule(
		{ 'Temperatura':'Caliente',
			'Humedad':'Humedo' },
		{ 'Velocidad':'Normal'})

system.add_rule(
		{ 'Temperatura':'Caliente',
			'Humedad':'Moderado' },
		{ 'Velocidad':'Rapido'})

system.add_rule(
		{ 'Temperatura':'Caliente',
			'Humedad':'Seco' },
		{ 'Velocidad':'Rapido'})

system.add_rule(
		{ 'Temperatura':'Tibia',
			'Humedad':'Seco' },
		{ 'Velocidad':'Rapido'})

##################TESTS####################

test1 = {'Temperatura':90,
		'Humedad':20}


inf_method = "Larsen" #Metodo de inferencia: Larsen

def_method = "BOA" #Bisector of Area
output = system.execute(test1, inf_method, def_method)
format_print(test1, inf_method, def_method, output)

def_method = "COA" #Centroide of Area
output = system.execute(test1, inf_method, def_method)
format_print(test1, inf_method, def_method, output)

def_method = "MOM" #Mean of Maximum
output = system.execute(test1, inf_method, def_method)
format_print(test1, inf_method, def_method, output)


inf_method = "Mamdani" #Metodo de inferencia: Mamdani

def_method = "BOA" #Bisector of Area
output = system.execute(test1, inf_method, def_method)
format_print(test1, inf_method, def_method, output)

def_method = "COA" #Centroide of Area
output = system.execute(test1, inf_method, def_method)
format_print(test1, inf_method, def_method, output)

def_method = "MOM" #Mean of Maximum
output = system.execute(test1, inf_method, def_method)
format_print(test1, inf_method, def_method, output)