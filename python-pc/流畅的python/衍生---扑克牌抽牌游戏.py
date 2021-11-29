import collections
import random
import time
#创建一个名为Card的元组子类，这里里面和外面的名字都为Card，但是外面的Card是接收这个创建的元组子类，里面的Card是输出的时候元组前面跟的名字
Card = collections.namedtuple('Card', ['rank', 'suit'])
#print(type(Card))
class FrenchDeck:
#模拟纸牌中所有数字，返回值为字符串，存在一个名为ranks的列表中
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    #print(type(ranks))
#模拟纸牌中的方片，黑桃梅花和红心，存在一个名为suits的列表中
    suits = 'spades diamonds clubs hearts'.split()
    #print(type(suits))
    def __init__(self):
#进行赋值操作，注意这里的写法，两个for，Card产生的是元组，而列表推导式产生的是列表，所以实际上是把元组依次存在列表中
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
        #print(type(self._cards))
        #print(type(self._cards[0].rank))
        #print(self._cards[1].rank)
        #print(self._cards)
#这个就是len方法，使用len（对象名）的时候就会自动调用这里的，帮你计算对象个数
    def __len__(self):
        return len(self._cards)
#这个是__getitem__方法，使用对象名[下标]这样的时就会调用这个方法
    def __getitem__(self, position):
        return self._cards[position]
    def __str__(self):
        return ("这个是 str的方法")
    def bidaxiao(self,c1,c2):
        suit_value=dict(spades=3,hearts=2,diamonds=1,clubs=0)
        #print(suit_value)
        if c1.suit==c2.suit:
            print("花色一样，进行点数比值")
            time.sleep(1)
            c1_value=self._cards.index(c1)
            c2_value=self._cards.index(c2)
            if c1_value>c2_value:
                print("C1比C2大")
            else:
                print("C1比C2小")
        else:
            print("进行花色比较")
            time.sleep(1)
            c1=suit_value[c1.suit]
            c2=suit_value[c2.suit]
            if c1>c2:
                print("C1比C2大")
            else:
                print("C1比C2小")
#这里就是创建对象了，实际上就是每张牌被包裹在元组中，然后元组被包裹在列表中，因为有__getitem__这个方法在，所以可以通过对象名[下标]
#的方法来访问对应的牌，如果只是显示花色或者值，那么就是对象名[下标].rank|suit这样来访问
if __name__ == '__main__':
    deck = FrenchDeck()
    c1=random.choice(deck)
    print("抽第一张牌，为{}".format(c1))
    c2 = random.choice(deck)
    print("抽第二张牌，为{}".format(c2))
    deck.bidaxiao(c1,c2)
