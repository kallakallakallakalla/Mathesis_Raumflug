from math import sqrt
import plotly.express as px
from astropy.time import Time
from astroquery.jplhorizons import Horizons
from scipy.constants import G

objects = []
mass = [3.302E23, 48.685E23, 5.97219E24, 6.4171E23, 1898E24, 5.6834E26, 86.813E24, 102.413E24, 7.348E22,
        10]  # Massen der Objekte
names = ["Merkur", "Venus", "Erde", "Mars", "Jupiter", "Saturn", "Uranus", "Neptun", "Mond",
         "Tesla-Starman"]  # Namen der Objekte
sizes = [7, 15, 15, 10, 30, 28, 20, 18, 5, 1]  # Grössen der Objekte - nicht Verhältnismäßig
time = "2020-02-10"  # Start der Simulation
data = {"x": [],  # Speicherort der Frame
        "y": [],
        "z": [],
        "size": [],
        "Object": [],
        "date": []}


def gravitation(obj):
    a = [0, 0, 0]
    for obj_ in objects:  # Einfluss aller anderen Objekte wird berechnet
        if obj != obj_:
            nvector_l = sqrt(
                (obj_.pos[0] - obj.pos[0]) ** 2 + (obj_.pos[1] - obj.pos[1]) ** 2 + (obj_.pos[2] - obj.pos[2]) ** 2)
            nvector = ((obj_.pos[0] - obj.pos[0]) / nvector_l, (obj_.pos[1] - obj.pos[1]) / nvector_l,
                       (obj_.pos[2] - obj.pos[2]) / nvector_l)
            acc = G * (obj_.m / (nvector_l ** 2))
            a[0] += acc * nvector[0]
            a[1] += acc * nvector[1]  # Normalenvektor wird berechnet und mit der Beschleunigung multipliziert
            a[2] += acc * nvector[2]

    return a  # nach Durchlauf aller Objekte wird der Beschleunigungsvektor zurückgegeben


class object():
    def __init__(self, size, name, id, m, x, y, z, vx=0, vy=0, vz=0):
        global objects
        self.size = size
        self.id = id
        self.name = name
        self.m = m
        self.pos = [x * 149597900000, y * 149597900000, z * 149597900000]  # AU in m
        self.v = [vx * 1731460, vy * 1731460, vz * 1731460]  # AU/d in m/s

    def update(self):
        dt = 100
        a = gravitation(self)
        self.v[0] += dt * a[0]
        self.v[1] += dt * a[1]
        self.v[2] += dt * a[2]
        self.pos[0] += dt * self.v[0]
        self.pos[1] += dt * self.v[1]
        self.pos[2] += dt * self.v[2]


def import_objects():
    i = 0
    for id_ in [1, 2, 3, 4, 5, 6, 7, 8, 301, -143205]:  # ids Horizon Objekte
        obj = Horizons(id=id_, location="@sun", epochs=Time(time).jd, id_type='id').vectors()
        objects.append(
            object(sizes[i],
                   names[i], id_, mass[i], obj["x"][0], obj["y"][0], obj["z"][0], obj["vx"][0],
                   obj["vy"][0], obj["vz"][0]))
        i += 1
    objects.append(object(80, "Sun", 0, 1988500E24, 0, 0, 0))
    # objects.append(object(5, "Satelit", 11, 10, objects[2].pos[0] + 0.01, objects[2].pos[1] + 0.01, objects[2].pos[2] + 0.01, objects[2].v[0], objects[2].v[1], objects[2].v[2]))
    # hier lassen sich weitere beliebige Objekte hinzufügen

def get_data():
    i = 1
    j = 365

    step = 0  # Tag:86400 Sekunden, pro tag 864 Updates--> Beschleunigung mit Faktor 100
    steps = 864
    while i <= j:
        print("calc frame :", str(i))
        for obj in objects:
            # geht objekte durch und ruft update-funktion auf
            data["x"].append(obj.pos[0] / 149597900000)
            data["y"].append(obj.pos[1] / 149597900000)  # speichert objektvariablen in data in AU
            data["z"].append(obj.pos[2] / 149597900000)
            data["size"].append(obj.size)
            data["Object"].append(obj.name)
            data["date"].append(i)
        while step < steps:
            for obj_ in objects:
                obj_.update()

            step += 1
        step = 0
        i += 1


def plot():
    size = 30
    fig = px.scatter_3d(data, x="x", y="y", z="z",
                        color="Object",
                        size="size",
                        range_x=[-size, size],
                        range_y=[-size, size],
                        range_z=[-size, size],
                        animation_group="Object",
                        animation_frame="date",
                        size_max=100,
                        text="Object",
                        color_discrete_map={"Sonne": "#fcf695",
                                            "Merkur": "#465b73", "Venus": "#ffffa0", "Erde": "#567ace",
                                            "Mars": "#ff8000", "Jupiter": "#c39595",
                                            "Saturn": "#cace88", "Uranus": "#b7d3e9", "Neptun": "#567ace",
                                            "Tesla-Starman": "#fff"},
                        opacity=0.9,
                        hover_name="Object",
                        hover_data={"date": False, "size": False}
                        )




    fig.update_layout(margin_l=10, margin_r=10, margin_t=10, paper_bgcolor="#333333",
                      margin_b=10,
                      font_family="Times New Roman",
                      font_color="#fff",
                      title_font_family="Arial",
                      title_font_color="#fff",
                      title_font_size=24,
                      legend_title_font_color="#fff",
                      title = {
                          'text': "Raumflug",
                          'y': 0.95,
                          'x': 0.1,
                          'xanchor': 'center',
                          'yanchor': 'top'})





    fig.update_scenes(bgcolor="#333333",
                      aspectmode="manual",
                      xaxis_showbackground=False, xaxis_color="#fff", xaxis_tickfont_family="Courier New",
                      xaxis_ticksuffix="AU", xaxis_zerolinewidth=3,
                      yaxis_showbackground=False, yaxis_color="#fff", yaxis_tickfont_family="Courier New",
                      yaxis_ticksuffix="AU", yaxis_zerolinewidth=3,
                      zaxis_showbackground=False, zaxis_color="#fff", zaxis_tickfont_family="Courier New",
                      zaxis_ticksuffix="AU", zaxis_zerolinewidth=3

                      )

    fig.show()


import_objects()
get_data()
plot()