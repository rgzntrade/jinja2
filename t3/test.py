from jinja2 import Environment, PackageLoader

# 定义一个函数，将字符串转换为大写
def uppercase(s):
    return s.upper()

# 创建一个加载器，jinja2会从't3'包中的'templates'文件夹中加载模板
loader = PackageLoader('t3', 'templates')

# 通过提供加载器，创建一个环境
env = Environment(loader=loader)

# 添加自定义过滤器
env.filters['uppercase'] = uppercase

# 加载模板
template = env.get_template('hello.html')

# 渲染模板
print(template.render(name='John Doe'))

