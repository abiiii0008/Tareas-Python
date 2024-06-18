# Definimos una lista para almacenar los trabajadores registrados
trabajadores = [];
decision="";

def registrar_trabajador():# Funcion de registro de trabajadores 
    nombre = input(" Ingrese el nombre y apellido del trabajador: ");
    print(" CARGOS: CEO -- Desarrollador -- Analista de Datos");
    cargo = input(" Ingrese el cargo del trabajador: ").lower();
    sueldo_bruto = float(input(" Ingrese el sueldo bruto del trabajador: "));

    # Calculamos los descuentos  y el sueldo liquido
    descuento_salud = sueldo_bruto * 0.07;
    descuento_afp = sueldo_bruto * 0.1;
    sueldo_liquido = sueldo_bruto - descuento_salud - descuento_afp;


    trabajador = {    # Creamos un diccionario con la información del trabajador 
        "Nombre": nombre,
        "Cargo": cargo,
        "Sueldo Bruto": sueldo_bruto,
        "Descuento Salud": descuento_salud,
        "Descuento AFP": descuento_afp,
        "Líquido a pagar": sueldo_liquido
    }

    trabajadores.append(trabajador)    # Agregamos el trabajador a la lista
    print("Trabajador registrado exitosamente.");

def lista_trabajadores(trabajadores): # Generemos una tabla para visualizar la lista "(:<15)" lo utilizamos para separar los datos.
    print(f"{'Nombre':<20} {'Cargo':<20} {'Sueldo Bruto':<15} {'Desc.Salud':<15} {'Desc.AFP':<15} {'Líquido a pagar':<15}");
    print("-" * 105) # linea de separacion 
    for trabajador in trabajadores: #Bucle que va imprimendo al trabajador por orden de ingreso
        print(f"{trabajador['Nombre']:<20}  {trabajador['Cargo']:<20} {int(trabajador['Sueldo Bruto']):<15} {int(trabajador['Descuento Salud']):<15} {int(trabajador['Descuento AFP']):<15} {int(trabajador['Líquido a pagar']):<15}");

def imprimir_planilla(trabajadores, decision, cargo_filtro=""):
    with open('planilla_sueldos.txt','w',encoding='utf-8',newline='') as archivo:
        # Escribe los titulos del encabezado
        archivo.write(f"{'Nombre':<20} {'Cargo':<20} {'Sueldo Bruto':<15} {'Desc.Salud':<15} {'Desc.AFP':<15} {'Líquido a pagar':<15}\n");
        archivo.write("-" * 105 + "\n") # Linea de separacion 
        
        for trabajador in trabajadores: #revision de cada trabajador en la lista
            # Verificamos si el cargo del trabajador coincide con el filtro que se escoge de lo contrario imprime todos.
            if decision == "no" or (decision == "si" and trabajador['Cargo'] == cargo_filtro):
                # Escribe los datos en el archivo de texto cumpliendo la condicion.
                archivo.write(f"{trabajador['Nombre']:<20} {trabajador['Cargo']:<20} {int(trabajador['Sueldo Bruto']):>15} {int(trabajador['Descuento Salud']):>15} {int(trabajador['Descuento AFP']):>15} {int(trabajador['Líquido a pagar']):>15}\n");