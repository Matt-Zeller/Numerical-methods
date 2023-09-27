x(n)=b(n)/a(n,n);
for i=n-1:-1:1
    s=0;
    for j=i+1:n
        s=s+a(i,j)*x(j);
    end
    x(i)=(b(i)-s)/a(i,i);
end