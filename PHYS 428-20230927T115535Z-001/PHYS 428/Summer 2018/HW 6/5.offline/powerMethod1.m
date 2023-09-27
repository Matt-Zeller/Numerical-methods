A = [1 4 5; 4 -3 0; 5 0 7];
v0 = ones(3,1);
v1 = ones(3,1);
v2 = ones(3,1);
v1 = (1/sqrt(3))*v1;
format long
for n=1:20
    v11 = v1(3,1);
    v2 = A*v1
    r = v2(3,1)/v11
    v0 = v11;
    v1 = v2;
end
