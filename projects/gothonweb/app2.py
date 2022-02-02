from flask import Flask
from flask import render_template
from flask import request
import os

app = Flask(__name__, template_folder="templates/")

@app.route('/hello', methods=['POST', 'GET'])
def index():
        greeting = "Hello World"

        if request.method == "POST":
            # file = request.files['file_name']

            file_name = ''
            # for file in request.files['file_name']:
            for file in request.files.getlist('file_name'):
                save_path = 'C:/Users/maggi/projects/GothonWeb/'
                file_name = file.filename
                file.save(os.path.join(save_path, file_name))
                return render_template("index.html", greeting=greeting)
        else:
            return render_template("file_form.html")

if __name__ == "__main__":
    app.run(threaded=True)
