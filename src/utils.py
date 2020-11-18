def integration(f, a, b, N = 50):
    y_right = f[1:]
    y_left = f[:-1]
    dx = (b - a)/N
    T = (dx/2)* (sum(y_right) + sum(y_left))

    return T

def format_print(input_vars, inf_method, def_method, output_vars):
    print(f"\nMetodo de Inferencia: {inf_method}")
    print(f"Metodo de Desdifusificacion: {def_method}\n")
    print("Parametros de entrada:")
    for var in input_vars.items():
        print(f"{var[0]} = {var[1]}")
    
    print("\nResultados:")
    for var in output_vars.items():
        print(f"{var[0]} = {var[1]}")
    
    print("-"*50)