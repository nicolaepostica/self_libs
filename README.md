# self_libs


## Installation

```shell
pip install git+https://github.com/nicolaepostica/self_libs.git 
```

Utils for Parsing

```python
from sl.common import headers, json_dump, json_load

data = {'name': 'python'}
json_dump(data, "data.json")
json_load("data.json")

print(headers)
```

```python
from sl.mouse import MouseControls

mc = MouseControls()
mc.move([100, 100])
mc.move_click([100, 100], wait=1)
mc.move_relative(100, 100)
mc.click(wait=1)
print(mc.get_position())
mc.tab(2)
mc.enter()
```
