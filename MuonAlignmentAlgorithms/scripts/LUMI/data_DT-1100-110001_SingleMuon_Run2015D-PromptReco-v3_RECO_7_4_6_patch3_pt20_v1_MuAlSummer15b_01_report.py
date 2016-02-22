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
reports[-1].posNum = 40823
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.0346603, 0.00546015, 0), \
                           ValErr(0.026955, 0.00776644, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000190597, 8.92036e-05, 0), \
                           -137103, 40823, 40823, -nan)
reports[-1].sigmax = ValErr(1.07399, 0.00375887, 0)
reports[-1].sigmay = ValErr(1.56709, 0.00548462, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0365043, 0.0248259, -0.000637591, -0.00431252, 0.0319926, 0.0278127, -0.000665836, -0.00363064, 0.0319926, 0.0278127, -0.000665836, -0.00363064, 0.0338788, 0.0267924, -0.000677171, -0.00374407, 0.0338788, 0.0267924, -0.000677171, -0.00374407, 1.07412, 1.567, 0.00528267, 0.0408889, 1.07412, 1.567, 0.00528267, 0.0408889)

reports.append(Report(575176704, ("DT", -2, 1, 2), "MBwhAst1sec02"))
reports[-1].posNum = 23524
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.0671651, 0.0075557, 0), \
                           ValErr(-0.0315716, 0.0100751, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000800936, 0.000118332, 0), \
                           -78839.9, 23524, 23524, -nan)
reports[-1].sigmax = ValErr(1.08157, 0.00498692, 0)
reports[-1].sigmay = ValErr(1.54523, 0.00712467, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0777545, -0.0258528, -0.000194142, -0.00138798, 0.08553, -0.0320343, -0.00022643, 0.000286924, 0.08553, -0.0320343, -0.00022643, 0.000286924, 0.0913334, -0.0328959, -0.000258383, 0.000278218, 0.0913334, -0.0328959, -0.000258383, 0.000278218, 1.08186, 1.54633, 0.00525537, 0.0397232, 1.08186, 1.54633, 0.00525537, 0.0397232)

reports.append(Report(575438848, ("DT", -2, 1, 3), "MBwhAst1sec03"))
reports[-1].posNum = 25708
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.0112007, 0.00707588, 0), \
                           ValErr(0.0943576, 0.00943486, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000275237, 0.000112853, 0), \
                           -84780.2, 25708, 25708, -nan)
reports[-1].sigmax = ValErr(1.0484, 0.00462392, 0)
reports[-1].sigmay = ValErr(1.51085, 0.0066635, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.021774, 0.0970991, 0.0012283, 0.000300754, 0.0177934, 0.095513, 0.00123136, 0.000615017, 0.0177934, 0.095513, 0.00123136, 0.000615017, 0.0164435, 0.0898458, 0.00119712, 0.000754461, 0.0164435, 0.0898458, 0.00119712, 0.000754461, 1.04835, 1.51109, 0.00514166, 0.0376082, 1.04835, 1.51109, 0.00514166, 0.0376082)

reports.append(Report(575700992, ("DT", -2, 1, 4), "MBwhAst1sec04"))
reports[-1].posNum = 30809
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.0230971, 0.00616725, 0), \
                           ValErr(-0.0744485, 0.00901385, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000197087, 9.8155e-05, 0), \
                           -103194, 30809, 30809, -nan)
reports[-1].sigmax = ValErr(1.06017, 0.00427094, 0)
reports[-1].sigmay = ValErr(1.57328, 0.00633802, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0298562, -0.0829033, 0.000229248, -0.00327969, -0.0205978, -0.0763563, 0.000237334, -0.00216454, -0.0205978, -0.0763563, 0.000237334, -0.00216454, -0.0145459, -0.0807215, 0.000205389, -0.0022338, -0.0145459, -0.0807215, 0.000205389, -0.0022338, 1.06024, 1.57327, 0.005224, 0.0418936, 1.06024, 1.57327, 0.005224, 0.0418936)

reports.append(Report(575963136, ("DT", -2, 1, 5), "MBwhAst1sec05"))
reports[-1].posNum = 27316
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.0196447, 0.00669191, 0), \
                           ValErr(0.0956626, 0.00936328, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.59046e-05, 0.000104577, 0), \
                           -91111.6, 27316, 27316, -nan)
reports[-1].sigmax = ValErr(1.06415, 0.00455284, 0)
reports[-1].sigmay = ValErr(1.5456, 0.00661261, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.014953, 0.111298, 0.000898334, -0.000849491, -0.0211434, 0.0960459, 0.000882998, -0.000285924, -0.0211434, 0.0960459, 0.000882998, -0.000285924, -0.0248532, 0.0912374, 0.000905217, -0.000127528, -0.0248532, 0.0912374, 0.000905217, -0.000127528, 1.06415, 1.54562, 0.00525697, 0.0397819, 1.06415, 1.54562, 0.00525697, 0.0397819)

reports.append(Report(576225280, ("DT", -2, 1, 6), "MBwhAst1sec06"))
reports[-1].posNum = 23881
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.0278719, 0.00779684, 0), \
                           ValErr(-0.0421354, 0.0101546, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00023759, 0.000125615, 0), \
                           -80294.2, 23881, 23881, -nan)
reports[-1].sigmax = ValErr(1.08386, 0.00495971, 0)
reports[-1].sigmay = ValErr(1.5587, 0.00713258, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0446322, -0.0370316, 0.000613081, -0.00115306, -0.0343132, -0.0443557, 0.0006344, -0.000673636, -0.0343132, -0.0443557, 0.0006344, -0.000673636, -0.0307043, -0.030412, 0.000624114, -0.000780538, -0.0307043, -0.030412, 0.000624114, -0.000780538, 1.08382, 1.55888, 0.00529367, 0.0375723, 1.08382, 1.55888, 0.00529367, 0.0375723)

reports.append(Report(576487424, ("DT", -2, 1, 7), "MBwhAst1sec07"))
reports[-1].posNum = 43228
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.0123168, 0.00539294, 0), \
                           ValErr(0.0197632, 0.00762617, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000512715, 9.08306e-05, 0), \
                           -146126, 43228, 43228, -nan)
reports[-1].sigmax = ValErr(1.08547, 0.0036929, 0)
reports[-1].sigmay = ValErr(1.58481, 0.00539163, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.020372, 0.0321759, -0.00310679, 0.000693957, -0.0199468, 0.0211082, -0.00312978, 0.00216954, -0.0199468, 0.0211082, -0.00312978, 0.00216954, -0.0254263, 0.0137044, -0.00312162, 0.00203218, -0.0254263, 0.0137044, -0.00312162, 0.00203218, 1.08629, 1.58419, 0.00533997, 0.0411066, 1.08629, 1.58419, 0.00533997, 0.0411066)

reports.append(Report(576749568, ("DT", -2, 1, 8), "MBwhAst1sec08"))
reports[-1].posNum = 36773
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.0723151, 0.00579745, 0), \
                           ValErr(0.0777745, 0.00810326, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000327357, 9.62546e-05, 0), \
                           -122760, 36773, 36773, -nan)
reports[-1].sigmax = ValErr(1.06424, 0.0039381, 0)
reports[-1].sigmay = ValErr(1.54989, 0.00573939, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0717177, 0.0834154, 0.00128097, 0.004921, -0.077638, 0.0797627, 0.00125896, 0.0074222, -0.077638, 0.0797627, 0.00125896, 0.0074222, -0.0823543, 0.0864248, 0.0012611, 0.00699597, -0.0823543, 0.0864248, 0.0012611, 0.00699597, 1.06434, 1.54999, 0.00533104, 0.0365591, 1.06434, 1.54999, 0.00533104, 0.0365591)

reports.append(Report(577011712, ("DT", -2, 1, 9), "MBwhAst1sec09"))
reports[-1].posNum = 20469
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.0164005, 0.00767529, 0), \
                           ValErr(0.040976, 0.0109536, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000345153, 0.000120807, 0), \
                           -68527.7, 20469, 20469, -nan)
reports[-1].sigmax = ValErr(1.06885, 0.00528266, 0)
reports[-1].sigmay = ValErr(1.55803, 0.00770037, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.011703, 0.0303384, 0.000918545, 0.00135829, 0.0214281, 0.0376088, 0.000927563, 0.00165076, 0.0214281, 0.0376088, 0.000927563, 0.00165076, 0.0260531, 0.05708, 0.000889989, 0.00124819, 0.0260531, 0.05708, 0.000889989, 0.00124819, 1.06901, 1.55811, 0.00523667, 0.039095, 1.06901, 1.55811, 0.00523667, 0.039095)

reports.append(Report(577273856, ("DT", -2, 1, 10), "MBwhAst1sec10"))
reports[-1].posNum = 21580
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.0630024, 0.00728488, 0), \
                           ValErr(-0.122836, 0.0107956, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000221092, 0.000117238, 0), \
                           -72630.8, 21580, 21580, -nan)
reports[-1].sigmax = ValErr(1.0695, 0.00514822, 0)
reports[-1].sigmay = ValErr(1.58501, 0.00762969, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.066023, -0.117414, 0.0007482, 0.00226591, 0.0634864, -0.123514, 0.00072827, 0.00289288, 0.0634864, -0.123514, 0.00072827, 0.00289288, 0.0758366, -0.121005, 0.000660114, 0.00280731, 0.0758366, -0.121005, 0.000660114, 0.00280731, 1.06948, 1.58517, 0.00529414, 0.0401617, 1.06948, 1.58517, 0.00529414, 0.0401617)

reports.append(Report(577536000, ("DT", -2, 1, 11), "MBwhAst1sec11"))
reports[-1].posNum = 22316
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.160024, 0.00724501, 0), \
                           ValErr(-0.0359627, 0.0105663, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000440857, 0.000117041, 0), \
                           -75061.6, 22316, 22316, -nan)
reports[-1].sigmax = ValErr(1.07382, 0.00509618, 0)
reports[-1].sigmay = ValErr(1.57535, 0.00750785, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.163567, -0.0268941, -0.000416346, -0.00221672, 0.157459, -0.0381525, -0.000441132, 0.000850609, 0.157459, -0.0381525, -0.000441132, 0.000850609, 0.154055, -0.0272339, -0.00048269, 0.000401841, 0.154055, -0.0272339, -0.00048269, 0.000401841, 1.07445, 1.57493, 0.00536518, 0.0405981, 1.07445, 1.57493, 0.00536518, 0.0405981)

reports.append(Report(577798144, ("DT", -2, 1, 12), "MBwhAst1sec12"))
reports[-1].posNum = 40434
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.086415, 0.00561975, 0), \
                           ValErr(0.0816405, 0.00778766, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000377763, 9.42819e-05, 0), \
                           -136206, 40434, 40434, -nan)
reports[-1].sigmax = ValErr(1.08593, 0.00381898, 0)
reports[-1].sigmay = ValErr(1.56563, 0.00550592, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0956324, 0.087635, -0.00107948, 0.00020566, 0.092644, 0.0810035, -0.00107695, -0.000218533, 0.092644, 0.0810035, -0.00107695, -0.000218533, 0.098771, 0.0802628, -0.00110063, -0.000337573, 0.098771, 0.0802628, -0.00110063, -0.000337573, 1.08591, 1.56598, 0.00529344, 0.0375659, 1.08591, 1.56598, 0.00529344, 0.0375659)

reports.append(Report(579108864, ("DT", -2, 2, 1), "MBwhAst2sec01"))
reports[-1].posNum = 59504
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.0650232, 0.00593637, 0), \
                           ValErr(0.0153664, 0.00767087, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000206682, 9.00374e-05, 0), \
                           -226934, 59504, 59504, -nan)
reports[-1].sigmax = ValErr(1.41825, 0.00411214, 0)
reports[-1].sigmay = ValErr(1.87097, 0.00542469, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0642748, 0.0199716, -0.00160894, -0.00136743, 0.0677753, 0.0156326, -0.001608, -0.00129738, 0.0677753, 0.0156326, -0.001608, -0.00129738, 0.0717969, 0.004179, -0.00165669, -0.0013065, 0.0717969, 0.004179, -0.00165669, -0.0013065, 1.41808, 1.87128, 0.00567847, 0.0237823, 1.41808, 1.87128, 0.00567847, 0.0237823)

reports.append(Report(579371008, ("DT", -2, 2, 2), "MBwhAst2sec02"))
reports[-1].posNum = 51299
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.0501013, 0.00641994, 0), \
                           ValErr(-0.0410832, 0.00820505, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000232471, 9.74929e-05, 0), \
                           -194043, 51299, 51299, -nan)
reports[-1].sigmax = ValErr(1.38715, 0.00433121, 0)
reports[-1].sigmay = ValErr(1.8542, 0.00578947, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.057221, -0.049434, -0.000828853, 0.0119538, 0.0546929, -0.0423937, -0.000824724, 0.0124891, 0.0546929, -0.0423937, -0.000824724, 0.0124891, 0.0489388, -0.0410266, -0.00083773, 0.0126052, 0.0489388, -0.0410266, -0.00083773, 0.0126052, 1.38702, 1.85448, 0.00554184, 0.025948, 1.38702, 1.85448, 0.00554184, 0.025948)

reports.append(Report(579633152, ("DT", -2, 2, 3), "MBwhAst2sec03"))
reports[-1].posNum = 48055
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.00446098, 0.00662185, 0), \
                           ValErr(0.176221, 0.0084177, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.00105799, 0.000101036, 0), \
                           -181401, 48055, 48055, -nan)
reports[-1].sigmax = ValErr(1.38372, 0.00446381, 0)
reports[-1].sigmay = ValErr(1.8445, 0.00595018, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0227761, 0.192261, 0.00147362, -8.23867e-05, 0.0254209, 0.178782, 0.00147146, -5.70971e-05, 0.0254209, 0.178782, 0.00147146, -5.70971e-05, 0.0254283, 0.164314, 0.00145999, -9.23707e-05, 0.0254283, 0.164314, 0.00145999, -9.23707e-05, 1.38385, 1.84644, 0.00553436, 0.0233782, 1.38385, 1.84644, 0.00553436, 0.0233782)

reports.append(Report(579895296, ("DT", -2, 2, 4), "MBwhAst2sec04"))
reports[-1].posNum = 56574
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.0121574, 0.00607644, 0), \
                           ValErr(0.0324924, 0.00788727, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.43771e-05, 9.34739e-05, 0), \
                           -215242, 56574, 56574, -nan)
reports[-1].sigmax = ValErr(1.40197, 0.00416802, 0)
reports[-1].sigmay = ValErr(1.87546, 0.00557568, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00785241, 0.0469657, 0.000929013, 0.00228627, 0.0131749, 0.032361, 0.00091005, 0.00218886, 0.0131749, 0.032361, 0.00091005, 0.00218886, 0.0124946, 0.0321065, 0.000909871, 0.00208378, 0.0124946, 0.0321065, 0.000909871, 0.00208378, 1.40194, 1.8755, 0.00562427, 0.024506, 1.40194, 1.8755, 0.00562427, 0.024506)

reports.append(Report(580157440, ("DT", -2, 2, 5), "MBwhAst2sec05"))
reports[-1].posNum = 50403
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.0447023, 0.00643439, 0), \
                           ValErr(-0.00780261, 0.00821553, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00027523, 9.91109e-05, 0), \
                           -190182, 50403, 50403, -nan)
reports[-1].sigmax = ValErr(1.38252, 0.00435451, 0)
reports[-1].sigmay = ValErr(1.84309, 0.00580513, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0497679, -0.00918303, 0.000222777, 0.00420667, -0.0498814, -0.00867288, 0.000255714, 0.00427823, -0.0498814, -0.00867288, 0.000255714, 0.00427823, -0.047372, -0.0209997, 0.000223649, 0.00419166, -0.047372, -0.0209997, 0.000223649, 0.00419166, 1.38265, 1.84306, 0.00551844, 0.0233938, 1.38265, 1.84306, 0.00551844, 0.0233938)

reports.append(Report(580419584, ("DT", -2, 2, 6), "MBwhAst2sec06"))
reports[-1].posNum = 45456
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.0512994, 0.00699288, 0), \
                           ValErr(0.0278053, 0.00886493, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00029121, 0.000107233, 0), \
                           -173437, 45456, 45456, -nan)
reports[-1].sigmax = ValErr(1.41191, 0.0046828, 0)
reports[-1].sigmay = ValErr(1.88264, 0.00624401, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0665846, 0.0344254, 0.000989944, 0.00302672, -0.0573986, 0.0256759, 0.000951585, 0.00294419, -0.0573986, 0.0256759, 0.000951585, 0.00294419, -0.0492572, 0.014691, 0.000925665, 0.00290697, -0.0492572, 0.014691, 0.000925665, 0.00290697, 1.41204, 1.88262, 0.00563473, 0.0231379, 1.41204, 1.88262, 0.00563473, 0.0231379)

reports.append(Report(580681728, ("DT", -2, 2, 7), "MBwhAst2sec07"))
reports[-1].posNum = 60640
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.0608101, 0.00583039, 0), \
                           ValErr(-0.0322009, 0.00763724, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000419736, 8.86288e-05, 0), \
                           -231489, 60640, 60640, -nan)
reports[-1].sigmax = ValErr(1.41617, 0.00406661, 0)
reports[-1].sigmay = ValErr(1.88061, 0.00540024, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0666972, -0.0345509, 2.12949e-05, 0.00172102, -0.0653544, -0.0325106, 3.62417e-05, 0.00161053, -0.0653544, -0.0325106, 3.62417e-05, 0.00161053, -0.0671688, -0.0411264, 4.00136e-06, 0.00149791, -0.0671688, -0.0411264, 4.00136e-06, 0.00149791, 1.41644, 1.88061, 0.00565989, 0.027277, 1.41644, 1.88061, 0.00565989, 0.027277)

reports.append(Report(580943872, ("DT", -2, 2, 8), "MBwhAst2sec08"))
reports[-1].posNum = 62307
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.128879, 0.00574275, 0), \
                           ValErr(0.126022, 0.00761819, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000155493, 8.80977e-05, 0), \
                           -238266, 62307, 62307, -nan)
reports[-1].sigmax = ValErr(1.40985, 0.00399418, 0)
reports[-1].sigmay = ValErr(1.9016, 0.00538739, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.13604, 0.11718, 0.00296453, 0.00683836, -0.130709, 0.126059, 0.00295083, 0.00642384, -0.130709, 0.126059, 0.00295083, 0.00642384, -0.128906, 0.122403, 0.00292606, 0.00639459, -0.128906, 0.122403, 0.00292606, 0.00639459, 1.40977, 1.90175, 0.00558783, 0.025169, 1.40977, 1.90175, 0.00558783, 0.025169)

reports.append(Report(581206016, ("DT", -2, 2, 9), "MBwhAst2sec09"))
reports[-1].posNum = 40833
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.0292522, 0.00729107, 0), \
                           ValErr(0.089003, 0.00913474, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000695234, 0.000107046, 0), \
                           -154717, 40833, 40833, -nan)
reports[-1].sigmax = ValErr(1.40617, 0.00492066, 0)
reports[-1].sigmay = ValErr(1.84091, 0.00644194, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0136743, 0.100626, 6.1712e-05, 0.00153699, 0.0151186, 0.0933525, 4.73189e-05, 0.0017737, 0.0151186, 0.0933525, 4.73189e-05, 0.0017737, 0.0141138, 0.0658609, 9.92665e-05, 0.00185851, 0.0141138, 0.0658609, 9.92665e-05, 0.00185851, 1.40669, 1.84118, 0.00559808, 0.0232924, 1.40669, 1.84118, 0.00559808, 0.0232924)

reports.append(Report(581468160, ("DT", -2, 2, 10), "MBwhAst2sec10"))
reports[-1].posNum = 37126
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.00589722, 0.00793651, 0), \
                           ValErr(-0.0845621, 0.00951222, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000610222, 0.000117604, 0), \
                           -140217, 37126, 37126, -nan)
reports[-1].sigmax = ValErr(1.39551, 0.00512127, 0)
reports[-1].sigmay = ValErr(1.83246, 0.00672483, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0144557, -0.0692511, 0.00161719, 0.00301372, 0.0227379, -0.0855433, 0.00157535, 0.00310735, 0.0227379, -0.0855433, 0.00157535, 0.00310735, 0.0184, -0.101571, 0.00158369, 0.00326603, 0.0184, -0.101571, 0.00158369, 0.00326603, 1.39569, 1.83289, 0.00555462, 0.0228652, 1.39569, 1.83289, 0.00555462, 0.0228652)

reports.append(Report(581730304, ("DT", -2, 2, 11), "MBwhAst2sec11"))
reports[-1].posNum = 35449
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.0623358, 0.00785072, 0), \
                           ValErr(0.0282811, 0.00970768, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00049328, 0.000117412, 0), \
                           -133328, 35449, 35449, -nan)
reports[-1].sigmax = ValErr(1.38234, 0.00519173, 0)
reports[-1].sigmay = ValErr(1.82115, 0.00683972, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0551124, 0.0250386, 8.23051e-05, 0.00809682, 0.0506546, 0.0248194, 8.05793e-05, 0.00858895, 0.0506546, 0.0248194, 8.05793e-05, 0.00858895, 0.0525984, 0.0282331, 5.61447e-05, 0.00877265, 0.0525984, 0.0282331, 5.61447e-05, 0.00877265, 1.38266, 1.82117, 0.0055248, 0.0253419, 1.38266, 1.82117, 0.0055248, 0.0253419)

reports.append(Report(581992448, ("DT", -2, 2, 12), "MBwhAst2sec12"))
reports[-1].posNum = 54637
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.0515928, 0.00607762, 0), \
                           ValErr(-0.0276241, 0.0079757, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000274094, 9.35524e-05, 0), \
                           -206536, 54637, 54637, -nan)
reports[-1].sigmax = ValErr(1.37722, 0.00416728, 0)
reports[-1].sigmay = ValErr(1.86303, 0.00563716, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0521879, -0.0322866, -0.000753216, 0.000909399, 0.0559607, -0.0267692, -0.000746119, 0.000973461, 0.0559607, -0.0267692, -0.000746119, 0.000973461, 0.059071, -0.0316861, -0.000756928, 0.000998376, 0.059071, -0.0316861, -0.000756928, 0.000998376, 1.37702, 1.86346, 0.00555124, 0.0247602, 1.37702, 1.86346, 0.00555124, 0.0247602)

reports.append(Report(583303168, ("DT", -2, 3, 1), "MBwhAst3sec01"))
reports[-1].posNum = 64347
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.122659, 0.00734952, 0), \
                           ValErr(-0.0689215, 0.00902684, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000115072, 9.74732e-05, 0), \
                           -275874, 64347, 64347, -nan)
reports[-1].sigmax = ValErr(1.86071, 0.00518699, 0)
reports[-1].sigmay = ValErr(2.28976, 0.00638299, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.115868, -0.0674093, -0.0010474, 0.000355508, 0.123199, -0.0688489, -0.00103425, 0.000135129, 0.123199, -0.0688489, -0.00103425, 0.000135129, 0.121094, -0.0713182, -0.00106601, 0.000176629, 0.121094, -0.0713182, -0.00106601, 0.000176629, 1.86066, 2.28984, 0.00648294, 0.0197589, 1.86066, 2.28984, 0.00648294, 0.0197589)

reports.append(Report(583565312, ("DT", -2, 3, 2), "MBwhAst3sec02"))
reports[-1].posNum = 56116
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.00892561, 0.00771894, 0), \
                           ValErr(-0.119262, 0.00963141, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000340282, 0.000104177, 0), \
                           -239287, 56116, 56116, -nan)
reports[-1].sigmax = ValErr(1.82681, 0.005453, 0)
reports[-1].sigmay = ValErr(2.27893, 0.00680258, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0127575, -0.117744, -0.000482492, -0.00127778, -0.00783586, -0.120772, -0.000485228, -0.00101784, -0.00783586, -0.120772, -0.000485228, -0.00101784, -0.00489611, -0.123114, -0.000530815, -0.000871627, -0.00489611, -0.123114, -0.000530815, -0.000871627, 1.82692, 2.279, 0.00641987, 0.02012, 1.82692, 2.279, 0.00641987, 0.02012)

reports.append(Report(583827456, ("DT", -2, 3, 3), "MBwhAst3sec03"))
reports[-1].posNum = 55163
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.0438701, 0.0077415, 0), \
                           ValErr(-0.00386635, 0.00963174, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000403207, 0.000104145, 0), \
                           -234447, 55163, 55163, -nan)
reports[-1].sigmax = ValErr(1.81458, 0.00546308, 0)
reports[-1].sigmay = ValErr(2.26219, 0.00681064, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0413182, -0.00212829, 0.00117337, -0.00056513, 0.0457675, -0.00383261, 0.00116282, -0.000495414, 0.0457675, -0.00383261, 0.00116282, -0.000495414, 0.0509041, 0.000182579, 0.00115403, -0.000377009, 0.0509041, 0.000182579, 0.00115403, -0.000377009, 1.81473, 2.26232, 0.00640653, 0.019636, 1.81473, 2.26232, 0.00640653, 0.019636)

reports.append(Report(584089600, ("DT", -2, 3, 4), "MBwhAst3sec04"))
reports[-1].posNum = 61142
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.0350319, 0.00740004, 0), \
                           ValErr(0.0760697, 0.00927576, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000658127, 9.96842e-05, 0), \
                           -261115, 61142, 61142, -nan)
reports[-1].sigmax = ValErr(1.82721, 0.00522521, 0)
reports[-1].sigmay = ValErr(2.29325, 0.00655795, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0302809, 0.0726918, 0.000847063, -0.00114094, 0.0376311, 0.0749939, 0.000847085, -0.00103331, 0.0376311, 0.0749939, 0.000847085, -0.00103331, 0.0413414, 0.0620804, 0.000827347, -0.00091864, 0.0413414, 0.0620804, 0.000827347, -0.00091864, 1.82743, 2.2938, 0.00640938, 0.0196726, 1.82743, 2.2938, 0.00640938, 0.0196726)

reports.append(Report(584351744, ("DT", -2, 3, 5), "MBwhAst3sec05"))
reports[-1].posNum = 57448
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.00910798, 0.00768657, 0), \
                           ValErr(-0.0824277, 0.00955685, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000250286, 0.000104198, 0), \
                           -245585, 57448, 57448, -nan)
reports[-1].sigmax = ValErr(1.83988, 0.00542796, 0)
reports[-1].sigmay = ValErr(2.28721, 0.0067477, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00557858, -0.084401, 0.00101126, -0.00203592, 0.00815295, -0.0811785, 0.00104312, -0.00185863, 0.00815295, -0.0811785, 0.00104312, -0.00185863, 0.0149793, -0.0939339, 0.00102594, -0.00174687, 0.0149793, -0.0939339, 0.00102594, -0.00174687, 1.83989, 2.28731, 0.00637311, 0.0193138, 1.83989, 2.28731, 0.00637311, 0.0193138)

reports.append(Report(584613888, ("DT", -2, 3, 6), "MBwhAst3sec06"))
reports[-1].posNum = 53295
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.0985061, 0.00803497, 0), \
                           ValErr(-0.0346834, 0.0101449, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000755854, 0.000109094, 0), \
                           -229225, 53295, 53295, -nan)
reports[-1].sigmax = ValErr(1.85347, 0.00567734, 0)
reports[-1].sigmay = ValErr(2.33056, 0.00713869, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.100402, -0.0215126, 0.00110399, 0.000886494, -0.0962893, -0.0277417, 0.00108923, 0.000776048, -0.0962893, -0.0277417, 0.00108923, 0.000776048, -0.0936549, -0.0355984, 0.00111077, 0.000970386, -0.0936549, -0.0355984, 0.00111077, 0.000970386, 1.85348, 2.33161, 0.00650433, 0.0201493, 1.85348, 2.33161, 0.00650433, 0.0201493)

reports.append(Report(584876032, ("DT", -2, 3, 7), "MBwhAst3sec07"))
reports[-1].posNum = 63043
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.0633389, 0.00740143, 0), \
                           ValErr(-0.0362806, 0.00920761, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000124276, 9.89645e-05, 0), \
                           -270719, 63043, 63043, -nan)
reports[-1].sigmax = ValErr(1.85599, 0.0052273, 0)
reports[-1].sigmay = ValErr(2.31149, 0.0065101, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.063552, -0.0422765, -0.00187415, -4.21764e-05, -0.0628651, -0.0360639, -0.00186657, 0.00018358, -0.0628651, -0.0360639, -0.00186657, 0.00018358, -0.0711622, -0.0415097, -0.0018502, 0.000183943, -0.0711622, -0.0415097, -0.0018502, 0.000183943, 1.85592, 2.31161, 0.00645382, 0.01995, 1.85592, 2.31161, 0.00645382, 0.01995)

reports.append(Report(585138176, ("DT", -2, 3, 8), "MBwhAst3sec08"))
reports[-1].posNum = 53991
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.042172, 0.00807169, 0), \
                           ValErr(0.0277233, 0.00983899, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(7.34572e-05, 0.000106304, 0), \
                           -231610, 53991, 53991, -nan)
reports[-1].sigmax = ValErr(1.86998, 0.00569069, 0)
reports[-1].sigmay = ValErr(2.28414, 0.00695108, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.039627, 0.0224905, 0.00128714, -0.0013027, -0.0417434, 0.0280105, 0.00130488, -0.00147932, -0.0417434, 0.0280105, 0.00130488, -0.00147932, -0.0462201, 0.0238105, 0.00133404, -0.00130609, -0.0462201, 0.0238105, 0.00133404, -0.00130609, 1.87, 2.28412, 0.00651124, 0.0202644, 1.87, 2.28412, 0.00651124, 0.0202644)

reports.append(Report(585400320, ("DT", -2, 3, 9), "MBwhAst3sec09"))
reports[-1].posNum = 47702
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.0133884, 0.0084618, 0), \
                           ValErr(0.108375, 0.0104181, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000362911, 0.000111937, 0), \
                           -203752, 47702, 47702, -nan)
reports[-1].sigmax = ValErr(1.84291, 0.00596654, 0)
reports[-1].sigmay = ValErr(2.27534, 0.00736656, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0117869, 0.114962, 0.000393242, 0.00465468, 0.0113332, 0.10815, 0.000399142, 0.00472455, 0.0113332, 0.10815, 0.000399142, 0.00472455, 0.000991926, 0.0945383, 0.000408655, 0.00488925, 0.000991926, 0.0945383, 0.000408655, 0.00488925, 1.84296, 2.27552, 0.00642693, 0.0199982, 1.84296, 2.27552, 0.00642693, 0.0199982)

reports.append(Report(585662464, ("DT", -2, 3, 10), "MBwhAst3sec10"))
reports[-1].posNum = 49397
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.103471, 0.00828285, 0), \
                           ValErr(-0.055165, 0.0102863, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000143174, 0.000112678, 0), \
                           -210851, 49397, 49397, -nan)
reports[-1].sigmax = ValErr(1.83178, 0.00582784, 0)
reports[-1].sigmay = ValErr(2.28264, 0.00726226, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.10611, -0.0456479, -0.0011163, -0.000947781, -0.102421, -0.0558841, -0.00108863, -0.00114169, -0.102421, -0.0558841, -0.00108863, -0.00114169, -0.0988024, -0.0561323, -0.00110584, -0.0010439, -0.0988024, -0.0561323, -0.00110584, -0.0010439, 1.83178, 2.28268, 0.00642648, 0.0211167, 1.83178, 2.28268, 0.00642648, 0.0211167)

reports.append(Report(585924608, ("DT", -2, 3, 11), "MBwhAst3sec11"))
reports[-1].posNum = 48616
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.0768231, 0.00837945, 0), \
                           ValErr(0.0543685, 0.010279, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000403837, 0.00011271, 0), \
                           -207445, 48616, 48616, -nan)
reports[-1].sigmax = ValErr(1.84217, 0.00590802, 0)
reports[-1].sigmay = ValErr(2.26641, 0.00726856, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0743655, 0.0544917, -0.000960001, 0.000121869, 0.079117, 0.0542347, -0.00101141, -3.81063e-05, 0.079117, 0.0542347, -0.00101141, -3.81063e-05, 0.0820665, 0.0525583, -0.00101164, 6.68582e-05, 0.0820665, 0.0525583, -0.00101164, 6.68582e-05, 1.84208, 2.26681, 0.00645692, 0.0207264, 1.84208, 2.26681, 0.00645692, 0.0207264)

reports.append(Report(586186752, ("DT", -2, 3, 12), "MBwhAst3sec12"))
reports[-1].posNum = 61784
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.0833812, 0.00734022, 0), \
                           ValErr(-0.0494821, 0.00919264, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.08433e-05, 9.92831e-05, 0), \
                           -263454, 61784, 61784, -nan)
reports[-1].sigmax = ValErr(1.82203, 0.00518359, 0)
reports[-1].sigmay = ValErr(2.28482, 0.00650012, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.08747, -0.0403319, -0.000251447, 0.00110791, 0.0832227, -0.049437, -0.000255542, 0.00120361, 0.0832227, -0.049437, -0.000255542, 0.00120361, 0.0722819, -0.0568084, -0.000249027, 0.00140566, 0.0722819, -0.0568084, -0.000249027, 0.00140566, 1.82206, 2.28479, 0.00637487, 0.0202199, 1.82206, 2.28479, 0.00637487, 0.0202199)

reports.append(Report(574947328, ("DT", -1, 1, 1), "MBwhBst1sec01"))
reports[-1].posNum = 79275
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.0525382, 0.00344526, 0), \
                           ValErr(-0.0292399, 0.00378885, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000155161, 5.41367e-05, 0), \
                           -226968, 79275, 79275, -nan)
reports[-1].sigmax = ValErr(0.961863, 0.00241625, 0)
reports[-1].sigmay = ValErr(1.06614, 0.00267727, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0470729, -0.0274475, -9.62007e-05, 3.99625e-05, 0.0512767, -0.0289793, -8.52731e-05, -0.000391712, 0.0512767, -0.0289793, -8.52731e-05, -0.000391712, 0.0545591, -0.0274502, -0.000129566, -0.000520247, 0.0545591, -0.0274502, -0.000129566, -0.000520247, 0.961868, 1.0662, 0.00479741, 0.0149291, 0.961868, 1.0662, 0.00479741, 0.0149291)

reports.append(Report(575209472, ("DT", -1, 1, 2), "MBwhBst1sec02"))
reports[-1].posNum = 71215
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.0218665, 0.00360828, 0), \
                           ValErr(-0.0496181, 0.00399528, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000120911, 5.69004e-05, 0), \
                           -203409, 71215, 71215, -nan)
reports[-1].sigmax = ValErr(0.958235, 0.00253913, 0)
reports[-1].sigmay = ValErr(1.06295, 0.00281657, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0236197, -0.0511378, -0.000760285, -0.00277245, 0.0226212, -0.05028, -0.00075254, -0.00314676, 0.0226212, -0.05028, -0.00075254, -0.00314676, 0.0252485, -0.0534344, -0.000808359, -0.00313288, 0.0252485, -0.0534344, -0.000808359, -0.00313288, 0.958213, 1.06301, 0.00487616, 0.0148379, 0.958213, 1.06301, 0.00487616, 0.0148379)

reports.append(Report(575471616, ("DT", -1, 1, 3), "MBwhBst1sec03"))
reports[-1].posNum = 60669
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.00640768, 0.00390155, 0), \
                           ValErr(0.0488788, 0.0043969, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.89764e-07, 7.13238e-05, 0), \
                           -174388, 60669, 60669, -nan)
reports[-1].sigmax = ValErr(0.958322, 0.00275116, 0)
reports[-1].sigmay = ValErr(1.08232, 0.00310713, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00483802, 0.0464307, 0.000431496, -0.000133667, -0.00640752, 0.0488784, 0.000445386, -0.000491618, -0.00640752, 0.0488784, 0.000445386, -0.000491618, -0.00564216, 0.0454422, 0.000400842, -0.000501669, -0.00564216, 0.0454422, 0.000400842, -0.000501669, 0.958322, 1.08232, 0.00482255, 0.0148152, 0.958322, 1.08232, 0.00482255, 0.0148152)

reports.append(Report(575733760, ("DT", -1, 1, 4), "MBwhBst1sec04"))
reports[-1].posNum = 76593
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.0177654, 0.00346245, 0), \
                           ValErr(0.0366013, 0.00388624, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000259955, 5.48902e-05, 0), \
                           -218837, 76593, 76593, -nan)
reports[-1].sigmax = ValErr(0.954861, 0.00243985, 0)
reports[-1].sigmay = ValErr(1.06764, 0.00272699, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0192033, 0.0395089, 0.000870238, -0.0013639, -0.019152, 0.0388096, 0.000883791, -0.00164757, -0.019152, 0.0388096, 0.000883791, -0.00164757, -0.0144634, 0.0402451, 0.000784044, -0.00164133, -0.0144634, 0.0402451, 0.000784044, -0.00164133, 0.954834, 1.06783, 0.0049835, 0.0149026, 0.954834, 1.06783, 0.0049835, 0.0149026)

reports.append(Report(575995904, ("DT", -1, 1, 5), "MBwhBst1sec05"))
reports[-1].posNum = 74348
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.0500252, 0.00352957, 0), \
                           ValErr(-0.0130026, 0.0039203, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000126822, 5.47738e-05, 0), \
                           -212368, 74348, 74348, -nan)
reports[-1].sigmax = ValErr(0.956315, 0.00248006, 0)
reports[-1].sigmay = ValErr(1.06523, 0.00276251, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0489883, -0.0172553, 0.000712169, 0.000491282, -0.049107, -0.0137579, 0.000709249, 0.00011339, -0.049107, -0.0137579, 0.000709249, 0.00011339, -0.0485628, -0.0144687, 0.000710763, 5.05306e-05, -0.0485628, -0.0144687, 0.000710763, 5.05306e-05, 0.956296, 1.06529, 0.00481094, 0.0144609, 0.956296, 1.06529, 0.00481094, 0.0144609)

reports.append(Report(576258048, ("DT", -1, 1, 6), "MBwhBst1sec06"))
reports[-1].posNum = 70973
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.0660346, 0.00363999, 0), \
                           ValErr(-0.0232778, 0.00412015, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000123128, 5.95165e-05, 0), \
                           -205735, 70973, 70973, -nan)
reports[-1].sigmax = ValErr(0.969496, 0.00257332, 0)
reports[-1].sigmay = ValErr(1.09624, 0.00290971, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0695193, -0.0233374, 0.00150314, 0.00185045, -0.066197, -0.0228474, 0.00151567, 0.00156056, -0.066197, -0.0228474, 0.00151567, 0.00156056, -0.0673146, -0.0233973, 0.00150241, 0.00146153, -0.0673146, -0.0233973, 0.00150241, 0.00146153, 0.969546, 1.09621, 0.00493662, 0.0155602, 0.969546, 1.09621, 0.00493662, 0.0155602)

reports.append(Report(576520192, ("DT", -1, 1, 7), "MBwhBst1sec07"))
reports[-1].posNum = 90995
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.0310646, 0.003229, 0), \
                           ValErr(0.00938105, 0.00354407, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000104922, 5.09965e-05, 0), \
                           -261184, 90995, 90995, -nan)
reports[-1].sigmax = ValErr(0.966459, 0.00226615, 0)
reports[-1].sigmay = ValErr(1.06882, 0.00250611, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0293981, 0.0109937, -0.000630271, -0.00300584, -0.0318955, 0.00954242, -0.000634508, -0.00324573, -0.0318955, 0.00954242, -0.000634508, -0.00324573, -0.0286056, 0.00578975, -0.000669437, -0.00329191, -0.0286056, 0.00578975, -0.000669437, -0.00329191, 0.966582, 1.06871, 0.00484434, 0.0145475, 0.966582, 1.06871, 0.00484434, 0.0145475)

reports.append(Report(576782336, ("DT", -1, 1, 8), "MBwhBst1sec08"))
reports[-1].posNum = 84721
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.0418505, 0.00331608, 0), \
                           ValErr(-0.0294852, 0.00366051, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000127641, 5.21087e-05, 0), \
                           -242044, 84721, 84721, -nan)
reports[-1].sigmax = ValErr(0.959539, 0.00233106, 0)
reports[-1].sigmay = ValErr(1.06224, 0.00258055, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0446349, -0.0292787, 0.000889857, 0.000334523, -0.0427295, -0.0287888, 0.000894947, 2.722e-05, -0.0427295, -0.0287888, 0.000894947, 2.722e-05, -0.0401899, -0.0308959, 0.000876581, -1.39429e-05, -0.0401899, -0.0308959, 0.000876581, -1.39429e-05, 0.959563, 1.06225, 0.00480373, 0.0151778, 0.959563, 1.06225, 0.00480373, 0.0151778)

reports.append(Report(577044480, ("DT", -1, 1, 9), "MBwhBst1sec09"))
reports[-1].posNum = 62830
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.0142023, 0.00388989, 0), \
                           ValErr(0.00346832, 0.00430243, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.42494e-05, 5.94305e-05, 0), \
                           -180910, 62830, 62830, -nan)
reports[-1].sigmax = ValErr(0.968079, 0.00273094, 0)
reports[-1].sigmay = ValErr(1.07672, 0.00303743, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0138542, 0.00328986, 0.00127329, 0.000229029, 0.0147041, 0.00320607, 0.00128048, -0.000160753, 0.0147041, 0.00320607, 0.00128048, -0.000160753, 0.0191526, -0.00137913, 0.00125878, -0.000222376, 0.0191526, -0.00137913, 0.00125878, -0.000222376, 0.968084, 1.07673, 0.00482764, 0.0146987, 0.968084, 1.07673, 0.00482764, 0.0146987)

reports.append(Report(577306624, ("DT", -1, 1, 10), "MBwhBst1sec10"))
reports[-1].posNum = 76006
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.018857, 0.00347815, 0), \
                           ValErr(-0.0143557, 0.00383911, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.19986e-05, 5.56808e-05, 0), \
                           -216103, 76006, 76006, -nan)
reports[-1].sigmax = ValErr(0.95333, 0.00244546, 0)
reports[-1].sigmay = ValErr(1.05459, 0.00270518, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0176401, -0.0184142, 0.000149829, 0.000842097, 0.0183054, -0.0138755, 0.000167974, 0.000409248, 0.0183054, -0.0138755, 0.000167974, 0.000409248, 0.0234381, -0.0201433, 0.00011177, 0.000394683, 0.0234381, -0.0201433, 0.00011177, 0.000394683, 0.953395, 1.05453, 0.00486726, 0.0151436, 0.953395, 1.05453, 0.00486726, 0.0151436)

reports.append(Report(577568768, ("DT", -1, 1, 11), "MBwhBst1sec11"))
reports[-1].posNum = 70969
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.0294144, 0.00361498, 0), \
                           ValErr(-0.0309615, 0.00399933, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000222454, 5.62116e-05, 0), \
                           -202488, 70969, 70969, -nan)
reports[-1].sigmax = ValErr(0.955016, 0.00253512, 0)
reports[-1].sigmay = ValErr(1.06326, 0.00282243, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0312, -0.0338333, -0.000108039, 0.00210163, 0.0312588, -0.0319687, -0.000104024, 0.0018635, 0.0312588, -0.0319687, -0.000104024, 0.0018635, 0.0323394, -0.0382358, -0.00012639, 0.0018614, 0.0323394, -0.0382358, -0.00012639, 0.0018614, 0.954948, 1.06345, 0.00489277, 0.0146726, 0.954948, 1.06345, 0.00489277, 0.0146726)

reports.append(Report(577830912, ("DT", -1, 1, 12), "MBwhBst1sec12"))
reports[-1].posNum = 86624
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.0355805, 0.00329667, 0), \
                           ValErr(-0.00732972, 0.00364952, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000433809, 5.27339e-05, 0), \
                           -249187, 86624, 86624, -nan)
reports[-1].sigmax = ValErr(0.967803, 0.00232528, 0)
reports[-1].sigmay = ValErr(1.07412, 0.00258071, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0368172, -0.00685295, 2.86919e-05, -0.00127975, 0.0375158, -0.00736665, 2.60863e-05, -0.00170026, 0.0375158, -0.00736665, 2.60863e-05, -0.00170026, 0.0453187, -0.0076919, -5.60785e-05, -0.00167425, 0.0453187, -0.0076919, -5.60785e-05, -0.00167425, 0.967839, 1.0745, 0.00487513, 0.0148544, 0.967839, 1.0745, 0.00487513, 0.0148544)

reports.append(Report(579141632, ("DT", -1, 2, 1), "MBwhBst2sec01"))
reports[-1].posNum = 87638
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.0770548, 0.00433399, 0), \
                           ValErr(-0.030627, 0.00463632, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000307817, 5.86434e-05, 0), \
                           -298593, 87638, 87638, -nan)
reports[-1].sigmax = ValErr(1.28659, 0.00307078, 0)
reports[-1].sigmay = ValErr(1.37334, 0.0032629, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0792409, -0.0289616, -0.00120909, 0.00145192, 0.0780434, -0.0307904, -0.00119225, 0.00140136, 0.0780434, -0.0307904, -0.00119225, 0.00140136, 0.0818157, -0.0326456, -0.00121266, 0.00140704, 0.0818157, -0.0326456, -0.00121266, 0.00140704, 1.28643, 1.37372, 0.00510727, 0.0144173, 1.28643, 1.37372, 0.00510727, 0.0144173)

reports.append(Report(579403776, ("DT", -1, 2, 2), "MBwhBst2sec02"))
reports[-1].posNum = 80350
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.0593549, 0.0044818, 0), \
                           ValErr(-0.0440176, 0.00478117, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.0061e-05, 6.01435e-05, 0), \
                           -271410, 80350, 80350, -nan)
reports[-1].sigmax = ValErr(1.26831, 0.00316387, 0)
reports[-1].sigmay = ValErr(1.35295, 0.00337501, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0561169, -0.0408323, -0.00142326, 0.00138093, 0.0593109, -0.043974, -0.0014297, 0.00163463, 0.0593109, -0.043974, -0.0014297, 0.00163463, 0.0607604, -0.0450904, -0.00143562, 0.00168033, 0.0607604, -0.0450904, -0.00143562, 0.00168033, 1.26831, 1.35295, 0.00508859, 0.0143833, 1.26831, 1.35295, 0.00508859, 0.0143833)

reports.append(Report(579665920, ("DT", -1, 2, 3), "MBwhBst2sec03"))
reports[-1].posNum = 51475
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.0130855, 0.00564206, 0), \
                           ValErr(-0.00328676, 0.00611883, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000483585, 8.59982e-05, 0), \
                           -175550, 51475, 51475, -nan)
reports[-1].sigmax = ValErr(1.27941, 0.00398746, 0)
reports[-1].sigmay = ValErr(1.38557, 0.00431833, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0179376, -0.00419717, 0.000866301, 0.0046866, -0.0120579, -0.00115126, 0.000882959, 0.00443887, -0.0120579, -0.00115126, 0.000882959, 0.00443887, -0.0133816, 0.000733, 0.000870965, 0.004408, -0.0133816, 0.000733, 0.000870965, 0.004408, 1.27949, 1.38591, 0.00510639, 0.0147, 1.27949, 1.38591, 0.00510639, 0.0147)

reports.append(Report(579928064, ("DT", -1, 2, 4), "MBwhBst2sec04"))
reports[-1].posNum = 81835
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.0334987, 0.00447447, 0), \
                           ValErr(0.0422997, 0.0047825, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.57807e-05, 5.99139e-05, 0), \
                           -278552, 81835, 81835, -nan)
reports[-1].sigmax = ValErr(1.28426, 0.00314612, 0)
reports[-1].sigmay = ValErr(1.37131, 0.00337832, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0264826, 0.04538, -0.000240563, 0.00180992, -0.0335742, 0.0424274, -0.000258768, 0.00173402, -0.0335742, 0.0424274, -0.000258768, 0.00173402, -0.0234744, 0.0396119, -0.000326132, 0.00171715, -0.0234744, 0.0396119, -0.000326132, 0.00171715, 1.28427, 1.37129, 0.00518283, 0.0142349, 1.28427, 1.37129, 0.00518283, 0.0142349)

reports.append(Report(580190208, ("DT", -1, 2, 5), "MBwhBst2sec05"))
reports[-1].posNum = 81503
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.04625, 0.00442157, 0), \
                           ValErr(-0.0149351, 0.00474055, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000385015, 5.89047e-05, 0), \
                           -274891, 81503, 81503, -nan)
reports[-1].sigmax = ValErr(1.26233, 0.00311169, 0)
reports[-1].sigmay = ValErr(1.35248, 0.00334638, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0466795, -0.017153, 0.00217628, 0.0030359, -0.0467817, -0.0150601, 0.00218179, 0.00305585, -0.0467817, -0.0150601, 0.00218179, 0.00305585, -0.044847, -0.0202937, 0.00220388, 0.00306168, -0.044847, -0.0202937, 0.00220388, 0.00306168, 1.26241, 1.35273, 0.00506221, 0.0146887, 1.26241, 1.35273, 0.00506221, 0.0146887)

reports.append(Report(580452352, ("DT", -1, 2, 6), "MBwhBst2sec06"))
reports[-1].posNum = 73001
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.0478766, 0.00481648, 0), \
                           ValErr(0.0549981, 0.00512896, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000270514, 6.49929e-05, 0), \
                           -250090, 73001, 73001, -nan)
reports[-1].sigmax = ValErr(1.30126, 0.00340559, 0)
reports[-1].sigmay = ValErr(1.38352, 0.00362088, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0507626, 0.0471525, 0.000787269, 0.00364576, -0.0476473, 0.0562212, 0.000778862, 0.00359816, -0.0476473, 0.0562212, 0.000778862, 0.00359816, -0.0434724, 0.0532597, 0.000773903, 0.00357459, -0.0434724, 0.0532597, 0.000773903, 0.00357459, 1.30141, 1.38353, 0.00516324, 0.0150048, 1.30141, 1.38353, 0.00516324, 0.0150048)

reports.append(Report(580714496, ("DT", -1, 2, 7), "MBwhBst2sec07"))
reports[-1].posNum = 93874
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.0630776, 0.00420419, 0), \
                           ValErr(-0.00306285, 0.00448924, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000406508, 5.66304e-05, 0), \
                           -320014, 93874, 93874, -nan)
reports[-1].sigmax = ValErr(1.28715, 0.00297081, 0)
reports[-1].sigmay = ValErr(1.37529, 0.00317422, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.062561, -0.00292718, 0.000553789, 0.00225066, -0.0619049, -0.00355692, 0.00054707, 0.00223437, -0.0619049, -0.00355692, 0.00054707, 0.00223437, -0.0622859, -0.0125989, 0.000522008, 0.00225098, -0.0622859, -0.0125989, 0.000522008, 0.00225098, 1.28703, 1.37579, 0.00512207, 0.0141917, 1.28703, 1.37579, 0.00512207, 0.0141917)

reports.append(Report(580976640, ("DT", -1, 2, 8), "MBwhBst2sec08"))
reports[-1].posNum = 94802
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.0483284, 0.00413765, 0), \
                           ValErr(-0.0549716, 0.00438477, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000117257, 5.56594e-05, 0), \
                           -320879, 94802, 94802, -nan)
reports[-1].sigmax = ValErr(1.27707, 0.00292666, 0)
reports[-1].sigmay = ValErr(1.35294, 0.00309483, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0435874, -0.0538901, 0.000364851, 0.00159574, -0.0480214, -0.0550132, 0.00034966, 0.00154733, -0.0480214, -0.0550132, 0.00034966, 0.00154733, -0.0462831, -0.055147, 0.000339871, 0.00157399, -0.0462831, -0.055147, 0.000339871, 0.00157399, 1.27705, 1.353, 0.00516018, 0.0142205, 1.27705, 1.353, 0.00516018, 0.0142205)

reports.append(Report(581238784, ("DT", -1, 2, 9), "MBwhBst2sec09"))
reports[-1].posNum = 80550
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.0463609, 0.00452539, 0), \
                           ValErr(-0.00426569, 0.00476351, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.39538e-05, 6.00831e-05, 0), \
                           -272996, 80550, 80550, -nan)
reports[-1].sigmax = ValErr(1.28299, 0.00319296, 0)
reports[-1].sigmay = ValErr(1.35266, 0.00336683, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0420713, -0.00787712, 0.000950046, 0.0026433, 0.0465917, -0.00449347, 0.000946047, 0.00267615, 0.0465917, -0.00449347, 0.000946047, 0.00267615, 0.0440643, -0.00719785, 0.000940296, 0.0026711, 0.0440643, -0.00719785, 0.000940296, 0.0026711, 1.28296, 1.35271, 0.00519672, 0.0145154, 1.28296, 1.35271, 0.00519672, 0.0145154)

reports.append(Report(581500928, ("DT", -1, 2, 10), "MBwhBst2sec10"))
reports[-1].posNum = 78475
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.0289342, 0.00459884, 0), \
                           ValErr(0.00749034, 0.00486851, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000602203, 6.21163e-05, 0), \
                           -266879, 78475, 78475, -nan)
reports[-1].sigmax = ValErr(1.28766, 0.00325028, 0)
reports[-1].sigmay = ValErr(1.36358, 0.00344193, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0213489, 0.00681706, 0.00230828, 0.00161292, -0.0275413, 0.00658774, 0.0023309, 0.00157375, -0.0275413, 0.00658774, 0.0023309, 0.00157375, -0.0294358, 0.00263095, 0.0023527, 0.00162828, -0.0294358, 0.00263095, 0.0023527, 0.00162828, 1.28798, 1.36406, 0.0051509, 0.0142751, 1.28798, 1.36406, 0.0051509, 0.0142751)

reports.append(Report(581763072, ("DT", -1, 2, 11), "MBwhBst2sec11"))
reports[-1].posNum = 78431
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.0766433, 0.00453891, 0), \
                           ValErr(0.0546528, 0.00485865, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.74578e-05, 6.14116e-05, 0), \
                           -265472, 78431, 78431, -nan)
reports[-1].sigmax = ValErr(1.27076, 0.00320888, 0)
reports[-1].sigmay = ValErr(1.35974, 0.00343353, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0770561, 0.0600557, 0.00122353, 0.00318961, 0.07673, 0.0547936, 0.0012292, 0.00306763, 0.07673, 0.0547936, 0.0012292, 0.00306763, 0.0773093, 0.0471507, 0.00121893, 0.00309055, 0.0773093, 0.0471507, 0.00121893, 0.00309055, 1.27072, 1.35978, 0.00506993, 0.0143442, 1.27072, 1.35978, 0.00506993, 0.0143442)

reports.append(Report(582025216, ("DT", -1, 2, 12), "MBwhBst2sec12"))
reports[-1].posNum = 85940
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.0419686, 0.00439812, 0), \
                           ValErr(0.0670049, 0.00465233, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000226326, 5.93681e-05, 0), \
                           -292251, 85940, 85940, -nan)
reports[-1].sigmax = ValErr(1.28717, 0.00310497, 0)
reports[-1].sigmay = ValErr(1.36385, 0.00328991, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0411823, 0.0653206, -0.00132498, 0.00329305, 0.0429377, 0.0669578, -0.00133008, 0.00309801, 0.0429377, 0.0669578, -0.00133008, 0.00309801, 0.0430218, 0.0622676, -0.00132715, 0.00309667, 0.0430218, 0.0622676, -0.00132715, 0.00309667, 1.28707, 1.36407, 0.00520431, 0.0144195, 1.28707, 1.36407, 0.00520431, 0.0144195)

reports.append(Report(583335936, ("DT", -1, 3, 1), "MBwhBst3sec01"))
reports[-1].posNum = 76202
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.0524168, 0.00621042, 0), \
                           ValErr(-0.0146159, 0.00640034, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.77507e-05, 7.24883e-05, 0), \
                           -301508, 76202, 76202, -nan)
reports[-1].sigmax = ValErr(1.72206, 0.00436726, 0)
reports[-1].sigmay = ValErr(1.77767, 0.00457493, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0487301, -0.0104965, -0.00113568, 0.00489105, 0.0523599, -0.0148584, -0.00111754, 0.00506528, 0.0523599, -0.0148584, -0.00111754, 0.00506528, 0.0537658, -0.0165028, -0.00111724, 0.00506008, 0.0537658, -0.0165028, -0.00111724, 0.00506008, 1.72212, 1.77763, 0.0060761, 0.0135131, 1.72212, 1.77763, 0.0060761, 0.0135131)

reports.append(Report(583598080, ("DT", -1, 3, 2), "MBwhBst3sec02"))
reports[-1].posNum = 65353
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.0463123, 0.00665839, 0), \
                           ValErr(-0.013217, 0.0069412, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000639164, 7.74328e-05, 0), \
                           -257765, 65353, 65353, -nan)
reports[-1].sigmax = ValErr(1.70382, 0.00467562, 0)
reports[-1].sigmay = ValErr(1.77438, 0.00485713, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0427368, -0.0114592, -0.00125832, -0.000673506, 0.0452855, -0.0112423, -0.00121923, -0.000582408, 0.0452855, -0.0112423, -0.00121923, -0.000582408, 0.0435105, -0.0118092, -0.00122514, -0.000559079, 0.0435105, -0.0118092, -0.00122514, -0.000559079, 1.70414, 1.77494, 0.00595485, 0.0133003, 1.70414, 1.77494, 0.00595485, 0.0133003)

reports.append(Report(583860224, ("DT", -1, 3, 3), "MBwhBst3sec03"))
reports[-1].posNum = 49964
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.00412192, 0.00760849, 0), \
                           ValErr(0.124633, 0.00793672, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.20439e-05, 9.71969e-05, 0), \
                           -196828, 49964, 49964, -nan)
reports[-1].sigmax = ValErr(1.70063, 0.0053798, 0)
reports[-1].sigmay = ValErr(1.76917, 0.00559666, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00445231, 0.117078, -0.000462816, -0.00169084, 0.00413274, 0.124562, -0.000430942, -0.00151756, 0.00413274, 0.124562, -0.000430942, -0.00151756, 0.00124674, 0.123862, -0.000409725, -0.00144732, 0.00124674, 0.123862, -0.000409725, -0.00144732, 1.70063, 1.76917, 0.00599402, 0.0134563, 1.70063, 1.76917, 0.00599402, 0.0134563)

reports.append(Report(584122368, ("DT", -1, 3, 4), "MBwhBst3sec04"))
reports[-1].posNum = 71376
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.099415, 0.00637645, 0), \
                           ValErr(0.0532362, 0.00658467, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000589861, 7.50036e-05, 0), \
                           -282010, 71376, 71376, -nan)
reports[-1].sigmax = ValErr(1.71601, 0.00451998, 0)
reports[-1].sigmay = ValErr(1.77389, 0.00466188, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.100412, 0.0564255, 0.000705883, -0.00314151, -0.0998678, 0.0537172, 0.000723827, -0.00308811, -0.0998678, 0.0537172, 0.000723827, -0.00308811, -0.0963096, 0.0538976, 0.000727715, -0.00302141, -0.0963096, 0.0538976, 0.000727715, -0.00302141, 1.7164, 1.77424, 0.00602898, 0.0141532, 1.7164, 1.77424, 0.00602898, 0.0141532)

reports.append(Report(584384512, ("DT", -1, 3, 5), "MBwhBst3sec05"))
reports[-1].posNum = 69414
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.106631, 0.00640662, 0), \
                           ValErr(-0.103666, 0.00665046, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000143698, 7.70337e-05, 0), \
                           -271987, 69414, 69414, -nan)
reports[-1].sigmax = ValErr(1.68725, 0.00457433, 0)
reports[-1].sigmay = ValErr(1.74605, 0.0047586, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.107949, -0.105452, 0.000540535, 0.00035301, -0.106577, -0.103849, 0.000535825, 0.000476211, -0.106577, -0.103849, 0.000535825, 0.000476211, -0.106243, -0.106263, 0.000556954, 0.000520009, -0.106243, -0.106263, 0.000556954, 0.000520009, 1.68723, 1.74611, 0.00587616, 0.0131676, 1.68723, 1.74611, 0.00587616, 0.0131676)

reports.append(Report(584646656, ("DT", -1, 3, 6), "MBwhBst3sec06"))
reports[-1].posNum = 66632
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.0761726, 0.00673067, 0), \
                           ValErr(0.0571164, 0.00699143, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.31139e-05, 8.0684e-05, 0), \
                           -264772, 66632, 66632, -nan)
reports[-1].sigmax = ValErr(1.73714, 0.00475862, 0)
reports[-1].sigmay = ValErr(1.79234, 0.00490983, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0820341, 0.0507179, 0.00124326, 4.73309e-05, -0.0760676, 0.0563756, 0.00124542, 0.000182303, -0.0760676, 0.0563756, 0.00124542, 0.000182303, -0.0671445, 0.0483701, 0.00123332, 0.000202419, -0.0671445, 0.0483701, 0.00123332, 0.000202419, 1.73716, 1.79233, 0.00616233, 0.0133888, 1.73716, 1.79233, 0.00616233, 0.0133888)

reports.append(Report(584908800, ("DT", -1, 3, 7), "MBwhBst3sec07"))
reports[-1].posNum = 67579
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.0832014, 0.00665003, 0), \
                           ValErr(-0.00406111, 0.00696837, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000164061, 7.98155e-05, 0), \
                           -267772, 67579, 67579, -nan)
reports[-1].sigmax = ValErr(1.72873, 0.00470227, 0)
reports[-1].sigmay = ValErr(1.78086, 0.00484405, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0751408, -0.0054073, 0.000596604, 0.000639447, -0.0832365, -0.00668466, 0.000595696, 0.00077808, -0.0832365, -0.00668466, 0.000595696, 0.00077808, -0.0837502, -0.00539584, 0.000596269, 0.000788105, -0.0837502, -0.00539584, 0.000596269, 0.000788105, 1.72876, 1.78088, 0.00606734, 0.013408, 1.72876, 1.78088, 0.00606734, 0.013408)

reports.append(Report(585170944, ("DT", -1, 3, 8), "MBwhBst3sec08"))
reports[-1].posNum = 76489
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.0994141, 0.00618729, 0), \
                           ValErr(-0.0597684, 0.00637836, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000225938, 7.33638e-05, 0), \
                           -301533, 76489, 76489, -nan)
reports[-1].sigmax = ValErr(1.71117, 0.00437499, 0)
reports[-1].sigmay = ValErr(1.76319, 0.00450801, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0987295, -0.0528545, 0.00123251, -0.000284656, -0.0993183, -0.0591509, 0.00124722, -0.000189486, -0.0993183, -0.0591509, 0.00124722, -0.000189486, -0.108747, -0.0605786, 0.00127342, -0.000186085, -0.108747, -0.0605786, 0.00127342, -0.000186085, 1.71123, 1.76324, 0.00594326, 0.013501, 1.71123, 1.76324, 0.00594326, 0.013501)

reports.append(Report(585433088, ("DT", -1, 3, 9), "MBwhBst3sec09"))
reports[-1].posNum = 60475
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.0839342, 0.00723892, 0), \
                           ValErr(0.0161319, 0.00713034, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000103433, 8.21998e-05, 0), \
                           -238321, 60475, 60475, -nan)
reports[-1].sigmax = ValErr(1.71551, 0.00494205, 0)
reports[-1].sigmay = ValErr(1.75634, 0.0049733, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0898734, 0.0186301, 0.000178812, 0.00114854, -0.0836144, 0.015885, 0.000211559, 0.00123649, -0.0836144, 0.015885, 0.000211559, 0.00123649, -0.0833045, 0.0143712, 0.00021865, 0.00122763, -0.0833045, 0.0143712, 0.00021865, 0.00122763, 1.71554, 1.75633, 0.00598371, 0.0134854, 1.71554, 1.75633, 0.00598371, 0.0134854)

reports.append(Report(585695232, ("DT", -1, 3, 10), "MBwhBst3sec10"))
reports[-1].posNum = 23439
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.0901742, 0.0132825, 0), \
                           ValErr(0.0706452, 0.0110086, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000556734, 0.000147954, 0), \
                           -90965.7, 23439, 23439, -nan)
reports[-1].sigmax = ValErr(1.68611, 0.00778755, 0)
reports[-1].sigmay = ValErr(1.68313, 0.00777385, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.126663, 0.0723103, -0.00125631, -0.00143167, 0.118115, 0.0727887, -0.00119621, -0.00130689, 0.118115, 0.0727887, -0.00119621, -0.00130689, 0.107963, 0.0729878, -0.00115551, -0.00128434, 0.107963, 0.0729878, -0.00115551, -0.00128434, 1.6862, 1.68355, 0.00592186, 0.0130932, 1.6862, 1.68355, 0.00592186, 0.0130932)

reports.append(Report(585957376, ("DT", -1, 3, 11), "MBwhBst3sec11"))
reports[-1].posNum = 63285
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.141565, 0.00683194, 0), \
                           ValErr(0.0421781, 0.00705983, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.28764e-05, 8.05668e-05, 0), \
                           -250134, 63285, 63285, -nan)
reports[-1].sigmax = ValErr(1.71827, 0.00482986, 0)
reports[-1].sigmay = ValErr(1.77411, 0.00498678, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.139616, 0.0382612, -0.00212862, -0.00011933, 0.141634, 0.0419934, -0.00214037, -4.89456e-05, 0.141634, 0.0419934, -0.00214037, -4.89456e-05, 0.144027, 0.0342717, -0.00213171, 7.80461e-07, 0.144027, 0.0342717, -0.00213171, 7.80461e-07, 1.71829, 1.7741, 0.00601517, 0.0135772, 1.71829, 1.7741, 0.00601517, 0.0135772)

reports.append(Report(586219520, ("DT", -1, 3, 12), "MBwhBst3sec12"))
reports[-1].posNum = 57560
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.132393, 0.0071679, 0), \
                           ValErr(-0.0478139, 0.00743917, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000179629, 8.01167e-05, 0), \
                           -227678, 57560, 57560, -nan)
reports[-1].sigmax = ValErr(1.71956, 0.00506808, 0)
reports[-1].sigmay = ValErr(1.77811, 0.00524067, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.126051, -0.0562265, 0.00183701, 8.38703e-05, 0.132593, -0.0492581, 0.00183252, 0.000208994, 0.132593, -0.0492581, 0.00183252, 0.000208994, 0.136708, -0.0535822, 0.00182981, 0.000198628, 0.136708, -0.0535822, 0.00182981, 0.000198628, 1.71962, 1.77812, 0.00602772, 0.0133753, 1.71962, 1.77812, 0.00602772, 0.0133753)

reports.append(Report(574980096, ("DT", 0, 1, 1), "MBwhCst1sec01"))
reports[-1].posNum = 46264
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.00170447, 0.00423837, 0), \
                           ValErr(-0.0139057, 0.00408095, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000112371, 6.10126e-05, 0), \
                           -120650, 46264, 46264, -nan)
reports[-1].sigmax = ValErr(0.905597, 0.00297713, 0)
reports[-1].sigmay = ValErr(0.877334, 0.00288422, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00262737, -0.0168466, -0.000213058, -0.00109394, 0.00261162, -0.0136685, -0.000226428, -0.00104972, 0.00261162, -0.0136685, -0.000226428, -0.00104972, -0.00253055, -0.012423, -0.000186286, -0.00106958, -0.00253055, -0.012423, -0.000186286, -0.00106958, 0.90561, 0.877357, 0.00485516, 0.0109221, 0.90561, 0.877357, 0.00485516, 0.0109221)

reports.append(Report(576028672, ("DT", 0, 1, 5), "MBwhCst1sec05"))
reports[-1].posNum = 73931
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.0471812, 0.00332864, 0), \
                           ValErr(-0.0140531, 0.00320027, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000180427, 4.91987e-05, 0), \
                           -191913, 73931, 73931, -nan)
reports[-1].sigmax = ValErr(0.903054, 0.00234849, 0)
reports[-1].sigmay = ValErr(0.8693, 0.0022607, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0435532, -0.0154124, 0.00123631, 2.75962e-05, -0.0463678, -0.0145751, 0.0012436, 9.54539e-05, -0.0463678, -0.0145751, 0.0012436, 9.54539e-05, -0.0514261, -0.015019, 0.00132327, 7.76206e-05, -0.0514261, -0.015019, 0.00132327, 7.76206e-05, 0.903072, 0.869362, 0.00480769, 0.0106178, 0.903072, 0.869362, 0.00480769, 0.0106178)

reports.append(Report(577077248, ("DT", 0, 1, 9), "MBwhCst1sec09"))
reports[-1].posNum = 45033
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.0175199, 0.00429522, 0), \
                           ValErr(0.00306212, 0.00413917, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.95385e-05, 6.19056e-05, 0), \
                           -117598, 45033, 45033, -nan)
reports[-1].sigmax = ValErr(0.909629, 0.00303107, 0)
reports[-1].sigmay = ValErr(0.876533, 0.00292077, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0175545, -0.00161131, 0.00122404, -6.69173e-05, 0.0172112, 0.00336224, 0.00125003, -6.52031e-06, 0.0172112, 0.00336224, 0.00125003, -6.52031e-06, 0.022072, -0.00213578, 0.00122247, 7.26527e-05, 0.022072, -0.00213578, 0.00122247, 7.26527e-05, 0.909659, 0.876516, 0.00498559, 0.0107186, 0.909659, 0.876516, 0.00498559, 0.0107186)

reports.append(Report(575242240, ("DT", 0, 1, 2), "MBwhCst1sec02"))
reports[-1].posNum = 29893
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.0270667, 0.0053134, 0), \
                           ValErr(0.044975, 0.00506149, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000497884, 7.78613e-05, 0), \
                           -77635, 29893, 29893, -nan)
reports[-1].sigmax = ValErr(0.902158, 0.00368964, 0)
reports[-1].sigmay = ValErr(0.871256, 0.00356326, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0377266, 0.048929, 0.000878389, -0.00196958, 0.0334888, 0.0480109, 0.000907693, -0.00160385, 0.0334888, 0.0480109, 0.000907693, -0.00160385, 0.0401295, 0.0478865, 0.000860174, -0.00172211, 0.0401295, 0.0478865, 0.000860174, -0.00172211, 0.90253, 0.871497, 0.00480021, 0.0119431, 0.90253, 0.871497, 0.00480021, 0.0119431)

reports.append(Report(576290816, ("DT", 0, 1, 6), "MBwhCst1sec06"))
reports[-1].posNum = 63128
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.0710067, 0.0036492, 0), \
                           ValErr(0.0125145, 0.00353963, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.66435e-05, 5.3879e-05, 0), \
                           -166232, 63128, 63128, -nan)
reports[-1].sigmax = ValErr(0.916788, 0.00258044, 0)
reports[-1].sigmay = ValErr(0.888924, 0.00250196, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0700844, 0.0154305, -0.0025083, -0.000283345, 0.0710317, 0.0125882, -0.00253741, -0.000276554, 0.0710317, 0.0125882, -0.00253741, -0.000276554, 0.0773288, 0.0183172, -0.00261457, -0.000306606, 0.0773288, 0.0183172, -0.00261457, -0.000306606, 0.916759, 0.88895, 0.00496917, 0.0104079, 0.916759, 0.88895, 0.00496917, 0.0104079)

reports.append(Report(577339392, ("DT", 0, 1, 10), "MBwhCst1sec10"))
reports[-1].posNum = 43194
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.00337481, 0.00246715, 0), \
                           ValErr(0.0325768, 0.00418214, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000217956, 6.20895e-05, 0), \
                           -111800, 43194, 43194, -nan)
reports[-1].sigmax = ValErr(0.89622, 0.00304348, 0)
reports[-1].sigmay = ValErr(0.869374, 0.00295793, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00661075, 0.0331046, -0.00106853, -0.00124129, -0.00466291, 0.0333735, -0.00111929, -0.00118582, -0.00466291, 0.0333735, -0.00111929, -0.00118582, -0.00278801, 0.0347952, -0.00120227, -0.00116578, -0.00278801, 0.0347952, -0.00120227, -0.00116578, 0.896236, 0.869478, 0.00491454, 0.0110555, 0.896236, 0.869478, 0.00491454, 0.0110555)

reports.append(Report(575504384, ("DT", 0, 1, 3), "MBwhCst1sec03"))
reports[-1].posNum = 47207
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.0362834, 0.00417262, 0), \
                           ValErr(-0.00797785, 0.00406633, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.01282e-05, 6.2009e-05, 0), \
                           -122603, 47207, 47207, -nan)
reports[-1].sigmax = ValErr(0.899365, 0.00292699, 0)
reports[-1].sigmay = ValErr(0.874003, 0.00284442, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.037234, -0.0126143, -0.000901273, 0.000836326, 0.036368, -0.00787977, -0.000916769, 0.000917412, 0.036368, -0.00787977, -0.000916769, 0.000917412, 0.0394361, -0.00934438, -0.000944559, 0.00101066, 0.0394361, -0.00934438, -0.000944559, 0.00101066, 0.899364, 0.874003, 0.00482742, 0.0107707, 0.899364, 0.874003, 0.00482742, 0.0107707)

reports.append(Report(576552960, ("DT", 0, 1, 7), "MBwhCst1sec07"))
reports[-1].posNum = 64919
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.0819916, 0.00360475, 0), \
                           ValErr(0.00830158, 0.00347055, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000498018, 5.32819e-05, 0), \
                           -170299, 64919, 64919, -nan)
reports[-1].sigmax = ValErr(0.916301, 0.00254299, 0)
reports[-1].sigmay = ValErr(0.880543, 0.00244375, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0814123, 0.00374937, 0.0010754, 0.000126713, 0.0843012, 0.0053266, 0.00106624, 0.00014995, 0.0843012, 0.0053266, 0.00106624, 0.00014995, 0.0896689, 0.00465577, 0.000999314, 0.000223911, 0.0896689, 0.00465577, 0.000999314, 0.000223911, 0.916474, 0.88097, 0.00487811, 0.0112051, 0.916474, 0.88097, 0.00487811, 0.0112051)

reports.append(Report(577601536, ("DT", 0, 1, 11), "MBwhCst1sec11"))
reports[-1].posNum = 45348
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.00730128, 0.00426595, 0), \
                           ValErr(0.0149693, 0.00413907, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000499058, 6.31167e-05, 0), \
                           -117959, 45348, 45348, -nan)
reports[-1].sigmax = ValErr(0.903991, 0.00300174, 0)
reports[-1].sigmay = ValErr(0.873061, 0.00289902, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00221156, 0.00787004, 0.000649644, 7.41314e-05, 0.0039648, 0.0104683, 0.000634019, 0.000145807, 0.0039648, 0.0104683, 0.000634019, 0.000145807, 0.00550384, 0.00696684, 0.000595605, 0.000163168, 0.00550384, 0.00696684, 0.000595605, 0.000163168, 0.904276, 0.873385, 0.00483937, 0.0112173, 0.904276, 0.873385, 0.00483937, 0.0112173)

reports.append(Report(575766528, ("DT", 0, 1, 4), "MBwhCst1sec04"))
reports[-1].posNum = 58369
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.0155251, 0.00375221, 0), \
                           ValErr(0.0203443, 0.00363718, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000214906, 5.53241e-05, 0), \
                           -152238, 58369, 58369, -nan)
reports[-1].sigmax = ValErr(0.906034, 0.00265184, 0)
reports[-1].sigmay = ValErr(0.877227, 0.00256751, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0185956, 0.0179282, 0.00252643, -0.00185037, -0.0160008, 0.0195172, 0.00255862, -0.00183521, -0.0160008, 0.0195172, 0.00255862, -0.00183521, -0.0180396, 0.0192418, 0.00256445, -0.00182065, -0.0180396, 0.0192418, 0.00256445, -0.00182065, 0.90604, 0.877334, 0.00491489, 0.0100229, 0.90604, 0.877334, 0.00491489, 0.0100229)

reports.append(Report(576815104, ("DT", 0, 1, 8), "MBwhCst1sec08"))
reports[-1].posNum = 62319
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.0263218, 0.00362654, 0), \
                           ValErr(0.021729, 0.003504, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.93149e-05, 5.26399e-05, 0), \
                           -162118, 62319, 62319, -nan)
reports[-1].sigmax = ValErr(0.904636, 0.00256247, 0)
reports[-1].sigmay = ValErr(0.872647, 0.00247184, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0298472, 0.0239072, 0.000836759, 0.000402419, -0.0262695, 0.0218178, 0.000852912, 0.000383072, -0.0262695, 0.0218178, 0.000852912, 0.000383072, -0.0299436, 0.0218646, 0.000904109, 0.000405065, -0.0299436, 0.0218646, 0.000904109, 0.000405065, 0.904641, 0.87264, 0.00479203, 0.0109275, 0.904641, 0.87264, 0.00479203, 0.0109275)

reports.append(Report(577863680, ("DT", 0, 1, 12), "MBwhCst1sec12"))
reports[-1].posNum = 66682
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.036277, 0.00351028, 0), \
                           ValErr(0.0163134, 0.00340957, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000262858, 5.24482e-05, 0), \
                           -174157, 66682, 66682, -nan)
reports[-1].sigmax = ValErr(0.905928, 0.0024807, 0)
reports[-1].sigmay = ValErr(0.880445, 0.00241092, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0388872, 0.0133312, -0.000245058, 0.000550781, 0.0368769, 0.0162725, -0.000239295, 0.000628061, 0.0368769, 0.0162725, -0.000239295, 0.000628061, 0.0353661, 0.0210469, -0.000225798, 0.000591764, 0.0353661, 0.0210469, -0.000225798, 0.000591764, 0.906018, 0.880522, 0.00491465, 0.0106747, 0.906018, 0.880522, 0.00491465, 0.0106747)

reports.append(Report(579174400, ("DT", 0, 2, 1), "MBwhCst2sec01"))
reports[-1].posNum = 40846
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.0120669, 0.00252305, 0), \
                           ValErr(0.000404131, 0.00585774, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000764985, 7.6466e-05, 0), \
                           -131329, 40846, 40846, -nan)
reports[-1].sigmax = ValErr(1.23098, 0.00430647, 0)
reports[-1].sigmay = ValErr(1.18475, 0.00414935, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0277167, 0.00337547, -0.000636337, -0.00103339, 0.0124283, -0.00163188, -0.000653324, -0.001064, 0.0124283, -0.00163188, -0.000653324, -0.001064, 0.0181095, -0.00218245, -0.000715782, -0.00110674, 0.0181095, -0.00218245, -0.000715782, -0.00110674, 1.23169, 1.18552, 0.00524676, 0.0117011, 1.23169, 1.18552, 0.00524676, 0.0117011)

reports.append(Report(580222976, ("DT", 0, 2, 5), "MBwhCst2sec05"))
reports[-1].posNum = 67460
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.0741961, 0.00465011, 0), \
                           ValErr(-0.0284866, 0.00446463, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(9.07946e-05, 5.83691e-05, 0), \
                           -214147, 67460, 67460, -nan)
reports[-1].sigmax = ValErr(1.20772, 0.00328831, 0)
reports[-1].sigmay = ValErr(1.1593, 0.00315643, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0724521, -0.0295676, 0.000133778, -0.000159339, -0.0742659, -0.028645, 0.000123126, -0.000188294, -0.0742659, -0.028645, 0.000123126, -0.000188294, -0.07398, -0.0295817, 8.7295e-05, -0.000223133, -0.07398, -0.0295817, 8.7295e-05, -0.000223133, 1.20766, 1.15938, 0.00512317, 0.0112858, 1.20766, 1.15938, 0.00512317, 0.0112858)

reports.append(Report(581271552, ("DT", 0, 2, 9), "MBwhCst2sec09"))
reports[-1].posNum = 43582
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.0204339, 0.00589035, 0), \
                           ValErr(-0.0236094, 0.00560748, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000656691, 7.11274e-05, 0), \
                           -139060, 43582, 43582, -nan)
reports[-1].sigmax = ValErr(1.22941, 0.00416433, 0)
reports[-1].sigmay = ValErr(1.15761, 0.00392113, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0209084, -0.0182369, 0.00131615, -0.000765183, -0.0192809, -0.0159078, 0.00131662, -0.000678857, -0.0192809, -0.0159078, 0.00131662, -0.000678857, -0.0110002, -0.0153288, 0.00121021, -0.000707255, -0.0110002, -0.0153288, 0.00121021, -0.000707255, 1.23018, 1.15802, 0.00520044, 0.0118998, 1.23018, 1.15802, 0.00520044, 0.0118998)

reports.append(Report(579436544, ("DT", 0, 2, 2), "MBwhCst2sec02"))
reports[-1].posNum = 20344
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.0485029, 0.00939345, 0), \
                           ValErr(-0.0256411, 0.00892739, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000234029, 0.000106943, 0), \
                           -68579.2, 20344, 20344, -nan)
reports[-1].sigmax = ValErr(1.33881, 0.00663733, 0)
reports[-1].sigmay = ValErr(1.2729, 0.00631085, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0447265, -0.0195282, 0.00362463, 0.000703089, -0.0477544, -0.0261491, 0.00366642, 0.000717382, -0.0477544, -0.0261491, 0.00366642, 0.000717382, -0.0567051, -0.0243431, 0.00381462, 0.000640916, -0.0567051, -0.0243431, 0.00381462, 0.000640916, 1.33873, 1.27315, 0.00570817, 0.0111449, 1.33873, 1.27315, 0.00570817, 0.0111449)

reports.append(Report(580485120, ("DT", 0, 2, 6), "MBwhCst2sec06"))
reports[-1].posNum = 66326
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.0392861, 0.00480453, 0), \
                           ValErr(0.0336832, 0.0046446, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.65905e-05, 6.01126e-05, 0), \
                           -213983, 66326, 66326, -nan)
reports[-1].sigmax = ValErr(1.2364, 0.00339472, 0)
reports[-1].sigmay = ValErr(1.19263, 0.00327453, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0408594, 0.0395938, 0.00224706, 0.00227467, 0.0393684, 0.0338421, 0.0023051, 0.00223967, 0.0393684, 0.0338421, 0.0023051, 0.00223967, 0.041208, 0.0278505, 0.00230906, 0.00221961, 0.041208, 0.0278505, 0.00230906, 0.00221961, 1.2364, 1.19263, 0.00517816, 0.0114624, 1.2364, 1.19263, 0.00517816, 0.0114624)

reports.append(Report(581533696, ("DT", 0, 2, 10), "MBwhCst2sec10"))
reports[-1].posNum = 45559
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.00915936, 0.00572093, 0), \
                           ValErr(-0.0352231, 0.00547112, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000222811, 7.27146e-05, 0), \
                           -144987, 45559, 45559, -nan)
reports[-1].sigmax = ValErr(1.21254, 0.00401693, 0)
reports[-1].sigmay = ValErr(1.16393, 0.00385592, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0109679, -0.0319586, -0.000122503, 0.000962129, 0.0112346, -0.0338626, -0.000100098, 0.000927065, 0.0112346, -0.0338626, -0.000100098, 0.000927065, 0.00836443, -0.0321311, -5.13284e-05, 0.000902461, 0.00836443, -0.0321311, -5.13284e-05, 0.000902461, 1.21256, 1.16403, 0.00516807, 0.0117657, 1.21256, 1.16403, 0.00516807, 0.0117657)

reports.append(Report(579698688, ("DT", 0, 2, 3), "MBwhCst2sec03"))
reports[-1].posNum = 55379
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.0701713, 0.00523692, 0), \
                           ValErr(-0.0109074, 0.0050849, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.42928e-05, 6.66379e-05, 0), \
                           -178109, 55379, 55379, -nan)
reports[-1].sigmax = ValErr(1.23203, 0.003702, 0)
reports[-1].sigmay = ValErr(1.18487, 0.00356029, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0725279, -0.0173245, 0.00405823, 0.00155747, 0.0702744, -0.0114838, 0.00408702, 0.00156754, 0.0702744, -0.0114838, 0.00408702, 0.00156754, 0.0640161, -0.00917106, 0.00413886, 0.00158108, 0.0640161, -0.00917106, 0.00413886, 0.00158108, 1.23203, 1.18488, 0.0052388, 0.0118808, 1.23203, 1.18488, 0.0052388, 0.0118808)

reports.append(Report(580747264, ("DT", 0, 2, 7), "MBwhCst2sec07"))
reports[-1].posNum = 63638
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.0713834, 0.0049246, 0), \
                           ValErr(0.0105748, 0.00473752, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000334222, 6.12812e-05, 0), \
                           -205615, 63638, 63638, -nan)
reports[-1].sigmax = ValErr(1.24185, 0.00348096, 0)
reports[-1].sigmay = ValErr(1.19306, 0.00334422, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.068708, 0.0102627, 0.00204392, -0.000323706, 0.0721105, 0.012089, 0.00205829, -0.000413756, 0.0721105, 0.012089, 0.00205829, -0.000413756, 0.0707533, 0.0135484, 0.00212199, -0.000423541, 0.0707533, 0.0135484, 0.00212199, -0.000423541, 1.24188, 1.19331, 0.00524439, 0.0116683, 1.24188, 1.19331, 0.00524439, 0.0116683)

reports.append(Report(581795840, ("DT", 0, 2, 11), "MBwhCst2sec11"))
reports[-1].posNum = 43609
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.0459725, 0.00583446, 0), \
                           ValErr(-0.0176685, 0.00562364, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000135123, 7.27981e-05, 0), \
                           -138844, 43609, 43609, -nan)
reports[-1].sigmax = ValErr(1.21442, 0.00411217, 0)
reports[-1].sigmay = ValErr(1.16382, 0.00394081, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0474958, -0.0185998, -0.000156976, 0.000622132, 0.0450937, -0.0190654, -0.000157543, 0.000638532, 0.0450937, -0.0190654, -0.000157543, 0.000638532, 0.0460828, -0.0155469, -0.000149062, 0.000602661, 0.0460828, -0.0155469, -0.000149062, 0.000602661, 1.21446, 1.16381, 0.00512278, 0.0113992, 1.21446, 1.16381, 0.00512278, 0.0113992)

reports.append(Report(579960832, ("DT", 0, 2, 4), "MBwhCst2sec04"))
reports[-1].posNum = 57090
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.0246513, 0.00516283, 0), \
                           ValErr(-0.00332201, 0.0049043, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000179267, 6.42189e-05, 0), \
                           -182860, 57090, 57090, -nan)
reports[-1].sigmax = ValErr(1.22953, 0.00363869, 0)
reports[-1].sigmay = ValErr(1.17175, 0.0034677, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0292456, -0.00575476, -0.000130737, -0.00196199, -0.0258211, -0.00318666, -0.00015413, -0.00197327, -0.0258211, -0.00318666, -0.00015413, -0.00197327, -0.0190585, -0.00163393, -0.00018969, -0.00206944, -0.0190585, -0.00163393, -0.00018969, -0.00206944, 1.22956, 1.17181, 0.00525808, 0.0111639, 1.22956, 1.17181, 0.00525808, 0.0111639)

reports.append(Report(581009408, ("DT", 0, 2, 8), "MBwhCst2sec08"))
reports[-1].posNum = 66431
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.0587604, 0.004756, 0), \
                           ValErr(0.0762583, 0.0045705, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000438945, 5.88426e-05, 0), \
                           -212820, 66431, 66431, -nan)
reports[-1].sigmax = ValErr(1.22522, 0.00336152, 0)
reports[-1].sigmay = ValErr(1.1766, 0.00322808, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0657263, 0.0739756, 0.00100844, -1.40716e-05, -0.059867, 0.0745905, 0.000971162, -1.92423e-05, -0.059867, 0.0745905, 0.000971162, -1.92423e-05, -0.0616859, 0.0688944, 0.000912541, -8.2483e-06, -0.0616859, 0.0688944, 0.000912541, -8.2483e-06, 1.22518, 1.17713, 0.00516189, 0.0118121, 1.22518, 1.17713, 0.00516189, 0.0118121)

reports.append(Report(582057984, ("DT", 0, 2, 12), "MBwhCst2sec12"))
reports[-1].posNum = 58021
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.018013, 0.00504273, 0), \
                           ValErr(-0.0598023, 0.00486836, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.95913e-05, 6.27842e-05, 0), \
                           -185057, 58021, 58021, -nan)
reports[-1].sigmax = ValErr(1.21466, 0.00356577, 0)
reports[-1].sigmay = ValErr(1.17017, 0.00343516, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0192656, -0.0562524, -0.000134316, 0.000279364, -0.0179945, -0.0600521, -0.000132505, 0.000367881, -0.0179945, -0.0600521, -0.000132505, 0.000367881, -0.0156207, -0.0597314, -0.000160237, 0.000330686, -0.0156207, -0.0597314, -0.000160237, 0.000330686, 1.21464, 1.17019, 0.00514061, 0.011601, 1.21464, 1.17019, 0.00514061, 0.011601)

reports.append(Report(583368704, ("DT", 0, 3, 1), "MBwhCst3sec01"))
reports[-1].posNum = 39451
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.0222207, 0.0085324, 0), \
                           ValErr(0.00450658, 0.00812666, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000459484, 9.26609e-05, 0), \
                           -151534, 39451, 39451, -nan)
reports[-1].sigmax = ValErr(1.68944, 0.00601449, 0)
reports[-1].sigmay = ValErr(1.61414, 0.00574641, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.026628, 0.0140202, -0.001103, -0.00270312, -0.0255603, 0.00456181, -0.00110259, -0.00267782, -0.0255603, 0.00456181, -0.00110259, -0.00267782, -0.0199199, 0.00104373, -0.00108831, -0.00263829, -0.0199199, 0.00104373, -0.00108831, -0.00263829, 1.68956, 1.61452, 0.00609723, 0.0119193, 1.68956, 1.61452, 0.00609723, 0.0119193)

reports.append(Report(584417280, ("DT", 0, 3, 5), "MBwhCst3sec05"))
reports[-1].posNum = 58663
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.0685404, 0.00680307, 0), \
                           ValErr(0.0231255, 0.00654059, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.12241e-06, 7.6875e-05, 0), \
                           -222744, 58663, 58663, -nan)
reports[-1].sigmax = ValErr(1.64721, 0.00480896, 0)
reports[-1].sigmay = ValErr(1.58415, 0.00462487, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0681835, 0.0191855, 0.000851973, 0.00170943, -0.0685265, 0.0231181, 0.000872393, 0.0016804, -0.0685265, 0.0231181, 0.000872393, 0.0016804, -0.071064, 0.0193013, 0.000911076, 0.00171617, -0.071064, 0.0193013, 0.000911076, 0.00171617, 1.64722, 1.58415, 0.00591715, 0.0113936, 1.64722, 1.58415, 0.00591715, 0.0113936)

reports.append(Report(585465856, ("DT", 0, 3, 9), "MBwhCst3sec09"))
reports[-1].posNum = 38660
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.0136318, 0.00855058, 0), \
                           ValErr(-0.0396147, 0.00803402, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.63632e-05, 9.35282e-05, 0), \
                           -147447, 38660, 38660, -nan)
reports[-1].sigmax = ValErr(1.68119, 0.00604613, 0)
reports[-1].sigmay = ValErr(1.57863, 0.00567723, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0192887, -0.0420929, 0.000967263, 0.000609658, -0.0136055, -0.0397225, 0.000977596, 0.000501801, -0.0136055, -0.0397225, 0.000977596, 0.000501801, -0.0209547, -0.0481449, 0.00100292, 0.000483709, -0.0209547, -0.0481449, 0.00100292, 0.000483709, 1.68118, 1.57864, 0.0060105, 0.0110674, 1.68118, 1.57864, 0.0060105, 0.0110674)

reports.append(Report(583630848, ("DT", 0, 3, 2), "MBwhCst3sec02"))
reports[-1].posNum = 30935
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.112891, 0.00949006, 0), \
                           ValErr(-0.0225115, 0.00907822, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000250269, 0.000102816, 0), \
                           -118060, 30935, 30935, -nan)
reports[-1].sigmax = ValErr(1.66639, 0.00669938, 0)
reports[-1].sigmay = ValErr(1.59658, 0.00641875, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.106382, -0.0154606, 0.000956287, -0.000725371, 0.111562, -0.0227915, 0.000950747, -0.000724987, 0.111562, -0.0227915, 0.000950747, -0.000724987, 0.107574, -0.0202467, 0.000950154, -0.000723813, 0.107574, -0.0202467, 0.000950154, -0.000723813, 1.66643, 1.59669, 0.0059907, 0.0115596, 1.66643, 1.59669, 0.0059907, 0.0115596)

reports.append(Report(584679424, ("DT", 0, 3, 6), "MBwhCst3sec06"))
reports[-1].posNum = 53083
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.0890406, 0.00725845, 0), \
                           ValErr(0.0973948, 0.00694334, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000126376, 8.09587e-05, 0), \
                           -202845, 53083, 53083, -nan)
reports[-1].sigmax = ValErr(1.67131, 0.00512948, 0)
reports[-1].sigmay = ValErr(1.59967, 0.00490962, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0959477, 0.100063, -0.000122061, -0.000495208, 0.0886449, 0.0974955, -0.000106478, -0.000500928, 0.0886449, 0.0974955, -0.000106478, -0.000500928, 0.0926891, 0.101422, -0.000141401, -0.000464533, 0.0926891, 0.101422, -0.000141401, -0.000464533, 1.67127, 1.59976, 0.00593937, 0.0117327, 1.67127, 1.59976, 0.00593937, 0.0117327)

reports.append(Report(585728000, ("DT", 0, 3, 10), "MBwhCst3sec10"))
reports[-1].posNum = 38631
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.00509141, 0.00839148, 0), \
                           ValErr(-0.014397, 0.00804007, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000138539, 9.58799e-05, 0), \
                           -146383, 38631, 38631, -nan)
reports[-1].sigmax = ValErr(1.64179, 0.00590665, 0)
reports[-1].sigmay = ValErr(1.57712, 0.00567397, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00479811, -0.00896534, 0.000690647, -0.00284438, 0.00624862, -0.0151288, 0.000672353, -0.00283705, 0.00624862, -0.0151288, 0.000672353, -0.00283705, 0.00228515, -0.0177215, 0.000681044, -0.0028454, 0.00228515, -0.0177215, 0.000681044, -0.0028454, 1.64185, 1.5771, 0.00590975, 0.0118598, 1.64185, 1.5771, 0.00590975, 0.0118598)

reports.append(Report(583892992, ("DT", 0, 3, 3), "MBwhCst3sec03"))
reports[-1].posNum = 52622
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.00351746, 0.00711473, 0), \
                           ValErr(0.0275575, 0.00688966, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000417675, 7.54708e-05, 0), \
                           -199649, 52622, 52622, -nan)
reports[-1].sigmax = ValErr(1.64169, 0.00505113, 0)
reports[-1].sigmay = ValErr(1.58474, 0.00486724, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00492141, 0.0165129, 0.000612832, -0.00183591, 0.00375697, 0.0275184, 0.000619905, -0.0017875, 0.00375697, 0.0275184, 0.000619905, -0.0017875, 0.000619369, 0.0288045, 0.000580242, -0.00167197, 0.000619369, 0.0288045, 0.000580242, -0.00167197, 1.64186, 1.58497, 0.00590949, 0.0117572, 1.64186, 1.58497, 0.00590949, 0.0117572)

reports.append(Report(584941568, ("DT", 0, 3, 7), "MBwhCst3sec07"))
reports[-1].posNum = 22442
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.144359, 0.0132527, 0), \
                           ValErr(0.103193, 0.0108677, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000244731, 0.000143497, 0), \
                           -86284, 22442, 22442, -nan)
reports[-1].sigmax = ValErr(1.68406, 0.00794911, 0)
reports[-1].sigmay = ValErr(1.62528, 0.00767151, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.138068, 0.0950794, -0.00111294, -0.00376077, 0.132386, 0.102121, -0.00109509, -0.00373912, 0.132386, 0.102121, -0.00109509, -0.00373912, 0.131383, 0.102213, -0.00106175, -0.00383277, 0.131383, 0.102213, -0.00106175, -0.00383277, 1.68408, 1.62535, 0.00601549, 0.012366, 1.68408, 1.62535, 0.00601549, 0.012366)

reports.append(Report(585990144, ("DT", 0, 3, 11), "MBwhCst3sec11"))
reports[-1].posNum = 37680
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.0863582, 0.00845247, 0), \
                           ValErr(-0.0158187, 0.00816678, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000594184, 9.58024e-05, 0), \
                           -142896, 37680, 37680, -nan)
reports[-1].sigmax = ValErr(1.63943, 0.00597205, 0)
reports[-1].sigmay = ValErr(1.58428, 0.00577118, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0681693, -0.0146396, 5.45129e-05, 0.000695012, -0.0842656, -0.0140203, 3.97097e-05, 0.00069457, -0.0842656, -0.0140203, 3.97097e-05, 0.00069457, -0.0846146, -0.0144028, 2.32651e-05, 0.000733611, -0.0846146, -0.0144028, 2.32651e-05, 0.000733611, 1.63956, 1.58496, 0.00587678, 0.0117972, 1.63956, 1.58496, 0.00587678, 0.0117972)

reports.append(Report(584155136, ("DT", 0, 3, 4), "MBwhCst3sec04"))
reports[-1].posNum = 51121
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.00707948, 0.00738803, 0), \
                           ValErr(-0.0287827, 0.0070782, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000658227, 8.27471e-05, 0), \
                           -195153, 51121, 51121, -nan)
reports[-1].sigmax = ValErr(1.66976, 0.00522206, 0)
reports[-1].sigmay = ValErr(1.59507, 0.00498844, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00478158, -0.023347, 0.000228438, 0.000639426, 0.00542308, -0.0241995, 0.000248257, 0.000602457, 0.00542308, -0.0241995, 0.000248257, 0.000602457, -0.00528861, -0.0250475, 0.000283092, 0.000618706, -0.00528861, -0.0250475, 0.000283092, 0.000618706, 1.67008, 1.59574, 0.00601223, 0.0114465, 1.67008, 1.59574, 0.00601223, 0.0114465)

reports.append(Report(585203712, ("DT", 0, 3, 8), "MBwhCst3sec08"))
reports[-1].posNum = 54424
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.0883169, 0.00711918, 0), \
                           ValErr(0.055984, 0.00687603, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000158439, 7.93297e-05, 0), \
                           -207751, 54424, 54424, -nan)
reports[-1].sigmax = ValErr(1.66006, 0.0050317, 0)
reports[-1].sigmay = ValErr(1.60406, 0.00486195, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0946369, 0.0469496, 3.57814e-05, -7.27836e-05, -0.0887494, 0.0560855, 2.74801e-05, -7.20565e-05, -0.0887494, 0.0560855, 2.74801e-05, -7.20565e-05, -0.0916356, 0.0591665, 6.82092e-05, -0.000114208, -0.0916356, 0.0591665, 6.82092e-05, -0.000114208, 1.66006, 1.60412, 0.00594453, 0.0119013, 1.66006, 1.60412, 0.00594453, 0.0119013)

reports.append(Report(586252288, ("DT", 0, 3, 12), "MBwhCst3sec12"))
reports[-1].posNum = 57749
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.0651819, 0.00690259, 0), \
                           ValErr(0.0198859, 0.00660445, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000441987, 7.70086e-05, 0), \
                           -219736, 57749, 57749, -nan)
reports[-1].sigmax = ValErr(1.65868, 0.00488062, 0)
reports[-1].sigmay = ValErr(1.58586, 0.00466638, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0742464, 0.0218131, -0.00158584, -0.00161887, 0.0655782, 0.0213972, -0.00153802, -0.00164925, 0.0655782, 0.0213972, -0.00153802, -0.00164925, 0.0608916, 0.0225889, -0.00147512, -0.00167542, 0.0608916, 0.0225889, -0.00147512, -0.00167542, 1.65886, 1.58614, 0.00592836, 0.0116882, 1.65886, 1.58614, 0.00592836, 0.0116882)

reports.append(Report(575012864, ("DT", 1, 1, 1), "MBwhDst1sec01"))
reports[-1].posNum = 42690
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.00313187, 0.0047821, 0), \
                           ValErr(0.00644316, 0.00552796, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000296457, 8.0374e-05, 0), \
                           -122569, 42690, 42690, -nan)
reports[-1].sigmax = ValErr(0.969853, 0.00331926, 0)
reports[-1].sigmay = ValErr(1.06596, 0.00364822, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00270217, -0.000420651, 0.000416042, 0.000426973, 0.00650217, -0.000879693, 0.00037979, 0.000157797, 0.00650217, -0.000879693, 0.00037979, 0.000157797, 0.00184887, -0.00184839, 0.000436909, 0.000276822, 0.00184887, -0.00184839, 0.000436909, 0.000276822, 0.970057, 1.06591, 0.00477301, 0.0142154, 0.970057, 1.06591, 0.00477301, 0.0142154)

reports.append(Report(575275008, ("DT", 1, 1, 2), "MBwhDst1sec02"))
reports[-1].posNum = 58817
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.0532186, 0.00403813, 0), \
                           ValErr(0.0123448, 0.00437285, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.00718e-06, 6.31235e-05, 0), \
                           -168233, 58817, 58817, -nan)
reports[-1].sigmax = ValErr(0.964651, 0.00281258, 0)
reports[-1].sigmay = ValErr(1.06013, 0.00309096, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0470736, 0.00888228, -0.000199867, 2.97499e-05, -0.053185, 0.0123503, -0.000167555, -0.000145271, -0.053185, 0.0123503, -0.000167555, -0.000145271, -0.0496988, 0.0102096, -0.000144731, -9.42297e-05, -0.0496988, 0.0102096, -0.000144731, -9.42297e-05, 0.964651, 1.06013, 0.00481714, 0.0149092, 0.964651, 1.06013, 0.00481714, 0.0149092)

reports.append(Report(575537152, ("DT", 1, 1, 3), "MBwhDst1sec03"))
reports[-1].posNum = 88311
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.0365892, 0.00321866, 0), \
                           ValErr(-0.0173467, 0.00357312, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000198408, 5.12113e-05, 0), \
                           -251702, 88311, 88311, -nan)
reports[-1].sigmax = ValErr(0.953611, 0.00226908, 0)
reports[-1].sigmay = ValErr(1.06163, 0.00252609, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0314982, -0.0171467, -0.00108482, 0.00303512, -0.0356224, -0.0170771, -0.0010778, 0.00281216, -0.0356224, -0.0170771, -0.0010778, 0.00281216, -0.0391083, -0.0224218, -0.00104511, 0.00281004, -0.0391083, -0.0224218, -0.00104511, 0.00281004, 0.953675, 1.06165, 0.00479653, 0.0145575, 0.953675, 1.06165, 0.00479653, 0.0145575)

reports.append(Report(575799296, ("DT", 1, 1, 4), "MBwhDst1sec04"))
reports[-1].posNum = 40797
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.0547801, 0.00523272, 0), \
                           ValErr(-0.033094, 0.00591261, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000535553, 0.000105629, 0), \
                           -121982, 40797, 40797, -nan)
reports[-1].sigmax = ValErr(0.998663, 0.00349626, 0)
reports[-1].sigmay = ValErr(1.16584, 0.00408165, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0519921, -0.0355013, 0.000201609, 0.00472125, -0.0460899, -0.0265961, 0.000209544, 0.00432024, -0.0460899, -0.0265961, 0.000209544, 0.00432024, -0.0487854, -0.0275002, 0.000287729, 0.00435655, -0.0487854, -0.0275002, 0.000287729, 0.00435655, 0.998623, 1.16625, 0.00505835, 0.014837, 0.998623, 1.16625, 0.00505835, 0.014837)

reports.append(Report(576061440, ("DT", 1, 1, 5), "MBwhDst1sec05"))
reports[-1].posNum = 81705
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.0370593, 0.00337552, 0), \
                           ValErr(-0.0520669, 0.00372464, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.00012785, 5.38371e-05, 0), \
                           -233868, 81705, 81705, -nan)
reports[-1].sigmax = ValErr(0.960947, 0.00237721, 0)
reports[-1].sigmay = ValErr(1.06642, 0.00263665, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0458972, -0.0497952, -0.00142939, 0.000170801, 0.0377825, -0.0518028, -0.00141618, -6.36398e-05, 0.0377825, -0.0518028, -0.00141618, -6.36398e-05, 0.0389751, -0.0543656, -0.00139147, -6.93357e-05, 0.0389751, -0.0543656, -0.00139147, -6.93357e-05, 0.96093, 1.06647, 0.00479054, 0.0145889, 0.96093, 1.06647, 0.00479054, 0.0145889)

reports.append(Report(576323584, ("DT", 1, 1, 6), "MBwhDst1sec06"))
reports[-1].posNum = 89435
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.0302794, 0.0032291, 0), \
                           ValErr(-0.0246694, 0.00357577, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000394087, 5.11259e-05, 0), \
                           -256478, 89435, 89435, -nan)
reports[-1].sigmax = ValErr(0.964006, 0.00227954, 0)
reports[-1].sigmay = ValErr(1.06881, 0.00252733, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0296764, -0.0224727, -0.00279596, 0.00149345, 0.0288154, -0.0255516, -0.00282249, 0.00129199, 0.0288154, -0.0255516, -0.00282249, 0.00129199, 0.0264668, -0.0290104, -0.00274978, 0.00135589, 0.0264668, -0.0290104, -0.00274978, 0.00135589, 0.964406, 1.06872, 0.0048913, 0.0144151, 0.964406, 1.06872, 0.0048913, 0.0144151)

reports.append(Report(576585728, ("DT", 1, 1, 7), "MBwhDst1sec07"))
reports[-1].posNum = 87859
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.0384574, 0.00328394, 0), \
                           ValErr(-0.0391154, 0.00361992, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000159629, 5.21498e-05, 0), \
                           -252923, 87859, 87859, -nan)
reports[-1].sigmax = ValErr(0.968624, 0.00231204, 0)
reports[-1].sigmay = ValErr(1.07545, 0.00256556, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0421957, -0.0368067, 0.000391905, -7.72808e-05, 0.039463, -0.0394539, 0.00038641, -0.000279022, 0.039463, -0.0394539, 0.00038641, -0.000279022, 0.0384118, -0.0395032, 0.000402218, -0.000275394, 0.0384118, -0.0395032, 0.000402218, -0.000275394, 0.968741, 1.07537, 0.00483175, 0.0143122, 0.968741, 1.07537, 0.00483175, 0.0143122)

reports.append(Report(576847872, ("DT", 1, 1, 8), "MBwhDst1sec08"))
reports[-1].posNum = 84841
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.0808502, 0.00333721, 0), \
                           ValErr(-0.0060093, 0.0036687, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000321555, 5.26176e-05, 0), \
                           -243814, 84841, 84841, -nan)
reports[-1].sigmax = ValErr(0.970334, 0.00235562, 0)
reports[-1].sigmay = ValErr(1.06824, 0.00259331, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0873058, -0.0033222, -0.00219183, -0.00165443, 0.0820626, -0.00543252, -0.00218766, -0.00180736, 0.0820626, -0.00543252, -0.00218766, -0.00180736, 0.0793009, -0.00648871, -0.00213424, -0.00174785, 0.0793009, -0.00648871, -0.00213424, -0.00174785, 0.970414, 1.06839, 0.00486081, 0.0142592, 0.970414, 1.06839, 0.00486081, 0.0142592)

reports.append(Report(577110016, ("DT", 1, 1, 9), "MBwhDst1sec09"))
reports[-1].posNum = 81094
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.0234591, 0.00338624, 0), \
                           ValErr(0.0277194, 0.00373506, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000294737, 5.3007e-05, 0), \
                           -231879, 81094, 81094, -nan)
reports[-1].sigmax = ValErr(0.960751, 0.00238564, 0)
reports[-1].sigmay = ValErr(1.06348, 0.00264073, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0210988, 0.0325895, -0.000873286, -0.000836962, 0.0218474, 0.0280666, -0.000888664, -0.00114738, 0.0218474, 0.0280666, -0.000888664, -0.00114738, 0.0233165, 0.0314751, -0.000923337, -0.00113451, 0.0233165, 0.0314751, -0.000923337, -0.00113451, 0.960899, 1.06352, 0.00480718, 0.0145961, 0.960899, 1.06352, 0.00480718, 0.0145961)

reports.append(Report(577372160, ("DT", 1, 1, 10), "MBwhDst1sec10"))
reports[-1].posNum = 91271
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.0570257, 0.00318185, 0), \
                           ValErr(-0.0406552, 0.00351038, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000137431, 5.00365e-05, 0), \
                           -260470, 91271, 91271, -nan)
reports[-1].sigmax = ValErr(0.958469, 0.00224335, 0)
reports[-1].sigmay = ValErr(1.06009, 0.0024812, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0579758, -0.037736, -0.000950573, 0.000813727, 0.0563586, -0.0409317, -0.000954038, 0.000408072, 0.0563586, -0.0409317, -0.000954038, 0.000408072, 0.0574287, -0.0431649, -0.000958835, 0.000421085, 0.0574287, -0.0431649, -0.000958835, 0.000421085, 0.958506, 1.06009, 0.00476232, 0.0144245, 0.958506, 1.06009, 0.00476232, 0.0144245)

reports.append(Report(577634304, ("DT", 1, 1, 11), "MBwhDst1sec11"))
reports[-1].posNum = 89215
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.0343141, 0.0032286, 0), \
                           ValErr(-0.0109215, 0.00354923, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000184586, 5.06152e-05, 0), \
                           -254812, 89215, 89215, -nan)
reports[-1].sigmax = ValErr(0.960855, 0.00227478, 0)
reports[-1].sigmay = ValErr(1.05994, 0.00250938, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0327487, -0.0101315, 0.000460715, 0.0024756, 0.033313, -0.0111575, 0.000458358, 0.00217184, 0.033313, -0.0111575, 0.000458358, 0.00217184, 0.0281008, -0.0164668, 0.000507404, 0.00218366, 0.0281008, -0.0164668, 0.000507404, 0.00218366, 0.960822, 1.06005, 0.00477548, 0.0149372, 0.960822, 1.06005, 0.00477548, 0.0149372)

reports.append(Report(577896448, ("DT", 1, 1, 12), "MBwhDst1sec12"))
reports[-1].posNum = 94259
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.061346, 0.00312297, 0), \
                           ValErr(0.0552052, 0.0034337, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.37084e-05, 4.90625e-05, 0), \
                           -268569, 94259, 94259, -nan)
reports[-1].sigmax = ValErr(0.957496, 0.00219878, 0)
reports[-1].sigmay = ValErr(1.05635, 0.00243197, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.062555, 0.0516048, -0.000146616, 6.13194e-05, -0.061733, 0.0551196, -0.000162163, -0.000272926, -0.061733, 0.0551196, -0.000162163, -0.000272926, -0.0625779, 0.0506657, -0.000120619, -0.000260065, -0.0625779, 0.0506657, -0.000120619, -0.000260065, 0.9575, 1.05636, 0.00473715, 0.0145188, 0.9575, 1.05636, 0.00473715, 0.0145188)

reports.append(Report(579207168, ("DT", 1, 2, 1), "MBwhDst2sec01"))
reports[-1].posNum = 84036
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.0403599, 0.0044091, 0), \
                           ValErr(-0.0686214, 0.00465492, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000286713, 5.91809e-05, 0), \
                           -284309, 84036, 84036, -nan)
reports[-1].sigmax = ValErr(1.27691, 0.00311437, 0)
reports[-1].sigmay = ValErr(1.35103, 0.0032792, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0410356, -0.0658476, 0.00248873, 0.0033452, -0.0393613, -0.0691792, 0.00250031, 0.00314785, -0.0393613, -0.0691792, 0.00250031, 0.00314785, -0.040068, -0.0710278, 0.00252216, 0.0031929, -0.040068, -0.0710278, 0.00252216, 0.0031929, 1.27692, 1.3512, 0.00508174, 0.0143611, 1.27692, 1.3512, 0.00508174, 0.0143611)

reports.append(Report(579469312, ("DT", 1, 2, 2), "MBwhDst2sec02"))
reports[-1].posNum = 71345
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.0407746, 0.00478771, 0), \
                           ValErr(0.00281309, 0.00505067, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000159007, 6.36183e-05, 0), \
                           -241043, 71345, 71345, -nan)
reports[-1].sigmax = ValErr(1.27293, 0.00336982, 0)
reports[-1].sigmay = ValErr(1.349, 0.0035712, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.035062, 0.00556587, 0.000803626, 0.00511522, -0.0419285, 0.00268565, 0.000806766, 0.00513566, -0.0419285, 0.00268565, 0.000806766, 0.00513566, -0.045076, 0.00441158, 0.00081922, 0.00519317, -0.045076, 0.00441158, 0.00081922, 0.00519317, 1.27296, 1.34903, 0.00507773, 0.0146167, 1.27296, 1.34903, 0.00507773, 0.0146167)

reports.append(Report(579731456, ("DT", 1, 2, 3), "MBwhDst2sec03"))
reports[-1].posNum = 52287
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.000752108, 0.00563335, 0), \
                           ValErr(-0.024866, 0.00600714, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000577167, 6.82768e-05, 0), \
                           -178149, 52287, 52287, -nan)
reports[-1].sigmax = ValErr(1.28725, 0.00398071, 0)
reports[-1].sigmay = ValErr(1.37266, 0.00424485, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00443553, -0.032631, -0.00011798, 0.00343672, 0.00255366, -0.0229809, -0.000129032, 0.00332159, 0.00255366, -0.0229809, -0.000129032, 0.00332159, -0.000477569, -0.0236015, -0.000133973, 0.00336432, -0.000477569, -0.0236015, -0.000133973, 0.00336432, 1.28729, 1.37356, 0.00523217, 0.0143617, 1.28729, 1.37356, 0.00523217, 0.0143617)

reports.append(Report(579993600, ("DT", 1, 2, 4), "MBwhDst2sec04"))
reports[-1].posNum = 58984
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.00558205, 0.00528798, 0), \
                           ValErr(0.0356821, 0.00574868, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000347952, 7.89264e-05, 0), \
                           -201682, 58984, 58984, -nan)
reports[-1].sigmax = ValErr(1.285, 0.00373919, 0)
reports[-1].sigmay = ValErr(1.39184, 0.00405042, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.00979239, 0.0386219, 5.79801e-05, 0.00356392, 0.00597589, 0.0333428, 8.34035e-05, 0.00318904, 0.00597589, 0.0333428, 8.34035e-05, 0.00318904, 0.000821868, 0.0297937, 0.00010209, 0.00323395, 0.000821868, 0.0297937, 0.00010209, 0.00323395, 1.28485, 1.39223, 0.00512635, 0.0149592, 1.28485, 1.39223, 0.00512635, 0.0149592)

reports.append(Report(580255744, ("DT", 1, 2, 5), "MBwhDst2sec05"))
reports[-1].posNum = 70104
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.0857263, 0.00478775, 0), \
                           ValErr(0.0267743, 0.00536582, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000136846, 7.04619e-05, 0), \
                           -237022, 70104, 70104, -nan)
reports[-1].sigmax = ValErr(1.26765, 0.00338557, 0)
reports[-1].sigmay = ValErr(1.35793, 0.00362665, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0833931, 0.0276852, -1.77218e-05, 0.00528188, 0.0857612, 0.0237107, -1.66043e-05, 0.00518637, 0.0857612, 0.0237107, -1.66043e-05, 0.00518637, 0.0853459, 0.0218193, -2.47165e-05, 0.00520619, 0.0853459, 0.0218193, -2.47165e-05, 0.00520619, 1.26761, 1.35801, 0.00511513, 0.0144203, 1.26761, 1.35801, 0.00511513, 0.0144203)

reports.append(Report(580517888, ("DT", 1, 2, 6), "MBwhDst2sec06"))
reports[-1].posNum = 91825
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.0742821, 0.00424261, 0), \
                           ValErr(0.0187006, 0.00452724, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000724996, 5.69098e-05, 0), \
                           -312624, 91825, 91825, -nan)
reports[-1].sigmax = ValErr(1.28546, 0.00299985, 0)
reports[-1].sigmay = ValErr(1.37104, 0.00319952, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0739594, 0.023721, -0.000842335, 0.00384301, 0.0734218, 0.0207087, -0.000846387, 0.00379342, 0.0734218, 0.0207087, -0.000846387, 0.00379342, 0.0717692, 0.0222223, -0.000828396, 0.0038458, 0.0717692, 0.0222223, -0.000828396, 0.0038458, 1.28642, 1.37122, 0.00511775, 0.0145974, 1.28642, 1.37122, 0.00511775, 0.0145974)

reports.append(Report(580780032, ("DT", 1, 2, 7), "MBwhDst2sec07"))
reports[-1].posNum = 89213
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.0735942, 0.00431198, 0), \
                           ValErr(0.114682, 0.00452184, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.65495e-05, 5.79311e-05, 0), \
                           -303450, 89213, 89213, -nan)
reports[-1].sigmax = ValErr(1.28734, 0.0030464, 0)
reports[-1].sigmay = ValErr(1.36473, 0.00323071, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0819208, 0.114115, 0.000868951, 0.00348207, 0.0735453, 0.114763, 0.000869064, 0.00327345, 0.0735453, 0.114763, 0.000869064, 0.00327345, 0.0704355, 0.108092, 0.000896737, 0.00333333, 0.0704355, 0.108092, 0.000896737, 0.00333333, 1.28736, 1.36471, 0.00512462, 0.0143213, 1.28736, 1.36471, 0.00512462, 0.0143213)

reports.append(Report(581042176, ("DT", 1, 2, 8), "MBwhDst2sec08"))
reports[-1].posNum = 87189
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.143085, 0.0043379, 0), \
                           ValErr(0.0199888, 0.00450634, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0003678, 5.81374e-05, 0), \
                           -296049, 87189, 87189, -nan)
reports[-1].sigmax = ValErr(1.28165, 0.00305872, 0)
reports[-1].sigmay = ValErr(1.36268, 0.00325718, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.142968, 0.02247, 0.00015641, 0.00246881, 0.143715, 0.020147, 0.000134768, 0.00230921, 0.143715, 0.020147, 0.000134768, 0.00230921, 0.139293, 0.0180339, 0.000178165, 0.00231611, 0.139293, 0.0180339, 0.000178165, 0.00231611, 1.28144, 1.36323, 0.00511303, 0.0148464, 1.28144, 1.36323, 0.00511303, 0.0148464)

reports.append(Report(581304320, ("DT", 1, 2, 9), "MBwhDst2sec09"))
reports[-1].posNum = 83730
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.0140684, 0.00440315, 0), \
                           ValErr(0.0137933, 0.00468435, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.00014591, 5.9668e-05, 0), \
                           -283108, 83730, 83730, -nan)
reports[-1].sigmax = ValErr(1.27021, 0.00310401, 0)
reports[-1].sigmay = ValErr(1.35546, 0.00331233, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0203168, 0.0178822, 0.000375684, 0.00347335, 0.0149094, 0.0138352, 0.000413025, 0.00344993, 0.0149094, 0.0138352, 0.000413025, 0.00344993, 0.017152, 0.013769, 0.000425174, 0.00348966, 0.017152, 0.013769, 0.000425174, 0.00348966, 1.2702, 1.35552, 0.00512699, 0.0143864, 1.2702, 1.35552, 0.00512699, 0.0143864)

reports.append(Report(581566464, ("DT", 1, 2, 10), "MBwhDst2sec10"))
reports[-1].posNum = 87481
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.0660237, 0.00431203, 0), \
                           ValErr(-0.0413736, 0.00458945, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000171572, 5.80142e-05, 0), \
                           -296177, 87481, 87481, -nan)
reports[-1].sigmax = ValErr(1.2753, 0.00304892, 0)
reports[-1].sigmay = ValErr(1.35602, 0.00324187, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0668853, -0.0436238, -0.000117524, 0.0030469, 0.06616, -0.0419926, -0.000112631, 0.00302025, 0.06616, -0.0419926, -0.000112631, 0.00302025, 0.0649324, -0.0432736, -9.52604e-05, 0.00301355, 0.0649324, -0.0432736, -9.52604e-05, 0.00301355, 1.2753, 1.35609, 0.00508273, 0.0143478, 1.2753, 1.35609, 0.00508273, 0.0143478)

reports.append(Report(581828608, ("DT", 1, 2, 11), "MBwhDst2sec11"))
reports[-1].posNum = 88428
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.00976746, 0.00427836, 0), \
                           ValErr(0.00614528, 0.0045442, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.86848e-05, 5.80606e-05, 0), \
                           -299085, 88428, 88428, -nan)
reports[-1].sigmax = ValErr(1.27212, 0.00302381, 0)
reports[-1].sigmay = ValErr(1.35484, 0.00322367, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00914192, 0.00692771, -0.000109235, 0.00319489, -0.00987752, 0.00618807, -0.000101633, 0.00289594, -0.00987752, 0.00618807, -0.000101633, 0.00289594, -0.00681095, 0.00711076, -0.000101753, 0.00294912, -0.00681095, 0.00711076, -0.000101753, 0.00294912, 1.27214, 1.35483, 0.0050791, 0.0145865, 1.27214, 1.35483, 0.0050791, 0.0145865)

reports.append(Report(582090752, ("DT", 1, 2, 12), "MBwhDst2sec12"))
reports[-1].posNum = 91275
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.0723385, 0.00422149, 0), \
                           ValErr(0.0490868, 0.00448685, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000342784, 5.68595e-05, 0), \
                           -308952, 91275, 91275, -nan)
reports[-1].sigmax = ValErr(1.27478, 0.00298366, 0)
reports[-1].sigmay = ValErr(1.35554, 0.00317266, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0723289, 0.0480558, 0.00103199, 0.00484561, -0.0731164, 0.0492155, 0.00105425, 0.00465289, -0.0731164, 0.0492155, 0.00105425, 0.00465289, -0.0698023, 0.047264, 0.0010508, 0.00467878, -0.0698023, 0.047264, 0.0010508, 0.00467878, 1.27495, 1.35563, 0.00509714, 0.0147274, 1.27495, 1.35563, 0.00509714, 0.0147274)

reports.append(Report(583401472, ("DT", 1, 3, 1), "MBwhDst3sec01"))
reports[-1].posNum = 65756
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.0866472, 0.00670626, 0), \
                           ValErr(-0.066314, 0.00699535, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000479123, 7.90918e-05, 0), \
                           -260572, 65756, 65756, -nan)
reports[-1].sigmax = ValErr(1.719, 0.00474027, 0)
reports[-1].sigmay = ValErr(1.79158, 0.00494044, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0919791, -0.0641261, 0.000631062, -0.00090236, -0.0855055, -0.0684284, 0.000600774, -0.000721485, -0.0855055, -0.0684284, 0.000600774, -0.000721485, -0.0853867, -0.0686031, 0.000621167, -0.000724038, -0.0853867, -0.0686031, 0.000621167, -0.000724038, 1.71898, 1.7921, 0.00597484, 0.0136866, 1.71898, 1.7921, 0.00597484, 0.0136866)

reports.append(Report(583663616, ("DT", 1, 3, 2), "MBwhDst3sec02"))
reports[-1].posNum = 62604
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.0525434, 0.0067689, 0), \
                           ValErr(0.029867, 0.00734698, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.68792e-06, 7.98886e-05, 0), \
                           -245566, 62604, 62604, -nan)
reports[-1].sigmax = ValErr(1.68696, 0.00482847, 0)
reports[-1].sigmay = ValErr(1.75368, 0.00504629, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0539356, 0.0354788, 0.000499195, -0.00151933, -0.0525475, 0.0298442, 0.000489476, -0.00140808, -0.0525475, 0.0298442, 0.000489476, -0.00140808, -0.0528196, 0.0161495, 0.00051268, -0.00138284, -0.0528196, 0.0161495, 0.00051268, -0.00138284, 1.68696, 1.75368, 0.00590566, 0.0132028, 1.68696, 1.75368, 0.00590566, 0.0132028)

reports.append(Report(583925760, ("DT", 1, 3, 3), "MBwhDst3sec03"))
reports[-1].posNum = 70445
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.0299969, 0.006365, 0), \
                           ValErr(0.0412029, 0.00664891, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000255744, 7.63081e-05, 0), \
                           -277091, 70445, 70445, -nan)
reports[-1].sigmax = ValErr(1.70519, 0.00454358, 0)
reports[-1].sigmay = ValErr(1.75398, 0.00471862, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0296365, 0.0408315, -0.000703992, 0.000367969, -0.0298425, 0.0407169, -0.000718026, 0.000448783, -0.0298425, 0.0407169, -0.000718026, 0.000448783, -0.0272622, 0.0412537, -0.000722984, 0.000496282, -0.0272622, 0.0412537, -0.000722984, 0.000496282, 1.70527, 1.75404, 0.00599974, 0.0135464, 1.70527, 1.75404, 0.00599974, 0.0135464)

reports.append(Report(584187904, ("DT", 1, 3, 4), "MBwhDst3sec04"))
reports[-1].posNum = 47255
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.0292989, 0.00790514, 0), \
                           ValErr(0.0992025, 0.00818625, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000746036, 9.98675e-05, 0), \
                           -186911, 47255, 47255, -nan)
reports[-1].sigmax = ValErr(1.7182, 0.00558904, 0)
reports[-1].sigmay = ValErr(1.7793, 0.0057878, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0260605, 0.101154, -1.78805e-05, 0.00148785, -0.0302782, 0.10022, -1.47734e-05, 0.00140393, -0.0302782, 0.10022, -1.47734e-05, 0.00140393, -0.0272011, 0.0976449, 1.28584e-06, 0.00142352, -0.0272011, 0.0976449, 1.28584e-06, 0.00142352, 1.71856, 1.77997, 0.00602987, 0.013901, 1.71856, 1.77997, 0.00602987, 0.013901)

reports.append(Report(584450048, ("DT", 1, 3, 5), "MBwhDst3sec05"))
reports[-1].posNum = 69163
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.0460771, 0.00650416, 0), \
                           ValErr(-0.0447992, 0.00670419, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.65546e-05, 7.63316e-05, 0), \
                           -272512, 69163, 69163, -nan)
reports[-1].sigmax = ValErr(1.71048, 0.00459906, 0)
reports[-1].sigmay = ValErr(1.76032, 0.00473305, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0361025, -0.0427057, -0.000344954, -0.00102399, 0.0461307, -0.0452772, -0.0003645, -0.000928247, 0.0461307, -0.0452772, -0.0003645, -0.000928247, 0.0451596, -0.0485954, -0.000367635, -0.000839001, 0.0451596, -0.0485954, -0.000367635, -0.000839001, 1.71051, 1.76031, 0.00599001, 0.0136039, 1.71051, 1.76031, 0.00599001, 0.0136039)

reports.append(Report(584712192, ("DT", 1, 3, 6), "MBwhDst3sec06"))
reports[-1].posNum = 75286
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.112279, 0.00625172, 0), \
                           ValErr(0.00381203, 0.00646835, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000530657, 7.37943e-05, 0), \
                           -297426, 75286, 75286, -nan)
reports[-1].sigmax = ValErr(1.71533, 0.00442074, 0)
reports[-1].sigmay = ValErr(1.77381, 0.00457144, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.109259, 0.00449906, -0.000960498, 0.00261933, 0.112583, 0.0022594, -0.00100133, 0.00276081, 0.112583, 0.0022594, -0.00100133, 0.00276081, 0.109693, -0.00847526, -0.00100292, 0.00276995, 0.109693, -0.00847526, -0.00100292, 0.00276995, 1.71582, 1.77391, 0.00600904, 0.0133475, 1.71582, 1.77391, 0.00600904, 0.0133475)

reports.append(Report(584974336, ("DT", 1, 3, 7), "MBwhDst3sec07"))
reports[-1].posNum = 71333
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.120138, 0.00646861, 0), \
                           ValErr(0.00827401, 0.00659176, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000165034, 7.56452e-05, 0), \
                           -281643, 71333, 71333, -nan)
reports[-1].sigmax = ValErr(1.72764, 0.00457408, 0)
reports[-1].sigmay = ValErr(1.75708, 0.004652, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.120549, 0.0135984, -0.000221734, 0.00299059, 0.120176, 0.00917429, -0.000208014, 0.00308453, 0.120176, 0.00917429, -0.000208014, 0.00308453, 0.11945, 0.00987263, -0.000200371, 0.00306175, 0.11945, 0.00987263, -0.000200371, 0.00306175, 1.7276, 1.75719, 0.00604455, 0.0135996, 1.7276, 1.75719, 0.00604455, 0.0135996)

reports.append(Report(585236480, ("DT", 1, 3, 8), "MBwhDst3sec08"))
reports[-1].posNum = 68839
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.166143, 0.00652861, 0), \
                           ValErr(-0.0736979, 0.00671926, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000370356, 7.65472e-05, 0), \
                           -271202, 68839, 68839, -nan)
reports[-1].sigmax = ValErr(1.71267, 0.00461611, 0)
reports[-1].sigmay = ValErr(1.75721, 0.00473609, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.163152, -0.0749529, -0.000584165, 0.00322777, 0.165601, -0.0710777, -0.000615985, 0.00332002, 0.165601, -0.0710777, -0.000615985, 0.00332002, 0.173113, -0.0773654, -0.0006133, 0.00333967, 0.173113, -0.0773654, -0.0006133, 0.00333967, 1.71249, 1.75769, 0.00594899, 0.0133442, 1.71249, 1.75769, 0.00594899, 0.0133442)

reports.append(Report(585498624, ("DT", 1, 3, 9), "MBwhDst3sec09"))
reports[-1].posNum = 71800
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.0291591, 0.00638306, 0), \
                           ValErr(0.101386, 0.00655405, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000251419, 7.56963e-05, 0), \
                           -282587, 71800, 71800, -nan)
reports[-1].sigmax = ValErr(1.71024, 0.0045132, 0)
reports[-1].sigmay = ValErr(1.75285, 0.00462563, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0294045, 0.104147, -0.000953493, -0.000624555, 0.0294272, 0.100046, -0.000974993, -0.000648164, 0.0294272, 0.100046, -0.000974993, -0.000648164, 0.0360601, 0.0881806, -0.00100845, -0.000621321, 0.0360601, 0.0881806, -0.00100845, -0.000621321, 1.71035, 1.75287, 0.00600262, 0.0134848, 1.71035, 1.75287, 0.00600262, 0.0134848)

reports.append(Report(585760768, ("DT", 1, 3, 10), "MBwhDst3sec10"))
reports[-1].posNum = 70892
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.0230346, 0.00638946, 0), \
                           ValErr(-0.13322, 0.00659193, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000173515, 7.54379e-05, 0), \
                           -278578, 70892, 70892, -nan)
reports[-1].sigmax = ValErr(1.7012, 0.00451797, 0)
reports[-1].sigmay = ValErr(1.75139, 0.00465126, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0236169, -0.135615, 0.000616872, 0.00403507, 0.0229564, -0.132227, 0.000615808, 0.00409243, 0.0229564, -0.132227, 0.000615808, 0.00409243, 0.0249921, -0.141186, 0.00062157, 0.00411216, 0.0249921, -0.141186, 0.00062157, 0.00411216, 1.70123, 1.75142, 0.00595539, 0.0136705, 1.70123, 1.75142, 0.00595539, 0.0136705)

reports.append(Report(586022912, ("DT", 1, 3, 11), "MBwhDst3sec11"))
reports[-1].posNum = 74374
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.0616998, 0.00619952, 0), \
                           ValErr(-0.00953501, 0.00643239, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000463496, 7.3596e-05, 0), \
                           -291839, 74374, 74374, -nan)
reports[-1].sigmax = ValErr(1.69071, 0.00438377, 0)
reports[-1].sigmay = ValErr(1.75227, 0.00454337, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0642277, -0.0162966, -0.00107252, -0.00132609, 0.061663, -0.011442, -0.00105981, -0.00121695, 0.061663, -0.011442, -0.00105981, -0.00121695, 0.0637232, -0.0166266, -0.00104685, -0.00119966, 0.0637232, -0.0166266, -0.00104685, -0.00119966, 1.69097, 1.75246, 0.00593284, 0.0133068, 1.69097, 1.75246, 0.00593284, 0.0133068)

reports.append(Report(586285056, ("DT", 1, 3, 12), "MBwhDst3sec12"))
reports[-1].posNum = 75351
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.0793486, 0.00623302, 0), \
                           ValErr(0.0792621, 0.00643254, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.40188e-05, 7.34516e-05, 0), \
                           -296673, 75351, 75351, -nan)
reports[-1].sigmax = ValErr(1.70542, 0.00440356, 0)
reports[-1].sigmay = ValErr(1.76038, 0.00455761, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0760851, 0.0771814, 0.000940241, -0.00407949, -0.0793669, 0.0794022, 0.000935687, -0.00404556, -0.0793669, 0.0794022, 0.000935687, -0.00404556, -0.0792248, 0.0752566, 0.000944969, -0.00410772, -0.0792248, 0.0752566, 0.000944969, -0.00410772, 1.70542, 1.76038, 0.00594565, 0.013812, 1.70542, 1.76038, 0.00594565, 0.013812)

reports.append(Report(575045632, ("DT", 2, 1, 1), "MBwhEst1sec01"))
reports[-1].posNum = 24071
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.0373632, 0.00768894, 0), \
                           ValErr(-0.111978, 0.00993871, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000215568, 0.000121808, 0), \
                           -80270.4, 24071, 24071, -nan)
reports[-1].sigmax = ValErr(1.06588, 0.00485853, 0)
reports[-1].sigmay = ValErr(1.54197, 0.00702878, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0421724, -0.111817, -0.000165043, -0.00144802, -0.0434748, -0.112004, -0.000150334, -0.000485772, -0.0434748, -0.112004, -0.000150334, -0.000485772, -0.0529044, -0.115233, -4.06993e-05, -0.000615779, -0.0529044, -0.115233, -4.06993e-05, -0.000615779, 1.06578, 1.54222, 0.00534272, 0.0355175, 1.06578, 1.54222, 0.00534272, 0.0355175)

reports.append(Report(575307776, ("DT", 2, 1, 2), "MBwhEst1sec02"))
reports[-1].posNum = 24509
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.00348902, 0.00851169, 0), \
                           ValErr(-0.0199646, 0.00985508, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000423391, 0.000134694, 0), \
                           -81996.6, 24509, 24509, -nan)
reports[-1].sigmax = ValErr(1.07689, 0.00486418, 0)
reports[-1].sigmay = ValErr(1.54284, 0.00696881, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0167088, -0.0098462, -0.00112599, 0.000587534, -0.0192452, -0.0198888, -0.00109971, 0.00122065, -0.0192452, -0.0198888, -0.00109971, 0.00122065, -0.0222566, -0.0268872, -0.0010718, 0.000944702, -0.0222566, -0.0268872, -0.0010718, 0.000944702, 1.07688, 1.54315, 0.00526297, 0.0392441, 1.07688, 1.54315, 0.00526297, 0.0392441)

reports.append(Report(575569920, ("DT", 2, 1, 3), "MBwhEst1sec03"))
reports[-1].posNum = 18589
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.120632, 0.0150708, 0), \
                           ValErr(0.0614392, 0.0110149, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000891952, 0.000223924, 0), \
                           -61035.3, 18589, 18589, -nan)
reports[-1].sigmax = ValErr(1.05687, 0.0054813, 0)
reports[-1].sigmay = ValErr(1.4773, 0.00766178, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0673845, 0.0395986, 0.000276121, -0.00240176, -0.0691504, 0.0535554, 0.000235548, -0.00193231, -0.0691504, 0.0535554, 0.000235548, -0.00193231, -0.0822977, 0.055471, 0.000364191, -0.00259155, -0.0822977, 0.055471, 0.000364191, -0.00259155, 1.05688, 1.47791, 0.00520719, 0.0320589, 1.05688, 1.47791, 0.00520719, 0.0320589)

reports.append(Report(575832064, ("DT", 2, 1, 4), "MBwhEst1sec04"))
reports[-1].posNum = 30373
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.058776, 0.00627045, 0), \
                           ValErr(-0.00381956, 0.0089897, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000404303, 0.000108268, 0), \
                           -101934, 30373, 30373, -nan)
reports[-1].sigmax = ValErr(1.07257, 0.00435181, 0)
reports[-1].sigmay = ValErr(1.5654, 0.00635144, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0686694, 0.00382876, -0.000912325, -0.00470958, 0.0632607, -0.00244916, -0.000916435, -0.0016255, 0.0632607, -0.00244916, -0.000916435, -0.0016255, 0.06162, -0.00579528, -0.000914055, -0.00191035, 0.06162, -0.00579528, -0.000914055, -0.00191035, 1.07281, 1.56541, 0.00522367, 0.0409389, 1.07281, 1.56541, 0.00522367, 0.0409389)

reports.append(Report(576094208, ("DT", 2, 1, 5), "MBwhEst1sec05"))
reports[-1].posNum = 23420
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.0145539, 0.00735936, 0), \
                           ValErr(0.113479, 0.0102382, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(9.13172e-05, 0.0001166, 0), \
                           -78606, 23420, 23420, -nan)
reports[-1].sigmax = ValErr(1.07237, 0.00495573, 0)
reports[-1].sigmay = ValErr(1.56615, 0.00723756, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0216809, 0.119561, -0.00127571, 0.00513255, 0.0163161, 0.113246, -0.00129941, 0.00489613, 0.0163161, 0.113246, -0.00129941, 0.00489613, 0.0133827, 0.106432, -0.00124157, 0.00471687, 0.0133827, 0.106432, -0.00124157, 0.00471687, 1.07231, 1.56626, 0.0052643, 0.0413933, 1.07231, 1.56626, 0.0052643, 0.0413933)

reports.append(Report(576356352, ("DT", 2, 1, 6), "MBwhEst1sec06"))
reports[-1].posNum = 32312
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.0069984, 0.00640608, 0), \
                           ValErr(0.0213207, 0.00889248, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000161577, 0.000114391, 0), \
                           -106742, 32312, 32312, -nan)
reports[-1].sigmax = ValErr(1.0481, 0.00412311, 0)
reports[-1].sigmay = ValErr(1.51988, 0.00597902, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0042826, 0.0146095, -1.88203e-05, -0.00631864, -0.00325038, 0.0252102, -2.91759e-07, -0.00458122, -0.00325038, 0.0252102, -2.91759e-07, -0.00458122, -0.00851693, 0.0177519, 4.21382e-05, -0.00494872, -0.00851693, 0.0177519, 4.21382e-05, -0.00494872, 1.04807, 1.51997, 0.0051296, 0.0391293, 1.04807, 1.51997, 0.0051296, 0.0391293)

reports.append(Report(576618496, ("DT", 2, 1, 7), "MBwhEst1sec07"))
reports[-1].posNum = 32199
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.226031, 0.00636253, 0), \
                           ValErr(0.00640451, 0.00905847, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000736321, 0.000102969, 0), \
                           -110200, 32199, 32199, -nan)
reports[-1].sigmax = ValErr(1.10764, 0.00437396, 0)
reports[-1].sigmay = ValErr(1.61988, 0.00644076, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.234618, 0.00264688, -0.00316804, -0.000414363, 0.218741, 0.00652604, -0.00315153, 0.00120289, 0.218741, 0.00652604, -0.00315153, 0.00120289, 0.214207, 0.00921008, -0.00313937, 0.00126111, 0.214207, 0.00921008, -0.00313937, 0.00126111, 1.10902, 1.6192, 0.00551214, 0.0393501, 1.10902, 1.6192, 0.00551214, 0.0393501)

reports.append(Report(576880640, ("DT", 2, 1, 8), "MBwhEst1sec08"))
reports[-1].posNum = 31585
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.0947329, 0.00635504, 0), \
                           ValErr(-0.0685084, 0.00879463, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.06379e-05, 0.000102893, 0), \
                           -105978, 31585, 31585, -nan)
reports[-1].sigmax = ValErr(1.07515, 0.00427791, 0)
reports[-1].sigmay = ValErr(1.56049, 0.00620902, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0868426, -0.0642964, -0.00228244, -0.00104229, 0.0943431, -0.0686076, -0.00233269, 0.000387513, 0.0943431, -0.0686076, -0.00233269, 0.000387513, 0.0867199, -0.0685367, -0.00224302, 9.96739e-05, 0.0867199, -0.0685367, -0.00224302, 9.96739e-05, 1.07515, 1.56048, 0.00527883, 0.0388003, 1.07515, 1.56048, 0.00527883, 0.0388003)

reports.append(Report(577142784, ("DT", 2, 1, 9), "MBwhEst1sec09"))
reports[-1].posNum = 24606
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.0519093, 0.00819084, 0), \
                           ValErr(-0.104249, 0.0097661, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000233482, 0.000129509, 0), \
                           -82013.3, 24606, 24606, -nan)
reports[-1].sigmax = ValErr(1.07345, 0.00483914, 0)
reports[-1].sigmay = ValErr(1.52853, 0.00689061, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0555596, -0.0889014, -1.45305e-05, -0.000955238, 0.0600239, -0.103075, 1.73011e-06, -0.000662291, 0.0600239, -0.103075, 1.73011e-06, -0.000662291, 0.0583675, -0.103901, 5.98667e-05, -0.000832839, 0.0583675, -0.103901, 5.98667e-05, -0.000832839, 1.07341, 1.52869, 0.00527944, 0.0383842, 1.07341, 1.52869, 0.00527944, 0.0383842)

reports.append(Report(577404928, ("DT", 2, 1, 10), "MBwhEst1sec10"))
reports[-1].posNum = 37875
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.133517, 0.0057292, 0), \
                           ValErr(0.00498284, 0.00804084, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000551301, 9.56284e-05, 0), \
                           -126840, 37875, 37875, -nan)
reports[-1].sigmax = ValErr(1.06939, 0.00388563, 0)
reports[-1].sigmay = ValErr(1.55883, 0.00566407, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.129374, 0.0106888, -0.000992294, -0.00378622, 0.124171, 0.000918181, -0.000994301, -0.00229328, 0.124171, 0.000918181, -0.000994301, -0.00229328, 0.120211, -0.00618932, -0.000999533, -0.00268423, 0.120211, -0.00618932, -0.000999533, -0.00268423, 1.06951, 1.55933, 0.00524409, 0.0374936, 1.06951, 1.55933, 0.00524409, 0.0374936)

reports.append(Report(577667072, ("DT", 2, 1, 11), "MBwhEst1sec11"))
reports[-1].posNum = 35216
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.0443293, 0.00608545, 0), \
                           ValErr(-0.0383522, 0.00820677, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000433581, 9.99906e-05, 0), \
                           -117309, 35216, 35216, -nan)
reports[-1].sigmax = ValErr(1.06343, 0.00400707, 0)
reports[-1].sigmay = ValErr(1.53996, 0.00580264, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0549188, -0.0219873, -0.00261541, -0.000445469, -0.0539445, -0.0387963, -0.00264402, 0.00171066, -0.0539445, -0.0387963, -0.00264402, 0.00171066, -0.049793, -0.0436151, -0.002617, 0.00171102, -0.049793, -0.0436151, -0.002617, 0.00171102, 1.06368, 1.54, 0.00528123, 0.0388354, 1.06368, 1.54, 0.00528123, 0.0388354)

reports.append(Report(577929216, ("DT", 2, 1, 12), "MBwhEst1sec12"))
reports[-1].posNum = 41442
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.0537987, 0.00596908, 0), \
                           ValErr(0.0753027, 0.00756769, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.10033e-05, 0.000102337, 0), \
                           -138282, 41442, 41442, -nan)
reports[-1].sigmax = ValErr(1.07017, 0.00371728, 0)
reports[-1].sigmay = ValErr(1.53888, 0.00534538, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0576392, 0.0812126, 0.000584329, 0.000947746, -0.0557606, 0.0750567, 0.000588386, 0.00101839, -0.0557606, 0.0750567, 0.000588386, 0.00101839, -0.0624431, 0.0705223, 0.000636297, 0.000755632, -0.0624431, 0.0705223, 0.000636297, 0.000755632, 1.07016, 1.53891, 0.0052348, 0.0349465, 1.07016, 1.53891, 0.0052348, 0.0349465)

reports.append(Report(579239936, ("DT", 2, 2, 1), "MBwhEst2sec01"))
reports[-1].posNum = 47604
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.0907997, 0.00672032, 0), \
                           ValErr(0.0419382, 0.00859066, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000142244, 0.000103413, 0), \
                           -181258, 47604, 47604, -nan)
reports[-1].sigmax = ValErr(1.40723, 0.00456116, 0)
reports[-1].sigmay = ValErr(1.8741, 0.00607445, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0861034, 0.0467583, 0.00453704, 0.00494485, -0.0882034, 0.0417496, 0.00457092, 0.00483866, -0.0882034, 0.0417496, 0.00457092, 0.00483866, -0.0879464, 0.0321535, 0.0045501, 0.00484156, -0.0879464, 0.0321535, 0.0045501, 0.00484156, 1.40734, 1.87399, 0.0055771, 0.0239432, 1.40734, 1.87399, 0.0055771, 0.0239432)

reports.append(Report(579502080, ("DT", 2, 2, 2), "MBwhEst2sec02"))
reports[-1].posNum = 46825
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.0105046, 0.00661241, 0), \
                           ValErr(-0.0352425, 0.00863281, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000359134, 0.000100895, 0), \
                           -177820, 46825, 46825, -nan)
reports[-1].sigmax = ValErr(1.39897, 0.00457145, 0)
reports[-1].sigmay = ValErr(1.86624, 0.00609838, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0098057, -0.0382602, 0.00147244, 0.0045255, -0.00556281, -0.0365999, 0.00145877, 0.00438423, -0.00556281, -0.0365999, 0.00145877, 0.00438423, -0.00192224, -0.0455115, 0.00144957, 0.00445699, -0.00192224, -0.0455115, 0.00144957, 0.00445699, 1.39908, 1.86634, 0.00556656, 0.0235202, 1.39908, 1.86634, 0.00556656, 0.0235202)

reports.append(Report(579764224, ("DT", 2, 2, 3), "MBwhEst2sec03"))
reports[-1].posNum = 54889
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.0361594, 0.00606302, 0), \
                           ValErr(0.0998697, 0.00794007, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(8.46564e-06, 9.28205e-05, 0), \
                           -207407, 54889, 54889, -nan)
reports[-1].sigmax = ValErr(1.38438, 0.0041784, 0)
reports[-1].sigmay = ValErr(1.85065, 0.00558566, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0314145, 0.0974683, 0.00098964, 0.00636658, -0.0360352, 0.0997962, 0.00100966, 0.00626301, -0.0360352, 0.0997962, 0.00100966, 0.00626301, -0.0433105, 0.0963616, 0.00105722, 0.00644998, -0.0433105, 0.0963616, 0.00105722, 0.00644998, 1.38438, 1.85065, 0.00554904, 0.0240827, 1.38438, 1.85065, 0.00554904, 0.0240827)

reports.append(Report(580026368, ("DT", 2, 2, 4), "MBwhEst2sec04"))
reports[-1].posNum = 53097
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.00348439, 0.00628211, 0), \
                           ValErr(0.0435889, 0.00810959, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000420721, 9.50932e-05, 0), \
                           -202051, 53097, 53097, -nan)
reports[-1].sigmax = ValErr(1.40817, 0.00432132, 0)
reports[-1].sigmay = ValErr(1.86852, 0.00573398, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000302234, 0.0386568, 0.00160058, 0.0035236, 0.00295779, 0.043122, 0.00160963, 0.00336565, 0.00295779, 0.043122, 0.00160963, 0.00336565, -0.00380688, 0.0368693, 0.00167473, 0.0031895, -0.00380688, 0.0368693, 0.00167473, 0.0031895, 1.40816, 1.86886, 0.00561324, 0.0238155, 1.40816, 1.86886, 0.00561324, 0.0238155)

reports.append(Report(580288512, ("DT", 2, 2, 5), "MBwhEst2sec05"))
reports[-1].posNum = 45495
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.0682531, 0.00673325, 0), \
                           ValErr(0.055078, 0.00869191, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000371134, 0.000102663, 0), \
                           -172219, 45495, 45495, -nan)
reports[-1].sigmax = ValErr(1.39429, 0.0046226, 0)
reports[-1].sigmay = ValErr(1.84999, 0.00613337, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0778264, 0.0430416, -0.000576669, -0.000403661, 0.0740896, 0.0530234, -0.000543212, -4.87466e-05, 0.0740896, 0.0530234, -0.000543212, -4.87466e-05, 0.0634863, 0.0586272, -0.000465916, 4.92662e-05, 0.0634863, 0.0586272, -0.000465916, 4.92662e-05, 1.3942, 1.85038, 0.00557355, 0.0277158, 1.3942, 1.85038, 0.00557355, 0.0277158)

reports.append(Report(580550656, ("DT", 2, 2, 6), "MBwhEst2sec06"))
reports[-1].posNum = 60167
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.0204759, 0.00574093, 0), \
                           ValErr(0.000320468, 0.00762025, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000294155, 8.85131e-05, 0), \
                           -228072, 60167, 60167, -nan)
reports[-1].sigmax = ValErr(1.39015, 0.00400826, 0)
reports[-1].sigmay = ValErr(1.86517, 0.00537782, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0257765, 0.00831865, -0.00069636, 0.00223714, 0.023522, -0.00133494, -0.000682665, 0.00202606, 0.023522, -0.00133494, -0.000682665, 0.00202606, 0.0272072, -0.00519583, -0.00067774, 0.00217292, 0.0272072, -0.00519583, -0.00067774, 0.00217292, 1.38996, 1.86561, 0.00557251, 0.0245264, 1.38996, 1.86561, 0.00557251, 0.0245264)

reports.append(Report(580812800, ("DT", 2, 2, 7), "MBwhEst2sec07"))
reports[-1].posNum = 56781
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.0485898, 0.00602033, 0), \
                           ValErr(0.00374971, 0.00788244, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00012432, 9.02193e-05, 0), \
                           -216248, 56781, 56781, -nan)
reports[-1].sigmax = ValErr(1.40574, 0.00417182, 0)
reports[-1].sigmay = ValErr(1.87764, 0.00557223, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0487411, 0.0110064, 0.00153232, 0.00525886, 0.0469347, 0.0040378, 0.0015367, 0.00510435, 0.0469347, 0.0040378, 0.0015367, 0.00510435, 0.0527923, -0.0147642, 0.00153068, 0.00510629, 0.0527923, -0.0147642, 0.00153068, 0.00510629, 1.40583, 1.87755, 0.00561793, 0.0255328, 1.40583, 1.87755, 0.00561793, 0.0255328)

reports.append(Report(581074944, ("DT", 2, 2, 8), "MBwhEst2sec08"))
reports[-1].posNum = 57456
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.122241, 0.00599457, 0), \
                           ValErr(0.0449811, 0.00784572, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.72673e-05, 9.14219e-05, 0), \
                           -219138, 57456, 57456, -nan)
reports[-1].sigmax = ValErr(1.4117, 0.00416562, 0)
reports[-1].sigmay = ValErr(1.88014, 0.00554777, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.123605, 0.0357578, -0.000545922, 0.00173401, 0.121052, 0.044793, -0.000535245, 0.0017288, 0.121052, 0.044793, -0.000535245, 0.0017288, 0.121955, 0.0466191, -0.000530697, 0.00181418, 0.121955, 0.0466191, -0.000530697, 0.00181418, 1.41181, 1.88001, 0.00562483, 0.0255802, 1.41181, 1.88001, 0.00562483, 0.0255802)

reports.append(Report(581337088, ("DT", 2, 2, 9), "MBwhEst2sec09"))
reports[-1].posNum = 41249
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.0433153, 0.00709577, 0), \
                           ValErr(-0.0802219, 0.00942177, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000486541, 0.000118878, 0), \
                           -156305, 41249, 41249, -nan)
reports[-1].sigmax = ValErr(1.39528, 0.00485817, 0)
reports[-1].sigmay = ValErr(1.85584, 0.0064617, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0533986, -0.0568577, -0.00187284, 0.00225843, 0.0505838, -0.0708177, -0.00187068, 0.00275531, 0.0505838, -0.0708177, -0.00187068, 0.00275531, 0.052834, -0.077267, -0.00186303, 0.00285682, 0.052834, -0.077267, -0.00186303, 0.00285682, 1.39523, 1.85629, 0.00555199, 0.0262075, 1.39523, 1.85629, 0.00555199, 0.0262075)

reports.append(Report(581599232, ("DT", 2, 2, 10), "MBwhEst2sec10"))
reports[-1].posNum = 52923
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.0726771, 0.00616961, 0), \
                           ValErr(-0.013631, 0.00819032, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(8.32281e-05, 9.60509e-05, 0), \
                           -201266, 52923, 52923, -nan)
reports[-1].sigmax = ValErr(1.39899, 0.00430012, 0)
reports[-1].sigmay = ValErr(1.87642, 0.00576765, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0790594, -0.0115809, 0.000444402, 0.00265736, 0.0735748, -0.0142772, 0.000476604, 0.00278394, 0.0735748, -0.0142772, 0.000476604, 0.00278394, 0.0700846, -0.0208418, 0.000512804, 0.00293807, 0.0700846, -0.0208418, 0.000512804, 0.00293807, 1.39901, 1.87641, 0.00561185, 0.025469, 1.39901, 1.87641, 0.00561185, 0.025469)

reports.append(Report(581861376, ("DT", 2, 2, 11), "MBwhEst2sec11"))
reports[-1].posNum = 54233
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.00463161, 0.00606646, 0), \
                           ValErr(-0.0525809, 0.0079879, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000378373, 9.23588e-05, 0), \
                           -204954, 54233, 54233, -nan)
reports[-1].sigmax = ValErr(1.38247, 0.00419785, 0)
reports[-1].sigmay = ValErr(1.85411, 0.00563001, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0121346, -0.0373654, -0.000667574, 0.00294717, -0.00974408, -0.0499291, -0.000675615, 0.0028016, -0.00974408, -0.0499291, -0.000675615, 0.0028016, -0.0137333, -0.0602929, -0.000670487, 0.00304181, -0.0137333, -0.0602929, -0.000670487, 0.00304181, 1.38243, 1.85444, 0.00555318, 0.0250787, 1.38243, 1.85444, 0.00555318, 0.0250787)

reports.append(Report(582123520, ("DT", 2, 2, 12), "MBwhEst2sec12"))
reports[-1].posNum = 62922
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.0369057, 0.00565248, 0), \
                           ValErr(0.0576138, 0.00747813, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000126125, 8.64334e-05, 0), \
                           -239234, 62922, 62922, -nan)
reports[-1].sigmax = ValErr(1.39935, 0.0039447, 0)
reports[-1].sigmay = ValErr(1.87421, 0.0052833, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0489331, 0.068032, 0.000416548, 0.00377894, -0.0382307, 0.0580694, 0.00043198, 0.00462171, -0.0382307, 0.0580694, 0.00043198, 0.00462171, -0.0441316, 0.050086, 0.000462934, 0.00478332, -0.0441316, 0.050086, 0.000462934, 0.00478332, 1.39935, 1.87425, 0.00556369, 0.0254977, 1.39935, 1.87425, 0.00556369, 0.0254977)

reports.append(Report(583434240, ("DT", 2, 3, 1), "MBwhEst3sec01"))
reports[-1].posNum = 48746
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.18077, 0.00844412, 0), \
                           ValErr(0.0762919, 0.0104537, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000360746, 0.00011173, 0), \
                           -209332, 48746, 48746, -nan)
reports[-1].sigmax = ValErr(1.86339, 0.00596787, 0)
reports[-1].sigmay = ValErr(2.30269, 0.0073748, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.173646, 0.0754243, 0.00155684, 0.00345113, -0.179905, 0.0785817, 0.00156528, 0.00362276, -0.179905, 0.0785817, 0.00156528, 0.00362276, -0.175724, 0.0755266, 0.00155951, 0.00386591, -0.175724, 0.0755266, 0.00155951, 0.00386591, 1.86346, 2.30284, 0.00651166, 0.0195743, 1.86346, 2.30284, 0.00651166, 0.0195743)

reports.append(Report(583696384, ("DT", 2, 3, 2), "MBwhEst3sec02"))
reports[-1].posNum = 43848
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.0380795, 0.00872636, 0), \
                           ValErr(-0.0437763, 0.0110908, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000164878, 0.000119091, 0), \
                           -187556, 43848, 43848, -nan)
reports[-1].sigmax = ValErr(1.82699, 0.00616949, 0)
reports[-1].sigmay = ValErr(2.30911, 0.00779754, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0380355, -0.0383286, 0.000661938, -0.0013905, 0.0382981, -0.0454271, 0.000628746, -0.00160151, 0.0382981, -0.0454271, 0.000628746, -0.00160151, 0.0401458, -0.0386959, 0.000622383, -0.00156379, 0.0401458, -0.0386959, 0.000622383, -0.00156379, 1.82699, 2.30916, 0.00636051, 0.0204403, 1.82699, 2.30916, 0.00636051, 0.0204403)

reports.append(Report(583958528, ("DT", 2, 3, 3), "MBwhEst3sec03"))
reports[-1].posNum = 56787
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.0193676, 0.00766218, 0), \
                           ValErr(0.070324, 0.00951821, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000251971, 0.000103349, 0), \
                           -241780, 56787, 56787, -nan)
reports[-1].sigmax = ValErr(1.82388, 0.00541207, 0)
reports[-1].sigmay = ValErr(2.26783, 0.00672938, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0262858, 0.0809873, -0.000180795, -0.00219717, -0.0184824, 0.0707493, -0.000199141, -0.00222127, -0.0184824, 0.0707493, -0.000199141, -0.00222127, -0.0169167, 0.0619956, -0.00019039, -0.00205929, -0.0169167, 0.0619956, -0.00019039, -0.00205929, 1.82386, 2.26796, 0.00632926, 0.0193151, 1.82386, 2.26796, 0.00632926, 0.0193151)

reports.append(Report(584220672, ("DT", 2, 3, 4), "MBwhEst3sec04"))
reports[-1].posNum = 53437
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.00481199, 0.00799686, 0), \
                           ValErr(-0.0457414, 0.00984727, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000404309, 0.000106795, 0), \
                           -228377, 53437, 53437, -nan)
reports[-1].sigmax = ValErr(1.84668, 0.00564878, 0)
reports[-1].sigmay = ValErr(2.2762, 0.00696265, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00120752, -0.036228, -0.000117351, 0.00172142, -0.00343723, -0.0453293, -0.000120753, 0.00185552, -0.00343723, -0.0453293, -0.000120753, 0.00185552, -0.00277148, -0.0597752, -0.000157273, 0.00198643, -0.00277148, -0.0597752, -0.000157273, 0.00198643, 1.8468, 2.27635, 0.0064302, 0.0194909, 1.8468, 2.27635, 0.0064302, 0.0194909)

reports.append(Report(584482816, ("DT", 2, 3, 5), "MBwhEst3sec05"))
reports[-1].posNum = 52441
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.0456094, 0.00800057, 0), \
                           ValErr(0.00700172, 0.00999656, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000134278, 0.000105269, 0), \
                           -223887, 52441, 52441, -nan)
reports[-1].sigmax = ValErr(1.83076, 0.00565315, 0)
reports[-1].sigmay = ValErr(2.28579, 0.00705816, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.0429206, 0.00457588, -0.000417103, -0.00298905, 0.0452154, 0.00630471, -0.000439047, -0.00285032, 0.0452154, 0.00630471, -0.000439047, -0.00285032, 0.046073, 0.00121808, -0.000431262, -0.00260631, 0.046073, 0.00121808, -0.000431262, -0.00260631, 1.83082, 2.28576, 0.00635137, 0.0199665, 1.83082, 2.28576, 0.00635137, 0.0199665)

reports.append(Report(584744960, ("DT", 2, 3, 6), "MBwhEst3sec06"))
reports[-1].posNum = 59753
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.125288, 0.00753804, 0), \
                           ValErr(-0.0884939, 0.0093772, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000516311, 0.000101618, 0), \
                           -255259, 59753, 59753, -nan)
reports[-1].sigmax = ValErr(1.83693, 0.00531376, 0)
reports[-1].sigmay = ValErr(2.28399, 0.00660698, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.120873, -0.0748252, -0.00128945, 0.000358178, 0.128297, -0.0844649, -0.00132035, 0.000608516, 0.128297, -0.0844649, -0.00132035, 0.000608516, 0.120414, -0.0974142, -0.00129162, 0.000908433, 0.120414, -0.0974142, -0.00129162, 0.000908433, 1.83698, 2.28443, 0.00646072, 0.0197564, 1.83698, 2.28443, 0.00646072, 0.0197564)

reports.append(Report(585007104, ("DT", 2, 3, 7), "MBwhEst3sec07"))
reports[-1].posNum = 61156
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.0248633, 0.00754193, 0), \
                           ValErr(-0.0396984, 0.00927615, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000359278, 9.97818e-05, 0), \
                           -262301, 61156, 61156, -nan)
reports[-1].sigmax = ValErr(1.86058, 0.00532012, 0)
reports[-1].sigmay = ValErr(2.29396, 0.00655935, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0203359, -0.0313631, 0.000998092, 0.000656185, -0.0229752, -0.0396228, 0.00100561, 0.000816846, -0.0229752, -0.0396228, 0.00100561, 0.000816846, -0.0148251, -0.0476701, 0.000991947, 0.000956123, -0.0148251, -0.0476701, 0.000991947, 0.000956123, 1.86078, 2.29396, 0.00647684, 0.0198871, 1.86078, 2.29396, 0.00647684, 0.0198871)

reports.append(Report(585269248, ("DT", 2, 3, 8), "MBwhEst3sec08"))
reports[-1].posNum = 55383
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.134845, 0.00778466, 0), \
                           ValErr(-0.0783638, 0.00970314, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000143406, 0.000103769, 0), \
                           -236064, 55383, 55383, -nan)
reports[-1].sigmax = ValErr(1.82736, 0.00549068, 0)
reports[-1].sigmay = ValErr(2.27422, 0.00683336, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.140001, -0.0744083, -0.00161347, -0.00232193, 0.134075, -0.07958, -0.00163944, -0.00187175, 0.134075, -0.07958, -0.00163944, -0.00187175, 0.135302, -0.0820178, -0.0016593, -0.00173687, 0.135302, -0.0820178, -0.0016593, -0.00173687, 1.82741, 2.27419, 0.0063622, 0.0230731, 1.82741, 2.27419, 0.0063622, 0.0230731)

reports.append(Report(585531392, ("DT", 2, 3, 9), "MBwhEst3sec09"))
reports[-1].posNum = 55598
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.0440517, 0.00781816, 0), \
                           ValErr(0.103241, 0.00982315, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000198803, 0.000105322, 0), \
                           -238422, 55598, 55598, -nan)
reports[-1].sigmax = ValErr(1.84291, 0.00552711, 0)
reports[-1].sigmay = ValErr(2.3143, 0.00694078, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0494687, 0.0977197, -0.000904292, 0.00154259, -0.0444171, 0.102501, -0.000932713, 0.00158863, -0.0444171, 0.102501, -0.000932713, 0.00158863, -0.0428627, 0.100129, -0.000951469, 0.00162411, -0.0428627, 0.100129, -0.000951469, 0.00162411, 1.84306, 2.31417, 0.00641834, 0.0197863, 1.84306, 2.31417, 0.00641834, 0.0197863)

reports.append(Report(585793536, ("DT", 2, 3, 10), "MBwhEst3sec10"))
reports[-1].posNum = 59399
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(0.124267, 0.0075501, 0), \
                           ValErr(-0.16585, 0.00943066, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000510091, 0.000101932, 0), \
                           -254107, 59399, 59399, -nan)
reports[-1].sigmax = ValErr(1.83941, 0.00533676, 0)
reports[-1].sigmay = ValErr(2.29481, 0.006658, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(0.128238, -0.167228, -3.32022e-06, 0.00198967, 0.123233, -0.1685, -2.74475e-06, 0.00210742, 0.123233, -0.1685, -2.74475e-06, 0.00210742, 0.12543, -0.182129, -1.24831e-05, 0.00224281, 0.12543, -0.182129, -1.24831e-05, 0.00224281, 1.83966, 2.29498, 0.00639786, 0.0198618, 1.83966, 2.29498, 0.00639786, 0.0198618)

reports.append(Report(586055680, ("DT", 2, 3, 11), "MBwhEst3sec11"))
reports[-1].posNum = 49380
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.104475, 0.00826777, 0), \
                           ValErr(-0.0880723, 0.010277, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000501431, 0.000106273, 0), \
                           -210902, 49380, 49380, -nan)
reports[-1].sigmax = ValErr(1.83593, 0.00584216, 0)
reports[-1].sigmay = ValErr(2.28322, 0.00726555, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.107131, -0.0682591, 0.000780758, -0.00132773, -0.105947, -0.0870854, 0.000758813, -0.00114246, -0.105947, -0.0870854, 0.000758813, -0.00114246, -0.10399, -0.100448, 0.000730015, -0.00107922, -0.10399, -0.100448, 0.000730015, -0.00107922, 1.8359, 2.28376, 0.00642965, 0.0192223, 1.8359, 2.28376, 0.00642965, 0.0192223)

reports.append(Report(586317824, ("DT", 2, 3, 12), "MBwhEst3sec12"))
reports[-1].posNum = 57277
reports[-1].negNum = 0
reports[-1].fittype = "6DOF"
reports[-1].add_parameters(ValErr(-0.226034, 0.00766394, 0), \
                           ValErr(0.0292714, 0.00959503, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000444211, 0.000103828, 0), \
                           -244858, 57277, 57277, -nan)
reports[-1].sigmax = ValErr(1.83668, 0.00542897, 0)
reports[-1].sigmay = ValErr(2.29136, 0.00674042, 0)
reports[-1].sigmadxdz = ValErr(0, 0, 0)
reports[-1].sigmadydz = ValErr(0, 0, 0)
reports[-1].add_stats(-0.225148, 0.0359628, 0.00139658, 0.000135931, -0.224851, 0.0339921, 0.00139102, 0.000176088, -0.224851, 0.0339921, 0.00139102, 0.000176088, -0.225043, 0.0223966, 0.00140894, 0.000346893, -0.225043, 0.0223966, 0.00140894, 0.000346893, 1.83669, 2.2917, 0.00634113, 0.0202774, 1.83669, 2.2917, 0.00634113, 0.0202774)

reports.append(Report(587497472, ("DT", -2, 4, 1), "MBwhAst4sec01"))
reports[-1].posNum = 83435
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.120946, 0.00895852, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000588527, 0.00018302, 0), \
                           -197715, 83435, 83435, -nan)
reports[-1].sigmaresid = ValErr(2.58767, 0.00633462, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.114223, None, -0.00152808, None, 0.121041, None, -0.0015691, None, 0.121041, None, -0.0015691, None, 0.120553, None, -0.00151876, None, 0.120553, None, -0.00151876, None, 2.58782, None, 0.00796681, None, 2.58782, None, 0.00796681, None)

reports.append(Report(587759616, ("DT", -2, 4, 2), "MBwhAst4sec02"))
reports[-1].posNum = 96906
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.0319703, 0.00828967, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.26256e-05, 0.000169265, 0), \
                           -229366, 96906, 96906, -nan)
reports[-1].sigmaresid = ValErr(2.58042, 0.00586139, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0302607, None, -0.000459708, None, -0.0319507, None, -0.000502167, None, -0.0319507, None, -0.000502167, None, -0.0304454, None, -0.000552861, None, -0.0304454, None, -0.000552861, None, 2.58042, None, 0.0079992, None, 2.58042, None, 0.0079992, None)

reports.append(Report(588021760, ("DT", -2, 4, 3), "MBwhAst4sec03"))
reports[-1].posNum = 83765
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.0358895, 0.00888746, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000214457, 0.000181685, 0), \
                           -197961, 83765, 83765, -nan)
reports[-1].sigmaresid = ValErr(2.57115, 0.00628176, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.031344, None, -0.000262849, None, 0.0361952, None, -0.000321261, None, 0.0361952, None, -0.000321261, None, 0.0369181, None, -0.000339132, None, 0.0369181, None, -0.000339132, None, 2.57118, None, 0.00790923, None, 2.57118, None, 0.00790923, None)

reports.append(Report(588283904, ("DT", -2, 4, 4), "MBwhAst4sec04"))
reports[-1].posNum = 63229
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.0541867, 0.0107281, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000323122, 0.000216152, 0), \
                           -152449, 63229, 63229, -nan)
reports[-1].sigmaresid = ValErr(2.69696, 0.00758406, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0555758, None, -0.00309573, None, -0.0545602, None, -0.00313117, None, -0.0545602, None, -0.00313117, None, -0.0321459, None, -0.00324634, None, -0.0321459, None, -0.00324634, None, 2.697, None, 0.00830807, None, 2.697, None, 0.00830807, None)

reports.append(Report(590643200, ("DT", -2, 4, 13), "MBwhAst4sec13"))
reports[-1].posNum = 68463
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.0339648, 0.0100185, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000345571, 0.000204602, 0), \
                           -163105, 68463, 68463, -nan)
reports[-1].sigmaresid = ValErr(2.6207, 0.00708229, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0533482, None, 0.00092814, None, 0.0335812, None, 0.000968385, None, 0.0335812, None, 0.000968385, None, 0.0327622, None, 0.00105372, None, 0.0327622, None, 0.00105372, None, 2.62075, None, 0.00810629, None, 2.62075, None, 0.00810629, None)

reports.append(Report(588546048, ("DT", -2, 4, 5), "MBwhAst4sec05"))
reports[-1].posNum = 92012
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.0446, 0.00849947, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00159998, 0.000172651, 0), \
                           -217651, 92012, 92012, -nan)
reports[-1].sigmaresid = ValErr(2.57673, 0.00600663, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0400595, None, -0.000218217, None, 0.0419577, None, -0.000179823, None, 0.0419577, None, -0.000179823, None, 0.0569918, None, -0.000149104, None, 0.0569918, None, -0.000149104, None, 2.57793, None, 0.00791449, None, 2.57793, None, 0.00791449, None)

reports.append(Report(588808192, ("DT", -2, 4, 6), "MBwhAst4sec06"))
reports[-1].posNum = 96650
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.0955687, 0.00834389, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.201e-05, 0.000169625, 0), \
                           -229226, 96650, 96650, -nan)
reports[-1].sigmaresid = ValErr(2.59288, 0.00589748, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0924331, None, 0.00108875, None, -0.0956738, None, 0.00114648, None, -0.0956738, None, 0.00114648, None, -0.100144, None, 0.00119487, None, -0.100144, None, 0.00119487, None, 2.59289, None, 0.00799943, None, 2.59289, None, 0.00799943, None)

reports.append(Report(589070336, ("DT", -2, 4, 7), "MBwhAst4sec07"))
reports[-1].posNum = 106528
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.0903646, 0.00795658, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000648249, 0.000162689, 0), \
                           -252805, 106528, 106528, -nan)
reports[-1].sigmaresid = ValErr(2.59657, 0.00562539, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.102393, None, -0.000441764, None, -0.090885, None, -0.000462122, None, -0.090885, None, -0.000462122, None, -0.0912596, None, -0.000414063, None, -0.0912596, None, -0.000414063, None, 2.59676, None, 0.00802639, None, 2.59676, None, 0.00802639, None)

reports.append(Report(589332480, ("DT", -2, 4, 8), "MBwhAst4sec08"))
reports[-1].posNum = 105735
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.0315363, 0.00788302, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000449973, 0.000160284, 0), \
                           -249536, 105735, 105735, -nan)
reports[-1].sigmaresid = ValErr(2.56275, 0.00557292, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0309187, None, -0.00115334, None, -0.0320063, None, -0.00111054, None, -0.0320063, None, -0.00111054, None, -0.0349465, None, -0.0010881, None, -0.0349465, None, -0.0010881, None, 2.56284, None, 0.00790158, None, 2.56284, None, 0.00790158, None)

reports.append(Report(589594624, ("DT", -2, 4, 9), "MBwhAst4sec09"))
reports[-1].posNum = 35144
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.0993819, 0.0134431, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000496951, 0.000274654, 0), \
                           -82333.8, 35144, 35144, -nan)
reports[-1].sigmaresid = ValErr(2.51889, 0.00950096, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.116142, None, 0.000709031, None, -0.0986145, None, 0.000659145, None, -0.0986145, None, 0.000659145, None, -0.107572, None, 0.000712232, None, -0.107572, None, 0.000712232, None, 2.519, None, 0.00761277, None, 2.519, None, 0.00761277, None)

reports.append(Report(589856768, ("DT", -2, 4, 10), "MBwhAst4sec10"))
reports[-1].posNum = 49791
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.0811387, 0.0116836, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000901892, 0.000237774, 0), \
                           -118316, 49791, 49791, -nan)
reports[-1].sigmaresid = ValErr(2.60468, 0.00825399, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0875062, None, -0.000790585, None, 0.0792461, None, -0.000812567, None, 0.0792461, None, -0.000812567, None, 0.0818409, None, -0.000832896, None, 0.0818409, None, -0.000832896, None, 2.60506, None, 0.00814175, None, 2.60506, None, 0.00814175, None)

reports.append(Report(590905344, ("DT", -2, 4, 14), "MBwhAst4sec14"))
reports[-1].posNum = 50802
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.028782, 0.0115231, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.30523e-05, 0.000236222, 0), \
                           -120563, 50802, 50802, -nan)
reports[-1].sigmaresid = ValErr(2.59675, 0.00814656, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0220048, None, 0.000646999, None, -0.0287243, None, 0.000606436, None, -0.0287243, None, 0.000606436, None, -0.0469865, None, 0.000613395, None, -0.0469865, None, 0.000613395, None, 2.59675, None, 0.00823169, None, 2.59675, None, 0.00823169, None)

reports.append(Report(590118912, ("DT", -2, 4, 11), "MBwhAst4sec11"))
reports[-1].posNum = 36020
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.15969, 0.0131833, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00108795, 0.000268294, 0), \
                           -84062.6, 36020, 36020, -nan)
reports[-1].sigmaresid = ValErr(2.49637, 0.00930079, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.163729, None, -0.000831903, None, 0.156094, None, -0.000796328, None, 0.156094, None, -0.000796328, None, 0.14235, None, -0.000746234, None, 0.14235, None, -0.000746234, None, 2.49694, None, 0.00753678, None, 2.49694, None, 0.00753678, None)

reports.append(Report(590381056, ("DT", -2, 4, 12), "MBwhAst4sec12"))
reports[-1].posNum = 103088
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.0554538, 0.00802863, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.46769e-05, 0.000163377, 0), \
                           -243889, 103088, 103088, -nan)
reports[-1].sigmaresid = ValErr(2.5777, 0.00567693, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0499087, None, 0.000400902, None, 0.0554458, None, 0.000356969, None, 0.0554458, None, 0.000356969, None, 0.0639553, None, 0.000352564, None, 0.0639553, None, 0.000352564, None, 2.5777, None, 0.00799618, None, 2.5777, None, 0.00799618, None)

reports.append(Report(587530240, ("DT", -1, 4, 1), "MBwhBst4sec01"))
reports[-1].posNum = 115756
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.0978586, 0.00732075, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.13472e-05, 0.000151044, 0), \
                           -269818, 115756, 115756, -nan)
reports[-1].sigmaresid = ValErr(2.48925, 0.00517346, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0969, None, -0.00147077, None, 0.0977566, None, -0.00152113, None, 0.0977566, None, -0.00152113, None, 0.098664, None, -0.00147962, None, 0.098664, None, -0.00147962, None, 2.48925, None, 0.0078733, None, 2.48925, None, 0.0078733, None)

reports.append(Report(587792384, ("DT", -1, 4, 2), "MBwhBst4sec02"))
reports[-1].posNum = 110189
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.0535079, 0.00735474, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000542565, 0.000152083, 0), \
                           -254577, 110189, 110189, -nan)
reports[-1].sigmaresid = ValErr(2.43862, 0.00519469, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0547334, None, -0.000904509, None, 0.0547567, None, -0.000954274, None, 0.0547567, None, -0.000954274, None, 0.0617477, None, -0.000929334, None, 0.0617477, None, -0.000929334, None, 2.43876, None, 0.00780343, None, 2.43876, None, 0.00780343, None)

reports.append(Report(588054528, ("DT", -1, 4, 3), "MBwhBst4sec03"))
reports[-1].posNum = 72653
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.070284, 0.00908029, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000542805, 0.000246394, 0), \
                           -167911, 72653, 72653, -nan)
reports[-1].sigmaresid = ValErr(2.44049, 0.00640227, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0735495, None, -0.000750771, None, 0.0717994, None, -0.000777, None, 0.0717994, None, -0.000777, None, 0.0725003, None, -0.000731831, None, 0.0725003, None, -0.000731831, None, 2.44057, None, 0.00770908, None, 2.44057, None, 0.00770908, None)

reports.append(Report(588316672, ("DT", -1, 4, 4), "MBwhBst4sec04"))
reports[-1].posNum = 74906
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.0625405, 0.00925633, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00053952, 0.000192227, 0), \
                           -175433, 74906, 74906, -nan)
reports[-1].sigmaresid = ValErr(2.5171, 0.00650319, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0516133, None, 5.8731e-05, None, -0.0596038, None, 7.43703e-05, None, -0.0596038, None, 7.43703e-05, None, -0.0608281, None, 4.77216e-05, None, -0.0608281, None, 4.77216e-05, None, 2.51724, None, 0.0078487, None, 2.51724, None, 0.0078487, None)

reports.append(Report(590675968, ("DT", -1, 4, 13), "MBwhBst4sec13"))
reports[-1].posNum = 77126
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.0878504, 0.00894115, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000993474, 0.000184678, 0), \
                           -179490, 77126, 77126, -nan)
reports[-1].sigmaresid = ValErr(2.4801, 0.00631471, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0847363, None, 0.0010043, None, -0.0854876, None, 0.00101103, None, -0.0854876, None, 0.00101103, None, -0.0830283, None, 0.000971563, None, -0.0830283, None, 0.000971563, None, 2.48056, None, 0.00780818, None, 2.48056, None, 0.00780818, None)

reports.append(Report(588578816, ("DT", -1, 4, 5), "MBwhBst4sec05"))
reports[-1].posNum = 103425
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.0768624, 0.00755649, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000939685, 0.000155375, 0), \
                           -238587, 103425, 103425, -nan)
reports[-1].sigmaresid = ValErr(2.43008, 0.00534139, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0780738, None, 0.000736802, None, -0.0769894, None, 0.000845403, None, -0.0769894, None, 0.000845403, None, -0.0680192, None, 0.00088384, None, -0.0680192, None, 0.00088384, None, 2.43051, None, 0.00771002, None, 2.43051, None, 0.00771002, None)

reports.append(Report(588840960, ("DT", -1, 4, 6), "MBwhBst4sec06"))
reports[-1].posNum = 109776
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.107512, 0.00743691, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000104524, 0.000152592, 0), \
                           -254586, 109776, 109776, -nan)
reports[-1].sigmaresid = ValErr(2.4601, 0.0052503, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.108881, None, 0.00104906, None, -0.107225, None, 0.00112709, None, -0.107225, None, 0.00112709, None, -0.103776, None, 0.00115088, None, -0.103776, None, 0.00115088, None, 2.46011, None, 0.0077184, None, 2.46011, None, 0.0077184, None)

reports.append(Report(589103104, ("DT", -1, 4, 7), "MBwhBst4sec07"))
reports[-1].posNum = 124567
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.0898524, 0.00696614, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.38161e-05, 0.00014316, 0), \
                           -288757, 124567, 124567, -nan)
reports[-1].sigmaresid = ValErr(2.45751, 0.00492356, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0905717, None, -0.00103152, None, -0.0899026, None, -0.000988589, None, -0.0899026, None, -0.000988589, None, -0.0960676, None, -0.000975866, None, -0.0960676, None, -0.000975866, None, 2.45751, None, 0.00774263, None, 2.45751, None, 0.00774263, None)

reports.append(Report(589365248, ("DT", -1, 4, 8), "MBwhBst4sec08"))
reports[-1].posNum = 124777
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.102354, 0.00687, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000329824, 0.00014118, 0), \
                           -287613, 124777, 124777, -nan)
reports[-1].sigmaresid = ValErr(2.4256, 0.00485553, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.101801, None, 0.00135752, None, -0.102847, None, 0.00138183, None, -0.102847, None, 0.00138183, None, -0.106762, None, 0.00141098, None, -0.106762, None, 0.00141098, None, 2.42565, None, 0.00755817, None, 2.42565, None, 0.00755817, None)

reports.append(Report(589627392, ("DT", -1, 4, 9), "MBwhBst4sec09"))
reports[-1].posNum = 41253
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.0294557, 0.0118376, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00199459, 0.000245245, 0), \
                           -94448.5, 41253, 41253, -nan)
reports[-1].sigmaresid = ValErr(2.38824, 0.0083145, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0247271, None, -0.00238144, None, -0.0183434, None, -0.00240925, None, -0.0183434, None, -0.00240925, None, -0.0105942, None, -0.00244541, None, -0.0105942, None, -0.00244541, None, 2.39015, None, 0.00712732, None, 2.39015, None, 0.00712732, None)

reports.append(Report(589889536, ("DT", -1, 4, 10), "MBwhBst4sec10"))
reports[-1].posNum = 48017
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.0803732, 0.0113567, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.50691e-05, 0.000234303, 0), \
                           -111508, 48017, 48017, -nan)
reports[-1].sigmaresid = ValErr(2.46778, 0.00796331, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0962435, None, 0.000130821, None, 0.0805993, None, 0.000105887, None, 0.0805993, None, 0.000105887, None, 0.0902419, None, 7.37999e-05, None, 0.0902419, None, 7.37999e-05, None, 2.46778, None, 0.00774044, None, 2.46778, None, 0.00774044, None)

reports.append(Report(590938112, ("DT", -1, 4, 14), "MBwhBst4sec14"))
reports[-1].posNum = 51125
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.106623, 0.0108615, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000224811, 0.00022434, 0), \
                           -118316, 51125, 51125, -nan)
reports[-1].sigmaresid = ValErr(2.4481, 0.00765592, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.104051, None, -0.00122377, None, 0.105756, None, -0.00125879, None, 0.105756, None, -0.00125879, None, 0.113565, None, -0.00133309, None, 0.113565, None, -0.00133309, None, 2.44813, None, 0.00779588, None, 2.44813, None, 0.00779588, None)

reports.append(Report(590151680, ("DT", -1, 4, 11), "MBwhBst4sec11"))
reports[-1].posNum = 40499
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.231686, 0.011728, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000486416, 0.000239707, 0), \
                           -92152.4, 40499, 40499, -nan)
reports[-1].sigmaresid = ValErr(2.35486, 0.00827423, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.231508, None, -0.000571194, None, 0.233278, None, -0.000585258, None, 0.233278, None, -0.000585258, None, 0.23547, None, -0.000597116, None, 0.23547, None, -0.000597116, None, 2.35499, None, 0.00720241, None, 2.35499, None, 0.00720241, None)

reports.append(Report(590413824, ("DT", -1, 4, 12), "MBwhBst4sec12"))
reports[-1].posNum = 83107
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.0033253, 0.00876391, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000498548, 0.000181207, 0), \
                           -194628, 83107, 83107, -nan)
reports[-1].sigmaresid = ValErr(2.51671, 0.00617304, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0055838, None, -0.000831301, None, 0.00544209, None, -0.000934746, None, 0.00544209, None, -0.000934746, None, -0.00204119, None, -0.000919125, None, -0.00204119, None, -0.000919125, None, 2.51683, None, 0.00796188, None, 2.51683, None, 0.00796188, None)

reports.append(Report(587563008, ("DT", 0, 4, 1), "MBwhCst4sec01"))
reports[-1].posNum = 98203
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.0185385, 0.00785016, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000412417, 0.000160794, 0), \
                           -227502, 98203, 98203, -nan)
reports[-1].sigmaresid = ValErr(2.45398, 0.00553726, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0362097, None, -0.00154932, None, 0.0199238, None, -0.00161228, None, 0.0199238, None, -0.00161228, None, 0.0408559, None, -0.00178123, None, 0.0408559, None, -0.00178123, None, 2.45406, None, 0.00799613, None, 2.45406, None, 0.00799613, None)

reports.append(Report(587825152, ("DT", 0, 4, 2), "MBwhCst4sec02"))
reports[-1].posNum = 72194
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.005373, 0.00896312, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000454422, 0.000183924, 0), \
                           -165756, 72194, 72194, -nan)
reports[-1].sigmaresid = ValErr(2.40379, 0.00632602, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00575202, None, 0.0011403, None, 0.00402329, None, 0.00122082, None, 0.00402329, None, 0.00122082, None, -0.00568221, None, 0.00134472, None, -0.00568221, None, 0.00134472, None, 2.40389, None, 0.0079362, None, 2.40389, None, 0.0079362, None)

reports.append(Report(588087296, ("DT", 0, 4, 3), "MBwhCst4sec03"))
reports[-1].posNum = 95691
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.00886442, 0.007826, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.00106912, 0.000160718, 0), \
                           -220366, 95691, 95691, -nan)
reports[-1].sigmaresid = ValErr(2.42045, 0.00553281, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00590173, None, 0.000812724, None, -0.00787239, None, 0.000961633, None, -0.00787239, None, 0.000961633, None, -0.0228689, None, 0.0010748, None, -0.0228689, None, 0.0010748, None, 2.42101, None, 0.00789731, None, 2.42101, None, 0.00789731, None)

reports.append(Report(588349440, ("DT", 0, 4, 4), "MBwhCst4sec04"))
reports[-1].posNum = 71881
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.0415237, 0.00955493, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000964425, 0.000195644, 0), \
                           -169284, 71881, 71881, -nan)
reports[-1].sigmaresid = ValErr(2.55008, 0.0067256, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0386264, None, -0.000171669, None, -0.0459755, None, -0.000175132, None, -0.0459755, None, -0.000175132, None, -0.0469831, None, -0.000288737, None, -0.0469831, None, -0.000288737, None, 2.55051, None, 0.00840139, None, 2.55051, None, 0.00840139, None)

reports.append(Report(590708736, ("DT", 0, 4, 13), "MBwhCst4sec13"))
reports[-1].posNum = 76157
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.0480695, 0.0089102, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.00106069, 0.000182791, 0), \
                           -176581, 76157, 76157, -nan)
reports[-1].sigmaresid = ValErr(2.45888, 0.0063004, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0407499, None, 0.000544128, None, 0.048325, None, 0.00055505, None, 0.048325, None, 0.00055505, None, 0.0252688, None, 0.000634381, None, 0.0252688, None, 0.000634381, None, 2.45941, None, 0.0080366, None, 2.45941, None, 0.0080366, None)

reports.append(Report(588611584, ("DT", 0, 4, 5), "MBwhCst4sec05"))
reports[-1].posNum = 114787
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.0563779, 0.00715401, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.44184e-05, 0.000146433, 0), \
                           -264199, 114787, 114787, -nan)
reports[-1].sigmaresid = ValErr(2.41743, 0.00504537, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0603773, None, 0.00221795, None, -0.05615, None, 0.00231439, None, -0.05615, None, 0.00231439, None, -0.0616948, None, 0.00236943, None, -0.0616948, None, 0.00236943, None, 2.41743, None, 0.00788109, None, 2.41743, None, 0.00788109, None)

reports.append(Report(588873728, ("DT", 0, 4, 6), "MBwhCst4sec06"))
reports[-1].posNum = 120393
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.107923, 0.00700177, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.4827e-05, 0.000143374, 0), \
                           -277693, 120393, 120393, -nan)
reports[-1].sigmaresid = ValErr(2.42933, 0.00495076, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.11429, None, -0.000876107, None, 0.107934, None, -0.000975914, None, 0.107934, None, -0.000975914, None, 0.125582, None, -0.0011174, None, 0.125582, None, -0.0011174, None, 2.42933, None, 0.00790931, None, 2.42933, None, 0.00790931, None)

reports.append(Report(589135872, ("DT", 0, 4, 7), "MBwhCst4sec07"))
reports[-1].posNum = 128166
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.09298, 0.00684182, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000231759, 0.000139834, 0), \
                           -296675, 128166, 128166, -nan)
reports[-1].sigmaresid = ValErr(2.44938, 0.00483788, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0986857, None, -0.00146032, None, 0.0929473, None, -0.00148842, None, 0.0929473, None, -0.00148842, None, 0.0966576, None, -0.00158615, None, 0.0966576, None, -0.00158615, None, 2.44941, None, 0.00788416, None, 2.44941, None, 0.00788416, None)

reports.append(Report(589398016, ("DT", 0, 4, 8), "MBwhCst4sec08"))
reports[-1].posNum = 125195
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.00645793, 0.00681826, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000799207, 0.000139231, 0), \
                           -287788, 125195, 125195, -nan)
reports[-1].sigmaresid = ValErr(2.41036, 0.00481697, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00586632, None, 0.00198601, None, -0.00810373, None, 0.00205793, None, -0.00810373, None, 0.00205793, None, -0.023426, None, 0.00223997, None, -0.023426, None, 0.00223997, None, 2.41068, None, 0.00785252, None, 2.41068, None, 0.00785252, None)

reports.append(Report(589660160, ("DT", 0, 4, 9), "MBwhCst4sec09"))
reports[-1].posNum = 32624
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.0607992, 0.0130664, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000315021, 0.000271136, 0), \
                           -74304.6, 32624, 32624, -nan)
reports[-1].sigmaresid = ValErr(2.36001, 0.00923999, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0521681, None, -0.000238237, None, -0.06087, None, -0.000243003, None, -0.06087, None, -0.000243003, None, -0.0580447, None, -0.000194488, None, -0.0580447, None, -0.000194488, None, 2.36006, None, 0.00721913, None, 2.36006, None, 0.00721913, None)

reports.append(Report(589922304, ("DT", 0, 4, 10), "MBwhCst4sec10"))
reports[-1].posNum = 39904
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.0563521, 0.0122583, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000546156, 0.000251803, 0), \
                           -92173.6, 39904, 39904, -nan)
reports[-1].sigmaresid = ValErr(2.43743, 0.00862792, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0548878, None, 0.00102878, None, -0.0589286, None, 0.00104223, None, -0.0589286, None, 0.00104223, None, -0.0790011, None, 0.0011091, None, -0.0790011, None, 0.0011091, None, 2.43758, None, 0.00805908, None, 2.43758, None, 0.00805908, None)

reports.append(Report(590970880, ("DT", 0, 4, 14), "MBwhCst4sec14"))
reports[-1].posNum = 38446
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.0922333, 0.0125243, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.00044759, 0.000257536, 0), \
                           -88937.4, 38446, 38446, -nan)
reports[-1].sigmaresid = ValErr(2.44579, 0.00882017, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0834706, None, -0.00356021, None, 0.0902775, None, -0.00365637, None, 0.0902775, None, -0.00365637, None, 0.0848958, None, -0.00362089, None, 0.0848958, None, -0.00362089, None, 2.44589, None, 0.00819522, None, 2.44589, None, 0.00819522, None)

reports.append(Report(590184448, ("DT", 0, 4, 11), "MBwhCst4sec11"))
reports[-1].posNum = 38265
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.0563695, 0.0117182, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.00026691, 0.000241154, 0), \
                           -85789.5, 38265, 38265, -nan)
reports[-1].sigmaresid = ValErr(2.27743, 0.00823243, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0551198, None, -0.00231795, None, -0.0578464, None, -0.00233843, None, -0.0578464, None, -0.00233843, None, -0.055826, None, -0.00235634, None, -0.055826, None, -0.00235634, None, 2.27746, None, 0.00696745, None, 2.27746, None, 0.00696745, None)

reports.append(Report(590446592, ("DT", 0, 4, 12), "MBwhCst4sec12"))
reports[-1].posNum = 118192
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.101911, 0.00701337, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000761044, 0.000143731, 0), \
                           -271666, 118192, 118192, -nan)
reports[-1].sigmaresid = ValErr(2.40988, 0.00495664, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.101433, None, -0.00279093, None, 0.103103, None, -0.00289212, None, 0.103103, None, -0.00289212, None, 0.106327, None, -0.00293821, None, 0.106327, None, -0.00293821, None, 2.41017, None, 0.00791523, None, 2.41017, None, 0.00791523, None)

reports.append(Report(587595776, ("DT", 1, 4, 1), "MBwhDst4sec01"))
reports[-1].posNum = 109746
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.00055155, 0.00744702, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000492003, 0.000154035, 0), \
                           -254277, 109746, 109746, -nan)
reports[-1].sigmaresid = ValErr(2.45474, 0.00523957, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0087133, None, 0.000685857, None, -0.0029224, None, 0.000721027, None, -0.0029224, None, 0.000721027, None, -0.0175418, None, 0.000826447, None, -0.0175418, None, 0.000826447, None, 2.45485, None, 0.00772516, None, 2.45485, None, 0.00772516, None)

reports.append(Report(587857920, ("DT", 1, 4, 2), "MBwhDst4sec02"))
reports[-1].posNum = 100251
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.0203951, 0.00770083, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000638504, 0.000161509, 0), \
                           -231127, 100251, 100251, -nan)
reports[-1].sigmaresid = ValErr(2.42673, 0.00541954, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0180827, None, 8.38033e-05, None, 0.0174364, None, 0.00012793, None, 0.0174364, None, 0.00012793, None, 0.0259672, None, 0.000113125, None, 0.0259672, None, 0.000113125, None, 2.42692, None, 0.00766042, None, 2.42692, None, 0.00766042, None)

reports.append(Report(588120064, ("DT", 1, 4, 3), "MBwhDst4sec03"))
reports[-1].posNum = 101213
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.0915194, 0.00757161, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000750474, 0.000156413, 0), \
                           -232465, 101213, 101213, -nan)
reports[-1].sigmaresid = ValErr(2.40573, 0.00534704, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0948945, None, 0.000954374, None, -0.0933732, None, 0.00105898, None, -0.0933732, None, 0.00105898, None, -0.0913878, None, 0.00111702, None, -0.0913878, None, 0.00111702, None, 2.406, None, 0.00768224, None, 2.406, None, 0.00768224, None)

reports.append(Report(588382208, ("DT", 1, 4, 4), "MBwhDst4sec04"))
reports[-1].posNum = 57229
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.018804, 0.0105487, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000147002, 0.00028866, 0), \
                           -133880, 57229, 57229, -nan)
reports[-1].sigmaresid = ValErr(2.5104, 0.00742028, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0300881, None, -2.10232e-05, None, 0.0182585, None, -2.71955e-06, None, 0.0182585, None, -2.71955e-06, None, -0.000105779, None, 5.94841e-05, None, -0.000105779, None, 5.94841e-05, None, 2.51041, None, 0.00792184, None, 2.51041, None, 0.00792184, None)

reports.append(Report(590741504, ("DT", 1, 4, 13), "MBwhDst4sec13"))
reports[-1].posNum = 50875
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.0294552, 0.0111803, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00145379, 0.000263935, 0), \
                           -119212, 50875, 50875, -nan)
reports[-1].sigmaresid = ValErr(2.5201, 0.00790044, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0314696, None, -0.00285936, None, 0.0316845, None, -0.0029163, None, 0.0316845, None, -0.0029163, None, 0.0476663, None, -0.00299531, None, 0.0476663, None, -0.00299531, None, 2.52086, None, 0.00797002, None, 2.52086, None, 0.00797002, None)

reports.append(Report(588644352, ("DT", 1, 4, 5), "MBwhDst4sec05"))
reports[-1].posNum = 106842
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.0582095, 0.00772105, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00115115, 0.000159025, 0), \
                           -250221, 106842, 106842, -nan)
reports[-1].sigmaresid = ValErr(2.51692, 0.00544482, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0737553, None, -0.0044794, None, 0.062343, None, -0.00457797, None, 0.062343, None, -0.00457797, None, 0.0712483, None, -0.00465448, None, 0.0712483, None, -0.00465448, None, 2.51754, None, 0.00797469, None, 2.51754, None, 0.00797469, None)

reports.append(Report(588906496, ("DT", 1, 4, 6), "MBwhDst4sec06"))
reports[-1].posNum = 117489
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.0798841, 0.00710327, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000433743, 0.00014647, 0), \
                           -271220, 117489, 117489, -nan)
reports[-1].sigmaresid = ValErr(2.43399, 0.00502118, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0826703, None, -0.000636413, None, 0.0793549, None, -0.000689926, None, 0.0793549, None, -0.000689926, None, 0.0824559, None, -0.0007348, None, 0.0824559, None, -0.0007348, None, 2.43408, None, 0.00769187, None, 2.43408, None, 0.00769187, None)

reports.append(Report(589168640, ("DT", 1, 4, 7), "MBwhDst4sec07"))
reports[-1].posNum = 123812
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.12084, 0.00698212, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.92536e-05, 0.000143982, 0), \
                           -286868, 123812, 123812, -nan)
reports[-1].sigmaresid = ValErr(2.45476, 0.00493301, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.119443, None, -0.000891296, None, 0.120978, None, -0.000933064, None, 0.120978, None, -0.000933064, None, 0.121418, None, -0.000922989, None, 0.121418, None, -0.000922989, None, 2.45476, None, 0.0078651, None, 2.45476, None, 0.0078651, None)

reports.append(Report(589430784, ("DT", 1, 4, 8), "MBwhDst4sec08"))
reports[-1].posNum = 108289
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.110277, 0.00757806, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000369353, 0.000158763, 0), \
                           -252294, 108289, 108289, -nan)
reports[-1].sigmaresid = ValErr(2.4865, 0.00534295, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.109346, None, -0.00414158, None, 0.111618, None, -0.00421205, None, 0.111618, None, -0.00421205, None, 0.118219, None, -0.0042926, None, 0.118219, None, -0.0042926, None, 2.48657, None, 0.00778629, None, 2.48657, None, 0.00778629, None)

reports.append(Report(589692928, ("DT", 1, 4, 9), "MBwhDst4sec09"))
reports[-1].posNum = 49560
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.0352438, 0.0105279, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000158697, 0.00021711, 0), \
                           -112473, 49560, 49560, -nan)
reports[-1].sigmaresid = ValErr(2.34081, 0.00743508, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0546604, None, -0.000620186, None, 0.0348602, None, -0.00060549, None, 0.0348602, None, -0.00060549, None, 0.0239228, None, -0.000569675, None, 0.0239228, None, -0.000569675, None, 2.34083, None, 0.00712314, None, 2.34083, None, 0.00712314, None)

reports.append(Report(589955072, ("DT", 1, 4, 10), "MBwhDst4sec10"))
reports[-1].posNum = 54258
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.0388212, 0.0106666, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.00145473, 0.000220817, 0), \
                           -126233, 54258, 54258, -nan)
reports[-1].sigmaresid = ValErr(2.47834, 0.00752339, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0367843, None, 0.000333147, None, 0.0338324, None, 0.000277557, None, 0.0338324, None, 0.000277557, None, 0.0204881, None, 0.000258081, None, 0.0204881, None, 0.000258081, None, 2.47933, None, 0.00793751, None, 2.47933, None, 0.00793751, None)

reports.append(Report(591003648, ("DT", 1, 4, 14), "MBwhDst4sec14"))
reports[-1].posNum = 58150
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.0073642, 0.0104217, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00235505, 0.000220997, 0), \
                           -136062, 58150, 58150, -nan)
reports[-1].sigmaresid = ValErr(2.51159, 0.00736475, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00979028, None, -1.6006e-05, None, 0.0112528, None, -6.21521e-05, None, 0.0112528, None, -6.21521e-05, None, 0.0318047, None, -0.000113411, None, 0.0318047, None, -0.000113411, None, 2.51404, None, 0.00792021, None, 2.51404, None, 0.00792021, None)

reports.append(Report(590217216, ("DT", 1, 4, 11), "MBwhDst4sec11"))
reports[-1].posNum = 50810
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.0836817, 0.0103541, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000111992, 0.000212198, 0), \
                           -115148, 50810, 50810, -nan)
reports[-1].sigmaresid = ValErr(2.33337, 0.00731973, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.090381, None, -0.0007456, None, 0.0835676, None, -0.000755595, None, 0.0835676, None, -0.000755595, None, 0.0918101, None, -0.000788531, None, 0.0918101, None, -0.000788531, None, 2.33338, None, 0.00698299, None, 2.33338, None, 0.00698299, None)

reports.append(Report(590479360, ("DT", 1, 4, 12), "MBwhDst4sec12"))
reports[-1].posNum = 126953
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.0796779, 0.00681292, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00124806, 0.000140157, 0), \
                           -292691, 126953, 126953, -nan)
reports[-1].sigmaresid = ValErr(2.4268, 0.00481611, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0730945, None, -1.12631e-06, None, -0.0782427, None, 4.99104e-05, None, -0.0782427, None, 4.99104e-05, None, -0.0762552, None, 8.0847e-05, None, -0.0762552, None, 8.0847e-05, None, 2.42755, None, 0.00765095, None, 2.42755, None, 0.00765095, None)

reports.append(Report(587628544, ("DT", 2, 4, 1), "MBwhEst4sec01"))
reports[-1].posNum = 92469
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.065867, 0.00866952, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000432282, 0.000174831, 0), \
                           -220792, 92469, 92469, -nan)
reports[-1].sigmaresid = ValErr(2.63479, 0.00612678, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0545341, None, 0.00115171, None, -0.0651474, None, 0.00117874, None, -0.0651474, None, 0.00117874, None, -0.062849, None, 0.00112362, None, -0.062849, None, 0.00112362, None, 2.63488, None, 0.0080516, None, 2.63488, None, 0.0080516, None)

reports.append(Report(587890688, ("DT", 2, 4, 2), "MBwhEst4sec02"))
reports[-1].posNum = 71095
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.0436237, 0.00970589, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000936738, 0.000193396, 0), \
                           -168481, 71095, 71095, -nan)
reports[-1].sigmaresid = ValErr(2.58794, 0.00686308, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0417807, None, 0.00097546, None, -0.0437352, None, 0.001006, None, -0.0437352, None, 0.001006, None, -0.042011, None, 0.00102926, None, -0.042011, None, 0.00102926, None, 2.58836, None, 0.00800988, None, 2.58836, None, 0.00800988, None)

reports.append(Report(588152832, ("DT", 2, 4, 3), "MBwhEst4sec03"))
reports[-1].posNum = 77410
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.0945934, 0.0091605, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00121948, 0.000184841, 0), \
                           -182259, 77410, 77410, -nan)
reports[-1].sigmaresid = ValErr(2.54855, 0.00647711, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0923106, None, 0.000201685, None, -0.0952426, None, 0.000247148, None, -0.0952426, None, 0.000247148, None, -0.0793114, None, 0.000226838, None, -0.0793114, None, 0.000226838, None, 2.54927, None, 0.00776381, None, 2.54927, None, 0.00776381, None)

reports.append(Report(588414976, ("DT", 2, 4, 4), "MBwhEst4sec04"))
reports[-1].posNum = 64142
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.0589237, 0.0105748, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000303875, 0.000214756, 0), \
                           -154169, 64142, 64142, -nan)
reports[-1].sigmaresid = ValErr(2.67679, 0.00747356, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0698006, None, 0.00016699, None, 0.0584368, None, 0.000138534, None, 0.0584368, None, 0.000138534, None, 0.0342871, None, 0.000271824, None, 0.0342871, None, 0.000271824, None, 2.67683, None, 0.00818211, None, 2.67683, None, 0.00818211, None)

reports.append(Report(590774272, ("DT", 2, 4, 13), "MBwhEst4sec13"))
reports[-1].posNum = 61117
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.00607997, 0.0109585, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00220368, 0.000221593, 0), \
                           -147623, 61117, 61117, -nan)
reports[-1].sigmaresid = ValErr(2.70873, 0.00774763, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0112064, None, -0.00343638, None, -0.00417305, None, -0.00346101, None, -0.00417305, None, -0.00346101, None, 0.00762939, None, -0.00352701, None, 0.00762939, None, -0.00352701, None, 2.71092, None, 0.00838281, None, 2.71092, None, 0.00838281, None)

reports.append(Report(588677120, ("DT", 2, 4, 5), "MBwhEst4sec05"))
reports[-1].posNum = 99908
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.0833616, 0.00818424, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000784983, 0.000166971, 0), \
                           -236656, 99908, 99908, -nan)
reports[-1].sigmaresid = ValErr(2.58521, 0.00578336, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.089009, None, -0.000779358, None, 0.0847496, None, -0.00079066, None, 0.0847496, None, -0.00079066, None, 0.0816866, None, -0.000803659, None, 0.0816866, None, -0.000803659, None, 2.58549, None, 0.00798284, None, 2.58549, None, 0.00798284, None)

reports.append(Report(588939264, ("DT", 2, 4, 6), "MBwhEst4sec06"))
reports[-1].posNum = 104611
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.147162, 0.00807239, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.00115595, 0.000166316, 0), \
                           -248621, 104611, 104611, -nan)
reports[-1].sigmaresid = ValErr(2.60565, 0.00569654, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.151128, None, -0.001382, None, 0.150724, None, -0.00143295, None, 0.150724, None, -0.00143295, None, 0.142987, None, -0.0014978, None, 0.142987, None, -0.0014978, None, 2.60625, None, 0.00799574, None, 2.60625, None, 0.00799574, None)

reports.append(Report(589201408, ("DT", 2, 4, 7), "MBwhEst4sec07"))
reports[-1].posNum = 103648
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.0697139, 0.00812112, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00058945, 0.000166206, 0), \
                           -246632, 103648, 103648, -nan)
reports[-1].sigmaresid = ValErr(2.6132, 0.00573954, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0720725, None, -0.00226699, None, 0.0687919, None, -0.00231206, None, 0.0687919, None, -0.00231206, None, 0.0821547, None, -0.0023275, None, 0.0821547, None, -0.0023275, None, 2.61336, None, 0.00805249, None, 2.61336, None, 0.00805249, None)

reports.append(Report(589463552, ("DT", 2, 4, 8), "MBwhEst4sec08"))
reports[-1].posNum = 100844
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.123637, 0.00810658, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00198429, 0.000166197, 0), \
                           -238445, 100844, 100844, -nan)
reports[-1].sigmaresid = ValErr(2.57424, 0.00573205, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.12462, None, -0.00221244, None, 0.122895, None, -0.00226357, None, 0.122895, None, -0.00226357, None, 0.138666, None, -0.00228729, None, 0.138666, None, -0.00228729, None, 2.57606, None, 0.00791825, None, 2.57606, None, 0.00791825, None)

reports.append(Report(589725696, ("DT", 2, 4, 9), "MBwhEst4sec09"))
reports[-1].posNum = 34440
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.0168396, 0.0137603, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.00318439, 0.000275271, 0), \
                           -81140.4, 34440, 34440, -nan)
reports[-1].sigmaresid = ValErr(2.55245, 0.00972545, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0164262, None, 0.00155433, None, 0.011969, None, 0.00150231, None, 0.011969, None, 0.00150231, None, -0.00329057, None, 0.00157396, None, -0.00329057, None, 0.00157396, None, 2.55741, None, 0.00770693, None, 2.55741, None, 0.00770693, None)

reports.append(Report(589987840, ("DT", 2, 4, 10), "MBwhEst4sec10"))
reports[-1].posNum = 52675
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.012775, 0.0114549, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000532126, 0.000233716, 0), \
                           -125607, 52675, 52675, -nan)
reports[-1].sigmaresid = ValErr(2.62643, 0.00809186, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0168486, None, 0.00140116, None, 0.0139271, None, 0.00139994, None, 0.0139271, None, 0.00139994, None, 0.00577089, None, 0.00142485, None, 0.00577089, None, 0.00142485, None, 2.62656, None, 0.00818585, None, 2.62656, None, 0.00818585, None)

reports.append(Report(591036416, ("DT", 2, 4, 14), "MBwhEst4sec14"))
reports[-1].posNum = 55923
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(0.0578867, 0.0111008, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.00115593, 0.000226752, 0), \
                           -133323, 55923, 55923, -nan)
reports[-1].sigmaresid = ValErr(2.62507, 0.00784929, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0462436, None, 0.00249902, None, 0.0582384, None, 0.00247847, None, 0.0582384, None, 0.00247847, None, 0.0500406, None, 0.00248367, None, 0.0500406, None, 0.00248367, None, 2.62568, None, 0.00824556, None, 2.62568, None, 0.00824556, None)

reports.append(Report(590249984, ("DT", 2, 4, 11), "MBwhEst4sec11"))
reports[-1].posNum = 42589
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.110548, 0.0121295, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.00152495, 0.000246606, 0), \
                           -99506, 42589, 42589, -nan)
reports[-1].sigmaresid = ValErr(2.50299, 0.00857622, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.107898, None, 0.0027001, None, -0.10962, None, 0.00270547, None, -0.10962, None, 0.00270547, None, -0.127282, None, 0.00275455, None, -0.127282, None, 0.00275455, None, 2.50411, None, 0.00754903, None, 2.50411, None, 0.00754903, None)

reports.append(Report(590512128, ("DT", 2, 4, 12), "MBwhEst4sec12"))
reports[-1].posNum = 100005
reports[-1].negNum = 0
reports[-1].fittype = "5DOF"
reports[-1].add_parameters(ValErr(-0.110514, 0.00829717, 0), \
                           None, \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000715043, 0.000167283, 0), \
                           -238343, 100005, 100005, -nan)
reports[-1].sigmaresid = ValErr(2.62315, 0.00586539, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.118222, None, 0.00264184, None, -0.109701, None, 0.00268007, None, -0.109701, None, 0.00268007, None, -0.123507, None, 0.00273953, None, -0.123507, None, 0.00273953, None, 2.62338, None, 0.0080526, None, 2.62338, None, 0.0080526, None)

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

