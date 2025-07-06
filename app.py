from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def serve_vue_app():
    return render_template('index.html')

from routes.child_routes import child_bp
from routes.parent_routes import parent_bp
from routes.teacher_routes import teacher_bp

app.register_blueprint(child_bp, url_prefix='/api/child')
app.register_blueprint(parent_bp, url_prefix='/api/parent')
app.register_blueprint(teacher_bp, url_prefix='/api/teacher')

if __name__ == '__main__':
    app.run(debug=True)