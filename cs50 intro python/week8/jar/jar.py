class Jar:
    def __init__(self, capacity=12):        # ok
        self.capacity = capacity
        self.size = 0

    def __str__(self):                      # ok
        bis = ""
        if self.size == 0:
            return bis
        for _ in range(0, self.size):
            bis += '🍪'
        return bis

    def deposit(self, n):                   # ok
        self.size += n
        if self.size < 0 or self.size > int(self.capacity):
            raise ValueError

    def withdraw(self, n):                  # ok
        if n > self.size:
            raise ValueError
        self.size -= n
        if self.size < 0 or self.size > int(self.capacity):
            raise ValueError



    @property # <-- Getter decorator
    def size(self):
        return self._size
    @size.setter # <-- Setter decorator
    def size(self, size):
        self._size = size


    @property
    def capacity(self):
        return self._capacity
    @capacity.setter
    def capacity(self, capacity):
        if int(capacity) > 12 or int(capacity) < 0:
            raise ValueError
        self._capacity = capacity



def main():
    jar = Jar()
    jar.deposit(1)
    print(jar)
    print(jar.capacity)

if __name__ == '__main__':
    main()