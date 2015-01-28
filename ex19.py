def cheese_and_crackers(cheese_count, boxes_of_crackers):
  print "You have %d cheeses!" % cheese_count
  print "You have %d boxes of crackers." % boxes_of_crackers
  print "Man that's enough for a party!"
  print "Get a blanket.\n"

print "We can just give the function numbers directly"
cheese_and_crackers(20, 30)

print "OR, we can use variables from our script"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

#My own function

def beauty_parlor(shampoo_cost, cut_cost, dye_cost):
  print "%d is the cost for only a wash." % shampoo_cost
  print "And for a haircut, that will cost %d" % cut_cost
  print "If you want your hair dyed, that will be %d." % dye_cost
  print "And the entire cost for all services is %d." % (shampoo_cost + cut_cost + dye_cost)

beauty_parlor(20, 30, 40)

special_shampoo = 80
long_cut = 100
highlights = 250

beauty_parlor(special_shampoo, long_cut, highlights)
