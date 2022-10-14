# render-static-once-flask

* Change 'static_url_path' to some random path. It will stop static files from rendering.
 Check URL: http://localhost:7000/static/pdfs/sample.pdf.
* Add 'SECRET_KEY' in app.config to use session
* Using session render static file once