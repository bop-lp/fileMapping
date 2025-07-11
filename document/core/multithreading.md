# `multithreading.py` 模块文档

## 模块概述
`multithreading.py` 模块主要用于实现多线程处理功能，借助 `concurrent.futures` 模块来完成。该模块支持多种任务执行方式，包括阻塞和非阻塞模式，同时提供了任务递归处理的能力。适用于 Python 3.2 及以上版本。

## 函数说明

### `_task_run`
- **功能**：任务执行函数，向线程池提交任务。
- **参数**：
  - `executor`：`concurrent.futures.ThreadPoolExecutor` 类型，线程池对象。
  - `task_list`：列表类型，包含任务函数及参数的列表。
  - `wrapper_list`：列表类型，装饰器列表，默认为 `None`。
  - `wrapper_parameters`：字典类型，装饰器参数字典，默认为 `None`。
  - `parameters`：字典类型，参数字典，默认为 `None`。
- **返回值**：`concurrent.futures.Future` 对象列表，表示提交的任务。

### `task_run`
- **功能**：任务执行函数，会阻塞等待所有任务完成。
- **参数**：与 `_task_run` 相同。
- **返回值**：列表类型，任务执行结果列表。

### `task_recursion`
- **功能**：递归处理任务字典。
- **参数**：
  - `task`：字典类型，任务字典。
  - 其他参数与 `_task_run` 相同。
- **返回值**：字典类型，任务处理结果字典。

### `task_run_clogging`
- **功能**：任务执行函数，不会阻塞等待所有任务完成。
- **参数**：与 `_task_run` 相同。
- **返回值**：`concurrent.futures.Future` 对象列表，表示提交的任务。

### `task_recursion_clogging`
- **功能**：递归处理任务字典，不阻塞。
- **参数**：
  - `task`：字典类型，任务字典。
  - 其他参数与 `_task_run` 相同。
- **返回值**：字典类型，任务处理结果字典。

### `threadPools`
- **功能**：多线程处理函数，创建线程池并递归处理任务字典。
- **参数**：
  - `task`：字典类型，任务字典。
  - `wrapper_list`：列表类型，装饰器列表，默认为 `None`。
  - `wrapper_parameters`：字典类型，装饰器参数字典，默认为 `None`。
  - `max_workers`：整数类型，线程池最大工作线程数，默认为 3。
  - `callback_function`：函数类型，回调函数，默认为 `None`。
  - `errorHandling`：函数类型，错误处理函数，默认为 `None`。
  - `parameters`：字典类型，参数字典，默认为 `None`。
- **返回值**：根据 `callback_function` 或错误处理情况返回相应结果。

## 类说明

### `EnableMultithreading`
- **功能**：封装多线程处理功能。
- **初始化参数**：
  - `max_workers`：整数类型，线程池最大工作线程数，默认为 3。
  - `callback_function`：函数类型，回调函数，默认为 `None`。
  - `errorHandling`：函数类型，错误处理函数，默认为 `None`。
- **方法**：
  - `task_run`：执行任务列表，支持阻塞和非阻塞模式。
    - **参数**：
      - `task_list`：列表类型，任务列表。
      - `clogging`：布尔类型，是否阻塞，默认为 `True`。
      - 其他参数与 `_task_run` 相同。
    - **返回值**：根据 `clogging` 参数返回任务执行结果或 `Future` 对象列表。
  - `task_recursion`：递归处理任务字典，支持阻塞和非阻塞模式。
    - **参数**：
      - `task_dict`：字典类型，任务字典。
      - `clogging`：布尔类型，是否阻塞，默认为 `True`。
      - 其他参数与 `_task_run` 相同。
    - **返回值**：根据 `clogging` 参数返回任务处理结果字典。
  - `close`：关闭线程池。
    - **参数**：无。
    - **返回值**：无。













