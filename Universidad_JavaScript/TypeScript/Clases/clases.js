"use strict";
var Persona = /** @class */ (function () {
    function Persona(nombre, apellido) {
        this.nombre = nombre;
        this.apellido = apellido;
    }
    Persona.prototype.getNombre = function () {
        return this.nombre;
    };
    return Persona;
}());
var persona1 = new Persona('Juan', 'Lara');
console.log(persona1.getNombre());
