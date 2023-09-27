h=0.2;
n=1/h;
u1 = zeros(1,n);
u2 = zeros(1,n);
u1(1,1) = 0;
u1(1,2) = u1(1,1) + h*2*u1(1,1);
u2(1,1) = u1(1,1) + (h/2)*(2*u1(1,1) + 2*u1(1,2));
for i=2:1:n+1
    u1(1,i+1) = u2(1,i-1) + h*2*u2(1,i-1);
    u2(1,i) = u2(1,i-1) + (h/2)*(2*u2(1,i-1) + 2*u1(1,i+1));
end

u2(1,n)