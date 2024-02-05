# Proyecto de Envío de Correos Electrónicos Automatizados

Este proyecto es un script de Python que permite al usuario enviar correos electrónicos automatizados con contenido personalizado. El script solicita al usuario que proporcione el asunto del correo, un párrafo de introducción, el cuerpo principal del mensaje y el destinatario antes de enviarlo.

## Características

- Solicitud de asunto del correo electrónico.
- Solicitud de párrafo de introducción y cuerpo principal del mensaje.
- Añade una despedida personalizada con la fecha actual al final del mensaje.
- Permite especificar el destinatario del correo electrónico.

## Requisitos

- Python 3.x
- Acceso a un servidor SMTP (el script está configurado para usar `smtp.outlook.com`).

## Configuración

1. Clone o descargue este repositorio en su máquina local.
2. Abra el archivo `script_envio_correo.py` (o como lo haya nombrado) en su editor de código.
3. Modifique las siguientes líneas con su información de correo electrónico:

   ```python
   remitente = "su_correo@outlook.com"
   password = "su_contraseña"

## Cómo usarlo

`python3 script_envio_correo.py`
# Auto-Mail
