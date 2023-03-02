import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Line
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.clock import Clock

from vector import Vector
import map

Builder.load_file('gui.kv')


class TerritoryButton(Button):
    pass


class GUIMapScreen(Screen):
    content_area = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self._build_map)

    def _build_map(self, dt):
        tile_size = 75
        button_size_multiplier = 2 / 3
        # calculated
        button_size = tile_size * button_size_multiplier
        center_offset = Vector(button_size / 2, button_size / 2)

        map_obj = map.Map()

        # creates a map of buttons from the map object from map.py for each territory
        # each button will have a label with the territory name
        # each button will have a label with the troop count
        # each button will have a label with the team id
        # draws lines between the different territories

        # draws the lines between territories
        for territory_name in map_obj.territories:
            territory = map_obj.territories[territory_name]
            for neighbor in territory.neighbors:
                self.content_area.canvas.add(Line(points=[
                    territory.position.multiply(tile_size).add(center_offset).to_tuple(),
                    neighbor.position.multiply(tile_size).add(center_offset).to_tuple()
                ], width=2))

        # draws the continents
        for territory_name in map_obj.territories:
            territory = map_obj.territories[territory_name]

            button = TerritoryButton(text=territory.name,
                color=(0.25, 0.25, 0.25, 1),
                size_hint=(None, None),
                size=(button_size, button_size),
                pos=territory.position.multiply(tile_size).to_tuple(),
                background_color=map_obj.colors[territory.continent_name],
                background_normal=''
                )

            self.content_area.add_widget(button)


class GUIMapApp(App):
    def build(self):
        # create screen manager and add GUIMapScreen
        screen_manager = ScreenManager()
        guimap_screen = GUIMapScreen(name='map_screen')
        screen_manager.add_widget(guimap_screen)
        return screen_manager


if __name__ == '__main__':
    GUIMapApp().run()
