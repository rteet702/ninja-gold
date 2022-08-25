from flask import Flask, render_template, redirect, session, request
from random import randint


app = Flask(__name__)
app.secret_key = 'bahamut is a loser'


@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
    if 'activity' not in session:
        session['activity'] = []
    return render_template('index.html', session=session)


@app.route('/process_money', methods=['POST'])
def process_money():
    add_gold = request.form

    match add_gold['building']:
        case 'farm':
            num = randint(10, 20)
            session['gold'] += num
            session['activity'].append(f'You worked at {add_gold["building"]} and made {num} gold!')
        case 'cave':
            num = randint(5, 10)
            session['gold'] += num
            session['activity'].append(f'You worked at {add_gold["building"]} and made {num} gold!')
        case 'house':
            num = randint(2, 5)
            session['gold'] += num
            session['activity'].append(f'You worked at {add_gold["building"]} and made {num} gold!')
        case 'casino':
            num = randint(0, 50)
            if randint(0,100) >= 50:
                session['gold'] += num
                session['activity'].append(f'You went to the {add_gold["building"]} and made {num} gold!')
            else:
                session['gold'] -= num
                session['activity'].append(f'You went to the {add_gold["building"]} and lost {num} gold!')

    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)