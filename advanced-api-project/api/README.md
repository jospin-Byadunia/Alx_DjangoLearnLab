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
- **Example:**  
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
