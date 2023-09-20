from flask import Flask, render_template, request, redirect, url_for, flash
from function_csv import append_csv_data
from classes import Journey, Trips


app = Flask(__name__)

app.config['SECRET_KEY'] = '123123'


@app.route('/', methods=['GET', 'POST'])
def index():

    # Tworzy listę zaproponowanych wycieczek
    trip = Trips()
    trip.load_trips()

    if request.method == 'GET':
        active_menu = 'Home'
        return render_template('index.html', trip=trip.list_of_trips, active_menu=active_menu)
    
    else:
        
        trip.get_priority_by_code(request.form['choosen_trip'])
        var = trip.get_priority_by_code(request.form['choosen_trip'])
   
        return render_template('added_proposal.html', var=var)


@app.route('/proposal', methods=['GET', "POST"])
def proposal():

    if request.method == 'GET':
        active_menu = 'Add idea'
        return render_template('proposal.html', active_menu=active_menu)

    else:

        trip = Trips()
        trip.load_trips()
        id = len(trip.list_of_trips)
        id = id + 1

        trip_text = ''
        if 'trip_text' in request.form:
            trip_text = request.form['trip_text']
            
        email = ''
        if 'email' in request.form:
            email = request.form['email']

        short_text = 'brak'
        if 'short_text' in request.form:
            short_text = request.form['short_text']

        completness = 'brak'
        if 'completness' in request.form:
            completness = request.form['completness']
       
        contact = False if 'contact' not in request.form else True

        # Sprawdza czy nazwa wycieczki jest wpisana
        if trip_text.strip() == '':
                again = [email, short_text, completness, contact]

                if short_text.strip() == '':
                    short_text = 'brak'
                return redirect(url_for('proposalAgain', email=email, short_text=short_text, completness=completness, contact=contact)), flash(f"Trip proposal hasn't had name. Fill again form!")

        data = {'trip_text': trip_text, 'email': email, 'short_text': short_text, 'completness': completness, 'contact': contact, 'id': id}

        append_csv_data(data)

        
        return redirect(url_for('index')), flash('Proposal trip has been saved.')


# Przekazuje wartości z forma i oczekuje jeszcze wypełnienia nazwy wycieczki
@app.route('/proposalAgain/<email>/<short_text>/<completness>/<contact>', methods=['GET'])
def proposalAgain(email, short_text, completness, contact ):

    return render_template('proposalAgain.html', email=email, short_text=short_text, completness=completness, contact=contact)

if __name__ == '__main__':
    app.run()
