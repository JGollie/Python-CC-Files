from user import User

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