let miPromesa = new Promise((resolve, rejected) => {
    let expresion = true;
    if (expresion){
        resolve('Resolvió correcto.')
    }else{
        rejected('Se produjo un error.');
    }
});

// miPromesa.then(
//     valor => console.log(valor),
//     error => console.log(error)
// );

// miPromesa
// .then(valor => console.log(valor))
// .catch(error => console.log(error));

let promesa = new Promise((resolve) => {
    setTimeout(()=> resolve('saludos con promesa y timeout'), 3000);
});

// promesa.then(valor => console.log(valor));

// async: Indica que una función regresa una promesa
async function miFuncionConPromesa(){
    return 'Saludos con promesa y async';
}
// miFuncionConPromesa().then(valor => console.log(valor))

//async/await
async function funcionAsyncConAwait(){
    let miPromesa = new Promise(resolve=>{
        resolve('Promesa con await');
    });

    console.log(await miPromesa);
}

// funcionAsyncConAwait();

//promesas, await, async, y setTimeout
async function funcionConPromesaAsyncAwaitTimeout() {
    let miPromesa = new Promise(resolver => {
        setTimeout(() => resolver('promesa con await y timeout'),3000);
    });
    console.log(await miPromesa);
    console.log('fin de la función');
}

funcionConPromesaAsyncAwaitTimeout()