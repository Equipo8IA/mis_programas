 
% Hechos
tanque_poca_agua(encendido).
cisterna_poca_agua(encendido).
turbina(apagado).
taque_lleno(encendido).

% Regla_1
encender_turbina(X, Y, Z):- tanque_poca_agua(X), cisterna_poca_agua(Y), turbina(Z), Z == apagado.
encender_turbina(X, Y, Z):- tanque_poca_agua(X), cisterna_poca_agua(Y), Z == apagado.

% Regla_2
apagar_turbina(X, Y, T):- turbina(X), taque_lleno(T), X == encendido.
apagar_turbina(X, Y, T):- turbina(X), cisterna_poca_agua(Y), X == encendido.