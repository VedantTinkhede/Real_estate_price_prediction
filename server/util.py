import json, pickle
import numpy as np

# Global variables
__locations = None
__data_columns = None
__model = None


def get_estimated_price(location, sqft, bath, bhk):
    loc_index = __data_columns.index(location.lower()) if location.lower() in __data_columns else -1
    
    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk

    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)


def get_location_names():
    load_saved_artifacts()  # Ensure artifacts are loaded before accessing locations
    return __locations


def load_saved_artifacts():  # needs to be called just once before any prediction
    print("Loading saved artifacts...")

    global __data_columns
    global __locations
    global __model

    with open("server/artifacts/columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:] # Because the locations start from the 4th index, see the file

    with open("server/artifacts/banglore_model.pickle", 'rb') as f:
        __model = pickle.load(f)
    
    print("Artifacts loaded successfully")


if __name__ == "__main__":
    load_saved_artifacts()
    # print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    print(get_estimated_price('1st Phase JP Nagar', 1000, 3, 3))
    print(get_estimated_price('Kalhalli', 1000, 2, 2))
    print(get_estimated_price('Ejipura', 1000, 2, 2))