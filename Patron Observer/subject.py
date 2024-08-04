from observer import Observer
import tkinter as tk

class Subject ():

    def __init__(self):
        self.observers = []

    def registerInterest(self, obs: Observer):
        self.observers.append(obs)

    def notifyObservers(self, color: str):
        for observer in self.observers:
            observer.sendNotify(color)

