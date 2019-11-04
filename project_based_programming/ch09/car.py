class Car():

    def __init__(self, make, model, year):
        """初始化汽车属性"""
        self.make = make
        self.model = model
        self.year = year
        # 属性指定默认值
        self.odemeter_reading = 0

    def get_descriptive_name(self):
        """返回简洁描述信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name

    # 通过方法修改属性值
    def update_odometer(self, mileage):
        self.odemeter_reading = mileage

    # 通过方法对属性值进行递增
    def increment_odometer(self, miles):
        self.odemeter_reading += miles
