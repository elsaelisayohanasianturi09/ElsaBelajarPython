import requests

kode_kelas = "26224"
ci_session = "944a642327508fb8d9c020ada4070e1006363a8c"

url = "http://siakad.itera.ac.id/mahasiswa/krsbaru/simpanKRS"
headers = {
    "Cookie": f"ci_session={ci_session}"
}

data = {
    'idkelas': kode_kelas
}

response = requests.post(url, headers=headers, data=data)