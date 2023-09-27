%interpolError
%MATT ZELLER
%12/13/18
%PHYS 428

%Set n ad hoc for now
n=10;
%Initialize point arrays
xia = zeros(n,1);
xib = zeros(n,1);

%Build sets of points
for i=1:n
    %(a) case, indexed as i + 1 since i starts at 0
    xia(i) = -1 + (2*i/n);
    %(b) case
    xib(i) = -cos((pi/(n+1))*(0.5+i));
end

%Initialize w1, the variable storing terms to be
%multiplied in computation of wn, rep'd here
%as w2--initialize w2 too
w1=0;
w2=zeros(1000,1);
x=zeros(200,1);
%Build set of x values for wn(x)
for j=1:200
    x(j)= (j/100)-1;
    N(j)=j;
end

%initialize dummy variable for iterative
%multiplication to compute wn(a)
w0=1;
for j=1:200
    for i=1:n
        wna(j) = w0*(x(j)-xia(i));
        w0 = wna(j);
    end
end

%initialize dummy variable for iterative
%multiplication to compute wn(b)
w0=1;
for j=1:200
    for i=1:n
        wnb(j) = w0*(x(j)-xib(i));
        w0 = wnb(j);
    end
end
% plot(N,x)
% plot(x,wna)

subplot(2,1,1);
plot(x,wna)
title('Interpolation Error for n = 10')
ylabel('wn (a)')

subplot(2,1,2)
plot(x,wnb)
xlabel('x')
ylabel('wn (b)')