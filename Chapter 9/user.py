class User():
    """Create user attributes"""
    def __init__(self,first_name,last_name,height,sex,race):
        
        """Initialize user attributes"""
        self.first_name = first_name
        self.last_name = last_name        
        self.height = height
        self.sex = sex
        self.race = race
        
    def describe_user(self):
        """Print summary of user"""
        print("\nHere's a brief summary of " + self.first_name.title() + ":")
        print("Name: " + self.first_name.title() + " " + self.last_name.title())
        print("Height: " + self.height)
        print("Sex: " + self.sex)
        print("Race: " + self.race)
        
    def greet_user(self):
        """Print a greeting to user."""
        print('\n' + self.first_name.title() + ' ' +  self.last_name.title() + 
              ' welcome to the village.')

class Admin(User):
    def __init__(self,first_name,last_name,height,sex,race):
        super().__init__(first_name,last_name,height,sex,race)   
        
        self.privileges = Privileges()
            
            
class Privileges():
    def __init__(self, privileges=[]):
        self.privileges = privileges
        
    def show_privileges(self):
        """Print list of privilages"""
        print("\nPrivileges:")
        if self.privileges:
            print('\nAdding privileges...')
            for privilege in self.privileges:
                print('- ' + privilege)
            print('\nUser now has privileges.')    
        else:
            print('This user has no privileges')