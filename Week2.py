#This string is talking about what kinds of people there are
x = "There are %d types of people." %10\
# This is a string for the first type of person
bianary = "bianary"
# this is the string for the second type of person
doNot = "don't"
# This string adds the two types together
y = "Those who know %s and those who know %s." % (bianary, doNot)

print(x)
print(y)

print("I said: %r" % x)
print("I also said: '%s' ." % y)

# Hilarious = false due to the joke not being funny
hilarious = False

joke_evaluation = "Isn't that joke so funny?! %r"
print(joke_evaluation % hilarious)

# These two are the two types of strings
w = "This is the left side of..."
e = "a string with a right side."

print(w + e)

# start of the 10/8 work day
print("mary had a little lamb.")
print("Its fleece was white as %s." % 'snow')
print("And everywhere that mary went.")
print("." * 10)

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

print(end1+end2+end3+end3+end4+end5+end6+end7+end8+end9+end10+end11+end12)

# More formatting
formatter = "%r %r %r %r"
print(formatter % (1,2,3,4))
print(formatter % ("one","two","three","four"))
print(formatter % (True,False,False,True))
print(formatter % (formatter,formatter,formatter,formatter))

# Why did i use %r instead of %s?
# it shows the entire quotes isntead of just the function of the quotes

days = "Mon Tue Wed Thu Fri"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug\nSep\nOct\nNov\nDec"

print("the days of the week are .", days)
print("the months of the year are .", months)

print("""
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""")

#What if i didn't like jan being on the the line with the rest of the
#text and away from the other months? How could i fix that?

#More Escaping

tabbyCat = "\tI'm tabbed in"
persianCat = "I'm split\non a line"
backslashCat = "I'm\\a\\cat."
taskCat = """
I'll make a list:
\t*cat food
\t*Fishies
\t*catnip\n\t* grass
"""
print(tabbyCat)
print(persianCat)
print(backslashCat)
print(taskCat)

#Escape Seq         What does it do
#\\
#\'
#\"
#\a
#\b
#\f
#\n
#\N{name}
#\r
#\t
#\uxxxx
#\Uxxxxxxxx
#\v
#\ooo
#\xhh

# What's the following code do:
#   While true:
#        for i in ["/","-","|","\\","|"]:
#            print("%s\r"%i,end='')
# Can you replace """ with '''?
#No

# Asking Questions

age = input("How old are you? ")
height = input("How tall are you? ")

print("So, you're really %r years old and %r feet tall? Wow..." % (age, height))

trip = input("how was your trip? ")
fun = input("Did you have fun at the beach? ")

print("Hey, you went on a trip? %r. Thats good, So was the water nice %r. sounds like it was a good time." % (trip, fun))

intro = input("hi? ")
well being = input("feeling? ")
User deletion = input("why?")