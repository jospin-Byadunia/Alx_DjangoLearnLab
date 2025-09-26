# Operations in `views.py`

Below is a typical breakdown of operations you might find in a Django `views.py` file for an advanced API project:

## 1. List Operation
- **Purpose:** Retrieve and display a list of objects.
- **Example:**  
    ```python
    class ItemListView(APIView):
            def get(self, request):
                    items = Item.objects.all()
                    serializer = ItemSerializer(items, many=True)
                    return Response(serializer.data)
    ```

## 2. Retrieve Operation
- **Purpose:** Retrieve a single object by its ID.
- **Example:**  
    ```python
    class ItemDetailView(APIView):
            def get(self, request, pk):
                    item = get_object_or_404(Item, pk=pk)
                    serializer = ItemSerializer(item)
                    return Response(serializer.data)
    ```

## 3. Create Operation
- **Purpose:** Add a new object to the database.
- **Example:**  
    ```python
    class ItemCreateView(APIView):
            def post(self, request):
                    serializer = ItemSerializer(data=request.data)
                    if serializer.is_valid():
                            serializer.save()
                            return Response(serializer.data, status=status.HTTP_201_CREATED)
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    ```

## 4. Update Operation
- **Purpose:** Modify an existing object.

    ```python
    class ItemUpdateView(APIView):
            def put(self, request, pk):
                    item = get_object_or_404(Item, pk=pk)
                    serializer = ItemSerializer(item, data=request.data)
                    if serializer.is_valid():
                            serializer.save()
                            return Response(serializer.data)
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    ```

## 5. Delete Operation
- **Purpose:** Remove an object from the database.
- **Example:**  
    ```python
    class ItemDeleteView(APIView):
            def delete(self, request, pk):
                    item = get_object_or_404(Item, pk=pk)
                    item.delete()
                    return Response(status=status.HTTP_204_NO_CONTENT)
    ```

## 6. Custom Actions
- **Purpose:** Any additional logic, such as filtering, searching, or custom endpoints.
- **Example:**  
    ```python
    class ItemSearchView(APIView):
            def get(self, request):
                    query = request.query_params.get('q')
                    items = Item.objects.filter(name__icontains=query)
                    serializer = ItemSerializer(items, many=True)
                    return Response(serializer.data)
    ```

---

> **Note:**  
> The actual operations and class names may vary depending on your project structure and requirements.  
> For DRF (Django Rest Framework), you might also use `ViewSet` or `GenericAPIView` for more concise code.


## Testing Strategy and Test Cases (`test_views.py`)

### Testing Strategy
- **Unit Tests:** Each view operation is tested in isolation to ensure correct behavior.
- **Integration Tests:** Endpoints are tested using Django's test client to simulate real API requests.
- **Edge Cases:** Tests cover invalid input, missing data, and permission checks.

### Example Test Cases
- **List Operation:** Verify that a GET request returns all items.
- **Retrieve Operation:** Check that retrieving an existing item by ID returns correct data; test 404 for non-existent IDs.
- **Create Operation:** Ensure valid data creates an item; invalid data returns errors.
- **Update Operation:** Confirm that updating an item with valid data changes the object; invalid data returns errors.
- **Delete Operation:** Test that deleting an item removes it; deleting a non-existent item returns 404.
- **Custom Actions:** Validate filtering/search endpoints return expected results.

### Running the Tests
1. Ensure your virtual environment is active and dependencies are installed.
2. Run the tests using:
    ```bash
    python manage.py test api.tests.test_views
    ```

### Interpreting Test Results
- **OK:** All tests passed.
- **FAIL/ERROR:** Details will be shown in the output. Review the traceback to identify and fix issues.

---