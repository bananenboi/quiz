from flask import Flask, render_template, request, redirect

app = Flask(__name__)

scores = {}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        answer = request.form['answer']
        score = check_answer(answer)  # Functie om het antwoord te controleren en punten toe te kennen
        scores[name] = scores.get(name, 0) + score
        return redirect('/leaderboard')
    return render_template('index.html')

@app.route('/leaderboard')
def leaderboard():
    top_scorer = max(scores, key=scores.get) if scores else None
    return render_template('leaderboard.html', scores=scores, top_scorer=top_scorer)

def check_answer(answer):
    # Functie om het antwoord te controleren en punten toe te kennen
    # Implementeer hier je eigen logica om het antwoord te controleren
    # en een passende score toe te kennen.
    # Bijvoorbeeld:
    if answer == 'optie2':
        return 1
    else:
        return 0

if __name__ == '__main__':
    app.run(debug=True)
