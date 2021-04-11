def clocktest ():
    if current_week == site_week:
        year = current_year
    if current_week > site_week:
        someshit=abs(current_week-site_week)
        if someshit >= 180:
            year = current_year + 1
        else: 
            year = current_year
    if current_week < site_week:
        someshit=abs(current_week-site_week)
        if someshit <= 180:
            year = current_year
        else: 
            year = current_year + 1  