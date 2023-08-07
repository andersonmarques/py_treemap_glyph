

class File_Observable:
    def __init__(self):
        self.observers = []

    def attach_observer(self, observer):
        '''Adds an observer to the list of observers'''
        self.observers.append(observer)

    def detach_observer(self, observer):
        '''Removes an observer from the list of observers'''
        self.observers.remove(observer)

    def notify_file_selected(self, file_path):
        '''Notifies all observers that a file was selected'''
        for observer in self.observers:
            observer.update_file_selection(file_path)

    def notify_closing(self):
        '''Notifies all observers that the application is closing'''
        for observer in self.observers:
            observer.update_closing()

  