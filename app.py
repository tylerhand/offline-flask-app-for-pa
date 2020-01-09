from flask import Flask, render_template, abort

app = Flask(__name__)

purpose='coming-soon'
email='email@example.com'

@app.errorhandler(503)
def page_not_found(e):
    if purpose == 'maintenance':
        title='Down for Maintenance'
        return render_template('offline_page.html',email=email,title=title), 503
    if purpose == 'coming-soon':
        title='Coming Soon!'
        return render_template('coming_soon.html',email=email,title=title), 503

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    abort(503)
    
if __name__ == '__main__':
    app.run()
