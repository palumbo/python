from sys import argv

noun, verb = argv

thing = raw_input("Give me a ", noun)
action = raw_input("Give me a ", verb) 

print "The ", thing, " did ", action, "."
