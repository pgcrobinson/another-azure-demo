from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hey Anish how is it going ?'

if __name__ == '__main__':
  app.run()
