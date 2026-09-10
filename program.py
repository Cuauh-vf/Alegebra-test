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
#function for test
def tests():
    mostrador(1,2,0)
    mostrador(4,4,0)
    mostrador(2,2,5)
    verificador(1,2,0)
    verificador(4,4,0)
    verificador(2,2,5)
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
    coeficiente1=random.randint(1,10)
    terminoInd=random.randint(-15,15)
    coeficiente2=2*coeficiente1*terminoInd
    print("Given the equation %ix^2 + %ix + %i = 0, x is equal to what? (Round up to 2 decimals)" %(coeficiente1**2,coeficiente2,terminoInd**2))
    answerUser=float(input(":"))
    answerComp=round((0-terminoInd)/coeficiente1,2)
    return answerUser,answerComp
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
    coeficiente=random.randint(1,13)
    terminoI=random.randint(-10,12)
    exponente=random.randint(2,4)
    seleccionador=random.randint(1,5)
    print("(%ix+%i)^%i" %(coeficiente,terminoI,exponente))
    if exponente==2: #estos ifs son para calcular los coeficientes del binomio presentado, si no se tendrían que calular más cosas
        if seleccionador==1 or seleccionador==4:#esto es para solo preguntar por 1 respuesta al usuario, habilitando el uso de la función verificador
            answerU=int(input("Give me the coeficient for the first term: "))
            answerC=coeficiente**exponente
            return answerU,answerC
        elif seleccionador==2 or seleccionador==5:
            answerU=int(input("Give me the coeficient for the second term: "))
            answerC=2*coeficiente*terminoI
            return answerU,answerC
        elif seleccionador==3:
            answerU=int(input("Give me the coeficient for the third term: "))
            answerC=terminoI**exponente
            return answerU,answerC
    if exponente==3:
        if seleccionador==1 or seleccionador==5:
            answerU=int(input("Give me the coeficient for the first term: "))
            answerC=coeficiente**exponente
            return answerU,answerC
        elif seleccionador==2:
            answerU=int(input("Give me the coeficient for the second term: "))
            answerC=3*(coeficiente**2)*terminoI
            return answerU,answerC
        elif seleccionador==3:
            answerU=int(input("Give me the coeficient for the third term: "))
            answerC=3*coeficiente*(terminoI**2)
            return answerU,answerC
        elif seleccionador==4:
            answerU=int(input("Give me the coeficient of the fourth term: "))
            answerC=terminoI**exponente
            return answerU,answerC
    if exponente==4:
        if seleccionador==1:
            answerU=int(input("Give me the coeficient for the first term: "))
            answerC=coeficiente**exponente
            return answerU,answerC
        elif seleccionador==2:
            answerU=int(input("Give me the coeficient for the second term: "))
            answerC=4*(coeficiente**3)*terminoI
            return answerU,answerC
        elif seleccionador==3:
            answerU=int(input("Give me the coeficient for the third term: "))
            answerC=6*(coeficiente**2)*(terminoI**2)
            return answerU,answerC
        elif seleccionador==4:
            answerU=int(input("Give me the coeficient of the fourth term: "))
            answerC=4*coeficiente*(terminoI**3)
            return answerU,answerC
        elif seleccionador==5:
            answerU=int(input("Give me the coeficient of the fifth term"))
            answerC=terminoI**exponente
            return answerU,answerC
      
#function for algebraic fractions
def fractions():
    print("fracciones")
    coeficienteA1=random.randint(-12,11)#se me fue el avión y en vez de poner exponente puse coeficiente, solo tomar eso en cuenta
    coeficienteA2=random.randint(-12,11)
    coeficienteZ1=random.randint(-12,11)
    coeficienteZ2=random.randint(-12,11)
    coeficienteW1=random.randint(-12,11)
    coeficienteW2=random.randint(-12,11)
    exponente=random.randint(1,3)
    seleccionar=random.randint(1,3)#esta variable es para simplificar la funcion, si no hiciera esto, la funcion arrogaría 6 resultados
    print("((a^%i * z^%i * w^%i)/(a^%i * z^%i * w^%i))^%i" %(coeficienteA1,coeficienteZ1,coeficienteW1,coeficienteA2,coeficienteZ2,coeficienteW2,exponente))
    if seleccionar==1:#aleatorizar cuál variable vamos a "resolver" para poder utilizar la funcion de verificador 
        userA=int(input("What is the exponent of variable a: "))
        compA=(coeficienteA1-coeficienteA2)*exponente
        return userA,compA
    elif seleccionar==2:
        userZ=int(input("Exponent of variable z: "))
        compZ=(coeficienteZ1-coeficienteZ2)*exponente
        return userZ,compZ
    elif seleccionar==3:
        userW=int(input("Exponent of variable w: "))
        compW=(coeficienteW1-coeficienteW2)*exponente
        return userW,compW
def factorization():#funcion factorizacion
    print("Factorizacion")
    coeficiente1=random.randint(1,10)
    terminoInd=random.randint(-15,15)
    coeficiente2=2*coeficiente1*terminoInd
    seleccionar=random.randint(1,2)
    print("Given the equation %ix^2 + %ix + %i = 0, x is equal to what? (Round up to 2 decimals)" %(coeficiente1**2,coeficiente2,terminoInd**2))
    answerUser=float(input(":"))
def main(): #funcion main
    calificacion=0
    opcion=int(input("Hello user, welcome to the algebra test, the objective of this test is evaluate your knowledge on this fundamental topic for engineering.\n Now please select which topic do you want to practice:  \n General test (1) \n First and second degree equations (2) \n Systems of equations (3) \n Development of binomials (4) \n Simplification of algebraic fractions (5) \n Factorization of equations (6) \n Test cases (7) \n:"))
    match opcion:
        case 1:
            print("General test")
        case 2:
            respUser,resp=ecuaciones_lineales()
            calificacion=verificador(resp,respUser,calificacion)
            respUser,resp=ecuaciones_lineales()
            calificacion=verificador(resp,respUser,calificacion)
            respUser,resp=ecuaciones_cuadraticas()
            calificacion=verificador(resp,respUser,calificacion)
            respUser,resp=ecuaciones_cuadraticas()
            calificacion=verificador(resp,respUser,calificacion)
        case 3:
            sistemas_ecuaciones_1()
        case 4:
            respUser,resp=binomio()
            calificacion=verificador(resp,respUser,calificacion)
            respUser,resp=binomio()
            calificacion=verificador(resp,respUser,calificacion)
        case 5:
            respUser,resp=fractions()
            calificacion=verificador(resp,respUser,calificacion)
            respUser,resp=fractions()
            calificacion=verificador(resp,respUser,calificacion)
            respUser,resp=fractions()
            calificacion=verificador(resp,respUser,calificacion)
            respUser,resp=fractions()
            calificacion=verificador(resp,respUser,calificacion)
        case 6:
            respUser,resp=factorization()
            calificacion=verificador(resp,respUser,calificacion)
        case 7:
            tests()
        case _:
            print("Please insert a valid option")
            main()
main()
