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
reports[-1].posNum = 69615
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000246734, 0.00319735, 0), \
                           ValErr(0.000650947, 0.00467422, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.46683e-05, 5.43339e-05, 0), \
                           -198476, 69615, 69615, -nan)
reports[-1].sigmax = ValErr(0.822092, 0.0022032, 0)
reports[-1].sigmay = ValErr(1.23255, 0.00330324, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00132274, 0.00215296, 0.000293739, -0.00172861, 5.35468e-05, 0.000693926, 0.000308395, -0.000229028, 5.35468e-05, 0.000693926, 0.000308395, -0.000229028, 0.00447239, 0.00458896, 0.000289453, -0.000431035, 0.00447239, 0.00458896, 0.000289453, -0.000431035, 0.822091, 1.23255, 0.00410117, 0.0287355, 0.822091, 1.23255, 0.00410117, 0.0287355)

reports.append(Report(575176704, ("DT", -2, 1, 2), "MBwhAst1sec02"))
reports[-1].posNum = 67200
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000224407, 0.0032846, 0), \
                           ValErr(-0.000436972, 0.00470913, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.02024e-06, 5.53963e-05, 0), \
                           -191260, 67200, 67200, -nan)
reports[-1].sigmax = ValErr(0.826003, 0.00225318, 0)
reports[-1].sigmay = ValErr(1.22068, 0.0033298, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00338955, 0.00159359, 0.000961839, -0.00197162, 0.000195151, -0.000439613, 0.000966565, -0.000593585, 0.000195151, -0.000439613, 0.000966565, -0.000593585, -0.00119307, -0.00310888, 0.000975571, -0.000836544, -0.00119307, -0.00310888, 0.000975571, -0.000836544, 0.826002, 1.22068, 0.0041077, 0.0287434, 0.826002, 1.22068, 0.0041077, 0.0287434)

reports.append(Report(575438848, ("DT", -2, 1, 3), "MBwhAst1sec03"))
reports[-1].posNum = 65171
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000257331, 0.00331947, 0), \
                           ValErr(-0.000317661, 0.00478338, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.04102e-05, 5.62196e-05, 0), \
                           -184553, 65171, 65171, -nan)
reports[-1].sigmax = ValErr(0.814434, 0.00225588, 0)
reports[-1].sigmay = ValErr(1.22044, 0.00338047, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00454046, 0.00395204, 0.000514478, -0.00222451, 8.74007e-05, -0.000287135, 0.000505074, -0.000689714, 8.74007e-05, -0.000287135, 0.000505074, -0.000689714, 0.00239869, 0.00184568, 0.000491138, -0.000938778, 0.00239869, 0.00184568, 0.000491138, -0.000938778, 0.814432, 1.22044, 0.00405547, 0.0285653, 0.814432, 1.22044, 0.00405547, 0.0285653)

reports.append(Report(575700992, ("DT", -2, 1, 4), "MBwhAst1sec04"))
reports[-1].posNum = 68687
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.00211166, 0.00222942, 0), \
                           ValErr(0.00128516, 0.00467429, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.69695e-05, 5.24131e-05, 0), \
                           -195001, 68687, 68687, -nan)
reports[-1].sigmax = ValErr(0.818724, 0.00216383, 0)
reports[-1].sigmay = ValErr(1.22276, 0.00329995, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000878337, 0.00147369, -9.4152e-05, -0.00277448, -0.00146637, 0.00114753, -9.53304e-05, -0.00134696, -0.00146637, 0.00114753, -9.53304e-05, -0.00134696, 0.00121853, -0.00541844, -0.000109507, -0.00133988, 0.00121853, -0.00541844, -0.000109507, -0.00133988, 0.81872, 1.22277, 0.0040764, 0.0288475, 0.81872, 1.22277, 0.0040764, 0.0288475)

reports.append(Report(575963136, ("DT", -2, 1, 5), "MBwhAst1sec05"))
reports[-1].posNum = 67407
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-2.52033e-05, 0.00325776, 0), \
                           ValErr(0.000246314, 0.00472511, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.75745e-05, 5.49389e-05, 0), \
                           -191719, 67407, 67407, -nan)
reports[-1].sigmax = ValErr(0.820342, 0.00223423, 0)
reports[-1].sigmay = ValErr(1.22674, 0.00334107, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00179507, 0.000575027, 0.000112333, -0.000666689, -0.00028135, 0.000256587, 0.000106928, 0.000727408, -0.00028135, 0.000256587, 0.000106928, 0.000727408, 0.000292364, -0.00261386, 9.92712e-05, 0.000559484, 0.000292364, -0.00261386, 9.92712e-05, 0.000559484, 0.820339, 1.22674, 0.00408701, 0.0288867, 0.820339, 1.22674, 0.00408701, 0.0288867)

reports.append(Report(576225280, ("DT", -2, 1, 6), "MBwhAst1sec06"))
reports[-1].posNum = 65045
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000327861, 0.00332263, 0), \
                           ValErr(-0.00116894, 0.00479721, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.67501e-06, 5.60507e-05, 0), \
                           -184432, 65045, 65045, -nan)
reports[-1].sigmax = ValErr(0.815803, 0.00226185, 0)
reports[-1].sigmay = ValErr(1.22282, 0.00339034, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00368595, -0.0020378, 0.000222795, -0.00419737, -0.000485976, -0.00114422, 0.000220446, -0.00279273, -0.000485976, -0.00114422, 0.000220446, -0.00279273, -0.00239777, 0.000336528, 0.000233565, -0.00290055, -0.00239777, 0.000336528, 0.000233565, -0.00290055, 0.815801, 1.22282, 0.00406848, 0.0289536, 0.815801, 1.22282, 0.00406848, 0.0289536)

reports.append(Report(576487424, ("DT", -2, 1, 7), "MBwhAst1sec07"))
reports[-1].posNum = 68918
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.00109139, 0.00319275, 0), \
                           ValErr(0.00046544, 0.00466941, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.44017e-05, 5.43327e-05, 0), \
                           -195604, 68918, 68918, -nan)
reports[-1].sigmax = ValErr(0.816492, 0.00219934, 0)
reports[-1].sigmay = ValErr(1.22516, 0.00330018, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000905983, 0.00472018, 0.000694595, -0.0018755, 0.000767375, 0.000533896, 0.00068527, -0.000488621, 0.000767375, 0.000533896, 0.00068527, -0.000488621, 8.16779e-05, -0.00139908, 0.0006886, -0.000671279, 8.16779e-05, -0.00139908, 0.0006886, -0.000671279, 0.816483, 1.22518, 0.00406325, 0.0288193, 0.816483, 1.22518, 0.00406325, 0.0288193)

reports.append(Report(576749568, ("DT", -2, 1, 8), "MBwhAst1sec08"))
reports[-1].posNum = 66154
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000155946, 0.00327549, 0), \
                           ValErr(0.00207963, 0.00476252, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.08042e-06, 5.55396e-05, 0), \
                           -187799, 66154, 66154, -nan)
reports[-1].sigmax = ValErr(0.817144, 0.00224657, 0)
reports[-1].sigmay = ValErr(1.22492, 0.00336768, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00343323, 4.83538e-05, 0.000889098, -0.00120526, -0.00028629, 0.002084, 0.000887315, 0.000151857, -0.00028629, 0.002084, 0.000887315, 0.000151857, 0.00638533, -9.6441e-05, 0.000856909, -0.00013991, 0.00638533, -9.6441e-05, 0.000856909, -0.00013991, 0.81714, 1.22492, 0.00407466, 0.0289174, 0.81714, 1.22492, 0.00407466, 0.0289174)

reports.append(Report(577011712, ("DT", -2, 1, 9), "MBwhAst1sec09"))
reports[-1].posNum = 65410
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.00102793, 0.00336231, 0), \
                           ValErr(0.00055723, 0.00476562, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.62902e-06, 5.65673e-05, 0), \
                           -186025, 65410, 65410, -nan)
reports[-1].sigmax = ValErr(0.825963, 0.00228363, 0)
reports[-1].sigmay = ValErr(1.21812, 0.00336785, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.000563142, 0.00624583, -8.24974e-05, -0.00268989, -0.000918054, 0.000537271, -6.33167e-05, -0.00112475, -0.000918054, 0.000537271, -6.33167e-05, -0.00112475, 0.00261473, 0.00772581, -7.8617e-05, -0.00133129, 0.00261473, 0.00772581, -7.8617e-05, -0.00133129, 0.825962, 1.21812, 0.00411774, 0.0286636, 0.825962, 1.21812, 0.00411774, 0.0286636)

reports.append(Report(577273856, ("DT", -2, 1, 10), "MBwhAst1sec10"))
reports[-1].posNum = 68612
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000630225, 0.00321314, 0), \
                           ValErr(0.00109173, 0.00469533, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.7599e-05, 5.45356e-05, 0), \
                           -195308, 68612, 68612, -nan)
reports[-1].sigmax = ValErr(0.820719, 0.00221556, 0)
reports[-1].sigmay = ValErr(1.22907, 0.0033179, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00173369, 0.00942769, -0.000221973, -0.00128174, -0.000269582, 0.00100604, -0.000221874, 0.000235547, -0.000269582, 0.00100604, -0.000221874, 0.000235547, 0.000107405, 0.00274012, -0.000223251, 4.20108e-05, 0.000107405, 0.00274012, -0.000223251, 4.20108e-05, 0.820715, 1.22907, 0.0041051, 0.0287586, 0.820715, 1.22907, 0.0041051, 0.0287586)

reports.append(Report(577536000, ("DT", -2, 1, 11), "MBwhAst1sec11"))
reports[-1].posNum = 67822
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000265576, 0.00326467, 0), \
                           ValErr(0.000820067, 0.00471164, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.14479e-05, 5.52754e-05, 0), \
                           -193317, 67822, 67822, -nan)
reports[-1].sigmax = ValErr(0.825225, 0.00224078, 0)
reports[-1].sigmay = ValErr(1.22701, 0.00333174, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00304314, 0.0064752, -0.000622554, -0.00301892, 3.9253e-05, 0.000810626, -0.000639467, -0.00171795, 3.9253e-05, 0.000810626, -0.000639467, -0.00171795, -0.00119057, 0.00055785, -0.00063255, -0.00190362, -0.00119057, 0.00055785, -0.00063255, -0.00190362, 0.825216, 1.22702, 0.00411367, 0.0288874, 0.825216, 1.22702, 0.00411367, 0.0288874)

reports.append(Report(577798144, ("DT", -2, 1, 12), "MBwhAst1sec12"))
reports[-1].posNum = 64725
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-5.78523e-05, 0.00335416, 0), \
                           ValErr(0.000490616, 0.0047951, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.14119e-05, 5.65583e-05, 0), \
                           -183534, 64725, 64725, -nan)
reports[-1].sigmax = ValErr(0.818282, 0.00227438, 0)
reports[-1].sigmay = ValErr(1.21929, 0.00338896, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00696608, 0.00247836, 0.00050008, -0.00189425, 0.000133064, 0.000452838, 0.000467517, -0.000429486, 0.000133064, 0.000452838, 0.000467517, -0.000429486, -0.000743691, -0.00263034, 0.000473717, -0.000598231, -0.000743691, -0.00263034, 0.000473717, -0.000598231, 0.818285, 1.21928, 0.00408443, 0.0289303, 0.818285, 1.21928, 0.00408443, 0.0289303)

reports.append(Report(579108864, ("DT", -2, 2, 1), "MBwhAst2sec01"))
reports[-1].posNum = 79761
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.00101337, 0.00387663, 0), \
                           ValErr(-0.00049958, 0.00503651, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.54988e-05, 5.92114e-05, 0), \
                           -264871, 79761, 79761, -nan)
reports[-1].sigmax = ValErr(1.08994, 0.00271364, 0)
reports[-1].sigmay = ValErr(1.48707, 0.00371997, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00110041, 0.00308557, 0.000600136, -0.000362132, 0.000846815, -0.000470168, 0.000578191, -0.000856606, 0.000846815, -0.000470168, 0.000578191, -0.000856606, -0.000778971, 0.00451484, 0.000581225, -0.000980071, -0.000778971, 0.00451484, 0.000581225, -0.000980071, 1.08993, 1.48708, 0.00434637, 0.0232817, 1.08993, 1.48708, 0.00434637, 0.0232817)

reports.append(Report(579371008, ("DT", -2, 2, 2), "MBwhAst2sec02"))
reports[-1].posNum = 79121
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000377456, 0.00387742, 0), \
                           ValErr(0.00135926, 0.00514336, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.32829e-05, 5.94039e-05, 0), \
                           -262494, 79121, 79121, -nan)
reports[-1].sigmax = ValErr(1.08699, 0.00266761, 0)
reports[-1].sigmay = ValErr(1.48637, 0.0037361, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.000427481, 0.00035212, 0.000125173, -0.00065497, 0.000280705, 0.00137639, 0.000117671, -0.00121888, 0.000280705, 0.00137639, 0.000117671, -0.00121888, -0.00291221, 0.00226131, 0.000134154, -0.00134466, -0.00291221, 0.00226131, 0.000134154, -0.00134466, 1.08699, 1.48637, 0.00432739, 0.0232981, 1.08699, 1.48637, 0.00432739, 0.0232981)

reports.append(Report(579633152, ("DT", -2, 2, 3), "MBwhAst2sec03"))
reports[-1].posNum = 79269
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-2.79145e-05, 0.00387715, 0), \
                           ValErr(-0.000533401, 0.00526757, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.18814e-05, 5.91317e-05, 0), \
                           -262677, 79269, 79269, -nan)
reports[-1].sigmax = ValErr(1.08527, 0.00272567, 0)
reports[-1].sigmay = ValErr(1.48296, 0.00372449, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00373363, -0.00389365, 0.00034568, -0.000356686, -0.000112625, -0.000519102, 0.000348373, -0.000879905, -0.000112625, -0.000519102, 0.000348373, -0.000879905, 0.00120136, 0.000205325, 0.000347112, -0.000928927, 0.00120136, 0.000205325, 0.000347112, -0.000928927, 1.08527, 1.48297, 0.0043382, 0.0233855, 1.08527, 1.48297, 0.0043382, 0.0233855)

reports.append(Report(579895296, ("DT", -2, 2, 4), "MBwhAst2sec04"))
reports[-1].posNum = 79012
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000300767, 0.00383488, 0), \
                           ValErr(0.000202604, 0.00500774, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.14751e-05, 5.92026e-05, 0), \
                           -261700, 79012, 79012, -nan)
reports[-1].sigmax = ValErr(1.0829, 0.00266302, 0)
reports[-1].sigmay = ValErr(1.48384, 0.00373222, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00180456, 0.00841457, 5.41731e-05, -0.00112822, 0.000381027, 0.000194833, 3.95015e-05, -0.00155221, 0.000381027, 0.000194833, 3.95015e-05, -0.00155221, 0.000259787, 0.00407152, 4.26203e-05, -0.00173193, 0.000259787, 0.00407152, 4.26203e-05, -0.00173193, 1.0829, 1.48384, 0.00431727, 0.0232727, 1.0829, 1.48384, 0.00431727, 0.0232727)

reports.append(Report(580157440, ("DT", -2, 2, 5), "MBwhAst2sec05"))
reports[-1].posNum = 79222
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-1.8385e-05, 0.00243087, 0), \
                           ValErr(-0.000213116, 0.00508733, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.96894e-05, 5.77435e-05, 0), \
                           -263504, 79222, 79222, -nan)
reports[-1].sigmax = ValErr(1.08445, 0.0026259, 0)
reports[-1].sigmay = ValErr(1.50259, 0.00377369, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00178931, -0.000392692, -2.15279e-05, -0.000403862, -0.000170045, -0.000187499, -3.04256e-05, -0.000899101, -0.000170045, -0.000187499, -3.04256e-05, -0.000899101, -0.00252086, 0.00828637, -2.8635e-05, -0.00102047, -0.00252086, 0.00828637, -2.8635e-05, -0.00102047, 1.08445, 1.50259, 0.00432431, 0.0232776, 1.08445, 1.50259, 0.00432431, 0.0232776)

reports.append(Report(580419584, ("DT", -2, 2, 6), "MBwhAst2sec06"))
reports[-1].posNum = 79000
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000197369, 0.00385571, 0), \
                           ValErr(-0.00123936, 0.00512302, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.58001e-06, 5.93625e-05, 0), \
                           -261769, 79000, 79000, -nan)
reports[-1].sigmax = ValErr(1.0792, 0.002678, 0)
reports[-1].sigmay = ValErr(1.491, 0.00375045, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00438261, -0.00132429, -0.000219715, -0.00156661, 0.000183528, -0.00123688, -0.000208102, -0.00204794, 0.000183528, -0.00123688, -0.000208102, -0.00204794, -0.00519059, 0.00413063, -0.000189688, -0.00224565, -0.00519059, 0.00413063, -0.000189688, -0.00224565, 1.07919, 1.491, 0.00430592, 0.0233413, 1.07919, 1.491, 0.00430592, 0.0233413)

reports.append(Report(580681728, ("DT", -2, 2, 7), "MBwhAst2sec07"))
reports[-1].posNum = 79357
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000243478, 0.00386494, 0), \
                           ValErr(-0.00113049, 0.00515707, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.02999e-05, 5.93738e-05, 0), \
                           -263633, 79357, 79357, -nan)
reports[-1].sigmax = ValErr(1.0831, 0.00270984, 0)
reports[-1].sigmay = ValErr(1.49843, 0.00374584, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000152136, -0.00265008, -0.00102989, 0.000751778, 0.000380879, -0.00114853, -0.00103542, 0.000385194, 0.000380879, -0.00114853, -0.00103542, 0.000385194, 0.00200517, 0.00416514, -0.00103827, 0.000309035, 0.00200517, 0.00416514, -0.00103827, 0.000309035, 1.08308, 1.49845, 0.00434686, 0.0232872, 1.08308, 1.49845, 0.00434686, 0.0232872)

reports.append(Report(580943872, ("DT", -2, 2, 8), "MBwhAst2sec08"))
reports[-1].posNum = 79327
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000168363, 0.00386264, 0), \
                           ValErr(2.93186e-05, 0.00505536, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.21283e-05, 5.93008e-05, 0), \
                           -263446, 79327, 79327, -nan)
reports[-1].sigmax = ValErr(1.08386, 0.00271105, 0)
reports[-1].sigmay = ValErr(1.49571, 0.00375359, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00608219, 5.06495e-05, 0.000395188, -0.0006626, 8.70212e-05, 4.57412e-05, 0.000397827, -0.00095721, 8.70212e-05, 4.57412e-05, 0.000397827, -0.00095721, -0.00395836, 0.00305052, 0.000412368, -0.00104441, -0.00395836, 0.00305052, 0.000412368, -0.00104441, 1.08386, 1.49572, 0.00432426, 0.0233393, 1.08386, 1.49572, 0.00432426, 0.0233393)

reports.append(Report(581206016, ("DT", -2, 2, 9), "MBwhAst2sec09"))
reports[-1].posNum = 78729
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.00064218, 0.00390668, 0), \
                           ValErr(-0.00153031, 0.00510437, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.1165e-05, 5.96684e-05, 0), \
                           -261283, 78729, 78729, -nan)
reports[-1].sigmax = ValErr(1.09021, 0.00271909, 0)
reports[-1].sigmay = ValErr(1.48367, 0.00373644, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.000290029, 0.00673514, 0.000305239, -0.000706176, 0.000140025, -0.00146944, 0.000316863, -0.00115555, 0.000140025, -0.00146944, 0.000316863, -0.00115555, 0.00268215, 0.000712475, 0.000313111, -0.00124485, 0.00268215, 0.000712475, 0.000313111, -0.00124485, 1.09022, 1.48366, 0.00436404, 0.0233526, 1.09022, 1.48366, 0.00436404, 0.0233526)

reports.append(Report(581468160, ("DT", -2, 2, 10), "MBwhAst2sec10"))
reports[-1].posNum = 79530
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000151364, 0.0039007, 0), \
                           ValErr(-0.000457148, 0.00503606, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.28969e-06, 5.95653e-05, 0), \
                           -264468, 79530, 79530, -nan)
reports[-1].sigmax = ValErr(1.09477, 0.00272859, 0)
reports[-1].sigmay = ValErr(1.4873, 0.00372821, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000820357, 0.00461544, -0.000155634, -0.00132136, -0.0001189, -0.000460263, -0.000151787, -0.00173721, -0.0001189, -0.000460263, -0.000151787, -0.00173721, -0.000296469, -0.000891883, -0.000148919, -0.0018288, -0.000296469, -0.000891883, -0.000148919, -0.0018288, 1.09477, 1.4873, 0.00437046, 0.0234299, 1.09477, 1.4873, 0.00437046, 0.0234299)

reports.append(Report(581730304, ("DT", -2, 2, 11), "MBwhAst2sec11"))
reports[-1].posNum = 78786
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000694006, 0.00183573, 0), \
                           ValErr(-5.96172e-05, 0.0050675, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.06097e-05, 5.82624e-05, 0), \
                           -261999, 78786, 78786, -nan)
reports[-1].sigmax = ValErr(1.08897, 0.00274319, 0)
reports[-1].sigmay = ValErr(1.49534, 0.00377024, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00160009, 0.00732277, 0.000164798, -0.000218667, -0.000615493, -7.13071e-05, 0.000161463, -0.000715902, -0.000615493, -7.13071e-05, 0.000161463, -0.000715902, -0.000648442, -0.0013912, 0.00016131, -0.000764664, -0.000648442, -0.0013912, 0.00016131, -0.000764664, 1.08896, 1.49534, 0.00434879, 0.0233886, 1.08896, 1.49534, 0.00434879, 0.0233886)

reports.append(Report(581992448, ("DT", -2, 2, 12), "MBwhAst2sec12"))
reports[-1].posNum = 79331
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000703656, 0.00389398, 0), \
                           ValErr(-0.00030275, 0.00501413, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.21997e-05, 5.9347e-05, 0), \
                           -263361, 79331, 79331, -nan)
reports[-1].sigmax = ValErr(1.09079, 0.00273651, 0)
reports[-1].sigmay = ValErr(1.48437, 0.00372317, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00193408, -0.00229499, -0.00127291, -0.000560985, -0.000413635, -0.000348174, -0.00126873, -0.00103517, -0.000413635, -0.000348174, -0.00126873, -0.00103517, 0.00131635, 0.0012277, -0.00127893, -0.00109343, 0.00131635, 0.0012277, -0.00127893, -0.00109343, 1.09077, 1.48441, 0.00435597, 0.0232949, 1.09077, 1.48441, 0.00435597, 0.0232949)

reports.append(Report(583303168, ("DT", -2, 3, 1), "MBwhAst3sec01"))
reports[-1].posNum = 70915
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000586309, 0.00536988, 0), \
                           ValErr(0.000803162, 0.00681895, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.29916e-05, 7.18544e-05, 0), \
                           -268822, 70915, 70915, -nan)
reports[-1].sigmax = ValErr(1.42837, 0.0037928, 0)
reports[-1].sigmay = ValErr(1.81549, 0.00482075, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00422839, 0.00163823, 0.000224654, -0.000491557, -0.00063188, 0.00078222, 0.000211867, -0.00034733, -0.00063188, 0.00078222, 0.000211867, -0.00034733, -0.00310463, 0.00446877, 0.000213311, -0.000181731, -0.00310463, 0.00446877, 0.000213311, -0.000181731, 1.42837, 1.81549, 0.00488288, 0.0179992, 1.42837, 1.81549, 0.00488288, 0.0179992)

reports.append(Report(583565312, ("DT", -2, 3, 2), "MBwhAst3sec02"))
reports[-1].posNum = 70616
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000393675, 0.00541005, 0), \
                           ValErr(-0.000740705, 0.0068764, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.85989e-06, 7.25349e-05, 0), \
                           -268506, 70616, 70616, -nan)
reports[-1].sigmax = ValErr(1.43597, 0.0038211, 0)
reports[-1].sigmay = ValErr(1.82693, 0.00486143, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0057248, 0.000388908, 0.000213236, -0.000422548, -0.000418532, -0.000750143, 0.000236752, -0.000313461, -0.000418532, -0.000750143, 0.000236752, -0.000313461, 0.000977651, 0.00161091, 0.000235619, -0.000163358, 0.000977651, 0.00161091, 0.000235619, -0.000163358, 1.43596, 1.82693, 0.00486474, 0.0179834, 1.43596, 1.82693, 0.00486474, 0.0179834)

reports.append(Report(583827456, ("DT", -2, 3, 3), "MBwhAst3sec03"))
reports[-1].posNum = 71236
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.00017, 0.00535106, 0), \
                           ValErr(-0.000534407, 0.00679958, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.92452e-05, 7.17586e-05, 0), \
                           -269911, 71236, 71236, -nan)
reports[-1].sigmax = ValErr(1.42665, 0.00377973, 0)
reports[-1].sigmay = ValErr(1.81441, 0.00480709, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00276937, -0.000361179, 0.000583675, 0.000885217, -4.80876e-07, -0.000633504, 0.000610179, 0.00108541, -4.80876e-07, -0.000633504, 0.000610179, 0.00108541, 0.00253746, 0.0011546, 0.000605561, 0.00119748, 0.00253746, 0.0011546, 0.000605561, 0.00119748, 1.42663, 1.81443, 0.00485083, 0.0180967, 1.42663, 1.81443, 0.00485083, 0.0180967)

reports.append(Report(584089600, ("DT", -2, 3, 4), "MBwhAst3sec04"))
reports[-1].posNum = 70779
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.00164218, 0.00539775, 0), \
                           ValErr(0.00264394, 0.00683392, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.03463e-05, 7.21417e-05, 0), \
                           -268687, 70779, 70779, -nan)
reports[-1].sigmax = ValErr(1.43444, 0.00381255, 0)
reports[-1].sigmay = ValErr(1.81755, 0.00483083, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0042845, 0.00810128, 0.000567998, -0.00111857, 0.00150746, 0.00257481, 0.00057762, -0.000973908, 0.00150746, 0.00257481, 0.00057762, -0.000973908, 0.00408855, 0.0053838, 0.000575267, -0.000887997, 0.00408855, 0.0053838, 0.000575267, -0.000887997, 1.43443, 1.81756, 0.00485884, 0.0180229, 1.43443, 1.81756, 0.00485884, 0.0180229)

reports.append(Report(584351744, ("DT", -2, 3, 5), "MBwhAst3sec05"))
reports[-1].posNum = 70669
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000501355, 0.00539246, 0), \
                           ValErr(0.000465799, 0.00684257, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.81529e-05, 7.20119e-05, 0), \
                           -268181, 70669, 70669, -nan)
reports[-1].sigmax = ValErr(1.43189, 0.00380873, 0)
reports[-1].sigmay = ValErr(1.81852, 0.00483715, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000946991, -0.00648118, 0.000124413, 0.00047861, -0.000566083, 0.000426163, 0.000112832, 0.000545894, -0.000566083, 0.000426163, 0.000112832, 0.000545894, -0.00498486, 0.0104325, 0.000115475, 0.000678172, -0.00498486, 0.0104325, 0.000115475, 0.000678172, 1.43189, 1.81852, 0.0048726, 0.0180426, 1.43189, 1.81852, 0.0048726, 0.0180426)

reports.append(Report(584613888, ("DT", -2, 3, 6), "MBwhAst3sec06"))
reports[-1].posNum = 71309
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000630832, 0.00536821, 0), \
                           ValErr(0.00225809, 0.00683896, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.16963e-06, 7.19901e-05, 0), \
                           -270899, 71309, 71309, -nan)
reports[-1].sigmax = ValErr(1.43207, 0.0037921, 0)
reports[-1].sigmay = ValErr(1.82567, 0.0048343, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00281276, 0.00591224, 3.04576e-05, -0.000934558, 0.000608133, 0.00223648, 5.01267e-05, -0.000931092, 0.000608133, 0.00223648, 5.01267e-05, -0.000931092, 0.00613308, 0.0146179, 3.96488e-05, -0.00082525, 0.00613308, 0.0146179, 3.96488e-05, -0.00082525, 1.43207, 1.82567, 0.00486353, 0.0182217, 1.43207, 1.82567, 0.00486353, 0.0182217)

reports.append(Report(584876032, ("DT", -2, 3, 7), "MBwhAst3sec07"))
reports[-1].posNum = 70750
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.00096843, 0.00539885, 0), \
                           ValErr(-0.000281305, 0.00685357, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.71278e-05, 7.21815e-05, 0), \
                           -268770, 70750, 70750, -nan)
reports[-1].sigmax = ValErr(1.43466, 0.00381394, 0)
reports[-1].sigmay = ValErr(1.82224, 0.00484431, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.000570743, -0.00300639, -0.000316943, -0.000660394, -0.000929124, -0.000233315, -0.000307659, -0.000540447, -0.000929124, -0.000233315, -0.000307659, -0.000540447, -0.00271035, 0.00160121, -0.000294704, -0.000478964, -0.00271035, 0.00160121, -0.000294704, -0.000478964, 1.43465, 1.82223, 0.00489555, 0.0181095, 1.43465, 1.82223, 0.00489555, 0.0181095)

reports.append(Report(585138176, ("DT", -2, 3, 8), "MBwhAst3sec08"))
reports[-1].posNum = 70241
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000769406, 0.00542188, 0), \
                           ValErr(-0.000811805, 0.00694617, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.19725e-06, 7.27674e-05, 0), \
                           -267579, 70241, 70241, -nan)
reports[-1].sigmax = ValErr(1.43576, 0.00383072, 0)
reports[-1].sigmay = ValErr(1.84022, 0.00490984, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00238385, -0.00106732, -0.00097701, -0.00080819, -0.000805211, -0.000836184, -0.000966937, -0.000725742, -0.000805211, -0.000836184, -0.000966937, -0.000725742, 0.00383756, -0.00523306, -0.000977818, -0.000601359, 0.00383756, -0.00523306, -0.000977818, -0.000601359, 1.43575, 1.8402, 0.00489382, 0.0181431, 1.43575, 1.8402, 0.00489382, 0.0181431)

reports.append(Report(585400320, ("DT", -2, 3, 9), "MBwhAst3sec09"))
reports[-1].posNum = 71233
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000388004, 0.00539238, 0), \
                           ValErr(0.00180785, 0.00681729, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.79834e-05, 7.20148e-05, 0), \
                           -270640, 71233, 71233, -nan)
reports[-1].sigmax = ValErr(1.43782, 0.00380935, 0)
reports[-1].sigmay = ValErr(1.81913, 0.00481958, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00785517, 0.00847226, -0.000251073, -1.63293e-05, -0.000274823, 0.00188021, -0.000249073, 7.82171e-05, -0.000274823, 0.00188021, -0.000249073, 7.82171e-05, -0.00250701, 0.00763018, -0.00025406, 0.000201488, -0.00250701, 0.00763018, -0.00025406, 0.000201488, 1.43782, 1.81914, 0.00486783, 0.0180126, 1.43782, 1.81914, 0.00486783, 0.0180126)

reports.append(Report(585662464, ("DT", -2, 3, 10), "MBwhAst3sec10"))
reports[-1].posNum = 70745
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000800344, 0.00537291, 0), \
                           ValErr(-0.000584005, 0.00684957, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.48344e-06, 7.19968e-05, 0), \
                           -268377, 70745, 70745, -nan)
reports[-1].sigmax = ValErr(1.42772, 0.00379562, 0)
reports[-1].sigmay = ValErr(1.82143, 0.00484229, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00204044, 0.00174681, -0.000108054, -0.000587786, -0.000791738, -0.000574175, -0.000126586, -0.000499438, -0.000791738, -0.000574175, -0.000126586, -0.000499438, -0.00163987, -0.000899006, -0.000117252, -0.000394005, -0.00163987, -0.000899006, -0.000117252, -0.000394005, 1.42772, 1.82143, 0.00484065, 0.0180154, 1.42772, 1.82143, 0.00484065, 0.0180154)

reports.append(Report(585924608, ("DT", -2, 3, 11), "MBwhAst3sec11"))
reports[-1].posNum = 71085
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000487448, 0.00539051, 0), \
                           ValErr(-0.000772462, 0.00682949, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.34104e-05, 7.18977e-05, 0), \
                           -270008, 71085, 71085, -nan)
reports[-1].sigmax = ValErr(1.43558, 0.00380745, 0)
reports[-1].sigmay = ValErr(1.82019, 0.00482753, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.000431882, 0.00365381, 0.000569684, 2.65796e-05, 0.000368489, -0.000858053, 0.00058528, 9.3948e-05, 0.000368489, -0.000858053, 0.00058528, 9.3948e-05, -0.00101136, 0.0004417, 0.000582779, 0.000230666, -0.00101136, 0.0004417, 0.000582779, 0.000230666, 1.43557, 1.82021, 0.00490198, 0.0181068, 1.43557, 1.82021, 0.00490198, 0.0181068)

reports.append(Report(586186752, ("DT", -2, 3, 12), "MBwhAst3sec12"))
reports[-1].posNum = 70937
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000557857, 0.00537693, 0), \
                           ValErr(-0.000752021, 0.00685298, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.87423e-06, 7.20962e-05, 0), \
                           -269372, 70937, 70937, -nan)
reports[-1].sigmax = ValErr(1.43046, 0.00379775, 0)
reports[-1].sigmay = ValErr(1.82482, 0.00484473, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00554196, -0.00314795, -0.000157415, -0.000365664, -0.000531019, -0.000737247, -0.000158464, -0.000292767, -0.000531019, -0.000737247, -0.000158464, -0.000292767, -0.000215409, -0.00427319, -0.000160614, -0.000159381, -0.000215409, -0.00427319, -0.000160614, -0.000159381, 1.43045, 1.82481, 0.00485517, 0.0179239, 1.43045, 1.82481, 0.00485517, 0.0179239)

reports.append(Report(574947328, ("DT", -1, 1, 1), "MBwhBst1sec01"))
reports[-1].posNum = 113989
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000127359, 0.00217372, 0), \
                           ValErr(1.4072e-06, 0.00243934, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.23592e-05, 3.42107e-05, 0), \
                           -265561, 113989, 113989, -nan)
reports[-1].sigmax = ValErr(0.730663, 0.0015303, 0)
reports[-1].sigmay = ValErr(0.823358, 0.00172445, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00116595, -0.000242616, 0.000451595, -0.000764111, -6.14127e-05, 5.4189e-05, 0.000452547, -0.00135789, -6.14127e-05, 5.4189e-05, 0.000452547, -0.00135789, 0.00146343, 0.00091145, 0.000451035, -0.00136838, 0.00146343, 0.00091145, 0.000451035, -0.00136838, 0.730656, 0.823368, 0.00366452, 0.0128301, 0.730656, 0.823368, 0.00366452, 0.0128301)

reports.append(Report(575209472, ("DT", -1, 1, 2), "MBwhBst1sec02"))
reports[-1].posNum = 113665
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000547318, 0.00218955, 0), \
                           ValErr(4.82291e-05, 0.00245683, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.94187e-05, 3.44263e-05, 0), \
                           -266153, 113665, 113665, -nan)
reports[-1].sigmax = ValErr(0.735136, 0.00154184, 0)
reports[-1].sigmay = ValErr(0.828098, 0.00173682, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00156087, 0.00268166, 0.000122872, 0.000308614, -0.000435421, 1.74799e-05, 0.000118364, -0.000175026, -0.000435421, 1.74799e-05, 0.000118364, -0.000175026, 0.000999258, 0.00249043, 0.000112176, -0.000192648, 0.000999258, 0.00249043, 0.000112176, -0.000192648, 0.735138, 0.8281, 0.00367452, 0.0128689, 0.735138, 0.8281, 0.00367452, 0.0128689)

reports.append(Report(575471616, ("DT", -1, 1, 3), "MBwhBst1sec03"))
reports[-1].posNum = 77867
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-5.03662e-05, 0.00190799, 0), \
                           ValErr(-0.000320183, 0.00335389, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.97337e-06, 4.70527e-05, 0), \
                           -183441, 77867, 77867, -nan)
reports[-1].sigmax = ValErr(0.729329, 0.00183963, 0)
reports[-1].sigmay = ValErr(0.846691, 0.00214069, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00121689, 0.00485142, -0.000412532, -0.000448389, -4.44778e-05, -0.000325662, -0.000434433, -0.00095962, -4.44778e-05, -0.000325662, -0.000434433, -0.00095962, 0.000851871, -0.00157701, -0.000437902, -0.000966766, 0.000851871, -0.00157701, -0.000437902, -0.000966766, 0.729329, 0.846692, 0.00357893, 0.0132111, 0.729329, 0.846692, 0.00357893, 0.0132111)

reports.append(Report(575733760, ("DT", -1, 1, 4), "MBwhBst1sec04"))
reports[-1].posNum = 113848
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000425925, 0.00217318, 0), \
                           ValErr(-1.05107e-05, 0.00250101, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.47049e-05, 3.43267e-05, 0), \
                           -266009, 113848, 113848, -nan)
reports[-1].sigmax = ValErr(0.730464, 0.00150598, 0)
reports[-1].sigmay = ValErr(0.82922, 0.00173326, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.000392792, -0.00106974, 0.000634675, 0.000523383, -0.000174726, -8.36452e-05, 0.000641194, -7.46147e-05, -0.000174726, -8.36452e-05, 0.000641194, -7.46147e-05, -0.000225894, 0.00237913, 0.000641339, -7.9169e-05, -0.000225894, 0.00237913, 0.000641339, -7.9169e-05, 0.730485, 0.8292, 0.00365616, 0.0129019, 0.730485, 0.8292, 0.00365616, 0.0129019)

reports.append(Report(575995904, ("DT", -1, 1, 5), "MBwhBst1sec05"))
reports[-1].posNum = 113737
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000701622, 0.00215468, 0), \
                           ValErr(0.000112392, 0.00252515, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.24348e-05, 3.40624e-05, 0), \
                           -266146, 113737, 113737, -nan)
reports[-1].sigmax = ValErr(0.730977, 0.00150119, 0)
reports[-1].sigmay = ValErr(0.831527, 0.00172914, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.000300437, -0.00132902, -0.00189552, -0.000384009, -0.000513856, 5.325e-05, -0.00189002, -0.000994487, -0.000513856, 5.325e-05, -0.00189002, -0.000994487, 0.00172803, -0.000911648, -0.00189943, -0.000958304, 0.00172803, -0.000911648, -0.00189943, -0.000958304, 0.730952, 0.83156, 0.00365673, 0.0129165, 0.730952, 0.83156, 0.00365673, 0.0129165)

reports.append(Report(576258048, ("DT", -1, 1, 6), "MBwhBst1sec06"))
reports[-1].posNum = 113922
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-4.77828e-05, 0.00217765, 0), \
                           ValErr(0.000142659, 0.00245835, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.16452e-06, 3.43727e-05, 0), \
                           -266435, 113922, 113922, -nan)
reports[-1].sigmax = ValErr(0.731862, 0.00153323, 0)
reports[-1].sigmay = ValErr(0.829469, 0.00173773, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.000783921, 0.00308206, -0.000148363, 0.000868359, -9.80885e-06, 0.000131271, -0.000147158, 0.00026003, -9.80885e-06, 0.000131271, -0.000147158, 0.00026003, 0.000489998, 0.000407672, -0.000150888, 0.000289381, 0.000489998, 0.000407672, -0.000150888, 0.000289381, 0.731864, 0.829468, 0.00365525, 0.0129158, 0.731864, 0.829468, 0.00365525, 0.0129158)

reports.append(Report(576520192, ("DT", -1, 1, 7), "MBwhBst1sec07"))
reports[-1].posNum = 113866
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000176534, 0.00218305, 0), \
                           ValErr(0.000407868, 0.00245727, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.16022e-05, 3.43968e-05, 0), \
                           -266531, 113866, 113866, -nan)
reports[-1].sigmax = ValErr(0.733776, 0.00153764, 0)
reports[-1].sigmay = ValErr(0.828956, 0.0017371, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00062846, 0.000453431, -0.000618582, 5.05037e-08, 0.000292286, 0.000372722, -0.000615127, -0.00065186, 0.000292286, 0.000372722, -0.000615127, -0.00065186, -0.00123785, 0.000582497, -0.000608542, -0.000647176, -0.00123785, 0.000582497, -0.000608542, -0.000647176, 0.733775, 0.828961, 0.00366887, 0.0129372, 0.733775, 0.828961, 0.00366887, 0.0129372)

reports.append(Report(576782336, ("DT", -1, 1, 8), "MBwhBst1sec08"))
reports[-1].posNum = 113660
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000133349, 0.00218434, 0), \
                           ValErr(0.000218797, 0.00245619, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.6273e-06, 3.44757e-05, 0), \
                           -265797, 113660, 113660, -nan)
reports[-1].sigmax = ValErr(0.733212, 0.00153784, 0)
reports[-1].sigmay = ValErr(0.827761, 0.00173615, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0015583, 0.00183689, 0.000400054, 5.64895e-05, 0.000115835, 0.000224142, 0.000401743, -0.000501507, 0.000115835, 0.000224142, 0.000401743, -0.000501507, -0.000284168, 0.00084071, 0.000405089, -0.000510864, -0.000284168, 0.00084071, 0.000405089, -0.000510864, 0.733213, 0.82776, 0.00366922, 0.012905, 0.733213, 0.82776, 0.00366922, 0.012905)

reports.append(Report(577044480, ("DT", -1, 1, 9), "MBwhBst1sec09"))
reports[-1].posNum = 114344
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000347686, 0.00217381, 0), \
                           ValErr(-0.000498167, 0.00244307, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.75443e-05, 3.42872e-05, 0), \
                           -266896, 114344, 114344, -nan)
reports[-1].sigmax = ValErr(0.731683, 0.00153008, 0)
reports[-1].sigmay = ValErr(0.825868, 0.00172703, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00295436, 0.000190956, -0.000259084, -0.000615018, 0.000240711, -0.000467425, -0.000278807, -0.00122188, 0.000240711, -0.000467425, -0.000278807, -0.00122188, 0.00112798, 0.00205725, -0.000284099, -0.00121883, 0.00112798, 0.00205725, -0.000284099, -0.00121883, 0.73169, 0.825862, 0.00366242, 0.0128487, 0.73169, 0.825862, 0.00366242, 0.0128487)

reports.append(Report(577306624, ("DT", -1, 1, 10), "MBwhBst1sec10"))
reports[-1].posNum = 113434
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000472315, 0.00217319, 0), \
                           ValErr(-5.86547e-06, 0.00246407, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.5139e-08, 3.43849e-05, 0), \
                           -264846, 113434, 113434, -nan)
reports[-1].sigmax = ValErr(0.728825, 0.00153017, 0)
reports[-1].sigmay = ValErr(0.82965, 0.00174186, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000761049, -0.000316047, 0.000103856, 0.000432879, -0.000465614, -6.09198e-06, 0.000105209, -0.000171813, -0.000465614, -6.09198e-06, 0.000105209, -0.000171813, 0.000504092, -0.00110018, 0.000110258, -0.00015453, 0.000504092, -0.00110018, 0.000110258, -0.00015453, 0.728825, 0.82965, 0.00364484, 0.0129845, 0.728825, 0.82965, 0.00364484, 0.0129845)

reports.append(Report(577568768, ("DT", -1, 1, 11), "MBwhBst1sec11"))
reports[-1].posNum = 114384
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000138437, 0.00217856, 0), \
                           ValErr(-0.000251409, 0.00244902, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.99433e-07, 3.43664e-05, 0), \
                           -267641, 114384, 114384, -nan)
reports[-1].sigmax = ValErr(0.73396, 0.00153453, 0)
reports[-1].sigmay = ValErr(0.828006, 0.00173115, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00118369, -0.0011541, -0.000182415, 0.000534048, 0.000138625, -0.000252228, -0.000167428, -7.80979e-05, 0.000138625, -0.000252228, -0.000167428, -7.80979e-05, -0.000874587, 0.000584144, -0.000164638, -7.41349e-05, -0.000874587, 0.000584144, -0.000164638, -7.41349e-05, 0.733961, 0.828008, 0.00367519, 0.0129429, 0.733961, 0.828008, 0.00367519, 0.0129429)

reports.append(Report(577830912, ("DT", -1, 1, 12), "MBwhBst1sec12"))
reports[-1].posNum = 113494
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000175523, 0.00217287, 0), \
                           ValErr(-0.000281605, 0.00245098, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.84342e-06, 3.43176e-05, 0), \
                           -264425, 113494, 113494, -nan)
reports[-1].sigmax = ValErr(0.728928, 0.00152997, 0)
reports[-1].sigmay = ValErr(0.825437, 0.00173254, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00162888, 0.00322966, 0.000103682, -0.000567366, -0.000163213, -0.000284915, 0.000107213, -0.00116204, -0.000163213, -0.000284915, 0.000107213, -0.00116204, 0.000185017, -0.00160029, 0.000103312, -0.00114221, 0.000185017, -0.00160029, 0.000103312, -0.00114221, 0.728929, 0.825437, 0.00365036, 0.012918, 0.728929, 0.825437, 0.00365036, 0.012918)

reports.append(Report(579141632, ("DT", -1, 2, 1), "MBwhBst2sec01"))
reports[-1].posNum = 104024
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-6.09461e-05, 0.00161058, 0), \
                           ValErr(0.000202254, 0.00330763, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.61659e-05, 4.07487e-05, 0), \
                           -300491, 104024, 104024, -nan)
reports[-1].sigmax = ValErr(0.984964, 0.00215327, 0)
reports[-1].sigmay = ValErr(1.06816, 0.00233862, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00244381, -0.00495845, -0.000455734, -0.000204116, 7.59723e-06, 0.000192444, -0.000447247, -0.000580277, 7.59723e-06, 0.000192444, -0.000447247, -0.000580277, -0.000221354, 0.00220519, -0.000444236, -0.00058222, -0.000221354, 0.00220519, -0.000444236, -0.00058222, 0.984962, 1.06816, 0.00392895, 0.0118935, 0.984962, 1.06816, 0.00392895, 0.0118935)

reports.append(Report(579403776, ("DT", -1, 2, 2), "MBwhBst2sec02"))
reports[-1].posNum = 103721
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.0001159, 0.00306973, 0), \
                           ValErr(0.000386856, 0.0033369, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.88174e-05, 4.17455e-05, 0), \
                           -300394, 103721, 103721, -nan)
reports[-1].sigmax = ValErr(0.986397, 0.00216573, 0)
reports[-1].sigmay = ValErr(1.07464, 0.0023595, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00533967, -0.00237222, 0.000623105, 0.000174188, -0.00011539, 0.000418, 0.000636406, -0.000214626, -0.00011539, 0.000418, 0.000636406, -0.000214626, 2.32783e-05, 0.00208807, 0.000634255, -0.000210837, 2.32783e-05, 0.00208807, 0.000634255, -0.000210837, 0.986391, 1.07466, 0.0039215, 0.0118392, 0.986391, 1.07466, 0.0039215, 0.0118392)

reports.append(Report(579665920, ("DT", -1, 2, 3), "MBwhBst2sec03"))
reports[-1].posNum = 77550
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-3.61434e-05, 0.00185637, 0), \
                           ValErr(0.000174399, 0.00385438, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.80471e-06, 5.25837e-05, 0), \
                           -223666, 77550, 77550, -nan)
reports[-1].sigmax = ValErr(0.973471, 0.00245812, 0)
reports[-1].sigmay = ValErr(1.07591, 0.00272739, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00135516, 0.00359171, 0.000110168, -0.000713895, -3.12461e-05, 0.000175983, 0.000114153, -0.00125494, -3.12461e-05, 0.000175983, 0.000114153, -0.00125494, -0.00167434, 0.0011383, 0.000127006, -0.00127666, -0.00167434, 0.0011383, 0.000127006, -0.00127666, 0.973472, 1.07591, 0.00378569, 0.012153, 0.973472, 1.07591, 0.00378569, 0.012153)

reports.append(Report(579928064, ("DT", -1, 2, 4), "MBwhBst2sec04"))
reports[-1].posNum = 103777
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-7.69782e-05, 0.00305604, 0), \
                           ValErr(-0.000201937, 0.00333398, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.77328e-07, 4.15628e-05, 0), \
                           -300084, 103777, 103777, -nan)
reports[-1].sigmax = ValErr(0.982529, 0.00215664, 0)
reports[-1].sigmay = ValErr(1.07398, 0.00235738, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00165362, -0.00031408, -0.000250131, 4.69685e-05, -7.24204e-05, -0.000203065, -0.000254126, -0.000291351, -7.24204e-05, -0.000203065, -0.000254126, -0.000291351, -0.00212768, 0.000560669, -0.00025628, -0.000330293, -0.00212768, 0.000560669, -0.00025628, -0.000330293, 0.982532, 1.07398, 0.00391339, 0.0119597, 0.982532, 1.07398, 0.00391339, 0.0119597)

reports.append(Report(580190208, ("DT", -1, 2, 5), "MBwhBst2sec05"))
reports[-1].posNum = 103577
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000247296, 0.00306798, 0), \
                           ValErr(6.315e-05, 0.003337, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.59369e-06, 4.16177e-05, 0), \
                           -299786, 103577, 103577, -nan)
reports[-1].sigmax = ValErr(0.985275, 0.0021648, 0)
reports[-1].sigmay = ValErr(1.07389, 0.0023595, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0031998, 0.000392953, -0.000289557, 0.000183113, -0.000273098, 6.83161e-05, -0.000311347, -0.000217319, -0.000273098, 6.83161e-05, -0.000311347, -0.000217319, -0.000872412, -0.000122801, -0.000311369, -0.000234435, -0.000872412, -0.000122801, -0.000311369, -0.000234435, 0.985277, 1.07389, 0.00392548, 0.0118976, 0.985277, 1.07389, 0.00392548, 0.0118976)

reports.append(Report(580452352, ("DT", -1, 2, 6), "MBwhBst2sec06"))
reports[-1].posNum = 103755
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000686008, 0.00159108, 0), \
                           ValErr(-0.0001234, 0.00331909, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.92277e-06, 4.10212e-05, 0), \
                           -299674, 103755, 103755, -nan)
reports[-1].sigmax = ValErr(0.982752, 0.00215561, 0)
reports[-1].sigmay = ValErr(1.07015, 0.00234824, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.000836148, 0.00114174, 4.74416e-05, 1.52643e-05, 0.000675424, -0.000122218, 3.28128e-05, -0.000326712, 0.000675424, -0.000122218, 3.28128e-05, -0.000326712, -0.00039136, 0.000623918, 3.67197e-05, -0.000333034, -0.00039136, 0.000623918, 3.67197e-05, -0.000333034, 0.982753, 1.07015, 0.00390954, 0.0118422, 0.982753, 1.07015, 0.00390954, 0.0118422)

reports.append(Report(580714496, ("DT", -1, 2, 7), "MBwhBst2sec07"))
reports[-1].posNum = 103327
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000430874, 0.00158599, 0), \
                           ValErr(0.000209881, 0.00331837, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.91072e-05, 4.10365e-05, 0), \
                           -298416, 103327, 103327, -nan)
reports[-1].sigmax = ValErr(0.985465, 0.00216288, 0)
reports[-1].sigmay = ValErr(1.06698, 0.00234575, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000191913, -0.00224553, 0.000375328, 2.59566e-05, 0.000195177, 0.000254083, 0.000370104, -0.000355841, 0.000195177, 0.000254083, 0.000370104, -0.000355841, 0.00234789, 0.0021259, 0.000366056, -0.000365116, 0.00234789, 0.0021259, 0.000366056, -0.000365116, 0.985458, 1.067, 0.00391094, 0.0119274, 0.985458, 1.067, 0.00391094, 0.0119274)

reports.append(Report(580976640, ("DT", -1, 2, 8), "MBwhBst2sec08"))
reports[-1].posNum = 103734
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000139624, 0.00307225, 0), \
                           ValErr(-0.00028134, 0.00332184, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.04288e-06, 4.16896e-05, 0), \
                           -300095, 103734, 103734, -nan)
reports[-1].sigmax = ValErr(0.987591, 0.00216823, 0)
reports[-1].sigmay = ValErr(1.06987, 0.00234887, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00235845, 0.00326065, 0.000242536, 0.000651342, 0.000107, -0.000277888, 0.000253048, 0.000199042, 0.000107, -0.000277888, 0.000253048, 0.000199042, -0.000380266, 0.00249438, 0.000253686, 0.000163616, -0.000380266, 0.00249438, 0.000253686, 0.000163616, 0.98759, 1.06987, 0.00392147, 0.011955, 0.98759, 1.06987, 0.00392147, 0.011955)

reports.append(Report(581238784, ("DT", -1, 2, 9), "MBwhBst2sec09"))
reports[-1].posNum = 104269
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(4.71396e-05, 0.00305863, 0), \
                           ValErr(8.24573e-05, 0.00331747, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.18791e-05, 4.14928e-05, 0), \
                           -301543, 104269, 104269, -nan)
reports[-1].sigmax = ValErr(0.985423, 0.00215794, 0)
reports[-1].sigmay = ValErr(1.0712, 0.00234577, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00286146, 0.00263856, -0.000391849, -0.000758308, 0.000106427, 7.48442e-05, -0.00038615, -0.00116667, 0.000106427, 7.48442e-05, -0.00038615, -0.00116667, -0.001176, 0.00148914, -0.000376784, -0.00115576, -0.001176, 0.00148914, -0.000376784, -0.00115576, 0.985419, 1.0712, 0.00392433, 0.0119254, 0.985419, 1.0712, 0.00392433, 0.0119254)

reports.append(Report(581500928, ("DT", -1, 2, 10), "MBwhBst2sec10"))
reports[-1].posNum = 103417
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.00078059, 0.00306347, 0), \
                           ValErr(0.000700073, 0.00331628, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.7252e-05, 4.14974e-05, 0), \
                           -298370, 103417, 103417, -nan)
reports[-1].sigmax = ValErr(0.98306, 0.00216157, 0)
reports[-1].sigmay = ValErr(1.06644, 0.0023449, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.000815394, 0.00173945, -0.000141296, -0.00117029, -0.000908298, 0.000716508, -0.000149568, -0.00156896, -0.000908298, 0.000716508, -0.000149568, -0.00156896, -0.000179037, -0.00026546, -0.000153559, -0.00154935, -0.000179037, -0.00026546, -0.000153559, -0.00154935, 0.983061, 1.06644, 0.0039163, 0.0119412, 0.983061, 1.06644, 0.0039163, 0.0119412)

reports.append(Report(581763072, ("DT", -1, 2, 11), "MBwhBst2sec11"))
reports[-1].posNum = 103501
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000143977, 0.00308226, 0), \
                           ValErr(9.87568e-05, 0.00332119, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.5078e-06, 4.16189e-05, 0), \
                           -299523, 103501, 103501, -nan)
reports[-1].sigmax = ValErr(0.989874, 0.0021757, 0)
reports[-1].sigmay = ValErr(1.06845, 0.0023484, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000705711, 0.0022694, -0.000252348, -0.000156723, 0.000111583, 0.00010281, -0.00024631, -0.000567571, 0.000111583, 0.00010281, -0.00024631, -0.000567571, -0.00404945, -0.00230442, -0.00022529, -0.000569073, -0.00404945, -0.00230442, -0.00022529, -0.000569073, 0.989876, 1.06845, 0.00393567, 0.0119162, 0.989876, 1.06845, 0.00393567, 0.0119162)

reports.append(Report(582025216, ("DT", -1, 2, 12), "MBwhBst2sec12"))
reports[-1].posNum = 103622
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.00017388, 0.00163657, 0), \
                           ValErr(-6.18049e-05, 0.00332452, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.20478e-05, 4.07904e-05, 0), \
                           -299578, 103622, 103622, -nan)
reports[-1].sigmax = ValErr(0.983983, 0.00217353, 0)
reports[-1].sigmay = ValErr(1.0718, 0.00235359, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00066049, 0.00145987, 0.000122165, 0.000241933, 0.000131032, -5.67901e-05, 0.000129946, -0.00015579, 0.000131032, -5.67901e-05, 0.000129946, -0.00015579, -0.00167789, 0.000418246, 0.000134568, -0.000180908, -0.00167789, 0.000418246, 0.000134568, -0.000180908, 0.983984, 1.0718, 0.00390547, 0.0119255, 0.983984, 1.0718, 0.00390547, 0.0119255)

reports.append(Report(583335936, ("DT", -1, 3, 1), "MBwhBst3sec01"))
reports[-1].posNum = 89090
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.00019776, 0.00451657, 0), \
                           ValErr(0.00131611, 0.00473075, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.2876e-05, 5.37296e-05, 0), \
                           -310103, 89090, 89090, -nan)
reports[-1].sigmax = ValErr(1.34725, 0.00319174, 0)
reports[-1].sigmay = ValErr(1.41176, 0.00334461, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00381044, -0.00748005, 0.00045968, 0.000474552, 0.000127413, 0.00127761, 0.000483605, 0.000239278, 0.000127413, 0.00127761, 0.000483605, 0.000239278, 0.00207563, 0.00451349, 0.000479777, 0.000243806, 0.00207563, 0.00451349, 0.000479777, 0.000243806, 1.34724, 1.41177, 0.00457593, 0.0109312, 1.34724, 1.41177, 0.00457593, 0.0109312)

reports.append(Report(583598080, ("DT", -1, 3, 2), "MBwhBst3sec02"))
reports[-1].posNum = 89120
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000185487, 0.00451071, 0), \
                           ValErr(0.00095127, 0.00472317, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.60486e-05, 5.3647e-05, 0), \
                           -309965, 89120, 89120, -nan)
reports[-1].sigmax = ValErr(1.34562, 0.00318732, 0)
reports[-1].sigmay = ValErr(1.40964, 0.00333897, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(7.27123e-05, -0.00151912, 0.000732151, 0.000620818, 0.00010172, 0.000898838, 0.000748838, 0.000453499, 0.00010172, 0.000898838, 0.000748838, 0.000453499, 8.10874e-06, 0.000832524, 0.000751025, 0.00043527, 8.10874e-06, 0.000832524, 0.000751025, 0.00043527, 1.34561, 1.40965, 0.00453659, 0.0108538, 1.34561, 1.40965, 0.00453659, 0.0108538)

reports.append(Report(583860224, ("DT", -1, 3, 3), "MBwhBst3sec03"))
reports[-1].posNum = 67320
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000725568, 0.00502906, 0), \
                           ValErr(0.000302578, 0.00533221, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.87409e-05, 6.53437e-05, 0), \
                           -230784, 67320, 67320, -nan)
reports[-1].sigmax = ValErr(1.30462, 0.00355545, 0)
reports[-1].sigmay = ValErr(1.38316, 0.00376952, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.000139426, 0.0110447, 0.00017707, 5.13588e-05, 0.000675146, 0.000268761, 0.000183748, -0.000234027, 0.000675146, 0.000268761, 0.000183748, -0.000234027, 0.0015775, -0.00031993, 0.000171158, -0.00023663, 0.0015775, -0.00031993, 0.000171158, -0.00023663, 1.30462, 1.38316, 0.00439337, 0.010987, 1.30462, 1.38316, 0.00439337, 0.010987)

reports.append(Report(584122368, ("DT", -1, 3, 4), "MBwhBst3sec04"))
reports[-1].posNum = 88933
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000198413, 0.00167952, 0), \
                           ValErr(-8.70492e-05, 0.00474846, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.38948e-05, 5.35668e-05, 0), \
                           -308671, 88933, 88933, -nan)
reports[-1].sigmax = ValErr(1.3308, 0.00315707, 0)
reports[-1].sigmay = ValErr(1.41506, 0.00335407, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0041585, -0.000977744, -5.08592e-05, 0.000152118, 0.00013172, -0.000135257, -5.45771e-05, -6.815e-05, 0.00013172, -0.000135257, -5.45771e-05, -6.815e-05, -0.0010172, 0.00448407, -4.83982e-05, -6.45161e-05, -0.0010172, 0.00448407, -4.83982e-05, -6.45161e-05, 1.3308, 1.41506, 0.00453885, 0.0109476, 1.3308, 1.41506, 0.00453885, 0.0109476)

reports.append(Report(584384512, ("DT", -1, 3, 5), "MBwhBst3sec05"))
reports[-1].posNum = 88480
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000436404, 0.00170514, 0), \
                           ValErr(8.07985e-05, 0.00485903, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.05653e-05, 5.37916e-05, 0), \
                           -307712, 88480, 88480, -nan)
reports[-1].sigmax = ValErr(1.3396, 0.00321627, 0)
reports[-1].sigmay = ValErr(1.41554, 0.00336385, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00239015, 0.00426585, 0.000580526, 0.000235971, -0.000461745, 5.86495e-05, 0.000576353, -1.28697e-05, -0.000461745, 5.86495e-05, 0.000576353, -1.28697e-05, 0.000398739, -0.00162017, 0.000562102, -1.05487e-05, 0.000398739, -0.00162017, 0.000562102, -1.05487e-05, 1.3396, 1.41554, 0.00454735, 0.0109238, 1.3396, 1.41554, 0.00454735, 0.0109238)

reports.append(Report(584646656, ("DT", -1, 3, 6), "MBwhBst3sec06"))
reports[-1].posNum = 88855
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.00218106, 0.00450545, 0), \
                           ValErr(-0.000453406, 0.00473044, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.59132e-05, 5.37701e-05, 0), \
                           -308817, 88855, 88855, -nan)
reports[-1].sigmax = ValErr(1.34228, 0.00318417, 0)
reports[-1].sigmay = ValErr(1.40956, 0.00334379, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.000892531, -0.00281149, 0.000544276, 0.000632436, -0.00213755, -0.000414941, 0.000544088, 0.000412271, -0.00213755, -0.000414941, 0.000544088, 0.000412271, -0.00415785, -0.00200936, 0.000544485, 0.000392952, -0.00415785, -0.00200936, 0.000544485, 0.000392952, 1.34228, 1.40955, 0.00453831, 0.0110563, 1.34228, 1.40955, 0.00453831, 0.0110563)

reports.append(Report(584908800, ("DT", -1, 3, 7), "MBwhBst3sec07"))
reports[-1].posNum = 88959
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.00038672, 0.00171001, 0), \
                           ValErr(0.00028248, 0.00473462, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.65484e-05, 5.35563e-05, 0), \
                           -309243, 88959, 88959, -nan)
reports[-1].sigmax = ValErr(1.33927, 0.00317613, 0)
reports[-1].sigmay = ValErr(1.41373, 0.00335488, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000195583, -0.00106362, -8.10414e-05, 0.000270632, 0.00040894, 0.000316892, -9.20406e-05, 1.19143e-05, 0.00040894, 0.000316892, -9.20406e-05, 1.19143e-05, 0.000421328, 0.000867628, -9.01822e-05, -1.61556e-05, 0.000421328, 0.000867628, -9.01822e-05, -1.61556e-05, 1.33927, 1.41374, 0.00453258, 0.0110684, 1.33927, 1.41374, 0.00453258, 0.0110684)

reports.append(Report(585170944, ("DT", -1, 3, 8), "MBwhBst3sec08"))
reports[-1].posNum = 88813
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.00064265, 0.00173172, 0), \
                           ValErr(-0.000367748, 0.00476067, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.65125e-05, 5.39296e-05, 0), \
                           -309044, 88813, 88813, -nan)
reports[-1].sigmax = ValErr(1.3486, 0.00321677, 0)
reports[-1].sigmay = ValErr(1.40885, 0.003352, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00121264, -0.00504225, 0.000324155, 0.000742016, 0.000746113, -0.000313512, 0.000294893, 0.000498574, 0.000746113, -0.000313512, 0.000294893, 0.000498574, 0.00247492, 0.00146961, 0.000284593, 0.000509654, 0.00247492, 0.00146961, 0.000284593, 0.000509654, 1.3486, 1.40884, 0.00456636, 0.0110333, 1.3486, 1.40884, 0.00456636, 0.0110333)

reports.append(Report(585433088, ("DT", -1, 3, 9), "MBwhBst3sec09"))
reports[-1].posNum = 89165
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-6.47814e-05, 0.00167793, 0), \
                           ValErr(-6.29743e-05, 0.00474156, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.63965e-05, 5.35576e-05, 0), \
                           -309818, 89165, 89165, -nan)
reports[-1].sigmax = ValErr(1.3356, 0.00316519, 0)
reports[-1].sigmay = ValErr(1.41538, 0.00335093, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0049252, -0.000767208, -4.03398e-05, 0.000619243, -0.000113366, -9.6867e-05, -3.89477e-05, 0.000398739, -0.000113366, -9.6867e-05, -3.89477e-05, 0.000398739, 0.000138531, -0.00122883, -3.73255e-05, 0.000367119, 0.000138531, -0.00122883, -3.73255e-05, 0.000367119, 1.3356, 1.41538, 0.00454022, 0.0109594, 1.3356, 1.41538, 0.00454022, 0.0109594)

reports.append(Report(585695232, ("DT", -1, 3, 10), "MBwhBst3sec10"))
reports[-1].posNum = 88650
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000261472, 0.00170303, 0), \
                           ValErr(0.00103419, 0.00472585, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.31935e-05, 5.36512e-05, 0), \
                           -307627, 88650, 88650, -nan)
reports[-1].sigmax = ValErr(1.33525, 0.00317156, 0)
reports[-1].sigmay = ValErr(1.40937, 0.00334772, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00405734, 0.00181279, 0.0001839, 0.000222767, 0.000295972, 0.0010586, 0.000178908, 4.88907e-05, 0.000295972, 0.0010586, 0.000178908, 4.88907e-05, 0.00556735, -0.00113641, 0.000158709, 5.13527e-05, 0.00556735, -0.00113641, 0.000158709, 5.13527e-05, 1.33525, 1.40937, 0.00453772, 0.0109293, 1.33525, 1.40937, 0.00453772, 0.0109293)

reports.append(Report(585957376, ("DT", -1, 3, 11), "MBwhBst3sec11"))
reports[-1].posNum = 88578
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.0012003, 0.00257742, 0), \
                           ValErr(-0.000212842, 0.00490305, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.67347e-05, 5.34328e-05, 0), \
                           -307828, 88578, 88578, -nan)
reports[-1].sigmax = ValErr(1.3408, 0.0030966, 0)
reports[-1].sigmay = ValErr(1.41069, 0.00332183, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00174725, 0.00146103, -0.0002126, -0.000167399, -0.00110302, -0.000148597, -0.000209309, -0.000375231, -0.00110302, -0.000148597, -0.000209309, -0.000375231, 0.00342301, -0.00108512, -0.000224171, -0.000422697, 0.00342301, -0.00108512, -0.000224171, -0.000422697, 1.3408, 1.41069, 0.00456539, 0.0108368, 1.3408, 1.41069, 0.00456539, 0.0108368)

reports.append(Report(586219520, ("DT", -1, 3, 12), "MBwhBst3sec12"))
reports[-1].posNum = 88422
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000270399, 0.00168758, 0), \
                           ValErr(0.00054422, 0.00474165, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.49959e-05, 5.36053e-05, 0), \
                           -306807, 88422, 88422, -nan)
reports[-1].sigmax = ValErr(1.33451, 0.00317528, 0)
reports[-1].sigmay = ValErr(1.40968, 0.00335783, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00312251, -0.00240693, -9.27429e-05, -6.40698e-05, -0.000128756, 0.000645324, -8.02691e-05, -0.000266415, -0.000128756, 0.000645324, -8.02691e-05, -0.000266415, -0.00473512, 0.00047085, -8.21771e-05, -0.000255641, -0.00473512, 0.00047085, -8.21771e-05, -0.000255641, 1.33451, 1.40969, 0.00452576, 0.0108506, 1.33451, 1.40969, 0.00452576, 0.0108506)

reports.append(Report(574980096, ("DT", 0, 1, 1), "MBwhCst1sec01"))
reports[-1].posNum = 127348
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000163077, 0.00196495, 0), \
                           ValErr(-0.000341759, 0.00192399, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.30207e-05, 2.88769e-05, 0), \
                           -268245, 127348, 127348, -nan)
reports[-1].sigmax = ValErr(0.701196, 0.0013894, 0)
reports[-1].sigmay = ValErr(0.686247, 0.00135978, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.000811142, 0.00107913, -6.23104e-05, 0.000316844, 0.000155735, -0.000369324, -6.3607e-05, 0.000300956, 0.000155735, -0.000369324, -6.3607e-05, 0.000300956, 0.00187813, 7.1476e-05, -6.66823e-05, 0.000306436, 0.00187813, 7.1476e-05, -6.66823e-05, 0.000306436, 0.701197, 0.686246, 0.00371579, 0.00833384, 0.701197, 0.686246, 0.00371579, 0.00833384)

reports.append(Report(576028672, ("DT", 0, 1, 5), "MBwhCst1sec05"))
reports[-1].posNum = 128077
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000200543, 0.00139804, 0), \
                           ValErr(0.000243914, 0.00191928, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.93309e-05, 2.47478e-05, 0), \
                           -269009, 128077, 128077, -nan)
reports[-1].sigmax = ValErr(0.696232, 0.00137474, 0)
reports[-1].sigmay = ValErr(0.686988, 0.00135816, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00182486, -0.000965949, 0.000314894, 0.000387338, -0.000219934, 0.000184057, 0.000303734, 0.000392749, -0.000219934, 0.000184057, 0.000303734, 0.000392749, -0.00290884, 0.000737552, 0.000318957, 0.000378025, -0.00290884, 0.000737552, 0.000318957, 0.000378025, 0.696237, 0.686986, 0.00370022, 0.00833486, 0.696237, 0.686986, 0.00370022, 0.00833486)

reports.append(Report(577077248, ("DT", 0, 1, 9), "MBwhCst1sec09"))
reports[-1].posNum = 127771
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000165511, 0.00194568, 0), \
                           ValErr(0.000334933, 0.00192238, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.97897e-05, 2.86501e-05, 0), \
                           -268184, 127771, 127771, -nan)
reports[-1].sigmax = ValErr(0.695432, 0.00137571, 0)
reports[-1].sigmay = ValErr(0.686801, 0.00135864, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00276279, -0.000613532, -0.000137039, -4.49535e-05, -0.000148424, 0.000377631, -0.000128166, -5.52721e-05, -0.000148424, 0.000377631, -0.000128166, -5.52721e-05, 0.00116527, 0.00179878, -0.00013437, -8.84063e-05, 0.00116527, 0.00179878, -0.00013437, -8.84063e-05, 0.695428, 0.686805, 0.0036906, 0.00836411, 0.695428, 0.686805, 0.0036906, 0.00836411)

reports.append(Report(575242240, ("DT", 0, 1, 2), "MBwhCst1sec02"))
reports[-1].posNum = 127288
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000286302, 0.00194954, 0), \
                           ValErr(-0.000534857, 0.00192615, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.41864e-05, 2.87213e-05, 0), \
                           -267262, 127288, 127288, -nan)
reports[-1].sigmax = ValErr(0.695537, 0.00137852, 0)
reports[-1].sigmay = ValErr(0.687191, 0.00136197, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(9.20206e-05, 0.00112008, 0.000642102, 4.55733e-06, 0.000288918, -0.000540163, 0.000635743, -6.85924e-06, 0.000288918, -0.000540163, 0.000635743, -6.85924e-06, -0.000253761, -0.00145073, 0.000642843, -2.4694e-05, -0.000253761, -0.00145073, 0.000642843, -2.4694e-05, 0.695539, 0.68719, 0.00368213, 0.00831101, 0.695539, 0.68719, 0.00368213, 0.00831101)

reports.append(Report(576290816, ("DT", 0, 1, 6), "MBwhCst1sec06"))
reports[-1].posNum = 126704
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-2.75982e-05, 0.00197209, 0), \
                           ValErr(0.000441865, 0.00192917, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.6949e-05, 2.89074e-05, 0), \
                           -267107, 126704, 126704, -nan)
reports[-1].sigmax = ValErr(0.701969, 0.00139447, 0)
reports[-1].sigmay = ValErr(0.686675, 0.00136409, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.000802985, -0.00166677, 0.000541147, -0.000359063, -2.25418e-05, 0.000432967, 0.000536625, -0.000335375, -2.25418e-05, 0.000432967, 0.000536625, -0.000335375, -0.00137497, -0.000483681, 0.000542665, -0.000347258, -0.00137497, -0.000483681, 0.000542665, -0.000347258, 0.701968, 0.686677, 0.00371658, 0.00835884, 0.701968, 0.686677, 0.00371658, 0.00835884)

reports.append(Report(577339392, ("DT", 0, 1, 10), "MBwhCst1sec10"))
reports[-1].posNum = 126711
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000136075, 0.00140698, 0), \
                           ValErr(-0.000261051, 0.00192035, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.12727e-05, 2.53988e-05, 0), \
                           -265523, 126711, 126711, -nan)
reports[-1].sigmax = ValErr(0.693974, 0.00137182, 0)
reports[-1].sigmay = ValErr(0.685878, 0.00135651, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000562024, 0.000549435, 0.000660375, 0.000143167, -0.000146986, -0.000246835, 0.00068752, 0.000130551, -0.000146986, -0.000246835, 0.00068752, 0.000130551, -0.000302979, -0.000905428, 0.000687734, 0.000134707, -0.000302979, -0.000905428, 0.000687734, 0.000134707, 0.69397, 0.685884, 0.00367884, 0.0083672, 0.69397, 0.685884, 0.00367884, 0.0083672)

reports.append(Report(575504384, ("DT", 0, 1, 3), "MBwhCst1sec03"))
reports[-1].posNum = 126853
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.00023655, 0.00140776, 0), \
                           ValErr(0.000273637, 0.0019273, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.57108e-05, 2.48448e-05, 0), \
                           -266780, 126853, 126853, -nan)
reports[-1].sigmax = ValErr(0.698064, 0.0013834, 0)
reports[-1].sigmay = ValErr(0.687037, 0.00136248, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.000508313, 0.000236113, -0.000387837, 0.000375955, 0.000239464, 0.000271612, -0.000403864, 0.000400256, 0.000239464, 0.000271612, -0.000403864, 0.000400256, 0.000829687, 0.000183456, -0.000409284, 0.000402572, 0.000829687, 0.000183456, -0.000409284, 0.000402572, 0.698064, 0.687038, 0.00369456, 0.00837672, 0.698064, 0.687038, 0.00369456, 0.00837672)

reports.append(Report(576552960, ("DT", 0, 1, 7), "MBwhCst1sec07"))
reports[-1].posNum = 126908
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000242414, 0.00141325, 0), \
                           ValErr(-0.000192019, 0.00192923, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.89395e-07, 2.48799e-05, 0), \
                           -266705, 126908, 126908, -nan)
reports[-1].sigmax = ValErr(0.695549, 0.00137867, 0)
reports[-1].sigmay = ValErr(0.688487, 0.00136556, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0015167, -0.000669215, -9.96805e-05, -0.000117679, 0.000240257, -0.000191876, -9.48799e-05, -0.000126504, 0.000240257, -0.000191876, -9.48799e-05, -0.000126504, -0.000144426, -0.00178783, -9.35665e-05, -0.000126902, -0.000144426, -0.00178783, -9.35665e-05, -0.000126902, 0.695549, 0.688487, 0.00367855, 0.00837082, 0.695549, 0.688487, 0.00367855, 0.00837082)

reports.append(Report(577601536, ("DT", 0, 1, 11), "MBwhCst1sec11"))
reports[-1].posNum = 126634
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000172553, 0.00140837, 0), \
                           ValErr(0.00019748, 0.00192201, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.32292e-05, 2.49086e-05, 0), \
                           -265547, 126634, 126634, -nan)
reports[-1].sigmax = ValErr(0.696379, 0.00138208, 0)
reports[-1].sigmay = ValErr(0.684511, 0.00135949, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00201458, 0.00158827, 0.000881047, 0.000446586, 0.000178533, 0.000192618, 0.000867291, 0.000393134, 0.000178533, 0.000192618, 0.000867291, 0.000393134, 8.38883e-05, 0.0022427, 0.000866552, 0.000376849, 8.38883e-05, 0.0022427, 0.000866552, 0.000376849, 0.696379, 0.684512, 0.00368798, 0.00841565, 0.696379, 0.684512, 0.00368798, 0.00841565)

reports.append(Report(575766528, ("DT", 0, 1, 4), "MBwhCst1sec04"))
reports[-1].posNum = 127310
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-3.92213e-05, 0.00195269, 0), \
                           ValErr(-0.000112787, 0.0019239, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.63143e-05, 2.87548e-05, 0), \
                           -267324, 127310, 127310, -nan)
reports[-1].sigmax = ValErr(0.696711, 0.00138073, 0)
reports[-1].sigmay = ValErr(0.686119, 0.00135973, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00032204, 0.00153737, 2.59263e-05, 0.00020305, -5.24398e-05, -0.00016803, 2.21786e-05, 0.000210131, -5.24398e-05, -0.00016803, 2.21786e-05, 0.000210131, -0.00141001, 0.000896376, 2.82781e-05, 0.000207754, -0.00141001, 0.000896376, 2.82781e-05, 0.000207754, 0.696711, 0.686121, 0.00368908, 0.00837602, 0.696711, 0.686121, 0.00368908, 0.00837602)

reports.append(Report(576815104, ("DT", 0, 1, 8), "MBwhCst1sec08"))
reports[-1].posNum = 127542
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(2.7203e-05, 0.00140006, 0), \
                           ValErr(-0.000352454, 0.00192198, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.52096e-05, 2.47749e-05, 0), \
                           -267568, 127542, 127542, -nan)
reports[-1].sigmax = ValErr(0.694783, 0.00137407, 0)
reports[-1].sigmay = ValErr(0.686713, 0.00135914, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00120641, 0.00179347, -0.000346023, 0.000650223, 3.06224e-05, -0.00031899, -0.000351213, 0.000664746, 3.06224e-05, -0.00031899, -0.000351213, 0.000664746, 0.000909532, -0.000687056, -0.000353427, 0.000690828, 0.000909532, -0.000687056, -0.000353427, 0.000690828, 0.694783, 0.686713, 0.0036837, 0.0083818, 0.694783, 0.686713, 0.0036837, 0.0083818)

reports.append(Report(577863680, ("DT", 0, 1, 12), "MBwhCst1sec12"))
reports[-1].posNum = 127603
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000134423, 0.00142454, 0), \
                           ValErr(-0.000242473, 0.00191221, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.04337e-05, 2.4829e-05, 0), \
                           -268010, 127603, 127603, -nan)
reports[-1].sigmax = ValErr(0.697144, 0.00137879, 0)
reports[-1].sigmay = ValErr(0.686074, 0.00135814, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.000472785, -0.00352555, 0.000720052, 0.000185454, -0.000125773, -0.000218864, 0.000720924, 0.000180037, -0.000125773, -0.000218864, 0.000720924, 0.000180037, 0.000808954, 0.000514523, 0.000720619, 0.000179513, 0.000808954, 0.000514523, 0.000720619, 0.000179513, 0.697145, 0.686073, 0.00369221, 0.00835329, 0.697145, 0.686073, 0.00369221, 0.00835329)

reports.append(Report(579174400, ("DT", 0, 2, 1), "MBwhCst2sec01"))
reports[-1].posNum = 113290
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000267257, 0.00149069, 0), \
                           ValErr(0.000677687, 0.00263281, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.68192e-05, 3.59337e-05, 0), \
                           -309328, 113290, 113290, -nan)
reports[-1].sigmax = ValErr(0.958194, 0.00198948, 0)
reports[-1].sigmay = ValErr(0.937297, 0.0019681, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000445978, 0.00189505, -0.000304918, 0.000219622, -0.000250147, 0.000699738, -0.000311615, 0.000214214, -0.000250147, 0.000699738, -0.000311615, 0.000214214, -0.00283063, 6.34479e-05, -0.000299439, 0.000220913, -0.00283063, 6.34479e-05, -0.000299439, 0.000220913, 0.958191, 0.937298, 0.00397827, 0.00862781, 0.958191, 0.937298, 0.00397827, 0.00862781)

reports.append(Report(580222976, ("DT", 0, 2, 5), "MBwhCst2sec05"))
reports[-1].posNum = 113228
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-2.78107e-05, 0.00148668, 0), \
                           ValErr(0.000105345, 0.00264992, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.95822e-06, 3.58201e-05, 0), \
                           -308291, 113228, 113228, -nan)
reports[-1].sigmax = ValErr(0.953676, 0.00198579, 0)
reports[-1].sigmay = ValErr(0.934545, 0.00195943, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00310467, -0.00257322, -0.000373076, 8.5081e-06, -2.94036e-05, 0.000102495, -0.000375143, 2.27442e-05, -2.94036e-05, 0.000102495, -0.000375143, 2.27442e-05, 0.003231, 0.00110336, -0.000386875, 3.42069e-07, 0.003231, 0.00110336, -0.000386875, 3.42069e-07, 0.953674, 0.934545, 0.00397741, 0.00864395, 0.953674, 0.934545, 0.00397741, 0.00864395)

reports.append(Report(581271552, ("DT", 0, 2, 9), "MBwhCst2sec09"))
reports[-1].posNum = 113143
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-1.72955e-05, 0.00148704, 0), \
                           ValErr(-2.44113e-05, 0.00263759, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.54719e-05, 3.59391e-05, 0), \
                           -308635, 113143, 113143, -nan)
reports[-1].sigmax = ValErr(0.95491, 0.00198476, 0)
reports[-1].sigmay = ValErr(0.938099, 0.00197156, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.000874437, -0.00410817, 0.00103627, -0.00131409, 8.35107e-07, -1.21541e-05, 0.00103317, -0.00131604, 8.35107e-07, -1.21541e-05, 0.00103317, -0.00131604, -0.00151349, -0.00271866, 0.00103867, -0.00132163, -0.00151349, -0.00271866, 0.00103867, -0.00132163, 0.954904, 0.938103, 0.00396247, 0.00857948, 0.954904, 0.938103, 0.00396247, 0.00857948)

reports.append(Report(579436544, ("DT", 0, 2, 2), "MBwhCst2sec02"))
reports[-1].posNum = 113673
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000477856, 0.00149302, 0), \
                           ValErr(-0.000350666, 0.00263732, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.00797e-06, 3.57741e-05, 0), \
                           -310009, 113673, 113673, -nan)
reports[-1].sigmax = ValErr(0.954551, 0.00198081, 0)
reports[-1].sigmay = ValErr(0.937858, 0.00196637, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00267883, 0.000581525, 6.14366e-06, 5.22508e-05, -0.000472455, -0.000345559, 1.39781e-05, 8.19285e-05, -0.000472455, -0.000345559, 1.39781e-05, 8.19285e-05, -0.00104395, 0.000784589, 1.70475e-05, 9.7343e-05, -0.00104395, 0.000784589, 1.70475e-05, 9.7343e-05, 0.954548, 0.937858, 0.00396842, 0.00864345, 0.954548, 0.937858, 0.00396842, 0.00864345)

reports.append(Report(580485120, ("DT", 0, 2, 6), "MBwhCst2sec06"))
reports[-1].posNum = 113606
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000243175, 0.00148349, 0), \
                           ValErr(0.00024986, 0.00263468, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.42073e-06, 3.59099e-05, 0), \
                           -310044, 113606, 113606, -nan)
reports[-1].sigmax = ValErr(0.958936, 0.00200877, 0)
reports[-1].sigmay = ValErr(0.935358, 0.00196112, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00134231, 0.000779432, 7.33278e-05, 0.000500562, -0.000240938, 0.000253097, 6.40831e-05, 0.000478401, -0.000240938, 0.000253097, 6.40831e-05, 0.000478401, -0.00161608, 0.0026278, 6.40025e-05, 0.000461843, -0.00161608, 0.0026278, 6.40025e-05, 0.000461843, 0.958935, 0.93536, 0.00397614, 0.00865498, 0.958935, 0.93536, 0.00397614, 0.00865498)

reports.append(Report(581533696, ("DT", 0, 2, 10), "MBwhCst2sec10"))
reports[-1].posNum = 113530
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000390927, 0.00159676, 0), \
                           ValErr(0.00044996, 0.00264963, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.53398e-05, 3.51407e-05, 0), \
                           -309149, 113530, 113530, -nan)
reports[-1].sigmax = ValErr(0.953513, 0.00199512, 0)
reports[-1].sigmay = ValErr(0.935, 0.00196078, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.000648549, 9.83244e-05, -0.000498024, -6.36408e-05, 0.000379091, 0.000411894, -0.000501984, -5.5309e-05, 0.000379091, 0.000411894, -0.000501984, -5.5309e-05, 0.0021797, -2.63926e-05, -0.000504809, -7.31436e-05, 0.0021797, -2.63926e-05, -0.000504809, -7.31436e-05, 0.953511, 0.935001, 0.0039525, 0.008644, 0.953511, 0.935001, 0.0039525, 0.008644)

reports.append(Report(579698688, ("DT", 0, 2, 3), "MBwhCst2sec03"))
reports[-1].posNum = 113206
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000217865, 0.00148623, 0), \
                           ValErr(-6.82793e-05, 0.00263286, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.68549e-05, 3.60009e-05, 0), \
                           -309118, 113206, 113206, -nan)
reports[-1].sigmax = ValErr(0.956211, 0.00198721, 0)
reports[-1].sigmay = ValErr(0.939394, 0.00197384, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000434598, 0.00205531, -0.000581249, -0.000238566, 0.000209396, -0.000105701, -0.000587389, -0.000235525, 0.000209396, -0.000105701, -0.000587389, -0.000235525, -0.000815379, -0.00216396, -0.00058557, -0.000233096, -0.000815379, -0.00216396, -0.00058557, -0.000233096, 0.956206, 0.939397, 0.00396212, 0.00866933, 0.956206, 0.939397, 0.00396212, 0.00866933)

reports.append(Report(580747264, ("DT", 0, 2, 7), "MBwhCst2sec07"))
reports[-1].posNum = 113115
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000137593, 0.00148796, 0), \
                           ValErr(-0.000140334, 0.00264543, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.67236e-05, 3.59451e-05, 0), \
                           -308561, 113115, 113115, -nan)
reports[-1].sigmax = ValErr(0.953928, 0.00200422, 0)
reports[-1].sigmay = ValErr(0.939073, 0.00197457, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00119972, -0.00425026, -0.000350187, 0.00045497, 0.000112661, -0.000204156, -0.000347753, 0.000442455, 0.000112661, -0.000204156, -0.000347753, 0.000442455, -0.000795936, -0.00114781, -0.000350857, 0.000435293, -0.000795936, -0.00114781, -0.000350857, 0.000435293, 0.953932, 0.939072, 0.00396622, 0.00862988, 0.953932, 0.939072, 0.00396622, 0.00862988)

reports.append(Report(581795840, ("DT", 0, 2, 11), "MBwhCst2sec11"))
reports[-1].posNum = 113589
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000937533, 0.00161002, 0), \
                           ValErr(-0.000294826, 0.0026496, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(7.67736e-06, 3.50985e-05, 0), \
                           -309285, 113589, 113589, -nan)
reports[-1].sigmax = ValErr(0.953111, 0.00199817, 0)
reports[-1].sigmay = ValErr(0.935188, 0.00196099, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000117295, -0.000814661, 0.000456779, 2.31343e-05, -0.000933294, -0.000312386, 0.000464689, 5.91317e-05, -0.000933294, -0.000312386, 0.000464689, 5.91317e-05, -0.000675471, 0.000578391, 0.000461888, 7.29386e-05, -0.000675471, 0.000578391, 0.000461888, 7.29386e-05, 0.953111, 0.935189, 0.00395993, 0.0086599, 0.953111, 0.935189, 0.00395993, 0.0086599)

reports.append(Report(579960832, ("DT", 0, 2, 4), "MBwhCst2sec04"))
reports[-1].posNum = 113338
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000350074, 0.0014899, 0), \
                           ValErr(-0.000423536, 0.00265923, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(9.67181e-06, 3.58482e-05, 0), \
                           -308697, 113338, 113338, -nan)
reports[-1].sigmax = ValErr(0.953688, 0.00199923, 0)
reports[-1].sigmay = ValErr(0.935409, 0.00196323, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.000450003, 0.00152385, 0.00100057, 6.26135e-05, 0.000339828, -0.000431571, 0.000998518, 6.78465e-05, 0.000339828, -0.000431571, 0.000998518, 6.78465e-05, -0.00126141, -0.000735624, 0.00100123, 7.03839e-05, -0.00126141, -0.000735624, 0.00100123, 7.03839e-05, 0.953691, 0.935409, 0.00396454, 0.00866751, 0.953691, 0.935409, 0.00396454, 0.00866751)

reports.append(Report(581009408, ("DT", 0, 2, 8), "MBwhCst2sec08"))
reports[-1].posNum = 112881
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(6.38073e-05, 0.00148824, 0), \
                           ValErr(9.84003e-05, 0.00263929, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.78739e-05, 3.60398e-05, 0), \
                           -308035, 112881, 112881, -nan)
reports[-1].sigmax = ValErr(0.956547, 0.00198651, 0)
reports[-1].sigmay = ValErr(0.937445, 0.00197222, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00219536, 0.000980056, -0.000600907, 1.96657e-05, 5.71533e-05, 8.54702e-05, -0.000582131, 2.18379e-06, 5.71533e-05, 8.54702e-05, -0.000582131, 2.18379e-06, -0.00121339, -6.57322e-05, -0.000579092, -2.17798e-07, -0.00121339, -6.57322e-05, -0.000579092, -2.17798e-07, 0.956543, 0.937446, 0.00395661, 0.00867226, 0.956543, 0.937446, 0.00395661, 0.00867226)

reports.append(Report(582057984, ("DT", 0, 2, 12), "MBwhCst2sec12"))
reports[-1].posNum = 113574
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000317642, 0.00148476, 0), \
                           ValErr(0.000847803, 0.0026613, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.43677e-05, 3.57687e-05, 0), \
                           -309058, 113574, 113574, -nan)
reports[-1].sigmax = ValErr(0.951815, 0.00199342, 0)
reports[-1].sigmay = ValErr(0.934922, 0.00196009, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.000662796, -0.00255993, -2.62619e-05, 1.76385e-05, -0.000335162, 0.000827387, -2.97428e-05, 9.18171e-06, -0.000335162, 0.000827387, -2.97428e-05, 9.18171e-06, 0.000948034, 0.00205757, -3.47377e-05, 1.76849e-05, 0.000948034, 0.00205757, -3.47377e-05, 1.76849e-05, 0.951816, 0.934926, 0.00395098, 0.00865409, 0.951816, 0.934926, 0.00395098, 0.00865409)

reports.append(Report(583368704, ("DT", 0, 3, 1), "MBwhCst3sec01"))
reports[-1].posNum = 92005
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000264827, 0.00165901, 0), \
                           ValErr(0.000417935, 0.00430017, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.64968e-06, 4.89776e-05, 0), \
                           -310294, 92005, 92005, -nan)
reports[-1].sigmax = ValErr(1.32348, 0.00308431, 0)
reports[-1].sigmay = ValErr(1.28974, 0.00301192, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00106498, 0.000788634, -5.42795e-05, -0.000531843, -0.000263784, 0.00042819, -6.55122e-05, -0.000556286, -0.000263784, 0.00042819, -6.55122e-05, -0.000556286, -0.00263112, -0.000519416, -5.2183e-05, -0.000556739, -0.00263112, -0.000519416, -5.2183e-05, -0.000556739, 1.32348, 1.28974, 0.00456188, 0.00884492, 1.32348, 1.28974, 0.00456188, 0.00884492)

reports.append(Report(584417280, ("DT", 0, 3, 5), "MBwhCst3sec05"))
reports[-1].posNum = 91860
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-3.73212e-05, 0.00165029, 0), \
                           ValErr(-0.000408934, 0.00405301, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(7.34544e-06, 4.86016e-05, 0), \
                           -308760, 91860, 91860, -nan)
reports[-1].sigmax = ValErr(1.31577, 0.0030229, 0)
reports[-1].sigmay = ValErr(1.28263, 0.00294162, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00218462, -0.00321433, 0.000458316, 5.93488e-06, -4.32055e-05, -0.000399676, 0.000449501, 1.74626e-05, -4.32055e-05, -0.000399676, 0.000449501, 1.74626e-05, -0.00294806, -0.00338351, 0.000466809, -3.46399e-06, -0.00294806, -0.00338351, 0.000466809, -3.46399e-06, 1.31577, 1.28262, 0.00452745, 0.00878096, 1.31577, 1.28262, 0.00452745, 0.00878096)

reports.append(Report(585465856, ("DT", 0, 3, 9), "MBwhCst3sec09"))
reports[-1].posNum = 92037
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000111516, 0.00164888, 0), \
                           ValErr(0.00024736, 0.00407206, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.48101e-05, 4.85662e-05, 0), \
                           -309311, 92037, 92037, -nan)
reports[-1].sigmax = ValErr(1.31799, 0.0030296, 0)
reports[-1].sigmay = ValErr(1.27986, 0.00294322, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00098681, -0.00255584, 0.000574646, -0.000324606, 9.64813e-05, 0.000291972, 0.000569377, -0.00032998, 9.64813e-05, 0.000291972, 0.000569377, -0.00032998, -0.00125682, -0.000967323, 0.000569225, -0.000327464, -0.00125682, -0.000967323, 0.000569225, -0.000327464, 1.31799, 1.27985, 0.00453835, 0.00882292, 1.31799, 1.27985, 0.00453835, 0.00882292)

reports.append(Report(583630848, ("DT", 0, 3, 2), "MBwhCst3sec02"))
reports[-1].posNum = 91922
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.0001435, 0.00167104, 0), \
                           ValErr(-0.000300368, 0.00434571, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.92218e-06, 4.88877e-05, 0), \
                           -309392, 91922, 91922, -nan)
reports[-1].sigmax = ValErr(1.31437, 0.00306041, 0)
reports[-1].sigmay = ValErr(1.28992, 0.00300049, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00329415, 0.00146017, -0.000722931, -0.000315135, 0.000140736, -0.000327214, -0.000713156, -0.0003086, 0.000140736, -0.000327214, -0.000713156, -0.0003086, -0.00301462, 0.00176697, -0.000706469, -0.000295973, -0.00301462, 0.00176697, -0.000706469, -0.000295973, 1.31437, 1.28992, 0.0045212, 0.00880887, 1.31437, 1.28992, 0.0045212, 0.00880887)

reports.append(Report(584679424, ("DT", 0, 3, 6), "MBwhCst3sec06"))
reports[-1].posNum = 92502
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000129488, 0.00433958, 0), \
                           ValErr(0.000403745, 0.0042488, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.80012e-05, 4.89311e-05, 0), \
                           -311786, 92502, 92502, -nan)
reports[-1].sigmax = ValErr(1.31982, 0.00306847, 0)
reports[-1].sigmay = ValErr(1.29073, 0.00300086, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.000485419, 0.00109456, -0.000165197, 0.000320133, -0.000142372, 0.000515669, -0.00016536, 0.000275202, -0.000142372, 0.000515669, -0.00016536, 0.000275202, -0.0032866, 0.00188872, -0.000154012, 0.000275835, -0.0032866, 0.00188872, -0.000154012, 0.000275835, 1.31982, 1.29074, 0.00453369, 0.00885547, 1.31982, 1.29074, 0.00453369, 0.00885547)

reports.append(Report(585728000, ("DT", 0, 3, 10), "MBwhCst3sec10"))
reports[-1].posNum = 91946
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.00156207, 0.00436713, 0), \
                           ValErr(-0.000119123, 0.00434994, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.73523e-05, 4.9142e-05, 0), \
                           -310370, 91946, 91946, -nan)
reports[-1].sigmax = ValErr(1.32457, 0.00307919, 0)
reports[-1].sigmay = ValErr(1.29254, 0.00299692, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00124733, -0.00244819, -0.00114605, -0.00077611, 0.00155644, -5.08593e-05, -0.00115311, -0.00077411, 0.00155644, -5.08593e-05, -0.00115311, -0.00077411, 0.00230424, -0.000240593, -0.00115259, -0.000777595, 0.00230424, -0.000240593, -0.00115259, -0.000777595, 1.32457, 1.29253, 0.00455031, 0.00878938, 1.32457, 1.29253, 0.00455031, 0.00878938)

reports.append(Report(583892992, ("DT", 0, 3, 3), "MBwhCst3sec03"))
reports[-1].posNum = 91774
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000656016, 0.00173733, 0), \
                           ValErr(-0.000514693, 0.00425562, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.16981e-05, 4.90274e-05, 0), \
                           -309185, 91774, 91774, -nan)
reports[-1].sigmax = ValErr(1.32162, 0.00307509, 0)
reports[-1].sigmay = ValErr(1.28692, 0.00301718, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(3.62015e-05, 0.00225469, 2.54186e-05, -0.00035268, 0.000648742, -0.000560025, 1.67378e-05, -0.000339515, 0.000648742, -0.000560025, 1.67378e-05, -0.000339515, -0.00328646, -0.00284518, 2.66397e-05, -0.000312177, -0.00328646, -0.00284518, 2.66397e-05, -0.000312177, 1.32162, 1.28692, 0.00454117, 0.00877419, 1.32162, 1.28692, 0.00454117, 0.00877419)

reports.append(Report(584941568, ("DT", 0, 3, 7), "MBwhCst3sec07"))
reports[-1].posNum = 91736
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000149899, 0.00165135, 0), \
                           ValErr(0.00026628, 0.00437942, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.49394e-05, 4.90122e-05, 0), \
                           -308918, 91736, 91736, -nan)
reports[-1].sigmax = ValErr(1.31607, 0.0030236, 0)
reports[-1].sigmay = ValErr(1.29037, 0.00297856, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000960452, -0.00534983, 0.000314759, -6.73832e-05, -0.000133355, 0.000210413, 0.000323035, -8.43503e-05, -0.000133355, 0.000210413, 0.000323035, -8.43503e-05, 0.000584244, -0.00012604, 0.000327199, -0.000119506, 0.000584244, -0.00012604, 0.000327199, -0.000119506, 1.31608, 1.29038, 0.00453245, 0.00879308, 1.31608, 1.29038, 0.00453245, 0.00879308)

reports.append(Report(585990144, ("DT", 0, 3, 11), "MBwhCst3sec11"))
reports[-1].posNum = 92077
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(7.08145e-05, 0.00164782, 0), \
                           ValErr(-0.000133202, 0.00435265, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.75929e-06, 4.89828e-05, 0), \
                           -309810, 92077, 92077, -nan)
reports[-1].sigmax = ValErr(1.31666, 0.00301067, 0)
reports[-1].sigmay = ValErr(1.28622, 0.00296574, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00297442, -0.00274726, -0.000323596, 0.000164889, 7.25175e-05, -0.000149714, -0.000309487, 0.000191904, 7.25175e-05, -0.000149714, -0.000309487, 0.000191904, -0.00369975, 0.00224197, -0.000298436, 0.000198753, -0.00369975, 0.00224197, -0.000298436, 0.000198753, 1.31666, 1.28622, 0.00453796, 0.0087981, 1.31666, 1.28622, 0.00453796, 0.0087981)

reports.append(Report(584155136, ("DT", 0, 3, 4), "MBwhCst3sec04"))
reports[-1].posNum = 92050
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.00127111, 0.0043354, 0), \
                           ValErr(-0.000977639, 0.00426686, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(7.24461e-06, 4.90316e-05, 0), \
                           -310196, 92050, 92050, -nan)
reports[-1].sigmax = ValErr(1.31531, 0.00306551, 0)
reports[-1].sigmay = ValErr(1.29423, 0.00301637, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0018376, 0.000149033, 0.000365075, 6.25357e-05, 0.00124472, -0.000967887, 0.000364723, 5.07954e-05, 0.00124472, -0.000967887, 0.000364723, 5.07954e-05, 0.00335163, 0.000906183, 0.000359386, 5.94236e-05, 0.00335163, 0.000906183, 0.000359386, 5.94236e-05, 1.3153, 1.29423, 0.00452164, 0.00879759, 1.3153, 1.29423, 0.00452164, 0.00879759)

reports.append(Report(585203712, ("DT", 0, 3, 8), "MBwhCst3sec08"))
reports[-1].posNum = 91629
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000296651, 0.00165237, 0), \
                           ValErr(0.000807333, 0.00432985, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.49697e-05, 4.88714e-05, 0), \
                           -308340, 91629, 91629, -nan)
reports[-1].sigmax = ValErr(1.31573, 0.003027, 0)
reports[-1].sigmay = ValErr(1.28765, 0.00299049, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00629712, 0.00601863, -2.38105e-05, 0.000164906, 0.000300635, 0.000757802, -9.91504e-06, 0.000158835, 0.000300635, 0.000757802, -9.91504e-06, 0.000158835, 0.00314217, -0.0025482, -2.07053e-05, 0.00014572, 0.00314217, -0.0025482, -2.07053e-05, 0.00014572, 1.31574, 1.28765, 0.00452506, 0.00879432, 1.31574, 1.28765, 0.00452506, 0.00879432)

reports.append(Report(586252288, ("DT", 0, 3, 12), "MBwhCst3sec12"))
reports[-1].posNum = 92231
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000941374, 0.00165348, 0), \
                           ValErr(0.000179281, 0.00434599, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.50665e-07, 4.86996e-05, 0), \
                           -309999, 92231, 92231, -nan)
reports[-1].sigmax = ValErr(1.31358, 0.00300962, 0)
reports[-1].sigmay = ValErr(1.28464, 0.00295692, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00143046, -0.00928191, -9.61936e-05, -0.000310997, 0.00092087, 0.000177881, -0.000102679, -0.000326185, 0.00092087, 0.000177881, -0.000102679, -0.000326185, 0.00521469, 0.000636354, -0.000119352, -0.00031383, 0.00521469, 0.000636354, -0.000119352, -0.00031383, 1.31358, 1.28464, 0.00451134, 0.00879776, 1.31358, 1.28464, 0.00451134, 0.00879776)

reports.append(Report(575012864, ("DT", 1, 1, 1), "MBwhDst1sec01"))
reports[-1].posNum = 113226
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000459566, 0.00218371, 0), \
                           ValErr(-8.02262e-05, 0.00244881, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.53632e-05, 3.4376e-05, 0), \
                           -264026, 113226, 113226, -nan)
reports[-1].sigmax = ValErr(0.731667, 0.00153754, 0)
reports[-1].sigmay = ValErr(0.823991, 0.00173155, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00385904, -0.00217222, 4.21896e-05, -0.00057992, 0.000307756, -7.14858e-05, 5.06622e-05, -0.00121109, 0.000307756, -7.14858e-05, 5.06622e-05, -0.00121109, 0.000692987, 0.000999697, 4.49183e-05, -0.00123437, 0.000692987, 0.000999697, 4.49183e-05, -0.00123437, 0.731669, 0.82399, 0.00366475, 0.0128528, 0.731669, 0.82399, 0.00366475, 0.0128528)

reports.append(Report(575275008, ("DT", 1, 1, 2), "MBwhDst1sec02"))
reports[-1].posNum = 113489
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000238701, 0.00218117, 0), \
                           ValErr(7.52637e-05, 0.0024614, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.56414e-05, 3.44102e-05, 0), \
                           -265388, 113489, 113489, -nan)
reports[-1].sigmax = ValErr(0.731882, 0.00153622, 0)
reports[-1].sigmay = ValErr(0.829196, 0.00174048, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000608274, 0.000388348, -0.000484268, -0.000538759, 8.75932e-05, 8.14597e-05, -0.000481277, -0.00114412, 8.75932e-05, 8.14597e-05, -0.000481277, -0.00114412, -0.00100437, -0.00107725, -0.000479687, -0.00114846, -0.00100437, -0.00107725, -0.000479687, -0.00114846, 0.731888, 0.829192, 0.00366261, 0.0129629, 0.731888, 0.829192, 0.00366261, 0.0129629)

reports.append(Report(575537152, ("DT", 1, 1, 3), "MBwhDst1sec03"))
reports[-1].posNum = 113029
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000228146, 0.00218153, 0), \
                           ValErr(-0.000239028, 0.0024678, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.74862e-06, 3.45078e-05, 0), \
                           -264170, 113029, 113029, -nan)
reports[-1].sigmax = ValErr(0.73054, 0.0015365, 0)
reports[-1].sigmay = ValErr(0.82967, 0.00174499, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000428213, -0.00135324, 0.000327197, -0.00101086, -0.000251471, -0.000239262, 0.00033493, -0.0015985, -0.000251471, -0.000239262, 0.00033493, -0.0015985, -0.00277607, 0.00109116, 0.00034355, -0.00158901, -0.00277607, 0.00109116, 0.00034355, -0.00158901, 0.73054, 0.829674, 0.00366095, 0.0129414, 0.73054, 0.829674, 0.00366095, 0.0129414)

reports.append(Report(575799296, ("DT", 1, 1, 4), "MBwhDst1sec04"))
reports[-1].posNum = 77125
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.00040768, 0.00265922, 0), \
                           ValErr(0.000122397, 0.0030687, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.87979e-05, 4.87949e-05, 0), \
                           -183052, 77125, 77125, -nan)
reports[-1].sigmax = ValErr(0.737474, 0.00187774, 0)
reports[-1].sigmay = ValErr(0.85222, 0.0021699, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.000953193, 0.000719891, -0.000297463, 0.00114064, -0.00026206, 0.000123027, -0.000308119, 0.000674299, -0.00026206, 0.000123027, -0.000308119, 0.000674299, -0.00438314, 0.00115442, -0.000288353, 0.000645061, -0.00438314, 0.00115442, -0.000288353, 0.000645061, 0.737473, 0.852229, 0.00366513, 0.0131889, 0.737473, 0.852229, 0.00366513, 0.0131889)

reports.append(Report(576061440, ("DT", 1, 1, 5), "MBwhDst1sec05"))
reports[-1].posNum = 113758
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000242374, 0.002183, 0), \
                           ValErr(0.000240256, 0.00246187, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.05855e-05, 3.44954e-05, 0), \
                           -266354, 113758, 113758, -nan)
reports[-1].sigmax = ValErr(0.73304, 0.00153681, 0)
reports[-1].sigmay = ValErr(0.830342, 0.00174081, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000316614, 0.00346266, 8.40087e-05, -3.63784e-05, 5.90708e-05, 0.00024033, 8.44769e-05, -0.000581718, 5.90708e-05, 0.00024033, 8.44769e-05, -0.000581718, -8.20347e-05, -0.000206667, 7.93387e-05, -0.000630609, -8.20347e-05, -0.000206667, 7.93387e-05, -0.000630609, 0.733043, 0.830343, 0.00366183, 0.012831, 0.733043, 0.830343, 0.00366183, 0.012831)

reports.append(Report(576323584, ("DT", 1, 1, 6), "MBwhDst1sec06"))
reports[-1].posNum = 113233
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000373659, 0.00217638, 0), \
                           ValErr(0.000338297, 0.00246252, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.00869e-06, 3.44236e-05, 0), \
                           -264344, 113233, 113233, -nan)
reports[-1].sigmax = ValErr(0.729505, 0.00153295, 0)
reports[-1].sigmay = ValErr(0.828636, 0.00174126, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00144732, 0.00127003, 5.61978e-05, 0.000589255, 0.000350486, 0.000339193, 4.03942e-05, -1.90202e-05, 0.000350486, 0.000339193, 4.03942e-05, -1.90202e-05, -0.000278493, 0.00154053, 4.65476e-05, -3.17475e-05, -0.000278493, 0.00154053, 4.65476e-05, -3.17475e-05, 0.729505, 0.828636, 0.0036623, 0.0129378, 0.729505, 0.828636, 0.0036623, 0.0129378)

reports.append(Report(576585728, ("DT", 1, 1, 7), "MBwhDst1sec07"))
reports[-1].posNum = 113662
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-6.39016e-05, 0.00219098, 0), \
                           ValErr(-7.03787e-06, 0.00245443, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.16516e-05, 3.4568e-05, 0), \
                           -266101, 113662, 113662, -nan)
reports[-1].sigmax = ValErr(0.735425, 0.00154248, 0)
reports[-1].sigmay = ValErr(0.827448, 0.00173548, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.000369065, -0.00212958, -0.000428609, 3.71121e-05, -0.000138054, 3.15404e-07, -0.000436108, -0.000542906, -0.000138054, 3.15404e-07, -0.000436108, -0.000542906, -0.000429693, -0.000980768, -0.000431028, -0.000592168, -0.000429693, -0.000980768, -0.000431028, -0.000592168, 0.735427, 0.827446, 0.00367434, 0.012852, 0.735427, 0.827446, 0.00367434, 0.012852)

reports.append(Report(576847872, ("DT", 1, 1, 8), "MBwhDst1sec08"))
reports[-1].posNum = 113341
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000353353, 0.00218285, 0), \
                           ValErr(9.13686e-05, 0.00246831, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.20459e-06, 3.45274e-05, 0), \
                           -265261, 113341, 113341, -nan)
reports[-1].sigmax = ValErr(0.731723, 0.0015369, 0)
reports[-1].sigmay = ValErr(0.830982, 0.00174538, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.000659084, 0.000168572, -0.000501675, 0.000152153, -0.000346455, 9.12776e-05, -0.000496393, -0.000508976, -0.000346455, 9.12776e-05, -0.000496393, -0.000508976, -0.0015501, 0.000129208, -0.000491406, -0.00051988, -0.0015501, 0.000129208, -0.000491406, -0.00051988, 0.731724, 0.830982, 0.00366545, 0.0129568, 0.731724, 0.830982, 0.00366545, 0.0129568)

reports.append(Report(577110016, ("DT", 1, 1, 9), "MBwhDst1sec09"))
reports[-1].posNum = 114324
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-2.5402e-05, 0.00216306, 0), \
                           ValErr(-0.000128458, 0.00250712, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.57252e-06, 3.41714e-05, 0), \
                           -267142, 114324, 114324, -nan)
reports[-1].sigmax = ValErr(0.730201, 0.00145959, 0)
reports[-1].sigmay = ValErr(0.829668, 0.00173213, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00150211, -0.00234157, 0.00104326, 0.000443383, -7.95216e-05, -0.000126517, 0.00105151, -0.000138555, -7.95216e-05, -0.000126517, 0.00105151, -0.000138555, -0.00244598, 0.000860188, 0.00106152, -0.00012849, -0.00244598, 0.000860188, 0.00106152, -0.00012849, 0.730197, 0.829671, 0.0036597, 0.012915, 0.730197, 0.829671, 0.0036597, 0.012915)

reports.append(Report(577372160, ("DT", 1, 1, 10), "MBwhDst1sec10"))
reports[-1].posNum = 114239
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000576251, 0.00217381, 0), \
                           ValErr(0.000528774, 0.00245806, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.6454e-05, 3.43936e-05, 0), \
                           -267296, 114239, 114239, -nan)
reports[-1].sigmax = ValErr(0.731452, 0.00153027, 0)
reports[-1].sigmay = ValErr(0.830807, 0.00173812, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00152341, 0.00155711, 0.000205359, -0.000574927, 0.000359553, 0.000531133, 0.000193508, -0.00119107, 0.000359553, 0.000531133, 0.000193508, -0.00119107, 0.00155128, 0.00124542, 0.000187817, -0.00120026, 0.00155128, 0.00124542, 0.000187817, -0.00120026, 0.731446, 0.830815, 0.0036608, 0.0128937, 0.731446, 0.830815, 0.0036608, 0.0128937)

reports.append(Report(577634304, ("DT", 1, 1, 11), "MBwhDst1sec11"))
reports[-1].posNum = 113654
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000836024, 0.0021879, 0), \
                           ValErr(0.000243887, 0.00245315, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.31126e-05, 3.45249e-05, 0), \
                           -265842, 113654, 113654, -nan)
reports[-1].sigmax = ValErr(0.734248, 0.00154005, 0)
reports[-1].sigmay = ValErr(0.82702, 0.00173464, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00234462, 0.00204738, -0.00014005, 0.000615003, 0.000570491, 0.000250087, -0.000128405, 3.89919e-05, 0.000570491, 0.000250087, -0.000128405, 3.89919e-05, -0.000333546, -0.0020053, -0.00012473, 4.24063e-05, -0.000333546, -0.0020053, -0.00012473, 4.24063e-05, 0.734251, 0.827022, 0.00367594, 0.0129166, 0.734251, 0.827022, 0.00367594, 0.0129166)

reports.append(Report(577896448, ("DT", 1, 1, 12), "MBwhDst1sec12"))
reports[-1].posNum = 113479
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000142796, 0.00217652, 0), \
                           ValErr(-0.000254149, 0.00246631, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.38261e-05, 3.44643e-05, 0), \
                           -265318, 113479, 113479, -nan)
reports[-1].sigmax = ValErr(0.730156, 0.00153271, 0)
reports[-1].sigmay = ValErr(0.830817, 0.001744, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00146535, -0.00206941, -0.000836267, -0.000162878, 0.000279666, -0.000255111, -0.000836674, -0.000838894, 0.000279666, -0.000255111, -0.000836674, -0.000838894, -0.00118697, 0.00154435, -0.000829302, -0.000831185, -0.00118697, 0.00154435, -0.000829302, -0.000831185, 0.730148, 0.830828, 0.00364863, 0.0129058, 0.730148, 0.830828, 0.00364863, 0.0129058)

reports.append(Report(579207168, ("DT", 1, 2, 1), "MBwhDst2sec01"))
reports[-1].posNum = 103076
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000347146, 0.00307995, 0), \
                           ValErr(0.000145631, 0.00333779, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.77305e-05, 4.16912e-05, 0), \
                           -298234, 103076, 103076, -nan)
reports[-1].sigmax = ValErr(0.986876, 0.0021736, 0)
reports[-1].sigmay = ValErr(1.07109, 0.00235906, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00330718, -0.00196972, -0.000758979, 0.00012911, -0.000171478, 5.14184e-05, -0.000755723, -0.000278704, -0.000171478, 5.14184e-05, -0.000755723, -0.000278704, 0.001292, 0.000669126, -0.000761072, -0.000269743, 0.001292, 0.000669126, -0.000761072, -0.000269743, 0.986865, 1.0711, 0.00393241, 0.011843, 0.986865, 1.0711, 0.00393241, 0.011843)

reports.append(Report(579469312, ("DT", 1, 2, 2), "MBwhDst2sec02"))
reports[-1].posNum = 103883
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000741556, 0.00306333, 0), \
                           ValErr(7.89672e-05, 0.00334541, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.60054e-05, 4.1605e-05, 0), \
                           -301072, 103883, 103883, -nan)
reports[-1].sigmax = ValErr(0.985478, 0.00216202, 0)
reports[-1].sigmay = ValErr(1.07782, 0.00236461, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.000749684, -0.000751669, 0.000172631, -7.51402e-05, 0.000579521, 0.000161052, 0.00017, -0.000463445, 0.000579521, 0.000161052, 0.00017, -0.000463445, 0.00200031, 0.000165118, 0.00016845, -0.000454525, 0.00200031, 0.000165118, 0.00016845, -0.000454525, 0.98548, 1.07782, 0.00390163, 0.0119654, 0.98548, 1.07782, 0.00390163, 0.0119654)

reports.append(Report(579731456, ("DT", 1, 2, 3), "MBwhDst2sec03"))
reports[-1].posNum = 104171
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-9.71459e-05, 0.00305949, 0), \
                           ValErr(-0.000490963, 0.00333352, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.25711e-05, 4.16027e-05, 0), \
                           -301675, 104171, 104171, -nan)
reports[-1].sigmax = ValErr(0.985479, 0.00215906, 0)
reports[-1].sigmay = ValErr(1.07542, 0.00235613, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00174999, -0.000607233, 0.000600951, -0.000776989, -0.000152383, -0.000459566, 0.000591658, -0.00116, -0.000152383, -0.000459566, 0.000591658, -0.00116, 0.00369223, -0.000181159, 0.000575781, -0.00115502, 0.00369223, -0.000181159, 0.000575781, -0.00115502, 0.985474, 1.07543, 0.0039207, 0.012001, 0.985474, 1.07543, 0.0039207, 0.012001)

reports.append(Report(579993600, ("DT", 1, 2, 4), "MBwhDst2sec04"))
reports[-1].posNum = 77443
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000214964, 0.00353427, 0), \
                           ValErr(0.000110416, 0.00390011, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.50092e-05, 5.34335e-05, 0), \
                           -224730, 77443, 77443, -nan)
reports[-1].sigmax = ValErr(0.982814, 0.00249728, 0)
reports[-1].sigmay = ValErr(1.08474, 0.00275627, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00214576, -0.00808836, 0.000576962, -0.00114702, -0.000260917, 0.000145803, 0.000560726, -0.00165419, -0.000260917, 0.000145803, 0.000560726, -0.00165419, 0.000339812, 0.00227224, 0.000557368, -0.00166412, 0.000339812, 0.00227224, 0.000557368, -0.00166412, 0.982811, 1.08474, 0.00385213, 0.0121432, 0.982811, 1.08474, 0.00385213, 0.0121432)

reports.append(Report(580255744, ("DT", 1, 2, 5), "MBwhDst2sec05"))
reports[-1].posNum = 104062
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000285989, 0.00308714, 0), \
                           ValErr(5.01824e-05, 0.00334515, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.10849e-05, 4.18487e-05, 0), \
                           -302548, 104062, 104062, -nan)
reports[-1].sigmax = ValErr(0.993791, 0.00217838, 0)
reports[-1].sigmay = ValErr(1.07868, 0.00236444, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00138759, -0.00106415, -7.42037e-05, 0.000312488, -0.000132036, -1.8506e-05, -8.51316e-05, -9.96917e-05, -0.000132036, -1.8506e-05, -8.51316e-05, -9.96917e-05, 0.00106282, 0.00453399, -8.92962e-05, -0.00013032, 0.00106282, 0.00453399, -8.92962e-05, -0.00013032, 0.993792, 1.07868, 0.00394476, 0.0119368, 0.993792, 1.07868, 0.00394476, 0.0119368)

reports.append(Report(580517888, ("DT", 1, 2, 6), "MBwhDst2sec06"))
reports[-1].posNum = 103881
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.00014133, 0.0030615, 0), \
                           ValErr(1.37981e-05, 0.00334985, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.69898e-05, 4.16852e-05, 0), \
                           -301085, 103881, 103881, -nan)
reports[-1].sigmax = ValErr(0.984455, 0.00215982, 0)
reports[-1].sigmay = ValErr(1.07913, 0.00236753, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0017952, 0.000773953, 0.00014484, -0.00057003, 0.000274603, -5.51072e-05, 0.000135263, -0.000973065, 0.000274603, -5.51072e-05, 0.000135263, -0.000973065, -0.000277099, 0.00493827, 0.000143246, -0.00100432, -0.000277099, 0.00493827, 0.000143246, -0.00100432, 0.984462, 1.07913, 0.00390704, 0.0118596, 0.984462, 1.07913, 0.00390704, 0.0118596)

reports.append(Report(580780032, ("DT", 1, 2, 7), "MBwhDst2sec07"))
reports[-1].posNum = 104388
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000313548, 0.00307339, 0), \
                           ValErr(7.42471e-05, 0.00333191, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(7.96614e-06, 4.15071e-05, 0), \
                           -302957, 104388, 104388, -nan)
reports[-1].sigmax = ValErr(0.991032, 0.00216895, 0)
reports[-1].sigmay = ValErr(1.07611, 0.00235516, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-8.01072e-05, -0.000822776, 0.000123311, -0.000261315, -0.000277155, 5.68556e-05, 0.000115244, -0.000673621, -0.000277155, 5.68556e-05, 0.000115244, -0.000673621, -0.00172205, -0.0022573, 0.000118327, -0.000660493, -0.00172205, -0.0022573, 0.000118327, -0.000660493, 0.991033, 1.07611, 0.00393222, 0.0118915, 0.991033, 1.07611, 0.00393222, 0.0118915)

reports.append(Report(581042176, ("DT", 1, 2, 8), "MBwhDst2sec08"))
reports[-1].posNum = 103427
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000301806, 0.0030843, 0), \
                           ValErr(-0.000152052, 0.00333468, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.13705e-05, 4.18002e-05, 0), \
                           -299633, 103427, 103427, -nan)
reports[-1].sigmax = ValErr(0.989691, 0.00217606, 0)
reports[-1].sigmay = ValErr(1.07201, 0.00235705, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0040009, 0.00109199, 0.000134784, 0.000449278, -0.000237363, -0.000176358, 0.000135386, 1.71205e-05, -0.000237363, -0.000176358, 0.000135386, 1.71205e-05, 0.000614263, 0.000178974, 0.000136073, 6.19449e-06, 0.000614263, 0.000178974, 0.000136073, 6.19449e-06, 0.989687, 1.07201, 0.00393121, 0.0118404, 0.989687, 1.07201, 0.00393121, 0.0118404)

reports.append(Report(581304320, ("DT", 1, 2, 9), "MBwhDst2sec09"))
reports[-1].posNum = 104161
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000905358, 0.00155012, 0), \
                           ValErr(-0.000159271, 0.00331369, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.6527e-05, 4.13914e-05, 0), \
                           -301824, 104161, 104161, -nan)
reports[-1].sigmax = ValErr(0.991363, 0.00214435, 0)
reports[-1].sigmay = ValErr(1.07085, 0.0023448, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(7.81914e-05, 0.000213741, -5.88097e-05, -6.51374e-06, -0.000829412, -0.00019913, -5.10982e-05, -0.000418972, -0.000829412, -0.00019913, -5.10982e-05, -0.000418972, -0.000767203, 0.00358571, -5.52618e-05, -0.000433956, -0.000767203, 0.00358571, -5.52618e-05, -0.000433956, 0.991366, 1.07086, 0.00394425, 0.0118849, 0.991366, 1.07086, 0.00394425, 0.0118849)

reports.append(Report(581566464, ("DT", 1, 2, 10), "MBwhDst2sec10"))
reports[-1].posNum = 104116
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000158123, 0.00306685, 0), \
                           ValErr(-0.000638856, 0.00330984, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.12178e-06, 4.14572e-05, 0), \
                           -300959, 104116, 104116, -nan)
reports[-1].sigmax = ValErr(0.987551, 0.00216416, 0)
reports[-1].sigmay = ValErr(1.06743, 0.0023392, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.001688, 0.00418744, 2.55068e-05, -0.000295795, -0.000162948, -0.000647267, 3.72676e-05, -0.0006959, -0.000162948, -0.000647267, 3.72676e-05, -0.0006959, -0.000990233, -0.00530161, 3.9445e-05, -0.000687734, -0.000990233, -0.00530161, 3.9445e-05, -0.000687734, 0.98755, 1.06744, 0.00392833, 0.0119248, 0.98755, 1.06744, 0.00392833, 0.0119248)

reports.append(Report(581828608, ("DT", 1, 2, 11), "MBwhDst2sec11"))
reports[-1].posNum = 104770
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(9.22167e-05, 0.00296912, 0), \
                           ValErr(-0.000272554, 0.00329085, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.34635e-05, 4.12303e-05, 0), \
                           -303165, 104770, 104770, -nan)
reports[-1].sigmax = ValErr(0.989536, 0.00199401, 0)
reports[-1].sigmay = ValErr(1.06852, 0.00233373, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00167502, -0.000952688, -2.88728e-05, 0.000340622, 0.000241259, -0.000343724, -2.30512e-05, -3.83042e-05, 0.000241259, -0.000343724, -2.30512e-05, -3.83042e-05, 2.47443e-05, -8.63256e-05, -2.50435e-05, -4.9836e-05, 2.47443e-05, -8.63256e-05, -2.50435e-05, -4.9836e-05, 0.989524, 1.06853, 0.00393089, 0.0118565, 0.989524, 1.06853, 0.00393089, 0.0118565)

reports.append(Report(582090752, ("DT", 1, 2, 12), "MBwhDst2sec12"))
reports[-1].posNum = 104058
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000114905, 0.00306039, 0), \
                           ValErr(0.00010298, 0.00332298, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.21664e-05, 4.15358e-05, 0), \
                           -300929, 104058, 104058, -nan)
reports[-1].sigmax = ValErr(0.985072, 0.00215933, 0)
reports[-1].sigmay = ValErr(1.07154, 0.00234887, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00449651, -0.000467392, 0.000136122, 0.000382715, 0.000173635, 7.66215e-05, 0.000148991, 9.92175e-07, 0.000173635, 7.66215e-05, 0.000148991, 9.92175e-07, 0.000465589, -0.000298336, 0.000152131, -1.00289e-05, 0.000465589, -0.000298336, 0.000152131, -1.00289e-05, 0.985075, 1.07153, 0.00391717, 0.0119061, 0.985075, 1.07153, 0.00391717, 0.0119061)

reports.append(Report(583401472, ("DT", 1, 3, 1), "MBwhDst3sec01"))
reports[-1].posNum = 89184
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000446988, 0.00448941, 0), \
                           ValErr(-0.000872907, 0.00473641, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(7.64881e-06, 5.3583e-05, 0), \
                           -310041, 89184, 89184, -nan)
reports[-1].sigmax = ValErr(1.33986, 0.00317253, 0)
reports[-1].sigmay = ValErr(1.41337, 0.00334658, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00309645, 0.00252791, -0.000215535, 0.000295717, 0.000470295, -0.000846496, -0.000229068, 9.90115e-05, 0.000470295, -0.000846496, -0.000229068, 9.90115e-05, 0.00171198, -0.00244315, -0.000223168, 7.62295e-05, 0.00171198, -0.00244315, -0.000223168, 7.62295e-05, 1.33986, 1.41337, 0.0045621, 0.0108707, 1.33986, 1.41337, 0.0045621, 0.0108707)

reports.append(Report(583663616, ("DT", 1, 3, 2), "MBwhDst3sec02"))
reports[-1].posNum = 88649
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(5.736e-06, 0.00169524, 0), \
                           ValErr(-6.12922e-05, 0.0047515, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.44714e-06, 5.37418e-05, 0), \
                           -308183, 88649, 88649, -nan)
reports[-1].sigmax = ValErr(1.33855, 0.00317981, 0)
reports[-1].sigmay = ValErr(1.41479, 0.00336137, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00211883, 0.00245419, 0.000341519, 0.000323481, 4.196e-05, -4.04654e-05, 0.000348282, 0.000133459, 4.196e-05, -4.04654e-05, 0.000348282, 0.000133459, 0.00172444, 0.0050108, 0.000342355, 0.000113022, 0.00172444, 0.0050108, 0.000342355, 0.000113022, 1.33855, 1.41479, 0.00454544, 0.0108478, 1.33855, 1.41479, 0.00454544, 0.0108478)

reports.append(Report(583925760, ("DT", 1, 3, 3), "MBwhDst3sec03"))
reports[-1].posNum = 89555
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.00010774, 0.00168423, 0), \
                           ValErr(0.000107429, 0.00474507, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.00088e-06, 5.35338e-05, 0), \
                           -311493, 89555, 89555, -nan)
reports[-1].sigmax = ValErr(1.34091, 0.00318034, 0)
reports[-1].sigmay = ValErr(1.41483, 0.00335585, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00630225, -0.00223317, -0.000311101, -0.000176879, -0.000115159, 0.00011533, -0.000318938, -0.000390521, -0.000115159, 0.00011533, -0.000318938, -0.000390521, -0.000941141, 0.00133482, -0.000307192, -0.000417371, -0.000941141, 0.00133482, -0.000307192, -0.000417371, 1.34091, 1.41483, 0.0045335, 0.0109052, 1.34091, 1.41483, 0.0045335, 0.0109052)

reports.append(Report(584187904, ("DT", 1, 3, 4), "MBwhDst3sec04"))
reports[-1].posNum = 66607
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.00125164, 0.00507156, 0), \
                           ValErr(0.000229777, 0.00539533, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.46141e-05, 6.57695e-05, 0), \
                           -228668, 66607, 66607, -nan)
reports[-1].sigmax = ValErr(1.30909, 0.00357822, 0)
reports[-1].sigmay = ValErr(1.38526, 0.00378274, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.000935468, -0.00284587, -0.000289875, -0.000126715, 0.00127473, 0.000293405, -0.000269463, -0.00039255, 0.00127473, 0.000293405, -0.000269463, -0.00039255, -0.00195902, 0.00710836, -0.000267852, -0.000463422, -0.00195902, 0.00710836, -0.000267852, -0.000463422, 1.30909, 1.38526, 0.00437325, 0.0110996, 1.30909, 1.38526, 0.00437325, 0.0110996)

reports.append(Report(584450048, ("DT", 1, 3, 5), "MBwhDst3sec05"))
reports[-1].posNum = 88690
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000268788, 0.00168128, 0), \
                           ValErr(0.000448586, 0.00473579, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.42261e-05, 5.37129e-05, 0), \
                           -308375, 88690, 88690, -nan)
reports[-1].sigmax = ValErr(1.34456, 0.00319447, 0)
reports[-1].sigmay = ValErr(1.40925, 0.00334595, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000520477, -0.00536855, 0.000273791, -0.000143038, -0.000397997, 0.000287957, 0.00026844, -0.000406565, -0.000397997, 0.000287957, 0.00026844, -0.000406565, -0.000505902, 0.000325521, 0.000270924, -0.000432519, -0.000505902, 0.000325521, 0.000270924, -0.000432519, 1.34456, 1.40925, 0.00454924, 0.0109385, 1.34456, 1.40925, 0.00454924, 0.0109385)

reports.append(Report(584712192, ("DT", 1, 3, 6), "MBwhDst3sec06"))
reports[-1].posNum = 88764
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000300637, 0.0045237, 0), \
                           ValErr(-0.000724747, 0.00475142, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.29777e-05, 5.39117e-05, 0), \
                           -309101, 88764, 88764, -nan)
reports[-1].sigmax = ValErr(1.34688, 0.00319667, 0)
reports[-1].sigmay = ValErr(1.41426, 0.00335657, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00394301, -0.00128283, 0.000286328, -5.18815e-05, 0.000262389, -0.000774702, 0.000265029, -0.000312154, 0.000262389, -0.000774702, 0.000265029, -0.000312154, 0.00379483, -0.00287454, 0.000262845, -0.000352381, 0.00379483, -0.00287454, 0.000262845, -0.000352381, 1.34688, 1.41426, 0.00458481, 0.011041, 1.34688, 1.41426, 0.00458481, 0.011041)

reports.append(Report(584974336, ("DT", 1, 3, 7), "MBwhDst3sec07"))
reports[-1].posNum = 88598
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.00034818, 0.00451338, 0), \
                           ValErr(0.00022499, 0.00476049, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.16526e-05, 5.38752e-05, 0), \
                           -308347, 88598, 88598, -nan)
reports[-1].sigmax = ValErr(1.34253, 0.00318932, 0)
reports[-1].sigmay = ValErr(1.41604, 0.00336394, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.000992705, -0.00369577, 7.40141e-05, -0.000389194, 0.000282649, 0.00015535, 6.21977e-05, -0.000622675, 0.000282649, 0.00015535, 6.21977e-05, -0.000622675, 0.00102834, -0.005614, 8.26498e-05, -0.000599923, 0.00102834, -0.005614, 8.26498e-05, -0.000599923, 1.34253, 1.41604, 0.00454299, 0.0109739, 1.34253, 1.41604, 0.00454299, 0.0109739)

reports.append(Report(585236480, ("DT", 1, 3, 8), "MBwhDst3sec08"))
reports[-1].posNum = 88976
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000685686, 0.00452753, 0), \
                           ValErr(2.86466e-05, 0.0047292, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.62277e-06, 5.36895e-05, 0), \
                           -309707, 88976, 88976, -nan)
reports[-1].sigmax = ValErr(1.3496, 0.0031993, 0)
reports[-1].sigmay = ValErr(1.40932, 0.0033409, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00346452, 0.00353695, 0.000322847, 0.000291611, -0.000682385, 3.41017e-05, 0.000335981, 0.000106177, -0.000682385, 3.41017e-05, 0.000335981, 0.000106177, -0.00318204, -0.00227937, 0.00034941, 9.12437e-05, -0.00318204, -0.00227937, 0.00034941, 9.12437e-05, 1.3496, 1.40932, 0.00457898, 0.0109659, 1.3496, 1.40932, 0.00457898, 0.0109659)

reports.append(Report(585498624, ("DT", 1, 3, 9), "MBwhDst3sec09"))
reports[-1].posNum = 88413
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000197413, 0.00451554, 0), \
                           ValErr(-0.000278814, 0.00475365, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(8.9399e-06, 5.38688e-05, 0), \
                           -307416, 88413, 88413, -nan)
reports[-1].sigmax = ValErr(1.34168, 0.00319065, 0)
reports[-1].sigmay = ValErr(1.41234, 0.00335868, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00179986, -0.00215433, 1.58451e-05, 0.00061279, -0.000168338, -0.000247408, -6.3068e-06, 0.000371744, -0.000168338, -0.000247408, -6.3068e-06, 0.000371744, -0.00168155, 0.00342558, 5.17491e-06, 0.000363554, -0.00168155, 0.00342558, 5.17491e-06, 0.000363554, 1.34168, 1.41234, 0.00455188, 0.0109097, 1.34168, 1.41234, 0.00455188, 0.0109097)

reports.append(Report(585760768, ("DT", 1, 3, 10), "MBwhDst3sec10"))
reports[-1].posNum = 89412
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000698302, 0.00450145, 0), \
                           ValErr(0.000776064, 0.00473112, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.67223e-05, 5.36375e-05, 0), \
                           -311210, 89412, 89412, -nan)
reports[-1].sigmax = ValErr(1.34509, 0.00318088, 0)
reports[-1].sigmay = ValErr(1.41382, 0.00334341, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00134728, 0.00230614, -0.000756402, -0.000280582, -0.000583668, 0.000890637, -0.00076179, -0.000474833, -0.000583668, 0.000890637, -0.00076179, -0.000474833, -0.000954724, 0.00252433, -0.000753814, -0.000464344, -0.000954724, 0.00252433, -0.000753814, -0.000464344, 1.34507, 1.41384, 0.00457564, 0.0109461, 1.34507, 1.41384, 0.00457564, 0.0109461)

reports.append(Report(586022912, ("DT", 1, 3, 11), "MBwhDst3sec11"))
reports[-1].posNum = 89131
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000329194, 0.00450744, 0), \
                           ValErr(0.00113319, 0.00472952, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.94024e-05, 5.3761e-05, 0), \
                           -310001, 89131, 89131, -nan)
reports[-1].sigmax = ValErr(1.34481, 0.0031852, 0)
reports[-1].sigmay = ValErr(1.41045, 0.00334068, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00159196, 0.00298536, 0.000654704, 0.00087212, 0.000209254, 0.000971417, 0.000644873, 0.000644106, 0.000209254, 0.000971417, 0.000644873, 0.000644106, -0.000912409, 0.000893484, 0.000642034, 0.000651695, -0.000912409, 0.000893484, 0.000642034, 0.000651695, 1.3448, 1.41046, 0.00455246, 0.0108761, 1.3448, 1.41046, 0.00455246, 0.0108761)

reports.append(Report(586285056, ("DT", 1, 3, 12), "MBwhDst3sec12"))
reports[-1].posNum = 88571
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.00109701, 0.00168672, 0), \
                           ValErr(-0.000320939, 0.00477854, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.42034e-05, 5.3916e-05, 0), \
                           -308044, 88571, 88571, -nan)
reports[-1].sigmax = ValErr(1.33441, 0.0031635, 0)
reports[-1].sigmay = ValErr(1.42129, 0.00337783, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00301852, -0.00469496, -7.84896e-06, -0.000755782, 0.00107508, -0.000375614, -1.63857e-06, -0.000954677, 0.00107508, -0.000375614, -1.63857e-06, -0.000954677, 0.000261139, -0.00123878, 2.39718e-06, -0.000947305, 0.000261139, -0.00123878, 2.39718e-06, -0.000947305, 1.3344, 1.4213, 0.00453945, 0.0109133, 1.3344, 1.4213, 0.00453945, 0.0109133)

reports.append(Report(575045632, ("DT", 2, 1, 1), "MBwhEst1sec01"))
reports[-1].posNum = 69419
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000224443, 0.00323189, 0), \
                           ValErr(0.00105827, 0.00465592, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.48766e-06, 5.497e-05, 0), \
                           -197783, 69419, 69419, -nan)
reports[-1].sigmax = ValErr(0.824423, 0.00221257, 0)
reports[-1].sigmay = ValErr(1.22668, 0.00329214, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00147769, 0.0026005, -0.000586032, -0.0024399, -0.000202273, 0.00106001, -0.000578574, -0.000979568, -0.000202273, 0.00106001, -0.000578574, -0.000979568, -0.00274698, 0.00488934, -0.000570907, -0.00121642, -0.00274698, 0.00488934, -0.000570907, -0.00121642, 0.824423, 1.22668, 0.00410446, 0.0288232, 0.824423, 1.22668, 0.00410446, 0.0288232)

reports.append(Report(575307776, ("DT", 2, 1, 2), "MBwhEst1sec02"))
reports[-1].posNum = 66527
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000514552, 0.0033082, 0), \
                           ValErr(-0.000728155, 0.00475652, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.51777e-05, 5.62025e-05, 0), \
                           -189232, 66527, 66527, -nan)
reports[-1].sigmax = ValErr(0.820723, 0.00225002, 0)
reports[-1].sigmay = ValErr(1.22645, 0.00336233, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(1.40614e-05, 0.00349448, -0.000871725, -0.00318533, 5.34977e-05, -0.000806354, -0.000885192, -0.00195441, 5.34977e-05, -0.000806354, -0.000885192, -0.00195441, -0.00018634, 0.000330514, -0.00088276, -0.00218966, -0.00018634, 0.000330514, -0.00088276, -0.00218966, 0.820718, 1.22646, 0.0040773, 0.0289141, 0.820718, 1.22646, 0.0040773, 0.0289141)

reports.append(Report(575569920, ("DT", 2, 1, 3), "MBwhEst1sec03"))
reports[-1].posNum = 65695
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(6.68656e-05, 0.00337083, 0), \
                           ValErr(-0.000623018, 0.00477218, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.5373e-05, 5.73199e-05, 0), \
                           -186913, 65695, 65695, -nan)
reports[-1].sigmax = ValErr(0.823547, 0.0022721, 0)
reports[-1].sigmay = ValErr(1.22314, 0.00337451, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00486564, 0.00310079, -0.000868424, -0.00386716, 0.000340549, -0.000626134, -0.000889642, -0.0025933, 0.000340549, -0.000626134, -0.000889642, -0.0025933, -0.00237924, -0.00388328, -0.000885636, -0.00269565, -0.00237924, -0.00388328, -0.000885636, -0.00269565, 0.82354, 1.22314, 0.00410493, 0.0287657, 0.82354, 1.22314, 0.00410493, 0.0287657)

reports.append(Report(575832064, ("DT", 2, 1, 4), "MBwhEst1sec04"))
reports[-1].posNum = 69282
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000437308, 0.00324627, 0), \
                           ValErr(-0.000537995, 0.00464429, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.91778e-06, 5.52642e-05, 0), \
                           -197346, 69282, 69282, -nan)
reports[-1].sigmax = ValErr(0.826791, 0.00222115, 0)
reports[-1].sigmay = ValErr(1.22234, 0.00328382, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00139663, 0.0042691, 0.000205173, -0.00155718, 0.000336929, -0.000539769, 0.000211757, -0.000198633, 0.000336929, -0.000539769, 0.000211757, -0.000198633, -7.40641e-05, 0.00108848, 0.000211201, -0.000429314, -7.40641e-05, 0.00108848, 0.000211201, -0.000429314, 0.826793, 1.22235, 0.00411047, 0.0287538, 0.826793, 1.22235, 0.00411047, 0.0287538)

reports.append(Report(576094208, ("DT", 2, 1, 5), "MBwhEst1sec05"))
reports[-1].posNum = 67108
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000874618, 0.00330914, 0), \
                           ValErr(-5.20462e-05, 0.00471139, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.59295e-05, 5.61268e-05, 0), \
                           -191047, 67108, 67108, -nan)
reports[-1].sigmax = ValErr(0.826865, 0.00225715, 0)
reports[-1].sigmay = ValErr(1.22029, 0.0033311, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00194132, -0.00127046, -0.000936498, -0.00133628, -0.000471131, -8.91963e-05, -0.000936389, -0.000121495, -0.000471131, -8.91963e-05, -0.000936389, -0.000121495, -0.00393808, 0.00482001, -0.000921357, -0.000261627, -0.00393808, 0.00482001, -0.000921357, -0.000261627, 0.826854, 1.22031, 0.0041136, 0.0287877, 0.826854, 1.22031, 0.0041136, 0.0287877)

reports.append(Report(576356352, ("DT", 2, 1, 6), "MBwhEst1sec06"))
reports[-1].posNum = 64407
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.00104522, 0.00244947, 0), \
                           ValErr(-0.00079646, 0.00471567, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.76855e-05, 5.74764e-05, 0), \
                           -182421, 64407, 64407, -nan)
reports[-1].sigmax = ValErr(0.819679, 0.00227991, 0)
reports[-1].sigmay = ValErr(1.21322, 0.00338108, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00319529, 0.00435964, 1.81357e-06, -0.00328215, 0.000715861, -0.00080863, -4.63921e-06, -0.00198207, 0.000715861, -0.00080863, -4.63921e-06, -0.00198207, -0.00116533, -0.00211645, -1.011e-06, -0.00206956, -0.00116533, -0.00211645, -1.011e-06, -0.00206956, 0.819678, 1.21322, 0.0040804, 0.0286827, 0.819678, 1.21322, 0.0040804, 0.0286827)

reports.append(Report(576618496, ("DT", 2, 1, 7), "MBwhEst1sec07"))
reports[-1].posNum = 69561
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000147235, 0.00323753, 0), \
                           ValErr(0.000474478, 0.00464099, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.90597e-06, 5.52025e-05, 0), \
                           -198188, 69561, 69561, -nan)
reports[-1].sigmax = ValErr(0.826272, 0.00221526, 0)
reports[-1].sigmay = ValErr(1.22395, 0.00328146, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00392533, 0.000830026, -0.000143552, -0.00149302, -8.95695e-05, 0.000478767, -0.000133061, -0.000125906, -8.95695e-05, 0.000478767, -0.000133061, -0.000125906, 0.0031889, 0.000618222, -0.000145489, -0.000325939, 0.0031889, 0.000618222, -0.000145489, -0.000325939, 0.826272, 1.22395, 0.00410895, 0.0288455, 0.826272, 1.22395, 0.00410895, 0.0288455)

reports.append(Report(576880640, ("DT", 2, 1, 8), "MBwhEst1sec08"))
reports[-1].posNum = 66839
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000615435, 0.0033279, 0), \
                           ValErr(-0.000474969, 0.0047626, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.55155e-05, 5.6648e-05, 0), \
                           -191081, 66839, 66839, -nan)
reports[-1].sigmax = ValErr(0.829537, 0.00226919, 0)
reports[-1].sigmay = ValErr(1.23102, 0.00336747, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0007955, 0.00725693, 0.00127535, -0.00281479, 6.20333e-05, -0.000416526, 0.00126676, -0.00163955, 6.20333e-05, -0.000416526, 0.00126676, -0.00163955, 0.000197035, -0.00664977, 0.00126898, -0.00182391, 0.000197035, -0.00664977, 0.00126898, -0.00182391, 0.829513, 1.23105, 0.00412053, 0.0288492, 0.829513, 1.23105, 0.00412053, 0.0288492)

reports.append(Report(577142784, ("DT", 2, 1, 9), "MBwhEst1sec09"))
reports[-1].posNum = 64783
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.00108247, 0.00339633, 0), \
                           ValErr(0.00126075, 0.0047522, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.1237e-05, 5.75326e-05, 0), \
                           -183590, 64783, 64783, -nan)
reports[-1].sigmax = ValErr(0.82351, 0.00228783, 0)
reports[-1].sigmay = ValErr(1.20952, 0.00336024, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0022328, 0.00430432, 0.000345884, -0.00133822, 0.000700742, 0.00124899, 0.000315705, 2.94258e-05, 0.000700742, 0.00124899, 0.000315705, 2.94258e-05, -0.00334737, 0.00693561, 0.000335931, -0.000182057, -0.00334737, 0.00693561, 0.000335931, -0.000182057, 0.823508, 1.20953, 0.00410017, 0.0285809, 0.823508, 1.20953, 0.00410017, 0.0285809)

reports.append(Report(577404928, ("DT", 2, 1, 10), "MBwhEst1sec10"))
reports[-1].posNum = 68619
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000644294, 0.00323992, 0), \
                           ValErr(0.000442228, 0.00469485, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.89943e-05, 5.51532e-05, 0), \
                           -195450, 68619, 68619, -nan)
reports[-1].sigmax = ValErr(0.821729, 0.0022183, 0)
reports[-1].sigmay = ValErr(1.22973, 0.00331976, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-1.90899e-06, 0.0107233, 0.000815754, -0.00242716, 0.000218371, 0.000413154, 0.000831671, -0.000976245, 0.000218371, 0.000413154, 0.000831671, -0.000976245, -0.00234293, 0.00445004, 0.00084665, -0.00122155, -0.00234293, 0.00445004, 0.00084665, -0.00122155, 0.821717, 1.22976, 0.00409039, 0.0288645, 0.821717, 1.22976, 0.00409039, 0.0288645)

reports.append(Report(577667072, ("DT", 2, 1, 11), "MBwhEst1sec11"))
reports[-1].posNum = 67363
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-6.71733e-05, 0.00330765, 0), \
                           ValErr(0.00148219, 0.00473129, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.7185e-06, 5.62808e-05, 0), \
                           -192132, 67363, 67363, -nan)
reports[-1].sigmax = ValErr(0.826205, 0.00225097, 0)
reports[-1].sigmay = ValErr(1.22781, 0.0033451, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00278045, 0.00414895, -0.000329202, -0.00292203, -9.45139e-05, 0.00148787, -0.000305369, -0.0015135, -9.45139e-05, 0.00148787, -0.000305369, -0.0015135, -0.000806327, 0.000569345, -0.000304525, -0.00174555, -0.000806327, 0.000569345, -0.000304525, -0.00174555, 0.826204, 1.22781, 0.00411076, 0.0287755, 0.826204, 1.22781, 0.00411076, 0.0287755)

reports.append(Report(577929216, ("DT", 2, 1, 12), "MBwhEst1sec12"))
reports[-1].posNum = 65294
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.00073321, 0.00339141, 0), \
                           ValErr(-0.000751048, 0.00475241, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.68115e-05, 5.75403e-05, 0), \
                           -185229, 65294, 65294, -nan)
reports[-1].sigmax = ValErr(0.822634, 0.00227858, 0)
reports[-1].sigmay = ValErr(1.21435, 0.00336174, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.000180713, -0.000823598, 0.00107119, -0.002899, -5.25584e-05, -0.000734927, 0.00107553, -0.00165423, -5.25584e-05, -0.000734927, 0.00107553, -0.00165423, 0.00108302, -0.00335453, 0.00106623, -0.00183005, 0.00108302, -0.00335453, 0.00106623, -0.00183005, 0.822656, 1.21432, 0.0040887, 0.0287087, 0.822656, 1.21432, 0.0040887, 0.0287087)

reports.append(Report(579239936, ("DT", 2, 2, 1), "MBwhEst2sec01"))
reports[-1].posNum = 81129
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000495541, 0.0020517, 0), \
                           ValErr(-0.000113602, 0.00484984, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.38342e-05, 5.67059e-05, 0), \
                           -269701, 81129, 81129, -nan)
reports[-1].sigmax = ValErr(1.08622, 0.00267542, 0)
reports[-1].sigmay = ValErr(1.49745, 0.00369672, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000547866, -0.000795575, 0.000621912, 0.000268836, 0.000288304, -3.2821e-05, 0.000630158, -0.000124449, 0.000288304, -3.2821e-05, 0.000630158, -0.000124449, 0.000433224, 0.00498302, 0.000626656, -0.000266649, 0.000433224, 0.00498302, 0.000626656, -0.000266649, 1.08622, 1.49746, 0.00433615, 0.0233474, 1.08622, 1.49746, 0.00433615, 0.0233474)

reports.append(Report(579502080, ("DT", 2, 2, 2), "MBwhEst2sec02"))
reports[-1].posNum = 79847
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000197751, 0.00320911, 0), \
                           ValErr(-0.000694764, 0.00499482, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.46863e-05, 5.90258e-05, 0), \
                           -265053, 79847, 79847, -nan)
reports[-1].sigmax = ValErr(1.0853, 0.00267167, 0)
reports[-1].sigmay = ValErr(1.49151, 0.00355378, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00466728, -0.000148967, 0.000206926, -0.00129148, 2.37229e-05, -0.000633524, 0.00020561, -0.00169451, 2.37229e-05, -0.000633524, 0.00020561, -0.00169451, -0.00501486, 0.00587232, 0.000230367, -0.00178381, -0.00501486, 0.00587232, 0.000230367, -0.00178381, 1.0853, 1.4915, 0.00433425, 0.0231489, 1.0853, 1.4915, 0.00433425, 0.0231489)

reports.append(Report(579764224, ("DT", 2, 2, 3), "MBwhEst2sec03"))
reports[-1].posNum = 80524
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(8.96438e-05, 0.00185027, 0), \
                           ValErr(-0.000825602, 0.00500732, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.77919e-05, 5.68239e-05, 0), \
                           -266913, 80524, 80524, -nan)
reports[-1].sigmax = ValErr(1.07857, 0.00268694, 0)
reports[-1].sigmay = ValErr(1.4936, 0.0037251, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000242296, -0.00734272, 0.000332384, -0.00138979, -0.000206724, -0.000744053, 0.000351196, -0.00185139, -0.000206724, -0.000744053, 0.000351196, -0.00185139, 0.000945938, -0.00233912, 0.000341231, -0.00187374, 0.000945938, -0.00233912, 0.000341231, -0.00187374, 1.07857, 1.49361, 0.00431316, 0.0232807, 1.07857, 1.49361, 0.00431316, 0.0232807)

reports.append(Report(580026368, ("DT", 2, 2, 4), "MBwhEst2sec04"))
reports[-1].posNum = 80307
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000414951, 0.00385821, 0), \
                           ValErr(0.000291597, 0.00526375, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.91619e-05, 5.90864e-05, 0), \
                           -266798, 80307, 80307, -nan)
reports[-1].sigmax = ValErr(1.08845, 0.00271595, 0)
reports[-1].sigmay = ValErr(1.49122, 0.00372098, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.000698722, 0.00742769, 0.000648374, -0.000362796, -0.000173657, 0.000206873, 0.00064567, -0.00078627, -0.000173657, 0.000206873, 0.00064567, -0.00078627, 0.00468967, 1.17811e-05, 0.000622078, -0.000876742, 0.00468967, 1.17811e-05, 0.000622078, -0.000876742, 1.08846, 1.49121, 0.00434659, 0.0232664, 1.08846, 1.49121, 0.00434659, 0.0232664)

reports.append(Report(580288512, ("DT", 2, 2, 5), "MBwhEst2sec05"))
reports[-1].posNum = 80843
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000685713, 0.00384089, 0), \
                           ValErr(-0.000579147, 0.00502291, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.14555e-05, 5.88215e-05, 0), \
                           -268418, 80843, 80843, -nan)
reports[-1].sigmax = ValErr(1.0866, 0.00269749, 0)
reports[-1].sigmay = ValErr(1.4908, 0.00370045, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00104141, -0.00241268, -0.00113264, -0.00143346, -0.000412791, -0.000663903, -0.00113146, -0.0017977, -0.000412791, -0.000663903, -0.00113146, -0.0017977, -0.00104016, -0.00327477, -0.00113183, -0.00190977, -0.00104016, -0.00327477, -0.00113183, -0.00190977, 1.08657, 1.49084, 0.00434657, 0.0232038, 1.08657, 1.49084, 0.00434657, 0.0232038)

reports.append(Report(580550656, ("DT", 2, 2, 6), "MBwhEst2sec06"))
reports[-1].posNum = 80495
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.0001307, 0.00383341, 0), \
                           ValErr(0.000385169, 0.00500006, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.35313e-05, 5.87397e-05, 0), \
                           -266860, 80495, 80495, -nan)
reports[-1].sigmax = ValErr(1.08299, 0.00269784, 0)
reports[-1].sigmay = ValErr(1.4883, 0.00370474, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00183106, 0.000835849, 0.000175003, -0.000196863, -0.000344395, 0.000459832, 0.00018125, -0.000537778, -0.000344395, 0.000459832, 0.00018125, -0.000537778, -0.000657671, -0.00145464, 0.000182013, -0.000533463, -0.000657671, -0.00145464, 0.000182013, -0.000533463, 1.08298, 1.48831, 0.00434396, 0.0231753, 1.08298, 1.48831, 0.00434396, 0.0231753)

reports.append(Report(580812800, ("DT", 2, 2, 7), "MBwhEst2sec07"))
reports[-1].posNum = 80458
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000771873, 0.00385134, 0), \
                           ValErr(-0.00128428, 0.00528307, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.61992e-05, 5.89448e-05, 0), \
                           -267594, 80458, 80458, -nan)
reports[-1].sigmax = ValErr(1.08749, 0.00271109, 0)
reports[-1].sigmay = ValErr(1.49801, 0.00373452, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00522953, -0.00370578, 0.00127472, -0.000977318, -0.000671675, -0.00132359, 0.00128951, -0.0014891, -0.000671675, -0.00132359, 0.00128951, -0.0014891, -0.00110074, -0.00356873, 0.00129753, -0.00159053, -0.00110074, -0.00356873, 0.00129753, -0.00159053, 1.0875, 1.498, 0.00433327, 0.0231483, 1.0875, 1.498, 0.00433327, 0.0231483)

reports.append(Report(581074944, ("DT", 2, 2, 8), "MBwhEst2sec08"))
reports[-1].posNum = 80786
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(5.65237e-05, 0.00181696, 0), \
                           ValErr(-0.000590833, 0.00501523, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.58834e-05, 3.34972e-05, 0), \
                           -268280, 80786, 80786, -nan)
reports[-1].sigmax = ValErr(1.08416, 0.00268378, 0)
reports[-1].sigmay = ValErr(1.49511, 0.00372002, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000681424, 0.00525436, 0.000541015, -0.000695229, -4.32632e-05, -0.00056098, 0.000531041, -0.000974914, -4.32632e-05, -0.00056098, 0.000531041, -0.000974914, 0.000423374, 0.00424105, 0.000527978, -0.00107078, 0.000423374, 0.00424105, 0.000527978, -0.00107078, 1.08416, 1.49511, 0.00433385, 0.0232279, 1.08416, 1.49511, 0.00433385, 0.0232279)

reports.append(Report(581337088, ("DT", 2, 2, 9), "MBwhEst2sec09"))
reports[-1].posNum = 80175
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000177686, 0.00192824, 0), \
                           ValErr(-0.000222356, 0.00503251, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.04213e-05, 5.62355e-05, 0), \
                           -266165, 80175, 80175, -nan)
reports[-1].sigmax = ValErr(1.08161, 0.00270176, 0)
reports[-1].sigmay = ValErr(1.49701, 0.00374162, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00333935, -0.000343994, 0.000117359, -0.00111169, -5.81087e-05, -0.000272915, 0.000114053, -0.00162141, -5.81087e-05, -0.000272915, 0.000114053, -0.00162141, -0.000285208, 0.00361666, 0.000118649, -0.00179788, -0.000285208, 0.00361666, 0.000118649, -0.00179788, 1.0816, 1.49702, 0.00433433, 0.0231527, 1.0816, 1.49702, 0.00433433, 0.0231527)

reports.append(Report(581599232, ("DT", 2, 2, 10), "MBwhEst2sec10"))
reports[-1].posNum = 79943
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000466637, 0.00385442, 0), \
                           ValErr(0.000555367, 0.0052798, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(8.4484e-06, 5.90221e-05, 0), \
                           -265366, 79943, 79943, -nan)
reports[-1].sigmax = ValErr(1.08457, 0.00271246, 0)
reports[-1].sigmay = ValErr(1.49239, 0.00373237, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.000949722, 0.00362125, -0.000608918, -0.000174265, -0.000411629, 0.000535494, -0.000604094, -0.000669331, -0.000411629, 0.000535494, -0.000604094, -0.000669331, -0.000961985, 0.00203192, -0.00059978, -0.000805654, -0.000961985, 0.00203192, -0.00059978, -0.000805654, 1.08457, 1.49239, 0.00433206, 0.0232582, 1.08457, 1.49239, 0.00433206, 0.0232582)

reports.append(Report(581861376, ("DT", 2, 2, 11), "MBwhEst2sec11"))
reports[-1].posNum = 81128
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000605332, 0.00196885, 0), \
                           ValErr(-0.000403267, 0.00495113, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.32009e-05, 5.66578e-05, 0), \
                           -270072, 81128, 81128, -nan)
reports[-1].sigmax = ValErr(1.09071, 0.00267765, 0)
reports[-1].sigmay = ValErr(1.4982, 0.00369949, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00371958, 0.000951042, 0.000356373, -0.00197426, 0.000338889, -0.000311333, 0.000355285, -0.00242001, 0.000338889, -0.000311333, 0.000355285, -0.00242001, -0.000347958, 0.00714533, 0.000347745, -0.0024605, -0.000347958, 0.00714533, 0.000347745, -0.0024605, 1.0907, 1.49821, 0.00435167, 0.0232282, 1.0907, 1.49821, 0.00435167, 0.0232282)

reports.append(Report(582123520, ("DT", 2, 2, 12), "MBwhEst2sec12"))
reports[-1].posNum = 80762
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000671595, 0.00383368, 0), \
                           ValErr(0.00147923, 0.00504913, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.3776e-06, 5.87789e-05, 0), \
                           -268023, 80762, 80762, -nan)
reports[-1].sigmax = ValErr(1.08606, 0.00266966, 0)
reports[-1].sigmay = ValErr(1.48922, 0.00370505, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00194927, 0.00715616, 0.000477268, 0.000896592, -0.000708579, 0.00149165, 0.000485683, 0.000509526, -0.000708579, 0.00149165, 0.000485683, 0.000509526, -0.00279013, 0.00318456, 0.000489563, 0.000399248, -0.00279013, 0.00318456, 0.000489563, 0.000399248, 1.08605, 1.48922, 0.00434067, 0.0232904, 1.08605, 1.48922, 0.00434067, 0.0232904)

reports.append(Report(583434240, ("DT", 2, 3, 1), "MBwhEst3sec01"))
reports[-1].posNum = 71308
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000426104, 0.00538069, 0), \
                           ValErr(5.56215e-06, 0.00681505, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.46701e-05, 7.18998e-05, 0), \
                           -270789, 71308, 71308, -nan)
reports[-1].sigmax = ValErr(1.43549, 0.00380123, 0)
reports[-1].sigmay = ValErr(1.81862, 0.00481573, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00220233, -0.00138982, -0.000445745, 0.000260779, 0.000479215, 5.62322e-05, -0.000440952, 0.00045055, 0.000479215, 5.62322e-05, -0.000440952, 0.00045055, -0.00104301, -0.000426015, -0.000431133, 0.000501056, -0.00104301, -0.000426015, -0.000431133, 0.000501056, 1.43548, 1.81862, 0.00488498, 0.0180075, 1.43548, 1.81862, 0.00488498, 0.0180075)

reports.append(Report(583696384, ("DT", 2, 3, 2), "MBwhEst3sec02"))
reports[-1].posNum = 71703
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000744107, 0.00534339, 0), \
                           ValErr(-0.000502865, 0.00684237, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.27338e-05, 7.17674e-05, 0), \
                           -272479, 71703, 71703, -nan)
reports[-1].sigmax = ValErr(1.42949, 0.00377485, 0)
reports[-1].sigmay = ValErr(1.8311, 0.00483536, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00603443, -0.00293936, 0.000279913, 0.000530065, -0.000668804, -0.000427256, 0.000277208, 0.000665284, -0.000668804, -0.000427256, 0.000277208, 0.000665284, -0.00651405, 0.0030068, 0.000292266, 0.000750277, -0.00651405, 0.0030068, 0.000292266, 0.000750277, 1.42949, 1.83109, 0.00485472, 0.0179574, 1.42949, 1.83109, 0.00485472, 0.0179574)

reports.append(Report(583958528, ("DT", 2, 3, 3), "MBwhEst3sec03"))
reports[-1].posNum = 71584
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000735569, 0.00535845, 0), \
                           ValErr(0.000629072, 0.0068285, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.73684e-05, 7.18582e-05, 0), \
                           -271942, 71584, 71584, -nan)
reports[-1].sigmax = ValErr(1.43198, 0.00378454, 0)
reports[-1].sigmay = ValErr(1.82574, 0.00482522, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00170054, 0.00217376, 0.00028954, -0.000474374, -0.000672241, 0.000682937, 0.000301209, -0.000372557, -0.000672241, 0.000682937, 0.000301209, -0.000372557, -0.00277836, 0.00144992, 0.000309397, -0.000285165, -0.00277836, 0.00144992, 0.000309397, -0.000285165, 1.43198, 1.82574, 0.0048409, 0.0180278, 1.43198, 1.82574, 0.0048409, 0.0180278)

reports.append(Report(584220672, ("DT", 2, 3, 4), "MBwhEst3sec04"))
reports[-1].posNum = 70923
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000425526, 0.00536765, 0), \
                           ValErr(-0.00107846, 0.00686516, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.11164e-05, 7.20154e-05, 0), \
                           -269280, 70923, 70923, -nan)
reports[-1].sigmax = ValErr(1.42797, 0.00379151, 0)
reports[-1].sigmay = ValErr(1.82698, 0.00485094, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000591663, 0.00107614, 0.000161401, -2.36047e-05, -0.000464411, -0.00111871, 0.000181582, 5.68011e-05, -0.000464411, -0.00111871, 0.000181582, 5.68011e-05, 0.00126423, 0.00706139, 0.00017485, 0.00011346, 0.00126423, 0.00706139, 0.00017485, 0.00011346, 1.42797, 1.82698, 0.00486511, 0.0180326, 1.42797, 1.82698, 0.00486511, 0.0180326)

reports.append(Report(584482816, ("DT", 2, 3, 5), "MBwhEst3sec05"))
reports[-1].posNum = 70479
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000462005, 0.00539296, 0), \
                           ValErr(0.000802825, 0.00688295, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.92084e-06, 7.23772e-05, 0), \
                           -267670, 70479, 70479, -nan)
reports[-1].sigmax = ValErr(1.43029, 0.0038096, 0)
reports[-1].sigmay = ValErr(1.82598, 0.00486354, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00752574, -0.00310653, 2.70213e-05, -3.61318e-05, -0.000479604, 0.000784914, 2.33363e-05, 6.62545e-05, -0.000479604, 0.000784914, 2.33363e-05, 6.62545e-05, 0.000895869, 0.00233134, 1.54984e-05, 0.000190329, 0.000895869, 0.00233134, 1.54984e-05, 0.000190329, 1.43029, 1.82598, 0.00486375, 0.0179682, 1.43029, 1.82598, 0.00486375, 0.0179682)

reports.append(Report(584744960, ("DT", 2, 3, 6), "MBwhEst3sec06"))
reports[-1].posNum = 70884
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000376703, 0.00539786, 0), \
                           ValErr(0.00179859, 0.006836, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.10296e-05, 7.18609e-05, 0), \
                           -269185, 70884, 70884, -nan)
reports[-1].sigmax = ValErr(1.43579, 0.00381346, 0)
reports[-1].sigmay = ValErr(1.81841, 0.00482972, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00366609, 0.00754352, 0.00089522, -0.000617899, -0.000469492, 0.0016779, 0.000879307, -0.000548396, -0.000469492, 0.0016779, 0.000879307, -0.000548396, 0.00248803, 0.00649892, 0.000875729, -0.00038786, 0.00248803, 0.00649892, 0.000875729, -0.00038786, 1.43577, 1.81842, 0.00489278, 0.0180136, 1.43577, 1.81842, 0.00489278, 0.0180136)

reports.append(Report(585007104, ("DT", 2, 3, 7), "MBwhEst3sec07"))
reports[-1].posNum = 70769
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.00106481, 0.00541648, 0), \
                           ValErr(-0.00147919, 0.00690923, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.77933e-05, 7.25925e-05, 0), \
                           -269643, 70769, 70769, -nan)
reports[-1].sigmax = ValErr(1.43922, 0.00382554, 0)
reports[-1].sigmay = ValErr(1.83714, 0.00488326, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00332337, -0.00232659, 0.000559082, -0.000445099, 0.000938218, -0.00159003, 0.000569653, -0.000324468, 0.000938218, -0.00159003, 0.000569653, -0.000324468, 0.00361899, -0.00088875, 0.000569809, -0.000262361, 0.00361899, -0.00088875, 0.000569809, -0.000262361, 1.43921, 1.83715, 0.00488639, 0.0181309, 1.43921, 1.83715, 0.00488639, 0.0181309)

reports.append(Report(585269248, ("DT", 2, 3, 8), "MBwhEst3sec08"))
reports[-1].posNum = 70924
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000320156, 0.00536327, 0), \
                           ValErr(0.00011851, 0.00687875, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.58879e-06, 7.20299e-05, 0), \
                           -269368, 70924, 70924, -nan)
reports[-1].sigmax = ValErr(1.42698, 0.00378885, 0)
reports[-1].sigmay = ValErr(1.83042, 0.00486008, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00137272, -0.000954624, 0.000508952, 0.000586521, -0.000334324, 9.39138e-05, 0.000499786, 0.000695261, -0.000334324, 9.39138e-05, 0.000499786, 0.000695261, -0.00537887, -0.000871714, 0.000509823, 0.000739094, -0.00537887, -0.000871714, 0.000509823, 0.000739094, 1.42698, 1.83042, 0.00485617, 0.0181386, 1.42698, 1.83042, 0.00485617, 0.0181386)

reports.append(Report(585531392, ("DT", 2, 3, 9), "MBwhEst3sec09"))
reports[-1].posNum = 71177
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000609267, 0.00536209, 0), \
                           ValErr(0.000550403, 0.00684367, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.47069e-06, 7.2171e-05, 0), \
                           -270200, 71177, 71177, -nan)
reports[-1].sigmax = ValErr(1.42898, 0.00378743, 0)
reports[-1].sigmay = ValErr(1.82454, 0.00483586, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00547931, -0.00399743, 0.000136066, -0.000638227, -0.000589882, 0.000569564, 0.000135112, -0.000609588, -0.000589882, 0.000569564, 0.000135112, -0.000609588, 0.00288228, 0.00265317, 0.000123959, -0.000449988, 0.00288228, 0.00265317, 0.000123959, -0.000449988, 1.42898, 1.82454, 0.00486694, 0.0179428, 1.42898, 1.82454, 0.00486694, 0.0179428)

reports.append(Report(585793536, ("DT", 2, 3, 10), "MBwhEst3sec10"))
reports[-1].posNum = 70100
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.00153043, 0.00536792, 0), \
                           ValErr(0.00228315, 0.00688633, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.18726e-06, 7.22365e-05, 0), \
                           -265548, 70100, 70100, -nan)
reports[-1].sigmax = ValErr(1.41968, 0.00379157, 0)
reports[-1].sigmay = ValErr(1.8218, 0.00486552, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000631834, 0.00508756, -0.000251222, -0.000673076, -0.00157582, 0.00224094, -0.000247246, -0.000624739, -0.00157582, 0.00224094, -0.000247246, -0.000624739, 0.00161079, 0.00648066, -0.000258479, -0.000511009, 0.00161079, 0.00648066, -0.000258479, -0.000511009, 1.41968, 1.8218, 0.00485191, 0.01801, 1.41968, 1.8218, 0.00485191, 0.01801)

reports.append(Report(586055680, ("DT", 2, 3, 11), "MBwhEst3sec11"))
reports[-1].posNum = 70531
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000108058, 0.00541063, 0), \
                           ValErr(-0.000226263, 0.00693065, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.74572e-05, 7.26294e-05, 0), \
                           -268658, 70531, 70531, -nan)
reports[-1].sigmax = ValErr(1.43583, 0.0038231, 0)
reports[-1].sigmay = ValErr(1.83944, 0.00489773, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00435155, -0.00609168, -0.000882489, -0.000325436, -2.63111e-05, -0.000134059, -0.000894903, -0.000261129, -2.63111e-05, -0.000134059, -0.000894903, -0.000261129, 0.00277506, 0.00354968, -0.000906464, -8.86409e-05, 0.00277506, 0.00354968, -0.000906464, -8.86409e-05, 1.43582, 1.83946, 0.00484874, 0.0180844, 1.43582, 1.83946, 0.00484874, 0.0180844)

reports.append(Report(586317824, ("DT", 2, 3, 12), "MBwhEst3sec12"))
reports[-1].posNum = 70917
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000271478, 0.00537118, 0), \
                           ValErr(-0.00175538, 0.00686308, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.60079e-06, 7.21067e-05, 0), \
                           -269295, 70917, 70917, -nan)
reports[-1].sigmax = ValErr(1.42901, 0.00379442, 0)
reports[-1].sigmay = ValErr(1.82663, 0.00485021, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.000953163, -0.00462512, 0.000151497, 0.000290514, 0.000280012, -0.00175823, 0.00015261, 0.000479034, 0.000280012, -0.00175823, 0.00015261, 0.000479034, -0.00358733, -0.00486374, 0.000164552, 0.000637151, -0.00358733, -0.00486374, 0.000164552, 0.000637151, 1.42901, 1.82662, 0.00485171, 0.0180354, 1.42901, 1.82662, 0.00485171, 0.0180354)

reports.append(Report(587497472, ("DT", -2, 4, 1), "MBwhAst4sec01"))
reports[-1].posNum = 101857
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.000956873, 0.00621896, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.3961e-06, 0.000126581, 0), \
                           -214321, 101857, 101857, -nan)
reports[-1].sigmaresid = ValErr(1.98416, 0.00439609, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00483097, None, 0.00105962, None, -0.000954699, None, 0.00104332, None, -0.000954699, None, 0.00104332, None, -0.0122539, None, 0.00106798, None, -0.0122539, None, 0.00106798, None, 1.98417, None, 0.00572309, None, 1.98417, None, 0.00572309, None)

reports.append(Report(587759616, ("DT", -2, 4, 2), "MBwhAst4sec02"))
reports[-1].posNum = 101349
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(8.51782e-05, 0.00625302, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.22852e-05, 0.000127444, 0), \
                           -213558, 101349, 101349, -nan)
reports[-1].sigmaresid = ValErr(1.99016, 0.00442042, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0028958, None, 0.000242995, None, 9.56834e-05, None, 0.000250863, None, 9.56834e-05, None, 0.000250863, None, -0.00216747, None, 0.000250843, None, -0.00216747, None, 0.000250843, None, 1.99016, None, 0.00575003, None, 1.99016, None, 0.00575003, None)

reports.append(Report(588021760, ("DT", -2, 4, 3), "MBwhAst4sec03"))
reports[-1].posNum = 102409
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.000671476, 0.00619249, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.08677e-06, 0.000126327, 0), \
                           -215315, 102409, 102409, -nan)
reports[-1].sigmaresid = ValErr(1.98091, 0.00437705, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00061821, None, -0.000657501, None, -0.000665299, None, -0.000662965, None, -0.000665299, None, -0.000662965, None, -0.00178722, None, -0.000648811, None, -0.00178722, None, -0.000648811, None, 1.98091, None, 0.00571116, None, 1.98091, None, 0.00571116, None)

reports.append(Report(588283904, ("DT", -2, 4, 4), "MBwhAst4sec04"))
reports[-1].posNum = 70618
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.00186082, 0.00763897, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.48821e-06, 0.00015553, 0), \
                           -150171, 70618, 70618, -nan)
reports[-1].sigmaresid = ValErr(2.0291, 0.00539922, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00062737, None, 5.35528e-05, None, 0.00187061, None, 7.2415e-05, None, 0.00187061, None, 7.2415e-05, None, -0.00675955, None, 9.88102e-05, None, -0.00675955, None, 9.88102e-05, None, 2.0291, None, 0.00583505, None, 2.0291, None, 0.00583505, None)

reports.append(Report(590643200, ("DT", -2, 4, 13), "MBwhAst4sec13"))
reports[-1].posNum = 71579
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.000525518, 0.00758296, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.86962e-05, 0.000154758, 0), \
                           -152175, 71579, 71579, -nan)
reports[-1].sigmaresid = ValErr(2.02797, 0.00535987, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00445143, None, 0.000375706, None, -0.00050545, None, 0.000406536, None, -0.00050545, None, 0.000406536, None, 0.0205581, None, 0.000352283, None, 0.0205581, None, 0.000352283, None, 2.02797, None, 0.00583436, None, 2.02797, None, 0.00583436, None)

reports.append(Report(588546048, ("DT", -2, 4, 5), "MBwhAst4sec05"))
reports[-1].posNum = 102132
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.000142748, 0.00622571, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(7.7362e-06, 0.000126775, 0), \
                           -215146, 102132, 102132, -nan)
reports[-1].sigmaresid = ValErr(1.98895, 0.00440076, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(9.80876e-05, None, -0.000690863, None, 0.000150479, None, -0.000703034, None, 0.000150479, None, -0.000703034, None, -2.89836e-05, None, -0.000698904, None, -2.89836e-05, None, -0.000698904, None, 1.98895, None, 0.0057304, None, 1.98895, None, 0.0057304, None)

reports.append(Report(588808192, ("DT", -2, 4, 6), "MBwhAst4sec06"))
reports[-1].posNum = 102807
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.00113354, 0.00619567, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.75419e-05, 0.000126202, 0), \
                           -216418, 102807, 102807, -nan)
reports[-1].sigmaresid = ValErr(1.98605, 0.00437989, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00218325, None, 0.000833291, None, -0.00110496, None, 0.000854765, None, -0.00110496, None, 0.000854765, None, 0.0074921, None, 0.000845419, None, 0.0074921, None, 0.000845419, None, 1.98605, None, 0.00571502, None, 1.98605, None, 0.00571502, None)

reports.append(Report(589070336, ("DT", -2, 4, 7), "MBwhAst4sec07"))
reports[-1].posNum = 102265
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.00204519, 0.00619695, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.19929e-05, 0.000126276, 0), \
                           -215018, 102265, 102265, -nan)
reports[-1].sigmaresid = ValErr(1.98104, 0.0043804, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00358602, None, -0.00112523, None, 0.00199064, None, -0.00112711, None, 0.00199064, None, -0.00112711, None, 0.00834284, None, -0.00115613, None, 0.00834284, None, -0.00115613, None, 1.98104, None, 0.0057175, None, 1.98104, None, 0.0057175, None)

reports.append(Report(589332480, ("DT", -2, 4, 8), "MBwhAst4sec08"))
reports[-1].posNum = 102230
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.000450186, 0.00619245, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.54154e-06, 0.000126351, 0), \
                           -214843, 102230, 102230, -nan)
reports[-1].sigmaresid = ValErr(1.97907, 0.00437681, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00552697, None, 0.00051469, None, -0.00044711, None, 0.00050263, None, -0.00044711, None, 0.00050263, None, 0.000919329, None, 0.000506919, None, 0.000919329, None, 0.000506919, None, 1.97908, None, 0.00572698, None, 1.97908, None, 0.00572698, None)

reports.append(Report(589594624, ("DT", -2, 4, 9), "MBwhAst4sec09"))
reports[-1].posNum = 42691
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.00153377, 0.00932292, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.30158e-06, 0.000190172, 0), \
                           -88548.4, 42691, 42691, -nan)
reports[-1].sigmaresid = ValErr(1.92559, 0.00658992, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00215952, None, -0.000163387, None, -0.00154613, None, -0.000171973, None, -0.00154613, None, -0.000171973, None, 0.001737, None, -0.000178219, None, 0.001737, None, -0.000178219, None, 1.92559, None, 0.00552598, None, 1.92559, None, 0.00552598, None)

reports.append(Report(589856768, ("DT", -2, 4, 10), "MBwhAst4sec10"))
reports[-1].posNum = 53773
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.00194698, 0.00860297, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(7.56251e-06, 0.000174685, 0), \
                           -113423, 53773, 53773, -nan)
reports[-1].sigmaresid = ValErr(1.99443, 0.00608164, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000246204, None, 0.000594049, None, -0.00194006, None, 0.000604697, None, -0.00194006, None, 0.000604697, None, 0.00277617, None, 0.000599153, None, 0.00277617, None, 0.000599153, None, 1.99443, None, 0.00575569, None, 1.99443, None, 0.00575569, None)

reports.append(Report(590905344, ("DT", -2, 4, 14), "MBwhAst4sec14"))
reports[-1].posNum = 54427
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.00040254, 0.00852142, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.01189e-05, 0.000174005, 0), \
                           -114613, 54427, 54427, -nan)
reports[-1].sigmaresid = ValErr(1.98749, 0.00602397, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000800951, None, 0.000423011, None, -0.000421976, None, 0.000424424, None, -0.000421976, None, 0.000424424, None, 0.00189403, None, 0.000418713, None, 0.00189403, None, 0.000418713, None, 1.98749, None, 0.00577468, None, 1.98749, None, 0.00577468, None)

reports.append(Report(590118912, ("DT", -2, 4, 11), "MBwhAst4sec11"))
reports[-1].posNum = 42949
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.000337364, 0.00931687, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.10218e-05, 0.000190164, 0), \
                           -89186.1, 42949, 42949, -nan)
reports[-1].sigmaresid = ValErr(1.93019, 0.0065858, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00726363, None, 0.000459838, None, -0.000393545, None, 0.000473715, None, -0.000393545, None, 0.000473715, None, 0.000373194, None, 0.000475984, None, 0.000373194, None, 0.000475984, None, 1.93019, None, 0.00553348, None, 1.93019, None, 0.00553348, None)

reports.append(Report(590381056, ("DT", -2, 4, 12), "MBwhAst4sec12"))
reports[-1].posNum = 102346
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.0010325, 0.00616748, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.28474e-05, 0.000125451, 0), \
                           -214749, 102346, 102346, -nan)
reports[-1].sigmaresid = ValErr(1.97254, 0.00435989, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00603087, None, 0.000251918, None, 0.00105792, None, 0.000250751, None, 0.00105792, None, 0.000250751, None, -0.00832638, None, 0.000271535, None, -0.00832638, None, 0.000271535, None, 1.97254, None, 0.00569501, None, 1.97254, None, 0.00569501, None)

reports.append(Report(587530240, ("DT", -1, 4, 1), "MBwhBst4sec01"))
reports[-1].posNum = 119755
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.00114996, 0.00546512, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.92405e-05, 0.000111276, 0), \
                           -246236, 119755, 119755, -nan)
reports[-1].sigmaresid = ValErr(1.89123, 0.00386439, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00101879, None, 8.13691e-05, None, 0.00115249, None, 7.70409e-05, None, 0.00115249, None, 7.70409e-05, None, 0.00282961, None, 8.42025e-05, None, 0.00282961, None, 8.42025e-05, None, 1.89123, None, 0.00546677, None, 1.89123, None, 0.00546677, None)

reports.append(Report(587792384, ("DT", -1, 4, 2), "MBwhBst4sec02"))
reports[-1].posNum = 119120
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.000487313, 0.00545622, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.0391e-05, 0.000111072, 0), \
                           -244420, 119120, 119120, -nan)
reports[-1].sigmaresid = ValErr(1.88314, 0.00385812, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00331307, None, -0.000223265, None, -0.000487655, None, -0.000216381, None, -0.000487655, None, -0.000216381, None, -0.00457138, None, -0.000207956, None, -0.00457138, None, -0.000207956, None, 1.88314, None, 0.00543024, None, 1.88314, None, 0.00543024, None)

reports.append(Report(588054528, ("DT", -1, 4, 3), "MBwhBst4sec03"))
reports[-1].posNum = 89965
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.000387633, 0.00616399, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.32112e-05, 0.000164504, 0), \
                           -182921, 89965, 89965, -nan)
reports[-1].sigmaresid = ValErr(1.84838, 0.00435753, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00382303, None, 0.000568721, None, 0.000356613, None, 0.000567154, None, 0.000356613, None, 0.000567154, None, -0.00591564, None, 0.000573326, None, -0.00591564, None, 0.000573326, None, 1.84839, None, 0.00531973, None, 1.84839, None, 0.00531973, None)

reports.append(Report(588316672, ("DT", -1, 4, 4), "MBwhBst4sec04"))
reports[-1].posNum = 81011
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.000791046, 0.00672776, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.63089e-05, 0.000137188, 0), \
                           -167579, 81011, 81011, -nan)
reports[-1].sigmaresid = ValErr(1.91488, 0.00475723, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00533157, None, 0.000337204, None, 0.000787015, None, 0.000354331, None, 0.000787015, None, 0.000354331, None, -0.00365914, None, 0.000377925, None, -0.00365914, None, 0.000377925, None, 1.91488, None, 0.00550751, None, 1.91488, None, 0.00550751, None)

reports.append(Report(590675968, ("DT", -1, 4, 13), "MBwhBst4sec13"))
reports[-1].posNum = 82921
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.00211408, 0.0066681, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.15798e-05, 0.000136011, 0), \
                           -171758, 82921, 82921, -nan)
reports[-1].sigmaresid = ValErr(1.92015, 0.00471506, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00497747, None, 0.00123944, None, 0.00211193, None, 0.00123567, None, 0.00211193, None, 0.00123567, None, 0.00607333, None, 0.00121811, None, 0.00607333, None, 0.00121811, None, 1.92015, None, 0.00554986, None, 1.92015, None, 0.00554986, None)

reports.append(Report(588578816, ("DT", -1, 4, 5), "MBwhBst4sec05"))
reports[-1].posNum = 119286
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.000470255, 0.00546695, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.9455e-06, 0.000111621, 0), \
                           -245076, 119286, 119286, -nan)
reports[-1].sigmaresid = ValErr(1.88813, 0.00386565, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0114916, None, -0.000219312, None, 0.00046525, None, -0.000211241, None, 0.00046525, None, -0.000211241, None, 0.00399644, None, -0.000214687, None, 0.00399644, None, -0.000214687, None, 1.88813, None, 0.00547145, None, 1.88813, None, 0.00547145, None)

reports.append(Report(588840960, ("DT", -1, 4, 6), "MBwhBst4sec06"))
reports[-1].posNum = 120012
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.00014391, 0.00546937, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.0394e-05, 0.000111684, 0), \
                           -246987, 120012, 120012, -nan)
reports[-1].sigmaresid = ValErr(1.89474, 0.00386743, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00565002, None, 0.000475536, None, -0.000144275, None, 0.000488258, None, -0.000144275, None, 0.000488258, None, 0.000197104, None, 0.000492162, None, 0.000197104, None, 0.000492162, None, 1.89474, None, 0.00547459, None, 1.89474, None, 0.00547459, None)

reports.append(Report(589103104, ("DT", -1, 4, 7), "MBwhBst4sec07"))
reports[-1].posNum = 118589
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.000846231, 0.00546225, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.68542e-06, 0.000111661, 0), \
                           -243196, 118589, 118589, -nan)
reports[-1].sigmaresid = ValErr(1.88101, 0.00386238, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00554253, None, -4.18914e-05, None, 0.000842991, None, -4.56474e-05, None, 0.000842991, None, -4.56474e-05, None, 0.00716423, None, -6.06472e-05, None, 0.00716423, None, -6.06472e-05, None, 1.88101, None, 0.005434, None, 1.88101, None, 0.005434, None)

reports.append(Report(589365248, ("DT", -1, 4, 8), "MBwhBst4sec08"))
reports[-1].posNum = 120359
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.000536914, 0.00543386, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.00068e-05, 0.000111015, 0), \
                           -247090, 120359, 120359, -nan)
reports[-1].sigmaresid = ValErr(1.88514, 0.00384228, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00166973, None, -0.000222061, None, 0.000531092, None, -0.000216125, None, 0.000531092, None, -0.000216125, None, 0.00267494, None, -0.000222992, None, 0.00267494, None, -0.000222992, None, 1.88514, None, 0.00544548, None, 1.88514, None, 0.00544548, None)

reports.append(Report(589627392, ("DT", -1, 4, 9), "MBwhBst4sec09"))
reports[-1].posNum = 50561
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-3.96821e-05, 0.00813435, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.17992e-06, 0.000165915, 0), \
                           -102272, 50561, 50561, -nan)
reports[-1].sigmaresid = ValErr(1.82905, 0.00575179, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00136656, None, -4.09662e-05, None, -4.09512e-05, None, -3.43028e-05, None, -4.09512e-05, None, -3.43028e-05, None, -0.000583611, None, -2.0115e-05, None, -0.000583611, None, -2.0115e-05, None, 1.82905, None, 0.00527633, None, 1.82905, None, 0.00527633, None)

reports.append(Report(589889536, ("DT", -1, 4, 10), "MBwhBst4sec10"))
reports[-1].posNum = 63644
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.00111543, 0.00744134, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.52094e-05, 0.00015205, 0), \
                           -130391, 63644, 63644, -nan)
reports[-1].sigmaresid = ValErr(1.87727, 0.00526178, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.012214, None, -9.43862e-05, None, 0.0011106, None, -0.000115294, None, 0.0011106, None, -0.000115294, None, -0.00321558, None, -0.000115988, None, -0.00321558, None, -0.000115988, None, 1.87727, None, 0.00544099, None, 1.87727, None, 0.00544099, None)

reports.append(Report(590938112, ("DT", -1, 4, 14), "MBwhBst4sec14"))
reports[-1].posNum = 63365
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.000399077, 0.00756838, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.92632e-05, 0.000154528, 0), \
                           -130752, 63365, 63365, -nan)
reports[-1].sigmaresid = ValErr(1.90512, 0.00535157, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.002112, None, 0.000546722, None, -0.00040234, None, 0.000555756, None, -0.00040234, None, 0.000555756, None, 0.00770765, None, 0.000535987, None, 0.00770765, None, 0.000535987, None, 1.90512, None, 0.00551642, None, 1.90512, None, 0.00551642, None)

reports.append(Report(590151680, ("DT", -1, 4, 11), "MBwhBst4sec11"))
reports[-1].posNum = 50106
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.00100064, 0.00820246, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.1566e-06, 0.000167772, 0), \
                           -101541, 50106, 50106, -nan)
reports[-1].sigmaresid = ValErr(1.83599, 0.00579976, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00679178, None, 9.06224e-06, None, 0.000995192, None, 3.0232e-05, None, 0.000995192, None, 3.0232e-05, None, 0.00716667, None, 2.90759e-06, None, 0.00716667, None, 2.90759e-06, None, 1.83599, None, 0.00527393, None, 1.83599, None, 0.00527393, None)

reports.append(Report(590413824, ("DT", -1, 4, 12), "MBwhBst4sec12"))
reports[-1].posNum = 119366
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.000616136, 0.00542266, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.24611e-06, 0.000110837, 0), \
                           -244307, 119366, 119366, -nan)
reports[-1].sigmaresid = ValErr(1.87342, 0.00383424, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00362449, None, -0.000532724, None, 0.000612657, None, -0.000530634, None, 0.000612657, None, -0.000530634, None, -0.00014944, None, -0.000529673, None, -0.00014944, None, -0.000529673, None, 1.87341, None, 0.00542107, None, 1.87341, None, 0.00542107, None)

reports.append(Report(587563008, ("DT", 0, 4, 1), "MBwhCst4sec01"))
reports[-1].posNum = 127919
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.000781204, 0.00526329, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.86466e-05, 0.000107106, 0), \
                           -262420, 127919, 127919, -nan)
reports[-1].sigmaresid = ValErr(1.88235, 0.00372149, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000420432, None, 0.000414045, None, 0.000798971, None, 0.000411874, None, 0.000798971, None, 0.000411874, None, -0.00471991, None, 0.000439476, None, -0.00471991, None, 0.000439476, None, 1.88235, None, 0.00550069, None, 1.88235, None, 0.00550069, None)

reports.append(Report(587825152, ("DT", 0, 4, 2), "MBwhCst4sec02"))
reports[-1].posNum = 127567
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.00144712, 0.00522898, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.53385e-05, 0.000106408, 0), \
                           -260682, 127567, 127567, -nan)
reports[-1].sigmaresid = ValErr(1.86742, 0.00369706, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0013624, None, 0.000779016, None, 0.00143409, None, 0.000779261, None, 0.00143409, None, 0.000779261, None, 0.00623727, None, 0.000756225, None, 0.00623727, None, 0.000756225, None, 1.86742, None, 0.00548035, None, 1.86742, None, 0.00548035, None)

reports.append(Report(588087296, ("DT", 0, 4, 3), "MBwhCst4sec03"))
reports[-1].posNum = 127586
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-2.62676e-05, 0.00523605, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.37712e-06, 0.000106188, 0), \
                           -260914, 127586, 127586, -nan)
reports[-1].sigmaresid = ValErr(1.87024, 0.00370238, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00396019, None, 0.000561909, None, -2.47326e-05, None, 0.000559655, None, -2.47326e-05, None, 0.000559655, None, 0.00317808, None, 0.000536889, None, 0.00317808, None, 0.000536889, None, 1.87023, None, 0.00546915, None, 1.87023, None, 0.00546915, None)

reports.append(Report(588349440, ("DT", 0, 4, 4), "MBwhCst4sec04"))
reports[-1].posNum = 88090
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.000223546, 0.00649395, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.07584e-05, 0.000132188, 0), \
                           -182793, 88090, 88090, -nan)
reports[-1].sigmaresid = ValErr(1.92732, 0.00459172, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00832166, None, -0.000523406, None, 0.00021958, None, -0.000517336, None, 0.00021958, None, -0.000517336, None, -0.00298834, None, -0.000508297, None, -0.00298834, None, -0.000508297, None, 1.92732, None, 0.0056191, None, 1.92732, None, 0.0056191, None)

reports.append(Report(590708736, ("DT", 0, 4, 13), "MBwhCst4sec13"))
reports[-1].posNum = 88851
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.000893619, 0.0064219, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(8.31932e-06, 0.000130477, 0), \
                           -183761, 88851, 88851, -nan)
reports[-1].sigmaresid = ValErr(1.91411, 0.00454072, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00868729, None, -0.000567878, None, 0.000881727, None, -0.000550428, None, 0.000881727, None, -0.000550428, None, 0.00474498, None, -0.000543827, None, 0.00474498, None, -0.000543827, None, 1.9141, None, 0.00557929, None, 1.9141, None, 0.00557929, None)

reports.append(Report(588611584, ("DT", 0, 4, 5), "MBwhCst4sec05"))
reports[-1].posNum = 127999
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.000252908, 0.00522277, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.59787e-05, 0.000106202, 0), \
                           -261630, 127999, 127999, -nan)
reports[-1].sigmaresid = ValErr(1.86837, 0.0036927, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00920091, None, -0.000259726, None, -0.000261806, None, -0.000259661, None, -0.000261806, None, -0.000259661, None, 0.000643403, None, -0.000257185, None, 0.000643403, None, -0.000257185, None, 1.86837, None, 0.00545586, None, 1.86837, None, 0.00545586, None)

reports.append(Report(588873728, ("DT", 0, 4, 6), "MBwhCst4sec06"))
reports[-1].posNum = 126946
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.00044342, 0.00526175, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.89759e-05, 0.000106857, 0), \
                           -259903, 126946, 126946, -nan)
reports[-1].sigmaresid = ValErr(1.87463, 0.00372042, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00658668, None, 0.000488027, None, -0.000451281, None, 0.000482325, None, -0.000451281, None, 0.000482325, None, 0.0030703, None, 0.000467641, None, 0.0030703, None, 0.000467641, None, 1.87463, None, 0.00549343, None, 1.87463, None, 0.00549343, None)

reports.append(Report(589135872, ("DT", 0, 4, 7), "MBwhCst4sec07"))
reports[-1].posNum = 127415
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.000559593, 0.0052311, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.93129e-05, 0.000106404, 0), \
                           -260345, 127415, 127415, -nan)
reports[-1].sigmaresid = ValErr(1.86702, 0.00369848, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000320348, None, -0.000151023, None, -0.000573089, None, -0.000135901, None, -0.000573089, None, -0.000135901, None, 0.00163584, None, -0.000140269, None, 0.00163584, None, -0.000140269, None, 1.86702, None, 0.00546176, None, 1.86702, None, 0.00546176, None)

reports.append(Report(589398016, ("DT", 0, 4, 8), "MBwhCst4sec08"))
reports[-1].posNum = 128253
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.000674249, 0.00518718, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.23639e-05, 0.000105332, 0), \
                           -261405, 128253, 128253, -nan)
reports[-1].sigmaresid = ValErr(1.85755, 0.00366769, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000248256, None, 0.000836032, None, 0.000665967, None, 0.000838351, None, 0.000665967, None, 0.000838351, None, -3.67202e-06, None, 0.000840274, None, -3.67202e-06, None, 0.000840274, None, 1.85755, None, 0.00545616, None, 1.85755, None, 0.00545616, None)

reports.append(Report(589660160, ("DT", 0, 4, 9), "MBwhCst4sec09"))
reports[-1].posNum = 54028
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.000396823, 0.00779149, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.00018e-05, 0.00015846, 0), \
                           -108749, 54028, 54028, -nan)
reports[-1].sigmaresid = ValErr(1.81102, 0.00550934, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00384805, None, 0.000245426, None, 0.000393102, None, 0.000249783, None, 0.000393102, None, 0.000249783, None, 0.00532302, None, 0.000236973, None, 0.00532302, None, 0.000236973, None, 1.81102, None, 0.00526426, None, 1.81102, None, 0.00526426, None)

reports.append(Report(589922304, ("DT", 0, 4, 10), "MBwhCst4sec10"))
reports[-1].posNum = 67602
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.000895114, 0.0072337, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.64325e-06, 0.000147297, 0), \
                           -138616, 67602, 67602, -nan)
reports[-1].sigmaresid = ValErr(1.8805, 0.0051142, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00457392, None, 0.000545824, None, 0.000891116, None, 0.000537648, None, 0.000891116, None, 0.000537648, None, -0.00189213, None, 0.000540516, None, -0.00189213, None, 0.000540516, None, 1.8805, None, 0.00555712, None, 1.8805, None, 0.00555712, None)

reports.append(Report(590970880, ("DT", 0, 4, 14), "MBwhCst4sec14"))
reports[-1].posNum = 67941
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.000165964, 0.00721919, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000105014, 0.000146646, 0), \
                           -139354, 67941, 67941, -nan)
reports[-1].sigmaresid = ValErr(1.88169, 0.00510465, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00218923, None, 0.000234993, None, 0.000141477, None, 0.000240564, None, 0.000141477, None, 0.000240564, None, 0.000951295, None, 0.000241519, None, 0.000951295, None, 0.000241519, None, 1.88169, None, 0.00553207, None, 1.88169, None, 0.00553207, None)

reports.append(Report(590184448, ("DT", 0, 4, 11), "MBwhCst4sec11"))
reports[-1].posNum = 54521
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.0004177, 0.0077523, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.07576e-05, 0.000157653, 0), \
                           -109710, 54521, 54521, -nan)
reports[-1].sigmaresid = ValErr(1.80999, 0.00548125, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00750434, None, -7.78285e-05, None, -0.000409981, None, -6.99676e-05, None, -0.000409981, None, -6.99676e-05, None, 0.00128714, None, -7.48615e-05, None, 0.00128714, None, -7.48615e-05, None, 1.80999, None, 0.00526918, None, 1.80999, None, 0.00526918, None)

reports.append(Report(590446592, ("DT", 0, 4, 12), "MBwhCst4sec12"))
reports[-1].posNum = 127023
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.000497581, 0.00522419, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.38946e-06, 0.000106109, 0), \
                           -259190, 127023, 127023, -nan)
reports[-1].sigmaresid = ValErr(1.86182, 0.00369387, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000463932, None, 0.000365871, None, -0.000498369, None, 0.000359092, None, -0.000498369, None, 0.000359092, None, -0.000900674, None, 0.000367014, None, -0.000900674, None, 0.000367014, None, 1.86182, None, 0.00547355, None, 1.86182, None, 0.00547355, None)

reports.append(Report(587595776, ("DT", 1, 4, 1), "MBwhDst4sec01"))
reports[-1].posNum = 119014
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.000323859, 0.00544978, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.88212e-05, 0.000110996, 0), \
                           -244007, 119014, 119014, -nan)
reports[-1].sigmaresid = ValErr(1.88005, 0.0038535, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00297593, None, 0.000585014, None, 0.000328124, None, 0.000593808, None, 0.000328124, None, 0.000593808, None, -6.21528e-05, None, 0.000578006, None, -6.21528e-05, None, 0.000578006, None, 1.88005, None, 0.00542383, None, 1.88005, None, 0.00542383, None)

reports.append(Report(587857920, ("DT", 1, 4, 2), "MBwhDst4sec02"))
reports[-1].posNum = 119824
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.000103774, 0.0054384, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.40008e-05, 0.000110942, 0), \
                           -245822, 119824, 119824, -nan)
reports[-1].sigmaresid = ValErr(1.88248, 0.00384542, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00263025, None, -0.000229035, None, -9.96045e-05, None, -0.000211735, None, -9.96045e-05, None, -0.000211735, None, 0.00318063, None, -0.00022854, None, 0.00318063, None, -0.00022854, None, 1.88248, None, 0.00545375, None, 1.88248, None, 0.00545375, None)

reports.append(Report(588120064, ("DT", 1, 4, 3), "MBwhDst4sec03"))
reports[-1].posNum = 119671
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.00033409, 0.00544111, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.35107e-05, 0.000111046, 0), \
                           -245494, 119671, 119671, -nan)
reports[-1].sigmaresid = ValErr(1.88226, 0.00384742, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00305312, None, -4.79818e-05, None, 0.000330582, None, -6.33309e-05, None, 0.000330582, None, -6.33309e-05, None, 0.00524297, None, -9.15081e-05, None, 0.00524297, None, -9.15081e-05, None, 1.88226, None, 0.00542093, None, 1.88226, None, 0.00542093, None)

reports.append(Report(588382208, ("DT", 1, 4, 4), "MBwhDst4sec04"))
reports[-1].posNum = 62503
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.00161426, 0.0076238, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.38638e-05, 0.000204532, 0), \
                           -128989, 62503, 62503, -nan)
reports[-1].sigmaresid = ValErr(1.90557, 0.00538964, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00764502, None, -0.000375565, None, -0.001648, None, -0.000341745, None, -0.001648, None, -0.000341745, None, 0.00737648, None, -0.000375059, None, 0.00737648, None, -0.000375059, None, 1.90557, None, 0.0055197, None, 1.90557, None, 0.0055197, None)

reports.append(Report(590741504, ("DT", 1, 4, 13), "MBwhDst4sec13"))
reports[-1].posNum = 77502
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.00104877, 0.00720612, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.80615e-05, 0.000148132, 0), \
                           -160080, 77502, 77502, -nan)
reports[-1].sigmaresid = ValErr(1.90896, 0.00484794, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000853236, None, 0.00027043, None, 0.00146813, None, 0.000264687, None, 0.00146813, None, 0.000264687, None, 0.00338771, None, 0.000263335, None, 0.00338771, None, 0.000263335, None, 1.90896, None, 0.00549932, None, 1.90896, None, 0.00549932, None)

reports.append(Report(588644352, ("DT", 1, 4, 5), "MBwhDst4sec05"))
reports[-1].posNum = 119440
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.00131309, 0.0054749, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.28671e-05, 0.000111978, 0), \
                           -245643, 119440, 119440, -nan)
reports[-1].sigmaresid = ValErr(1.89209, 0.00387126, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00230951, None, -5.87413e-05, None, -0.00131931, None, -8.19574e-05, None, -0.00131931, None, -8.19574e-05, None, 0.00208524, None, -7.98071e-05, None, 0.00208524, None, -7.98071e-05, None, 1.89209, None, 0.00543577, None, 1.89209, None, 0.00543577, None)

reports.append(Report(588906496, ("DT", 1, 4, 6), "MBwhDst4sec06"))
reports[-1].posNum = 119943
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.00145875, 0.00546704, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.67796e-05, 0.000111721, 0), \
                           -246756, 119943, 119943, -nan)
reports[-1].sigmaresid = ValErr(1.89333, 0.00386566, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0026308, None, 0.000427787, None, -0.00145015, None, 0.000435759, None, -0.00145015, None, 0.000435759, None, -0.00493212, None, 0.000439599, None, -0.00493212, None, 0.000439599, None, 1.89333, None, 0.00545923, None, 1.89333, None, 0.00545923, None)

reports.append(Report(589168640, ("DT", 1, 4, 7), "MBwhDst4sec07"))
reports[-1].posNum = 118879
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.000999466, 0.00547167, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.11529e-05, 0.000111942, 0), \
                           -244141, 118879, 118879, -nan)
reports[-1].sigmaresid = ValErr(1.88656, 0.00386904, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00487102, None, 0.000722943, None, -0.00100121, None, 0.000740403, None, -0.00100121, None, 0.000740403, None, -0.00411517, None, 0.000750867, None, -0.00411517, None, 0.000750867, None, 1.88656, None, 0.00544245, None, 1.88656, None, 0.00544245, None)

reports.append(Report(589430784, ("DT", 1, 4, 8), "MBwhDst4sec08"))
reports[-1].posNum = 119641
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.000959713, 0.0054412, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.93499e-05, 0.00011097, 0), \
                           -245419, 119641, 119641, -nan)
reports[-1].sigmaresid = ValErr(1.88204, 0.00384745, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00206013, None, -3.26211e-05, None, -0.000951774, None, -4.66168e-05, None, -0.000951774, None, -4.66168e-05, None, 0.00656662, None, -5.37185e-05, None, 0.00656662, None, -5.37185e-05, None, 1.88204, None, 0.00545804, None, 1.88204, None, 0.00545804, None)

reports.append(Report(589692928, ("DT", 1, 4, 9), "MBwhDst4sec09"))
reports[-1].posNum = 50354
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.00130728, 0.0081472, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(9.65133e-06, 0.000166132, 0), \
                           -101828, 50354, 50354, -nan)
reports[-1].sigmaresid = ValErr(1.82816, 0.00576079, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00132266, None, 0.000569837, None, -0.00130262, None, 0.000588899, None, -0.00130262, None, 0.000588899, None, -0.00456855, None, 0.000604482, None, -0.00456855, None, 0.000604482, None, 1.82816, None, 0.00526005, None, 1.82816, None, 0.00526005, None)

reports.append(Report(589955072, ("DT", 1, 4, 10), "MBwhDst4sec10"))
reports[-1].posNum = 63656
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.00259058, 0.00753362, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.66739e-05, 0.000153825, 0), \
                           -131206, 63656, 63656, -nan)
reports[-1].sigmaresid = ValErr(1.90072, 0.005327, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00723277, None, 0.000181657, None, -0.00258485, None, 0.000155715, None, -0.00258485, None, 0.000155715, None, -0.00180338, None, 0.000158173, None, -0.00180338, None, 0.000158173, None, 1.90072, None, 0.00550545, None, 1.90072, None, 0.00550545, None)

reports.append(Report(591003648, ("DT", 1, 4, 14), "MBwhDst4sec14"))
reports[-1].posNum = 63546
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.000806026, 0.00751931, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.12823e-05, 0.000153654, 0), \
                           -130804, 63546, 63546, -nan)
reports[-1].sigmaresid = ValErr(1.89548, 0.00531691, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00647877, None, -7.17587e-05, None, -0.000797093, None, -7.01592e-05, None, -0.000797093, None, -7.01592e-05, None, -0.00126663, None, -6.95408e-05, None, -0.00126663, None, -6.95408e-05, None, 1.89548, None, 0.00551452, None, 1.89548, None, 0.00551452, None)

reports.append(Report(590217216, ("DT", 1, 4, 11), "MBwhDst4sec11"))
reports[-1].posNum = 50558
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.000946112, 0.00812881, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.88119e-05, 0.000166473, 0), \
                           -102230, 50558, 50558, -nan)
reports[-1].sigmaresid = ValErr(1.82777, 0.00574791, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0123065, None, 0.000102703, None, -0.000947665, None, 0.000104999, None, -0.000947665, None, 0.000104999, None, -0.000282375, None, 0.000106908, None, -0.000282375, None, 0.000106908, None, 1.82777, None, 0.00524242, None, 1.82777, None, 0.00524242, None)

reports.append(Report(590479360, ("DT", 1, 4, 12), "MBwhDst4sec12"))
reports[-1].posNum = 120150
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(4.48143e-05, 0.00541217, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.76923e-05, 0.00011058, 0), \
                           -246076, 120150, 120150, -nan)
reports[-1].sigmaresid = ValErr(1.87599, 0.00382696, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00260372, None, 0.00039695, None, 4.67924e-05, None, 0.000407121, None, 4.67924e-05, None, 0.000407121, None, -0.0067467, None, 0.000426851, None, -0.0067467, None, 0.000426851, None, 1.87599, None, 0.00544241, None, 1.87599, None, 0.00544241, None)

reports.append(Report(587628544, ("DT", 2, 4, 1), "MBwhEst4sec01"))
reports[-1].posNum = 102451
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.000410127, 0.00622291, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.15369e-05, 0.000126594, 0), \
                           -215930, 102451, 102451, -nan)
reports[-1].sigmaresid = ValErr(1.99114, 0.00439874, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00323809, None, -0.000289549, None, -0.000455753, None, -0.000265158, None, -0.000455753, None, -0.000265158, None, 0.00650147, None, -0.000278717, None, 0.00650147, None, -0.000278717, None, 1.99113, None, 0.00573214, None, 1.99113, None, 0.00573214, None)

reports.append(Report(587890688, ("DT", 2, 4, 2), "MBwhEst4sec02"))
reports[-1].posNum = 102786
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.000745079, 0.00616492, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.78388e-05, 0.000125462, 0), \
                           -215829, 102786, 102786, -nan)
reports[-1].sigmaresid = ValErr(1.97555, 0.0043572, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00227663, None, 0.000541175, None, -0.000784673, None, 0.000544437, None, -0.000784673, None, 0.000544437, None, 0.00525141, None, 0.000517267, None, 0.00525141, None, 0.000517267, None, 1.97555, None, 0.00570615, None, 1.97555, None, 0.00570615, None)

reports.append(Report(588152832, ("DT", 2, 4, 3), "MBwhEst4sec03"))
reports[-1].posNum = 102959
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.000805807, 0.00614719, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.29305e-05, 0.000125443, 0), \
                           -215986, 102959, 102959, -nan)
reports[-1].sigmaresid = ValErr(1.97161, 0.00434483, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00658303, None, -0.000462288, None, 0.000777077, None, -0.000490325, None, 0.000777077, None, -0.000490325, None, 0.00267424, None, -0.000514089, None, 0.00267424, None, -0.000514089, None, 1.97161, None, 0.00566602, None, 1.97161, None, 0.00566602, None)

reports.append(Report(588414976, ("DT", 2, 4, 4), "MBwhEst4sec04"))
reports[-1].posNum = 70767
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.00061333, 0.00762767, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.28668e-05, 0.000155288, 0), \
                           -150463, 70767, 70767, -nan)
reports[-1].sigmaresid = ValErr(2.02838, 0.00539162, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00568455, None, -0.00153683, None, 0.000562919, None, -0.00152333, None, 0.000562919, None, -0.00152333, None, 0.00429893, None, -0.00154518, None, 0.00429893, None, -0.00154518, None, 2.02838, None, 0.00586179, None, 2.02838, None, 0.00586179, None)

reports.append(Report(590774272, ("DT", 2, 4, 13), "MBwhEst4sec13"))
reports[-1].posNum = 70521
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.00098913, 0.00769261, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.33742e-08, 0.00015651, 0), \
                           -150414, 70521, 70521, -nan)
reports[-1].sigmaresid = ValErr(2.04207, 0.00543745, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000383887, None, -0.000692444, None, 0.000990489, None, -0.000723167, None, 0.000990489, None, -0.000723167, None, -0.0144964, None, -0.000678743, None, -0.0144964, None, -0.000678743, None, 2.04207, None, 0.00586381, None, 2.04207, None, 0.00586381, None)

reports.append(Report(588677120, ("DT", 2, 4, 5), "MBwhEst4sec05"))
reports[-1].posNum = 101659
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.00113468, 0.00623864, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.52681e-05, 0.000127294, 0), \
                           -214117, 101659, 101659, -nan)
reports[-1].sigmaresid = ValErr(1.98832, 0.00440959, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00324116, None, -0.000361329, None, -0.00111068, None, -0.000363338, None, -0.00111068, None, -0.000363338, None, -0.00932167, None, -0.000346227, None, -0.00932167, None, -0.000346227, None, 1.98832, None, 0.00573481, None, 1.98832, None, 0.00573481, None)

reports.append(Report(588939264, ("DT", 2, 4, 6), "MBwhEst4sec06"))
reports[-1].posNum = 102104
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.000100583, 0.00622654, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.40441e-05, 0.000127036, 0), \
                           -215080, 102104, 102104, -nan)
reports[-1].sigmaresid = ValErr(1.98882, 0.00440107, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00519011, None, -0.000188714, None, 8.57539e-05, None, -0.00018629, None, 8.57539e-05, None, -0.00018629, None, -0.00640731, None, -0.000172631, None, -0.00640731, None, -0.000172631, None, 1.98882, None, 0.00573302, None, 1.98882, None, 0.00573302, None)

reports.append(Report(589201408, ("DT", 2, 4, 7), "MBwhEst4sec07"))
reports[-1].posNum = 101846
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.00104318, 0.00626017, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.22894e-06, 0.000127286, 0), \
                           -214961, 101846, 101846, -nan)
reports[-1].sigmaresid = ValErr(1.99713, 0.00442507, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00143743, None, -0.000720441, None, 0.00104653, None, -0.000729962, None, 0.00104653, None, -0.000729962, None, -0.000411948, None, -0.000725718, None, -0.000411948, None, -0.000725718, None, 1.99713, None, 0.00575436, None, 1.99713, None, 0.00575436, None)

reports.append(Report(589463552, ("DT", 2, 4, 8), "MBwhEst4sec08"))
reports[-1].posNum = 102175
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.000317981, 0.00620216, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.17665e-05, 0.000126846, 0), \
                           -214871, 102175, 102175, -nan)
reports[-1].sigmaresid = ValErr(1.98185, 0.00438414, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00243204, None, 0.000348548, None, 0.000266924, None, 0.000341664, None, 0.000266924, None, 0.000341664, None, -0.00313235, None, 0.000350989, None, -0.00313235, None, 0.000350989, None, 1.98185, None, 0.00574068, None, 1.98185, None, 0.00574068, None)

reports.append(Report(589725696, ("DT", 2, 4, 9), "MBwhEst4sec09"))
reports[-1].posNum = 43278
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.000107401, 0.00925541, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.13655e-05, 0.000188135, 0), \
                           -89748.6, 43278, 43278, -nan)
reports[-1].sigmaresid = ValErr(1.92482, 0.00654246, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00127239, None, -0.000200306, None, 0.000129309, None, -0.000226201, None, 0.000129309, None, -0.000226201, None, -0.00985285, None, -0.00021092, None, -0.00985285, None, -0.00021092, None, 1.92482, None, 0.00552534, None, 1.92482, None, 0.00552534, None)

reports.append(Report(589987840, ("DT", 2, 4, 10), "MBwhEst4sec10"))
reports[-1].posNum = 53973
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.00084123, 0.00857248, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.89424e-06, 0.00017503, 0), \
                           -113742, 53973, 53973, -nan)
reports[-1].sigmaresid = ValErr(1.99064, 0.00605883, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00256688, None, 0.000516212, None, -0.000856986, None, 0.000511744, None, -0.000856986, None, 0.000511744, None, 0.00654291, None, 0.000482103, None, 0.00654291, None, 0.000482103, None, 1.99064, None, 0.00579375, None, 1.99064, None, 0.00579375, None)

reports.append(Report(591036416, ("DT", 2, 4, 14), "MBwhEst4sec14"))
reports[-1].posNum = 54031
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.000374027, 0.00851756, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.80972e-05, 0.000173146, 0), \
                           -113549, 54031, 54031, -nan)
reports[-1].sigmaresid = ValErr(1.97905, 0.00602034, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00209354, None, -0.000509988, None, 0.000296671, None, -0.00051348, None, 0.000296671, None, -0.00051348, None, -0.00234266, None, -0.000510535, None, -0.00234266, None, -0.000510535, None, 1.97905, None, 0.00577499, None, 1.97905, None, 0.00577499, None)

reports.append(Report(590249984, ("DT", 2, 4, 11), "MBwhEst4sec11"))
reports[-1].posNum = 42945
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.00130334, 0.00927393, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.72612e-05, 0.000189382, 0), \
                           -88974.4, 42945, 42945, -nan)
reports[-1].sigmaresid = ValErr(1.92107, 0.006555, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000297578, None, 0.000330953, None, 0.00124808, None, 0.00030688, None, 0.00124808, None, 0.00030688, None, -0.0122952, None, 0.000345859, None, -0.0122952, None, 0.000345859, None, 1.92108, None, 0.00549707, None, 1.92108, None, 0.00549707, None)

reports.append(Report(590512128, ("DT", 2, 4, 12), "MBwhEst4sec12"))
reports[-1].posNum = 102580
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.000821104, 0.00615241, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.28008e-05, 0.0001253, 0), \
                           -215073, 102580, 102580, -nan)
reports[-1].sigmaresid = ValErr(1.96933, 0.00434783, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00251025, None, 0.000158988, None, -0.000787617, None, 0.000166623, None, -0.000787617, None, 0.000166623, None, 0.00446299, None, 0.000141844, None, 0.00446299, None, 0.000141844, None, 1.96933, None, 0.00568664, None, 1.96933, None, 0.00568664, None)

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

