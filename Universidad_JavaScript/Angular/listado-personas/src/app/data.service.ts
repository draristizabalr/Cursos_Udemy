
import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Persona } from './persona.module';

@Injectable()
export class DataServices{

    constructor(private httpClient:HttpClient){}

    cargarPersonas(){
        return this.httpClient.get('https://listado-personas-4319f-default-rtdb.firebaseio.com/datos.json');
    }

    // Grabar personas
    grabarPersonas(personas:Persona[]){
        this.httpClient.put('https://listado-personas-4319f-default-rtdb.firebaseio.com/datos.json', personas)
        .subscribe(
            response => {
                return console.log('Resultado de guardar las personas: ' + response);
            },
            error => {
                console.log('Error al guardar personas:' + error)
            }
        );
    }

    modificarPersona(index:number, persona:Persona){
        let url:string;
        url = 'https://listado-personas-4319f-default-rtdb.firebaseio.com/datos/' + index + '.json';
        this.httpClient.put(url, persona)
        .subscribe(
            response => console.log('Resultado de modificar el objeto persona: ' + response),
            error => console.log('Error en modificar persona: ' + error)
        )
    }

    eliminarPersona(index:number){
        let url:string;
        url = 'https://listado-personas-4319f-default-rtdb.firebaseio.com/datos/' + index + '.json';
        this.httpClient.delete(url)
        .subscribe(
            response => console.log('Resultado de eliminar el objeto persona: ' + response),
            error => console.log('Error en eliminar persona: ' + error)
        )
    }
}