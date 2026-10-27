from flask import Flask, render_template

app = Flask(__name__)

categories = {
    "🍎": "Всі фрукти",
    "🍓": "Ягоди",
    "🍊": "Цитрусові",
    "🍑": "Кісточкові",
    "🥭": "Тропічні",
    "🍐": "Яблука та груші"
}
products = [
    {
        "name": "Банани",
        "price": 45,
        "image": "https://images.unsplash.com/photo-1571771894821-ce9b6c11b08e?auto=format&fit=crop&w=400&q=75"
    },
    {
        "name": "Яблука",
        "price": 35,
        "image": "https://images.unsplash.com/photo-1560806887-1e4cd0b6cbd6?auto=format&fit=crop&w=400&q=75"
    },
    {
        "name": "Апельсини",
        "price": 55,
        "image": "https://images.unsplash.com/photo-1547514701-42782101795e?auto=format&fit=crop&w=400&q=75"
    },
    {
        "name": "Полуниця",
        "price": 120,
        "image": "https://images.unsplash.com/photo-1464965911861-746a04b4bca6?auto=format&fit=crop&w=400&q=75"
    },
    {
        "name": "Чорниця",
        "price": 150,
        "image": "https://images.unsplash.com/photo-1498557850523-fd3d118b962e?auto=format&fit=crop&w=400&q=75"
    },
    {
        "name": "Виноград",
        "price": 95,
        "image": "https://images.unsplash.com/photo-1537640538966-79f369143f8f?auto=format&fit=crop&w=400&q=75"
    },
    {
        "name": "Ківі",
        "price": 80,
        "image": "https://images.unsplash.com/photo-1618897996318-5a901fa6ca71?auto=format&fit=crop&w=400&q=75"
    },
    {
        "name": "Манго",
        "price": 140,
        "image": "https://images.unsplash.com/photo-1553279768-865429fa0078?auto=format&fit=crop&w=400&q=75"
    },
]

@app.route("/")
def index():
    return render_template("index.html", categories=categories, products=products)

if __name__ == "__main__":
    app.run(debug=True)
