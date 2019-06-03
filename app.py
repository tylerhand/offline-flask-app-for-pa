from flask import Flask, render_template

app = Flask(__name__)

purpose='coming-soon'
email='hand7029@vandals.uidaho.edu'

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if purpose == 'maintenance':
        title='Down for Maintenance'
        return render_template('offline_page.html',email=email,title=title)
    if purpose == 'coming-soon':
        title='Coming Soon!'
        return render_template('coming_soon.html',email=email,title=title)

if __name__ == '__main__':
    app.run()