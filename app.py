from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)


model = pickle.load(open("artifacts/model.pkl", "rb"))
books_name = pickle.load(open("artifacts/books_name.pkl", "rb"))
book_pivot = pickle.load(open("artifacts/book_pivot.pkl", "rb"))
final_rating = pickle.load(open("artifacts/final_rating.pkl", "rb"))  

def recommend_book(book_name):
    if book_name not in books_name:
        return [{"title": "Book not found in database", "img_url": ""}]
    
    book_id = np.where(book_pivot.index == book_name)[0][0]
    distances, suggestions = model.kneighbors(book_pivot.iloc[book_id, :].values.reshape(1, -1), n_neighbors=6)

    recommended_books = []
    for suggestion in suggestions[0][1:]: 
        book_title = book_pivot.index[suggestion]
        book_info = final_rating[final_rating["title"] == book_title].iloc[0]
        recommended_books.append({
            "title": book_info["title"],
            "img_url": book_info["img_url"]
        })
    
    return recommended_books

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/recommend', methods=["POST"])
def recommend():
    book_name = request.form.get("book_name")
    recommendations = recommend_book(book_name)
    return render_template("index.html", book_name=book_name, recommendations=recommendations)

if __name__ == "__main__":
    app.run(debug=True)
