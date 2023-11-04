# Recomendador de ropa Micropython ESP8266

Este proyecto es un ejemplo de una aplicación que obtiene datos de pronóstico del tiempo de una API y muestra la información en una pantalla OLED en un dispositivo basado en el microcontrolador ESP8266.

## Requisitos

- Microcontrolador ESP8266
- Pantalla OLED SH1106
- Conexión a Internet
- Bibliotecas de Python para micropython

## Configuración

Antes de usar la aplicación, asegúrate de configurar los siguientes parámetros en el código:

- `SSID`: Nombre de tu red Wi-Fi.
- `PASSWORD`: Contraseña de tu red Wi-Fi.
- `URL_API`: URL de la API del pronóstico del tiempo.

Asegúrate de haber conectado físicamente tu dispositivo al hardware correspondiente, como la pantalla OLED y los pines I2C, según las conexiones en el código.

## Uso

1. El código se encarga de conectarse a tu red Wi-Fi proporcionando las credenciales (`SSID` y `PASSWORD`) y luego obtiene datos del pronóstico del tiempo desde la API definida en `URL_API`.

2. Los datos del pronóstico del tiempo se muestran en la pantalla OLED, incluyendo el día de la semana, temperaturas mínimas y máximas, y un ícono que representa el estado del tiempo.

3. Además, el código también interactúa con un sistema de administración de ropa (`ClothingManager`) para sugerir un atuendo adecuado según el pronóstico del tiempo.

## Personalización

Puedes personalizar este código agregando modificando la biblioteca `ClothingManager` ajustando la forma en que se sugiere el atuendo de acuerdo a tus preferencias personales.

## Créditos

Este código utiliza las bibliotecas de micropython para interactuar con la pantalla OLED de robert-hh y la API del pronóstico del tiempo de Meteored.cl.

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.
