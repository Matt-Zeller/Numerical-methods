A = [1 4 5; 4 -3 0; 5 0 7];
%vector array to store and recall vectors
V = ones(20,1);
%vectors
V(1,1) = (1/sqrt(3))*[1; 1; 1];
%initialize convergence tolerance
tol = 1;
%initialize indices
n = 0;
while tol > 5*10^-5
    n=n+1;
    %compute n+1-th vector
    V(n+1,1) = A*V(n,1);
    %compute ratios
    if n > 2
        r0 = V(n-2,1)/V(n-3,1);
        r1 = V(n-1,1)/V(n-2,1);
        r2 = V(n,1)/V/V(n-1,1);
        %compute convergence
        c = abs((r2-r1)/(r1-r0))
    end
end
