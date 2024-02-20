#include <iostream>
#include <TurbinaControl.h>

class DatosUsuario {
public:
    static bool solicitarRespuesta(const std::string& pregunta) {
        char input;
        do {
            std::cout << pregunta << " (S/N): ";
            std::cin >> input;
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            input = std::toupper(input);
        } while (input != 'S' && input != 'N');
        return (input == 'S');
    }
};

int main() {
    cout << "\tPROGRAMA DE CONTROL DE UNA TURBINA" << endl;

TurbinaControl TanqueAgua;


 TanqueAgua.setTanqueLleno(DatosUsuario::solicitarRespuesta("Esta el tanque lleno? (S/N): "));

if(!TanqueAgua.getTanqueLleno())
{

 TanqueAgua.setCisternaPocaAgua(DatosUsuario::solicitarRespuesta("El tanque tiene poca agua? (S/N): "));


 TanqueAgua.setCisternaPocaAgua(DatosUsuario::solicitarRespuesta("La cisterna tiene agua? (S/N): "));


 TanqueAgua.setTurbinaEncendida(DatosUsuario::solicitarRespuesta("Esta la turbina encendida? (S/N): "));
}

TanqueAgua.Estado();

 return 0;
}


