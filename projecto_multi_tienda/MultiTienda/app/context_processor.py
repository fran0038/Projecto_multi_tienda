from app.bolsaCompra import Bolsa


def total_bolsita(request):
    total = 0
    if request.user.is_authenticated:
        if "bolsita" in request.session.keys():
            
            for key , value in request.session["bolsita"].items():
                total += int(value["precio"])
    return {"total_bolsita":total}