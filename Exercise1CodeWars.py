def longest_consec(strarr, k):
    n = len(strarr)
    if (k == 0) or (k > n) or (k <= 0):
       return ""
    list_result = []
    items_number = len(strarr)
    for y in range(0, items_number):
        list2 = [x for ind, x in enumerate(strarr) if ind < k]
        list_result.append("".join(list2))
        strarr.pop(0)   
        
    return(str(max([(len(x),x) for x in list_result])[1]))