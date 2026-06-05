##Este  codigo  Calcula  e  imprime  **
#el numero pi  **
#** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **
#Parametros  de  entredad : **
#N  =  el  número  de  veces  que  se  va  repetir  el  codigo  **
#para  que el pi sea  mas  exacto  **
#** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **
#Autor : Juan  Felipe  Corrales  Toro  **
#ULTIMA  ACTUALIZACION : 15  de  Septiembre  /  2021  **
import math
x=1
n=int(input("ingresa un n ENTRE MAS GRANDE MAS PRECISO!! " ))
def cal(x,n):
    m=0
    i=1
    while n>=i:
        suma=(((-1)**(i+1))*(x**(2*i-1))/(2*i-1))
        m=m+suma
        i=i+1
    return(m)
cal(x,n)
p=cal(x,n)*4
print(p)
e=p-math.pi
print("te falta esto de precision ",e)






