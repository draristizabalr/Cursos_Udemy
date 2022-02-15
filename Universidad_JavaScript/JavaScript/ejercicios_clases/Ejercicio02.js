class Producto{
    static idProducto = 0;
    constructor(nombre, precio, unidad){
        Producto.idProducto++
        this._nombre = nombre;
        this._precio = precio;
        this.unidad = unidad;
        this.idProducto = Producto.idProducto;
    }
    get nombre(){
        return this._nombre;
    }
    get precio(){
        return this._precio;
    }
    get idProducto(){
        return Producto.idProducto;
    }
    set nombre(nombre){
        this._nombre = nombre;
    }
    set precio(precio){
        this._precio = precio;
    }
    set idProducto(_a){
    }
    toString(){
        return this.idProducto + '| ' + 'Nombre: ' + this.nombre + ' | Precio $' + this.precio + ' | Unidad: ' + this.unidad;
    }

}
let producto1 = new Producto('Cerveza', '2000', 1);
console.log(producto1.toString());
console.log(producto1);

let producto2 = new Producto('Agua', '1000', 1);
console.log(producto2.toString());
console.log(producto2);

let producto3 = new Producto('Coca Cola', '1500', 1);
console.log(producto3.toString());
console.log(producto3);

let producto4 = new Producto('Cafe', '800', 1);
console.log(producto4.toString());
console.log(producto4);

let producto5 = new Producto('Cafe con Leche', '1300', 1);
console.log(producto5.toString());
console.log(producto5);

class Orden{
    static idOrden = 0;
    static MaxProductos = 5;
    contadorProductos = 0;
    constructor(){
        this.productos = {idProducto: [], _nombre: [], _precio: [], unidad: []}
        Orden.idOrden++;
    }
    agregarProducto(producto){
        if (Orden.MaxProductos > this.contadorProductos){
            this.contadorProductos++;
            for (let nombrePropiedad in this.productos){
                this.productos[nombrePropiedad].push(producto[nombrePropiedad])
            }
        }else{
            return 'Ya se tiene la cantidad máxima de productos en la orden';
        }
    }
    calcularTotal(){
        let suma = 0;
        for (let i = 0; i < this.productos['_precio'].length; i++){
            suma += Number(this.productos['_precio'][i]);
        }
        return suma
    }
}
let orden = new Orden();
orden.agregarProducto(producto1);
console.log(producto1)
console.log(orden.calcularTotal())
console.log(orden)

orden.agregarProducto(producto2);
console.log(producto2)
console.log(orden.calcularTotal())
console.log(orden)