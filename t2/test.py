from jinja2 import Environment, PackageLoader

# 创建一个加载器，jinja2会从't2'包中的'templates'文件夹中加载模板
loader = PackageLoader('t2', 'templates')

# 通过提供加载器，创建一个环境
env = Environment(loader=loader)

# 加载模板
template = env.get_template('hello.html')

# 渲染模板
print(template.render(name='John Doe'))

