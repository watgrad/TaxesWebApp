from flask import Flask, render_template, request
from taxes import calculate_taxes
from waitress import serve

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/taxes')
def get_amounts():
    gross_income = request.args.get('gross_income')
    gross_income = abs(int(gross_income))

    try:
        gross_income = int(gross_income)
    except TypeError:
        gross_income = 50000

    p_total, f_total, total_taxes = calculate_taxes(int(gross_income))

    return render_template(
        "taxes.html",
        gross_income = gross_income,
        p_total = p_total,
        f_total = f_total,
        total_taxes = total_taxes

    )


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8008)
