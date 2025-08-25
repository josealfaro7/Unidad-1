from django.shortcuts import render

def panel(request):
    dispositivos = [
        {"nombre": "Refrigerador", "consumo": 120, "limite": 150},
        {"nombre": "Horno Eléctrico", "consumo": 250, "limite": 200},
        {"nombre": "Televisor", "consumo": 80, "limite": 100},
    ]

    contexto = {"dispositivos": dispositivos}
    return render(request, "dispositivos/panel.html", contexto)
