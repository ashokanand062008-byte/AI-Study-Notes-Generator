from flask import Flask , render_template ,request
from notes_generator import gen_notes
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/gen_notes',methods = ['POST','GET'])
def gen():
    user_input = request.data
    result = gen_notes(user_input = user_input)
    return result
if __name__ == '__main__':
    app.run(debug = True)