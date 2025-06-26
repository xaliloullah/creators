import datetime 

class Date:
    
    @staticmethod
    def now():
        return datetime.datetime.now()
    
    @staticmethod
    def today():
        return datetime.date.today()
    
    @staticmethod
    def today_str():
        return Date.today().strftime("%Y-%m-%d")
    
    @staticmethod
    def current_time():
        return Date.now().strftime("%H:%M:%S")
    
    @staticmethod
    def current_datetime():
        return Date.now().strftime("%Y-%m-%d %H:%M:%S")
    
    
    @staticmethod
    def strtotime(date , format="%Y-%m-%d %H:%M:%S.%f"):
        return datetime.datetime.strptime(date, format)
    
    @staticmethod
    def format_date(date, format="%Y-%m-%d"):
        return datetime.datetime.strptime(date,  format)
    
    @staticmethod
    def string_to_date(date_str, format="%Y-%m-%d"):
        return datetime.datetime.strptime(date_str, format)
    
    @staticmethod
    def add(date, days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0):
        
        return date + datetime.timedelta(days=days, seconds=seconds, microseconds=microseconds, milliseconds=milliseconds, minutes=minutes, hours=hours, weeks=weeks)
    
    @staticmethod
    def add_days(date, days): 
        return Date.add(date, days=days)
    
    @staticmethod
    def add_minutes(date, minutes): 
        return Date.add(date, minutes=minutes)
    
    @staticmethod
    def add_seconds(date, seconds): 
        return Date.add(date, seconds=seconds)
    
    @staticmethod
    def add_hours(date, hours): 
        return Date.add(date, hours=hours)
    
    @staticmethod
    def add_weeks(date, weeks):
        return Date.add(date, weeks=weeks) 
    
    @staticmethod 
    def subtract_days(date, days):
        return date - datetime.timedelta(days=days)
 
    @staticmethod
    def is_past(date):
        return date < Date.now()
 
    @staticmethod
    def is_future(date):
        return date > Date.now()
 
    @staticmethod
    def time_of_day():
        hour = Date.now().hour
        if 5 <= hour < 12:
            return "matin"
        elif 12 <= hour < 17:
            return "après-midi"
        elif 17 <= hour < 21:
            return "soir"
        else:
            return "nuit"

    @staticmethod
    # Retourne la différence entre deux dates
    def date_difference(date1, date2):
        return (date1 - date2).days

    # Retourne la date d'un jour spécifique de la semaine (par exemple, le lundi de cette semaine)
    @staticmethod
    def get_weekday_date(weekday):
        today_date = Date.today()
        days_to_subtract = (today_date.weekday() - weekday) % 7
        return today_date - datetime.timedelta(days=days_to_subtract)

    # Exemple : obtenir la date du lundi de la semaine actuelle
    @staticmethod
    def get_monday():
        return Date.get_weekday_date(0)  # 0 pour lundi

    # Exemple : obtenir la date du dimanche de la semaine actuelle
    @staticmethod
    def get_sunday():
        return Date.get_weekday_date(6)  # 6 pour dimanche

    # Retourne le mois actuel sous forme de numéro (1-12)
    @staticmethod
    def current_month():
        return Date.now().month

    # Retourne l'année actuelle
    @staticmethod
    def current_year():
        return Date.now().year
    
    @staticmethod
    def time():
        return datetime.time