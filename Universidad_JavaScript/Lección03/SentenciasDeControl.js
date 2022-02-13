let numero = 5.5;
let numeroTexto = 'Valor desconocido';

switch (numero){
    case 1:
        numeroTexto = 'Numero uno';
        break;
    case 2:
        numeroTexto = 'Número dos';
        break;
    case 3:
        numeroTexto = 'Número tres';
        break;
    case 4:
        numeroTexto = 'Número cuarto';
        break;
    case 5:
        numeroTexto = 'Número cinco';
        break;
    case 5.5:
        numeroTexto = 'Número cinco y medio'
        break;
    default:
        numeroTexto = 'Caso no encontrado';
        break;
}
console.log(numeroTexto)