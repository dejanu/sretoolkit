
import smtplib

originator_email = 'mr_vending@vending.ro'
destinatari = ['Gabriel.@yahoo.com']
username = 'autoreplynospam'
parola = 'sss@'

mesaj = """From:  Maria Contea <MContea@vending.ro>
To: Alexandru Lupu <ALupu@vending.com>
Subject:  Tonomat Cafea Orange
Content-type: text/html
<html>

<body>


<p>Buna ziua ,</p>

<br>
<p> &nbsp; Stimate domnule Rondelli, va contactam din partea firmei car realizeaza mentenata tonomatului de cafea din cladirea Orange Skanska .</p>

<p>&nbsp; Din pacate tonomatul de cafea de la etajul 5 a suferit o problema de configurare, in urma careia putea sa ofere produse fara a incasa bani. Din acest motiv cu aprobarea firmei, s-au verificat camerele si dvs. apareti pe cele mai multe filmari, manipuland aparatul intr-un mod malitios, mai mult oferind colegilor cafea.<p>
<p>&nbsp; Paguba facuta este in valoarea de <b>452 de RON</b>, ca urmarea acesta suma o sa fie retrasa din salariu dvs. , de asemenea o sa suportati inlocuirea unui servo-motor din interior, va lasam libertatea de a alege dvs. un motor de aici: <a href="https://www.vendingworld.com/smallparts/vending-machine-motors">link</a> </p>.

<p><i>Numai bine,
</p><p>Maria Contea

Vending Professional Romania

Tel: +4 021 203 64345
Fax:+4 021 203 664323
</i></p>

</body>
</html> 
"""



# Gmail Login


try:
   smtpObj = smtplib.SMTP('smtp.gmail.com:587')
   smtpObj.starttls()
   smtpObj.login(username,parola)
   smtpObj.sendmail(originator_email, destinatari, mesaj)         
   print "Mesajul electronic a fost trimis cu succes"
except(),e:
   print "Mesajul electronic nu a fost trimis cu succes"
   print e
else:
    smtpObj.quit()



