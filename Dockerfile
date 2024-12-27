# Menggunakan image Python resmi
FROM python:3.10-slim

# Menambahkan dependencies
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Menyalin seluruh aplikasi ke dalam container
COPY . .

# Tentukan perintah untuk menjalankan aplikasi
CMD ["python", "-m", "app"]