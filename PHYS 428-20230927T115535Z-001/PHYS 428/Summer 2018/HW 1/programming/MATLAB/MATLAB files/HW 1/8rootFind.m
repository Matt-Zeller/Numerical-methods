%rootFind
%MATT ZELLER
%06/18/18
%PHYS 428

%initial parameters for each method
j = 10;
p = sqrt(5);
%initial parameters for bisection
a = 2;
b = 3;
%bisection loop
disp('BISECTION')
for n = 1:j
    x = (a + b)/2;
    f = x^2 - 5;
    fa= a^2 - 5;
    err = abs(p - x);
    if (f*fa) < 0
        b = x;
    else
        a = x;
    end
    disp(['n = ',num2str(n),'     xn (approximation) = ',num2str(x,'%1.15e'),'     f(xn) (residual) = ',num2str(f,'%1.15e'),'     |p-xn| (error) = ',num2str(err,'%1.15e')]) 
end

%initial parameters for fixed point
x = 2.5;
%fixed point loop w/ g1
disp('FIXED POINT, G1')
for n = 1:j
    x=5/x;
    f = x^2 - 5;
    err = abs(p - x);
    disp(['n = ',num2str(n),'     xn (approximation) = ',num2str(x,'%1.15e'),'     f(xn) (residual) = ',num2str(f,'%1.15e'),'     |p-xn| (error) = ',num2str(err,'%1.15e')])
end

%fixed point loop w/ g2
disp('FIXED POINT, G2')
for n=1:j
    x=x-((x^2) - 5)/3;
    f = x^2 - 5;
    err = abs(p - x);
    disp(['n = ',num2str(n),'     xn (approximation) = ',num2str(x,'%1.15e'),'     f(xn) (residual) = ',num2str(f,'%1.15e'),'     |p-xn| (error) = ',num2str(err,'%1.15e')])
end

%initial parameters for newton's
x = 2.5;
%newton's method
disp('NEWTONS METHOD')
for n=1:j
    x = x - (((x^2) - 5)/(2*x));
    f = x^2 - 5;
    err = abs(p - x);
    disp(['n = ',num2str(n),'     xn (approximation) = ',num2str(x,'%1.15e'),'     f(xn) (residual) = ',num2str(f,'%1.15e'),'     |p-xn| (error) = ',num2str(err,'%1.15e')])
end