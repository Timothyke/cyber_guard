from django.shortcuts import render
import nmap
from django.contrib.auth.decorators import login_required

@login_required
def scan_network(request):
    results = {}
    if request.method == "POST":
        ip = request.POST.get('ip')
        nm = nmap.PortScanner()
        nm.scan(ip, '1-1024')  # Scanning ports 1-1024
        # Prepare results by extracting tcp information for each host
        results = {host: nm[host]['tcp'] for host in nm.all_hosts()}
    # Pass results to the template
    return render(request, 'scan_network.html', {'results': results})
