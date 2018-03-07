class Cell(object):
    def __init__(self, value = None, 
        dependencies = None, updater_callback = None):

        if value is None: # Compute cell
            if dependencies is None and \
                updater_callback is None:
                raise ValueError("Compute cell requires dependencies and callback function")

        else: # input cell
            self.set_value(value)

    def set_value(self, value):
        self.value = value

    def add_watcher(self, watcher_callback):
        pass

    def remove_watcher(self, watcher_callback):
        pass


class Reactor(object):

    def __init__(self):
        pass

    def create_input_cell(self, value):
        return Cell(value = value)

    def create_compute_cell(self, dependencies, updater_callback):
        return Cell(
            dependencies = dependencies, 
            updater_callback = updater_callback
        )






def increment(values):
    return values[0] + 1

def decrement(values):
    return values[0] - 1

def product(values):
    return values[0] * values[1]

if __name__ == '__main__':
    reactor = Reactor()
    inputCell1 = reactor.create_input_cell(1)
    computeCell1 = reactor.create_compute_cell({inputCell1}, increment)
    computeCell2 = reactor.create_compute_cell({inputCell1}, decrement)
    computeCell3 = reactor.create_compute_cell({computeCell1,
                                                computeCell2},
                                                product)
    assert computeCell3.value == 0
    inputCell1.set_value(3)
    assert computeCell3.value == 8
