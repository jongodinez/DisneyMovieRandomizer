import random
import json

disneyMovies = json.loads(open('movies.json').read())

movie = random.choice(disneyMovies)

print movie
