import requests
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'}

page = requests.get('https://www.google.com.br/search?q=dolar&sxsrf=AOaemvK3HDR5HFexMuoKWSFzinP3zvQu9Q%     3A1643074931117&source=hp&ei=c1XvYbL2BO-r5OUPw_224AQ&iflsig=ALs-wAMAAAAAYe9jg-wJrlGtHrEN-ZgyQFIu_2d268Ct&ved=0ahUKEwjy--yM48v1AhXvFbkGHcO-DUwQ4dUDCAc&uact=5&oq=dolar&gs_lcp=Cgdnd3Mtd2l6EAMyEAgAEIAEELEDEIMBEEYQggIyCggAELEDEIMBEEMyBAgAEEMyBAgAEEMyCAgAEIAEELEDMgoILhDHARDRAxBDMgQIABBDMggIABCABBCxAzILCAAQgAQQsQMQgwEyBAgAEEM6BwgjEOoCECc6DQguEMcBENEDEOoCECc6BAgjECc6BggjECcQEzoFCAAQgAQ6DgguEIAEELEDEMcBENEDOg4ILhCABBCxAxDHARCjAjoKCAAQgAQQsQMQClD5B1jhD2CWEWgBcAB4AIABuAGIAacGkgEDMC41mAEAoAEBsAEK&sclient=gws-wiz', headers=headers)
#print(page.content)


soup = BeautifulSoup(page.content, 'html.parser')
print(page.content)
atributos = {'class':'g'}

valor_dolar = soup.find_all('span',class_='DFlfde SwHCTb')[0]
print(valor_dolar)
print(valor_dolar.text)
print(valor_dolar['data-value'])