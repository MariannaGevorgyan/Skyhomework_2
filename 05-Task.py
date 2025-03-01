def month_to_season(num):

    if num  in [12,1,2]:
        return "Winter"
    elif num in [3,4,5]:
       return "Spring"
    elif  num in  [6,7,8]:
        return "Summer"
    elif num in [9,10,11]:
        return "Autumn"


season = int(input("Введите номер месяца : "))
print(month_to_season(season))
