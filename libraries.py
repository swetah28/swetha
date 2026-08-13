'''import numpy as nP
x=nP.linspace(1,30,20)
y=nP.sin(x)
print(x)
print(y)

import numpy as np
from bs4 import BeautifulSoup
x=np.linspace(2,20,18)
y=np.tan(x)
print(x)
print(y)
import pandas as pd,matplotlib.pyplot as plt
c=pd.DataFrame({'TeamA':x,'TeamB':y})
' '
print(c)
plt.plot(c['TeamA'],c['TeamB'],marker='^')
plt.title("The Graph")
plt.show()
html="<u1><li>Tamil</li><li>English</li><li>Hindi</li></u1>"
soup=BeautifulSoup (html,'html.parser')
print([li.text for li in soup.find_all('li')])

from scipy.optimize import fsolve
def equation(x):
    return x**2-9
root=fsolve(equation,5)
print("The solution of the equation :",root[0])'''

import numpy as np,pandas as pd,matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from scipy.optimize import fsolve
x=np.linspace(1,20,7)
y=np.sin(x)
print(x)
print(y)
c=pd.DataFrame({'ClassA':x,'ClassB':y})
print(c)
plt.plot(c['ClassA'],c['ClassB'],marker='^')
plt.title("The Shape of the Graph")
plt.show()
html="<u1><li>Name</li><li>Age</li><li>Gender</li><li>strength</li></u1>" 
soup=BeautifulSoup(html,'html.parser')
print([li.text for li in soup.find_all('li')])
def equation(z):
    return z**2-9
some=fsolve(equation,4)
print("The Solution of the equation is :",some[0])



