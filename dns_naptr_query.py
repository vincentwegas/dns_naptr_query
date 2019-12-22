"""
This script returns the all the IPv4 addresses of a SIP Registrar, 
by performing a DNS NAPTR and DNS SRV Query 

"""
import dns.resolver

debug = False

def dnsNaptrQuery(name):
    
    qtype = 'NAPTR'
    
    try:
        answer = dns.resolver.query(name, qtype, raise_on_no_answer=False)

        res = []
        for rdata in answer:
            res.append(rdata.replacement)
                
        print ("[+] NAPTR Response for %s: " % (name) +" "+str(res))
        if res == []: print ("[!] The entered DNS Name contains no NAPTR Record!")
        
        return res

    except:
        raise Exception('[!] The entered DNS Name is empty or not valid!')



def dnsSrvQuery(name):

    qtype = 'SRV'
    
    try: 
        answer = dns.resolver.query(name, qtype, raise_on_no_answer=False)
    
        res = []
        for rdata in answer:
            res.append(rdata.target)

        print ("[+] SRV Response for %s: " %(name) +" " +str(res))
        if res == []: print ("[!] The entered DNS Name contains no SRV Record!")
        return res
    
    except:
        raise Exception("[!] The entered DNS Name is empty or not valid! ")



def dnsArecordQuery(name):
    
    qtype = 'A'
        
    try:
        answer = dns.resolver.query(name, qtype, raise_on_no_answer=False)
        
        res = []
        for rdata in answer:
                res.append(rdata.address)
                print ("[+] A-Record Response for %s: " %(name) +" " +str(res))
                if res == []: print ("[!] The entered DNS Name contains no A Record!")

        return res

    except:
        raise Exception("[!] The entered DNS Name is empty or not valid! ")



def startQuery(name):

    res = dnsNaptrQuery(name)

    for i in res:
        res2 = dnsSrvQuery(i)
        for j in res2:
            dnsArecordQuery(j)

    

if __name__ == '__main__':

    startQuery(input("Type in the Name of your SIP Registrar: "))

