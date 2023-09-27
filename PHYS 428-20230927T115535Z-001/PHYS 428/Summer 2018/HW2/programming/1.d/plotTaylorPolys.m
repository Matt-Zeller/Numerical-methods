%plotTaylorPolys
%MATT ZELLER
%06/25/18
%PHYS 428

%actual function
x = linspace(-2,2,100);
y = sin((pi*x)/2);

%first degree taylor polynomial
y1 = (pi/4)*x;
%third degree...
y3 = y1-((pi.^3)/48)*(x.^3);
%fifth degree...
y5 = y3+((pi.^5)/3840)*(x.^5);
%seventh degree...
y7 = y5-((pi.^7)/645120)*(x.^7);

%encapsulate all following plot commands within one end display, one figure
figure
%initialize each subplot... not sure what three digits do
ax1=subplot(5,1,1);
ax2=subplot(5,1,2);
ax3=subplot(5,1,3);
ax4=subplot(5,1,4);
ax5=subplot(5,1,5);
%define the x domain
x = linspace(-2,2);
%tell matlab to show these functions
y;
y1;
y3;
y5;
y7;
%tell matlab which titles to display, per subplots
plot(ax1,x,y);
title(ax1,'Actual Function')

plot(ax2,x,y1);
title(ax2,'First Degree')


plot(ax3,x,y3);
title(ax3,'Third Degree')
ylabel(ax3,'f(x)')

plot(ax4,x,y5);
title(ax4,'Fifth Degree')

plot(ax5,x,y7);
title(ax5,'Seventh Degree')
xlabel(ax5,'x')
