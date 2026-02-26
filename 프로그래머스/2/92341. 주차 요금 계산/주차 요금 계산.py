
def solution(fees, records):
    d = {}
    cal = {}
    check = []
    for data in records:
        time, num, wh = data.split(' ')
        hh, mm = time.split(':')
        
        total = int(hh)*60 + int(mm)
        if wh == "IN":
            cal[num] = total
            check.append(num)
        if wh == "OUT":
            cal[num] = total - cal.get(num, 0)
            d[num] = d.get(num, 0) + cal[num]
            check.remove(num)
    
    for a in check:
        stay = 60*23 + 59 - cal[a]
        d[a] = d.get(a, 0) + stay
    
    sorted_car_num = sorted(d.keys())
    answer = []
    for n in sorted_car_num:
        timea, feea, timeb, feeb = fees
        if d[n] <= timea:
            d[n] = feea
        else:
            if (d[n] - timea)%timeb == 0:
                d[n] = feea + feeb*(d[n] - timea)//timeb
            else:
                d[n] = feea + feeb*((d[n] - timea)//timeb + 1)
        answer.append(d[n])
    return answer