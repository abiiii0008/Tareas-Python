import funciones 

while True:
    print("\n\n// Bienvenido al Menu\n");
    print("// Ingrese una de las siguientes opciones\n");
    print("/  1 Registrar un usario");
    print("/  2 Lista de trabajadores");
    print("/  3 Imprimir planilla de sueldos");
    print("/  4 Salir... ");
    print("-" * 105);
    try:
        opciones=int(input("\n || Ingrese: "));
    except:
        print("\n  || El comando ingresado no es valido  ||");
    else:
        if (opciones==1):# Registra Usuarios en la lista
            funciones.registrar_trabajador();

        elif(opciones==2):# Muestra Lista de Trabajadores
            print("\n\n");
            print("-" * 105);
            funciones.lista_trabajadores(funciones.trabajadores)
            print("-" * 105);
            print("\n\n");

        elif (opciones==3): # Imprimir plantilla en archivo.txt
            decision = input("¿Desea filtrar por algún cargo? (si/no): ").lower();# Imprimir por filtro o todos
            cargo_filtro = "";
            if decision == "si":# Escoge el tipo de filtro
                cargo_filtro = input("Ingrese el cargo a filtrar: ").lower();
            # se llama a la funcion imprimir con sus respectivas variables
            funciones.imprimir_planilla(funciones.trabajadores, decision, cargo_filtro);
            print("\n Plantilla de Sueldos Creada con exito.\n");

        else:
            break;
# Integrantes {
#  Atara 
#  Matias
#  Claudio
# }