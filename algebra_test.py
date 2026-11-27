"""
Code in general: 
Inputs:
-Topic for the test 
-Answers given by the user trhoughout the test
-If they want the question they got wrong

Outputs: 
-Right or worng 
-Calculated answer
-Corresponding questions
-Final result
-File with wrong questions

Process: 
1. Analyze the topic wanted for the test

2. Based on the answer, determine which questions to throw the user

3. Import random values for the coeficients of equiations, in the case of algebraic fractions also randomize the values for exponents of variables

4. Determine the question to show the user

5. Show the user the question

6. Read the user's answer

7. Calculate the result

8. Show the user if it got the question right or wrong

9. If it was wrong, save the questin and answers in a file

10. Repeat this process until all the questions asigned are showed and answered

11. Show the final grade of the user

12. Ask if they want a register of their wrong answers

13. If yes, then show the respective questions and answers

14. If not, end program
"""
"""
Algorithm for system of equations of 2 variables
Inputs: 
--Answer by the user
Outputs: 
--Question printed
--Question saved as value
--Right answer as value
--User answer as value
Process:
1. Create an empty list to save the equations
2. Import a random value between 1-2 to decide whether to ask for x or y
3. With nested for loops create a matrix, which will make as the coefficients of the equation, with random values between -10 and 15
4. If the coefficient of the variable y is equal to 0 in the first equation, make the second y equal to a random value between 1-8
5. We save the system in the question variable and display the system
6. Evalueat if asking for x or y (im going to do the process as if it was x). We are doing elimination process
7. Multiply the coefficient of the first x times the value of the second y
8. Multiply the second x times the negtive of the value of the first y (we cancel the y's)
9. Add the values of both x's obtained, this is the final x of a linear equation
10. Multiply the first independent term times the second y and add to it the product of the second independent term times the negative of the first y, this is the final independent term
11. Clear the x by dividing the final independent term by the coefficient of the final x
12. Round to 2 decimals 
13. Create the line asking for the value of x to the user
14. ask the user for the value fo x with the function get_float of cs50, ensuring to get a float from the user and no errors with string and symbols
15. add the line to the question variable 
16. return the user answer, the computer answer and the whole question (system and asking for the value of x)
"""

"""Here we are going to define the functions used in the main program"""
import random
from cs50 import get_float,get_int #functions to force the user to give a proper answer
#function for test, just prints the functions, since practically everything require input, its difficult to make them as tests
def tests():
    mostrador(1,2,0)
    mostrador(4,4,0)
    verificador(4,4,0)
    verificador(2,2,5)
    print(ecuaciones_cuadraticas())
    print(factorization_square())
    print(factorization_cube())
    print(binomio())
    print(sistemas_ecuaciones_2())
    print(sistemas_ecuaciones_1())
    print(ecuaciones_lineales())
    print(fractions())
    displaySistemas1([[1,2,3],[4,5,6]])
    displaySistemas2([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
    mostrarRegistro()

#function to keep track of the wrong answers
def almacenarPreguntas(mal,pregunta,u,c):
    if mal==1:#verifies if the the answer is wrong, if it isnt then it does nothing
        with open("registro.txt","a") as file:#adds it to the file previously created (created in main)
            file.seek(0,2)#make sure its at the end of the file
            for i in range(len(pregunta)):
                file.writelines(pregunta[i])#since there are questions that have more than 1 line, i did it like this so it saves in the file as they were printed
            file.write("\n"+"Your answer: "+str(u)+"\n")#place \n because it doesnt do the jump automatically
            file.write("Right answer: "+str(c)+"\n")#place the \n so next question jumps line

#function to show the file
def mostrarRegistro(): 
    with open("registro.txt") as file:
        file.seek(0)#make sure its at the beginning of the file
        print(file.read())
#function to show the answer and grade
def mostrador(c,u,cal):
    print("The right answer is: ",c)
    print("Your answer: ",u)
    print("Grade: ", cal)

#function to verify the answers and determine either right or wrong
def verificador(comp,user,cal):
    mal=1
    if comp==user:
        cal=cal+1
        mal=0
    mostrador(comp,user,cal)
    return cal,mal
    
#function for linear equations
def ecuaciones_lineales():
    pregunta=[]#list to save questions
    coeficiente=random.randint(1,10)#import random values for different questions each time
    terminoInd=random.randint(-15,15)
    terminoInd2=random.randint(-15,15)
    linea="Given the equation %ix + %i = %i, x is equal to what? (Give the answer with 2 decimals rounding up)\n: " %(coeficiente,terminoInd,terminoInd2)#save in a variable so its eaisier to save it in the question bank
    pregunta.append(linea)#add the queestion to the bank
    answerUser=get_float(linea)#use of cs50 so it caan only give floats and no strins break the code
    answerComp=round((terminoInd2-terminoInd)/coeficiente,2)#calculate answer, clearing x
    return answerUser,answerComp,pregunta
#function for second degree functions
def ecuaciones_cuadraticas():
    pregunta=[]#list for the questions
    coeficiente1=random.randint(1,10)
    terminoInd=random.randint(-15,15)
    coeficiente2=2*coeficiente1*terminoInd#we calculate the second term this way to ensure there is always 1 real answer
    linea="Given the equation %ix^2 + %ix + %i = 0, x is equal to what? (Round up to 2 decimals)\n: " %(coeficiente1**2,coeficiente2,terminoInd**2)
    pregunta.append(linea)
    answerUser=get_float(linea)
    answerComp=round((0-terminoInd)/coeficiente1,2)#we clear as normal to solve, since its a perfect squared binomial, we can coeffx+ind=0
    return answerUser,answerComp,pregunta
#function for the display of system of ecuations of 2 variables
def  displaySistemas1(sistema):
    pregunta=[]
    for i in sistema:#adquires the value of each equation
        for cont in range(len(i)):#travels through each value of the coeficients
            match cont:
                case 0: #matches with x
                    x="%ix"%(i[cont])
                    
                case 1: #matches with y
                    if i[cont]>-1:#conditional so it doesnt dupe signs 
                        y="+%iy="%(i[cont])
                    else: 
                        y="%iy="%(i[cont])                    
                case 2: 
                    w="%i"%(i[cont])            
        linea=x+y+w+"\n"#saves the equation as a line in the question
        print(linea,end="")
        pregunta.append(linea)
    return pregunta
#function for the display of system of ecuations of 3 variables
def  displaySistemas2(sistema):
    pregunta=[]
    for i in sistema:#turns into the different equations
        for cont in range(len(i)):#goes through each cofficient of the equations
            match cont:
                case 0: 
                    x="%ix"%(i[cont])
                case 1: 
                    if i[cont]>-1:#to avoid duping signs
                        y="+%iy"%(i[cont])
                    else: 
                        y="%iy"%(i[cont])
                case 2: 
                    if i[cont]>-1:
                        z="+%iz="%(i[cont])
                    else: 
                        z="%iz="%(i[cont])
                case 3:
                    w="%i"%(i[cont])
        linea=x+y+z+w+"\n"
        pregunta.append(linea)
        print(linea,end="")
    return pregunta
#function for systems of equations with 2 variables
def sistemas_ecuaciones_1():
    sistema=[]#to save each equation
    escoger=random.randint(1,2)#so it asks either for x or y 
    for i in range(2):#creates the system
        ecuacion=[]#save the coefficients of the equation
        for cont in range(3):
            ecuacion.append(random.randint(-10,15))
        sistema.append(ecuacion)#adds equation to the system
    if sistema[0][1]==0:
        sistema[1][1]=random.randint(1,8)#make sure the system always has solution
    pregunta=displaySistemas1(sistema)#display to the user 
    if escoger==1:#so it asks either for x or y 
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
def sistemas_ecuaciones_2():
    sistema=[]
    posiblesErrores=["No","no","nO"]#in case the user doesnt follow instructions
    escoger=random.randint(1,3)
    for i in range(3):
        ecuacion=[]
        for cont in range(4):
            ecuacion.append(random.randint(-5,8))
        sistema.append(ecuacion)
    pregunta=displaySistemas2(sistema)
    match escoger:
        case 1:#ask for different values (x,y,z)
            try: #try's are so if there is a system with no solution, it doesnt break and enables 'No solution' as an answer
                x1SisNuevo1=sistema[0][0]*sistema[1][2]
                x2SisNuevo1=sistema[1][0]*(-sistema[0][2])#we do elimination to solve the system
                xFSisNuevo1=x1SisNuevo1+x2SisNuevo1#we start as a 2 variables system, using 2 equations and eliminating a variables
                y1SisNuevo1=sistema[0][1]*sistema[1][2]
                y2SisNuevo1=sistema[1][1]*(-sistema[0][2])
                yFSisNuevo1=y1SisNuevo1+y2SisNuevo1
                indSisNuevo1=sistema[0][3]*sistema[1][2]+sistema[1][3]*(-sistema[0][2])#we get the first equation without z
                x1SisNuevo2=sistema[0][0]*sistema[2][2]#we do the same with the other equation left and one of the two already used
                x2SisNuevo2=sistema[2][0]*(-sistema[0][2])
                xFSisNuevo2=x1SisNuevo2+x2SisNuevo2
                y1SisNuevo2=sistema[0][1]*sistema[2][2]
                y2SisNuevo2=sistema[2][1]*(-sistema[0][2])
                yFSisNuevo2=y1SisNuevo2+y2SisNuevo2
                indSisNuevo2=sistema[0][3]*sistema[2][2]+sistema[2][3]*(-sistema[0][2])#2nd equation without z
                x1Res=xFSisNuevo1*yFSisNuevo2#now we solve the new system with only 2 variables
                x2Res=xFSisNuevo2*(-yFSisNuevo1)
                xFinal=x1Res+x2Res
                indFinal=indSisNuevo1*yFSisNuevo2+indSisNuevo2*(-yFSisNuevo1)
                answerComp=round((indFinal/xFinal),2)
                linea="Give me the value of x, round up to 2 decimals, if no solution then 'NO': "
                answerUser=get_float(linea)
                pregunta.append(linea)
            except ZeroDivisionError: #if there is no solution, it doesnt break and the right answer is no solution
                answerComp="NO"
                linea="Give me the value of x, round up to 2 decimals, if no solution then 'NO': "
                answerUser=input(linea)
                if answerUser in posiblesErrores:#if the user doesnt answer exactly as told (NO), it corrects it 
                    answerUser="NO"
                pregunta.append(linea)
        case 2:
            try: 
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
                y1Res=yFSisNuevo1*xFSisNuevo2
                y2Res=yFSisNuevo2*(-xFSisNuevo1)
                yFinal=y1Res+y2Res
                indFinal=indSisNuevo1*xFSisNuevo2+indSisNuevo2*(-xFSisNuevo1)
                answerComp=round((indFinal/yFinal),2)
                linea="Give me the value of y, round up to 2 decimals, if no solution then 'NO': "
                answerUser=get_float(linea)
                pregunta.append(linea)
            except ZeroDivisionError:
                answerComp="NO"
                linea="Give me the value of y, round up to 2 decimals, if no solution then 'NO': "
                answerUser=input(linea)
                if answerUser in posiblesErrores:
                    answerUser="NO"
                pregunta.append(linea)
        case 3: 
            try: 
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
                linea="Give me the value of z, round up to 2 decimals, if no solution then 'NO': "
                answerUser=get_float(linea)
                pregunta.append(linea)
            except ZeroDivisionError:
                answerComp="NO"
                linea="Give me the value of z, round up to 2 decimals, if no solution then 'NO': "
                answerUser=input(linea)
                if answerUser in posiblesErrores:
                    answerUser="NO"
                pregunta.append(linea)
    return answerUser,answerComp,pregunta
#function for development of binomials
def binomio():
    pregunta=[]
    coeficiente=random.randint(1,13)
    terminoI=random.randint(-10,12)
    exponente=random.randint(2,4)
    seleccionador=random.randint(1,5)
    linea="(%ix+%i)^%i" %(coeficiente,terminoI,exponente)
    print(linea)
    pregunta.append(linea+"\n")
    if exponente==2: #to differentiate the coefficients depending on the exponent of the binomial, to simplify calculations
        if seleccionador==1 or seleccionador==4:#to answer for 1 answer only, allowing the use of the verificador function, for example this is the 1 term
            linea="Given the past binomial, expand and give me the coeficient for the first term: "
            answerU=get_int(linea)
            pregunta.append(linea)
            answerC=coeficiente**exponente
        elif seleccionador==2 or seleccionador==5:#second
            linea="Given the past binomial, expand and give me the coeficient for the second term: "
            answerU=get_int(linea)
            pregunta.append(linea)
            answerC=2*coeficiente*terminoI#we calculate the terms coefficients with the definition of pascal's triangle
        elif seleccionador==3:#third
            linea="Given the past binomial, expand and give me the coeficient for the third term: "
            answerU=get_int(linea)
            pregunta.append(linea)
            answerC=terminoI**exponente
    if exponente==3:#if exponent is 3
        if seleccionador==1 or seleccionador==5:#first term
            linea="Given the past binomial, expand and give me the coeficient for the first term: "
            answerU=get_int(linea)
            pregunta.append(linea)
            answerC=coeficiente**exponente
        elif seleccionador==2:#second
            linea="Given the past binomial, expand and give me the coeficient for the second term: "
            answerU=get_int(linea)
            pregunta.append(linea)
            answerC=3*(coeficiente**2)*terminoI
        elif seleccionador==3:#third
            linea="Given the past binomial, expand and give me the coeficient for the third term: "
            answerU=get_int(linea)
            pregunta.append(linea)
            answerC=3*coeficiente*(terminoI**2)
        elif seleccionador==4:#fourth
            linea="Given the past binomial, expand and give me the coeficient for the fourth term: "
            answerU=get_int(linea)
            pregunta.append(linea)
            answerC=terminoI**exponente
    if exponente==4:
        if seleccionador==1:
            linea="Given the past binomial, expand and give me the coeficient for the first term: "
            answerU=get_int(linea)
            pregunta.append(linea)
            answerC=coeficiente**exponente
        elif seleccionador==2:
            linea="Given the past binomial, expand and give me the coeficient for the second term: "
            answerU=get_int(linea)
            pregunta.append(linea)
            answerC=4*(coeficiente**3)*terminoI
        elif seleccionador==3:
            linea="Given the past binomial, expand and give me the coeficient for the third term: "
            answerU=get_int(linea)
            pregunta.append(linea)
            answerC=6*(coeficiente**2)*(terminoI**2)
        elif seleccionador==4:
            linea="Given the past binomial, expand and give me the coeficient for the fourth term: "
            answerU=get_int(linea)
            pregunta.append(linea)
            answerC=4*coeficiente*(terminoI**3)
        elif seleccionador==5:
            linea="Given the past binomial, expand and give me the coeficient for the fifth term: "
            answerU=get_int(linea)
            pregunta.append(linea)
            answerC=terminoI**exponente
    return answerU,answerC,pregunta
      
#function for algebraic fractions
def fractions():
    pregunta=[]
    exponenteA1=random.randint(-12,11)
    exponenteA2=random.randint(-12,11)#exponents of the different variables
    exponenteZ1=random.randint(-12,11)
    exponenteZ2=random.randint(-12,11)
    exponenteW1=random.randint(-12,11)
    exponenteW2=random.randint(-12,11)
    exponenteFraccion=random.randint(1,3)#exponent that covers the whole fraction
    seleccionar=random.randint(1,3)#to simplify the function and ask for only 1 result
    linea="((a^%i * z^%i * w^%i)/(a^%i * z^%i * w^%i))^%i" %(exponenteA1,exponenteZ1,exponenteW1,exponenteA2,exponenteZ2,exponenteW2,exponenteFraccion)
    print(linea)
    pregunta.append(linea+"\n")
    if seleccionar==1:#randomize which variable to solve and being able to use virifcador
        linea="What is the exponent of variable a: "
        userA=get_int(linea)
        pregunta.append(linea)
        compA=(exponenteA1-exponenteA2)*exponenteFraccion#we calculate from subtracting the lower value to the top value and then multiplying by the exponent (exponent rules)
        return userA,compA,pregunta
    elif seleccionar==2:#ask for exponent of z
        linea="What is the exponent of variable z: "
        userZ=get_int(linea)
        pregunta.append(linea)
        compZ=(exponenteZ1-exponenteZ2)*exponenteFraccion
        return userZ,compZ,pregunta
    elif seleccionar==3:#ask for exponent of w
        linea="What is the exponent of variable w: "
        userW=get_int(linea)
        pregunta.append(linea)
        compW=(exponenteW1-exponenteW2)*exponenteFraccion
        return userW,compW,pregunta
#function factorizacion
def factorization_square():
    coeficiente1=random.randint(1,10)
    terminoInd=random.randint(-15,15)
    coeficiente2=2*coeficiente1*terminoInd#we make sure its factorable, calculated with the definition of binomials
    seleccionar=random.randint(1,2)
    pregunta=[]
    if seleccionar==1:#ask for either coefficient 
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
#function factorizacion of cube binomials
def factorization_cube():
    coeficiente1=random.randint(1,10)
    terminoInd=random.randint(-15,15)
    coeficiente2=3*(coeficiente1**2)*terminoInd#make sure its factorable
    coeficiente3=3*coeficiente1*(terminoInd**2)
    seleccionar=random.randint(1,2)
    pregunta=[]
    if seleccionar==1:#ask for either x coefficient or independent term
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
#function for general test (2 questions per topic)
def generalTest(num):
    if num==1:#num is the question number, depending on it throws one or another question
        respUser,resp,preguntaActual=ecuaciones_lineales()
    elif num==2:
        respUser,resp,preguntaActual=ecuaciones_cuadraticas()
    elif num==3:
        respUser,resp,preguntaActual=sistemas_ecuaciones_1()
    elif num==4:
        respUser,resp,preguntaActual=sistemas_ecuaciones_2()
    elif num<7 and num>4:
        respUser,resp,preguntaActual=binomio()
    elif num>6 and num<9:
        respUser,resp,preguntaActual=fractions()
    elif num==9:
        respUser,resp,preguntaActual=factorization_square()      
    elif num==10:
        respUser,resp,preguntaActual=factorization_cube()     
    return respUser,resp,preguntaActual
#function check yes
def checkYes(respuesta):
    possibleErrorsYes=["Y","yes","YES","YEs","YeS"]#in case the user doesnt follow instructions
    if respuesta in possibleErrorsYes:
        respuesta="y"
    return respuesta
#function main
def main(): 
    repeat=True
    
    while repeat:
        calificacion=0#to keep the grade 
        mal=0##to know if it is wrong or right
        with open("registro.txt","w") as file:#creates a file for the answers
            file.write("")#just creates the file, dont write
        opcion=get_int("Hello user, welcome to the algebra test, the objective of this test is evaluate your knowledge on this fundamental topic for engineering.\n Now please select which topic do you want to practice:  \n General test (1) \n First and second degree equations (2) \n Systems of equations (3) \n Development of binomials (4) \n Simplification of algebraic fractions (5) \n Factorization of equations (6) \n Test cases (7) \n:")
        match opcion:#select which topic to study
            case 1:
                print("Read the questions carefully and with attention, follow the instructions as presented")
                for i in range(1,11):#keep track of the question number
                    print("Question %i"%(i))
                    respUser,resp,preguntaActual=generalTest(i)#saves current question and answers
                    calificacion,mal=verificador(resp,respUser,calificacion)#saves grade and if it is right or wrong
                    almacenarPreguntas(mal,preguntaActual,respUser,resp)#saves the question if it is wrong
                mostrarArchivo=input("Do you want me to show you which questions you got wrong? (y/n)")#asks if it wants to show the file
                checkYes(mostrarArchivo)
                if mostrarArchivo=="y":
                    mostrarRegistro()#shows file
                else: 
                    print("Ok")
                repeat=input("Wanna go again? (y/n)")#ask if it wants another test
                checkYes(repeat)
                if repeat=="y":
                    repeat=True
                else: 
                    repeat=False
                    print("Ok, have a good one!")
            case 2:
                preguntas=get_int("How many questions of the topic do you want? ")#makes sure dont introduce nonsense values
                cambio=1#to alternate between one or another, since several topics divided in different functions
                print("Read the questions carefully and with attention, follow the instructions as presented")
                for cont in range (1,preguntas+1):
                    print("Question %i"%(cont))
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
                checkYes(mostrarArchivo)
                if mostrarArchivo=="y":
                    mostrarRegistro()
                else: 
                    print("Ok")
                repeat=input("Wanna go again? (y/n)")
                checkYes(repeat)
                if repeat=="y":
                    repeat=True
                else: 
                    repeat=False
                    print("Ok, have a good one!")
            case 3:
                preguntas=get_int("How many questions of the topic do you want? ")
                cambio=1
                print("Read the questions carefully and with attention, follow the instructions as presented")
                for cont in range(1,preguntas+1):
                    print("Question %i"%(cont))
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
                checkYes(mostrarArchivo)
                if mostrarArchivo=="y":
                    mostrarRegistro()
                else: 
                    print("Ok")
                repeat=input("Wanna go again? (y/n)")
                checkYes(repeat)
                if repeat=="y":
                    repeat=True
                else: 
                    repeat=False
                    print("Ok, have a good one!")
            case 4:
                preguntas=get_int("How many questions of the topic do you want? ")
                print("Read the questions carefully and with attention, follow the instructions as presented")
                for cont in range(1,preguntas+1):
                    print("Question %i"%(cont))
                    respUser,resp,preguntaActual=binomio()
                    calificacion,mal=verificador(resp,respUser,calificacion)
                    almacenarPreguntas(mal,preguntaActual,respUser,resp)
                mostrarArchivo=input("Do you want me to show you which questions you got wrong? (y/n)")
                checkYes(mostrarArchivo)
                if mostrarArchivo=="y":
                    mostrarRegistro()
                else: 
                    print("Ok")
                repeat=input("Wanna go again? (y/n)")
                checkYes(repeat)
                if repeat=="y":
                    repeat=True
                else: 
                    repeat=False
                    print("Ok, have a good one!")
            case 5:
                preguntas=get_int("How many questions of the topic do you want? ")
                print("Read the questions carefully and with attention, follow the instructions as presented")
                for cont in range(1,preguntas+1):
                    print("Question %i"%(cont))
                    respUser,resp,preguntaActual=fractions()
                    calificacion,mal=verificador(resp,respUser,calificacion)
                    almacenarPreguntas(mal,preguntaActual,respUser,resp)
                mostrarArchivo=input("Do you want me to show you which questions you got wrong? (y/n)")
                checkYes(mostrarArchivo)
                if mostrarArchivo=="y":
                    mostrarRegistro()
                else: 
                    print("Ok")
                repeat=input("Wanna go again? (y/n)")
                checkYes(repeat)
                if repeat=="y":
                    repeat=True
                else: 
                    repeat=False
                    print("Ok, have a good one!")
            case 6:
                preguntas=get_int("How many questions of the topic do you want? ")
                cambio=1
                print("Read the questions carefully and with attention, follow the instructions as presented")
                for cont in range (1,preguntas+1):
                    print("Question %i"%(cont))
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
                checkYes(mostrarArchivo)
                if mostrarArchivo=="y":
                    mostrarRegistro()
                else: 
                    print("Ok")
                repeat=input("Wanna go again? (y/n)")
                checkYes(repeat)
                if repeat=="y":
                    repeat=True
                else: 
                    repeat=False
                    print("Ok, have a good one!")
            case 7:#if you want to check the test cases, which are pretty mid
                tests()
            case _:#if the user inserts an unvalid option, starts the whole thing over
                print("Please insert a valid option")
                main()#calls main again, starting over
"""Here we run the program"""
main()#calls for main and executes all of the program
