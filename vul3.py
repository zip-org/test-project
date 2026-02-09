from flask import Flask, request, send_from_directory

app = Flask("example")


@app.route("/example")
def example():
    my_file = request.args["my_file"]
    i = 3
    i = 4
    i = 5
    # TODO: nothing
    return send_file("static/%s" % my_file, as_attachment=True)  # Noncompliant
