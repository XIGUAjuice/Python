import json
import pygal
from pygal.style import RotateStyle, LightColorizedStyle
from country_codes import get_country_code

filename = 'population_data.json'
with open(filename) as f:
    data = json.load(f)

pop_dic = {}
for index in data:
    if index['Year'] == '2010':
        country = index['Country Name']
        population = int(float(index['Value']))
        code = get_country_code(country)
        if code:
            pop_dic[code] = population

pop_dic1, pop_dic2, pop_dic3 = {}, {}, {}
for code, pop in pop_dic.items():
    if pop < 10000000:
        pop_dic1[code] = pop
    elif pop < 1000000000:
        pop_dic2[code] = pop
    else:
        pop_dic3[code] = pop


dark_rotate_style = RotateStyle('#336676', base_style=LightColorizedStyle)
wmap = pygal.maps.world.World(style=dark_rotate_style)
wmap.title = '2010年世界人口分布'
wmap.add('少于1000万', pop_dic1)
wmap.add('1000万--10亿', pop_dic2)
wmap.add('大于10亿', pop_dic3)

wmap.render_to_file('population.svg')
