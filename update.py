import codecs
import re

with codecs.open('d:\\niss\\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

data = {
  "Domates Çorbası": "https://cdn.qrall.co/tenancy/tenants/3a185e42-1b07-4008-abec-7b00d2fc9097/Product/3a185e42-2b9f-79c0-de8f-e99d25c6d8f4/3a1b3028-2a23-2e85-7bcf-1829dcfcc240",
  "Mercimek Çorbası": "https://cdn.qrall.co/tenancy/tenants/3a185e42-1b07-4008-abec-7b00d2fc9097/Product/3a185e42-2bd9-158f-693c-ccf1426638df/3a1a4cf8-d91b-3cb4-666d-a0e21e46f9f7",
  "Haşlanmış Kıymalı Mantı": "https://cdn.qrall.co/tenancy/tenants/3a185e42-1b07-4008-abec-7b00d2fc9097/Product/3a185e42-2f2a-61d6-33b1-a778f628a313/3a1a4d02-9cc3-e85f-02b7-d69bfb02579e",
  "Kızarmış Kıymalı Mantı": "https://cdn.adisyo.com/mahrezphotos/449274_20362_20230526113936.jpg",
  "Karışık Kıymalı Mantı": "https://cdn.qrall.co/tenancy/tenants/3a185e42-1b07-4008-abec-7b00d2fc9097/Product/3a185e42-2f9e-5574-cc02-c7c29d024a7a/3a1a4d05-c52e-1767-c460-f0f3133a768a",
  "Kıymalı Hingel": "https://cdn.qrall.co/tenancy/tenants/3a185e42-1b07-4008-abec-7b00d2fc9097/Product/3a185e42-2fdc-b7c3-b91f-b8e5ec6f4310/3a1a4d07-d656-6342-ba72-100f01316723",
  "Kızarmış Kıymalı Hingel": "https://cdn.qrall.co/tenancy/tenants/3a185e42-1b07-4008-abec-7b00d2fc9097/Product/3a185e42-3033-4206-0354-46c85a243a1a/3a1a4d0a-49ed-dc1d-3c18-c4e439b9b7ce",
  "Rus Mantısı": "https://cdn.qrall.co/tenancy/tenants/3a185e42-1b07-4008-abec-7b00d2fc9097/Product/3a18cf77-f7e1-81fd-af95-c1fcbcb1cfef/3a1a4d13-c157-a3d7-6708-7545f5fcae79",
  "Patatesli Mantı": "https://cdn.qrall.co/tenancy/tenants/3a185e42-1b07-4008-abec-7b00d2fc9097/Product/3a185e42-307b-c0b2-57ea-4a92adc499da/3a1a4d0d-d173-1ab5-1e3e-b4a0099b9ab6",
  "Kızarmış Patatesli Mantı": "https://cdn.qrall.co/tenancy/tenants/3a185e42-1b07-4008-abec-7b00d2fc9097/Product/3a185e42-30c8-228d-5623-874ac1a3cb71/3a1a4d0e-68e3-e508-e309-6e42454257de",
  "Yeşil Mercimekli Mantı": "https://cdn.qrall.co/tenancy/tenants/3a185e42-1b07-4008-abec-7b00d2fc9097/Product/3a185e42-3119-a523-ebdf-41c05768a365/3a1a4d15-d1f3-58d3-69a6-5316cf18fcb1",
  "Kızarmış Yeşil Mercimekli Mantı": "https://cdn.qrall.co/tenancy/tenants/3a185e42-1b07-4008-abec-7b00d2fc9097/Product/3a185e42-314e-1cef-0a5a-9b2ee4747ebb/3a1a4d16-dcbe-ce35-4663-42d013cd9ff7",
  "Ispanaklı Mantı": "https://cdn.qrall.co/tenancy/tenants/3a185e42-1b07-4008-abec-7b00d2fc9097/Product/3a185e42-3183-7b40-0647-3ff7d3fc2ea9/3a1a4d19-d4fc-fdd3-6a88-1df8594c928a",
  "Kızarmış Ispanaklı Mantı": "https://cdn.qrall.co/tenancy/tenants/3a185e42-1b07-4008-abec-7b00d2fc9097/Product/3a185e42-31b6-25b4-833d-57e603f81d8a/3a1a4d1a-f5b2-0ac6-e4be-183f2d44be34",
  "Haşlanmış İçli Köfte": "https://cdn.qrall.co/tenancy/tenants/3a185e42-1b07-4008-abec-7b00d2fc9097/Product/3a185e42-31f0-eb37-a49b-9cd050246b15/3a1b3017-9051-0aad-a64a-9e2d11786a6b",
  "Kızarmış İçli Köfte": "https://cdn.qrall.co/tenancy/tenants/3a185e42-1b07-4008-abec-7b00d2fc9097/Product/3a185e42-321e-bfd2-b206-526c1e5663e5/3a1b3025-4b08-ad79-ef0f-c8f0efb0872b",
  "Kabak Mücveri": "https://cdn.qrall.co/tenancy/tenants/3a185e42-1b07-4008-abec-7b00d2fc9097/Product/3a185e42-327d-07a4-2086-9b7bad13e59e/3a1a4d26-e415-d552-040b-679d0aeb12ca",
  "Zeytinyağlı Yaprak Sarma": "https://cdn.qrall.co/tenancy/tenants/3a185e42-1b07-4008-abec-7b00d2fc9097/Product/3a185e42-32ab-af1c-8ff9-1b12307c1313/3a1b3022-13ad-a077-0546-986fb96f5256",
  "Patates Kızartması": "https://cdn.adisyo.com/mahrezphotos/2151726_20362.jpg?202205190542",
  "Ekstra Sos": "https://cdn.adisyo.com/mahrezphotos/2196181_20362_20230526013548.jpg",
  "Ekstra Yoğurt": "https://cdn.adisyo.com/mahrezphotos/2196183_20362_20230526013558.jpg",
  "El Açması Kremalı Fettuccine": "https://cdn.qrall.co/tenancy/tenants/3a185e42-1b07-4008-abec-7b00d2fc9097/Product/3a185e42-4477-22e1-8ef4-881d3e095d04/3a1a4d2a-3a24-8e0e-39ac-e37c85a220dc",
  "El Açması Salçalı Makarna": "https://cdn.qrall.co/tenancy/tenants/3a185e42-1b07-4008-abec-7b00d2fc9097/Product/3a18cf78-28ef-405b-26a2-61e688914eb8/3a1a4d2b-8752-10da-9435-fb25dadaaa14",
  "El Açması Kremalı Mantarlı Fettuccine": "https://cdn.qrall.co/tenancy/tenants/3a185e42-1b07-4008-abec-7b00d2fc9097/Product/3a185e42-44d5-6774-5ec9-17e7e164ef36/3a1a4d2d-9f3d-19aa-6a1c-3431259035d8",
  "El Açması Köri Soslu Fettuccine": "https://cdn.qrall.co/tenancy/tenants/3a185e42-1b07-4008-abec-7b00d2fc9097/Product/3a185e42-455e-a0c0-9690-05e9a3453665/3a1a4d2f-bf00-25ea-7944-229805af1a1b",
  "El Açması Pesto Soslu Fettuccine": "https://cdn.qrall.co/tenancy/tenants/3a185e42-1b07-4008-abec-7b00d2fc9097/Product/3a185e42-45aa-69b7-3528-82564fc5abb7/3a1a4d30-f416-4a17-d37e-45b0fd15be94",
  "El Açması Bolonez Soslu Fettuccine": "https://cdn.qrall.co/tenancy/tenants/3a185e42-1b07-4008-abec-7b00d2fc9097/Product/3a185e42-45d8-75dc-72c9-68d0f17c6f5e/3a1a4d33-3a2b-7a10-826f-fe53630d17e1",
  "El Açması Kremalı Karidesli Fettuccine": "https://cdn.qrall.co/tenancy/tenants/3a185e42-1b07-4008-abec-7b00d2fc9097/Product/3a185e42-460b-e10f-ca3c-58022ac2d8fb/3a1a4d35-08b9-c1ea-f1ce-1284353f224f",
  "El Açması Kremalı Biftekli Fettuccine": "https://cdn.qrall.co/tenancy/tenants/3a185e42-1b07-4008-abec-7b00d2fc9097/Product/3a185e42-463c-2ef8-4644-5544ae617767/3a1a4d37-eb77-9c81-13ef-ec3c9931e57a",
  "El Açması Domates Soslu Köfteli Makarna": "",
  "El Açması 3 Peynirli Makarna": "",
  "Coca Cola": "https://cdn.adisyo.com/mahrezphotos/449269_20362.jpg?202206251205",
  "Coca Cola Zero": "https://cdn.adisyo.com/mahrezphotos/449544_20362.jpg?202206251206",
  "Fanta": "https://cdn.adisyo.com/mahrezphotos/449542_20362.jpg?202206251206",
  "Sprite": "https://cdn.adisyo.com/mahrezphotos/449543_20362.jpg?202206251207",
  "Fusetea Limon": "https://cdn.adisyo.com/mahrezphotos/449545_20362.jpg?202206251208",
  "Fusetea Şeftali": "https://cdn.adisyo.com/mahrezphotos/449546_20362.jpg?202206251208",
  "Fusetea Mango": "",
  "Soda": "https://cdn.adisyo.com/mahrezphotos/449271_20362.jpg?202206251206",
  "Ayran": "https://cdn.adisyo.com/mahrezphotos/469313_20362.jpg?202206251208",
  "Cappy Şeftali": "https://cdn.adisyo.com/mahrezphotos/2256156_20362.jpg?202206251208",
  "Su": "https://cdn.adisyo.com/mahrezphotos/449266_20362.jpg?202206251205",
  "Efes Pilsen 33 cl": "https://cdn.adisyo.com/mahrezphotos/2321878_20362_20240607041838.jpg",
  "Kırmızı Şarap": "",
  "Becks 33 cl": "",
  "Beyaz Şarap": "",
  "Roze Şarap": ""
}

img_map_lower = {k.lower(): v for k, v in data.items() if v}

def replacer(match):
    full_str = match.group(0)
    title = match.group(1)
    t_clean = title.strip().lower()
    
    found_url = None
    for k, v in img_map_lower.items():
        if t_clean == k:
            found_url = v
            break
            
    if found_url:
        img_html = f'''<div class="menu-item-img">
          <img src="{found_url}" alt="{title}" loading="lazy" />
        </div>'''
        
        # we will place the image before the <h3> tag inside the match
        return f'<div class="card-body">\n          {img_html}\n          <h3>{title}</h3>'
    return full_str

pattern = re.compile(r'<div class="card-body">\s*<h3>([^<]+)</h3>', re.IGNORECASE)

new_content = pattern.sub(replacer, content)

with codecs.open('d:\\niss\\index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
    
print("Updated index.html successfully.")
