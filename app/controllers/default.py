from app import app
from bottle import request, template
from bottle import static_file


# static routes
@app.get('/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='static/css')

@app.get('/<filename:re:.*\.js>')
def javascript(filename):
    return static_file(filename, root='static/js')

@app.get('/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    return static_file(filename, root='static/img')

@app.get('/<filename:re:.*\.(eot|ttf|woff|svg)>')
def fonts(filename):
    return static_file(filename, root='static/fonts')


# @route('/')
# def index():
#     return '<h1>Hello world</h1>'

# @route('/')
# def index():
#     return template('index')

@app.route('/')# @get('/login')
def login():
    return template('login')

@app.route('/login')# @get('/login')
def login():
    return template('login')



@app.route('/cadastro')
def cadastro():
    return template('cadastro')


@app.route('/cadastro', method='POST')
def acao_cadastro():
    username = request.forms.get('username')
    password = request.forms.get('password')
    insert_user(username, password)
    return template('verificacao_cadastro', nome=username)



# def check_login(username, password):
#     d = {'marcos':'python', 'joao':'java','pedro':'go'}
#     return True if d[username] == password else False
#     if username in d.keys() and d[username] == password:
#         return True
#     return False


@app.route('/', method='POST') # @post('/login')
def acao_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    return template('verificacao_login', sucesso=True)

@app.error(404)
def error404(error):
    return template('pagina404')

