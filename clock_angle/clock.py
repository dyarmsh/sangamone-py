# 0900 to 2055
def clock_angle(startTime,endTime):

    fullRevAngle = 360
    
    angle5Min = (5/60) * fullRevAngle
    fullHourAngle = angle5Min

    angle5MinHour = (5/60) * fullHourAngle

    startHour = int(startTime[0:2])
    endHour = int(endTime[0:2])

    startAngle = 90
    for hour in range(startHour,endHour+1):
        count = 0
        for min in range(0,60,5):
            angle = startAngle + (angle5Min * count) - (angle5MinHour * count)
            angle = angle%360
            info = str(hour) + ":" + str(min).zfill(2) + " = " + str(angle) + " degrees"
            print(info)
            count += 1

        print()
        startAngle -= 30



    # for i in range(startHour, endHour+1):
    #     for j in range(0, 60):
    #         info = str(i) + ":" + str(j) + "-" + angle


clock_angle("0900","2055")
    