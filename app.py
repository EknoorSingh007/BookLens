from flask import Flask, render_template, request
import pickle
import numpy as np
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

popular_df = pickle.load(open(os.path.join(BASE_DIR, 'popular.pkl'), 'rb'))
pt = pickle.load(open(os.path.join(BASE_DIR, 'pt.pkl'), 'rb'))
books = pickle.load(open(os.path.join(BASE_DIR, 'books.pkl'), 'rb'))
similarity_scores = pickle.load(open(os.path.join(BASE_DIR, 'similarity_scores.pkl'), 'rb'))

app = Flask(__name__)

book_list = sorted(list(pt.index))

@app.route('/')
def index():
    return render_template('index.html',
                           book_name = list(popular_df['Book-Title'].values),
                           author = list(popular_df['Book-Author'].values),
                           image = list(popular_df['Image-URL-M'].values),
                           votes = list(popular_df['num_ratings'].values),
                           rating = list(popular_df['avg_rating'].values)
                           )

@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html', book_list=book_list)

@app.route('/recommend_books', methods=['post'])
def recommend():
    user_input = request.form.get("user_input")
    num_rec = request.form.get("num_rec")

    matches = np.where(pt.index == user_input)[0]
    if len(matches) == 0:
        return render_template('recommend.html', book_list=book_list,
                               error=f'Book "{user_input}" not found. Please select a title from the suggestions.')

    index = matches[0]
    similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:int(num_rec) + 1]

    data = []
    for i in similar_items:
        item = []
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))
        data.append(item)
    return render_template('recommend.html', book_list=book_list, data=data)


if __name__ == '__main__':
    app.run(debug=False)