from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>مرحباً بك في تطبيق خدمة حديثة - النسخة الاحترافية</h1><p>التطبيق يعمل بنجاح على المنصة الجديدة!</p>"

if __name__ == "__main__":
    app.run(debug=True)
