from flask import Flask, render_template

# 1. CREAR LA APP PRIMERO
app = Flask(__name__)

# 2. RUTA PRINCIPAL
@app.route("/")
def home():
    return render_template("index.html")

# 3. EJECUTAR EL SERVIDOR
if __name__ == "__main__":
    app.run(debug=True)