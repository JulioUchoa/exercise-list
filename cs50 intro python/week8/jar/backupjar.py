class Jar:
    def __init__(self, capacity=0):        # ok
        self.capacity = capacity
        self.size = 0

    def __str__(self):                      # ok
        bis = ""
        if self.size == 0:
            return "The Jar is Empty"
        for _ in range(0, self.size):
            bis += '🍪'
        return bis

    def deposit(self, n):                   # ok
        self.size += n
        if self.size < 0 or self.size > int(self.capacity):
            raise ValueError

    def withdraw(self, n):                  # ok
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
        if int(capacity) > 12:
            raise ValueError
        self._capacity = capacity




def main():
    j = input("Which jar capacity you want to set?: ")
    if not int(j) or int(j) > 12 or int(j) < 0:
        raise ValueError
    jar = Jar(j)
    while True:
        s = input("press 'd' for deposit or 'w' for withdraw biscuits from the Jar, otherwise if you want to quit press '0': ").lower()
        if s == 'd':
            jar.deposit(int(input("n: ")))
            print(jar)

        if s == 'w':
            jar.withdraw(int(input("n: ")))
            print(jar)

        elif s == '0':
            print(f"number of biscuits in the har: {jar.size}")
            print(f"Jar capacity: {jar.capacity}")

            return False

if __name__ == '__main__':
    main()