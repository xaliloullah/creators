from utils.creator.src.core import Storage, Path, File, Task

class Cache :
    path = Path.cache

    @classmethod
    def make(cls, source, destination, mode="default"): 

        path = File.join_path(cls.path, destination)

        if mode == 'import':
            content = File.list_dir(source, endswith='.py')  
            data = Task.build_import(source, *content)
        else:
            data = File.load(source)

        cache = Storage(path, absolute=False, format='auto') 
        cache.save(data)


    @classmethod
    def add(cls, **kwargs):
        source=kwargs.get('source', None)
        destination=kwargs.get('destination', None) 
        path = File.join_path(cls.path, destination)
        cache = Storage(path, absolute=False, format='py') 
        content = File.list_dir(source, endswith='.py')  
        cache.create(Task.build_import(source, *content))

    