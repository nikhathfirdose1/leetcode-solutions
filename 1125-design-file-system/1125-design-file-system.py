class FileSystem:

    def __init__(self):

        self.hm = {"/" : -1}
        

    def createPath(self, path: str, value: int) -> bool:

        if path == "/" or len(path) == 0 or path in self.hm:
            return False

        i = path.rfind("/")
        parent = path[:i] if i >0 else "/"

        if parent not in self.hm:
            return False

        self.hm[path] = value
        return True
        

    def get(self, path: str) -> int:

        if path in self.hm:
            return self.hm[path]
        else:
            return -1
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)