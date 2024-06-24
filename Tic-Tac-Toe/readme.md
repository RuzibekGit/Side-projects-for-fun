``` python
from gui import gui_for_terminal
import time
from random import randint

count = 1
y = 1
while True:
    x = randint(1,10)
    if x == 10:
        for i in range(1,10):
            gui_for_terminal(i, 0)
            time.sleep(0.01)


    gui_for_terminal(x, randint(1,2))
    count += 1
    y += 1
    if y == 3:
        y = 1
    if count == 9:
        1
    time.sleep(0.5)

```

### Hello world!..

``` html
<h1>Hello world!</h1>
```

