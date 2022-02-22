import { EventEmitter, Injectable } from "@angular/core";
import { LoggingService } from "./LoggingService.service";
import { Persona } from "./persona.module";

@Injectable()
export class PersonasService{
    personas: Persona[] = [
        new Persona('Juan', 'Perez'),
        new Persona('Laura', 'Juarez'),
        new Persona('Karla', 'Lara')
      ];
    
    constructor(private loggingService: LoggingService){}

    saludar = new EventEmitter<number>();

    agregarPersona(persona:Persona){
        this.loggingService.enviaMensajeAConsola('Agregamos persona: ' + persona.nombre + ' ' + persona.apellido);
        this.personas.push( persona );
    }
}