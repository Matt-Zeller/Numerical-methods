h=0.1;
n=1/h
exact=exp(2);
un=zeros(n,1);
j=1;
for i=0:h:1
    
    un(j,1)=(1+2*h)^j;
    j=j+1;
    
end
format long
un(n+1,1)
