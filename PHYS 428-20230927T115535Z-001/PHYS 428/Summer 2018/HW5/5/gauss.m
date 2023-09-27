%trapezoid
%Matt Zeller
%December 15 2018
%PHYS 428

%This script calculates an estimate of the
%integral of the function y on [a,b] using the
%trapezoid rule.

h=(b-a)/n;
T=zeros(1,n+1);
T(1,1)=0.5*z(a);
for i=2:1:n
    T(1,i)=z(a+(i-1)*h);
end
T(1,n+1)=0.5*z(b);
format long
T=h*sum(T);

function y = z(x)
y=sin(sqrt(pi*x));
end

