%y2
%Matt Zeller
%PHYS 428
%12/5/2018

%u2 is solution to y'(t), v2 is solution to y(t)
function y2(u1,v1)
format long
u2=u1+(0.5/6)*((  -sin(u1)  )  -  2*(  sin(u1 - 2*(  sin(u1)  )))  -  2*(  sin(u1 - 2*(  (  sin(u1 - 2*sin(u1))  )))  )  -  (  (sin(u1 - 2*(  sin(u1 - 2*(sin(u1 - 2*sin(u1)))))))  ))
v2=v1*((0.5^4)/24+(0.5^3)/6+(0.5^2)/2+0.5+1)
end
