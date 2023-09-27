A = [1 4 5; 4 -3 0; 5 0 7];
vi = (1/sqrt(3))*[1; 1; 1];
vf = [0;0;0];
tol = 0
while tol > 5*10^-5
    r1 = vf/vi;
    vf = vi*A;
    r2 = vf/vi;
    tol = r2-r1;
    vi = vf;
end

vf