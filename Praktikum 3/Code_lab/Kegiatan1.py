data = ["3 minggu 3 hari 7 jam 21 menit",
        "5 minggu 5 hari 8 jam 11 menit",
        "7 minggu 1 hari 5 jam 33 menit"]

def convert_to_minutes(weeks,days,hours,minutes): #Convert data dari Menit, Jam, Hari, Minggu
    return weeks * 7 *24 * 60 + days * 24 * 60 + hours * 60 + minutes

def curried_coverter(weeks): #Currying
    def inner_curried(days):
        def inner_inner_curried(hours):
            def final_curried(minutes):
                return convert_to_minutes(weeks,days,hours,minutes) #Convert ke dalam Menit
            return final_curried
        return inner_inner_curried
    return inner_curried

outputData = [] #Data displit dan diambil sesuai array imo
for item in data:
    parts = item.split()
    weeks = int(parts[0])
    days = int(parts[2])
    hours = int(parts[4])
    minutes = int(parts[6])

    coverted_values = curried_coverter(weeks)(days)(hours)(minutes)
    outputData.append(coverted_values)

print("OutputData = " ,outputData)
