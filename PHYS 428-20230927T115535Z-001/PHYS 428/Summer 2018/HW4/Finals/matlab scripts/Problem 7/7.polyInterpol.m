%polyInterpol
%Matt Zeller
%PHYS 428
%Dec. 13, 2018

n=8;
x = linspace(-1,1,n);
f = abs(x);
F = sign(x);
% use polyfit to fit a nth-degree polynomial to
% the points on the function
p = polyfit(x,f,n);
p1 = polyfit(x,F,n);
x1 = linspace(-1,1);
f1 = polyval(p,x1);
F1 = polyval(p1,x1);

figure(1)
subplot(3,2,1)
plot(x,F,'o')
hold on
plot(x1,F1)
plot(x1,sign(x1))
hold off
title(['n = ',num2str(n)])

subplot(3,2,2)
plot(x,f,'o')
hold on
plot(x1,f1)
plot(x1,abs(x1))
hold off
title(['n = ',num2str(n)])


n=16;
x = linspace(-1,1,n);
f = abs(x);
F = sign(x);
% use polyfit to fit a nth-degree polynomial to
% the points on the function
p = polyfit(x,f,n);
p1 = polyfit(x,F,n);
x1 = linspace(-1,1);
f1 = polyval(p,x1);
F1 = polyval(p1,x1);

figure(1)
subplot(3,2,3)
plot(x,F,'o')
ylim([-4 4])
hold on
plot(x1,F1)
plot(x1,sign(x1))
hold off
title(['n = ',num2str(n)])
ylabel('f(x)')

subplot(3,2,4)
plot(x,f,'o')
ylim([0 1])
hold on
plot(x1,f1)
plot(x1,abs(x1))
hold off
title(['n = ',num2str(n)])

n=32;
x = linspace(-1,1,n);
f = abs(x);
F = sign(x);
% use polyfit to fit a nth-degree polynomial to
% the points on the function
p = polyfit(x,f,n);
p1 = polyfit(x,F,n);
x1 = linspace(-1,1);
f1 = polyval(p,x1);
F1 = polyval(p1,x1);

figure(1)
subplot(3,2,5)
plot(x,F,'o')
ylim([-4 4])
hold on
plot(x1,F1)
plot(x1,sign(x1))
hold off
title(['n = ',num2str(n)])
xlabel('x')

subplot(3,2,6)
plot(x,f,'o')
ylim([0 1])
hold on
plot(x1,f1)
plot(x1,abs(x1))
hold off
title(['n = ',num2str(n)])