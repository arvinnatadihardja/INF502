import csv


class AntBait:
    """ maps to month, year, plot, stake, species, abundance"""

    # Constructor
    def __init__(self, month, year, plot, stake, species, abundance):
        self.month = month
        self.year = year
        self.plot = plot
        self.stake = stake
        self.species = species  # Actual object of type AntSpecies
        self.abundance = abundance

    # Prints String
    def __str__(self):
        # species - month, year: abundance
        return '%s - %s, %s: %s' % (self.species.speciescode, self.month, self.year, self.abundance)  # Formatted string


class AntSpecies:
    """ maps to speciescode, genus, altgenus, species, altspecies, tribe, subfamily, IDissues"""

    def __init__(self, speciescode, genus, altgenus, species, altspecies, tribe, subfamily, idissues):
        self.speciescode = speciescode
        self.genus = genus
        self.altgenus = altgenus
        self.species = species
        self.altspecies = altspecies
        self.tribe = tribe
        self.subfamily = subfamily
        self.idissues = idissues

    # Print String
    def __str__(self):
        # genus species
        return '%s %s' % (self.genus, self.species)


# Function to read ant-bait
def read_bait(filename):
    global array_species
    bait_list = []

    # Read ant-bait.csv and
    with open(filename, 'r') as file_data:
        # Read object
        read_object = csv.reader(file_data)

        next(read_object)  # Skip header
        # Read each line, create object, and append it to list for return
        for i in read_object:
            month, year, plot, stake, species, abundance = i  # (unfolds into tuple)

            # Add an object of the same type ant-species instead of a string
            # species maps to ant-species speciescode
            code = i[4]
            for specie_object in array_species:
                if specie_object.speciescode == code:
                    species = specie_object  # Re-assign species to Object of type AntSpecies
                    temp = AntBait(month, year, plot, stake, species, abundance)
                    break  # Break inner loop because species code was found

            # Finally, add the temporary variable
            bait_list.append(temp)
    return bait_list  # Return the list with file data


def read_species(filename):
    species_list = []
    # Read ant-species.csv and
    with open(filename, 'r') as file_data:
        # Read object
        read_object = csv.reader(file_data)

        next(read_object)  # Skip header

        for i in read_object:
            temp = AntSpecies(*i)  # Creates object of the type AntSpecies, uses *i to get as many values in list row
            species_list.append(temp)
    return species_list


# Variables hold each of the values as they are read
array_species = read_species('ant-species.csv')  # Create species first, because point 3 requires a look up
array_baits = read_bait('ant-bait.csv')

# Test array baits
for i in array_baits:
    print(i)  # Tests for __str__

# Test array species
for i in array_species:
    print(i)  # Tests for __str__
