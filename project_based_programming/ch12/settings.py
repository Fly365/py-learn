# 设置类，修改值，只需要修改该文件，而无需查找散步在文件不同设置
class Settings():
    """存储<<外星人入侵>>的所有设置类"""

    def __init__(self):
        """初始化游戏设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # 飞船的设置
        self.ship_speed_factor = 1.5