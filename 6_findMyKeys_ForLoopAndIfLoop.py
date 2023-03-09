key_location = "Study Room"
locations = ["garage", "Living Room", "Bedroom", "Study Room", "Closet", "Kitchen Counter"]

for i in locations:
    if i == key_location:
        print("Yayy!! I found my keys in ", i)
        break
    else:
        print("OMG!! I can't find my keys in ", i)