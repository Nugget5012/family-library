from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Manual
from django.conf import settings
from django.core.files.storage import FileSystemStorage

# Create your views here.
def index(request):
    num_products = Product.objects.all().count()
    num_manuals = Manual.objects.all().count()

    context ={
        'num_products': num_products,
        'num_manuals':num_manuals,
    }
    return render(request,'index.html', context=context)
   

def products(request):
    products = Product.objects.all()
    num_products = products.count()
    context ={
        'products': products,
        'products_count':num_products
        
    }
    return render(request,'products.html',context=context)

def detail(request,id):
    print(id)
    prod_id=int(id)
    manuals=Manual.objects.filter(product_id=prod_id)
    manual_files=[]
    for manual in manuals:# Only intrested in title and URL
        manual_vm={}
        manual_vm["title"]=manual.manual_title
        manual_vm["description"]=manual.manual_description
        if manual.manual_url==None or manual.manual_url =='':
            manual_vm["file_url"]= manual.manual_file.url
            
        else:
            manual_vm["file_url"]=manual.manual_url
        manual_files.append(manual_vm)
        
    context ={
        'myproduct': Product.objects.get(product_id=prod_id),
        'manuals':manual_files
    }
    return render(request,'detail.html',context=context)

def search(request):
    if request.method =='POST':
        data = request.POST["q"]
        print(data)
        products=Product.objects.filter(product_name__icontains=data)
        context ={
        'products': products,
        'products_count':products.count()
        }   
        return render(request,'products.html', context=context)
    else:
        return null

def pdf_view(request): 
    file_name=request.GET.get("file")
    file_path=settings.PDF_FOLDER +file_name+'.pdf'
    with open(file_path,'rb') as pdf:
        response = HttpResponse(pdf.read(),content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename='+file_name+'.pdf'
        return response

#def manual_upload(request):
 #   if request.method == 'POST' and request.FILES['myfile']:
  #      myfile = request.FILES['myfile']
   #     file_store = FileSystemStorage()
    #    filename= file_store.save(myfile.name,myfile)
     #   uploaded_file_url = file_store(filename)
      #  return render(request, 'core/simple_upload.html', {
       #     'uploaded_file_url': uploaded_file_url
        #})
    #return render(request, 'core/simple_upload.html')