import kivy
from kivy.app import App
from kivy.uix.button import Button
import map

class GUImap(App):
    def build(self):
        #gets of the window size
        MAp=map.Map()
        #creates a map of buttons from the map object from map.py for each territory
        #each button will have a label with the territory name
        #each button will have a label with the troop count
        #each button will have a label with the team id
        for territory_name in MAp.territories:
            territory = MAp.territories[territory_name]
            button = Button(text=territory.name, size_hint=(None, None), size=(100, 100), pos=(territory.position.x, territory.position.y))
            #button.bind(on_press=self.callback)

            return button

GUImap().run()