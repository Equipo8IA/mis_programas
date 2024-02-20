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
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

if(input=='N'){
    // Solicitar si el tanque tiene poca agua
    do {
        cout << "\nEl tanque tiene poca agua? (S/N): ";
        cin >> input;
        input = toupper(input);

    } while (input != 'S' && input != 'N');
    tanquePocaAgua = (input == 'S');
   cin.ignore(numeric_limits<streamsize>::max(), '\n');

    // Solicitar si la cisterna tiene poca agua
    do {
        cout << "La cisterna tiene agua? (S/N): ";
        cin >> input;
        input = toupper(input);

    } while (input != 'S' && input != 'N');
    cisternaPocaAgua = (input == 'S');
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    // Solicitar si la turbina est� encendida
    do {
        cout << "Esta la turbina encendida? (S/N): ";
        cin >> input;
        input = toupper(input);

    } while (input != 'S' && input != 'N');
    turbinaEncendida = (input == 'S');
}
}

// Implementaci�n del m�todo para controlar la turbina seg�n los datos ingresados
void TurbinaControl::controlTurbina() {
    // Determinar si la turbina debe apagarse o encenderse seg�n las condiciones
    if (cisternaPocaAgua && turbinaEncendida) {
        cout << "\nLa turbina debe apagarse." << endl;
        turbinaEncendida=0;
    } else if (turbinaEncendida && tanqueLleno) {
        turbinaEncendida=0;
        cout << "\nLa turbina debe apagarse." << endl;
    } else if (tanquePocaAgua && !cisternaPocaAgua && !turbinaEncendida) {
        cout << "\nLa turbina debe encenderse." << endl;
         turbinaEncendida=1;
    } else {
        cout << "\nNo se requiere ninguna accion." << endl;
    }
system("pause");
}

int main() {
    cout << "\tPROGRAMA DE CONTROL DE UNA TURBINA" << endl;
    TurbinaControl control; //declaracion del objeto
    control.pedirDatos();
    control.controlTurbina();

    return 0;
}

