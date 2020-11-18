from fuzzy_variable import OutputVariable, InputVariable
from fuzzy_system import InferenceSys

temperatura = InputVariable('Temperatura', 10, 50)

temperatura.add_triangular('Fria', 10, 10, 20)
temperatura.add_triangular('Tibia', 15, 25, 35)
temperatura.add_triangular('Caliente', 30, 50, 50)

humedad = InputVariable('Humedad', 20, 100)

humedad.add_triangular('Humedo', 20, 20, 40)
humedad.add_trapezoidal('Moderado', 30, 50, 70, 90)
humedad.add_triangular('Seco', 80, 100, 100)

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


#Test

out_par = {'Temperatura':32,
		'Humedad':60}

inf_method = "Mamdani" #Metodo de inferencia
def_method = "COA" #Metodo de desdifusificacion

output = system.execute(out_par, inf_method, def_method)
print(output)

