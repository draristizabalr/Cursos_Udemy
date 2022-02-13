function calcular_tiempo(){
    let tiempo = {horas: 0, minutos: 0};
    let sumaTiempo = 0;
    
    for (i = 0; i < arguments.length; i++){
        sumaTiempo += arguments[i];
        if (sumaTiempo > 60){
            tiempo.horas += (sumaTiempo - (sumaTiempo % 60)) / 60;
            sumaTiempo = sumaTiempo % 60;
        }
    }
    tiempo.minutos = sumaTiempo;
    return tiempo;
}
let resultado = calcular_tiempo(29, 48, 60, 22, 38, 31, 21, 58, 7);
console.log(resultado);