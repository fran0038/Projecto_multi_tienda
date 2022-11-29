class Ropa:

    def __init__(self, request):
        self.request = request
        self.session = resquest.session
        ropa = self.session["ropa"]
        if not bolsita:
            self.session["ropa"] = {}
            self.ropa = self.session["ropa"]
        else:
            self.ropa = ropa

    def agregarCompra(self, ropa):
        id = str(ropa.id)
        if id not in self.ropa.keys():
            self.ropa[id]={
                "ropa_id": ropa.id,
                "nombre": ropa.nombre,
                "codigo": ropa.codigo,
                "precio": ropa.precio,
                "talla": ropa.talla,
                "detalle":ropa.detalle,
                "cantidad": 1,
            }
        else:
            self.ropa[id]["bolsita"] += 1
            self.ropa[id]["precio"] += ropa.precio
        self.guardarCompra()

    def guardarCompra(self):
        self.session["ropa"] = self.ropa
        self.session.modified = True

    def eliminarCompra(self , ropa):
        id = str(ropa.id)
        if id in self.ropa:
            del self.ropa[id]
            self.agregarCompra()

    def resta(self, ropa):
        id = str(ropa.id)
        if id in self.ropa.keys():
            self.ropa[id]["cantidad"] -= 1
            self.ropa[id]["precio"] -= ropa.precio
            if self.ropa[id]["cantidad"] <= 0:
                self.eliminarCompra(ropa)
                self.guardarCompra()
            
    def limpiarBolsa(self):
        self.session["ropa"] = {}
        self.session.modified = True
