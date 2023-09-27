h=0.1;
n=1/h
un=zeros(n,1);
j=1;
un(1,1)=1;
for i=0:h:1
    un(j+1,1)=un(j,1)*((1-h^2));
    j=j+1;
end
format long
un(n+1,1)
