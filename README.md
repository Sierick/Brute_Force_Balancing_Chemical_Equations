# Brute_Force_Balancing_Chemical_Equations
Brute Force Balancing Chemical Equations Script

To use the script you have to change the var variables and the co variables to the values in the chemical equation you are balancing.
These variables are hard coded because otherwise there are over 20 inputs.

The var variables are split up into four sections with var1, var2, var3, and var4.
Each one of these is a different element in your equation.
The order of these doesn't matter as long as you are consistant.

There are four variables for each var section.
These are the position in the equation there are left to right.

Then there are the co variables.
co is short for Coffient they are in order left to right with co1 being the left most.

The final thing you may want to change is the range of the random number generation for the brute force aspect.
I have it set as 1-10 by default because as the range increases the time to solve also increases.
