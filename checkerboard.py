def cb():
  lines = 8
  row = 0
  while(row <= lines):
    if(row % 2 == 0):
      print "* * * *"
    else:
      print "  * * * *"
    row += 1

cb()
