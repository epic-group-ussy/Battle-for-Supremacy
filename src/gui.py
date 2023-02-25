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

        tile_size = 75
        button_size_multiplier = .66666
        #calculated
        button_size = tile_size * button_size_multiplier
        center_offset = Vector(button_size/2, button_size/2)

        MAp=map.Map()
        
        #creates a map of buttons from the map object from map.py for each territory
        #each button will have a label with the territory name
        #each button will have a label with the troop count
        #each button will have a label with the team id
        for territory_name in MAp.territories:

            territory = MAp.territories[territory_name]

            button = Button(text=territory.name,
                            size_hint=(None, None),
                            size=(button_size, button_size),
                            pos=territory.position.multiply(tile_size).to_tuple()
                        )

            #draws lines between the difrent teritories
            for neighbor in territory.neighbors:
                button.canvas.add(Line(points=[
                    territory.position.multiply(tile_size).add(center_offset).to_tuple(), 
                    neighbor.position.multiply(tile_size).add(center_offset).to_tuple()
                ], width=2))

            #button.bind(on_press=self.callback)
            screen.add_widget(button)
        return screen

        #return self.root

GUImap().run()