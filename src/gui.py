import kivy
from kivy.app import App
from kivy.uix.button import Button
import map
class GUImap(App):
    def build(self):
        #creates a map of buttons from the map object from map.py for each territory
        #each button will have a label with the territory name
        #each button will have a label with the troop count
        #each button will have a label with the team id
        for territory in map.Map().territories:
            button = Button(text=territory.name)
            button.bind(on_press=self.callback)
            print(territory)
            return button
        

GUImap().run()