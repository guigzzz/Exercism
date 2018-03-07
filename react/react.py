class Cell(object):
    def __init__(self, value = None, 
        dependencies = None, updater_callback = None):

        self.following_cells = []
        self.value = None

        if value is None: # Compute cell
            if dependencies is None or \
                updater_callback is None:
                raise ValueError("Compute cell requires dependencies and callback function")
            else:
                self.register_updates(dependencies)
                self.dependencies = dependencies
                self.old_dep_values = [None] * len(self.dependencies)
                self.updater_callback = updater_callback

                self.watchers = set()
                self.update()

        else: # input cell
            self.set_value(value)
    

    def register_updates(self, dependencies):
        for d in dependencies:
            d.add_following_cell(self)

    def add_following_cell(self, compute_cell):
        self.following_cells.append(compute_cell)

    def set_value(self, value):
        self.value = value

        for cell in self.following_cells:
            cell.update()

    def update(self):
        values = [c.value for c in self.dependencies]

        if all([old != new for old, new in zip(self.old_dep_values, values)]):
            self.old_dep_values = values
            
            new_value = self.updater_callback(values)
            if new_value != self.value:
                self.set_value(new_value)
                self.call_watchers()
        
    def call_watchers(self):
        for w in self.watchers:
            w(self, self.value)

    def add_watcher(self, watcher_callback):
        self.watchers.add(watcher_callback)

    def remove_watcher(self, watcher_callback):
        self.watchers.discard(watcher_callback)

    def __repr__(self):
        if self.dependencies and self.updater_callback:
            return 'Compute Cell: value = {}'.format(self.value)
        else:
            return 'Input Cell: value = {}'.format(self.value)


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

if __name__ == '__main__':
    pass