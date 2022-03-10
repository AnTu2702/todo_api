# swagger_client.ToDoHandlerApi

All URIs are relative to *&lt;AWS_API_URL&gt;*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_todo_get**](ToDoHandlerApi.md#v1_todo_get) | **GET** /v1/todo | Get all ToDo objects
[**v1_todo_put**](ToDoHandlerApi.md#v1_todo_put) | **PUT** /v1/todo | Creat a new ToDo object
[**v1_todo_todo_id_delete**](ToDoHandlerApi.md#v1_todo_todo_id_delete) | **DELETE** /v1/todo/{todo_id} | Delete an existing ToDo object
[**v1_todo_todo_id_get**](ToDoHandlerApi.md#v1_todo_todo_id_get) | **GET** /v1/todo/{todo_id} | Get a single ToDo object
[**v1_todo_todo_id_put**](ToDoHandlerApi.md#v1_todo_todo_id_put) | **PUT** /v1/todo/{todo_id} | Update an existing ToDo object

# **v1_todo_get**
> list[ToDo] v1_todo_get()

Get all ToDo objects

ToDo-API-Handler (Get all ToDo objects)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ToDoHandlerApi()

try:
    # Get all ToDo objects
    api_response = api_instance.v1_todo_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ToDoHandlerApi->v1_todo_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ToDo]**](ToDo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_todo_put**
> v1_todo_put(body=body)

Creat a new ToDo object

ToDo-API-Handler (Update an existing ToDo object)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ToDoHandlerApi()
body = swagger_client.ToDo() # ToDo |  (optional)

try:
    # Creat a new ToDo object
    api_instance.v1_todo_put(body=body)
except ApiException as e:
    print("Exception when calling ToDoHandlerApi->v1_todo_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ToDo**](ToDo.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_todo_todo_id_delete**
> v1_todo_todo_id_delete(todo_id)

Delete an existing ToDo object

ToDo-API-Handler (Delete an existing ToDo object)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ToDoHandlerApi()
todo_id = 'todo_id_example' # str | 

try:
    # Delete an existing ToDo object
    api_instance.v1_todo_todo_id_delete(todo_id)
except ApiException as e:
    print("Exception when calling ToDoHandlerApi->v1_todo_todo_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **todo_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_todo_todo_id_get**
> list[ToDo] v1_todo_todo_id_get(todo_id)

Get a single ToDo object

ToDo-API-Handler (Get a single ToDo object)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ToDoHandlerApi()
todo_id = 'todo_id_example' # str | 

try:
    # Get a single ToDo object
    api_response = api_instance.v1_todo_todo_id_get(todo_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ToDoHandlerApi->v1_todo_todo_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **todo_id** | **str**|  | 

### Return type

[**list[ToDo]**](ToDo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_todo_todo_id_put**
> v1_todo_todo_id_put(todo_id, body=body)

Update an existing ToDo object

ToDo-API-Handler (Update an existing ToDo object)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ToDoHandlerApi()
todo_id = 'todo_id_example' # str | 
body = swagger_client.ToDo() # ToDo |  (optional)

try:
    # Update an existing ToDo object
    api_instance.v1_todo_todo_id_put(todo_id, body=body)
except ApiException as e:
    print("Exception when calling ToDoHandlerApi->v1_todo_todo_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **todo_id** | **str**|  | 
 **body** | [**ToDo**](ToDo.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

