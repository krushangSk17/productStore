from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
from django.utils.dateparse import parse_datetime
from django.contrib.auth.hashers import make_password
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

@api_view(['POST'])
def change_password(request):
    try:
        username = request.data.get('username')
        new_password = request.data.get('newpassword')
        
        if not username or not new_password:
            return Response({"status": "error", "message": "Username and new password are required."}, status=400)
        
        # Find the user
        user = User.objects.filter(username=username).first()
        if not user:
            return Response({"status": "error", "message": "User does not exist."}, status=404)
        
        # Update the password
        user.password = make_password(new_password)
        user.save()
        
        return Response({"status": "success", "message": "Password updated successfully."}, status=200)
    
    except Exception as e:
        return Response({"status": "error", "message": str(e)}, status=500)

@api_view(['POST'])
def register_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "User created successfully"}, status=201)
    else:
        return Response(serializer.errors, status=400)

    
@api_view(['GET'])
@cache_page(60 * 15) 
def get_products(request):
    queryset = Products.objects.all()

    # Date range filtering
    start_date = request.query_params.get('start_date')
    end_date = request.query_params.get('end_date')
    if start_date:
        # Assuming `created_at` is a DateTimeField
        start_date = parse_datetime(start_date)
        if start_date:
            queryset = queryset.filter(created_at__gte=start_date)
    if end_date:
        end_date = parse_datetime(end_date)
        if end_date:
            queryset = queryset.filter(created_at__lte=end_date)

    # Stock status filtering
    stock_status = request.query_params.get('stock_status')
    if stock_status is not None:
        queryset = queryset.filter(stock_status=stock_status)

    # Serialize the filtered queryset
    products_serializer = ProductSerializer(queryset, many=True)

    # No changes here; assuming you want to list all categories regardless of the product filter
    category = Category.objects.all()
    category_serializer = CategorySerializer(category, many=True)

    return Response({
        'status': 200,
        'categories': category_serializer.data,
        'products': products_serializer.data
    })

@api_view(['POST'])
def save_category(request):
    try:
        data = request.data
        category = Category.objects.create(name = data['name'])
        category.save()
        return Response({'status': 'success', 'id': category.id})

    except Exception as e:
        return Response({'status': 'error', 'error': str(e)})

@api_view(['POST'])
def save_product(request):
    try:
        # Assuming you're sending data as JSON
        data = request.data

        # Fetch the Category instance corresponding to the 'category' name provided in the request
        category_name = data.get('category')  # This assumes 'category' is the name of the category
        category = Category.objects.get(name=category_name)  # Get the Category instance

        # Create a product, now correctly setting the category
        product = Products.objects.create(
            sku=data['sku'],
            name=data['name'],
            category=category,  # Correctly assign the Category instance
            stock_status=data['stock_status'],
            available_stock=data['available_stock']
        )

        # Process tags
        tags_list = data.get('tags', [])
        for tag_name in tags_list:
            tag, created = Tag.objects.get_or_create(name=tag_name)
            product.tags.add(tag)

        # Now save the product to commit the ManyToMany changes
        product.save()

        return Response({'status': 'success', 'id': product.id})

    except Exception as e:
        return Response({'status': 'error', 'error': str(e)})


@api_view(['POST'])
def delete_product(request):
    try:
        # Extract the product ID from the request data
        product_id = request.data.get('id')
        
        if not product_id:
            return Response({'status': 'error', 'message': 'Product ID is required.'}, status=400)
        
        # Try to retrieve the product with the given ID
        try:
            product = Products.objects.get(id=product_id)
        except Products.DoesNotExist:
            return Response({'status': 'error', 'message': 'Product not found.'}, status=404)
        
        # Delete the product
        product.delete()
        
        return Response({'status': 'success', 'message': 'Product deleted successfully.'}, status=200)
    
    except Exception as e:
        return Response({'status': 'error', 'message': str(e)}, status=500)

