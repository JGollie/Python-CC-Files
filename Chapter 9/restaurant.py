"""Class describing a restaurant."""

class Restaurant():
    """Building my restaurant."""
    
    def __init__(self,name,cuisine):
        """Initianlize restaurant name and type of food."""
        
        self.name = name
        self.cuisine = cuisine
        
    def describe_restaurant(self):
        """Print message describing the restaurant."""
        
        message = self.name.title() + " serves " + self.cuisine.title() + " food."
            
        return message
        
    def open_restaurant(self):
        """Print message opening restarant"""
        
        print(self.name.title() + " is open for business.") 