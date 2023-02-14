from flask import Flask, render_template

app = Flask (__name__)

# POSTS MOCK
posts = [
    {
        "titulo": "Post 1",
        "texto": "Meu Primeiro Post"
    },
    {
        "titulo": "Post 2",
        "texto": "Olha eu aqui de novo"
    },
    {
        "titulo": "Post 3",
        "texto" : "New Post"
    }
]

@app.route('/')
def exibir_entradas ():
    return render_template ("exibir_entradas.html",  entradas=posts)
    
    