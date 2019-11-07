import json
# pip install pygal_maps_world 原来的pygal.i18n文件
from pygal_maps_world.i18n import COUNTRIES
# import pygal_maps_world.maps 原来是 pygal.Worldmap()
import pygal_maps_world.maps
from pygal.style import RotateStyle
# 加亮颜色主题
from pygal.style import LightColorizedStyle

# 获取两个字母国别码
# for country_code in sorted(COUNTRIES.keys()):
#     print(country_code, COUNTRIES[country_code])


def get_country_code(country_name):
    """根据指定国家，返回Pygal使用的两个字国别码"""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    # 如果没有找到指定国家，就返回 None
    return None


# 将数据加载到一个列表中
filename = "population_data.json"
with open(filename) as f:
    pop_data = json.load(f)

# 打印每个国家2010年的人口数量
# 人口字典
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            print(code + ": " + str(population))
            cc_populations[code] = population
        else:
            print("Error -" + country_name)

# 根据人口数量将所有国家分成三组
cc_pop_1, cc_pop_2, cc_pop_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pop_1[cc] = pop
    elif pop < 1000000000:
        cc_pop_2[cc] = pop
    else:
        cc_pop_3[cc] = pop

# 设置地图样式
# vm_style = RotateStyle('#336699')
vm_style = RotateStyle('#336699', base_style=LightColorizedStyle)
vm = pygal_maps_world.maps.World(style=vm_style)
vm.title = 'World Population in 2010, by Country'
# vm.add('2010', cc_populations)
vm.add('0-10m', cc_pop_1)
vm.add('10m-1bn', cc_pop_2)
vm.add('>1bn', cc_pop_3)
vm.render_to_file('world_population.svg')


