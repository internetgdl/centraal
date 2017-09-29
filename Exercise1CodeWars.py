def longest_consec(strarr, k):
    n = len(strarr)
    print(k)
    if (k == 0) or (k >= n) or (k <= 0):
        return ""
    element = str(max([(len(x),x) for x in strarr])[1])
    position = strarr.index(element)
    
    for x in range(0, k):
        text_concatena = ""
        position_element = position+x+1
        if(position_element>=n):
            position = 0
        position_element = (x+position)
        print(position_element)
        if(position_element!=position):
            text_concatena += strarr[position_element]
        print(text_concatena)
    return(str(max([(len(x),x) for x in strarr])[1]+text_concatena))