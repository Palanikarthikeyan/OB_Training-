class Delivery:
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
    def calculate_cost(self):
        pass

class standard_delivery(Delivery):
    def calculate_cost(self):
        return self.weight * self.distance
    def update_status(self, status, time_updated):
        return super().update_status(status, time_updated)
    
class express_delivery(Delivery):
    def calculate_cost(self):
        return self.weight * self.distance * 1.5
    def update_status(self, status, time_updated):
        return super().update_status(status, time_updated)
    

std_obj = standard_delivery("STD001",10,5)
exp_obj = express_delivery("EXP001",10,5)

std_obj.start_delivery()
std_obj.update_status("Out for Delivery","10:05 AM")
print("Standard Cost:",std_obj.calculate_cost())

exp_obj.start_delivery()
exp_obj.update_status("Dispatched","10:15 AM") 
print("Express Cost:",exp_obj.calculate_cost())
       