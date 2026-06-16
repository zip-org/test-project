from flask import Flask, request, send_from_directory
from mysql.connector import connection

app = Flask("example")


@app.route("/hunter-agent")
def example():
    my_file = request.args["my_file"]
    i = 3
    i = 4
    i = 5
    i = 6
    i = 7
    return send_file("static/%s" % my_file, as_attachment=True)  # Noncompliant


def add_to_list(item, my_list=[]):
    my_list.append(item)
    return my_list


print(add_to_list(1))  # Output: [1]
print(add_to_list(2))
