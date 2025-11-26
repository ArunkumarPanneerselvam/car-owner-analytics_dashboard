import pandas as pd
import numpy as np
import random

np.random.seed(42)

genders = ["Male", "Female", "Other"]
ethnicities = ["White", "Black", "Asian", "Hispanic", "Mixed", "Other"]
occupations = ["Engineer", "Doctor", "Artist", "Teacher", "Developer", "Manager", "Lawyer", "Student", "Unemployed"]
hair_colors = ["Blonde", "Brown", "Black", "Red", "Gray", "Dyed", "Bald"]

car_makes_models = {
    "Toyota": ["Camry", "Corolla", "Yaris", "Prius"],
    "Honda": ["Civic", "Accord", "Fit", "CR-V"],
    "Ford": ["Focus", "Fiesta", "Mustang", "Explorer"],
    "BMW": ["320i", "X5", "M3", "i3"],
    "Audi": ["A3", "A4", "Q5", "TT"],
    "Skoda": ["Octavia", "Superb", "Fabia", "Kodiaq"],
    "Hyundai": ["Elantra", "Sonata", "Tucson", "Accent"]
}

body_styles = ["Sedan", "Hatchback", "SUV", "Coupe", "Convertible", "Wagon"]
engine_sizes = [1.0, 1.2, 1.4, 1.6, 2.0, 2.2, 3.0, 4.0]
fuel_types = ["Petrol", "Diesel", "Electric", "Hybrid"]
driving_styles = ["Calm", "Moderate", "Aggressive"]
is_modified_opts = ["Yes", "No"]

def generate_data(num=200):
    data = []
    for _ in range(num):
        gender = random.choice(genders)
        ethnicity = random.choice(ethnicities)
        age = np.random.randint(18, 70)
        income = np.random.randint(15000, 200000)
        occupation = random.choice(occupations)
        hair_color = random.choice(hair_colors)

        car_make = random.choice(list(car_makes_models.keys()))
        car_model = random.choice(car_makes_models[car_make])
        car_age = np.random.randint(0, 20)
        engine_size = round(random.choice(engine_sizes), 1)
        body_style = random.choice(body_styles)
        fuel_type = random.choice(fuel_types)
        driving_style = random.choice(driving_styles)
        is_modified = random.choice(is_modified_opts)
        mileage_per_year = np.random.randint(5000, 30000)
        service_visits = np.random.randint(0, 6)

        cost = round(np.random.normal(30000 - (car_age * 1000) + (engine_size * 2000), 5000), -2)
        cost = max(5000, cost)

        data.append({
            "OwnerID": f"O{_+1:03d}",
            "Gender": gender,
            "Ethnicity": ethnicity,
            "Age": age,
            "Income": income,
            "Occupation": occupation,
            "HairColor": hair_color,
            "CarMake": car_make,
            "CarModel": car_model,
            "CarAge": car_age,
            "EngineSize": engine_size,
            "BodyStyle": body_style,
            "CarCost": int(cost),
            "FuelType": fuel_type,
            "DrivingStyle": driving_style,
            "IsModified": is_modified,
            "MileagePerYear": mileage_per_year,
            "ServiceHistory": service_visits
        })
    return pd.DataFrame(data)

# Generate dataset
df = generate_data(300)
df.to_csv("car_owner_data.csv", index=False)
print("✅ Dataset created with extended features: 'car_owner_data.csv'")
