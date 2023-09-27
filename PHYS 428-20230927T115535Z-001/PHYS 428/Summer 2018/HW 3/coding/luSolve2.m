%input needs to include p
function y=luSolve2(a,b)
[L,U,P] = lu(a);
b = P*b;
n = length(b);
x = zeros(n,1);
y = zeros(n,1);
y(1,1)=b(1,1);

%forward substitution to find y in Ly=b
for k=2:n
    for i=2:k   
        sum = 0.0;            
        for j=1:i
            sum = sum+L(k,j)*y(j,1);
        end
    end
    y(k,1) = b(k,1)-sum;
end
%backwards elimination to find x in Ux=y
for k=2:n
    for i=2:k   
        sum = 0.0;
        for j=1:i
            sum = sum+L(k,j)*x(j,1);
        end
    end
    x(k,1) = (y(k,1)-sum)/U(k,k);
end
end

