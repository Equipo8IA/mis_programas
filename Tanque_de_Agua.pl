% Hechos

%X
tanque_poca_agua(encendido).

%Y
cisterna_poca_agua(encendido).

%Z
turbina(apagado).

%T
taque_lleno(encendido).

 % Regla_1
encender_turbina(X, Y, Z):- tanque_poca_agua(X), cisterna_poca_agua(Y), turbina(Z), Z == apagado ; tanque_poca_agua(X), cisterna_poca_agua(Y), Y == apagado.

% Regla_2
apagar_turbina(X, Y, T):- turbina(X), taque_lleno(T), X == encendido ; turbina(X), cisterna_poca_agua(Y), X == encendido.