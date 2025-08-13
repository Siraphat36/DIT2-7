a = (input("Your Name :"))
b = int(input("AD Born :"))
from datetime import datetime
current_year = datetime.now().year
pi = (current_year - int(b))
print(a,b,pi)