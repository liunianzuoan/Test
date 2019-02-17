"""
反射

静态----运行前，如果要调用类的属性或者是方法，就需要实例化它的对象
动态---运行时，我就获取类的属性或者方法，甚至更改它的属性或者是方法
"""

class Girls:

    single = False
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def singer(self):
        print(self.name+'会唱歌')

if __name__ == '__main__':
    g = Girls('mongo',18)
    print(g.name)
    g.singer()

    setattr(Girls,'hobby','swimming')  # 给类或者是实例对象动态的去添加属性或者是方法
    # 如果只给实例对象去添加属性，那么久只能通过它的对象去访问属性
    # 如果给类去添加属性，那么可以通过类或者是对象去访问属性
    print(g.hobby)

    print(getattr(Girls,'hobby'))  # 根据属性名获取类的属性,不存在这个属性的话就报错 attribute error错误

    print(hasattr(g,'male')) #判断当前有没有这个属性，有的话返回True，没有的话返回False
    print(hasattr(Girls,'single'))  # 判断是否有这个类属性
    print(hasattr(g,'name'))  # 判断对象是否有这个实例属性

    delattr(g,'name')  # 删除对象属性
    print(g.name)

    delattr(Girls,'single')  # 删除类属性
    getattr(Girls,'single')