% polyInterpol
% MATT ZELLER
% 07/?/18
% PHYS 428
% Perfom poly interpolation using equally
% x is the set of equally spaced points
% y is function to be interpolated(look
% at first example in polyfit doc)
% x1 is for finer mesh
n=8;
x = linspace(-1,1,n);
% generate chebyshev points in v
% for i = 1:n
% v = -cos((pi/(n+1))*(0.5+i));
% end
f = abs(x);
F = sign(x);
% use polyfit to fit a nth-degree polynomial to
% the points on the function

figure(1)
subplot(3,2,1)
subplot(3,2,2)
subplot(3,2,3)
subplot(3,2,3)
subplot(3,2,4)
subplot(3,2,5)
subplot(3,2,6)
subplot(3,2,7)
subplot(3,2,8)



for i = n:(2*i):32
    n
    p = polyfit(x,f,i);
    p1 = polyfit(x,F,i)
    %pC1 = polyfit(v,f,n)
    x1 = linspace(-1,1);
    f1 = polyval(p,x1);
    F1 = polyval(p1,x1);
    
    
    j=1
    
    figure(1)
    
    %subplot(3,2,j)
    subplot(3,2,j,'replace(3,2,j,3,2,j,3,2,j')
    plot(x,F,'o')
    hold on
    plot(x1,F1)
    plot(x1,sign(x1))
    hold off
    title(['n = ',num2str(i)])
    ylabel('f(x)')
    
    subplot(3,2,j,'replace(3,2,j+1)')
    plot(x,f,'o')
    hold on
    plot(x1,f1)
    plot(x1,abs(x1))
    hold off
    title(['n = ',num2str(i)])
    ylabel('f(x)')
    
    j = j + 3
    
end


