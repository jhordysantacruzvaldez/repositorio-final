@app.route("/")
def index():
    return render_template_string(HTML)

if __name__ == "__main__":
    # debug=False evita que el servidor se reinicie solo y cause errores de conexion
    app.run(host='0.0.0.0', port=5000, debug=False)