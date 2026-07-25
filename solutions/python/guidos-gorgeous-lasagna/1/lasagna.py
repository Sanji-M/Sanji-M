"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""



EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time):
    """
       for calculating the remaining bake time after placed in the oven
       takes total expected time of preparation and minus the time already in oven
    """
    remaining_time  = EXPECTED_BAKE_TIME - elapsed_bake_time
    return remaining_time


def preparation_time_in_minutes(number_of_layers):
    """
       for calculating the preparation time of both the layers to be added to the lasagna
       it takes the number of layers and multiplies it to the time of preparation
    """
    total_prep = number_of_layers * PREPARATION_TIME
    
    
    return total_prep


def elapsed_time_in_minutes(number_of_layers,elapsed_bake_time):
    """
        for calculating the total elapsed time of lasagna 
        it takes the total elapsed time of the layers and adds to the elapsed time in oven
    """
    total_elapsed_time  = (number_of_layers * PREPARATION_TIME) + elapsed_bake_time
    return total_elapsed_time