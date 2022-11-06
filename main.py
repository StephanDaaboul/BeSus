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
        sm.add_widget(FriendsScreen(name='friends'))
        return sm
   
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


def on_start(self):
    styles = {
        "elevated": "#f6eeee", "filled": "#f4dedc", "outlined": "#f8f5f4"
    }
    for style in styles.keys():
        self.root.ids.box.add_widget(
            MDCard(
                line_color=(0.2, 0.2, 0.2, 0.8),
                style=style,
                text=style.capitalize(),
                md_bg_color=styles[style],
                shadow_softness=2 if style == "elevated" else 12,
                shadow_offset=(0, 1) if style == "elevated" else (0, 2),
                )
            )
    
MainApp().run()