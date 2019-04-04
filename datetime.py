
from datetime import datetime
datetime(year=2015, month=7, day=4).strftime("%A")

date = datetime.now()

date.strftime("%A")

datetime.strptime(format(date),"%Y-%m-%d %H:%M:%S.%f")

datetime.strptime(format(date),"%Y-%m-%d %H:%M:%S.%f").strftime("%A")



currenttime = datetime.now()
datetime.timestamp(currenttime)

timestamp = datetime.timestamp(currenttime)

date = datetime.fromtimestamp(1554346894)


ts = timestamp#int("1284101485")

print(datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))

print(date.hour)
print(date.date())
print(date.minute)
print(date.second)


print(" %s:%s:%s" % (date.hour, date.minute,date.second))

print("Created at : %s" % (date.date()))


from dateutil.parser import parse

date_array = [  
    '2018-06-29 08:15:27.243860',
    'Jun 28 2018  7:40AM',
    'Jun 28 2018 at 7:40AM',
    'September 18, 2017, 22:19:55',
    'Sun, 05/12/1999, 12:30PM',
    'Mon, 21 March, 2015',
    '2018-03-12T10:12:45Z',
    '2018-06-29 17:08:00.586525+00:00',
    '2018-06-29 17:08:00.586525+05:00',
    'Tuesday , 6th September, 2017 at 4:30pm',
    'Tue 6th September, 2017 at 4:30pm'
]


for i in date_array:
    date = parse(i)
    #print(date.strftime("%A"))
    print(date)
    #print(date.time())

vsl = map(lambda x : parse(x).time(), date_array)
list(vsl)
