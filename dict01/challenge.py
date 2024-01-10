challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]


trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]


nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]

# 1
    c1 = challenge[2][1]
    c2 = challenge[2][0]
    c3 = challenge[3]

    print(f"My {c1}! The {c2} do {c3}!" 

#2
    t1 = trial[2]["goggles"]
    t2 = trial[2]["eyes"]
    t3 = trial[-1]
