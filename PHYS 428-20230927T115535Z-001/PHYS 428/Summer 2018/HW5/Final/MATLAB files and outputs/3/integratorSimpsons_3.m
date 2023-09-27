%integratorSimpsons
%Matt Zeller
%December 15 2018
%PHYS 428

%This script calculates an estimate of the
%integral of the function y on [a,b] using
%Simpson's rule.
%Outputs are, respectively, the estimated
%value and the difference between this value
%and the integral's true value.
estimate=Simpsons(0,2*pi,125)
true=0.49907;
error=abs(true-estimate)
function S = Simpsons(a,b,n)
h=(b-a)/n;
S=zeros(1,n);
S(1,1)=(1/3)*z(a);
for i=2:1:(0.5*n)-2
    S(1,i)=(4/3)*z(a+(2*(i-1))*h)+(2/3)*z(a+(2*i)*h);
end
S(1,n)=(1/3)*z(b);
S=h*sum(S);
end
function y = z(x)
y=(exp(-x))*sin(x);
end

