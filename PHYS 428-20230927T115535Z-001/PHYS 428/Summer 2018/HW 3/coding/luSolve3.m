function x=luSolve3(a,b)
[L,U,P] = lu(a);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%from forwardSub.m
%%%%%%%%%%%%%%%%%%%%%%%%%%%%
b = P*b;
n = length(b);
y = [2;2.2;-2];
x = zeros(n,1);
x(1,1) = b(1,1);
%backwards substitution to find y in Ly=b
for k=2:n
    for i=2:k   
        sum = 0.0
        for j=1:i
            sum = sum+L(k,j)*x(j,1)
        end
    end
    x(k,1) = (y(k,1)-sum)/U(k,k)
end
end