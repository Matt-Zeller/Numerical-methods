%iterMeth
%MATT ZELLER
%PHYS 428
%7/13/2018

%This program solves a linear system of equations A using Jacobi,
%Gauss-Seidel, and SOR iterative methods

%A in Ax=b
A = [4 -1 0;-1 4 -1;0 -1 4];
%b in Ax=b
b = [2;4;10];

%Optimal solution
x = [1;2;3];

%Initialize x's of the kth step, (k-1)th step, and (k+1)th step, respectively 
xk = zeros(3,1);
xkMin = zeros(3,1);
xkPlus = zeros(3,1);

%Initialize vectors that will hold error at step N for each method
eJ = zeros(100,1);
eGS = zeros(100,1);
eSOR = zeros(100,1);
N = zeros(100,1);

%Omega parameter for SOR
w = 2/(1+sqrt(7/8));

%Loop to solve iterative system using Jacobi's method
for n = 1:100
    %Compute the three vector entries for nth x
    xkPlus(1)=(b(1) - A(1,2)*xk(2) - A(1,3)*xk(3))/A(1,1);
    xkPlus(2)=(b(2) - A(2,1)*xk(1) - A(2,3)*xk(3))/A(2,2);
    xkPlus(3)=(b(3) - A(3,2)*xk(2) - A(3,1)*xk(1))/A(3,3);
    
    %Compute nth asymptotic error constant estimate c
    cJ(n) = norm((xkPlus-xk),inf)/norm(xk-xkMin,inf);
    
    %Prepare for the next computation of x and c
    xkMin = xk;
    xk = xkPlus;
    
    %Store iteration number in a vector to represent x-axis of later plot of
    %errors of Jacobi, Gauss-Seidel, and SOR methods
    N(n+1) = n;
    
    %Computer nth error
    eJ(n) = (norm(x-xk,inf));
    
    %Cease looping if error is less than 10^-7
    if norm((xkPlus - xk), inf) < 10^-7
        break
    end
end

xkPlus

% %Reset x vectors for Gauss-Seidel
% xk = zeros(3,1);
% xkPlus = zeros(3,1);
% xkMin = zeros(3,1);
% 
% for n = 1:100
%     xkPlus(1)=(b(1) - A(1,2)*xk(2) - A(1,3)*xk(3))/A(1,1);
%     xkPlus(2)=(b(2) - A(2,1)*xkPlus(1) - A(2,3)*xk(3))/A(2,2);
%     xkPlus(3)=(b(3) - A(3,2)*xkPlus(2) - A(3,1)*xkPlus(1))/A(3,3);
%     cGS(n) = norm((xkPlus-xk),inf)/norm(xk-xkMin,inf);
%     xkMin = xk;
%     xk = xkPlus;
%     eGS(n)=(norm(x-xk,inf));
%     if norm((xkPlus - xk), inf) < 10^-7
%         break
%     end
% end
% 
% xk = zeros(3,1);
% xkPlus = zeros(3,1);
% xkMin = zeros(3,1);
% for n = 1:100
%     xkPlus(1) = xk(1) - w*(A(1,1)*xk(1) + A(1,2)*xk(2) + A(1,3)*xk(3) - b(1))/A(1,1);
%     xkPlus(2) = xk(2) - w*(A(2,1)*xkPlus(1) + A(2,2)*xk(2) + A(2,3)*xk(3) - b(2))/A(2,2);
%     xkPlus(3) = xk(3) - w*(A(3,1)*xkPlus(1) + A(3,2)*xkPlus(2) + A(3,3)*xk(3) - b(3))/A(3,3);
%     cSOR(n) = norm((xkPlus-xk),inf)/norm(xk-xkMin,inf);
%     xkMin = xk;
%     xk = xkPlus;
%     if norm((xkPlus - xk), inf) < 10^-7
%         break
%     end
%     xk = xkPlus;
%     eSOR(n)=(norm(x-xk,inf));
% end
% 
% semilogy(N,eJ,N,eGS,N,eSOR)
%plot(N,cJ,N,cGS,N,cSOR)
%disp([num2str(N,'%u'), num2str(cJ,'%1.8e')])