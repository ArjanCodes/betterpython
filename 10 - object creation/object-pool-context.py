from typing import List

class PoolManager():
    def __init__(self, pool):
        self.pool = pool
    def __enter__(self):
        self.obj = self.pool.acquire()
        return self.obj
    def __exit__(self, type, value, traceback):
        self.pool.release(self.obj)

class Reusable:
    def test(self):
        print(f"Using object {id(self)}")

class ReusablePool:

    def __init__(self, size):
        self.size = size
        self.free: List[Reusable] = []
        self.in_use: List[Reusable] = []
        for _ in range(0, size):
            self.free.append(Reusable())

    def acquire(self) -> Reusable:
        assert len(self.free) > 0
        r = self.free[0]
        self.free.remove(r)
        self.in_use.append(r)
        return r

    def release(self, r: Reusable):
        self.in_use.remove(r)
        self.free.append(r)

# Create reusable pool
pool= ReusablePool(2)

with PoolManager(pool) as r:
    r.test()

with PoolManager(pool) as r2:
    r2.test()