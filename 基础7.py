class Goods:
    __goods_number = int
    __goods_name = str
    __goods_price = int
    __goods_total = int
    __goods_left = int

    def __init__(self):  # 构造函数传参，但是不设参(bushi)
        self.__goods_number = 1
        self.__goods_name = "小黄老师"
        self.__goods_price = 114514
        self.__goods_total = 514
        self.__goods_left = 114

    def display(self):
        print("商品编号:", self.__goods_number)
        print("商品名称:", self.__goods_name)
        print("商品价格:", self.__goods_price)
        print("商品总数量:", self.__goods_total)
        print("商品剩余数量:", self.__goods_left)

    def income(self):
        return (self.__goods_total - self.__goods_left) * self.__goods_price

    def setdeta(self, Goods):
        self.__goods_number = Goods.__goods_number
        self.__goods_price = Goods.__goods_price
        self.__goods_left = Goods.__goods_left
        self.__goods_total = Goods.__goods_total
        self.__goods_name = Goods.__goods_name


class Main:
    good1 = Goods()
    good1.display()
    print("\n收入为:", good1.income())
    # good1.setdeta(good2)
