import { Component, Input, OnInit } from '@angular/core';
import { Persona } from '../../persona.module';
import { PersonasService } from '../../personas.service';

@Component({
  selector: 'app-persona',
  templateUrl: './persona.component.html',
  styleUrls: ['./persona.component.css']
})
export class PersonaComponent implements OnInit {
  
  @Input() persona: Persona;
  @Input() indice: number;

  constructor(private personasService: PersonasService) {}

  ngOnInit(): void {
  }
  emitirSaludo(){
    return this.personasService.saludar.emit(this.indice);
  }

}
