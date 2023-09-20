from function_csv import append_csv_data, read_csv_data

class Journey:
    def __init__(self, trip_text, email, short_text, completness, contact, id):
        self.trip_text = trip_text
        self.email = email
        self.short_text = short_text
        self.completness = completness
        self.contact = contact
        self.id = id

class Trips:
    def __init__(self):
        self.list_of_trips = []
        self.i = read_csv_data()

    def load_trips(self):
        for trip in self.i:
            self.list_of_trips.append(Journey(trip['trip_text'],trip['email'], trip['short_text'], trip['completness'], trip['contact'], trip['id'] ))
        
    def get_priority_by_code(self, id):
        for id_t in self.list_of_trips:
            if id_t.id == id:
                return id_t
            