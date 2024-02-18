#include <iostream>
#include <cctype> // Para usar la funci�n toupper
#include <stdlib.h> // Para usar system("color F1")

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

    // M�todo para pedir datos al usuario
    void pedirDatos();

    // M�todo para controlar la turbina seg�n los datos ingresados
    void controlTurbina();
};

// Implementaci�n del constructor de la clase TurbinaControl
TurbinaControl::TurbinaControl(){}

// Implementaci�n del m�todo para solicitar datos al usuario
void TurbinaControl::pedirDatos() {
    char input;

    // Solicitar si el tanque est� lleno
    do {
        cout << "Esta el tanque lleno? (S/N): ";
        cin >> input;
        input = toupper(input);
        system("cls");
    } while (input != 'S' && input != 'N');
    tanqueLleno = (input == 'S');

if(input=='N'){
    // Solicitar si el tanque tiene poca agua
    do {
        cout << "\nEl tanque tiene poca agua? (S/N): ";
        cin >> input;
        input = toupper(input);
        system("cls");
    } while (input != 'S' && input != 'N');
    tanquePocaAgua = (input == 'S');

    // Solicitar si la cisterna tiene poca agua
    do {
        cout << "La cisterna tiene agua? (S/N): ";
        cin >> input;
        input = toupper(input);
        system("cls");
    } while (input != 'S' && input != 'N');
    cisternaPocaAgua = (input == 'S');

    // Solicitar si la turbina est� encendida
    do {
        cout << "Esta la turbina encendida? (S/N): ";
        cin >> input;
        input = toupper(input);
        system("cls");
    } while (input != 'S' && input != 'N');
    turbinaEncendida = (input == 'S');
}
}

// Implementaci�n del m�todo para controlar la turbina seg�n los datos ingresados
void TurbinaControl::controlTurbina() {
    // Determinar si la turbina debe apagarse o encenderse seg�n las condiciones
    if (cisternaPocaAgua && turbinaEncendida) {
        cout << "\nLa turbina debe apagarse." << endl;
    } else if (turbinaEncendida && tanqueLleno) {
        cout << "\nLa turbina debe apagarse." << endl;
    } else if (tanquePocaAgua && !cisternaPocaAgua && !turbinaEncendida) {
        cout << "\nLa turbina debe encenderse." << endl;
    } else {
        cout << "\nNo se requiere ninguna accion." << endl;
    }
system("pause");
}

int main() {
    system("color 1F"); // Cambiar el color de la consola a blanco sobre fondo azul claro
    cout << "\tPROGRAMA DE CONTROL DE UNA TURBINA" << endl;
    TurbinaControl control; //declaracion del objeto
    control.pedirDatos();
    control.controlTurbina();

    return 0;
}

