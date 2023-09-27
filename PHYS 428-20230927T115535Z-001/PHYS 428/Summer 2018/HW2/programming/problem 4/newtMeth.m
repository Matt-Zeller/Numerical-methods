%newtMeth
%MATT ZELLER
%06/25/18
%PHYS 428

%first guess x = 0
x = 0;
%number of iterations to be run
n = 10;
%initialize variable for numerical determination of order of convergence
En0 = 0.0;

%loop newton's method ten times
for i=0:n
    %function to be evaluated
    f =  27*x^4 + 162*x^3 - 180*x^2 + 62*x - 7;
    %derivative of function to be evaluated
    f1 = 108*x^3 + 486*x^2 - 360*x + 62;
    %Newton's iteration
    x = x - f/f1;
    %numerically determine order of convergence
    En1 = abs((1/3)-x);
    r = log(En1)/log(En0);
    En0 = En1;
    
end
display('The root is approximated as...')
x

display('...and the order of convergence is apparently one, since... ')
r

display('...which implies the multiplicity of this root is two or higher.')
display('Further, since the order of conv. is one, this converges as slowly')
display('as bisection.')