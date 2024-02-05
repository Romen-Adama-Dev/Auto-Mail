import smtplib
from email.mime.text import MIMEText
from datetime import datetime

def enviar_correo(asunto, mensaje, destinatario):
    # Configuración del servidor SMTP
    servidor = "smtp.outlook.com"
    puerto = 587
    remitente = ""
    password = ""

    # Creación del mensaje
    msg = MIMEText(mensaje, "plain", "utf-8")
    msg['Subject'] = asunto
    msg['From'] = remitente
    msg['To'] = destinatario

    # Envío del correo
    with smtplib.SMTP(servidor, puerto) as server:
        server.starttls()  # Seguridad
        server.login(remitente, password)
        server.sendmail(remitente, destinatario, msg.as_string())

def main():
    asunto = input("Ingrese el asunto del mensaje: ")
    introduccion = input("Escriba un párrafo de introducción: ")
    cuerpo = input("Escriba el cuerpo principal del mensaje: ")
    fecha_actual = datetime.now().strftime("%d/%m/%Y")
    
    mensaje_completo = (
        f"{introduccion}\n\n"
        f"{cuerpo}\n\n"
        f"Un saludo,\n"
        f"Firmado: , \n"
        f"{fecha_actual}"
    )

    destinatario = input("Ingrese la dirección de correo electrónico del destinatario: ")

    enviar_correo(asunto, mensaje_completo, destinatario)

if __name__ == "__main__":
    main()



