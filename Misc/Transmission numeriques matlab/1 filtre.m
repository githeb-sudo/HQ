function [g ] = filtre( Tb, alpha,t)
g=(1/sqrt(Tb))*((sin((pi*t/Tb)*(1-alpha))+((4*alpha*t/Tb).*cos((pi*t/Tb)*(1+alpha))))./((pi*t/Tb).*(1-(4*t*alpha/Tb).^2)));
end
