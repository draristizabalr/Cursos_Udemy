class Persona{
    private nombre:string;
    private apellido:string;

    constructor(nombre:string, apellido:string){
        this.nombre = nombre;
        this.apellido = apellido
    }
    getNombre():string{
        return this.nombre;
    }
}

let persona1 = new Persona('Juan', 'Lara');
console.log(persona1.getNombre())