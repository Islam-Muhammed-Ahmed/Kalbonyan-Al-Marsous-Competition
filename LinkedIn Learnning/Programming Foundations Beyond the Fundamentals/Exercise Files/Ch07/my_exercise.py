def check_temp(temp):
    if  temp < 15:
        print('Bring a jacket')
    elif temp > 25 and temp <= 35:
        print('Pack a jacket')
    elif temp > 35:
        print('Leave the jacket at home')

check_temp(12)
check_temp(34)
check_temp(40)

#solve challenge
def plant_recommendation(care):
    if care == "low":
        print("aloe")
    elif care == "medium":
        print("pothos")
    elif care == "high":
        print("orchid")
plant_recommendation("low")
plant_recommendation("medium")
plant_recommendation("high")