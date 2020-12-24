from django.shortcuts import render

def root(request):
	return render(request, 'root.html')

def dev(request):
	return render(request, 'dev.html')

def network(request):
	return render(request, 'network.html')

def whoami(request):
	return render(request, 'whoami.html')

def ping_me(request):
	return render(request, 'ping_me.html')