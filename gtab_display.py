#This program defines how to display music notation in guitar tab form.
#The following is just for reference
"""
e|---------------|---------------|-----------------|
B|-1-------1-----|-0-------0-----|-3-------3-------|
G|-----0-------0-|-----0-------0-|-----0-------0---|
D|---2-------2---|---2-------2---|---2-------2-----|
A|-3-----3-------|-3-----3-------|-3-----3---------|
E|---------------|---------------|-----------------|
"""

#Each string as an object, string 6 as low E and so forth
class GuitarString:
    def __init__(self, string_num):
        self.string_num = string_num

    def get_name(self):
        # Define the standard name for each string number
        name = {
            1: "e",  # High E
            2: "B",
            3: "G",
            4: "D",
            5: "A",
            6: "E"   # Low E
        }
        # Return the note associated with the string number
        return name.get(self.string_num, "Unknown")

    def __str__(self):
        # Return the string number and its name note
        return f"Guitar String {self.get_name()}"

# Create 6 instances of GuitarString with string_num from 1 to 6
strings = [GuitarString(i) for i in range(1, 7)]

# Print each string instance with name information
for string in strings:
    print(string)

