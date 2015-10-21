from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def play():
  return render_template('pages/play.html')

@app.route('/board')
def board():
  return render_template('/general/board.html')

if __name__=="__main__":
  app.debug = True
  app.run(host='0.0.0.0', use_evalex=False)
