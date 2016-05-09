nan = None;  NAN = None
nan = 0
reports = []
class ValErr:
    def __init__(self, value, error, antisym):
        self.value, self.error, self.antisym = value, error, antisym

    def __repr__(self):
        if self.antisym == 0.:
            return "%g +- %g" % (self.value, self.error)
        else:
            return "%g +- %g ~ %g" % (self.value, self.error, self.antisym)

class Report:
    def __init__(self, chamberId, postal_address, name):
        self.chamberId, self.postal_address, self.name = chamberId, postal_address, name
        self.status = "NOFIT"
        self.fittype = None

    def add_parameters(self, deltax, deltay, deltaz, deltaphix, deltaphiy, deltaphiz, loglikelihood, numsegments, sumofweights, redchi2):
        self.status = "PASS"
        self.deltax, self.deltay, self.deltaz, self.deltaphix, self.deltaphiy, self.deltaphiz = deltax, deltay, deltaz, deltaphix, deltaphiy, deltaphiz
        self.loglikelihood, self.numsegments, self.sumofweights, self.redchi2 = loglikelihood, numsegments, sumofweights, redchi2

    def add_stats(self, median_x, median_y, median_dxdz, median_dydz, mean30_x, mean30_y, mean20_dxdz, mean50_dydz, mean15_x, mean15_y, mean10_dxdz, mean25_dydz, wmean30_x, wmean30_y, wmean20_dxdz, wmean50_dydz, wmean15_x, wmean15_y, wmean10_dxdz, wmean25_dydz, stdev30_x, stdev30_y, stdev20_dxdz, stdev50_dydz, stdev15_x, stdev15_y, stdev10_dxdz, stdev25_dydz):
        self.median_x, self.median_y, self.median_dxdz, self.median_dydz, self.mean30_x, self.mean30_y, self.mean20_dxdz, self.mean50_dydz, self.mean15_x, self.mean15_y, self.mean10_dxdz, self.mean25_dydz, self.wmean30_x, self.wmean30_y, self.wmean20_dxdz, self.wmean50_dydz, self.wmean15_x, self.wmean15_y, self.wmean10_dxdz, self.wmean25_dydz, self.stdev30_x, self.stdev30_y, self.stdev20_dxdz, self.stdev50_dydz, self.stdev15_x, self.stdev15_y, self.stdev10_dxdz, self.stdev25_dydz = median_x, median_y, median_dxdz, median_dydz, mean30_x, mean30_y, mean20_dxdz, mean50_dydz, mean15_x, mean15_y, mean10_dxdz, mean25_dydz, wmean30_x, wmean30_y, wmean20_dxdz, wmean50_dydz, wmean15_x, wmean15_y, wmean10_dxdz, wmean25_dydz, stdev30_x, stdev30_y, stdev20_dxdz, stdev50_dydz, stdev15_x, stdev15_y, stdev10_dxdz, stdev25_dydz

    def __repr__(self):
        return "<Report %s %s %s>" % (self.postal_address[0], " ".join(map(str, self.postal_address[1:])), self.status)

reports.append(Report(574914560, ("DT", -2, 1, 1), "MBwhAst1sec01"))
reports[-1].posNum = 103458
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(4.92837e-05, 0.00268609, 0), \
                           ValErr(7.4288e-05, 0.00381261, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.36291e-06, 3.7629e-05, 0), \
                           -294505, 103458, 103458, -nan)
reports[-1].sigmax = ValErr(0.823107, 0.0018095, 0)
reports[-1].sigmay = ValErr(1.22557, 0.00269427, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00217242, -0.0017012, -8.42548e-05, -0.00163757, 9.84489e-05, 6.62584e-05, -6.64218e-05, -0.000764281, 9.84489e-05, 6.62584e-05, -6.64218e-05, -0.000764281, 0.0033706, 0.00252044, -7.8608e-05, -0.000942188, 0.0033706, 0.00252044, -7.8608e-05, -0.000942188, 0.823107, 1.22557, 0.00409309, 0.0287645, 0.823107, 1.22557, 0.00409309, 0.0287645)

reports.append(Report(575176704, ("DT", -2, 1, 2), "MBwhAst1sec02"))
reports[-1].posNum = 100510
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000103975, 0.0027523, 0), \
                           ValErr(0.000612038, 0.00383027, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.02462e-05, 3.82535e-05, 0), \
                           -285770, 100510, 100510, -nan)
reports[-1].sigmax = ValErr(0.827992, 0.00184675, 0)
reports[-1].sigmay = ValErr(1.21418, 0.00270811, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00323295, 0.00477427, -0.000152545, -0.00139269, 0.000336864, 0.000595477, -0.000141261, -0.000749117, 0.000336864, 0.000595477, -0.000141261, -0.000749117, -0.00140073, -0.00249457, -0.00013098, -0.000949726, -0.00140073, -0.00249457, -0.00013098, -0.000949726, 0.827991, 1.21419, 0.00410368, 0.0287898, 0.827991, 1.21419, 0.00410368, 0.0287898)

reports.append(Report(575438848, ("DT", -2, 1, 3), "MBwhAst1sec03"))
reports[-1].posNum = 97974
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000216334, 0.00276708, 0), \
                           ValErr(-2.64573e-05, 0.0038878, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.4554e-06, 3.86115e-05, 0), \
                           -277035, 97974, 97974, -nan)
reports[-1].sigmax = ValErr(0.813997, 0.00183888, 0)
reports[-1].sigmay = ValErr(1.216, 0.00274702, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00215423, 0.00116359, 1.53716e-07, -0.00192025, 0.000180701, -2.09156e-05, -6.36921e-06, -0.00101095, 0.000180701, -2.09156e-05, -6.36921e-06, -0.00101095, 0.00135285, 0.00213054, -1.38166e-05, -0.00128258, 0.00135285, 0.00213054, -1.38166e-05, -0.00128258, 0.813997, 1.216, 0.00404594, 0.0286377, 0.813997, 1.216, 0.00404594, 0.0286377)

reports.append(Report(575700992, ("DT", -2, 1, 4), "MBwhAst1sec04"))
reports[-1].posNum = 102566
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-3.76006e-05, 0.00249735, 0), \
                           ValErr(0.000111927, 0.00374408, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(7.98496e-06, 3.71488e-05, 0), \
                           -291031, 102566, 102566, -nan)
reports[-1].sigmax = ValErr(0.821029, 0.00178814, 0)
reports[-1].sigmay = ValErr(1.21752, 0.00256768, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(6.81229e-05, -0.000943438, -2.76078e-05, -0.0016507, 0.000133402, 8.02703e-05, -2.83687e-05, -0.000906748, 0.000133402, 8.02703e-05, -2.83687e-05, -0.000906748, 0.00250211, -0.00695068, -3.89483e-05, -0.000983132, 0.00250211, -0.00695068, -3.89483e-05, -0.000983132, 0.821029, 1.21752, 0.00407683, 0.0288267, 0.821029, 1.21752, 0.00407683, 0.0288267)

reports.append(Report(575963136, ("DT", -2, 1, 5), "MBwhAst1sec05"))
reports[-1].posNum = 99874
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(7.70105e-06, 0.00274715, 0), \
                           ValErr(0.000277418, 0.00385917, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.92155e-06, 3.82933e-05, 0), \
                           -283787, 99874, 99874, -nan)
reports[-1].sigmax = ValErr(0.822909, 0.00184124, 0)
reports[-1].sigmay = ValErr(1.21955, 0.00272872, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00133753, 0.000631534, -3.85091e-05, -0.00144637, 5.19072e-05, 0.000275281, -3.969e-05, -0.00071905, 5.19072e-05, 0.000275281, -3.969e-05, -0.00071905, 0.00189072, -0.00259947, -5.15403e-05, -0.000922714, 0.00189072, -0.00259947, -5.15403e-05, -0.000922714, 0.822909, 1.21955, 0.00408617, 0.0289482, 0.822909, 1.21955, 0.00408617, 0.0289482)

reports.append(Report(576225280, ("DT", -2, 1, 6), "MBwhAst1sec06"))
reports[-1].posNum = 98646
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.00028329, 0.00277071, 0), \
                           ValErr(-0.000676041, 0.00387792, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.9588e-06, 3.84783e-05, 0), \
                           -279434, 98646, 98646, -nan)
reports[-1].sigmax = ValErr(0.817234, 0.00183989, 0)
reports[-1].sigmay = ValErr(1.2173, 0.00274059, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00141477, -0.00283293, 9.19011e-05, -0.00149678, 3.78322e-05, -0.000642181, 9.66209e-05, -0.000817307, 3.78322e-05, -0.000642181, 9.66209e-05, -0.000817307, -0.00158169, 0.0024514, 0.00010649, -0.000948427, -0.00158169, 0.0024514, 0.00010649, -0.000948427, 0.817237, 1.21731, 0.00406785, 0.0288771, 0.817237, 1.21731, 0.00406785, 0.0288771)

reports.append(Report(576487424, ("DT", -2, 1, 7), "MBwhAst1sec07"))
reports[-1].posNum = 102420
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-7.01849e-05, 0.00268812, 0), \
                           ValErr(0.000128091, 0.00381243, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.23423e-06, 3.77068e-05, 0), \
                           -290479, 102420, 102420, -nan)
reports[-1].sigmax = ValErr(0.818749, 0.00180902, 0)
reports[-1].sigmay = ValErr(1.21927, 0.00269398, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0013617, 0.00442547, 1.47804e-07, -0.00166148, -9.7293e-05, 0.000132581, -9.67882e-06, -0.000858351, -9.7293e-05, 0.000132581, -9.67882e-06, -0.000858351, -0.00135812, -0.00287169, -8.35351e-07, -0.00103712, -0.00135812, -0.00287169, -8.35351e-07, -0.00103712, 0.818749, 1.21927, 0.00406435, 0.0287686, 0.818749, 1.21927, 0.00406435, 0.0287686)

reports.append(Report(576749568, ("DT", -2, 1, 8), "MBwhAst1sec08"))
reports[-1].posNum = 98892
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000617132, 0.00274956, 0), \
                           ValErr(-0.000320062, 0.00386937, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.01247e-06, 3.83419e-05, 0), \
                           -280297, 98892, 98892, -nan)
reports[-1].sigmax = ValErr(0.819038, 0.00184166, 0)
reports[-1].sigmay = ValErr(1.21668, 0.00273578, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00148487, -0.00360655, -0.000104669, -0.00137328, -0.000592794, -0.000321369, -0.000105324, -0.000638213, -0.000592794, -0.000321369, -0.000105324, -0.000638213, 0.00435895, -0.00192697, -0.00012634, -0.000951186, 0.00435895, -0.00192697, -0.00012634, -0.000951186, 0.81904, 1.21668, 0.004074, 0.0288209, 0.81904, 1.21668, 0.004074, 0.0288209)

reports.append(Report(577011712, ("DT", -2, 1, 9), "MBwhAst1sec09"))
reports[-1].posNum = 98334
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000185238, 0.00280489, 0), \
                           ValErr(-2.08503e-05, 0.00386604, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.65083e-06, 3.88857e-05, 0), \
                           -279138, 98334, 98334, -nan)
reports[-1].sigmax = ValErr(0.826103, 0.00186282, 0)
reports[-1].sigmay = ValErr(1.21147, 0.0027318, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00019421, 0.0023458, -3.02663e-05, -0.00179793, -0.000144926, -2.69478e-05, -1.21863e-05, -0.000871237, -0.000144926, -2.69478e-05, -1.21863e-05, -0.000871237, 0.00141799, 0.00380397, -1.54243e-05, -0.00102188, 0.00141799, 0.00380397, -1.54243e-05, -0.00102188, 0.826102, 1.21147, 0.00410882, 0.0287779, 0.826102, 1.21147, 0.00410882, 0.0287779)

reports.append(Report(577273856, ("DT", -2, 1, 10), "MBwhAst1sec10"))
reports[-1].posNum = 102394
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000347166, 0.00269303, 0), \
                           ValErr(0.000434173, 0.0038214, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(8.12772e-06, 3.76827e-05, 0), \
                           -290916, 102394, 102394, -nan)
reports[-1].sigmax = ValErr(0.821063, 0.00181437, 0)
reports[-1].sigmay = ValErr(1.22192, 0.00270019, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00129675, 0.00571305, -4.31985e-05, -0.00179129, -0.0001784, 0.000403889, -4.51259e-05, -0.000920311, -0.0001784, 0.000403889, -4.51259e-05, -0.000920311, 1.58069e-05, 0.0032027, -4.43198e-05, -0.00117321, 1.58069e-05, 0.0032027, -4.43198e-05, -0.00117321, 0.821061, 1.22192, 0.00408711, 0.028763, 0.821061, 1.22192, 0.00408711, 0.028763)

reports.append(Report(577536000, ("DT", -2, 1, 11), "MBwhAst1sec11"))
reports[-1].posNum = 100102
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000151349, 0.00275225, 0), \
                           ValErr(-8.65587e-05, 0.00385261, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.57695e-07, 3.84955e-05, 0), \
                           -284655, 100102, 100102, -nan)
reports[-1].sigmax = ValErr(0.825177, 0.00184423, 0)
reports[-1].sigmay = ValErr(1.21888, 0.00272414, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00287627, 0.00421645, -2.5992e-05, -0.00123047, 0.000157258, -8.67761e-05, -3.48517e-05, -0.000613939, 0.000157258, -8.67761e-05, -3.48517e-05, -0.000613939, -0.000640403, -0.000646482, -3.0343e-05, -0.000780055, -0.000640403, -0.000646482, -3.0343e-05, -0.000780055, 0.825176, 1.21888, 0.00410066, 0.0289104, 0.825176, 1.21888, 0.00410066, 0.0289104)

reports.append(Report(577798144, ("DT", -2, 1, 12), "MBwhAst1sec12"))
reports[-1].posNum = 97788
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000275894, 0.0027934, 0), \
                           ValErr(-1.06668e-05, 0.00388207, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.75348e-06, 3.87653e-05, 0), \
                           -277030, 97788, 97788, -nan)
reports[-1].sigmax = ValErr(0.820241, 0.00185475, 0)
reports[-1].sigmay = ValErr(1.21319, 0.00274329, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00459671, 0.00240425, 2.8214e-05, -0.00180286, 0.000320059, -1.69692e-05, -9.29915e-06, -0.000935927, 0.000320059, -1.69692e-05, -9.29915e-06, -0.000935927, -0.00022345, -0.00141536, -2.73194e-06, -0.00112905, -0.00022345, -0.00141536, -2.73194e-06, -0.00112905, 0.82024, 1.21319, 0.00408679, 0.0288459, 0.82024, 1.21319, 0.00408679, 0.0288459)

reports.append(Report(579108864, ("DT", -2, 2, 1), "MBwhAst2sec01"))
reports[-1].posNum = 110564
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000117528, 0.00332523, 0), \
                           ValErr(-0.000307216, 0.00451935, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.98788e-06, 4.26625e-05, 0), \
                           -366711, 110564, 110564, -nan)
reports[-1].sigmax = ValErr(1.08821, 0.00231662, 0)
reports[-1].sigmay = ValErr(1.48337, 0.00317126, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00435452, -0.00252878, 4.58829e-05, -0.000488145, 6.19741e-05, -0.000307384, 3.11559e-05, -0.00104437, 6.19741e-05, -0.000307384, 3.11559e-05, -0.00104437, -0.00159862, 0.00357114, 3.79972e-05, -0.00111782, -0.00159862, 0.00357114, 3.79972e-05, -0.00111782, 1.08821, 1.48337, 0.00432276, 0.0231694, 1.08821, 1.48337, 0.00432276, 0.0231694)

reports.append(Report(579371008, ("DT", -2, 2, 2), "MBwhAst2sec02"))
reports[-1].posNum = 109482
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000337225, 0.00335098, 0), \
                           ValErr(0.000199994, 0.00456014, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.64319e-06, 4.30227e-05, 0), \
                           -363085, 109482, 109482, -nan)
reports[-1].sigmax = ValErr(1.08979, 0.00232938, 0)
reports[-1].sigmay = ValErr(1.48072, 0.00317514, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000390991, -0.00203058, 9.1197e-05, -0.000631162, 0.000242606, 0.000196418, 7.96498e-05, -0.00120874, 0.000242606, 0.000196418, 7.96498e-05, -0.00120874, -0.00315275, -0.00176426, 9.70881e-05, -0.00125794, -0.00315275, -0.00176426, 9.70881e-05, -0.00125794, 1.08979, 1.48072, 0.0043057, 0.0230904, 1.08979, 1.48072, 0.0043057, 0.0230904)

reports.append(Report(579633152, ("DT", -2, 2, 3), "MBwhAst2sec03"))
reports[-1].posNum = 109954
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-1.96688e-05, 0.00333551, 0), \
                           ValErr(0.00011446, 0.00454419, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(7.37581e-06, 4.27288e-05, 0), \
                           -364032, 109954, 109954, -nan)
reports[-1].sigmax = ValErr(1.08679, 0.0023192, 0)
reports[-1].sigmay = ValErr(1.47649, 0.00316069, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00400162, -0.00174931, -2.63861e-06, -0.00061051, 8.70061e-05, 0.000116874, 3.15687e-07, -0.00112391, 8.70061e-05, 0.000116874, 3.15687e-07, -0.00112391, 0.000486579, 0.000641828, 1.45811e-06, -0.00117282, 0.000486579, 0.000641828, 1.45811e-06, -0.00117282, 1.08679, 1.47649, 0.00432024, 0.0232631, 1.08679, 1.47649, 0.00432024, 0.0232631)

reports.append(Report(579895296, ("DT", -2, 2, 4), "MBwhAst2sec04"))
reports[-1].posNum = 109582
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000122033, 0.00332718, 0), \
                           ValErr(0.000553286, 0.00446284, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.49064e-06, 4.27039e-05, 0), \
                           -362471, 109582, 109582, -nan)
reports[-1].sigmax = ValErr(1.08292, 0.00231319, 0)
reports[-1].sigmay = ValErr(1.47732, 0.00315566, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00120268, 0.00765305, 4.16112e-05, -0.000669744, -0.000186999, 0.000549966, 2.94566e-05, -0.00115382, -0.000186999, 0.000549966, 2.94566e-05, -0.00115382, -5.64758e-05, 0.000771505, 3.08361e-05, -0.00127061, -5.64758e-05, 0.000771505, 3.08361e-05, -0.00127061, 1.08292, 1.47732, 0.0042953, 0.0231409, 1.08292, 1.47732, 0.0042953, 0.0231409)

reports.append(Report(580157440, ("DT", -2, 2, 5), "MBwhAst2sec05"))
reports[-1].posNum = 109888
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.00012538, 0.00333794, 0), \
                           ValErr(0.000164315, 0.00450729, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.48717e-06, 4.29745e-05, 0), \
                           -365174, 109888, 109888, -nan)
reports[-1].sigmax = ValErr(1.08732, 0.00231937, 0)
reports[-1].sigmay = ValErr(1.49414, 0.00318713, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.000223638, 0.00132615, 2.72365e-06, -0.000671384, 9.84353e-05, 0.00016056, 8.11523e-06, -0.00114646, 9.84353e-05, 0.00016056, 8.11523e-06, -0.00114646, -0.00190244, 0.00423131, 6.95399e-06, -0.00119122, -0.00190244, 0.00423131, 6.95399e-06, -0.00119122, 1.08732, 1.49414, 0.00430984, 0.0231362, 1.08732, 1.49414, 0.00430984, 0.0231362)

reports.append(Report(580419584, ("DT", -2, 2, 6), "MBwhAst2sec06"))
reports[-1].posNum = 109572
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000215536, 0.00332127, 0), \
                           ValErr(-0.000195891, 0.00457202, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.33565e-06, 4.28419e-05, 0), \
                           -362765, 109572, 109572, -nan)
reports[-1].sigmax = ValErr(1.08099, 0.0023093, 0)
reports[-1].sigmay = ValErr(1.48437, 0.00317861, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00534272, -0.00323434, 0.000167112, -0.000756641, -0.000278436, -0.000197227, 0.000177786, -0.00123096, -0.000278436, -0.000197227, 0.000177786, -0.00123096, -0.00377249, 0.00745419, 0.000191539, -0.00136729, -0.00377249, 0.00745419, 0.000191539, -0.00136729, 1.08099, 1.48437, 0.00428792, 0.0231717, 1.08099, 1.48437, 0.00428792, 0.0231717)

reports.append(Report(580681728, ("DT", -2, 2, 7), "MBwhAst2sec07"))
reports[-1].posNum = 110326
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000127114, 0.00331887, 0), \
                           ValErr(0.000591723, 0.00448295, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.42671e-07, 4.26657e-05, 0), \
                           -365943, 110326, 110326, -nan)
reports[-1].sigmax = ValErr(1.0843, 0.00230832, 0)
reports[-1].sigmay = ValErr(1.48901, 0.0031699, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00212885, -0.00228661, 5.56489e-05, -0.000629267, -0.000134425, 0.000590514, 5.20969e-05, -0.00111772, -0.000134425, 0.000590514, 5.20969e-05, -0.00111772, 0.000170414, 0.00423714, 5.24802e-05, -0.00116683, 0.000170414, 0.00423714, 5.24802e-05, -0.00116683, 1.0843, 1.48901, 0.00432272, 0.0231575, 1.0843, 1.48901, 0.00432272, 0.0231575)

reports.append(Report(580943872, ("DT", -2, 2, 8), "MBwhAst2sec08"))
reports[-1].posNum = 109922
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-9.00134e-05, 0.00330335, 0), \
                           ValErr(-0.000268507, 0.00454164, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.16006e-06, 3.8418e-05, 0), \
                           -364770, 109922, 109922, -nan)
reports[-1].sigmax = ValErr(1.08345, 0.00231028, 0)
reports[-1].sigmay = ValErr(1.49246, 0.00310384, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00462724, -0.000473846, 4.99453e-05, -0.00083541, -0.000161704, -0.000273085, 5.4716e-05, -0.00125629, -0.000161704, -0.000273085, 5.4716e-05, -0.00125629, -0.00196966, 0.0017406, 6.04022e-05, -0.00130931, -0.00196966, 0.0017406, 6.04022e-05, -0.00130931, 1.08344, 1.49246, 0.00430131, 0.0231743, 1.08344, 1.49246, 0.00430131, 0.0231743)

reports.append(Report(581206016, ("DT", -2, 2, 9), "MBwhAst2sec09"))
reports[-1].posNum = 109540
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-5.98786e-05, 0.00335427, 0), \
                           ValErr(-0.000448456, 0.00446939, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.32134e-06, 4.29316e-05, 0), \
                           -363273, 109540, 109540, -nan)
reports[-1].sigmax = ValErr(1.09085, 0.00233057, 0)
reports[-1].sigmay = ValErr(1.47922, 0.00316033, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0015831, 0.00660796, 3.55243e-05, -0.000772128, -0.000136579, -0.000448701, 4.81753e-05, -0.00121503, -0.000136579, -0.000448701, 4.81753e-05, -0.00121503, 0.00149389, 0.00263039, 4.49366e-05, -0.00127612, 0.00149389, 0.00263039, 4.49366e-05, -0.00127612, 1.09085, 1.47922, 0.00433837, 0.0231673, 1.09085, 1.47922, 0.00433837, 0.0231673)

reports.append(Report(581468160, ("DT", -2, 2, 10), "MBwhAst2sec10"))
reports[-1].posNum = 110236
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000211212, 0.00335311, 0), \
                           ValErr(0.000107561, 0.00455331, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.62746e-06, 4.28923e-05, 0), \
                           -366145, 110236, 110236, -nan)
reports[-1].sigmax = ValErr(1.09419, 0.00233212, 0)
reports[-1].sigmay = ValErr(1.48226, 0.00316748, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000478986, 0.002862, 3.96165e-05, -0.000695394, 0.00018756, 0.000105886, 3.28286e-05, -0.00118415, 0.00018756, 0.000105886, 3.28286e-05, -0.00118415, 0.00107609, -0.000205734, 3.2366e-05, -0.00126314, 0.00107609, -0.000205734, 3.2366e-05, -0.00126314, 1.09419, 1.48226, 0.00433488, 0.0232561, 1.09419, 1.48226, 0.00433488, 0.0232561)

reports.append(Report(581730304, ("DT", -2, 2, 11), "MBwhAst2sec11"))
reports[-1].posNum = 109548
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-9.83697e-05, 0.00197313, 0), \
                           ValErr(-0.000107272, 0.00461007, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.20396e-06, 3.65192e-05, 0), \
                           -364119, 109548, 109548, -nan)
reports[-1].sigmax = ValErr(1.09074, 0.00232694, 0)
reports[-1].sigmay = ValErr(1.49047, 0.00319162, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000533369, 0.00780842, 7.06952e-05, -0.000557856, -7.15479e-05, -0.000105885, 7.45774e-05, -0.00106029, -7.15479e-05, -0.000105885, 7.45774e-05, -0.00106029, 0.0010445, 0.00067451, 6.86245e-05, -0.00110494, 0.0010445, 0.00067451, 6.86245e-05, -0.00110494, 1.09074, 1.49047, 0.00433174, 0.0232312, 1.09074, 1.49047, 0.00433174, 0.0232312)

reports.append(Report(581992448, ("DT", -2, 2, 12), "MBwhAst2sec12"))
reports[-1].posNum = 110290
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000485274, 0.00157133, 0), \
                           ValErr(0.000518988, 0.00457577, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(7.27198e-06, 4.0532e-05, 0), \
                           -366118, 110290, 110290, -nan)
reports[-1].sigmax = ValErr(1.09271, 0.00232718, 0)
reports[-1].sigmay = ValErr(1.4815, 0.00316368, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00115109, -0.00566728, -7.28028e-05, -0.000619833, 0.000572582, 0.000515878, -6.49995e-05, -0.00111467, 0.000572582, 0.000515878, -6.49995e-05, -0.00111467, 0.00309285, 0.00109127, -7.24792e-05, -0.0011477, 0.00309285, 0.00109127, -7.24792e-05, -0.0011477, 1.09271, 1.48151, 0.00433212, 0.0231808, 1.09271, 1.48151, 0.00433212, 0.0231808)

reports.append(Report(583303168, ("DT", -2, 3, 1), "MBwhAst3sec01"))
reports[-1].posNum = 102696
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-7.37637e-05, 0.00450078, 0), \
                           ValErr(-0.000300985, 0.00566209, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.11574e-06, 4.99883e-05, 0), \
                           -389601, 102696, 102696, -nan)
reports[-1].sigmax = ValErr(1.43389, 0.00316392, 0)
reports[-1].sigmay = ValErr(1.81387, 0.00400234, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0053841, 0.00248907, 6.66382e-05, -0.000480499, -0.000142617, -0.000279819, 5.63875e-05, -0.000389678, -0.000142617, -0.000279819, 5.63875e-05, -0.000389678, -0.00189962, 0.00309235, 5.82921e-05, -0.0002283, -0.00189962, 0.00309235, 5.82921e-05, -0.0002283, 1.43389, 1.81387, 0.00486685, 0.0179574, 1.43389, 1.81387, 0.00486685, 0.0179574)

reports.append(Report(583565312, ("DT", -2, 3, 2), "MBwhAst3sec02"))
reports[-1].posNum = 102450
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000404184, 0.00452193, 0), \
                           ValErr(-1.03105e-05, 0.00569647, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.46421e-06, 5.02613e-05, 0), \
                           -389514, 102450, 102450, -nan)
reports[-1].sigmax = ValErr(1.43865, 0.00317823, 0)
reports[-1].sigmay = ValErr(1.82286, 0.00402704, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00237813, 0.000111798, -0.000126723, -0.000316513, -0.000348745, -2.33477e-05, -0.000109361, -0.00026981, -0.000348745, -2.33477e-05, -0.000109361, -0.00026981, -0.00042531, 0.000796855, -0.000104314, -0.000146576, -0.00042531, 0.000796855, -0.000104314, -0.000146576, 1.43865, 1.82286, 0.00485376, 0.0179767, 1.43865, 1.82286, 0.00485376, 0.0179767)

reports.append(Report(583827456, ("DT", -2, 3, 3), "MBwhAst3sec03"))
reports[-1].posNum = 103338
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.00012917, 0.00447749, 0), \
                           ValErr(-0.000600136, 0.00563629, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.30095e-06, 4.97358e-05, 0), \
                           -391657, 103338, 103338, -nan)
reports[-1].sigmax = ValErr(1.43063, 0.00314692, 0)
reports[-1].sigmay = ValErr(1.81134, 0.00398433, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00454138, -0.000757278, 1.7598e-05, -0.000441517, 0.000104963, -0.000593825, 3.23242e-05, -0.000368737, 0.000104963, -0.000593825, 3.23242e-05, -0.000368737, 0.000705924, 0.00109656, 2.99029e-05, -0.000245738, 0.000705924, 0.00109656, 2.99029e-05, -0.000245738, 1.43063, 1.81134, 0.00483349, 0.0180551, 1.43063, 1.81134, 0.00483349, 0.0180551)

reports.append(Report(584089600, ("DT", -2, 3, 4), "MBwhAst3sec04"))
reports[-1].posNum = 102508
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000333691, 0.00451163, 0), \
                           ValErr(0.000140038, 0.00565965, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.84316e-06, 5.00486e-05, 0), \
                           -388912, 102508, 102508, -nan)
reports[-1].sigmax = ValErr(1.43593, 0.00317134, 0)
reports[-1].sigmay = ValErr(1.81173, 0.00400131, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00429102, 0.00481552, -3.14076e-05, -0.000417525, -0.000299251, 0.000133218, -1.27168e-05, -0.000321624, -0.000299251, 0.000133218, -1.27168e-05, -0.000321624, 0.00559808, 0.00267296, -2.64576e-05, -0.000233214, 0.00559808, 0.00267296, -2.64576e-05, -0.000233214, 1.43593, 1.81173, 0.00483654, 0.0179701, 1.43593, 1.81173, 0.00483654, 0.0179701)

reports.append(Report(584351744, ("DT", -2, 3, 5), "MBwhAst3sec05"))
reports[-1].posNum = 102388
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000611211, 0.00450597, 0), \
                           ValErr(-0.000130759, 0.00569072, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.74633e-06, 5.01129e-05, 0), \
                           -388738, 102388, 102388, -nan)
reports[-1].sigmax = ValErr(1.43301, 0.00316672, 0)
reports[-1].sigmay = ValErr(1.82042, 0.00402286, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.000590189, -0.00652457, 4.91494e-05, -0.000323994, 0.000562234, -0.000113607, 4.36768e-05, -0.000329423, 0.000562234, -0.000113607, 4.36768e-05, -0.000329423, -0.00232972, 0.0047225, 4.86906e-05, -0.000196649, -0.00232972, 0.0047225, 4.86906e-05, -0.000196649, 1.43301, 1.82041, 0.00485017, 0.0179937, 1.43301, 1.82041, 0.00485017, 0.0179937)

reports.append(Report(584613888, ("DT", -2, 3, 6), "MBwhAst3sec06"))
reports[-1].posNum = 103260
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(6.69907e-05, 0.00449936, 0), \
                           ValErr(0.000358506, 0.00566757, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.11903e-06, 5.00214e-05, 0), \
                           -392360, 103260, 103260, -nan)
reports[-1].sigmax = ValErr(1.43699, 0.00316208, 0)
reports[-1].sigmay = ValErr(1.82084, 0.00400674, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00676743, 0.00191664, 4.02392e-05, -0.000452762, 3.54846e-05, 0.000366263, 6.4841e-05, -0.000517156, 3.54846e-05, 0.000366263, 6.4841e-05, -0.000517156, 0.00331149, 0.00746554, 6.06395e-05, -0.000418702, 0.00331149, 0.00746554, 6.06395e-05, -0.000418702, 1.43699, 1.82084, 0.00485824, 0.0181562, 1.43699, 1.82084, 0.00485824, 0.0181562)

reports.append(Report(584876032, ("DT", -2, 3, 7), "MBwhAst3sec07"))
reports[-1].posNum = 102806
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000264584, 0.00451326, 0), \
                           ValErr(-0.000210421, 0.00567343, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.38341e-06, 5.00396e-05, 0), \
                           -390633, 102806, 102806, -nan)
reports[-1].sigmax = ValErr(1.43855, 0.0031725, 0)
reports[-1].sigmay = ValErr(1.81884, 0.00401117, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00171296, -0.0036301, 3.23788e-05, -0.000523348, 0.000288767, -0.000214799, 2.64571e-05, -0.000430073, 0.000288767, -0.000214799, 2.64571e-05, -0.000430073, -0.00186006, 0.00344632, 3.785e-05, -0.000368076, -0.00186006, 0.00344632, 3.785e-05, -0.000368076, 1.43855, 1.81884, 0.00487633, 0.0180047, 1.43855, 1.81884, 0.00487633, 0.0180047)

reports.append(Report(585138176, ("DT", -2, 3, 8), "MBwhAst3sec08"))
reports[-1].posNum = 102010
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000203367, 0.00452825, 0), \
                           ValErr(0.000209138, 0.00574734, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.76068e-06, 5.04784e-05, 0), \
                           -388505, 102010, 102010, -nan)
reports[-1].sigmax = ValErr(1.43823, 0.00318414, 0)
reports[-1].sigmay = ValErr(1.83531, 0.00406327, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00122801, 0.000371787, 5.39939e-05, -0.000511737, 0.00017758, 0.000214447, 7.03394e-05, -0.000479647, 0.00017758, 0.000214447, 7.03394e-05, -0.000479647, -4.94374e-05, -0.00460044, 6.99312e-05, -0.000362619, -4.94374e-05, -0.00460044, 6.99312e-05, -0.000362619, 1.43822, 1.83531, 0.004865, 0.0180021, 1.43822, 1.83531, 0.004865, 0.0180021)

reports.append(Report(585400320, ("DT", -2, 3, 9), "MBwhAst3sec09"))
reports[-1].posNum = 103220
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000529223, 0.00451164, 0), \
                           ValErr(-0.00022127, 0.00565559, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.64993e-07, 5.00122e-05, 0), \
                           -392246, 103220, 103220, -nan)
reports[-1].sigmax = ValErr(1.44096, 0.00317144, 0)
reports[-1].sigmay = ValErr(1.81649, 0.00399796, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0068488, -0.00145566, 9.52405e-06, -0.000316996, -0.000532566, -0.000221797, 9.39609e-06, -0.000330495, -0.000532566, -0.000221797, 9.39609e-06, -0.000330495, -0.00258703, 0.00402302, 9.24103e-06, -0.000192953, -0.00258703, 0.00402302, 9.24103e-06, -0.000192953, 1.44097, 1.81649, 0.00485856, 0.0179576, 1.44097, 1.81649, 0.00485856, 0.0179576)

reports.append(Report(585662464, ("DT", -2, 3, 10), "MBwhAst3sec10"))
reports[-1].posNum = 102442
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.00061792, 0.00449771, 0), \
                           ValErr(-9.98008e-06, 0.00568618, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.19535e-06, 5.01056e-05, 0), \
                           -388756, 102442, 102442, -nan)
reports[-1].sigmax = ValErr(1.43103, 0.00316154, 0)
reports[-1].sigmay = ValErr(1.81959, 0.00401996, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00194184, 0.00409608, 6.26025e-05, -0.000485911, -0.000677719, 3.82045e-06, 5.0586e-05, -0.000412087, -0.000677719, 3.82045e-06, 5.0586e-05, -0.000412087, -0.00296048, -0.00136495, 6.49661e-05, -0.000294503, -0.00296048, -0.00136495, 6.49661e-05, -0.000294503, 1.43103, 1.81959, 0.00482908, 0.0179334, 1.43103, 1.81959, 0.00482908, 0.0179334)

reports.append(Report(585924608, ("DT", -2, 3, 11), "MBwhAst3sec11"))
reports[-1].posNum = 103028
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000278275, 0.00451681, 0), \
                           ValErr(-0.000875734, 0.00564921, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.11533e-06, 4.99696e-05, 0), \
                           -391293, 103028, 103028, -nan)
reports[-1].sigmax = ValErr(1.4407, 0.0031738, 0)
reports[-1].sigmay = ValErr(1.8129, 0.00399378, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.000964969, 0.00167336, 4.79942e-05, -0.000366327, 0.000206387, -0.000858683, 5.95451e-05, -0.00033504, 0.000206387, -0.000858683, 5.95451e-05, -0.00033504, 0.000430162, 0.000235147, 5.04038e-05, -0.0002214, 0.000430162, 0.000235147, 5.04038e-05, -0.0002214, 1.44069, 1.81289, 0.00489528, 0.0180064, 1.44069, 1.81289, 0.00489528, 0.0180064)

reports.append(Report(586186752, ("DT", -2, 3, 12), "MBwhAst3sec12"))
reports[-1].posNum = 102548
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-3.33181e-06, 0.00450032, 0), \
                           ValErr(-0.000757409, 0.00569494, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.57008e-07, 5.02197e-05, 0), \
                           -389458, 102548, 102548, -nan)
reports[-1].sigmax = ValErr(1.43242, 0.00316295, 0)
reports[-1].sigmay = ValErr(1.82316, 0.00402575, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0035592, -0.000962735, 1.79624e-05, -0.0003239, -1.57614e-05, -0.000757993, 1.40037e-05, -0.000336557, -1.57614e-05, -0.000757993, 1.40037e-05, -0.000336557, 0.000532004, -0.00439017, 1.27895e-05, -0.000205213, 0.000532004, -0.00439017, 1.27895e-05, -0.000205213, 1.43241, 1.82316, 0.00484484, 0.0179134, 1.43241, 1.82316, 0.00484484, 0.0179134)

reports.append(Report(574947328, ("DT", -1, 1, 1), "MBwhBst1sec01"))
reports[-1].posNum = 178300
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(7.93061e-06, 0.00175923, 0), \
                           ValErr(0.000124982, 0.00194771, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(8.59851e-07, 2.18706e-05, 0), \
                           -415594, 178300, 178300, -nan)
reports[-1].sigmax = ValErr(0.732509, 0.00122666, 0)
reports[-1].sigmay = ValErr(0.822235, 0.00137691, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00026632, 0.000909861, 1.50442e-06, -2.25946e-05, 1.78424e-05, 0.000123405, -2.31012e-06, -0.000630014, 1.78424e-05, 0.000123405, -2.31012e-06, -0.000630014, 0.000319973, 0.000941564, -1.3592e-08, -0.000630533, 0.000319973, 0.000941564, -1.3592e-08, -0.000630533, 0.732508, 0.822235, 0.00366728, 0.0133304, 0.732508, 0.822235, 0.00366728, 0.0133304)

reports.append(Report(575209472, ("DT", -1, 1, 2), "MBwhBst1sec02"))
reports[-1].posNum = 178186
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000101256, 0.00177053, 0), \
                           ValErr(-0.000195701, 0.00195927, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.14483e-06, 2.19817e-05, 0), \
                           -417320, 178186, 178186, -nan)
reports[-1].sigmax = ValErr(0.736574, 0.00123386, 0)
reports[-1].sigmay = ValErr(0.826884, 0.00138513, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000420561, 0.000543714, 4.52347e-05, -2.99081e-05, -0.000171539, -0.000186611, 4.48512e-05, -0.000608961, -0.000171539, -0.000186611, 4.48512e-05, -0.000608961, 0.000202852, 0.000318032, 4.40323e-05, -0.0006164, 0.000202852, 0.000318032, 4.40323e-05, -0.0006164, 0.736575, 0.826886, 0.0036791, 0.0132946, 0.736575, 0.826886, 0.0036791, 0.0132946)

reports.append(Report(575471616, ("DT", -1, 1, 3), "MBwhBst1sec03"))
reports[-1].posNum = 130802
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000190472, 0.00153829, 0), \
                           ValErr(0.000321913, 0.00231672, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.63614e-06, 2.5795e-05, 0), \
                           -308215, 130802, 130802, -nan)
reports[-1].sigmax = ValErr(0.731731, 0.0014386, 0)
reports[-1].sigmay = ValErr(0.844351, 0.00165359, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0019257, 0.00341096, 6.64566e-05, -1.78907e-05, -0.000250798, 0.000334903, 4.59692e-05, -0.000658165, -0.000250798, 0.000334903, 4.59692e-05, -0.000658165, 0.00152897, 0.000162839, 3.95436e-05, -0.000671208, 0.00152897, 0.000162839, 3.95436e-05, -0.000671208, 0.731731, 0.844351, 0.00357466, 0.0136993, 0.731731, 0.844351, 0.00357466, 0.0136993)

reports.append(Report(575733760, ("DT", -1, 1, 4), "MBwhBst1sec04"))
reports[-1].posNum = 178232
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(1.07139e-05, 0.00176005, 0), \
                           ValErr(-0.000336836, 0.0019599, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.02926e-06, 2.19077e-05, 0), \
                           -416565, 178232, 178232, -nan)
reports[-1].sigmax = ValErr(0.73269, 0.0012272, 0)
reports[-1].sigmay = ValErr(0.827259, 0.0013856, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000553038, -0.000597535, -3.32649e-05, 2.14339e-05, -3.56688e-06, -0.00033485, -2.75933e-05, -0.000603696, -3.56688e-06, -0.00033485, -2.75933e-05, -0.000603696, 4.92744e-05, 0.00147807, -2.70442e-05, -0.000615822, 4.92744e-05, 0.00147807, -2.70442e-05, -0.000615822, 0.732689, 0.827259, 0.00365803, 0.0133382, 0.732689, 0.827259, 0.00365803, 0.0133382)

reports.append(Report(575995904, ("DT", -1, 1, 5), "MBwhBst1sec05"))
reports[-1].posNum = 178004
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000179955, 0.00176073, 0), \
                           ValErr(0.000127856, 0.00196201, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.14517e-07, 2.19502e-05, 0), \
                           -416047, 178004, 178004, -nan)
reports[-1].sigmax = ValErr(0.732428, 0.00122754, 0)
reports[-1].sigmay = ValErr(0.827622, 0.00138708, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000823031, -0.000846972, 1.13432e-05, -1.64123e-05, -0.000181641, 0.000127792, 1.14009e-05, -0.000654412, -0.000181641, 0.000127792, 1.14009e-05, -0.000654412, 0.00270648, -0.000963766, 7.82402e-07, -0.000624163, 0.00270648, -0.000963766, 7.82402e-07, -0.000624163, 0.732428, 0.827622, 0.00365756, 0.0133292, 0.732428, 0.827622, 0.00365756, 0.0133292)

reports.append(Report(576258048, ("DT", -1, 1, 6), "MBwhBst1sec06"))
reports[-1].posNum = 178502
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-3.14779e-05, 0.00176199, 0), \
                           ValErr(0.000131588, 0.00195518, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.21748e-07, 2.1911e-05, 0), \
                           -417244, 178502, 178502, -nan)
reports[-1].sigmax = ValErr(0.734123, 0.00122867, 0)
reports[-1].sigmay = ValErr(0.825866, 0.00138221, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00063607, 0.00214709, 2.48502e-05, -2.59021e-05, -3.32935e-05, 0.000132755, 3.00228e-05, -0.000682679, -3.32935e-05, 0.000132755, 3.00228e-05, -0.000682679, 0.000135108, -0.000231905, 2.77945e-05, -0.000669426, 0.000135108, -0.000231905, 2.77945e-05, -0.000669426, 0.734122, 0.825865, 0.0036615, 0.0133305, 0.734122, 0.825865, 0.0036615, 0.0133305)

reports.append(Report(576520192, ("DT", -1, 1, 7), "MBwhBst1sec07"))
reports[-1].posNum = 178368
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000219614, 0.00176551, 0), \
                           ValErr(-9.13543e-05, 0.00195391, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.997e-07, 2.19367e-05, 0), \
                           -417023, 178368, 178368, -nan)
reports[-1].sigmax = ValErr(0.73527, 0.00123105, 0)
reports[-1].sigmay = ValErr(0.825001, 0.00138128, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00148486, 0.00102709, -1.29356e-05, -1.45485e-08, -0.000218105, -9.19733e-05, -1.30008e-05, -0.000668626, -0.000218105, -9.19733e-05, -1.30008e-05, -0.000668626, -0.000988819, 0.000460268, -1.03111e-05, -0.000694335, -0.000988819, 0.000460268, -1.03111e-05, -0.000694335, 0.73527, 0.825003, 0.00366925, 0.0133711, 0.73527, 0.825003, 0.00366925, 0.0133711)

reports.append(Report(576782336, ("DT", -1, 1, 8), "MBwhBst1sec08"))
reports[-1].posNum = 177802
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000248918, 0.00176901, 0), \
                           ValErr(-0.000165269, 0.00196147, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.52917e-06, 2.20157e-05, 0), \
                           -416127, 177802, 177802, -nan)
reports[-1].sigmax = ValErr(0.735335, 0.00123312, 0)
reports[-1].sigmay = ValErr(0.826916, 0.00138669, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00267982, 0.000842784, -4.19836e-06, 1.40958e-05, -0.00022802, -0.000167929, -7.88314e-06, -0.000599116, -0.00022802, -0.000167929, -7.88314e-06, -0.000599116, -0.000996986, 0.000317019, -4.55809e-06, -0.000601411, -0.000996986, 0.000317019, -4.55809e-06, -0.000601411, 0.735333, 0.826916, 0.00367294, 0.0133165, 0.735333, 0.826916, 0.00367294, 0.0133165)

reports.append(Report(577044480, ("DT", -1, 1, 9), "MBwhBst1sec09"))
reports[-1].posNum = 178878
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000146707, 0.0017557, 0), \
                           ValErr(4.33265e-06, 0.00195115, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.5019e-07, 2.18582e-05, 0), \
                           -417406, 178878, 178878, -nan)
reports[-1].sigmax = ValErr(0.73195, 0.00122374, 0)
reports[-1].sigmay = ValErr(0.825005, 0.00137932, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00220966, 0.001445, 1.80765e-05, -2.99079e-05, 0.000139341, 3.98831e-06, 1.51029e-05, -0.000650486, 0.000139341, 3.98831e-06, 1.51029e-05, -0.000650486, 0.00183812, 0.00155876, 6.07654e-06, -0.000648732, 0.00183812, 0.00155876, 6.07654e-06, -0.000648732, 0.731952, 0.825003, 0.00365576, 0.0133141, 0.731952, 0.825003, 0.00365576, 0.0133141)

reports.append(Report(577306624, ("DT", -1, 1, 10), "MBwhBst1sec10"))
reports[-1].posNum = 177512
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(7.6719e-05, 0.00175746, 0), \
                           ValErr(2.18516e-05, 0.00196588, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.07626e-07, 2.19264e-05, 0), \
                           -414395, 177512, 177512, -nan)
reports[-1].sigmax = ValErr(0.72993, 0.00122505, 0)
reports[-1].sigmay = ValErr(0.82811, 0.00138983, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000569354, -0.000890907, 3.57821e-05, -3.90007e-05, 8.56887e-05, 2.11756e-05, 3.05552e-05, -0.000682675, 8.56887e-05, 2.11756e-05, 3.05552e-05, -0.000682675, 0.000722207, -0.000695106, 3.44944e-05, -0.000705959, 0.000722207, -0.000695106, 3.44944e-05, -0.000705959, 0.72993, 0.828109, 0.0036428, 0.0133552, 0.72993, 0.828109, 0.0036428, 0.0133552)

reports.append(Report(577568768, ("DT", -1, 1, 11), "MBwhBst1sec11"))
reports[-1].posNum = 178398
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(4.39408e-05, 0.00176717, 0), \
                           ValErr(4.35164e-05, 0.00195654, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.51969e-06, 2.19739e-05, 0), \
                           -417601, 178398, 178398, -nan)
reports[-1].sigmax = ValErr(0.736313, 0.00123269, 0)
reports[-1].sigmay = ValErr(0.826184, 0.00138315, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00124884, -0.000319685, 1.30737e-06, -3.52124e-05, 0.000121662, 3.25228e-05, 1.00667e-05, -0.000687857, 0.000121662, 3.25228e-05, 1.00667e-05, -0.000687857, 0.000147962, 0.00101846, 1.05297e-05, -0.000692456, 0.000147962, 0.00101846, 1.05297e-05, -0.000692456, 0.736314, 0.826183, 0.00367405, 0.0133772, 0.736314, 0.826183, 0.00367405, 0.0133772)

reports.append(Report(577830912, ("DT", -1, 1, 12), "MBwhBst1sec12"))
reports[-1].posNum = 177490
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000105949, 0.00175848, 0), \
                           ValErr(-7.69263e-05, 0.00195635, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.88347e-07, 2.19063e-05, 0), \
                           -413629, 177490, 177490, -nan)
reports[-1].sigmax = ValErr(0.730619, 0.00122628, 0)
reports[-1].sigmay = ValErr(0.824008, 0.00138302, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000133965, 0.0010759, -3.7758e-05, 1.92956e-05, -0.000104422, -7.72517e-05, -2.65199e-05, -0.000643425, -0.000104422, -7.72517e-05, -2.65199e-05, -0.000643425, 0.00123252, -0.00169903, -3.50078e-05, -0.00064139, 0.00123252, -0.00169903, -3.50078e-05, -0.00064139, 0.730619, 0.824007, 0.0036539, 0.0133367, 0.730619, 0.824007, 0.0036539, 0.0133367)

reports.append(Report(579141632, ("DT", -1, 2, 1), "MBwhBst2sec01"))
reports[-1].posNum = 153132
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(1.57873e-05, 0.00255331, 0), \
                           ValErr(-0.000147898, 0.00272519, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.52625e-06, 2.83758e-05, 0), \
                           -442908, 153132, 153132, -nan)
reports[-1].sigmax = ValErr(0.990218, 0.00178931, 0)
reports[-1].sigmay = ValErr(1.0664, 0.00192696, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00156537, -0.00228089, -3.45511e-05, -3.06008e-05, 9.4658e-05, -0.000142849, -2.9661e-05, -0.000355094, 9.4658e-05, -0.000142849, -2.9661e-05, -0.000355094, -0.00179443, 0.000755168, -2.06916e-05, -0.000375491, -0.00179443, 0.000755168, -2.06916e-05, -0.000375491, 0.990216, 1.06639, 0.00395817, 0.012348, 0.990216, 1.06639, 0.00395817, 0.012348)

reports.append(Report(579403776, ("DT", -1, 2, 2), "MBwhBst2sec02"))
reports[-1].posNum = 152744
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-4.24369e-05, 0.00255644, 0), \
                           ValErr(0.000228511, 0.00274463, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.82259e-06, 2.85114e-05, 0), \
                           -442674, 152744, 152744, -nan)
reports[-1].sigmax = ValErr(0.990212, 0.00179157, 0)
reports[-1].sigmay = ValErr(1.07262, 0.00194066, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00169476, -0.00170251, -4.26552e-05, 1.1963e-05, 2.79332e-05, 0.000234167, -3.82936e-05, -0.000341971, 2.79332e-05, 0.000234167, -3.82936e-05, -0.000341971, -0.00125405, -0.000657726, -3.20254e-05, -0.000302159, -0.00125405, -0.000657726, -3.20254e-05, -0.000302159, 0.990211, 1.07262, 0.00393627, 0.0123232, 0.990211, 1.07262, 0.00393627, 0.0123232)

reports.append(Report(579665920, ("DT", -1, 2, 3), "MBwhBst2sec03"))
reports[-1].posNum = 122810
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000194817, 0.00188253, 0), \
                           ValErr(-7.96405e-05, 0.00318013, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.68479e-06, 3.21863e-05, 0), \
                           -354241, 122810, 122810, -nan)
reports[-1].sigmax = ValErr(0.975804, 0.00199215, 0)
reports[-1].sigmay = ValErr(1.07367, 0.00216516, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.000140435, 0.00206373, 2.65525e-05, 0.000126801, -0.000167783, -7.11657e-05, 3.3589e-05, -0.000339648, -0.000167783, -7.11657e-05, 3.3589e-05, -0.000339648, -7.49591e-05, 0.00010091, 3.56869e-05, -0.000315147, -7.49591e-05, 0.00010091, 3.56869e-05, -0.000315147, 0.975803, 1.07367, 0.00379597, 0.0125874, 0.975803, 1.07367, 0.00379597, 0.0125874)

reports.append(Report(579928064, ("DT", -1, 2, 4), "MBwhBst2sec04"))
reports[-1].posNum = 152770
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000131052, 0.00254426, 0), \
                           ValErr(0.00013714, 0.00274346, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.13852e-06, 2.8418e-05, 0), \
                           -442031, 152770, 152770, -nan)
reports[-1].sigmax = ValErr(0.985884, 0.00178358, 0)
reports[-1].sigmay = ValErr(1.07227, 0.00193987, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000555665, 0.000438312, -1.53797e-05, -2.75948e-05, -9.45307e-05, 0.00013914, -2.16647e-05, -0.000340121, -9.45307e-05, 0.00013914, -2.16647e-05, -0.000340121, -0.0013049, -0.000687821, -2.14873e-05, -0.000368108, -0.0013049, -0.000687821, -2.14873e-05, -0.000368108, 0.985884, 1.07227, 0.00392736, 0.012379, 0.985884, 1.07227, 0.00392736, 0.012379)

reports.append(Report(580190208, ("DT", -1, 2, 5), "MBwhBst2sec05"))
reports[-1].posNum = 152710
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000356068, 0.00255083, 0), \
                           ValErr(2.56843e-05, 0.00274497, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.83021e-06, 2.84205e-05, 0), \
                           -442244, 152710, 152710, -nan)
reports[-1].sigmax = ValErr(0.988028, 0.00178781, 0)
reports[-1].sigmay = ValErr(1.07266, 0.00194095, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0022355, 0.00133423, 1.28674e-05, 4.7062e-05, -0.000287646, 2.88477e-05, 8.09993e-07, -0.000322315, -0.000287646, 2.88477e-05, 8.09993e-07, -0.000322315, 0.000576801, -0.000270047, -2.57372e-06, -0.0003096, 0.000576801, -0.000270047, -2.57372e-06, -0.0003096, 0.988027, 1.07266, 0.00394588, 0.0123801, 0.988027, 1.07266, 0.00394588, 0.0123801)

reports.append(Report(580452352, ("DT", -1, 2, 6), "MBwhBst2sec06"))
reports[-1].posNum = 153188
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000520115, 0.00253899, 0), \
                           ValErr(0.000112654, 0.00273274, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.34818e-06, 2.83219e-05, 0), \
                           -442747, 153188, 153188, -nan)
reports[-1].sigmax = ValErr(0.985225, 0.00177996, 0)
reports[-1].sigmay = ValErr(1.06954, 0.00193229, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00079894, 9.8659e-05, 2.9997e-05, 1.29378e-05, -0.000559539, 0.000110148, 2.92417e-05, -0.00033227, -0.000559539, 0.000110148, 2.92417e-05, -0.00033227, -0.00276601, 0.00253425, 3.57237e-05, -0.000333595, -0.00276601, 0.00253425, 3.57237e-05, -0.000333595, 0.985225, 1.06954, 0.00391808, 0.0123221, 0.985225, 1.06954, 0.00391808, 0.0123221)

reports.append(Report(580714496, ("DT", -1, 2, 7), "MBwhBst2sec07"))
reports[-1].posNum = 152692
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(1.72438e-06, 0.00255039, 0), \
                           ValErr(-0.000141788, 0.00273235, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.4665e-06, 2.83358e-05, 0), \
                           -441448, 152692, 152692, -nan)
reports[-1].sigmax = ValErr(0.98785, 0.0017876, 0)
reports[-1].sigmay = ValErr(1.06765, 0.001932, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00125215, -0.000771647, -3.49494e-05, 1.66508e-05, 6.84295e-05, -0.000137195, -3.55362e-05, -0.000337588, 6.84295e-05, -0.000137195, -3.55362e-05, -0.000337588, 0.00130055, 0.000277593, -3.6677e-05, -0.000331859, 0.00130055, 0.000277593, -3.6677e-05, -0.000331859, 0.987847, 1.06764, 0.00393346, 0.0123759, 0.987847, 1.06764, 0.00393346, 0.0123759)

reports.append(Report(580976640, ("DT", -1, 2, 8), "MBwhBst2sec08"))
reports[-1].posNum = 152882
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(6.68107e-05, 0.00157364, 0), \
                           ValErr(2.40033e-05, 0.00279139, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(8.85794e-07, 2.55883e-05, 0), \
                           -442846, 152882, 152882, -nan)
reports[-1].sigmax = ValErr(0.99088, 0.00183971, 0)
reports[-1].sigmay = ValErr(1.07029, 0.0019366, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00261975, 0.00320163, -1.70974e-06, 4.93041e-05, 8.62701e-05, 2.87978e-05, 5.23899e-06, -0.000328858, 8.62701e-05, 2.87978e-05, 5.23899e-06, -0.000328858, 0.000987714, 0.00256541, 1.73227e-07, -0.00033901, 0.000987714, 0.00256541, 1.73227e-07, -0.00033901, 0.990882, 1.07029, 0.00393233, 0.0123924, 0.990882, 1.07029, 0.00393233, 0.0123924)

reports.append(Report(581238784, ("DT", -1, 2, 9), "MBwhBst2sec09"))
reports[-1].posNum = 153410
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(1.52648e-05, 0.00254127, 0), \
                           ValErr(9.95881e-05, 0.00272878, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.55491e-06, 2.8336e-05, 0), \
                           -443496, 153410, 153410, -nan)
reports[-1].sigmax = ValErr(0.98664, 0.00178123, 0)
reports[-1].sigmay = ValErr(1.06876, 0.00192947, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000314203, 0.000856196, 3.67666e-05, -1.50169e-05, -2.80586e-05, 9.26131e-05, 5.22039e-05, -0.000370646, -2.80586e-05, 9.26131e-05, 5.22039e-05, -0.000370646, -0.000682383, 0.00179289, 5.61894e-05, -0.000362412, -0.000682383, 0.00179289, 5.61894e-05, -0.000362412, 0.986636, 1.06876, 0.0039316, 0.0123661, 0.986636, 1.06876, 0.0039316, 0.0123661)

reports.append(Report(581500928, ("DT", -1, 2, 10), "MBwhBst2sec10"))
reports[-1].posNum = 152496
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000393999, 0.00254669, 0), \
                           ValErr(-4.13935e-05, 0.00272829, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.89495e-07, 2.83303e-05, 0), \
                           -440215, 152496, 152496, -nan)
reports[-1].sigmax = ValErr(0.985633, 0.00178473, 0)
reports[-1].sigmay = ValErr(1.06537, 0.00192912, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00181202, 0.00218407, 1.83546e-05, 8.24762e-06, -0.000396781, -4.27463e-05, 1.1345e-05, -0.00037796, -0.000396781, -4.27463e-05, 1.1345e-05, -0.00037796, -0.000132782, -0.000985556, 1.05684e-05, -0.000350457, -0.000132782, -0.000985556, 1.05684e-05, -0.000350457, 0.985633, 1.06537, 0.00392138, 0.0123818, 0.985633, 1.06537, 0.00392138, 0.0123818)

reports.append(Report(581763072, ("DT", -1, 2, 11), "MBwhBst2sec11"))
reports[-1].posNum = 152930
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000369858, 0.00255827, 0), \
                           ValErr(0.000114696, 0.00272893, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.74656e-06, 2.83769e-05, 0), \
                           -442729, 152930, 152930, -nan)
reports[-1].sigmax = ValErr(0.992163, 0.001794, 0)
reports[-1].sigmay = ValErr(1.06713, 0.00192955, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0009023, 0.00117134, -9.26243e-07, 2.09717e-05, -0.000436032, 0.00010959, 7.10837e-06, -0.000359489, -0.000436032, 0.00010959, 7.10837e-06, -0.000359489, -0.0035071, -0.000645388, 2.3656e-05, -0.000364776, -0.0035071, -0.000645388, 2.3656e-05, -0.000364776, 0.992163, 1.06713, 0.0039616, 0.0123657, 0.992163, 1.06713, 0.0039616, 0.0123657)

reports.append(Report(582025216, ("DT", -1, 2, 12), "MBwhBst2sec12"))
reports[-1].posNum = 152384
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(4.1645e-05, 0.00254554, 0), \
                           ValErr(6.27199e-05, 0.0027397, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.45088e-06, 2.8398e-05, 0), \
                           -440375, 152384, 152384, -nan)
reports[-1].sigmax = ValErr(0.985014, 0.00178426, 0)
reports[-1].sigmay = ValErr(1.06943, 0.00193718, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.000160947, 0.000531526, 1.58591e-06, 5.8677e-05, 7.03112e-05, 6.49354e-05, 3.2324e-06, -0.00031349, 7.03112e-05, 6.49354e-05, 3.2324e-06, -0.00031349, -0.00181218, -0.000124385, 1.00822e-05, -0.000328201, -0.00181218, -0.000124385, 1.00822e-05, -0.000328201, 0.985014, 1.06943, 0.00391638, 0.0123639, 0.985014, 1.06943, 0.00391638, 0.0123639)

reports.append(Report(583335936, ("DT", -1, 3, 1), "MBwhBst3sec01"))
reports[-1].posNum = 134084
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-4.63287e-05, 0.00370057, 0), \
                           ValErr(0.000133334, 0.00387417, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.1599e-07, 3.63294e-05, 0), \
                           -467411, 134084, 134084, -nan)
reports[-1].sigmax = ValErr(1.35016, 0.00259764, 0)
reports[-1].sigmay = ValErr(1.41604, 0.00272867, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00429227, -0.00891936, -1.4415e-05, -8.4157e-05, -4.36271e-05, 0.000132771, -3.86883e-06, -0.00027124, -4.36271e-05, 0.000132771, -3.86883e-06, -0.00027124, 0.000937918, 0.00186007, -5.17656e-06, -0.000262784, 0.000937918, 0.00186007, -5.17656e-06, -0.000262784, 1.35015, 1.41604, 0.00457617, 0.0110234, 1.35015, 1.41604, 0.00457617, 0.0110234)

reports.append(Report(583598080, ("DT", -1, 3, 2), "MBwhBst3sec02"))
reports[-1].posNum = 134036
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000117106, 0.00140151, 0), \
                           ValErr(-0.000313811, 0.00387923, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.40188e-06, 3.57349e-05, 0), \
                           -466478, 134036, 134036, -nan)
reports[-1].sigmax = ValErr(1.3478, 0.00259946, 0)
reports[-1].sigmay = ValErr(1.41043, 0.00272008, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00298536, -0.00189716, 1.47626e-05, -7.27225e-05, 0.000110454, -0.000307577, 2.76319e-05, -0.000229988, 0.000110454, -0.000307577, 2.76319e-05, -0.000229988, 0.00310906, -0.000787555, 1.91879e-05, -0.000232385, 0.00310906, -0.000787555, 1.91879e-05, -0.000232385, 1.3478, 1.41043, 0.00453495, 0.0109168, 1.3478, 1.41043, 0.00453495, 0.0109168)

reports.append(Report(583860224, ("DT", -1, 3, 3), "MBwhBst3sec03"))
reports[-1].posNum = 108652
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000174976, 0.00153841, 0), \
                           ValErr(-0.000204968, 0.00431124, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.90383e-06, 4.1952e-05, 0), \
                           -373357, 108652, 108652, -nan)
reports[-1].sigmax = ValErr(1.30842, 0.0027504, 0)
reports[-1].sigmay = ValErr(1.39036, 0.00295674, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00182958, 0.00829161, 5.768e-05, -8.2102e-05, -0.000180242, -0.000198891, 4.79798e-05, -0.000319525, -0.000180242, -0.000198891, 4.79798e-05, -0.000319525, 0.00178141, -0.00123904, 3.40649e-05, -0.000323355, 0.00178141, -0.00123904, 3.40649e-05, -0.000323355, 1.30842, 1.39036, 0.00440895, 0.0110109, 1.30842, 1.39036, 0.00440895, 0.0110109)

reports.append(Report(584122368, ("DT", -1, 3, 4), "MBwhBst3sec04"))
reports[-1].posNum = 133610
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-3.71136e-05, 0.0020458, 0), \
                           ValErr(-1.65352e-05, 0.00391432, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.08423e-06, 3.59001e-05, 0), \
                           -463932, 133610, 133610, -nan)
reports[-1].sigmax = ValErr(1.33387, 0.00246612, 0)
reports[-1].sigmay = ValErr(1.41386, 0.00271539, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00189883, -0.00220267, -3.55203e-05, -8.83013e-05, -2.92238e-05, -1.40935e-05, -3.32592e-05, -0.00027448, -2.92238e-05, -1.40935e-05, -3.32592e-05, -0.00027448, 0.000493309, 0.00431245, -3.17161e-05, -0.000272129, 0.000493309, 0.00431245, -3.17161e-05, -0.000272129, 1.33387, 1.41386, 0.00453147, 0.0110051, 1.33387, 1.41386, 0.00453147, 0.0110051)

reports.append(Report(584384512, ("DT", -1, 3, 5), "MBwhBst3sec05"))
reports[-1].posNum = 133410
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000197541, 0.00368021, 0), \
                           ValErr(0.00028939, 0.00390305, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.43439e-07, 3.61908e-05, 0), \
                           -464439, 133410, 133410, -nan)
reports[-1].sigmax = ValErr(1.34307, 0.00250315, 0)
reports[-1].sigmay = ValErr(1.41687, 0.00273382, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00280634, 0.00270547, 3.44762e-05, -3.81091e-05, 0.000187371, 0.000292385, 2.41939e-05, -0.000239501, 0.000187371, 0.000292385, 2.41939e-05, -0.000239501, 0.00125115, -0.000754867, 1.0692e-05, -0.000239724, 0.00125115, -0.000754867, 1.0692e-05, -0.000239724, 1.34308, 1.41687, 0.00455414, 0.0109717, 1.34308, 1.41687, 0.00455414, 0.0109717)

reports.append(Report(584646656, ("DT", -1, 3, 6), "MBwhBst3sec06"))
reports[-1].posNum = 133732
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(2.64022e-05, 0.00368914, 0), \
                           ValErr(-5.5731e-05, 0.00389364, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.3153e-06, 3.62888e-05, 0), \
                           -465453, 133732, 133732, -nan)
reports[-1].sigmax = ValErr(1.34432, 0.00257553, 0)
reports[-1].sigmay = ValErr(1.41443, 0.0027317, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0022447, -0.00201428, 3.87323e-05, -0.000146528, 5.71062e-06, -5.02362e-05, 3.84012e-05, -0.000336842, 5.71062e-06, -5.02362e-05, 3.84012e-05, -0.000336842, -0.000883301, -0.000637138, 3.5613e-05, -0.000355759, -0.000883301, -0.000637138, 3.5613e-05, -0.000355759, 1.34432, 1.41443, 0.00453588, 0.0110719, 1.34432, 1.41443, 0.00453588, 0.0110719)

reports.append(Report(584908800, ("DT", -1, 3, 7), "MBwhBst3sec07"))
reports[-1].posNum = 133950
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000270959, 0.00368366, 0), \
                           ValErr(-0.000297626, 0.00386635, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.44902e-06, 3.62401e-05, 0), \
                           -466124, 133950, 133950, -nan)
reports[-1].sigmax = ValErr(1.34323, 0.00259517, 0)
reports[-1].sigmay = ValErr(1.41465, 0.00273314, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00198787, -0.00273028, 1.56539e-05, -9.57925e-05, 0.000250535, -0.000291327, 4.95365e-06, -0.000314802, 0.000250535, -0.000291327, 4.95365e-06, -0.000314802, -7.48512e-06, -0.000235753, 1.04089e-06, -0.000326776, -7.48512e-06, -0.000235753, 1.04089e-06, -0.000326776, 1.34323, 1.41465, 0.00453928, 0.0110865, 1.34323, 1.41465, 0.00453928, 0.0110865)

reports.append(Report(585170944, ("DT", -1, 3, 8), "MBwhBst3sec08"))
reports[-1].posNum = 133622
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000143475, 0.0037068, 0), \
                           ValErr(-5.9791e-06, 0.00388651, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.67316e-06, 3.63256e-05, 0), \
                           -465296, 133622, 133622, -nan)
reports[-1].sigmax = ValErr(1.35078, 0.00260593, 0)
reports[-1].sigmay = ValErr(1.41004, 0.002726, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000546451, -0.00287938, 1.38863e-05, -0.000119751, 0.000166878, -1.26609e-05, -7.21087e-06, -0.000317036, 0.000166878, -1.26609e-05, -7.21087e-06, -0.000317036, 0.00165633, 0.00104521, -2.22147e-05, -0.000314177, 0.00165633, 0.00104521, -2.22147e-05, -0.000314177, 1.35078, 1.41004, 0.00456248, 0.0110872, 1.35078, 1.41004, 0.00456248, 0.0110872)

reports.append(Report(585433088, ("DT", -1, 3, 9), "MBwhBst3sec09"))
reports[-1].posNum = 134252
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-2.59693e-05, 0.00139029, 0), \
                           ValErr(-0.000663731, 0.00388531, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.72245e-06, 3.57385e-05, 0), \
                           -466823, 134252, 134252, -nan)
reports[-1].sigmax = ValErr(1.34051, 0.00252239, 0)
reports[-1].sigmay = ValErr(1.41382, 0.00270515, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00511932, 0.00201949, 5.80562e-06, -0.000130142, 1.56348e-05, -0.000677658, 1.17803e-05, -0.000295027, 1.56348e-05, -0.000677658, 1.17803e-05, -0.000295027, -0.00110627, -0.00214018, 1.58969e-05, -0.000327841, -0.00110627, -0.00214018, 1.58969e-05, -0.000327841, 1.3405, 1.41382, 0.00453839, 0.0110281, 1.3405, 1.41382, 0.00453839, 0.0110281)

reports.append(Report(585695232, ("DT", -1, 3, 10), "MBwhBst3sec10"))
reports[-1].posNum = 133150
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000136677, 0.0014045, 0), \
                           ValErr(9.40049e-05, 0.0039192, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.15662e-06, 3.57647e-05, 0), \
                           -462254, 133150, 133150, -nan)
reports[-1].sigmax = ValErr(1.33827, 0.00258762, 0)
reports[-1].sigmay = ValErr(1.40835, 0.00270557, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00345678, 0.00112375, -4.88075e-06, -0.000142016, 0.000130361, 8.99787e-05, -5.01661e-06, -0.000297235, 0.000130361, 8.99787e-05, -5.01661e-06, -0.000297235, 0.0020857, -0.00125983, -1.25522e-05, -0.000309175, 0.0020857, -0.00125983, -1.25522e-05, -0.000309175, 1.33827, 1.40836, 0.00453761, 0.0109805, 1.33827, 1.40836, 0.00453761, 0.0109805)

reports.append(Report(585957376, ("DT", -1, 3, 11), "MBwhBst3sec11"))
reports[-1].posNum = 133442
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000608608, 0.00369169, 0), \
                           ValErr(0.000378797, 0.00386589, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.12598e-06, 3.62864e-05, 0), \
                           -464146, 133442, 133442, -nan)
reports[-1].sigmax = ValErr(1.34369, 0.00260099, 0)
reports[-1].sigmay = ValErr(1.41194, 0.0027331, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00183962, -0.00226514, -5.18443e-06, -0.00011798, -0.000635664, 0.000385149, 1.14922e-07, -0.000281548, -0.000635664, 0.000385149, 1.14922e-07, -0.000281548, 0.00432479, -0.00147598, -1.62226e-05, -0.000312378, 0.00432479, -0.00147598, -1.62226e-05, -0.000312378, 1.34369, 1.41194, 0.00456451, 0.0109081, 1.34369, 1.41194, 0.00456451, 0.0109081)

reports.append(Report(586219520, ("DT", -1, 3, 12), "MBwhBst3sec12"))
reports[-1].posNum = 133132
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.00012543, 0.00217448, 0), \
                           ValErr(6.60113e-05, 0.00391663, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.32506e-06, 3.60494e-05, 0), \
                           -462835, 133132, 133132, -nan)
reports[-1].sigmax = ValErr(1.34072, 0.00245721, 0)
reports[-1].sigmay = ValErr(1.41261, 0.00271733, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.000500939, 0.000198359, -2.14974e-05, -7.56128e-05, 0.000151419, 5.35619e-05, -2.22427e-05, -0.000248608, 0.000151419, 5.35619e-05, -2.22427e-05, -0.000248608, -0.00296832, 0.000652951, -2.58704e-05, -0.000239013, -0.00296832, 0.000652951, -2.58704e-05, -0.000239013, 1.34071, 1.4126, 0.00453543, 0.0108838, 1.34071, 1.4126, 0.00453543, 0.0108838)

reports.append(Report(574980096, ("DT", 0, 1, 1), "MBwhCst1sec01"))
reports[-1].posNum = 207822
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-5.47887e-05, 0.00109814, 0), \
                           ValErr(-3.48706e-05, 0.00151064, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.77174e-06, 1.4929e-05, 0), \
                           -439112, 207822, 207822, -nan)
reports[-1].sigmax = ValErr(0.702282, 0.00108754, 0)
reports[-1].sigmay = ValErr(0.689677, 0.00106969, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000393858, 0.000702925, 4.85429e-06, 2.38227e-05, -5.37542e-05, -3.95445e-05, 8.81865e-06, 2.03258e-05, -5.37542e-05, -3.95445e-05, 8.81865e-06, 2.03258e-05, 0.00123635, 0.000536845, 6.3842e-06, 1.78213e-05, 0.00123635, 0.000536845, 6.3842e-06, 1.78213e-05, 0.702282, 0.689677, 0.0037192, 0.00848413, 0.702282, 0.689677, 0.0037192, 0.00848413)

reports.append(Report(576028672, ("DT", 0, 1, 5), "MBwhCst1sec05"))
reports[-1].posNum = 207568
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-4.91165e-07, 0.00109747, 0), \
                           ValErr(-7.36532e-05, 0.00151534, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.7169e-06, 1.49947e-05, 0), \
                           -437727, 207568, 207568, -nan)
reports[-1].sigmax = ValErr(0.698834, 0.00108306, 0)
reports[-1].sigmay = ValErr(0.690252, 0.00107156, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000798228, -0.00123117, 9.00979e-06, 1.4967e-05, -7.35849e-07, -8.29748e-05, -3.51997e-06, 8.41293e-06, -7.35849e-07, -8.29748e-05, -3.51997e-06, 8.41293e-06, -0.00292769, -0.000170283, 1.1578e-05, -5.00121e-06, -0.00292769, -0.000170283, 1.1578e-05, -5.00121e-06, 0.698834, 0.690253, 0.00371385, 0.00846532, 0.698834, 0.690253, 0.00371385, 0.00846532)

reports.append(Report(577077248, ("DT", 0, 1, 9), "MBwhCst1sec09"))
reports[-1].posNum = 207300
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-6.05171e-05, 0.00109852, 0), \
                           ValErr(0.000176482, 0.0015173, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.4532e-06, 1.49323e-05, 0), \
                           -436760, 207300, 207300, -nan)
reports[-1].sigmax = ValErr(0.697067, 0.00108094, 0)
reports[-1].sigmay = ValErr(0.690661, 0.00107216, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.000741959, -0.00143978, -9.61292e-06, 1.76148e-05, -5.97271e-05, 0.000183191, -4.98105e-06, 1.02691e-06, -5.97271e-05, 0.000183191, -4.98105e-06, 1.02691e-06, 0.000884388, 0.00170124, -8.15416e-06, -1.17666e-05, 0.000884388, 0.00170124, -8.15416e-06, -1.17666e-05, 0.697067, 0.690661, 0.00369986, 0.00847631, 0.697067, 0.690661, 0.00369986, 0.00847631)

reports.append(Report(575242240, ("DT", 0, 1, 2), "MBwhCst1sec02"))
reports[-1].posNum = 207814
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000231006, 0.00152937, 0), \
                           ValErr(-1.31143e-05, 0.00151197, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.14393e-06, 1.75752e-05, 0), \
                           -437364, 207814, 207814, -nan)
reports[-1].sigmax = ValErr(0.697185, 0.00108142, 0)
reports[-1].sigmay = ValErr(0.688956, 0.00106866, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000660926, 0.000659345, -7.01281e-06, 1.16767e-06, -0.000228079, -1.7269e-05, -1.22187e-05, 4.38995e-06, -0.000228079, -1.7269e-05, -1.22187e-05, 4.38995e-06, -8.57366e-05, -0.00113853, -6.68045e-06, -1.14242e-05, -8.57366e-05, -0.00113853, -6.68045e-06, -1.14242e-05, 0.697185, 0.688957, 0.00368681, 0.00846147, 0.697185, 0.688957, 0.00368681, 0.00846147)

reports.append(Report(576290816, ("DT", 0, 1, 6), "MBwhCst1sec06"))
reports[-1].posNum = 207288
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000213232, 0.00154449, 0), \
                           ValErr(2.14295e-05, 0.0015134, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.04349e-07, 1.76858e-05, 0), \
                           -437959, 207288, 207288, -nan)
reports[-1].sigmax = ValErr(0.703189, 0.00109212, 0)
reports[-1].sigmay = ValErr(0.688703, 0.00106962, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00126076, -0.00164938, 9.97212e-06, -2.60833e-05, 0.000210073, 2.40115e-05, 5.49453e-06, -1.16645e-05, 0.000210073, 2.40115e-05, 5.49453e-06, -1.16645e-05, -0.00123574, -0.000520225, 1.20898e-05, -2.35183e-05, -0.00123574, -0.000520225, 1.20898e-05, -2.35183e-05, 0.703189, 0.688703, 0.00371616, 0.00848684, 0.703189, 0.688703, 0.00371616, 0.00848684)

reports.append(Report(577339392, ("DT", 0, 1, 10), "MBwhCst1sec10"))
reports[-1].posNum = 206894
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-5.45105e-06, 0.0015306, 0), \
                           ValErr(-5.94989e-06, 0.00151293, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.51037e-07, 1.76047e-05, 0), \
                           -434813, 206894, 206894, -nan)
reports[-1].sigmax = ValErr(0.696199, 0.00108229, 0)
reports[-1].sigmay = ValErr(0.687884, 0.00106936, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00136951, 0.00144461, -8.58818e-06, 2.11307e-05, -5.49312e-06, -8.54863e-06, 1.15944e-05, 8.58805e-06, -5.49312e-06, -8.54863e-06, 1.15944e-05, 8.58805e-06, -0.000960128, 0.00017387, 1.36837e-05, 7.26274e-06, -0.000960128, 0.00017387, 1.36837e-05, 7.26274e-06, 0.696199, 0.687884, 0.00368894, 0.00850063, 0.696199, 0.687884, 0.00368894, 0.00850063)

reports.append(Report(575504384, ("DT", 0, 1, 3), "MBwhCst1sec03"))
reports[-1].posNum = 207218
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000155783, 0.00153695, 0), \
                           ValErr(2.6561e-05, 0.00151792, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.15635e-06, 1.76495e-05, 0), \
                           -437355, 207218, 207218, -nan)
reports[-1].sigmax = ValErr(0.699639, 0.00108679, 0)
reports[-1].sigmay = ValErr(0.690677, 0.00107287, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00050211, 0.000452698, 1.8274e-06, -3.48989e-05, 0.000153396, 2.38876e-05, -7.76161e-06, -1.86869e-05, 0.000153396, 2.38876e-05, -7.76161e-06, -1.86869e-05, 0.0005391, 0.000137309, -1.24955e-05, -2.64541e-05, 0.0005391, 0.000137309, -1.24955e-05, -2.64541e-05, 0.699639, 0.690677, 0.00370728, 0.00849203, 0.699639, 0.690677, 0.00370728, 0.00849203)

reports.append(Report(576552960, ("DT", 0, 1, 7), "MBwhCst1sec07"))
reports[-1].posNum = 207634
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000136671, 0.00110073, 0), \
                           ValErr(0.000128654, 0.0015157, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(8.89022e-07, 1.48903e-05, 0), \
                           -437892, 207634, 207634, -nan)
reports[-1].sigmax = ValErr(0.69806, 0.00108153, 0)
reports[-1].sigmay = ValErr(0.691103, 0.0010722, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00103663, 6.16562e-05, 4.06172e-06, 1.06967e-05, -0.000135346, 0.000130844, 5.41197e-06, 8.5834e-06, -0.000135346, 0.000130844, 5.41197e-06, 8.5834e-06, 0.000651436, -0.000851313, 1.11677e-07, 5.63423e-06, 0.000651436, -0.000851313, 1.11677e-07, 5.63423e-06, 0.69806, 0.691103, 0.00369388, 0.00848532, 0.69806, 0.691103, 0.00369388, 0.00848532)

reports.append(Report(577601536, ("DT", 0, 1, 11), "MBwhCst1sec11"))
reports[-1].posNum = 207058
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000130784, 0.00109983, 0), \
                           ValErr(0.000234655, 0.00151201, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(7.46879e-07, 1.48993e-05, 0), \
                           -435553, 207058, 207058, -nan)
reports[-1].sigmax = ValErr(0.697065, 0.00108176, 0)
reports[-1].sigmay = ValErr(0.688343, 0.00106903, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.000867611, 0.000477929, 5.11603e-06, 5.87321e-06, 0.000129565, 0.000236696, -7.73163e-06, -1.75796e-05, 0.000129565, 0.000236696, -7.73163e-06, -1.75796e-05, -2.06851e-05, 0.00142853, -8.31176e-06, -3.17988e-05, -2.06851e-05, 0.00142853, -8.31176e-06, -3.17988e-05, 0.697065, 0.688343, 0.00369235, 0.00850547, 0.697065, 0.688343, 0.00369235, 0.00850547)

reports.append(Report(575766528, ("DT", 0, 1, 4), "MBwhCst1sec04"))
reports[-1].posNum = 207862
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-7.85242e-05, 0.0015302, 0), \
                           ValErr(-1.95146e-05, 0.00151376, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.72231e-07, 1.76073e-05, 0), \
                           -437866, 207862, 207862, -nan)
reports[-1].sigmax = ValErr(0.697647, 0.00108202, 0)
reports[-1].sigmay = ValErr(0.689827, 0.00106989, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(1.4632e-05, 0.000327991, -8.55936e-06, -2.93617e-05, -7.74229e-05, -1.77438e-05, -6.60329e-06, -3.64504e-05, -7.74229e-05, -1.77438e-05, -6.60329e-06, -3.64504e-05, -0.00151768, 0.000173174, -3.70637e-06, -3.66808e-05, -0.00151768, 0.000173174, -3.70637e-06, -3.66808e-05, 0.697647, 0.689827, 0.0037005, 0.00848239, 0.697647, 0.689827, 0.0037005, 0.00848239)

reports.append(Report(576815104, ("DT", 0, 1, 8), "MBwhCst1sec08"))
reports[-1].posNum = 207554
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000122261, 0.0010992, 0), \
                           ValErr(-0.000204945, 0.00151074, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.77283e-06, 1.49221e-05, 0), \
                           -436799, 207554, 207554, -nan)
reports[-1].sigmax = ValErr(0.696761, 0.00107985, 0)
reports[-1].sigmay = ValErr(0.689317, 0.00106924, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000495432, 0.00196643, 5.94548e-06, 1.03617e-05, 0.000121235, -0.000192797, 1.81948e-06, 1.61666e-05, 0.000121235, -0.000192797, 1.81948e-06, 1.61666e-05, 0.0012206, -0.000311774, -2.12683e-06, 3.16953e-05, 0.0012206, -0.000311774, -2.12683e-06, 3.16953e-05, 0.696761, 0.689317, 0.00369342, 0.0085088, 0.696761, 0.689317, 0.00369342, 0.0085088)

reports.append(Report(577863680, ("DT", 0, 1, 12), "MBwhCst1sec12"))
reports[-1].posNum = 207260
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-2.8933e-05, 0.00109831, 0), \
                           ValErr(0.000158817, 0.00151228, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.2015e-06, 1.49464e-05, 0), \
                           -436378, 207260, 207260, -nan)
reports[-1].sigmax = ValErr(0.69769, 0.00108206, 0)
reports[-1].sigmay = ValErr(0.689054, 0.00106954, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.000630346, -0.00160777, 1.32169e-05, 1.61608e-05, -2.8819e-05, 0.000162082, 1.61908e-05, 7.6965e-06, -2.8819e-05, 0.000162082, 1.61908e-05, 7.6965e-06, 0.0012417, 0.00133547, 1.22939e-05, 9.4827e-06, 0.0012417, 0.00133547, 1.22939e-05, 9.4827e-06, 0.69769, 0.689054, 0.0037025, 0.00848025, 0.69769, 0.689054, 0.0037025, 0.00848025)

reports.append(Report(579174400, ("DT", 0, 2, 1), "MBwhCst2sec01"))
reports[-1].posNum = 175144
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(3.30296e-05, 0.00119587, 0), \
                           ValErr(-0.000107471, 0.00210402, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.05462e-06, 2.36765e-05, 0), \
                           -479386, 175144, 175144, -nan)
reports[-1].sigmax = ValErr(0.962174, 0.00161458, 0)
reports[-1].sigmay = ValErr(0.939676, 0.00158329, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.000570307, 0.000424301, 1.25061e-05, 6.26292e-06, 3.31695e-05, -0.000107136, 1.15312e-05, -6.79204e-06, 3.31695e-05, -0.000107136, 1.15312e-05, -6.79204e-06, -0.00086015, -0.00115905, 1.32143e-05, 2.30386e-06, -0.00086015, -0.00115905, 1.32143e-05, 2.30386e-06, 0.962173, 0.939676, 0.00398934, 0.00874725, 0.962173, 0.939676, 0.00398934, 0.00874725)

reports.append(Report(580222976, ("DT", 0, 2, 5), "MBwhCst2sec05"))
reports[-1].posNum = 175090
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.00010465, 0.00119519, 0), \
                           ValErr(-6.79427e-05, 0.00211798, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(8.17435e-08, 2.36032e-05, 0), \
                           -477839, 175090, 175090, -nan)
reports[-1].sigmax = ValErr(0.955831, 0.0015979, 0)
reports[-1].sigmay = ValErr(0.938388, 0.00158541, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00161488, -0.00347027, 1.2598e-05, -7.29895e-07, 0.000103715, -6.80245e-05, 9.73392e-06, 6.61309e-07, 0.000103715, -6.80245e-05, 9.73392e-06, 6.61309e-07, 0.00255275, -0.000393415, 1.68426e-06, -6.60697e-06, 0.00255275, -0.000393415, 1.68426e-06, -6.60697e-06, 0.955827, 0.938388, 0.00397815, 0.00875892, 0.955827, 0.938388, 0.00397815, 0.00875892)

reports.append(Report(581271552, ("DT", 0, 2, 9), "MBwhCst2sec09"))
reports[-1].posNum = 175416
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-8.44254e-05, 0.00119498, 0), \
                           ValErr(1.61202e-05, 0.00210674, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.43476e-06, 2.36053e-05, 0), \
                           -479491, 175416, 175416, -nan)
reports[-1].sigmax = ValErr(0.956799, 0.00160058, 0)
reports[-1].sigmay = ValErr(0.941514, 0.00158689, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000131607, -0.00230433, -1.64366e-06, 1.22358e-05, -8.45213e-05, 1.76651e-05, -5.70865e-06, 8.7623e-06, -8.45213e-05, 1.76651e-05, -5.70865e-06, 8.7623e-06, -0.00295055, -0.00211604, 7.48364e-06, -1.358e-07, -0.00295055, -0.00211604, 7.48364e-06, -1.358e-07, 0.956799, 0.941514, 0.00397895, 0.00871637, 0.956799, 0.941514, 0.00397895, 0.00871637)

reports.append(Report(579436544, ("DT", 0, 2, 2), "MBwhCst2sec02"))
reports[-1].posNum = 175324
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000180158, 0.00119451, 0), \
                           ValErr(0.000195924, 0.00210313, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.46446e-07, 2.36616e-05, 0), \
                           -479642, 175324, 175324, -nan)
reports[-1].sigmax = ValErr(0.958349, 0.0015955, 0)
reports[-1].sigmay = ValErr(0.942157, 0.00159072, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.000440057, -0.00150052, -2.20119e-05, -1.59311e-06, 0.000178807, 0.00019717, -2.00187e-05, 1.06721e-05, 0.000178807, 0.00019717, -2.00187e-05, 1.06721e-05, 0.000558701, -0.000371101, -2.03828e-05, 2.04094e-05, 0.000558701, -0.000371101, -2.03828e-05, 2.04094e-05, 0.958344, 0.942156, 0.00397753, 0.00877768, 0.958344, 0.942156, 0.00397753, 0.00877768)

reports.append(Report(580485120, ("DT", 0, 2, 6), "MBwhCst2sec06"))
reports[-1].posNum = 175440
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(8.87606e-05, 0.00119414, 0), \
                           ValErr(-0.000302643, 0.0021021, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.81539e-07, 2.36602e-05, 0), \
                           -480088, 175440, 175440, -nan)
reports[-1].sigmax = ValErr(0.961861, 0.00159147, 0)
reports[-1].sigmay = ValErr(0.939407, 0.00158507, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0012498, -0.000550996, 1.2787e-05, 2.63945e-05, 8.81665e-05, -0.000304414, 2.02816e-06, 1.40481e-05, 8.81665e-05, -0.000304414, 2.02816e-06, 1.40481e-05, -0.000984009, 0.000640164, 2.98184e-06, 5.87034e-06, -0.000984009, 0.000640164, 2.98184e-06, 5.87034e-06, 0.961856, 0.939406, 0.00398139, 0.00876631, 0.961856, 0.939406, 0.00398139, 0.00876631)

reports.append(Report(581533696, ("DT", 0, 2, 10), "MBwhCst2sec10"))
reports[-1].posNum = 175208
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(1.41332e-05, 0.00119452, 0), \
                           ValErr(6.32064e-05, 0.00212144, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.12095e-07, 2.35634e-05, 0), \
                           -477814, 175208, 175208, -nan)
reports[-1].sigmax = ValErr(0.955183, 0.00159957, 0)
reports[-1].sigmay = ValErr(0.937163, 0.00158266, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00100379, -0.000250571, 1.76971e-05, 3.05144e-05, 1.4011e-05, 6.40771e-05, 1.7128e-05, 4.57738e-05, 1.4011e-05, 6.40771e-05, 1.7128e-05, 4.57738e-05, 0.000689305, -0.00084587, 1.52563e-05, 3.59707e-05, 0.000689305, -0.00084587, 1.52563e-05, 3.59707e-05, 0.95518, 0.937163, 0.00396519, 0.00875269, 0.95518, 0.937163, 0.00396519, 0.00875269)

reports.append(Report(579698688, ("DT", 0, 2, 3), "MBwhCst2sec03"))
reports[-1].posNum = 175252
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000271553, 0.00119742, 0), \
                           ValErr(-1.5792e-05, 0.00210243, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.31751e-06, 2.36437e-05, 0), \
                           -479605, 175252, 175252, -nan)
reports[-1].sigmax = ValErr(0.960122, 0.0015947, 0)
reports[-1].sigmay = ValErr(0.94128, 0.00158938, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(5.38611e-05, 0.00083041, -3.68168e-05, 1.78713e-05, -0.000269676, -1.4255e-05, -4.29099e-05, 2.96103e-05, -0.000269676, -1.4255e-05, -4.29099e-05, 2.96103e-05, -0.00153027, -0.000733694, -4.04192e-05, 2.61022e-05, -0.00153027, -0.000733694, -4.04192e-05, 2.61022e-05, 0.960117, 0.941279, 0.00397248, 0.00879102, 0.960117, 0.941279, 0.00397248, 0.00879102)

reports.append(Report(580747264, ("DT", 0, 2, 7), "MBwhCst2sec07"))
reports[-1].posNum = 175310
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.00021907, 0.00119441, 0), \
                           ValErr(0.000307072, 0.00210788, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.00096e-06, 2.36181e-05, 0), \
                           -479174, 175310, 175310, -nan)
reports[-1].sigmax = ValErr(0.956666, 0.00159529, 0)
reports[-1].sigmay = ValErr(0.941503, 0.0015897, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00063997, -0.00369966, 1.47097e-05, -1.84065e-05, 0.00021689, 0.00030782, 1.45141e-05, -3.44217e-05, 0.00021689, 0.00030782, 1.45141e-05, -3.44217e-05, 0.00131991, -0.00177649, 6.75364e-06, -2.53391e-05, 0.00131991, -0.00177649, 6.75364e-06, -2.53391e-05, 0.95666, 0.941504, 0.00396982, 0.00876511, 0.95666, 0.941504, 0.00396982, 0.00876511)

reports.append(Report(581795840, ("DT", 0, 2, 11), "MBwhCst2sec11"))
reports[-1].posNum = 175140
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-8.6646e-05, 0.0022844, 0), \
                           ValErr(-0.000105148, 0.00224028, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(7.11007e-07, 2.36087e-05, 0), \
                           -477854, 175140, 175140, -nan)
reports[-1].sigmax = ValErr(0.956017, 0.00161531, 0)
reports[-1].sigmay = ValErr(0.937546, 0.00158411, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(3.05334e-05, 7.74546e-05, -2.85102e-05, 1.43119e-05, -8.46765e-05, -0.000105013, -2.56368e-05, 3.97431e-05, -8.46765e-05, -0.000105013, -2.56368e-05, 3.97431e-05, 0.00203258, -0.000277035, -3.70053e-05, 6.36566e-05, 0.00203258, -0.000277035, -3.70053e-05, 6.36566e-05, 0.956019, 0.937547, 0.00396964, 0.00877356, 0.956019, 0.937547, 0.00396964, 0.00877356)

reports.append(Report(579960832, ("DT", 0, 2, 4), "MBwhCst2sec04"))
reports[-1].posNum = 175950
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000209637, 0.00119257, 0), \
                           ValErr(-2.35315e-06, 0.0021065, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.46035e-06, 2.35544e-05, 0), \
                           -480740, 175950, 175950, -nan)
reports[-1].sigmax = ValErr(0.957308, 0.00159434, 0)
reports[-1].sigmay = ValErr(0.939896, 0.00158414, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.000436939, 0.00130698, -7.9963e-06, 3.62471e-06, -0.000207814, -3.31485e-07, -7.93762e-06, 1.68252e-05, -0.000207814, -3.31485e-07, -7.93762e-06, 1.68252e-05, -0.00141248, -0.000201706, -8.79972e-06, 1.53607e-05, -0.00141248, -0.000201706, -8.79972e-06, 1.53607e-05, 0.957304, 0.939895, 0.00397113, 0.00878396, 0.957304, 0.939895, 0.00397113, 0.00878396)

reports.append(Report(581009408, ("DT", 0, 2, 8), "MBwhCst2sec08"))
reports[-1].posNum = 174888
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000118974, 0.00119586, 0), \
                           ValErr(-0.000141479, 0.00211185, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.97227e-06, 2.3646e-05, 0), \
                           -477997, 174888, 174888, -nan)
reports[-1].sigmax = ValErr(0.958643, 0.00160762, 0)
reports[-1].sigmay = ValErr(0.939435, 0.00158773, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.000470976, 0.000900998, -6.44173e-06, -7.36225e-06, 0.000116175, -0.000144249, 1.84714e-06, -7.83133e-06, 0.000116175, -0.000144249, 1.84714e-06, -7.83133e-06, -0.000228762, -0.00111867, 2.25163e-06, -6.4714e-06, -0.000228762, -0.00111867, 2.25163e-06, -6.4714e-06, 0.95864, 0.939435, 0.00396325, 0.00875545, 0.95864, 0.939435, 0.00396325, 0.00875545)

reports.append(Report(582057984, ("DT", 0, 2, 12), "MBwhCst2sec12"))
reports[-1].posNum = 175222
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-5.49815e-06, 0.00119447, 0), \
                           ValErr(2.89382e-05, 0.00211727, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.68663e-07, 2.35939e-05, 0), \
                           -478176, 175222, 175222, -nan)
reports[-1].sigmax = ValErr(0.955476, 0.00159465, 0)
reports[-1].sigmay = ValErr(0.93861, 0.00158514, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.000348572, -0.00180227, 8.07523e-06, 3.17002e-05, -5.5298e-06, 2.86297e-05, 1.99046e-06, 2.3139e-05, -5.5298e-06, 2.86297e-05, 1.99046e-06, 2.3139e-05, 0.000572633, 0.000868767, -3.96947e-06, 4.05225e-05, 0.000572633, 0.000868767, -3.96947e-06, 4.05225e-05, 0.955472, 0.938609, 0.00396614, 0.00878817, 0.955472, 0.938609, 0.00396614, 0.00878817)

reports.append(Report(583368704, ("DT", 0, 3, 1), "MBwhCst3sec01"))
reports[-1].posNum = 144394
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000167668, 0.00349287, 0), \
                           ValErr(-0.000365477, 0.00341005, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.10682e-07, 3.22676e-05, 0), \
                           -488033, 144394, 144394, -nan)
reports[-1].sigmax = ValErr(1.32726, 0.00246983, 0)
reports[-1].sigmay = ValErr(1.29548, 0.0024107, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00195831, -0.00103628, 1.67273e-05, -3.33731e-05, -0.000162947, -0.000366044, 5.48545e-06, -3.02457e-05, -0.000162947, -0.000366044, 5.48545e-06, -3.02457e-05, -0.00217848, -0.000546626, 1.69945e-05, -2.82698e-05, -0.00217848, -0.000546626, 1.69945e-05, -2.82698e-05, 1.32726, 1.29547, 0.00458942, 0.00895535, 1.32726, 1.29547, 0.00458942, 0.00895535)

reports.append(Report(584417280, ("DT", 0, 3, 5), "MBwhCst3sec05"))
reports[-1].posNum = 144420
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000290977, 0.00136451, 0), \
                           ValErr(1.68411e-05, 0.00347246, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.18286e-06, 3.20768e-05, 0), \
                           -486470, 144420, 144420, -nan)
reports[-1].sigmax = ValErr(1.32266, 0.00245612, 0)
reports[-1].sigmay = ValErr(1.2852, 0.00238936, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00146324, -0.00227555, -2.46152e-06, 5.28814e-05, -0.000285978, 1.25069e-05, -7.82181e-06, 4.30343e-05, -0.000285978, 1.25069e-05, -7.82181e-06, 4.30343e-05, -0.00391132, -0.00178376, 4.41345e-06, 3.29096e-05, -0.00391132, -0.00178376, 4.41345e-06, 3.29096e-05, 1.32266, 1.2852, 0.00456422, 0.00892032, 1.32266, 1.2852, 0.00456422, 0.00892032)

reports.append(Report(585465856, ("DT", 0, 3, 9), "MBwhCst3sec09"))
reports[-1].posNum = 144212
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000227385, 0.00133106, 0), \
                           ValErr(0.000129658, 0.00347672, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.21839e-06, 3.20623e-05, 0), \
                           -486042, 144212, 144212, -nan)
reports[-1].sigmax = ValErr(1.32417, 0.00246176, 0)
reports[-1].sigmay = ValErr(1.28617, 0.00238451, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-6.25667e-05, -0.000585967, 9.11693e-06, 1.81566e-05, 0.00022332, 0.000138793, 7.64072e-06, 2.07354e-05, 0.00022332, 0.000138793, 7.64072e-06, 2.07354e-05, 0.000619859, 0.00150977, 5.38964e-06, 1.8308e-05, 0.000619859, 0.00150977, 5.38964e-06, 1.8308e-05, 1.32416, 1.28617, 0.00457389, 0.00893637, 1.32416, 1.28617, 0.00457389, 0.00893637)

reports.append(Report(583630848, ("DT", 0, 3, 2), "MBwhCst3sec02"))
reports[-1].posNum = 143976
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000245449, 0.00131803, 0), \
                           ValErr(9.77026e-05, 0.00336684, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.41891e-06, 3.22187e-05, 0), \
                           -485411, 143976, 143976, -nan)
reports[-1].sigmax = ValErr(1.31758, 0.0024558, 0)
reports[-1].sigmay = ValErr(1.29408, 0.00241204, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00336716, 0.00333243, -4.2454e-05, 3.22549e-06, 0.000240892, 0.000105332, -2.84783e-05, -7.88583e-06, 0.000240892, 0.000105332, -2.84783e-05, -7.88583e-06, -0.00457895, 0.00205566, -1.55919e-05, -1.07216e-05, -0.00457895, 0.00205566, -1.55919e-05, -1.07216e-05, 1.31757, 1.29408, 0.004552, 0.00892496, 1.31757, 1.29408, 0.004552, 0.00892496)

reports.append(Report(584679424, ("DT", 0, 3, 6), "MBwhCst3sec06"))
reports[-1].posNum = 144546
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000120893, 0.00132368, 0), \
                           ValErr(-0.000176713, 0.00340521, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.38235e-06, 3.22634e-05, 0), \
                           -488650, 144546, 144546, -nan)
reports[-1].sigmax = ValErr(1.32861, 0.00247192, 0)
reports[-1].sigmay = ValErr(1.29508, 0.00240758, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.000995253, -0.00373249, -4.8706e-06, -1.05795e-05, -0.0001156, -0.000165169, -2.56308e-06, -1.58898e-05, -0.0001156, -0.000165169, -2.56308e-06, -1.58898e-05, -0.000223871, 0.000375964, -1.83343e-06, -8.64488e-06, -0.000223871, 0.000375964, -1.83343e-06, -8.64488e-06, 1.32861, 1.29508, 0.00457138, 0.00894925, 1.32861, 1.29508, 0.00457138, 0.00894925)

reports.append(Report(585728000, ("DT", 0, 3, 10), "MBwhCst3sec10"))
reports[-1].posNum = 144466
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000469889, 0.00131614, 0), \
                           ValErr(-0.000588849, 0.00337595, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.02407e-06, 3.22121e-05, 0), \
                           -487901, 144466, 144466, -nan)
reports[-1].sigmax = ValErr(1.3256, 0.00246567, 0)
reports[-1].sigmay = ValErr(1.29374, 0.00240636, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000128378, -0.00285578, 2.11662e-05, -4.45476e-05, 0.000460326, -0.000581292, 1.57525e-05, -2.27674e-05, 0.000460326, -0.000581292, 1.57525e-05, -2.27674e-05, -0.00136058, -0.00157864, 2.56848e-05, -3.12583e-05, -0.00136058, -0.00157864, 2.56848e-05, -3.12583e-05, 1.32559, 1.29374, 0.00457163, 0.00890489, 1.32559, 1.29374, 0.00457163, 0.00890489)

reports.append(Report(583892992, ("DT", 0, 3, 3), "MBwhCst3sec03"))
reports[-1].posNum = 144556
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000115724, 0.00131618, 0), \
                           ValErr(-4.47592e-06, 0.00332596, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.24059e-06, 3.21355e-05, 0), \
                           -487935, 144556, 144556, -nan)
reports[-1].sigmax = ValErr(1.32612, 0.0024665, 0)
reports[-1].sigmay = ValErr(1.29081, 0.00240055, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.000138786, 0.000283328, -5.28669e-06, -2.16092e-05, -0.000115166, -1.45551e-05, -1.002e-05, -4.73629e-07, -0.000115166, -1.45551e-05, -1.002e-05, -4.73629e-07, 6.89668e-05, 0.00016368, -1.44219e-05, 1.60261e-05, 6.89668e-05, 0.00016368, -1.44219e-05, 1.60261e-05, 1.32612, 1.2908, 0.00456356, 0.00891615, 1.32612, 1.2908, 0.00456356, 0.00891615)

reports.append(Report(584941568, ("DT", 0, 3, 7), "MBwhCst3sec07"))
reports[-1].posNum = 144096
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(5.97646e-05, 0.00131757, 0), \
                           ValErr(-0.000172999, 0.00336873, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.96724e-06, 3.2175e-05, 0), \
                           -485931, 144096, 144096, -nan)
reports[-1].sigmax = ValErr(1.31856, 0.00245595, 0)
reports[-1].sigmay = ValErr(1.29415, 0.00241058, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00149845, -0.00505995, -1.00149e-05, -5.02699e-05, 5.73209e-05, -0.000163958, -5.09258e-06, -3.38752e-05, 5.73209e-05, -0.000163958, -5.09258e-06, -3.38752e-05, -0.000510764, -0.00062214, 6.67064e-06, -5.05805e-05, -0.000510764, -0.00062214, 6.67064e-06, -5.05805e-05, 1.31856, 1.29415, 0.00456234, 0.00891299, 1.31856, 1.29415, 0.00456234, 0.00891299)

reports.append(Report(585990144, ("DT", 0, 3, 11), "MBwhCst3sec11"))
reports[-1].posNum = 144218
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000387812, 0.00131806, 0), \
                           ValErr(-9.54785e-05, 0.00330846, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(9.88587e-06, 3.21644e-05, 0), \
                           -486111, 144218, 144218, -nan)
reports[-1].sigmax = ValErr(1.32022, 0.00245876, 0)
reports[-1].sigmay = ValErr(1.29045, 0.00240652, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00292884, 0.00106562, -2.16228e-05, -2.59449e-06, -0.000380001, -7.0974e-05, -1.08223e-05, -5.2458e-06, -0.000380001, -7.0974e-05, -1.08223e-05, -5.2458e-06, -0.00290595, 0.00134916, -8.90668e-07, 6.70483e-06, -0.00290595, 0.00134916, -8.90668e-07, 6.70483e-06, 1.32021, 1.29046, 0.00456139, 0.00894051, 1.32021, 1.29046, 0.00456139, 0.00894051)

reports.append(Report(584155136, ("DT", 0, 3, 4), "MBwhCst3sec04"))
reports[-1].posNum = 144184
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000236094, 0.0013366, 0), \
                           ValErr(0.000131743, 0.00339916, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.01111e-06, 3.22146e-05, 0), \
                           -486455, 144184, 144184, -nan)
reports[-1].sigmax = ValErr(1.31881, 0.00245216, 0)
reports[-1].sigmay = ValErr(1.29595, 0.00240004, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00240798, 0.00200024, 1.58227e-05, 2.63991e-05, -0.000231573, 0.000123162, 1.66728e-05, 1.87693e-05, -0.000231573, 0.000123162, 1.66728e-05, 1.87693e-05, 0.00124179, 0.00206549, 1.17928e-05, 1.99817e-05, 0.00124179, 0.00206549, 1.17928e-05, 1.99817e-05, 1.31881, 1.29595, 0.00454733, 0.00890808, 1.31881, 1.29595, 0.00454733, 0.00890808)

reports.append(Report(585203712, ("DT", 0, 3, 8), "MBwhCst3sec08"))
reports[-1].posNum = 144076
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000256218, 0.00131786, 0), \
                           ValErr(-7.11322e-05, 0.00348823, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.50401e-06, 3.21327e-05, 0), \
                           -485403, 144076, 144076, -nan)
reports[-1].sigmax = ValErr(1.31836, 0.00240934, 0)
reports[-1].sigmay = ValErr(1.29021, 0.00237698, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0029389, 0.00414569, 1.28938e-05, 2.17345e-05, -0.000250913, -6.61728e-05, 2.46725e-05, 2.57464e-05, -0.000250913, -6.61728e-05, 2.46725e-05, 2.57464e-05, 0.000585024, -0.00270158, 2.22382e-05, 1.89448e-05, 0.000585024, -0.00270158, 2.22382e-05, 1.89448e-05, 1.31836, 1.29022, 0.00454779, 0.00888461, 1.31836, 1.29022, 0.00454779, 0.00888461)

reports.append(Report(586252288, ("DT", 0, 3, 12), "MBwhCst3sec12"))
reports[-1].posNum = 144286
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-8.73857e-05, 0.00132081, 0), \
                           ValErr(-0.000457263, 0.00342662, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.37725e-06, 3.21454e-05, 0), \
                           -485914, 144286, 144286, -nan)
reports[-1].sigmax = ValErr(1.31933, 0.00245682, 0)
reports[-1].sigmay = ValErr(1.28751, 0.00240903, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00151748, -0.00864083, 2.44589e-05, 8.94142e-06, -8.58829e-05, -0.000460594, 1.57058e-05, 2.03641e-06, -8.58829e-05, -0.000460594, 1.57058e-05, 2.03641e-06, 0.00351754, 0.00112647, 3.23417e-07, 7.72312e-06, 0.00351754, 0.00112647, 3.23417e-07, 7.72312e-06, 1.31933, 1.28751, 0.00454731, 0.00892393, 1.31933, 1.28751, 0.00454731, 0.00892393)

reports.append(Report(575012864, ("DT", 1, 1, 1), "MBwhDst1sec01"))
reports[-1].posNum = 177564
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-3.50395e-05, 0.00176213, 0), \
                           ValErr(0.000163547, 0.0019514, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.03289e-07, 2.18894e-05, 0), \
                           -413792, 177564, 177564, -nan)
reports[-1].sigmax = ValErr(0.732207, 0.00122869, 0)
reports[-1].sigmay = ValErr(0.822176, 0.00137966, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00251674, -0.00282744, 2.01229e-06, -2.46953e-05, -3.79465e-05, 0.000163446, 2.30385e-06, -0.000674027, -3.79465e-05, 0.000163446, 2.30385e-06, -0.000674027, 0.00122278, -9.32179e-05, -4.35196e-06, -0.000701151, 0.00122278, -9.32179e-05, -4.35196e-06, -0.000701151, 0.732206, 0.822177, 0.00366583, 0.013269, 0.732206, 0.822177, 0.00366583, 0.013269)

reports.append(Report(575275008, ("DT", 1, 1, 2), "MBwhDst1sec02"))
reports[-1].posNum = 177722
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000107314, 0.00176268, 0), \
                           ValErr(-0.000330179, 0.00196303, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.86826e-06, 2.19547e-05, 0), \
                           -415420, 177722, 177722, -nan)
reports[-1].sigmax = ValErr(0.732724, 0.00122901, 0)
reports[-1].sigmay = ValErr(0.82744, 0.00138788, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00136304, -0.00237042, 3.31021e-05, 1.27518e-05, 4.06903e-05, -0.000337724, 3.05416e-05, -0.000617656, 4.06903e-05, -0.000337724, 3.05416e-05, -0.000617656, -0.000393096, -0.00330182, 3.01955e-05, -0.000611439, -0.000393096, -0.00330182, 3.01955e-05, -0.000611439, 0.732724, 0.82744, 0.00366374, 0.0133628, 0.732724, 0.82744, 0.00366374, 0.0133628)

reports.append(Report(575537152, ("DT", 1, 1, 3), "MBwhDst1sec03"))
reports[-1].posNum = 177568
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000103803, 0.00176276, 0), \
                           ValErr(0.000367021, 0.00196351, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.84513e-07, 2.19526e-05, 0), \
                           -414934, 177568, 177568, -nan)
reports[-1].sigmax = ValErr(0.732428, 0.00122905, 0)
reports[-1].sigmay = ValErr(0.827187, 0.00138806, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00163842, 0.000658669, 1.19377e-05, -1.96599e-05, -0.000107329, 0.000366366, 1.40351e-05, -0.000629864, -0.000107329, 0.000366366, 1.40351e-05, -0.000629864, -0.00163088, 0.000905265, 1.93427e-05, -0.000630245, -0.00163088, 0.000905265, 1.93427e-05, -0.000630245, 0.732427, 0.827186, 0.00366455, 0.0133763, 0.732427, 0.827186, 0.00366455, 0.0133763)

reports.append(Report(575799296, ("DT", 1, 1, 4), "MBwhDst1sec04"))
reports[-1].posNum = 129440
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(9.24368e-05, 0.00207171, 0), \
                           ValErr(0.000519228, 0.00235937, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.55872e-06, 2.91559e-05, 0), \
                           -306755, 129440, 129440, -nan)
reports[-1].sigmax = ValErr(0.737975, 0.00145042, 0)
reports[-1].sigmay = ValErr(0.848598, 0.00166784, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-1.71555e-05, 0.001073, 9.05875e-06, -5.16227e-05, 5.61258e-05, 0.000512259, 4.91157e-06, -0.000699802, 5.61258e-05, 0.000512259, 4.91157e-06, -0.000699802, -0.003205, 0.000999392, 1.81201e-05, -0.00073008, -0.003205, 0.000999392, 1.81201e-05, -0.00073008, 0.737974, 0.848597, 0.0036416, 0.0137365, 0.737974, 0.848597, 0.0036416, 0.0137365)

reports.append(Report(576061440, ("DT", 1, 1, 5), "MBwhDst1sec05"))
reports[-1].posNum = 178548
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000110859, 0.00176007, 0), \
                           ValErr(-5.79937e-05, 0.00196108, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.14604e-07, 2.19142e-05, 0), \
                           -417642, 178548, 178548, -nan)
reports[-1].sigmax = ValErr(0.73302, 0.00122666, 0)
reports[-1].sigmay = ValErr(0.828454, 0.00138636, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000595441, 0.00100317, -7.41839e-06, 1.6464e-05, -0.000114974, -5.85846e-05, -1.19034e-05, -0.000606515, -0.000114974, -5.85846e-05, -1.19034e-05, -0.000606515, -0.000536215, -7.39769e-05, -1.39244e-05, -0.000650874, -0.000536215, -7.39769e-05, -1.39244e-05, -0.000650874, 0.73302, 0.828455, 0.00365769, 0.013294, 0.73302, 0.828455, 0.00365769, 0.013294)

reports.append(Report(576323584, ("DT", 1, 1, 6), "MBwhDst1sec06"))
reports[-1].posNum = 177926
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-8.43914e-06, 0.00175848, 0), \
                           ValErr(-0.000240404, 0.00195877, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.88068e-06, 2.18732e-05, 0), \
                           -415275, 177926, 177926, -nan)
reports[-1].sigmax = ValErr(0.731383, 0.00122606, 0)
reports[-1].sigmay = ValErr(0.826066, 0.00138478, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(2.38426e-05, 0.000795615, 1.92291e-05, -6.33191e-05, -3.33776e-05, -0.000243778, 1.66179e-05, -0.000684847, -3.33776e-05, -0.000243778, 1.66179e-05, -0.000684847, -0.00126077, 0.0009706, 2.2451e-05, -0.000705684, -0.00126077, 0.0009706, 2.2451e-05, -0.000705684, 0.731383, 0.826066, 0.00365775, 0.0133552, 0.731383, 0.826066, 0.00365775, 0.0133552)

reports.append(Report(576585728, ("DT", 1, 1, 7), "MBwhDst1sec07"))
reports[-1].posNum = 178336
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.00013338, 0.00176774, 0), \
                           ValErr(8.14196e-05, 0.00195622, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.47129e-07, 2.19655e-05, 0), \
                           -417355, 178336, 178336, -nan)
reports[-1].sigmax = ValErr(0.736063, 0.00123248, 0)
reports[-1].sigmay = ValErr(0.826, 0.00138308, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.000635179, -0.00105933, -1.64294e-05, 9.29535e-06, -0.000124467, 8.23364e-05, -1.65767e-05, -0.000621221, -0.000124467, 8.23364e-05, -1.65767e-05, -0.000621221, -0.000322315, -0.00151627, -1.37215e-05, -0.000640228, -0.000322315, -0.00151627, -1.37215e-05, -0.000640228, 0.736063, 0.825999, 0.00366981, 0.0133149, 0.736063, 0.825999, 0.00366981, 0.0133149)

reports.append(Report(576847872, ("DT", 1, 1, 8), "MBwhDst1sec08"))
reports[-1].posNum = 177826
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000146961, 0.00176233, 0), \
                           ValErr(0.00022653, 0.00196882, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.47661e-06, 2.19823e-05, 0), \
                           -416180, 177826, 177826, -nan)
reports[-1].sigmax = ValErr(0.732528, 0.00122832, 0)
reports[-1].sigmay = ValErr(0.830072, 0.00139189, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00225878, -0.00132146, -2.48046e-05, -5.74987e-05, -0.000108523, 0.00023105, -1.90422e-05, -0.000721305, -0.000108523, 0.00023105, -1.90422e-05, -0.000721305, -0.00132251, -0.000212649, -1.42671e-05, -0.000726105, -0.00132251, -0.000212649, -1.42671e-05, -0.000726105, 0.732527, 0.830071, 0.00366364, 0.0133587, 0.732527, 0.830071, 0.00366364, 0.0133587)

reports.append(Report(577110016, ("DT", 1, 1, 9), "MBwhDst1sec09"))
reports[-1].posNum = 178858
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000223681, 0.00175581, 0), \
                           ValErr(-2.23636e-05, 0.00195516, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.95136e-06, 2.18838e-05, 0), \
                           -417833, 178858, 178858, -nan)
reports[-1].sigmax = ValErr(0.732367, 0.00122451, 0)
reports[-1].sigmay = ValErr(0.826719, 0.00138226, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00074705, -0.00288503, 1.43307e-05, 2.58019e-05, 0.00019811, -2.5601e-05, 1.48313e-05, -0.000623915, 0.00019811, -2.5601e-05, 1.48313e-05, -0.000623915, -0.00205146, 0.00153145, 2.49336e-05, -0.000613451, -0.00205146, 0.00153145, 2.49336e-05, -0.000613451, 0.732367, 0.826718, 0.0036648, 0.0133225, 0.732367, 0.826718, 0.0036648, 0.0133225)

reports.append(Report(577372160, ("DT", 1, 1, 10), "MBwhDst1sec10"))
reports[-1].posNum = 179432
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000190914, 0.00175512, 0), \
                           ValErr(5.19699e-05, 0.00195558, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.84277e-06, 2.18455e-05, 0), \
                           -419562, 179432, 179432, -nan)
reports[-1].sigmax = ValErr(0.732637, 0.00122299, 0)
reports[-1].sigmay = ValErr(0.828204, 0.00138252, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.000648777, 0.00072896, 1.40639e-05, -3.23056e-05, 0.000163657, 4.8639e-05, 9.41695e-06, -0.000674441, 0.000163657, 4.8639e-05, 9.41695e-06, -0.000674441, 0.000535937, -0.000424498, 7.44106e-06, -0.000678969, 0.000535937, -0.000424498, 7.44106e-06, -0.000678969, 0.732637, 0.828206, 0.00365664, 0.0133109, 0.732637, 0.828206, 0.00365664, 0.0133109)

reports.append(Report(577634304, ("DT", 1, 1, 11), "MBwhDst1sec11"))
reports[-1].posNum = 178454
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(4.73133e-05, 0.00176481, 0), \
                           ValErr(6.06606e-05, 0.00195615, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.4975e-06, 2.19379e-05, 0), \
                           -417269, 178454, 178454, -nan)
reports[-1].sigmax = ValErr(0.734444, 0.00122937, 0)
reports[-1].sigmay = ValErr(0.826142, 0.00138286, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.000825865, 0.000840273, 8.82463e-06, -3.04962e-05, 8.63733e-05, 6.59047e-05, 1.51184e-05, -0.00065726, 8.63733e-05, 6.59047e-05, 1.51184e-05, -0.00065726, -0.00102877, -0.000290802, 1.80093e-05, -0.000667415, -0.00102877, -0.000290802, 1.80093e-05, -0.000667415, 0.734444, 0.826141, 0.00366989, 0.0133454, 0.734444, 0.826141, 0.00366989, 0.0133454)

reports.append(Report(577896448, ("DT", 1, 1, 12), "MBwhDst1sec12"))
reports[-1].posNum = 177714
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(4.98158e-05, 0.00176365, 0), \
                           ValErr(0.000158686, 0.00196614, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.63006e-06, 2.19801e-05, 0), \
                           -415703, 177714, 177714, -nan)
reports[-1].sigmax = ValErr(0.73288, 0.0012293, 0)
reports[-1].sigmay = ValErr(0.828668, 0.00138997, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0011959, -0.00280688, -2.08924e-05, 5.85175e-05, 0.000117276, 0.00016772, -2.28154e-05, -0.00062919, 0.000117276, 0.00016772, -2.28154e-05, -0.00062919, 0.000326675, 0.000658194, -2.36294e-05, -0.000618076, 0.000326675, 0.000658194, -2.36294e-05, -0.000618076, 0.732881, 0.828667, 0.00365523, 0.0133509, 0.732881, 0.828667, 0.00365523, 0.0133509)

reports.append(Report(579207168, ("DT", 1, 2, 1), "MBwhDst2sec01"))
reports[-1].posNum = 152206
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000186229, 0.00144279, 0), \
                           ValErr(-0.000101793, 0.00273696, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.06752e-06, 2.63985e-05, 0), \
                           -440720, 152206, 152206, -nan)
reports[-1].sigmax = ValErr(0.989266, 0.00179154, 0)
reports[-1].sigmay = ValErr(1.07086, 0.0019394, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00156212, -0.00158362, -1.64088e-06, 9.00141e-05, -0.000154516, -0.000106847, 5.00959e-06, -0.0002756, -0.000154516, -0.000106847, 5.00959e-06, -0.0002756, 0.000100451, 0.00178265, 3.54735e-06, -0.000278701, 0.000100451, 0.00178265, 3.54735e-06, -0.000278701, 0.989269, 1.07086, 0.0039401, 0.0123341, 0.989269, 1.07086, 0.0039401, 0.0123341)

reports.append(Report(579469312, ("DT", 1, 2, 2), "MBwhDst2sec02"))
reports[-1].posNum = 153088
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000175124, 0.00254805, 0), \
                           ValErr(5.35491e-05, 0.00275248, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.85617e-06, 2.84334e-05, 0), \
                           -444025, 153088, 153088, -nan)
reports[-1].sigmax = ValErr(0.98856, 0.00178656, 0)
reports[-1].sigmay = ValErr(1.0769, 0.00194621, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00062179, -0.00176739, 7.0508e-06, 7.26307e-05, -0.000206833, 5.60839e-05, 1.24299e-05, -0.000315734, -0.000206833, 5.60839e-05, 1.24299e-05, -0.000315734, 0.000634484, -0.000541284, 1.03945e-05, -0.000309269, 0.000634484, -0.000541284, 1.03945e-05, -0.000309269, 0.98856, 1.0769, 0.00392178, 0.0124189, 0.98856, 1.0769, 0.00392178, 0.0124189)

reports.append(Report(579731456, ("DT", 1, 2, 3), "MBwhDst2sec03"))
reports[-1].posNum = 153006
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000206328, 0.00150681, 0), \
                           ValErr(7.92515e-05, 0.00273169, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.12835e-06, 2.59791e-05, 0), \
                           -443324, 153006, 153006, -nan)
reports[-1].sigmax = ValErr(0.988666, 0.00172417, 0)
reports[-1].sigmay = ValErr(1.07353, 0.00190974, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000640451, 0.00037415, -3.85509e-05, 3.52242e-05, 0.000251909, 7.91722e-05, -4.55128e-05, -0.00032981, 0.000251909, 7.91722e-05, -4.55128e-05, -0.00032981, 0.00371685, 0.000455661, -5.56456e-05, -0.000317697, 0.00371685, 0.000455661, -5.56456e-05, -0.000317697, 0.988668, 1.07353, 0.00392616, 0.0124658, 0.988668, 1.07353, 0.00392616, 0.0124658)

reports.append(Report(579993600, ("DT", 1, 2, 4), "MBwhDst2sec04"))
reports[-1].posNum = 122668
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000125463, 0.00282577, 0), \
                           ValErr(8.80912e-05, 0.00308843, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.76896e-06, 3.46968e-05, 0), \
                           -355652, 122668, 122668, -nan)
reports[-1].sigmax = ValErr(0.983096, 0.0019848, 0)
reports[-1].sigmay = ValErr(1.08164, 0.00218375, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.000901984, -0.00445146, 1.25512e-05, 8.33353e-05, -0.000104467, 8.54353e-05, 3.99689e-06, -0.000374366, -0.000104467, 8.54353e-05, 3.99689e-06, -0.000374366, -0.000764016, 0.00279061, 6.60995e-07, -0.000380811, -0.000764016, 0.00279061, 6.60995e-07, -0.000380811, 0.983095, 1.08164, 0.00384643, 0.0125497, 0.983095, 1.08164, 0.00384643, 0.0125497)

reports.append(Report(580255744, ("DT", 1, 2, 5), "MBwhDst2sec05"))
reports[-1].posNum = 152850
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(5.64923e-05, 0.00256861, 0), \
                           ValErr(0.000171615, 0.00275367, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.03887e-06, 2.86308e-05, 0), \
                           -444325, 152850, 152850, -nan)
reports[-1].sigmax = ValErr(0.995306, 0.00180015, 0)
reports[-1].sigmay = ValErr(1.07655, 0.0019471, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00435733, -0.00237523, -1.08655e-05, 4.46037e-05, 8.20368e-05, 0.000170347, -2.61341e-05, -0.000342126, 8.20368e-05, 0.000170347, -2.61341e-05, -0.000342126, 0.00117432, 0.00421267, -3.1563e-05, -0.000379917, 0.00117432, 0.00421267, -3.1563e-05, -0.000379917, 0.995305, 1.07655, 0.00395312, 0.0124218, 0.995305, 1.07655, 0.00395312, 0.0124218)

reports.append(Report(580517888, ("DT", 1, 2, 6), "MBwhDst2sec06"))
reports[-1].posNum = 152664
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-5.15159e-05, 0.00255535, 0), \
                           ValErr(-0.000233942, 0.00275576, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.26235e-06, 2.85581e-05, 0), \
                           -442916, 152664, 152664, -nan)
reports[-1].sigmax = ValErr(0.989528, 0.0017908, 0)
reports[-1].sigmay = ValErr(1.0767, 0.00194855, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00303269, -0.00129338, -1.26995e-05, 5.51731e-05, -2.59549e-05, -0.000235882, -1.13646e-05, -0.00033549, -2.59549e-05, -0.000235882, -1.13646e-05, -0.00033549, 0.00100563, 0.00173723, -9.75355e-06, -0.000318272, 0.00100563, 0.00173723, -9.75355e-06, -0.000318272, 0.989528, 1.07669, 0.00393801, 0.0123671, 0.989528, 1.07669, 0.00393801, 0.0123671)

reports.append(Report(580780032, ("DT", 1, 2, 7), "MBwhDst2sec07"))
reports[-1].posNum = 152998
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000337853, 0.00256356, 0), \
                           ValErr(-0.000117147, 0.00274794, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.91237e-06, 2.85247e-05, 0), \
                           -444308, 152998, 152998, -nan)
reports[-1].sigmax = ValErr(0.993982, 0.00179689, 0)
reports[-1].sigmay = ValErr(1.07484, 0.00194306, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000363389, -0.00185711, -4.40844e-05, -9.68147e-06, -0.000269309, -0.000120113, -4.69613e-05, -0.000384185, -0.000269309, -0.000120113, -4.69613e-05, -0.000384185, -0.00124702, -0.000632322, -4.62749e-05, -0.000356114, -0.00124702, -0.000632322, -4.62749e-05, -0.000356114, 0.993982, 1.07484, 0.00394659, 0.0123411, 0.993982, 1.07484, 0.00394659, 0.0123411)

reports.append(Report(581042176, ("DT", 1, 2, 8), "MBwhDst2sec08"))
reports[-1].posNum = 152866
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000150814, 0.00255562, 0), \
                           ValErr(0.000179811, 0.00274334, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.05611e-06, 2.84675e-05, 0), \
                           -443036, 152866, 152866, -nan)
reports[-1].sigmax = ValErr(0.990311, 0.00179103, 0)
reports[-1].sigmay = ValErr(1.07257, 0.00193979, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00318527, 0.000365449, 4.59108e-06, 8.16962e-06, -0.000170073, 0.000179896, 8.23638e-06, -0.000420161, -0.000170073, 0.000179896, 8.23638e-06, -0.000420161, 0.000362497, -0.000456677, 1.11787e-05, -0.000426703, 0.000362497, -0.000456677, 1.11787e-05, -0.000426703, 0.990307, 1.07257, 0.00394934, 0.0123765, 0.990307, 1.07257, 0.00394934, 0.0123765)

reports.append(Report(581304320, ("DT", 1, 2, 9), "MBwhDst2sec09"))
reports[-1].posNum = 153122
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000250987, 0.00216441, 0), \
                           ValErr(5.45072e-05, 0.00264296, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(9.10501e-07, 1.95449e-05, 0), \
                           -443706, 153122, 153122, -nan)
reports[-1].sigmax = ValErr(0.991633, 0.0017068, 0)
reports[-1].sigmay = ValErr(1.07063, 0.0019315, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000197396, -0.00246212, 3.12322e-05, 4.46821e-05, -0.000234547, 5.75501e-05, 3.49103e-05, -0.000348521, -0.000234547, 5.75501e-05, 3.49103e-05, -0.000348521, -0.000624355, 0.00156449, 3.28558e-05, -0.000346209, -0.000624355, 0.00156449, 3.28558e-05, -0.000346209, 0.991636, 1.07063, 0.00394461, 0.0123933, 0.991636, 1.07063, 0.00394461, 0.0123933)

reports.append(Report(581566464, ("DT", 1, 2, 10), "MBwhDst2sec10"))
reports[-1].posNum = 153294
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.00018896, 0.00255297, 0), \
                           ValErr(0.00023724, 0.00272755, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.45445e-06, 2.83879e-05, 0), \
                           -443708, 153294, 153294, -nan)
reports[-1].sigmax = ValErr(0.990998, 0.00178977, 0)
reports[-1].sigmay = ValErr(1.06786, 0.00192858, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00147722, 2.75208e-05, -1.85912e-05, -2.43748e-06, 0.00025349, 0.000232059, -1.86057e-05, -0.000391243, 0.00025349, 0.000232059, -1.86057e-05, -0.000391243, -0.00156568, -0.00292578, -1.3579e-05, -0.000374074, -0.00156568, -0.00292578, -1.3579e-05, -0.000374074, 0.990997, 1.06786, 0.00395618, 0.0124276, 0.990997, 1.06786, 0.00395618, 0.0124276)

reports.append(Report(581828608, ("DT", 1, 2, 11), "MBwhDst2sec11"))
reports[-1].posNum = 153552
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000137886, 0.00246722, 0), \
                           ValErr(-3.9054e-05, 0.00268381, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.45646e-06, 2.74617e-05, 0), \
                           -444832, 153552, 153552, -nan)
reports[-1].sigmax = ValErr(0.993558, 0.00167657, 0)
reports[-1].sigmay = ValErr(1.06774, 0.00192528, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.000504511, -0.000425995, 2.68853e-05, 1.40016e-05, -0.000198013, -3.36368e-05, 3.78536e-05, -0.000343317, -0.000198013, -3.36368e-05, 3.78536e-05, -0.000343317, -0.00110465, -0.000221078, 3.9643e-05, -0.000348161, -0.00110465, -0.000221078, 3.9643e-05, -0.000348161, 0.993554, 1.06774, 0.00394632, 0.0123755, 0.993554, 1.06774, 0.00394632, 0.0123755)

reports.append(Report(582090752, ("DT", 1, 2, 12), "MBwhDst2sec12"))
reports[-1].posNum = 152506
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000126654, 0.0025468, 0), \
                           ValErr(-0.00026923, 0.00274597, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.27461e-06, 2.84941e-05, 0), \
                           -441275, 152506, 152506, -nan)
reports[-1].sigmax = ValErr(0.985878, 0.00178511, 0)
reports[-1].sigmay = ValErr(1.07234, 0.00194166, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0029106, -0.00114917, -7.40937e-05, 3.47876e-05, 0.00018849, -0.000272395, -6.55339e-05, -0.000332193, 0.00018849, -0.000272395, -6.55339e-05, -0.000332193, 0.000409871, -0.000833527, -6.43292e-05, -0.000333689, 0.000409871, -0.000833527, -6.43292e-05, -0.000333689, 0.985879, 1.07233, 0.00392957, 0.0124014, 0.985879, 1.07233, 0.00392957, 0.0124014)

reports.append(Report(583401472, ("DT", 1, 3, 1), "MBwhDst3sec01"))
reports[-1].posNum = 134138
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000312304, 0.00368948, 0), \
                           ValErr(-8.03406e-05, 0.00386495, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.40263e-06, 3.62456e-05, 0), \
                           -467084, 134138, 134138, -nan)
reports[-1].sigmax = ValErr(1.34571, 0.00259812, 0)
reports[-1].sigmay = ValErr(1.41527, 0.00273243, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00356321, 0.00113999, 6.44669e-05, -7.25125e-05, 0.000307219, -8.32607e-05, 5.01461e-05, -0.000257856, 0.000307219, -8.32607e-05, 5.01461e-05, -0.000257856, 0.00394509, 0.00114836, 4.82853e-05, -0.000270786, 0.00394509, 0.00114836, 4.82853e-05, -0.000270786, 1.34571, 1.41527, 0.00456533, 0.0109138, 1.34571, 1.41527, 0.00456533, 0.0109138)

reports.append(Report(583663616, ("DT", 1, 3, 2), "MBwhDst3sec02"))
reports[-1].posNum = 133388
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-9.5639e-05, 0.00140431, 0), \
                           ValErr(0.000243887, 0.00390968, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.90166e-06, 3.58563e-05, 0), \
                           -464154, 133388, 133388, -nan)
reports[-1].sigmax = ValErr(1.3404, 0.00253318, 0)
reports[-1].sigmay = ValErr(1.41749, 0.002718, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00126717, 0.000452095, 3.12022e-05, -4.63912e-05, -0.00013892, 0.000231083, 3.53841e-05, -0.000215596, -0.00013892, 0.000231083, 3.53841e-05, -0.000215596, -0.00131881, 0.00640315, 4.2157e-05, -0.0002563, -0.00131881, 0.00640315, 4.2157e-05, -0.0002563, 1.34039, 1.41749, 0.0045501, 0.0109002, 1.34039, 1.41749, 0.0045501, 0.0109002)

reports.append(Report(583925760, ("DT", 1, 3, 3), "MBwhDst3sec03"))
reports[-1].posNum = 134374
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.00015652, 0.0014763, 0), \
                           ValErr(0.000169074, 0.0038803, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.12621e-06, 3.55584e-05, 0), \
                           -467452, 134374, 134374, -nan)
reports[-1].sigmax = ValErr(1.34139, 0.00257872, 0)
reports[-1].sigmay = ValErr(1.41504, 0.00272192, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00683567, -0.00380074, -9.11256e-06, -0.000157609, 0.000156463, 0.000173762, -1.57295e-05, -0.000319808, 0.000156463, 0.000173762, -1.57295e-05, -0.000319808, 4.62485e-05, 0.00205609, -1.46049e-05, -0.000353652, 4.62485e-05, 0.00205609, -1.46049e-05, -0.000353652, 1.34139, 1.41504, 0.00453629, 0.0109522, 1.34139, 1.41504, 0.00453629, 0.0109522)

reports.append(Report(584187904, ("DT", 1, 3, 4), "MBwhDst3sec04"))
reports[-1].posNum = 107604
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000127812, 0.00403171, 0), \
                           ValErr(-0.000444146, 0.00433643, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.18702e-06, 4.24612e-05, 0), \
                           -370547, 107604, 107604, -nan)
reports[-1].sigmax = ValErr(1.31892, 0.00283904, 0)
reports[-1].sigmay = ValErr(1.38947, 0.00297668, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00459534, -0.00191317, -2.23335e-05, -0.000116766, -9.81012e-05, -0.000431685, 9.18252e-07, -0.000338872, -9.81012e-05, -0.000431685, 9.18252e-07, -0.000338872, -0.000584794, 0.00425683, -2.07426e-06, -0.000386386, -0.000584794, 0.00425683, -2.07426e-06, -0.000386386, 1.31892, 1.38947, 0.00444178, 0.0111105, 1.31892, 1.38947, 0.00444178, 0.0111105)

reports.append(Report(584450048, ("DT", 1, 3, 5), "MBwhDst3sec05"))
reports[-1].posNum = 133230
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-6.00298e-05, 0.00139928, 0), \
                           ValErr(-0.000190658, 0.00390046, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.31808e-06, 3.58908e-05, 0), \
                           -463762, 133230, 133230, -nan)
reports[-1].sigmax = ValErr(1.34857, 0.00259057, 0)
reports[-1].sigmay = ValErr(1.41057, 0.00272411, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00181875, -0.00116425, 2.33658e-05, -4.45751e-05, -0.000125931, -0.000206485, 2.14742e-05, -0.000251757, -0.000125931, -0.000206485, 2.14742e-05, -0.000251757, -0.000874517, 0.000127544, 2.49173e-05, -0.000267794, -0.000874517, 0.000127544, 2.49173e-05, -0.000267794, 1.34856, 1.41057, 0.00454779, 0.0109721, 1.34856, 1.41057, 0.00454779, 0.0109721)

reports.append(Report(584712192, ("DT", 1, 3, 6), "MBwhDst3sec06"))
reports[-1].posNum = 133664
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000367557, 0.00171259, 0), \
                           ValErr(0.000138611, 0.00388548, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.3401e-06, 3.55016e-05, 0), \
                           -465988, 133664, 133664, -nan)
reports[-1].sigmax = ValErr(1.35045, 0.00253062, 0)
reports[-1].sigmay = ValErr(1.41616, 0.00269205, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00463421, -0.000427719, 1.30666e-05, -5.15267e-05, 0.000321681, 0.00013311, 8.98274e-06, -0.000275919, 0.000321681, 0.00013311, 8.98274e-06, -0.000275919, 0.00185784, -0.00300503, 1.15017e-05, -0.000306729, 0.00185784, -0.00300503, 1.15017e-05, -0.000306729, 1.35045, 1.41616, 0.00458682, 0.0110707, 1.35045, 1.41616, 0.00458682, 0.0110707)

reports.append(Report(584974336, ("DT", 1, 3, 7), "MBwhDst3sec07"))
reports[-1].posNum = 133422
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-8.28711e-05, 0.00369546, 0), \
                           ValErr(-5.78728e-05, 0.00388346, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.93216e-06, 3.63547e-05, 0), \
                           -464793, 133422, 133422, -nan)
reports[-1].sigmax = ValErr(1.34493, 0.0026036, 0)
reports[-1].sigmay = ValErr(1.41823, 0.00274548, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0030993, -0.00212729, -3.46805e-05, -0.000113989, -3.09842e-05, -4.5234e-05, -3.20363e-05, -0.000312667, -3.09842e-05, -4.5234e-05, -3.20363e-05, -0.000312667, -0.00234938, -0.00242957, -1.29448e-05, -0.000297146, -0.00234938, -0.00242957, -1.29448e-05, -0.000297146, 1.34493, 1.41823, 0.00453984, 0.0110383, 1.34493, 1.41823, 0.00453984, 0.0110383)

reports.append(Report(585236480, ("DT", 1, 3, 8), "MBwhDst3sec08"))
reports[-1].posNum = 133996
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000112347, 0.00140057, 0), \
                           ValErr(0.000380426, 0.00387666, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.76604e-07, 3.57409e-05, 0), \
                           -466703, 133996, 133996, -nan)
reports[-1].sigmax = ValErr(1.35018, 0.00257064, 0)
reports[-1].sigmay = ValErr(1.41178, 0.0026915, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000821667, 0.00395103, -3.66772e-07, -0.000173506, -0.000106801, 0.000380088, 6.69854e-06, -0.000323421, -0.000106801, 0.000380088, 6.69854e-06, -0.000323421, -0.00325754, -0.00216649, 1.73525e-05, -0.000326345, -0.00325754, -0.00216649, 1.73525e-05, -0.000326345, 1.35018, 1.41177, 0.00457721, 0.0110196, 1.35018, 1.41177, 0.00457721, 0.0110196)

reports.append(Report(585498624, ("DT", 1, 3, 9), "MBwhDst3sec09"))
reports[-1].posNum = 133414
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000190553, 0.00370101, 0), \
                           ValErr(0.000339697, 0.00389847, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.05296e-05, 3.6107e-05, 0), \
                           -464377, 133414, 133414, -nan)
reports[-1].sigmax = ValErr(1.34684, 0.00253126, 0)
reports[-1].sigmay = ValErr(1.41211, 0.00271817, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0019579, -0.00155256, 7.86855e-05, -7.38675e-05, 9.51694e-05, 0.000317212, 5.98534e-05, -0.000283318, 9.51694e-05, 0.000317212, 5.98534e-05, -0.000283318, -0.00166708, 0.00189878, 7.1597e-05, -0.000262346, -0.00166708, 0.00189878, 7.1597e-05, -0.000262346, 1.34684, 1.41211, 0.00454929, 0.0109875, 1.34684, 1.41211, 0.00454929, 0.0109875)

reports.append(Report(585760768, ("DT", 1, 3, 10), "MBwhDst3sec10"))
reports[-1].posNum = 134178
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000164257, 0.00368889, 0), \
                           ValErr(0.000300968, 0.00386264, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.40634e-06, 3.63099e-05, 0), \
                           -467205, 134178, 134178, -nan)
reports[-1].sigmax = ValErr(1.34611, 0.00259851, 0)
reports[-1].sigmay = ValErr(1.41466, 0.00273086, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.000439376, 0.000443349, -2.07259e-05, -9.83993e-05, 0.000106722, 0.000292725, -2.49539e-05, -0.000262519, 0.000106722, 0.000292725, -2.49539e-05, -0.000262519, -0.000439297, 0.000534936, -1.59572e-05, -0.000272552, -0.000439297, 0.000534936, -1.59572e-05, -0.000272552, 1.3461, 1.41466, 0.00456611, 0.0110174, 1.3461, 1.41466, 0.00456611, 0.0110174)

reports.append(Report(586022912, ("DT", 1, 3, 11), "MBwhDst3sec11"))
reports[-1].posNum = 134118
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000811378, 0.00369122, 0), \
                           ValErr(-0.000360796, 0.00385674, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.21357e-05, 3.62731e-05, 0), \
                           -466817, 134118, 134118, -nan)
reports[-1].sigmax = ValErr(1.34689, 0.00260062, 0)
reports[-1].sigmay = ValErr(1.41195, 0.00272625, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.000328423, 0.00153362, 5.91176e-05, -8.86524e-05, 0.000705687, -0.000394072, 4.78688e-05, -0.000253381, 0.000705687, -0.000394072, 4.78688e-05, -0.000253381, 0.000774208, -0.00148336, 4.24111e-05, -0.000255825, 0.000774208, -0.00148336, 4.24111e-05, -0.000255825, 1.34689, 1.41195, 0.00455141, 0.0109476, 1.34689, 1.41195, 0.00455141, 0.0109476)

reports.append(Report(586285056, ("DT", 1, 3, 12), "MBwhDst3sec12"))
reports[-1].posNum = 133464
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000405366, 0.00366896, 0), \
                           ValErr(0.00010702, 0.00391522, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.37621e-06, 3.62009e-05, 0), \
                           -464253, 133464, 133464, -nan)
reports[-1].sigmax = ValErr(1.33554, 0.00251021, 0)
reports[-1].sigmay = ValErr(1.42088, 0.00273923, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.000930394, 0.000106497, -5.5552e-05, -7.42369e-05, 0.000417567, 0.000110735, -5.18732e-05, -0.000269303, 0.000417567, 0.000110735, -5.18732e-05, -0.000269303, 0.000795206, -0.00086333, -4.92382e-05, -0.000261312, 0.000795206, -0.00086333, -4.92382e-05, -0.000261312, 1.33554, 1.42088, 0.00454008, 0.0109801, 1.33554, 1.42088, 0.00454008, 0.0109801)

reports.append(Report(575045632, ("DT", 2, 1, 1), "MBwhEst1sec01"))
reports[-1].posNum = 102704
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.0004794, 0.00273083, 0), \
                           ValErr(6.59202e-05, 0.00372532, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.41148e-06, 3.81788e-05, 0), \
                           -292106, 102704, 102704, -nan)
reports[-1].sigmax = ValErr(0.825927, 0.0018205, 0)
reports[-1].sigmay = ValErr(1.21838, 0.00268854, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00126385, -0.00439434, -2.11881e-05, -0.00183842, -0.000446393, 7.04726e-05, -9.64931e-06, -0.000867375, -0.000446393, 7.04726e-05, -9.64931e-06, -0.000867375, -0.0012566, 0.0031741, -7.92629e-06, -0.00109045, -0.0012566, 0.0031741, -7.92629e-06, -0.00109045, 0.825927, 1.21838, 0.00409906, 0.0287516, 0.825927, 1.21838, 0.00409906, 0.0287516)

reports.append(Report(575307776, ("DT", 2, 1, 2), "MBwhEst1sec02"))
reports[-1].posNum = 99316
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000203114, 0.00278037, 0), \
                           ValErr(-0.000559563, 0.00386454, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.7294e-06, 3.88719e-05, 0), \
                           -281834, 99316, 99316, -nan)
reports[-1].sigmax = ValErr(0.820987, 0.00184211, 0)
reports[-1].sigmay = ValErr(1.21788, 0.00273266, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.000800013, 0.00399247, -2.57043e-05, -0.00133348, -6.14679e-05, -0.000555953, -3.6324e-05, -0.000760714, -6.14679e-05, -0.000555953, -3.6324e-05, -0.000760714, -1.79511e-05, 0.000768641, -3.56734e-05, -0.00103021, -1.79511e-05, 0.000768641, -3.56734e-05, -0.00103021, 0.820992, 1.21788, 0.00407345, 0.0289523, 0.820992, 1.21788, 0.00407345, 0.0289523)

reports.append(Report(575569920, ("DT", 2, 1, 3), "MBwhEst1sec03"))
reports[-1].posNum = 99396
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000136294, 0.00280497, 0), \
                           ValErr(-0.000446658, 0.0038125, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.70739e-06, 3.90953e-05, 0), \
                           -282279, 99396, 99396, -nan)
reports[-1].sigmax = ValErr(0.824795, 0.00184622, 0)
reports[-1].sigmay = ValErr(1.21493, 0.00271681, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00435305, 0.000729414, -7.17658e-05, -0.00181658, 0.000309851, -0.0004212, -8.64105e-05, -0.00105998, 0.000309851, -0.0004212, -8.64105e-05, -0.00105998, -0.00146578, -0.00155214, -8.09493e-05, -0.00120088, -0.00146578, -0.00155214, -8.09493e-05, -0.00120088, 0.824794, 1.21493, 0.00409946, 0.0287884, 0.824794, 1.21493, 0.00409946, 0.0287884)

reports.append(Report(575832064, ("DT", 2, 1, 4), "MBwhEst1sec04"))
reports[-1].posNum = 102908
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000147947, 0.00272842, 0), \
                           ValErr(8.78079e-05, 0.00380299, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.04746e-06, 3.83228e-05, 0), \
                           -292938, 102908, 102908, -nan)
reports[-1].sigmax = ValErr(0.827422, 0.00182384, 0)
reports[-1].sigmay = ValErr(1.21916, 0.00268731, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.000698091, 0.000450243, -2.95219e-05, -0.00164787, -0.000126673, 9.17822e-05, -2.37348e-05, -0.000788139, -0.000126673, 9.17822e-05, -2.37348e-05, -0.000788139, 0.000332825, 0.00253339, -2.56883e-05, -0.00104342, 0.000332825, 0.00253339, -2.56883e-05, -0.00104342, 0.827423, 1.21916, 0.00410432, 0.0287482, 0.827423, 1.21916, 0.00410432, 0.0287482)

reports.append(Report(576094208, ("DT", 2, 1, 5), "MBwhEst1sec05"))
reports[-1].posNum = 100028
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000131165, 0.00278363, 0), \
                           ValErr(-0.000771393, 0.00384302, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.85484e-06, 3.88755e-05, 0), \
                           -284469, 100028, 100028, -nan)
reports[-1].sigmax = ValErr(0.827729, 0.00185061, 0)
reports[-1].sigmay = ValErr(1.21543, 0.0027174, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000696661, -0.00225208, 6.46797e-05, -0.0013463, -5.69275e-06, -0.000775549, 6.18973e-05, -0.000723465, -5.69275e-06, -0.000775549, 6.18973e-05, -0.000723465, -0.00133586, 0.00216435, 6.58093e-05, -0.000896972, -0.00133586, 0.00216435, 6.58093e-05, -0.000896972, 0.827727, 1.21542, 0.0041131, 0.0288874, 0.827727, 1.21542, 0.0041131, 0.0288874)

reports.append(Report(576356352, ("DT", 2, 1, 6), "MBwhEst1sec06"))
reports[-1].posNum = 97412
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000155106, 0.00283351, 0), \
                           ValErr(0.000201528, 0.00387957, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.00905e-05, 3.94331e-05, 0), \
                           -275814, 97412, 97412, -nan)
reports[-1].sigmax = ValErr(0.820974, 0.00185998, 0)
reports[-1].sigmay = ValErr(1.21022, 0.00274186, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.000691071, 0.00450295, 0.000130138, -0.00145514, -0.000423564, 0.000169589, 0.000124047, -0.000738277, -0.000423564, 0.000169589, 0.000124047, -0.000738277, -0.000241983, -0.00155603, 0.000120205, -0.000901043, -0.000241983, -0.00155603, 0.000120205, -0.000901043, 0.820974, 1.21022, 0.00408235, 0.0287937, 0.820974, 1.21022, 0.00408235, 0.0287937)

reports.append(Report(576618496, ("DT", 2, 1, 7), "MBwhEst1sec07"))
reports[-1].posNum = 103184
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(9.00497e-05, 0.00271344, 0), \
                           ValErr(-0.00019214, 0.00380256, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.49072e-06, 3.82152e-05, 0), \
                           -293434, 103184, 103184, -nan)
reports[-1].sigmax = ValErr(0.824034, 0.00181397, 0)
reports[-1].sigmay = ValErr(1.22075, 0.00268727, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00246813, -0.00274257, 3.16971e-05, -0.00156352, 0.000147649, -0.000183886, 3.5446e-05, -0.000727371, 0.000147649, -0.000183886, 3.5446e-05, -0.000727371, 0.00237109, -0.00103628, 2.67777e-05, -0.000966621, 0.00237109, -0.00103628, 2.67777e-05, -0.000966621, 0.824034, 1.22074, 0.00409291, 0.02886, 0.824034, 1.22074, 0.00409291, 0.02886)

reports.append(Report(576880640, ("DT", 2, 1, 8), "MBwhEst1sec08"))
reports[-1].posNum = 99440
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-5.84936e-05, 0.00278571, 0), \
                           ValErr(-0.000137781, 0.00375127, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.26661e-06, 3.90982e-05, 0), \
                           -283118, 99440, 99440, -nan)
reports[-1].sigmax = ValErr(0.825054, 0.00184654, 0)
reports[-1].sigmay = ValErr(1.22331, 0.00273314, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00216102, 0.00232989, 8.25681e-05, -0.0012959, -0.000260717, -0.000142727, 8.48293e-05, -0.000701314, -0.000260717, -0.000142727, 8.48293e-05, -0.000701314, 0.00112701, -0.00280346, 7.9499e-05, -0.000864824, 0.00112701, -0.00280346, 7.9499e-05, -0.000864824, 0.825053, 1.22331, 0.00409694, 0.0288805, 0.825053, 1.22331, 0.00409694, 0.0288805)

reports.append(Report(577142784, ("DT", 2, 1, 9), "MBwhEst1sec09"))
reports[-1].posNum = 98180
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000156646, 0.0028298, 0), \
                           ValErr(0.000493666, 0.00385071, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.78932e-06, 3.9273e-05, 0), \
                           -278138, 98180, 98180, -nan)
reports[-1].sigmax = ValErr(0.825161, 0.00186215, 0)
reports[-1].sigmay = ValErr(1.20591, 0.00272138, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0030158, 0.00338868, 0.000117145, -0.00165678, 0.000258429, 0.000504779, 9.132e-05, -0.00088223, 0.000258429, 0.000504779, 9.132e-05, -0.00088223, -0.00188051, 0.00534774, 0.000103265, -0.00105118, -0.00188051, 0.00534774, 0.000103265, -0.00105118, 0.825159, 1.20592, 0.00409551, 0.0286941, 0.825159, 1.20592, 0.00409551, 0.0286941)

reports.append(Report(577404928, ("DT", 2, 1, 10), "MBwhEst1sec10"))
reports[-1].posNum = 101966
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000170436, 0.00272593, 0), \
                           ValErr(-0.000417498, 0.0038352, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(9.95555e-07, 3.82578e-05, 0), \
                           -290060, 101966, 101966, -nan)
reports[-1].sigmax = ValErr(0.822641, 0.00182166, 0)
reports[-1].sigmay = ValErr(1.22389, 0.0027102, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000372654, 0.0071125, -3.19372e-05, -0.00186351, -0.000150274, -0.000413972, -1.76762e-05, -0.00101479, -0.000150274, -0.000413972, -1.76762e-05, -0.00101479, -0.00153567, 0.00384263, -8.03592e-06, -0.00127941, -0.00153567, 0.00384263, -8.03592e-06, -0.00127941, 0.822641, 1.22389, 0.00408788, 0.0288917, 0.822641, 1.22389, 0.00408788, 0.0288917)

reports.append(Report(577667072, ("DT", 2, 1, 11), "MBwhEst1sec11"))
reports[-1].posNum = 100364
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000300706, 0.00278519, 0), \
                           ValErr(0.000176349, 0.00385067, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.29177e-06, 3.89703e-05, 0), \
                           -285732, 100364, 100364, -nan)
reports[-1].sigmax = ValErr(0.827275, 0.00184649, 0)
reports[-1].sigmay = ValErr(1.21981, 0.00272264, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00078053, 0.00113955, 2.01841e-05, -0.00131981, -0.00024385, 0.000178973, 3.06084e-05, -0.000538541, -0.00024385, 0.000178973, 3.06084e-05, -0.000538541, -0.00048368, 0.000263161, 2.79949e-05, -0.000754846, -0.00048368, 0.000263161, 2.79949e-05, -0.000754846, 0.827275, 1.21981, 0.00410179, 0.0288774, 0.827275, 1.21981, 0.00410179, 0.0288774)

reports.append(Report(577929216, ("DT", 2, 1, 12), "MBwhEst1sec12"))
reports[-1].posNum = 98820
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000125361, 0.00281627, 0), \
                           ValErr(0.000393478, 0.0038613, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.07022e-06, 3.93004e-05, 0), \
                           -280165, 98820, 98820, -nan)
reports[-1].sigmax = ValErr(0.822029, 0.00184906, 0)
reports[-1].sigmay = ValErr(1.21313, 0.0027288, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.000671859, 0.00214309, -6.49022e-05, -0.00145108, -4.43529e-05, 0.000403761, -5.89596e-05, -0.000720938, -4.43529e-05, 0.000403761, -5.89596e-05, -0.000720938, -7.74646e-05, -0.000298359, -6.52592e-05, -0.000961668, -7.74646e-05, -0.000298359, -6.52592e-05, -0.000961668, 0.822028, 1.21313, 0.00408298, 0.0287519, 0.822028, 1.21313, 0.00408298, 0.0287519)

reports.append(Report(579239936, ("DT", 2, 2, 1), "MBwhEst2sec01"))
reports[-1].posNum = 111694
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000186305, 0.00330548, 0), \
                           ValErr(0.000271283, 0.00449937, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.83276e-06, 4.2602e-05, 0), \
                           -370807, 111694, 111694, -nan)
reports[-1].sigmax = ValErr(1.08747, 0.00230286, 0)
reports[-1].sigmay = ValErr(1.48902, 0.00316778, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00199744, -0.0046976, 2.1884e-05, -0.000708292, 0.000147711, 0.000273134, 2.37589e-05, -0.00113542, 0.000147711, 0.000273134, 2.37589e-05, -0.00113542, 0.000997212, 0.00231956, 2.17227e-05, -0.00125309, 0.000997212, 0.00231956, 2.17227e-05, -0.00125309, 1.08747, 1.48902, 0.00431627, 0.0232002, 1.08747, 1.48902, 0.00431627, 0.0232002)

reports.append(Report(579502080, ("DT", 2, 2, 2), "MBwhEst2sec02"))
reports[-1].posNum = 110596
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000200518, 0.00332177, 0), \
                           ValErr(-3.49812e-05, 0.00458245, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.38833e-06, 4.26352e-05, 0), \
                           -366908, 110596, 110596, -nan)
reports[-1].sigmax = ValErr(1.08723, 0.00231332, 0)
reports[-1].sigmay = ValErr(1.48593, 0.00316055, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00355232, -0.00173315, -3.01389e-05, -0.000589113, -0.000233238, -3.33231e-05, -3.97634e-05, -0.00099947, -0.000233238, -3.33231e-05, -3.97634e-05, -0.00099947, -0.00252431, 0.00500516, -2.67618e-05, -0.00108329, -0.00252431, 0.00500516, -2.67618e-05, -0.00108329, 1.08723, 1.48593, 0.00430891, 0.0230671, 1.08723, 1.48593, 0.00430891, 0.0230671)

reports.append(Report(579764224, ("DT", 2, 2, 3), "MBwhEst2sec03"))
reports[-1].posNum = 111336
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000267613, 0.00328316, 0), \
                           ValErr(4.25885e-05, 0.004564, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.45624e-06, 3.99283e-05, 0), \
                           -368537, 111336, 111336, -nan)
reports[-1].sigmax = ValErr(1.07979, 0.00228702, 0)
reports[-1].sigmay = ValErr(1.48511, 0.0030667, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00129416, -0.00613728, 4.22708e-06, -0.000943395, 0.000286126, 4.37462e-05, 1.35375e-05, -0.00140814, 0.000286126, 4.37462e-05, 1.35375e-05, -0.00140814, 0.000561553, 0.000693646, 8.63198e-06, -0.00140895, 0.000561553, 0.000693646, 8.63198e-06, -0.00140895, 1.07979, 1.4851, 0.004293, 0.023186, 1.07979, 1.4851, 0.004293, 0.023186)

reports.append(Report(580026368, ("DT", 2, 2, 4), "MBwhEst2sec04"))
reports[-1].posNum = 111224
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000333984, 0.00173414, 0), \
                           ValErr(0.00023193, 0.00457108, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.07557e-06, 3.85906e-05, 0), \
                           -369291, 111224, 111224, -nan)
reports[-1].sigmax = ValErr(1.08918, 0.00230876, 0)
reports[-1].sigmay = ValErr(1.48727, 0.00316163, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000218435, 0.00668872, 5.44988e-07, -0.000589213, -0.000378627, 0.000230687, -3.29376e-06, -0.00107909, -0.000378627, 0.000230687, -3.29376e-06, -0.00107909, 0.00243707, -0.00011158, -1.80519e-05, -0.00108716, 0.00243707, -0.00011158, -1.80519e-05, -0.00108716, 1.08918, 1.48728, 0.00432105, 0.0231832, 1.08918, 1.48728, 0.00432105, 0.0231832)

reports.append(Report(580288512, ("DT", 2, 2, 5), "MBwhEst2sec05"))
reports[-1].posNum = 111744
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000132181, 0.00330195, 0), \
                           ValErr(-6.45787e-05, 0.00445681, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.59174e-06, 4.25156e-05, 0), \
                           -370880, 111744, 111744, -nan)
reports[-1].sigmax = ValErr(1.08598, 0.00229719, 0)
reports[-1].sigmay = ValErr(1.48982, 0.00315143, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00166513, -0.00235884, -3.3282e-05, -0.000784597, 0.000112059, -6.4597e-05, -3.83398e-05, -0.00120787, 0.000112059, -6.4597e-05, -3.83398e-05, -0.00120787, -0.00082872, -0.00102126, -3.80153e-05, -0.00126731, -0.00082872, -0.00102126, -3.80153e-05, -0.00126731, 1.08598, 1.48982, 0.00431506, 0.0231143, 1.08598, 1.48982, 0.00431506, 0.0231143)

reports.append(Report(580550656, ("DT", 2, 2, 6), "MBwhEst2sec06"))
reports[-1].posNum = 111328
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000468533, 0.00329595, 0), \
                           ValErr(0.000167346, 0.0045476, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.09053e-05, 4.24623e-05, 0), \
                           -368871, 111328, 111328, -nan)
reports[-1].sigmax = ValErr(1.0833, 0.00229705, 0)
reports[-1].sigmay = ValErr(1.4851, 0.00315332, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00161457, 0.00295089, -0.000101698, -0.000769085, -0.000318059, 0.000162207, -9.4508e-05, -0.00112437, -0.000318059, 0.000162207, -9.4508e-05, -0.00112437, -2.87639e-05, -0.00348591, -9.56032e-05, -0.00107813, -2.87639e-05, -0.00348591, -9.56032e-05, -0.00107813, 1.0833, 1.4851, 0.00430418, 0.0230717, 1.0833, 1.4851, 0.00430418, 0.0230717)

reports.append(Report(580812800, ("DT", 2, 2, 7), "MBwhEst2sec07"))
reports[-1].posNum = 111058
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000270829, 0.00331232, 0), \
                           ValErr(-0.000201899, 0.00447469, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.40573e-06, 4.2576e-05, 0), \
                           -368820, 111058, 111058, -nan)
reports[-1].sigmax = ValErr(1.0871, 0.00230665, 0)
reports[-1].sigmay = ValErr(1.49119, 0.00316404, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00646752, -0.00746259, -4.73983e-05, -0.000620777, 0.000291721, -0.000199174, -4.18345e-05, -0.00113803, 0.000291721, -0.000199174, -4.18345e-05, -0.00113803, 0.00165284, -0.00247313, -4.38439e-05, -0.00117672, 0.00165284, -0.00247313, -4.38439e-05, -0.00117672, 1.0871, 1.49119, 0.00431047, 0.0230951, 1.0871, 1.49119, 0.00431047, 0.0230951)

reports.append(Report(581074944, ("DT", 2, 2, 8), "MBwhEst2sec08"))
reports[-1].posNum = 111648
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.00011109, 0.00329642, 0), \
                           ValErr(-6.48385e-05, 0.00446255, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.59709e-06, 4.24521e-05, 0), \
                           -370483, 111648, 111648, -nan)
reports[-1].sigmax = ValErr(1.08429, 0.00229463, 0)
reports[-1].sigmay = ValErr(1.4911, 0.00315554, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00331694, 0.00377236, 7.79044e-05, -0.000877879, 9.02903e-05, -6.56845e-05, 6.62247e-05, -0.00121437, 9.02903e-05, -6.56845e-05, 6.62247e-05, -0.00121437, 0.00145629, 0.00559321, 6.12512e-05, -0.00125612, 0.00145629, 0.00559321, 6.12512e-05, -0.00125612, 1.08429, 1.4911, 0.00431411, 0.0232315, 1.08429, 1.4911, 0.00431411, 0.0232315)

reports.append(Report(581337088, ("DT", 2, 2, 9), "MBwhEst2sec09"))
reports[-1].posNum = 110944
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000131983, 0.00330364, 0), \
                           ValErr(0.000238673, 0.00455685, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.77153e-06, 4.25429e-05, 0), \
                           -368056, 110944, 110944, -nan)
reports[-1].sigmax = ValErr(1.08293, 0.00230003, 0)
reports[-1].sigmay = ValErr(1.49174, 0.00317493, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00338078, -0.000607164, 9.0505e-05, -0.000692584, -0.000156478, 0.00023889, 7.90699e-05, -0.00121143, -0.000156478, 0.00023889, 7.90699e-05, -0.00121143, -0.000813556, 0.00298712, 8.27047e-05, -0.00131025, -0.000813556, 0.00298712, 8.27047e-05, -0.00131025, 1.08293, 1.49174, 0.00430978, 0.023103, 1.08293, 1.49174, 0.00430978, 0.023103)

reports.append(Report(581599232, ("DT", 2, 2, 10), "MBwhEst2sec10"))
reports[-1].posNum = 110772
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(3.44951e-05, 0.00330717, 0), \
                           ValErr(0.000220396, 0.00447054, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.93588e-06, 4.25364e-05, 0), \
                           -367262, 110772, 110772, -nan)
reports[-1].sigmax = ValErr(1.08355, 0.00230206, 0)
reports[-1].sigmay = ValErr(1.48788, 0.00316111, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.000849232, -0.000342194, -0.000112295, -0.000639392, 8.4824e-05, 0.000218783, -0.000105839, -0.00113574, 8.4824e-05, 0.000218783, -0.000105839, -0.00113574, -9.95205e-05, 0.00279006, -0.000104501, -0.00124983, -9.95205e-05, 0.00279006, -0.000104501, -0.00124983, 1.08355, 1.48788, 0.00430555, 0.0232561, 1.08355, 1.48788, 0.00430555, 0.0232561)

reports.append(Report(581861376, ("DT", 2, 2, 11), "MBwhEst2sec11"))
reports[-1].posNum = 111846
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000247205, 0.00149519, 0), \
                           ValErr(-2.70015e-05, 0.00501506, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(8.96989e-06, 2.39732e-05, 0), \
                           -372038, 111846, 111846, -nan)
reports[-1].sigmax = ValErr(1.09251, 0.002305, 0)
reports[-1].sigmay = ValErr(1.4918, 0.00315573, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00307846, 0.00108314, -0.000103743, -0.00066972, -0.000122393, -2.56196e-05, -0.000108623, -0.00114702, -0.000122393, -2.56196e-05, -0.000108623, -0.00114702, -0.000924533, 0.00653297, -0.000116429, -0.00116849, -0.000924533, 0.00653297, -0.000116429, -0.00116849, 1.09251, 1.4918, 0.00433153, 0.0231794, 1.09251, 1.4918, 0.00433153, 0.0231794)

reports.append(Report(582123520, ("DT", 2, 2, 12), "MBwhEst2sec12"))
reports[-1].posNum = 111396
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.00025301, 0.0033028, 0), \
                           ValErr(-4.66662e-06, 0.0045617, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.21193e-07, 4.24911e-05, 0), \
                           -369199, 111396, 111396, -nan)
reports[-1].sigmax = ValErr(1.08627, 0.00230298, 0)
reports[-1].sigmay = ValErr(1.48241, 0.00314171, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00315382, 0.00222894, -6.70269e-05, -0.000638282, -0.000259631, -4.5942e-06, -5.14106e-05, -0.00104143, -0.000259631, -4.5942e-06, -5.14106e-05, -0.00104143, -0.00181036, -0.00111242, -4.77203e-05, -0.00108361, -0.00181036, -0.00111242, -4.77203e-05, -0.00108361, 1.08627, 1.48241, 0.00431791, 0.0232761, 1.08627, 1.48241, 0.00431791, 0.0232761)

reports.append(Report(583434240, ("DT", 2, 3, 1), "MBwhEst3sec01"))
reports[-1].posNum = 103210
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000197514, 0.00450161, 0), \
                           ValErr(0.000386313, 0.00565076, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.58023e-06, 4.99329e-05, 0), \
                           -391908, 103210, 103210, -nan)
reports[-1].sigmax = ValErr(1.43797, 0.003165, 0)
reports[-1].sigmay = ValErr(1.81498, 0.00399481, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.000528967, -0.0044116, 6.18319e-06, -0.000400137, -0.000212695, 0.000388114, 1.26231e-05, -0.000285287, -0.000212695, 0.000388114, 1.26231e-05, -0.000285287, 0.00276723, -0.00196019, 7.14435e-06, -0.000203881, 0.00276723, -0.00196019, 7.14435e-06, -0.000203881, 1.43797, 1.81498, 0.00487229, 0.0179728, 1.43797, 1.81498, 0.00487229, 0.0179728)

reports.append(Report(583696384, ("DT", 2, 3, 2), "MBwhEst3sec02"))
reports[-1].posNum = 103712
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000307221, 0.0044764, 0), \
                           ValErr(0.000484854, 0.00568386, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.60246e-06, 4.99201e-05, 0), \
                           -394324, 103712, 103712, -nan)
reports[-1].sigmax = ValErr(1.43314, 0.00314673, 0)
reports[-1].sigmay = ValErr(1.83008, 0.00401828, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0054143, -0.00183383, -1.01365e-05, -0.000333249, -0.000281203, 0.000490112, -5.80712e-06, -0.0002368, -0.000281203, 0.000490112, -5.80712e-06, -0.0002368, -0.00405621, 0.0030156, 6.1916e-06, -0.000160034, -0.00405621, 0.0030156, 6.1916e-06, -0.000160034, 1.43314, 1.83008, 0.00485477, 0.0179095, 1.43314, 1.83008, 0.00485477, 0.0179095)

reports.append(Report(583958528, ("DT", 2, 3, 3), "MBwhEst3sec03"))
reports[-1].posNum = 103432
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000670766, 0.00448769, 0), \
                           ValErr(0.000168647, 0.0056714, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.84163e-06, 4.99712e-05, 0), \
                           -392984, 103432, 103432, -nan)
reports[-1].sigmax = ValErr(1.43449, 0.00315394, 0)
reports[-1].sigmay = ValErr(1.8235, 0.00400926, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0012501, -0.00216573, -5.24019e-05, -0.000357061, 0.000705171, 0.000179822, -4.6683e-05, -0.000309405, 0.000705171, 0.000179822, -4.6683e-05, -0.000309405, -0.000359418, 0.000958028, -4.16e-05, -0.000203788, -0.000359418, 0.000958028, -4.16e-05, -0.000203788, 1.43449, 1.8235, 0.00482658, 0.0179829, 1.43449, 1.8235, 0.00482658, 0.0179829)

reports.append(Report(584220672, ("DT", 2, 3, 4), "MBwhEst3sec04"))
reports[-1].posNum = 102624
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000184677, 0.00449927, 0), \
                           ValErr(0.000478145, 0.00569462, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.39155e-06, 5.00987e-05, 0), \
                           -389840, 102624, 102624, -nan)
reports[-1].sigmax = ValErr(1.43324, 0.00316364, 0)
reports[-1].sigmay = ValErr(1.82378, 0.00402567, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-9.57011e-05, -0.000146708, -0.00013309, -0.000498957, 0.000230007, 0.000486171, -0.000117159, -0.000432141, 0.000230007, 0.000486171, -0.000117159, -0.000432141, 0.00214103, 0.00875422, -0.00011962, -0.000374453, 0.00214103, 0.00875422, -0.00011962, -0.000374453, 1.43324, 1.82378, 0.00485107, 0.0180478, 1.43324, 1.82378, 0.00485107, 0.0180478)

reports.append(Report(584482816, ("DT", 2, 3, 5), "MBwhEst3sec05"))
reports[-1].posNum = 102302
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000647315, 0.00450851, 0), \
                           ValErr(-0.000160577, 0.00569455, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.92692e-06, 5.01188e-05, 0), \
                           -388477, 102302, 102302, -nan)
reports[-1].sigmax = ValErr(1.43348, 0.0031691, 0)
reports[-1].sigmay = ValErr(1.82097, 0.00402575, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00666457, -0.00176883, -2.33629e-06, -0.000450811, -0.000609777, -0.000152551, -1.08385e-05, -0.00045124, -0.000609777, -0.000152551, -1.08385e-05, -0.00045124, -0.00187348, 0.000993242, -9.57397e-06, -0.000367275, -0.00187348, 0.000993242, -9.57397e-06, -0.000367275, 1.43348, 1.82097, 0.00486029, 0.01795, 1.43348, 1.82097, 0.00486029, 0.01795)

reports.append(Report(584744960, ("DT", 2, 3, 6), "MBwhEst3sec06"))
reports[-1].posNum = 102794
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000139486, 0.00450607, 0), \
                           ValErr(-3.96824e-06, 0.00567227, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.15834e-06, 4.99264e-05, 0), \
                           -390385, 102794, 102794, -nan)
reports[-1].sigmax = ValErr(1.43623, 0.00316757, 0)
reports[-1].sigmay = ValErr(1.8182, 0.00400999, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000323054, 0.00316321, 1.71928e-06, -0.000448714, -0.000159786, -9.05525e-06, -4.94806e-07, -0.000450937, -0.000159786, -9.05525e-06, -4.94806e-07, -0.000450937, 0.00320373, 0.00261491, -8.54827e-06, -0.000330675, 0.00320373, 0.00261491, -8.54827e-06, -0.000330675, 1.43623, 1.8182, 0.00487909, 0.0179495, 1.43623, 1.8182, 0.00487909, 0.0179495)

reports.append(Report(585007104, ("DT", 2, 3, 7), "MBwhEst3sec07"))
reports[-1].posNum = 102300
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(6.6469e-05, 0.00453359, 0), \
                           ValErr(-9.75378e-05, 0.00573471, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.10243e-06, 5.04746e-05, 0), \
                           -389769, 102300, 102300, -nan)
reports[-1].sigmax = ValErr(1.44155, 0.00318695, 0)
reports[-1].sigmay = ValErr(1.83393, 0.00405441, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00148988, -0.00110562, -5.45591e-06, -0.000376306, 5.56566e-05, -9.63017e-05, -1.89251e-06, -0.000351641, 5.56566e-05, -9.63017e-05, -1.89251e-06, -0.000351641, 0.00347882, -8.44422e-05, -4.57581e-06, -0.000303898, 0.00347882, -8.44422e-05, -4.57581e-06, -0.000303898, 1.44155, 1.83393, 0.00486972, 0.0180602, 1.44155, 1.83393, 0.00486972, 0.0180602)

reports.append(Report(585269248, ("DT", 2, 3, 8), "MBwhEst3sec08"))
reports[-1].posNum = 102864
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-1.16114e-05, 0.00448459, 0), \
                           ValErr(-0.000369789, 0.00568829, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.53631e-06, 4.99259e-05, 0), \
                           -390494, 102864, 102864, -nan)
reports[-1].sigmax = ValErr(1.42961, 0.00315188, 0)
reports[-1].sigmay = ValErr(1.82384, 0.00402107, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00160659, -0.00535774, -1.2461e-05, -0.000506486, 1.47048e-05, -0.000362245, -1.30479e-05, -0.000514484, 1.47048e-05, -0.000362245, -1.30479e-05, -0.000514484, -0.00338518, -0.00736013, -1.90531e-06, -0.000448453, -0.00338518, -0.00736013, -1.90531e-06, -0.000448453, 1.42961, 1.82384, 0.00485165, 0.0180472, 1.42961, 1.82384, 0.00485165, 0.0180472)

reports.append(Report(585531392, ("DT", 2, 3, 9), "MBwhEst3sec09"))
reports[-1].posNum = 102852
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(4.68603e-05, 0.00449536, 0), \
                           ValErr(0.00126801, 0.00569075, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.76e-08, 5.02418e-05, 0), \
                           -390770, 102852, 102852, -nan)
reports[-1].sigmax = ValErr(1.43348, 0.00316062, 0)
reports[-1].sigmay = ValErr(1.82459, 0.00402299, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00511705, -0.00409538, 6.29449e-05, -0.000347728, 4.74089e-05, 0.00126746, 5.13043e-05, -0.000369112, 4.74089e-05, 0.00126746, 5.13043e-05, -0.000369112, 0.00119796, 0.00345245, 4.52776e-05, -0.000232054, 0.00119796, 0.00345245, 4.52776e-05, -0.000232054, 1.43348, 1.82459, 0.00486003, 0.01792, 1.43348, 1.82459, 0.00486003, 0.01792)

reports.append(Report(585793536, ("DT", 2, 3, 10), "MBwhEst3sec10"))
reports[-1].posNum = 101850
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000352474, 0.00449772, 0), \
                           ValErr(0.000622065, 0.00570596, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.47768e-06, 5.01006e-05, 0), \
                           -386247, 101850, 101850, -nan)
reports[-1].sigmax = ValErr(1.42669, 0.00316108, 0)
reports[-1].sigmay = ValErr(1.82044, 0.00403348, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00093392, 0.000917107, 7.51453e-05, -0.000418261, 0.000258665, 0.000596083, 7.28701e-05, -0.000457106, 0.000258665, 0.000596083, 7.28701e-05, -0.000457106, 0.000386139, 0.00492083, 6.81243e-05, -0.00030989, 0.000386139, 0.00492083, 6.81243e-05, -0.00030989, 1.42669, 1.82044, 0.00484334, 0.0179894, 1.42669, 1.82044, 0.00484334, 0.0179894)

reports.append(Report(586055680, ("DT", 2, 3, 11), "MBwhEst3sec11"))
reports[-1].posNum = 102792
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000242491, 0.0045138, 0), \
                           ValErr(-6.74727e-05, 0.00572681, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.11651e-06, 5.02103e-05, 0), \
                           -391600, 102792, 102792, -nan)
reports[-1].sigmax = ValErr(1.4396, 0.00317503, 0)
reports[-1].sigmay = ValErr(1.83564, 0.00404847, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00122193, -0.00664397, 5.21713e-05, -0.0004131, -0.000225564, -5.792e-05, 4.1766e-05, -0.000403714, -0.000225564, -5.792e-05, 4.1766e-05, -0.000403714, 0.00219566, 0.00166465, 3.67009e-05, -0.000264369, 0.00219566, 0.00166465, 3.67009e-05, -0.000264369, 1.4396, 1.83564, 0.00484765, 0.0180532, 1.4396, 1.83564, 0.00484765, 0.0180532)

reports.append(Report(586317824, ("DT", 2, 3, 12), "MBwhEst3sec12"))
reports[-1].posNum = 102960
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000270731, 0.00448867, 0), \
                           ValErr(-0.00048215, 0.00567998, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(7.11629e-06, 4.99929e-05, 0), \
                           -390946, 102960, 102960, -nan)
reports[-1].sigmax = ValErr(1.43215, 0.00315604, 0)
reports[-1].sigmay = ValErr(1.82214, 0.00401544, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00263077, -0.00157517, -1.81785e-05, -0.000469454, 0.000339171, -0.000467376, -2.47928e-05, -0.000377964, 0.000339171, -0.000467376, -2.47928e-05, -0.000377964, -0.00142358, -0.00414548, -2.11774e-05, -0.000212522, -0.00142358, -0.00414548, -2.11774e-05, -0.000212522, 1.43214, 1.82214, 0.00483885, 0.0180057, 1.43214, 1.82214, 0.00483885, 0.0180057)

reports.append(Report(587497472, ("DT", -2, 4, 1), "MBwhAst4sec01"))
reports[-1].posNum = 145002
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.000565444, 0.00525761, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.28271e-06, 8.49042e-05, 0), \
                           -305367, 145002, 145002, -nan)
reports[-1].sigmaresid = ValErr(1.98776, 0.00369115, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00543172, None, -2.02495e-06, None, -0.000524735, None, -6.11461e-06, None, -0.000524735, None, -6.11461e-06, None, -0.00719649, None, 8.71925e-06, None, -0.00719649, None, 8.71925e-06, None, 1.98776, None, 0.00570874, None, 1.98776, None, 0.00570874, None)

reports.append(Report(587759616, ("DT", -2, 4, 2), "MBwhAst4sec02"))
reports[-1].posNum = 146016
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.000743109, 0.00525877, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.90994e-06, 8.49377e-05, 0), \
                           -308089, 146016, 146016, -nan)
reports[-1].sigmaresid = ValErr(1.99576, 0.00369312, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00246832, None, -7.61478e-05, None, 0.000754341, None, -5.91131e-05, None, 0.000754341, None, -5.91131e-05, None, 0.00050667, None, -5.85233e-05, None, 0.00050667, None, -5.85233e-05, None, 1.99576, None, 0.00573274, None, 1.99576, None, 0.00573274, None)

reports.append(Report(588021760, ("DT", -2, 4, 3), "MBwhAst4sec03"))
reports[-1].posNum = 145136
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-4.12549e-05, 0.0052482, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.38458e-06, 8.48879e-05, 0), \
                           -305462, 145136, 145136, -nan)
reports[-1].sigmaresid = ValErr(1.9852, 0.00368469, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000596828, None, -8.34069e-05, None, -6.75601e-05, None, -8.2462e-05, None, -6.75601e-05, None, -8.2462e-05, None, -0.00261033, None, -6.11051e-05, None, -0.00261033, None, -6.11051e-05, None, 1.9852, None, 0.00568856, None, 1.9852, None, 0.00568856, None)

reports.append(Report(588283904, ("DT", -2, 4, 4), "MBwhAst4sec04"))
reports[-1].posNum = 106912
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.00160626, 0.00622703, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.2709e-05, 0.000100061, 0), \
                           -226962, 106912, 106912, -nan)
reports[-1].sigmaresid = ValErr(2.02172, 0.00437214, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00137565, None, -0.000173202, None, 0.00177081, None, -0.000163824, None, 0.00177081, None, -0.000163824, None, -0.00273443, None, -0.000145366, None, -0.00273443, None, -0.000145366, None, 2.02172, None, 0.00579688, None, 2.02172, None, 0.00579688, None)

reports.append(Report(590643200, ("DT", -2, 4, 13), "MBwhAst4sec13"))
reports[-1].posNum = 107022
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-4.41953e-06, 0.006236, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.2622e-05, 0.000100607, 0), \
                           -227522, 107022, 107022, -nan)
reports[-1].sigmaresid = ValErr(2.02789, 0.00438321, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00399708, None, 0.000120516, None, -9.69385e-05, None, 0.000144145, None, -9.69385e-05, None, 0.000144145, None, 0.0147141, None, 9.97597e-05, None, 0.0147141, None, 9.97597e-05, None, 2.02789, None, 0.00581155, None, 2.02789, None, 0.00581155, None)

reports.append(Report(588546048, ("DT", -2, 4, 5), "MBwhAst4sec05"))
reports[-1].posNum = 144124
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.000318972, 0.00528301, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.1436e-06, 8.53493e-05, 0), \
                           -303765, 144124, 144124, -nan)
reports[-1].sigmaresid = ValErr(1.99118, 0.00370875, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00350816, None, -7.00895e-06, None, 0.000281088, None, -9.17608e-06, None, 0.000281088, None, -9.17608e-06, None, -0.00156029, None, -1.33746e-06, None, -0.00156029, None, -1.33746e-06, None, 1.99118, None, 0.00571067, None, 1.99118, None, 0.00571067, None)

reports.append(Report(588808192, ("DT", -2, 4, 6), "MBwhAst4sec06"))
reports[-1].posNum = 147134
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.000385864, 0.00521749, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.41936e-05, 8.43911e-05, 0), \
                           -309900, 147134, 147134, -nan)
reports[-1].sigmaresid = ValErr(1.98835, 0.00366539, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00170822, None, 0.000106873, None, 0.000276771, None, 0.000115937, None, 0.000276771, None, 0.000115937, None, 0.00878548, None, 0.000105149, None, 0.00878548, None, 0.000105149, None, 1.98835, None, 0.00570247, None, 1.98835, None, 0.00570247, None)

reports.append(Report(589070336, ("DT", -2, 4, 7), "MBwhAst4sec07"))
reports[-1].posNum = 142776
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.000456369, 0.00529292, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.15605e-06, 8.55384e-05, 0), \
                           -300479, 142776, 142776, -nan)
reports[-1].sigmaresid = ValErr(1.98499, 0.00371462, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00521266, None, 0.000108471, None, -0.000465959, None, 0.000110779, None, -0.000465959, None, 0.000110779, None, 0.00243053, None, 9.31342e-05, None, 0.00243053, None, 9.31342e-05, None, 1.98499, None, 0.00569062, None, 1.98499, None, 0.00569062, None)

reports.append(Report(589332480, ("DT", -2, 4, 8), "MBwhAst4sec08"))
reports[-1].posNum = 141344
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.000480092, 0.00531699, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.13674e-05, 8.58395e-05, 0), \
                           -297369, 141344, 141344, -nan)
reports[-1].sigmaresid = ValErr(1.98363, 0.00373085, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0084292, None, 9.6801e-05, None, 0.000394369, None, 9.5272e-05, None, 0.000394369, None, 9.5272e-05, None, 0.00113025, None, 9.8432e-05, None, 0.00113025, None, 9.8432e-05, None, 1.98363, None, 0.0057064, None, 1.98363, None, 0.0057064, None)

reports.append(Report(589594624, ("DT", -2, 4, 9), "MBwhAst4sec09"))
reports[-1].posNum = 74486
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.000455897, 0.00710006, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.45819e-06, 0.000114844, 0), \
                           -154380, 74486, 74486, -nan)
reports[-1].sigmaresid = ValErr(1.9226, 0.00498126, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000526158, None, 4.40699e-05, None, 0.000409142, None, 3.47759e-05, None, 0.000409142, None, 3.47759e-05, None, 0.000504397, None, 4.04869e-05, None, 0.000504397, None, 4.04869e-05, None, 1.92259, None, 0.00552274, None, 1.92259, None, 0.00552274, None)

reports.append(Report(589856768, ("DT", -2, 4, 10), "MBwhAst4sec10"))
reports[-1].posNum = 91346
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.00179307, 0.00665452, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.47043e-05, 0.000106868, 0), \
                           -192824, 91346, 91346, -nan)
reports[-1].sigmaresid = ValErr(1.99767, 0.00467378, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00622348, None, -0.000163071, None, -0.0016869, None, -0.000155295, None, -0.0016869, None, -0.000155295, None, 0.000766903, None, -0.000151564, None, 0.000766903, None, -0.000151564, None, 1.99767, None, 0.00574406, None, 1.99767, None, 0.00574406, None)

reports.append(Report(590905344, ("DT", -2, 4, 14), "MBwhAst4sec14"))
reports[-1].posNum = 92254
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.000887887, 0.00659525, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.20872e-05, 0.000106598, 0), \
                           -194444, 92254, 92254, -nan)
reports[-1].sigmaresid = ValErr(1.99125, 0.00463574, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00481823, None, 0.000153772, None, 0.000671396, None, 0.000160866, None, 0.000671396, None, 0.000160866, None, 0.00248355, None, 0.000158982, None, 0.00248355, None, 0.000158982, None, 1.99125, None, 0.00574013, None, 1.99125, None, 0.00574013, None)

reports.append(Report(590118912, ("DT", -2, 4, 11), "MBwhAst4sec11"))
reports[-1].posNum = 75316
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.00200185, 0.0070645, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.13424e-05, 0.000114521, 0), \
                           -156193, 75316, 75316, -nan)
reports[-1].sigmaresid = ValErr(1.92493, 0.00495972, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00881881, None, -0.000248817, None, 0.00205803, None, -0.00023072, None, 0.00205803, None, -0.00023072, None, 0.00347757, None, -0.00022088, None, 0.00347757, None, -0.00022088, None, 1.92493, None, 0.0055199, None, 1.92493, None, 0.0055199, None)

reports.append(Report(590381056, ("DT", -2, 4, 12), "MBwhAst4sec12"))
reports[-1].posNum = 140646
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.000985601, 0.00530212, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.97085e-06, 8.58982e-05, 0), \
                           -295367, 140646, 140646, -nan)
reports[-1].sigmaresid = ValErr(1.97612, 0.00372593, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00316743, None, -7.04312e-05, None, -0.000937377, None, -6.21009e-05, None, -0.000937377, None, -6.21009e-05, None, -0.00704108, None, -4.16317e-05, None, -0.00704108, None, -4.16317e-05, None, 1.97612, None, 0.00567688, None, 1.97612, None, 0.00567688, None)

reports.append(Report(587530240, ("DT", -1, 4, 1), "MBwhBst4sec01"))
reports[-1].posNum = 179300
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.000356262, 0.00448406, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.12961e-06, 6.90412e-05, 0), \
                           -368990, 179300, 179300, -nan)
reports[-1].sigmaresid = ValErr(1.89461, 0.00316384, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00180177, None, -4.0459e-05, None, 0.00036295, None, -5.32131e-05, None, 0.00036295, None, -5.32131e-05, None, -0.00095012, None, -3.48396e-05, None, -0.00095012, None, -3.48396e-05, None, 1.89461, None, 0.0054381, None, 1.89461, None, 0.0054381, None)

reports.append(Report(587792384, ("DT", -1, 4, 2), "MBwhBst4sec02"))
reports[-1].posNum = 179688
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.000310719, 0.00446473, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.21456e-06, 6.8719e-05, 0), \
                           -369195, 179688, 179688, -nan)
reports[-1].sigmaresid = ValErr(1.88836, 0.00315001, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00273947, None, -5.93e-05, None, -0.000283124, None, -5.59256e-05, None, -0.000283124, None, -5.59256e-05, None, -0.000527849, None, -5.41034e-05, None, -0.000527849, None, -5.41034e-05, None, 1.88836, None, 0.00541292, None, 1.88836, None, 0.00541292, None)

reports.append(Report(588054528, ("DT", -1, 4, 3), "MBwhBst4sec03"))
reports[-1].posNum = 143582
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.00022421, 0.00489672, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.45077e-05, 9.18339e-05, 0), \
                           -292291, 143582, 143582, -nan)
reports[-1].sigmaresid = ValErr(1.85294, 0.00345776, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00172332, None, -2.39627e-05, None, 0.00026442, None, -2.46963e-05, None, 0.00026442, None, -2.46963e-05, None, -0.00447791, None, -1.40494e-05, None, -0.00447791, None, -1.40494e-05, None, 1.85294, None, 0.00531587, None, 1.85294, None, 0.00531587, None)

reports.append(Report(588316672, ("DT", -1, 4, 4), "MBwhBst4sec04"))
reports[-1].posNum = 128866
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.000383665, 0.00533697, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.24206e-06, 8.20085e-05, 0), \
                           -266359, 128866, 128866, -nan)
reports[-1].sigmaresid = ValErr(1.91172, 0.00376566, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00405826, None, -5.84984e-05, None, -0.000368498, None, -3.80705e-05, None, -0.000368498, None, -3.80705e-05, None, 0.000120583, None, -2.59749e-05, None, 0.000120583, None, -2.59749e-05, None, 1.91172, None, 0.00546949, None, 1.91172, None, 0.00546949, None)

reports.append(Report(590675968, ("DT", -1, 4, 13), "MBwhBst4sec13"))
reports[-1].posNum = 130682
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.000297899, 0.00532428, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.09943e-06, 8.19599e-05, 0), \
                           -270753, 130682, 130682, -nan)
reports[-1].sigmaresid = ValErr(1.92112, 0.00375778, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00148229, None, 1.40494e-06, None, -0.000256239, None, -5.91168e-06, None, -0.000256239, None, -5.91168e-06, None, 0.00404947, None, -2.6628e-05, None, 0.00404947, None, -2.6628e-05, None, 1.92112, None, 0.00550657, None, 1.92112, None, 0.00550657, None)

reports.append(Report(588578816, ("DT", -1, 4, 5), "MBwhBst4sec05"))
reports[-1].posNum = 176658
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.000109343, 0.00452109, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.24268e-06, 6.97918e-05, 0), \
                           -363680, 176658, 176658, -nan)
reports[-1].sigmaresid = ValErr(1.89597, 0.00318969, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00855428, None, -4.60583e-05, None, -7.52627e-05, None, -4.20939e-05, None, -7.52627e-05, None, -4.20939e-05, None, 0.00106787, None, -3.93705e-05, None, 0.00106787, None, -3.93705e-05, None, 1.89596, None, 0.00545953, None, 1.89596, None, 0.00545953, None)

reports.append(Report(588840960, ("DT", -1, 4, 6), "MBwhBst4sec06"))
reports[-1].posNum = 181586
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.000251781, 0.00446709, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.5136e-07, 6.87962e-05, 0), \
                           -374202, 181586, 181586, -nan)
reports[-1].sigmaresid = ValErr(1.89991, 0.00315267, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00157165, None, 3.87702e-05, None, 0.000254988, None, 4.49406e-05, None, 0.000254988, None, 4.49406e-05, None, -0.00381482, None, 5.44236e-05, None, -0.00381482, None, 5.44236e-05, None, 1.89991, None, 0.00544763, None, 1.89991, None, 0.00544763, None)

reports.append(Report(589103104, ("DT", -1, 4, 7), "MBwhBst4sec07"))
reports[-1].posNum = 174820
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.000349227, 0.00451474, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(7.37241e-07, 6.94708e-05, 0), \
                           -358786, 174820, 174820, -nan)
reports[-1].sigmaresid = ValErr(1.88396, 0.00318612, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0084185, None, -1.13533e-05, None, -0.000343044, None, -8.39533e-06, None, -0.000343044, None, -8.39533e-06, None, 0.00520613, None, -2.39539e-05, None, 0.00520613, None, -2.39539e-05, None, 1.88396, None, 0.00541844, None, 1.88396, None, 0.00541844, None)

reports.append(Report(589365248, ("DT", -1, 4, 8), "MBwhBst4sec08"))
reports[-1].posNum = 174552
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.000181864, 0.00453689, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.44102e-06, 6.99813e-05, 0), \
                           -358923, 174552, 174552, -nan)
reports[-1].sigmaresid = ValErr(1.89139, 0.00319939, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(6.42978e-05, None, 1.22267e-05, None, -0.000175783, None, 2.12779e-05, None, -0.000175783, None, 2.12779e-05, None, -0.00194881, None, 2.0745e-05, None, -0.00194881, None, 2.0745e-05, None, 1.89139, None, 0.00542405, None, 1.89139, None, 0.00542405, None)

reports.append(Report(589627392, ("DT", -1, 4, 9), "MBwhBst4sec09"))
reports[-1].posNum = 93526
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.000963253, 0.00599764, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.64701e-05, 9.24995e-05, 0), \
                           -189214, 93526, 93526, -nan)
reports[-1].sigmaresid = ValErr(1.82974, 0.00423066, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00695153, None, -5.31004e-06, None, -0.00089272, None, -6.96885e-06, None, -0.00089272, None, -6.96885e-06, None, 0.00170357, None, -2.25285e-06, None, 0.00170357, None, -2.25285e-06, None, 1.82974, None, 0.00524624, None, 1.82974, None, 0.00524624, None)

reports.append(Report(589889536, ("DT", -1, 4, 10), "MBwhBst4sec10"))
reports[-1].posNum = 112456
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.00019161, 0.00561887, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.61504e-07, 8.69173e-05, 0), \
                           -230593, 112456, 112456, -nan)
reports[-1].sigmaresid = ValErr(1.88058, 0.00396539, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00963215, None, 4.67588e-05, None, 0.00019189, None, 2.56614e-05, None, 0.00019189, None, 2.56614e-05, None, 0.00330788, None, 1.88229e-05, None, 0.00330788, None, 1.88229e-05, None, 1.88057, None, 0.0054165, None, 1.88057, None, 0.0054165, None)

reports.append(Report(590938112, ("DT", -1, 4, 14), "MBwhBst4sec14"))
reports[-1].posNum = 112632
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-7.20463e-05, 0.00569552, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.41396e-06, 8.78472e-05, 0), \
                           -232507, 112632, 112632, -nan)
reports[-1].sigmaresid = ValErr(1.9067, 0.00401733, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.002632, None, -1.37162e-05, None, -4.58579e-05, None, -8.48902e-06, None, -4.58579e-05, None, -8.48902e-06, None, 0.00733851, None, -2.67665e-05, None, 0.00733851, None, -2.67665e-05, None, 1.9067, None, 0.00548573, None, 1.9067, None, 0.00548573, None)

reports.append(Report(590151680, ("DT", -1, 4, 11), "MBwhBst4sec11"))
reports[-1].posNum = 92664
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-7.63448e-05, 0.00605237, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.34737e-06, 9.32908e-05, 0), \
                           -187872, 92664, 92664, -nan)
reports[-1].sigmaresid = ValErr(1.8377, 0.0042688, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00303066, None, -4.12211e-05, None, -8.02088e-05, None, -2.77946e-05, None, -8.02088e-05, None, -2.77946e-05, None, 0.00451771, None, -3.91866e-05, None, 0.00451771, None, -3.91866e-05, None, 1.8377, None, 0.00527637, None, 1.8377, None, 0.00527637, None)

reports.append(Report(590413824, ("DT", -1, 4, 12), "MBwhBst4sec12"))
reports[-1].posNum = 173450
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.000133662, 0.00451671, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.59193e-07, 6.96254e-05, 0), \
                           -355327, 173450, 173450, -nan)
reports[-1].sigmaresid = ValErr(1.87695, 0.00318678, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00390443, None, -2.96663e-05, None, 0.000133829, None, -2.13925e-05, None, 0.000133829, None, -2.13925e-05, None, 0.00268398, None, -2.89706e-05, None, 0.00268398, None, -2.89706e-05, None, 1.87695, None, 0.00538833, None, 1.87695, None, 0.00538833, None)

reports.append(Report(587563008, ("DT", 0, 4, 1), "MBwhCst4sec01"))
reports[-1].posNum = 196148
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.000396519, 0.00426658, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.07639e-06, 6.42771e-05, 0), \
                           -403144, 196148, 196148, -nan)
reports[-1].sigmaresid = ValErr(1.88961, 0.00301693, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00102212, None, 1.56815e-05, None, -0.000395771, None, 1.83398e-05, None, -0.000395771, None, 1.83398e-05, None, -0.00617845, None, 4.40062e-05, None, -0.00617845, None, 4.40062e-05, None, 1.8896, None, 0.00551545, None, 1.8896, None, 0.00551545, None)

reports.append(Report(587825152, ("DT", 0, 4, 2), "MBwhCst4sec02"))
reports[-1].posNum = 194626
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.0002805, 0.00424609, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.06008e-06, 6.39591e-05, 0), \
                           -398321, 194626, 194626, -nan)
reports[-1].sigmaresid = ValErr(1.87322, 0.00300244, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00214274, None, -2.82821e-05, None, -0.000279264, None, -2.67812e-05, None, -0.000279264, None, -2.67812e-05, None, 0.00327844, None, -3.90031e-05, None, 0.00327844, None, -3.90031e-05, None, 1.87322, None, 0.00548906, None, 1.87322, None, 0.00548906, None)

reports.append(Report(588087296, ("DT", 0, 4, 3), "MBwhCst4sec03"))
reports[-1].posNum = 192158
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.000782494, 0.00427708, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(9.39195e-06, 6.42429e-05, 0), \
                           -393440, 192158, 192158, -nan)
reports[-1].sigmaresid = ValErr(1.87488, 0.00302433, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00137635, None, -2.35198e-06, None, -0.00077848, None, -6.04851e-06, None, -0.00077848, None, -6.04851e-06, None, 0.00318174, None, -3.21768e-05, None, 0.00318174, None, -3.21768e-05, None, 1.87488, None, 0.00547776, None, 1.87488, None, 0.00547776, None)

reports.append(Report(588349440, ("DT", 0, 4, 4), "MBwhCst4sec04"))
reports[-1].posNum = 142636
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.000364542, 0.00509576, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.82028e-06, 7.67438e-05, 0), \
                           -295773, 142636, 142636, -nan)
reports[-1].sigmaresid = ValErr(1.92453, 0.00360325, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00107689, None, 1.48189e-06, None, -0.00036439, None, 8.26254e-06, None, -0.00036439, None, 8.26254e-06, None, -0.00583623, None, 2.55168e-05, None, -0.00583623, None, 2.55168e-05, None, 1.92453, None, 0.00560063, None, 1.92453, None, 0.00560063, None)

reports.append(Report(590708736, ("DT", 0, 4, 13), "MBwhCst4sec13"))
reports[-1].posNum = 142204
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.000281962, 0.00507335, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.02472e-06, 7.65223e-05, 0), \
                           -294034, 142204, 142204, -nan)
reports[-1].sigmaresid = ValErr(1.91316, 0.0035874, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00488482, None, 2.01349e-05, None, 0.000281906, None, 3.76881e-05, None, 0.000281906, None, 3.76881e-05, None, 0.000920941, None, 4.46755e-05, None, 0.000920941, None, 4.46755e-05, None, 1.91316, None, 0.00557546, None, 1.91316, None, 0.00557546, None)

reports.append(Report(588611584, ("DT", 0, 4, 5), "MBwhCst4sec05"))
reports[-1].posNum = 194954
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(1.45837e-05, 0.00425834, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.57044e-08, 6.40416e-05, 0), \
                           -399718, 194954, 194954, -nan)
reports[-1].sigmaresid = ValErr(1.88021, 0.0030111, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0053711, None, -2.71367e-05, None, 1.81636e-05, None, -2.46146e-05, None, 1.81636e-05, None, -2.46146e-05, None, 0.000786426, None, -2.45963e-05, None, 0.000786426, None, -2.45963e-05, None, 1.88021, None, 0.00548064, None, 1.88021, None, 0.00548064, None)

reports.append(Report(588873728, ("DT", 0, 4, 6), "MBwhCst4sec06"))
reports[-1].posNum = 194000
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-1.19916e-06, 0.00427061, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.28574e-06, 6.4275e-05, 0), \
                           -397844, 194000, 194000, -nan)
reports[-1].sigmaresid = ValErr(1.881, 0.00301978, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00407228, None, 9.41802e-06, None, -7.99496e-07, None, 1.02426e-05, None, -7.99496e-07, None, 1.02426e-05, None, 0.000711675, None, 3.40885e-06, None, 0.000711675, None, 3.40885e-06, None, 1.881, None, 0.00549978, None, 1.881, None, 0.00549978, None)

reports.append(Report(589135872, ("DT", 0, 4, 7), "MBwhCst4sec07"))
reports[-1].posNum = 191874
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.000525897, 0.00426911, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.46829e-06, 6.423e-05, 0), \
                           -392360, 191874, 191874, -nan)
reports[-1].sigmaresid = ValErr(1.87002, 0.00301872, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000429101, None, -1.15714e-05, None, -0.000523987, None, 3.33869e-06, None, -0.000523987, None, 3.33869e-06, None, 0.000375733, None, 2.33863e-06, None, 0.000375733, None, 2.33863e-06, None, 1.87002, None, 0.00546736, None, 1.87002, None, 0.00546736, None)

reports.append(Report(589398016, ("DT", 0, 4, 8), "MBwhCst4sec08"))
reports[-1].posNum = 189798
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.000923472, 0.00428377, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.72098e-06, 6.4375e-05, 0), \
                           -387734, 189798, 189798, -nan)
reports[-1].sigmaresid = ValErr(1.86626, 0.00302908, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00228788, None, -5.68058e-06, None, 0.000921469, None, -9.43204e-07, None, 0.000921469, None, -9.43204e-07, None, 0.00503835, None, -9.97959e-06, None, 0.00503835, None, -9.97959e-06, None, 1.86626, None, 0.00547686, None, 1.86626, None, 0.00547686, None)

reports.append(Report(589660160, ("DT", 0, 4, 9), "MBwhCst4sec09"))
reports[-1].posNum = 102068
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.000632859, 0.00567832, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.3138e-06, 8.53124e-05, 0), \
                           -205619, 102068, 102068, -nan)
reports[-1].sigmaresid = ValErr(1.8141, 0.00401515, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00384662, None, 2.45393e-05, None, -0.000630368, None, 2.20344e-05, None, -0.000630368, None, 2.20344e-05, None, 0.00129089, None, 1.64757e-05, None, 0.00129089, None, 1.64757e-05, None, 1.8141, None, 0.00528643, None, 1.8141, None, 0.00528643, None)

reports.append(Report(589922304, ("DT", 0, 4, 10), "MBwhCst4sec10"))
reports[-1].posNum = 123384
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.000303466, 0.00536073, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.85163e-06, 8.05269e-05, 0), \
                           -253159, 123384, 123384, -nan)
reports[-1].sigmaresid = ValErr(1.883, 0.00379058, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0031601, None, 1.25282e-05, None, -0.000301698, None, 1.06877e-05, None, -0.000301698, None, 1.06877e-05, None, -0.000914572, None, 1.27249e-06, None, -0.000914572, None, 1.27249e-06, None, 1.88299, None, 0.00554159, None, 1.88299, None, 0.00554159, None)

reports.append(Report(590970880, ("DT", 0, 4, 14), "MBwhCst4sec14"))
reports[-1].posNum = 123648
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.000450459, 0.005357, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.0634e-06, 8.04216e-05, 0), \
                           -253748, 123648, 123648, -nan)
reports[-1].sigmaresid = ValErr(1.88371, 0.00378797, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000581103, None, -2.31514e-05, None, -0.000448764, None, -1.81889e-05, None, -0.000448764, None, -1.81889e-05, None, -0.00031118, None, -1.14599e-05, None, -0.00031118, None, -1.14599e-05, None, 1.88371, None, 0.00553392, None, 1.88371, None, 0.00553392, None)

reports.append(Report(590184448, ("DT", 0, 4, 11), "MBwhCst4sec11"))
reports[-1].posNum = 102446
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.000788311, 0.00567402, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.51438e-06, 8.55314e-05, 0), \
                           -206493, 102446, 102446, -nan)
reports[-1].sigmaresid = ValErr(1.81609, 0.00401213, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00586749, None, -4.47216e-05, None, 0.000786988, None, -4.04617e-05, None, 0.000786988, None, -4.04617e-05, None, 0.000330501, None, -3.97044e-05, None, 0.000330501, None, -3.97044e-05, None, 1.81609, None, 0.00528594, None, 1.81609, None, 0.00528594, None)

reports.append(Report(590446592, ("DT", 0, 4, 12), "MBwhCst4sec12"))
reports[-1].posNum = 189444
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.000344182, 0.00428593, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.2741e-06, 6.43534e-05, 0), \
                           -386928, 189444, 189444, -nan)
reports[-1].sigmaresid = ValErr(1.86545, 0.0030306, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000672274, None, 2.16447e-05, None, 0.000342344, None, 1.91874e-05, None, 0.000342344, None, 1.91874e-05, None, 0.00272524, None, 1.85588e-05, None, 0.00272524, None, 1.85588e-05, None, 1.86544, None, 0.00547824, None, 1.86544, None, 0.00547824, None)

reports.append(Report(587595776, ("DT", 1, 4, 1), "MBwhDst4sec01"))
reports[-1].posNum = 177820
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.000202945, 0.00448751, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.08226e-06, 6.90461e-05, 0), \
                           -365325, 177820, 177820, -nan)
reports[-1].sigmaresid = ValErr(1.88802, 0.00316593, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000141545, None, 1.62265e-05, None, -0.000214354, None, 1.62015e-05, None, -0.000214354, None, 1.62015e-05, None, -0.00671848, None, 1.49973e-05, None, -0.00671848, None, 1.49973e-05, None, 1.88802, None, 0.00540932, None, 1.88802, None, 0.00540932, None)

reports.append(Report(587857920, ("DT", 1, 4, 2), "MBwhDst4sec02"))
reports[-1].posNum = 178416
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.000178024, 0.00448775, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.15913e-07, 6.92412e-05, 0), \
                           -366847, 178416, 178416, -nan)
reports[-1].sigmaresid = ValErr(1.89117, 0.00316592, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(1.90353e-05, None, 6.56626e-06, None, -0.000179916, None, 3.09296e-05, None, -0.000179916, None, 3.09296e-05, None, -0.000600948, None, 1.88064e-05, None, -0.000600948, None, 1.88064e-05, None, 1.89117, None, 0.00543986, None, 1.89117, None, 0.00543986, None)

reports.append(Report(588120064, ("DT", 1, 4, 3), "MBwhDst4sec03"))
reports[-1].posNum = 176146
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.000702363, 0.00450721, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.66551e-06, 6.94207e-05, 0), \
                           -361851, 176146, 176146, -nan)
reports[-1].sigmaresid = ValErr(1.88764, 0.00318029, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00202071, None, 5.28023e-06, None, 0.000724655, None, -7.69357e-06, None, 0.000724655, None, -7.69357e-06, None, 0.00585566, None, -3.67346e-05, None, 0.00585566, None, -3.67346e-05, None, 1.88764, None, 0.00539955, None, 1.88764, None, 0.00539955, None)

reports.append(Report(588382208, ("DT", 1, 4, 4), "MBwhDst4sec04"))
reports[-1].posNum = 105534
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-5.35384e-05, 0.00586263, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.86746e-07, 0.000110275, 0), \
                           -217598, 105534, 105534, -nan)
reports[-1].sigmaresid = ValErr(1.90207, 0.00414014, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00260691, None, 2.03077e-06, None, -7.10374e-05, None, 1.13776e-05, None, -7.10374e-05, None, 1.13776e-05, None, -7.17965e-05, None, 2.80804e-06, None, -7.17965e-05, None, 2.80804e-06, None, 1.90207, None, 0.0055085, None, 1.90207, None, 0.0055085, None)

reports.append(Report(590741504, ("DT", 1, 4, 13), "MBwhDst4sec13"))
reports[-1].posNum = 106372
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.00014152, 0.00585728, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.13345e-06, 0.000109927, 0), \
                           -219626, 106372, 106372, -nan)
reports[-1].sigmaresid = ValErr(1.90744, 0.00413545, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0012893, None, 6.0364e-05, None, 0.000120672, None, 4.69311e-05, None, 0.000120672, None, 4.69311e-05, None, 0.00565509, None, 4.06267e-05, None, 0.00565509, None, 4.06267e-05, None, 1.90744, None, 0.00547463, None, 1.90744, None, 0.00547463, None)

reports.append(Report(588644352, ("DT", 1, 4, 5), "MBwhDst4sec05"))
reports[-1].posNum = 175430
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.000616608, 0.0045377, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.22715e-05, 6.99645e-05, 0), \
                           -361196, 175430, 175430, -nan)
reports[-1].sigmaresid = ValErr(1.89645, 0.00320166, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00384104, None, 2.68912e-05, None, 0.000564277, None, 2.24851e-05, None, 0.000564277, None, 2.24851e-05, None, 0.00158882, None, 2.87029e-05, None, 0.00158882, None, 2.87029e-05, None, 1.89644, None, 0.00541625, None, 1.89644, None, 0.00541625, None)

reports.append(Report(588906496, ("DT", 1, 4, 6), "MBwhDst4sec06"))
reports[-1].posNum = 178654
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.000413348, 0.00449723, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.07955e-06, 6.93941e-05, 0), \
                           -367806, 178654, 178654, -nan)
reports[-1].sigmaresid = ValErr(1.89615, 0.00317213, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00284839, None, 2.78271e-05, None, 0.00038739, None, 2.70582e-05, None, 0.00038739, None, 2.70582e-05, None, -0.00259536, None, 3.18552e-05, None, -0.00259536, None, 3.18552e-05, None, 1.89615, None, 0.00543674, None, 1.89615, None, 0.00543674, None)

reports.append(Report(589168640, ("DT", 1, 4, 7), "MBwhDst4sec07"))
reports[-1].posNum = 177436
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.000283494, 0.00449503, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(9.71437e-06, 6.92408e-05, 0), \
                           -364687, 177436, 177436, -nan)
reports[-1].sigmaresid = ValErr(1.88962, 0.00317205, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000238787, None, -4.7656e-05, None, 0.000323236, None, -3.46063e-05, None, 0.000323236, None, -3.46063e-05, None, -0.00143617, None, -2.32627e-05, None, -0.00143617, None, -2.32627e-05, None, 1.88962, None, 0.00541836, None, 1.88962, None, 0.00541836, None)

reports.append(Report(589430784, ("DT", 1, 4, 8), "MBwhDst4sec08"))
reports[-1].posNum = 172790
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.000130418, 0.00454065, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.96894e-06, 7.01297e-05, 0), \
                           -354605, 172790, 172790, -nan)
reports[-1].sigmaresid = ValErr(1.8838, 0.00320451, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00190201, None, -3.05739e-05, None, 0.000144436, None, -4.45993e-05, None, 0.000144436, None, -4.45993e-05, None, 0.00386771, None, -4.69435e-05, None, 0.00386771, None, -4.69435e-05, None, 1.8838, None, 0.0054234, None, 1.8838, None, 0.0054234, None)

reports.append(Report(589692928, ("DT", 1, 4, 9), "MBwhDst4sec09"))
reports[-1].posNum = 92390
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(3.38181e-05, 0.00600924, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.58641e-05, 9.26502e-05, 0), \
                           -186545, 92390, 92390, -nan)
reports[-1].sigmaresid = ValErr(1.82242, 0.00423956, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00382713, None, -5.78444e-05, None, 0.000106489, None, -5.63581e-05, None, 0.000106489, None, -5.63581e-05, None, -0.000528285, None, -4.73727e-05, None, -0.000528285, None, -4.73727e-05, None, 1.82242, None, 0.00521702, None, 1.82242, None, 0.00521702, None)

reports.append(Report(589955072, ("DT", 1, 4, 10), "MBwhDst4sec10"))
reports[-1].posNum = 112806
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.000161788, 0.00569716, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.24848e-05, 8.78009e-05, 0), \
                           -233029, 112806, 112806, -nan)
reports[-1].sigmaresid = ValErr(1.90944, 0.00401998, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00538153, None, 6.11999e-05, None, -0.000214367, None, 4.76325e-05, None, -0.000214367, None, 4.76325e-05, None, 0.000941151, None, 4.86158e-05, None, 0.000941151, None, 4.86158e-05, None, 1.90944, None, 0.00548643, None, 1.90944, None, 0.00548643, None)

reports.append(Report(591003648, ("DT", 1, 4, 14), "MBwhDst4sec14"))
reports[-1].posNum = 112736
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.000439641, 0.00566698, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.76557e-05, 8.73966e-05, 0), \
                           -232264, 112736, 112736, -nan)
reports[-1].sigmaresid = ValErr(1.89897, 0.00399918, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000676367, None, -0.00013191, None, -0.000366737, None, -0.000114, None, -0.000366737, None, -0.000114, None, 0.000295622, None, -0.000113908, None, 0.000295622, None, -0.000113908, None, 1.89897, None, 0.00547955, None, 1.89897, None, 0.00547955, None)

reports.append(Report(590217216, ("DT", 1, 4, 11), "MBwhDst4sec11"))
reports[-1].posNum = 93184
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.000943842, 0.00602116, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.63691e-05, 9.28197e-05, 0), \
                           -188721, 93184, 93184, -nan)
reports[-1].sigmaresid = ValErr(1.83367, 0.00424751, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00583711, None, 3.93019e-07, None, -0.000874856, None, -3.00481e-06, None, -0.000874856, None, -3.00481e-06, None, 0.000302693, None, -5.61875e-06, None, 0.000302693, None, -5.61875e-06, None, 1.83367, None, 0.00521659, None, 1.83367, None, 0.00521659, None)

reports.append(Report(590479360, ("DT", 1, 4, 12), "MBwhDst4sec12"))
reports[-1].posNum = 173634
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.00055842, 0.0045338, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.29997e-05, 7.00264e-05, 0), \
                           -356485, 173634, 173634, -nan)
reports[-1].sigmaresid = ValErr(1.8854, 0.00319942, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00125811, None, 2.66282e-06, None, -0.000611753, None, 4.9204e-06, None, -0.000611753, None, 4.9204e-06, None, -0.00440499, None, 1.32274e-05, None, -0.00440499, None, 1.32274e-05, None, 1.8854, None, 0.00543681, None, 1.8854, None, 0.00543681, None)

reports.append(Report(587628544, ("DT", 2, 4, 1), "MBwhEst4sec01"))
reports[-1].posNum = 145236
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.00071824, 0.00526645, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.99386e-05, 8.51055e-05, 0), \
                           -306238, 145236, 145236, -nan)
reports[-1].sigmaresid = ValErr(1.99295, 0.00369797, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00120432, None, 0.000170912, None, 0.000572313, None, 0.000185835, None, 0.000572313, None, 0.000185835, None, 0.000260686, None, 0.000183341, None, 0.000260686, None, 0.000183341, None, 1.99295, None, 0.0057137, None, 1.99295, None, 0.0057137, None)

reports.append(Report(587890688, ("DT", 2, 4, 2), "MBwhEst4sec02"))
reports[-1].posNum = 145726
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.000117604, 0.0052263, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.43263e-06, 8.43915e-05, 0), \
                           -306337, 145726, 145726, -nan)
reports[-1].sigmaresid = ValErr(1.98022, 0.003668, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(3.20224e-05, None, 0.000157906, None, -0.00014445, None, 0.000163285, None, -0.00014445, None, 0.000163285, None, -0.00463884, None, 0.000160831, None, -0.00463884, None, 0.000160831, None, 1.98022, None, 0.00568767, None, 1.98022, None, 0.00568767, None)

reports.append(Report(588152832, ("DT", 2, 4, 3), "MBwhEst4sec03"))
reports[-1].posNum = 144128
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.00049011, 0.00524674, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.51367e-05, 8.47838e-05, 0), \
                           -302816, 144128, 144128, -nan)
reports[-1].sigmaresid = ValErr(1.97799, 0.00368414, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00793056, None, 0.000232337, None, -0.000607683, None, 0.000216078, None, -0.000607683, None, 0.000216078, None, -0.00257916, None, 0.000204997, None, -0.00257916, None, 0.000204997, None, 1.97799, None, 0.0056688, None, 1.97799, None, 0.0056688, None)

reports.append(Report(588414976, ("DT", 2, 4, 4), "MBwhEst4sec04"))
reports[-1].posNum = 106550
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.000374757, 0.00626142, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.48349e-05, 0.000100773, 0), \
                           -226704, 106550, 106550, -nan)
reports[-1].sigmaresid = ValErr(2.03142, 0.00440056, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00405059, None, 0.000197518, None, 0.000263972, None, 0.000219993, None, 0.000263972, None, 0.000219993, None, 0.000674103, None, 0.000206948, None, 0.000674103, None, 0.000206948, None, 2.03142, None, 0.00583018, None, 2.03142, None, 0.00583018, None)

reports.append(Report(590774272, ("DT", 2, 4, 13), "MBwhEst4sec13"))
reports[-1].posNum = 106894
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.000912185, 0.00627186, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.07759e-06, 0.000100894, 0), \
                           -227747, 106894, 106894, -nan)
reports[-1].sigmaresid = ValErr(2.03734, 0.00440628, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000316463, None, -7.07765e-05, None, 0.000857194, None, -8.77209e-05, None, 0.000857194, None, -8.77209e-05, None, -0.00868524, None, -5.9834e-05, None, -0.00868524, None, -5.9834e-05, None, 2.03734, None, 0.00581937, None, 2.03734, None, 0.00581937, None)

reports.append(Report(588677120, ("DT", 2, 4, 5), "MBwhEst4sec05"))
reports[-1].posNum = 142686
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.000520383, 0.00530374, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.81969e-05, 8.55668e-05, 0), \
                           -300621, 142686, 142686, -nan)
reports[-1].sigmaresid = ValErr(1.9896, 0.00372472, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00528001, None, -0.000150799, None, -0.000388016, None, -0.000143288, None, -0.000388016, None, -0.000143288, None, -0.00540601, None, -0.000129899, None, -0.00540601, None, -0.000129899, None, 1.9896, None, 0.00571253, None, 1.9896, None, 0.00571253, None)

reports.append(Report(588939264, ("DT", 2, 4, 6), "MBwhEst4sec06"))
reports[-1].posNum = 145240
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(7.04046e-05, 0.00526109, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.82862e-07, 8.50178e-05, 0), \
                           -306049, 145240, 145240, -nan)
reports[-1].sigmaresid = ValErr(1.99025, 0.00369275, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00730763, None, -8.48411e-06, None, 6.98051e-05, None, -1.36322e-06, None, 6.98051e-05, None, -1.36322e-06, None, -0.00426745, None, 1.2584e-05, None, -0.00426745, None, 1.2584e-05, None, 1.99025, None, 0.00571697, None, 1.99025, None, 0.00571697, None)

reports.append(Report(589201408, ("DT", 2, 4, 7), "MBwhEst4sec07"))
reports[-1].posNum = 144602
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.000464189, 0.00528862, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.39982e-05, 8.53401e-05, 0), \
                           -305140, 144602, 144602, -nan)
reports[-1].sigmaresid = ValErr(1.99624, 0.00371203, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00364982, None, -0.000111256, None, -0.000351342, None, -0.000118828, None, -0.000351342, None, -0.000118828, None, -0.00327837, None, -0.000103688, None, -0.00327837, None, -0.000103688, None, 1.99625, None, 0.00572978, None, 1.99625, None, 0.00572978, None)

reports.append(Report(589463552, ("DT", 2, 4, 8), "MBwhEst4sec08"))
reports[-1].posNum = 141036
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.00018594, 0.00531538, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.50854e-05, 8.60954e-05, 0), \
                           -296615, 141036, 141036, -nan)
reports[-1].sigmaresid = ValErr(1.98215, 0.00373213, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00227138, None, -6.63064e-05, None, 0.000307421, None, -7.08603e-05, None, 0.000307421, None, -7.08603e-05, None, -0.0029115, None, -6.3771e-05, None, -0.0029115, None, -6.3771e-05, None, 1.98215, None, 0.00571358, None, 1.98215, None, 0.00571358, None)

reports.append(Report(589725696, ("DT", 2, 4, 9), "MBwhEst4sec09"))
reports[-1].posNum = 75816
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.000104916, 0.0070642, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.95166e-06, 0.000114175, 0), \
                           -157464, 75816, 75816, -nan)
reports[-1].sigmaresid = ValErr(1.93091, 0.0049587, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00686672, None, -1.06192e-05, None, -5.3595e-05, None, -3.07771e-05, None, -5.3595e-05, None, -3.07771e-05, None, -0.0041363, None, -2.09547e-05, None, -0.0041363, None, -2.09547e-05, None, 1.9309, None, 0.00551237, None, 1.9309, None, 0.00551237, None)

reports.append(Report(589987840, ("DT", 2, 4, 10), "MBwhEst4sec10"))
reports[-1].posNum = 91788
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.000811412, 0.00662638, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.24715e-06, 0.000106814, 0), \
                           -193607, 91788, 91788, -nan)
reports[-1].sigmaresid = ValErr(1.99441, 0.00465486, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00745479, None, 0.000117237, None, -0.000833323, None, 0.000106377, None, -0.000833323, None, 0.000106377, None, 0.00210629, None, 9.82676e-05, None, 0.00210629, None, 9.82676e-05, None, 1.9944, None, 0.00575858, None, 1.9944, None, 0.00575858, None)

reports.append(Report(591036416, ("DT", 2, 4, 14), "MBwhEst4sec14"))
reports[-1].posNum = 91830
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.000520257, 0.00659187, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.76361e-05, 0.000106001, 0), \
                           -193240, 91830, 91830, -nan)
reports[-1].sigmaresid = ValErr(1.98453, 0.00463074, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-5.66036e-05, None, -6.64313e-05, None, 0.000384088, None, -7.31518e-05, None, 0.000384088, None, -7.31518e-05, None, -0.000945513, None, -6.20261e-05, None, -0.000945513, None, -6.20261e-05, None, 1.98453, None, 0.00573723, None, 1.98453, None, 0.00573723, None)

reports.append(Report(590249984, ("DT", 2, 4, 11), "MBwhEst4sec11"))
reports[-1].posNum = 75226
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.00067306, 0.00705899, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.5933e-06, 0.000114026, 0), \
                           -155792, 75226, 75226, -nan)
reports[-1].sigmaresid = ValErr(1.91948, 0.00494861, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000335412, None, 5.31683e-05, None, 0.000626766, None, 2.17941e-05, None, 0.000626766, None, 2.17941e-05, None, -0.00691215, None, 5.48864e-05, None, -0.00691215, None, 5.48864e-05, None, 1.91948, None, 0.00548597, None, 1.91948, None, 0.00548597, None)

reports.append(Report(590512128, ("DT", 2, 4, 12), "MBwhEst4sec12"))
reports[-1].posNum = 141256
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.000344686, 0.0052918, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.17287e-05, 8.55717e-05, 0), \
                           -296445, 141256, 141256, -nan)
reports[-1].sigmaresid = ValErr(1.97328, 0.00371253, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0055835, None, 0.000145047, None, -0.000442484, None, 0.000143894, None, -0.000442484, None, 0.000143894, None, 0.00348354, None, 0.000121441, None, 0.00348354, None, 0.000121441, None, 1.97328, None, 0.00567219, None, 1.97328, None, 0.00567219, None)

reports.append(Report(604017672, ("CSC", 1, 1, 1, 1), "MEp11_01"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604017688, ("CSC", 1, 1, 1, 3), "MEp11_03"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604017704, ("CSC", 1, 1, 1, 5), "MEp11_05"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604017720, ("CSC", 1, 1, 1, 7), "MEp11_07"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604017736, ("CSC", 1, 1, 1, 9), "MEp11_09"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604017752, ("CSC", 1, 1, 1, 11), "MEp11_11"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604017768, ("CSC", 1, 1, 1, 13), "MEp11_13"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604017784, ("CSC", 1, 1, 1, 15), "MEp11_15"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604017800, ("CSC", 1, 1, 1, 17), "MEp11_17"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604017816, ("CSC", 1, 1, 1, 19), "MEp11_19"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604017832, ("CSC", 1, 1, 1, 21), "MEp11_21"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604017848, ("CSC", 1, 1, 1, 23), "MEp11_23"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604017864, ("CSC", 1, 1, 1, 25), "MEp11_25"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604017880, ("CSC", 1, 1, 1, 27), "MEp11_27"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604017896, ("CSC", 1, 1, 1, 29), "MEp11_29"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604017912, ("CSC", 1, 1, 1, 31), "MEp11_31"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604017928, ("CSC", 1, 1, 1, 33), "MEp11_33"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604017944, ("CSC", 1, 1, 1, 35), "MEp11_35"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604017680, ("CSC", 1, 1, 1, 2), "MEp11_02"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604017696, ("CSC", 1, 1, 1, 4), "MEp11_04"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604017712, ("CSC", 1, 1, 1, 6), "MEp11_06"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604017728, ("CSC", 1, 1, 1, 8), "MEp11_08"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604017744, ("CSC", 1, 1, 1, 10), "MEp11_10"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604017760, ("CSC", 1, 1, 1, 12), "MEp11_12"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604017776, ("CSC", 1, 1, 1, 14), "MEp11_14"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604017792, ("CSC", 1, 1, 1, 16), "MEp11_16"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604017808, ("CSC", 1, 1, 1, 18), "MEp11_18"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604017824, ("CSC", 1, 1, 1, 20), "MEp11_20"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604017840, ("CSC", 1, 1, 1, 22), "MEp11_22"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604017856, ("CSC", 1, 1, 1, 24), "MEp11_24"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604017872, ("CSC", 1, 1, 1, 26), "MEp11_26"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604017888, ("CSC", 1, 1, 1, 28), "MEp11_28"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604017904, ("CSC", 1, 1, 1, 30), "MEp11_30"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604017920, ("CSC", 1, 1, 1, 32), "MEp11_32"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604017936, ("CSC", 1, 1, 1, 34), "MEp11_34"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604017952, ("CSC", 1, 1, 1, 36), "MEp11_36"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604018184, ("CSC", 1, 1, 2, 1), "MEp12_01"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604018200, ("CSC", 1, 1, 2, 3), "MEp12_03"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604018216, ("CSC", 1, 1, 2, 5), "MEp12_05"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604018232, ("CSC", 1, 1, 2, 7), "MEp12_07"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604018248, ("CSC", 1, 1, 2, 9), "MEp12_09"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604018264, ("CSC", 1, 1, 2, 11), "MEp12_11"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604018280, ("CSC", 1, 1, 2, 13), "MEp12_13"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604018296, ("CSC", 1, 1, 2, 15), "MEp12_15"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604018312, ("CSC", 1, 1, 2, 17), "MEp12_17"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604018328, ("CSC", 1, 1, 2, 19), "MEp12_19"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604018344, ("CSC", 1, 1, 2, 21), "MEp12_21"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604018360, ("CSC", 1, 1, 2, 23), "MEp12_23"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604018376, ("CSC", 1, 1, 2, 25), "MEp12_25"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604018392, ("CSC", 1, 1, 2, 27), "MEp12_27"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604018408, ("CSC", 1, 1, 2, 29), "MEp12_29"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604018424, ("CSC", 1, 1, 2, 31), "MEp12_31"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604018440, ("CSC", 1, 1, 2, 33), "MEp12_33"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604018456, ("CSC", 1, 1, 2, 35), "MEp12_35"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604018192, ("CSC", 1, 1, 2, 2), "MEp12_02"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604018208, ("CSC", 1, 1, 2, 4), "MEp12_04"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604018224, ("CSC", 1, 1, 2, 6), "MEp12_06"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604018240, ("CSC", 1, 1, 2, 8), "MEp12_08"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604018256, ("CSC", 1, 1, 2, 10), "MEp12_10"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604018272, ("CSC", 1, 1, 2, 12), "MEp12_12"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604018288, ("CSC", 1, 1, 2, 14), "MEp12_14"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604018304, ("CSC", 1, 1, 2, 16), "MEp12_16"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604018320, ("CSC", 1, 1, 2, 18), "MEp12_18"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604018336, ("CSC", 1, 1, 2, 20), "MEp12_20"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604018352, ("CSC", 1, 1, 2, 22), "MEp12_22"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604018368, ("CSC", 1, 1, 2, 24), "MEp12_24"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604018384, ("CSC", 1, 1, 2, 26), "MEp12_26"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604018400, ("CSC", 1, 1, 2, 28), "MEp12_28"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604018416, ("CSC", 1, 1, 2, 30), "MEp12_30"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604018432, ("CSC", 1, 1, 2, 32), "MEp12_32"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604018448, ("CSC", 1, 1, 2, 34), "MEp12_34"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604018464, ("CSC", 1, 1, 2, 36), "MEp12_36"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604018696, ("CSC", 1, 1, 3, 1), "MEp13_01"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604018704, ("CSC", 1, 1, 3, 2), "MEp13_02"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604018712, ("CSC", 1, 1, 3, 3), "MEp13_03"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604018720, ("CSC", 1, 1, 3, 4), "MEp13_04"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604018728, ("CSC", 1, 1, 3, 5), "MEp13_05"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604018736, ("CSC", 1, 1, 3, 6), "MEp13_06"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604018744, ("CSC", 1, 1, 3, 7), "MEp13_07"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604018752, ("CSC", 1, 1, 3, 8), "MEp13_08"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604018760, ("CSC", 1, 1, 3, 9), "MEp13_09"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604018768, ("CSC", 1, 1, 3, 10), "MEp13_10"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604018776, ("CSC", 1, 1, 3, 11), "MEp13_11"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604018784, ("CSC", 1, 1, 3, 12), "MEp13_12"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604018792, ("CSC", 1, 1, 3, 13), "MEp13_13"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604018800, ("CSC", 1, 1, 3, 14), "MEp13_14"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604018808, ("CSC", 1, 1, 3, 15), "MEp13_15"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604018816, ("CSC", 1, 1, 3, 16), "MEp13_16"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604018824, ("CSC", 1, 1, 3, 17), "MEp13_17"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604018832, ("CSC", 1, 1, 3, 18), "MEp13_18"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604018840, ("CSC", 1, 1, 3, 19), "MEp13_19"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604018848, ("CSC", 1, 1, 3, 20), "MEp13_20"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604018856, ("CSC", 1, 1, 3, 21), "MEp13_21"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604018864, ("CSC", 1, 1, 3, 22), "MEp13_22"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604018872, ("CSC", 1, 1, 3, 23), "MEp13_23"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604018880, ("CSC", 1, 1, 3, 24), "MEp13_24"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604018888, ("CSC", 1, 1, 3, 25), "MEp13_25"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604018896, ("CSC", 1, 1, 3, 26), "MEp13_26"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604018904, ("CSC", 1, 1, 3, 27), "MEp13_27"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604018912, ("CSC", 1, 1, 3, 28), "MEp13_28"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604018920, ("CSC", 1, 1, 3, 29), "MEp13_29"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604018928, ("CSC", 1, 1, 3, 30), "MEp13_30"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604018936, ("CSC", 1, 1, 3, 31), "MEp13_31"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604018944, ("CSC", 1, 1, 3, 32), "MEp13_32"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604018952, ("CSC", 1, 1, 3, 33), "MEp13_33"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604018960, ("CSC", 1, 1, 3, 34), "MEp13_34"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604018968, ("CSC", 1, 1, 3, 35), "MEp13_35"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604018976, ("CSC", 1, 1, 3, 36), "MEp13_36"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604017160, ("CSC", 1, 1, 4, 1), "MEp14_01"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604017176, ("CSC", 1, 1, 4, 3), "MEp14_03"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604017192, ("CSC", 1, 1, 4, 5), "MEp14_05"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604017208, ("CSC", 1, 1, 4, 7), "MEp14_07"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604017224, ("CSC", 1, 1, 4, 9), "MEp14_09"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604017240, ("CSC", 1, 1, 4, 11), "MEp14_11"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604017256, ("CSC", 1, 1, 4, 13), "MEp14_13"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604017272, ("CSC", 1, 1, 4, 15), "MEp14_15"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604017288, ("CSC", 1, 1, 4, 17), "MEp14_17"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604017304, ("CSC", 1, 1, 4, 19), "MEp14_19"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604017320, ("CSC", 1, 1, 4, 21), "MEp14_21"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604017336, ("CSC", 1, 1, 4, 23), "MEp14_23"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604017352, ("CSC", 1, 1, 4, 25), "MEp14_25"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604017368, ("CSC", 1, 1, 4, 27), "MEp14_27"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604017384, ("CSC", 1, 1, 4, 29), "MEp14_29"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604017400, ("CSC", 1, 1, 4, 31), "MEp14_31"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604017416, ("CSC", 1, 1, 4, 33), "MEp14_33"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604017432, ("CSC", 1, 1, 4, 35), "MEp14_35"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604017168, ("CSC", 1, 1, 4, 2), "MEp14_02"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604017184, ("CSC", 1, 1, 4, 4), "MEp14_04"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604017200, ("CSC", 1, 1, 4, 6), "MEp14_06"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604017216, ("CSC", 1, 1, 4, 8), "MEp14_08"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604017232, ("CSC", 1, 1, 4, 10), "MEp14_10"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604017248, ("CSC", 1, 1, 4, 12), "MEp14_12"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604017264, ("CSC", 1, 1, 4, 14), "MEp14_14"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604017280, ("CSC", 1, 1, 4, 16), "MEp14_16"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604017296, ("CSC", 1, 1, 4, 18), "MEp14_18"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604017312, ("CSC", 1, 1, 4, 20), "MEp14_20"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604017328, ("CSC", 1, 1, 4, 22), "MEp14_22"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604017344, ("CSC", 1, 1, 4, 24), "MEp14_24"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604017360, ("CSC", 1, 1, 4, 26), "MEp14_26"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604017376, ("CSC", 1, 1, 4, 28), "MEp14_28"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604017392, ("CSC", 1, 1, 4, 30), "MEp14_30"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604017408, ("CSC", 1, 1, 4, 32), "MEp14_32"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604017424, ("CSC", 1, 1, 4, 34), "MEp14_34"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604017440, ("CSC", 1, 1, 4, 36), "MEp14_36"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604021256, ("CSC", 1, 2, 1, 1), "MEp21_01"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604021272, ("CSC", 1, 2, 1, 3), "MEp21_03"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604021288, ("CSC", 1, 2, 1, 5), "MEp21_05"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604021304, ("CSC", 1, 2, 1, 7), "MEp21_07"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604021320, ("CSC", 1, 2, 1, 9), "MEp21_09"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604021336, ("CSC", 1, 2, 1, 11), "MEp21_11"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604021352, ("CSC", 1, 2, 1, 13), "MEp21_13"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604021368, ("CSC", 1, 2, 1, 15), "MEp21_15"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604021384, ("CSC", 1, 2, 1, 17), "MEp21_17"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604021264, ("CSC", 1, 2, 1, 2), "MEp21_02"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604021280, ("CSC", 1, 2, 1, 4), "MEp21_04"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604021296, ("CSC", 1, 2, 1, 6), "MEp21_06"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604021312, ("CSC", 1, 2, 1, 8), "MEp21_08"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604021328, ("CSC", 1, 2, 1, 10), "MEp21_10"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604021344, ("CSC", 1, 2, 1, 12), "MEp21_12"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604021360, ("CSC", 1, 2, 1, 14), "MEp21_14"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604021376, ("CSC", 1, 2, 1, 16), "MEp21_16"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604021392, ("CSC", 1, 2, 1, 18), "MEp21_18"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604021768, ("CSC", 1, 2, 2, 1), "MEp22_01"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604021784, ("CSC", 1, 2, 2, 3), "MEp22_03"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604021800, ("CSC", 1, 2, 2, 5), "MEp22_05"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604021816, ("CSC", 1, 2, 2, 7), "MEp22_07"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604021832, ("CSC", 1, 2, 2, 9), "MEp22_09"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604021848, ("CSC", 1, 2, 2, 11), "MEp22_11"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604021864, ("CSC", 1, 2, 2, 13), "MEp22_13"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604021880, ("CSC", 1, 2, 2, 15), "MEp22_15"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604021896, ("CSC", 1, 2, 2, 17), "MEp22_17"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604021912, ("CSC", 1, 2, 2, 19), "MEp22_19"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604021928, ("CSC", 1, 2, 2, 21), "MEp22_21"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604021944, ("CSC", 1, 2, 2, 23), "MEp22_23"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604021960, ("CSC", 1, 2, 2, 25), "MEp22_25"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604021976, ("CSC", 1, 2, 2, 27), "MEp22_27"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604021992, ("CSC", 1, 2, 2, 29), "MEp22_29"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604022008, ("CSC", 1, 2, 2, 31), "MEp22_31"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604022024, ("CSC", 1, 2, 2, 33), "MEp22_33"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604022040, ("CSC", 1, 2, 2, 35), "MEp22_35"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604021776, ("CSC", 1, 2, 2, 2), "MEp22_02"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604021792, ("CSC", 1, 2, 2, 4), "MEp22_04"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604021808, ("CSC", 1, 2, 2, 6), "MEp22_06"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604021824, ("CSC", 1, 2, 2, 8), "MEp22_08"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604021840, ("CSC", 1, 2, 2, 10), "MEp22_10"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604021856, ("CSC", 1, 2, 2, 12), "MEp22_12"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604021872, ("CSC", 1, 2, 2, 14), "MEp22_14"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604021888, ("CSC", 1, 2, 2, 16), "MEp22_16"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604021904, ("CSC", 1, 2, 2, 18), "MEp22_18"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604021920, ("CSC", 1, 2, 2, 20), "MEp22_20"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604021936, ("CSC", 1, 2, 2, 22), "MEp22_22"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604021952, ("CSC", 1, 2, 2, 24), "MEp22_24"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604021968, ("CSC", 1, 2, 2, 26), "MEp22_26"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604021984, ("CSC", 1, 2, 2, 28), "MEp22_28"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604022000, ("CSC", 1, 2, 2, 30), "MEp22_30"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604022016, ("CSC", 1, 2, 2, 32), "MEp22_32"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604022032, ("CSC", 1, 2, 2, 34), "MEp22_34"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604022048, ("CSC", 1, 2, 2, 36), "MEp22_36"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604025352, ("CSC", 1, 3, 1, 1), "MEp31_01"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604025368, ("CSC", 1, 3, 1, 3), "MEp31_03"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604025384, ("CSC", 1, 3, 1, 5), "MEp31_05"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604025400, ("CSC", 1, 3, 1, 7), "MEp31_07"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604025416, ("CSC", 1, 3, 1, 9), "MEp31_09"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604025432, ("CSC", 1, 3, 1, 11), "MEp31_11"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604025448, ("CSC", 1, 3, 1, 13), "MEp31_13"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604025464, ("CSC", 1, 3, 1, 15), "MEp31_15"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604025480, ("CSC", 1, 3, 1, 17), "MEp31_17"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604025360, ("CSC", 1, 3, 1, 2), "MEp31_02"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604025376, ("CSC", 1, 3, 1, 4), "MEp31_04"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604025392, ("CSC", 1, 3, 1, 6), "MEp31_06"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604025408, ("CSC", 1, 3, 1, 8), "MEp31_08"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604025424, ("CSC", 1, 3, 1, 10), "MEp31_10"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604025440, ("CSC", 1, 3, 1, 12), "MEp31_12"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604025456, ("CSC", 1, 3, 1, 14), "MEp31_14"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604025472, ("CSC", 1, 3, 1, 16), "MEp31_16"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604025488, ("CSC", 1, 3, 1, 18), "MEp31_18"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604025864, ("CSC", 1, 3, 2, 1), "MEp32_01"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604025880, ("CSC", 1, 3, 2, 3), "MEp32_03"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604025896, ("CSC", 1, 3, 2, 5), "MEp32_05"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604025912, ("CSC", 1, 3, 2, 7), "MEp32_07"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604025928, ("CSC", 1, 3, 2, 9), "MEp32_09"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604025944, ("CSC", 1, 3, 2, 11), "MEp32_11"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604025960, ("CSC", 1, 3, 2, 13), "MEp32_13"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604025976, ("CSC", 1, 3, 2, 15), "MEp32_15"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604025992, ("CSC", 1, 3, 2, 17), "MEp32_17"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604026008, ("CSC", 1, 3, 2, 19), "MEp32_19"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604026024, ("CSC", 1, 3, 2, 21), "MEp32_21"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604026040, ("CSC", 1, 3, 2, 23), "MEp32_23"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604026056, ("CSC", 1, 3, 2, 25), "MEp32_25"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604026072, ("CSC", 1, 3, 2, 27), "MEp32_27"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604026088, ("CSC", 1, 3, 2, 29), "MEp32_29"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604026104, ("CSC", 1, 3, 2, 31), "MEp32_31"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604026120, ("CSC", 1, 3, 2, 33), "MEp32_33"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604026136, ("CSC", 1, 3, 2, 35), "MEp32_35"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604025872, ("CSC", 1, 3, 2, 2), "MEp32_02"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604025888, ("CSC", 1, 3, 2, 4), "MEp32_04"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604025904, ("CSC", 1, 3, 2, 6), "MEp32_06"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604025920, ("CSC", 1, 3, 2, 8), "MEp32_08"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604025936, ("CSC", 1, 3, 2, 10), "MEp32_10"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604025952, ("CSC", 1, 3, 2, 12), "MEp32_12"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604025968, ("CSC", 1, 3, 2, 14), "MEp32_14"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604025984, ("CSC", 1, 3, 2, 16), "MEp32_16"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604026000, ("CSC", 1, 3, 2, 18), "MEp32_18"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604026016, ("CSC", 1, 3, 2, 20), "MEp32_20"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604026032, ("CSC", 1, 3, 2, 22), "MEp32_22"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604026048, ("CSC", 1, 3, 2, 24), "MEp32_24"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604026064, ("CSC", 1, 3, 2, 26), "MEp32_26"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604026080, ("CSC", 1, 3, 2, 28), "MEp32_28"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604026096, ("CSC", 1, 3, 2, 30), "MEp32_30"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604026112, ("CSC", 1, 3, 2, 32), "MEp32_32"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604026128, ("CSC", 1, 3, 2, 34), "MEp32_34"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604026144, ("CSC", 1, 3, 2, 36), "MEp32_36"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604029448, ("CSC", 1, 4, 1, 1), "MEp41_01"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604029464, ("CSC", 1, 4, 1, 3), "MEp41_03"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604029480, ("CSC", 1, 4, 1, 5), "MEp41_05"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604029496, ("CSC", 1, 4, 1, 7), "MEp41_07"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604029512, ("CSC", 1, 4, 1, 9), "MEp41_09"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604029528, ("CSC", 1, 4, 1, 11), "MEp41_11"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604029544, ("CSC", 1, 4, 1, 13), "MEp41_13"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604029560, ("CSC", 1, 4, 1, 15), "MEp41_15"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604029576, ("CSC", 1, 4, 1, 17), "MEp41_17"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604029456, ("CSC", 1, 4, 1, 2), "MEp41_02"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604029472, ("CSC", 1, 4, 1, 4), "MEp41_04"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604029488, ("CSC", 1, 4, 1, 6), "MEp41_06"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604029504, ("CSC", 1, 4, 1, 8), "MEp41_08"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604029520, ("CSC", 1, 4, 1, 10), "MEp41_10"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604029536, ("CSC", 1, 4, 1, 12), "MEp41_12"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604029552, ("CSC", 1, 4, 1, 14), "MEp41_14"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604029568, ("CSC", 1, 4, 1, 16), "MEp41_16"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604029584, ("CSC", 1, 4, 1, 18), "MEp41_18"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604029960, ("CSC", 1, 4, 2, 1), "MEp42_01"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604029976, ("CSC", 1, 4, 2, 3), "MEp42_03"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604029992, ("CSC", 1, 4, 2, 5), "MEp42_05"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604030008, ("CSC", 1, 4, 2, 7), "MEp42_07"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604030024, ("CSC", 1, 4, 2, 9), "MEp42_09"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604030040, ("CSC", 1, 4, 2, 11), "MEp42_11"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604030056, ("CSC", 1, 4, 2, 13), "MEp42_13"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604030072, ("CSC", 1, 4, 2, 15), "MEp42_15"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604030088, ("CSC", 1, 4, 2, 17), "MEp42_17"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604030104, ("CSC", 1, 4, 2, 19), "MEp42_19"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604030120, ("CSC", 1, 4, 2, 21), "MEp42_21"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604030136, ("CSC", 1, 4, 2, 23), "MEp42_23"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604030152, ("CSC", 1, 4, 2, 25), "MEp42_25"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604030168, ("CSC", 1, 4, 2, 27), "MEp42_27"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604030184, ("CSC", 1, 4, 2, 29), "MEp42_29"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604030200, ("CSC", 1, 4, 2, 31), "MEp42_31"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604030216, ("CSC", 1, 4, 2, 33), "MEp42_33"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604030232, ("CSC", 1, 4, 2, 35), "MEp42_35"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604029968, ("CSC", 1, 4, 2, 2), "MEp42_02"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604029984, ("CSC", 1, 4, 2, 4), "MEp42_04"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604030000, ("CSC", 1, 4, 2, 6), "MEp42_06"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604030016, ("CSC", 1, 4, 2, 8), "MEp42_08"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604030032, ("CSC", 1, 4, 2, 10), "MEp42_10"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604030048, ("CSC", 1, 4, 2, 12), "MEp42_12"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604030064, ("CSC", 1, 4, 2, 14), "MEp42_14"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604030080, ("CSC", 1, 4, 2, 16), "MEp42_16"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604030096, ("CSC", 1, 4, 2, 18), "MEp42_18"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604030112, ("CSC", 1, 4, 2, 20), "MEp42_20"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604030128, ("CSC", 1, 4, 2, 22), "MEp42_22"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604030144, ("CSC", 1, 4, 2, 24), "MEp42_24"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604030160, ("CSC", 1, 4, 2, 26), "MEp42_26"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604030176, ("CSC", 1, 4, 2, 28), "MEp42_28"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604030192, ("CSC", 1, 4, 2, 30), "MEp42_30"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604030208, ("CSC", 1, 4, 2, 32), "MEp42_32"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604030224, ("CSC", 1, 4, 2, 34), "MEp42_34"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604030240, ("CSC", 1, 4, 2, 36), "MEp42_36"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604050440, ("CSC", 2, 1, 1, 1), "MEm11_01"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604050456, ("CSC", 2, 1, 1, 3), "MEm11_03"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604050472, ("CSC", 2, 1, 1, 5), "MEm11_05"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604050488, ("CSC", 2, 1, 1, 7), "MEm11_07"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604050504, ("CSC", 2, 1, 1, 9), "MEm11_09"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604050520, ("CSC", 2, 1, 1, 11), "MEm11_11"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604050536, ("CSC", 2, 1, 1, 13), "MEm11_13"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604050552, ("CSC", 2, 1, 1, 15), "MEm11_15"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604050568, ("CSC", 2, 1, 1, 17), "MEm11_17"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604050584, ("CSC", 2, 1, 1, 19), "MEm11_19"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604050600, ("CSC", 2, 1, 1, 21), "MEm11_21"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604050616, ("CSC", 2, 1, 1, 23), "MEm11_23"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604050632, ("CSC", 2, 1, 1, 25), "MEm11_25"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604050648, ("CSC", 2, 1, 1, 27), "MEm11_27"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604050664, ("CSC", 2, 1, 1, 29), "MEm11_29"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604050680, ("CSC", 2, 1, 1, 31), "MEm11_31"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604050696, ("CSC", 2, 1, 1, 33), "MEm11_33"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604050712, ("CSC", 2, 1, 1, 35), "MEm11_35"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604050448, ("CSC", 2, 1, 1, 2), "MEm11_02"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604050464, ("CSC", 2, 1, 1, 4), "MEm11_04"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604050480, ("CSC", 2, 1, 1, 6), "MEm11_06"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604050496, ("CSC", 2, 1, 1, 8), "MEm11_08"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604050512, ("CSC", 2, 1, 1, 10), "MEm11_10"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604050528, ("CSC", 2, 1, 1, 12), "MEm11_12"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604050544, ("CSC", 2, 1, 1, 14), "MEm11_14"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604050560, ("CSC", 2, 1, 1, 16), "MEm11_16"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604050576, ("CSC", 2, 1, 1, 18), "MEm11_18"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604050592, ("CSC", 2, 1, 1, 20), "MEm11_20"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604050608, ("CSC", 2, 1, 1, 22), "MEm11_22"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604050624, ("CSC", 2, 1, 1, 24), "MEm11_24"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604050640, ("CSC", 2, 1, 1, 26), "MEm11_26"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604050656, ("CSC", 2, 1, 1, 28), "MEm11_28"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604050672, ("CSC", 2, 1, 1, 30), "MEm11_30"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604050688, ("CSC", 2, 1, 1, 32), "MEm11_32"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604050704, ("CSC", 2, 1, 1, 34), "MEm11_34"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604050720, ("CSC", 2, 1, 1, 36), "MEm11_36"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604050952, ("CSC", 2, 1, 2, 1), "MEm12_01"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604050968, ("CSC", 2, 1, 2, 3), "MEm12_03"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604050984, ("CSC", 2, 1, 2, 5), "MEm12_05"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604051000, ("CSC", 2, 1, 2, 7), "MEm12_07"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604051016, ("CSC", 2, 1, 2, 9), "MEm12_09"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604051032, ("CSC", 2, 1, 2, 11), "MEm12_11"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604051048, ("CSC", 2, 1, 2, 13), "MEm12_13"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604051064, ("CSC", 2, 1, 2, 15), "MEm12_15"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604051080, ("CSC", 2, 1, 2, 17), "MEm12_17"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604051096, ("CSC", 2, 1, 2, 19), "MEm12_19"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604051112, ("CSC", 2, 1, 2, 21), "MEm12_21"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604051128, ("CSC", 2, 1, 2, 23), "MEm12_23"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604051144, ("CSC", 2, 1, 2, 25), "MEm12_25"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604051160, ("CSC", 2, 1, 2, 27), "MEm12_27"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604051176, ("CSC", 2, 1, 2, 29), "MEm12_29"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604051192, ("CSC", 2, 1, 2, 31), "MEm12_31"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604051208, ("CSC", 2, 1, 2, 33), "MEm12_33"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604051224, ("CSC", 2, 1, 2, 35), "MEm12_35"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604050960, ("CSC", 2, 1, 2, 2), "MEm12_02"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604050976, ("CSC", 2, 1, 2, 4), "MEm12_04"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604050992, ("CSC", 2, 1, 2, 6), "MEm12_06"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604051008, ("CSC", 2, 1, 2, 8), "MEm12_08"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604051024, ("CSC", 2, 1, 2, 10), "MEm12_10"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604051040, ("CSC", 2, 1, 2, 12), "MEm12_12"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604051056, ("CSC", 2, 1, 2, 14), "MEm12_14"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604051072, ("CSC", 2, 1, 2, 16), "MEm12_16"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604051088, ("CSC", 2, 1, 2, 18), "MEm12_18"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604051104, ("CSC", 2, 1, 2, 20), "MEm12_20"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604051120, ("CSC", 2, 1, 2, 22), "MEm12_22"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604051136, ("CSC", 2, 1, 2, 24), "MEm12_24"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604051152, ("CSC", 2, 1, 2, 26), "MEm12_26"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604051168, ("CSC", 2, 1, 2, 28), "MEm12_28"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604051184, ("CSC", 2, 1, 2, 30), "MEm12_30"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604051200, ("CSC", 2, 1, 2, 32), "MEm12_32"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604051216, ("CSC", 2, 1, 2, 34), "MEm12_34"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604051232, ("CSC", 2, 1, 2, 36), "MEm12_36"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604051464, ("CSC", 2, 1, 3, 1), "MEm13_01"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604051472, ("CSC", 2, 1, 3, 2), "MEm13_02"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604051480, ("CSC", 2, 1, 3, 3), "MEm13_03"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604051488, ("CSC", 2, 1, 3, 4), "MEm13_04"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604051496, ("CSC", 2, 1, 3, 5), "MEm13_05"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604051504, ("CSC", 2, 1, 3, 6), "MEm13_06"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604051512, ("CSC", 2, 1, 3, 7), "MEm13_07"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604051520, ("CSC", 2, 1, 3, 8), "MEm13_08"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604051528, ("CSC", 2, 1, 3, 9), "MEm13_09"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604051536, ("CSC", 2, 1, 3, 10), "MEm13_10"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604051544, ("CSC", 2, 1, 3, 11), "MEm13_11"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604051552, ("CSC", 2, 1, 3, 12), "MEm13_12"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604051560, ("CSC", 2, 1, 3, 13), "MEm13_13"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604051568, ("CSC", 2, 1, 3, 14), "MEm13_14"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604051576, ("CSC", 2, 1, 3, 15), "MEm13_15"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604051584, ("CSC", 2, 1, 3, 16), "MEm13_16"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604051592, ("CSC", 2, 1, 3, 17), "MEm13_17"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604051600, ("CSC", 2, 1, 3, 18), "MEm13_18"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604051608, ("CSC", 2, 1, 3, 19), "MEm13_19"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604051616, ("CSC", 2, 1, 3, 20), "MEm13_20"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604051624, ("CSC", 2, 1, 3, 21), "MEm13_21"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604051632, ("CSC", 2, 1, 3, 22), "MEm13_22"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604051640, ("CSC", 2, 1, 3, 23), "MEm13_23"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604051648, ("CSC", 2, 1, 3, 24), "MEm13_24"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604051656, ("CSC", 2, 1, 3, 25), "MEm13_25"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604051664, ("CSC", 2, 1, 3, 26), "MEm13_26"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604051672, ("CSC", 2, 1, 3, 27), "MEm13_27"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604051680, ("CSC", 2, 1, 3, 28), "MEm13_28"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604051688, ("CSC", 2, 1, 3, 29), "MEm13_29"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604051696, ("CSC", 2, 1, 3, 30), "MEm13_30"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604051704, ("CSC", 2, 1, 3, 31), "MEm13_31"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604051712, ("CSC", 2, 1, 3, 32), "MEm13_32"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604051720, ("CSC", 2, 1, 3, 33), "MEm13_33"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604051728, ("CSC", 2, 1, 3, 34), "MEm13_34"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604051736, ("CSC", 2, 1, 3, 35), "MEm13_35"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604051744, ("CSC", 2, 1, 3, 36), "MEm13_36"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604049928, ("CSC", 2, 1, 4, 1), "MEm14_01"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604049944, ("CSC", 2, 1, 4, 3), "MEm14_03"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604049960, ("CSC", 2, 1, 4, 5), "MEm14_05"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604049976, ("CSC", 2, 1, 4, 7), "MEm14_07"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604049992, ("CSC", 2, 1, 4, 9), "MEm14_09"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604050008, ("CSC", 2, 1, 4, 11), "MEm14_11"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604050024, ("CSC", 2, 1, 4, 13), "MEm14_13"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604050040, ("CSC", 2, 1, 4, 15), "MEm14_15"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604050056, ("CSC", 2, 1, 4, 17), "MEm14_17"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604050072, ("CSC", 2, 1, 4, 19), "MEm14_19"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604050088, ("CSC", 2, 1, 4, 21), "MEm14_21"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604050104, ("CSC", 2, 1, 4, 23), "MEm14_23"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604050120, ("CSC", 2, 1, 4, 25), "MEm14_25"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604050136, ("CSC", 2, 1, 4, 27), "MEm14_27"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604050152, ("CSC", 2, 1, 4, 29), "MEm14_29"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604050168, ("CSC", 2, 1, 4, 31), "MEm14_31"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604050184, ("CSC", 2, 1, 4, 33), "MEm14_33"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604050200, ("CSC", 2, 1, 4, 35), "MEm14_35"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604049936, ("CSC", 2, 1, 4, 2), "MEm14_02"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604049952, ("CSC", 2, 1, 4, 4), "MEm14_04"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604049968, ("CSC", 2, 1, 4, 6), "MEm14_06"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604049984, ("CSC", 2, 1, 4, 8), "MEm14_08"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604050000, ("CSC", 2, 1, 4, 10), "MEm14_10"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604050016, ("CSC", 2, 1, 4, 12), "MEm14_12"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604050032, ("CSC", 2, 1, 4, 14), "MEm14_14"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604050048, ("CSC", 2, 1, 4, 16), "MEm14_16"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604050064, ("CSC", 2, 1, 4, 18), "MEm14_18"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604050080, ("CSC", 2, 1, 4, 20), "MEm14_20"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604050096, ("CSC", 2, 1, 4, 22), "MEm14_22"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604050112, ("CSC", 2, 1, 4, 24), "MEm14_24"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604050128, ("CSC", 2, 1, 4, 26), "MEm14_26"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604050144, ("CSC", 2, 1, 4, 28), "MEm14_28"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604050160, ("CSC", 2, 1, 4, 30), "MEm14_30"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604050176, ("CSC", 2, 1, 4, 32), "MEm14_32"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604050192, ("CSC", 2, 1, 4, 34), "MEm14_34"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604050208, ("CSC", 2, 1, 4, 36), "MEm14_36"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604054024, ("CSC", 2, 2, 1, 1), "MEm21_01"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604054040, ("CSC", 2, 2, 1, 3), "MEm21_03"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604054056, ("CSC", 2, 2, 1, 5), "MEm21_05"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604054072, ("CSC", 2, 2, 1, 7), "MEm21_07"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604054088, ("CSC", 2, 2, 1, 9), "MEm21_09"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604054104, ("CSC", 2, 2, 1, 11), "MEm21_11"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604054120, ("CSC", 2, 2, 1, 13), "MEm21_13"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604054136, ("CSC", 2, 2, 1, 15), "MEm21_15"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604054152, ("CSC", 2, 2, 1, 17), "MEm21_17"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604054032, ("CSC", 2, 2, 1, 2), "MEm21_02"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604054048, ("CSC", 2, 2, 1, 4), "MEm21_04"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604054064, ("CSC", 2, 2, 1, 6), "MEm21_06"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604054080, ("CSC", 2, 2, 1, 8), "MEm21_08"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604054096, ("CSC", 2, 2, 1, 10), "MEm21_10"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604054112, ("CSC", 2, 2, 1, 12), "MEm21_12"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604054128, ("CSC", 2, 2, 1, 14), "MEm21_14"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604054144, ("CSC", 2, 2, 1, 16), "MEm21_16"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604054160, ("CSC", 2, 2, 1, 18), "MEm21_18"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604054536, ("CSC", 2, 2, 2, 1), "MEm22_01"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604054552, ("CSC", 2, 2, 2, 3), "MEm22_03"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604054568, ("CSC", 2, 2, 2, 5), "MEm22_05"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604054584, ("CSC", 2, 2, 2, 7), "MEm22_07"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604054600, ("CSC", 2, 2, 2, 9), "MEm22_09"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604054616, ("CSC", 2, 2, 2, 11), "MEm22_11"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604054632, ("CSC", 2, 2, 2, 13), "MEm22_13"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604054648, ("CSC", 2, 2, 2, 15), "MEm22_15"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604054664, ("CSC", 2, 2, 2, 17), "MEm22_17"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604054680, ("CSC", 2, 2, 2, 19), "MEm22_19"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604054696, ("CSC", 2, 2, 2, 21), "MEm22_21"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604054712, ("CSC", 2, 2, 2, 23), "MEm22_23"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604054728, ("CSC", 2, 2, 2, 25), "MEm22_25"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604054744, ("CSC", 2, 2, 2, 27), "MEm22_27"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604054760, ("CSC", 2, 2, 2, 29), "MEm22_29"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604054776, ("CSC", 2, 2, 2, 31), "MEm22_31"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604054792, ("CSC", 2, 2, 2, 33), "MEm22_33"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604054808, ("CSC", 2, 2, 2, 35), "MEm22_35"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604054544, ("CSC", 2, 2, 2, 2), "MEm22_02"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604054560, ("CSC", 2, 2, 2, 4), "MEm22_04"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604054576, ("CSC", 2, 2, 2, 6), "MEm22_06"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604054592, ("CSC", 2, 2, 2, 8), "MEm22_08"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604054608, ("CSC", 2, 2, 2, 10), "MEm22_10"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604054624, ("CSC", 2, 2, 2, 12), "MEm22_12"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604054640, ("CSC", 2, 2, 2, 14), "MEm22_14"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604054656, ("CSC", 2, 2, 2, 16), "MEm22_16"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604054672, ("CSC", 2, 2, 2, 18), "MEm22_18"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604054688, ("CSC", 2, 2, 2, 20), "MEm22_20"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604054704, ("CSC", 2, 2, 2, 22), "MEm22_22"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604054720, ("CSC", 2, 2, 2, 24), "MEm22_24"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604054736, ("CSC", 2, 2, 2, 26), "MEm22_26"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604054752, ("CSC", 2, 2, 2, 28), "MEm22_28"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604054768, ("CSC", 2, 2, 2, 30), "MEm22_30"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604054784, ("CSC", 2, 2, 2, 32), "MEm22_32"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604054800, ("CSC", 2, 2, 2, 34), "MEm22_34"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604054816, ("CSC", 2, 2, 2, 36), "MEm22_36"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604058120, ("CSC", 2, 3, 1, 1), "MEm31_01"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604058136, ("CSC", 2, 3, 1, 3), "MEm31_03"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604058152, ("CSC", 2, 3, 1, 5), "MEm31_05"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604058168, ("CSC", 2, 3, 1, 7), "MEm31_07"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604058184, ("CSC", 2, 3, 1, 9), "MEm31_09"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604058200, ("CSC", 2, 3, 1, 11), "MEm31_11"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604058216, ("CSC", 2, 3, 1, 13), "MEm31_13"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604058232, ("CSC", 2, 3, 1, 15), "MEm31_15"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604058248, ("CSC", 2, 3, 1, 17), "MEm31_17"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604058128, ("CSC", 2, 3, 1, 2), "MEm31_02"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604058144, ("CSC", 2, 3, 1, 4), "MEm31_04"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604058160, ("CSC", 2, 3, 1, 6), "MEm31_06"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604058176, ("CSC", 2, 3, 1, 8), "MEm31_08"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604058192, ("CSC", 2, 3, 1, 10), "MEm31_10"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604058208, ("CSC", 2, 3, 1, 12), "MEm31_12"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604058224, ("CSC", 2, 3, 1, 14), "MEm31_14"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604058240, ("CSC", 2, 3, 1, 16), "MEm31_16"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604058256, ("CSC", 2, 3, 1, 18), "MEm31_18"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604058632, ("CSC", 2, 3, 2, 1), "MEm32_01"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604058648, ("CSC", 2, 3, 2, 3), "MEm32_03"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604058664, ("CSC", 2, 3, 2, 5), "MEm32_05"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604058680, ("CSC", 2, 3, 2, 7), "MEm32_07"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604058696, ("CSC", 2, 3, 2, 9), "MEm32_09"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604058712, ("CSC", 2, 3, 2, 11), "MEm32_11"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604058728, ("CSC", 2, 3, 2, 13), "MEm32_13"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604058744, ("CSC", 2, 3, 2, 15), "MEm32_15"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604058760, ("CSC", 2, 3, 2, 17), "MEm32_17"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604058776, ("CSC", 2, 3, 2, 19), "MEm32_19"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604058792, ("CSC", 2, 3, 2, 21), "MEm32_21"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604058808, ("CSC", 2, 3, 2, 23), "MEm32_23"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604058824, ("CSC", 2, 3, 2, 25), "MEm32_25"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604058840, ("CSC", 2, 3, 2, 27), "MEm32_27"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604058856, ("CSC", 2, 3, 2, 29), "MEm32_29"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604058872, ("CSC", 2, 3, 2, 31), "MEm32_31"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604058888, ("CSC", 2, 3, 2, 33), "MEm32_33"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604058904, ("CSC", 2, 3, 2, 35), "MEm32_35"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604058640, ("CSC", 2, 3, 2, 2), "MEm32_02"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604058656, ("CSC", 2, 3, 2, 4), "MEm32_04"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604058672, ("CSC", 2, 3, 2, 6), "MEm32_06"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604058688, ("CSC", 2, 3, 2, 8), "MEm32_08"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604058704, ("CSC", 2, 3, 2, 10), "MEm32_10"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604058720, ("CSC", 2, 3, 2, 12), "MEm32_12"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604058736, ("CSC", 2, 3, 2, 14), "MEm32_14"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604058752, ("CSC", 2, 3, 2, 16), "MEm32_16"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604058768, ("CSC", 2, 3, 2, 18), "MEm32_18"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604058784, ("CSC", 2, 3, 2, 20), "MEm32_20"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604058800, ("CSC", 2, 3, 2, 22), "MEm32_22"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604058816, ("CSC", 2, 3, 2, 24), "MEm32_24"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604058832, ("CSC", 2, 3, 2, 26), "MEm32_26"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604058848, ("CSC", 2, 3, 2, 28), "MEm32_28"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604058864, ("CSC", 2, 3, 2, 30), "MEm32_30"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604058880, ("CSC", 2, 3, 2, 32), "MEm32_32"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604058896, ("CSC", 2, 3, 2, 34), "MEm32_34"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604058912, ("CSC", 2, 3, 2, 36), "MEm32_36"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604062216, ("CSC", 2, 4, 1, 1), "MEm41_01"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604062232, ("CSC", 2, 4, 1, 3), "MEm41_03"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604062248, ("CSC", 2, 4, 1, 5), "MEm41_05"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604062264, ("CSC", 2, 4, 1, 7), "MEm41_07"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604062280, ("CSC", 2, 4, 1, 9), "MEm41_09"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604062296, ("CSC", 2, 4, 1, 11), "MEm41_11"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604062312, ("CSC", 2, 4, 1, 13), "MEm41_13"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604062328, ("CSC", 2, 4, 1, 15), "MEm41_15"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604062344, ("CSC", 2, 4, 1, 17), "MEm41_17"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604062224, ("CSC", 2, 4, 1, 2), "MEm41_02"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604062240, ("CSC", 2, 4, 1, 4), "MEm41_04"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604062256, ("CSC", 2, 4, 1, 6), "MEm41_06"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604062272, ("CSC", 2, 4, 1, 8), "MEm41_08"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604062288, ("CSC", 2, 4, 1, 10), "MEm41_10"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604062304, ("CSC", 2, 4, 1, 12), "MEm41_12"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604062320, ("CSC", 2, 4, 1, 14), "MEm41_14"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604062336, ("CSC", 2, 4, 1, 16), "MEm41_16"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604062352, ("CSC", 2, 4, 1, 18), "MEm41_18"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604062728, ("CSC", 2, 4, 2, 1), "MEm42_01"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604062744, ("CSC", 2, 4, 2, 3), "MEm42_03"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604062760, ("CSC", 2, 4, 2, 5), "MEm42_05"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604062776, ("CSC", 2, 4, 2, 7), "MEm42_07"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604062792, ("CSC", 2, 4, 2, 9), "MEm42_09"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604062808, ("CSC", 2, 4, 2, 11), "MEm42_11"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604062824, ("CSC", 2, 4, 2, 13), "MEm42_13"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604062840, ("CSC", 2, 4, 2, 15), "MEm42_15"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604062856, ("CSC", 2, 4, 2, 17), "MEm42_17"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604062872, ("CSC", 2, 4, 2, 19), "MEm42_19"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604062888, ("CSC", 2, 4, 2, 21), "MEm42_21"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604062904, ("CSC", 2, 4, 2, 23), "MEm42_23"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604062920, ("CSC", 2, 4, 2, 25), "MEm42_25"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604062936, ("CSC", 2, 4, 2, 27), "MEm42_27"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604062952, ("CSC", 2, 4, 2, 29), "MEm42_29"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604062968, ("CSC", 2, 4, 2, 31), "MEm42_31"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604062984, ("CSC", 2, 4, 2, 33), "MEm42_33"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604063000, ("CSC", 2, 4, 2, 35), "MEm42_35"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604062736, ("CSC", 2, 4, 2, 2), "MEm42_02"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604062752, ("CSC", 2, 4, 2, 4), "MEm42_04"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604062768, ("CSC", 2, 4, 2, 6), "MEm42_06"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604062784, ("CSC", 2, 4, 2, 8), "MEm42_08"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604062800, ("CSC", 2, 4, 2, 10), "MEm42_10"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604062816, ("CSC", 2, 4, 2, 12), "MEm42_12"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604062832, ("CSC", 2, 4, 2, 14), "MEm42_14"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604062848, ("CSC", 2, 4, 2, 16), "MEm42_16"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604062864, ("CSC", 2, 4, 2, 18), "MEm42_18"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604062880, ("CSC", 2, 4, 2, 20), "MEm42_20"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604062896, ("CSC", 2, 4, 2, 22), "MEm42_22"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604062912, ("CSC", 2, 4, 2, 24), "MEm42_24"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604062928, ("CSC", 2, 4, 2, 26), "MEm42_26"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604062944, ("CSC", 2, 4, 2, 28), "MEm42_28"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604062960, ("CSC", 2, 4, 2, 30), "MEm42_30"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604062976, ("CSC", 2, 4, 2, 32), "MEm42_32"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604062992, ("CSC", 2, 4, 2, 34), "MEm42_34"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604063008, ("CSC", 2, 4, 2, 36), "MEm42_36"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

