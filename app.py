from flask import Flask, render_template, request, redirect
import json
import os

app = Flask(__name__)

# =========================================
# 🔹 JSON FILES
# =========================================
PLANS_FILE = "plans.json"
PROFILE_FILE = "profile.json"

# =========================================
# 🔹 LOAD SAVED PLANS
# =========================================
if os.path.exists(PLANS_FILE):

    with open(PLANS_FILE, "r") as file:

        saved_plans = json.load(file)

else:

    saved_plans = []

# =========================================
# 🔹 LOAD PROFILE DATA
# =========================================
if os.path.exists(PROFILE_FILE):

    with open(PROFILE_FILE, "r") as file:

        profile_data = json.load(file)

else:

    profile_data = {

        "username": "Travel Explorer"

    }

# =========================================
# 🔹 MEMORY
# =========================================
expenses = []

trip_data = {

    "budget": 0

}

# =========================================
# 🔹 SAVE FUNCTIONS
# =========================================
def save_plans():

    with open(PLANS_FILE, "w") as file:

        json.dump(saved_plans, file, indent=4)


def save_profile():

    with open(PROFILE_FILE, "w") as file:

        json.dump(profile_data, file, indent=4)

# =========================================
# 🔥 FULL GOA DATA
# =========================================
placesData = {

    "Goa": [

        # Beaches
        {
            "name": "Baga Beach",
            "rating": 4.6,
            "time": "9:00 AM - 11:00 AM",
            "type": "Beach",
            "map": "https://maps.google.com/?q=Baga+Beach"
        },

        {
            "name": "Anjuna Beach",
            "rating": 4.5,
            "time": "11:30 AM - 1:30 PM",
            "type": "Beach",
            "map": "https://maps.google.com/?q=Anjuna+Beach"
        },

        {
            "name": "Calangute Beach",
            "rating": 4.4,
            "time": "2:30 PM - 4:30 PM",
            "type": "Beach",
            "map": "https://maps.google.com/?q=Calangute+Beach"
        },

        {
            "name": "Palolem Beach",
            "rating": 4.7,
            "time": "5:00 PM - 7:00 PM",
            "type": "Beach",
            "map": "https://maps.google.com/?q=Palolem+Beach"
        },

        # Heritage
        {
            "name": "Fort Aguada",
            "rating": 4.5,
            "time": "9:00 AM - 11:00 AM",
            "type": "Heritage",
            "map": "https://maps.google.com/?q=Fort+Aguada"
        },

        {
            "name": "Chapora Fort",
            "rating": 4.6,
            "time": "11:30 AM - 1:30 PM",
            "type": "Heritage",
            "map": "https://maps.google.com/?q=Chapora+Fort"
        },

        {
            "name": "Reis Magos Fort",
            "rating": 4.4,
            "time": "2:30 PM - 4:30 PM",
            "type": "Heritage",
            "map": "https://maps.google.com/?q=Reis+Magos+Fort"
        },

        # Markets
        {
            "name": "Anjuna Flea Market",
            "rating": 4.3,
            "time": "10:00 AM - 1:00 PM",
            "type": "Market",
            "map": "https://maps.google.com/?q=Anjuna+Flea+Market"
        },

        {
            "name": "Mapusa Market",
            "rating": 4.2,
            "time": "9:00 AM - 12:00 PM",
            "type": "Market",
            "map": "https://maps.google.com/?q=Mapusa+Market"
        },

        # Nightlife
        {
            "name": "Tito’s Lane",
            "rating": 4.4,
            "time": "7:00 PM - 10:00 PM",
            "type": "Nightlife",
            "map": "https://maps.google.com/?q=Titos+Lane"
        },

        {
            "name": "Curlies Beach Shack",
            "rating": 4.5,
            "time": "8:00 PM - 11:00 PM",
            "type": "Nightlife",
            "map": "https://maps.google.com/?q=Curlies+Goa"
        },

        # Nature
        {
            "name": "Dudhsagar Waterfalls",
            "rating": 4.8,
            "time": "6:00 AM - 11:00 AM",
            "type": "Nature",
            "map": "https://maps.google.com/?q=Dudhsagar+Waterfalls"
        },

        {
            "name": "Divar Island",
            "rating": 4.6,
            "time": "2:00 PM - 5:00 PM",
            "type": "Nature",
            "map": "https://maps.google.com/?q=Divar+Island"
        }

    ]
}

# =========================================
# 🔹 WELCOME PAGE
# =========================================
@app.route('/')
def welcome():

    return render_template('welcome.html')

# =========================================
# 🔹 HOME PAGE
# =========================================
@app.route('/home')
def home():

    return render_template('index.html')

# =========================================
# 🔥 PLAN GENERATION
# =========================================
@app.route('/plan', methods=['POST'])
def plan():

    destination = request.form.get(
        'destination',
        ''
    ).strip().capitalize()

    days_input = request.form.get(
        'days',
        ''
    ).strip()

    traveller = request.form.get(
        'traveller'
    )

    # validation
    if not destination:

        return "Enter destination"

    if not days_input.isdigit():

        return "Enter valid days"

    days = int(days_input)

    expenses.clear()

    places = placesData.get(destination, [])

    if not places:

        return "No data available"

    itinerary = []

    index = 0

    # 🔥 DAY-WISE ITINERARY
    for d in range(days):

        day_plan = []

        for i in range(3):

            if index < len(places):

                p = places[index]

                day_plan.append({

                    "name": p["name"],
                    "rating": p["rating"],
                    "time": p["time"],
                    "type": p["type"],
                    "map": p["map"]

                })

                index += 1

        itinerary.append({

            "day": d + 1,
            "places": day_plan

        })

    # 🔥 SAVE PLAN
    saved_plans.append({

        "destination": destination,
        "days": days,
        "traveller": traveller,
        "itinerary": itinerary

    })

    # 🔥 SAVE TO JSON
    save_plans()

    return render_template(

        'plan.html',

        itinerary=itinerary,
        destination=destination,
        traveller=traveller

    )

# =========================================
# 🔹 SAVED PAGE
# =========================================
@app.route('/saved')
def saved():

    return render_template(

        'saved.html',

        saved_plans=saved_plans

    )

# =========================================
# 🔹 DELETE SAVED PLAN
# =========================================
@app.route('/delete-plan/<int:index>')
def delete_plan(index):

    if index < len(saved_plans):

        saved_plans.pop(index)

        # 🔥 SAVE UPDATED DATA
        save_plans()

    return redirect('/saved')

# =========================================
# 🔹 PROFILE PAGE
# =========================================
@app.route('/profile')
def profile():

    return render_template(

        'profile.html',

        saved_count=len(saved_plans),

        username=profile_data["username"]

    )

# =========================================
# 🔹 EDIT PROFILE
# =========================================
@app.route('/edit-profile', methods=['GET', 'POST'])
def edit_profile():

    if request.method == 'POST':

        new_username = request.form.get('username')

        if new_username:

            profile_data["username"] = new_username

            # 🔥 SAVE PROFILE
            save_profile()

        return redirect('/profile')

    return render_template(

        'edit_profile.html',

        username=profile_data["username"]

    )

# =========================================
# 🔹 BUDGET PAGE
# =========================================
@app.route('/budget')
def budget():

    total_spent = sum(

        e["amount"]

        for e in expenses

    )

    remaining = trip_data["budget"] - total_spent

    return render_template(

        'budget.html',

        expenses=expenses,

        total_spent=total_spent,

        total_budget=trip_data["budget"],

        remaining=remaining

    )

# =========================================
# 🔹 ADD EXPENSE
# =========================================
@app.route('/add-expense', methods=['POST'])
def add_expense():

    category = request.form.get(
        'category',
        ''
    ).strip()

    amount_input = request.form.get(
        'amount',
        ''
    ).strip()

    if category and amount_input.isdigit():

        expenses.append({

            "category": category,

            "amount": int(amount_input)

        })

    return redirect('/budget')

# =========================================
# 🔹 RUN APP
# =========================================
if __name__ == '__main__':

    app.run(debug=True)