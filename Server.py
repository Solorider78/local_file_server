from flask import Flask , render_template ,send_from_directory
import os
app = Flask(__name__)

@app.route('/')
def home_page1():
  return render_template('./index.html')


@app.route('/<string:file_name>')
def send_file(file_name):
   return send_from_directory(os.getcwd() + '\\Uploads',file_name)




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=369,debug=True)

