# teachersfilter
硕士导师简单筛选
此代码以东南大学能环院为例
使用 xpath  导出为  xlsx

打分
```
def judge_teacher(t):
    g = 0
    if '计算机' in t:
        g += 1
    elif '人工智能' in t:
        g += 6
    elif '软件' in t:
        g += 1
    elif '网络' in t:
        g += 8
    elif '程序' in t:
        g += 1
    elif '数据' in t:
        g += 3
    elif '通信' in t:
        g += 8
    elif '物联网' in t:
        g += 8
    elif '电子' in t:
        g += 1
    elif '自动化' in t:
        g += 1
    elif '智能' in t:
        g += 2
    elif 'python' in t:
        g += 16
    else:
        pass
    return g

```
