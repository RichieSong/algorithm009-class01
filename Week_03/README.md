## 学习笔记

### 递归模板
```
# Python
def recursion(level, param1, param2, ...): 
    # recursion terminator 
    if level > MAX_LEVEL: 
	   process_result 
	   return 
    # process logic in current level 
    process(level, data...) 
    # drill down 
    self.recursion(level + 1, p1, ...) 
    # reverse the current level status if needed
```


### 回溯模板
```
def backtrack(nums(选择列表),track(路径)):
    # 终止掉价
    if len(nums)==len(track):
        res.append(track[:]) # 将结果的副本保存
    # 去掉不合法的结果，也就是提前剪枝
    if level xxx
        continue
    for i in range(len(nums)):
        track.append()
        backtrack(nums,track)
        res.pop()
    
```
