import { Component } from "@angular/core";

@Component({
    selector: 'app-personas',
    templateUrl: './personas.component.html',
    styleUrls: ['./personas.component.css']
    // styles: [`
    //     h1{
    //         color: blue;
    //     }
    // `]
})
export class PersonasComponent{
  
    deshabilitado = false;
    mensaje = '';
    titulo = 'Ingeniero';
    mostrar = false;

    agregarPersona(){
        this.mostrar = true
        this.mensaje = "Persona Agregada"
    }
    
    // modificarTitulo(event:Event){
    //     this.titulo = (<HTMLInputElement>event.target).value;
    // }

}