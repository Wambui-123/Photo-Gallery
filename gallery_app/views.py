from django.shortcuts import render, redirect, reverse

def landing_page(request):
    return render(request, "landing.html")