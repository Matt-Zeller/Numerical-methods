function [a,P]=mylu(a)
%this takes matrix a, performs partial pivoting to prepare for LU decomp
[~,n]=size(a); 
P = eye(n);
for k=1:n
    for i=1:(n-1)
        for j = 1:n
            if abs(a(i+1,j)) < abs(a(i,j))
                store=a(i,:);
                a(i,:)=a(i+1,:);
                a(i+1,:)=store;
                storeP=P(i,:);
                P(i,:)=P(i+1,:);
                P(i+1,:)=storeP;
            end
        end
    end
end
end
    