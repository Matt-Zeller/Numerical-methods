
disp('n             Relative Error        Relative residual')
disp(' ')

for n = 5:5:20
    [a,P]=mylu(hilb(n));
    x=ones(n,1);
    b=sum(hilb(n)')';
    x = luSolve(a,P,b);
    e = zeros(n,1);
   
    for i=2:n
        e(i)=x(i)-x(i-1);
    end
    
    r=b-a*x;
    relE=norm(e,inf)/norm(x,inf);
    relR=norm(r,inf)/norm(b,inf);
    
    disp([num2str(n),'             ',num2str(relE,'%1.4e'),'        ',num2str(relR,'%1.4e')])
end

disp('Error is increasing with n, while residual is decreasing, indicating')
disp('small residual does not necessarily correspond to small error.')
disp('If the problem was well conditioned however, small residual')
disp('would be likely to correspond to small error')

