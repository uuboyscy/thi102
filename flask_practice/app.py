from flask import Flask, request, jsonify, render_template

import poker as p
import model

app = Flask(__name__, static_url_path="/source", static_folder="./source")


@app.route("/")
def index_page():
    return "Hello Flask!"


# @app.route("/hello/<username>")
# def hello(username: str):
#     result = "<h1>Hello {}</h1>".format(username)
#     return result


@app.route("/hello/<username>")
def hello(username: str):
    return render_template("index.html", username=username)


@app.route("/two_sum/<int:x>/<int:y>")
def two_sum(x: int, y: int):
    return str(x + y)

# [GET] /get_emploeey/<string:dep_id>/<string:pos_type>
@app.route("/get_emploeey/<string:dep_id>/<string:pos_type>")
def get_emploeey(dep_id: str, pos_type: str) -> str:
    sql = f"""
        select emp_name, enm_id, emp_gender, emp_pos_type
        from emp
        where dep_id = '{dep_id}' and pos_type = '{pos_type}'
    """
    result = sql
    # result = db_connection(sql)
    return result


# /hello_get?username=Allen&age=22
@app.route("/hello_get")
def hello_get() -> str:
    username = request.args.get("username")
    age = request.args.get("age")

    if username is None:
        return "What is your name?"

    if age is None:
        return f"Hello {username}."

    return f"Hello {username}, you are {age} years old."


# @app.route("/hello_post", methods=["GET", "POST"])
# def hello_post() -> str:
#     html = """
#         What is your name?<br>
#         <form method="POST">
#             <input name="username">
#             <button>SUBMT</button>
#         </form>
#     """
#     request_method = request.method
#     if request_method == "POST":
#         username = request.form.get("username")
#         # request.json
#         html += f"<h1>Hello {username}</h1>"

#     return html


@app.route("/hello_post", methods=["GET", "POST"])
def hello_post() -> str:
    request_method = request.method
    username = request.form.get("username")

    return render_template(
        "hello_post.html",
        request_method=request_method,
        username=username,
    )


@app.route("/shuffle_poker/<int:player_num>")
def shuffle_poker(player_num: int) -> str:
    result = p.poker(player_num)
    return jsonify(result)


@app.route('/poker', methods=['GET', 'POST'])
def poker():
    request_method = request.method

    players = int(request.form.get('players', "1"))
    cards = p.poker(players)

    return render_template(
        'poker.html',
        request_method=request_method,
        cards=cards,
    )


@app.route('/show_staff')
def hello_google():
    staff_data = model.getStaff()
    column = ['ID', 'Name', 'DeptId', 'Age', 'Gender', 'Salary']
    return render_template(
        'show_staff.html',
        staff_data=staff_data,
        column=column,
    )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
