from datetime import date, datetime, timedelta
import pytz


tipo_carro = "M" # P, M, G 
tempo_pequeno = timedelta(minutes=30)
tempo_medio = timedelta(minutes=45)
tempo_grande = timedelta(minutes=60)
data_atual = datetime.now()
forma_hora = "%H:%M"
data_ptbr = "%d/%m/%Y %H:%M"


if tipo_carro == "P":
    data_estimada = data_atual + tempo_pequeno
    print(f"chegou: {data_atual.strftime(data_ptbr)}. ficará pronto: {data_estimada.strftime(forma_hora)}")
    
elif tipo_carro == "M":
    data_estimada = data_atual + tempo_medio
    print(f"chegou: {data_atual.strftime(data_ptbr)}. ficará pronto: {data_estimada.strftime(forma_hora)}")
    
else:
    data_estimada = data_atual + tempo_grande
    print(f"chegou: {data_atual.strftime(data_ptbr)}. ficará pronto: {data_estimada.strftime(forma_hora)}")

