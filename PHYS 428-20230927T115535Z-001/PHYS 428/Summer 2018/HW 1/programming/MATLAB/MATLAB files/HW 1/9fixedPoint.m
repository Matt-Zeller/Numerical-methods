%fixedPoint
%MATT ZELLER
%6/18/18
%PHYS 428

j = 10;
x(j) = 0.8;
a = 0.5;
En0 = 0.0;

for n = 1:j
    x(j) = 2*x(j)*(1-x(j));
    En1 = abs(a-x(j));
    r(j) = log(En1)/log(En0);
    En0 = En1;
    disp(['r = ',num2str(r(j),'%1.8e')])
end

display(' ')
display('     r = 0 as expected')

