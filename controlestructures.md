### Team
+ Saul Alberto Barrera García - [GitHub](https://github.com/saulbg/Programming2)
+ Mario Solórzano Ventura - [GitHub](https://github.com/mariosolven/programming2)

CONTROL STRUCTURES
======
Selective structures are used to make logical decisions. A condition is evaluated and depending on the result of the same, one option or another is made.  

## Selective Control Structures  

+ **Simple Conditional**  

Selective simple or conditional structures are made up of only one condition if it is true it will execute the action or actions if the condition is false will do nothing. 

Sintax:

```c
if (condition) {  
	(Statement/Statements to be executed)
}    
```

+ **Double Conditional**  

It is composed only of a single condition, if it is true it will execute the action or actions and if the condition is false it will execute the actions for the false condition. 

Sintax:

```c 
if (condition) {  
	(Statement/Statements to be executed)  
}  else {  
	(Statement/Statements to be executed)  
}   
```

+ **Multiple Conditional**  

Multiple conditionals are made up of several simple conditional structures that are linked by the `else if` command.

Sintax:

```c  
if (condition) {  
	(Statement/Statements to be executed)  
} else if{  
	(Statement/Statements to be executed)  
} else {  
        (Statement/Statements to be executed)  
}  
```

+ **Nested Conditional**  

It is when several conditionals have the potential to be fulfilled all unlike the previous one. 

Sintax:

```c 
if (condition)
{  
        if (condition) 
        {  
                (Statement/Statements to be executed)
        }
        (Statement/Statements to be executed)
        } 
}  
```

## Iterative Control Structures  

Often in an algorithm, a group of statements needs to be executed again and again until a certain condition is met, this is where we find the need for iteration.

*The repeated execution of some groups of code statements in a program is called iteration.*

+ **For**

A `for` loop is a repetition control structure that allows you to efficiently write a loop that needs to execute a specific number of times.

Sintax:

```c
for (init; condition; increment) {
   statement(s);
}
```

+ **Nested for**

C programming allows to use one loop inside another loop. The following section shows a few examples to illustrate the concept.

Sintax:

```c
for (init; condition; increment) {

   for (init; condition; increment) {
      statement(s);
   }
   statement(s);
}
```

+ **While**

A `while` loop in C programming repeatedly executes a target statement as long as a given condition is true.

Sintax:

```c
while(condition) {
   statement(s);
}
```

+ **Do-While**

Unlike `for` and `while` loops, which test the loop condition at the top of the loop, the `do...while` loop in C programming checks its condition at the bottom of the loop.

A `do...while` loop is similar to a while loop, except the fact that it is guaranteed to execute at least one time.

Sintax:

```c
do {
   statement(s);
} while(condition);
```

+ **Break statement**

The `break` statement in C programming has the following two usages:

   1. When a break statement is encountered inside a loop, the loop is immediately terminated and the program control resumes at the next statement following the loop.

   2. It can be used to terminate a case in the `switch` statement.

If you are using nested loops, the `break` statement will stop the execution of the innermost loop and start executing the next line of code after the block.

Sintax:

```c
if( condition ) {
         /* terminate the loop using break statement */
         break;
      }
```

+ **Continue statement**

The `continue` statement in C programming works somewhat like the `break` statement. Instead of forcing termination, it forces the next iteration of the loop to take place, skipping any code in between.

   1. For the `for` loop, continue statement causes the conditional test and increment portions of the loop to execute. 
    
   2. For the `while` and `do...while` loops, continue statement causes the program control to pass to the conditional tests.

Sintax: 

```c
if(condition) {
         /* skip the iteration */
         statement(s);
         continue;
```

### References

+ https://www.tutorialspoint.com/cprogramming
+ http://www.marcossarmiento.com/2014/09/02/estructuras-selectivas-simples-dobles-y-multiples/

