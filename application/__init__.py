from flask import Flask, render_template
import os
from application.model.entity.recuperacaoSenha import RecuperacaoSenha
from application.model.entity.autor import Autor


app = Flask(
    __name__,
    static_folder=os.path.abspath("application/view/static"),
    template_folder=os.path.abspath("application/view/template"),
)

recuperacaoList = []
listaAutores = []
from application.controller import alteracaoSenha_controller
from application.controller import recuperacaoSenha_controller
from application.controller import login_controller
from application.controller import a_controller
from application.controller import blog_controller
from application.controller import feed_controller

autor1 = Autor(1, "Pedro Silva", "PedroSilva", 12345, "pedro.q2000@outlook.com")
autor2 = Autor(2, "Tadeu Berardinelli", "TadeuBerardinelli", 54321, "antoniotadeubf98@gmail.com")
usuario_dao = UsuarioDAO()
app.config["usuario_dao"] = usuario_dao

recuperacao1 = RecuperacaoSenha(1, "17/10", autor2, "antoniotadeubf98@gmail.com")

listaAutores.append(autor1)
listaAutores.append(autor2)
recuperacaoList.append(recuperacao1)

from application.controller import index_controller
from application.controller import recuperacaoSenha_controller
from application.controller import alteracaoSenha_controller
