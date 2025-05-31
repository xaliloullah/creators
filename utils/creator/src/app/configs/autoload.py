from utils.creator.src.core.file import File
from utils.creator.src.core.task import Task

class Autoload:
    pass

    def creating_config(source, destination):
        File.ensure_path_exists(source)
        configs_file = File.list_dir(source, endswith='.py')
        
        content = []
        for config in configs_file:
            content.append(Task.build_import(File.join_path(source, config), "*"))
            
        File.save(destination, "\n".join(content))