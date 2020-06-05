import pickle

obj = ['foo', 'bar']
f = open('store.pckl', 'wb')
pickle.dump(obj, f)
f.close()

f = open('store.pckl', 'rb')
obj2 = pickle.load(f)
f.close()
print(obj2)
