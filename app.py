from flask import Flask,render_template,jsonify
import requests
app = Flask (__name__)

response = requests.get("https://api.npoint.io/f26432e9e880999eeb1b") 
coordinates =[]
if response.status_code==200:
    coordinates = [feature["geometry"]["coordinates"] for feature in response.json()["features"]]
    size=len(coordinates)
    print(size)
def are_coordinates_near(coord1, coord2, threshold):
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    
    lat_diff = abs(lat1 - lat2)
    lon_diff = abs(lon1 - lon2)
    
    return lat_diff < threshold and lon_diff < threshold


threshold = 0.01  # Adjust this threshold as needed

near_coordinates = []
far_coordinates = []

for i, coord1 in enumerate(coordinates):
    is_near = False
    for j, coord2 in enumerate(coordinates):
        if i != j and are_coordinates_near(coord1, coord2, threshold):
            is_near = True
            break
    if is_near:
        near_coordinates.append(coord1)
    else:
        far_coordinates.append(coord1)

print("Near Coordinates:", near_coordinates)





@app.route('/location', methods=['GET'])
def get_location():
    return jsonify(coordinates)   

@app.route('/') 
def index():


    
        
    return render_template("index.html",near_coordinates=near_coordinates, far_coordinates=far_coordinates)


if __name__ == '__main__':
    app.run(debug=True)