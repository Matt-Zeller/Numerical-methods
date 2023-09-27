%for now, L must be 3x3, b 3x1, x 3x1, n=3

function [x] = forwardSub(L, b)
n = length(b);
x = zeros(n,1);

x(1,1) =  b(1,1)/L(1,1);
x(2,1) = (b(2,1) - L(2,1)*x(1,1))/L(2,2);
x(3,1) = (b(3,1) - L(3,2)*x(2,1) - L(3,1)*x(1,1))/L(3,3);

end

disp(

    
