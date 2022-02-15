let persona1 = {
    nombre: 'David',
    apellido: 'Aristizábal',
    edad: 29,
    idioma: 'es',

    get lang(){
        return this.idioma.toUpperCase()
    },
    set lang(lang){
        return this.idioma = lang.toUpperCase();
    },
    nombreCompleto: function(titulo, telefono){
        return titulo + ', ' + telefono + ', ' + this.nombre + ', ' + this.apellido;
    }
}
console.log(persona1.idioma);
persona1.lang = 'fr';
console.log(persona1.idioma);

let persona2 = {
    nombre: 'Carlos',
    apellido: 'Lara',
    edad: 23,
    idioma: 'fr',

    get lang(){
        return this.idioma.toUpperCase()
    },
    set lang(lang){
        return this.idioma = lang.toUpperCase();
    },
}
console.log(persona1.nombreCompleto('Licenciado', 12348765324));


console.log(persona1.nombreCompleto.call(persona2, 'Ingeniero', 89723648203))
let arreglo = ['Ingeniero', 897236247826]
console.log(persona1.nombreCompleto.apply(persona2, arreglo));

