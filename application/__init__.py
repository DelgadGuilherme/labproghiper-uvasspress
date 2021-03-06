from flask import Flask, render_template
import os
from application.model.dao.usuarioDAO import UsuarioDAO
from application.model.dao.post_DAO import PostDAO
from application.model.entity.post import Post
from application.model.dao.administradorDAO import AdministradorDAO
from application.model.entity.administrador import Administrador
from application.model.dao.blog_dao import BlogDAO
from application.model.entity.blog import Blog
from application.model.entity.recuperacaoSenha import RecuperacaoSenha
from application.model.entity.autor import Autor


app = Flask(__name__, static_folder=os.path.abspath("application/view/static"), template_folder=os.path.abspath("application/view/template"))

todas_postagens = []
todas_postagens.append(Post(1, "Título do Post 1", "Conteúdo do post 1", "Descrição do post 1", "img/diretorioimagemdestaque", "data e hora criacao", "data e hora edicao", "ativo ou inativo", "Pedro Silva", 1))
todas_postagens.append(Post(2, "Título do Post 2", "Conteúdo do post 2", "Descrição do post 2", "img/diretorioimagemdestaque", "data e hora criacao", "data e hora edicao", "ativo ou inativo", "Tadeu Berardinelli", 2))

listaAdministradores = []
listaAdministradores.append(Administrador(1, "Pedro Silva", "PedroSilva", 12345, "pedro.q2000@outlook.com"))
listaAdministradores.append(Administrador(2, "Tadeu Berardinelli", "TadeuBerardinelli", 54321, "antoniotadeubf98@gmail.com"))

usuario_dao = UsuarioDAO()
app.config["usuario_dao"] = usuario_dao
blog_dao = BlogDAO()
app.config["blog_dao"] = blog_dao

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

from application.controller import post_controller