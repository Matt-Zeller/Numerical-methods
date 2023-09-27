A = [4 -1 0;-1 4 -1;0 -1 4];
xk = zeros(3,1);
xkPlus = zeros(3,1);
b = [2;4;10];

w = 2/(1+sqrt(7/8))

for n = 1:100
    xkPlus(1) = xk(1) - w*(A(1,1)*xk(1) + A(1,2)*xk(2) + A(1,3)*xk(3) - b(1))/A(1,1)
    xkPlus(2) = xk(2) - w*(A(2,1)*xkPlus(1) + A(2,2)*xk(2) + A(2,3)*xk(3) - b(2))/A(2,2)
    xkPlus(3) = xk(3) - w*(A(3,1)*xkPlus(1) + A(3,2)*xkPlus(2) + A(3,3)*xk(3) - b(3))/A(3,3)
    if norm((xkPlus - xk), inf) < 10^-7
        n
        break
    end
    
    xk = xkPlus

end

xkPlus