from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.properties import StringProperty, ListProperty
from kivymd.uix.card import MDCard
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock
#Window.size(310,580)

class Friend():
    def __init__(self, name = "Homie", points = "0", image = "images/pfp.png"):
        self.name = name
        self.points = points
        self.image = image

Friends = [
    Friend(name="John"), 
    Friend(name="Jane")
]



class MainApp(MDApp):
    def build(self):
        global sm
        self.theme_cls.material_style = "M3"
        sm = ScreenManager()
        sm.add_widget(SplashScreen(name='splash'))
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(ChallengesScreen(name='challenges'))
        sm.add_widget(FriendsScreen(name='friends'))
        return sm   

class SplashScreen(Screen):
    def switch(self, *args):
        self.parent.current = 'home'
    
    def on_enter(self, *args):
        Clock.schedule_once(self.switch,1)
   
class HomeScreen(Screen):
    pass

class ChallengesScreen(Screen):
    pass

class FriendsScreen(Screen):
    def update(self):
        self.ids.grid.clear_widgets()
        for friend in Friends:
            self.ids.grid.add_widget(FriendCard(friend))
    def on_enter(self):
        for friend in Friends:
            self.ids.grid.add_widget(FriendCard(friend))
    
    
class ScrollList(ScrollView):
    text = StringProperty()

class ElementCard(MDCard):
    text = StringProperty()
    image = StringProperty()
    items_count = StringProperty()
    subtext = StringProperty()

class ChallengeCard(MDCard):
    text = StringProperty()
    image = StringProperty()

class FriendCard(MDCard):
    def build(self, friend, **kwargs):
        self.root.name = StringProperty(friend.name)
        self.root.points = StringProperty(friend.points)
        self.root.image = StringProperty(friend.image)
        super().__init__(**kwargs)


MainApp().run()