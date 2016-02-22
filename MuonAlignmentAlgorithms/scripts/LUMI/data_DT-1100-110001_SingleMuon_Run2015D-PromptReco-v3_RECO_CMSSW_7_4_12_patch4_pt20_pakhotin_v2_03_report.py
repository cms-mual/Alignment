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
reports[-1].posNum = 60800
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.00194424, 0.00463087, 0), \
                           ValErr(0.000950126, 0.00632812, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.52183e-05, 6.25974e-05, 0), \
                           -204059, 60800, 60800, -nan)
reports[-1].sigmax = ValErr(1.07782, 0.00309088, 0)
reports[-1].sigmay = ValErr(1.55803, 0.00446797, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00247145, -0.000994839, 0.000458723, -0.00398981, 0.00108413, 0.00114451, 0.000436164, -0.0034333, 0.00108413, 0.00114451, 0.000436164, -0.0034333, 0.00347978, -0.00621051, 0.000395737, -0.00346685, 0.00347978, -0.00621051, 0.000395737, -0.00346685, 1.07783, 1.55802, 0.00527863, 0.0389029, 1.07783, 1.55802, 0.00527863, 0.0389029)

reports.append(Report(575176704, ("DT", -2, 1, 2), "MBwhAst1sec02"))
reports[-1].posNum = 37844
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.00100623, 0.00635288, 0), \
                           ValErr(0.00293646, 0.00792482, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.5836e-05, 8.1541e-05, 0), \
                           -126780, 37844, 37844, -nan)
reports[-1].sigmax = ValErr(1.08272, 0.00393581, 0)
reports[-1].sigmay = ValErr(1.54145, 0.00560328, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00862956, 0.00682274, -0.000962294, -0.000687298, 0.00146932, 0.00283036, -0.000991953, 0.00047106, 0.00146932, 0.00283036, -0.000991953, 0.00047106, 0.00405075, -0.000884468, -0.00103139, 0.000418732, 0.00405075, -0.000884468, -0.00103139, 0.000418732, 1.08269, 1.5415, 0.00527764, 0.0371997, 1.08269, 1.5415, 0.00527764, 0.0371997)

reports.append(Report(575438848, ("DT", -2, 1, 3), "MBwhAst1sec03"))
reports[-1].posNum = 41420
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000988623, 0.0058193, 0), \
                           ValErr(0.00248419, 0.00739626, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.41317e-05, 7.53979e-05, 0), \
                           -136580, 41420, 41420, -nan)
reports[-1].sigmax = ValErr(1.05188, 0.00365484, 0)
reports[-1].sigmay = ValErr(1.50528, 0.00523019, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00461868, 0.00319997, 0.000881506, 8.6757e-05, 0.000222083, 0.00248722, 0.000900898, 0.000152332, 0.000222083, 0.00248722, 0.000900898, 0.000152332, 0.000976709, 0.00777724, 0.000826361, 0.000214669, 0.000976709, 0.00777724, 0.000826361, 0.000214669, 1.05186, 1.5053, 0.00515771, 0.0363393, 1.05186, 1.5053, 0.00515771, 0.0363393)

reports.append(Report(575700992, ("DT", -2, 1, 4), "MBwhAst1sec04"))
reports[-1].posNum = 49028
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.001241, 0.00507779, 0), \
                           ValErr(-0.000334093, 0.00709291, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.1909e-05, 6.63895e-05, 0), \
                           -163936, 49028, 49028, -nan)
reports[-1].sigmax = ValErr(1.06242, 0.00339284, 0)
reports[-1].sigmay = ValErr(1.56094, 0.00498484, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00648461, -0.00903621, -0.000284403, -0.00324435, -0.00094537, -0.00047777, -0.000287247, -0.00236368, -0.00094537, -0.00047777, -0.000287247, -0.00236368, 0.00298609, -0.0100983, -0.000327447, -0.00223347, 0.00298609, -0.0100983, -0.000327447, -0.00223347, 1.06242, 1.56094, 0.00522803, 0.0399179, 1.06242, 1.56094, 0.00522803, 0.0399179)

reports.append(Report(575963136, ("DT", -2, 1, 5), "MBwhAst1sec05"))
reports[-1].posNum = 43392
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.00149549, 0.00558535, 0), \
                           ValErr(0.000248369, 0.00738195, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(8.18294e-07, 7.17387e-05, 0), \
                           -144363, 43392, 43392, -nan)
reports[-1].sigmax = ValErr(1.06298, 0.00360833, 0)
reports[-1].sigmay = ValErr(1.53418, 0.00520784, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00499832, 0.00853005, 0.000555067, -0.000751854, 0.00152104, 0.000242448, 0.000557929, -0.000457542, 0.00152104, 0.000242448, 0.000557929, -0.000457542, 0.00195153, -0.00422989, 0.000527696, -0.000262667, 0.00195153, -0.00422989, 0.000527696, -0.000262667, 1.06298, 1.53418, 0.00524707, 0.0378266, 1.06298, 1.53418, 0.00524707, 0.0378266)

reports.append(Report(576225280, ("DT", -2, 1, 6), "MBwhAst1sec06"))
reports[-1].posNum = 38646
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.00893243, 0.00635996, 0), \
                           ValErr(0.00604669, 0.00784605, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.99189e-05, 8.22451e-05, 0), \
                           -129364, 38646, 38646, -nan)
reports[-1].sigmax = ValErr(1.08254, 0.0038939, 0)
reports[-1].sigmay = ValErr(1.5376, 0.00553072, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00167418, 0.014039, 0.000603983, -0.000977424, 0.00545339, 0.00536985, 0.000600196, -0.000569155, 0.00545339, 0.00536985, 0.000600196, -0.000569155, 0.00576589, 0.0157527, 0.000582837, -0.000735913, 0.00576589, 0.0157527, 0.000582837, -0.000735913, 1.08258, 1.53757, 0.00527666, 0.0357611, 1.08258, 1.53757, 0.00527666, 0.0357611)

reports.append(Report(576487424, ("DT", -2, 1, 7), "MBwhAst1sec07"))
reports[-1].posNum = 62720
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.00117534, 0.00462991, 0), \
                           ValErr(-0.00265075, 0.00628396, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.30737e-05, 6.41771e-05, 0), \
                           -211569, 62720, 62720, -nan)
reports[-1].sigmax = ValErr(1.08573, 0.00306811, 0)
reports[-1].sigmay = ValErr(1.5732, 0.00444552, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00171449, 0.00131701, -0.00296327, 0.000511734, 0.000590511, -0.00258726, -0.00297607, 0.00160785, 0.000590511, -0.00258726, -0.00297607, 0.00160785, -0.00365986, -0.01081, -0.00298822, 0.00161034, -0.00365986, -0.01081, -0.00298822, 0.00161034, 1.08577, 1.57313, 0.00532952, 0.0393646, 1.08577, 1.57313, 0.00532952, 0.0393646)

reports.append(Report(576749568, ("DT", -2, 1, 8), "MBwhAst1sec08"))
reports[-1].posNum = 54468
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000189007, 0.00493837, 0), \
                           ValErr(-0.00132194, 0.00661053, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.29073e-05, 6.77566e-05, 0), \
                           -181117, 54468, 54468, -nan)
reports[-1].sigmax = ValErr(1.06229, 0.00321856, 0)
reports[-1].sigmay = ValErr(1.53249, 0.00464316, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00789877, -0.000985125, 0.000866822, 0.00567078, -0.000458607, -0.00106414, 0.000867055, 0.00751105, -0.000458607, -0.00106414, 0.000867055, 0.00751105, -0.00196013, -0.00132254, 0.000831631, 0.00731139, -0.00196013, -0.00132254, 0.000831631, 0.00731139, 1.0623, 1.53248, 0.00539123, 0.0353866, 1.0623, 1.53248, 0.00539123, 0.0353866)

reports.append(Report(577011712, ("DT", -2, 1, 9), "MBwhAst1sec09"))
reports[-1].posNum = 33844
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.0015385, 0.0062112, 0), \
                           ValErr(0.00185837, 0.00843805, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.18928e-05, 7.94113e-05, 0), \
                           -113059, 33844, 33844, -nan)
reports[-1].sigmax = ValErr(1.06933, 0.00411014, 0)
reports[-1].sigmay = ValErr(1.546, 0.00594231, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00371565, 0.00914428, -0.000202896, 0.00147632, 0.00241783, 0.00155314, -0.00018298, 0.00151706, 0.00241783, 0.00155314, -0.00018298, 0.00151706, 0.00433228, 0.0143048, -0.000221285, 0.0012885, 0.00433228, 0.0143048, -0.000221285, 0.0012885, 1.06933, 1.54601, 0.0052449, 0.0376442, 1.06933, 1.54601, 0.0052449, 0.0376442)

reports.append(Report(577273856, ("DT", -2, 1, 10), "MBwhAst1sec10"))
reports[-1].posNum = 33806
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000728763, 0.00596435, 0), \
                           ValErr(0.00243886, 0.0085162, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.6528e-05, 7.78e-05, 0), \
                           -113379, 33806, 33806, -nan)
reports[-1].sigmax = ValErr(1.07008, 0.00411539, 0)
reports[-1].sigmay = ValErr(1.5655, 0.00602069, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0028751, 0.00763536, 0.000494677, 0.00173474, 0.00117296, 0.00238039, 0.000509424, 0.00227587, 0.00117296, 0.00238039, 0.000509424, 0.00227587, 0.0112885, -0.00104958, 0.000408784, 0.00222738, 0.0112885, -0.00104958, 0.000408784, 0.00222738, 1.07008, 1.56551, 0.00533142, 0.0375921, 1.07008, 1.56551, 0.00533142, 0.0375921)

reports.append(Report(577536000, ("DT", -2, 1, 11), "MBwhAst1sec11"))
reports[-1].posNum = 32672
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.00132122, 0.00607184, 0), \
                           ValErr(0.00107087, 0.00871928, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.47313e-05, 8.29737e-05, 0), \
                           -109839, 32672, 32672, -nan)
reports[-1].sigmax = ValErr(1.07457, 0.00420401, 0)
reports[-1].sigmay = ValErr(1.57155, 0.00614828, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00249022, -0.000960136, 0.000444392, -0.00070795, 0.00153637, 0.00120015, 0.000411938, 0.00140485, 0.00153637, 0.00120015, 0.000411938, 0.00140485, 0.0024926, 0.0057651, 0.00030102, 0.00121295, 0.0024926, 0.0057651, 0.00030102, 0.00121295, 1.07457, 1.57156, 0.00537784, 0.0392995, 1.07457, 1.57156, 0.00537784, 0.0392995)

reports.append(Report(577798144, ("DT", -2, 1, 12), "MBwhAst1sec12"))
reports[-1].posNum = 50716
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000148831, 0.00495389, 0), \
                           ValErr(0.000697316, 0.00696247, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.56869e-05, 7.45931e-05, 0), \
                           -170866, 50716, 50716, -nan)
reports[-1].sigmax = ValErr(1.08484, 0.00340636, 0)
reports[-1].sigmay = ValErr(1.56794, 0.00492323, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00243671, -0.0036161, -0.000451123, 0.00103996, 0.000546682, 0.000682858, -0.000447879, 0.000559568, 0.000546682, 0.000682858, -0.000447879, 0.000559568, 0.00809341, -0.00388029, -0.000489954, 0.000553567, 0.00809341, -0.00388029, -0.000489954, 0.000553567, 1.08484, 1.56795, 0.00528278, 0.0381924, 1.08484, 1.56795, 0.00528278, 0.0381924)

reports.append(Report(579108864, ("DT", -2, 2, 1), "MBwhAst2sec01"))
reports[-1].posNum = 82566
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000110172, 0.00513579, 0), \
                           ValErr(0.000729566, 0.00648054, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.27822e-05, 6.51879e-05, 0), \
                           -314266, 82566, 82566, -nan)
reports[-1].sigmax = ValErr(1.41462, 0.00348143, 0)
reports[-1].sigmay = ValErr(1.86172, 0.00458173, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.000534538, 0.00547909, -0.00119022, -0.00062437, 0.000625285, 0.000800416, -0.00120706, -0.000454851, 0.000625285, 0.000800416, -0.00120706, -0.000454851, 0.00258612, 0.00199844, -0.00126741, -0.000532514, 0.00258612, 0.00199844, -0.00126741, -0.000532514, 1.4146, 1.86175, 0.00562246, 0.0241296, 1.4146, 1.86175, 0.00562246, 0.0241296)

reports.append(Report(579371008, ("DT", -2, 2, 2), "MBwhAst2sec02"))
reports[-1].posNum = 70988
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000609733, 0.00566667, 0), \
                           ValErr(-0.0023293, 0.0069301, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.88461e-05, 7.19489e-05, 0), \
                           -268089, 70988, 70988, -nan)
reports[-1].sigmax = ValErr(1.38795, 0.00368376, 0)
reports[-1].sigmay = ValErr(1.84196, 0.0048887, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00349137, -0.00894153, -0.000887938, 0.0123026, -2.67073e-05, -0.00245417, -0.000895044, 0.0127753, -2.67073e-05, -0.00245417, -0.000895044, 0.0127753, -0.00152701, -0.00020376, -0.000924534, 0.0128987, -0.00152701, -0.00020376, -0.000924534, 0.0128987, 1.38794, 1.84197, 0.00550666, 0.026261, 1.38794, 1.84197, 0.00550666, 0.026261)

reports.append(Report(579633152, ("DT", -2, 2, 3), "MBwhAst2sec03"))
reports[-1].posNum = 67166
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.00602765, 0.00577866, 0), \
                           ValErr(-0.00348853, 0.00709641, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(9.68953e-05, 7.34265e-05, 0), \
                           -253430, 67166, 67166, -nan)
reports[-1].sigmax = ValErr(1.38728, 0.00378555, 0)
reports[-1].sigmay = ValErr(1.8367, 0.00501188, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00452996, 0.00744418, 9.45014e-05, 0.000208863, -0.00315041, -0.00300928, 0.000100388, 0.000243023, -0.00315041, -0.00300928, 0.000100388, 0.000243023, 0.00309088, -0.010208, 7.43041e-05, 0.000212747, 0.00309088, -0.010208, 7.43041e-05, 0.000212747, 1.38721, 1.83681, 0.00549372, 0.0238012, 1.38721, 1.83681, 0.00549372, 0.0238012)

reports.append(Report(579895296, ("DT", -2, 2, 4), "MBwhAst2sec04"))
reports[-1].posNum = 79014
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.00044874, 0.00526361, 0), \
                           ValErr(-6.70056e-05, 0.00662113, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(7.88772e-06, 6.71326e-05, 0), \
                           -299723, 79014, 79014, -nan)
reports[-1].sigmax = ValErr(1.39724, 0.00351499, 0)
reports[-1].sigmay = ValErr(1.86064, 0.00468073, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00431091, 0.00753168, 0.000537853, 0.00321728, -0.000245322, -8.53614e-05, 0.000522244, 0.00314223, -0.000245322, -8.53614e-05, 0.000522244, 0.00314223, -0.00222119, -0.00271985, 0.000529821, 0.00304665, -0.00222119, -0.00271985, 0.000529821, 0.00304665, 1.39723, 1.86065, 0.00555152, 0.0250608, 1.39723, 1.86065, 0.00555152, 0.0250608)

reports.append(Report(580157440, ("DT", -2, 2, 5), "MBwhAst2sec05"))
reports[-1].posNum = 68520
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.00022592, 0.00565444, 0), \
                           ValErr(-0.00200365, 0.00700297, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.361e-05, 7.32889e-05, 0), \
                           -258035, 68520, 68520, -nan)
reports[-1].sigmax = ValErr(1.38055, 0.0037296, 0)
reports[-1].sigmay = ValErr(1.83212, 0.00494949, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00584122, 0.00464769, 0.000101, 0.00447849, 0.000883097, -0.00192947, 0.00012627, 0.00459589, 0.000883097, -0.00192947, 0.00012627, 0.00459589, 0.00102307, -0.00845973, 8.89168e-05, 0.00446012, 0.00102307, -0.00845973, 8.89168e-05, 0.00446012, 1.38054, 1.83214, 0.00547643, 0.0236774, 1.38054, 1.83214, 0.00547643, 0.0236774)

reports.append(Report(580419584, ("DT", -2, 2, 6), "MBwhAst2sec06"))
reports[-1].posNum = 63746
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.00225829, 0.00605341, 0), \
                           ValErr(-0.00138316, 0.00746156, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.92209e-05, 7.73026e-05, 0), \
                           -242893, 63746, 63746, -nan)
reports[-1].sigmax = ValErr(1.40847, 0.00394483, 0)
reports[-1].sigmay = ValErr(1.87752, 0.0052585, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00981139, 0.00596012, 0.000738262, 0.00331234, -0.00137222, -0.00114994, 0.000709269, 0.00336733, -0.00137222, -0.00114994, 0.000709269, 0.00336733, 0.00207809, 0.00041786, 0.000682227, 0.00333259, 0.00207809, 0.00041786, 0.000682227, 0.00333259, 1.40846, 1.87754, 0.005593, 0.0238954, 1.40846, 1.87754, 0.005593, 0.0238954)

reports.append(Report(580681728, ("DT", -2, 2, 7), "MBwhAst2sec07"))
reports[-1].posNum = 84464
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000122428, 0.00502921, 0), \
                           ValErr(-0.00197275, 0.00643749, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.46169e-05, 6.38178e-05, 0), \
                           -321958, 84464, 84464, -nan)
reports[-1].sigmax = ValErr(1.41559, 0.00344474, 0)
reports[-1].sigmay = ValErr(1.87078, 0.00455235, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.000620431, -0.00154913, 0.000158333, 0.00191324, -0.000408878, -0.00198992, 0.000166438, 0.0019271, -0.000408878, -0.00198992, 0.000166438, 0.0019271, -0.000208702, -0.00843723, 0.000109082, 0.00174145, -0.000208702, -0.00843723, 0.000109082, 0.00174145, 1.4156, 1.87076, 0.00562175, 0.0271102, 1.4156, 1.87076, 0.00562175, 0.0271102)

reports.append(Report(580943872, ("DT", -2, 2, 8), "MBwhAst2sec08"))
reports[-1].posNum = 84506
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000763434, 0.00500751, 0), \
                           ValErr(-0.00225482, 0.00651089, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.86113e-05, 6.46741e-05, 0), \
                           -322866, 84506, 84506, -nan)
reports[-1].sigmax = ValErr(1.41169, 0.00343401, 0)
reports[-1].sigmay = ValErr(1.89262, 0.00460393, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00163381, -0.013105, 0.0024964, 0.00710528, -0.00130383, -0.00222571, 0.00249692, 0.00685573, -0.00130383, -0.00222571, 0.00249692, 0.00685573, 0.00186641, 0.00319531, 0.00246284, 0.00682427, 0.00186641, 0.00319531, 0.00246284, 0.00682427, 1.41167, 1.89264, 0.00555518, 0.0251111, 1.41167, 1.89264, 0.00555518, 0.0251111)

reports.append(Report(581206016, ("DT", -2, 2, 9), "MBwhAst2sec09"))
reports[-1].posNum = 59156
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.00175662, 0.0062971, 0), \
                           ValErr(0.00202149, 0.00754321, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.96432e-05, 7.6732e-05, 0), \
                           -223905, 59156, 59156, -nan)
reports[-1].sigmax = ValErr(1.40785, 0.00409314, 0)
reports[-1].sigmay = ValErr(1.83134, 0.00532436, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00492216, 0.00667497, 0.000238067, 0.0021855, 0.000797446, 0.00219541, 0.000225993, 0.00243173, 0.000797446, 0.00219541, 0.000225993, 0.00243173, -0.00398717, -0.0143622, 0.000289799, 0.00241885, -0.00398717, -0.0143622, 0.000289799, 0.00241885, 1.40786, 1.83132, 0.00556847, 0.0234786, 1.40786, 1.83132, 0.00556847, 0.0234786)

reports.append(Report(581468160, ("DT", -2, 2, 10), "MBwhAst2sec10"))
reports[-1].posNum = 53530
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000258995, 0.00685647, 0), \
                           ValErr(0.00140907, 0.00783692, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(9.4006e-06, 8.44103e-05, 0), \
                           -201894, 53530, 53530, -nan)
reports[-1].sigmax = ValErr(1.39378, 0.00425259, 0)
reports[-1].sigmay = ValErr(1.82525, 0.00557522, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00558741, 0.0207316, 0.000932607, 0.00324465, 0.000623261, 0.00138761, 0.000877773, 0.00345463, 0.000623261, 0.00138761, 0.000877773, 0.00345463, -0.000718528, -0.00871928, 0.000873821, 0.0035994, -0.000718528, -0.00871928, 0.000873821, 0.0035994, 1.39378, 1.82524, 0.00551362, 0.0229884, 1.39378, 1.82524, 0.00551362, 0.0229884)

reports.append(Report(581730304, ("DT", -2, 2, 11), "MBwhAst2sec11"))
reports[-1].posNum = 51416
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.00204765, 0.00676176, 0), \
                           ValErr(0.00413148, 0.00800395, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.42169e-05, 8.34316e-05, 0), \
                           -192952, 51416, 51416, -nan)
reports[-1].sigmax = ValErr(1.38227, 0.00431051, 0)
reports[-1].sigmay = ValErr(1.80609, 0.00563218, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00274657, 0.00428079, 0.00118033, 0.00814613, 0.00155108, 0.0039956, 0.00115108, 0.00878362, 0.00155108, 0.0039956, 0.00115108, 0.00878362, 0.00485483, 0.0078259, 0.00112811, 0.00886832, 0.00485483, 0.0078259, 0.00112811, 0.00886832, 1.38227, 1.80609, 0.00547283, 0.0250259, 1.38227, 1.80609, 0.00547283, 0.0250259)

reports.append(Report(581992448, ("DT", -2, 2, 12), "MBwhAst2sec12"))
reports[-1].posNum = 75304
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000353158, 0.0052935, 0), \
                           ValErr(-0.00382183, 0.0067349, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.25539e-05, 6.79409e-05, 0), \
                           -283888, 75304, 75304, -nan)
reports[-1].sigmax = ValErr(1.37525, 0.00354418, 0)
reports[-1].sigmay = ValErr(1.84668, 0.00475908, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00333429, -0.00413083, -0.000518932, 0.00123182, -4.80029e-05, -0.00376796, -0.000507439, 0.00139993, -4.80029e-05, -0.00376796, -0.000507439, 0.00139993, 0.00342144, -0.0103094, -0.000524113, 0.00150344, 0.00342144, -0.0103094, -0.000524113, 0.00150344, 1.37523, 1.84669, 0.0055087, 0.0253112, 1.37523, 1.84669, 0.0055087, 0.0253112)

reports.append(Report(583303168, ("DT", -2, 3, 1), "MBwhAst3sec01"))
reports[-1].posNum = 90952
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.00155357, 0.00622777, 0), \
                           ValErr(0.00298797, 0.00757108, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.59263e-05, 6.88847e-05, 0), \
                           -389838, 90952, 90952, -nan)
reports[-1].sigmax = ValErr(1.86459, 0.00437196, 0)
reports[-1].sigmay = ValErr(2.28252, 0.00535187, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00614326, 0.00677789, -0.000439541, 0.000790953, 0.0018345, 0.00291313, -0.000434017, 0.000424915, 0.0018345, 0.00291313, -0.000434017, 0.000424915, -0.000789337, 0.00115735, -0.000471527, 0.000467208, -0.000789337, 0.00115735, -0.000471527, 0.000467208, 1.86458, 2.28254, 0.00647042, 0.0198167, 1.86458, 2.28254, 0.00647042, 0.0198167)

reports.append(Report(583565312, ("DT", -2, 3, 2), "MBwhAst3sec02"))
reports[-1].posNum = 79132
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000486635, 0.00654063, 0), \
                           ValErr(-0.00251521, 0.0081294, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.07112e-05, 7.38279e-05, 0), \
                           -337485, 79132, 79132, -nan)
reports[-1].sigmax = ValErr(1.83026, 0.00460073, 0)
reports[-1].sigmay = ValErr(2.27616, 0.00572159, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0073219, 0.00134416, -0.000290956, -0.000938764, -0.000583176, -0.00240129, -0.000314556, -0.000898358, -0.000583176, -0.00240129, -0.000314556, -0.000898358, 0.00168323, -0.000425346, -0.000358038, -0.000763567, 0.00168323, -0.000425346, -0.000358038, -0.000763567, 1.83027, 2.27616, 0.00642206, 0.0203865, 1.83027, 2.27616, 0.00642206, 0.0203865)

reports.append(Report(583827456, ("DT", -2, 3, 3), "MBwhAst3sec03"))
reports[-1].posNum = 76676
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.0025524, 0.00663881, 0), \
                           ValErr(0.00104642, 0.00817348, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.1126e-06, 7.49229e-05, 0), \
                           -326314, 76676, 76676, -nan)
reports[-1].sigmax = ValErr(1.82549, 0.00466159, 0)
reports[-1].sigmay = ValErr(2.26149, 0.00577498, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000482175, -0.00243145, 0.000765091, -0.000646403, 0.00251428, 0.00106305, 0.000769489, -0.000751121, 0.00251428, 0.00106305, 0.000769489, -0.000751121, 0.00728681, 0.00593234, 0.000743376, -0.000664365, 0.00728681, 0.00593234, 0.000743376, -0.000664365, 1.82549, 2.26149, 0.00642522, 0.020102, 1.82549, 2.26149, 0.00642522, 0.020102)

reports.append(Report(584089600, ("DT", -2, 3, 4), "MBwhAst3sec04"))
reports[-1].posNum = 86256
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.00118261, 0.00626996, 0), \
                           ValErr(-0.00159497, 0.00783273, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.37344e-05, 7.08339e-05, 0), \
                           -368561, 86256, 86256, -nan)
reports[-1].sigmax = ValErr(1.83029, 0.00440679, 0)
reports[-1].sigmay = ValErr(2.29452, 0.0055245, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00473279, -0.00428901, 8.9689e-05, -0.0010017, -0.00056242, -0.00209942, 8.03344e-05, -0.00119297, -0.00056242, -0.00209942, 8.03344e-05, -0.00119297, 0.00113072, -0.0121641, 5.42173e-05, -0.00110412, 0.00113072, -0.0121641, 5.42173e-05, -0.00110412, 1.83026, 2.29456, 0.00640337, 0.0199534, 1.83026, 2.29456, 0.00640337, 0.0199534)

reports.append(Report(584351744, ("DT", -2, 3, 5), "MBwhAst3sec05"))
reports[-1].posNum = 79726
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.00030148, 0.00654458, 0), \
                           ValErr(-0.000359637, 0.00812538, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.19301e-06, 7.46897e-05, 0), \
                           -340519, 79726, 79726, -nan)
reports[-1].sigmax = ValErr(1.83713, 0.00460072, 0)
reports[-1].sigmay = ValErr(2.28195, 0.00571468, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00275609, 6.7333e-05, 0.00085309, -0.00208753, 0.00028123, -0.000335237, 0.000876659, -0.00203718, 0.00028123, -0.000335237, 0.000876659, -0.00203718, 0.000842165, -0.00856433, 0.000870981, -0.00187524, 0.000842165, -0.00856433, 0.000870981, -0.00187524, 1.83713, 2.28195, 0.0063552, 0.019703, 1.83713, 2.28195, 0.0063552, 0.019703)

reports.append(Report(584613888, ("DT", -2, 3, 6), "MBwhAst3sec06"))
reports[-1].posNum = 75000
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.00332436, 0.00681736, 0), \
                           ValErr(0.000855949, 0.00849063, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.28219e-05, 7.68769e-05, 0), \
                           -322425, 75000, 75000, -nan)
reports[-1].sigmax = ValErr(1.85743, 0.0047963, 0)
reports[-1].sigmay = ValErr(2.32085, 0.00599287, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00341978, 0.0068866, -0.000390823, 0.000668003, 0.00380819, 0.00120717, -0.000414416, 0.000384358, 0.00380819, 0.00120717, -0.000414416, 0.000384358, 0.00516114, 0.00332028, -0.000396109, 0.00050548, 0.00516114, 0.00332028, -0.000396109, 0.00050548, 1.85739, 2.32091, 0.00648045, 0.0201607, 1.85739, 2.32091, 0.00648045, 0.0201607)

reports.append(Report(584876032, ("DT", -2, 3, 7), "MBwhAst3sec07"))
reports[-1].posNum = 88544
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000637891, 0.00626836, 0), \
                           ValErr(0.00199111, 0.00773178, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.22317e-06, 7.01166e-05, 0), \
                           -379702, 88544, 88544, -nan)
reports[-1].sigmax = ValErr(1.85422, 0.00440714, 0)
reports[-1].sigmay = ValErr(2.30007, 0.00546673, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000229635, -0.00622836, -0.00255601, -0.00016199, 0.000689655, 0.00197548, -0.00255154, -0.000153327, 0.000689655, 0.00197548, -0.00255154, -0.000153327, -0.00390524, 0.000857811, -0.00255605, -0.00016012, -0.00390524, 0.000857811, -0.00255605, -0.00016012, 1.85422, 2.30008, 0.00643349, 0.0199426, 1.85422, 2.30008, 0.00643349, 0.0199426)

reports.append(Report(585138176, ("DT", -2, 3, 8), "MBwhAst3sec08"))
reports[-1].posNum = 77396
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.00319234, 0.00676649, 0), \
                           ValErr(0.00413316, 0.00822795, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(7.6577e-06, 7.44598e-05, 0), \
                           -332050, 77396, 77396, -nan)
reports[-1].sigmax = ValErr(1.86699, 0.00474535, 0)
reports[-1].sigmay = ValErr(2.28888, 0.00581767, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00234812, -0.00370693, 0.000742493, -0.0012561, -0.00310328, 0.00414267, 0.000770364, -0.00152396, -0.00310328, 0.00414267, 0.000770364, -0.00152396, -0.000906389, -0.00187636, 0.000788023, -0.00131516, -0.000906389, -0.00187636, 0.000788023, -0.00131516, 1.86699, 2.28888, 0.00649558, 0.0203077, 1.86699, 2.28888, 0.00649558, 0.0203077)

reports.append(Report(585400320, ("DT", -2, 3, 9), "MBwhAst3sec09"))
reports[-1].posNum = 68646
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000365538, 0.00710699, 0), \
                           ValErr(0.00189797, 0.00867316, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.76317e-05, 7.81502e-05, 0), \
                           -292998, 68646, 68646, -nan)
reports[-1].sigmax = ValErr(1.84287, 0.00497362, 0)
reports[-1].sigmay = ValErr(2.26835, 0.00612191, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00507662, 0.010348, 0.000561842, 0.00453936, -0.000725309, 0.00208152, 0.000568037, 0.0044735, -0.000725309, 0.00208152, 0.000568037, 0.0044735, -0.00556607, 0.0052988, 0.000554631, 0.00464327, -0.00556607, 0.0052988, 0.000554631, 0.00464327, 1.84287, 2.26835, 0.00642205, 0.0204198, 1.84287, 2.26835, 0.00642205, 0.0204198)

reports.append(Report(585662464, ("DT", -2, 3, 10), "MBwhAst3sec10"))
reports[-1].posNum = 67810
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.00366897, 0.00714291, 0), \
                           ValErr(-0.00372249, 0.00880266, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.02348e-08, 8.22861e-05, 0), \
                           -289197, 67810, 67810, -nan)
reports[-1].sigmax = ValErr(1.83127, 0.00497272, 0)
reports[-1].sigmay = ValErr(2.27487, 0.00617724, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00221749, 0.00539138, -0.000979599, -0.000855874, 0.00367034, -0.0037219, -0.00097382, -0.0012237, 0.00367034, -0.0037219, -0.00097382, -0.0012237, 0.00484326, -0.0071194, -0.000992373, -0.00102248, 0.00484326, -0.0071194, -0.000992373, -0.00102248, 1.83127, 2.27486, 0.00639892, 0.0217251, 1.83127, 2.27486, 0.00639892, 0.0217251)

reports.append(Report(585924608, ("DT", -2, 3, 11), "MBwhAst3sec11"))
reports[-1].posNum = 66346
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.00222694, 0.00726747, 0), \
                           ValErr(-0.0035508, 0.00878172, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.18508e-05, 8.24738e-05, 0), \
                           -282910, 66346, 66346, -nan)
reports[-1].sigmax = ValErr(1.84448, 0.00506354, 0)
reports[-1].sigmay = ValErr(2.25711, 0.00619628, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00946486, -0.00949001, -0.000894643, 0.000431637, -0.00159754, -0.00384473, -0.000940707, 5.2755e-05, -0.00159754, -0.00384473, -0.000940707, 5.2755e-05, 0.00218591, -0.00109461, -0.000958547, 0.00021296, 0.00218591, -0.00109461, -0.000958547, 0.00021296, 1.84447, 2.25712, 0.00643212, 0.0212463, 1.84447, 2.25712, 0.00643212, 0.0212463)

reports.append(Report(586186752, ("DT", -2, 3, 12), "MBwhAst3sec12"))
reports[-1].posNum = 85804
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.00270091, 0.00626846, 0), \
                           ValErr(0.00252845, 0.0078198, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.77983e-06, 7.14798e-05, 0), \
                           -366076, 85804, 85804, -nan)
reports[-1].sigmax = ValErr(1.82523, 0.00440617, 0)
reports[-1].sigmay = ValErr(2.28609, 0.00551868, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00618196, 0.0116457, 0.000626566, 0.000861746, -0.00279532, 0.00259574, 0.000620562, 0.000845554, -0.00279532, 0.00259574, 0.000620562, 0.000845554, -0.0115059, 0.00217803, 0.00061647, 0.00101237, -0.0115059, 0.00217803, 0.00061647, 0.00101237, 1.82523, 2.28608, 0.00636386, 0.0205969, 1.82523, 2.28608, 0.00636386, 0.0205969)

reports.append(Report(574947328, ("DT", -1, 1, 1), "MBwhBst1sec01"))
reports[-1].posNum = 123890
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000493567, 0.00280884, 0), \
                           ValErr(0.000894603, 0.00301895, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.67984e-05, 3.47562e-05, 0), \
                           -354644, 123890, 123890, -nan)
reports[-1].sigmax = ValErr(0.965138, 0.00193891, 0)
reports[-1].sigmay = ValErr(1.06203, 0.00213357, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00412725, 0.000434993, 0.000749714, 0.000106519, 0.000200317, 0.000943864, 0.000752659, -0.000211795, 0.000200317, 0.000943864, 0.000752659, -0.000211795, 0.00214765, 0.000897267, 0.000695744, -0.000317516, 0.00214765, 0.000897267, 0.000695744, -0.000317516, 0.965136, 1.06203, 0.00480973, 0.0151711, 0.965136, 1.06203, 0.00480973, 0.0151711)

reports.append(Report(575209472, ("DT", -1, 1, 2), "MBwhBst1sec02"))
reports[-1].posNum = 107022
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000149667, 0.00296752, 0), \
                           ValErr(0.000470438, 0.00325416, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.62637e-06, 3.74464e-05, 0), \
                           -305858, 107022, 107022, -nan)
reports[-1].sigmax = ValErr(0.959827, 0.00207477, 0)
reports[-1].sigmay = ValErr(1.06292, 0.0022976, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00216753, 0.000346752, -0.000425635, -0.00255057, 0.000228787, 0.000439661, -0.000396921, -0.00295123, 0.000228787, 0.000439661, -0.000396921, -0.00295123, 0.00355565, -0.00260349, -0.000461385, -0.00293462, 0.00355565, -0.00260349, -0.000461385, -0.00293462, 0.959823, 1.06293, 0.00489915, 0.015111, 0.959823, 1.06293, 0.00489915, 0.015111)

reports.append(Report(575471616, ("DT", -1, 1, 3), "MBwhBst1sec03"))
reports[-1].posNum = 96078
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000428882, 0.00315282, 0), \
                           ValErr(-0.000170227, 0.00348734, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.29228e-05, 4.49749e-05, 0), \
                           -275924, 96078, 96078, -nan)
reports[-1].sigmax = ValErr(0.958245, 0.00218599, 0)
reports[-1].sigmay = ValErr(1.07966, 0.00246298, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00130367, -0.00261108, 0.000522187, -0.000151205, 0.000248273, -0.000124775, 0.000549614, -0.000513953, 0.000248273, -0.000124775, 0.000549614, -0.000513953, -0.00051303, -0.000537823, 0.000493782, -0.000537642, -0.00051303, -0.000537823, 0.000493782, -0.000537642, 0.958245, 1.07966, 0.0048193, 0.0151709, 0.958245, 1.07966, 0.0048193, 0.0151709)

reports.append(Report(575733760, ("DT", -1, 1, 4), "MBwhBst1sec04"))
reports[-1].posNum = 111592
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(9.86361e-05, 0.00288493, 0), \
                           ValErr(0.00156133, 0.00322416, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.22432e-05, 3.71394e-05, 0), \
                           -318456, 111592, 111592, -nan)
reports[-1].sigmax = ValErr(0.953621, 0.00201858, 0)
reports[-1].sigmay = ValErr(1.06541, 0.00225522, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(2.55058e-05, 0.0017808, 0.000745879, -0.0015054, -0.000149763, 0.00184502, 0.000769501, -0.00181988, -0.000149763, 0.00184502, 0.000769501, -0.00181988, 0.00343843, 0.00150634, 0.000647613, -0.00176643, 0.00343843, 0.00150634, 0.000647613, -0.00176643, 0.953618, 1.06542, 0.00499456, 0.0151255, 0.953618, 1.06542, 0.00499456, 0.0151255)

reports.append(Report(575995904, ("DT", -1, 1, 5), "MBwhBst1sec05"))
reports[-1].posNum = 114832
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-5.93908e-05, 0.00287681, 0), \
                           ValErr(-0.000669078, 0.00315179, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.21723e-05, 3.59292e-05, 0), \
                           -327922, 114832, 114832, -nan)
reports[-1].sigmax = ValErr(0.958923, 0.00200102, 0)
reports[-1].sigmay = ValErr(1.06156, 0.00221519, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0013628, -0.00452025, 3.34597e-05, 0.000206243, 0.000114421, -0.000784664, 3.15555e-05, -0.000142909, 0.000114421, -0.000784664, 3.15555e-05, -0.000142909, 0.00188026, -0.000884753, 1.46213e-05, -0.000193124, 0.00188026, -0.000884753, 1.46213e-05, -0.000193124, 0.958917, 1.06156, 0.00482874, 0.0148236, 0.958917, 1.06156, 0.00482874, 0.0148236)

reports.append(Report(576258048, ("DT", -1, 1, 6), "MBwhBst1sec06"))
reports[-1].posNum = 96586
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000545938, 0.00312691, 0), \
                           ValErr(0.000954568, 0.00352683, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.70386e-06, 4.20467e-05, 0), \
                           -279816, 96586, 96586, -nan)
reports[-1].sigmax = ValErr(0.9705, 0.00220817, 0)
reports[-1].sigmay = ValErr(1.09322, 0.00248738, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00111985, 0.00038189, 0.000894547, 0.00160388, 0.000552758, 0.000944405, 0.000922898, 0.00132492, 0.000552758, 0.000944405, 0.000922898, 0.00132492, 0.00207028, 0.000465458, 0.000899543, 0.00129366, 0.00207028, 0.000465458, 0.000899543, 0.00129366, 0.9705, 1.09322, 0.00496047, 0.0160652, 0.9705, 1.09322, 0.00496047, 0.0160652)

reports.append(Report(576520192, ("DT", -1, 1, 7), "MBwhBst1sec07"))
reports[-1].posNum = 134192
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000355112, 0.00272356, 0), \
                           ValErr(-0.000367017, 0.00290061, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.79355e-06, 3.45299e-05, 0), \
                           -384496, 134192, 134192, -nan)
reports[-1].sigmax = ValErr(0.967457, 0.00186804, 0)
reports[-1].sigmay = ValErr(1.06234, 0.00205121, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000103002, 0.00372061, -0.00119014, -0.00315906, -0.000544292, -0.000349006, -0.00119157, -0.00327682, -0.000544292, -0.000349006, -0.00119157, -0.00327682, 0.000357251, -0.00292876, -0.00122765, -0.00333092, 0.000357251, -0.00292876, -0.00122765, -0.00333092, 0.967469, 1.06233, 0.00482821, 0.014524, 0.967469, 1.06233, 0.00482821, 0.014524)

reports.append(Report(576782336, ("DT", -1, 1, 8), "MBwhBst1sec08"))
reports[-1].posNum = 125870
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.00117438, 0.00275494, 0), \
                           ValErr(0.000313835, 0.0029961, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.86266e-06, 3.47631e-05, 0), \
                           -359077, 125870, 125870, -nan)
reports[-1].sigmax = ValErr(0.960548, 0.00191446, 0)
reports[-1].sigmay = ValErr(1.05669, 0.00210608, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.000472854, 0.000293305, 0.000279521, 0.000121691, -0.00123343, 0.000349443, 0.000298608, -0.000199633, -0.00123343, 0.000349443, 0.000298608, -0.000199633, 0.00021244, -0.00317168, 0.000264468, -0.000235531, 0.00021244, -0.00317168, 0.000264468, -0.000235531, 0.960548, 1.05669, 0.00482753, 0.0153775, 0.960548, 1.05669, 0.00482753, 0.0153775)

reports.append(Report(577044480, ("DT", -1, 1, 9), "MBwhBst1sec09"))
reports[-1].posNum = 97412
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.00109532, 0.0031712, 0), \
                           ValErr(0.00037879, 0.00344259, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.1368e-07, 3.91289e-05, 0), \
                           -280094, 97412, 97412, -nan)
reports[-1].sigmax = ValErr(0.970116, 0.00219788, 0)
reports[-1].sigmay = ValErr(1.07017, 0.00242456, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00148419, 0.00155766, 0.000755691, -0.00032806, 0.00109464, 0.00038021, 0.000767776, -0.00053169, 0.00109464, 0.00038021, 0.000767776, -0.00053169, 0.00437094, -0.0047618, 0.000725287, -0.000595396, 0.00437094, -0.0047618, 0.000725287, -0.000595396, 0.970115, 1.07017, 0.00485212, 0.0153472, 0.970115, 1.07017, 0.00485212, 0.0153472)

reports.append(Report(577306624, ("DT", -1, 1, 10), "MBwhBst1sec10"))
reports[-1].posNum = 109062
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000267158, 0.00293859, 0), \
                           ValErr(-0.000331101, 0.00319834, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.77306e-05, 3.79892e-05, 0), \
                           -309583, 109062, 109062, -nan)
reports[-1].sigmax = ValErr(0.951961, 0.00203839, 0)
reports[-1].sigmay = ValErr(1.05122, 0.0022509, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00277818, -0.000811612, 0.000420441, 0.000724221, -0.000683854, -9.97101e-05, 0.000431862, 0.000472501, -0.000683854, -9.97101e-05, 0.000431862, 0.000472501, 0.00480476, -0.00412125, 0.000354603, 0.000431362, 0.00480476, -0.00412125, 0.000354603, 0.000431362, 0.951973, 1.0512, 0.00489756, 0.0153988, 0.951973, 1.0512, 0.00489756, 0.0153988)

reports.append(Report(577568768, ("DT", -1, 1, 11), "MBwhBst1sec11"))
reports[-1].posNum = 105404
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000490354, 0.00300327, 0), \
                           ValErr(-0.00116569, 0.0032724, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.10892e-05, 3.78792e-05, 0), \
                           -300654, 105404, 105404, -nan)
reports[-1].sigmax = ValErr(0.957606, 0.00208572, 0)
reports[-1].sigmay = ValErr(1.05955, 0.00230774, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00226923, -0.00316803, 0.000337569, 0.00217863, 0.000654899, -0.00123599, 0.000341941, 0.00200685, 0.000654899, -0.00123599, 0.000341941, 0.00200685, 0.00225478, -0.00356206, 0.000275208, 0.00199064, 0.00225478, -0.00356206, 0.000275208, 0.00199064, 0.957602, 1.05955, 0.00495528, 0.0151591, 0.957602, 1.05955, 0.00495528, 0.0151591)

reports.append(Report(577830912, ("DT", -1, 1, 12), "MBwhBst1sec12"))
reports[-1].posNum = 125880
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000115193, 0.00276146, 0), \
                           ValErr(0.000387138, 0.00302254, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.4766e-05, 3.56069e-05, 0), \
                           -362175, 125880, 125880, -nan)
reports[-1].sigmax = ValErr(0.970729, 0.00193475, 0)
reports[-1].sigmay = ValErr(1.07142, 0.00213541, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000252229, 0.00418239, 0.000573945, -0.00109155, 0.000375294, 0.000476564, 0.000566532, -0.00141738, 0.000375294, 0.000476564, 0.000566532, -0.00141738, 0.00551953, -0.000655043, 0.000477433, -0.00139888, 0.00551953, -0.000655043, 0.000477433, -0.00139888, 0.970716, 1.07143, 0.00492038, 0.015134, 0.970716, 1.07143, 0.00492038, 0.015134)

reports.append(Report(579141632, ("DT", -1, 2, 1), "MBwhBst2sec01"))
reports[-1].posNum = 125136
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000600019, 0.00366238, 0), \
                           ValErr(0.00110289, 0.00387443, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.91975e-05, 4.10978e-05, 0), \
                           -426249, 125136, 125136, -nan)
reports[-1].sigmax = ValErr(1.28844, 0.00257581, 0)
reports[-1].sigmay = ValErr(1.37023, 0.00273931, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00286433, 0.00299329, -0.000553622, 0.00177593, -0.000421081, 0.00114193, -0.000555444, 0.00176138, -0.000421081, 0.00114193, -0.000555444, 0.00176138, 0.00178118, 0.00516338, -0.000589119, 0.00176409, 0.00178118, 0.00516338, -0.000589119, 0.00176409, 1.28842, 1.37025, 0.00512887, 0.0148978, 1.28842, 1.37025, 0.00512887, 0.0148978)

reports.append(Report(579403776, ("DT", -1, 2, 2), "MBwhBst2sec02"))
reports[-1].posNum = 115236
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(9.1018e-05, 0.00192437, 0), \
                           ValErr(0.000864728, 0.00399263, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.45342e-06, 3.83181e-05, 0), \
                           -389686, 115236, 115236, -nan)
reports[-1].sigmax = ValErr(1.27182, 0.00264257, 0)
reports[-1].sigmay = ValErr(1.35433, 0.00282206, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0029917, 0.00015236, -0.000801389, 0.00150649, 1.29371e-05, 0.000895424, -0.000810813, 0.00179159, 1.29371e-05, 0.000895424, -0.000810813, 0.00179159, 0.00187324, 0.00098012, -0.000821161, 0.00182864, 0.00187324, 0.00098012, -0.000821161, 0.00182864, 1.27182, 1.35433, 0.00514033, 0.014742, 1.27182, 1.35433, 0.00514033, 0.014742)

reports.append(Report(579665920, ("DT", -1, 2, 3), "MBwhBst2sec03"))
reports[-1].posNum = 80060
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000563403, 0.00455887, 0), \
                           ValErr(0.000702668, 0.00442685, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.19152e-05, 5.62893e-05, 0), \
                           -273152, 80060, 80060, -nan)
reports[-1].sigmax = ValErr(1.28504, 0.00320975, 0)
reports[-1].sigmay = ValErr(1.38151, 0.00345116, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00409866, -0.00125321, 0.000664172, 0.00446842, -0.000292063, 0.000874191, 0.000662282, 0.00433787, -0.000292063, 0.000874191, 0.000662282, 0.00433787, -0.000847318, 0.00319039, 0.000647821, 0.00437634, -0.000847318, 0.00319039, 0.000647821, 0.00437634, 1.28503, 1.38152, 0.00512741, 0.0149557, 1.28503, 1.38152, 0.00512741, 0.0149557)

reports.append(Report(579928064, ("DT", -1, 2, 4), "MBwhBst2sec04"))
reports[-1].posNum = 119872
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000356938, 0.00373203, 0), \
                           ValErr(0.000585451, 0.00396422, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.17307e-06, 4.12978e-05, 0), \
                           -408289, 119872, 119872, -nan)
reports[-1].sigmax = ValErr(1.28669, 0.00262806, 0)
reports[-1].sigmay = ValErr(1.37175, 0.00280176, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00328936, 0.00201197, -0.000322828, 0.00205563, -0.000399671, 0.000601797, -0.000356712, 0.00194438, -0.000399671, 0.000601797, -0.000356712, 0.00194438, 0.00597139, -0.000282271, -0.000423054, 0.00191191, 0.00597139, -0.000282271, -0.000423054, 0.00191191, 1.2867, 1.37174, 0.00519148, 0.0146205, 1.2867, 1.37174, 0.00519148, 0.0146205)

reports.append(Report(580190208, ("DT", -1, 2, 5), "MBwhBst2sec05"))
reports[-1].posNum = 117492
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(8.53025e-05, 0.00369293, 0), \
                           ValErr(-6.77342e-05, 0.00394459, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.82678e-06, 4.11009e-05, 0), \
                           -396204, 117492, 117492, -nan)
reports[-1].sigmax = ValErr(1.26208, 0.00260358, 0)
reports[-1].sigmay = ValErr(1.35195, 0.00278898, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00204375, -0.00132482, 0.00192631, 0.00300415, 4.82996e-05, -7.26404e-05, 0.00194353, 0.00297523, 4.82996e-05, -7.26404e-05, 0.00194353, 0.00297523, 0.000118559, -0.00317101, 0.0019708, 0.00296603, 0.000118559, -0.00317101, 0.0019708, 0.00296603, 1.26207, 1.35195, 0.00507444, 0.014897, 1.26207, 1.35195, 0.00507444, 0.014897)

reports.append(Report(580452352, ("DT", -1, 2, 6), "MBwhBst2sec06"))
reports[-1].posNum = 102344
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.00106946, 0.00160879, 0), \
                           ValErr(-0.000759037, 0.00439687, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.53624e-05, 4.58082e-05, 0), \
                           -350714, 102344, 102344, -nan)
reports[-1].sigmax = ValErr(1.30378, 0.00287941, 0)
reports[-1].sigmay = ValErr(1.38219, 0.00305391, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00060069, -0.00344553, 3.71636e-05, 0.00379589, 0.00121762, -0.00061801, 2.97526e-05, 0.0037448, 0.00121762, -0.00061801, 2.97526e-05, 0.0037448, 0.00474619, 0.000681595, 1.54727e-05, 0.00378025, 0.00474619, 0.000681595, 1.54727e-05, 0.00378025, 1.30379, 1.38219, 0.00518012, 0.0152321, 1.30379, 1.38219, 0.00518012, 0.0152321)

reports.append(Report(580714496, ("DT", -1, 2, 7), "MBwhBst2sec07"))
reports[-1].posNum = 134714
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000158611, 0.00353725, 0), \
                           ValErr(-0.0018603, 0.00373421, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.26573e-05, 3.94707e-05, 0), \
                           -459238, 134714, 134714, -nan)
reports[-1].sigmax = ValErr(1.2916, 0.00248871, 0)
reports[-1].sigmay = ValErr(1.37056, 0.00264082, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00155443, 0.00125394, -0.000348638, 0.00214322, 0.000456047, -0.00184513, -0.000351088, 0.00208161, 0.000456047, -0.00184513, -0.000351088, 0.00208161, 0.00323806, -0.00698593, -0.000407559, 0.002126, 0.00323806, -0.00698593, -0.000407559, 0.002126, 1.29157, 1.3706, 0.00515983, 0.014512, 1.29157, 1.3706, 0.00515983, 0.014512)

reports.append(Report(580976640, ("DT", -1, 2, 8), "MBwhBst2sec08"))
reports[-1].posNum = 135312
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.00036027, 0.00349848, 0), \
                           ValErr(6.18453e-05, 0.00367175, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.16266e-07, 3.90291e-05, 0), \
                           -457904, 135312, 135312, -nan)
reports[-1].sigmax = ValErr(1.27841, 0.00245753, 0)
reports[-1].sigmay = ValErr(1.35063, 0.00259635, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00398315, 0.00143031, -0.000296555, 0.00159855, -0.000367629, 6.14601e-05, -0.00031774, 0.00155947, -0.000367629, 6.14601e-05, -0.00031774, 0.00155947, 0.00220979, -0.00292224, -0.000331985, 0.00158667, 0.00220979, -0.00292224, -0.000331985, 0.00158667, 1.2784, 1.35063, 0.00519218, 0.0145083, 1.2784, 1.35063, 0.00519218, 0.0145083)

reports.append(Report(581238784, ("DT", -1, 2, 9), "MBwhBst2sec09"))
reports[-1].posNum = 112630
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000242253, 0.00384195, 0), \
                           ValErr(0.000982681, 0.00403437, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.0917e-06, 4.29347e-05, 0), \
                           -381972, 112630, 112630, -nan)
reports[-1].sigmax = ValErr(1.28576, 0.0027094, 0)
reports[-1].sigmay = ValErr(1.35277, 0.00285056, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00235269, -0.00242486, 0.000510278, 0.00264316, -0.000228596, 0.000974513, 0.00051273, 0.00264207, -0.000228596, 0.000974513, 0.00051273, 0.00264207, -0.00318809, 0.000200009, 0.000509953, 0.00264086, -0.00318809, 0.000200009, 0.000509953, 0.00264086, 1.28576, 1.35277, 0.00522695, 0.0148778, 1.28576, 1.35277, 0.00522695, 0.0148778)

reports.append(Report(581500928, ("DT", -1, 2, 10), "MBwhBst2sec10"))
reports[-1].posNum = 113166
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.00252143, 0.00383786, 0), \
                           ValErr(0.000701259, 0.00406047, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.95232e-05, 4.29528e-05, 0), \
                           -385085, 113166, 113166, -nan)
reports[-1].sigmax = ValErr(1.28805, 0.00270745, 0)
reports[-1].sigmay = ValErr(1.36592, 0.00287114, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00259495, -0.00100729, 0.00192336, 0.00153451, -0.00215994, 0.000665297, 0.00194514, 0.00143266, -0.00215994, 0.000665297, 0.00194514, 0.00143266, -0.00355444, -0.0025123, 0.00196524, 0.00148267, -0.00355444, -0.0025123, 0.00196524, 0.00148267, 1.28804, 1.36593, 0.00516892, 0.0146279, 1.28804, 1.36593, 0.00516892, 0.0146279)

reports.append(Report(581763072, ("DT", -1, 2, 11), "MBwhBst2sec11"))
reports[-1].posNum = 112878
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.0023676, 0.00156732, 0), \
                           ValErr(0.000367512, 0.00397954, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.28478e-05, 4.1797e-05, 0), \
                           -382130, 112878, 112878, -nan)
reports[-1].sigmax = ValErr(1.27255, 0.00266273, 0)
reports[-1].sigmay = ValErr(1.35858, 0.00284885, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00373745, 0.000855667, 0.00170581, 0.00305438, -0.00251089, 0.000275562, 0.00170335, 0.00294761, -0.00251089, 0.000275562, 0.00170335, 0.00294761, -0.00310177, -0.00620277, 0.0016992, 0.00296127, -0.00310177, -0.00620277, 0.0016992, 0.00296127, 1.27256, 1.35857, 0.00508469, 0.0148415, 1.27256, 1.35857, 0.00508469, 0.0148415)

reports.append(Report(582025216, ("DT", -1, 2, 12), "MBwhBst2sec12"))
reports[-1].posNum = 120520
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.00203764, 0.00373863, 0), \
                           ValErr(-0.000942748, 0.00392395, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.37245e-06, 4.21979e-05, 0), \
                           -409916, 120520, 120520, -nan)
reports[-1].sigmax = ValErr(1.28966, 0.00262718, 0)
reports[-1].sigmay = ValErr(1.36203, 0.00277457, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00335557, -0.000911364, -0.000641142, 0.00352996, 0.00210297, -0.000932493, -0.000647789, 0.00340081, 0.00210297, -0.000932493, -0.000647789, 0.00340081, 0.00202244, -0.00405248, -0.000653909, 0.00340129, 0.00202244, -0.00405248, -0.000653909, 0.00340129, 1.28965, 1.36204, 0.00522822, 0.0148961, 1.28965, 1.36204, 0.00522822, 0.0148961)

reports.append(Report(583335936, ("DT", -1, 3, 1), "MBwhBst3sec01"))
reports[-1].posNum = 111664
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.00241488, 0.00516837, 0), \
                           ValErr(0.000351436, 0.00531278, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.86943e-06, 5.06083e-05, 0), \
                           -441839, 111664, 111664, -nan)
reports[-1].sigmax = ValErr(1.72486, 0.00364999, 0)
reports[-1].sigmay = ValErr(1.77508, 0.00375627, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00762153, 0.0026727, -0.000464738, 0.00474804, -0.00242322, 0.000351516, -0.000447234, 0.00495691, -0.00242322, 0.000351516, -0.000447234, 0.00495691, -0.00356177, 0.00141938, -0.000446781, 0.00496641, -0.00356177, 0.00141938, -0.000446781, 0.00496641, 1.72486, 1.77507, 0.00609443, 0.0135716, 1.72486, 1.77507, 0.00609443, 0.0135716)

reports.append(Report(583598080, ("DT", -1, 3, 2), "MBwhBst3sec02"))
reports[-1].posNum = 98108
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000837342, 0.00547502, 0), \
                           ValErr(0.00148198, 0.00567464, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.7393e-05, 5.33679e-05, 0), \
                           -387241, 98108, 98108, -nan)
reports[-1].sigmax = ValErr(1.71144, 0.0038637, 0)
reports[-1].sigmay = ValErr(1.77159, 0.00399946, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00210102, 0.00308297, -0.000561779, -0.000585107, 0.000399136, 0.00206109, -0.000533069, -0.000487936, 0.000399136, 0.00206109, -0.000533069, -0.000487936, -0.00180003, 0.00168215, -0.000543545, -0.000465946, -0.00180003, 0.00168215, -0.000543545, -0.000465946, 1.71148, 1.77157, 0.00597877, 0.0132382, 1.71148, 1.77157, 0.00597877, 0.0132382)

reports.append(Report(583860224, ("DT", -1, 3, 3), "MBwhBst3sec03"))
reports[-1].posNum = 78686
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.0016216, 0.00607208, 0), \
                           ValErr(0.00104792, 0.00632379, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.13523e-05, 6.40844e-05, 0), \
                           -310201, 78686, 78686, -nan)
reports[-1].sigmax = ValErr(1.70219, 0.00429088, 0)
reports[-1].sigmay = ValErr(1.77265, 0.00446847, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000593258, -0.00880402, -0.000339853, -0.00151193, -0.00169257, 0.000967227, -0.000293388, -0.0013549, -0.00169257, 0.000967227, -0.000293388, -0.0013549, -0.00138467, -0.00415282, -0.00027679, -0.00125378, -0.00138467, -0.00415282, -0.00027679, -0.00125378, 1.70219, 1.77264, 0.00598573, 0.0134403, 1.70219, 1.77264, 0.00598573, 0.0134403)

reports.append(Report(584122368, ("DT", -1, 3, 4), "MBwhBst3sec04"))
reports[-1].posNum = 105844
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000261574, 0.00530189, 0), \
                           ValErr(0.000447191, 0.00546742, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.59728e-05, 5.17166e-05, 0), \
                           -418899, 105844, 105844, -nan)
reports[-1].sigmax = ValErr(1.72431, 0.00374774, 0)
reports[-1].sigmay = ValErr(1.77712, 0.00386254, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00378832, 0.00421323, 0.000172257, -0.00331435, 0.000384554, 0.000239086, 0.000183305, -0.00317158, 0.000384554, 0.000239086, 0.000183305, -0.00317158, 0.00116462, 0.00327953, 0.000185037, -0.00312488, 0.00116462, 0.00327953, 0.000185037, -0.00312488, 1.72433, 1.77712, 0.00602595, 0.0141953, 1.72433, 1.77712, 0.00602595, 0.0141953)

reports.append(Report(584384512, ("DT", -1, 3, 5), "MBwhBst3sec05"))
reports[-1].posNum = 102548
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000862891, 0.00530014, 0), \
                           ValErr(0.000759755, 0.00546163, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.36441e-06, 5.22188e-05, 0), \
                           -402455, 102548, 102548, -nan)
reports[-1].sigmax = ValErr(1.6961, 0.00374518, 0)
reports[-1].sigmay = ValErr(1.74778, 0.0038593, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00305886, -0.000953755, 0.000141534, 0.000259349, -0.00087557, 0.000773437, 0.000146939, 0.00036284, -0.00087557, 0.000773437, 0.000146939, 0.00036284, 0.000151018, 0.00147594, 0.000155723, 0.000383573, 0.000151018, 0.00147594, 0.000155723, 0.000383573, 1.6961, 1.74778, 0.00588968, 0.0132249, 1.6961, 1.74778, 0.00588968, 0.0132249)

reports.append(Report(584646656, ("DT", -1, 3, 6), "MBwhBst3sec06"))
reports[-1].posNum = 94432
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.00197205, 0.00566014, 0), \
                           ValErr(-0.000152718, 0.00583654, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.48058e-06, 5.70233e-05, 0), \
                           -375363, 94432, 94432, -nan)
reports[-1].sigmax = ValErr(1.73888, 0.00400125, 0)
reports[-1].sigmay = ValErr(1.79291, 0.00412557, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00633412, -0.00276965, 0.000616024, 2.17909e-05, -0.00198473, -0.000167517, 0.000603573, 0.000181251, -0.00198473, -0.000167517, 0.000603573, 0.000181251, 0.00537114, -0.00568876, 0.00058239, 0.000199864, 0.00537114, -0.00568876, 0.00058239, 0.000199864, 1.73888, 1.7929, 0.00617928, 0.0134801, 1.73888, 1.7929, 0.00617928, 0.0134801)

reports.append(Report(584908800, ("DT", -1, 3, 7), "MBwhBst3sec07"))
reports[-1].posNum = 98708
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000243363, 0.00553799, 0), \
                           ValErr(-0.00163036, 0.00570664, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.11177e-05, 5.46715e-05, 0), \
                           -391345, 98708, 98708, -nan)
reports[-1].sigmax = ValErr(1.73635, 0.00390794, 0)
reports[-1].sigmay = ValErr(1.77715, 0.00399976, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00363871, -0.00462219, 4.79888e-05, 0.000402096, 0.000171307, -0.00178391, 4.94432e-05, 0.000533464, 0.000171307, -0.00178391, 4.94432e-05, 0.000533464, 0.000478043, 0.00132508, 3.61732e-05, 0.00056751, 0.000478043, 0.00132508, 3.61732e-05, 0.00056751, 1.73635, 1.77715, 0.00605018, 0.013367, 1.73635, 1.77715, 0.00605018, 0.013367)

reports.append(Report(585170944, ("DT", -1, 3, 8), "MBwhBst3sec08"))
reports[-1].posNum = 113638
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000444334, 0.00509137, 0), \
                           ValErr(-0.00119852, 0.00522666, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.01658e-05, 4.98274e-05, 0), \
                           -448096, 113638, 113638, -nan)
reports[-1].sigmax = ValErr(1.71432, 0.003596, 0)
reports[-1].sigmay = ValErr(1.76172, 0.0036954, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00239916, 0.00179955, 0.000564722, -0.00035684, -0.000395429, -0.00121417, 0.000564043, -0.000287722, -0.000395429, -0.00121417, 0.000564043, -0.000287722, -0.00864915, -0.00356077, 0.000589768, -0.000267947, -0.00864915, -0.00356077, 0.000589768, -0.000267947, 1.71432, 1.76172, 0.00595082, 0.0135229, 1.71432, 1.76172, 0.00595082, 0.0135229)

reports.append(Report(585433088, ("DT", -1, 3, 9), "MBwhBst3sec09"))
reports[-1].posNum = 87926
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.0003188, 0.00580671, 0), \
                           ValErr(0.000371618, 0.00592867, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.34036e-07, 5.67383e-05, 0), \
                           -346868, 87926, 87926, -nan)
reports[-1].sigmax = ValErr(1.72179, 0.00410593, 0)
reports[-1].sigmay = ValErr(1.75727, 0.0041905, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00897787, 0.00388023, -6.56328e-05, 0.00109488, -0.000318834, 0.000372666, -4.80801e-05, 0.00120372, -0.000318834, 0.000372666, -4.80801e-05, 0.00120372, 0.00638158, -0.00375409, -5.52637e-05, 0.00121743, 0.00638158, -0.00375409, -5.52637e-05, 0.00121743, 1.72179, 1.75727, 0.00598817, 0.0135389, 1.72179, 1.75727, 0.00598817, 0.0135389)

reports.append(Report(585695232, ("DT", -1, 3, 10), "MBwhBst3sec10"))
reports[-1].posNum = 37264
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.00262408, 0.0107699, 0), \
                           ValErr(0.0051128, 0.00869884, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.06914e-05, 9.91619e-05, 0), \
                           -144449, 37264, 37264, -nan)
reports[-1].sigmax = ValErr(1.68236, 0.00616252, 0)
reports[-1].sigmay = ValErr(1.67917, 0.00615083, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00241137, 0.00769489, -0.00130642, -0.00124401, -0.00130283, 0.00512546, -0.0012797, -0.00102347, -0.00130283, 0.00512546, -0.0012797, -0.00102347, -0.0156279, 0.00481296, -0.00122702, -0.000975284, -0.0156279, 0.00481296, -0.00122702, -0.000975284, 1.68236, 1.67917, 0.00587868, 0.0132333, 1.68236, 1.67917, 0.00587868, 0.0132333)

reports.append(Report(585957376, ("DT", -1, 3, 11), "MBwhBst3sec11"))
reports[-1].posNum = 91724
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.00104335, 0.00567892, 0), \
                           ValErr(-0.0015402, 0.00585716, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.65908e-07, 5.60051e-05, 0), \
                           -362608, 91724, 91724, -nan)
reports[-1].sigmax = ValErr(1.71992, 0.00401563, 0)
reports[-1].sigmay = ValErr(1.77375, 0.00414132, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00635522, -0.00311265, -0.00156826, -4.77401e-05, -0.00104248, -0.00154073, -0.00159528, 6.11923e-05, -0.00104248, -0.00154073, -0.00159528, 6.11923e-05, -0.00113438, -0.00859496, -0.00158233, 7.88888e-05, -0.00113438, -0.00859496, -0.00158233, 7.88888e-05, 1.71991, 1.77375, 0.00601961, 0.013642, 1.71991, 1.77375, 0.00601961, 0.013642)

reports.append(Report(586219520, ("DT", -1, 3, 12), "MBwhBst3sec12"))
reports[-1].posNum = 85290
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.00248196, 0.00592492, 0), \
                           ValErr(-0.00307969, 0.00611825, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.8915e-05, 5.60612e-05, 0), \
                           -337598, 85290, 85290, -nan)
reports[-1].sigmax = ValErr(1.72782, 0.0041836, 0)
reports[-1].sigmay = ValErr(1.77446, 0.00429658, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00364762, -0.00340691, 0.00240187, 0.000321892, 0.00237454, -0.00283588, 0.00240217, 0.00043026, 0.00237454, -0.00283588, 0.00240217, 0.00043026, 0.00669319, -0.00934507, 0.00239501, 0.000424996, 0.00669319, -0.00934507, 0.00239501, 0.000424996, 1.72781, 1.77448, 0.00605715, 0.0134244, 1.72781, 1.77448, 0.00605715, 0.0134244)

reports.append(Report(574980096, ("DT", 0, 1, 1), "MBwhCst1sec01"))
reports[-1].posNum = 78374
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000583708, 0.00329052, 0), \
                           ValErr(-0.00118152, 0.0031606, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.88732e-06, 3.69379e-05, 0), \
                           -205298, 78374, 78374, -nan)
reports[-1].sigmax = ValErr(0.909889, 0.0022982, 0)
reports[-1].sigmay = ValErr(0.883401, 0.0022313, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00170326, -0.00426418, 0.000485835, -0.000866762, 0.000678024, -0.0011501, 0.000474047, -0.000828341, 0.000678024, -0.0011501, 0.000474047, -0.000828341, -0.00274769, 0.0022436, 0.000510187, -0.000801185, -0.00274769, 0.0022436, 0.000510187, -0.000801185, 0.909888, 0.883401, 0.00487854, 0.0109247, 0.909888, 0.883401, 0.00487854, 0.0109247)

reports.append(Report(576028672, ("DT", 0, 1, 5), "MBwhCst1sec05"))
reports[-1].posNum = 121446
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000120834, 0.0015381, 0), \
                           ValErr(8.49189e-05, 0.00251233, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(7.58681e-06, 2.87262e-05, 0), \
                           -316514, 121446, 121446, -nan)
reports[-1].sigmax = ValErr(0.90607, 0.00183439, 0)
reports[-1].sigmay = ValErr(0.875442, 0.00177638, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00383907, 0.00056081, 0.000615598, 8.39191e-05, -7.78573e-05, 5.36312e-05, 0.000626643, 0.000161095, -7.78573e-05, 5.36312e-05, 0.000626643, 0.000161095, -0.00234958, -0.000460059, 0.000686184, 0.000159797, -0.00234958, -0.000460059, 0.000686184, 0.000159797, 0.90607, 0.875443, 0.00483547, 0.0106315, 0.90607, 0.875443, 0.00483547, 0.0106315)

reports.append(Report(577077248, ("DT", 0, 1, 9), "MBwhCst1sec09"))
reports[-1].posNum = 79574
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000320524, 0.00326, 0), \
                           ValErr(1.85927e-05, 0.00312996, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.09973e-06, 3.59725e-05, 0), \
                           -208726, 79574, 79574, -nan)
reports[-1].sigmax = ValErr(0.916289, 0.00229692, 0)
reports[-1].sigmay = ValErr(0.880376, 0.00220689, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00158117, -0.00350765, 0.000924435, 3.92138e-05, 0.000304758, 3.00723e-05, 0.000950874, 4.16119e-05, 0.000304758, 3.00723e-05, 0.000950874, 4.16119e-05, 0.00331159, -0.00282504, 0.000901207, 9.26358e-05, 0.00331159, -0.00282504, 0.000901207, 9.26358e-05, 0.916287, 0.880372, 0.0050775, 0.0107656, 0.916287, 0.880372, 0.0050775, 0.0107656)

reports.append(Report(575242240, ("DT", 0, 1, 2), "MBwhCst1sec02"))
reports[-1].posNum = 51058
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000545519, 0.00407789, 0), \
                           ValErr(0.000306541, 0.00385974, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.98624e-06, 4.55842e-05, 0), \
                           -132669, 51058, 51058, -nan)
reports[-1].sigmax = ValErr(0.90292, 0.00282554, 0)
reports[-1].sigmay = ValErr(0.871658, 0.00272772, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00310921, 0.00114674, 0.000555983, -0.00258358, 0.000719568, 0.000332565, 0.000561339, -0.00205337, 0.000719568, 0.000332565, 0.000561339, -0.00205337, 0.00570082, 0.00219938, 0.000533919, -0.00227122, 0.00570082, 0.00219938, 0.000533919, -0.00227122, 0.902921, 0.871657, 0.00482138, 0.0124907, 0.902921, 0.871657, 0.00482138, 0.0124907)

reports.append(Report(576290816, ("DT", 0, 1, 6), "MBwhCst1sec06"))
reports[-1].posNum = 102824
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-3.59441e-05, 0.00156925, 0), \
                           ValErr(0.000284151, 0.0027885, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.435e-06, 3.28172e-05, 0), \
                           -271417, 102824, 102824, -nan)
reports[-1].sigmax = ValErr(0.918941, 0.00202659, 0)
reports[-1].sigmay = ValErr(0.892508, 0.00196806, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00123609, -0.000260138, -0.0016541, -0.000364532, -5.23284e-05, 0.000230427, -0.00168963, -0.000352353, -5.23284e-05, 0.000230427, -0.00168963, -0.000352353, 0.00315631, 0.00692296, -0.00171904, -0.000396409, 0.00315631, 0.00692296, -0.00171904, -0.000396409, 0.918945, 0.892504, 0.00502983, 0.0104963, 0.918945, 0.892504, 0.00502983, 0.0104963)

reports.append(Report(577339392, ("DT", 0, 1, 10), "MBwhCst1sec10"))
reports[-1].posNum = 74936
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.00052265, 0.00328722, 0), \
                           ValErr(-0.000311172, 0.0031878, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.40173e-07, 3.6695e-05, 0), \
                           -194323, 74936, 74936, -nan)
reports[-1].sigmax = ValErr(0.898203, 0.00232018, 0)
reports[-1].sigmay = ValErr(0.871689, 0.00225168, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00453096, -0.000341816, -0.00135632, -0.00140059, -0.000521888, -0.000309509, -0.00140082, -0.00133553, -0.000521888, -0.000309509, -0.00140082, -0.00133553, -0.00141661, 0.00314923, -0.00146053, -0.00134739, -0.00141661, 0.00314923, -0.00146053, -0.00134739, 0.898201, 0.871689, 0.00499522, 0.0109917, 0.898201, 0.871689, 0.00499522, 0.0109917)

reports.append(Report(575504384, ("DT", 0, 1, 3), "MBwhCst1sec03"))
reports[-1].posNum = 75908
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000640165, 0.00330014, 0), \
                           ValErr(0.000198118, 0.00321738, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(8.77681e-06, 3.81999e-05, 0), \
                           -198137, 75908, 75908, -nan)
reports[-1].sigmax = ValErr(0.904775, 0.0023221, 0)
reports[-1].sigmay = ValErr(0.880214, 0.00225907, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00246223, -0.00292816, -0.000821798, 0.00070612, -0.000724309, 0.000110023, -0.000836867, 0.000780377, -0.000724309, 0.000110023, -0.000836867, 0.000780377, 0.002945, -0.00347267, -0.000878694, 0.000867345, 0.002945, -0.00347267, -0.000878694, 0.000867345, 0.904779, 0.880215, 0.0048681, 0.0108244, 0.904779, 0.880215, 0.0048681, 0.0108244)

reports.append(Report(576552960, ("DT", 0, 1, 7), "MBwhCst1sec07"))
reports[-1].posNum = 101816
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000261963, 0.00289322, 0), \
                           ValErr(0.000419382, 0.00277362, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.68311e-05, 3.36704e-05, 0), \
                           -267476, 101816, 101816, -nan)
reports[-1].sigmax = ValErr(0.918648, 0.00203578, 0)
reports[-1].sigmay = ValErr(0.881639, 0.00195376, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00104016, -0.000787923, 0.00178744, -3.46248e-05, 0.000565963, 0.000157895, 0.00177708, 1.38002e-05, 0.000565963, 0.000157895, 0.00177708, 1.38002e-05, 0.000919773, -0.0012389, 0.00170996, 6.47338e-05, 0.000919773, -0.0012389, 0.00170996, 6.47338e-05, 0.91864, 0.88165, 0.00491031, 0.0111539, 0.91864, 0.88165, 0.00491031, 0.0111539)

reports.append(Report(577601536, ("DT", 0, 1, 11), "MBwhCst1sec11"))
reports[-1].posNum = 76894
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000139444, 0.0024019, 0), \
                           ValErr(-0.000101428, 0.00307336, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.31944e-05, 3.49599e-05, 0), \
                           -200286, 76894, 76894, -nan)
reports[-1].sigmax = ValErr(0.902387, 0.00230601, 0)
reports[-1].sigmay = ValErr(0.877685, 0.00222683, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00117589, -0.00102568, 3.80311e-05, -0.000336044, -2.44685e-05, -0.000314602, 4.17065e-05, -0.000269966, -2.44685e-05, -0.000314602, 4.17065e-05, -0.000269966, 0.000347476, -0.000190921, 1.28084e-05, -0.000239128, 0.000347476, -0.000190921, 1.28084e-05, -0.000239128, 0.902381, 0.877693, 0.00486063, 0.011158, 0.902381, 0.877693, 0.00486063, 0.011158)

reports.append(Report(575766528, ("DT", 0, 1, 4), "MBwhCst1sec04"))
reports[-1].posNum = 90406
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000294573, 0.00303901, 0), \
                           ValErr(0.0018009, 0.00294122, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.41391e-05, 3.55817e-05, 0), \
                           -236513, 90406, 90406, -nan)
reports[-1].sigmax = ValErr(0.909101, 0.00213795, 0)
reports[-1].sigmay = ValErr(0.881211, 0.00207237, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00114108, -0.000118505, 0.00214091, -0.0017319, -0.000419249, 0.00170218, 0.00218224, -0.00167562, -0.000419249, 0.00170218, 0.00218224, -0.00167562, -0.0020072, 0.00244271, 0.00215677, -0.0016645, -0.0020072, 0.00244271, 0.00215677, -0.0016645, 0.909101, 0.881211, 0.00494102, 0.0100814, 0.909101, 0.881211, 0.00494102, 0.0100814)

reports.append(Report(576815104, ("DT", 0, 1, 8), "MBwhCst1sec08"))
reports[-1].posNum = 105100
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.00100509, 0.00279917, 0), \
                           ValErr(-0.000990668, 0.00271402, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.775e-06, 3.1564e-05, 0), \
                           -274109, 105100, 105100, -nan)
reports[-1].sigmax = ValErr(0.90698, 0.00197825, 0)
reports[-1].sigmay = ValErr(0.876201, 0.00191112, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00245619, -0.000637547, 0.000213595, 0.000572887, -0.00098763, -0.000952652, 0.000227961, 0.000561632, -0.00098763, -0.000952652, 0.000227961, 0.000561632, -0.00224981, -0.00098813, 0.000252831, 0.000553818, -0.00224981, -0.00098813, 0.000252831, 0.000553818, 0.90698, 0.8762, 0.00483598, 0.0108846, 0.90698, 0.8762, 0.00483598, 0.0108846)

reports.append(Report(577863680, ("DT", 0, 1, 12), "MBwhCst1sec12"))
reports[-1].posNum = 107320
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000365695, 0.00198615, 0), \
                           ValErr(-5.15152e-05, 0.00257102, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.12162e-05, 3.12479e-05, 0), \
                           -281163, 107320, 107320, -nan)
reports[-1].sigmax = ValErr(0.911206, 0.00195362, 0)
reports[-1].sigmay = ValErr(0.88247, 0.0018963, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00336896, -0.00314081, 0.000505545, 0.00084686, -0.000316631, -5.36356e-05, 0.000522946, 0.000914934, -0.000316631, -5.36356e-05, 0.000522946, 0.000914934, -0.00248619, 0.00431715, 0.000515011, 0.000860284, -0.00248619, 0.00431715, 0.000515011, 0.000860284, 0.911207, 0.882467, 0.0049955, 0.010744, 0.911207, 0.882467, 0.0049955, 0.010744)

reports.append(Report(579174400, ("DT", 0, 2, 1), "MBwhCst2sec01"))
reports[-1].posNum = 65664
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000269562, 0.00480367, 0), \
                           ValErr(0.000293007, 0.00462571, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.67962e-05, 4.86057e-05, 0), \
                           -211116, 65664, 65664, -nan)
reports[-1].sigmax = ValErr(1.22996, 0.00339009, 0)
reports[-1].sigmay = ValErr(1.1856, 0.00326953, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00944813, 0.0035788, 6.48125e-05, -0.00062736, 0.000539638, 8.89897e-05, 5.89775e-05, -0.000668461, 0.000539638, 8.89897e-05, 5.89775e-05, -0.000668461, 0.00264611, 0.00861914, -8.49659e-05, -0.000651242, 0.00264611, 0.00861914, -8.49659e-05, -0.000651242, 1.22999, 1.18558, 0.00524999, 0.0117444, 1.22999, 1.18558, 0.00524999, 0.0117444)

reports.append(Report(580222976, ("DT", 0, 2, 5), "MBwhCst2sec05"))
reports[-1].posNum = 103254
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.00137564, 0.00376414, 0), \
                           ValErr(-0.000492087, 0.00364224, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(9.03965e-06, 3.86342e-05, 0), \
                           -328289, 103254, 103254, -nan)
reports[-1].sigmax = ValErr(1.20951, 0.00265598, 0)
reports[-1].sigmay = ValErr(1.1634, 0.00255721, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0047896, -0.00321302, -0.000319189, -5.22548e-06, 0.00138224, -0.000498022, -0.000329837, -1.19809e-05, 0.00138224, -0.000498022, -0.000329837, -1.19809e-05, 0.000218076, -0.00279308, -0.000366103, -5.77571e-05, 0.000218076, -0.00279308, -0.000366103, -5.77571e-05, 1.2095, 1.16341, 0.00511851, 0.0112877, 1.2095, 1.16341, 0.00511851, 0.0112877)

reports.append(Report(581271552, ("DT", 0, 2, 9), "MBwhCst2sec09"))
reports[-1].posNum = 66834
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.00141058, 0.00472951, 0), \
                           ValErr(0.000846198, 0.00452504, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.06602e-05, 4.76515e-05, 0), \
                           -212854, 66834, 66834, -nan)
reports[-1].sigmax = ValErr(1.22269, 0.0033446, 0)
reports[-1].sigmay = ValErr(1.15707, 0.00316506, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00316589, 0.00014814, 0.000924375, -0.000539426, -0.00141623, 0.00155484, 0.000930592, -0.000516309, -0.00141623, 0.00155484, 0.000930592, -0.000516309, 0.000934956, -0.0010722, 0.000826515, -0.000535051, 0.000934956, -0.0010722, 0.000826515, -0.000535051, 1.22274, 1.15702, 0.00515278, 0.0118598, 1.22274, 1.15702, 0.00515278, 0.0118598)

reports.append(Report(579436544, ("DT", 0, 2, 2), "MBwhCst2sec02"))
reports[-1].posNum = 42240
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000289914, 0.00293735, 0), \
                           ValErr(-0.000551617, 0.00620753, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.91472e-05, 5.81654e-05, 0), \
                           -141300, 42240, 42240, -nan)
reports[-1].sigmax = ValErr(1.32168, 0.00454179, 0)
reports[-1].sigmay = ValErr(1.25658, 0.00428043, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0067073, 0.00533923, 0.00331288, 0.000513452, 0.000297309, -0.000598248, 0.00335525, 0.000553971, 0.000297309, -0.000598248, 0.00335525, 0.000553971, -0.00519806, -0.00137112, 0.00343722, 0.00053398, -0.00519806, -0.00137112, 0.00343722, 0.00053398, 1.32166, 1.2566, 0.0056415, 0.0114366, 1.32166, 1.2566, 0.0056415, 0.0114366)

reports.append(Report(580485120, ("DT", 0, 2, 6), "MBwhCst2sec06"))
reports[-1].posNum = 103626
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.00111682, 0.00386209, 0), \
                           ValErr(0.000849262, 0.00357907, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.38525e-05, 3.93068e-05, 0), \
                           -335122, 103626, 103626, -nan)
reports[-1].sigmax = ValErr(1.24163, 0.00271591, 0)
reports[-1].sigmay = ValErr(1.19681, 0.00262364, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000967391, 0.00495273, 0.00295942, 0.00211945, -0.00103759, 0.000914239, 0.00299544, 0.0020697, -0.00103759, 0.000914239, 0.00299544, 0.0020697, -0.000509648, -0.000627826, 0.0030091, 0.00202421, -0.000509648, -0.000627826, 0.0030091, 0.00202421, 1.24162, 1.19682, 0.0051763, 0.0114679, 1.24162, 1.19682, 0.0051763, 0.0114679)

reports.append(Report(581533696, ("DT", 0, 2, 10), "MBwhCst2sec10"))
reports[-1].posNum = 72500
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000753903, 0.00453281, 0), \
                           ValErr(0.00193218, 0.00434507, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.13901e-06, 4.63122e-05, 0), \
                           -231011, 72500, 72500, -nan)
reports[-1].sigmax = ValErr(1.21256, 0.00318432, 0)
reports[-1].sigmay = ValErr(1.16853, 0.00306872, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00162795, 0.00355096, -0.000266963, 0.000846279, 0.000674841, 0.00190821, -0.000238201, 0.000796702, 0.000674841, 0.00190821, -0.000238201, 0.000796702, -0.00265675, 0.00353525, -0.000167267, 0.00078743, -0.00265675, 0.00353525, -0.000167267, 0.00078743, 1.21256, 1.16853, 0.00520178, 0.0118117, 1.21256, 1.16853, 0.00520178, 0.0118117)

reports.append(Report(579698688, ("DT", 0, 2, 3), "MBwhCst2sec03"))
reports[-1].posNum = 84730
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000558901, 0.00424742, 0), \
                           ValErr(-0.00061922, 0.00412346, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.36788e-06, 4.41564e-05, 0), \
                           -273053, 84730, 84730, -nan)
reports[-1].sigmax = ValErr(1.23612, 0.0030028, 0)
reports[-1].sigmay = ValErr(1.18859, 0.00288738, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.000406804, -0.00277067, 0.0039309, 0.00164153, -0.000529381, -0.000663448, 0.00397126, 0.00163484, -0.000529381, -0.000663448, 0.00397126, 0.00163484, -0.00243409, -0.00106526, 0.00400832, 0.0016466, -0.00243409, -0.00106526, 0.00400832, 0.0016466, 1.23612, 1.18859, 0.00523508, 0.0117849, 1.23612, 1.18859, 0.00523508, 0.0117849)

reports.append(Report(580747264, ("DT", 0, 2, 7), "MBwhCst2sec07"))
reports[-1].posNum = 100106
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000823805, 0.00186593, 0), \
                           ValErr(0.00117278, 0.00369444, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.9425e-06, 3.97532e-05, 0), \
                           -323907, 100106, 100106, -nan)
reports[-1].sigmax = ValErr(1.24502, 0.00276578, 0)
reports[-1].sigmay = ValErr(1.19556, 0.00263774, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00180433, -0.000637091, 0.00285729, -0.000317548, 0.000813579, 0.00118686, 0.0028589, -0.000454456, 0.000813579, 0.00118686, 0.0028589, -0.000454456, -0.00116877, 0.0034515, 0.00294197, -0.000447815, -0.00116877, 0.0034515, 0.00294197, -0.000447815, 1.24501, 1.19557, 0.00528168, 0.0117733, 1.24501, 1.19557, 0.00528168, 0.0117733)

reports.append(Report(581795840, ("DT", 0, 2, 11), "MBwhCst2sec11"))
reports[-1].posNum = 70616
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.00286695, 0.0045727, 0), \
                           ValErr(-0.00606892, 0.00440859, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.31201e-05, 4.59894e-05, 0), \
                           -224816, 70616, 70616, -nan)
reports[-1].sigmax = ValErr(1.2122, 0.00322558, 0)
reports[-1].sigmay = ValErr(1.16571, 0.00310189, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00256145, -0.00426155, -0.000704324, 0.000406113, -0.00271047, -0.0058496, -0.000701478, 0.00042215, -0.00271047, -0.0058496, -0.000701478, 0.00042215, -0.00574306, -0.000982872, -0.000672695, 0.00036222, -0.00574306, -0.000982872, -0.000672695, 0.00036222, 1.2122, 1.16571, 0.00511704, 0.0114638, 1.2122, 1.16571, 0.00511704, 0.0114638)

reports.append(Report(579960832, ("DT", 0, 2, 4), "MBwhCst2sec04"))
reports[-1].posNum = 89512
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000265072, 0.00413108, 0), \
                           ValErr(-0.000279015, 0.00393428, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.78404e-05, 4.20336e-05, 0), \
                           -287241, 89512, 89512, -nan)
reports[-1].sigmax = ValErr(1.23177, 0.0029114, 0)
reports[-1].sigmay = ValErr(1.17661, 0.00278105, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00129984, -0.000306263, -0.000366288, -0.00177983, 0.000122071, -0.000232458, -0.000371367, -0.00184511, 0.000122071, -0.000232458, -0.000371367, -0.00184511, 0.000507058, -0.00359207, -0.000390542, -0.00188082, 0.000507058, -0.00359207, -0.000390542, -0.00188082, 1.23179, 1.1766, 0.00528469, 0.0111823, 1.23179, 1.1766, 0.00528469, 0.0111823)

reports.append(Report(581009408, ("DT", 0, 2, 8), "MBwhCst2sec08"))
reports[-1].posNum = 105154
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000402522, 0.00378474, 0), \
                           ValErr(0.000473729, 0.00363405, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.38955e-05, 3.81082e-05, 0), \
                           -337168, 105154, 105154, -nan)
reports[-1].sigmax = ValErr(1.22683, 0.00266949, 0)
reports[-1].sigmay = ValErr(1.17835, 0.0025673, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00363301, -0.00123767, 0.000349554, 0.0002756, 0.000308602, 0.000347961, 0.000332167, 0.000269806, 0.000308602, 0.000347961, 0.000332167, 0.000269806, -0.00359568, -0.00225386, 0.00025802, 0.000249198, -0.00359568, -0.00225386, 0.00025802, 0.000249198, 1.22679, 1.17838, 0.00516518, 0.0117742, 1.22679, 1.17838, 0.00516518, 0.0117742)

reports.append(Report(582057984, ("DT", 0, 2, 12), "MBwhCst2sec12"))
reports[-1].posNum = 89850
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000231062, 0.0040669, 0), \
                           ValErr(0.000437529, 0.00391596, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.3061e-05, 4.13663e-05, 0), \
                           -287138, 89850, 89850, -nan)
reports[-1].sigmax = ValErr(1.21896, 0.00287569, 0)
reports[-1].sigmay = ValErr(1.17336, 0.00276809, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(3.9313e-05, 0.00232702, 0.000599568, 0.000392146, 0.000194692, 0.000471962, 0.000583661, 0.000441505, 0.000194692, 0.000471962, 0.000583661, 0.000441505, 0.000466398, -0.000667187, 0.000558507, 0.000406282, 0.000466398, -0.000667187, 0.000558507, 0.000406282, 1.21897, 1.17336, 0.00515805, 0.0116509, 1.21897, 1.17336, 0.00515805, 0.0116509)

reports.append(Report(583368704, ("DT", 0, 3, 1), "MBwhCst3sec01"))
reports[-1].posNum = 61858
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.0010593, 0.00681202, 0), \
                           ValErr(-0.000447647, 0.00649653, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.93743e-05, 6.11147e-05, 0), \
                           -237613, 61858, 61858, -nan)
reports[-1].sigmax = ValErr(1.68997, 0.00480484, 0)
reports[-1].sigmay = ValErr(1.61395, 0.00458868, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00423008, 0.00540271, -0.000475216, -0.00247628, 0.000906086, -0.000545289, -0.000471928, -0.00248901, 0.000906086, -0.000545289, -0.000471928, -0.00248901, 0.00155944, -0.00240016, -0.000453484, -0.00245471, 0.00155944, -0.00240016, -0.000453484, -0.00245471, 1.68995, 1.61396, 0.00610366, 0.0119371, 1.68995, 1.61396, 0.00610366, 0.0119371)

reports.append(Report(584417280, ("DT", 0, 3, 5), "MBwhCst3sec05"))
reports[-1].posNum = 89802
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-9.02415e-05, 0.00553397, 0), \
                           ValErr(-0.000486512, 0.00532601, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.29807e-05, 5.15635e-05, 0), \
                           -342135, 89802, 89802, -nan)
reports[-1].sigmax = ValErr(1.65762, 0.00391138, 0)
reports[-1].sigmay = ValErr(1.59458, 0.00376264, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.000485979, -0.00289896, 0.00030854, 0.00180108, -1.73849e-05, -0.000581113, 0.000343551, 0.00178733, -1.73849e-05, -0.000581113, 0.000343551, 0.00178733, -0.0041424, -0.00325705, 0.000373676, 0.00180548, -0.0041424, -0.00325705, 0.000373676, 0.00180548, 1.65763, 1.59458, 0.00597259, 0.0114308, 1.65763, 1.59458, 0.00597259, 0.0114308)

reports.append(Report(585465856, ("DT", 0, 3, 9), "MBwhCst3sec09"))
reports[-1].posNum = 61794
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.00442904, 0.00679563, 0), \
                           ValErr(0.000672837, 0.00639647, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.88741e-06, 6.06795e-05, 0), \
                           -236236, 61794, 61794, -nan)
reports[-1].sigmax = ValErr(1.6889, 0.00480414, 0)
reports[-1].sigmay = ValErr(1.58568, 0.00451054, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0089653, 0.0021613, 0.00071019, 0.000591441, -0.00445111, 0.000742041, 0.000707142, 0.000549283, -0.00445111, 0.000742041, 0.000707142, 0.000549283, -0.0141868, -0.00608414, 0.000737011, 0.000538534, -0.0141868, -0.00608414, 0.000737011, 0.000538534, 1.6889, 1.58568, 0.00604964, 0.0110923, 1.6889, 1.58568, 0.00604964, 0.0110923)

reports.append(Report(583630848, ("DT", 0, 3, 2), "MBwhCst3sec02"))
reports[-1].posNum = 50098
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000251651, 0.00748918, 0), \
                           ValErr(0.000501335, 0.00712859, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.47618e-06, 6.65436e-05, 0), \
                           -191335, 50098, 50098, -nan)
reports[-1].sigmax = ValErr(1.67287, 0.00528493, 0)
reports[-1].sigmay = ValErr(1.59487, 0.00503853, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00810443, 0.00652144, 0.000501086, -0.000862336, 0.000182044, 0.000530783, 0.000470295, -0.00089378, 0.000182044, 0.000530783, 0.000470295, -0.00089378, -0.000192496, 0.00178026, 0.000462973, -0.000884535, -0.000192496, 0.00178026, 0.000462973, -0.000884535, 1.67287, 1.59488, 0.00602345, 0.0116413, 1.67287, 1.59488, 0.00602345, 0.0116413)

reports.append(Report(584679424, ("DT", 0, 3, 6), "MBwhCst3sec06"))
reports[-1].posNum = 82536
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000459122, 0.00584523, 0), \
                           ValErr(-0.0033489, 0.00558719, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.72805e-07, 5.35262e-05, 0), \
                           -315993, 82536, 82536, -nan)
reports[-1].sigmax = ValErr(1.67834, 0.00413097, 0)
reports[-1].sigmay = ValErr(1.6046, 0.00394944, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00547756, 0.00205664, 0.000502913, -0.000573764, 0.000456548, -0.00335001, 0.00049242, -0.000544914, 0.000456548, -0.00335001, 0.00049242, -0.000544914, 0.000632219, 0.00271935, 0.000473443, -0.000558807, 0.000632219, 0.00271935, 0.000473443, -0.000558807, 1.67834, 1.6046, 0.00603381, 0.01173, 1.67834, 1.6046, 0.00603381, 0.01173)

reports.append(Report(585728000, ("DT", 0, 3, 10), "MBwhCst3sec10"))
reports[-1].posNum = 60034
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.00141461, 0.00673138, 0), \
                           ValErr(0.000687582, 0.00646409, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.29734e-06, 6.27787e-05, 0), \
                           -227744, 60034, 60034, -nan)
reports[-1].sigmax = ValErr(1.64273, 0.00474081, 0)
reports[-1].sigmay = ValErr(1.58305, 0.00456857, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00292223, 0.00517968, 0.000517335, -0.00301949, -0.00138389, 0.000676335, 0.000468286, -0.00304927, -0.00138389, 0.000676335, 0.000468286, -0.00304927, -0.00918592, -0.00447835, 0.000502503, -0.00303562, -0.00918592, -0.00447835, 0.000502503, -0.00303562, 1.64273, 1.58305, 0.00596936, 0.011916, 1.64273, 1.58305, 0.00596936, 0.011916)

reports.append(Report(583892992, ("DT", 0, 3, 3), "MBwhCst3sec03"))
reports[-1].posNum = 79596
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.00197647, 0.00583758, 0), \
                           ValErr(0.00176817, 0.00561994, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.25489e-05, 5.48926e-05, 0), \
                           -302272, 79596, 79596, -nan)
reports[-1].sigmax = ValErr(1.64684, 0.00412754, 0)
reports[-1].sigmay = ValErr(1.58541, 0.00397356, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00693634, -0.00753631, 0.00050083, -0.00194104, -0.00202691, 0.00182326, 0.000473713, -0.00188369, -0.00202691, 0.00182326, 0.000473713, -0.00188369, -0.00414005, 0.00386966, 0.000421067, -0.00177953, -0.00414005, 0.00386966, 0.000421067, -0.00177953, 1.64684, 1.58541, 0.00596283, 0.0119591, 1.64684, 1.58541, 0.00596283, 0.0119591)

reports.append(Report(584941568, ("DT", 0, 3, 7), "MBwhCst3sec07"))
reports[-1].posNum = 37240
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000943681, 0.0106755, 0), \
                           ValErr(-0.00108183, 0.00842454, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.10398e-05, 9.44779e-05, 0), \
                           -143477, 37240, 37240, -nan)
reports[-1].sigmax = ValErr(1.69783, 0.0062212, 0)
reports[-1].sigmay = ValErr(1.62507, 0.00595459, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00470991, -0.00361765, -0.000537328, -0.00368193, -0.000402217, -0.00113498, -0.000534687, -0.00364223, -0.000402217, -0.00113498, -0.000534687, -0.00364223, -0.00549034, 0.00282891, -0.000519499, -0.00377335, -0.00549034, 0.00282891, -0.000519499, -0.00377335, 1.69783, 1.62507, 0.00607877, 0.012387, 1.69783, 1.62507, 0.00607877, 0.012387)

reports.append(Report(585990144, ("DT", 0, 3, 11), "MBwhCst3sec11"))
reports[-1].posNum = 59366
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.00277827, 0.00677261, 0), \
                           ValErr(0.00159541, 0.00654067, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.85791e-05, 6.26581e-05, 0), \
                           -225594, 59366, 59366, -nan)
reports[-1].sigmax = ValErr(1.64797, 0.00478261, 0)
reports[-1].sigmay = ValErr(1.58825, 0.0046093, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.016533, -0.00302427, -0.000495729, 0.000365132, 0.00288183, 0.00175486, -0.000514564, 0.000393236, 0.00288183, 0.00175486, -0.000514564, 0.000393236, 0.00481106, -0.000315373, -0.000536761, 0.000414285, 0.00481106, -0.000315373, -0.000536761, 0.000414285, 1.64797, 1.58825, 0.00594468, 0.0119308, 1.64797, 1.58825, 0.00594468, 0.0119308)

reports.append(Report(584155136, ("DT", 0, 3, 4), "MBwhCst3sec04"))
reports[-1].posNum = 79340
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(3.70228e-06, 0.00596874, 0), \
                           ValErr(-0.00234053, 0.00566738, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(8.48666e-05, 5.4571e-05, 0), \
                           -303455, 79340, 79340, -nan)
reports[-1].sigmax = ValErr(1.68068, 0.00421916, 0)
reports[-1].sigmay = ValErr(1.59626, 0.00400722, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00252601, -0.00647482, -6.75785e-05, 0.000682612, -0.000236973, -0.00225085, -3.89979e-05, 0.000668185, -0.000236973, -0.00225085, -3.89979e-05, 0.000668185, -0.00963251, 0.000214869, -1.12858e-05, 0.000645848, -0.00963251, 0.000214869, -1.12858e-05, 0.000645848, 1.68068, 1.59628, 0.0060875, 0.0115486, 1.68068, 1.59628, 0.0060875, 0.0115486)

reports.append(Report(585203712, ("DT", 0, 3, 8), "MBwhCst3sec08"))
reports[-1].posNum = 84990
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000184464, 0.00573659, 0), \
                           ValErr(0.000252286, 0.00550725, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.05258e-06, 5.24805e-05, 0), \
                           -325002, 84990, 84990, -nan)
reports[-1].sigmax = ValErr(1.67161, 0.0040545, 0)
reports[-1].sigmay = ValErr(1.60375, 0.00388988, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00611174, -0.00478298, -0.000509012, 7.85594e-05, -0.000167395, 0.00025982, -0.000521598, 8.00935e-05, -0.000167395, 0.00025982, -0.000521598, 8.00935e-05, -0.00370626, 0.00368422, -0.000497896, 5.74706e-05, -0.00370626, 0.00368422, -0.000497896, 5.74706e-05, 1.67161, 1.60375, 0.00602981, 0.0119372, 1.67161, 1.60375, 0.00602981, 0.0119372)

reports.append(Report(586252288, ("DT", 0, 3, 12), "MBwhCst3sec12"))
reports[-1].posNum = 88374
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(3.80459e-05, 0.00557029, 0), \
                           ValErr(-0.00169725, 0.0053364, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.52806e-05, 5.14358e-05, 0), \
                           -336077, 88374, 88374, -nan)
reports[-1].sigmax = ValErr(1.65475, 0.00393448, 0)
reports[-1].sigmay = ValErr(1.58624, 0.00377036, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00651036, -0.00206073, -0.000979274, -0.00135715, 7.08609e-05, -0.00171826, -0.000955138, -0.00141591, 7.08609e-05, -0.00171826, -0.000955138, -0.00141591, -0.00249017, -0.00418377, -0.000910375, -0.00143634, -0.00249017, -0.00418377, -0.000910375, -0.00143634, 1.65475, 1.58624, 0.00596224, 0.0117595, 1.65475, 1.58624, 0.00596224, 0.0117595)

reports.append(Report(575012864, ("DT", 1, 1, 1), "MBwhDst1sec01"))
reports[-1].posNum = 63438
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000607293, 0.00405046, 0), \
                           ValErr(0.00128456, 0.00455799, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.00704e-06, 5.47079e-05, 0), \
                           -182056, 63438, 63438, -nan)
reports[-1].sigmax = ValErr(0.973627, 0.00273344, 0)
reports[-1].sigmay = ValErr(1.06043, 0.00297716, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00217099, -0.00122491, -0.000607903, 2.52366e-05, -0.000540826, 0.00118803, -0.000621449, -8.67642e-05, -0.000540826, 0.00118803, -0.000621449, -8.67642e-05, -0.00332425, 0.0009519, -0.000561269, 2.46782e-05, -0.00332425, 0.0009519, -0.000561269, 2.46782e-05, 0.973628, 1.06043, 0.00477799, 0.014256, 0.973628, 1.06043, 0.00477799, 0.014256)

reports.append(Report(575275008, ("DT", 1, 1, 2), "MBwhDst1sec02"))
reports[-1].posNum = 90408
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(9.00964e-05, 0.00330662, 0), \
                           ValErr(-0.000157601, 0.00351157, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.28334e-05, 4.11775e-05, 0), \
                           -257931, 90408, 90408, -nan)
reports[-1].sigmax = ValErr(0.962842, 0.00226431, 0)
reports[-1].sigmay = ValErr(1.05438, 0.00247959, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00130519, -0.000610849, -0.000490607, -0.0001345, 0.000353185, -9.99289e-05, -0.000489258, -0.00026404, 0.000353185, -9.99289e-05, -0.000489258, -0.00026404, 0.00221517, -0.00129063, -0.000428648, -0.000277105, 0.00221517, -0.00129063, -0.000428648, -0.000277105, 0.962843, 1.05438, 0.00481482, 0.0151099, 0.962843, 1.05438, 0.00481482, 0.0151099)

reports.append(Report(575537152, ("DT", 1, 1, 3), "MBwhDst1sec03"))
reports[-1].posNum = 130190
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000173977, 0.00267958, 0), \
                           ValErr(-0.000329757, 0.00294455, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.37707e-06, 3.42614e-05, 0), \
                           -371450, 130190, 130190, -nan)
reports[-1].sigmax = ValErr(0.956516, 0.00187452, 0)
reports[-1].sigmay = ValErr(1.06154, 0.00208034, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0014963, -0.00151472, -0.00109767, 0.00267062, 0.000201672, -0.000321318, -0.0011052, 0.00251386, 0.000201672, -0.000321318, -0.0011052, 0.00251386, -0.00204277, -0.00408086, -0.00105182, 0.00249761, -0.00204277, -0.00408086, -0.00105182, 0.00249761, 0.956516, 1.06154, 0.0048155, 0.0148418, 0.956516, 1.06154, 0.0048155, 0.0148418)

reports.append(Report(575799296, ("DT", 1, 1, 4), "MBwhDst1sec04"))
reports[-1].posNum = 53920
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.00192788, 0.00470716, 0), \
                           ValErr(-7.22618e-05, 0.00523877, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.98382e-05, 7.94397e-05, 0), \
                           -161959, 53920, 53920, -nan)
reports[-1].sigmax = ValErr(1.00369, 0.00305643, 0)
reports[-1].sigmay = ValErr(1.176, 0.00358115, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00345213, -0.0050455, 0.00118445, 0.00463531, -0.00098793, 0.00060639, 0.00119424, 0.00421968, -0.00098793, 0.00060639, 0.00119424, 0.00421968, -0.00221615, 0.000448912, 0.0012755, 0.00421185, -0.00221615, 0.000448912, 0.0012755, 0.00421185, 1.00368, 1.17601, 0.00508513, 0.0152425, 1.00368, 1.17601, 0.00508513, 0.0152425)

reports.append(Report(576061440, ("DT", 1, 1, 5), "MBwhDst1sec05"))
reports[-1].posNum = 119736
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.00023512, 0.00282017, 0), \
                           ValErr(-0.000628079, 0.00309008, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.25804e-05, 3.64407e-05, 0), \
                           -343062, 119736, 119736, -nan)
reports[-1].sigmax = ValErr(0.964122, 0.00197019, 0)
reports[-1].sigmay = ValErr(1.0659, 0.00217817, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00565946, 0.00223153, -0.000634288, 7.45726e-05, 8.56775e-05, -0.000712515, -0.00062177, -0.000118017, 8.56775e-05, -0.000712515, -0.00062177, -0.000118017, 0.00115482, -0.00317431, -0.000581122, -9.01066e-05, 0.00115482, -0.00317431, -0.000581122, -9.01066e-05, 0.964124, 1.0659, 0.00480551, 0.0149876, 0.964124, 1.0659, 0.00480551, 0.0149876)

reports.append(Report(576323584, ("DT", 1, 1, 6), "MBwhDst1sec06"))
reports[-1].posNum = 130566
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000558295, 0.00270307, 0), \
                           ValErr(0.000548927, 0.00304222, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.25556e-05, 3.45736e-05, 0), \
                           -373844, 130566, 130566, -nan)
reports[-1].sigmax = ValErr(0.963088, 0.00187343, 0)
reports[-1].sigmay = ValErr(1.06502, 0.00208558, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00165758, 0.00366555, -0.00144352, 0.00119016, 0.000268323, 0.000421575, -0.001484, 0.00100635, 0.000268323, 0.000421575, -0.001484, 0.00100635, -0.00302314, -0.00216346, -0.00138132, 0.00105536, -0.00302314, -0.00216346, -0.00138132, 0.00105536, 0.963088, 1.06502, 0.00492476, 0.0145838, 0.963088, 1.06502, 0.00492476, 0.0145838)

reports.append(Report(576585728, ("DT", 1, 1, 7), "MBwhDst1sec07"))
reports[-1].posNum = 121966
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.00019523, 0.00282644, 0), \
                           ValErr(4.69535e-06, 0.00306532, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.44936e-05, 3.6684e-05, 0), \
                           -350161, 121966, 121966, -nan)
reports[-1].sigmax = ValErr(0.966305, 0.00195691, 0)
reports[-1].sigmay = ValErr(1.06969, 0.0021663, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00327041, 0.00313134, 0.00114975, -0.000403751, 0.000422651, 5.22913e-05, 0.00114482, -0.000524246, 0.000422651, 5.22913e-05, 0.00114482, -0.000524246, -0.00115305, -0.00160694, 0.00119065, -0.000514697, -0.00115305, -0.00160694, 0.00119065, -0.000514697, 0.966323, 1.06967, 0.00482877, 0.014417, 0.966323, 1.06967, 0.00482877, 0.014417)

reports.append(Report(576847872, ("DT", 1, 1, 8), "MBwhDst1sec08"))
reports[-1].posNum = 123748
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000301834, 0.00238515, 0), \
                           ValErr(-0.000249615, 0.00289654, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.26386e-05, 3.28197e-05, 0), \
                           -355465, 123748, 123748, -nan)
reports[-1].sigmax = ValErr(0.970291, 0.00194322, 0)
reports[-1].sigmay = ValErr(1.06692, 0.00213852, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00237938, 0.00166087, -0.00160394, -0.00191313, -0.000190157, -0.000187263, -0.0016107, -0.00208204, -0.000190157, -0.000187263, -0.0016107, -0.00208204, -0.000106882, -0.000964662, -0.00154992, -0.00208289, -0.000106882, -0.000964662, -0.00154992, -0.00208289, 0.97029, 1.06692, 0.00487965, 0.0145928, 0.97029, 1.06692, 0.00487965, 0.0145928)

reports.append(Report(577110016, ("DT", 1, 1, 9), "MBwhDst1sec09"))
reports[-1].posNum = 122756
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000265066, 0.00277718, 0), \
                           ValErr(-0.000220164, 0.0030296, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.68443e-05, 3.47581e-05, 0), \
                           -350933, 122756, 122756, -nan)
reports[-1].sigmax = ValErr(0.962109, 0.00194173, 0)
reports[-1].sigmay = ValErr(1.06134, 0.00214201, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00203561, 0.00481555, -0.000395095, -0.00120207, -4.98543e-05, -0.000256778, -0.000397178, -0.0015116, -4.98543e-05, -0.000256778, -0.000397178, -0.0015116, -0.00102348, 0.000836332, -0.000415605, -0.00149932, -0.00102348, 0.000836332, -0.000415605, -0.00149932, 0.962108, 1.06134, 0.0048247, 0.014889, 0.962108, 1.06134, 0.0048247, 0.014889)

reports.append(Report(577372160, ("DT", 1, 1, 10), "MBwhDst1sec10"))
reports[-1].posNum = 138056
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-4.8823e-05, 0.00261086, 0), \
                           ValErr(-0.000391625, 0.00285168, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.68542e-06, 3.28461e-05, 0), \
                           -393858, 138056, 138056, -nan)
reports[-1].sigmax = ValErr(0.959207, 0.00182549, 0)
reports[-1].sigmay = ValErr(1.0583, 0.00201407, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00185325, 0.00174602, -0.0012052, 0.000216062, -9.51036e-05, -0.000406497, -0.00120085, -0.00015706, -9.51036e-05, -0.000406497, -0.00120085, -0.00015706, -0.00129619, -0.00122258, -0.00117658, -0.000190972, -0.00129619, -0.00122258, -0.00117658, -0.000190972, 0.959207, 1.05829, 0.00479669, 0.0146894, 0.959207, 1.05829, 0.00479669, 0.0146894)

reports.append(Report(577634304, ("DT", 1, 1, 11), "MBwhDst1sec11"))
reports[-1].posNum = 135444
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000652858, 0.00263931, 0), \
                           ValErr(-0.000499544, 0.00287517, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.71099e-05, 3.31828e-05, 0), \
                           -386337, 135444, 135444, -nan)
reports[-1].sigmax = ValErr(0.95953, 0.00184364, 0)
reports[-1].sigmay = ValErr(1.0574, 0.00203169, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00173187, -0.00223981, -6.67747e-05, 0.00202797, -0.000862265, -0.00055508, -7.70038e-05, 0.00175892, -0.000862265, -0.00055508, -7.70038e-05, 0.00175892, -0.00384993, -0.00270025, -2.80649e-05, 0.0017758, -0.00384993, -0.00270025, -2.80649e-05, 0.0017758, 0.959523, 1.05741, 0.00478883, 0.0151234, 0.959523, 1.05741, 0.00478883, 0.0151234)

reports.append(Report(577896448, ("DT", 1, 1, 12), "MBwhDst1sec12"))
reports[-1].posNum = 141310
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-1.49592e-05, 0.00257467, 0), \
                           ValErr(-0.00139014, 0.00280739, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.73122e-06, 3.24587e-05, 0), \
                           -402397, 141310, 141310, -nan)
reports[-1].sigmax = ValErr(0.957824, 0.00180171, 0)
reports[-1].sigmay = ValErr(1.05425, 0.0019831, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.002507, -0.00322947, -0.000904261, -0.000309864, -0.000121736, -0.00142516, -0.000901278, -0.000611236, -0.000121736, -0.00142516, -0.000901278, -0.000611236, -0.00239258, -0.0058514, -0.000842412, -0.000615585, -0.00239258, -0.0058514, -0.000842412, -0.000615585, 0.957823, 1.05425, 0.00475502, 0.0148284, 0.957823, 1.05425, 0.00475502, 0.0148284)

reports.append(Report(579207168, ("DT", 1, 2, 1), "MBwhDst2sec01"))
reports[-1].posNum = 119014
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.00034141, 0.00372468, 0), \
                           ValErr(0.000876182, 0.00391177, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.21681e-05, 4.16081e-05, 0), \
                           -402591, 119014, 119014, -nan)
reports[-1].sigmax = ValErr(1.27779, 0.0026194, 0)
reports[-1].sigmay = ValErr(1.34947, 0.00276628, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000429612, 0.00059324, 0.00154866, 0.00283424, 0.000550534, 0.000890446, 0.0015604, 0.00260861, 0.000550534, 0.000890446, 0.0015604, 0.00260861, -0.000819687, 0.00160107, 0.00159324, 0.00263941, -0.000819687, 0.00160107, 0.00159324, 0.00263941, 1.27777, 1.34949, 0.00508272, 0.0145564, 1.27777, 1.34949, 0.00508272, 0.0145564)

reports.append(Report(579469312, ("DT", 1, 2, 2), "MBwhDst2sec02"))
reports[-1].posNum = 103254
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(9.75773e-05, 0.00400879, 0), \
                           ValErr(2.62137e-05, 0.00419127, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.92139e-06, 4.42642e-05, 0), \
                           -348531, 103254, 103254, -nan)
reports[-1].sigmax = ValErr(1.27178, 0.00279863, 0)
reports[-1].sigmay = ValErr(1.34606, 0.00296209, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00332548, 0.00352612, 0.000573772, 0.00458981, 0.000168067, 4.16948e-05, 0.000582588, 0.00455268, 0.000168067, 4.16948e-05, 0.000582588, 0.00455268, -0.00297447, -0.000506038, 0.000603146, 0.00459236, -0.00297447, -0.000506038, 0.000603146, 0.00459236, 1.27178, 1.34606, 0.00508576, 0.0147303, 1.27178, 1.34606, 0.00508576, 0.0147303)

reports.append(Report(579731456, ("DT", 1, 2, 3), "MBwhDst2sec03"))
reports[-1].posNum = 80342
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000394341, 0.00456148, 0), \
                           ValErr(0.000160839, 0.00483415, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.66722e-05, 4.67183e-05, 0), \
                           -273606, 80342, 80342, -nan)
reports[-1].sigmax = ValErr(1.28777, 0.00321277, 0)
reports[-1].sigmay = ValErr(1.36989, 0.0034176, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000473028, -0.00341343, -0.00037165, 0.00335523, 0.000801583, 0.000267764, -0.000378712, 0.00324535, 0.000801583, 0.000267764, -0.000378712, 0.00324535, 0.000793868, 0.00032416, -0.000400254, 0.00329766, 0.000793868, 0.00032416, -0.000400254, 0.00329766, 1.28774, 1.36993, 0.00524655, 0.0145107, 1.28774, 1.36993, 0.00524655, 0.0145107)

reports.append(Report(579993600, ("DT", 1, 2, 4), "MBwhDst2sec04"))
reports[-1].posNum = 92028
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000571894, 0.00426142, 0), \
                           ValErr(-0.00164013, 0.00459297, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.92498e-05, 5.19681e-05, 0), \
                           -314884, 92028, 92028, -nan)
reports[-1].sigmax = ValErr(1.28912, 0.00300498, 0)
reports[-1].sigmay = ValErr(1.39066, 0.00324162, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00104966, 0.00028498, 0.000169734, 0.00355126, -0.000391844, -0.00180024, 0.000176475, 0.0032639, -0.000391844, -0.00180024, 0.000176475, 0.0032639, -0.00179815, -0.00571585, 0.000173887, 0.00331104, -0.00179815, -0.00571585, 0.000173887, 0.00331104, 1.28911, 1.39068, 0.00512331, 0.0151825, 1.28911, 1.39068, 0.00512331, 0.0151825)

reports.append(Report(580255744, ("DT", 1, 2, 5), "MBwhDst2sec05"))
reports[-1].posNum = 92406
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.00038906, 0.00417364, 0), \
                           ValErr(0.000736124, 0.0047114, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.62403e-05, 5.29129e-05, 0), \
                           -312486, 92406, 92406, -nan)
reports[-1].sigmax = ValErr(1.26827, 0.00295026, 0)
reports[-1].sigmay = ValErr(1.35817, 0.00315934, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000209392, 0.00413667, 0.000601049, 0.00491943, -0.000460189, 0.00147564, 0.000601711, 0.00481912, -0.000460189, 0.00147564, 0.000601711, 0.00481912, 0.00190285, 0.000234921, 0.000581027, 0.00478622, 0.00190285, 0.000234921, 0.000581027, 0.00478622, 1.26828, 1.35816, 0.00511682, 0.0145852, 1.26828, 1.35816, 0.00511682, 0.0145852)

reports.append(Report(580517888, ("DT", 1, 2, 6), "MBwhDst2sec06"))
reports[-1].posNum = 133974
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.00121829, 0.0035271, 0), \
                           ValErr(0.000589681, 0.00373127, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.53318e-05, 3.90002e-05, 0), \
                           -455859, 133974, 133974, -nan)
reports[-1].sigmax = ValErr(1.28793, 0.00248812, 0)
reports[-1].sigmay = ValErr(1.36571, 0.00263838, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00086688, 0.00178777, 0.000572728, 0.00348218, -0.00162307, 0.00062408, 0.000569947, 0.00345109, -0.00162307, 0.00062408, 0.000569947, 0.00345109, -0.0046568, 0.00286768, 0.000594123, 0.00350898, -0.0046568, 0.00286768, 0.000594123, 0.00350898, 1.28795, 1.3657, 0.00512925, 0.0148355, 1.28795, 1.3657, 0.00512925, 0.0148355)

reports.append(Report(580780032, ("DT", 1, 2, 7), "MBwhDst2sec07"))
reports[-1].posNum = 121914
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.00123062, 0.00372462, 0), \
                           ValErr(0.000813546, 0.0038935, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.47217e-05, 4.20716e-05, 0), \
                           -413931, 121914, 121914, -nan)
reports[-1].sigmax = ValErr(1.28585, 0.00260409, 0)
reports[-1].sigmay = ValErr(1.35795, 0.00275011, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00243425, -0.00361783, 0.00170808, 0.0031091, -0.00169059, 0.000964548, 0.00170764, 0.00296214, -0.00169059, 0.000964548, 0.00170764, 0.00296214, -0.00336588, -0.00473964, 0.00172706, 0.00300276, -0.00336588, -0.00473964, 0.00172706, 0.00300276, 1.28586, 1.35794, 0.00512309, 0.0145035, 1.28586, 1.35794, 0.00512309, 0.0145035)

reports.append(Report(581042176, ("DT", 1, 2, 8), "MBwhDst2sec08"))
reports[-1].posNum = 119366
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.00126196, 0.00371984, 0), \
                           ValErr(0.000814678, 0.00395738, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.83277e-05, 4.2559e-05, 0), \
                           -406016, 119366, 119366, -nan)
reports[-1].sigmax = ValErr(1.2854, 0.00262501, 0)
reports[-1].sigmay = ValErr(1.36684, 0.00279612, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000101659, 0.00400863, 0.000667488, 0.0021141, 0.00127924, 0.000872705, 0.000653571, 0.00199703, 0.00127924, 0.000872705, 0.000653571, 0.00199703, -0.00336441, -0.00214257, 0.000705215, 0.00202577, -0.00336441, -0.00214257, 0.000705215, 0.00202577, 1.28538, 1.36685, 0.00513425, 0.0151921, 1.28538, 1.36685, 0.00513425, 0.0151921)

reports.append(Report(581304320, ("DT", 1, 2, 9), "MBwhDst2sec09"))
reports[-1].posNum = 119828
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000844018, 0.00369955, 0), \
                           ValErr(0.000866502, 0.00392229, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.36795e-05, 4.15898e-05, 0), \
                           -405313, 119828, 119828, -nan)
reports[-1].sigmax = ValErr(1.27091, 0.0025961, 0)
reports[-1].sigmay = ValErr(1.35641, 0.00277075, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00298786, 0.00525019, 0.000642268, 0.00298852, -0.000587352, 0.00096565, 0.000674646, 0.00290008, -0.000587352, 0.00096565, 0.000674646, 0.00290008, -8.40414e-06, 0.00271845, 0.000699167, 0.00291713, -8.40414e-06, 0.00271845, 0.000699167, 0.00291713, 1.27091, 1.35641, 0.00514173, 0.0146747, 1.27091, 1.35641, 0.00514173, 0.0146747)

reports.append(Report(581566464, ("DT", 1, 2, 10), "MBwhDst2sec10"))
reports[-1].posNum = 127682
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.00123178, 0.00358489, 0), \
                           ValErr(0.00037928, 0.00379445, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.29215e-05, 3.98722e-05, 0), \
                           -432514, 127682, 127682, -nan)
reports[-1].sigmax = ValErr(1.27807, 0.0025292, 0)
reports[-1].sigmay = ValErr(1.35555, 0.00268252, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00428682, -0.00203392, -0.000387173, 0.00278133, 0.00131309, 0.000353621, -0.000376853, 0.00273608, 0.00131309, 0.000353621, -0.000376853, 0.00273608, 0.00331327, -0.00233754, -0.000366134, 0.0027524, 0.00331327, -0.00233754, -0.000366134, 0.0027524, 1.27806, 1.35555, 0.00511777, 0.0145597, 1.27806, 1.35555, 0.00511777, 0.0145597)

reports.append(Report(581828608, ("DT", 1, 2, 11), "MBwhDst2sec11"))
reports[-1].posNum = 126408
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000685702, 0.00359273, 0), \
                           ValErr(0.000371539, 0.00381156, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.38188e-05, 4.05086e-05, 0), \
                           -427781, 126408, 126408, -nan)
reports[-1].sigmax = ValErr(1.27449, 0.00253477, 0)
reports[-1].sigmay = ValErr(1.35486, 0.00269461, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00149062, -0.00271125, -0.000565733, 0.00258842, -0.000602504, 0.000398684, -0.000561028, 0.00228112, -0.000602504, 0.000398684, -0.000561028, 0.00228112, 0.00197407, 0.000876017, -0.000566618, 0.00232463, 0.00197407, 0.000876017, -0.000566618, 0.00232463, 1.27449, 1.35487, 0.0051223, 0.0149177, 1.27449, 1.35487, 0.0051223, 0.0149177)

reports.append(Report(582090752, ("DT", 1, 2, 12), "MBwhDst2sec12"))
reports[-1].posNum = 130278
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000921812, 0.00348318, 0), \
                           ValErr(-0.000937792, 0.00372387, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.59762e-06, 2.10071e-05, 0), \
                           -441482, 130278, 130278, -nan)
reports[-1].sigmax = ValErr(1.27686, 0.00249, 0)
reports[-1].sigmay = ValErr(1.35865, 0.00258763, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000790083, -0.00322169, 0.00055979, 0.00425403, -0.000968018, -0.000948047, 0.000582851, 0.00405174, -0.000968018, -0.000948047, 0.000582851, 0.00405174, 0.00167298, -0.00275792, 0.00059723, 0.00406494, 0.00167298, -0.00275792, 0.00059723, 0.00406494, 1.27686, 1.35864, 0.00512372, 0.0150534, 1.27686, 1.35864, 0.00512372, 0.0150534)

reports.append(Report(583401472, ("DT", 1, 3, 1), "MBwhDst3sec01"))
reports[-1].posNum = 94628
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.0010332, 0.00559756, 0), \
                           ValErr(-0.00160853, 0.00581882, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.17305e-05, 5.49298e-05, 0), \
                           -375004, 94628, 94628, -nan)
reports[-1].sigmax = ValErr(1.72164, 0.00395752, 0)
reports[-1].sigmay = ValErr(1.78921, 0.00411288, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00502402, 0.00173041, 0.000148432, -0.00117619, 0.00105427, -0.00164464, 0.000126847, -0.00099877, 0.00105427, -0.00164464, 0.000126847, -0.00099877, -0.00189102, -0.00609322, 0.000149786, -0.00102142, -0.00189102, -0.00609322, 0.000149786, -0.00102142, 1.72163, 1.78922, 0.00598673, 0.0136359, 1.72163, 1.78922, 0.00598673, 0.0136359)

reports.append(Report(583663616, ("DT", 1, 3, 2), "MBwhDst3sec02"))
reports[-1].posNum = 90688
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000109458, 0.00562539, 0), \
                           ValErr(-7.56889e-05, 0.00582817, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.56858e-05, 5.53797e-05, 0), \
                           -356105, 90688, 90688, -nan)
reports[-1].sigmax = ValErr(1.69293, 0.00397519, 0)
reports[-1].sigmay = ValErr(1.75483, 0.00412057, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000442154, 0.00699173, 0.000170686, -0.00190047, -5.0051e-05, -4.43318e-05, 0.000130244, -0.00177221, -5.0051e-05, -4.43318e-05, 0.000130244, -0.00177221, -0.000721972, -0.0107542, 0.000157575, -0.00177466, -0.000721972, -0.0107542, 0.000157575, -0.00177466, 1.69294, 1.75482, 0.0059384, 0.0132035, 1.69294, 1.75482, 0.0059384, 0.0132035)

reports.append(Report(583925760, ("DT", 1, 3, 3), "MBwhDst3sec03"))
reports[-1].posNum = 102628
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000233875, 0.0053293, 0), \
                           ValErr(-0.00055041, 0.00548233, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.61609e-05, 5.26905e-05, 0), \
                           -403900, 102628, 102628, -nan)
reports[-1].sigmax = ValErr(1.70657, 0.00376686, 0)
reports[-1].sigmay = ValErr(1.75629, 0.00387658, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000755426, 0.00490925, -0.00051769, 0.000147999, 0.000156914, -0.000553165, -0.000528388, 0.000293148, 0.000156914, -0.000553165, -0.000528388, 0.000293148, 0.00127122, 0.000832928, -0.000530874, 0.000328624, 0.00127122, 0.000832928, -0.000530874, 0.000328624, 1.70657, 1.7563, 0.00600653, 0.0134789, 1.70657, 1.7563, 0.00600653, 0.0134789)

reports.append(Report(584187904, ("DT", 1, 3, 4), "MBwhDst3sec04"))
reports[-1].posNum = 73948
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000209639, 0.00634941, 0), \
                           ValErr(0.0010842, 0.00654768, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.62106e-05, 6.60487e-05, 0), \
                           -292875, 73948, 73948, -nan)
reports[-1].sigmax = ValErr(1.72634, 0.00448901, 0)
reports[-1].sigmay = ValErr(1.78011, 0.00462884, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00467037, 0.00426146, -0.000154418, 0.00126044, -0.000113203, 0.000962277, -0.000165646, 0.00127672, -0.000113203, 0.000962277, -0.000165646, 0.00127672, 0.000446395, -0.00555267, -0.000139797, 0.00132219, 0.000446395, -0.00555267, -0.000139797, 0.00132219, 1.72636, 1.7801, 0.00604227, 0.0138687, 1.72636, 1.7801, 0.00604227, 0.0138687)

reports.append(Report(584450048, ("DT", 1, 3, 5), "MBwhDst3sec05"))
reports[-1].posNum = 102136
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000970087, 0.00538443, 0), \
                           ValErr(-0.00191498, 0.00551282, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.02797e-05, 5.24307e-05, 0), \
                           -403065, 102136, 102136, -nan)
reports[-1].sigmax = ValErr(1.72, 0.00380563, 0)
reports[-1].sigmay = ValErr(1.76148, 0.00389739, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00345575, 0.00068294, 0.000392341, -0.0010053, -0.00109525, -0.00199914, 0.000366523, -0.00091146, -0.00109525, -0.00199914, 0.000366523, -0.00091146, -0.0029936, -0.00674052, 0.000365582, -0.000836275, -0.0029936, -0.00674052, 0.000365582, -0.000836275, 1.72001, 1.76148, 0.00602713, 0.0136483, 1.72001, 1.76148, 0.00602713, 0.0136483)

reports.append(Report(584712192, ("DT", 1, 3, 6), "MBwhDst3sec06"))
reports[-1].posNum = 111144
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000493289, 0.00515539, 0), \
                           ValErr(0.00178082, 0.00531912, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.21873e-05, 5.04553e-05, 0), \
                           -439207, 111144, 111144, -nan)
reports[-1].sigmax = ValErr(1.71838, 0.00364533, 0)
reports[-1].sigmay = ValErr(1.77258, 0.00376765, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00454897, -0.00101374, 4.62676e-05, 0.00215612, -0.00059842, 0.00175222, 2.02155e-05, 0.00223523, -0.00059842, 0.00175222, 2.02155e-05, 0.00223523, -0.00329905, -0.00360809, 1.44624e-05, 0.00223786, -0.00329905, -0.00360809, 1.44624e-05, 0.00223786, 1.71838, 1.77258, 0.00603324, 0.0133864, 1.71838, 1.77258, 0.00603324, 0.0133864)

reports.append(Report(584974336, ("DT", 1, 3, 7), "MBwhDst3sec07"))
reports[-1].posNum = 96306
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.00024542, 0.00562826, 0), \
                           ValErr(-0.000130869, 0.00565631, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.99512e-05, 5.57894e-05, 0), \
                           -380236, 96306, 96306, -nan)
reports[-1].sigmax = ValErr(1.73007, 0.00394207, 0)
reports[-1].sigmay = ValErr(1.75447, 0.00399766, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00301495, 0.00340655, 0.000517448, 0.00273993, -3.10761e-05, -0.000194392, 0.000509675, 0.00282462, -3.10761e-05, -0.000194392, 0.000509675, 0.00282462, -0.00180585, -0.000252298, 0.000517204, 0.00285478, -0.00180585, -0.000252298, 0.000517204, 0.00285478, 1.73007, 1.75447, 0.0060629, 0.0136138, 1.73007, 1.75447, 0.0060629, 0.0136138)

reports.append(Report(585236480, ("DT", 1, 3, 8), "MBwhDst3sec08"))
reports[-1].posNum = 101864
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000163879, 0.00537454, 0), \
                           ValErr(-8.08078e-05, 0.00552506, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.09794e-05, 5.22064e-05, 0), \
                           -401665, 101864, 101864, -nan)
reports[-1].sigmax = ValErr(1.71533, 0.0038004, 0)
reports[-1].sigmay = ValErr(1.76062, 0.00390074, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.004906, -0.00369962, -0.000132005, 0.00280458, -0.000149764, 0.000103786, -0.000162796, 0.00291398, -0.000149764, 0.000103786, -0.000162796, 0.00291398, 0.0044805, -0.00413314, -0.000157015, 0.00293485, 0.0044805, -0.00413314, -0.000157015, 0.00293485, 1.71533, 1.76063, 0.00597985, 0.0133753, 1.71533, 1.76063, 0.00597985, 0.0133753)

reports.append(Report(585498624, ("DT", 1, 3, 9), "MBwhDst3sec09"))
reports[-1].posNum = 103354
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.00058078, 0.00532396, 0), \
                           ValErr(-0.000543106, 0.00547312, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.98489e-05, 5.29014e-05, 0), \
                           -407242, 103354, 103354, -nan)
reports[-1].sigmax = ValErr(1.71158, 0.00376461, 0)
reports[-1].sigmay = ValErr(1.75939, 0.00386977, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00421494, 0.00278641, -0.000559621, -0.00105098, 0.000572802, -0.000582934, -0.000565467, -0.00106832, 0.000572802, -0.000582934, -0.000565467, -0.00106832, 0.00541491, -0.0078344, -0.000589842, -0.00103675, 0.00541491, -0.0078344, -0.000589842, -0.00103675, 1.71158, 1.75939, 0.00603174, 0.0135089, 1.71158, 1.75939, 0.00603174, 0.0135089)

reports.append(Report(585760768, ("DT", 1, 3, 10), "MBwhDst3sec10"))
reports[-1].posNum = 102758
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000303592, 0.00530199, 0), \
                           ValErr(0.00130105, 0.00546083, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.42501e-05, 5.24492e-05, 0), \
                           -403541, 102758, 102758, -nan)
reports[-1].sigmax = ValErr(1.69946, 0.00374878, 0)
reports[-1].sigmay = ValErr(1.74878, 0.00385758, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.000290341, -0.00182389, 0.000279, 0.00367444, 0.000347977, 0.00145963, 0.000245762, 0.00377268, 0.000347977, 0.00145963, 0.000245762, 0.00377268, -0.00248066, -0.00472989, 0.00026929, 0.00379372, -0.00248066, -0.00472989, 0.00026929, 0.00379372, 1.69947, 1.74877, 0.00599168, 0.0137975, 1.69947, 1.74877, 0.00599168, 0.0137975)

reports.append(Report(586022912, ("DT", 1, 3, 11), "MBwhDst3sec11"))
reports[-1].posNum = 108992
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.00109299, 0.00515202, 0), \
                           ValErr(-0.000805031, 0.00530904, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.12628e-05, 5.07697e-05, 0), \
                           -428308, 108992, 108992, -nan)
reports[-1].sigmax = ValErr(1.70018, 0.00364155, 0)
reports[-1].sigmay = ValErr(1.75262, 0.00375385, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00843102, -0.00457519, -0.00132644, -0.00144428, 0.00103061, -0.000829329, -0.00133535, -0.00132867, 0.00103061, -0.000829329, -0.00133535, -0.00132867, 0.00173015, -0.00153172, -0.00131403, -0.00131848, 0.00173015, -0.00153172, -0.00131403, -0.00131848, 1.70018, 1.75261, 0.00597311, 0.0133618, 1.70018, 1.75261, 0.00597311, 0.0133618)

reports.append(Report(586285056, ("DT", 1, 3, 12), "MBwhDst3sec12"))
reports[-1].posNum = 110534
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000176414, 0.00515116, 0), \
                           ValErr(0.000372223, 0.00530238, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.55219e-05, 5.04701e-05, 0), \
                           -435703, 110534, 110534, -nan)
reports[-1].sigmax = ValErr(1.71206, 0.00364133, 0)
reports[-1].sigmay = ValErr(1.7616, 0.00374673, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00573987, 0.00167918, 0.000276688, -0.00465832, -0.000137014, 0.000434056, 0.000259277, -0.00465967, -0.000137014, 0.000434056, 0.000259277, -0.00465967, 0.00297413, -0.000805147, 0.000269595, -0.00470826, 0.00297413, -0.000805147, 0.000269595, -0.00470826, 1.71206, 1.7616, 0.00597305, 0.0139228, 1.71206, 1.7616, 0.00597305, 0.0139228)

reports.append(Report(575045632, ("DT", 2, 1, 1), "MBwhEst1sec01"))
reports[-1].posNum = 38432
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000611767, 0.00630209, 0), \
                           ValErr(-0.000665726, 0.00783077, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.57156e-06, 8.24225e-05, 0), \
                           -127984, 38432, 38432, -nan)
reports[-1].sigmax = ValErr(1.06573, 0.00384427, 0)
reports[-1].sigmay = ValErr(1.53512, 0.0055375, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000751537, 0.000312509, -0.000563763, -0.000915092, 0.00028029, -0.000670407, -0.000548689, -0.000356096, 0.00028029, -0.000670407, -0.000548689, -0.000356096, -0.00643466, -0.00835852, -0.000385942, -0.000423093, -0.00643466, -0.00835852, -0.000385942, -0.000423093, 1.06572, 1.53513, 0.00537424, 0.034093, 1.06572, 1.53513, 0.00537424, 0.034093)

reports.append(Report(575307776, ("DT", 2, 1, 2), "MBwhEst1sec02"))
reports[-1].posNum = 39762
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000244539, 0.00700435, 0), \
                           ValErr(0.000243314, 0.00765407, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.2319e-05, 9.03991e-05, 0), \
                           -132556, 39762, 39762, -nan)
reports[-1].sigmax = ValErr(1.07657, 0.00381775, 0)
reports[-1].sigmay = ValErr(1.52514, 0.00540852, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00129544, 0.00612101, -0.000737333, 0.00105898, -0.000857162, 0.00017042, -0.000723221, 0.00143925, -0.000857162, 0.00017042, -0.000723221, 0.00143925, -0.00275159, -0.00597739, -0.000670346, 0.00115479, -0.00275159, -0.00597739, -0.000670346, 0.00115479, 1.07656, 1.52515, 0.00526565, 0.0381408, 1.07656, 1.52515, 0.00526565, 0.0381408)

reports.append(Report(575569920, ("DT", 2, 1, 3), "MBwhEst1sec03"))
reports[-1].posNum = 31300
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.00218698, 0.0113842, 0), \
                           ValErr(-0.00221318, 0.0084062, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.58232e-05, 0.00013941, 0), \
                           -102643, 31300, 31300, -nan)
reports[-1].sigmax = ValErr(1.05822, 0.00422952, 0)
reports[-1].sigmay = ValErr(1.46942, 0.005873, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00243956, -0.00546716, -0.000575577, -0.00215021, 0.000294052, -0.0025393, -0.000591897, -0.00160696, 0.000294052, -0.0025393, -0.000591897, -0.00160696, -0.00665881, -0.00528075, -0.000481676, -0.00188773, -0.00665881, -0.00528075, -0.000481676, -0.00188773, 1.05822, 1.46942, 0.00520705, 0.0309455, 1.05822, 1.46942, 0.00520705, 0.0309455)

reports.append(Report(575832064, ("DT", 2, 1, 4), "MBwhEst1sec04"))
reports[-1].posNum = 47168
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000691807, 0.00524207, 0), \
                           ValErr(-0.00155294, 0.00716313, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(9.21731e-06, 7.1886e-05, 0), \
                           -157827, 47168, 47168, -nan)
reports[-1].sigmax = ValErr(1.07224, 0.00349107, 0)
reports[-1].sigmay = ValErr(1.55028, 0.0050476, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00107299, 0.000968051, -0.000750601, -0.00427345, -0.000458787, -0.00147253, -0.000786256, -0.00195679, -0.000458787, -0.00147253, -0.000786256, -0.00195679, -0.00577867, -0.00961662, -0.000734981, -0.00209374, -0.00577867, -0.00961662, -0.000734981, -0.00209374, 1.07224, 1.55027, 0.00521809, 0.0394856, 1.07224, 1.55027, 0.00521809, 0.0394856)

reports.append(Report(576094208, ("DT", 2, 1, 5), "MBwhEst1sec05"))
reports[-1].posNum = 34830
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.00340888, 0.0062227, 0), \
                           ValErr(-0.00230526, 0.00836051, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.72832e-05, 8.3623e-05, 0), \
                           -117006, 34830, 34830, -nan)
reports[-1].sigmax = ValErr(1.07965, 0.00409068, 0)
reports[-1].sigmay = ValErr(1.56022, 0.00591149, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00185274, -0.00431332, -0.000535142, 0.00447463, -0.00293537, -0.0022869, -0.000557523, 0.00468963, -0.00293537, -0.0022869, -0.000557523, 0.00468963, -0.0133121, -0.00717897, -0.000442887, 0.00465375, -0.0133121, -0.00717897, -0.000442887, 0.00465375, 1.07966, 1.56021, 0.00528317, 0.0402523, 1.07966, 1.56021, 0.00528317, 0.0402523)

reports.append(Report(576356352, ("DT", 2, 1, 6), "MBwhEst1sec06"))
reports[-1].posNum = 46628
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000122681, 0.00549671, 0), \
                           ValErr(-0.00351025, 0.00748724, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.03514e-05, 8.15052e-05, 0), \
                           -153577, 46628, 46628, -nan)
reports[-1].sigmax = ValErr(1.04392, 0.00341849, 0)
reports[-1].sigmay = ValErr(1.51106, 0.00494817, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00407482, -0.00495417, 0.000556048, -0.00566292, 0.000528437, -0.00284916, 0.000556558, -0.00428535, 0.000528437, -0.00284916, 0.000556558, -0.00428535, -0.00267873, -0.0085594, 0.000607699, -0.00451109, -0.00267873, -0.0085594, 0.000607699, -0.00451109, 1.04392, 1.51106, 0.00511426, 0.0380337, 1.04392, 1.51106, 0.00511426, 0.0380337)

reports.append(Report(576618496, ("DT", 2, 1, 7), "MBwhEst1sec07"))
reports[-1].posNum = 50340
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.0038836, 0.00515706, 0), \
                           ValErr(-0.000226808, 0.0071625, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.83287e-05, 6.86192e-05, 0), \
                           -171711, 50340, 50340, -nan)
reports[-1].sigmax = ValErr(1.10451, 0.00348101, 0)
reports[-1].sigmay = ValErr(1.60599, 0.00506149, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00213984, -0.00335368, -0.000951077, -0.000629176, -0.00541319, -0.000480203, -0.000956002, 0.000588801, -0.00541319, -0.000480203, -0.000956002, 0.000588801, -0.00941865, 0.000718728, -0.000894493, 0.000765571, -0.00941865, 0.000718728, -0.000894493, 0.000765571, 1.10454, 1.60597, 0.00549653, 0.0380683, 1.10454, 1.60597, 0.00549653, 0.0380683)

reports.append(Report(576880640, ("DT", 2, 1, 8), "MBwhEst1sec08"))
reports[-1].posNum = 49434
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000315279, 0.00526652, 0), \
                           ValErr(-0.00216896, 0.00698435, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.29149e-06, 7.00922e-05, 0), \
                           -165407, 49434, 49434, -nan)
reports[-1].sigmax = ValErr(1.07455, 0.00341747, 0)
reports[-1].sigmay = ValErr(1.54689, 0.00491967, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00530696, -0.00543329, -0.0013458, -0.00112212, -0.000126991, -0.00211468, -0.00137615, 1.81873e-05, -0.000126991, -0.00211468, -0.00137615, 1.81873e-05, -0.00462416, -0.00825993, -0.00123458, -2.70334e-05, -0.00462416, -0.00825993, -0.00123458, -2.70334e-05, 1.07455, 1.54689, 0.00530089, 0.037787, 1.07455, 1.54689, 0.00530089, 0.037787)

reports.append(Report(577142784, ("DT", 2, 1, 9), "MBwhEst1sec09"))
reports[-1].posNum = 40824
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.00241793, 0.00658546, 0), \
                           ValErr(-0.000842871, 0.00759575, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.68503e-05, 8.48218e-05, 0), \
                           -135782, 40824, 40824, -nan)
reports[-1].sigmax = ValErr(1.07226, 0.00375255, 0)
reports[-1].sigmay = ValErr(1.51953, 0.00531786, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00187181, 0.00479827, -6.82104e-05, -0.00151051, -0.000723956, -0.000380011, -8.05834e-05, -0.00121069, -0.000723956, -0.000380011, -8.05834e-05, -0.00121069, -0.00202452, -0.00369587, 3.86484e-06, -0.00122175, -0.00202452, -0.00369587, 3.86484e-06, -0.00122175, 1.07225, 1.51953, 0.00527703, 0.0371979, 1.07225, 1.51953, 0.00527703, 0.0371979)

reports.append(Report(577404928, ("DT", 2, 1, 10), "MBwhEst1sec10"))
reports[-1].posNum = 55290
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.00218158, 0.00490472, 0), \
                           ValErr(0.000541339, 0.00662784, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.88278e-05, 6.76149e-05, 0), \
                           -184659, 55290, 55290, -nan)
reports[-1].sigmax = ValErr(1.06772, 0.00321098, 0)
reports[-1].sigmay = ValErr(1.54716, 0.00465282, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0080436, 0.00702637, -0.000408941, -0.00350474, 0.000568739, -0.000152128, -0.000432495, -0.00246485, 0.000568739, -0.000152128, -0.000432495, -0.00246485, 0.00132025, -0.00756678, -0.000415474, -0.00277987, 0.00132025, -0.00756678, -0.000415474, -0.00277987, 1.0677, 1.5472, 0.00525898, 0.0363568, 1.0677, 1.5472, 0.00525898, 0.0363568)

reports.append(Report(577667072, ("DT", 2, 1, 11), "MBwhEst1sec11"))
reports[-1].posNum = 52816
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.00176736, 0.00518522, 0), \
                           ValErr(-0.00300829, 0.00667067, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.11926e-05, 7.0247e-05, 0), \
                           -175645, 52816, 52816, -nan)
reports[-1].sigmax = ValErr(1.06318, 0.00327138, 0)
reports[-1].sigmay = ValErr(1.53184, 0.00471342, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00415421, -0.000138059, -0.00223336, -0.000167281, 5.97599e-05, -0.00320054, -0.00225866, 0.00155665, 5.97599e-05, -0.00320054, -0.00225866, 0.00155665, 0.00201876, -0.00828599, -0.002192, 0.00160987, 0.00201876, -0.00828599, -0.002192, 0.00160987, 1.06321, 1.53181, 0.00531121, 0.0378771, 1.06321, 1.53181, 0.00531121, 0.0378771)

reports.append(Report(577929216, ("DT", 2, 1, 12), "MBwhEst1sec12"))
reports[-1].posNum = 61556
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000187386, 0.00503479, 0), \
                           ValErr(-0.000413397, 0.00618906, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.07268e-06, 7.01109e-05, 0), \
                           -204900, 61556, 61556, -nan)
reports[-1].sigmax = ValErr(1.06755, 0.00304256, 0)
reports[-1].sigmay = ValErr(1.53026, 0.00436129, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000913633, -0.000433196, 0.00013312, 0.000428684, -0.000447767, -0.000462459, 0.000145942, 0.00053543, -0.000447767, -0.000462459, 0.000145942, 0.00053543, -0.00562797, -0.00411324, 0.000210852, 0.000308962, -0.00562797, -0.00411324, 0.000210852, 0.000308962, 1.06755, 1.53026, 0.00522682, 0.0336011, 1.06755, 1.53026, 0.00522682, 0.0336011)

reports.append(Report(579239936, ("DT", 2, 2, 1), "MBwhEst2sec01"))
reports[-1].posNum = 64994
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000293758, 0.00594936, 0), \
                           ValErr(-0.000912533, 0.00728685, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.49627e-05, 7.63517e-05, 0), \
                           -246915, 64994, 64994, -nan)
reports[-1].sigmax = ValErr(1.40793, 0.00390527, 0)
reports[-1].sigmay = ValErr(1.85716, 0.00515138, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.000759527, 0.00273554, 0.00359931, 0.00473182, 0.00101713, -0.000853165, 0.00362024, 0.00487736, 0.00101713, -0.000853165, 0.00362024, 0.00487736, 0.00203876, -0.00450015, 0.00360314, 0.00489379, 0.00203876, -0.00450015, 0.00360314, 0.00489379, 1.40794, 1.85715, 0.00554147, 0.0239908, 1.40794, 1.85715, 0.00554147, 0.0239908)

reports.append(Report(579502080, ("DT", 2, 2, 2), "MBwhEst2sec02"))
reports[-1].posNum = 63894
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.00275347, 0.00579764, 0), \
                           ValErr(0.000119248, 0.00732883, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.27173e-05, 7.4302e-05, 0), \
                           -242174, 63894, 63894, -nan)
reports[-1].sigmax = ValErr(1.39913, 0.00391394, 0)
reports[-1].sigmay = ValErr(1.85248, 0.00518214, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00602723, 0.00659335, 0.000660221, 0.00435584, -0.00199617, 9.43818e-05, 0.000652558, 0.00440378, -0.00199617, 9.43818e-05, 0.000652558, 0.00440378, 0.00253992, -0.00516865, 0.000641258, 0.00440887, 0.00253992, -0.00516865, 0.000641258, 0.00440887, 1.39913, 1.85248, 0.00554838, 0.0236611, 1.39913, 1.85248, 0.00554838, 0.0236611)

reports.append(Report(579764224, ("DT", 2, 2, 3), "MBwhEst2sec03"))
reports[-1].posNum = 74240
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-8.78852e-05, 0.00535031, 0), \
                           ValErr(-0.00291372, 0.00676368, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.27757e-05, 6.89801e-05, 0), \
                           -280138, 74240, 74240, -nan)
reports[-1].sigmax = ValErr(1.386, 0.00359702, 0)
reports[-1].sigmay = ValErr(1.83879, 0.00477208, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.000383309, 0.00372728, 0.000784664, 0.00669152, -0.000395233, -0.00283036, 0.00079144, 0.00665024, -0.000395233, -0.00283036, 0.00079144, 0.00665024, -0.00666219, -0.00671483, 0.000839115, 0.00685913, -0.00666219, -0.00671483, 0.000839115, 0.00685913, 1.38601, 1.83878, 0.00550802, 0.0242908, 1.38601, 1.83878, 0.00550802, 0.0242908)

reports.append(Report(580026368, ("DT", 2, 2, 4), "MBwhEst2sec04"))
reports[-1].posNum = 73452
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000495206, 0.00548246, 0), \
                           ValErr(-0.000775975, 0.00684561, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.03032e-05, 6.95457e-05, 0), \
                           -279077, 73452, 73452, -nan)
reports[-1].sigmax = ValErr(1.40997, 0.00367871, 0)
reports[-1].sigmay = ValErr(1.85521, 0.00484037, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00733949, -0.000102588, 0.00126434, 0.00397208, 0.00149832, -0.000737496, 0.00125978, 0.00387796, 0.00149832, -0.000737496, 0.00125978, 0.00387796, -0.00225355, -0.00281135, 0.00131585, 0.00373799, -0.00225355, -0.00281135, 0.00131585, 0.00373799, 1.40998, 1.85521, 0.00558919, 0.0239792, 1.40998, 1.85521, 0.00558919, 0.0239792)

reports.append(Report(580288512, ("DT", 2, 2, 5), "MBwhEst2sec05"))
reports[-1].posNum = 62662
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.00236452, 0.00586846, 0), \
                           ValErr(-0.00117654, 0.00733992, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.02277e-06, 7.45141e-05, 0), \
                           -236711, 62662, 62662, -nan)
reports[-1].sigmax = ValErr(1.39331, 0.00393578, 0)
reports[-1].sigmay = ValErr(1.83679, 0.00518852, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00147499, -0.00904843, -0.000403028, -6.94332e-05, -0.00221408, -0.00119078, -0.000403864, 0.000382567, -0.00221408, -0.00119078, -0.000403864, 0.000382567, -0.00780151, 0.00368887, -0.000346033, 0.000532267, -0.00780151, 0.00368887, -0.000346033, 0.000532267, 1.39331, 1.83679, 0.00554439, 0.0284456, 1.39331, 1.83679, 0.00554439, 0.0284456)

reports.append(Report(580550656, ("DT", 2, 2, 6), "MBwhEst2sec06"))
reports[-1].posNum = 82214
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000655058, 0.00500335, 0), \
                           ValErr(-0.0014528, 0.00647366, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.80722e-05, 6.4462e-05, 0), \
                           -311232, 82214, 82214, -nan)
reports[-1].sigmax = ValErr(1.39158, 0.00343184, 0)
reports[-1].sigmay = ValErr(1.85395, 0.00457211, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00138714, 0.00647178, -3.19027e-05, 0.00230639, -0.000314679, -0.00154135, -2.09793e-05, 0.00215671, -0.000314679, -0.00154135, -2.09793e-05, 0.00215671, 0.000638082, -0.00265004, -2.915e-06, 0.00225954, 0.000638082, -0.00265004, -2.915e-06, 0.00225954, 1.39157, 1.85396, 0.00555101, 0.025279, 1.39157, 1.85396, 0.00555101, 0.025279)

reports.append(Report(580812800, ("DT", 2, 2, 7), "MBwhEst2sec07"))
reports[-1].posNum = 79518
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000108251, 0.00519921, 0), \
                           ValErr(-0.000707995, 0.00662522, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.72203e-05, 6.53101e-05, 0), \
                           -302620, 79518, 79518, -nan)
reports[-1].sigmax = ValErr(1.4089, 0.00353294, 0)
reports[-1].sigmay = ValErr(1.86824, 0.00468479, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.000523902, 0.00597545, 0.00273872, 0.00533301, -0.000712318, -0.000711356, 0.00272506, 0.00522725, -0.000712318, -0.000711356, 0.00272506, 0.00522725, 0.00274665, -0.00849863, 0.00270108, 0.00518079, 0.00274665, -0.00849863, 0.00270108, 0.00518079, 1.40889, 1.86825, 0.00559717, 0.0262025, 1.40889, 1.86825, 0.00559717, 0.0262025)

reports.append(Report(581074944, ("DT", 2, 2, 8), "MBwhEst2sec08"))
reports[-1].posNum = 80432
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-2.5374e-05, 0.00517323, 0), \
                           ValErr(-0.00141161, 0.00660938, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.09742e-05, 6.56705e-05, 0), \
                           -306370, 80432, 80432, -nan)
reports[-1].sigmax = ValErr(1.41077, 0.00351757, 0)
reports[-1].sigmay = ValErr(1.87206, 0.00466771, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.000690023, -0.00103772, 0.000242979, 0.0016431, -0.000695151, -0.0015691, 0.000243445, 0.00184038, -0.000695151, -0.0015691, 0.000243445, 0.00184038, -0.00116564, 0.0005688, 0.000260083, 0.00190911, -0.00116564, 0.0005688, 0.000260083, 0.00190911, 1.41078, 1.87205, 0.0056044, 0.0259692, 1.41078, 1.87205, 0.0056044, 0.0259692)

reports.append(Report(581337088, ("DT", 2, 2, 9), "MBwhEst2sec09"))
reports[-1].posNum = 55076
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.00194911, 0.00633359, 0), \
                           ValErr(-0.00216595, 0.00819544, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.40254e-05, 8.83566e-05, 0), \
                           -208168, 55076, 55076, -nan)
reports[-1].sigmax = ValErr(1.39336, 0.00419831, 0)
reports[-1].sigmay = ValErr(1.84054, 0.00554571, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00114351, 0.00878049, -0.00188315, 0.002305, -0.00110052, -0.00125006, -0.00188379, 0.00284906, -0.00110052, -0.00125006, -0.00188379, 0.00284906, -0.00024108, -0.00396167, -0.00187434, 0.00297575, -0.00024108, -0.00396167, -0.00187434, 0.00297575, 1.39335, 1.84056, 0.00553071, 0.0262945, 1.39335, 1.84056, 0.00553071, 0.0262945)

reports.append(Report(581599232, ("DT", 2, 2, 10), "MBwhEst2sec10"))
reports[-1].posNum = 72800
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.00212459, 0.00538849, 0), \
                           ValErr(0.00253604, 0.00693089, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.48298e-06, 6.95222e-05, 0), \
                           -276535, 72800, 72800, -nan)
reports[-1].sigmax = ValErr(1.39945, 0.00366756, 0)
reports[-1].sigmay = ValErr(1.86751, 0.00489422, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00125011, 0.00569779, 0.000177774, 0.00281696, -0.00230198, 0.00257878, 0.000202743, 0.00296702, -0.00230198, 0.00257878, 0.000202743, 0.00296702, -0.00337167, -0.0005291, 0.000240822, 0.00305134, -0.00337167, -0.0005291, 0.000240822, 0.00305134, 1.39945, 1.86751, 0.00559281, 0.0259182, 1.39945, 1.86751, 0.00559281, 0.0259182)

reports.append(Report(581861376, ("DT", 2, 2, 11), "MBwhEst2sec11"))
reports[-1].posNum = 75358
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000682391, 0.00527784, 0), \
                           ValErr(-0.00352269, 0.00671133, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.924e-06, 6.69109e-05, 0), \
                           -284550, 75358, 75358, -nan)
reports[-1].sigmax = ValErr(1.3879, 0.00357519, 0)
reports[-1].sigmay = ValErr(1.84099, 0.00474239, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00353083, 0.000211776, -0.000434332, 0.00264146, -0.00064046, -0.0035305, -0.000458082, 0.00257675, -0.00064046, -0.0035305, -0.000458082, 0.00257675, -0.00571535, -0.0113195, -0.000452112, 0.0027991, -0.00571535, -0.0113195, -0.000452112, 0.0027991, 1.3879, 1.84099, 0.00555247, 0.0256872, 1.3879, 1.84099, 0.00555247, 0.0256872)

reports.append(Report(582123520, ("DT", 2, 2, 12), "MBwhEst2sec12"))
reports[-1].posNum = 86704
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000690405, 0.00490088, 0), \
                           ValErr(0.000163915, 0.00634307, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.03785e-05, 6.27467e-05, 0), \
                           -329292, 86704, 86704, -nan)
reports[-1].sigmax = ValErr(1.39839, 0.00335814, 0)
reports[-1].sigmay = ValErr(1.86767, 0.00448508, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00447683, 0.000661763, -3.68162e-05, 0.00367628, 0.00048988, 0.000172964, -1.77025e-05, 0.00454932, 0.00048988, 0.000172964, -1.77025e-05, 0.00454932, -0.00208182, -0.00702077, 1.17499e-05, 0.0047048, -0.00208182, -0.00702077, 1.17499e-05, 0.0047048, 1.39839, 1.86767, 0.00552953, 0.0259108, 1.39839, 1.86767, 0.00552953, 0.0259108)

reports.append(Report(583434240, ("DT", 2, 3, 1), "MBwhEst3sec01"))
reports[-1].posNum = 68250
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.00202618, 0.00717515, 0), \
                           ValErr(-0.00488384, 0.00878631, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.07931e-05, 7.95363e-05, 0), \
                           -292921, 68250, 68250, -nan)
reports[-1].sigmax = ValErr(1.86589, 0.00505034, 0)
reports[-1].sigmay = ValErr(2.29393, 0.00620889, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.001144, -0.00877005, 0.000332684, 0.00313404, 0.00255061, -0.00464369, 0.000336, 0.0032201, 0.00255061, -0.00464369, 0.000336, 0.0032201, 0.007067, -0.00565534, 0.000340704, 0.00344114, 0.007067, -0.00565534, 0.000340704, 0.00344114, 1.8659, 2.29393, 0.00650884, 0.0197754, 1.8659, 2.29393, 0.00650884, 0.0197754)

reports.append(Report(583696384, ("DT", 2, 3, 2), "MBwhEst3sec02"))
reports[-1].posNum = 61072
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000328058, 0.00739353, 0), \
                           ValErr(-0.00131847, 0.00937696, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.70173e-06, 8.44891e-05, 0), \
                           -261034, 61072, 61072, -nan)
reports[-1].sigmax = ValErr(1.82589, 0.00522451, 0)
reports[-1].sigmay = ValErr(2.30309, 0.00658993, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00140119, -0.00136436, 0.000474963, -0.00148714, 0.000349288, -0.0012456, 0.000454499, -0.0018122, 0.000349288, -0.0012456, 0.000454499, -0.0018122, 8.91482e-05, 0.00484698, 0.00046694, -0.00176861, 8.91482e-05, 0.00484698, 0.00046694, -0.00176861, 1.82589, 2.30309, 0.00633916, 0.020775, 1.82589, 2.30309, 0.00633916, 0.020775)

reports.append(Report(583958528, ("DT", 2, 3, 3), "MBwhEst3sec03"))
reports[-1].posNum = 78962
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.00123414, 0.00654472, 0), \
                           ValErr(0.000936388, 0.0080301, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.01495e-05, 7.37787e-05, 0), \
                           -336040, 78962, 78962, -nan)
reports[-1].sigmax = ValErr(1.82955, 0.00460395, 0)
reports[-1].sigmay = ValErr(2.2564, 0.00567805, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00305952, 0.00952763, -0.000326864, -0.00223758, 0.00141742, 0.000913869, -0.000356377, -0.00232329, 0.00141742, 0.000913869, -0.000356377, -0.00232329, 0.00167943, -0.00817998, -0.000356786, -0.0021596, 0.00167943, -0.00817998, -0.000356786, -0.0021596, 1.82955, 2.25641, 0.00637133, 0.0194546, 1.82955, 2.25641, 0.00637133, 0.0194546)

reports.append(Report(584220672, ("DT", 2, 3, 4), "MBwhEst3sec04"))
reports[-1].posNum = 74234
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.00281359, 0.00681648, 0), \
                           ValErr(0.000294664, 0.00837182, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.7215e-06, 7.66919e-05, 0), \
                           -317432, 74234, 74234, -nan)
reports[-1].sigmax = ValErr(1.84749, 0.00479474, 0)
reports[-1].sigmay = ValErr(2.28052, 0.0059186, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00481632, 0.00568839, -2.9071e-05, 0.00150959, -0.00279967, 0.000301903, -3.50926e-05, 0.00148021, -0.00279967, 0.000301903, -3.50926e-05, 0.00148021, -0.00199856, -0.0106457, -6.0127e-05, 0.00158272, -0.00199856, -0.0106457, -6.0127e-05, 0.00158272, 1.84748, 2.28052, 0.00642088, 0.0196464, 1.84748, 2.28052, 0.00642088, 0.0196464)

reports.append(Report(584482816, ("DT", 2, 3, 5), "MBwhEst3sec05"))
reports[-1].posNum = 74718
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.0045666, 0.00674568, 0), \
                           ValErr(0.00523669, 0.00834436, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.87725e-05, 7.43738e-05, 0), \
                           -318913, 74718, 74718, -nan)
reports[-1].sigmax = ValErr(1.8339, 0.00474407, 0)
reports[-1].sigmay = ValErr(2.27939, 0.00589648, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00034533, 0.00654633, 0.000590443, -0.00324303, 0.00420057, 0.00507885, 0.000571307, -0.00329366, 0.00420057, 0.00507885, 0.000571307, -0.00329366, 0.00540163, 0.00182505, 0.000567266, -0.00310962, 0.00540163, 0.00182505, 0.000567266, -0.00310962, 1.83391, 2.27938, 0.00635823, 0.0203252, 1.83391, 2.27938, 0.00635823, 0.0203252)

reports.append(Report(584744960, ("DT", 2, 3, 6), "MBwhEst3sec06"))
reports[-1].posNum = 84722
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.00216279, 0.00637772, 0), \
                           ValErr(0.000363003, 0.00782412, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.2236e-05, 7.13304e-05, 0), \
                           -361505, 84722, 84722, -nan)
reports[-1].sigmax = ValErr(1.83781, 0.00446462, 0)
reports[-1].sigmay = ValErr(2.27165, 0.00551862, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000753213, 0.00557604, -0.000702117, -0.000100334, 0.00188444, 0.00019506, -0.000725545, 0.000128356, 0.00188444, 0.00019506, -0.000725545, 0.000128356, -0.00521009, -0.00827036, -0.000694132, 0.000417487, -0.00521009, -0.00827036, -0.000694132, 0.000417487, 1.83781, 2.27164, 0.0064202, 0.0200969, 1.83781, 2.27164, 0.0064202, 0.0200969)

reports.append(Report(585007104, ("DT", 2, 3, 7), "MBwhEst3sec07"))
reports[-1].posNum = 86708
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.00321122, 0.00637495, 0), \
                           ValErr(0.00359794, 0.00777367, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.01842e-05, 7.06358e-05, 0), \
                           -371708, 86708, 86708, -nan)
reports[-1].sigmax = ValErr(1.86088, 0.00446887, 0)
reports[-1].sigmay = ValErr(2.28866, 0.00549625, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00321296, 0.0121927, 0.00178475, 0.000419582, 0.00285306, 0.00365897, 0.00177245, 0.000398271, 0.00285306, 0.00365897, 0.00177245, 0.000398271, 0.0101294, -0.00423515, 0.00176815, 0.000520139, 0.0101294, -0.00423515, 0.00176815, 0.000520139, 1.86086, 2.28869, 0.00647453, 0.0202278, 1.86086, 2.28869, 0.00647453, 0.0202278)

reports.append(Report(585269248, ("DT", 2, 3, 8), "MBwhEst3sec08"))
reports[-1].posNum = 76918
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.000351, 0.00668171, 0), \
                           ValErr(0.000104706, 0.00825087, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.07762e-05, 7.51619e-05, 0), \
                           -328271, 76918, 76918, -nan)
reports[-1].sigmax = ValErr(1.83527, 0.00467921, 0)
reports[-1].sigmay = ValErr(2.27669, 0.00580466, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00178136, 0.0061774, -0.000722102, -0.00249548, -0.000731523, -0.000235632, -0.000765957, -0.00232421, -0.000731523, -0.000235632, -0.000765957, -0.00232421, 0.00189787, -0.000858819, -0.000782027, -0.00217464, 0.00189787, -0.000858819, -0.000782027, -0.00217464, 1.83529, 2.27669, 0.00636181, 0.0226966, 1.83529, 2.27669, 0.00636181, 0.0226966)

reports.append(Report(585531392, ("DT", 2, 3, 9), "MBwhEst3sec09"))
reports[-1].posNum = 78284
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000876112, 0.00662693, 0), \
                           ValErr(0.00274914, 0.00828014, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.98043e-05, 7.45503e-05, 0), \
                           -335991, 78284, 78284, -nan)
reports[-1].sigmax = ValErr(1.84775, 0.00467, 0)
reports[-1].sigmay = ValErr(2.31661, 0.0058549, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00403382, -0.0065193, -0.000304054, 0.00105463, 0.000577595, 0.00271273, -0.000331686, 0.000948263, 0.000577595, 0.00271273, -0.000331686, 0.000948263, -0.000772502, -0.000608132, -0.000344846, 0.00101986, -0.000772502, -0.000608132, -0.000344846, 0.00101986, 1.84777, 2.31658, 0.00644027, 0.0199563, 1.84777, 2.31658, 0.00644027, 0.0199563)

reports.append(Report(585793536, ("DT", 2, 3, 10), "MBwhEst3sec10"))
reports[-1].posNum = 83224
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.00194787, 0.00639924, 0), \
                           ValErr(-0.00104322, 0.00793992, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.44104e-05, 7.22442e-05, 0), \
                           -355669, 83224, 83224, -nan)
reports[-1].sigmax = ValErr(1.83701, 0.0045027, 0)
reports[-1].sigmay = ValErr(2.28785, 0.00560776, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00254933, 0.00842306, 0.000238283, 0.00146505, -0.00216247, -0.00117352, 0.000243129, 0.00151538, -0.00216247, -0.00117352, 0.000243129, 0.00151538, -0.00475538, -0.00613361, 0.000259725, 0.00170278, -0.00475538, -0.00613361, 0.000259725, 0.00170278, 1.83702, 2.28785, 0.00638803, 0.0200246, 1.83702, 2.28785, 0.00638803, 0.0200246)

reports.append(Report(586055680, ("DT", 2, 3, 11), "MBwhEst3sec11"))
reports[-1].posNum = 70180
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.00367094, 0.00699266, 0), \
                           ValErr(0.00144045, 0.00866831, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.72106e-05, 7.59266e-05, 0), \
                           -300477, 70180, 70180, -nan)
reports[-1].sigmax = ValErr(1.84615, 0.00492776, 0)
reports[-1].sigmay = ValErr(2.29457, 0.00612472, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00378248, 0.012583, 0.000790967, -0.00184987, 0.00346408, 0.0015629, 0.000787059, -0.0017627, 0.00346408, 0.0015629, 0.000787059, -0.0017627, 0.00187229, -0.00490311, 0.000769504, -0.00175875, 0.00187229, -0.00490311, 0.000769504, -0.00175875, 1.84614, 2.29458, 0.00644604, 0.0193564, 1.84614, 2.29458, 0.00644604, 0.0193564)

reports.append(Report(586317824, ("DT", 2, 3, 12), "MBwhEst3sec12"))
reports[-1].posNum = 80860
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(6.85935e-05, 0.00650598, 0), \
                           ValErr(0.00245415, 0.00808466, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.46393e-05, 7.32906e-05, 0), \
                           -345665, 80860, 80860, -nan)
reports[-1].sigmax = ValErr(1.83951, 0.00457434, 0)
reports[-1].sigmay = ValErr(2.28755, 0.00568847, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00427561, 0.00960328, 9.32785e-05, -0.000218949, 0.000206489, 0.00261078, 0.000100735, -0.000382737, 0.000206489, 0.00261078, 0.000100735, -0.000382737, 0.00512826, -0.00764856, 0.000112473, -0.000201426, 0.00512826, -0.00764856, 0.000112473, -0.000201426, 1.8395, 2.28755, 0.00633664, 0.0204676, 1.8395, 2.28755, 0.00633664, 0.0204676)

reports.append(Report(587497472, ("DT", -2, 4, 1), "MBwhAst4sec01"))
reports[-1].posNum = 121040
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.000170101, 0.00746951, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.11615e-05, 0.000121828, 0), \
                           -286978, 121040, 121040, -nan)
reports[-1].sigmaresid = ValErr(2.59089, 0.00526585, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.010506, None, -0.000691519, None, 0.000202551, None, -0.000745552, None, 0.000202551, None, -0.000745552, None, 0.00115279, None, -0.00069362, None, 0.00115279, None, -0.00069362, None, 2.59089, None, 0.00793728, None, 2.59089, None, 0.00793728, None)

reports.append(Report(587759616, ("DT", -2, 4, 2), "MBwhAst4sec02"))
reports[-1].posNum = 136816
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.00167986, 0.00701523, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.57817e-05, 0.000114643, 0), \
                           -324368, 136816, 136816, -nan)
reports[-1].sigmaresid = ValErr(2.59061, 0.00495243, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00153821, None, 0.000230952, None, 0.00158098, None, 0.00017447, None, 0.00158098, None, 0.00017447, None, 0.0101346, None, 8.09999e-05, None, 0.0101346, None, 8.09999e-05, None, 2.59061, None, 0.00796112, None, 2.59061, None, 0.00796112, None)

reports.append(Report(588021760, ("DT", -2, 4, 3), "MBwhAst4sec03"))
reports[-1].posNum = 118136
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.00202935, 0.00750901, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.69403e-05, 0.000121812, 0), \
                           -279485, 118136, 118136, -nan)
reports[-1].sigmaresid = ValErr(2.57758, 0.00530341, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0120104, None, -6.57458e-05, None, 0.00197634, None, -0.000126633, None, 0.00197634, None, -0.000126633, None, 0.00333452, None, -0.000145237, None, 0.00333452, None, -0.000145237, None, 2.57758, None, 0.00786508, None, 2.57758, None, 0.00786508, None)

reports.append(Report(588283904, ("DT", -2, 4, 4), "MBwhAst4sec04"))
reports[-1].posNum = 97132
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.00268903, 0.00865127, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.38672e-05, 0.000138359, 0), \
                           -233785, 97132, 97132, -nan)
reports[-1].sigmaresid = ValErr(2.68571, 0.00609347, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000509117, None, -0.0033667, None, 0.00295823, None, -0.00339972, None, 0.00295823, None, -0.00339972, None, 0.018869, None, -0.00349645, None, 0.018869, None, -0.00349645, None, 2.6857, None, 0.00820744, None, 2.6857, None, 0.00820744, None)

reports.append(Report(590643200, ("DT", -2, 4, 13), "MBwhAst4sec13"))
reports[-1].posNum = 101808
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.0011364, 0.00825743, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.81883e-05, 0.000133982, 0), \
                           -242634, 101808, 101808, -nan)
reports[-1].sigmaresid = ValErr(2.623, 0.0058129, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.01003, None, 0.00160658, None, -0.00158822, None, 0.00164304, None, -0.00158822, None, 0.00164304, None, 0.00328722, None, 0.00171985, None, 0.00328722, None, 0.00171985, None, 2.623, None, 0.00802246, None, 2.623, None, 0.00802246, None)

reports.append(Report(588546048, ("DT", -2, 4, 5), "MBwhAst4sec05"))
reports[-1].posNum = 128760
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.000426734, 0.00724946, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.97293e-05, 0.000117351, 0), \
                           -304921, 128760, 128760, -nan)
reports[-1].sigmaresid = ValErr(2.58363, 0.00509126, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00122095, None, 0.000846432, None, -0.000215655, None, 0.000892173, None, -0.000215655, None, 0.000892173, None, 0.000995975, None, 0.0009329, None, 0.000995975, None, 0.0009329, None, 2.58364, None, 0.00788373, None, 2.58364, None, 0.00788373, None)

reports.append(Report(588808192, ("DT", -2, 4, 6), "MBwhAst4sec06"))
reports[-1].posNum = 136658
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.00116053, 0.0070843, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.55453e-05, 0.000114113, 0), \
                           -324504, 136658, 136658, -nan)
reports[-1].sigmaresid = ValErr(2.6003, 0.00497384, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00629896, None, 0.000476142, None, 0.000823129, None, 0.000549371, None, 0.000823129, None, 0.000549371, None, -0.00172736, None, 0.00061006, None, -0.00172736, None, 0.00061006, None, 2.60031, None, 0.00797276, None, 2.60031, None, 0.00797276, None)

reports.append(Report(589070336, ("DT", -2, 4, 7), "MBwhAst4sec07"))
reports[-1].posNum = 148166
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.000180382, 0.00677264, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(7.31402e-07, 0.000109555, 0), \
                           -351374, 148166, 148166, -nan)
reports[-1].sigmaresid = ValErr(2.59233, 0.00476214, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.010056, None, -0.000616147, None, -0.000177756, None, -0.000606515, None, -0.000177756, None, -0.000606515, None, -0.00463752, None, -0.00052183, None, -0.00463752, None, -0.00052183, None, 2.59232, None, 0.00797967, None, 2.59232, None, 0.00797967, None)

reports.append(Report(589332480, ("DT", -2, 4, 8), "MBwhAst4sec08"))
reports[-1].posNum = 144592
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.000201591, 0.00678949, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.62904e-06, 0.000109437, 0), \
                           -341309, 144592, 144592, -nan)
reports[-1].sigmaresid = ValErr(2.56397, 0.00476789, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00833901, None, -0.0011869, None, -0.000176847, None, -0.00114624, None, -0.000176847, None, -0.00114624, None, -0.00749549, None, -0.00110681, None, -0.00749549, None, -0.00110681, None, 2.56397, None, 0.00787068, None, 2.56397, None, 0.00787068, None)

reports.append(Report(589594624, ("DT", -2, 4, 9), "MBwhAst4sec09"))
reports[-1].posNum = 62650
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.00359535, 0.0101248, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(7.35422e-06, 0.000163831, 0), \
                           -146574, 62650, 62650, -nan)
reports[-1].sigmaresid = ValErr(2.51088, 0.00709334, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00135452, None, -0.000126047, None, 0.00367159, None, -0.000157892, None, 0.00367159, None, -0.000157892, None, 0.00736336, None, -0.000148764, None, 0.00736336, None, -0.000148764, None, 2.51088, None, 0.00754748, None, 2.51088, None, 0.00754748, None)

reports.append(Report(589856768, ("DT", -2, 4, 10), "MBwhAst4sec10"))
reports[-1].posNum = 84576
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.00134827, 0.00898981, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.02968e-05, 0.000144843, 0), \
                           -200640, 84576, 84576, -nan)
reports[-1].sigmaresid = ValErr(2.59443, 0.00630818, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00748888, None, -0.000669491, None, -0.00203782, None, -0.000685674, None, -0.00203782, None, -0.000685674, None, 0.000579569, None, -0.000679169, None, 0.000579569, None, -0.000679169, None, 2.59443, None, 0.00811873, None, 2.59443, None, 0.00811873, None)

reports.append(Report(590905344, ("DT", -2, 4, 14), "MBwhAst4sec14"))
reports[-1].posNum = 83914
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.000531043, 0.00897696, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.16091e-05, 0.000146423, 0), \
                           -198868, 83914, 83914, -nan)
reports[-1].sigmaresid = ValErr(2.58819, 0.00631778, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00475608, None, 0.00128658, None, 5.01598e-05, None, 0.00125752, None, 5.01598e-05, None, 0.00125752, None, -0.00879383, None, 0.00122693, None, -0.00879383, None, 0.00122693, None, 2.5882, None, 0.00808844, None, 2.5882, None, 0.00808844, None)

reports.append(Report(590118912, ("DT", -2, 4, 11), "MBwhAst4sec11"))
reports[-1].posNum = 62410
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.00417278, 0.0100942, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.26322e-06, 0.000165803, 0), \
                           -145865, 62410, 62410, -nan)
reports[-1].sigmaresid = ValErr(2.50493, 0.0070902, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00249599, None, 0.00106862, None, -0.00420269, None, 0.00106815, None, -0.00420269, None, 0.00106815, None, -0.0189421, None, 0.00110953, None, -0.0189421, None, 0.00110953, None, 2.50493, None, 0.00755037, None, 2.50493, None, 0.00755037, None)

reports.append(Report(590381056, ("DT", -2, 4, 12), "MBwhAst4sec12"))
reports[-1].posNum = 141280
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.00269349, 0.00687298, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.86686e-05, 0.000111476, 0), \
                           -334208, 141280, 141280, -nan)
reports[-1].sigmaresid = ValErr(2.57703, 0.00484801, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0122683, None, 0.000623428, None, -0.00261171, None, 0.000583102, None, -0.00261171, None, 0.000583102, None, -0.000593684, None, 0.000611202, None, -0.000593684, None, 0.000611202, None, 2.57703, None, 0.00795739, None, 2.57703, None, 0.00795739, None)

reports.append(Report(587530240, ("DT", -1, 4, 1), "MBwhBst4sec01"))
reports[-1].posNum = 172058
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.00200869, 0.00599992, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(7.94031e-06, 9.37872e-05, 0), \
                           -400987, 172058, 172058, -nan)
reports[-1].sigmaresid = ValErr(2.48829, 0.0042418, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00420861, None, -0.00115072, None, -0.00199667, None, -0.00119635, None, -0.00199667, None, -0.00119635, None, -0.000267847, None, -0.00112541, None, -0.000267847, None, -0.00112541, None, 2.48829, None, 0.00777662, None, 2.48829, None, 0.00777662, None)

reports.append(Report(587792384, ("DT", -1, 4, 2), "MBwhBst4sec02"))
reports[-1].posNum = 161752
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.00209733, 0.00608719, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.47457e-05, 9.65147e-05, 0), \
                           -374316, 161752, 161752, -nan)
reports[-1].sigmaresid = ValErr(2.44781, 0.00430366, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00227489, None, -0.00026343, None, 0.00213177, None, -0.000313118, None, 0.00213177, None, -0.000313118, None, 0.00703819, None, -0.000279792, None, 0.00703819, None, -0.000279792, None, 2.44782, None, 0.00771174, None, 2.44782, None, 0.00771174, None)

reports.append(Report(588054528, ("DT", -1, 4, 3), "MBwhBst4sec03"))
reports[-1].posNum = 105768
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.00228007, 0.0076177, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.21126e-05, 0.000154661, 0), \
                           -244878, 105768, 105768, -nan)
reports[-1].sigmaresid = ValErr(2.45051, 0.005328, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00321297, None, -0.000273402, None, 0.00265915, None, -0.000319365, None, 0.00265915, None, -0.000319365, None, 0.0016307, None, -0.000248658, None, 0.0016307, None, -0.000248658, None, 2.45051, None, 0.00770011, None, 2.45051, None, 0.00770011, None)

reports.append(Report(588316672, ("DT", -1, 4, 4), "MBwhBst4sec04"))
reports[-1].posNum = 119940
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.000332878, 0.00726693, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.21819e-05, 0.000112256, 0), \
                           -280825, 119940, 119940, -nan)
reports[-1].sigmaresid = ValErr(2.51541, 0.00513585, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000706045, None, 0.000158408, None, 0.000458592, None, 0.000151314, None, 0.000458592, None, 0.000151314, None, -0.00215189, None, 0.00011264, None, -0.00215189, None, 0.00011264, None, 2.51542, None, 0.00770673, None, 2.51542, None, 0.00770673, None)

reports.append(Report(590675968, ("DT", -1, 4, 13), "MBwhBst4sec13"))
reports[-1].posNum = 119126
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.00193055, 0.00721437, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.33629e-05, 0.000113328, 0), \
                           -277677, 119126, 119126, -nan)
reports[-1].sigmaresid = ValErr(2.48932, 0.0050987, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00321046, None, 0.0011931, None, 0.00202335, None, 0.00119792, None, 0.00202335, None, 0.00119792, None, -0.00133889, None, 0.00115144, None, -0.00133889, None, 0.00115144, None, 2.48932, None, 0.00769304, None, 2.48932, None, 0.00769304, None)

reports.append(Report(588578816, ("DT", -1, 4, 5), "MBwhBst4sec05"))
reports[-1].posNum = 152294
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.00108535, 0.00626622, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.53625e-05, 9.72667e-05, 0), \
                           -351996, 152294, 152294, -nan)
reports[-1].sigmaresid = ValErr(2.44086, 0.0044227, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00169021, None, 0.000790777, None, -0.00141973, None, 0.000891037, None, -0.00141973, None, 0.000891037, None, 0.00422837, None, 0.000900906, None, 0.00422837, None, 0.000900906, None, 2.44087, None, 0.00765343, None, 2.44087, None, 0.00765343, None)

reports.append(Report(588840960, ("DT", -1, 4, 6), "MBwhBst4sec06"))
reports[-1].posNum = 161738
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.00154169, 0.00612403, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.47688e-05, 9.49159e-05, 0), \
                           -375276, 161738, 161738, -nan)
reports[-1].sigmaresid = ValErr(2.46288, 0.00433034, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00767077, None, 0.000468562, None, -0.00153805, None, 0.000518697, None, -0.00153805, None, 0.000518697, None, 0.00539967, None, 0.000518696, None, 0.00539967, None, 0.000518696, None, 2.46288, None, 0.00764119, None, 2.46288, None, 0.00764119, None)

reports.append(Report(589103104, ("DT", -1, 4, 7), "MBwhBst4sec07"))
reports[-1].posNum = 180600
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.000426785, 0.0057946, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.76025e-05, 9.00703e-05, 0), \
                           -418889, 180600, 180600, -nan)
reports[-1].sigmaresid = ValErr(2.46081, 0.00409468, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00395719, None, -0.00143773, None, 0.000359825, None, -0.00139249, None, 0.000359825, None, -0.00139249, None, -0.00169731, None, -0.00141647, None, -0.00169731, None, -0.00141647, None, 2.46081, None, 0.0076649, None, 2.46081, None, 0.0076649, None)

reports.append(Report(589365248, ("DT", -1, 4, 8), "MBwhBst4sec08"))
reports[-1].posNum = 176438
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.00118379, 0.00578069, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.05369e-05, 9.01576e-05, 0), \
                           -406832, 176438, 176438, -nan)
reports[-1].sigmaresid = ValErr(2.42752, 0.0040865, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00461249, None, 0.000855844, None, -0.00115451, None, 0.000884626, None, -0.00115451, None, 0.000884626, None, -0.00453267, None, 0.000905903, None, -0.00453267, None, 0.000905903, None, 2.42752, None, 0.0074865, None, 2.42752, None, 0.0074865, None)

reports.append(Report(589627392, ("DT", -1, 4, 9), "MBwhBst4sec09"))
reports[-1].posNum = 73940
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.000377257, 0.00878176, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000105903, 0.000138393, 0), \
                           -169077, 73940, 73940, -nan)
reports[-1].sigmaresid = ValErr(2.38153, 0.006193, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00471742, None, -0.00181423, None, 0.000867124, None, -0.0018338, None, 0.000867124, None, -0.0018338, None, 0.00210987, None, -0.00185958, None, 0.00210987, None, -0.00185958, None, 2.38153, None, 0.00709098, None, 2.38153, None, 0.00709098, None)

reports.append(Report(589889536, ("DT", -1, 4, 10), "MBwhBst4sec10"))
reports[-1].posNum = 85514
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.00423994, 0.00844574, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.64069e-05, 0.000132633, 0), \
                           -198398, 85514, 85514, -nan)
reports[-1].sigmaresid = ValErr(2.46237, 0.00595414, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00233299, None, -2.64273e-05, None, -0.00401055, None, -1.99104e-05, None, -0.00401055, None, -1.99104e-05, None, 0.00271009, None, -3.19427e-05, None, 0.00271009, None, -3.19427e-05, None, 2.46237, None, 0.00773042, None, 2.46237, None, 0.00773042, None)

reports.append(Report(590938112, ("DT", -1, 4, 14), "MBwhBst4sec14"))
reports[-1].posNum = 88140
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.00231037, 0.00827853, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.70879e-06, 0.000129637, 0), \
                           -204296, 88140, 88140, -nan)
reports[-1].sigmaresid = ValErr(2.45694, 0.00585185, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00287762, None, -0.000736679, None, -0.00233412, None, -0.00076107, None, -0.00233412, None, -0.00076107, None, 0.00410601, None, -0.00088418, None, 0.00410601, None, -0.00088418, None, 2.45694, None, 0.0077298, None, 2.45694, None, 0.0077298, None)

reports.append(Report(590151680, ("DT", -1, 4, 11), "MBwhBst4sec11"))
reports[-1].posNum = 74032
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.00297195, 0.00868967, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.75061e-06, 0.000135353, 0), \
                           -168740, 74032, 74032, -nan)
reports[-1].sigmaresid = ValErr(2.36399, 0.00614356, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00218077, None, 0.000163682, None, -0.00296948, None, 0.000144478, None, -0.00296948, None, 0.000144478, None, -0.0033909, None, 0.00013357, None, -0.0033909, None, 0.00013357, None, 2.36399, None, 0.00716152, None, 2.36399, None, 0.00716152, None)

reports.append(Report(590413824, ("DT", -1, 4, 12), "MBwhBst4sec12"))
reports[-1].posNum = 123308
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.000659575, 0.00713615, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.09408e-05, 0.000111206, 0), \
                           -288201, 123308, 123308, -nan)
reports[-1].sigmaresid = ValErr(2.50505, 0.00504438, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0059519, None, -0.000177407, None, 0.000680505, None, -0.00025328, None, 0.000680505, None, -0.00025328, None, -0.00668362, None, -0.000258949, None, -0.00668362, None, -0.000258949, None, 2.50505, None, 0.00781042, None, 2.50505, None, 0.00781042, None)

reports.append(Report(587563008, ("DT", 0, 4, 1), "MBwhCst4sec01"))
reports[-1].posNum = 149058
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-8.54999e-05, 0.00637975, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.16851e-05, 9.65159e-05, 0), \
                           -345464, 149058, 149058, -nan)
reports[-1].sigmaresid = ValErr(2.45643, 0.00449896, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0110538, None, -0.00103051, None, 0.000263067, None, -0.00109546, None, 0.000263067, None, -0.00109546, None, 0.00820342, None, -0.00123912, None, 0.00820342, None, -0.00123912, None, 2.45644, None, 0.00792048, None, 2.45644, None, 0.00792048, None)

reports.append(Report(587825152, ("DT", 0, 4, 2), "MBwhCst4sec02"))
reports[-1].posNum = 111474
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.0021561, 0.00725566, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.04892e-05, 0.000108559, 0), \
                           -256302, 111474, 111474, -nan)
reports[-1].sigmaresid = ValErr(2.41155, 0.00510733, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00272917, None, 0.000807634, None, -0.00224185, None, 0.000879793, None, -0.00224185, None, 0.000879793, None, -0.00160489, None, 0.000973933, None, -0.00160489, None, 0.000973933, None, 2.41155, None, 0.00784115, None, 2.41155, None, 0.00784115, None)

reports.append(Report(588087296, ("DT", 0, 4, 3), "MBwhCst4sec03"))
reports[-1].posNum = 141362
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.00366322, 0.00646766, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.59316e-05, 9.83406e-05, 0), \
                           -326131, 141362, 141362, -nan)
reports[-1].sigmaresid = ValErr(2.43056, 0.00457115, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00186866, None, 0.000730519, None, -0.00355136, None, 0.000835262, None, -0.00355136, None, 0.000835262, None, -0.00562994, None, 0.000945751, None, -0.00562994, None, 0.000945751, None, 2.43057, None, 0.00785735, None, 2.43057, None, 0.00785735, None)

reports.append(Report(588349440, ("DT", 0, 4, 4), "MBwhCst4sec04"))
reports[-1].posNum = 117348
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.00109475, 0.00747113, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(8.6992e-05, 0.000113109, 0), \
                           -276363, 117348, 117348, -nan)
reports[-1].sigmaresid = ValErr(2.55011, 0.00526387, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00877543, None, -0.000366071, None, 0.000610696, None, -0.000375081, None, 0.000610696, None, -0.000375081, None, 0.00309773, None, -0.000497164, None, 0.00309773, None, -0.000497164, None, 2.55011, None, 0.00819746, None, 2.55011, None, 0.00819746, None)

reports.append(Report(590708736, ("DT", 0, 4, 13), "MBwhCst4sec13"))
reports[-1].posNum = 122128
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.000636061, 0.0070627, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(9.07483e-05, 0.000107069, 0), \
                           -283618, 122128, 122128, -nan)
reports[-1].sigmaresid = ValErr(2.46788, 0.00499292, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00264159, None, 0.000190123, None, -0.000559079, None, 0.000219551, None, -0.000559079, None, 0.000219551, None, -0.00841267, None, 0.000255622, None, -0.00841267, None, 0.000255622, None, 2.46789, None, 0.00788084, None, 2.46789, None, 0.00788084, None)

reports.append(Report(588611584, ("DT", 0, 4, 5), "MBwhCst4sec05"))
reports[-1].posNum = 172638
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.00136518, 0.00586099, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.80528e-05, 8.86704e-05, 0), \
                           -397881, 172638, 172638, -nan)
reports[-1].sigmaresid = ValErr(2.42485, 0.00412669, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000293333, None, 0.00172481, None, 0.00147665, None, 0.00181379, None, 0.00147665, None, 0.00181379, None, 0.000345886, None, 0.0018287, None, 0.000345886, None, 0.0018287, None, 2.42486, None, 0.00781167, None, 2.42486, None, 0.00781167, None)

reports.append(Report(588873728, ("DT", 0, 4, 6), "MBwhCst4sec06"))
reports[-1].posNum = 179220
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.00129837, 0.00575351, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.85323e-06, 8.72832e-05, 0), \
                           -413851, 179220, 179220, -nan)
reports[-1].sigmaresid = ValErr(2.43571, 0.00406834, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00337313, None, -0.000223348, None, 0.00129453, None, -0.000321309, None, 0.00129453, None, -0.000321309, None, 0.00948751, None, -0.000449462, None, 0.00948751, None, -0.000449462, None, 2.43571, None, 0.00784051, None, 2.43571, None, 0.00784051, None)

reports.append(Report(589135872, ("DT", 0, 4, 7), "MBwhCst4sec07"))
reports[-1].posNum = 192654
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.000656241, 0.00558791, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.31046e-05, 8.44837e-05, 0), \
                           -446206, 192654, 192654, -nan)
reports[-1].sigmaresid = ValErr(2.45263, 0.00395119, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00563007, None, -0.000892534, None, 0.000651496, None, -0.000916158, None, 0.000651496, None, -0.000916158, None, 0.0064907, None, -0.00101451, None, 0.0064907, None, -0.00101451, None, 2.45263, None, 0.00783782, None, 2.45263, None, 0.00783782, None)

reports.append(Report(589398016, ("DT", 0, 4, 8), "MBwhCst4sec08"))
reports[-1].posNum = 182142
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.000279614, 0.00567015, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.54362e-05, 8.58044e-05, 0), \
                           -419342, 182142, 182142, -nan)
reports[-1].sigmaresid = ValErr(2.41897, 0.00400785, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00394563, None, 0.00161914, None, 0.000271548, None, 0.00168084, None, 0.000271548, None, 0.00168084, None, -0.00661512, None, 0.00191748, None, -0.00661512, None, 0.00191748, None, 2.41897, None, 0.0078122, None, 2.41897, None, 0.0078122, None)

reports.append(Report(589660160, ("DT", 0, 4, 9), "MBwhCst4sec09"))
reports[-1].posNum = 61954
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.00359616, 0.00947048, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.53452e-05, 0.000143437, 0), \
                           -140965, 61954, 61954, -nan)
reports[-1].sigmaresid = ValErr(2.3546, 0.0066902, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0114571, None, -0.000424657, None, 0.00348556, None, -0.000433786, None, 0.00348556, None, -0.000433786, None, 0.00934178, None, -0.000373327, None, 0.00934178, None, -0.000373327, None, 2.35461, None, 0.00719246, None, 2.35461, None, 0.00719246, None)

reports.append(Report(589922304, ("DT", 0, 4, 10), "MBwhCst4sec10"))
reports[-1].posNum = 75084
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.00201694, 0.00889252, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.98771e-05, 0.000133518, 0), \
                           -172998, 75084, 75084, -nan)
reports[-1].sigmaresid = ValErr(2.42326, 0.00625333, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00508268, None, 0.000855828, None, -0.0021626, None, 0.000886299, None, -0.0021626, None, 0.000886299, None, -0.0158479, None, 0.000874564, None, -0.0158479, None, 0.000874564, None, 2.42326, None, 0.00796825, None, 2.42326, None, 0.00796825, None)

reports.append(Report(590970880, ("DT", 0, 4, 14), "MBwhCst4sec14"))
reports[-1].posNum = 71098
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.00117721, 0.00923926, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.30653e-06, 0.000138921, 0), \
                           -164717, 71098, 71098, -nan)
reports[-1].sigmaresid = ValErr(2.45425, 0.00650841, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000958956, None, -0.00383062, None, -0.0012207, None, -0.00391694, None, -0.0012207, None, -0.00391694, None, -0.00806813, None, -0.00380957, None, -0.00806813, None, -0.00380957, None, 2.45425, None, 0.00812104, None, 2.45425, None, 0.00812104, None)

reports.append(Report(590184448, ("DT", 0, 4, 11), "MBwhCst4sec11"))
reports[-1].posNum = 70032
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.00362876, 0.00860257, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.84227e-05, 0.000130138, 0), \
                           -156631, 70032, 70032, -nan)
reports[-1].sigmaresid = ValErr(2.26511, 0.00605239, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00849221, None, -0.0027663, None, 0.00382201, None, -0.00276327, None, 0.00382201, None, -0.00276327, None, 0.00346257, None, -0.00275372, None, 0.00346257, None, -0.00275372, None, 2.26511, None, 0.00695857, None, 2.26511, None, 0.00695857, None)

reports.append(Report(590446592, ("DT", 0, 4, 12), "MBwhCst4sec12"))
reports[-1].posNum = 174440
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.000906584, 0.00576315, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.97881e-05, 8.72289e-05, 0), \
                           -400532, 174440, 174440, -nan)
reports[-1].sigmaresid = ValErr(2.40407, 0.00407014, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00059195, None, -0.00222607, None, 0.000961468, None, -0.00232456, None, 0.000961468, None, -0.00232456, None, 0.00257281, None, -0.00233122, None, 0.00257281, None, -0.00233122, None, 2.40407, None, 0.0078127, None, 2.40407, None, 0.0078127, None)

reports.append(Report(587595776, ("DT", 1, 4, 1), "MBwhDst4sec01"))
reports[-1].posNum = 160800
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.00110866, 0.00614774, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.36768e-05, 9.67017e-05, 0), \
                           -373050, 160800, 160800, -nan)
reports[-1].sigmaresid = ValErr(2.46212, 0.0043416, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00668668, None, -7.97241e-05, None, -0.00118743, None, -2.87446e-05, None, -0.00118743, None, -2.87446e-05, None, -0.005534, None, 5.17205e-05, None, -0.005534, None, 5.17205e-05, None, 2.46212, None, 0.00766161, None, 2.46212, None, 0.00766161, None)

reports.append(Report(587857920, ("DT", 1, 4, 2), "MBwhDst4sec02"))
reports[-1].posNum = 143048
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.000801044, 0.00644623, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.14318e-05, 0.000103294, 0), \
                           -330277, 143048, 143048, -nan)
reports[-1].sigmaresid = ValErr(2.43492, 0.00455228, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00170736, None, -0.000530343, None, -0.000857634, None, -0.000499694, None, -0.000857634, None, -0.000499694, None, 0.00382421, None, -0.000500797, None, 0.00382421, None, -0.000500797, None, 2.43492, None, 0.00758386, None, 2.43492, None, 0.00758386, None)

reports.append(Report(588120064, ("DT", 1, 4, 3), "MBwhDst4sec03"))
reports[-1].posNum = 146392
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(2.07685e-05, 0.0063017, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.01004e-05, 9.85888e-05, 0), \
                           -336554, 146392, 146392, -nan)
reports[-1].sigmaresid = ValErr(2.41102, 0.00445582, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00305045, None, 0.000612227, None, 2.84969e-05, None, 0.000702774, None, 2.84969e-05, None, 0.000702774, None, 0.00444182, None, 0.000764103, None, 0.00444182, None, 0.000764103, None, 2.41103, None, 0.00761852, None, 2.41103, None, 0.00761852, None)

reports.append(Report(588382208, ("DT", 1, 4, 4), "MBwhDst4sec04"))
reports[-1].posNum = 89730
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.000577919, 0.00852968, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(7.94091e-06, 0.000172077, 0), \
                           -210502, 89730, 89730, -nan)
reports[-1].sigmaresid = ValErr(2.52695, 0.00596506, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00192484, None, 5.058e-05, None, -0.000637597, None, 5.48988e-05, None, -0.000637597, None, 5.48988e-05, None, -0.0180187, None, 0.000119107, None, -0.0180187, None, 0.000119107, None, 2.52694, None, 0.00785019, None, 2.52694, None, 0.00785019, None)

reports.append(Report(590741504, ("DT", 1, 4, 13), "MBwhDst4sec13"))
reports[-1].posNum = 74198
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.00142751, 0.00958363, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000109344, 0.000191497, 0), \
                           -173767, 74198, 74198, -nan)
reports[-1].sigmaresid = ValErr(2.51682, 0.00653342, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00176937, None, -0.00149109, None, 2.58021e-05, None, -0.00153959, None, 2.58021e-05, None, -0.00153959, None, 0.0118431, None, -0.00160825, None, 0.0118431, None, -0.00160825, None, 2.51682, None, 0.00789515, None, 2.51682, None, 0.00789515, None)

reports.append(Report(588644352, ("DT", 1, 4, 5), "MBwhDst4sec05"))
reports[-1].posNum = 155678
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.000439533, 0.00639525, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000117957, 9.85768e-05, 0), \
                           -364987, 155678, 155678, -nan)
reports[-1].sigmaresid = ValErr(2.52328, 0.00452207, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00751047, None, -0.00331384, None, -0.000443439, None, -0.00340208, None, -0.000443439, None, -0.00340208, None, -0.000273505, None, -0.00349946, None, -0.000273505, None, -0.00349946, None, 2.52329, None, 0.00788373, None, 2.52329, None, 0.00788373, None)

reports.append(Report(588906496, ("DT", 1, 4, 6), "MBwhDst4sec06"))
reports[-1].posNum = 173758
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.00242438, 0.00585027, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.32443e-05, 9.12536e-05, 0), \
                           -401273, 173758, 173758, -nan)
reports[-1].sigmaresid = ValErr(2.4362, 0.00413287, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00348912, None, -0.000256482, None, -0.00235745, None, -0.00029633, None, -0.00235745, None, -0.00029633, None, -0.00169672, None, -0.000337101, None, -0.00169672, None, -0.000337101, None, 2.4362, None, 0.00757512, None, 2.4362, None, 0.00757512, None)

reports.append(Report(589168640, ("DT", 1, 4, 7), "MBwhDst4sec07"))
reports[-1].posNum = 181264
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.000249548, 0.00577789, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.65976e-05, 8.98449e-05, 0), \
                           -420313, 181264, 181264, -nan)
reports[-1].sigmaresid = ValErr(2.45923, 0.0040844, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00345312, None, -0.000235083, None, 0.00024145, None, -0.000286441, None, 0.00024145, None, -0.000286441, None, 0.00117512, None, -0.000239557, None, 0.00117512, None, -0.000239557, None, 2.45923, None, 0.00777547, None, 2.45923, None, 0.00777547, None)

reports.append(Report(589430784, ("DT", 1, 4, 8), "MBwhDst4sec08"))
reports[-1].posNum = 154084
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.00161371, 0.00632184, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.99778e-06, 9.93301e-05, 0), \
                           -358671, 154084, 154084, -nan)
reports[-1].sigmaresid = ValErr(2.4814, 0.00446997, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0014359, None, -0.00368344, None, -0.0016185, None, -0.00373463, None, -0.0016185, None, -0.00373463, None, -0.000978822, None, -0.00382096, None, -0.000978822, None, -0.00382096, None, 2.4814, None, 0.00770003, None, 2.4814, None, 0.00770003, None)

reports.append(Report(589692928, ("DT", 1, 4, 9), "MBwhDst4sec09"))
reports[-1].posNum = 89288
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.00294466, 0.00782591, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.69438e-05, 0.00012277, 0), \
                           -202543, 89288, 89288, -nan)
reports[-1].sigmaresid = ValErr(2.33843, 0.00553367, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0118432, None, -0.000261169, None, 0.00293508, None, -0.000247139, None, 0.00293508, None, -0.000247139, None, 0.000338299, None, -0.000221066, None, 0.000338299, None, -0.000221066, None, 2.33843, None, 0.00705974, None, 2.33843, None, 0.00705974, None)

reports.append(Report(589955072, ("DT", 1, 4, 10), "MBwhDst4sec10"))
reports[-1].posNum = 94824
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.000357706, 0.00801636, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(7.17806e-05, 0.000125857, 0), \
                           -220214, 94824, 94824, -nan)
reports[-1].sigmaresid = ValErr(2.468, 0.00566697, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00505442, None, -0.000319567, None, 0.000272263, None, -0.000351258, None, 0.000272263, None, -0.000351258, None, 0.0030252, None, -0.000454562, None, 0.0030252, None, -0.000454562, None, 2.468, None, 0.0078653, None, 2.468, None, 0.0078653, None)

reports.append(Report(591003648, ("DT", 1, 4, 14), "MBwhDst4sec14"))
reports[-1].posNum = 98402
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.000527616, 0.00808211, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000132791, 0.000131447, 0), \
                           -231043, 98402, 98402, -nan)
reports[-1].sigmaresid = ValErr(2.53199, 0.00570749, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00450047, None, 0.000509671, None, 0.000114636, None, 0.000489862, None, 0.000114636, None, 0.000489862, None, 0.00287173, None, 0.00052154, None, 0.00287173, None, 0.00052154, None, 2.53201, None, 0.00786149, None, 2.53201, None, 0.00786149, None)

reports.append(Report(590217216, ("DT", 1, 4, 11), "MBwhDst4sec11"))
reports[-1].posNum = 91140
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.0065566, 0.00770102, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.38097e-05, 0.000119976, 0), \
                           -206184, 91140, 91140, -nan)
reports[-1].sigmaresid = ValErr(2.32411, 0.00544363, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.013132, None, -0.00121029, None, 0.00646754, None, -0.00122581, None, 0.00646754, None, -0.00122581, None, 0.00594917, None, -0.00122484, None, 0.00594917, None, -0.00122484, None, 2.32411, None, 0.0069679, None, 2.32411, None, 0.0069679, None)

reports.append(Report(590479360, ("DT", 1, 4, 12), "MBwhDst4sec12"))
reports[-1].posNum = 181132
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.000306663, 0.00572541, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.16793e-05, 8.93669e-05, 0), \
                           -418244, 181132, 181132, -nan)
reports[-1].sigmaresid = ValErr(2.43542, 0.00404634, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00645008, None, 0.000127268, None, 0.000114856, None, 0.000172018, None, 0.000114856, None, 0.000172018, None, -0.00149276, None, 0.000211745, None, -0.00149276, None, 0.000211745, None, 2.43543, None, 0.00757891, None, 2.43543, None, 0.00757891, None)

reports.append(Report(587628544, ("DT", 2, 4, 1), "MBwhEst4sec01"))
reports[-1].posNum = 132072
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.00233628, 0.00729493, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.45991e-05, 0.000116802, 0), \
                           -315336, 132072, 132072, -nan)
reports[-1].sigmaresid = ValErr(2.63444, 0.00512588, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0106499, None, 7.29857e-05, None, 0.0025287, None, 8.47451e-05, None, 0.0025287, None, 8.47451e-05, None, 0.00606665, None, 2.32839e-05, None, 0.00606665, None, 2.32839e-05, None, 2.63444, None, 0.00802146, None, 2.63444, None, 0.00802146, None)

reports.append(Report(587890688, ("DT", 2, 4, 2), "MBwhEst4sec02"))
reports[-1].posNum = 102804
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.00270483, 0.0081082, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.15944e-05, 0.000128013, 0), \
                           -243607, 102804, 102804, -nan)
reports[-1].sigmaresid = ValErr(2.5875, 0.0057064, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00754249, None, 0.00153681, None, -0.00278093, None, 0.00157378, None, -0.00278093, None, 0.00157378, None, -0.00379122, None, 0.00159211, None, -0.00379122, None, 0.00159211, None, 2.58749, None, 0.007953, None, 2.58749, None, 0.007953, None)

reports.append(Report(588152832, ("DT", 2, 4, 3), "MBwhEst4sec03"))
reports[-1].posNum = 108340
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.000674894, 0.00779259, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000128058, 0.000125016, 0), \
                           -255133, 108340, 108340, -nan)
reports[-1].sigmaresid = ValErr(2.54974, 0.00547754, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000320429, None, 0.00153786, None, -0.00154072, None, 0.00158037, None, -0.00154072, None, 0.00158037, None, 0.00511996, None, 0.00155934, None, 0.00511996, None, 0.00155934, None, 2.54975, None, 0.00771834, None, 2.54975, None, 0.00771834, None)

reports.append(Report(588414976, ("DT", 2, 4, 4), "MBwhEst4sec04"))
reports[-1].posNum = 98094
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.000326837, 0.00858052, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.80878e-05, 0.000138192, 0), \
                           -235764, 98094, 98094, -nan)
reports[-1].sigmaresid = ValErr(2.67651, 0.00604276, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00384942, None, 0.00114646, None, -0.000535672, None, 0.00114077, None, -0.000535672, None, 0.00114077, None, -0.0148989, None, 0.0012451, None, -0.0148989, None, 0.0012451, None, 2.6765, None, 0.00811997, None, 2.6765, None, 0.00811997, None)

reports.append(Report(590774272, ("DT", 2, 4, 13), "MBwhEst4sec13"))
reports[-1].posNum = 90264
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.00138438, 0.00904036, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.32341e-05, 0.000149146, 0), \
                           -218237, 90264, 90264, -nan)
reports[-1].sigmaresid = ValErr(2.7151, 0.00639023, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00447728, None, -0.00129674, None, 0.00125722, None, -0.00132037, None, 0.00125722, None, -0.00132037, None, 0.00347909, None, -0.00136882, None, 0.00347909, None, -0.00136882, None, 2.71509, None, 0.00830356, None, 2.71509, None, 0.00830356, None)

reports.append(Report(588677120, ("DT", 2, 4, 5), "MBwhEst4sec05"))
reports[-1].posNum = 139036
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.000631109, 0.00699502, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.5055e-05, 0.00011309, 0), \
                           -329336, 139036, 139036, -nan)
reports[-1].sigmaresid = ValErr(2.58512, 0.00490235, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0045703, None, -0.000928167, None, 0.000973547, None, -0.000950734, None, 0.000973547, None, -0.000950734, None, 0.00537251, None, -0.000974429, None, 0.00537251, None, -0.000974429, None, 2.58512, None, 0.00794386, None, 2.58512, None, 0.00794386, None)

reports.append(Report(588939264, ("DT", 2, 4, 6), "MBwhEst4sec06"))
reports[-1].posNum = 148192
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.000339941, 0.0068606, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.88985e-05, 0.00011167, 0), \
                           -351992, 148192, 148192, -nan)
reports[-1].sigmaresid = ValErr(2.60206, 0.00477622, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00383924, None, -0.00175629, None, 0.000377617, None, -0.00181995, None, 0.000377617, None, -0.00181995, None, 0.00192131, None, -0.00193622, None, 0.00192131, None, -0.00193622, None, 2.60206, None, 0.00795701, None, 2.60206, None, 0.00795701, None)

reports.append(Report(589201408, ("DT", 2, 4, 7), "MBwhEst4sec07"))
reports[-1].posNum = 141346
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.00168788, 0.00698554, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.5761e-05, 0.000114578, 0), \
                           -336432, 141346, 141346, -nan)
reports[-1].sigmaresid = ValErr(2.615, 0.0049183, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000590344, None, -0.00117725, None, 0.00179796, None, -0.0012198, None, 0.00179796, None, -0.0012198, None, 0.00487562, None, -0.0012155, None, 0.00487562, None, -0.0012155, None, 2.615, None, 0.00802841, None, 2.615, None, 0.00802841, None)

reports.append(Report(589463552, ("DT", 2, 4, 8), "MBwhEst4sec08"))
reports[-1].posNum = 131770
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.000194246, 0.0071127, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000119164, 0.000120169, 0), \
                           -311900, 131770, 131770, -nan)
reports[-1].sigmaresid = ValErr(2.58071, 0.00502708, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00277106, None, 0.000103458, None, -0.000405941, None, 5.1299e-05, None, -0.000405941, None, 5.1299e-05, None, 0.00567095, None, 5.49347e-05, None, 0.00567095, None, 5.49347e-05, None, 2.58072, None, 0.00792641, None, 2.58072, None, 0.00792641, None)

reports.append(Report(589725696, ("DT", 2, 4, 9), "MBwhEst4sec09"))
reports[-1].posNum = 61170
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-4.49492e-05, 0.0103555, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000171615, 0.000164811, 0), \
                           -144180, 61170, 61170, -nan)
reports[-1].sigmaresid = ValErr(2.55511, 0.00730508, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00397918, None, -0.000641843, None, 0.000693947, None, -0.000665337, None, 0.000693947, None, -0.000665337, None, 0.017442, None, -0.000676292, None, 0.017442, None, -0.000676292, None, 2.55513, None, 0.00770486, None, 2.55513, None, 0.00770486, None)

reports.append(Report(589987840, ("DT", 2, 4, 10), "MBwhEst4sec10"))
reports[-1].posNum = 89766
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.00124929, 0.00881541, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.39965e-05, 0.000142545, 0), \
                           -213907, 89766, 89766, -nan)
reports[-1].sigmaresid = ValErr(2.62218, 0.006189, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00273182, None, 0.00113654, None, -0.00114564, None, 0.00111472, None, -0.00114564, None, 0.00111472, None, -0.0111242, None, 0.00112001, None, -0.0111242, None, 0.00112001, None, 2.62218, None, 0.00813131, None, 2.62218, None, 0.00813131, None)

reports.append(Report(591036416, ("DT", 2, 4, 14), "MBwhEst4sec14"))
reports[-1].posNum = 89822
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.0010405, 0.00882275, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000103645, 0.000145413, 0), \
                           -214640, 89822, 89822, -nan)
reports[-1].sigmaresid = ValErr(2.63974, 0.00622811, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00121771, None, 0.000991118, None, -0.000678105, None, 0.000982873, None, -0.000678105, None, 0.000982873, None, -0.00576487, None, 0.00102248, None, -0.00576487, None, 0.00102248, None, 2.63974, None, 0.0082479, None, 2.63974, None, 0.0082479, None)

reports.append(Report(590249984, ("DT", 2, 4, 11), "MBwhEst4sec11"))
reports[-1].posNum = 73124
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.00251223, 0.00931155, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(9.09073e-05, 0.000149923, 0), \
                           -170865, 73124, 73124, -nan)
reports[-1].sigmaresid = ValErr(2.50353, 0.00654637, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00364805, None, 0.0011383, None, 0.00311594, None, 0.00113094, None, 0.00311594, None, 0.00113094, None, -0.0158103, None, 0.00119212, None, -0.0158103, None, 0.00119212, None, 2.50354, None, 0.00752183, None, 2.50354, None, 0.00752183, None)

reports.append(Report(590512128, ("DT", 2, 4, 12), "MBwhEst4sec12"))
reports[-1].posNum = 136282
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.00266447, 0.00715351, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.07475e-05, 0.000114621, 0), \
                           -324862, 136282, 136282, -nan)
reports[-1].sigmaresid = ValErr(2.6243, 0.00502668, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00197934, None, 0.001417, None, 0.0030569, None, 0.00145138, None, 0.0030569, None, 0.00145138, None, -0.00102127, None, 0.00151488, None, -0.00102127, None, 0.00151488, None, 2.6243, None, 0.00801042, None, 2.6243, None, 0.00801042, None)

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

