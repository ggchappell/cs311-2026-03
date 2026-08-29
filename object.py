# object.py
# Glenn G. Chappell
# 2026-08-28
"""Classes, objects, operator overloading in Python."""


class Dogs:
    """class for tracking how many dogs you have."""

    # Attributes:
    #   _num_dogs: how mamy dogs we have - must be nonnegative int

    def __init__(self, start_num=None):
        """Set current number of dogs to given value - or 0 if none."""

        if start_num is None:
            start_num = 0
        assert isinstance(start_num, int)

        self._num_dogs = start_num

    def how_many(self):
        """Return how many dogs you have."""

        return self._num_dogs

    def get_a_dog(self):
        """Get a new dog (so number of dogs goes up by 1)."""

        self._num_dogs += 1

    def lose_a_dog(self):
        """Lose a dog (so number of dogs goes down by 1
        -- if you have at least one dog.
        """

        self._num_dogs -= 1
        self._fix_num_dogs()

    def __iadd__(self, chg):
        """Add given value to our number of dogs."""

        assert isinstance(chg, int)

        self._num_dogs += chg
        self._fix_num_dogs()
        return self

    def __isub__(self, chg):
        """Subtract given value from our number of dogs."""

        assert isinstance(chg, int)

        self._num_dogs -= chg
        self._fix_num_dogs()
        return self

    def __str__(self):
        """Convert to a string: how many dogs, in sentence form."""

        return "I have " + str(self._num_dogs) + " dogs."

    def _fix_num_dogs(self):
        """(Internal only) Handle a negative _num_dogs: make it zero."""

        if self._num_dogs < 0:
            self._num_dogs = 0


# Main program

# Make ourselves a dog counter
my_dogs = Dogs(1)  # Start with 1 dog

# Get some more dogs
my_dogs.get_a_dog()
my_dogs.get_a_dog()
my_dogs += 2

# Output the results
print("Print results the hard way (must have 5 dogs):")
print("I have", my_dogs.how_many(), "dogs.")
print()

print("Print results the easy way (must be same as above):")
print(my_dogs)
print()

