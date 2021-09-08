import random
last = 13
rnd = random.randint(0, last)
def primary():
  # print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  print(quotes[rnd])
  print(quotes[3])
  print ("prueba python")
  width = 20
  height = 5 * 9
  print (width * height)
if __name__== "__main__":
  primary()
