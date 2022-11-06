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


class MainApp(MDApp):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.user_points = 0

    def build(self):
        global sm
        self.theme_cls.material_style = "M3"
        sm = ScreenManager()
        sm.add_widget(SplashScreen(name='splash'))
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(ChallengesScreen(name='challenges'))
        sm.add_widget(NewChallengeScreen(name='newchallenge'))
        sm.add_widget(FriendsScreen(name='friends'))
        sm.add_widget(ApproveChallengeScreen(name='approve'))

        self.user_points = 0

        return sm   

    def complete_challenge(self, points):
        self.user_points += points
        print(self.user_points)

    def get_points(self):
        return str(self.user_points)

class SplashScreen(Screen):
    def switch(self, *args):
        self.parent.current = 'home'
    
    def on_enter(self, *args):
        Clock.schedule_once(self.switch,1)
   
class HomeScreen(Screen):
    pass

class ChallengesScreen(Screen):
    pass

class NewChallengeScreen(Screen):
    pass

class FriendsScreen(Screen):
    pass

class ApproveChallengeScreen(Screen):
    pass
    
    
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
    name = StringProperty()
    image = StringProperty()
    points = StringProperty()
    
class NewChallengeCard(MDCard):
    text = StringProperty()
    image = StringProperty()
    points = StringProperty()

class ApproveChallengeCard(MDCard):
    image = StringProperty()

MainApp().run()