import math
# -b+- sqrt b^2 -4ac/2a
def quad(a,b,c):
  try:
    nump= (-b + math.sqrt(b**2-4*a*c))/(2*a)
    numn= (-b - math.sqrt(b**2-4*a*c))/(2*a)
    
    if (nump == numn):
      return nump, "There is only one solution"
      
    else:
      return nump, numn

  except:
    return "There are no solutions"

# N(monthly payments is constant?)
def morg(p,d,i):
  #pa=p-d
  pp=p-d
  i1=i/12
  num= pp*(i1*((1+i1)**300))
  deno=((1+i1)**300)-1
  return num/deno