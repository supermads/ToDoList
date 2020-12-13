def select_dates(potential_dates):
    matches = []
    for date in potential_dates:
        if date["age"] > 30:
            if "art" in date["hobbies"]:
                if date["city"] == "Berlin":
                    matches.append(date["name"])
    print('<{}>'.format(','.join(matches)))
select_dates([{"name": "Julia", "gender": "female", "age": 29,
                    "hobbies": ["jogging", "music"], "city": "Hamburg"},
                   {"name": "Sasha", "gender": "male", "age": 18,
                    "hobbies": ["rock music", "art"], "city": "Berlin"},
                   {"name": "Maria", "gender": "female", "age": 35,
                    "hobbies": ["art"], "city": "Berlin"},
                   {"name": "Daniel", "gender": "non-conforming", "age": 50,
                    "hobbies": ["boxing", "reading", "art"], "city": "Berlin"},
                   {"name": "John", "gender": "male", "age": 41,
                    "hobbies": ["reading", "alpinism", "museums"], "city": "Munich"}])
