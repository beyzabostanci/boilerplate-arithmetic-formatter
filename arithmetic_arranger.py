def arithmetic_arranger(problems, seen = False):
  if len(problems)>5:
    return "Error: Too many problems."
    
  #variables home  
  topline = ""
  bottomline =""
  dashline =""
  resultline =""
  
  
  for problem in problems:
    add1= problem.split()[0]
    op = problem.split()[1]
    add2= problem.split()[2]

    if not(add1.isdigit() and add2.isdigit()):
      return 'Error: Numbers must only contain digits.'

    if (len(add1)>4 or len(add2)>4):
      return "Error: Numbers cannot be more than four digits."

    sum = ""
    if op == "+":
        sum = int(add1) + int(add2)
    elif op == "-":
        sum = int(add1) - int(add2)
    else:
      return "Error: Operator must be '+' or '-'."

    linelen = max(len(add1), len(add2))+2
    top = str(add1).rjust(linelen)
    bottom=op + str(add2).rjust(linelen -1)
    result= str(sum).rjust(linelen)
    dash = ""
    for i in range(linelen):
      dash += "-"
      
    if problem != problems[-1]:
            topline += top + "    "
            bottomline += bottom + "    "
            dashline += dash + "    "
            resultline += result + "    "
        
    else:
            topline += top
            bottomline += bottom
            dashline += dash
            resultline += result

    
  if seen is True:
        arranger = topline + "\n" + bottomline + "\n" + dashline + "\n" + resultline
  else:
        arranger = topline + "\n" + bottomline + "\n" + dashline
    
  return arranger
