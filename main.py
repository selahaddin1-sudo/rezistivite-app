from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivy.uix.spinner import Spinner
from kivy.core.window import Window
from kivy.metrics import dp

Window.clearcolor = (0.04, 0.06, 0.08, 1)

class DataCell(BoxLayout):
    def __init__(self, row, col, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.size_hint = (None, None)
        self.size = (dp(60), dp(55))
        self.spacing = dp(1)
        self.padding = dp(2)
        
        self.label = Label(text=f"S{row+1}K{col+1}", font_size='7sp', 
                          color=(0.9,0.9,0.95,1), bold=True, size_hint_y=0.2)
        self.input = TextInput(text='', hint_text='0', font_size='11sp', 
                              multiline=False, input_filter='float', halign='center',
                              background_color=(0.1,0.15,0.2,1), 
                              foreground_color=(0,0.83,1,1), size_hint_y=0.6)
        self.unit = Label(text='Ω', font_size='7sp', 
                         color=(0.9,0.9,0.95,1), size_hint_y=0.2)
        
        self.add_widget(self.label)
        self.add_widget(self.input)
        self.add_widget(self.unit)
        
    def get_value(self):
        try: return float(self.input.text)
        except: return None

class RezistiviteApp(App):
    def build(self):
        self.depth_value = 4.0
        self.cells = []
        
        root = ScrollView()
        main = BoxLayout(orientation='vertical', spacing=dp(4), 
                        padding=dp(6), size_hint_y=None)
        main.bind(minimum_height=main.setter('height'))
        
        main.add_widget(Label(text='⚡ Rezistivite PRO', font_size='15sp', 
                             bold=True, color=(0,0.83,1,1), 
                             size_hint_y=None, height=dp(30)))
        
        db = BoxLayout(orientation='horizontal', spacing=dp(4), 
                      size_hint_y=None, height=dp(38))
        db.add_widget(Label(text='Civi Araligi:', color=(0.9,0.9,0.95,1), 
                           font_size='11sp', size_hint_x=0.4))
        spinner = Spinner(text='4.0 m', 
                         values=['0.5 m','1.0 m','2.0 m','3.0 m','4.0 m',
                                '5.0 m','6.0 m','8.0 m','10.0 m'],
                         size_hint_x=0.6, background_color=(0.1,0.15,0.2,1),
                         color=(0,0.83,1,1), font_size='11sp')
        spinner.bind(text=lambda s,t: setattr(self, 'depth_value', 
                                              float(t.replace(' m',''))))
        db.add_widget(spinner)
        main.add_widget(db)
        
        grid = GridLayout(cols=5, spacing=dp(2), size_hint_y=None)
        grid.bind(minimum_height=grid.setter('height'))
        
        for i in range(5):
            row_cells = []
            for j in range(5):
                cell = DataCell(i, j)
                grid.add_widget(cell)
                row_cells.append(cell)
            self.cells.append(row_cells)
        
        main.add_widget(grid)
        
        bg = GridLayout(cols=2, spacing=dp(4), size_hint_y=None, height=dp(130))
        
        for text, color, func in [
            ('🗺 HARITA', (0.49,0.23,0.93,1), self.show_map),
            ('💾 KAYDET', (0.06,0.73,0.51,1), self.save_data),
            ('📂 YUKLE', (0.96,0.62,0.04,1), self.load_data),
            ('🗑 TEMIZLE', (0.94,0.27,0.27,1), self.clear_data),
        ]:
            btn = Button(text=text, background_normal='', background_color=color,
                        color=(1,1,1,1), font_size='12sp', bold=True,
                        size_hint_y=None, height=dp(38))
            btn.bind(on_press=func)
            bg.add_widget(btn)
        
        main.add_widget(bg)
        root.add_widget(main)
        return root
    
    def popup_msg(self, title, message):
        content = BoxLayout(orientation='vertical', spacing=dp(8), padding=dp(15))
        content.add_widget(Label(text=message, color=(0.9,0.9,0.95,1), font_size='13sp'))
        btn = Button(text='Tamam', size_hint_y=None, height=dp(35),
                    background_color=(0,0.83,1,1), color=(0,0,0,1), font_size='13sp', bold=True)
        popup = Popup(title=title, content=content, size_hint=(0.75, 0.3))
        btn.bind(on_press=popup.dismiss)
        content.add_widget(btn)
        popup.open()
    
    def show_map(self, i): self.popup_msg('🗺 Harita', 'Harita ozelligi aktif!')
    def save_data(self, i): self.popup_msg('💾 Kaydet', 'Veriler kaydedildi!')
    def load_data(self, i): self.popup_msg('📂 Yukle', 'Proje yukleniyor...')
    def clear_data(self, i):
        for row in self.cells:
            for cell in row: cell.input.text = ''
        self.popup_msg('✅ Temizlendi', 'Tum veriler silindi!')

if __name__ == '__main__':
    RezistiviteApp().run()