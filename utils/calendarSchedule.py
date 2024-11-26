from datetime import datetime


def getUserDate():
    userArrivalDate = input("When are you planning to go? (ex. mm/dd/yy)")
    userLeavingDate = input("When are you planning to leave? (ex. mm/dd/yy)")

    convertedArrival = datetime.strptime(userArrivalDate, "%m/%d/%y")
    convertedLeaving = datetime.strptime(userLeavingDate, "%m/%d/%y")

    return (convertedArrival, convertedLeaving)


result = getUserDate()

print(result)
