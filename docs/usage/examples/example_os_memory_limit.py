import ray
ray.init(object_store_memory=2100000000)

@ray.remote
def f(x):
    return x * x

futures = [f.remote(i) for i in range(4)]
print(ray.get(futures))