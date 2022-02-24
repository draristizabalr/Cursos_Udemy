import { Component } from '@angular/core';
import { Egreso } from './egreso/egreso.model';
import { EgresoServicio } from './egreso/egreso.servicio';
import { Ingreso } from './ingreso/ingreso.model';
import { IngresoServicio } from './ingreso/ingreso.servicio';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  
  ingreso:Ingreso[] = [];
  egreso:Egreso[] = [];

  constructor(private ingresoServicio:IngresoServicio,
              private egresoServicio: EgresoServicio){
    this.ingreso = ingresoServicio.ingreso;
    this.egreso = egresoServicio.egreso;
  }
  
  getIngresoTotal(){
    let ingresoTotal:number = 0;
    this.ingreso.forEach(ingreso => {
      ingresoTotal += ingreso.valor;
    });
    return ingresoTotal;
  }

  getEgresoTotal(){
    let egresoTotal:number = 0;
    this.egreso.forEach(egreso => {
      egresoTotal += egreso.valor;
    });
    return egresoTotal;
  }

  getPorcentajeTotal(){
    return this.getEgresoTotal() / this.getIngresoTotal();
  }

  getPresupuestoTotal(){
    return this.getIngresoTotal() - this.getEgresoTotal();
  }
}

