from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def begin():
    return 'Hello Kamya'


@app.route('/p')
def render():
    message = "Hello, Flask!"
    # return render_template('./index2.html')
    return render_template('index2.html', message=message)

@app.route('/k')
def htmltag():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>K Page</title>
    </head>
    <body>
        <h1>This is the K Page</h1>
        <p>Hello, this is a simple HTML page rendered by Flask.</p>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True, port=1029)

