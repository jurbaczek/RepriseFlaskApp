from flask import Flask, escape, request, render_template
from bs4 import BeautifulSoup

app = Flask(__name__)


@app.route('/')
def form():
    return render_template('form.html')


def get_image_and_id_coord_pairs(map_code):
    # print(map_code)
    img_src = map_code.split('  <map name="image-map">')[0]
    area_tags = map_code.split('     <area target="" ')[1:]
    id_coords_dict = {}
    for area in area_tags:
        id = area.split('title="')[1].split('"')[0]
        coords = [int(i) for i in area.split('coords="')[1].split('"')[0].split(',')]
        id_coords_dict[id] = coords
    return img_src, id_coords_dict

@app.route('/data', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        form_data = request.form
        map_code = request.form.getlist('map')[0]
        print(map_code)
        image, clickables = get_image_and_id_coord_pairs(map_code=map_code)
        print(image)

        return render_template('image_div_map.html', image = image, divs = clickables)


app.run(host="localhost", port=8000, debug=True)

# def translateMap():
#     mapSoup = BeautifulSoup("./Templates/map.html")
#     mapText = mapSoup.get_text()
#     print(mapText)


