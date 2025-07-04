from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from faker import Faker
from datetime import timedelta
from random import randint
 
from futbol.models import *
 
faker = Faker(["es_CA","es_ES"])
 
class Command(BaseCommand):
    help = 'Crea una lliga amb equips i jugadors'
 
    #per definir arguments
    def add_arguments(self, parser):
        parser.add_argument('titol_lliga', nargs=1, type=str)
 
    def handle(self, *args, **options):
        titol_lliga = options['titol_lliga'][0]
        lliga = Lliga.objects.filter(nom=titol_lliga)
        if lliga.count()>0:
            print("Aquesta lliga ja està creada. Posa un altre nom.")
            return
 
        print("Creem la nova lliga: {}".format(titol_lliga))
        lliga = Lliga( nom=titol_lliga, temporada="temporada" )
        lliga.save()
 
        print("Creem equips")
        prefixos = ["RCD", "Athletic", "", "Deportivo", "Unión Deportiva","FC"]
        for i in range(20):
            ciutat = faker.city()
            prefix = prefixos[randint(0,len(prefixos)-1)]
            if prefix:
                prefix += " "
            nom =  prefix + ciutat
            equip = Equip(ciutat=ciutat,nom=nom)
            equip.save()
            equip.lliga.add(lliga)
 
            #per cada equip creo 25 jugadors
            print("Creem jugadors de l'equip "+nom)
            for j in range(25):
                nom = faker.name()
                posicio = "jugador"
                data_naixement = timezone.now()-timedelta(days=24*365)
                jugador = Jugador(nom=nom,posicio=posicio,dorsal=j,
                    data_naixement=data_naixement,equip=equip)
                #print(jugador)
                jugador.save()
 
        print("Creem partits de la lliga")
        for local in lliga.equips.all():
            for visitant in lliga.equips.all():
                if local!=visitant:
                    partit = Partit(local=local,visitant=visitant,
                                    data=timezone.now())
                    partit.local = local
                    partit.visitant = visitant
                    partit.lliga = lliga
                    partit.save()


                    # creem gools locals
                    for i in range(randint(0,6)):
                        gol=Event(partit=partit,temps=timezone.now(), tipus="GOL", equip=local,
                                  jugador=local.jugadors.all()[randint(0,24)])
                        gol.save()
                        #partit.events.add(gol)

                    # creem gools visitant
                    for i in range(randint(0,6)):
                        gol=Event(partit=partit,temps=timezone.now(), tipus="GOL", equip=visitant,
                                  jugador=visitant.jugadors.all()[randint(0,24)])
                        gol.save()
                        #partit.events.add(gol)


