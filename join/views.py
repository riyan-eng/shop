from django.shortcuts import render
from shop.settings import cursor


# Create your views here.
def index(req):
    # query tampilkan kelamin
    query = "SELECT * FROM public.join_kelamin"
    cursor.execute(query)
    data_kelamin = cursor.fetchall()
    print(data_kelamin)

    # query tampilkan ortu
    query = "SELECT * FROM public.join_ortu"
    cursor.execute(query)
    data_ortu = cursor.fetchall()

    # query join 
    query = "SELECT a.nama, b.name, c.name FROM public.join_anak a JOIN public.join_kelamin b ON a.jenis_kelamin_id=b.id JOIN public.join_ortu c ON a.nama_orang_tua_id=c.id"
    cursor.execute(query)
    data_anak = cursor.fetchall()


    data={
        'kelamin': data_kelamin,
        'ortu': data_ortu,
        'anak': data_anak,
    }
    return render(req, 'index_join.html',{'data': data})