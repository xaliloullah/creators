import os 
import sys
import time 
try:
    import keyboard
except:
    pass

class Terminal:  
    width = 100
    lang = None
    # colors
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    GREY = '\033[90m'
    LIGHT_BLACK = '\033[80m'
    LIGHT_RED = '\033[91m'
    LIGHT_GREEN = '\033[92m'
    LIGHT_YELLOW = '\033[93m'
    LIGHT_BLUE = '\033[94m'
    LIGHT_MAGENTA = '\033[95m'
    LIGHT_CYAN = '\033[96m'
    LIGHT_WHITE = '\033[97m'
            

    # Background colors
    BACKGROUND_BLACK = '\033[40m '
    BACKGROUND_RED = '\033[41m '
    BACKGROUND_GREEN = '\033[42m '
    BACKGROUND_YELLOW = '\033[43m '
    BACKGROUND_BLUE = '\033[44m '
    BACKGROUND_MAGENTA = '\033[45m '
    BACKGROUND_CYAN = '\033[46m '
    BACKGROUND_WHITE = '\033[47m '
    BACKGROUND_GREY = '\033[48m '
    BACKGROUND_LIGHT_BLACK = '\033[100m '
    BACKGROUND_LIGHT_RED = '\033[101m '
    BACKGROUND_LIGHT_GREEN = '\033[102m '
    BACKGROUND_LIGHT_YELLOW = '\033[103m '
    BACKGROUND_LIGHT_BLUE = '\033[104m '
    BACKGROUND_LIGHT_MAGENTA = '\033[105m '
    BACKGROUND_LIGHT_CYAN = '\033[106m '
    BACKGROUND_LIGHT_WHITE = '\033[107m '

    # Text Formatting
    BOLD = '\033[1m'         
    UNDERLINE = '\033[4m'     
    ITALIC = '\033[3m'        
    BLINK = '\033[5m'         
    REVERSE = '\033[7m'       
    HIDDEN = '\033[8m'        
    RESET = '\033[0m'

    # icon
    ICON_LIGHT_CHECK = "✔"
    ICON_LIGHT_ERROR = "✖" 
    ICON_LIGHT_WARNING = "⚠" 
    ICON_LIGHT_INFO = "ℹ"
    ICON_INFO_CIRCLE = "🛈"
    ICON_LIGHT_LOCK = "🗝"
    ICON_ARROW_UP = "🔼"
    ICON_ARROW_DOWN = "🔽"
    ICON_ARROW_RIGHT = "▶"
    ICON_ARROW_LEFT = "◀"
    ICON_CHECK = "✔️"
    ICON_ERROR = "❌"
    ICON_PLUS = "➕"
    ICON_MOIN = "➖"
    ICON_EDIT = "📝"
    ICON_EXCLAMATION = "❗"
    ICON_QUESTION = "❓"
    ICON_STOP = "⛔"
    ICON_WARNING = "⚠️"
    ICON_LIGHTBULB = "💡"
    ICON_LOCK = "🔒"
    ICON_ENVELOPPE = "📧" 
    ICON_NUMBER = "🔢"
    ICON_PHONE = "📞"
    ICON_GLOBE = "🌐"
    ICON_SEARCH = "🔍"
    ICON_CALENDAR = "📅"
    ICON_CARD = "💳"
    ICON_FILE = "📁"
    ICON_LOCATION = "🏠"
    ICON_HEART = "❤️"
    ICON_STAR = "⭐"
    ICON_BELL = "🔔"
    ICON_FIRE = "🔥"
    ICON_GEAR = "⚙️" 
    ICON_CHECKMARK = "✅" 
    ICON_INFO = "ℹ️"
    ICON_THUMBS_UP = "👍"
    ICON_THUMBS_DOWN = "👎"
    ICON_SUN = "☀️"
    ICON_MOON = "🌙"
    ICON_CLOUD = "☁️"
    ICON_RAIN = "🌧️"
    ICON_SNOW = "❄️"
    ICON_MOUNTAIN = "⛰️"
    ICON_TROPHY = "🏆"
    ICON_MEDAL = "🏅"
    ICON_PEACE = "✌️"
    ICON_HEART_EYES = "😍"
    ICON_FIREWORKS = "🎆"
    ICON_GIFT = "🎁"
    ICON_PARTY_POPPER = "🎉"
    ICON_FINGERPOINTING = "👉"
    ICON_SOS = "🆘"
    ICON_FOOTBALL = "⚽"
    ICON_BASKETBALL = "🏀"
    ICON_FUEL = "⛽"
    ICON_MONEY = "💵"
    ICON_BOMB = "💣"
    ICON_APPLE = "🍎"
    ICON_TABS = "📑"

    @classmethod            
    def clear(cls):
        return os.system("cls" if os.name == "nt" else "clear")
     
    # color 
    @classmethod     
    def black(cls):
        return cls.BLACK
    
    @classmethod     
    def dark(cls):
        return cls.BLACK
    
    @classmethod 
    def red(cls):
        return cls.RED
    
    @classmethod 
    def green(cls):
        return cls.GREEN
    
    @classmethod 
    def yellow(cls):
        return cls.YELLOW
    
    @classmethod 
    def blue(cls):
        return cls.BLUE
    
    @classmethod 
    def magenta(cls):
        return cls.MAGENTA
    
    @classmethod 
    def cyan(cls):
        return cls.CYAN
    
    @classmethod 
    def white(cls):
        return cls.WHITE
    
    @classmethod 
    def grey(cls):
        return cls.GREY
    
    @classmethod 
    def light_black(cls):
        return cls.LIGHT_BLACK
    
    @classmethod 
    def light_red(cls):
        return cls.LIGHT_RED
    
    @classmethod 
    def light_green(cls):
        return cls.LIGHT_GREEN
    
    @classmethod 
    def light_yellow(cls):
        return cls.LIGHT_YELLOW
    
    @classmethod 
    def light_blue(cls):
        return cls.LIGHT_BLUE
    
    @classmethod 
    def light_magenta(cls):
        return cls.LIGHT_MAGENTA
    
    @classmethod 
    def light_cyan(cls):
        return cls.LIGHT_CYAN
    
    @classmethod 
    def light(cls):
        return cls.LIGHT_WHITE

    # BACKGROUND
    @classmethod     
    def bg_black(cls):
        return cls.BACKGROUND_BLACK
    
    @classmethod 
    def bg_red(cls):
        return cls.BACKGROUND_RED
    
    @classmethod 
    def bg_green(cls):
        return cls.BACKGROUND_GREEN
    
    @classmethod 
    def bg_yellow(cls):
        return cls.BACKGROUND_YELLOW
    
    @classmethod 
    def bg_blue(cls):
        return cls.BACKGROUND_BLUE
    
    @classmethod 
    def bg_magenta(cls):
        return cls.BACKGROUND_MAGENTA
    
    @classmethod 
    def bg_cyan(cls):
        return cls.BACKGROUND_CYAN
    
    @classmethod 
    def bg_white(cls):
        return cls.BACKGROUND_WHITE
    
    @classmethod 
    def bg_grey(cls):
        return cls.BACKGROUND_GREY
    
    @classmethod 
    def bg_light_black(cls):
        return cls.BACKGROUND_LIGHT_BLACK
    
    @classmethod 
    def bg_light_red(cls):
        return cls.BACKGROUND_LIGHT_RED
    
    @classmethod 
    def bg_light_green(cls):
        return cls.BACKGROUND_LIGHT_GREEN
    
    @classmethod 
    def bg_light_yellow(cls):
        return cls.BACKGROUND_LIGHT_YELLOW
    
    @classmethod 
    def bg_light_blue(cls):
        return cls.BACKGROUND_LIGHT_BLUE
    
    @classmethod 
    def bg_light_magenta(cls):
        return cls.BACKGROUND_LIGHT_MAGENTA
    
    @classmethod 
    def bg_light_cyan(cls):
        return cls.BACKGROUND_LIGHT_CYAN
    
    @classmethod 
    def bg_light(cls):
        return cls.BACKGROUND_LIGHT_WHITE
    
    @classmethod     
    def bold(cls):
        return cls.BOLD
    
    @classmethod     
    def underline(cls):
        return cls.UNDERLINE
    
    @classmethod     
    def italic(cls):
        return cls.ITALIC
    
    @classmethod     
    def blink(cls):
        return cls.BLINK
    
    @classmethod     
    def reverse(cls):
        return cls.REVERSE
    
    @classmethod     
    def hidden(cls):
        return cls.HIDDEN
    
    @classmethod     
    def reset(cls):
        return cls.RESET
    
    @classmethod     
    def icon_light_check(cls):
        return cls.ICON_LIGHT_CHECK
    
    @classmethod 
    def icon_light_error(cls):
        return cls.ICON_LIGHT_ERROR
    
    @classmethod 
    def icon_light_warning(cls):
        return cls.ICON_LIGHT_WARNING
    
    @classmethod 
    def icon_light_info(cls):
        return cls.ICON_LIGHT_INFO
    
    @classmethod 
    def icon_info_circle(cls):
        return cls.ICON_INFO_CIRCLE
    
    @classmethod 
    def icon_light_lock(cls):
        return cls.ICON_LIGHT_LOCK
    
    @classmethod 
    def icon_arrow_up(cls):
        return cls.ICON_ARROW_UP
    
    @classmethod 
    def icon_arrow_down(cls):
        return cls.ICON_ARROW_DOWN
    
    @classmethod 
    def icon_arrow_right(cls):
        return cls.ICON_ARROW_RIGHT
    
    @classmethod 
    def icon_arrow_left(cls):
        return cls.ICON_ARROW_LEFT
    
    @classmethod 
    def icon_check(cls):
        return cls.ICON_CHECK
    
    @classmethod 
    def icon_error(cls):
        return cls.ICON_ERROR
    
    @classmethod 
    def icon_plus(cls):
        return cls.ICON_PLUS
    
    @classmethod 
    def icon_moin(cls):
        return cls.ICON_MOIN
    
    @classmethod 
    def icon_edit(cls):
        return cls.ICON_EDIT
    
    @classmethod 
    def icon_exclamation(cls):
        return cls.ICON_EXCLAMATION
    
    @classmethod 
    def icon_question(cls):
        return cls.ICON_QUESTION
    
    @classmethod 
    def icon_stop(cls):
        return cls.ICON_STOP
    
    @classmethod 
    def icon_warning(cls):
        return cls.ICON_WARNING
    
    @classmethod 
    def icon_lightbulb(cls):
        return cls.ICON_LIGHTBULB
    
    @classmethod 
    def icon_lock(cls):
        return cls.ICON_LOCK
    
    @classmethod 
    def icon_enveloppe(cls):
        return cls.ICON_ENVELOPPE
    
    @classmethod 
    def icon_number(cls):
        return cls.ICON_NUMBER
    
    @classmethod 
    def icon_phone(cls):
        return cls.ICON_PHONE
    
    @classmethod 
    def icon_globe(cls):
        return cls.ICON_GLOBE
    
    @classmethod 
    def icon_search(cls):
        return cls.ICON_SEARCH
    
    @classmethod 
    def icon_calendar(cls):
        return cls.ICON_CALENDAR
    
    @classmethod 
    def icon_card(cls):
        return cls.ICON_CARD
    
    @classmethod 
    def icon_file(cls):
        return cls.ICON_FILE
    
    @classmethod 
    def icon_location(cls):
        return cls.ICON_LOCATION
    
    @classmethod 
    def icon_heart(cls):
        return cls.ICON_HEART
    
    @classmethod 
    def icon_star(cls):
        return cls.ICON_STAR
    
    @classmethod 
    def icon_bell(cls):
        return cls.ICON_BELL
    
    @classmethod 
    def icon_fire(cls):
        return cls.ICON_FIRE
    
    @classmethod 
    def icon_gear(cls):
        return cls.ICON_GEAR
    
    @classmethod 
    def icon_checkmark(cls):
        return cls.ICON_CHECKMARK
    
    @classmethod 
    def icon_info(cls):
        return cls.ICON_INFO
    
    @classmethod 
    def icon_thumbs_up(cls):
        return cls.ICON_THUMBS_UP
    
    @classmethod 
    def icon_thumbs_down(cls):
        return cls.ICON_THUMBS_DOWN
    
    @classmethod 
    def icon_sun(cls):
        return cls.ICON_SUN
    
    @classmethod 
    def icon_moon(cls):
        return cls.ICON_MOON
    
    @classmethod 
    def icon_cloud(cls):
        return cls.ICON_CLOUD
    
    @classmethod 
    def icon_rain(cls):
        return cls.ICON_RAIN
    
    @classmethod 
    def icon_snow(cls):
        return cls.ICON_SNOW
    
    @classmethod 
    def icon_mountain(cls):
        return cls.ICON_MOUNTAIN
    
    @classmethod 
    def icon_trophy(cls):
        return cls.ICON_TROPHY
    
    @classmethod 
    def icon_medal(cls):
        return cls.ICON_MEDAL
    
    @classmethod 
    def icon_peace(cls):
        return cls.ICON_PEACE
    
    @classmethod 
    def icon_heart_eyes(cls):
        return cls.ICON_HEART_EYES
    
    @classmethod 
    def icon_fireworks(cls):
        return cls.ICON_FIREWORKS
    
    @classmethod 
    def icon_gift(cls):
        return cls.ICON_GIFT
    
    @classmethod 
    def icon_party_popper(cls):
        return cls.ICON_PARTY_POPPER
    
    @classmethod 
    def icon_fingerpointing(cls):
        return cls.ICON_FINGERPOINTING
    
    @classmethod     
    def icon_help(cls):
        return cls.ICON_SOS
    
    @classmethod
    def icon_fuel(cls):
        return cls.ICON_FUEL
    
    @classmethod
    def icon_money(cls):
        return cls.ICON_MONEY
    
    @classmethod
    def icon_bomb(cls):
        return cls.ICON_BOMB
    
    @classmethod
    def icon_apple(cls):
        return cls.ICON_APPLE
    
    # -----------------------------------------------------
    
    @classmethod     
    def success(cls, text):
        cls.SUCCESS = f"{cls.icon_check()}  {cls.style('[SUCCESS] : ', cls.bold)}"
        cls.echo(f"{cls.style(cls.SUCCESS, cls.green)}{cls.style(text, cls.green)}")
    
    @classmethod 
    def error(cls, text):
        cls.ERROR = f"{cls.icon_error()} {cls.style('[ERROR] : ', cls.bold)}"
        cls.echo(f"{cls.style(cls.ERROR, cls.light_red)}{cls.style(text, cls.light_red)}")
    
    @classmethod 
    def info(cls, text):
        cls.INFO = f"{cls.icon_info_circle()} {cls.style( '[INFO] : ', cls.bold)}"
        cls.echo(f"{cls.style(cls.INFO, cls.blue)}{cls.style(text, cls.light)}")
    
    @classmethod      
    def warning(cls, text):
        cls.WARNING = f"{cls.icon_warning()}  {cls.style( '[WARNING] : ', cls.bold)}"
        cls.echo(f"{cls.style(cls.WARNING, cls.yellow)}{cls.style(text, cls.yellow)}")
    
    @classmethod 
    def danger(cls, text):
        cls.CRITICAL = f"{cls.icon_stop()} {cls.style('[CRITICAL] : ', cls.bold)}"
        cls.echo(f"{cls.style(cls.CRITICAL, cls.red)}{cls.style(text, cls.red)}")
    
    @classmethod      
    def comment(cls, text):
        cls.COMMENT = f"{cls.icon_info()} "
        cls.echo(f"{cls.style(cls.COMMENT, cls.light)}{cls.style(text, cls.black)}")
    
    @classmethod      
    def description(cls, text):
        cls.echo(f"{cls.style(text, cls.black, cls.italic)}")
    
    @classmethod 
    def question(cls, text):
        cls.QUESTION = f"{cls.style(': ', cls.bold)}{cls.icon_question()}" 
        cls.echo(f"{cls.style(text, cls.light)} {cls.style(cls.QUESTION, cls.grey)}")
    
    @classmethod      
    def debug(cls, text):
        cls.DEBUG = f"{cls.icon_lightbulb()} {cls.style('[DEBUG] : ', cls.bold)}"
        cls.echo(f"{cls.style(cls.DEBUG, cls.black)}{cls.style(text, cls.light)}")
    
    @classmethod      
    def help(cls, text):
        cls.HELP = f"{cls.icon_lightbulb()} {cls.style('[HELP] : ', cls.bold)}" 
        cls.echo(f"{cls.style(cls.HELP, cls.cyan)}{cls.style(text, cls.cyan)}")
    
    
    @classmethod 
    def highlight(cls, text):
        cls.echo(f"{cls.style(text, cls.bold, cls.yellow)}")
    
    @classmethod 
    def muted(cls, text):
        cls.echo(f"{cls.style(text, cls.grey)}")
    
    @classmethod 
    def emphasize(cls, text):
        cls.echo(f"{cls.style(text, cls.italic, cls.green)}")
    
    @classmethod 
    def title(cls, text: str, icon="≖", width=width):
        border = icon * width 
        cls.echo(f"{cls.style(border, cls.bold, cls.light)}")
        cls.echo(f"{cls.style(cls.uppercase(text).center(width), cls.bold, cls.light)}")
        cls.echo(f"{cls.style(border, cls.bold, cls.light)}")
 
    
    @classmethod
    def subtitle(cls, text: str, icon="⋆", width=width):
        cls.echo(f"{cls.style(text.center(width, icon), cls.bold, cls.grey, cls.underline)}")
    
    @classmethod      
    def label(cls, text):
        cls.echo(cls.style(text, cls.light))
    
    @classmethod      
    def quote(cls, text, author="Unknown"):
        cls.echo(f"{cls.style('“', cls.magenta)}{cls.style(text,cls.grey, cls.italic)}{cls.style('”', cls.magenta)} - {cls.style(author, cls.light, cls.underline)}")

    @classmethod
    def banner(cls, text:str, width=width, char='*'):
        border = char * width
        cls.echo(cls.style(border, cls.bold, cls.light))
        cls.echo(cls.style(text.center(width), cls.bold, cls.light))
        cls.echo(cls.style(border, cls.bold, cls.light))
    
    @classmethod      
    def style(cls, text, *styles): 
        styles = [style() if callable(style) else str(style) for style in styles]
        return f"{''.join(styles)}{text}{cls.reset()}"
    
    @classmethod      
    def echo(cls, text="", **kwargs):
        end=kwargs.get("end", None)
        flush=kwargs.get("flush", False) 
        print(text, end=end, flush=flush)
    
    @classmethod      
    def uppercase(cls, text:str):
        return text.upper()
    
    @classmethod 
    def lowercase(cls, text:str):
        return text.lower()
    
    
    @classmethod      
    def ascii_art(cls, art):
        cls.echo(cls.style(art, cls.green))
    
    @classmethod 
    def animate(cls, text, speed=0.1):
        for char in text:
            cls.echo(char, end='', flush=True)
            time.sleep(speed)
        cls.echo()
    
    @classmethod     
    def center(cls, text:str, width=width):
        cls.echo(f"{cls.style(text.center(width), cls.bold)}") 
    
    @classmethod      
    def progress(cls, step, total=100, **kwargs): 
        color = kwargs.get('color', cls.green) 
        pattern = kwargs.get('pattern', 'bars') 
        patterns = { 
            'bars':['|', '/', '-', '\\'],
            'bars_dots':['⋮', '⋰', '⋯', '⋱'],
            'dots': ['.', '..', '...'],  
            'circles': ['◐', '◓', '◑', '◒'],   
            'blocks': ['▁', '▂', '▃', '▄', '▅', '▆', '▇', '█'],
            'loading':['◜','◝','◞','◟'],  
        }
        pattern = patterns[pattern]
        step = max(1, min(step, total))   
        margin = max(len(symbol) for symbol in pattern) 
        for progress in range(0, total + 1, step):
            symbol:str = pattern[int(progress/step) % len(pattern)]
            symbol = symbol.ljust(margin)
            percent = (progress / total) * 100
            print(f"\r{cls.style(symbol, color)} {percent:.0f}%", end="")
            time.sleep(0.1)
        cls.echo() 

 
    @classmethod
    def progress_bar(cls, step, total=100, width=50, **kwargs):
        color = kwargs.get('color', cls.green) 
        progress = 0
        step = max(1, min(step, total)) 
        for progress in range(0, total + 1, step):
            progress = min(progress + step, total)  
            percent = (progress / total) * 100
            filled = int(width * progress / total)
            bar = '█' * filled + '░' * (width - filled)
            print(f"\r{cls.style(bar, color)} {percent:.0f}%", end="")
            time.sleep(0.1)
        cls.echo() 
 

    @classmethod          
    def limit(cls, text, length=30, suffix="..."):
        if len(text) > length:
            cls.echo(cls.style(text[:length] + suffix, cls.light))
        else:
            cls.echo(cls.style(text, cls.light))

    
    # @classmethod 
    # def text_to_speech(cls, text):
    #     import pyttsx3
    #     engine = pyttsx3.init()
    #     engine.say(text)
    #     engine.runAndWait()

    
    @classmethod 
    def wrap(cls, text, width=width):
        import textwrap
        text = textwrap.fill(text, width)
        return text

    
    @classmethod
    def table(cls, data, **kwargs): 
        """Generates a textual representation of a formatted table.

        Arguments:
            **kwargs:
                - `data` (list of dict): A list of dictionaries representing table rows.
                Each dictionary contains key-value pairs corresponding to columns (default: empty list).
                - `keys` (list of str): List of keys to display as columns.
                If None, all keys found in the `data` dictionaries are used.
                - `margin` (int): Number of spaces between columns (default: 3).
                - `icon` (str): Icon or separator used to draw the table border (default: "-").
                - `color_header` (str): Color used for the table header (default: "grey").
                - `color_rows` (str): Color used for the table rows (default: "light").
                - `color_border` (str): Color used for the border (default: "grey").
                - `display` (bool): Whether to display the table or return it as a string (default: False).

        Returns:
            str: A string representing the formatted table (if `display` is False).
        """
        if not data:
            return cls.warning("Aucune donnée dans la table")
        if isinstance(data, dict):
            keys = kwargs.get('keys', list(data.keys()))  # Default to dictionary keys
            data = [data]
        else:
            keys = kwargs.get('keys', None)


        data = list(data)
        margin = kwargs.get('margin', 3)
        icon = kwargs.get('icon', "-")
        color_header = kwargs.get('color_header', cls.grey)
        color_rows = kwargs.get('color_rows', cls.light)
        color_border = kwargs.get('color_border', cls.grey)
        display = kwargs.get('display', False)

        if keys:
            head = keys
        else:
            head = data[0].keys()

        width = {key: max(len(key), max(len(str(row[key])) if key in row else 0 for row in data)) + margin for key in head}

        def border():
            return cls.style(icon * (sum(width.values()) + len(width) - (1 + margin)), color_border)

        header = cls.style(" ".join([f"{key:<{width[key]}}" for key in head]), color_header, cls.bold)
        body = "\n".join(
            cls.style(" ".join([f"{row[key]:<{width[key]}}" for key in head]), color_rows)
            for row in data
        )

        table = f"{header}\n{border()}\n{body}\n{border()}"

        if display:
            cls.echo(header)
            cls.echo(border())
            for row in data:
                cls.echo(cls.style(" ".join([f"{row.get(key, ''):<{width[key]}}" for key in head]), color_rows))
            cls.echo(border())
        else:
            return table
  
    
    @classmethod
    def list(cls, data, **kwargs):
        """Generates a textual representation of a formatted list.

        Arguments:
            **kwargs:
                - `data` (list of dict): A list of dictionaries representing list rows.
                Each dictionary contains key-value pairs corresponding to columns (default: empty list).
                - `margin` (int): Number of spaces between columns (default: 0).
                - `icon` (str): Icon or separator used to draw the list border (default: "-").
                - `color` (str): Color used to style the list (default: "cyan").
                - `numbered` (bool): Whether the list should be numbered (default: False).
                - `inline` (bool): Whether the list should be displayed inline (default: False).
                - `separator` (str): Separator line to use between items (default: None).
                - `display` (bool): Whether to display the list or return it as a string (default: False).

        Returns:
            str: A string representing the formatted list (if `display` is False).
        """
        if not data:
            return cls.warning("Aucune donnée dans la liste")  

        if isinstance(data, dict):
            data = [f"{key}: {value}" if value else key for key, value in data.items()]
        data = list(data)

        margin = kwargs.get('margin', 0)
        icon = kwargs.get('icon', "")
        color = kwargs.get('color', cls.cyan)
        numbered = kwargs.get('numbered', False)
        inline = kwargs.get('inline', False)
        separator:str = kwargs.get('separator', " ")
        display = kwargs.get('display', False)

        lists = []
        if numbered:
            for index, item in enumerate(data, start=1):
                lists.append(f"{index:<{margin}}. {item}")
        else:
            for item in data:
                lists.append(f"{icon:<{margin}}{item}")

        if inline:
            formatted_list = cls.style((separator).join(lists), color)
        else:
            formatted_list = "\n".join(
                [cls.style(item, color) + (f"\n{cls.style(separator * cls.width, cls.grey)}" if separator else "")
                for item in lists]
            )

        if display:
            cls.echo(formatted_list)
        else:
            return formatted_list

    @classmethod
    def textarea(cls, placeholder="textarea: ", end="\n"):
        print(placeholder, end='', flush=True)
        textarea = []

        while True:
            text = input()
            if text == "":
                if textarea and textarea[-1] == "":
                    break
                else:
                    textarea.append("")
            else:
                textarea.append(text)
                    
        output = end.join(textarea)
        if output.endswith(end):
            output = output[:-len(end)]
        return output

    
    
    @classmethod      
    def password(cls, placehoder="password : ", **kwargs):
        cls.echo(placehoder, end='', flush=True)
        password = '' 
        while True:
            event = keyboard.read_event(suppress=True)
            if event.event_type == 'down': 
                char = event.name
                if char == 'enter':
                    cls.echo() 
                    break
                elif char == 'backspace':
                    if len(password) > 0:
                        password = password[:-1]
                        cls.echo('\b \b', end='', flush=True)
                elif len(char) == 1:
                    password += char
                    cls.echo('*', end='', flush=True)
        return password
    
    @classmethod 
    def input(cls, placehoder="", **kwargs):  

        value = kwargs.get('value', "")     
        options:dict = kwargs.get('options', {})     
        choices = ""    
        type = kwargs.get('type', 'text')  
        min_len = kwargs.get('min_len', None)  
        max_len = kwargs.get('max_len', None)  
        min = kwargs.get('min', None)  
        max = kwargs.get('max', None)  
        required = kwargs.get('required', False)   
        default = kwargs.get('default', "")        
        accept:str = kwargs.get('accept', 'yes')
        accept_action = kwargs.get('accept_action', None)
        reject:str = kwargs.get('reject', 'no') 
        reject_action = kwargs.get('reject_action', None) 
        prompt = kwargs.get("prompt", ": ")

        action = input
        icon = cls.icon_arrow_right()

        if type =="email":
            icon = cls.icon_enveloppe()

        elif type == "password": 
            icon = cls.icon_lock()
            action = cls.password
            
        elif type in ("tel", "phone"):
            icon = cls.icon_phone()
            
        elif type == "address":
            icon = cls.icon_location()
            
        elif type == "url":
            icon = cls.icon_globe()
            
        elif type == "search":
            icon = cls.icon_search()
            
        elif type == "date":
            icon = cls.icon_calendar()
            
        elif type == "number":
            icon = cls.icon_number()
            
        elif type in ("textarea", "message"):
            icon = cls.icon_file()
            action = cls.textarea

        elif type in ("select", "option"):
            icon = cls.icon_arrow_down() 
        
        elif type in ("confirmation", "confirm", "checkbox", 'dialog'):  
            icon = f"{cls.icon_check()} |{cls.icon_error()}"
            options = {accept:"", reject:""}

        if value:  
            default = f" [{cls.style(value, cls.grey)}]"

        if options: 
            choices = f" ({cls.list(options, inline=True, separator="/")})"

        result = action(f"{cls.style(f"{icon} {placehoder}{choices}{default}{prompt}", cls.light)}") or value  

        if required:
            while not result:
                cls.warning("This field is required.")
                return cls.input(placehoder, **kwargs)

        if max_len:
            if len(str(result)) > max_len:
                cls.warning(f"Input exceeds maximum length of {max_len} characters.")
                return cls.input(placehoder, **kwargs)
        if min_len:
            if len(str(result)) < min_len:
                cls.warning(f"Input is below the minimum length of {min_len} characters.")
                return cls.input(placehoder, **kwargs) 
            
        if min:
            if float(result) < float(min):
                cls.warning(f"Input is below the minimum value of {min}.")
                return cls.input(placehoder, **kwargs)
        if max:
            if float(result) > float(max):
                cls.warning(f"Input exceeds the maximum value of {max}.")
                return cls.input(placehoder, **kwargs)   

        if options:
            if result not in options:
                cls.warning(f"Invalid input. Please enter one of the following options: {', '.join(options)}.")
                return cls.input(placehoder, **kwargs) 
            if result.lower() == accept.lower():
                if accept_action:
                    accept_action()
                return True
            elif result.lower() == reject.lower():
                if reject_action:
                    reject_action()
                return False
        return result