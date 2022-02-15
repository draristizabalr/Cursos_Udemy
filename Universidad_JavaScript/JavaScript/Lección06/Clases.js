class Persona{
    static contadorObjetosPersona = 0;
    constructor(nombre, apellido){
        this._nombre = nombre;
        this._apellido = apellido;
        Persona.contadorObjetosPersona++;
    }
    get nombre(){
        return this._nombre;
    }
    set nombre(nombre){
        this._nombre = nombre;
    }
    get apellido(){
        return this._apellido;
    }
    set apellido(apellido){
        this._apellido = apellido
    }
    nombreCompleto(){
        return this._nombre + ' ' + this._apellido;
    }
    toString(){
        return this.nombreCompleto();
    }
    static saludar(){
        console.log('Hola mundo, desde la función static.')
    }
    static saludar2(objeto){
        console.log('Hola ' + objeto.nombre)
    }
}

let persona = new Persona('Juan', 'Lara');
console.log(persona);
console.log(persona.nombre);
console.log(persona.nombreCompleto());
console.log(persona.toString())
Persona.saludar();
Persona.saludar2(persona);
console.log(Persona.contadorObjetosPersona);

let persona2 = new Persona('Carlos', 'Perez');
console.log(persona2);
console.log(persona2.nombre);
console.log(persona2.nombreCompleto());
console.log(persona2.toString());
Persona.saludar();
Persona.saludar2(persona2);
console.log(Persona.contadorObjetosPersona);

class Empleado extends Persona{
    constructor(nombre, apellido, departamento){
        super(nombre, apellido);
        this._departamento = departamento;
    }
    get departamento(){
        return this._departamento;
    }
    set departamento(departamento){
        this._departamento = departamento;
    }
    nombreCompleto(){
        return this._nombre + ' ' + this._apellido + ', ' + this._departamento;
    }

}

let empleado = new Empleado('Maria', 'Jimenez', 'Sistemas');
console.log(empleado);
console.log(empleado.nombreCompleto());
console.log(empleado.toString());
Empleado.saludar();
Empleado.saludar2(empleado);
console.log(Empleado.contadorObjetosPersona);
