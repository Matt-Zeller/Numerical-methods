%integrator
%Matt Zeller
%December 15 2018
%PHYS 428

%This script calculates an estimate of the
%integral of the function y on [a,b]
%Outputs are, respectively, the estimated
%value and the difference between this value
%and the integral's true value
estimate=trapezoid(0,2*pi,363)
true=0.49907;
error=abs(true-estimate)
function T = trapezoid(a,b,n)
h=(b-a)/n;
T=zeros(1,n);
T(1,1)=0.5*z(a);
for i=2:1:n-1
    T(1,i)=z(a+i*h);
end
T(1,n)=0.5*z(b);
T=h*sum(T);
end
function y = z(x)
y=(exp(-x))*sin(x);
end

