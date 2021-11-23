clc;
clear all;
close all;
m=2;
g1=6;
g2=7;

N=10^6;
R=randi([0,1],1,N);

t=poly2trellis(m+1,[g1 g2]);
code=convenc(R,t);

TEB=[];
vRSB=0:0.2:2;
RSB=0.1;
peb=0.5*erfc(sqrt(10^(RSB/10)));
r=bsc(code,peb);
d=vitdec(r,t,5,'trunc','hard');
teb=sum(abs(d-R));
teb
r1=bsc(R,peb);

teb1=sum(abs(r1-R));
teb1


