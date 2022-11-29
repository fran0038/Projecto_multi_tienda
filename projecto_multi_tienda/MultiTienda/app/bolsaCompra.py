
class Bolsa:


    def __init__(self, request):
        self.request = request
        self.session = resquest.session
        bolsita = self.session.get("bolsita")
        if not bolsita:
            self.session["bolsita"] = {}
            self.bolsita = self.session["bolsita"]
        else:
            self.bolsita = bolsita

    def agregarCompra(self, producto):
        id = str(producto.id)
        if id not in self.bolsita.keys():
            self.bolsita[id]={
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "precio": producto.precio,
                "cantidad": 1,
            }
        else:
            self.bolsita[id]["bolsita"] += 1
            self.bolsita[id]["precio"] += producto.precio
        self.guardarCompra()

    def guardarCompra(self):
        self.session["bolsita"] = self.bolsita
        self.session.modified = True

    def eliminarCompra(self , producto):
        id = str(producto.id)
        if id in self.bolsita:
            del self.bolsita[id]
            self.agregarCompra()

    def resta(self, producto):
        id = str(producto.id)
        if id in self.bolsita.keys():
            self.bolsita[id]["cantidad"] -= 1
            self.bolsita[id]["precio"] -= producto.precio
            if self.bolsita[id]["cantidad"] <= 0:
                self.eliminarCompra(producto)
                self.guardarCompra()
            
    def limpiarBolsa(self):
        self.session["bolsita"] = {}
        self.session.modified = True
