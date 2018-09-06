#encoding: utf-8
import sys
from flask import Flask
#from flask import current_app
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from views import view


app = Flask(__name__,static_folder="./static",template_folder="./templates")
app.config['SECRET_KEY'] = 'kfeefeuplkmmnkl'
#ctx=app.app_context()
#ctx.push()


bootstrap = Bootstrap(app)
moment=Moment(app)
view(app)#注册函数
"""
@app.route("/")
def index():
    return "eee"
    """
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
