
function [a,p]=mylu(a)
%this takes matrix a, generates matrix a in echelon form with the 
%corresponding permutation matrix p
[n n]=size(a); 
p = eye(n);
for k=1:n
    for i=1:(n-1)
        for j = 1:n
            %if the maximum value of a given column is not the pivot entry,
            %interchange it iteratively until it is
            if a(i+1,j) > a(i,j);
                store = a(i,j);
                storeP= p(i,:);
                a(i,j) = a(i+1,j);
                p(i,:) = p(i+1,:);
                a(i+1,j) = store;
                p(i+1,:) = storeP;
            end
        end
    end
end
p
end
    