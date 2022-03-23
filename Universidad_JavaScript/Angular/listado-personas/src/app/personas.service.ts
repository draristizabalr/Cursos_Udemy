import { EventEmitter, Injectable } from "@angular/core";
import { DataServices } from "./data.service";
import { LoggingService } from "./LoggingService.service";
import { Persona } from "./persona.module";

@Injectable()
export class PersonasService{
    personas: Persona[] = [];
    
    constructor(
        private loggingService: LoggingService,
        private dataServices: DataServices
        ){}

    saludar = new EventEmitter<number>();
    
    setPersonas(personas: Persona[]){
        this.personas = personas;
    }

    obtenerPersonas(){
        return this.dataServices.cargarPersonas();
    }

    agregarPersona(persona:Persona){
        this.loggingService.enviaMensajeAConsola('Agregamos persona: ' + persona.nombre + ' ' + persona.apellido);
        if(this.personas == null){
            this.personas = [];
        }
        this.personas.push( persona );
        this.dataServices.grabarPersonas(this.personas);
        
        
    }

    encontrarPersona(index: number){
        let persona: Persona = this.personas[index];
        return persona
    }

    modificarPersona(index:number, persona:Persona){
        let persona1 = this.personas[index];
        persona1.nombre = persona.nombre;
        persona1.apellido= persona.apellido;
        this.dataServices.modificarPersona(index, persona);
    }

    eliminarPersona(index:number){
        this.personas.splice(index, 1);
        this.dataServices.eliminarPersona(index);
        // Se vuelve a guardar el arreglo entero para regerar los indices
        this.modificarPersonas();

    }

    modificarPersonas(){
        if(this.personas != null){
            this.dataServices.grabarPersonas(this.personas);
        }
    }
}