import random
random.seed(123456)

sigmax = 0.08
sigmay = 0.17
sigmaz = 0.12
sigmaphix = 0.00027
sigmaphiy = 0.00044
sigmaphiz = 0.00024

print """<MuonAlignment>
"""

for wheel in -2, -1, 0, +1, +2:
    for station in 1, 2, 3, 4:
        sectors = range(1, 12+1)
        if station == 4: sectors = range(1, 14+1)
        for sector in sectors:
            mean_y = -0.34
            if wheel>0 : mean_y = 0.34
            x = random.gauss(0., sigmax)
            y = random.gauss(mean_y, sigmay)#!!
            z = random.gauss(0., sigmaz)
            phix = random.gauss(0., sigmaphix)
            phiy = random.gauss(0., sigmaphiy)
            phiz = random.gauss(0., sigmaphiz)

            print """<operation>
  <DTChamber wheel="%(wheel)d" station="%(station)d" sector="%(sector)d" />
  <setposition relativeto="ideal" x="%(x)g" y="%(y)g" z="%(z)g" phix="%(phix)g" phiy="%(phiy)g" phiz="%(phiz)g" />
</operation>
""" % vars()
            
for endcap in 1, 2:
    for chamberNumber in range(1, 36+1):
        x = random.gauss(0., sigmax)
        y = random.gauss(0., sigmay)
        z = random.gauss(0., sigmaz)
        phix = random.gauss(0., sigmaphix)
        phiy = random.gauss(0., sigmaphiy)
        phiz = random.gauss(0., sigmaphiz)

        print """<operation>
  <CSCChamber endcap="%(endcap)d" station="1" ring="1" chamber="%(chamberNumber)d" />
  <CSCChamber endcap="%(endcap)d" station="1" ring="4" chamber="%(chamberNumber)d" />
  <setposition relativeto="ideal" x="%(x)g" y="%(y)g" z="%(z)g" phix="%(phix)g" phiy="%(phiy)g" phiz="%(phiz)g" />
</operation>
""" % vars()

for endcap in 1, 2:
    for station, ring in [(1, 2), (1, 3), (2, 1), (2, 2), (3, 1), (3, 2), (4, 1), (4, 2)]:
        chamberNumbers = range(1, 36+1)
        if (station, ring) in [(2, 1), (3, 1), (4, 1)]: chamberNumbers = range(1, 18+1)
        for chamberNumber in chamberNumbers:
            x = random.gauss(0., sigmax)
            y = random.gauss(0., sigmay)
            z = random.gauss(0., sigmaz)
            phix = random.gauss(0., sigmaphix)
            phiy = random.gauss(0., sigmaphiy)
            phiz = random.gauss(0., sigmaphiz)

            print """<operation>
  <CSCChamber endcap="%(endcap)d" station="%(station)d" ring="%(ring)d" chamber="%(chamberNumber)d" />
  <setposition relativeto="ideal" x="%(x)g" y="%(y)g" z="%(z)g" phix="%(phix)g" phiy="%(phiy)g" phiz="%(phiz)g" />
</operation>
""" % vars()

print """</MuonAlignment>
"""
