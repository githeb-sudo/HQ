
%%%%%%%%%%%%%%%%%%%%%%%%%%Q2
F=f
disp('on a F*A^2=')
F*A^2
disp('L''energie moyenne par symoble est:')
Es = F .* sum(abs(W).^2)./length(W)
Eb = Es./3
hold off






%%%%%%%%%%%%%%%%%%%%%%%%%%%%Q3
disp('mappage utilisé pour le code de gray')
dec2base(map,2)

%%%%%%%%%%%%%%%%%%%%%Q4
t=-K*tb:tb/f:K*tb;
alpha=0.1 ;
gt=(sin(pi*t*(1-alpha))+4*alpha*t.*cos(pi*t*(1+alpha)))./(pi*t.*(1-((4*alpha*t).^2)));
syms x ;
g= (sin(pi*x*(1-alpha))+4*alpha*x*cos(pi*x*(1+alpha)))./(pi*x*(1-((4*alpha*x).^2)));
l1 =limit(g,0);
l2 =limit(g,tb/(4*alpha));
l3 =limit(g,-tb/(4*alpha));
gt(find(t==tb/(4*alpha)))=l2;
gt(find(t==0))=l1;
gt(find(t==-tb/(4*alpha)))=l3;
e=conv (Se,gt) ;

Es=8 ;
Eb=Es/3;
RSB=0:1:10 ;
for h=1:length(RSB)
    Eb=5/2*A*A*f;
    N0=Eb/(10^(RSB(h)/10));
    b1=sqrt(N0/2)*randn(1,length(e));
    b2=sqrt(N0/2)*randn(1,length(e));
    
    b=b1+j*b2;
    r=e+b;
    z=conv(r,gt);
end
figure('name','signal z(t) à la sortie du filtre adapté');
plot(z)
%%%%%%%%%Q5
t0=length(gt);
    x=[] ;
    xk=[] ;
    ze=[] ;
    for q=1:N/3
        ze(q)=z(t0+(q-1)*f);
        phase =angle(ze(q)) ;
        
        if (phase >=0 && phase <pi/4)              x=[x 0 0 0] ;xk=[xk d(1)] ;
        elseif (phase >= pi/4 && phase <pi/2)      x=[x 0 0 1] ;xk=[xk d(2)] ;
        elseif (phase >= pi/2 && phase <3*pi/4)    x=[x 0 1 1] ;xk=[xk d(3)] ;
        elseif (phase >= 3*pi/4 && phase <=pi)     x=[x 0 1 0] ;xk=[xk d(4)] ;
        elseif (phase >= -pi && phase < -3*pi/4)   x=[x 1 1 0] ;xk=[xk d(5)] ;
        elseif (phase >= -3*pi/4 && phase < -pi/2) x=[x 1 1 1] ;xk=[xk d(6)] ;
        elseif (phase >= -pi/2 && phase < -pi/4)   x=[x 1 0 1] ;xk=[xk d(7)] ;
        elseif (phase >= -pi/4 && phase < 0)       x=[x 1 0 0] ;xk=[xk d(8)] ;
            
        end
    end
    
    figure('NumberTitle','off','Name',strcat('RSB= ', num2str(RSB(h))));
    axes1 = axes;
    hold(axes1,'on');
    xlabel('Re','FontSize',11);
    title({'detection'},'FontSize',11);
    ylabel('Im','FontSize',11);
    box(axes1,'on');
    set(axes1,'XAxisLocation','origin','YAxisLocation','origin');
    legend(axes1,'show');
    hold on
    
    plot(XCercle, YCercle,'DisplayName','cercle unitaire');
    fplot(@(x) x)
    fplot(@(x) -x)
    
    plot (real(ze) , imag(ze),'b.') ;
    echelle = max(abs(ze))/2;
    plot (real(W).*echelle , imag(W).*echelle,'DisplayName','constellation','Marker','*','LineStyle','none', 'Color',[1 0 0]);
    hold off
    
%%%%%%%%%%%%%%%%%%Q6
erreur_binaire=0 ;
erreur_symbole=0 ;
    for o=1:N
        if (x(o)~=Seq_Gray(o))
            erreur_binaire=erreur_binaire+1;
        end
    end
    for o=1:N/3
        if (x(o)+10*x(o+1)+100*x(o+2)~=Seq_Gray(o)+10*Seq_Gray(o+1)+100*Seq_Gray(o+2))
            erreur_symbole=erreur_symbole+1;
        end
    end
    TEB(h) = erreur_binaire/N ;
    TES(h) = erreur_symbole/(N/3) ;
    TE(h)= erfc(sin(pi/8)*sqrt(Es/N0)) ;
    figure('name','TEB');
    plot(TEB);
    figure('name','TEs');
    plot(TES);
    figure('name','TE');
    plot(TE);
    hold off
    
   %%%%%%%%%%%%%%%%%%Q7
figure
semilogy(RSB,TE,'b');
hold on
semilogy(RSB,TEB,'b*');
hold on
semilogy(RSB,TES,'ro');
grid ;
title 'Variation de TEB et TES en fonction de RSB'
xlabel '(Eb/N0)dB'
ylabel ' Taux d"erreur binaire et symbole'
legend('TES théorique','TEB','TES');
    
    
