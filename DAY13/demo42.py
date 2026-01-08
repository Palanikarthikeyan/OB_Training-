from abc import ABC,abstractmethod
class Delivery(ABC):
    def __init__(self,package_id,weight,distance):
        self.package_id = package_id
        self.weight = weight
        self.distance = distance
        self.status = "pending"
    def start_delivery(self):
        self.status = "In Process"
        print(f'Package {self.package_id} delivery started')
    def update_status(self,status,time_updated):
        self.status = status
        print(f"{time_updated} Package {self.package_id} status updated to:{self.status}")
    @abstractmethod
    def calculate_cost(self):
        pass

class standard_delivery(Delivery):
    def calculate_cost(self):
        return self.weight * self.distance
        
class express_delivery(Delivery):
    def calculate_cost(self):
        return self.weight * self.distance * 1.5

std_obj = standard_delivery("STD001",8,10)
exp_obj = express_delivery("EXP001",8,10)

std_obj.start_delivery()
std_obj.update_status("Out for Delivery","9:35 AM")
print("Standard Cost:",std_obj.calculate_cost())

exp_obj.start_delivery()
exp_obj.update_status("Dispatched","09:45 AM") 
print("Express Cost:",exp_obj.calculate_cost())