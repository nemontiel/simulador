def calcular(*args, **kwargs):
    problemas = []
    edadMin = 24
    edadMax = 79
    sueldoMin = 300_000
    antiguedadMin = 3
    montoMin = 500_000
    montoVeces = 10
    cuotasMin = 3
    cuotasMax = 84

    edad = int(Element('edad').value)
    nacionalidad = Element('nacionalidad').value
    sueldo = int(Element('sueldo').value)
    antiguedad = int(Element('antiguedad').value)
    monto = int(Element('monto').value)
    cuotas = int(Element('cuotas').value)
    resultado = Element("resultado")

    montoMax = sueldo * 10
    tasa = 1.46
    interes = monto * (pow(1 + tasa * 0.01, cuotas) - 1)
    total = round(interes + monto)

    if edad < edadMin or edad > edadMax:
        problemas.append("Su edad no es válida, debe tener entre 24 y 79 años")
    if "chile" not in nacionalidad.lower():
        problemas.append("Su nacionalidad no es válida, debe ser chileno/a")
    if sueldo < sueldoMin:
        problemas.append(
            "Su sueldo no es válido, debe ser al menos de 300.000")
    if antiguedad < antiguedadMin:
        problemas.append(
            "Su antigüedad laboral no es válida, debe tener al menos 3 años de antigüedad"
        )
    if monto < montoMin:
        problemas.append(
            "Monto solicitado no válido, debe solicitar al menos $500.000")
    if monto > sueldo * montoVeces:
        problemas.append(
            "Monto solicitado no válido, no debe sobrepasar diez veces su sueldo"
        )
    if cuotas < cuotasMin or cuotas > cuotasMax:
        problemas.append(
            "Cantidad de cuotas no válida, deben estar entre los 3 y 84 meses")
    resultado.write("")
    if len(problemas) == 0:
        resultado.write(
            f"{Element('nombre').value} {Element('apellido').value} {Element('rut').value}",
            append=True)
        resultado.write("Cumple con los requisitos", append=True)
        resultado.write(f"Sueldo: ${Element('sueldo').value}", append=True)
        resultado.write(f"Monto Máximo: ${montoMax}", append=True)
        resultado.write(f"Monto Solicitado: ${Element('monto').value}",
                        append=True)
        resultado.write(f"Tasa Mensual: {tasa}%", append=True)
        resultado.write(f"Cuotas: {Element('cuotas').value}", append=True)
        resultado.write(f"Monto a Pagar: ${format(total,',')}", append=True)
    else:
        resultado.write(
            f"{Element('nombre').value} {Element('apellido').value} {Element('rut').value}",
            append=True)
        resultado.write("No cumple con los requisitos", append=True)
        for problema in problemas:
            resultado.write(f"{problema}", append=True)
