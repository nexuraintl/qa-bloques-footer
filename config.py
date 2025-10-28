# /var/www/html/servicios/serviciofooter/config.py

MSG_ERROR_PARAMETRO_REQUERIDO = "El parámetro 'url' es requerido."
MSG_ERROR_URL_INVALIDA = "La URL proporcionada no es válida o utiliza un protocolo no permitido."
MSG_ERROR_SSRF = "La URL apunta a una dirección de red interna o reservada, lo cual no está permitido."
MSG_ERROR_OBTENER_CONTENIDO = "No se pudo obtener el contenido de la URL especificada."
MSG_ERROR_FOOTER_NO_ENCONTRADO = "No se encontró la etiqueta <footer> en la URL especificada."
PROTOCOLOS_PERMITIDOS = ['http', 'https']
USER_AGENT = 'Footer-Extractor/1.0'