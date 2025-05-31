class Translator: 
    
    @classmethod
    def setup(cls, target, source = "auto"):
        cls.target = target
        cls.source = source 
        try:
            from deep_translator import GoogleTranslator
            cls.translator = GoogleTranslator(cls.source, cls.target)
        except:
            raise ImportError("GoogleTranslator module is not installed.")

    @classmethod
    def translate(cls, text:str, target="fr", **kwargs):
        source = kwargs.get("source", "auto")   
        cls.setup(target, source)
        return cls.translator.translate(text)
    
    @classmethod
    def translate_batch(cls, texts:list, target="fr", **kwargs):
        cls.source = kwargs.get("source", "auto")
        cls.target = target
        return [cls.translator.translate(text) for text in texts]
    
    # @classmethod
    # def detect_language(cls, text: str):
    #     return cls.translator.translate_batch(text)

    @classmethod
    def supported_languages(cls):
        return cls.translator.get_supported_languages(as_dict=True)