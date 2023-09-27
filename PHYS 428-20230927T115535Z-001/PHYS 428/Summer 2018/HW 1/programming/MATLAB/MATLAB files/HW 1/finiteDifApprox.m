%finiteDifApprox
%MATT ZELLER
%06/18/18
%PHYS 428

x = pi/4;
n = 6;
h = 0;
error = 0;

disp('FORWARD DIFFERENCE APPROXIMATION')
for j=1:n
    
    h(j) = 1/2^j;
    deriv = (sin(x+h(j))- sin(x))/h(j);
    error(j) = deriv-sin(x);
    errPerH(j) = error(j)/h(j);
    errPerSquaredH(j) = error(j)/h(j)^2;
    errPerCubedH(j)= error(j)/h(j)^3;
    
    disp(['h = ',num2str(h(j),'%1.8e'), ', error = ',num2str(error(j),'%1.8e'),', error / h = ',num2str(errPerH(j),'%1.8e'),', error / h^2 = ',num2str(errPerSquaredH(j),'%1.8e'),', error / h^3 = ',num2str(errPerCubedH(j),'%1.8e')]) 

   
end

hC = 0;
errorC = 0;

disp('CENTRAL DIFFERENCE APPROXIMATION')
for j=1:n
    
    hC(j) = 1/2^j;
    deriv = (sin(x+hC(j))- sin(x-hC(j)))/2*hC(j);
    errorC(j) = deriv-sin(x);
    errPerHC(j) = errorC(j)/hC(j);
    errPerSquaredHC(j) = errorC(j)/hC(j)^2;
    errPerCubedHC(j)= errorC(j)/hC(j)^3;
    
    disp(['h = ',num2str(hC(j),'%1.8e'), ', error = ',num2str(errorC(j),'%1.8e'),', error / h = ',num2str(errPerHC(j),'%1.8e'),', error / h^2 = ',num2str(errPerSquaredHC(j),'%1.8e'),', error / h^3 = ',num2str(errPerCubedHC(j),'%1.8e')]) 

end

loglog(h,abs(error))
title('log(error) vs. log(h)')
xlabel('log(h)')
ylabel('log(abs(error)')

hold on

loglog(hC,abs(errorC))

disp('Forward difference is more accurate since error is proportional to h and central difference involves twice as much h as forward difference')