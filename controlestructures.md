### Team:
+ Saul Alberto Barrera García - [GitHub](https://github.com/saulbg/Programming2)
+ Mario Solórzano Ventura - [GitHub](https://github.com/mariosolven/programming2)

Control Structures
======
Selective structures are used to make logical decisions. A condition is evaluated and depending on the result of the same, one option or another is made.  

## Selective Control Structures  

+ Simple Conditional  
Selective simple or conditional structures are made up of only one condition if it is true it will execute the action or actions if the condition is false will do nothing.  

if (condition) {  
	(Statement/Statements to be executed)
}  
end  

+ Double Conditional  
It is composed only of a single condition, if it is true it will execute the action or actions and if the condition is false it will execute the actions for the false condition.  

if (condition) {  
	(Statement/Statements to be executed)  
}  else {  
	(Statement/Statements to be executed)  
}  
end  

+ Multiple Conditional  
Multiple conditionals are made up of several simple conditional structures that are linked by the elsif command.  

if (condition) {  
	(Statement/Statements to be executed)  
} else if{  
	(Statement/Statements to be executed)  
} else {  
        (Statement/Statements to be executed)  
}  
end

+ Nested Conditional  
It is when several conditionals have the potential to be fulfilled all unlike the previous one.  

if (condition)
{  
        if (condition) 
        {  
                (Statement/Statements to be executed)
        }
        (Statement/Statements to be executed)
        } 
}  
end  

## Iterative control structures  
