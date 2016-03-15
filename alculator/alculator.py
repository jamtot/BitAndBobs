# -*- coding: utf-8 -*-

def formatted(f): return format(f, '.2f').rstrip('0').rstrip('.')

class Drink(object):
    def __init__(self,percentage,mil_amount,cost=0.0,name="Your drink"):
        self.percentage = percentage
        self.mil_amount = mil_amount
        self.cost = cost
        self.name = name
        self.units = (self.percentage*self.mil_amount)/1000.0
        self.cost_per_unit = self.cost / self.units
        self.alc_content, self.cent_content, self.mil_of_alc = self.get_content()
          
    def get_content(self):
        # get the alcoholic content
        alc_content = (self.mil_amount/100.0)*self.percentage

        if self.cost > 0: 
            # alcohol per cent
            cent_content = alc_content/(self.cost*100.) # cost in euro
            # the price per mil of alcohol
            mil_of_alc = (self.cost*100.)/alc_content

            return alc_content, cent_content, mil_of_alc

    def describe(self):
        if self.cost > 0:
            print "At €%s,"%formatted(self.cost),
        print "%.fml of %s at %s%% contains %sml of alcohol."%(
            self.mil_amount, self.name, formatted(self.percentage), formatted(self.alc_content))
        if self.cost > 0:
            print "You get %sml of alcohol per every cent." % (
                formatted(self.cent_content))
            print "It is %s cent per mil of alcohol." % formatted(self.mil_of_alc)
        print "Contains %s units, €%s per unit."% (
            formatted(self.units), formatted(self.cost_per_unit) )
            
    def compare(self, other):
        # comparisons using a couple of different methods
        print "Comparing %s and %s." % (self.name, other.name)

        print "-\tBetter bang for buck:",
        winner = self if self.comparison(
                self.cost_per_unit, other.cost_per_unit, False) else other   
        print winner.name+" - Cost per unit €%.2f" % winner.cost_per_unit
        
        print "-\tCheaper overall:",
        if self.cost<other.cost:
            print self.name+" - €%s"%formatted(self.cost)    
        else: print other.name+" - €%s"%formatted(other.cost)
  
        print "-\tHigher alcoholic content:",
        winner = self if self.comparison(
                self.percentage, other.percentage) else other   
        print winner.name+" - %s%%" % formatted(winner.percentage)

        print "-\tMore volume:",
        winner = self if self.comparison(
                self.mil_amount, other.mil_amount) else other   
        print winner.name+" - %sml" % formatted(winner.mil_amount)

        print "-\tPrice per ml of alcohol:",
        winner = self.compare_attr(other, "mil_of_alc", False)
        print "%s - %sc per ml" % (winner.name, formatted( winner.mil_of_alc))
        
    def comparison(self, d1, d2, higher_wins=True):
        if d1==d2: 
            print "Same for both, returning first -",
            return True      
        elif (d1>d2) == higher_wins:
            return True
        else:
            return False
 
    def compare_attr(self, other, var, higher_wins=True):
        if getattr(self,var)==getattr(other,var): print "Same."        
        elif (getattr(self,var)>getattr(other,var)) == higher_wins:
            return self
        else:
            return other      

if __name__ == "__main__":
    print
    jack = Drink(40, 700, 25.00, "Jack Daniel's (700ml)")
    jack.describe()
    print "---------"
    capn = Drink(35, 1000, 28.00, "Captain Morgan (1000ml)")
    capn.describe()
    print "---------"
    capn2 = Drink(35, 350, 12.00, "Captain Morgan (350ml)")
    capn2.describe()
    print "---------"
    miller = Drink(4.3, 24*500, 24.00, "Miller 24pk (4000ml)")
    miller.describe()
    print "---------"
    # a promotion the local tesco had while I was in college
    bush = Drink(40, 350, 5.00, "Bushmills (350ml)")
    bush.describe()
    print "---------"
    print "Some comparisons."
    bush.compare(capn2)
    print "---------"
    jack.compare(capn)
