from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.properties import StringProperty
from kivymd.uix.card import MDCard
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.scrollview import ScrollView
from kivy.clock import Clock
#Window.size(310,580)

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
    points= StringProperty()
   
MainApp().run()