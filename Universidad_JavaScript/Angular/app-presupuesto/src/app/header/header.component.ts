import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent implements OnInit {
  titulo:string = 'Presupuesto Disponible:'
  presupuestoTotal: number = 0;
  ingresosTotales: number = 0;
  egresosTotales: number = 0;
  porcentajeEgresos: number = 0;

  constructor() { }

  ngOnInit(): void {
  }

}
