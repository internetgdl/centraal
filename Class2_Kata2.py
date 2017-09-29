def get_number_of_reachable_fields(grid, rows, columns, start_row, start_column):
    if (1 >= rows >= 2000):
        return False
    if (1 >= columns >= 500):
        return False
    start_from = start_row
    for i, e in reversed(list(enumerate(grid[start_from]))):
        print("posicion "+str(start_column) + " "+ str(i))
        if(start_column>i):
            print(grid[start_from][i])
            if(grid[start_from][i]!=0):
                '''recorremos hacia abajo'''
                print('recorremos hacia abajo')
            else :
                '''detenemos el recorrimiento a la izquierda'''
                break
    return False
    pass
    
def traverse_down(grid, start_row, start_column):
    for i, e in reversed(list(enumerate(grid[start_from]))):
        
    return False