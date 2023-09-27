%inversepmethod
%Matt Zeller
%12/3/2018
%PHYS 428

%This program finds dominant eigenvalue of matrix A using
%Rayleigh Quotient
A = [1 4 5; 4 -3 0; 5 0 7];
v1 = (1/sqrt(3))*ones(3,1);
v2 = ones(3,1);
S = v1'*A/v1'*v1;
As = A-eye(3)*S;

disp(['n','    ','Estimate at n','                               ','Reciprocal'])
disp(' ')
format long
for n=1:20
    v2 = As'*v1;
    en = norm(v2,inf);
    disp([num2str(n),'    ',num2str(en,'%1.10e'),'                    ',num2str(1/en,'%1.10e')])
    v2 = v2 / norm(v2,inf);
    v1 = v2;
end
disp(' ')
disp(' ')
disp(['The approximate dominant eigenvalue of A is ',num2str(1/en),])
disp(['The associated eigenvector is '])
disp(' ')
disp(v2)

