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

#funcion para poder llevar el registro de las preguntas malas
def almacenarPreguntas(mal,pregunta,u,c):
    if mal==1:
        with open("registro.txt","a") as file:#lo añade al archivo previamente creado (se crea en el main)
            file.seek(0,2)
            for i in range(len(pregunta)):
                file.writelines(pregunta[i])#como hay algunas preguntas que tienen más de 1 linea, lo hago así para que las escriba como cuando aparecieron 
            file.write("\n"+"Your answer: "+str(u)+"\n")
            file.write("Right answer: "+str(c)+"\n")

            
#funcion para mostrar respuesta
def mostrador(c,u,cal):
    print("The right answer is: ",c)
    print("Your answer: ",u)
    print("Grade: ", cal)

#funcion para verificar las respuestas
def verificador(comp,user,cal):
    mal=1
    if comp==user:
        cal=cal+1
        mal=0
    mostrador(comp,user,cal)
    return cal,mal
    
#function for linear equations
def ecuaciones_lineales():
    print("Lineal")
    pregunta=[]
    coeficiente=random.randint(1,10)
    terminoInd=random.randint(-15,15)
    terminoInd2=random.randint(-15,15)
    linea="Given the equation %ix + %i = %i, x is equal to what? (Give the answer with 2 decimals rounding up)\n: " %(coeficiente,terminoInd,terminoInd2)
    pregunta.append(linea)
    answerUser=get_float(linea)
    answerComp=round((terminoInd2-terminoInd)/coeficiente,2)
    return answerUser,answerComp,pregunta
#function for second degree functions
def ecuaciones_cuadraticas():
    print("Cuadraticas")
    pregunta=[]
    coeficiente1=random.randint(1,10)
    terminoInd=random.randint(-15,15)
    coeficiente2=2*coeficiente1*terminoInd#se saca el 2 termino de esta manera asegurando que siempre sea solo 1 respuesta real
    linea="Given the equation %ix^2 + %ix + %i = 0, x is equal to what? (Round up to 2 decimals)\n: " %(coeficiente1**2,coeficiente2,terminoInd**2)
    pregunta.append(linea)
    answerUser=get_float(linea)
    answerComp=round((0-terminoInd)/coeficiente1,2)
    return answerUser,answerComp,pregunta
#funcion para hacer el display del sistema de ecuaciones
def  displaySistemas1(sistema):
    pregunta=[]
    for i in sistema:
        for cont in range(len(i)):
            match cont:
                case 0: 
                    x="%ix + "%(i[cont])
                    
                case 1: 
                    y="%iy = "%(i[cont])
                    
                case 2: 
                    w="%i"%(i[cont])            
        linea=x+y+w+"\n"
        print(linea,end="")
        pregunta.append(linea)
    return pregunta
#funcion para hacer el display del sistema de ecuaciones de 3 variables, nno se si lo puedo incluir en el otro pero para no complicarme por lo pronto
def  displaySistemas2(sistema):
    pregunta=[]
    for i in sistema:
        for cont in range(len(i)):
            match cont:
                case 0: 
                    x="%ix + "%(i[cont])
                case 1: 
                    y="%iy + "%(i[cont])
                case 2: 
                    z="%iz = "%(i[cont])
                case 3:
                    w="%i"%(i[cont])
        linea=x+y+z+w+"\n"
        pregunta.append(linea)
        print(linea,end="")
    return pregunta
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
    pregunta=displaySistemas1(sistema)#mostrar el sistema de manera bonita al ususario
    if escoger==1:
            x1Res=sistema[0][0]*sistema[1][1]
            x2Res=sistema[1][0]*(-sistema[0][1])
            xFinal=x1Res+x2Res
            indFinal=sistema[0][2]*sistema[1][1]+sistema[1][2]*(-sistema[0][1])
            answerComp=round((indFinal/xFinal),2)
            linea="Give me the value of x, round to 2 decimals: "
            answerUser=get_float(linea)
            pregunta.append(linea)
    else: 
            y1Res=sistema[0][1]*sistema[1][0]
            y2Res=sistema[1][1]*(-sistema[0][0])
            yFinal=y1Res+y2Res
            indFinal=sistema[0][2]*sistema[1][0]+(sistema[1][2]*(-sistema[0][0]))
            answerComp=round((indFinal/yFinal),2)
            linea="Give me the value of y, round to 2 decimals: "
            answerUser=get_float(linea)
            pregunta.append(linea)
    return answerUser,answerComp,pregunta
#function for systems of equations with 3 variables
def sistemas_ecuaciones_2():#hay que revisar el caso cuando aún pueden aparecer sin solucion
    print("Sist ec 2")
    sistema=[]
    escoger=random.randint(1,3)
    for i in range(3):
        ecuacion=[]
        for cont in range(4):
            ecuacion.append(random.randint(-5,8))
            #debo verificar si es necesario esto o si es posible y no muy complicado asegurar que no hayan sistemas sin solución
            """if ecuacion[cont]==0:
                ecuacion[cont]+=1 #aqui reducimos la probabilidad que nos de un sistema sin solucion"""
        sistema.append(ecuacion)
    pregunta=displaySistemas2(sistema)
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
            linea="Give me the value of x, round up to 2 decimals: "
            answerUser=get_float(linea)
            pregunta.append(linea)
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
            linea="Give me the value of y, round up to 2 decimals: "
            answerUser=get_float(linea)
            pregunta.append(linea)
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
            linea="Give me the value of z, round up to 2 decimals: "
            answerUser=get_float(linea)
            pregunta.append(linea)
    return answerUser,answerComp,pregunta
#function for development of binomials
def binomio():
    print("binomio")
    pregunta=[]
    coeficiente=random.randint(1,13)
    terminoI=random.randint(-10,12)
    exponente=random.randint(2,4)
    seleccionador=random.randint(1,5)
    linea="(%ix+%i)^%i" %(coeficiente,terminoI,exponente)
    print(linea)
    pregunta.append(linea+"\n")
    if exponente==2: #estos ifs son para calcular los coeficientes del binomio presentado, si no se tendrían que calular más cosas
        if seleccionador==1 or seleccionador==4:#esto es para solo preguntar por 1 respuesta al usuario, habilitando el uso de la función verificador
            linea="Give me the coeficient for the first term: "
            answerU=get_int(linea)
            pregunta.append(linea)
            answerC=coeficiente**exponente
        elif seleccionador==2 or seleccionador==5:
            linea="Give me the coeficient for the second term: "
            answerU=get_int(linea)
            pregunta.append(linea)
            answerC=2*coeficiente*terminoI
        elif seleccionador==3:
            linea="Give me the coeficient for the third term: "
            answerU=get_int(linea)
            pregunta.append(linea)
            answerC=terminoI**exponente
    if exponente==3:
        if seleccionador==1 or seleccionador==5:
            linea="Give me the coeficient for the first term: "
            answerU=get_int(linea)
            pregunta.append(linea)
            answerC=coeficiente**exponente
        elif seleccionador==2:
            linea="Give me the coeficient for the second term: "
            answerU=get_int(linea)
            pregunta.append(linea)
            answerC=3*(coeficiente**2)*terminoI
        elif seleccionador==3:
            linea="Give me the coeficient for the third term: "
            answerU=get_int(linea)
            pregunta.append(linea)
            answerC=3*coeficiente*(terminoI**2)
        elif seleccionador==4:
            linea="Give me the coeficient for the fourth term: "
            answerU=get_int(linea)
            pregunta.append(linea)
            answerC=terminoI**exponente
    if exponente==4:
        if seleccionador==1:
            linea="Give me the coeficient for the first term: "
            answerU=get_int(linea)
            pregunta.append(linea)
            answerC=coeficiente**exponente
        elif seleccionador==2:
            linea="Give me the coeficient for the second term: "
            answerU=get_int(linea)
            pregunta.append(linea)
            answerC=4*(coeficiente**3)*terminoI
        elif seleccionador==3:
            linea="Give me the coeficient for the third term: "
            answerU=get_int(linea)
            pregunta.append(linea)
            answerC=6*(coeficiente**2)*(terminoI**2)
        elif seleccionador==4:
            linea="Give me the coeficient for the fourth term: "
            answerU=get_int(linea)
            pregunta.append(linea)
            answerC=4*coeficiente*(terminoI**3)
        elif seleccionador==5:
            linea="Give me the coeficient for the fifth term: "
            answerU=get_int(linea)
            pregunta.append(linea)
            answerC=terminoI**exponente
    return answerU,answerC,pregunta
      
#function for algebraic fractions
def fractions():
    print("fracciones")
    pregunta=[]
    coeficienteA1=random.randint(-12,11)#se me fue el avión y en vez de poner exponente puse coeficiente, solo tomar eso en cuenta
    coeficienteA2=random.randint(-12,11)
    coeficienteZ1=random.randint(-12,11)
    coeficienteZ2=random.randint(-12,11)
    coeficienteW1=random.randint(-12,11)
    coeficienteW2=random.randint(-12,11)
    exponente=random.randint(1,3)
    seleccionar=random.randint(1,3)#esta variable es para simplificar la funcion, si no hiciera esto, la funcion arrogaría 6 resultados
    linea="((a^%i * z^%i * w^%i)/(a^%i * z^%i * w^%i))^%i" %(coeficienteA1,coeficienteZ1,coeficienteW1,coeficienteA2,coeficienteZ2,coeficienteW2,exponente)
    print(linea)
    pregunta.append(linea+"\n")
    if seleccionar==1:#aleatorizar cuál variable vamos a "resolver" para poder utilizar la funcion de verificador 
        linea="What is the exponent of variable a: "
        userA=get_int(linea)
        pregunta.append(linea)
        compA=(coeficienteA1-coeficienteA2)*exponente
        return userA,compA,pregunta
    elif seleccionar==2:
        linea="What is the exponent of variable z: "
        userZ=get_int(linea)
        pregunta.append(linea)
        compZ=(coeficienteZ1-coeficienteZ2)*exponente
        return userZ,compZ,pregunta
    elif seleccionar==3:
        linea="What is the exponent of variable w: "
        userW=get_int(linea)
        pregunta.append(linea)
        compW=(coeficienteW1-coeficienteW2)*exponente
        return userW,compW,pregunta
#funcion factorizacion
def factorization_square():
    print("Factorizacion")
    coeficiente1=random.randint(1,10)
    terminoInd=random.randint(-15,15)
    coeficiente2=2*coeficiente1*terminoInd
    seleccionar=random.randint(1,2)
    pregunta=[]
    if seleccionar==1:
        linea="Given the equation %ix^2 + %ix + %i = 0, factorize and give the coeficient of x\n:" %(coeficiente1**2,coeficiente2,terminoInd**2)
        pregunta.append(linea)
        answerUser=get_int(linea)
        answerComp=coeficiente1
    elif seleccionar==2:
        linea="Given the equation %ix^2 + %ix + %i = 0, factorize and give me the independent term\n: " %(coeficiente1**2,coeficiente2,terminoInd**2)
        pregunta.append(linea)
        answerUser=get_int(linea)
        answerComp=terminoInd
    return answerUser,answerComp,pregunta
#funcion factorizacion de binomios al cubo
def factorization_cube():
    coeficiente1=random.randint(1,10)
    terminoInd=random.randint(-15,15)
    coeficiente2=3*(coeficiente1**2)*terminoInd
    coeficiente3=3*coeficiente1*(terminoInd**2)
    seleccionar=random.randint(1,2)
    pregunta=[]
    if seleccionar==1:
        linea="Given the equation %ix^3 + %ix^2 + %ix + %i = 0, factorize and give the coeficient of x\n: " %(coeficiente1**3,coeficiente2,coeficiente3,terminoInd**3)
        answerUser=get_int(linea)
        pregunta.append(linea)
        answerComp=coeficiente1
    elif seleccionar==2:
        linea="Given the equation %ix^3 + %ix^2 + %ix + %i = 0, factorize and give the independent term\n:" %(coeficiente1**3,coeficiente2,coeficiente3,terminoInd**3)
        answerUser=get_int(linea)
        pregunta.append(linea)
        answerComp=terminoInd
    return answerUser,answerComp,pregunta
def main(): #funcion main
    calificacion=0
    mal=0#para saber si la pregunta esta mal o no
    with open("registro.txt","w") as file:#crea un archivo para guardar las respuestas
        file.write("")#solo es para crear el archivo, no se escribe nada
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
                    respUser,resp,preguntaActual=ecuaciones_lineales()
                    calificacion,mal=verificador(resp,respUser,calificacion)
                    cambio=2
                elif cambio==2:
                    respUser,resp,preguntaActual=ecuaciones_cuadraticas()
                    calificacion,mal=verificador(resp,respUser,calificacion)
                    cambio=1
                almacenarPreguntas(mal,preguntaActual,respUser,resp)
            mostrarArchivo=input("Do you want me to show you which questions you got wrong? (y/n)")
            if mostrarArchivo=="y":
                file=open("registro.txt")
                file.seek(0)
                print(file.read())
            else: 
                print("Ok, bye")
        case 3:
            preguntas=get_int("How many questions of the topic do you want? ")
            cambio=1
            for cont in range(1,preguntas+1):
                print("Pregunta %i"%(cont))
                if cambio==1:    
                    respUser,resp,preguntaActual=sistemas_ecuaciones_1()
                    calificacion,mal=verificador(resp,respUser,calificacion)
                    cambio=2
                elif cambio==2:
                    respUser,resp,preguntaActual=sistemas_ecuaciones_2()
                    calificacion,mal=verificador(resp,respUser,calificacion)
                    cambio=1
                almacenarPreguntas(mal,preguntaActual,respUser,resp)
            mostrarArchivo=input("Do you want me to show you which questions you got wrong? (y/n)")
            if mostrarArchivo=="y":
                file=open("registro.txt")
                file.seek(0)
                print(file.read())
            else: 
                print("Ok, bye")
        case 4:
            preguntas=get_int("How many questions of the topic do you want? ")
            for cont in range(1,preguntas+1):
                print("Pregunta %i"%(cont))
                respUser,resp,preguntaActual=binomio()
                calificacion,mal=verificador(resp,respUser,calificacion)
                almacenarPreguntas(mal,preguntaActual,respUser,resp)
            mostrarArchivo=input("Do you want me to show you which questions you got wrong? (y/n)")
            if mostrarArchivo=="y":
                file=open("registro.txt")
                file.seek(0)
                print(file.read())
            else: 
                print("Ok, bye")
        case 5:
            preguntas=get_int("How many questions of the topic do you want? ")
            for cont in range(1,preguntas+1):
                print("Pregunta %i"%(cont))
                respUser,resp,preguntaActual=fractions()
                calificacion,mal=verificador(resp,respUser,calificacion)
                almacenarPreguntas(mal,preguntaActual,respUser,resp)
            mostrarArchivo=input("Do you want me to show you which questions you got wrong? (y/n)")
            if mostrarArchivo=="y":
                file=open("registro.txt")
                file.seek(0)
                print(file.read())
            else: 
                print("Ok, bye")
        case 6:
            preguntas=get_int("How many questions of the topic do you want? ")
            cambio=1
            for cont in range (1,preguntas+1):
                print("Pregunta %i"%(cont))
                if cambio==1:    
                    respUser,resp,preguntaActual=factorization_square()
                    calificacion,mal=verificador(resp,respUser,calificacion)
                    cambio=2
                elif cambio==2:
                    respUser,resp,preguntaActual=factorization_cube()
                    calificacion,mal=verificador(resp,respUser,calificacion)
                    cambio=1
                almacenarPreguntas(mal,preguntaActual,respUser,resp)
            mostrarArchivo=input("Do you want me to show you which questions you got wrong? (y/n)")
            if mostrarArchivo=="y":
                file=open("registro.txt")
                file.seek(0)
                print(file.read())
            else: 
                print("Ok, bye")
        case 7:
            tests()
        case _:
            print("Please insert a valid option")
            main()
main()
