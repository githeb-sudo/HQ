
clear
clc
close('all');

%% 1.
disp('le code de gray utilisé est le suivant')
[ 0 0 -3; 0 1 -1; 1 1 1; 1 0 3]
N=8;
Tb=1;
Ts=1;
I=randi([0,1],[1 N]);

Gray=[];
for i=1:2:N-1
    if (I(i)==0) && (I(i+1)==0)
        Gray=[Gray -3]; 
    elseif (I(i)==0 )&& (I(i+1)==1)
        Gray=[Gray -1]; 
    elseif (I(i)==1) && (I(i+1)==1)
       Gray=[Gray 1];  
    elseif (I(i)==1) && (I(i+1)==0)
        Gray=[Gray 3]; 
    end
end
I;
Gray;

%% 2.
%
alpha=0.9
F=8;
l=(N/2-1)*(F-1)-N/2;
ae=zeros(1,l);
ae(1)=Gray(1);
for i=1:N/2-1
    ae(F*i+1)=Gray(i+1);
end
ae;

%%%%filtrage
K=8;
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


%%%
e=conv(ae,g);
Eb=2.5*F;
RSB=5;
n0=Eb/10^(RSB/10);
B=sqrt(n0/2)*randn(1,length(e));
%%%decimation
d=[];
r=B+e;
z=conv(r,g);
t0=length(g);
for i=0:N/2-1
    d=[d z(t0+F*i)];
end

d
figure('name','signal emis');
plot(d);
%%%pise de décision
decis=zeros(1,length(d));
for i=1:N/2
    if (d(i)>2*F)
        decis(i)=3;
    elseif d(i)>0 && d(i)<2*F
        decis(i)=1;
    elseif d(i)<(-2*F)
        decis(i)=-3;
    else decis(i)=-1;
    end
end

decis
Gray
figure('name','signal recu');
plot(decis);
%%%reconstitution du signal
reconstituee=zeros(1,N);
k=1;
for i=1:N/2
    if decis(i)==3
        reconstituee(k)=1;
        reconstituee(k+1)=0;
    elseif decis(i)==-3
        reconstituee(k)=0;
        reconstituee(k+1)=0;
    elseif decis(i)==-1
        reconstituee(k)=0;
        reconstituee(k+1)=1;
    elseif decis(i)==1
        reconstituee(k)=1;
        reconstituee(k+1)=1;
    end
    k=k+2;
end
figure('name','signal reconstituee');
plot(reconstituee);
disp('échantillon original:')
I
reconstituee

return

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
RSB=0:0.1:5;
RSB1=10.^(RSB/10);
PEB=(3/8)*erfc(sqrt((6/15)*RSB1));
figure('name','a');
semilogy(RSB,PEB);
hold on


TEB=[];
 RSB=0:0.1:5
 for p=1:length(RSB)
    e=conv(ae,g);
Eb=2.5*F;
n0=Eb/10^(RSB(p)/10);
B=sqrt(n0/2)*randn(1,length(e));
%%%decimation
d=[];
r=B+e;
z=conv(r,g);
t0=length(g);
for i=0:N/2-1
    d=[d z(t0+F*i)];
end


%%%pise de décision
decis=zeros(1,length(d));
for i=1:N/2
    if (d(i)>2*F)
        decis(i)=3;
    elseif d(i)>0 && d(i)<2*F
        decis(i)=1;
    elseif d(i)<(-2*F)
        decis(i)=-3;
    else decis(i)=-1;
    end
end

%%%reconstitution du signal
recons=zeros(1,N);
k=1;
for i=1:N/2
    if decis(i)==3
        recons(k)=1;
        recons(k+1)=0;
    elseif decis(i)==-3
        recons(k)=0;
        recons(k+1)=0;
    elseif decis(i)==-1
        recons(k)=0;
        recons(k+1)=1;
    elseif decis(i)==1
        recons(k)=1;
        recons(k+1)=1;
    end
    k=k+2;
end

diff=abs(I-recons);
nbe=sum(diff);
TEB(p)=nbe/N;

end
hold on
semilogy(RSB,TEB,'*');
title(strcat('BER de la modulation MDA-4 (alpha = ',num2str(alpha),')'))