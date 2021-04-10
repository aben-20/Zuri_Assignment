class Budget:
    
    def __init__(self, category: str):
        
        self.name = category
        
        self.total = 0

    def deposit(self, amount):
        
        self.total += amount
        
    def withdraw(self, amount):
        
        if self.check_funds(amount):
            
            self.total -= amount
            
            return True
        
        else:
            
            return False        

    def get_balance(self):
        
        return self.total
    
    def check_funds(self, amount):
        
        return True if self.total - amount >= 0 else False

    def transfer(self, amount, dest_category):
        
        if self.check_funds(amount):
            
            try:
                
                self.withdraw(amount, f"Transfer to {dest_category.name}")
                
                dest_category.deposit(amount, f"Transfer from {self.name}")
                
                return True
            
            except:
                
                raise ValueError("Create category for destination!")
            
        return False
   
