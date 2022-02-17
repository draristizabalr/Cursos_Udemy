import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = "Aplicacion Calculadora";

  firstNumber:number = 0;
  secondNumber:number = 0;
  result:number = 0;

  add():void{
    this.result = this.firstNumber + this.secondNumber;
  }
}
