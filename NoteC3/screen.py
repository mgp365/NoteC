from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.core.window import Window

class ImageButton(Button):
    def __init__(self, image_source, **kwargs):
        super().__init__(**kwargs)
        # Botoncito bonito :D
        self.background_normal = image_source
        self.background_down = image_source
        # PA Q NO ESTEN APLASTADOTES
        self.size_hint = (None, None)
        self.size = (80, 80)  # NS AYUDAAAAAA

class TimerScreen(BoxLayout):
    def __init__(self, switch_to_main, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 10
        
        self.time = 0  # q empiece desde 0
        self.label = Label(text='00:00', font_size='48sp')
        
        header = BoxLayout(orientation='horizontal', size_hint=(1, 0.1))
        header.add_widget(Label(text='Task', font_size='24sp'))
        
        self.add_widget(header)
        self.add_widget(self.label)
        
        self.clock_event = None

    def start_timer(self):
        self.clock_event = Clock.schedule_interval(self.update_timer, 1)

    def update_timer(self, dt):
        self.time += 1
        minutes, seconds = divmod(self.time, 60)
        self.label.text = f'{minutes:02}:{seconds:02}'

    def stop_timer(self):
        if self.clock_event:
            Clock.unschedule(self.clock_event)
            self.clock_event = None

class MainScreen(BoxLayout):
    def __init__(self, switch_to_timer, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 70
        self.spacing = 20
        
        label = Label(text='Hello, team\nTime to start', font_size='24sp', size_hint=(1, 0.2))
        self.add_widget(label)
        
        #El boxlayout pa que no se estiren los malditos
        button_layout = BoxLayout(orientation='horizontal', spacing=180, size_hint=(None, None))
        button_layout.size = (200, 400)  # tamaño del layout d los botoncitos
        
        button_x = ImageButton(image_source='images/reject.png')
        button_check = ImageButton(image_source='images/verified.png')
        
        #verified lleva al temporizador
        button_check.bind(on_press=switch_to_timer)
        
        button_layout.add_widget(button_x)
        button_layout.add_widget(button_check)
        
        self.add_widget(button_layout)

class MyApp(App):
    def build(self):
        Window.size = (360, 640)  #tamaño del celular
        self.main_screen = MainScreen(self.switch_to_timer)
        self.timer_screen = TimerScreen(self.switch_to_main)
        return self.main_screen

    def switch_to_timer(self, instance):
        self.root.clear_widgets()
        self.root.add_widget(self.timer_screen)
        self.timer_screen.start_timer()

    def switch_to_main(self, instance):
        self.timer_screen.stop_timer()
        self.root.clear_widgets()
        self.root.add_widget(self.main_screen)

if __name__ == '__main__':
    MyApp().run()
