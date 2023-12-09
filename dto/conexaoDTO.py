import app
import conexao

#realizar o GET e POST das imagens

@app.route("/")
def hello_world():
    return "Hello World!!"

@app.post("/login")
def login_post():
    file = request.files['img']
    print(file)
    return "LOGIN"

@app.get("/imagens")
def listar_img():
    get_clients_with_connection_string()
    return "lista de imagens"

app.run(port=8080, host='localhost', debug=True)