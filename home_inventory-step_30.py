# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: HomeInventory
class UserProfiles:
    def __init__(self):
        self.profiles = {}
        self.current_profile = None
    
    def add_profile(self, name, role="user"):
        if name in self.profiles:
            print(f"Профиль '{name}' уже существует.")
            return False
        self.profiles[name] = {"role": role}
        self.current_profile = name
        print(f"Профиль '{name}' создан и выбран.")
        return True
    
    def switch_profile(self, name):
        if name not in self.profiles:
            print(f"Профиль '{name}' не найден.")
            return False
        self.current_profile = name
        print(f"Переключен на профиль '{name}'.")
        return True
    
    def get_current_profile(self):
        if self.current_profile is None and not self.profiles:
            print("Нет активных профилей.")
            return None
        profile = self.profiles[self.current_profile]
        return {"name": self.current_profile, **profile}
    
    def list_profiles(self):
        if not self.profiles:
            print("Список профилей пуст.")
            return []
        return [{"name": name, "role": data["role"]} for name, data in self.profiles.items()]
