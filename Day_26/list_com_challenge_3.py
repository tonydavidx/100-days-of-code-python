sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:

sentence_list = sentence.split()

result = {text: len(text) for text in sentence_list}

print(result)
