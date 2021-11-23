clear
clc
close('all');

N=10;
I=randi([0,1],[1 N]);
A=6;
%%%Gray
Gray=[];
for i=1:N
    if I(i)==1
        Gray(i)=A;
    else
        Gray(i)=-A;
    end
end
 
%%%surechantillonnage
K=8;
F=8;
Tb=1;
fe=F/Tb;
 
l=(N-1)*(F-1)-N;
ae=zeros(1,l);
ae(1)=Gray(1);
for i=1:N-1
    ae(i*F+1)=Gray(i+1);
end
I;
Gray;
ae;
 
%%%%filtrage
alpha=0.5;
syms z;
g=(1/(sqrt(Tb)))*(sin(pi*z*(1-alpha))+4*alpha*z.*cos(pi*z*(1+alpha)))./(pi*z.*(1-(4*alpha*z).*(4*alpha*z)));
l1=eval(limit(g,z,0));
l2=eval(limit(g,z,Tb/(4*alpha)));
l3=eval(limit(g,z,-Tb/(4*alpha)));
 
t=-K*Tb:1/F:K*Tb;
g=(1/(sqrt(Tb)))*(sin(pi*t*(1-alpha))+4*alpha*t.*cos(pi*t*(1+alpha)))./(pi*t.*(1-(4*alpha*t).*(4*alpha*t)));
g(find(t==0))=l1;
g(find(t==Tb/(4*alpha)))=l2;
g(find(t==-Tb/(4*alpha)))=l3;
figure('Name','Partie 1 question 1')
plot(t,g);
title('réponse impulsionnelle d’un filtre en racine de cosinus surélevé')
 
%%%%energie
energie=0;
for i=1:length(g)
    energie=energie+g(i)^2;
end
energie;
 
Eb=energie*A*A;
RSB=4;
N0=0
e=conv(ae,g);
B=sqrt(N0/2)*randn(1,length(e));
r=e+B;
z=conv(r,g);
figure('name','signsignal apres sortie du filtre de reception');
plot(z);
 
%%%%decimation
d=[];
t0=length(g);
for i=0:N-1
    d=[d z(t0+i*F)];
end
Gray
decision=sign(d)*A
decision(1)=A
Nb_erreur = sum( (abs(Gray - decision))/(2*A) )