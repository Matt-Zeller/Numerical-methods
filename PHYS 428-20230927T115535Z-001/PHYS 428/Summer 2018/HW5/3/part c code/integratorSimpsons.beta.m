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
estimate=Simpsons(0,2*pi,362)
true=0.49907;
error=abs(true-estimate)
function S = Simpsons(a,b,n)
h=(b-a)/n;
S=zeros(1,n)
SOdd=zeros(1,0.5*n);
SEven=zeros(0.5*n,n);
S(1,1)=(1/3)*z(a);
for i=2:1:0.5*n
    SOdd(1,i)=z(a+i*h);
end
for i=0.5*n:1:n-1
    SEven(1,i)=z(a+i*h);
end
S(1,n)=(1/3)*z(b);
S=S+SEven+SOdd;
S=h*sum(S);
end
function y = z(x)
y=(exp(-x))*sin(x);
end

