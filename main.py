print ("== Time Converter ==")
print ("")
print ("This would convert between seconds, minutes, hours, days, months and years")
print (" ")
time = input("Which would you like to convert to: seconds, minutes, hours, days, months or years?  ")
print (" ")
expected_time = input("Which you would like to convert to: seconds, minutes, hours, days, months or years?  ")
print (" ")
initial_unit = float(input("Input the duration:  "))
print (" ")

#this portion converts seconds to other units
if time == "seconds" and expected_time == "seconds":
  print (initial_unit, "seconds")
elif time == "seconds" and expected_time == "minutes":
  print (initial_unit / 60, "minutes")
elif time == "seconds" and expected_time == "hours":
  print (initial_unit / 3600, "hours")
elif time == "seconds" and expected_time == "days":
  print (initial_unit / 86400, "days")
elif time == "seconds" and expected_time == "months":
  print (initial_unit / 2629746, "months")
elif time == "seconds" and expected_time == "years":
  if initial_unit % 4 == 0 and (initial_unit % 100 != 0 or initial_unit % 400 == 0):
      print(initial_unit / 31622400, "years")
  else:
      print(initial_unit / 31536000, "years")
#this portion converts minutes to other units
elif time == "minutes" and expected_time == "seconds":
  print (initial_unit * 60, "seconds")
elif time == "minutes" and expected_time == "minutes":
  print (initial_unit, "minutes")
elif time == "minutes" and expected_time == "hours":
  print (initial_unit / 60, "hours")
elif time == "minutes" and expected_time == "days":
  print (initial_unit / 1440, "days")
elif time == "minutes" and expected_time == "months":
  print (initial_unit / 43800, "months")
elif time == "minutes" and expected_time == "years":
  if initial_unit % 4 == 0 and (initial_unit % 100 != 0 or initial_unit % 400 == 0):
      print(initial_unit / 525600, "years")
  else:
      print(initial_unit / 527000, "years")
#this portion converts hours to other units
elif time == "hours" and expected_time == "seconds":
  print (initial_unit * 3600, "seconds")
elif time == "hours" and expected_time == "minutes":
  print (initial_unit * 60, "minutes")
elif time == "hours" and expected_time == "hours":
  print (initial_unit, "hours")
elif time == "hours" and expected_time == "days":
  print (initial_unit / 1440, "days")
elif time == "hours" and expected_time == "months":
  print (initial_unit / 730, "months")
elif time == "hours" and expected_time == "years":
  if initial_unit % 4 == 0 and (initial_unit % 100 != 0 or initial_unit % 400 == 0):
      print(initial_unit / 8760, "years")
  else:
      print(initial_unit / 8784, "years")
#this portion converts days to other units
elif time == "days" and expected_time == "seconds":
  print (initial_unit * 86400, "seconds")
elif time == "days" and expected_time == "minutes":
  print (initial_unit * 1440, "minutes")
elif time == "days" and expected_time == "hours":
  print (initial_unit * 24, "hours")
elif time == "days" and expected_time == "days":
  print (initial_unit, "days")
elif time == "days" and expected_time == "months":
  print (initial_unit / 30.417, "months")
elif time == "days" and expected_time == "years":
  if initial_unit % 4 == 0 and (initial_unit % 100 != 0 or initial_unit % 400 == 0):
      print(initial_unit / 365, "years")
  else:
      print(initial_unit / 366, "years")
#this portion converts months to other units
elif time == "months" and expected_time == "seconds":
  print (initial_unit * 2629746, "seconds")
elif time == "months" and expected_time == "minutes":
  print (initial_unit * 43800, "minutes")
elif time == "months" and expected_time == "hours":
  print (initial_unit * 730, "hours")
elif time == "months" and expected_time == "days":
  print (initial_unit * 30.417, "days")
elif time == "months" and expected_time == "months":
  print (initial_unit, "months")
elif time == "months" and expected_time == "years":
  if initial_unit % 4 == 0 and (initial_unit % 100 != 0 or initial_unit % 400 == 0):
      print(initial_unit / 12, "years")
  else:
      print(initial_unit / 12.033, "years")
#this portion converts years to other units
elif time == "years" and expected_time == "seconds":
  print (initial_unit * 31556952, "seconds")
elif time == "years" and expected_time == "minutes":
  print (initial_unit * 525600, "minutes")
elif time == "years" and expected_time == "hours":
  print (initial_unit * 8760, "hours")
elif time == "years" and expected_time == "days":
  print (initial_unit * 365, "days")
elif time == "years" and expected_time == "months":
  print (initial_unit * 12, "months")
elif time == "years" and expected_time == "years":
  print(initial_unit, "years")
else:
  print ("Input correct option")
