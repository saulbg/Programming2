# Saul Barrera Garcia

def break_words(stuff):
  """This function will break up words for us."""
  words = stuff.split(' ') 
  return words

def sort_words(words):
  """Sorts the words."""
  return sorted(words)

# def print_first_word(words)
def print_first_word(words): # We add ":" at the end of a function
  """Prints the first word after popping it off."""
   # word = words.poop(0)
  word = words.pop(0) # Change poop for pop
  print(word) # Collocate the parentheses

def print_last_word(words):
  """Prints the last word after popping it off."""
  # word = words.pop(-1
  word = words.pop(-1) # Close the parentheses
  # print word
  print(word) # Collocate parenthesis

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


print("Let's practice everything.") # Collocate parentheses
print('You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.') # Collocate parentheses

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explantion
\n\t\twhere there is none.
"""

print("--------------") # Collocate parentheses
# print poem
print(poem) # We collocate parentheses to the variable
print("--------------") # Collocate the use of parentheses

five = 10 -2 + 2 - 5 # We correct the operation

print(f"This should be five: %s" % five) # Collocate parentheses

def secret_formula(started):
  jelly_beans = started * 500
  jars = jelly_beans / 1000 # Put the correct divition character "/"
  crates = jars / 100
  return jelly_beans, jars, crates


start_point = 10000

# beans, jars, crates == secret_formula(start-point)
beans, jars, crates = secret_formula(start_point) # We correct the "==" for "=" and correct the "-" for "_"

print("With a starting point of: %d" %start_point) # Collocate parenthesis

print("We'd have %d jeans, %d jars, and %d crates." % (beans, jars, crates)) # Collocate the parentheses

start_point = start_point / 10

print("We can also do that this way:")  # Collocate parenthesis

print("We'd have %d beans, %d jars, and %d crabapples." % secret_formula(start_point))
# Collocate parentheses, change to "start_pont" for "start_point" and add a parentheses at the end


sentence =("All good things come to those who weight.")
# Collocate parentheses and correct the spelling

words = break_words(sentence) #The variable ex25 doesn't have any sense

sorted_words = sort_words(words) # Correcting the variable ex25 
print_first_word(words)
print_last_word(words)

print_first_word(sorted_words) # Print without a point at the beginning
print_last_word(sorted_words)

sorted_words = sort_sentence(sentence) # Correcting the variable ex25

print(sorted_words) # Correct the print and collocating parentheses

print_first_and_last(sentence) # Correct the spelling 

print_first_and_last_sorted(sentence) # Correct function name
