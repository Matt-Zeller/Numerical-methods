%asks for x value, gives function value - a template
function u2(u1,v1)
format long
u2=u1+(0.5/6)*((  -sin(u1)  )  -  2*(  sin(u1 - 2*(  sin(u1)  )))  -  2*(  sin(u1 - 2*(  (  sin(u1 - 2*sin(u1))  )))  )  -  (  (sin(u1 - 2*(  sin(u1 - 2*(sin(u1 - 2*sin(u1)))))))  ))
v2=v1*((0.5^4)/24+(0.5^3)/6+(0.5^2)/2+0.5+1)
end
