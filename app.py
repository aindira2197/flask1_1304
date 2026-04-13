from flask import Flask, render_template

app = Flask(__name__)

@app.route('/juft')
def juft():
    sonlar = [1, 2, 3, 4, 5, 6]
    juftlar = [s for s in sonlar if s % 2 == 0]
    return render_template('juft.html', juftlar=juftlar)

if __name__ == "__main__":
    app.run(debug=True)
