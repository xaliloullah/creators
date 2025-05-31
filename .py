import json
import os

class Memory:
    def __init__(self, file_path="memory.json"):
        self.file_path = file_path
        self.data = self._load_memory()
    
    def _load_memory(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r", encoding="utf-8") as file:
                return json.load(file)
        return {}
    
    def save_memory(self):
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(self.data, file, indent=4, ensure_ascii=False)
    
    def add_info(self, key, value, importance=1):
        self.data[key] = {"value": value, "importance": importance}
        self.save_memory()
    
    def get_info(self, key):
        return self.data.get(key, {}).get("value", None)
    
    def remove_info(self, key):
        if key in self.data:
            del self.data[key]
            self.save_memory()
    
    def list_info(self):
        return {k: v["value"] for k, v in self.data.items()}
    
# Exemple d'utilisation
if __name__ == "__main__":
    memory = Memory()
    memory.add_info("nom", "Alice", importance=3)
    memory.add_info("age", 25)
    print(memory.get_info("nom"))  # Alice
    print(memory.list_info())  # {'nom': 'Alice', 'age': 25}
