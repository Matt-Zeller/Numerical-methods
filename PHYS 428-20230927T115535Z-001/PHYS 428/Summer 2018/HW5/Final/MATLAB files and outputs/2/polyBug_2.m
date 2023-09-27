%polyBug
%Matt Zeller
%PHYS 428
%Dec. 13, 2018

x=[0 .5 1 1.5 1.7 1.85 2 2.5 3 3.5 4 4.5 5 5.5 5.75 6];
y=[0 .9 1.2 1.35 1.4 1.7 1.95 2.3 2.35 2.4 2.35 2.25 1.8 1 .7 0]; 
v=[0 .5 1 1.25 1.5 1.75 2 2.25 2.5 2.75 3 3.25 3.5 3.75 4 4.25 4.5 4.75 5 5.25 5.5 5.75 6];
w=[0 0 0 0 0 .45 .6 .45 0 0 0 0 0 0 0 .45 .6 .45 0 0 0 0 0];


pu=polyfit(x,y,3);
pl=polyfit(v,w,3);

X = linspace(0,6);
Yu=(polyval(pu,X));
Yl=(polyval(pl,X));
su=spline(x,y,X);
sl=spline(v,w,X);

figure

plot(x,y,'o')
hold
plot(v,w,'o')
plot(X,Yu)
plot(X,Yl)
plot(X,su)
plot(X,sl)

xlabel('x')
ylabel('f(x)')
title('Spline vs. Polynomial Interpolation')
legend('Upper Data','Lower Data','Upper Polynomial','Lower Polynomial','Upper Spline','Lower Spline')
hold off

%Cubic spline interpolation is more accurate than 
%polynomial interpolation, since the spline more
%accurately reflects the nature of the data, especially
%near areas of large, abrupt changes in data