#include <iostream>
#include <cctype> // Para usar la funci�n toupper
#include <stdlib.h> // Para usar system pause
#include <limits> //Para limpiar el buffer

using namespace std;

class TurbinaControl {
private:
    bool tanquePocaAgua=0;
    bool cisternaPocaAgua=0;
    bool turbinaEncendida=0;
    bool tanqueLleno=0;

public:
    // Constructor de la clase TurbinaControl
    TurbinaControl();

    void setTanquePocaAgua(bool);
    void setCisternaPocaAgua(bool);
    void setTurbinaEncendida(bool);
    void setTanqueLleno(bool);
    void Estado();
    char getTanqueLleno();
};

// Implementaci�n del constructor de la clase TurbinaControl
TurbinaControl::TurbinaControl(){}



void TurbinaControl::setTanquePocaAgua(bool value) {
    tanquePocaAgua = value;
}

void TurbinaControl::setCisternaPocaAgua(bool value) {
    cisternaPocaAgua = value;
}

void TurbinaControl::setTurbinaEncendida(bool value) {
    turbinaEncendida = value;
}

void TurbinaControl::setTanqueLleno(bool value) {
    tanqueLleno = value;
}

// Implementaci�n del m�todo para controlar la turbina seg�n los datos ingresados
void TurbinaControl::Estado() {
    // Determinar si la turbina debe apagarse o encenderse seg�n las condiciones
    if (cisternaPocaAgua && turbinaEncendida) {
        cout << "\nLa turbina debe apagarse." << endl;
        turbinaEncendida=0;
    } else if (turbinaEncendida && !cisternaPocaAgua) {
        turbinaEncendida=0;
        cout << "\nLa turbina debe apagarse." << endl;
    } else if (tanquePocaAgua &&!cisternaPocaAgua && !turbinaEncendida) {
        cout << "\nLa turbina debe encenderse." << endl;
         turbinaEncendida=1;
    } else {
        cout << "\nNo se requiere ninguna accion." << endl;
    }
}

char TurbinaControl::getTanqueLleno(){
return tanqueLleno;
}
