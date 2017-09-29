def add_by(value1,value2):
    try:
        result = int(value1 * value2)
        return result
    except:
        print("el valor no es esperado")
        raise TypeError("hubo una bronca acá")


def sum_by(value1,value2):
    if(value1==1):
        raise exc.AnotherError("El valor introducido por el usuario no es valido")
    return value1+value2