import datetime as dt
format = '%Y-%m-%dt%H:%M:%S'
t1 = dt.datetime.strptime('2008-10-12T14:45:52', format)
print('Day' + str(t1.day))
print('Month' + str(t1.minute))
print('Minute' + str(t1.second))

# Define todays date and time
t2 = dt.datetime.now()
diff = t2 - t1
print(' How many days difference?' + str(diff.day))
