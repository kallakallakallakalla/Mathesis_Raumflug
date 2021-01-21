import math
from matplotlib import pyplot as plt
from matplotlib.patches import Ellipse
import numpy as np




def Hohmann_Transfer_(R1, R2, P1, P2):
    pi = math.pi
    GM = 1.327 * 10 ** 11
    a_transfer = (R1 + R2) / 2  # große halbachse
    p_transfer = math.sqrt(4 * pi ** 2 / GM)  # l
    v1 = (2 * pi * R1) / P1
    v2 = (2 * pi * R2) / P2
    v_periapsis = (2 * pi * a_transfer / p_transfer) * math.sqrt((2 * a_transfer / R1) - 1)
    delta_v1 = v_periapsis - v1
    v_apoapsis = (2 * pi * a_transfer / p_transfer) * math.sqrt((2 * a_transfer / R2) - 1)
    delta_v2 = v2 - v_apoapsis
    TOF = 1 / 2 * p_transfer  # Time of flight
    return a_transfer, p_transfer, delta_v1, delta_v2




def draw_ell():

    ells = Ellipse(xy= (0,0), width=5, height=2.5, fill=False)

    fig, ax = plt.subplots(subplot_kw={'aspect': 'equal'})

    ax.add_artist(ells)


    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)

    plt.show()


draw_ell()