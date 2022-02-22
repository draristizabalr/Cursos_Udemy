import { Component, EventEmitter, Output } from '@angular/core';

@Component({
  selector: 'app-formulario',
  templateUrl: './formulario.component.html',
  styleUrls: ['./formulario.component.css']
})
export class FormularioComponent {
  
  firstNumber:number = 0;
  secondNumber:number = 0;

  @Output() resultadoSuma = new EventEmitter<number>();
  
  sumar():void{
    let resultado = this.firstNumber + this.secondNumber;
    this.resultadoSuma.emit(resultado)
  }
}
