A = [4 -1 0;-1 4 -1;0 -1 4];
xk = [1;2;3]
xkPlus = zeros(3,1);
b = [2;4;10];
xOpt = [1;2;3];
n = length(xk);

sum = 0;
sumShort = 0;

for i = 1:n
    for j = 1:10
        for h = 2:n
            sum = sum + A(i,h)*xk(h)
        end
%         for h = 1:n-1
%             sumShort = sumShort +A(i,h)*xk(h)
%         end
        xkPlus(i) = (b(i) - sum)/A(i,i)
    end
    sum = 0;
    sumShort = 0;
end

xkPlus