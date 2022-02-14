console.log('Funciona')

function add(){
    let number_1 = document.getElementById('firstNumber');
    let number_2 = document.getElementById('secondNumber');
    if (number_1.value === '' || number_2.value === ''){
        document.getElementById('result').innerHTML = 'You have to write 2 numbers to add.';
    }else{
        let result = Number(number_1.value) + Number(number_2.value);
        document.getElementById('result').innerHTML = result;
    }
}