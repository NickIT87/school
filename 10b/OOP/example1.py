class Car:
    model = "Hundai"
    repair_history = ['28.11.22', '30.11.22']
    __usage_history: str = None

    def __init__(self, use_data: str = "No history"):
        print("init")
        self.__usage_history = use_data

    def get_last_data_repair(self):
        return self.repair_history[1:]

    def get_usage_history(self):
        return self.__usage_history

    def set_usage_history(self, history: str):
        self.usage_history = history

car1 = Car()
print(car1.get_usage_history())