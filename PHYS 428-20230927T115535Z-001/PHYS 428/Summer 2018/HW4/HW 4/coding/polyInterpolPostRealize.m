%polyInterpol
%MATT ZELLER
%07/?/18
%PHYS 428

function [x,p]=polyInterpolCheb(n)
%Perfom poly interpolation using Chebyshev
%points

%x is the set of equally spaced points
%y is function to be interpolated(look
%at first example in polyfit doc)
for i=1:1000
    x(i) = -cos((pi/(n+1))*(0.5+i));
end

X = linspace(-1,1,1000)

y = sign(X)
    

%use polyfit to fit a nth-degree polynomial to
%the points
    p1 = polyfit(x,y,n)
    y1 = polyval(p1,x)
    
    p2 = polyfit(x,y,(2*n))
    y2 = polyval(p2,x)
    
    p4 = polyfit(x,y,(4*n))
    y4 = polyval(p4,x)
    
    figure
    subplot(3,2,[1,2])
    plot(x,y,x,y1)
    title(['Interpolation of |x| with Regular Points when n = ',num2str(n)])

    subplot(3,2,[3,4])
    plot(x,y,x,y2)
    title(['n = ',num2str(2*n)])
    ylabel('f(x)')

    subplot(3,2,[5,6])
    plot(x,y,x,y4)
    title(['n = ',num2str(4*n)])
    xlabel('x')
    
end