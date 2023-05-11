

class File_Selection_Observable:
    def __init__(self):
        self.observers = []

    def attach_observer(self, observer):
        self.observers.append(observer)

    def detach_observer(self, observer):
        self.observers.remove(observer)

    def notify_file_selected(self, file_path):
        for observer in self.observers:
            observer.update_file_selection(file_path)

    def notify_closing(self):
        '''Notifies all observers that the application is closing'''
        for observer in self.observers:
            observer.update_closing()

  