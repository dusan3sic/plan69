# [Plan 9](https://9p.io/plan9/)


## 1 - [Manifest](https://9p.io/sys/doc/9.pdf)

#### <font color="#325aa8"> 1.1 - Motivacija

>*"The early catch phrase was to build a UNIX out of a lot of little systems, not a
system out of a lot of little UNIXes"*

#### <font color="#325aa8"> 1.2 - Design

1. resursi se tretiraju kao file systemi
2. 9p protokol za pristupanje resursima
3. privatni namespace koji poseduje sve potrebne resurse

#### <font color="#325aa8"> ~1.3 File Server~

#### <font color="#325aa8"> 1.4 Unusual file servers
- 8 1/2
- ftpfs - prebacuje sve u 9p

#### <font color="#325aa8"> 1.5 Configurability and administration
Sistem je isti odakle oces

#### <font color="#325aa8"> 1.6 C Programming
- nema #if direktivu
- izbegavati #ifdef
- cudne stvari moram priznati
- UTF-8 ASCII
- tex

#### <font color="#325aa8"> 1.7 Portability and Compilation
##### make
* `mk`
* $cputype i $objtype
* `objtype=sparc mk` makuje za sparc arhitekturu

#### <font color="#325aa8"> 1.8 Parallel programming
* `rfork` - pravi nove procese
* 'segattach` - davanje segmenta memorije (parent -> child) sistemski poziv
* 'rendezvous' - sinkovanje procesa


#### <font color="#325aa8"> 1.9 Implementation of Name Spaces
**Tri sistemska poziva**
1. `mount` - dodaje stablo od file servera
2. `bind` - duplira delove postojeceg namespace-a u neki drugi namespace
3. `unmount` - brise namespace

* Pre mounta mora da se uspostavi neki pipe/konekcija
* Unija fajlova - primer:
>/bin je unija /$cputype/bin(bin fajlovi) i /rc/bin(shell skripte)

* $PATH je neophodan zbog unija
* <font color=red>pravljenje novog fajla<font>

#### <font color="#325aa8"> 1.10 9P Protocol

* 9P protokol je protokol za sve servise a ne specifican za samo jedan servis(rlogin, FTP, TFTP, X  windows)
* 9P tretira fajlove kao bytove a ne kao blokove
* fid - file id pointer

* **Poruke**:
1. *session* - obostrana autentikacija
2. *attach* - povezuje fid sa server file stablom
3. *walk* - pomera fid za jedan nibo
4. *clone* - klonira trenutni fid
5. *open* - lockuje fid, provera permisiju i sprema fid za i/o
6. *read*
7. *write*
8. *clunk* - odbacuje fid
9. *remove* - kao klank samo sto brise fajl

* 9P ima dve forme - rpc/kernel procedure

* <font color=red> ne kontam ovo mozak mi ne radi<font>

#### <font color="#325aa8"> 1.11 File Caching
Zajednicki cache?, moguce istraziti nesto
>A similar method can be applied to build a general client cache in unused local memory, but this has not been done in Plan 9.

#### <font color="#325aa8"> 1.12 Networks and Communication Devices
* **Povezivanje na adresu:** `connect [ip adresa]![port]`
* Connection server - *cs* = file koji sluzi za povezivanje aplikacije sa hostom (uz pomoc funkcije `dial` )

#### <font color="#325aa8"> 1.13 Kernel structures for networks
* *stream* - bidirekcioni kanal izmedju uredjaja i procesa
* Upstream i downstream put rutina (stavlja podatke u nekom smeru)

#### <font color="#325aa8"> 1.14 The IL Protocol
* IL - Internet Link
* sluzi za slanje pouzdanih 9P poruka preko interneta

#### <font color="#325aa8"> 1.15 Overview of authentication
* 9p *attach*
* DES auth key, challenges
* neki user moze biti autoritet nekom drugom (recimo user - CPU server)
* <font color="yellow">citati razmenu kljuceva?<font>

#### <font color="#325aa8"> 1.16 Authenticating external connections
* *authenticators*

#### <font color="#325aa8"> 1.17 Special users
* *adm* - admin, dodavanje usera i konfiguracija diskova i mreze
* *none* - nema sifru i svima je pristupan

#### <font color="#325aa8"> 1.18 The cpu command and proxied authentication
* cpu se prvo spusta na user none
* cpu se predstavlja kao user
* speaks for relacija - tabela

#### <font color="#325aa8"> 1.19 File Permissions
* grupe usera su zapravo useri koji imaju vise usera


#### <font color="#325aa8"> ~1.20 Performance~
#### <font color="#325aa8"> 1.21 Discussion

>*"It is fair to say that the Plan 9 kernel is primarily a 9P multiplexer"*
#### <font color="#325aa8"> 