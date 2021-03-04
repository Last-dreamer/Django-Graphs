from django.shortcuts import render
import matplotlib.pyplot as plt
import io, csv
import urllib, base64

def home(request):
    plt.subplot(111)
    plt.plot([1,2,5,7], color='r', label='data', linewidth=3)
    plt.legend()
    
    figure = plt.gcf()
    # convert graph into string and then to  64bit image
    buffer = io.BytesIO()
    figure.savefig(buffer, format='png')
    buffer.seek(0)
    string = base64.b64encode(buffer.read())
    uri = urllib.parse.quote(string)
    return  render(request, 'home.html', {'data':uri})
