% Hechos:
tanque_poca_agua(apagado).
cisterna_poca_agua(apagado).
turbina(encendido).
tanque_lleno(apagado).

% Regla:
encender_turbina( X, Y, T, Z):-tanque_poca_agua(X), cisterna_poca_agua(Y), turbina(T), tanque_lleno(Z); V=encendido, X = V, cisterna_poca_agua(Y), turbina(T), tanque_lleno(Z); tanque_poca_agua(X), cisterna_poca_agua(Y), V=apagado, T = V, tanque_lleno(Z); V=encendido, X = V, cisterna_poca_agua(Y), A=apagado, T = A, tanque_lleno(Z).


%Readme:
% X para tanque_poca_agua
% Y para cisterna_poca_agua
% T para turbina
% Z para tanque_lleno

% Las letras V y A solo son usadas como varibles para comparar con el resultado deseado

% Ojo la interpretacionde los hechos es de manera que su nombre se refiere a la condicion del sensor 
% ejemplo: Si hay "poca agua en el tanque" el sencosr se = enciende 
% en el caso de turbina esta fefinida como encendida, pero en si el programa Python es el que activa la verdadera Turbina 
% no olvidar que esto es más una Desmotración(simulación)