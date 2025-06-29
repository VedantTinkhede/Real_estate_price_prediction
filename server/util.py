import json, pickle
import numpy as np

# global variables
__locations = None
__data_columns = None
__model = None




def get_estimated_price(location, sqft, bath, bhk):
    try:
        loc_index = __data_columns.index(location.lower())

    except:
        loc_index = -1    # if it doesn't find the index, set it to -1
    
    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)   # round it to 2 decimal places

def get_location_names():
    return __locations

def load_saved_artifacts():
    print("Loading saved artifacts...start")

    # reference to global variables
    global __locations
    global __data_columns
    global __model

    with open("./artifacts/columns.json", 'r') as f:
        __data_columns = json.load(f)["data_columns"]
        __locations = __data_columns[3:]   # locations in columns.json start from 3rd index 

    with open("./artifacts/banglore_model.pickle", "rb") as f:
        __model = pickle.load(f)

    print("Loading saved artifacts...done")




if __name__ == "__main__":
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st phase jp nagar', 1000, 2, 2))   # trial run