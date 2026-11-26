# Alegebra-test

Engineers are some of the most important jobs that exist nowadays. If it hadn't been by them, humanity wouldn't be where it is right now, from the technology at the reach of our hands, to life-saving machinery and structure. Engineers have relevance anywhere in the world, despite their specialization they have direct impact on human lives, making critical their general knowledge to ensure the quality and safety of their actions. 

In this context, the most important basis for engineering is algebra, since this topic is required for the expertise and full comprehension in any of the engineering areas. Thus making crucial de practice and understanding of algebra for a successful engineering career. 

This test is designed to evaluate the users knowledge on different topics of algebra. At the beginning of the program, the user is asked if they want to make a general test, having only a few questions per topic, or do a deep dive in a specific topic. The topics included are first and second degree equations, systems of equations of 2 and 3 variables, development of binomials, factorization of equations and simplification of algebraic fractions. 

At the end of the test, the user is asked if they want to consult the questions that they got wrong, and if they do, then a file is given that has the question, the user answer and the computer answer for the problem. 

(The matrices are going to be implemented in the calculation of the results of systems of equations, and the files are going to be involved in the didactic material)

# Instructions # 

Inputs: 

  -Topic for the test or general test

  -The answers given by the user throughout the test
  
  -If they want file with wrong answers
  
Outputs: 

  -Right or wrong answer
  
  -Calculated answer
  
  -Corresponding questions
  
  -Final results
  
  -Corresponding wrong answers and questions
  
Process:

  1. Analyze the topic wanted for the test
  
  2. Based on the answer, determine which and how many questions to throw the user
  
  3. Import random values for the coeficients of equiations, in the case of algebraic fractions also randomize the values for exponents of variables
  
  4. Determine the question to show the user
  
  5. Show the user the question
  
  6. Read the user's answer 
  
  7. Calculate the result 
  
  8. Show the user if it got the question right or wrong

  9. If it was wrong, save the question in a file
  
  10. Repeat this process until all the questions asigned are showed and answered
  
  11. Show the final grade of the user
  
  12. Ask if they want register of wrong answers
  
  13. If yes, then show the file with the question, answer by the user and computer answer
  
  14. If not, end program


For the use of the external library integrated into the program (cs50), to install it you have to go to the terminal of your computer, write "pip install cs50" and hit enter, which will automatically download all the requirements for the use of this library. 

To run the program, download it and run it in terminal with 'python algebra_test.py' (to run it you need to have the right route in terminal)

Note: the reason that strings won't be used in this proyecto is because of the nature of it, since most of the otuputs or ptinrting for the user are going to be numbers, there is not much point in the string maniuplation, since it is not a key function, we just need the basics to be able to communicate to the reader. In other words, the proyect is mostly numbers and we only need strings to ask the question. 

