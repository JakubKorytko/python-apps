""" A program that calculates the minimum effort needed to move elephants
from one position to another. """

from sys import exit as sys_exit


def get_cycles(current_configuration, target_configuration):
    """Transform the array of the current elephant configuration into individual cycles"""

    cycles = []

    current_cycle = current_configuration.copy()

    while len(current_cycle) != 0:
        current_cycle_elements = []
        current_elephant = current_cycle[0]
        first_element = current_elephant
        first_index = 0
        while True:
            if current_elephant == first_element:
                first_index += 1
            if first_index == 2:
                # Break the loop when returning to the beginning of the cycle for the second time
                # (the first time happens at the start of the loop)
                break
            current_cycle_elements.append(current_elephant)
            current_cycle.remove(current_elephant)
            current_elephant = current_configuration[
                target_configuration.index(current_elephant)
            ]
        cycles.append(current_cycle_elements)

    return cycles


def calculate_effort(current_configuration, elephant_weights, cycles):
    """Calculate the sum of effort values for each cycle"""

    total_effort = 0

    for cycle in cycles:
        weights_in_cycle = []
        weights_in_current_cycle = []

        for elephant_index in current_configuration:
            weights_in_cycle.append(elephant_weights[elephant_index - 1])
        for elephant_index in cycle:
            weights_in_current_cycle.append(elephant_weights[elephant_index - 1])

        sum_in_cycle = 0
        min_weight_in_array = min(weights_in_cycle)
        min_weight_in_current_cycle = min(weights_in_current_cycle)

        for elephant_index in cycle:
            sum_in_cycle += elephant_weights[elephant_index - 1]

        effort_method1 = sum_in_cycle + (len(cycle) - 2) * min_weight_in_current_cycle

        effort_method2 = (
            sum_in_cycle
            + min_weight_in_current_cycle
            + (len(cycle) + 1) * min_weight_in_array
        )

        total_effort += min(effort_method1, effort_method2)

    return total_effort


#################################
#                               #
#   n - number of elephants     #
#   m - weights of elephants    #
#   a - current arrangement     #
#   b - target arrangement      #
#                               #
#################################

try:
    n = int(input(""))
    m = list(map(int, input("").strip().split(" ")))
    a = list(map(int, input("").strip().split(" ")))
    b = list(map(int, input("").strip().split(" ")))
except (ValueError, TypeError):
    print(0)
    sys_exit()

# Copy of the initial configuration (to avoid modifying the original array)
CYCLES = get_cycles(a, b)

print(calculate_effort(a, m, CYCLES))
