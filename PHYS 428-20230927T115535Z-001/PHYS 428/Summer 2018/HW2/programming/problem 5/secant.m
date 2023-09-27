%secant
%MATT ZELLER
%06/25/2018
%PHYS 428

%This file determines unknown secant convergence outcomes for comparison
%to known newton convergence outcomes for the same problem

%first guesses
x0 = -2;
x1 = -3;
%number of iterations to be run
n = 10;

%loop secant method ten times
for i=0:n
    %function to be evaluated
    f0 = x0^3 + 2*x0^2 - 3*x0 - 1;
    f1 = x1^3 + 2*x1^2 - 3*x1 - 1;
    %Secant iteration
    x2 = x1 - (f1*(x1-x0))/(f1 - f0);
    
    disp(['i = ',num2str(i),'     r = ',num2str(r,'%1.15e'), '      x0 = ',num2str(x0,'%1.15e'),'     x1 = ',num2str(x1,'%1.15e'),'     x2 = ',num2str(x2,'%1.15e')])
    
    x0 = x1;
    x1 = x2;
end

display('Secant method reaches an approximation accurate to within near') 
display('10^-11 in 6 steps with 6 function evaluations')

