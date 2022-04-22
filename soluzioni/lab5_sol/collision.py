import math

# distanza tra due punti
def point_distance(x1, x2):
    return math.sqrt((x1[0] - x2[0])**2 + (x1[1] - x2[1])**2)

# controllo se un punto è su un segmento
def on_segment(x, s1, s2):
    return min(s1[0], s2[0]) <= x[0] <= max(s1[0], s2[0]) and min(s1[1], s2[1]) <= x[1] <= max(s1[1], s2[1])

# trova centro asteroide
def asteroid_center(canvas, asteroid):
    coords = canvas.coords(asteroid)
    x = int(round((coords[0] + coords[2])/2))
    y = int(round((coords[1] + coords[3])/2))
    return x, y    

# controlla se la navicella è stata colpita
def check_hit(canvas, ship, asteroid_set):
    # trovo segmenti lati navicella
    coords_ship = canvas.coords(ship)
    ship_segments = [coords_ship[:4], coords_ship[2:], coords_ship[0:2] + coords_ship[4:]]
    # per ogni asteroide su schermo
    for asteroid in asteroid_set:
        # ottengo informazioni su asteroide
        center = asteroid_center(canvas, asteroid)
        asteroid_coords = canvas.coords(asteroid)
        radius = abs(asteroid_coords[0] - asteroid_coords[2])/2
        # cerco collisione su ogni lato della navicella
        for segment in ship_segments:
            # retta passante per lato astronave y = mx + k
            m = (segment[3] - segment[1]) / (segment[2] - segment[0])
            if m != 0:
                k = segment[1] - m*segment[0]
                # retta per pendicolare lato astronave passante per centro asteroide y = m_p*x + k_p
                m_p = - 1/m
                k_p = center[1] - m_p*center[0]
                # punto intersezione rette
                x = -(k_p - k)/(m_p - m)
                y = k_p*x + m_p
            else:
                # punto intersezione se retta è orizzontale
                x = center[0]
                y = segment[1]
            # controllo se punto è sul lato astronave
            if on_segment((x,y), segment[0:2], segment[2:]):
                # se distanza tra centro asteroide e lato navicella è minore del raggio asteroide: collisione
                if point_distance((x,y), center) < radius:
                    return True
            else:
                # se distanza tra centro asteroide e estremi lato navicella minore raggio asteroide: collisione
                dist = min(point_distance(center, segment[0:2]), point_distance(center, segment[2:]))
                if dist < radius:
                    return True
    return False