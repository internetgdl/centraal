def function_series_fibonacci( number ):
   """ create a function that receives a number and return this numer as fibonacci list"""
   series=[]
   for x in range(0, number):
       series.append(x);

   print(list((series[k-1]+series[k]) for k in series))
  
function_series_fibonacci(6)