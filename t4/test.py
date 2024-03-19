from jinja2 import Environment, PackageLoader

# 定义一个测试，检查一个字符串是否为大写
def is_uppercase(s):
    return s.isupper()

# 创建一个加载器，jinja2会从't4'包中的'templates'文件夹中加载模板
loader = PackageLoader('t4', 'templates')

# 通过提供加载器，创建一个环境
env = Environment(loader=loader)

# 添加自定义测试
env.tests['uppercase'] = is_uppercase

# 加载模板
template = env.get_template('hello.html')

# 渲染模板
print(template.render(name='JOHN DOE'))

