from jinja2 import Template

# 创建一个模板
template = Template('Hello, {{ name }}!')

# 渲染模板
message = template.render(name='World')

print(message)

