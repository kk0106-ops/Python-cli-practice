from flask import Flask, render_template

app = Flask(__name__)

@app.route("/<int:number>")
def hello_world(number):
    posts = [
        {"title": "記事のタイトル1", "body" : "記事の内容1", "created_at" : "2026-03-31"},
        {"title": "記事のタイトル2", "body" : "記事の内容2", "created_at" : "2026-04-01"},
        {"title": "記事のタイトル3", "body" : "記事の内容3", "created_at" : "2026-04-02"},
        {"title": "記事のタイトル4", "body" : "記事の内容4", "created_at" : "2026-04-02"}

    ]
    post = posts[number]
    return render_template("admin.html", post = post)

if __name__ == "__main__":
    app.run(debug=True)