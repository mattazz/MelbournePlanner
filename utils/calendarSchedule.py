from datetime import datetime


def getUserDate():
    userArrivalDate = input("When are you planning to go? (ex. mm/dd/yy)")
    userLeavingDate = input("When are you planning to leave? (ex. mm/dd/yy)")

    convertedArrival = datetime.strptime(userArrivalDate, "%y/%m/%d")
    convertedLeaving = datetime.strptime(userLeavingDate, "%y/%m/%d")

    return (convertedArrival, convertedLeaving)


result = getUserDate()

print(result)
