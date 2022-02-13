class Persona{
    static contadorPersonas = 0;
    constructor(nombre, apellido, edad){
        this._nombre = nombre;
        this._apellido = apellido;
        this._edad = edad;
        Persona.contadorPersonas++;
    }
    get nombre(){
        return this._nombre;
    }
    get apellido(){
        return this._apellido;
    }
    get edad(){
        return this._edad;
    }
    set nombre(nombre){
        this._nombre = nombre;
    }
    set apellido(apellido){
        this._apellido = apellido;
    }
    set edad(edad){
        this._edad = edad;
    }
    detalles(){
        return Persona.contadorPersonas + '| Nombre: ' + this.nombre + ' ' + this.apellido + ' |Edad: ' + this.edad;
    }
    toString(){
        return this.detalles();
    }
}
let persona = new Persona('David', 'Aristizabal', 29);
console.log(persona.toString());

class Empleado extends Persona{
    static contadorEmpleados = 0;

    constructor(nombre, apellido, edad, sueldo){
        super(nombre, apellido, edad);
        this._sueldo = sueldo;
        Empleado.contadorEmpleados++;
    }
    get sueldo(){
        return this._sueldo;
    }
    set sueldo(sueldo){
        this._sueldo = sueldo;
    }
    detalles(){
        return 'EMP' + Empleado.contadorEmpleados + '| Nombre: ' + this.nombre + ' ' + this.apellido + ' |Edad: ' + this.edad + ' |Sueldo: $' + this.sueldo;
    }
}
let empleado = new Empleado('Pedro', 'Aristizabal', '34', '9000000');
console.log(empleado.toString());

class Cliente extends Persona{
    static contadorClientes = 0;
    constructor(nombre, apellido, edad, fecha){
        super(nombre, apellido, edad);
        this._fecha = fecha;
        Cliente.contadorClientes++;
    }
    get fecha(){
        return this._fecha;
    }
    set fecha(fecha){
        this._fecha = fecha;
    }
    detalles(){
        return 'CLI' + Cliente.contadorClientes + '| Nombre: ' + this.nombre + ' ' + this.apellido + ' |Edad: ' + this.edad + ' |Fecha: ' + this.fecha;
    }
}
let cliente = new Cliente('Daniel', 'Acosta', 21, '6 de Febrero del 2022');
console.log(cliente.toString())
