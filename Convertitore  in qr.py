import qrcode
from PIL import Image

def genera_qr_code(data, filename):
    # Crea un oggetto QRCode
    qr = qrcode.QRCode(
        version=1,  # Controlla la dimensione del QR Code
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # Livello di correzione degli errori
        box_size=10,  # Dimensione di ogni box del QR Code
        border=4,  # Spessore del bordo
    )
    
    # Aggiungi i dati al QR Code
    qr.add_data(data)
    qr.make(fit=True)

    # Crea un'immagine del QR Code
    img = qr.make_image(fill_color="black", back_color="white")

    # Salva l'immagine
    img.save(filename)

    # Mostra l'immagine (opzionale)
    img.show()

if __name__ == "__main__":
    # Richiedi i dati e il nome del file all'utente
    data = input("Inserisci i dati da codificare nel QR Code: ")
    filename = input("Inserisci il nome del file per salvare l'immagine (es: qr_code.png): ")

    # Genera il QR Code
    genera_qr_code(data, filename)
