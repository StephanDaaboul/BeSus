from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.properties import StringProperty
from kivymd.uix.card import MDCard
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.scrollview import ScrollView

class MainApp(MDApp):
    def build(self):
        self.theme_cls.material_style = "M3"
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(ChallengesScreen(name='challenges'))
        return sm
   
class HomeScreen(Screen):
    pass

class ChallengesScreen(Screen):
    pass
    
class ScrollList(ScrollView):
    text = StringProperty()

class ElementCard(MDCard):
    text = StringProperty()
    image = StringProperty()
    items_count = StringProperty()
    subtext = StringProperty()
    
MainApp().run()