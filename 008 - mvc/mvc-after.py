import tkinter as tk
import uuid
from abc import ABC, abstractmethod

class Model:
    def __init__(self):
        self.uuid = []

    def append(self, item):
        self.uuid.append(item)

    def clear(self):
        self.uuid = []

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
    
    def start(self):
        self.view.setup(self)
        self.view.start_main_loop()

    def handle_click_generate_uuid(self):
        # generate a uuid and add it to the list
        newid = uuid.uuid4()
        self.model.append(newid)
        self.view.append_to_list(newid)

    def handle_click_clear_list(self):
        # clear the uuid list in the model and the view
        self.model.clear()
        self.view.clear_list()

class View(ABC):
    @abstractmethod
    def setup(self, controller):
        pass

    @abstractmethod
    def append_to_list(self, item):
        pass

    @abstractmethod
    def clear_list(self):
        pass
    
    @abstractmethod
    def start_main_loop(self):
        pass

class TkView(View):
    def setup(self, controller):

        # setup tkinter
        self.root = tk.Tk()
        self.root.geometry("400x400")
        self.root.title("UUIDGen")

        # create the gui
        self.frame = tk.Frame(self.root)
        self.frame.pack(fill=tk.BOTH, expand=1)
        self.label = tk.Label(self.frame, text="Result:")
        self.label.pack()
        self.list = tk.Listbox(self.frame)
        self.list.pack(fill=tk.BOTH, expand=1)
        self.generate_uuid_button = tk.Button(self.frame, text="Generate UUID", command=controller.handle_click_generate_uuid)
        self.generate_uuid_button.pack()
        self.clear_button = tk.Button(self.frame, text="Clear list", command=controller.handle_click_clear_list)
        self.clear_button.pack()

    def append_to_list(self, item):
        self.list.insert(tk.END, item)

    def clear_list(self):
        self.list.delete(0, tk.END)
    
    def start_main_loop(self):
        # start the loop
        self.root.mainloop()

# create the MVC & start the application
c = Controller(Model(), TkView())
c.start()