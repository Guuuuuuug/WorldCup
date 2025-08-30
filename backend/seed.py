from sqlmodel import Session, select
from database import engine
from worldcup.models import WorldCup

WORLD_CUP_DATA = [
    # 1930–1950 (your original entries kept as-is)
    {
        "year": 1930,
        "host": "Uruguay",
        "winner": "Uruguay",
        "runner_up": "Argentina",
        "third_place": "USA",
        "final_score": "4-2",
        "stadium": "Estadio Centenario",
        "referee": None,
        "attendance": None,
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/d/d5/Uruguay_national_football_team_1930.jpg",
        "continent": "South America"
    },
    {
        "year": 1934,
        "host": "Italy",
        "winner": "Italy",
        "runner_up": "Czechoslovakia",
        "third_place": "Germany",
        "final_score": "2-1 (a.e.t.)",
        "stadium": "Stadio Nazionale PNF",
        "referee": "Ivan Eklind (Sweden)",
        "attendance": 55000,
        "image_url": "https://i0.wp.com/thesefootballtimes.co/wp-content/uploads/2016/07/Italy-1934.jpg?w=1600&ssl=1",
        "continent": "Europe"
    },
    {
        "year": 1938,
        "host": "France",
        "winner": "Italy",
        "runner_up": "Hungary",
        "third_place": "Brazil",
        "final_score": "4-2",
        "stadium": "Stade Olympique de Colombes",
        "referee": "Georges Capdeville (France)",
        "attendance": 45000,
        "image_url": "https://i.guim.co.uk/img/media/e6624c2303117e78c6f6d83f752b0ac6fba96dba/0_147_1772_1063/master/1772.jpg?width=1900&dpr=2&s=none&crop=none",
        "continent": "Europe"
    },
    {
        "year": 1942,
        "host": "Canceled (World War II)",
        "winner": None,
        "runner_up": None,
        "third_place": None,
        "final_score": None,
        "stadium": None,
        "referee": None,
        "attendance": None,
        "image_url": "https://media.defense.gov/2020/Jul/27/2002465078/825/780/0/200319-O-ZZ999-001A.JPG",
        "continent": None
    },
    {
        "year": 1946,
        "host": "Canceled (World War II)",
        "winner": None,
        "runner_up": None,
        "third_place": None,
        "final_score": None,
        "stadium": None,
        "referee": None,
        "attendance": None,
        "image_url": "https://media.defense.gov/2020/Jul/27/2002465078/825/780/0/200319-O-ZZ999-001A.JPG",
        "continent": None
    },
    {
        "year": 1950,
        "host": "Brazil",
        "winner": "Uruguay",
        "runner_up": "Brazil",
        "third_place": "Sweden",
        "final_score": "2-1",
        "stadium": "Maracanã Stadium, Rio de Janeiro",
        "referee": "George Reader (England)",
        "attendance": 199854,
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/3/38/Urug1950.jpg",
        "continent": "South America"
    },

    # 1954 Switzerland
    {
        "year": 1954,
        "host": "Switzerland",
        "winner": "West Germany",
        "runner_up": "Hungary",
        "third_place": "Austria",
        "final_score": "3-2",
        "stadium": "Wankdorf Stadium, Bern",
        "referee": "William Ling (England)",
        "attendance": 65000,
        "image_url": "https://www.aljazeera.com/wp-content/uploads/2022/10/AP5407040111.jpg?resize=1800%2C1800",
        "continent": "Europe"
    },
    # 1958 Sweden
    {
        "year": 1958,
        "host": "Sweden",
        "winner": "Brazil",
        "runner_up": "Sweden",
        "third_place": "France",
        "final_score": "5-2",
        "stadium": "Råsunda Stadium, Solna",
        "referee": "Maurice Guigue (France)",
        "attendance": 49737,
        "image_url": "https://media.gettyimages.com/id/78971294/photo/brazil-team-at-1958-world-cup-finals.jpg?s=1024x1024&w=gi&k=20&c=CpyZhO8qFCNin7Cj-1258NuaeS5eIfuownSkSAD-QHE=",
        "continent": "Europe"
    },
    # 1962 Chile
    {
        "year": 1962,
        "host": "Chile",
        "winner": "Brazil",
        "runner_up": "Czechoslovakia",
        "third_place": "Chile",
        "final_score": "3-1",
        "stadium": "Estadio Nacional, Santiago",
        "referee": "Nikolay Latyshev (Soviet Union)",
        "attendance": 68679,
        "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRE7e0NdEe5qQ_AHSK0niGXLmHpaVjKy3I53w&s",
        "continent": "South America"
    },
    # 1966 England
    {
        "year": 1966,
        "host": "England",
        "winner": "England",
        "runner_up": "West Germany",
        "third_place": "Portugal",
        "final_score": "4-2 (a.e.t.)",
        "stadium": "Wembley Stadium, London",
        "referee": "Gottfried Dienst (Switzerland)",
        "attendance": 96924,
        "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRE05kPTo9o9uQmFZxlVsFqX8rhwRhoTrvL-Q&s",
        "continent": "Europe"
    },
    # 1970 Mexico
    {
        "year": 1970,
        "host": "Mexico",
        "winner": "Brazil",
        "runner_up": "Italy",
        "third_place": "West Germany",
        "final_score": "4-1",
        "stadium": "Estadio Azteca, Mexico City",
        "referee": "Rudi Glöckner (East Germany)",
        "attendance": 107412,
        "image_url": "https://www.americasquarterly.org/wp-content/uploads/2022/10/GettyImages-1227541383-scaled.jpg",
        "continent": "North America"
    },
    # 1974 West Germany
    {
        "year": 1974,
        "host": "West Germany",
        "winner": "West Germany",
        "runner_up": "Netherlands",
        "third_place": "Poland",
        "final_score": "2-1",
        "stadium": "Olympiastadion, Munich",
        "referee": "Jack Taylor (England)",
        "attendance": 75200,
        "image_url": "https://i.guim.co.uk/img/static/sys-images/Football/Pix/pictures/2008/09/19/germany74476.jpg?width=465&dpr=1&s=none&crop=none",
        "continent": "Europe"
    },
    # 1978 Argentina
    {
        "year": 1978,
        "host": "Argentina",
        "winner": "Argentina",
        "runner_up": "Netherlands",
        "third_place": "Brazil",
        "final_score": "3-1 (a.e.t.)",
        "stadium": "Estadio Monumental, Buenos Aires",
        "referee": "Sergio Gonella (Italy)",
        "attendance": 71483,
        "image_url": "https://static.toiimg.com/thumb/msid-64338300,imgsize-133547,width-400,resizemode-4/64338300.jpg",
        "continent": "South America"
    },
    # 1982 Spain
    {
        "year": 1982,
        "host": "Spain",
        "winner": "Italy",
        "runner_up": "West Germany",
        "third_place": "Poland",
        "final_score": "3-1",
        "stadium": "Santiago Bernabéu, Madrid",
        "referee": "Arnaldo Cézar Coelho (Brazil)",
        "attendance": 90000,
        "image_url": "https://sc0.blr1.digitaloceanspaces.com/large/881809-ttadtsawgq-1528802953.jpg",
        "continent": "Europe"
    },
    # 1986 Mexico
    {
        "year": 1986,
        "host": "Mexico",
        "winner": "Argentina",
        "runner_up": "West Germany",
        "third_place": "France",
        "final_score": "3-2",
        "stadium": "Estadio Azteca, Mexico City",
        "referee": "Romualdo Arppi Filho (Brazil)",
        "attendance": 114600,
        "image_url": "https://www.aljazeera.com/wp-content/uploads/2022/10/AP761775293235.jpg?resize=1800%2C1800",
        "continent": "North America"
    },
    # 1990 Italy
    {
        "year": 1990,
        "host": "Italy",
        "winner": "West Germany",
        "runner_up": "Argentina",
        "third_place": "Italy",
        "final_score": "1-0",
        "stadium": "Stadio Olimpico, Rome",
        "referee": "Edgardo Codesal (Mexico)",
        "attendance": 73603,
        "image_url": "https://images.daznservices.com/di/library/DAZN_News/e/67/germany-1990-world-cup-final_1nvuprw2mcgo21xjnpcinvscuw.jpg?t=2100839284",
        "continent": "Europe"
    },
    # 1994 USA
    {
        "year": 1994,
        "host": "United States",
        "winner": "Brazil",
        "runner_up": "Italy",
        "third_place": "Sweden",
        "final_score": "0-0 (3-2 pens)",
        "stadium": "Rose Bowl, Pasadena",
        "referee": "Sandor Puhl (Hungary)",
        "attendance": 94194,
        "image_url": "https://www.aljazeera.com/wp-content/uploads/2022/10/GettyImages-52917111.jpg?resize=1800%2C1271",
        "continent": "North America"
    },
    # 1998 France
    {
        "year": 1998,
        "host": "France",
        "winner": "France",
        "runner_up": "Brazil",
        "third_place": "Croatia",
        "final_score": "3-0",
        "stadium": "Stade de France, Saint-Denis",
        "referee": "Said Belqola (Morocco)",
        "attendance": 75000,
        "image_url": "https://i.cbc.ca/1.2176363.1382505571!/httpImage/image.jpg_gen/derivatives/original_1180/1998-francexl.jpg?im=",
        "continent": "Europe"
    },
    # 2002 Korea/Japan
    {
        "year": 2002,
        "host": "South Korea & Japan",
        "winner": "Brazil",
        "runner_up": "Germany",
        "third_place": "Turkey",
        "final_score": "2-0",
        "stadium": "International Stadium Yokohama",
        "referee": "Pierluigi Collina (Italy)",
        "attendance": 69029,
        "image_url": "https://i.ebayimg.com/images/g/ZNAAAOxydINSZR6z/s-l1200.jpg",
        "continent": "Asia"
    },
    # 2006 Germany
    {
        "year": 2006,
        "host": "Germany",
        "winner": "Italy",
        "runner_up": "France",
        "third_place": "Germany",
        "final_score": "1-1 (5-3 pens)",
        "stadium": "Olympiastadion, Berlin",
        "referee": "Horacio Elizondo (Argentina)",
        "attendance": 69000,
        "image_url": "https://www.aljazeera.com/wp-content/uploads/2022/10/000_DV90996.jpg?resize=1800%2C1800",
        "continent": "Europe"
    },
    # 2010 South Africa
    {
        "year": 2010,
        "host": "South Africa",
        "winner": "Spain",
        "runner_up": "Netherlands",
        "third_place": "Germany",
        "final_score": "1-0 (a.e.t.)",
        "stadium": "Soccer City, Johannesburg",
        "referee": "Howard Webb (England)",
        "attendance": 84490,
        "image_url": "https://static.independent.co.uk/s3fs-public/thumbnails/image/2020/06/15/11/spain-2010-world-cup-final.jpg",
        "continent": "Africa"
    },
    # 2014 Brazil
    {
        "year": 2014,
        "host": "Brazil",
        "winner": "Germany",
        "runner_up": "Argentina",
        "third_place": "Netherlands",
        "final_score": "1-0 (a.e.t.)",
        "stadium": "Maracanã, Rio de Janeiro",
        "referee": "Nicola Rizzoli (Italy)",
        "attendance": 74738,
        "image_url": "https://res.cloudinary.com/confirmed-web/image/upload/v1706273929/adidas-group/press-releases/2014/adidas_dfb_win_world_cup_2014_gofuxx.jpg",
        "continent": "South America"
    },
    # 2018 Russia
    {
        "year": 2018,
        "host": "Russia",
        "winner": "France",
        "runner_up": "Croatia",
        "third_place": "Belgium",
        "final_score": "4-2",
        "stadium": "Luzhniki Stadium, Moscow",
        "referee": "Néstor Pitana (Argentina)",
        "attendance": 78011,
        "image_url": "https://images.mlssoccer.com/image/private/t_q-best/mls-lag-prd/jua6trkfwsccfydfm02f.jpg",
        "continent": "Europe"
    },
    # 2022 Qatar
    {
        "year": 2022,
        "host": "Qatar",
        "winner": "Argentina",
        "runner_up": "France",
        "third_place": "Croatia",
        "final_score": "3-3 (4-2 pens)",
        "stadium": "Lusail Iconic Stadium, Lusail",
        "referee": "Szymon Marciniak (Poland)",
        "attendance": 88966,
        "image_url": "https://media.cnn.com/api/v1/images/stellar/prod/221219105607-messi-crowd-world-cup-121822.jpg?q=w_3000,c_fill",
        "continent": "Asia"
    },
]

def seed_worldcups():
    inserted = 0
    updated = 0

    with Session(engine) as session:
        for data in WORLD_CUP_DATA:
            
            existing = session.exec(
                select(WorldCup).where(WorldCup.year == data["year"])
            ).first()

            if existing:
                # upsert: update fields if changed
                changed = False
                for k, v in data.items():
                    if getattr(existing, k) != v:
                        setattr(existing, k, v)
                        changed = True
                if changed:
                    updated += 1
            else:
                session.add(WorldCup(**data))
                inserted += 1

        session.commit()

    print(f"Seed complete. Inserted: {inserted}, Updated: {updated}")

if __name__ == "__main__":
    seed_worldcups()
