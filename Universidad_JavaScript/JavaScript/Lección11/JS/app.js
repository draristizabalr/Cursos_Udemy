const mostrarReloj = () => {
    let fecha = new Date();
    let tiempo ={
        hora: fecha.getHours(),
        min: fecha.getMinutes(),
        seg: fecha.getSeconds()
    }
    for (nombrePropiedad in tiempo){
        tiempo[nombrePropiedad] = formaHora(tiempo[nombrePropiedad]);
    }
    document.getElementById('hora').innerHTML = `${tiempo.hora}:${tiempo.min}:${tiempo.seg}`

    const meses = ['Ene', 'Feb', 'Marz', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
    const dias = ['Dom', 'Lun', 'Mar', 'Mie', 'Jue', 'Vie', 'Sab']
    let diaSemana = dias[fecha.getDay()];
    let dia = fecha.getDate();
    let mes = meses[fecha.getMonth()];
    let fechaTexto = `${diaSemana}, ${dia} ${mes}`;
    
    document.getElementById('fecha').innerHTML = fechaTexto;
}

const formaHora= (hora)=>{
    if (hora < 10)
        hora = '0' + hora;
    return hora;
}

setInterval(mostrarReloj, 1000);