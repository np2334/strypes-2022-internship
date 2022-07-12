def gas_stations(distance, tank_size, stations):
    shoretst_list_of_stations = []

    available_distance = tank_size
    last_station = 0
    for i in range(0, len(stations)):
        available_distance -= (stations[i] - last_station)
        distance_left = distance - stations[i]

        # ако минем бензиностанцията, но няма нужда да зареждаме, защото горивото ни стига до дестинацията
        if available_distance >= distance_left:
            break

        # ако не сме стигнали последната бензиностанция
        if i + 1 < len(stations):
             # ако не можем да стигнем до следващата бензиностанция
             if available_distance < stations[i + 1] - stations[i]:
                # добавям текущата бензиностанция 
                shoretst_list_of_stations.append(stations[i])
                available_distance = tank_size
        # ако сме на последната бензиностанция, но не ни стига горивото до дестинацията пак трябва да заредим
        elif available_distance < distance_left:
                shoretst_list_of_stations.append(stations[i])
                available_distance = tank_size

        last_station = stations[i]
    return shoretst_list_of_stations
        

print(gas_stations(90, 90, [50, 80, 140, 180, 220, 290]))
print(gas_stations(100, 90, [50, 80, 140, 180, 220, 290]))
print(gas_stations(320, 90, [50, 80, 140, 180, 220, 290]))
print(gas_stations(390, 80, [70, 90, 140, 210, 240, 280, 350]))