clear all;
close all;
clc;
A=1.8;
t1=4*pi;
t2=8*pi;
alfa=1;
t=[0:(24*pi)/1280:24*pi];
xinterrupcion=A*(1-alfa*(((t-t1)>0)-((t-t2)>0))).*sin(t);
%plot(xinterrupcion)
%hold on;
csvwrite('interrupcion.csv', xinterrupcion);

alfa=0.2;
xsag=A*(1-alfa*(((t-t1)>0)-((t-t2)>0))).*sin(t);
%plot(xsag)
csvwrite('sag.csv', xsag);

alfa=0.8;
xswell=A*(1+alfa*(((t-t1)>0)-((t-t2)>0))).*sin(t);
%plot(xswell)
csvwrite('swell.csv', xswell);

alfa2=0.1;
xharmonics=A*((sin(t))+(alfa2*sin(20*t)));
%plot(xharmonics)
%hold on;
csvwrite('armonicos.csv', xharmonics);

alfa=0.1;
beta=20;
xflicker=A*(1+alfa*sin(beta*t)).*sin(t);
%plot(xflicker)
csvwrite('flicker.csv', xflicker);

t1=4*pi;
t2=5*pi;
alfa=0.8;
betha=5;
%xtransients=A*(sin(t)+alfa*(exp(-(t-t1)./0.004)).*(((t-t1)>0)-((t-t2)>0)).*(sin(300*t)));
xtransients=A*(sin(t)+alfa*sin(betha*t).*(exp(-(t-t1)/0.004)).*(((t-t1)>0)-((t-t2)>0)));
plot(xtransients)
csvwrite('transients.csv', xtransients);



