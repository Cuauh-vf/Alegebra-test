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
from cs50 import get_float,get_int
#function for test
def tests():
    mostrador(1,2,0)
    mostrador(4,4,0)
    mostrador(2,2,5)
    verificador(1,2,0)
    verificador(4,4,0)
    verificador(2,2,5)
    #print(ecuaciones_cuadraticas())
    #print(factorization_square())
    #print(factorization_cube())
    print(binomio())
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
    answerUser=get_float(": ")
    answerComp=round((terminoInd2-terminoInd)/coeficiente,2)
    return answerUser,answerComp
#function for second degree functions
def ecuaciones_cuadraticas():
    print("Cuadraticas")
    coeficiente1=random.randint(1,10)
    terminoInd=random.randint(-15,15)
    coeficiente2=2*coeficiente1*terminoInd#se saca el 2 termino de esta manera asegurando que siempre sea solo 1 respuesta real
    print("Given the equation %ix^2 + %ix + %i = 0, x is equal to what? (Round up to 2 decimals)" %(coeficiente1**2,coeficiente2,terminoInd**2))
    answerUser=get_float(": ")
    answerComp=round((0-terminoInd)/coeficiente1,2)
    return answerUser,answerComp
#funcion para hacer el display del sistema de ecuaciones
def  displaySistemas1(sistema):
    for i in sistema:
            for cont in range(len(i)):
                match cont:
                    case 0: 
                        print("%ix + "%(i[cont]), end=" ")
                    case 1: 
                        print("%iy = "%(i[cont]), end=" ")
                    case 2: 
                        print("%i"%(i[cont]))
#funcion para hacer el display del sistema de ecuaciones de 3 variables, nno se si lo puedo incluir en el otro pero para no complicarme por lo pronto
def  displaySistemas2(sistema):
    for i in sistema:
            for cont in range(len(i)):
                match cont:
                    case 0: 
                        print("%ix + "%(i[cont]), end=" ")
                    case 1: 
                        print("%iy + "%(i[cont]), end=" ")
                    case 2: 
                        print("%iz = "%(i[cont]), end=" ")
                    case 3:
                        print("%i"%(i[cont]))
#function for systems of equations with 2 variables
def sistemas_ecuaciones_1():
    print("sist ec 1")
    sistema=[]
    escoger=random.randint(1,2)#para que pregunte por x o y en el sistema de ecuaciones
    for i in range(2):#crear el sistema de ecuaciones
        ecuacion=[]
        for cont in range(3):
            ecuacion.append(random.randint(-10,15))
        sistema.append(ecuacion)
    if sistema[0][1]==0:
        sistema[1][1]=random.randint(1,8)#para asegurar que haya solucion en el sistema
    displaySistemas1(sistema)#mostrar el sistema de manera bonita al ususario
    if escoger==1:
            x1Res=sistema[0][0]*sistema[1][1]
            x2Res=sistema[1][0]*(-sistema[0][1])
            xFinal=x1Res+x2Res
            indFinal=sistema[0][2]*sistema[1][1]+sistema[1][2]*(-sistema[0][1])
            answerComp=round((indFinal/xFinal),2)
            answerUser=get_float("Give me the value of x, round to 2 decimals: ")
    else: 
            y1Res=sistema[0][1]*sistema[1][0]
            y2Res=sistema[1][1]*(-sistema[0][0])
            yFinal=y1Res+y2Res
            indFinal=sistema[0][2]*sistema[1][0]+(sistema[1][2]*(-sistema[0][0]))
            answerComp=round((indFinal/yFinal),2)
            answerUser=get_float("Give me the value of y, round to 2 decimals: ")
    return answerUser,answerComp
#function for systems of equations with 3 variables
def sistemas_ecuaciones_2():
    print("Sist ec 2")
    sistema=[]
    escoger=random.randint(1,3)
    for i in range(3):
        ecuacion=[]
        for cont in range(4):
            ecuacion.append(random.randint(-5,8))
            if ecuacion[cont]==0:
                ecuacion[cont]+=1 #aqui aseguramos que no nos de un sistema sin solucion
        sistema.append(ecuacion)
    displaySistemas2(sistema)
    match escoger:
        case 1:#ver si se puede crear una funcino de esto, ya estoy pensando como hacerlo
            x1SisNuevo1=sistema[0][0]*sistema[1][2]
            x2SisNuevo1=sistema[1][0]*(-sistema[0][2])
            xFSisNuevo1=x1SisNuevo1+x2SisNuevo1
            y1SisNuevo1=sistema[0][1]*sistema[1][2]
            y2SisNuevo1=sistema[1][1]*(-sistema[0][2])
            yFSisNuevo1=y1SisNuevo1+y2SisNuevo1
            indSisNuevo1=sistema[0][3]*sistema[1][2]+sistema[1][3]*(-sistema[0][2])
            x1SisNuevo2=sistema[0][0]*sistema[2][2]
            x2SisNuevo2=sistema[2][0]*(-sistema[0][2])
            xFSisNuevo2=x1SisNuevo2+x2SisNuevo2
            y1SisNuevo2=sistema[0][1]*sistema[2][2]
            y2SisNuevo2=sistema[2][1]*(-sistema[0][2])
            yFSisNuevo2=y1SisNuevo2+y2SisNuevo2
            indSisNuevo2=sistema[0][3]*sistema[2][2]+sistema[2][3]*(-sistema[0][2])
            x1Res=xFSisNuevo1*yFSisNuevo2
            x2Res=xFSisNuevo2*(-yFSisNuevo1)
            xFinal=x1Res+x2Res
            indFinal=indSisNuevo1*yFSisNuevo2+indSisNuevo2*(-yFSisNuevo1)
            answerComp=round((indFinal/xFinal),2)
            answerUser=get_float("Give me the value of x, round up to 2 decimals: ")
        case 2:
            x1SisNuevo1=sistema[0][0]*sistema[1][2]
            x2SisNuevo1=sistema[1][0]*(-sistema[0][2])
            xFSisNuevo1=x1SisNuevo1+x2SisNuevo1
            y1SisNuevo1=sistema[0][1]*sistema[1][2]
            y2SisNuevo1=sistema[1][1]*(-sistema[0][2])
            yFSisNuevo1=y1SisNuevo1+y2SisNuevo1
            indSisNuevo1=sistema[0][3]*sistema[1][2]+sistema[1][3]*(-sistema[0][2]) #tal vez hago una funcion para esto, la verdad no se
            x1SisNuevo2=sistema[0][0]*sistema[2][2]
            x2SisNuevo2=sistema[2][0]*(-sistema[0][2])
            xFSisNuevo2=x1SisNuevo2+x2SisNuevo2
            y1SisNuevo2=sistema[0][1]*sistema[2][2]
            y2SisNuevo2=sistema[2][1]*(-sistema[0][2])
            yFSisNuevo2=y1SisNuevo2+y2SisNuevo2
            indSisNuevo2=sistema[0][3]*sistema[2][2]+sistema[2][3]*(-sistema[0][2])
            y1Res=yFSisNuevo1*xFSisNuevo2
            y2Res=yFSisNuevo2*(-xFSisNuevo1)
            yFinal=y1Res+y2Res
            indFinal=indSisNuevo1*xFSisNuevo2+indSisNuevo2*(-xFSisNuevo1)
            answerComp=round((indFinal/yFinal),2)
            answerUser=get_float("Give me the value of y, round up to 2 decimals: ")
        case 3: 
            z1SisNuevo1=sistema[0][2]*sistema[1][0]
            z2Sisnuevo1=sistema[1][2]*(-sistema[0][0])
            zFSisNuevo1=z1SisNuevo1+z2Sisnuevo1
            y1SisNuevo1=sistema[0][1]*sistema[1][0]
            y2SisNuevo1=sistema[1][1]*(-sistema[0][0])
            yFSisNuevo1=y1SisNuevo1+y2SisNuevo1
            indSisNuevo1=sistema[0][3]*sistema[1][0]+sistema[1][3]*(-sistema[0][0])
            z1SisNuevo2=sistema[0][2]*sistema[2][0]
            z2Sisnuevo2=sistema[2][2]*(-sistema[0][0])
            zFSisNuevo2=z1SisNuevo2+z2Sisnuevo2
            y1SisNuevo2=sistema[0][1]*sistema[2][0]
            y2SisNuevo2=sistema[2][1]*(-sistema[0][0])
            yFSisNuevo2=y1SisNuevo2+y2SisNuevo2
            indSisNuevo2=sistema[0][3]*sistema[2][0]+sistema[2][3]*(-sistema[0][0])
            z1Res=zFSisNuevo1*yFSisNuevo2
            z2Res=zFSisNuevo2*(-yFSisNuevo1)
            zFinal=z1Res+z2Res
            indFinal=indSisNuevo1*yFSisNuevo2+indSisNuevo2*(-yFSisNuevo1)
            answerComp=round((indFinal/zFinal),2)
            answerUser=get_float("Give me the value of z, round up to 2 decimals: ")
    return answerUser,answerComp
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
            answerU=get_int("Give me the coeficient for the first term: ")
            answerC=coeficiente**exponente
        elif seleccionador==2 or seleccionador==5:
            answerU=get_int("Give me the coeficient for the second term: ")
            answerC=2*coeficiente*terminoI
        elif seleccionador==3:
            answerU=get_int("Give me the coeficient for the third term: ")
            answerC=terminoI**exponente
    if exponente==3:
        if seleccionador==1 or seleccionador==5:
            answerU=get_int("Give me the coeficient for the first term: ")
            answerC=coeficiente**exponente
        elif seleccionador==2:
            answerU=get_int("Give me the coeficient for the second term: ")
            answerC=3*(coeficiente**2)*terminoI
        elif seleccionador==3:
            answerU=get_int("Give me the coeficient for the third term: ")
            answerC=3*coeficiente*(terminoI**2)
        elif seleccionador==4:
            answerU=get_int("Give me the coeficient of the fourth term: ")
            answerC=terminoI**exponente
    if exponente==4:
        if seleccionador==1:
            answerU=get_int("Give me the coeficient for the first term: ")
            answerC=coeficiente**exponente
        elif seleccionador==2:
            answerU=get_int("Give me the coeficient for the second term: ")
            answerC=4*(coeficiente**3)*terminoI
        elif seleccionador==3:
            answerU=get_int("Give me the coeficient for the third term: ")
            answerC=6*(coeficiente**2)*(terminoI**2)
        elif seleccionador==4:
            answerU=get_int("Give me the coeficient of the fourth term: ")
            answerC=4*coeficiente*(terminoI**3)
        elif seleccionador==5:
            answerU=get_int("Give me the coeficient of the fifth term")
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
        userA=get_int("What is the exponent of variable a: ")
        compA=(coeficienteA1-coeficienteA2)*exponente
        return userA,compA
    elif seleccionar==2:
        userZ=get_int("Exponent of variable z: ")
        compZ=(coeficienteZ1-coeficienteZ2)*exponente
        return userZ,compZ
    elif seleccionar==3:
        userW=get_int("Exponent of variable w: ")
        compW=(coeficienteW1-coeficienteW2)*exponente
        return userW,compW
#funcion factorizacion
def factorization_square():
    print("Factorizacion")
    coeficiente1=random.randint(1,10)
    terminoInd=random.randint(-15,15)
    coeficiente2=2*coeficiente1*terminoInd
    seleccionar=random.randint(1,2)
    if seleccionar==1:
        print("Given the equation %ix^2 + %ix + %i = 0, factorize and give the coeficient of x" %(coeficiente1**2,coeficiente2,terminoInd**2))
        answerUser=get_int(":")
        answerComp=coeficiente1
    elif seleccionar==2:
        print("Given the equation %ix^2 + %ix + %i = 0, factorize and give me the independent term" %(coeficiente1**2,coeficiente2,terminoInd**2))
        answerUser=get_int(":")
        answerComp=terminoInd
    return answerUser,answerComp
#funcion factorizacion de binomios al cubo
def factorization_cube():
    coeficiente1=random.randint(1,10)
    terminoInd=random.randint(-15,15)
    coeficiente2=3*(coeficiente1**2)*terminoInd
    coeficiente3=3*coeficiente1*(terminoInd**2)
    seleccionar=random.randint(1,2)
    if seleccionar==1:
        print("Given the equation %ix^3 + %ix^2 + %ix + %i = 0, factorize and give the coeficient of x" %(coeficiente1**3,coeficiente2,coeficiente3,terminoInd**3))
        answerUser=get_int(":")
        answerComp=coeficiente1
    elif seleccionar==2:
        print("Given the equation %ix^3 + %ix^2 + %ix + %i = 0, factorize and give the independent term" %(coeficiente1**3,coeficiente2,coeficiente3,terminoInd**3))
        answerUser=get_int(":")
        answerComp=terminoInd
    return answerUser,answerComp
def main(): #funcion main
    calificacion=0
    opcion=get_int("Hello user, welcome to the algebra test, the objective of this test is evaluate your knowledge on this fundamental topic for engineering.\n Now please select which topic do you want to practice:  \n General test (1) \n First and second degree equations (2) \n Systems of equations (3) \n Development of binomials (4) \n Simplification of algebraic fractions (5) \n Factorization of equations (6) \n Test cases (7) \n:")
    match opcion:
        case 1:
            print("General test")
        case 2:
            preguntas=get_int("How many questions of the topic do you want? ")
            cambio=1
            for cont in range (1,preguntas+1):
                print("Pregunta %i"%(cont))
                if cambio==1:    
                    respUser,resp=ecuaciones_lineales()
                    calificacion=verificador(resp,respUser,calificacion)
                    cambio=2
                elif cambio==2:
                    respUser,resp=ecuaciones_cuadraticas()
                    calificacion=verificador(resp,respUser,calificacion)
                    cambio=1
        case 3:
            preguntas=get_int("How many questions of the topic do you want? ")
            cambio=1
            for cont in range(1,preguntas+1):
                print("Pregunta %i"%(cont))
                if cambio==1:    
                    respUser,resp=sistemas_ecuaciones_1()
                    calificacion=verificador(resp,respUser,calificacion)
                    cambio=2
                elif cambio==2:
                    respUser,resp=sistemas_ecuaciones_2()
                    calificacion=verificador(resp,respUser,calificacion)
                    cambio=1
        case 4:
            preguntas=get_int("How many questions of the topic do you want? ")
            for cont in range(1,preguntas+1):
                print("Pregunta %i"%(cont))
                respUser,resp=binomio()
                calificacion=verificador(resp,respUser,calificacion)
        case 5:
            preguntas=get_int("How many questions of the topic do you want? ")
            for cont in range(1,preguntas+1):
                print("Pregunta %i"%(cont))
                respUser,resp=fractions()
                calificacion=verificador(resp,respUser,calificacion)
        case 6:
            preguntas=get_int("How many questions of the topic do you want? ")
            cambio=1
            for cont in range (1,preguntas+1):
                print("Pregunta %i"%(cont))
                if cambio==1:    
                    respUser,resp=factorization_square()
                    calificacion=verificador(resp,respUser,calificacion)
                    cambio=2
                elif cambio==2:
                    respUser,resp=factorization_cube()
                    calificacion=verificador(resp,respUser,calificacion)
                    cambio=1
        case 7:
            tests()
        case _:
            print("Please insert a valid option")
            main()
main()
