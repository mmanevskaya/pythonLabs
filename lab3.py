mal = input()
if 'ing' in mal:
   mal = mal+"ly"
   print(mal)
elif len(mal) >= 3:
   mal = mal+"ing"
   print(mal)
else:
   print(mal)
