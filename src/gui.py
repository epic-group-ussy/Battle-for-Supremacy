import kivy
from kivy.app import App
from kivy.uix.button import Button
from vector import Vector
import map
from kivy.uix.floatlayout import FloatLayout
class GUImap(App):
    def build(self):
        screen = Screen()

        MAp=map.Map()
        offset = Vector(200, 200)
        #creates a map of buttons from the map object from map.py for each territory
        #each button will have a label with the territory name
        #each button will have a label with the troop count
        #each button will have a label with the team id
        for territory_name in MAp.territories:
            territory = MAp.territories[territory_name]

            button = Button(text=territory.name, size_hint=(None, None), size=(100, 100), pos=territory.position.add(offset).to_tuple())
            #button.bind(on_press=self.callback)
            screen.add_widget(button)
        return screen

        #return self.root

GUImap().run()