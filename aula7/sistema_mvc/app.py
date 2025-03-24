from flask import Flask
from flask_mysqldb import MySQL
from controllers.produto_controller import produto_bp
import config

app = Flask(__name__)
app.config.from_object(config)

mysql = MySQL(app)

app.mysql = mysql

app.register_blueprint(produto_bp)

if __name__ == '__main__':
    app.run(debug=True)