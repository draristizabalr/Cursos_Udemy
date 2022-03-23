import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router, RouterLinkActive } from '@angular/router';
import { Persona } from '../../persona.module';
import { PersonasService } from '../../personas.service';

@Component({
  selector: 'app-formulario',
  templateUrl: './formulario.component.html',
  styleUrls: ['./formulario.component.css'],
  // providers: [LoggingService] con esta linea declaramos el proveedor en este componente, pero en "app.module" lo podemos declarar para todos los componentes
})
export class FormularioComponent implements OnInit{
  
  nombreInput: string;
  apellidoInput: string;
  index: number; 

  constructor(
    private personasService: PersonasService,
    private router: Router,
    private route: ActivatedRoute
    ){
    this.personasService.saludar.subscribe(
      (indice: number) => alert('El indice es: ' + (indice + 1))
    );
  }
  
  ngOnInit(){
    this.index = this.route.snapshot.params['id'];
    if (this.index){
      let persona:Persona = this.personasService.encontrarPersona(this.index);
      this.nombreInput = persona.nombre;
      this.apellidoInput = persona.apellido;
    }
  }
  
  guardarPersona(){
    let persona1 = new Persona(this.nombreInput, this.apellidoInput)
    
    if(this.index){
      this.personasService.modificarPersona(this.index, persona1);
    }else{
      this.personasService.agregarPersona( persona1 );
    }
    this.router.navigate(['personas'])
  }

  eliminarPersona(){
    if(this.index){
      this.personasService.eliminarPersona(this.index);
    }
    this.router.navigate(['personas']);
  }
}