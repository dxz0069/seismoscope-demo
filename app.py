"""候风 Seismoscope 演示应用——故意包含 5 类典型 vibe-coding 漏洞。

fork 本仓库后 CI 会自动运行候风审查，在 Security 标签页看到 SARIF 告警。
"""
from flask import Flask, request

import subprocess

app = Flask(__name__)

SECRET_KEY = "sk-demo-1234567890abcdef"  # 硬编码密钥（会被检出）


@app.route("/greet")
def greet():
    name = request.args.get("name", "")
    return f"<h1>Hello, {name}!</h1>"  # 反射型 XSS（f-string 拼 HTML）


@app.route("/lookup")
def lookup():
    title = request.args.get("title")
    query = "SELECT * FROM books WHERE title = '" + title + "'"  # SQL 注入（拼接）
    return query


@app.route("/ping")
def ping():
    host = request.args.get("host")
    return subprocess.run(f"ping -n 1 {host}", shell=True, capture_output=True).stdout  # 命令注入


@app.route("/book/<book_id>")
def get_book(book_id):
    from auth import token_validator  # noqa: F401
    token_validator(request.headers.get("Authorization"))  # 已认证接口
    from models import Book
    book = Book.query.filter_by(book_title=str(book_id)).first()  # IDOR（认证后无所有权谓词）
    return str(book)
