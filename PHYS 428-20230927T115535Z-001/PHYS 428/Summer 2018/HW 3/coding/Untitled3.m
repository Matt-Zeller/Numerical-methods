n=length(B);
X=zeros(n,1);
X(n)=b(n)/U(n,n);
 
for k=n-1:-1:1
 x(k)=( b(k) - U(k,k+1:n) * x(k+1:n) ) / U(k,k);
end