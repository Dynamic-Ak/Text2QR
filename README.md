# Text2QR
# QR Code Generator

A simple Flask web application to generate QR codes from your text input and download them as images.

---

## Features

- Generate QR codes from any text or URL
- Download the generated QR code as a PNG image
- Clean, user-friendly web interface

---

## Demo

<!-- Optionally, add a screenshot here -->
<!-- ![App Screenshot](static/screenshot.png) -->

---

## Getting Started

### Prerequisites

- Python 3.7 or higher
- pip

### Installation

1. **Clone the repository**
    ```
    git clone https://github.com/yourusername/qr-code-generator.git
    cd qr-code-generator
    ```

2. **Install dependencies**
    ```
    pip install -r requirements.txt
    ```
    Or manually:
    ```
    pip install flask qrcode pillow
    ```

3. **Run the application**
    ```
    python app.py
    ```

4. **Open your browser**
    - Visit [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## Usage

1. Enter your text or URL in the text area.
2. Click **Generate QR**.
3. The QR code will appear below.
4. Click **Download QR Code** to save the image.

---

## Project Structure

qr-code-generator/
├── app.py
├── templates/
│ └── index.html
├── static/
│ ├── style.css
│ ├── icon.png
│ └── qr_code.png
├── requirements.txt
└── README.md


---

## Dependencies

- [Flask](https://flask.palletsprojects.com/)
- [qrcode](https://pypi.org/project/qrcode/)
- [Pillow](https://python-pillow.org/)

---

## Credits

Created by dynamic ak with 🤍

---

## License

This project is licensed under the [MIT License](LICENSE).
