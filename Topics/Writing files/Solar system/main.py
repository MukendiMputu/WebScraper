planets = [
    "Mercury",
    "Venus",
    "Earth",
    "Mars",
    "Jupiter",
    "Saturn",
    "Uranus",
    "Neptune"
]
planet_file = open('planets.txt', 'w', encoding='utf-8')

for planet in planets:
    planet_file.write(planet + "\n")
planet_file.close()
