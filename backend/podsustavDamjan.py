from github import Github
from github import Auth
import re

class Kalkulator:
    def __init__(self):
        self.statistike = []

    def dodaj_statistiku(self, statistika):
        self.statistike.append(statistika)

    def ukloni_statistiku(self, statistika):
        self.statistike.remove(statistika)

    def racunaj_statistike(self, repozitorij):
        
        rezultati = []
        for statistika in self.statistike:
            rezultati.append(statistika.izracunaj(repozitorij))
        return rezultati
    
    
    

class KalkulatorPredaje(Kalkulator):

    def dodaj_statistiku(self, statistika):
        if isinstance(statistika, StatistikaPredaje):
            super().dodaj_statistiku(statistika)
        else:
            raise TypeError
        
    def  racunaj_statistike(self, repozitorij):
        with open("rezultati.txt", "a", encoding="utf-8") as datoteka:
            datoteka.write("#" * 30 + "\n")
            datoteka.write("**PREDAJE**\n")
            datoteka.write("#" * 30 + "\n\n")
        return super().racunaj_statistike(repozitorij)
    

class KalkulatorZahtjevi(Kalkulator):

    

    def dodaj_statistiku(self, statistika):
        if isinstance(statistika, StatistikaZahtjevi):
            super().dodaj_statistiku(statistika)
        else:
            raise TypeError
        
    def  racunaj_statistike(self, repozitorij):
        with open("rezultati.txt", "a", encoding="utf-8") as datoteka:
            datoteka.write("#" * 30 + "\n")
            datoteka.write("**ZAHTJEVI**\n")
            datoteka.write("#" * 30 + "\n\n")
        return super().racunaj_statistike(repozitorij)
        

class KalkulatorProblemi(Kalkulator):

    

    def dodaj_statistiku(self, statistika):
        if isinstance(statistika, StatistikaProblemi):
            super().dodaj_statistiku(statistika)
        else:
            raise TypeError
        
    def  racunaj_statistike(self, repozitorij):
        with open("rezultati.txt", "a", encoding="utf-8") as datoteka:
            datoteka.write("#" * 30 + "\n")
            datoteka.write("**PROBLEMI**\n")
            datoteka.write("#" * 30 + "\n\n")
        return super().racunaj_statistike(repozitorij)

class KalkulatorRasprave(Kalkulator):

    

    def dodaj_statistiku(self, statistika):
        if isinstance(statistika, StatistikaRasprave):
            super().dodaj_statistiku(statistika)
        else:
            raise TypeError


class Statistika:
    def __init__(self):
        pass

    def izracunaj(self, repozitorij):
        pass

class StatistikaPredaje(Statistika):
    pass
        

class StatistikaPredajePredaje(StatistikaPredaje):
    
    def izracunaj(self, repozitorij):
        with open("rezultati.txt", "a", encoding = "utf-8") as datoteka:
            datoteka.write("PREDAJE::PREDAJE\n\n")
        listaPredaja = repozitorij.get_commits()
        rjecnikClanoviPredaje = {}
        for predaja in listaPredaja:
            # print("Napredak...")
            if predaja.commit.author.name not in rjecnikClanoviPredaje.keys():
                rjecnikClanoviPredaje[predaja.commit.author.name] = 1
            else:
                rjecnikClanoviPredaje[predaja.commit.author.name] += 1
        
        ukupnoPredaja = 0
        for kljuc in rjecnikClanoviPredaje.keys():
            ukupnoPredaja += rjecnikClanoviPredaje[kljuc]
        
        povratnaLista = []
        for kljuc in rjecnikClanoviPredaje.keys():
            rjecnik = {}
            rjecnik["ime"] = kljuc
            rjecnik["broj predaja"] = rjecnikClanoviPredaje[kljuc]
            if ukupnoPredaja != 0:
                rjecnik["postotak predaja"] = rjecnikClanoviPredaje[kljuc] / ukupnoPredaja
            else:
                rjecnik["postotak predaja"] = 0
            povratnaLista.append(rjecnik)
            with open("rezultati.txt", "a", encoding = "utf-8") as datoteka:
                datoteka.write(f"ime: {kljuc}, broj: {rjecnikClanoviPredaje[kljuc]}, postotak: {rjecnik['postotak predaja'] * 100}\n")
        with open("rezultati.txt", "a", encoding = "utf-8") as datoteka:
            datoteka.write("\n" + "-" * 80 + "\n\n")
        return povratnaLista

class StatistikaPredajeDodavanja(StatistikaPredaje):
    def izracunaj(self, repozitorij):
        with open("rezultati.txt", "a", encoding = "utf-8") as datoteka:
            datoteka.write("PREDAJE::DODAVANJA\n\n")
        listaPredaja = repozitorij.get_commits()
        
        rjecnikClanoviPredaje = {}
        for predaja in listaPredaja:
            # print("Napredak...")
            if predaja.commit.author.name not in rjecnikClanoviPredaje.keys():
                rjecnikClanoviPredaje[predaja.commit.author.name] = predaja.stats.additions
            else:
                rjecnikClanoviPredaje[predaja.commit.author.name] += predaja.stats.additions
        ukupnoDodavanja = 0
        for kljuc in rjecnikClanoviPredaje.keys():
            ukupnoDodavanja += rjecnikClanoviPredaje[kljuc]
        povratnaLista = []
        for kljuc in rjecnikClanoviPredaje.keys():
            rjecnik = {}
            rjecnik["ime"] = kljuc
            rjecnik["broj dodavanja"] = rjecnikClanoviPredaje[kljuc]
            if ukupnoDodavanja != 0:
                rjecnik["postotak dodavanja"] = rjecnikClanoviPredaje[kljuc] / ukupnoDodavanja
            else:
                rjecnik["postotak dodavanja"] = 0
            povratnaLista.append(rjecnik)
            with open("rezultati.txt", "a", encoding = "utf-8") as datoteka:
                datoteka.write(f"ime: {kljuc}, broj: {rjecnikClanoviPredaje[kljuc]}, postotak: {rjecnik['postotak dodavanja'] * 100}\n")
        with open("rezultati.txt", "a", encoding = "utf-8") as datoteka:
            datoteka.write("\n" + "-" * 80 + "\n\n")
        return povratnaLista
    
class StatistikaPredajeUklanjanja(StatistikaPredaje):
    def izracunaj(self, repozitorij):
        with open("rezultati.txt", "a", encoding = "utf-8") as datoteka:
            datoteka.write("PREDAJE::UKLANJANJA\n\n")
        listaPredaja = repozitorij.get_commits()
        rjecnikClanoviPredaje = {}
        for predaja in listaPredaja:
            # print("Napredak...")
            if predaja.commit.author.name not in rjecnikClanoviPredaje.keys():
                rjecnikClanoviPredaje[predaja.commit.author.name] = predaja.stats.deletions
            else:
                rjecnikClanoviPredaje[predaja.commit.author.name] += predaja.stats.deletions
        
        ukupnoUklanjanja = 0
        for kljuc in rjecnikClanoviPredaje.keys():
            ukupnoUklanjanja += rjecnikClanoviPredaje[kljuc]
        povratnaLista = []
        for kljuc in rjecnikClanoviPredaje.keys():
            rjecnik = {}
            rjecnik["ime"] = kljuc
            rjecnik["broj uklanjanja"] = rjecnikClanoviPredaje[kljuc]
            if (ukupnoUklanjanja != 0):
                rjecnik["postotak uklanjanja"] = rjecnikClanoviPredaje[kljuc] / ukupnoUklanjanja
            else:
                rjecnik["postotak uklanjanja"] = 0
            povratnaLista.append(rjecnik)
            with open("rezultati.txt", "a", encoding = "utf-8") as datoteka:
                datoteka.write(f"ime: {kljuc}, broj: {rjecnik['broj uklanjanja']}, postotak: {rjecnik['postotak uklanjanja'] * 100}\n")
        with open("rezultati.txt", "a", encoding = "utf-8") as datoteka:
            datoteka.write("\n" + "-" * 80 + "\n\n")

        return povratnaLista
    
class StatistikaPredajeUkupno(StatistikaPredaje):
    def izracunaj(self, repozitorij):
        with open("rezultati.txt", "a", encoding = "utf-8") as datoteka:
            datoteka.write("PREDAJE::UKUPNO\n\n")
        listaPredaja = repozitorij.get_commits()
        
        rjecnikClanoviPredaje = {}
        for predaja in listaPredaja:
            # print("Napredak...")
            if predaja.commit.author.name not in rjecnikClanoviPredaje.keys():
                rjecnikClanoviPredaje[predaja.commit.author.name] = predaja.stats.total
            else:
                rjecnikClanoviPredaje[predaja.commit.author.name] += predaja.stats.total
        
        ukupnoUkupno = 0
        for kljuc in rjecnikClanoviPredaje.keys():
            ukupnoUkupno += rjecnikClanoviPredaje[kljuc]
        povratnaLista = []
        for kljuc in rjecnikClanoviPredaje.keys():
            rjecnik = {}
            rjecnik["ime"] = kljuc
            rjecnik["broj ukupno"] = rjecnikClanoviPredaje[kljuc]
            if ukupnoUkupno != 0:
                rjecnik["postotak ukupno"] = rjecnikClanoviPredaje[kljuc] / ukupnoUkupno
            else:
                rjecnik["postotak ukupno"] = 0
            povratnaLista.append(rjecnik)
            with open("rezultati.txt", "a", encoding = "utf-8") as datoteka:
                datoteka.write(f"ime: {kljuc}, broj: {rjecnikClanoviPredaje[kljuc]}, postotak: {rjecnik['postotak ukupno'] * 100}\n")
        with open("rezultati.txt", "a", encoding = "utf-8") as datoteka:
            datoteka.write("\n" + "-" * 80 + "\n\n")
        return povratnaLista
    
class StatistikaPredajeBroj(StatistikaPredaje):
    def izracunaj(self, repozitorij):
        listaPredaja = repozitorij.get_commits()
        with open("rezultati.txt", "a", encoding = "utf-8") as datoteka:
            datoteka.write("PREDAJE::BROJ\n\n")
            datoteka.write(f"Broj predaja: {listaPredaja.totalCount}\n")
            datoteka.write("\n" + "-" * 80 + "\n\n")
        return listaPredaja.totalCount
        
    
class StatistikaPredajePopis(StatistikaPredaje):
    def izracunaj(self, repozitorij):
       
        with open("rezultati.txt", "a", encoding = "utf-8") as datoteka:
            datoteka.write("PREDAJE::POPIS\n\n")
        listaPredaja = repozitorij.get_commits()
        povratnaLista = []
        for predaja in listaPredaja:
            # print("Napredak...")
            rjecnik = {}
            rjecnik["sazetak"] = predaja.sha
            rjecnik["autor"] = predaja.commit.author.name
            rjecnik["poruka"] = predaja.commit.message
            rjecnik["datum"] = predaja.commit.author.date.strftime("%d.%m.%Y.")
            rjecnik["dodavanja"] = predaja.stats.additions
            rjecnik["uklanjanja"] = predaja.stats.deletions
            rjecnik["ukupno"] = predaja.stats.total
            povratnaLista.append(rjecnik)
            with open("rezultati.txt", "a", encoding = "utf-8") as datoteka:
                datoteka.write(f"sazetak: {rjecnik['sazetak']}, autor: {rjecnik['autor']}, poruka: {rjecnik['poruka']}, datum: {rjecnik['datum']}, dodavanja: {rjecnik['dodavanja']}, uklanjanja: {rjecnik['uklanjanja']}, ukupno: {rjecnik['ukupno']}\n")
        with open("rezultati.txt", "a", encoding = "utf-8") as datoteka:
            datoteka.write("\n" + "-" * 80 + "\n\n")
        return povratnaLista
        
    
class StatistikaZahtjevi(Statistika):
    pass

class StatistikaZahtjeviPopis(StatistikaZahtjevi):
    def izracunaj(self, repozitorij):
       
        with open("rezultati.txt", "a", encoding = "utf-8") as datoteka:
            datoteka.write("ZAHTJEVI::POPIS\n\n")
        listaZahtjeva = repozitorij.get_pulls(state = "all")
        povratnaLista = []
        for zahtjev in listaZahtjeva:
            # print("Napredak...")
            rjecnik = {}
            rjecnik["id"] = zahtjev.id
            rjecnik["broj"] = zahtjev.number
            rjecnik["autor"] = zahtjev.user.login
            rjecnik["status"] = zahtjev.state
            rjecnik["datum kreiranja"] = zahtjev.created_at
            rjecnik["datum zatvaranja"] = zahtjev.closed_at
            rjecnik["datum spajanja"] = zahtjev.merged_at
            rjecnik["tijelo zahtjeva"] = zahtjev.body
            povratnaLista.append(rjecnik)
            with open("rezultati.txt", "a", encoding = "utf-8") as datoteka:
                datoteka.write(f"id: {rjecnik['id']}, broj: {rjecnik['broj']}, autor: {rjecnik['autor']}, status: {rjecnik['status']}, datum kreiranja: {rjecnik['datum kreiranja']}, datum zatvaranja: {rjecnik['datum zatvaranja']}, datum spajanja: {rjecnik['datum spajanja']}, tijelo zahtjeva: {rjecnik['tijelo zahtjeva']}\n")
        with open("rezultati.txt", "a", encoding = "utf-8") as datoteka:
            datoteka.write("\n" + "-" * 80 + "\n\n")
        return povratnaLista
    
class StatistikaZahtjeviBroj(StatistikaZahtjevi):
    def izracunaj(self, repozitorij):
        
        with open("rezultati.txt", "a", encoding = "utf-8") as datoteka:
            datoteka.write("ZAHTJEVI::BROJ\n\n")
        listaZahtjeva = repozitorij.get_pulls(state = "all")
        rjecnikClanoviOtvoreno = {}
        rjecnikClanoviZatvoreno = {}

        for zahtjev in listaZahtjeva:
            # print("Napredak...")
            if zahtjev.state == "open":
                if zahtjev.user.login not in rjecnikClanoviOtvoreno:
                    rjecnikClanoviOtvoreno[zahtjev.user.login] = 1
                else:
                    rjecnikClanoviOtvoreno[zahtjev.user.login] += 1
            else:
                if zahtjev.user.login not in rjecnikClanoviZatvoreno:
                    rjecnikClanoviZatvoreno[zahtjev.user.login] = 1
                else:
                    rjecnikClanoviZatvoreno[zahtjev.user.login] += 1
        
        povratnaLista = []
        for kljuc in rjecnikClanoviOtvoreno.keys():
            rjecnik = {}
            rjecnik["ime"] = kljuc
            rjecnik["broj otvorenih zahtjeva"] = rjecnikClanoviOtvoreno[kljuc]
            if kljuc in rjecnikClanoviZatvoreno.keys():
                rjecnik["broj zatvorenih zahtjeva"] = rjecnikClanoviZatvoreno[kljuc]
            else:
                rjecnik["broj zatvorenih zahtjeva"] = 0
            povratnaLista.append(rjecnik)
            with open("rezultati.txt", "a", encoding = "utf-8") as datoteka:
                datoteka.write(f"ime: {kljuc}, broj otvorenih: {rjecnik['broj otvorenih zahtjeva']}, broj zatvorenih: {rjecnik['broj zatvorenih zahtjeva']}\n")
        
        
        for kljuc in rjecnikClanoviZatvoreno.keys():
            
            if kljuc not in rjecnikClanoviOtvoreno.keys():
                rjecnik = {}
                rjecnik["ime"] = kljuc
                rjecnik["broj otvorenih zahtjeva"] = 0
                rjecnik["broj zatvorenih zahtjeva"] = rjecnikClanoviZatvoreno[kljuc]
                povratnaLista.append(rjecnik)
                with open("rezultati.txt", "a", encoding = "utf-8") as datoteka:
                    datoteka.write(f"ime: {kljuc}, broj otvorenih: {rjecnik['broj otvorenih zahtjeva']}, broj zatvorenih: {rjecnik['broj zatvorenih zahtjeva']}\n")
        with open("rezultati.txt", "a", encoding = "utf-8") as datoteka:
            datoteka.write("\n" + "-" * 80 + "\n\n")
        return povratnaLista
    
class StatistikaZahtjeviVrijeme(StatistikaZahtjevi):
    def izracunaj(self, repozitorij):
        
        with open("rezultati.txt", "a", encoding = "utf-8") as datoteka:
            datoteka.write("ZAHTJEVI::VRIJEME\n\n")
        listaZatvorenihZahtjeva = repozitorij.get_pulls(state = "closed")
        brojac = 0
        for p in listaZatvorenihZahtjeva:
            
            brojac += 1
        ukupno_sati = 0
        for zahtjev in listaZatvorenihZahtjeva:
            # print("Napredak...")
            otvoreno = zahtjev.created_at
            zatvoreno = zahtjev.closed_at
            vrijeme_sati = (zatvoreno - otvoreno).total_seconds() / 3600
            ukupno_sati += vrijeme_sati
        if brojac != 0:
            prosjecno_sati = ukupno_sati / brojac
        else:
            prosjecno_sati = "NEMA"
        with open("rezultati.txt", "a", encoding = "utf-8") as datoteka:
            datoteka.write(f"prosjecno sati: {prosjecno_sati}\n")
            datoteka.write("\n" + "-" * 80 + "\n\n")
        return prosjecno_sati
    
class StatistikaZahtjeviKomentari(StatistikaZahtjevi):
    
    def izracunaj(self, repozitorij):
        
        with open("rezultati.txt", "a", encoding = "utf-8") as datoteka:
            datoteka.write("ZAHTJEVI::KOMENTARI\n\n")
        listaZahtjeva = repozitorij.get_pulls(state = "all")
        brojac = 0
        for p in listaZahtjeva:
            brojac += 1
        ukupno_komentara = 0
        for zahtjev in listaZahtjeva:
            # print("Napredak...")
            komentari = zahtjev.get_review_comments()
            broj_komentara = komentari.totalCount
            ukupno_komentara += broj_komentara
        if (brojac != 0):
            prosjecno_komentara = ukupno_komentara / brojac
        else:
            prosjecno_komentara = "NEMA"
        with open("rezultati.txt", "a", encoding = "utf-8") as datoteka:
            datoteka.write(f"prosjecno komentara: {prosjecno_komentara}\n")
            datoteka.write("\n" + "-" * 80 + "\n\n")
        return prosjecno_komentara

class StatistikaProblemi(Statistika):
    pass

class StatistikaProblemiPopis(StatistikaProblemi):
    def izracunaj(self, repozitorij):
        
        with open("rezultati.txt", "a", encoding = "utf-8") as datoteka:
            datoteka.write("PROBLEMI::POPIS\n\n")
        listaProblema = repozitorij.get_issues(state = "all")
        povratnaLista = []
        for problem in listaProblema:
            # print("Napredak...")
            rjecnik = {}
            rjecnik["broj problema"] = problem.number
            rjecnik["naslov"] = problem.title
            rjecnik["stanje"] = problem.state
            povratnaLista.append(rjecnik)
            with open("rezultati.txt", "a", encoding = "utf-8") as datoteka:
                datoteka.write(f"broj: {rjecnik['broj problema']}, naslov: {rjecnik['naslov']}, stanje: {rjecnik['stanje']}\n")
        with open("rezultati.txt", "a", encoding = "utf-8") as datoteka:
            datoteka.write("\n" + "-" * 80 + "\n\n")
        return povratnaLista



class StatistikaProblemiBroj(StatistikaProblemi):
    def izracunaj(self, repozitorij):
        
        with open("rezultati.txt", "a", encoding = "utf-8") as datoteka:
            datoteka.write("PROBLEMI::BROJ\n\n")
        listaProblema = repozitorij.get_issues(state = "all")

        rjecnikClanoviOtvoreno = {}
        rjecnikClanoviZatvoreno = {}

        for problem in listaProblema:
            # print("Napredak...")
            if problem.state == "open":
                if problem.user.login not in rjecnikClanoviOtvoreno:
                    rjecnikClanoviOtvoreno[problem.user.login] = 1
                else:
                    rjecnikClanoviOtvoreno[problem.user.login] += 1
            elif problem.state == "closed":
                if problem.user.login not in rjecnikClanoviZatvoreno:
                    rjecnikClanoviZatvoreno[problem.user.login] = 1
                else:
                    rjecnikClanoviZatvoreno[problem.user.login] += 1
        
        povratnaLista = []
    
        for kljuc in rjecnikClanoviOtvoreno.keys():
            rjecnik = {}
            rjecnik["ime"] = kljuc
            rjecnik["broj otvorenih problema"] = rjecnikClanoviOtvoreno[kljuc]
            if kljuc in rjecnikClanoviZatvoreno.keys():
                rjecnik["broj zatvorenih problema"] = rjecnikClanoviZatvoreno[kljuc]
            else:
                rjecnik["broj zatvorenih problema"] = 0
            povratnaLista.append(rjecnik)
            with open("rezultati.txt", "a", encoding = "utf-8") as datoteka:
                datoteka.write(f"ime: {kljuc}, broj otvorenih: {rjecnik['broj otvorenih problema']}, broj zatvorenih: {rjecnik['broj zatvorenih problema']}\n")
        
        for kljuc in rjecnikClanoviZatvoreno.keys():
            if kljuc not in rjecnikClanoviOtvoreno.keys():
                rjecnik = {}
                rjecnik["ime"] = kljuc
                rjecnik["broj otvorenih problema"] = 0
                rjecnik["broj zatvorenih problema"] = rjecnikClanoviZatvoreno[kljuc]
                povratnaLista.append(rjecnik)
                with open("rezultati.txt", "a", encoding = "utf-8") as datoteka:
                    datoteka.write(f"ime: {kljuc}, broj otvorenih: {rjecnik['broj otvorenih problema']}, broj zatvorenih: {rjecnik['broj zatvorenih problema']}\n")
        with open("rezultati.txt", "a", encoding = "utf-8") as datoteka:
            datoteka.write("\n" + "-" * 80 + "\n\n")
        return povratnaLista
    
class StatistikaProblemiVrijeme(StatistikaProblemi):
    def izracunaj(self, repozitorij):
        
        with open("rezultati.txt", "a", encoding = "utf-8") as datoteka:
            datoteka.write("PROBLEMI::VRIJEME\n\n")
        listaZatvorenihProblema = repozitorij.get_issues(state = "closed")
        brojac = 0
        ukupno_sati = 0
        for zahtjev in listaZatvorenihProblema:
            # print("Napredak...")
            brojac += 1
            otvoreno = zahtjev.created_at
            zatvoreno = zahtjev.closed_at
            vrijeme_sati = (zatvoreno - otvoreno).total_seconds() / 3600
            ukupno_sati += vrijeme_sati
        if brojac != 0:
            prosjecno_sati = ukupno_sati / brojac
        else:
            prosjecno_sati = "NEMA"
        with open("rezultati.txt", "a", encoding = "utf-8") as datoteka:
            datoteka.write(f"prosjecno sati: {prosjecno_sati}\n")
            datoteka.write("\n" + "-" * 80 + "\n\n")
        return prosjecno_sati

class StatistikaProblemiLabele(StatistikaProblemi):
    def izracunaj(self, repozitorij):
        
        with open("rezultati.txt", "a", encoding = "utf-8") as datoteka:
            datoteka.write("PROBLEMI::LABELE\n\n")
        listaProblema = repozitorij.get_issues(state = "all")
        povratniRjecnik = {}
        for problem in listaProblema:
            # print("Napredak...")
            labele = problem.labels
            for labela in labele:
                if labela.name not in povratniRjecnik.keys():
                    povratniRjecnik[labela.name] = 1
                else:
                    povratniRjecnik[labela.name] += 1
        with open("rezultati.txt", "a", encoding = "utf-8") as datoteka:
            for labela in povratniRjecnik.keys():
                datoteka.write(f"labela: {labela}, broj: {povratniRjecnik[labela]}\n")
            datoteka.write("\n" + "-" * 80 + "\n\n")
        return povratniRjecnik
    
class StatistikaProblemiKomentari(StatistikaProblemi):
    def izracunaj(self, repozitorij):
        
        with open("rezultati.txt", "a", encoding = "utf-8") as datoteka:
            datoteka.write("PROBLEMI::KOMENTARI\n\n")
        listaProblema = repozitorij.get_issues(state = "all")
        ukupno_komentara = 0
        brojac = 0
        for problem in listaProblema:
            # print("Napredak...")
            brojac += 1
            ukupno_komentara += problem.get_comments().totalCount
        if brojac != 0:
            prosjecno_komentara = ukupno_komentara / brojac
        else:
            prosjecno_komentara = "NEMA"
        with open("rezultati.txt", "a", encoding = "utf-8") as datoteka:
            datoteka.write(f"prosjecno komentara: {prosjecno_komentara}\n")
            datoteka.write("\n" + "-" * 80 + "\n\n")
        return prosjecno_komentara
            

class StatistikaRasprave(Statistika):
    pass

class StatistikaRasprave():
    pass






class AnalizatorRepozitorija:
    def __init__(self, repozitorij):
        self.repozitorij = repozitorij
        self.kalkulatori = []

    def dodaj_kalkulator(self, kalkulator):
        if isinstance(kalkulator, Kalkulator):
            self.kalkulatori.append(kalkulator)
        else:
            raise TypeError

    def ukloni_kalkulator(self, kalkulator):
        self.kalkulatori.remove(kalkulator)

    def pokreni_kalkulatore(self):
        rezultati = []
        for kalkulator in self.kalkulatori:
            rezultati.append(kalkulator.racunaj_statistike(self.repozitorij))
        return rezultati



def getCommitCount(github_link):
    autentifikator = Auth.Token("")
    
    g = Github(auth = autentifikator)
    
    # autentificirani_korisnik = g.get_user()
    # repozitoriji = autentificirani_korisnik.get_repos()
    for repo in g.get_user().get_repos():
        github_path = re.sub(r'^https://github\.com/', '', github_link)
        # print(repo.full_name, end=": ")
        if github_path == repo.full_name:
            # print(repo.full_name, end=": ")
            A = AnalizatorRepozitorija(repo)
            kalkulator_predaje = KalkulatorPredaje()
            kalkulator_predaje.dodaj_statistiku(StatistikaPredajeBroj())
            A.dodaj_kalkulator(kalkulator_predaje)
            rez = A.pokreni_kalkulatore()
            # print(rez[0][0])
            # break
            return rez[0][0]

# getCommitCount("https://github.com/KrsticevicM/PROGI2023")

    # autentifikator = Auth.Token(UBACI TOKEN KAO STRING)
    
    # g = Github(auth = autentifikator)
    
    # autentificirani_korisnik = g.get_user()
    # repozitoriji = autentificirani_korisnik.get_repos()
    # brojac = 1
    # for repozitorij in repozitoriji:
    #     moj_repozitorij = repozitorij
    #     print(f"REPOZITORIJ BROJ {brojac}: {moj_repozitorij.name}")
        
    #     with open("rezultati.txt", "a", encoding = "utf-8") as datoteka:
    #         datoteka.write(f"REPOZITORIJ BROJ {brojac}: {moj_repozitorij.name}\n\n")
    #     print(f"Analizira se repozitorij broj {brojac}: {moj_repozitorij.name}")

    #     A = AnalizatorRepozitorija(moj_repozitorij)

    #     kalkulator_predaje = KalkulatorPredaje()
    #     kalkulator_zahtjevi = KalkulatorZahtjevi()
    #     kalkulator_problemi = KalkulatorProblemi()
        
    #     kalkulator_predaje.dodaj_statistiku(StatistikaPredajePopis())     #Vraca popis commitova
    #     kalkulator_predaje.dodaj_statistiku(StatistikaPredajePredaje())            #Vraca broj commitova po korisniku te postotak od ukupnog broja po korisniku/100
    #     kalkulator_predaje.dodaj_statistiku(StatistikaPredajeDodavanja())        #Broj additiona i postotak od ukupnog po korisniku/100
    #     kalkulator_predaje.dodaj_statistiku(StatistikaPredajeUklanjanja())       #Broj deletiona i postotak od ukupnog po korisniku/100
    #     kalkulator_predaje.dodaj_statistiku(StatistikaPredajeUkupno())       #Additions + deletions
    #     kalkulator_predaje.dodaj_statistiku(StatistikaPredajeBroj())         #Broj svih commitova u cijelom repozitoriju

    #     kalkulator_zahtjevi.dodaj_statistiku(StatistikaZahtjeviPopis())
    #     kalkulator_zahtjevi.dodaj_statistiku(StatistikaZahtjeviBroj())
    #     kalkulator_zahtjevi.dodaj_statistiku(StatistikaZahtjeviKomentari())
    #     kalkulator_zahtjevi.dodaj_statistiku(StatistikaZahtjeviVrijeme())
        
    #     kalkulator_problemi.dodaj_statistiku(StatistikaProblemiPopis())          #Popis issuea
    #     kalkulator_problemi.dodaj_statistiku(StatistikaProblemiBroj())           #Broj issuea po korisniku
    #     kalkulator_problemi.dodaj_statistiku(StatistikaProblemiKomentari())      #Prosjecan broj komentara na issueu
    #     kalkulator_problemi.dodaj_statistiku(StatistikaProblemiVrijeme())        #Prosjecno vrijeme potrebno za zatvaranje issuea u satima
    #     kalkulator_problemi.dodaj_statistiku(StatistikaProblemiLabele())         #Broj issuea po vrsti labele (bug, enhancement, ...)
        
    #     A.dodaj_kalkulator(kalkulator_predaje)
    #     A.dodaj_kalkulator(kalkulator_zahtjevi)
    #     A.dodaj_kalkulator(kalkulator_problemi)
        
    #     rez = A.pokreni_kalkulatore()

    #     print(rez)
        
    #     brojac += 1



    