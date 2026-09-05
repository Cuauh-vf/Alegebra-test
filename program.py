"""
Inputs:
-Topic for the test 
-Answers given by the user trhoughout the test
-If they want didactic resources

Outputs: 
-Right or worng 
-Calculated answer
-Corresponding questions
-Final result
-Corresponding didactic material

Process: 
1. Analyze the topic wanted for the test

2. Based on the answer, determine which questions to throw the user

3. Import random values for the coeficients of equiations, in the case of algebraic fractions also randomize the values for exponents of variables

4. Determine the question to show the user

5. Show the user the question

6. Read the user's answer

7. Calculate the result

8. Show the user if it got the question right or wrong

9. Repeat this process until all the questions asigned are showed and answered

10. Show the final grade of the user

11. Ask if they want didactic material to reinforce

12. If yes, then locate the specific material corresponding to the wrong answers

13. If not, end program
"""


"""Here we are going to define the functions used in the main program"""
import random
import math
#funcion para mostrar respuesta
def mostrador(c,u,cal):
    print("La respuesta correcta es: ",c)
    print("Tu respuesta: ",u)
    print("Calificacion: ", cal)

#funcion para verificar las respuestas
def verificador(comp,user,cal):
    if comp==user:
        cal=cal+1
    mostrador(comp,user,cal)
    return cal
    
#function for linear equations
def ecuaciones_lineales():
  print("Lineal")
  coeficiente=random.randint(1,10)
  terminoInd=random.randint(-15,15)
  terminoInd2=random.randint(-15,15)
  print("Given the equation %ix + %i = %i, x is equal to what? (Give the answer with 2 decimals rounding up)" %(coeficiente,terminoInd,terminoInd2))
  answerUser=float(input(": "))
  answerComp=round((terminoInd2-terminoInd)/coeficiente,2)
  return answerUser,answerComp
#function for second degree functions
def ecuaciones_cuadraticas():
  print("Cuadraticas")
  return
#function for systems of equations with 2 variables
def sistemas_ecuaciones_1():
  print("sist ec 1")
  return
#function for systems of equations with 3 variables
def sistemas_ecuaciones_2():
  print("Sist ec 2")
  return
#function for development of binomials
def binomio():
  print("binomio")
  return
#function for algebraic fractions
def fractions():
  print("fracciones")
  return
  
    
calificacion=0
opcion=int(input("Hello user, welcome to the algebra test, the objective of this test is evaluate your knowledge on this fundamental topic for engineering.\n Now please select which topic do you want to practice:  \n General test (1) \n First and second degree equations (2) \n Systems of equations (3) \n Development of binomials (4) \n Simplification of algebraic fractions (5) \n:"))
if opcion==1:
    general_test()
elif opcion==2:
    resp,respUser=ecuaciones_lineales()
    calificacion=verificador(resp,respUser,calificacion)
    resp,respUser=ecuaciones_lineales()
    calificacion=verificador(resp,respUser,calificacion)
    """resp,respUser=ecuaciones_cuadraticas()
    calificacion=verificador(resp,respUser,calificacion)
    resp,respUser=ecuaciones_cuadraticas()
    calificacion=verificador(resp,respUser,calificacion)"""
    
elif opcion==3:
    sistemas_ecuaciones_1()
elif opcion==4:
    binomio()
elif opcion==5:
    fractions()
