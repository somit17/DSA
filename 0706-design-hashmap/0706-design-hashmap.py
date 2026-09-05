class MyHashMap:
    def __init__(self):
        self.SIZE = 1009                  # prime → fewer modular collisions
        self.buckets = [[] for _ in range(self.SIZE)]

    def _hash(self, key):
        return key % self.SIZE

    def put(self, key, value):
        bucket = self.buckets[self._hash(key)]
        for i, (k, _) in enumerate(bucket):      # 1. same bucket?
            if k == key:                  # key already exists → update,
                bucket[i] = (key, value)  #   don't append a duplicate
                return
        bucket.append((key, value))       # 2. new key → chain it

    def get(self, key):
        bucket = self.buckets[self._hash(key)]
        for k, v in bucket:
            if k == key:
                return v
        return -1

    def remove(self, key):
        bucket = self.buckets[self._hash(key)]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                return