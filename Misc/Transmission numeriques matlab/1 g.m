clc;

clear all;

close all;

%partie1

%question 1

N=8;

A=2;

R=randi([0,1],1,N);

s=(R*2*A)-A;
%question 2

Tb=1;

F=8;

f=F/Tb;

z=zeros(1,F-1);

x=s(1);

for i=2:1:N

    x=[x z s(i)];

end
n=1:length(x);

scatter(n,x);

%partie 2

syms t; %to construct a symbolic number

alpha1=0.1;

alpha2=0.25;

alpha3=0.9;

Tb=1;

 
f1=filtre(Tb,alpha1,t);

f2=filtre(Tb,alpha2,t);

f3=filtre(Tb,alpha3,t);


limite11=eval(limit(f1,t,0)); 
limite12=eval(limit(f1,t,(Tb/(4*alpha1))));
limite13=eval(limit(f1,t,(-Tb/(4*alpha1))));


limite21=eval(limit(f2,t,0)); 
limite22=eval(limit(f2,t,(Tb/(4*alpha2)))); 
limite23=eval(limit(f2,t,(-Tb/(4*alpha2))));


limite31=eval(limit(f3,t,0));
limite32=eval(limit(f3,t,(Tb/(4*alpha3))));
limite33=eval(limit(f3,t,(-Tb/(4*alpha3))));
%question2

K=8;

intervalle=-K*Tb:1/K:K*Tb; %longueur d'intervalle 2*Tb

vecteur1=filtre(Tb,alpha1,intervalle);

vecteur2=filtre(Tb,alpha2,intervalle);

vecteur3=filtre(Tb,alpha3,intervalle);


% on rajoute les limites en 0 , en (Tb/(4*alpha1)et en (-Tb/(4*alpha1)


vecteur1(find(intervalle==0))=limite11 ;
vecteur1(find(intervalle==(Tb/(4*alpha1))))=limite12;
vecteur1(find(intervalle==(-Tb/(4*alpha1))))=limite13;


vecteur2(find(intervalle==0))=limite21;% on rajoute les limites vecteur2(find(intervalle==(Tb/(4*alpha2))))=limite22; vecteur2(find(intervalle==(-Tb/(4*alpha2))))=limite23;


vecteur3(find(intervalle==0))=limite31;% on rajoute les limites vecteur3(find(intervalle==(Tb/(4*alpha3))))=limite32;

 
vecteur3(find(intervalle==(-Tb/(4*alpha3))))=limite33;

figure;

plot(intervalle,vecteur1,'b');

hold on

plot(intervalle,vecteur2,'r');

plot(intervalle,vecteur3,'g');

legend('alpha=0.1','alpha=0.25','alpha=0.9');
title('filtre de mise en forme');
vecteur11=vecteur1.^2;

vecteur22=vecteur2.^2;

vecteur33=vecteur3.^2;


energie1=sum(vecteur11);

energie2=sum(vecteur22);

energie3=sum(vecteur33);
%question5

%pour obtenir le signal e(t) il suffit de convoluer l'entrée a(t) avec le %filtre de mise en forme.

ech1=conv(s,vecteur1);

ech2=conv(s,vecteur2);

ech3=conv(s,vecteur3);

%ehantillon aprés filtrage

figure;

plot(ech1,'b');

hold on

plot(ech2,'r');

plot(ech3,'g');

legend('alpha=0.1','alpha=0.25','alpha=0.9'); 
title('signal apres filtrage');
B=randn(1,length(ech1)); 

Eb_N0 = 4 ; %const == Eb/N0 en db c'est le rapport signal sur bruit ; 
sigmaa= sqrt(0.5*((A^2)*F*10^(-Eb_N0)/10)) ;

%Eb=A^2*F (densité spectrale du signal=variance du signal par rapport autemps), or le la variance de notre signal est égal à A² ; sigma=sqrt(N0/2))

B=sigmaa.*B ;

figure;

plot(B);

title('Bruit blanc gaussien de variance sigmaa');
Tb=1 ;
Ts= 1 ;

N=8;

alpha=0.1; subplot(3,1,1) ; syms t ; f1=filtre(Tb,alpha,t) ; L11=eval(limit (f1,t,0)); L12=eval(limit(f1,t,(Tb/(4*alpha)))); L13=eval(limit(f1,t,(-Tb/(4*alpha)))); K=8 ;


axe=-K*Tb:Ts/F:K*Tb ;

v1=filtre(Tb,alpha,axe) ;
v1(find(axe==0))=L11;
v1(find(axe==Tb/(4*alpha)))=L12 ;
v1(find(axe==-Tb/(4*alpha)))=L13 ;

for i=0:100
R =randi([0,1],1,N);
 
R1 =(R*2*A)-A ;

z=zeros(1,(N-1)*F+1);
z(1:F:(N-1)*F+1)=R1 ;
z=conv(z,v1) ;
plot(conv(z,v1)) ;
title 'alpha= 0.1 , K = 8' ;

hold on
end
%----------------------------------%
Tb=1 ;
Ts= 1 ;

N	=8;
alpha=0.25;

subplot(3,1,2); syms t ; f1=filtre(Tb,alpha,t) ; L11=eval(limit (f1,t,0)); L12=eval(limit(f1,t,(Tb/(4*alpha)))); L13=eval(limit(f1,t,(-Tb/(4*alpha)))); K=8 ;

axe=-K*Tb:Ts/F:K*Tb ;

v1=filtre(Tb,alpha,axe) ;

v1(find(axe==0))=L11;
v1(find(axe==Tb/(4*alpha)))=L12 ;
v1(find(axe==-Tb/(4*alpha)))=L13 ;

for i=0:100

R	=randi([0,1],1,N); R1 =(R*2*A)-A ; z=zeros(1,(N-1)*F+1); z(1:F:(N-1)*F+1)=R1 ; z=conv(z,v1) ; plot(conv(z,v1)) ;

title 'alpha= 0.25 , K = 8' ; hold on

end

%_________________________________________% Tb=1 ;

Ts= 1 ; N =8; alpha=0.9; subplot(3,1,3) ; syms t ; f1=filtre(Tb,alpha,t) ; L11=eval(limit (f1,t,0)); L12=eval(limit(f1,t,(Tb/(4*alpha)))); L13=eval(limit(f1,t,(-Tb/(4*alpha)))); K=8 ;



axe=-K*Tb:Ts/F:K*Tb ;

v1=filtre(Tb,alpha,axe) ;
v1(find(axe==0))=L11;
v1(find(axe==Tb/(4*alpha)))=L12 ;

v1(find(axe==-Tb/(4*alpha)))=L13 ;

for i=0:100
    R=randi([0,1],1,N); R1 =(R*2*A)-A ; z=zeros(1,(N-1)*F+1); z(1:F:(N-1)*F+1)=R1 ;
    z=conv(z,v1) ;

plot(conv(z,v1)) ;
title 'alpha= 0.9 , K = 8' ;
hold on
end

%qqqq
%%%%%k=8;
figure
alpha=0.25 ; subplot(2,2,1); 
for i=1:50 
    R=randi(1,N); R1=(2*R-ones(1,N))*A; S=[];
end
for j=1:1:length(R1)
     S=[S R1(j) zeros(1,F-1)];
end
syms t; f1=filtre(1,alpha,t); l0=eval(limit(f1,t,0)); l1=eval(limit(f1,t,Ts/(4*alpha))); l2=eval(limit(f1,t,-Ts/(4*alpha)));


axe=-K*Tb:Tb/F:K*Tb;
v1=filtre(1,alpha,axe) ;
v1(find(axe==0))=l0;

v1(find(axe==Tb/(4*alpha)))=l1 ;
v1(find(axe==-Tb/(4*alpha)))=l2 ;

r1=conv(S,v1);
z1=conv(r1,v1);

tz=-length(z1)/2:(length(z1)-1)/2;
plot(tz,z1);
hold on;
title( 'alpha=0.25 et K=8')

%%%k=4
K=4;
alpha=0.25 ; subplot(2,2,2); 
for i=1:50 
    R=randi(1,N); R1=(2*R-ones(1,N))*A; S=[];
end
for j=1:1:length(R1)
     S=[S R1(j) zeros(1,F-1)];
end
syms t; f1=filtre(1,alpha,t); l0=eval(limit(f1,t,0)); l1=eval(limit(f1,t,Ts/(4*alpha))); l2=eval(limit(f1,t,-Ts/(4*alpha)));


axe=-K*Tb:Tb/F:K*Tb;
v1=filtre(1,alpha,axe) ;
v1(find(axe==0))=l0;

v1(find(axe==Tb/(4*alpha)))=l1 ;
v1(find(axe==-Tb/(4*alpha)))=l2 ;

r1=conv(S,v1);
z1=conv(r1,v1);

tz=-length(z1)/2:(length(z1)-1)/2;
plot(tz,z1);
hold on;
title( 'alpha=0.25 et K=4')

%%%%k=2
K=2;
alpha=0.25 ; subplot(2,2,3); 
for i=1:50 
    R=randi(1,N); R1=(2*R-ones(1,N))*A; S=[];
end
for j=1:1:length(R1)
     S=[S R1(j) zeros(1,F-1)];
end
syms t; f1=filtre(1,alpha,t); l0=eval(limit(f1,t,0)); l1=eval(limit(f1,t,Ts/(4*alpha))); l2=eval(limit(f1,t,-Ts/(4*alpha)));


axe=-K*Tb:Tb/F:K*Tb;
v1=filtre(1,alpha,axe) ;
v1(find(axe==0))=l0;

v1(find(axe==Tb/(4*alpha)))=l1 ;
v1(find(axe==-Tb/(4*alpha)))=l2 ;

r1=conv(S,v1);
z1=conv(r1,v1);

tz=-length(z1)/2:(length(z1)-1)/2;
plot(tz,z1);
hold on;
title( 'alpha=0.25 et K=2')

%%%%%%%%question
alpha=0.25;
N=8;
Ts=1;
Tb=1;
K=8;
figure
R=randi(1,N); R1=(2*R-ones(1,N))*A ;S=[];

for i=1:1:length(R1)
S=[S R1(i) zeros(1,F-1)];

end
syms t; f1=filtre(1,alpha,t); l0=eval(limit(f1,t,0)); l1=eval(limit(f1,t,Ts/(4*alpha))); l2=eval(limit(f1,t,-Ts/(4*alpha))); axe=-K*Tb:Tb/F:K*Tb; v1=filtre(1,alpha,axe) ; v1(find(axe==0))=l0; v1(find(axe==Tb/(4*alpha)))=l1 ; v1(find(axe==-Tb/(4*alpha)))=l2 ; r1=conv(S,v1);

z1=conv(r1,v1); 
z=z1(length(axe):8:length(axe)+8*(N-1));
tz=0:length(z)-1;
stem(z); % Afficher les valeurs discrètes


%%%%%%question

B = randn (1, length(r1)); % Bruit blanc Gaussien
RSB = 5; %en dB

N0 = A^2*f*10^(-RSB/10);
B = sqrt (N0/2)*B;
Z1_bruit=conv(r1+B,v1);

Z_bruit=Z1_bruit(length(axe):8:length(axe)+8*(N-1));
tz=0:length(Z_bruit)-1;
figure
stem(Z_bruit); % Afficher les valeurs discrètes




