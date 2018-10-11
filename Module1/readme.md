# Interactive Mode

_ : similar to an ans calculator, only available in the interactive mode. 
It's possible to use this as a calculator or probe small concepts,
using arrows you can search for all the command or instructions history. 

It's prefered to use the python website for more information, but if you want quick info type in the interactive mode : 
`help(cmd)`
Using the python interpreter, we're going to check the estimated arrival times of CTABUS in chicago. 

```python 
import urllib.request
u = urllib.request.urlopen('http://ctabustracker.com/bustime/map/getStopPredictions.jsp?stop=14787&route=22')
data = u.read()
print(data)	# print an xml response
from xml.etree.ElementTree import XML 
doc = XML(data)
for pt in doc.findall('.//pt'):
	print(pt.text)
```

It's possible to create a debug session with the current python script, launching `python3 -i pythonscript.py`
if you want to go more deeper in your debug session you could import pdb  :
```python 
import pdb
pdb.pm()
```

If you want to  set a manual break point : 
```python 
import pdb; pdb.set_trace() 	#a manual break point this will launch debugger
```

Check the pdb documentation for the kind of steps that are available
