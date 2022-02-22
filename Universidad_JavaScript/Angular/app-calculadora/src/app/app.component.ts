import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  titulo = 'Aplicacion Calculadora 2';

  // firstNumber:number = 0;
  // secondNumber:number = 0;
  resultado:number = 0;

  // sumar():void{
  //   this.resultado = this.firstNumber + this.secondNumber;
  // }

  mostrarResultado(resultadoEvento:number){
    this.resultado = resultadoEvento
  }

}
