"""
str() 的输出追求可读性，输出格式要便于理解，适合用于输出内容到用户终端。
repr() 的输出追求明确性，除了对象内容，还需要展示出对象的数据类型信息，适合开发和调试阶段使用。

"""

a = 100
print(a,type(a))
print(str(a),type(str(a)))
print(repr(a),type(repr(a)))