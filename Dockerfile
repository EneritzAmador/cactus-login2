# Usa una imagen base de Python 3.8
FROM python:3.8

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos de tu proyecto al contenedor
COPY . .

# Instala las dependencias
RUN pip install -r requirements.txt

# Expone el puerto que usará tu aplicación
EXPOSE 8080

# Ejecuta tu aplicación cuando el contenedor se inicie
CMD ["python", "app.py"]
