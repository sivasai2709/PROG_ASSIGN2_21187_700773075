import pandas as pd
from db import driver

DATA_PATH = r"C:\Users\USER\Desktop\PROG_ASSIGN2_5600_700773075\StarWars Dataset"


# define a function to clean values (handle NaN, "NA", "None", etc.)
def clean(value):
    if pd.isna(value):
        return None
    if str(value).strip().lower() in ["na", "n/a", "none", ""]:
        return None
    return value


# define a function to load characters from the CSV file and create nodes in Neo4j
def load_characters():
    df = pd.read_csv(f"{DATA_PATH}\\characters.csv")

    query = """
    MERGE (c:Characters {name: $name})
    SET c.height = $height,
        c.mass = $mass,
        c.hair_color = $hair_color,
        c.skin_color = $skin_color,
        c.eye_color = $eye_color,
        c.birth_year = $birth_year,
        c.gender = $gender
    """

    with driver.session() as session:
        for _, r in df.iterrows():

            name = clean(r["name"])
            if name is None:
                continue

            session.run(query, {
                "name": name,
                "height": clean(r["height"]),
                "mass": clean(r["mass"]),
                "hair_color": clean(r["hair_color"]),
                "skin_color": clean(r["skin_color"]),
                "eye_color": clean(r["eye_color"]),
                "birth_year": clean(r["birth_year"]),
                "gender": clean(r["gender"])
            })


# load planets from the CSV file and create nodes in Neo4j
def load_planets():
    df = pd.read_csv(f"{DATA_PATH}\\planets.csv")

    query = """
    MERGE (p:Planets {name: $name})
    SET p.climate = $climate,
        p.terrain = $terrain,
        p.population = $population,
        p.gravity = $gravity
    """

    with driver.session() as session:
        for _, r in df.iterrows():

            name = clean(r["name"])
            if name is None:
                continue

            session.run(query, {
                "name": name,
                "climate": clean(r["climate"]),
                "terrain": clean(r["terrain"]),
                "population": clean(r["population"]),
                "gravity": clean(r["gravity"])
            })


# load species from the CSV file and create nodes in Neo4j
def load_species():
    df = pd.read_csv(f"{DATA_PATH}\\species.csv")

    query = """
    MERGE (s:Species {name: $name})
    SET s.classification = $classification,
        s.language = $language,
        s.average_height = $average_height
    """

    with driver.session() as session:
        for _, r in df.iterrows():

            name = clean(r["name"])
            if name is None:
                continue

            session.run(query, {
                "name": name,
                "classification": clean(r["classification"]),
                "language": clean(r["language"]),
                "average_height": clean(r["average_height"])
            })


# load films from the CSV file and create nodes in Neo4j
def load_films():
    df = pd.read_csv(f"{DATA_PATH}\\films.csv")

    query = """
    MERGE (f:Films {title: $title})
    SET f.episode_id = $episode_id,
        f.director = $director,
        f.release_date = $release_date
    """

    with driver.session() as session:
        for _, r in df.iterrows():

            title = clean(r["title"])
            if title is None:
                continue

            session.run(query, {
                "title": title,
                "episode_id": clean(r["episode_id"]),
                "director": clean(r["director"]),
                "release_date": clean(r["release_date"])
            })


# load starships from the CSV file and create nodes in Neo4j
def load_starships():
    df = pd.read_csv(f"{DATA_PATH}\\starships.csv")

    query = """
    MERGE (s:Starships {name: $name})
    SET s.model = $model,
        s.manufacturer = $manufacturer,
        s.starship_class = $starship_class
    """

    with driver.session() as session:
        for _, r in df.iterrows():

            name = clean(r["name"])
            if name is None:
                continue

            session.run(query, {
                "name": name,
                "model": clean(r["model"]),
                "manufacturer": clean(r["manufacturer"]),
                "starship_class": clean(r["starship_class"])
            })


# define a function to create relationships between characters, planets, and species
def create_relationships():
    with driver.session() as session:

        session.run("""
        MATCH (c:Characters), (p:Planets)
        WHERE c.homeworld = p.name
        MERGE (c)-[:FROM]->(p)
        """)

        session.run("""
        MATCH (c:Characters), (s:Species)
        WHERE c.species = s.name
        MERGE (c)-[:IDENTIFIES_AS]->(s)
        """)

# main function to load all data and create relationships
if __name__ == "__main__":
    load_characters()
    load_planets()
    load_species()
    load_films()
    load_starships()
    create_relationships()

    print("FULL STAR WARS GRAPH LOADED SUCCESSFULLY")