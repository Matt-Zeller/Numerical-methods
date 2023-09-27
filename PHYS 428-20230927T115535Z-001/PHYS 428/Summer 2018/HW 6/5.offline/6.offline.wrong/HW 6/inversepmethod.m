%inversepmethod
%Matt Zeller
%12/3/2018
%PHYS 428

%This program finds dominant eigenvalue of matrix A using
%inverse power method
A = [1 4 5; 4 -3 0; 5 0 7];
Ainv = inv(A);
v1 = (1/sqrt(3))*ones(3,1);
v2 = ones(3,1);
format long
disp(['n','    ','Estimate at n','     ','Reciprocal'])
disp(' ')
for n=1:10
    v2 = Ainv*v1;
    en = norm(v2,inf);
    disp([num2str(n),'    ',num2str(en),'                    ',num2str(1/en)])
    v2 = v2 / norm(v2,inf);
    v1 = v2;
end
disp(' ')
disp(' ')
disp(['The approximate eigenvalue of A nearest to q=1 is ',num2str(1/en),])
