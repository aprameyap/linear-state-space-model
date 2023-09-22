# linear-state-space-model
A simple, linear state space model

As systems become more complex, representing them with differential equations or transfer functions becomes cumbersome.  This is even more true if the system has multiple inputs and outputs.  This document introduces the state space method which largely alleviates this problem.  The state space representation of a system replaces an nth order differential equation with a single first order matrix differential equation.  The state space representation of a system is given by two equations :
![](https://lpsa.swarthmore.edu/Representations/SS/img48.gif)

Note: Bold face characters denote a vector or matrix. The variable x is more commonly used in textbooks and other references than is the variable q when state variables are discussed.  The variable q will be used here since we will often use x to represent position.

The first equation is called the state equation, the second equation is called the output equation.  For an nth order system (i.e., it can be represented by an nth order differential equation) with r inputs and m outputs the size of each of the matrices is as follows:

q is nx1 (n rows by 1 column); q is called the state vector, it is a function of time
A is nxn; A is the state matrix, a constant
B is nxr; B is the input matrix, a constant
u is rx1; u is the input, a function of time
C is mxn; C is the output matrix, a constant
D is mxr; D is the direct transition (or feedthrough) matrix, a constant
y is mx1; y is the output, a function of time

Note several features:
The state equation has a single first order derivative of the state vector on the left, and the state vector, q(t), and the input u(t) on the right.  There are no derivatives on the right hand side.
The output equation has the output on the left, and the state vector, q(t), and the input u(t) on the right.  There are no derivatives on the right hand side.


This text is purely copy pasted from: [https://lpsa.swarthmore.edu/Representations/SysRepSS.html](https://lpsa.swarthmore.edu/Representations/SysRepSS.html) to give some context about state space representation.
