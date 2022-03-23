import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';

@Component({
  selector: 'app-loggin',
  templateUrl: './loggin.component.html',
  styleUrls: ['./loggin.component.css']
})
export class LogginComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
  }
  
  loggin(form: NgForm){
    const email = form.value.email;
    const password = form.value.password;
    
  }
}
