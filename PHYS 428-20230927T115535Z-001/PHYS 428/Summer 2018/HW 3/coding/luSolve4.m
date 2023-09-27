function x=luSolve(a,P,b)
[L,U,p] = lu(a);
b = P*b;
n = length(b);
x = zeros(n,1);
y = zeros(n,1);
%lecture code forward elim
% for k=1:n-1
%     for i=k+1:n
%         y=L(i,k)/L(k,k);
%         for j=k+1:n
%             L(i,j)=L(i,j)-y*L(k,j);
%         end
%         b(i)=b(i)-y*b(k);
%     end
% end
%




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
for k=n-1:-1:1
 x(k)=( b(k) - U(k,k+1:n) * x(k+1:n) ) / U(k,k);
end   
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



 %backward sub (doesn't work)
% x(n)=b(n)/U(n,n)
% for i=n-1
%     s=0;
%     i
%     for j=i-1
%         j
%         s=s+U(i,j)*y(j)
% 
%     end
%     x(i)=(b(i)-s)/U(i,i)
% end
% end
% backwards substitution to find x in Ux=y
% x(n) = y(n)/U(n,n);
% for i=n-1:-1:1
%     for i=1:k
%         sum = 0.0;
%         for j=1:i
%             sum = sum+(y(n-U(n-k,n-j)*x(n-j,1)
%         end
%         x(n-k+1,1) = (y(n-k+1,1)-sum)/U(n-k,n-k)
%     end
%     
% end

