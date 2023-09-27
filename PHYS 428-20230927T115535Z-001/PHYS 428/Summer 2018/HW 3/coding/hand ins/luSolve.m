function x=luSolve(a,P,b)
[L,U,p] = lu(a);
b = P*b;
n = length(b);
x = zeros(n,1);
y = zeros(n,1);
%forward elim to find y in Ly=b (works)
y(1) = b(1);
    for i=2:n   
        sum = 0;            
        for j=1:i
            sum = sum+L(i,j)*y(j);
        end
        y(i) = b(i)-sum;
    end
%for the following for loop I used code from:

 %  NUMERICAL METHODS: Matlab Programs
% (c) 2004 by John H. Mathews and Kurtis D. Fink
%  Complementary Software to accompany the textbook:
%  NUMERICAL METHODS: Using Matlab, Fourth Edition
%  ISBN: 0-13-065248-2
%  Prentice-Hall Pub. Inc.
%  One Lake Street
%  Upper Saddle River, NJ 07458
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
x(n)=y(n)/U(n,n);

for k=n-1:-1:1
 x(k)=( y(k) - U(k,k+1:n) * x(k+1:n) ) / U(k,k);
end   
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
