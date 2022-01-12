from datetime import datetime
import pytz

bogota_timeZone = pytz.timezone("America/Bogota")
bogota_date = datetime.now(bogota_timeZone)
print("Bogotá: ", bogota_date.strftime("%d/%m/%Y, %I:%M:%S"))

mexico_timeZone = pytz.timezone("America/Mexico_City")
mexico_date = datetime.now(mexico_timeZone)
print("Ciudad de México: ", mexico_date.strftime("%d/%m/%Y, %I:%M:%S"))

caracas_timeZone = pytz.timezone("America/Caracas")
caracas_date = datetime.now(caracas_timeZone)
print("Caracas: ", caracas_date.strftime("%d/%m/%Y, %I:%M:%S"))