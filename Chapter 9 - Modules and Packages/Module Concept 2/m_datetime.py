import os
import datetime as dt

os.system("cls")

now=dt.datetime.now()
print(now.strftime("%d/%m/%Y"))
print("Today month:",dt.date.today().month)

x=dt.datetime(day=31,month=3,year=2024)
y=dt.datetime(day=18,month=9,year=2024)
remain=y-x
print(remain)
print()
end=dt.datetime.now()
diff=end-now
print(diff)