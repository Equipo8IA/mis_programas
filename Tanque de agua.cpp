#include "iostream"
#include "stdlib.h"
//Equipo #8

using namespace std;

class Controlador {                     // Clase  POO
public: 
//atributos
bool Tanque_Lleno=0;
bool Bomba_Encendida=0;
bool Cisterna_con_poca_agua=0;
bool Tanque_con_poca_agua=0;
//Constructor
Controlador();
//Metodos
void Menu();
void Estado();
};

Controlador::Controlador(){ }

void Controlador::Menu(){
short boton=0;

do{ system("cls");
cout <<"\n        Tu Cisterna del agua:       ";
cout <<"\n1-Tiene poca agua  ";
cout <<"\n2-Tiene mucha agua ";
cout <<"\n                        "<<endl;
cin>>boton;

switch(boton){

case 1:{ Tanque_con_poca_agua=0; break;}

case 2:{ Tanque_con_poca_agua=1; break;}

default:{  system("cls"); cout<<"Valor incorrecto digite 1 o 2!"<<endl; break;}

}//suich
}while( (boton!=1)&&(boton!=2) );

do{ system("cls");
cout <<"\n        Bomba del agua:       ";
cout <<"\n1-Esta Apagada ";
cout <<"\n2-Esta Encendida ";
cout <<"\n                        "<<endl;
cin>>boton;

switch(boton){

case 1:{ Bomba_Encendida=0; break;}

case 2:{ Bomba_Encendida=1; break;}

default:{  system("cls"); cout<<"Valor incorrecto digite 1 o 2!"<<endl; break;}

}//suich
}while( (boton!=1)&&(boton!=2) );

do{ system("cls");
cout <<"\n        Tanque de agua:       ";
cout <<"\n1-Tiene poca agua  ";
cout <<"\n2-Tiene mucha agua ";
cout <<"\n                        "<<endl;
cin>>boton;

switch(boton){

case 1:{ Tanque_con_poca_agua=0; break;}

case 2:{ Tanque_con_poca_agua=1; break;}

default:{  system("cls"); cout<<"Valor incorrecto digite 1 o 2!"<<endl; break;}

}//suich
}while( (boton!=1)&&(boton!=2) );


if((Bomba_Encendida==0)&&(Cisterna_con_poca_agua==1)&&(Tanque_con_poca_agua==1)) { Tanque_Lleno=1; }//esta lleno
else{ Tanque_Lleno=0;}// esta vacio o llenandose 

system("cls");
}

void Controlador::Estado(){
if(Tanque_Lleno==1){ cout <<"\nEl tanque de agua esta lleno. "<<endl; }//esta lleno

else if((Bomba_Encendida==1)&&(Cisterna_con_poca_agua==1)&&(Tanque_con_poca_agua==0)) { cout <<"\nLa sisterna tiene agua, la turbina esta encendida y el tanque esta llenandose el tanque.   "<<endl; }//esta lleno

else if((Cisterna_con_poca_agua==0)&&(Tanque_con_poca_agua==1)) { cout <<"\nEl tanque no esta lleno, pero tiene sufisiente agua, la turbina esta esperando que se llene la sisterna.   "<<endl; }//esta lleno

else if((Cisterna_con_poca_agua==0)&&(Tanque_con_poca_agua==0)) { cout <<"\nHay poca agua en el tanque, pero no se puede encender la turbina xq no hay agua en la sisterna.   "<<endl; }//esta lleno

else{ cout <<"\n  Error de sistema   "<<endl;}// esta vacio o llenandose 	
	
}

// programa 
int main(){
system("color F1"); system("cls"); Controlador agua;//declaraacion de objeto
agua.Menu();  agua.Estado(); system("pause"); //interaccion con metodos del objeto
return 0;
}