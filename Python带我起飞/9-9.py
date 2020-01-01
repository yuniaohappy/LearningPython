class WithClass:
    def __enter__(self):
        print('__enter__')
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__')
        print('type: ',exc_type)
        print('value: ',exc_val)
        print('trace: ',exc_tb)

    def work(self):
        print('自定义 with 语句测试！！！')
        raise Exception('异常测试！！！')

with WithClass() as myclass:
    myclass.work()
