def analyze_function(func): 
    print("Type:", type(func))
    print("\nFirst 10 dir results:") 
    print(dir(func))  
    print("\nHelp:",help(func)) 

analyze_function(str.upper)