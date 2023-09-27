%for now, U must be 3x3, b 3x1, x 3x1, n=3
function [x] = backwardsub(U, b)
n = length(b);
x = zeros(n,1);

x(3,1) =  b(3,1)/U(3,3);
x(2,1) = (b(2,1) - U(2,3)*x(3,1))/U(2,2);
x(1,1) = (b(1,1) - U(1,2)*x(2,1) - U(1,3)*x(3,1))/U(1,1);

end

    
