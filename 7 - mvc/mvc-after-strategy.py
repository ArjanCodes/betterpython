import tkinter as tk
import uuid
import string
import random
from abc import ABC, abstractmethod

# functional strategy 
def generate_uuid1():
    return uuid.uuid1()

def generate_uuid4():
    return uuid.uuid4()

def generate_simple_id():
    return ''.join(random.choices(string.ascii_lowercase, k=30))

class Model:
    def __init__(self):
        self.uuid = []

class Controller:
    def __init__(self, model, view, generate_uuid):
        self.model = model
        self.view = view
        self.generate_uuid = generate_uuid
    
    def start(self):
        self.view.setup(self)
        self.view.start_main_loop()

    def handle_click_generate_uuid(self):
        # generate a uuid and add it to the list
        self.model.uuid.append(self.generate_uuid())
        self.view.append_to_list(self.model.uuid[-1])

    def handle_click_clear_list(self):
        # clear the uuid list in the model and the view
        self.model.uuid = []
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
c = Controller(Model(), TkView(), generate_simple_id)
c.start()