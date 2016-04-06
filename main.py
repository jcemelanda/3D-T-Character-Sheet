from kivy.app import App
from kivy.storage.jsonstore import JsonStore
from kivy.uix.scrollview import ScrollView


class MainLayout(ScrollView):
    pass


class TokioDefendersCharacterSheetApp(App):
    def build(self):
        return MainLayout()

    def on_start(self):
        self.store = JsonStore('3det.json')
        if self.store.exists('3det'):
            data = self.store.get('3det')
            self.root.ids.name.text = data['name']
            self.root.ids.points.text = data['points']
            self.root.ids.strength.text = data['strength']
            self.root.ids.hability.text = data['hability']
            self.root.ids.resistance.text = data['resistance']
            self.root.ids.armor.text = data['armor']
            self.root.ids.fire_power.text = data['fire_power']

    def save(self):
        self.store = JsonStore('3det.json')
        data = {
            'name': self.root.ids.name.text,
            'points': self.root.ids.points.text,
            'strength': self.root.ids.strength.text,
            'hability': self.root.ids.hability.text,
            'resistance': self.root.ids.resistance.text,
            'armor': self.root.ids.armor.text,
            'fire_power': self.root.ids.fire_power.text,
        }
        self.store.put('3det', **data)


if __name__ == '__main__':
    TokioDefendersCharacterSheetApp().run()
