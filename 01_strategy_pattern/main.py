"""测试

策略模式：
定义了算法族，分别封装起来，让它们之间可以互相替换
让算法的变化独立于使用算法的客户
"""
from duck import WildDuck, RubberDuck

w = WildDuck()
w.quack()
w.fly()
w.display()

r = RubberDuck()
r.quack()
r.fly()
r.display()
