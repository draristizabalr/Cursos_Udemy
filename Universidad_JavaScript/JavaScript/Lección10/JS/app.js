const personas = [];

function mostrarPersonas(){
	let texto = '';
	for(let persona of personas){
		console.log(`${persona._nombre} ${persona._apellido}`);
		texto += `<li>${persona.nombre} ${persona.apellido}`;
	}
	document.getElementById('personas').innerHTML = texto;

}
function agregarPersona(){
	const form =document.forms['form'];
	const nombre = form['nombre'];
	const apellido = form['apellido'];
	const persona = new Persona(nombre.value, apellido.value);
	personas.push(persona);
	mostrarPersonas();
	for (elemento of document.forms['form']){
		elemento.value = '';
	}
}