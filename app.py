from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Asegúrate de que tu archivo HTML se llama index.html

if __name__ == '__main__':
    app.run(debug=True)
