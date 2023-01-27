from django.shortcuts import render
from django.views.decorators.csrf import requires_csrf_token
# Create your views here.
from details.models import IndustryType, Company

def allcompany(request):
    industries = IndustryType.objects.all()
    # companies = Company.objects.all()
    industry = request.GET.get('industry')
    if industry == None:
        allcompany = Company.objects.all()
    else:
        allcompany = Company.objects.filter(industry_name = industry)

    # industry_wise_company = Company.objects.filter(industry = industries)
    # print(companies)
    print(industries)

    context = {'industries': industries, 'allcompany': allcompany}
    return render(request, 'details/main.html', context)


def industry(request):
    if request.method == 'POST':
        name = request.POST['name']
        industry = IndustryType(name=name)
        industry.save()
    return render(request, 'details/industrytype.html')


def company(request):
    industry_list = IndustryType.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        owner_name = request.POST.get('owner_name')
        address = request.POST.get('address')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        industry = request.POST.get('industry')

        industryId = request.POST.get("industry") 
        industry = IndustryType.objects.get(id=industryId)

        print(industry)
        

        company = Company(name=name, owner_name=owner_name, address=address,email=email, contact=contact, industry=industry)
        company.save()

    context = {'industry_list': industry_list}
    return render(request, 'details/company.html', context)