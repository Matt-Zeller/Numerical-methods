%oneStepEuler
%Matt Zeller
%PHYS 428
%12/3/2018

h=0.001;
n=1/h
un=zeros(n,1);
j=1;
for i=0:h:1
    
    un(j,1)=(1+2*h)^j;
    j=j+1;
    
end
format long
un(n+1,1)
