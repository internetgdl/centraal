def add_by(number):
    '''return number by number'''
    try:
        print(number/number)
    except TypeError:
        print("Se necesita valor numerico")
    except:
        raise ValueError("Error personalizado")
    finally:
        print(1)

try:
    add_by(0)
except ValueError as err:
    print(err)