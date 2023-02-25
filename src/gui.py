import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivymd.uix.screen import Screen
from vector import Vector
import map
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Line
class GUImap(App):
    def build(self):
        """builds the gui"""
        screen = Screen()

        MAp=map.Map()
        offset = Vector(200, 200)
        #creates a map of buttons from the map object from map.py for each territory
        #each button will have a label with the territory name
        #each button will have a label with the troop count
        #each button will have a label with the team id
        for territory_name in MAp.territories:
            territory = MAp.territories[territory_name]
            button = Button(text=territory.name, size_hint=(None, None), size=(75, 75), pos=territory.position.multiply(100).add(offset).to_tuple())
            #draws lines between the difrent teritories
            for neighbor in territory.neighbors:
                button.canvas.add(Line(points=[territory.position.multiply(100).add(offset).to_tuple(), neighbor.position.multiply(100).add(offset).to_tuple()], width=1))

            #button.bind(on_press=self.callback)
            screen.add_widget(button)
        return screen

        #return self.root

GUImap().run()