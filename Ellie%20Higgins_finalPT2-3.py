from vpython import *
#Web VPython 3.2

G = 6.67E-11
c = 3E8

def force(planet1, planet2):
    r = planet1.pos - planet2.pos
    F = (-1)*G*planet1.mass*planet2.mass*norm(r)/mag(r)**2
    return F
    
def vel(RfromSun):
     v = sqrt(G*MSu/RfromSun)
     return v
    
RSu = 696265
MSu = 2E30
velSu = 0
sunMom = vec(0,0,0)

RMe = 2440
MMe =0.33E24
RMeS = 61E6
velMe = vel(RMeS)
mercuryMom = MMe*vec(0, velMe,0)


RV = 6052
MV = 4.87E24
RVS = 108E6
velV = vel(RVS)
venusMom = MV*vec(0, velV,0)

RE = 6371
ME = 6E24
RES = 91E6
velE = vel(RES)
earthMom = ME*vec(0, velE,0)

RMa = 3390
MMa = 0.642E24
RMaS = 229E6
velMa = vel(RMaS)
marsMom = MMa*vec(0, velMa,0)

RJ = 69911
MJ = 1898E24
RJS = 778E6
velJ = vel(RJS)
jupiterMom = MJ*vec(0, velJ,0)

RSa = 58232
MSa = 568E24
RSaS = 1.4E9
velSa = vel(RSaS)
saturnMom = MSa*vec(0, velSa,0)

RU = 25362
MU = 86E24
RUS = 3E9
velU = vel(RUS)
uranusMom = MU*vec(0, velU,0)

RN = 24622
MN = 102E24
RNS = 4.5E9
velN = vel(RNS)
neptuneMom = MN*vec(0, velN,0)

RC = 5
MC = 1E24
RCS = 5E9
velC = vel(RCS)
cometMom = MC*vec(-2*velC,-velC,0)

dt = 0.5
t = 0

Sun = sphere(pos = vec(0,0,0), mass = MSu, radius = RSu, color = vec(1,1,0))
Mercury = sphere(pos = Sun.pos + vec(RMeS, 0,0), mass = MMe, radius = RMe, color = vec(0.5,0.5,0.5), make_trail = True)
Venus = sphere(pos = Sun.pos + vec(RVS, 0,0), mass = MV, radius = RV, color = vec(1,0,0), make_trail = True)
Earth = sphere(pos = Sun.pos + vec(RES, 0,0), mass = ME, radius = RE,  color = vec(0,0,1), make_trail = True)
Mars = sphere(pos = Sun.pos + vec(RMaS, 0,0), mass = MMa, radius = RMa,  color = vec(1,0.6,0), make_trail = True)
Jupiter = sphere(pos = Sun.pos + vec(RJS, 0,0), mass = MJ, radius = RJ,  color = vec(0,1,0), make_trail = True)
Saturn = sphere(pos = Sun.pos + vec(RSaS, 0,0), mass = MSa, radius = RSa,  color = vec(0.4,0.2,0.6), make_trail = True)
Uranus = sphere(pos = Sun.pos + vec(RUS, 0,0), mass = MU, radius = RU,  color = vec(1,0,1), make_trail = True)
Neptune = sphere(pos = Sun.pos + vec(RNS, 0,0), mass = MN, radius = RN,  color =  vec(0,1,1), make_trail = True)
Comet = sphere(pos = Sun.pos + vec(RCS, 0,0), mass = MC, radius = RC, color = vec(1,1,1), make_trail = True)


while (True):
    rate(100000)
    
    sunForce = force(Sun, Mercury) + force(Sun, Venus) + force(Sun, Earth) + force(Sun, Mars) + force(Sun, Jupiter) + force(Sun, Saturn) + force(Sun, Uranus) + force(Sun, Neptune)
    mercuryForce = force(Mercury, Sun) + force(Mercury, Venus) + force(Mercury, Earth) + force(Mercury, Mars) + force(Mercury, Jupiter) + force(Mercury, Saturn) + force(Mercury,Uranus) + force(Mercury, Neptune) 
    venusForce = force(Venus, Sun) + force(Venus, Mercury) + force(Venus, Earth) + force(Venus, Mars) + force(Venus, Jupiter) + force(Venus, Saturn) + force(Venus, Uranus) + force(Venus, Neptune) 
    earthForce = force(Earth, Sun) + force(Earth, Mercury) + force(Earth, Venus) + force(Earth, Mars) + force(Earth, Jupiter) + force(Earth, Saturn) + force(Earth, Uranus) + force(Earth, Neptune) 
    marsForce = force(Mars, Sun) + force(Mars, Mercury) + force(Mars, Venus) + force(Mars, Earth) + force(Mars, Jupiter) + force(Mars, Saturn) + force(Mars, Uranus) + force(Mars, Neptune)
    jupiterForce = force(Jupiter, Sun) + force(Jupiter, Mercury) + force(Jupiter, Venus) + force(Jupiter, Earth) + force(Jupiter, Mars) + force(Jupiter, Saturn) + force(Jupiter, Uranus) + force(Jupiter, Neptune) 
    saturnForce = force(Saturn, Sun) + force(Saturn, Mercury) + force(Saturn, Venus) + force(Saturn, Earth) + force(Saturn, Mars) + force(Saturn, Jupiter) + force(Saturn, Uranus) + force(Saturn, Neptune) 
    uranusForce = force(Uranus, Sun) + force(Uranus, Mercury) + force(Uranus, Venus) + force(Uranus, Earth) + force(Uranus, Mars) + force(Uranus, Jupiter) + force(Uranus, Saturn) + force(Uranus, Neptune) 
    neptuneForce = force(Neptune, Sun) + force(Neptune, Mercury) + force(Neptune, Venus) + force(Neptune, Earth) + force(Neptune, Mars) + force(Neptune, Jupiter) + force(Neptune, Saturn) + force(Neptune, Uranus) 
    cometForce = force(Comet, Sun) 
    
    sunMom = sunMom + sunForce*dt
    mercuryMom = mercuryMom + mercuryForce*dt
    venusMom = venusMom + venusForce*dt
    earthMom = earthMom + earthForce*dt
    marsMom = marsMom + marsForce*dt
    jupiterMom = jupiterMom + jupiterForce*dt
    saturnMom = saturnMom + saturnForce*dt
    uranusMom = uranusMom + uranusForce*dt
    neptuneMom = neptuneMom + neptuneForce*dt
    cometMom = cometMom + cometForce*dt
    
    Sun.pos = Sun.pos + sunMom*dt/MSu
    Mercury.pos = Mercury.pos + mercuryMom*dt/MMe
    Venus.pos = Venus.pos + venusMom*dt/MV
    Earth.pos = Earth.pos + earthMom*dt/ME
    Mars.pos = Mars.pos + marsMom*dt/MMa
    Jupiter.pos = Jupiter.pos + jupiterMom*dt/MJ
    Saturn.pos = Saturn.pos + saturnMom*dt/MSa
    Uranus.pos = Uranus.pos + uranusMom*dt/MU
    Neptune.pos = Neptune.pos + neptuneMom*dt/MN
    Comet.pos = Comet.pos + cometMom*dt/MC
    
    t = t+dt