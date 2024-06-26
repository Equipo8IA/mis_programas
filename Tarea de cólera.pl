
% Hechos



% Reglas
colera(X) :- diarrea(X), vomitos(X), deshidratacion(X).
deshidratacion(X) :- preguntar(X, 'Tiene signos de deshidratacion? [s/n]', R), R = s.
diarrea(X) :- preguntar(X, 'Tiene diarrea? [s/n]', R), R = s.
vomitos(X) :- preguntar(X, 'Tiene vomitos? [s/n]', R), R = s.

preguntar(_, Texto, Res) :-
    nl, write(Texto),
    read(Respuesta),
    (Respuesta = 's'; Respuesta = 'n'),
    Res = Respuesta, !.

preguntar(_, Texto, Res) :-
    nl, write('Respuesta invalida. Por favor, responda con "s" o "n".'),
    preguntar(_, Texto, Res).

% Reglas
diagnosticar(X) :-
    nl, write('Se investiga COLERA'), colera(X),
    nl, write(X), write(' tiene sintomas de COLERA.'), !.

diagnosticar(_) :-
    write('No se puede lograr un diagnostico.').