#Kata 9

#Ejercicio 1
def informe(tanque1, tanque2, tanque3):
    promedio = (tanque1 + tanque2 + tanque3) / 3
    return f"""Informe de combustible:
    Promedio: {promedio}%
    Tanque 1: {tanque1}%
    Tanque 2: {tanque2}%
    Tanque3: {tanque3}%
    """

print(informe(80, 85, 81))

def promedio(values):
    total = sum(values)
    num_elementos = len(values)
    return total / num_elementos

promedio([80, 85, 81])

def informe(tanque1, tanque2, tanque3):
    return f"""Informe de combustible:
    Promedio: {promedio([tanque1, tanque2, tanque3])}%
    Tanque 1: {tanque1}%
    Tanque 2: {tanque2}%
    Tanque 3: {tanque3}%
    """
print(informe(88, 76, 70))

#Ejercicio 2
def informe_mision(hora_desp, tiempo_vuelo, destino, tanque_externo, tanque_interno):
    return f"""
    El destino es: {destino}
    El tiempo de vuelo es: {hora_desp + tiempo_vuelo} minutos
    El combustible total es: {tanque_externo + tanque_interno} litros
    """
print(informe_mision(14, 51, "Moon", 200000, 300000))

def informe_mision(destino, *minutos, **reservas_combustibles):
    return f"""
    El destino es: {destino}
    El tiempo de vuelo es: {sum(minutos)} minutos
    El combustible total es: {sum(reservas_combustibles.values())} litros
    """
print(informe_mision("Moon", 10, 15, 51, interno=300000, externo=200000))

def informe_mision(destino, *minutos, **reservas_combustibles):
    informe_principal = f"""
    El destino es: {destino}
    El tiempo de vuelo es: {sum(minutos)} minutos
    El combustible total es: {sum(reservas_combustibles.values())} litros
    """
    for nombre_tanque, litros in reservas_combustibles.items():
        informe_principal += f"El tanque {nombre_tanque} tiene -> {litros} litros restantes\n"
        return informe_principal

print(informe_mision("Moon", 8, 11, 55, interno=300000, externo=200000))