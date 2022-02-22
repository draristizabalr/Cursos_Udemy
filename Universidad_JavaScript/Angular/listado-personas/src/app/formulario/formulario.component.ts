import { Component, ElementRef, ViewChild } from '@angular/core';
import { Persona } from '../persona.module';
import { PersonasService } from '../personas.service';

@Component({
  selector: 'app-formulario',
  templateUrl: './formulario.component.html',
  styleUrls: ['./formulario.component.css'],
  // providers: [LoggingService] con esta linea declaramos el proveedor en este componente, pero en "app.module" lo podemos declarar para todos los componentes
})
export class FormularioComponent {
  
  

  @ViewChild('nombreInput') nombreInput: ElementRef;
  @ViewChild('apellidoInput') apellidoInput: ElementRef;

  constructor(private personasService: PersonasService){
    this.personasService.saludar.subscribe(
      (indice: number) => alert('El indice es: ' + (indice + 1))
    );
  }
  
  
  agregarPersona(){
    let persona1 = new Persona(
      this.nombreInput.nativeElement.value,
      this.apellidoInput.nativeElement.value);
      // this.loggingService.enviaMensajeAConsola("Enviamos persona: " + persona1.nombre + " " + persona1.apellido)
      // this.personaCreada.emit(persona1)
      this.personasService.agregarPersona( persona1 );
  }
}