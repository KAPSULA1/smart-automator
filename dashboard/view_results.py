from flask import Flask, render_template_string
import csv

TEMPLATE = """
<!doctype html>
<title>Smart Automator - Results</title>
<h1>Smart Automator - Last Run</h1>
<table border="1" cellpadding="8">
  <tr>{% for h in headers %}<th>{{ h }}</th>{% endfor %}</tr>
  {% for row in rows %}
  <tr>{% for h in headers %}<td>{{ row[h] }}</td>{% endfor %}</tr>
  {% endfor %}
</table>
"""

def load_csv(path="reports/results.csv"):
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        headers = reader.fieldnames
    return headers, rows

app = Flask(__name__)

@app.route("/")
def home():
    headers, rows = load_csv()
    return render_template_string(TEMPLATE, headers=headers, rows=rows)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
