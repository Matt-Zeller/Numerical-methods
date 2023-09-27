%gauss
%Matt Zeller
%December 15 2018
%PHYS 428

%This script calculates an estimate of the
%integral of the function y on [0,1] using gaussian
%quadrature after a change of variables
%m is the estimation and er is error
t=[-0.861136311594053 -0.339981043584856 0.339981043584856 0.861136311594053];
c=[0.347854845137454 0.652145454862546 0.652145454862546 0.347854845137454];
n=4;
M=zeros(1,n);
for j=1:n
    M(1,j)=c(1,j)*(f(t(1,j)))*exp(-(f(t(1,j)))^2);
end
format long
m=0.5*sum(M)
er=abs(m-0.316060279414279)

function y = f(t)
    y=0.5*t+0.5;
end
