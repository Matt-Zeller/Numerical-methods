%pmeth
%Matt Zeller
%12/3/2018
%PHYS 428

A = [1 4 5; 4 -3 0; 5 0 7];
v00 = ones(3,1);
v0 = ones(3,1);
v1 = ones(3,1);
v2 = ones(3,1);
v1 = (1/sqrt(3))*v1;
tolVec = 1;
tolVal = 1;
n = 0;
format long
%change tolVec to tolVal to evaluate convergence of the eigenvalue
while tolVec > 5*10^-5
    n=n+1;
    v2 = A*v1
    r2 = (v2(3,1)-v1(3,1))/(v1(3,1)-v0(3,1));
    r1 = (v1(3,1)-v0(3,1))/(v0(3,1)-v00(3,1));
    tolVec = abs(r2-r1);
    tolVal = abs((v2(3,1)/v1(3,1))-(v0(3,1)/v00(3,1)));
    v00 = v0;
    v0 = v1;
    v1 = v2;
end
domEig = v2(3,1)/v1(3,1)
n
tolVec
tolVal
v2