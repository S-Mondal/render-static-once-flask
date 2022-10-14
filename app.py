from flask import Flask, session, abort, redirect
import os

app = Flask(__name__, static_url_path='/test')

app.config.update(
    SECRET_KEY='IAMGENIUS'
)

@app.route('/getPDF/<path:path>')
def getPDF(path):
    session["path"] = os.path.dirname(path)
    return redirect('/protected/'+os.path.basename(path))

@app.route('/protected/<file>')
def static_file(file):
    if "path" in session:
        path = os.path.join(session['path'],file)
        
        session.pop('path', None)
        return app.send_static_file(path)
    else:
        abort(403)

app.run(port=7000)