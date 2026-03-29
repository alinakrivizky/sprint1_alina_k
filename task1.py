
string = '1h 45m,360s,25m,30m 120s,2h 60s'
sum_min=0
dates = string.split(',')
for d in dates:
  elements = d.split()
  for e in elements:
     if 'h' in e:
      hour = int(e.replace('h', ''))
      sum_min+=hour*60
     elif 'm' in e:
      minute = int(e.replace('m', ''))
      sum_min+=minute
     elif 's' in e:
      second = int(e.replace('s', '' ))
      sum_min+=second // 60
print(sum_min)


