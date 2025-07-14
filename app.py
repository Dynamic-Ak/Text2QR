import qrcode
import os
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def generate_qr():
    error = None
    qr_generated = False
    if request.method == "POST":
        data = request.form["data"]
        if not data.strip():
            error = "Please enter some text."
        else:
            qr_img = qrcode.make(data)
            qr_path = os.path.join("static", "qr_code.png")
            qr_img.save(qr_path)
            qr_generated = True
    return render_template("index.html", error=error, qr_generated=qr_generated)

if __name__ == "__main__":
    app.run(debug=True)
