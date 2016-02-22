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
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(575176704, ("DT", -2, 1, 2), "MBwhAst1sec02"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(575438848, ("DT", -2, 1, 3), "MBwhAst1sec03"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(575700992, ("DT", -2, 1, 4), "MBwhAst1sec04"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(575963136, ("DT", -2, 1, 5), "MBwhAst1sec05"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(576225280, ("DT", -2, 1, 6), "MBwhAst1sec06"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(576487424, ("DT", -2, 1, 7), "MBwhAst1sec07"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(576749568, ("DT", -2, 1, 8), "MBwhAst1sec08"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(577011712, ("DT", -2, 1, 9), "MBwhAst1sec09"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(577273856, ("DT", -2, 1, 10), "MBwhAst1sec10"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(577536000, ("DT", -2, 1, 11), "MBwhAst1sec11"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(577798144, ("DT", -2, 1, 12), "MBwhAst1sec12"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(579108864, ("DT", -2, 2, 1), "MBwhAst2sec01"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(579371008, ("DT", -2, 2, 2), "MBwhAst2sec02"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(579633152, ("DT", -2, 2, 3), "MBwhAst2sec03"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(579895296, ("DT", -2, 2, 4), "MBwhAst2sec04"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(580157440, ("DT", -2, 2, 5), "MBwhAst2sec05"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(580419584, ("DT", -2, 2, 6), "MBwhAst2sec06"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(580681728, ("DT", -2, 2, 7), "MBwhAst2sec07"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(580943872, ("DT", -2, 2, 8), "MBwhAst2sec08"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(581206016, ("DT", -2, 2, 9), "MBwhAst2sec09"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(581468160, ("DT", -2, 2, 10), "MBwhAst2sec10"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(581730304, ("DT", -2, 2, 11), "MBwhAst2sec11"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(581992448, ("DT", -2, 2, 12), "MBwhAst2sec12"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(583303168, ("DT", -2, 3, 1), "MBwhAst3sec01"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(583565312, ("DT", -2, 3, 2), "MBwhAst3sec02"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(583827456, ("DT", -2, 3, 3), "MBwhAst3sec03"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(584089600, ("DT", -2, 3, 4), "MBwhAst3sec04"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(584351744, ("DT", -2, 3, 5), "MBwhAst3sec05"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(584613888, ("DT", -2, 3, 6), "MBwhAst3sec06"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(584876032, ("DT", -2, 3, 7), "MBwhAst3sec07"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(585138176, ("DT", -2, 3, 8), "MBwhAst3sec08"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(585400320, ("DT", -2, 3, 9), "MBwhAst3sec09"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(585662464, ("DT", -2, 3, 10), "MBwhAst3sec10"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(585924608, ("DT", -2, 3, 11), "MBwhAst3sec11"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(586186752, ("DT", -2, 3, 12), "MBwhAst3sec12"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(574947328, ("DT", -1, 1, 1), "MBwhBst1sec01"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(575209472, ("DT", -1, 1, 2), "MBwhBst1sec02"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(575471616, ("DT", -1, 1, 3), "MBwhBst1sec03"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(575733760, ("DT", -1, 1, 4), "MBwhBst1sec04"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(575995904, ("DT", -1, 1, 5), "MBwhBst1sec05"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(576258048, ("DT", -1, 1, 6), "MBwhBst1sec06"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(576520192, ("DT", -1, 1, 7), "MBwhBst1sec07"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(576782336, ("DT", -1, 1, 8), "MBwhBst1sec08"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(577044480, ("DT", -1, 1, 9), "MBwhBst1sec09"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(577306624, ("DT", -1, 1, 10), "MBwhBst1sec10"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(577568768, ("DT", -1, 1, 11), "MBwhBst1sec11"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(577830912, ("DT", -1, 1, 12), "MBwhBst1sec12"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(579141632, ("DT", -1, 2, 1), "MBwhBst2sec01"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(579403776, ("DT", -1, 2, 2), "MBwhBst2sec02"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(579665920, ("DT", -1, 2, 3), "MBwhBst2sec03"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(579928064, ("DT", -1, 2, 4), "MBwhBst2sec04"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(580190208, ("DT", -1, 2, 5), "MBwhBst2sec05"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(580452352, ("DT", -1, 2, 6), "MBwhBst2sec06"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(580714496, ("DT", -1, 2, 7), "MBwhBst2sec07"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(580976640, ("DT", -1, 2, 8), "MBwhBst2sec08"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(581238784, ("DT", -1, 2, 9), "MBwhBst2sec09"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(581500928, ("DT", -1, 2, 10), "MBwhBst2sec10"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(581763072, ("DT", -1, 2, 11), "MBwhBst2sec11"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(582025216, ("DT", -1, 2, 12), "MBwhBst2sec12"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(583335936, ("DT", -1, 3, 1), "MBwhBst3sec01"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(583598080, ("DT", -1, 3, 2), "MBwhBst3sec02"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(583860224, ("DT", -1, 3, 3), "MBwhBst3sec03"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(584122368, ("DT", -1, 3, 4), "MBwhBst3sec04"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(584384512, ("DT", -1, 3, 5), "MBwhBst3sec05"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(584646656, ("DT", -1, 3, 6), "MBwhBst3sec06"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(584908800, ("DT", -1, 3, 7), "MBwhBst3sec07"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(585170944, ("DT", -1, 3, 8), "MBwhBst3sec08"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(585433088, ("DT", -1, 3, 9), "MBwhBst3sec09"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(585695232, ("DT", -1, 3, 10), "MBwhBst3sec10"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(585957376, ("DT", -1, 3, 11), "MBwhBst3sec11"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(586219520, ("DT", -1, 3, 12), "MBwhBst3sec12"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(574980096, ("DT", 0, 1, 1), "MBwhCst1sec01"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(576028672, ("DT", 0, 1, 5), "MBwhCst1sec05"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(577077248, ("DT", 0, 1, 9), "MBwhCst1sec09"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(575242240, ("DT", 0, 1, 2), "MBwhCst1sec02"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(576290816, ("DT", 0, 1, 6), "MBwhCst1sec06"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(577339392, ("DT", 0, 1, 10), "MBwhCst1sec10"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(575504384, ("DT", 0, 1, 3), "MBwhCst1sec03"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(576552960, ("DT", 0, 1, 7), "MBwhCst1sec07"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(577601536, ("DT", 0, 1, 11), "MBwhCst1sec11"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(575766528, ("DT", 0, 1, 4), "MBwhCst1sec04"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(576815104, ("DT", 0, 1, 8), "MBwhCst1sec08"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(577863680, ("DT", 0, 1, 12), "MBwhCst1sec12"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(579174400, ("DT", 0, 2, 1), "MBwhCst2sec01"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(580222976, ("DT", 0, 2, 5), "MBwhCst2sec05"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(581271552, ("DT", 0, 2, 9), "MBwhCst2sec09"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(579436544, ("DT", 0, 2, 2), "MBwhCst2sec02"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(580485120, ("DT", 0, 2, 6), "MBwhCst2sec06"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(581533696, ("DT", 0, 2, 10), "MBwhCst2sec10"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(579698688, ("DT", 0, 2, 3), "MBwhCst2sec03"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(580747264, ("DT", 0, 2, 7), "MBwhCst2sec07"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(581795840, ("DT", 0, 2, 11), "MBwhCst2sec11"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(579960832, ("DT", 0, 2, 4), "MBwhCst2sec04"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(581009408, ("DT", 0, 2, 8), "MBwhCst2sec08"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(582057984, ("DT", 0, 2, 12), "MBwhCst2sec12"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(583368704, ("DT", 0, 3, 1), "MBwhCst3sec01"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(584417280, ("DT", 0, 3, 5), "MBwhCst3sec05"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(585465856, ("DT", 0, 3, 9), "MBwhCst3sec09"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(583630848, ("DT", 0, 3, 2), "MBwhCst3sec02"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(584679424, ("DT", 0, 3, 6), "MBwhCst3sec06"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(585728000, ("DT", 0, 3, 10), "MBwhCst3sec10"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(583892992, ("DT", 0, 3, 3), "MBwhCst3sec03"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(584941568, ("DT", 0, 3, 7), "MBwhCst3sec07"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(585990144, ("DT", 0, 3, 11), "MBwhCst3sec11"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(584155136, ("DT", 0, 3, 4), "MBwhCst3sec04"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(585203712, ("DT", 0, 3, 8), "MBwhCst3sec08"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(586252288, ("DT", 0, 3, 12), "MBwhCst3sec12"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(575012864, ("DT", 1, 1, 1), "MBwhDst1sec01"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(575275008, ("DT", 1, 1, 2), "MBwhDst1sec02"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(575537152, ("DT", 1, 1, 3), "MBwhDst1sec03"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(575799296, ("DT", 1, 1, 4), "MBwhDst1sec04"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(576061440, ("DT", 1, 1, 5), "MBwhDst1sec05"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(576323584, ("DT", 1, 1, 6), "MBwhDst1sec06"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(576585728, ("DT", 1, 1, 7), "MBwhDst1sec07"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(576847872, ("DT", 1, 1, 8), "MBwhDst1sec08"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(577110016, ("DT", 1, 1, 9), "MBwhDst1sec09"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(577372160, ("DT", 1, 1, 10), "MBwhDst1sec10"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(577634304, ("DT", 1, 1, 11), "MBwhDst1sec11"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(577896448, ("DT", 1, 1, 12), "MBwhDst1sec12"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(579207168, ("DT", 1, 2, 1), "MBwhDst2sec01"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(579469312, ("DT", 1, 2, 2), "MBwhDst2sec02"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(579731456, ("DT", 1, 2, 3), "MBwhDst2sec03"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(579993600, ("DT", 1, 2, 4), "MBwhDst2sec04"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(580255744, ("DT", 1, 2, 5), "MBwhDst2sec05"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(580517888, ("DT", 1, 2, 6), "MBwhDst2sec06"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(580780032, ("DT", 1, 2, 7), "MBwhDst2sec07"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(581042176, ("DT", 1, 2, 8), "MBwhDst2sec08"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(581304320, ("DT", 1, 2, 9), "MBwhDst2sec09"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(581566464, ("DT", 1, 2, 10), "MBwhDst2sec10"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(581828608, ("DT", 1, 2, 11), "MBwhDst2sec11"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(582090752, ("DT", 1, 2, 12), "MBwhDst2sec12"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(583401472, ("DT", 1, 3, 1), "MBwhDst3sec01"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(583663616, ("DT", 1, 3, 2), "MBwhDst3sec02"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(583925760, ("DT", 1, 3, 3), "MBwhDst3sec03"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(584187904, ("DT", 1, 3, 4), "MBwhDst3sec04"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(584450048, ("DT", 1, 3, 5), "MBwhDst3sec05"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(584712192, ("DT", 1, 3, 6), "MBwhDst3sec06"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(584974336, ("DT", 1, 3, 7), "MBwhDst3sec07"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(585236480, ("DT", 1, 3, 8), "MBwhDst3sec08"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(585498624, ("DT", 1, 3, 9), "MBwhDst3sec09"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(585760768, ("DT", 1, 3, 10), "MBwhDst3sec10"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(586022912, ("DT", 1, 3, 11), "MBwhDst3sec11"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(586285056, ("DT", 1, 3, 12), "MBwhDst3sec12"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(575045632, ("DT", 2, 1, 1), "MBwhEst1sec01"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(575307776, ("DT", 2, 1, 2), "MBwhEst1sec02"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(575569920, ("DT", 2, 1, 3), "MBwhEst1sec03"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(575832064, ("DT", 2, 1, 4), "MBwhEst1sec04"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(576094208, ("DT", 2, 1, 5), "MBwhEst1sec05"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(576356352, ("DT", 2, 1, 6), "MBwhEst1sec06"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(576618496, ("DT", 2, 1, 7), "MBwhEst1sec07"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(576880640, ("DT", 2, 1, 8), "MBwhEst1sec08"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(577142784, ("DT", 2, 1, 9), "MBwhEst1sec09"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(577404928, ("DT", 2, 1, 10), "MBwhEst1sec10"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(577667072, ("DT", 2, 1, 11), "MBwhEst1sec11"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(577929216, ("DT", 2, 1, 12), "MBwhEst1sec12"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(579239936, ("DT", 2, 2, 1), "MBwhEst2sec01"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(579502080, ("DT", 2, 2, 2), "MBwhEst2sec02"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(579764224, ("DT", 2, 2, 3), "MBwhEst2sec03"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(580026368, ("DT", 2, 2, 4), "MBwhEst2sec04"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(580288512, ("DT", 2, 2, 5), "MBwhEst2sec05"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(580550656, ("DT", 2, 2, 6), "MBwhEst2sec06"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(580812800, ("DT", 2, 2, 7), "MBwhEst2sec07"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(581074944, ("DT", 2, 2, 8), "MBwhEst2sec08"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(581337088, ("DT", 2, 2, 9), "MBwhEst2sec09"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(581599232, ("DT", 2, 2, 10), "MBwhEst2sec10"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(581861376, ("DT", 2, 2, 11), "MBwhEst2sec11"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(582123520, ("DT", 2, 2, 12), "MBwhEst2sec12"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(583434240, ("DT", 2, 3, 1), "MBwhEst3sec01"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(583696384, ("DT", 2, 3, 2), "MBwhEst3sec02"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(583958528, ("DT", 2, 3, 3), "MBwhEst3sec03"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(584220672, ("DT", 2, 3, 4), "MBwhEst3sec04"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(584482816, ("DT", 2, 3, 5), "MBwhEst3sec05"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(584744960, ("DT", 2, 3, 6), "MBwhEst3sec06"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(585007104, ("DT", 2, 3, 7), "MBwhEst3sec07"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(585269248, ("DT", 2, 3, 8), "MBwhEst3sec08"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(585531392, ("DT", 2, 3, 9), "MBwhEst3sec09"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(585793536, ("DT", 2, 3, 10), "MBwhEst3sec10"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(586055680, ("DT", 2, 3, 11), "MBwhEst3sec11"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(586317824, ("DT", 2, 3, 12), "MBwhEst3sec12"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(587497472, ("DT", -2, 4, 1), "MBwhAst4sec01"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(587759616, ("DT", -2, 4, 2), "MBwhAst4sec02"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(588021760, ("DT", -2, 4, 3), "MBwhAst4sec03"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(588283904, ("DT", -2, 4, 4), "MBwhAst4sec04"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(590643200, ("DT", -2, 4, 13), "MBwhAst4sec13"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(588546048, ("DT", -2, 4, 5), "MBwhAst4sec05"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(588808192, ("DT", -2, 4, 6), "MBwhAst4sec06"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(589070336, ("DT", -2, 4, 7), "MBwhAst4sec07"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(589332480, ("DT", -2, 4, 8), "MBwhAst4sec08"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(589594624, ("DT", -2, 4, 9), "MBwhAst4sec09"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(589856768, ("DT", -2, 4, 10), "MBwhAst4sec10"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(590905344, ("DT", -2, 4, 14), "MBwhAst4sec14"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(590118912, ("DT", -2, 4, 11), "MBwhAst4sec11"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(590381056, ("DT", -2, 4, 12), "MBwhAst4sec12"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(587530240, ("DT", -1, 4, 1), "MBwhBst4sec01"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(587792384, ("DT", -1, 4, 2), "MBwhBst4sec02"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(588054528, ("DT", -1, 4, 3), "MBwhBst4sec03"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(588316672, ("DT", -1, 4, 4), "MBwhBst4sec04"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(590675968, ("DT", -1, 4, 13), "MBwhBst4sec13"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(588578816, ("DT", -1, 4, 5), "MBwhBst4sec05"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(588840960, ("DT", -1, 4, 6), "MBwhBst4sec06"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(589103104, ("DT", -1, 4, 7), "MBwhBst4sec07"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(589365248, ("DT", -1, 4, 8), "MBwhBst4sec08"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(589627392, ("DT", -1, 4, 9), "MBwhBst4sec09"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(589889536, ("DT", -1, 4, 10), "MBwhBst4sec10"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(590938112, ("DT", -1, 4, 14), "MBwhBst4sec14"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(590151680, ("DT", -1, 4, 11), "MBwhBst4sec11"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(590413824, ("DT", -1, 4, 12), "MBwhBst4sec12"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(587563008, ("DT", 0, 4, 1), "MBwhCst4sec01"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(587825152, ("DT", 0, 4, 2), "MBwhCst4sec02"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(588087296, ("DT", 0, 4, 3), "MBwhCst4sec03"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(588349440, ("DT", 0, 4, 4), "MBwhCst4sec04"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(590708736, ("DT", 0, 4, 13), "MBwhCst4sec13"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(588611584, ("DT", 0, 4, 5), "MBwhCst4sec05"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(588873728, ("DT", 0, 4, 6), "MBwhCst4sec06"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(589135872, ("DT", 0, 4, 7), "MBwhCst4sec07"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(589398016, ("DT", 0, 4, 8), "MBwhCst4sec08"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(589660160, ("DT", 0, 4, 9), "MBwhCst4sec09"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(589922304, ("DT", 0, 4, 10), "MBwhCst4sec10"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(590970880, ("DT", 0, 4, 14), "MBwhCst4sec14"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(590184448, ("DT", 0, 4, 11), "MBwhCst4sec11"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(590446592, ("DT", 0, 4, 12), "MBwhCst4sec12"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(587595776, ("DT", 1, 4, 1), "MBwhDst4sec01"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(587857920, ("DT", 1, 4, 2), "MBwhDst4sec02"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(588120064, ("DT", 1, 4, 3), "MBwhDst4sec03"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(588382208, ("DT", 1, 4, 4), "MBwhDst4sec04"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(590741504, ("DT", 1, 4, 13), "MBwhDst4sec13"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(588644352, ("DT", 1, 4, 5), "MBwhDst4sec05"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(588906496, ("DT", 1, 4, 6), "MBwhDst4sec06"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(589168640, ("DT", 1, 4, 7), "MBwhDst4sec07"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(589430784, ("DT", 1, 4, 8), "MBwhDst4sec08"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(589692928, ("DT", 1, 4, 9), "MBwhDst4sec09"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(589955072, ("DT", 1, 4, 10), "MBwhDst4sec10"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(591003648, ("DT", 1, 4, 14), "MBwhDst4sec14"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(590217216, ("DT", 1, 4, 11), "MBwhDst4sec11"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(590479360, ("DT", 1, 4, 12), "MBwhDst4sec12"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(587628544, ("DT", 2, 4, 1), "MBwhEst4sec01"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(587890688, ("DT", 2, 4, 2), "MBwhEst4sec02"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(588152832, ("DT", 2, 4, 3), "MBwhEst4sec03"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(588414976, ("DT", 2, 4, 4), "MBwhEst4sec04"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(590774272, ("DT", 2, 4, 13), "MBwhEst4sec13"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(588677120, ("DT", 2, 4, 5), "MBwhEst4sec05"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(588939264, ("DT", 2, 4, 6), "MBwhEst4sec06"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(589201408, ("DT", 2, 4, 7), "MBwhEst4sec07"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(589463552, ("DT", 2, 4, 8), "MBwhEst4sec08"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(589725696, ("DT", 2, 4, 9), "MBwhEst4sec09"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(589987840, ("DT", 2, 4, 10), "MBwhEst4sec10"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(591036416, ("DT", 2, 4, 14), "MBwhEst4sec14"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(590249984, ("DT", 2, 4, 11), "MBwhEst4sec11"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(590512128, ("DT", 2, 4, 12), "MBwhEst4sec12"))
reports[-1].posNum = 0
reports[-1].negNum = 0
reports[-1].status = "TOOFEWHITS"

reports.append(Report(604017672, ("CSC", 1, 1, 1, 1), "MEp11_01"))
reports[-1].posNum = 97540
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000377833, 0.000841781, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.05919e-06, 2.10588e-05, 0), \
                           -8087.72, 97540, 97540, -nan)
reports[-1].sigmaresid = ValErr(0.262889, 0.000595205, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00128222, None, 0.000722655, None, 0.000376627, None, 0.00069623, None, 0.000376627, None, 0.00069623, None, 0.000925405, None, 0.000723246, None, 0.000925405, None, 0.000723246, None, 0.26289, None, 0.00581969, None, 0.26289, None, 0.00581969, None)

reports.append(Report(604017688, ("CSC", 1, 1, 1, 3), "MEp11_03"))
reports[-1].posNum = 115828
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000709281, 0.00135874, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.7471e-06, 2.35931e-05, 0), \
                           -8159.71, 115828, 115828, -nan)
reports[-1].sigmaresid = ValErr(0.259631, 0.000540388, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00089427, None, -0.000626342, None, 0.000678114, None, -0.000665912, None, 0.000678114, None, -0.000665912, None, 0.00028239, None, -0.000694578, None, 0.00028239, None, -0.000694578, None, 0.259632, None, 0.00475711, None, 0.259632, None, 0.00475711, None)

reports.append(Report(604017704, ("CSC", 1, 1, 1, 5), "MEp11_05"))
reports[-1].posNum = 116862
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000522567, 0.000771748, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.10538e-06, 1.94038e-05, 0), \
                           -10001.3, 116862, 116862, -nan)
reports[-1].sigmaresid = ValErr(0.263591, 0.000545229, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00154887, None, 0.000293565, None, 0.000510727, None, 0.00025701, None, 0.000510727, None, 0.00025701, None, -0.0011849, None, 0.00029034, None, -0.0011849, None, 0.00029034, None, 0.263591, None, 0.00487714, None, 0.263591, None, 0.00487714, None)

reports.append(Report(604017720, ("CSC", 1, 1, 1, 7), "MEp11_07"))
reports[-1].posNum = 114800
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000345993, 0.000771572, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.40014e-07, 1.90836e-05, 0), \
                           -8700.64, 114800, 114800, -nan)
reports[-1].sigmaresid = ValErr(0.261022, 0.000544743, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0012505, None, 0.000211403, None, 0.000344331, None, 0.0002013, None, 0.000344331, None, 0.0002013, None, 0.000744648, None, 0.000213113, None, 0.000744648, None, 0.000213113, None, 0.261022, None, 0.00571749, None, 0.261022, None, 0.00571749, None)

reports.append(Report(604017736, ("CSC", 1, 1, 1, 9), "MEp11_09"))
reports[-1].posNum = 122742
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000297136, 0.000748112, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.54219e-05, 1.85584e-05, 0), \
                           -9602.27, 122742, 122742, -nan)
reports[-1].sigmaresid = ValErr(0.261661, 0.000528113, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0010765, None, -0.000297735, None, -0.000261244, None, -0.000324708, None, -0.000261244, None, -0.000324708, None, 0.00200632, None, -0.000354491, None, 0.00200632, None, -0.000354491, None, 0.261661, None, 0.00538029, None, 0.261661, None, 0.00538029, None)

reports.append(Report(604017752, ("CSC", 1, 1, 1, 11), "MEp11_11"))
reports[-1].posNum = 114404
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000107638, 0.000782079, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.18028e-05, 1.94637e-05, 0), \
                           -10081.4, 114404, 114404, -nan)
reports[-1].sigmaresid = ValErr(0.264261, 0.000552455, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000521479, None, 0.000107577, None, -8.60633e-05, None, 3.35857e-05, None, -8.60633e-05, None, 3.35857e-05, None, 4.69195e-05, None, 9.88151e-05, None, 4.69195e-05, None, 9.88151e-05, None, 0.264261, None, 0.00516574, None, 0.264261, None, 0.00516574, None)

reports.append(Report(604017768, ("CSC", 1, 1, 1, 13), "MEp11_13"))
reports[-1].posNum = 112934
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000119368, 0.000776489, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.30286e-06, 1.91015e-05, 0), \
                           -8407.78, 112934, 112934, -nan)
reports[-1].sigmaresid = ValErr(0.260673, 0.000548489, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000129845, None, -0.000322806, None, -0.000123461, None, -0.000378221, None, -0.000123461, None, -0.000378221, None, 0.00105007, None, -0.000391316, None, 0.00105007, None, -0.000391316, None, 0.260673, None, 0.00494454, None, 0.260673, None, 0.00494454, None)

reports.append(Report(604017784, ("CSC", 1, 1, 1, 15), "MEp11_15"))
reports[-1].posNum = 104278
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00011362, 0.000838321, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.72588e-05, 2.13873e-05, 0), \
                           -11569.2, 104278, 104278, -nan)
reports[-1].sigmaresid = ValErr(0.270362, 0.000592017, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000761843, None, 0.000191381, None, -5.93493e-05, None, 0.000112271, None, -5.93493e-05, None, 0.000112271, None, -0.00128383, None, 0.000139201, None, -0.00128383, None, 0.000139201, None, 0.270364, None, 0.00575453, None, 0.270364, None, 0.00575453, None)

reports.append(Report(604017800, ("CSC", 1, 1, 1, 17), "MEp11_17"))
reports[-1].posNum = 95660
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(7.90671e-05, 0.000975532, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.25594e-05, 2.77212e-05, 0), \
                           -15928.6, 95660, 95660, -nan)
reports[-1].sigmaresid = ValErr(0.285811, 0.000653429, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000267156, None, -0.000379631, None, 0.000333457, None, -0.000372822, None, 0.000333457, None, -0.000372822, None, 0.000525519, None, -0.000346676, None, 0.000525519, None, -0.000346676, None, 0.285812, None, 0.00518085, None, 0.285812, None, 0.00518085, None)

reports.append(Report(604017816, ("CSC", 1, 1, 1, 19), "MEp11_19"))
reports[-1].posNum = 105566
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000140405, 0.000808569, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.75148e-05, 2.04823e-05, 0), \
                           -8539.23, 105566, 105566, -nan)
reports[-1].sigmaresid = ValErr(0.262357, 0.000570973, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000723842, None, -0.00363602, None, -0.000176251, None, -0.00353662, None, -0.000176251, None, -0.00353662, None, 0.00152371, None, -0.00368462, None, 0.00152371, None, -0.00368462, None, 0.262358, None, 0.00509404, None, 0.262358, None, 0.00509404, None)

reports.append(Report(604017832, ("CSC", 1, 1, 1, 21), "MEp11_21"))
reports[-1].posNum = 104056
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000587732, 0.000823303, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.1829e-06, 2.05437e-05, 0), \
                           -9687.05, 104056, 104056, -nan)
reports[-1].sigmaresid = ValErr(0.265579, 0.000582163, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00135967, None, -2.12828e-06, None, 0.000587661, None, 7.34661e-06, None, 0.000587661, None, 7.34661e-06, None, -0.000189899, None, -1.28423e-05, None, -0.000189899, None, -1.28423e-05, None, 0.265579, None, 0.00487921, None, 0.265579, None, 0.00487921, None)

reports.append(Report(604017848, ("CSC", 1, 1, 1, 23), "MEp11_23"))
reports[-1].posNum = 106304
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000111266, 0.000826002, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.12815e-05, 2.07484e-05, 0), \
                           -11359.1, 106304, 106304, -nan)
reports[-1].sigmaresid = ValErr(0.269258, 0.000583955, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000591307, None, 0.000798332, None, -0.000102167, None, 0.000744411, None, -0.000102167, None, 0.000744411, None, 0.00245335, None, 0.000793957, None, 0.00245335, None, 0.000793957, None, 0.269259, None, 0.00577202, None, 0.269259, None, 0.00577202, None)

reports.append(Report(604017864, ("CSC", 1, 1, 1, 25), "MEp11_25"))
reports[-1].posNum = 114924
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000118101, 0.000785519, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.00678e-05, 1.96356e-05, 0), \
                           -10990.8, 114924, 114924, -nan)
reports[-1].sigmaresid = ValErr(0.266254, 0.000555362, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000178625, None, 0.000782494, None, -0.000111117, None, 0.000757478, None, -0.000111117, None, 0.000757478, None, -0.00137144, None, 0.000814106, None, -0.00137144, None, 0.000814106, None, 0.266255, None, 0.00633628, None, 0.266255, None, 0.00633628, None)

reports.append(Report(604017880, ("CSC", 1, 1, 1, 27), "MEp11_27"))
reports[-1].posNum = 111376
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000301518, 0.00079745, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.79445e-05, 2.02651e-05, 0), \
                           -10542, 111376, 111376, -nan)
reports[-1].sigmaresid = ValErr(0.265993, 0.000563584, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000247892, None, 5.65167e-05, None, -0.00027858, None, 2.92475e-05, None, -0.00027858, None, 2.92475e-05, None, -0.000294614, None, 3.62202e-05, None, -0.000294614, None, 3.62202e-05, None, 0.265994, None, 0.00481644, None, 0.265994, None, 0.00481644, None)

reports.append(Report(604017896, ("CSC", 1, 1, 1, 29), "MEp11_29"))
reports[-1].posNum = 115436
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000186116, 0.000780946, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.35244e-06, 1.95629e-05, 0), \
                           -10584.6, 115436, 115436, -nan)
reports[-1].sigmaresid = ValErr(0.265207, 0.000551949, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000835928, None, 0.00323012, None, -0.000196362, None, 0.00301851, None, -0.000196362, None, 0.00301851, None, 0.00167927, None, 0.00315382, None, 0.00167927, None, 0.00315382, None, 0.265207, None, 0.00517729, None, 0.265207, None, 0.00517729, None)

reports.append(Report(604017912, ("CSC", 1, 1, 1, 31), "MEp11_31"))
reports[-1].posNum = 114550
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000575884, 0.000775832, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.82418e-05, 1.91671e-05, 0), \
                           -9124.35, 114550, 114550, -nan)
reports[-1].sigmaresid = ValErr(0.262033, 0.000547448, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000292974, None, 0.000113175, None, -0.000527994, None, 0.00012818, None, -0.000527994, None, 0.00012818, None, 0.000290189, None, 5.92359e-05, None, 0.000290189, None, 5.92359e-05, None, 0.262034, None, 0.00499195, None, 0.262034, None, 0.00499195, None)

reports.append(Report(604017928, ("CSC", 1, 1, 1, 33), "MEp11_33"))
reports[-1].posNum = 73748
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000130742, 0.0011161, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.03389e-06, 4.46559e-05, 0), \
                           -6960.6, 73748, 73748, -nan)
reports[-1].sigmaresid = ValErr(0.265922, 0.000702651, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00219542, None, -0.000785156, None, 0.000128242, None, -0.000763493, None, 0.000128242, None, -0.000763493, None, 0.00252223, None, -0.000875182, None, 0.00252223, None, -0.000875182, None, 0.265921, None, 0.00499776, None, 0.265921, None, 0.00499776, None)

reports.append(Report(604017944, ("CSC", 1, 1, 1, 35), "MEp11_35"))
reports[-1].posNum = 118600
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000475695, 0.000760766, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.60303e-05, 1.85461e-05, 0), \
                           -9010.81, 118600, 118600, -nan)
reports[-1].sigmaresid = ValErr(0.261071, 0.000536046, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00175767, None, 0.000329588, None, 0.000386104, None, 0.000371281, None, 0.000386104, None, 0.000371281, None, 0.00113058, None, 0.000312341, None, 0.00113058, None, 0.000312341, None, 0.261073, None, 0.00528575, None, 0.261073, None, 0.00528575, None)

reports.append(Report(604017680, ("CSC", 1, 1, 1, 2), "MEp11_02"))
reports[-1].posNum = 120768
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000335141, 0.000672445, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.49833e-05, 1.61505e-05, 0), \
                           4717.65, 120768, 120768, -nan)
reports[-1].sigmaresid = ValErr(0.232701, 0.000473485, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-2.88534e-05, None, -0.0028276, None, 0.000239722, None, -0.00269796, None, 0.000239722, None, -0.00269796, None, -0.000487017, None, -0.00285197, None, -0.000487017, None, -0.00285197, None, 0.232703, None, 0.00537796, None, 0.232703, None, 0.00537796, None)

reports.append(Report(604017696, ("CSC", 1, 1, 1, 4), "MEp11_04"))
reports[-1].posNum = 123430
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(9.86305e-05, 0.000673568, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.89294e-06, 1.59616e-05, 0), \
                           3748.25, 123430, 123430, -nan)
reports[-1].sigmaresid = ValErr(0.234733, 0.000472443, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000370061, None, 0.00124894, None, 0.000135502, None, 0.00118722, None, 0.000135502, None, 0.00118722, None, 0.000666055, None, 0.00113649, None, 0.000666055, None, 0.00113649, None, 0.234733, None, 0.00538725, None, 0.234733, None, 0.00538725, None)

reports.append(Report(604017712, ("CSC", 1, 1, 1, 6), "MEp11_06"))
reports[-1].posNum = 114328
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000128627, 0.000691731, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.65161e-06, 1.63881e-05, 0), \
                           4588.1, 114328, 114328, -nan)
reports[-1].sigmaresid = ValErr(0.232452, 0.000486118, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000120283, None, 0.00167559, None, 9.74322e-05, None, 0.00162512, None, 9.74322e-05, None, 0.00162512, None, 0.000399434, None, 0.00156821, None, 0.000399434, None, 0.00156821, None, 0.232453, None, 0.00549014, None, 0.232453, None, 0.00549014, None)

reports.append(Report(604017728, ("CSC", 1, 1, 1, 8), "MEp11_08"))
reports[-1].posNum = 126762
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000182005, 0.000654482, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(8.80326e-06, 1.54296e-05, 0), \
                           5794.02, 126762, 126762, -nan)
reports[-1].sigmaresid = ValErr(0.23116, 0.000459095, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-9.94809e-05, None, -9.57857e-06, None, -0.000134922, None, -7.33293e-05, None, -0.000134922, None, -7.33293e-05, None, 0.00152432, None, -0.000141974, None, 0.00152432, None, -0.000141974, None, 0.23116, None, 0.00534043, None, 0.23116, None, 0.00534043, None)

reports.append(Report(604017744, ("CSC", 1, 1, 1, 10), "MEp11_10"))
reports[-1].posNum = 125272
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000307783, 0.000674938, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.27429e-06, 1.61163e-05, 0), \
                           2158.46, 125272, 125272, -nan)
reports[-1].sigmaresid = ValErr(0.237837, 0.000475157, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000654685, None, -0.000269726, None, 0.000319949, None, -0.000275826, None, 0.000319949, None, -0.000275826, None, 0.00121291, None, -0.000292794, None, 0.00121291, None, -0.000292794, None, 0.237837, None, 0.00549149, None, 0.237837, None, 0.00549149, None)

reports.append(Report(604017760, ("CSC", 1, 1, 1, 12), "MEp11_12"))
reports[-1].posNum = 127034
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000450404, 0.00066135, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.54522e-06, 1.55719e-05, 0), \
                           4268.06, 127034, 127034, -nan)
reports[-1].sigmaresid = ValErr(0.233977, 0.000464194, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00110314, None, -0.000201972, None, -0.000483934, None, -0.000268842, None, -0.000483934, None, -0.000268842, None, -6.45895e-05, None, -0.000298397, None, -6.45895e-05, None, -0.000298397, None, 0.233976, None, 0.00556263, None, 0.233976, None, 0.00556263, None)

reports.append(Report(604017776, ("CSC", 1, 1, 1, 14), "MEp11_14"))
reports[-1].posNum = 125074
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000115282, 0.00066657, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.13489e-05, 1.59559e-05, 0), \
                           3979.41, 125074, 125074, -nan)
reports[-1].sigmaresid = ValErr(0.234393, 0.000468648, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000241692, None, 0.000174226, None, 6.47193e-05, None, 0.000209433, None, 6.47193e-05, None, 0.000209433, None, 0.000183169, None, 0.000180701, None, 0.000183169, None, 0.000180701, None, 0.234394, None, 0.00520756, None, 0.234394, None, 0.00520756, None)

reports.append(Report(604017792, ("CSC", 1, 1, 1, 16), "MEp11_16"))
reports[-1].posNum = 121232
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000179444, 0.000679012, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.30155e-05, 1.66951e-05, 0), \
                           3278.02, 121232, 121232, -nan)
reports[-1].sigmaresid = ValErr(0.235516, 0.000478295, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-1.47468e-05, None, 0.00018722, None, 0.000133162, None, 0.000173286, None, 0.000133162, None, 0.000173286, None, 0.000760051, None, 0.000164611, None, 0.000760051, None, 0.000164611, None, 0.235516, None, 0.00529772, None, 0.235516, None, 0.00529772, None)

reports.append(Report(604017808, ("CSC", 1, 1, 1, 18), "MEp11_18"))
reports[-1].posNum = 122858
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000505916, 0.000605662, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.08183e-05, 1.64078e-05, 0), \
                           2644.18, 122858, 122858, -nan)
reports[-1].sigmaresid = ValErr(0.236819, 0.000477525, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000379114, None, 0.000551301, None, 0.000481084, None, 0.000499503, None, 0.000481084, None, 0.000499503, None, 0.000375904, None, 0.000499791, None, 0.000375904, None, 0.000499791, None, 0.236819, None, 0.00520143, None, 0.236819, None, 0.00520143, None)

reports.append(Report(604017824, ("CSC", 1, 1, 1, 20), "MEp11_20"))
reports[-1].posNum = 115722
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00123445, 0.000569163, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.29077e-05, 1.52129e-05, 0), \
                           2449.27, 115722, 115722, -nan)
reports[-1].sigmaresid = ValErr(0.236903, 0.000490108, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000610412, None, 0.00209017, None, 0.00116644, None, 0.00197666, None, 0.00116644, None, 0.00197666, None, 0.00258719, None, 0.00205713, None, 0.00258719, None, 0.00205713, None, 0.236905, None, 0.00520782, None, 0.236905, None, 0.00520782, None)

reports.append(Report(604017840, ("CSC", 1, 1, 1, 22), "MEp11_22"))
reports[-1].posNum = 115732
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00070883, 0.0007045, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.20383e-05, 1.70989e-05, 0), \
                           1245.1, 115732, 115732, -nan)
reports[-1].sigmaresid = ValErr(0.239381, 0.000497564, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000835676, None, -0.00552452, None, 0.000684636, None, -0.00529686, None, 0.000684636, None, -0.00529686, None, 0.00202564, None, -0.00544302, None, 0.00202564, None, -0.00544302, None, 0.239382, None, 0.0052257, None, 0.239382, None, 0.0052257, None)

reports.append(Report(604017856, ("CSC", 1, 1, 1, 24), "MEp11_24"))
reports[-1].posNum = 119668
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000301343, 0.000691081, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.78363e-06, 1.67546e-05, 0), \
                           1697.62, 119668, 119668, -nan)
reports[-1].sigmaresid = ValErr(0.238562, 0.000487638, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000156107, None, 0.00106178, None, 0.000277839, None, 0.0010701, None, 0.000277839, None, 0.0010701, None, -0.000264797, None, 0.00112626, None, -0.000264797, None, 0.00112626, None, 0.238563, None, 0.00563339, None, 0.238563, None, 0.00563339, None)

reports.append(Report(604017872, ("CSC", 1, 1, 1, 26), "MEp11_26"))
reports[-1].posNum = 125462
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000685549, 0.000666219, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.05098e-05, 1.58195e-05, 0), \
                           4115.43, 125462, 125462, -nan)
reports[-1].sigmaresid = ValErr(0.234162, 0.000467462, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000171892, None, -0.000123949, None, -0.000578487, None, -0.000106593, None, -0.000578487, None, -0.000106593, None, -0.00069598, None, -0.000158671, None, -0.00069598, None, -0.000158671, None, 0.234164, None, 0.00579588, None, 0.234164, None, 0.00579588, None)

reports.append(Report(604017888, ("CSC", 1, 1, 1, 28), "MEp11_28"))
reports[-1].posNum = 123420
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000190165, 0.000680835, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(7.99864e-06, 1.6477e-05, 0), \
                           1916.78, 123420, 123420, -nan)
reports[-1].sigmaresid = ValErr(0.238242, 0.000479524, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000703712, None, 0.000427411, None, -0.000160827, None, 0.000445522, None, -0.000160827, None, 0.000445522, None, 0.00109023, None, 0.000442783, None, 0.00109023, None, 0.000442783, None, 0.238242, None, 0.00537563, None, 0.238242, None, 0.00537563, None)

reports.append(Report(604017904, ("CSC", 1, 1, 1, 30), "MEp11_30"))
reports[-1].posNum = 129114
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000639197, 0.000654341, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.20147e-05, 1.56284e-05, 0), \
                           4730.65, 129114, 129114, -nan)
reports[-1].sigmaresid = ValErr(0.233266, 0.000459038, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000185108, None, 0.000408331, None, -0.000576134, None, 0.000372805, None, -0.000576134, None, 0.000372805, None, 0.000956079, None, 0.000313729, None, 0.000956079, None, 0.000313729, None, 0.233266, None, 0.00517038, None, 0.233266, None, 0.00517038, None)

reports.append(Report(604017920, ("CSC", 1, 1, 1, 32), "MEp11_32"))
reports[-1].posNum = 119410
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00030191, 0.000463417, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.25272e-05, 1.63322e-05, 0), \
                           3734.55, 119410, 119410, -nan)
reports[-1].sigmaresid = ValErr(0.23452, 0.000479766, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000711507, None, 0.00115163, None, -0.000247693, None, 0.00103263, None, -0.000247693, None, 0.00103263, None, -0.000365352, None, 0.00111914, None, -0.000365352, None, 0.00111914, None, 0.234521, None, 0.00531483, None, 0.234521, None, 0.00531483, None)

reports.append(Report(604017936, ("CSC", 1, 1, 1, 34), "MEp11_34"))
reports[-1].posNum = 113646
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000438262, 0.000584224, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.37362e-06, 1.58532e-05, 0), \
                           5413.47, 113646, 113646, -nan)
reports[-1].sigmaresid = ValErr(0.230715, 0.000483907, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00199665, None, 0.000249187, None, 0.000363483, None, 0.000248441, None, 0.000363483, None, 0.000248441, None, -0.00043688, None, 0.000154998, None, -0.00043688, None, 0.000154998, None, 0.230715, None, 0.00628728, None, 0.230715, None, 0.00628728, None)

reports.append(Report(604017952, ("CSC", 1, 1, 1, 36), "MEp11_36"))
reports[-1].posNum = 125090
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000462568, 0.000663473, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.10059e-06, 1.58485e-05, 0), \
                           4628.82, 125090, 125090, -nan)
reports[-1].sigmaresid = ValErr(0.23318, 0.000466192, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00157615, None, 0.00057322, None, 0.000457679, None, 0.000564876, None, 0.000457679, None, 0.000564876, None, 0.00276466, None, 0.000561152, None, 0.00276466, None, 0.000561152, None, 0.233181, None, 0.00546178, None, 0.233181, None, 0.00546178, None)

reports.append(Report(604018184, ("CSC", 1, 1, 2, 1), "MEp12_01"))
reports[-1].posNum = 45174
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00658353, 0.00394366, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0001314, 7.41754e-05, 0), \
                           -50040.4, 45174, 45174, -nan)
reports[-1].sigmaresid = ValErr(0.732558, 0.00243715, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00136721, None, 0.00044437, None, -0.00318839, None, 0.000273307, None, -0.00318839, None, 0.000273307, None, -0.0045712, None, 0.000367488, None, -0.0045712, None, 0.000367488, None, 0.732584, None, 0.00736048, None, 0.732584, None, 0.00736048, None)

reports.append(Report(604018200, ("CSC", 1, 1, 2, 3), "MEp12_03"))
reports[-1].posNum = 56270
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00270409, 0.00368002, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.25101e-05, 7.12121e-05, 0), \
                           -59134.3, 56270, 56270, -nan)
reports[-1].sigmaresid = ValErr(0.692093, 0.00206305, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00187787, None, 0.000135426, None, -0.00136523, None, -1.0365e-05, None, -0.00136523, None, -1.0365e-05, None, -0.00750507, None, -6.47263e-07, None, -0.00750507, None, -6.47263e-07, None, 0.692095, None, 0.0057583, None, 0.692095, None, 0.0057583, None)

reports.append(Report(604018216, ("CSC", 1, 1, 2, 5), "MEp12_05"))
reports[-1].posNum = 57174
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000370463, 0.00355906, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.95894e-05, 6.90951e-05, 0), \
                           -61866.7, 57174, 57174, -nan)
reports[-1].sigmaresid = ValErr(0.714009, 0.00211149, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00401812, None, 0.000347974, None, 0.00148049, None, 0.000190638, None, 0.00148049, None, 0.000190638, None, -9.01216e-05, None, 0.000189181, None, -9.01216e-05, None, 0.000189181, None, 0.714011, None, 0.00648386, None, 0.714011, None, 0.00648386, None)

reports.append(Report(604018232, ("CSC", 1, 1, 2, 7), "MEp12_07"))
reports[-1].posNum = 61314
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00194435, 0.00341197, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.97378e-05, 6.57473e-05, 0), \
                           -67058.8, 61314, 61314, -nan)
reports[-1].sigmaresid = ValErr(0.722352, 0.00206279, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00111517, None, -4.88144e-05, None, 0.000605543, None, -0.000140184, None, 0.000605543, None, -0.000140184, None, 0.00219111, None, -0.000177203, None, 0.00219111, None, -0.000177203, None, 0.722355, None, 0.00598746, None, 0.722355, None, 0.00598746, None)

reports.append(Report(604018248, ("CSC", 1, 1, 2, 9), "MEp12_09"))
reports[-1].posNum = 59466
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00267628, 0.00347158, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(8.15568e-05, 6.63027e-05, 0), \
                           -65425.9, 59466, 59466, -nan)
reports[-1].sigmaresid = ValErr(0.727083, 0.00210831, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00142762, None, -0.000724613, None, -0.000488718, None, -0.000776453, None, -0.000488718, None, -0.000776453, None, -0.0074943, None, -0.000798486, None, -0.0074943, None, -0.000798486, None, 0.727091, None, 0.00906163, None, 0.727091, None, 0.00906163, None)

reports.append(Report(604018264, ("CSC", 1, 1, 2, 11), "MEp12_11"))
reports[-1].posNum = 61360
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00258369, 0.00343952, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(8.68089e-05, 6.68927e-05, 0), \
                           -67341.3, 61360, 61360, -nan)
reports[-1].sigmaresid = ValErr(0.72509, 0.00206983, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00120734, None, -0.000943016, None, -0.000239648, None, -0.00113997, None, -0.000239648, None, -0.00113997, None, 0.00102719, None, -0.0011353, None, 0.00102719, None, -0.0011353, None, 0.7251, None, 0.00603463, None, 0.7251, None, 0.00603463, None)

reports.append(Report(604018280, ("CSC", 1, 1, 2, 13), "MEp12_13"))
reports[-1].posNum = 44362
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00606396, 0.00407783, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000109424, 7.78405e-05, 0), \
                           -47704.2, 44362, 44362, -nan)
reports[-1].sigmaresid = ValErr(0.709213, 0.00238098, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00255256, None, -0.000997978, None, 0.00283061, None, -0.00107858, None, 0.00283061, None, -0.00107858, None, -0.000368959, None, -0.00110471, None, -0.000368959, None, -0.00110471, None, 0.709228, None, 0.00578868, None, 0.709228, None, 0.00578868, None)

reports.append(Report(604018296, ("CSC", 1, 1, 2, 15), "MEp12_15"))
reports[-1].posNum = 51866
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00253103, 0.00357738, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.39355e-05, 6.88215e-05, 0), \
                           -56828, 51866, 51866, -nan)
reports[-1].sigmaresid = ValErr(0.723779, 0.00224724, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000857436, None, -0.00212998, None, 0.000288795, None, -0.00218394, None, 0.000288795, None, -0.00218394, None, -0.000530948, None, -0.00219887, None, -0.000530948, None, -0.00219887, None, 0.723792, None, 0.00589254, None, 0.723792, None, 0.00589254, None)

reports.append(Report(604018312, ("CSC", 1, 1, 2, 17), "MEp12_17"))
reports[-1].posNum = 58486
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000803081, 0.00348188, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.8169e-05, 6.68385e-05, 0), \
                           -62030.9, 58486, 58486, -nan)
reports[-1].sigmaresid = ValErr(0.698844, 0.00204333, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00326673, None, 0.000106762, None, 0.000275176, None, -0.000100761, None, 0.000275176, None, -0.000100761, None, 0.00121963, None, -0.000106034, None, 0.00121963, None, -0.000106034, None, 0.698844, None, 0.0063982, None, 0.698844, None, 0.0063982, None)

reports.append(Report(604018328, ("CSC", 1, 1, 2, 19), "MEp12_19"))
reports[-1].posNum = 65808
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0056658, 0.00317375, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000141711, 6.07316e-05, 0), \
                           -71953.5, 65808, 65808, -nan)
reports[-1].sigmaresid = ValErr(0.722128, 0.00199049, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00161215, None, -0.000661865, None, 0.00224524, None, -0.000798985, None, 0.00224524, None, -0.000798985, None, -0.00375232, None, -0.000829122, None, -0.00375232, None, -0.000829122, None, 0.722157, None, 0.00609483, None, 0.722157, None, 0.00609483, None)

reports.append(Report(604018344, ("CSC", 1, 1, 2, 21), "MEp12_21"))
reports[-1].posNum = 38044
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00539399, 0.00433584, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.70086e-05, 8.22636e-05, 0), \
                           -40877.4, 38044, 38044, -nan)
reports[-1].sigmaresid = ValErr(0.708601, 0.00256888, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00236859, None, -0.000351392, None, 0.00289089, None, -0.000554086, None, 0.00289089, None, -0.000554086, None, 0.00740879, None, -0.000471181, None, 0.00740879, None, -0.000471181, None, 0.708612, None, 0.00640212, None, 0.708612, None, 0.00640212, None)

reports.append(Report(604018360, ("CSC", 1, 1, 2, 23), "MEp12_23"))
reports[-1].posNum = 62800
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00360558, 0.0033075, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.6107e-05, 6.33224e-05, 0), \
                           -69420.9, 62800, 62800, -nan)
reports[-1].sigmaresid = ValErr(0.730878, 0.00206229, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00472751, None, -0.000654193, None, 0.00148385, None, -0.000856048, None, 0.00148385, None, -0.000856048, None, -0.00465375, None, -0.000821008, None, -0.00465375, None, -0.000821008, None, 0.730888, None, 0.006163, None, 0.730888, None, 0.006163, None)

reports.append(Report(604018376, ("CSC", 1, 1, 2, 25), "MEp12_25"))
reports[-1].posNum = 60236
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00716558, 0.00351681, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000129756, 6.77838e-05, 0), \
                           -65706.1, 60236, 60236, -nan)
reports[-1].sigmaresid = ValErr(0.720271, 0.00207517, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0034664, None, -0.000646479, None, 0.0034562, None, -0.000695628, None, 0.0034562, None, -0.000695628, None, 0.00860094, None, -0.000763455, None, 0.00860094, None, -0.000763455, None, 0.720293, None, 0.00639088, None, 0.720293, None, 0.00639088, None)

reports.append(Report(604018392, ("CSC", 1, 1, 2, 27), "MEp12_27"))
reports[-1].posNum = 51032
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00252698, 0.003847, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.76384e-05, 7.11891e-05, 0), \
                           -55145.9, 51032, 51032, -nan)
reports[-1].sigmaresid = ValErr(0.712964, 0.00223168, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000246982, None, -4.23628e-05, None, -0.00043714, None, -0.000202743, None, -0.00043714, None, -0.000202743, None, -0.00114481, None, -0.000160092, None, -0.00114481, None, -0.000160092, None, 0.71297, None, 0.00589705, None, 0.71297, None, 0.00589705, None)

reports.append(Report(604018408, ("CSC", 1, 1, 2, 29), "MEp12_29"))
reports[-1].posNum = 59850
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00330288, 0.00351846, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(8.22867e-05, 6.75625e-05, 0), \
                           -64814.4, 59850, 59850, -nan)
reports[-1].sigmaresid = ValErr(0.71463, 0.00206554, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000316328, None, -0.000281073, None, -0.000914313, None, -0.000426435, None, -0.000914313, None, -0.000426435, None, -0.0010763, None, -0.000422741, None, -0.0010763, None, -0.000422741, None, 0.714639, None, 0.00654736, None, 0.714639, None, 0.00654736, None)

reports.append(Report(604018424, ("CSC", 1, 1, 2, 31), "MEp12_31"))
reports[-1].posNum = 41480
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000825674, 0.00431622, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.26961e-05, 8.06969e-05, 0), \
                           -44578.1, 41480, 41480, -nan)
reports[-1].sigmaresid = ValErr(0.708752, 0.00246071, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00361127, None, -0.000636035, None, 0.00217716, None, -0.000759704, None, 0.00217716, None, -0.000759704, None, -0.00191618, None, -0.0006844, None, -0.00191618, None, -0.0006844, None, 0.708754, None, 0.00624198, None, 0.708754, None, 0.00624198, None)

reports.append(Report(604018440, ("CSC", 1, 1, 2, 33), "MEp12_33"))
reports[-1].posNum = 63536
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00222702, 0.00329719, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(7.63895e-05, 6.35277e-05, 0), \
                           -70492.9, 63536, 63536, -nan)
reports[-1].sigmaresid = ValErr(0.733856, 0.00205867, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00240232, None, -0.000366246, None, -0.000365341, None, -0.00051426, None, -0.000365341, None, -0.00051426, None, 0.00147353, None, -0.000521959, None, 0.00147353, None, -0.000521959, None, 0.733864, None, 0.00600684, None, 0.733864, None, 0.00600684, None)

reports.append(Report(604018456, ("CSC", 1, 1, 2, 35), "MEp12_35"))
reports[-1].posNum = 51168
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00294182, 0.00383924, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.05449e-05, 6.93947e-05, 0), \
                           -54930.9, 51168, 51168, -nan)
reports[-1].sigmaresid = ValErr(0.707938, 0.002213, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00125387, None, -0.00056056, None, -0.00164271, None, -0.000685925, None, -0.00164271, None, -0.000685925, None, -0.00500285, None, -0.000698027, None, -0.00500285, None, -0.000698027, None, 0.70794, None, 0.00583355, None, 0.70794, None, 0.00583355, None)

reports.append(Report(604018192, ("CSC", 1, 1, 2, 2), "MEp12_02"))
reports[-1].posNum = 50522
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0113076, 0.00375598, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000210022, 6.94275e-05, 0), \
                           -51984.2, 50522, 50522, -nan)
reports[-1].sigmaresid = ValErr(0.677059, 0.00212996, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00388578, None, 0.000847354, None, -0.00452059, None, 0.000600262, None, -0.00452059, None, 0.000600262, None, -0.00691122, None, 0.000707541, None, -0.00691122, None, 0.000707541, None, 0.67712, None, 0.00629428, None, 0.67712, None, 0.00629428, None)

reports.append(Report(604018208, ("CSC", 1, 1, 2, 4), "MEp12_04"))
reports[-1].posNum = 48196
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00734731, 0.0042522, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000125539, 7.97493e-05, 0), \
                           -47699, 48196, 48196, -nan)
reports[-1].sigmaresid = ValErr(0.650995, 0.00209679, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000394155, None, 0.000302254, None, -0.00254644, None, 0.00016854, None, -0.00254644, None, 0.00016854, None, 0.00197236, None, 0.000227398, None, 0.00197236, None, 0.000227398, None, 0.651013, None, 0.00678543, None, 0.651013, None, 0.00678543, None)

reports.append(Report(604018224, ("CSC", 1, 1, 2, 6), "MEp12_06"))
reports[-1].posNum = 57874
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000418076, 0.00341061, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.16897e-05, 6.6354e-05, 0), \
                           -60731.8, 57874, 57874, -nan)
reports[-1].sigmaresid = ValErr(0.691039, 0.00203117, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00252675, None, 0.000302363, None, -0.000459905, None, 0.000156302, None, -0.000459905, None, 0.000156302, None, 0.000610889, None, 0.000176329, None, 0.000610889, None, 0.000176329, None, 0.69104, None, 0.00596407, None, 0.69104, None, 0.00596407, None)

reports.append(Report(604018240, ("CSC", 1, 1, 2, 8), "MEp12_08"))
reports[-1].posNum = 52956
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00355556, 0.00349757, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000103627, 6.51128e-05, 0), \
                           -53722.3, 52956, 52956, -nan)
reports[-1].sigmaresid = ValErr(0.667332, 0.00205054, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000524753, None, -0.000185429, None, 0.000443834, None, -0.000358237, None, 0.000443834, None, -0.000358237, None, -0.00236575, None, -0.000342869, None, -0.00236575, None, -0.000342869, None, 0.667348, None, 0.00576024, None, 0.667348, None, 0.00576024, None)

reports.append(Report(604018256, ("CSC", 1, 1, 2, 10), "MEp12_10"))
reports[-1].posNum = 57988
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000715449, 0.00339104, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.94044e-06, 6.5558e-05, 0), \
                           -60858.4, 57988, 57988, -nan)
reports[-1].sigmaresid = ValErr(0.691121, 0.00202941, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00179179, None, 5.57666e-05, None, -0.000938204, None, -0.000114535, None, -0.000938204, None, -0.000114535, None, -0.00129568, None, -5.85707e-05, None, -0.00129568, None, -5.85707e-05, None, 0.691122, None, 0.00596238, None, 0.691122, None, 0.00596238, None)

reports.append(Report(604018272, ("CSC", 1, 1, 2, 12), "MEp12_12"))
reports[-1].posNum = 55874
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00109141, 0.0034535, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.3865e-05, 6.33369e-05, 0), \
                           -57217.2, 55874, 55874, -nan)
reports[-1].sigmaresid = ValErr(0.673748, 0.00201547, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00193496, None, -0.000609085, None, -4.91408e-05, None, -0.000692736, None, -4.91408e-05, None, -0.000692736, None, -0.00154835, None, -0.000714205, None, -0.00154835, None, -0.000714205, None, 0.67375, None, 0.00623551, None, 0.67375, None, 0.00623551, None)

reports.append(Report(604018288, ("CSC", 1, 1, 2, 14), "MEp12_14"))
reports[-1].posNum = 63980
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000803964, 0.00313361, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.17617e-05, 6.04352e-05, 0), \
                           -67995.2, 63980, 63980, -nan)
reports[-1].sigmaresid = ValErr(0.700346, 0.00195783, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000187188, None, -0.000445909, None, 3.27462e-05, None, -0.000624735, None, 3.27462e-05, None, -0.000624735, None, 0.00268541, None, -0.000588805, None, 0.00268541, None, -0.000588805, None, 0.700347, None, 0.00566392, None, 0.700347, None, 0.00566392, None)

reports.append(Report(604018304, ("CSC", 1, 1, 2, 16), "MEp12_16"))
reports[-1].posNum = 56962
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00801187, 0.00339852, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000152821, 6.31766e-05, 0), \
                           -59203.5, 56962, 56962, -nan)
reports[-1].sigmaresid = ValErr(0.684144, 0.00202694, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00369254, None, -0.000455013, None, 0.00359589, None, -0.000429971, None, 0.00359589, None, -0.000429971, None, 0.00090912, None, -0.000439192, None, 0.00090912, None, -0.000439192, None, 0.684179, None, 0.00636294, None, 0.684179, None, 0.00636294, None)

reports.append(Report(604018320, ("CSC", 1, 1, 2, 18), "MEp12_18"))
reports[-1].posNum = 59810
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00710719, 0.00323947, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000143581, 6.10861e-05, 0), \
                           -62041.3, 59810, 59810, -nan)
reports[-1].sigmaresid = ValErr(0.682745, 0.00197404, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(9.58433e-06, None, -0.000636097, None, 0.00324543, None, -0.000863092, None, 0.00324543, None, -0.000863092, None, 0.00417621, None, -0.000918588, None, 0.00417621, None, -0.000918588, None, 0.682778, None, 0.00618545, None, 0.682778, None, 0.00618545, None)

reports.append(Report(604018336, ("CSC", 1, 1, 2, 20), "MEp12_20"))
reports[-1].posNum = 49040
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0122974, 0.00361487, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000213797, 6.48653e-05, 0), \
                           -52022.1, 49040, 49040, -nan)
reports[-1].sigmaresid = ValErr(0.698982, 0.00223191, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00104804, None, 0.000127312, None, 0.00648994, None, 7.76143e-05, None, 0.00648994, None, 7.76143e-05, None, 0.00685797, None, 0.000113181, None, 0.00685797, None, 0.000113181, None, 0.69906, None, 0.00630522, None, 0.69906, None, 0.00630522, None)

reports.append(Report(604018352, ("CSC", 1, 1, 2, 22), "MEp12_22"))
reports[-1].posNum = 53648
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00483466, 0.00354949, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000127441, 6.56643e-05, 0), \
                           -56440.6, 53648, 53648, -nan)
reports[-1].sigmaresid = ValErr(0.69289, 0.0021153, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00170438, None, -0.000291624, None, 0.00112694, None, -0.00045662, None, 0.00112694, None, -0.00045662, None, 0.00266267, None, -0.000420967, None, 0.00266267, None, -0.000420967, None, 0.692914, None, 0.00610814, None, 0.692914, None, 0.00610814, None)

reports.append(Report(604018368, ("CSC", 1, 1, 2, 24), "MEp12_24"))
reports[-1].posNum = 59502
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0017069, 0.00329592, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.32863e-05, 6.26607e-05, 0), \
                           -63373.2, 59502, 59502, -nan)
reports[-1].sigmaresid = ValErr(0.70196, 0.00203485, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00130092, None, -0.000184063, None, -0.00136669, None, -0.000291813, None, -0.00136669, None, -0.000291813, None, -0.00298268, None, -0.000311277, None, -0.00298268, None, -0.000311277, None, 0.70196, None, 0.00588398, None, 0.70196, None, 0.00588398, None)

reports.append(Report(604018384, ("CSC", 1, 1, 2, 26), "MEp12_26"))
reports[-1].posNum = 49388
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00119344, 0.0038537, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.4005e-06, 6.87475e-05, 0), \
                           -48776.9, 49388, 49388, -nan)
reports[-1].sigmaresid = ValErr(0.649657, 0.00206708, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000423164, None, -0.000440379, None, -0.00131755, None, -0.000514016, None, -0.00131755, None, -0.000514016, None, 7.69922e-05, None, -0.00054366, None, 7.69922e-05, None, -0.00054366, None, 0.649657, None, 0.00659587, None, 0.649657, None, 0.00659587, None)

reports.append(Report(604018400, ("CSC", 1, 1, 2, 28), "MEp12_28"))
reports[-1].posNum = 60780
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000905799, 0.0032992, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.35854e-05, 6.33951e-05, 0), \
                           -65217.5, 60780, 60780, -nan)
reports[-1].sigmaresid = ValErr(0.707563, 0.00202941, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000411973, None, -0.000455083, None, 0.000212959, None, -0.000589997, None, 0.000212959, None, -0.000589997, None, 5.92824e-05, None, -0.000560653, None, 5.92824e-05, None, -0.000560653, None, 0.707566, None, 0.00629474, None, 0.707566, None, 0.00629474, None)

reports.append(Report(604018416, ("CSC", 1, 1, 2, 30), "MEp12_30"))
reports[-1].posNum = 43702
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00578574, 0.00417071, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000112724, 7.23271e-05, 0), \
                           -42686.3, 43702, 43702, -nan)
reports[-1].sigmaresid = ValErr(0.642633, 0.00217369, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00191973, None, -0.000563662, None, -0.00139379, None, -0.000720884, None, -0.00139379, None, -0.000720884, None, -0.00220766, None, -0.000651359, None, -0.00220766, None, -0.000651359, None, 0.642652, None, 0.00591409, None, 0.642652, None, 0.00591409, None)

reports.append(Report(604018432, ("CSC", 1, 1, 2, 32), "MEp12_32"))
reports[-1].posNum = 56294
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0110127, 0.00343073, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000227119, 6.58928e-05, 0), \
                           -59240.9, 56294, 56294, -nan)
reports[-1].sigmaresid = ValErr(0.693092, 0.00206559, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00369005, None, -0.000330105, None, -0.00481328, None, -0.000547554, None, -0.00481328, None, -0.000547554, None, 0.000599802, None, -0.000504662, None, 0.000599802, None, -0.000504662, None, 0.693166, None, 0.00585782, None, 0.693166, None, 0.00585782, None)

reports.append(Report(604018448, ("CSC", 1, 1, 2, 34), "MEp12_34"))
reports[-1].posNum = 51352
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00229465, 0.00364199, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.32008e-05, 6.59976e-05, 0), \
                           -54615.7, 51352, 51352, -nan)
reports[-1].sigmaresid = ValErr(0.700904, 0.00218708, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00285499, None, -0.000126347, None, -0.000744814, None, -0.00024822, None, -0.000744814, None, -0.00024822, None, 0.00180092, None, -0.000241041, None, 0.00180092, None, -0.000241041, None, 0.700909, None, 0.00574352, None, 0.700909, None, 0.00574352, None)

reports.append(Report(604018464, ("CSC", 1, 1, 2, 36), "MEp12_36"))
reports[-1].posNum = 34638
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00177246, 0.00433318, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.01228e-05, 7.68655e-05, 0), \
                           -36287.9, 34638, 34638, -nan)
reports[-1].sigmaresid = ValErr(0.689832, 0.00262091, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00338629, None, -0.000747634, None, -0.000308969, None, -0.000957141, None, -0.000308969, None, -0.000957141, None, -0.000447424, None, -0.000910343, None, -0.000447424, None, -0.000910343, None, 0.689836, None, 0.00622886, None, 0.689836, None, 0.00622886, None)

reports.append(Report(604018696, ("CSC", 1, 1, 3, 1), "MEp13_01"))
reports[-1].posNum = 9760
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00297893, 0.0212678, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.86403e-05, 0.000428133, 0), \
                           -20946.2, 9760, 9760, -nan)
reports[-1].sigmaresid = ValErr(2.06926, 0.0148107, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00247503, None, 0.00155245, None, 0.00255986, None, 0.00139719, None, 0.00255986, None, 0.00139719, None, -0.0157552, None, 0.00158402, None, -0.0157552, None, 0.00158402, None, 2.06926, None, 0.0104888, None, 2.06926, None, 0.0104888, None)

reports.append(Report(604018704, ("CSC", 1, 1, 3, 2), "MEp13_02"))
reports[-1].posNum = 9208
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00874401, 0.022809, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000168757, 0.000485013, 0), \
                           -19796.8, 9208, 9208, -nan)
reports[-1].sigmaresid = ValErr(2.07719, 0.0153067, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00593593, None, 0.00105617, None, 0.0111717, None, 0.00105305, None, 0.0111717, None, 0.00105305, None, -0.0137817, None, 0.00116344, None, -0.0137817, None, 0.00116344, None, 2.0772, None, 0.00922447, None, 2.0772, None, 0.00922447, None)

reports.append(Report(604018712, ("CSC", 1, 1, 3, 3), "MEp13_03"))
reports[-1].posNum = 11026
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00574609, 0.0202571, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000110487, 0.000456012, 0), \
                           -23313.5, 11026, 11026, -nan)
reports[-1].sigmaresid = ValErr(2.00466, 0.0134995, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0223146, None, 0.00124546, None, -0.0073122, None, 0.00119008, None, -0.0073122, None, 0.00119008, None, -0.0338885, None, 0.00136401, None, -0.0338885, None, 0.00136401, None, 2.00466, None, 0.00879633, None, 2.00466, None, 0.00879633, None)

reports.append(Report(604018720, ("CSC", 1, 1, 3, 4), "MEp13_04"))
reports[-1].posNum = 10510
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00884121, 0.0223221, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.00015842, 0.000495714, 0), \
                           -22975.5, 10510, 10510, -nan)
reports[-1].sigmaresid = ValErr(2.15355, 0.0148538, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00253542, None, -0.000272657, None, 0.00642842, None, -0.000306433, None, 0.00642842, None, -0.000306433, None, 0.00149639, None, -0.000336218, None, 0.00149639, None, -0.000336218, None, 2.15356, None, 0.00917437, None, 2.15356, None, 0.00917437, None)

reports.append(Report(604018728, ("CSC", 1, 1, 3, 5), "MEp13_05"))
reports[-1].posNum = 10310
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00305762, 0.0204149, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.50865e-05, 0.000443542, 0), \
                           -21736.8, 10310, 10310, -nan)
reports[-1].sigmaresid = ValErr(1.9925, 0.0138758, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.012696, None, 0.000882013, None, 0.00235221, None, 0.000944842, None, 0.00235221, None, 0.000944842, None, -0.0330641, None, 0.00109718, None, -0.0330641, None, 0.00109718, None, 1.99248, None, 0.0095539, None, 1.99248, None, 0.0095539, None)

reports.append(Report(604018736, ("CSC", 1, 1, 3, 6), "MEp13_06"))
reports[-1].posNum = 10232
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0114975, 0.0213, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000147196, 0.000459467, 0), \
                           -22022.8, 10232, 10232, -nan)
reports[-1].sigmaresid = ValErr(2.08219, 0.0145556, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0148171, None, 0.00209418, None, -0.00975066, None, 0.00202307, None, -0.00975066, None, 0.00202307, None, -0.00371445, None, 0.0022241, None, -0.00371445, None, 0.0022241, None, 2.08217, None, 0.00918813, None, 2.08217, None, 0.00918813, None)

reports.append(Report(604018744, ("CSC", 1, 1, 3, 7), "MEp13_07"))
reports[-1].posNum = 11892
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00201215, 0.0185741, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.14596e-05, 0.00041337, 0), \
                           -24981.8, 11892, 11892, -nan)
reports[-1].sigmaresid = ValErr(1.97741, 0.0128219, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0364115, None, 0.00161014, None, -0.00228338, None, 0.00159093, None, -0.00228338, None, 0.00159093, None, 0.023552, None, 0.00157104, None, 0.023552, None, 0.00157104, None, 1.97741, None, 0.00917292, None, 1.97741, None, 0.00917292, None)

reports.append(Report(604018752, ("CSC", 1, 1, 3, 8), "MEp13_08"))
reports[-1].posNum = 14456
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00217286, 0.0168162, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000110916, 0.000377118, 0), \
                           -30513.6, 14456, 14456, -nan)
reports[-1].sigmaresid = ValErr(1.99744, 0.0117473, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00824423, None, -0.00204992, None, -0.00140175, None, -0.0019902, None, -0.00140175, None, -0.0019902, None, -0.016641, None, -0.0018854, None, -0.016641, None, -0.0018854, None, 1.99742, None, 0.00962769, None, 1.99742, None, 0.00962769, None)

reports.append(Report(604018760, ("CSC", 1, 1, 3, 9), "MEp13_09"))
reports[-1].posNum = 12490
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00828118, 0.0183685, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.00021309, 0.000395266, 0), \
                           -26648, 12490, 12490, -nan)
reports[-1].sigmaresid = ValErr(2.0434, 0.0129289, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0245522, None, 0.00273876, None, 0.00732899, None, 0.00274581, None, 0.00732899, None, 0.00274581, None, -0.0246631, None, 0.00299779, None, -0.0246631, None, 0.00299779, None, 2.04341, None, 0.00937307, None, 2.04341, None, 0.00937307, None)

reports.append(Report(604018768, ("CSC", 1, 1, 3, 10), "MEp13_10"))
reports[-1].posNum = 14068
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00571137, 0.0176199, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.90626e-07, 0.000365645, 0), \
                           -30325.1, 14068, 14068, -nan)
reports[-1].sigmaresid = ValErr(2.08897, 0.0124538, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0172615, None, -0.00208167, None, -0.00573301, None, -0.00191827, None, -0.00573301, None, -0.00191827, None, -0.0191114, None, -0.0018392, None, -0.0191114, None, -0.0018392, None, 2.08896, None, 0.0089677, None, 2.08896, None, 0.0089677, None)

reports.append(Report(604018776, ("CSC", 1, 1, 3, 11), "MEp13_11"))
reports[-1].posNum = 8774
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0108748, 0.0207206, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.10394e-05, 0.00042543, 0), \
                           -18260.9, 8774, 8774, -nan)
reports[-1].sigmaresid = ValErr(1.93926, 0.0146393, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0106998, None, -0.00129197, None, 0.0109358, None, -0.00129247, None, 0.0109358, None, -0.00129247, None, 0.0288822, None, -0.00112715, None, 0.0288822, None, -0.00112715, None, 1.93926, None, 0.00874753, None, 1.93926, None, 0.00874753, None)

reports.append(Report(604018784, ("CSC", 1, 1, 3, 12), "MEp13_12"))
reports[-1].posNum = 11604
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00207281, 0.0187502, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.65034e-05, 0.000401732, 0), \
                           -24603, 11604, 11604, -nan)
reports[-1].sigmaresid = ValErr(2.01633, 0.0132356, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00706978, None, -0.00196382, None, 0.00219998, None, -0.00210388, None, 0.00219998, None, -0.00210388, None, 0.00782764, None, -0.00201771, None, 0.00782764, None, -0.00201771, None, 2.01633, None, 0.00911816, None, 2.01633, None, 0.00911816, None)

reports.append(Report(604018792, ("CSC", 1, 1, 3, 13), "MEp13_13"))
reports[-1].posNum = 13048
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0127595, 0.0171703, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000269667, 0.000363465, 0), \
                           -27290.6, 13048, 13048, -nan)
reports[-1].sigmaresid = ValErr(1.95936, 0.012129, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00951435, None, -0.000485892, None, -0.013331, None, -0.00055905, None, -0.013331, None, -0.00055905, None, -0.035934, None, -0.000486193, None, -0.035934, None, -0.000486193, None, 1.9594, None, 0.0115801, None, 1.9594, None, 0.0115801, None)

reports.append(Report(604018800, ("CSC", 1, 1, 3, 14), "MEp13_14"))
reports[-1].posNum = 18414
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0040801, 0.0143543, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000113402, 0.000305225, 0), \
                           -38389.5, 18414, 18414, -nan)
reports[-1].sigmaresid = ValErr(1.94616, 0.0101412, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00616526, None, -0.000677611, None, -0.00388306, None, -0.00047528, None, -0.00388306, None, -0.00047528, None, -0.00368104, None, -0.000380255, None, -0.00368104, None, -0.000380255, None, 1.94617, None, 0.00945552, None, 1.94617, None, 0.00945552, None)

reports.append(Report(604018808, ("CSC", 1, 1, 3, 15), "MEp13_15"))
reports[-1].posNum = 16626
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00229587, 0.0155966, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000210369, 0.000339115, 0), \
                           -35188.5, 16626, 16626, -nan)
reports[-1].sigmaresid = ValErr(2.0088, 0.0110161, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0230516, None, -0.000918126, None, 0.00272459, None, -0.000894513, None, 0.00272459, None, -0.000894513, None, -0.0205304, None, -0.000706403, None, -0.0205304, None, -0.000706403, None, 2.00882, None, 0.00910396, None, 2.00882, None, 0.00910396, None)

reports.append(Report(604018816, ("CSC", 1, 1, 3, 16), "MEp13_16"))
reports[-1].posNum = 14910
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00598182, 0.0165298, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.44908e-05, 0.000369072, 0), \
                           -31589.2, 14910, 14910, -nan)
reports[-1].sigmaresid = ValErr(2.0132, 0.0116582, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0308761, None, -0.000791568, None, 0.00590278, None, -0.00100781, None, 0.00590278, None, -0.00100781, None, 0.0267306, None, -0.000573332, None, 0.0267306, None, -0.000573332, None, 2.01319, None, 0.012136, None, 2.01319, None, 0.012136, None)

reports.append(Report(604018824, ("CSC", 1, 1, 3, 17), "MEp13_17"))
reports[-1].posNum = 14212
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00340654, 0.0168698, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.74333e-06, 0.000372401, 0), \
                           -30088.1, 14212, 14212, -nan)
reports[-1].sigmaresid = ValErr(2.01003, 0.0119223, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0142646, None, 0.0015075, None, 0.00343017, None, 0.00141614, None, 0.00343017, None, 0.00141614, None, -0.0129234, None, 0.00150559, None, -0.0129234, None, 0.00150559, None, 2.01003, None, 0.00966203, None, 2.01003, None, 0.00966203, None)

reports.append(Report(604018832, ("CSC", 1, 1, 3, 18), "MEp13_18"))
reports[-1].posNum = 13774
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00125244, 0.0164155, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.74017e-06, 0.000347109, 0), \
                           -28572.7, 13774, 13774, -nan)
reports[-1].sigmaresid = ValErr(1.92601, 0.0116042, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0172843, None, 0.000639831, None, 0.00124473, None, 0.000735691, None, 0.00124473, None, 0.000735691, None, 0.0162757, None, 0.000794445, None, 0.0162757, None, 0.000794445, None, 1.92601, None, 0.0103825, None, 1.92601, None, 0.0103825, None)

reports.append(Report(604018840, ("CSC", 1, 1, 3, 19), "MEp13_19"))
reports[-1].posNum = 12410
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00832371, 0.0182785, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000185561, 0.000375979, 0), \
                           -26335.5, 12410, 12410, -nan)
reports[-1].sigmaresid = ValErr(2.02018, 0.012823, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.033008, None, 0.00119546, None, -0.00725715, None, 0.0012002, None, -0.00725715, None, 0.0012002, None, -0.0129243, None, 0.00136188, None, -0.0129243, None, 0.00136188, None, 2.02019, None, 0.0094777, None, 2.02019, None, 0.0094777, None)

reports.append(Report(604018848, ("CSC", 1, 1, 3, 20), "MEp13_20"))
reports[-1].posNum = 18370
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00293652, 0.0146469, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.89358e-05, 0.000316351, 0), \
                           -38662, 18370, 18370, -nan)
reports[-1].sigmaresid = ValErr(1.98514, 0.0103567, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00289977, None, -0.000295137, None, -0.00291993, None, -0.000159177, None, -0.00291993, None, -0.000159177, None, -0.00401789, None, -3.78115e-06, None, -0.00401789, None, -3.78115e-06, None, 1.98514, None, 0.0101164, None, 1.98514, None, 0.0101164, None)

reports.append(Report(604018856, ("CSC", 1, 1, 3, 21), "MEp13_21"))
reports[-1].posNum = 16264
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000691841, 0.016163, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.09465e-05, 0.000364983, 0), \
                           -34604.2, 16264, 16264, -nan)
reports[-1].sigmaresid = ValErr(2.03138, 0.0112633, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0317618, None, 0.000364089, None, 0.00112689, None, 0.000556013, None, 0.00112689, None, 0.000556013, None, 0.000680977, None, 0.000659434, None, 0.000680977, None, 0.000659434, None, 2.03138, None, 0.00935867, None, 2.03138, None, 0.00935867, None)

reports.append(Report(604018864, ("CSC", 1, 1, 3, 22), "MEp13_22"))
reports[-1].posNum = 14378
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00329972, 0.0173626, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000219223, 0.000374211, 0), \
                           -30836, 14378, 14378, -nan)
reports[-1].sigmaresid = ValErr(2.06623, 0.0121847, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.016772, None, 0.0013564, None, 0.00454728, None, 0.00139446, None, 0.00454728, None, 0.00139446, None, -0.00354026, None, 0.00165996, None, -0.00354026, None, 0.00165996, None, 2.06626, None, 0.00897515, None, 2.06626, None, 0.00897515, None)

reports.append(Report(604018872, ("CSC", 1, 1, 3, 23), "MEp13_23"))
reports[-1].posNum = 13688
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00454869, 0.0174644, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000239794, 0.000361092, 0), \
                           -29202.3, 13688, 13688, -nan)
reports[-1].sigmaresid = ValErr(2.04313, 0.0123484, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0026411, None, -0.000175294, None, -0.00465715, None, -7.83979e-05, None, -0.00465715, None, -7.83979e-05, None, 0.00552039, None, -2.34846e-05, None, 0.00552039, None, -2.34846e-05, None, 2.04316, None, 0.0100453, None, 2.04316, None, 0.0100453, None)

reports.append(Report(604018880, ("CSC", 1, 1, 3, 24), "MEp13_24"))
reports[-1].posNum = 11824
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00829414, 0.0190708, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000119809, 0.000402501, 0), \
                           -25119.6, 11824, 11824, -nan)
reports[-1].sigmaresid = ValErr(2.0249, 0.0131676, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0341651, None, 0.000466281, None, -0.00706987, None, 0.000542534, None, -0.00706987, None, 0.000542534, None, -0.0302325, None, 0.000766198, None, -0.0302325, None, 0.000766198, None, 2.0249, None, 0.00943403, None, 2.0249, None, 0.00943403, None)

reports.append(Report(604018888, ("CSC", 1, 1, 3, 25), "MEp13_25"))
reports[-1].posNum = 11264
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0105228, 0.0221244, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000293192, 0.000483226, 0), \
                           -24366, 11264, 11264, -nan)
reports[-1].sigmaresid = ValErr(2.10482, 0.0140234, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000140015, None, 0.00270709, None, -0.00457216, None, 0.00250469, None, -0.00457216, None, 0.00250469, None, 0.0117218, None, 0.00263163, None, 0.0117218, None, 0.00263163, None, 2.10486, None, 0.00931293, None, 2.10486, None, 0.00931293, None)

reports.append(Report(604018896, ("CSC", 1, 1, 3, 26), "MEp13_26"))
reports[-1].posNum = 7686
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00496243, 0.0235978, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(7.50506e-05, 0.000514691, 0), \
                           -16170.5, 7686, 7686, -nan)
reports[-1].sigmaresid = ValErr(1.98371, 0.0159999, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00873655, None, 0.00211775, None, -0.00594842, None, 0.00210852, None, -0.00594842, None, 0.00210852, None, -0.0371268, None, 0.00231824, None, -0.0371268, None, 0.00231824, None, 1.98368, None, 0.0102334, None, 1.98368, None, 0.0102334, None)

reports.append(Report(604018904, ("CSC", 1, 1, 3, 27), "MEp13_27"))
reports[-1].posNum = 7718
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00901393, 0.0235653, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000410967, 0.000511049, 0), \
                           -16512.5, 7718, 7718, -nan)
reports[-1].sigmaresid = ValErr(2.05558, 0.0165452, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0180198, None, -0.00096794, None, -0.00674509, None, -0.000926787, None, -0.00674509, None, -0.000926787, None, -0.00556288, None, -0.000912045, None, -0.00556288, None, -0.000912045, None, 2.05564, None, 0.00881716, None, 2.05564, None, 0.00881716, None)

reports.append(Report(604018912, ("CSC", 1, 1, 3, 28), "MEp13_28"))
reports[-1].posNum = 17948
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00225296, 0.0146802, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000134955, 0.000313475, 0), \
                           -37566.9, 17948, 17948, -nan)
reports[-1].sigmaresid = ValErr(1.96238, 0.0103576, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0258077, None, -0.000880927, None, 0.002676, None, -0.000824691, None, 0.002676, None, -0.000824691, None, -0.0116043, None, -0.000747801, None, -0.0116043, None, -0.000747801, None, 1.96239, None, 0.0103028, None, 1.96239, None, 0.0103028, None)

reports.append(Report(604018920, ("CSC", 1, 1, 3, 29), "MEp13_29"))
reports[-1].posNum = 12414
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00990248, 0.0171636, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000286321, 0.000362019, 0), \
                           -25661.1, 12414, 12414, -nan)
reports[-1].sigmaresid = ValErr(1.91206, 0.0121348, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0247384, None, 0.00232191, None, 0.00969748, None, 0.00232333, None, 0.00969748, None, 0.00232333, None, 0.0105495, None, 0.00269114, None, 0.0105495, None, 0.00269114, None, 1.9121, None, 0.00956463, None, 1.9121, None, 0.00956463, None)

reports.append(Report(604018928, ("CSC", 1, 1, 3, 30), "MEp13_30"))
reports[-1].posNum = 10038
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000530247, 0.0218872, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000215993, 0.000479928, 0), \
                           -21877.9, 10038, 10038, -nan)
reports[-1].sigmaresid = ValErr(2.1395, 0.0150999, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0277787, None, -0.00157149, None, -0.00269148, None, -0.00164703, None, -0.00269148, None, -0.00164703, None, -0.0140509, None, -0.00150493, None, -0.0140509, None, -0.00150493, None, 2.13952, None, 0.00949956, None, 2.13952, None, 0.00949956, None)

reports.append(Report(604018936, ("CSC", 1, 1, 3, 31), "MEp13_31"))
reports[-1].posNum = 13422
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0095092, 0.0166509, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(9.89644e-07, 0.000366985, 0), \
                           -27780.2, 13422, 13422, -nan)
reports[-1].sigmaresid = ValErr(1.91709, 0.0117009, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0221306, None, 0.000876033, None, 0.00950266, None, 0.000829734, None, 0.00950266, None, 0.000829734, None, 0.00837501, None, 0.00101448, None, 0.00837501, None, 0.00101448, None, 1.91709, None, 0.00888562, None, 1.91709, None, 0.00888562, None)

reports.append(Report(604018944, ("CSC", 1, 1, 3, 32), "MEp13_32"))
reports[-1].posNum = 17540
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00365353, 0.0151536, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000116411, 0.000324219, 0), \
                           -37100.3, 17540, 17540, -nan)
reports[-1].sigmaresid = ValErr(2.00621, 0.0107114, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.008506, None, 0.000986871, None, -0.00379001, None, 0.0010252, None, -0.00379001, None, 0.0010252, None, -0.0097413, None, 0.00110851, None, -0.0097413, None, 0.00110851, None, 2.00621, None, 0.00946205, None, 2.00621, None, 0.00946205, None)

reports.append(Report(604018952, ("CSC", 1, 1, 3, 33), "MEp13_33"))
reports[-1].posNum = 14880
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00790087, 0.0161908, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.20652e-05, 0.000358025, 0), \
                           -31240.5, 14880, 14880, -nan)
reports[-1].sigmaresid = ValErr(1.97497, 0.0114484, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00847022, None, 0.00247794, None, -0.00788808, None, 0.00243658, None, -0.00788808, None, 0.00243658, None, -0.00827241, None, 0.00272416, None, -0.00827241, None, 0.00272416, None, 1.97497, None, 0.00952921, None, 1.97497, None, 0.00952921, None)

reports.append(Report(604018960, ("CSC", 1, 1, 3, 34), "MEp13_34"))
reports[-1].posNum = 18116
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00343069, 0.0151739, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.04114e-05, 0.000339447, 0), \
                           -38609.5, 18116, 18116, -nan)
reports[-1].sigmaresid = ValErr(2.03867, 0.0107103, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00108803, None, -0.00129395, None, -0.00323553, None, -0.00128908, None, -0.00323553, None, -0.00128908, None, -0.00831355, None, -0.00123268, None, -0.00831355, None, -0.00123268, None, 2.03868, None, 0.00909746, None, 2.03868, None, 0.00909746, None)

reports.append(Report(604018968, ("CSC", 1, 1, 3, 35), "MEp13_35"))
reports[-1].posNum = 16368
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00463918, 0.0158464, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.18146e-05, 0.000368335, 0), \
                           -34764, 16368, 16368, -nan)
reports[-1].sigmaresid = ValErr(2.02377, 0.0111853, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00893403, None, 0.00156599, None, 0.0048757, None, 0.00143998, None, 0.0048757, None, 0.00143998, None, -0.0197338, None, 0.00185403, None, -0.0197338, None, 0.00185403, None, 2.02377, None, 0.00990006, None, 2.02377, None, 0.00990006, None)

reports.append(Report(604018976, ("CSC", 1, 1, 3, 36), "MEp13_36"))
reports[-1].posNum = 10476
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0039376, 0.0201815, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.2001e-05, 0.00041476, 0), \
                           -22402.3, 10476, 10476, -nan)
reports[-1].sigmaresid = ValErr(2.05341, 0.0141861, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0144771, None, -0.00137805, None, 0.0039641, None, -0.00139155, None, 0.0039641, None, -0.00139155, None, 0.0130272, None, -0.00143802, None, 0.0130272, None, -0.00143802, None, 2.05341, None, 0.00916766, None, 2.05341, None, 0.00916766, None)

reports.append(Report(604017160, ("CSC", 1, 1, 4, 1), "MEp14_01"))
reports[-1].posNum = 97540
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000377833, 0.000841781, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.05919e-06, 2.10588e-05, 0), \
                           -8087.72, 97540, 97540, -nan)
reports[-1].sigmaresid = ValErr(0.262889, 0.000595205, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00128222, None, 0.000722655, None, 0.000376627, None, 0.00069623, None, 0.000376627, None, 0.00069623, None, 0.000925405, None, 0.000723246, None, 0.000925405, None, 0.000723246, None, 0.26289, None, 0.00581969, None, 0.26289, None, 0.00581969, None)

reports.append(Report(604017176, ("CSC", 1, 1, 4, 3), "MEp14_03"))
reports[-1].posNum = 115828
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000709281, 0.00135874, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.7471e-06, 2.35931e-05, 0), \
                           -8159.71, 115828, 115828, -nan)
reports[-1].sigmaresid = ValErr(0.259631, 0.000540388, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00089427, None, -0.000626342, None, 0.000678114, None, -0.000665912, None, 0.000678114, None, -0.000665912, None, 0.00028239, None, -0.000694578, None, 0.00028239, None, -0.000694578, None, 0.259632, None, 0.00475711, None, 0.259632, None, 0.00475711, None)

reports.append(Report(604017192, ("CSC", 1, 1, 4, 5), "MEp14_05"))
reports[-1].posNum = 116862
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000522567, 0.000771748, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.10538e-06, 1.94038e-05, 0), \
                           -10001.3, 116862, 116862, -nan)
reports[-1].sigmaresid = ValErr(0.263591, 0.000545229, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00154887, None, 0.000293565, None, 0.000510727, None, 0.00025701, None, 0.000510727, None, 0.00025701, None, -0.0011849, None, 0.00029034, None, -0.0011849, None, 0.00029034, None, 0.263591, None, 0.00487714, None, 0.263591, None, 0.00487714, None)

reports.append(Report(604017208, ("CSC", 1, 1, 4, 7), "MEp14_07"))
reports[-1].posNum = 114800
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000345993, 0.000771572, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.40014e-07, 1.90836e-05, 0), \
                           -8700.64, 114800, 114800, -nan)
reports[-1].sigmaresid = ValErr(0.261022, 0.000544743, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0012505, None, 0.000211403, None, 0.000344331, None, 0.0002013, None, 0.000344331, None, 0.0002013, None, 0.000744648, None, 0.000213113, None, 0.000744648, None, 0.000213113, None, 0.261022, None, 0.00571749, None, 0.261022, None, 0.00571749, None)

reports.append(Report(604017224, ("CSC", 1, 1, 4, 9), "MEp14_09"))
reports[-1].posNum = 122742
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000297136, 0.000748112, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.54219e-05, 1.85584e-05, 0), \
                           -9602.27, 122742, 122742, -nan)
reports[-1].sigmaresid = ValErr(0.261661, 0.000528113, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0010765, None, -0.000297735, None, -0.000261244, None, -0.000324708, None, -0.000261244, None, -0.000324708, None, 0.00200632, None, -0.000354491, None, 0.00200632, None, -0.000354491, None, 0.261661, None, 0.00538029, None, 0.261661, None, 0.00538029, None)

reports.append(Report(604017240, ("CSC", 1, 1, 4, 11), "MEp14_11"))
reports[-1].posNum = 114404
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000107638, 0.000782079, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.18028e-05, 1.94637e-05, 0), \
                           -10081.4, 114404, 114404, -nan)
reports[-1].sigmaresid = ValErr(0.264261, 0.000552455, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000521479, None, 0.000107577, None, -8.60633e-05, None, 3.35857e-05, None, -8.60633e-05, None, 3.35857e-05, None, 4.69195e-05, None, 9.88151e-05, None, 4.69195e-05, None, 9.88151e-05, None, 0.264261, None, 0.00516574, None, 0.264261, None, 0.00516574, None)

reports.append(Report(604017256, ("CSC", 1, 1, 4, 13), "MEp14_13"))
reports[-1].posNum = 112934
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000119368, 0.000776489, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.30286e-06, 1.91015e-05, 0), \
                           -8407.78, 112934, 112934, -nan)
reports[-1].sigmaresid = ValErr(0.260673, 0.000548489, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000129845, None, -0.000322806, None, -0.000123461, None, -0.000378221, None, -0.000123461, None, -0.000378221, None, 0.00105007, None, -0.000391316, None, 0.00105007, None, -0.000391316, None, 0.260673, None, 0.00494454, None, 0.260673, None, 0.00494454, None)

reports.append(Report(604017272, ("CSC", 1, 1, 4, 15), "MEp14_15"))
reports[-1].posNum = 104278
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00011362, 0.000838321, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.72588e-05, 2.13873e-05, 0), \
                           -11569.2, 104278, 104278, -nan)
reports[-1].sigmaresid = ValErr(0.270362, 0.000592017, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000761843, None, 0.000191381, None, -5.93493e-05, None, 0.000112271, None, -5.93493e-05, None, 0.000112271, None, -0.00128383, None, 0.000139201, None, -0.00128383, None, 0.000139201, None, 0.270364, None, 0.00575453, None, 0.270364, None, 0.00575453, None)

reports.append(Report(604017288, ("CSC", 1, 1, 4, 17), "MEp14_17"))
reports[-1].posNum = 95660
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(7.90671e-05, 0.000975532, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.25594e-05, 2.77212e-05, 0), \
                           -15928.6, 95660, 95660, -nan)
reports[-1].sigmaresid = ValErr(0.285811, 0.000653429, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000267156, None, -0.000379631, None, 0.000333457, None, -0.000372822, None, 0.000333457, None, -0.000372822, None, 0.000525519, None, -0.000346676, None, 0.000525519, None, -0.000346676, None, 0.285812, None, 0.00518085, None, 0.285812, None, 0.00518085, None)

reports.append(Report(604017304, ("CSC", 1, 1, 4, 19), "MEp14_19"))
reports[-1].posNum = 105566
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000140405, 0.000808569, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.75148e-05, 2.04823e-05, 0), \
                           -8539.23, 105566, 105566, -nan)
reports[-1].sigmaresid = ValErr(0.262357, 0.000570973, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000723842, None, -0.00363602, None, -0.000176251, None, -0.00353662, None, -0.000176251, None, -0.00353662, None, 0.00152371, None, -0.00368462, None, 0.00152371, None, -0.00368462, None, 0.262358, None, 0.00509404, None, 0.262358, None, 0.00509404, None)

reports.append(Report(604017320, ("CSC", 1, 1, 4, 21), "MEp14_21"))
reports[-1].posNum = 104056
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000587732, 0.000823303, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.1829e-06, 2.05437e-05, 0), \
                           -9687.05, 104056, 104056, -nan)
reports[-1].sigmaresid = ValErr(0.265579, 0.000582163, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00135967, None, -2.12828e-06, None, 0.000587661, None, 7.34661e-06, None, 0.000587661, None, 7.34661e-06, None, -0.000189899, None, -1.28423e-05, None, -0.000189899, None, -1.28423e-05, None, 0.265579, None, 0.00487921, None, 0.265579, None, 0.00487921, None)

reports.append(Report(604017336, ("CSC", 1, 1, 4, 23), "MEp14_23"))
reports[-1].posNum = 106304
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000111266, 0.000826002, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.12815e-05, 2.07484e-05, 0), \
                           -11359.1, 106304, 106304, -nan)
reports[-1].sigmaresid = ValErr(0.269258, 0.000583955, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000591307, None, 0.000798332, None, -0.000102167, None, 0.000744411, None, -0.000102167, None, 0.000744411, None, 0.00245335, None, 0.000793957, None, 0.00245335, None, 0.000793957, None, 0.269259, None, 0.00577202, None, 0.269259, None, 0.00577202, None)

reports.append(Report(604017352, ("CSC", 1, 1, 4, 25), "MEp14_25"))
reports[-1].posNum = 114924
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000118101, 0.000785519, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.00678e-05, 1.96356e-05, 0), \
                           -10990.8, 114924, 114924, -nan)
reports[-1].sigmaresid = ValErr(0.266254, 0.000555362, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000178625, None, 0.000782494, None, -0.000111117, None, 0.000757478, None, -0.000111117, None, 0.000757478, None, -0.00137144, None, 0.000814106, None, -0.00137144, None, 0.000814106, None, 0.266255, None, 0.00633628, None, 0.266255, None, 0.00633628, None)

reports.append(Report(604017368, ("CSC", 1, 1, 4, 27), "MEp14_27"))
reports[-1].posNum = 111376
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000301518, 0.00079745, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.79445e-05, 2.02651e-05, 0), \
                           -10542, 111376, 111376, -nan)
reports[-1].sigmaresid = ValErr(0.265993, 0.000563584, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000247892, None, 5.65167e-05, None, -0.00027858, None, 2.92475e-05, None, -0.00027858, None, 2.92475e-05, None, -0.000294614, None, 3.62202e-05, None, -0.000294614, None, 3.62202e-05, None, 0.265994, None, 0.00481644, None, 0.265994, None, 0.00481644, None)

reports.append(Report(604017384, ("CSC", 1, 1, 4, 29), "MEp14_29"))
reports[-1].posNum = 115436
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000186116, 0.000780946, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.35244e-06, 1.95629e-05, 0), \
                           -10584.6, 115436, 115436, -nan)
reports[-1].sigmaresid = ValErr(0.265207, 0.000551949, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000835928, None, 0.00323012, None, -0.000196362, None, 0.00301851, None, -0.000196362, None, 0.00301851, None, 0.00167927, None, 0.00315382, None, 0.00167927, None, 0.00315382, None, 0.265207, None, 0.00517729, None, 0.265207, None, 0.00517729, None)

reports.append(Report(604017400, ("CSC", 1, 1, 4, 31), "MEp14_31"))
reports[-1].posNum = 114550
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000575884, 0.000775832, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.82418e-05, 1.91671e-05, 0), \
                           -9124.35, 114550, 114550, -nan)
reports[-1].sigmaresid = ValErr(0.262033, 0.000547448, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000292974, None, 0.000113175, None, -0.000527994, None, 0.00012818, None, -0.000527994, None, 0.00012818, None, 0.000290189, None, 5.92359e-05, None, 0.000290189, None, 5.92359e-05, None, 0.262034, None, 0.00499195, None, 0.262034, None, 0.00499195, None)

reports.append(Report(604017416, ("CSC", 1, 1, 4, 33), "MEp14_33"))
reports[-1].posNum = 73748
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000130742, 0.0011161, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.03389e-06, 4.46559e-05, 0), \
                           -6960.6, 73748, 73748, -nan)
reports[-1].sigmaresid = ValErr(0.265922, 0.000702651, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00219542, None, -0.000785156, None, 0.000128242, None, -0.000763493, None, 0.000128242, None, -0.000763493, None, 0.00252223, None, -0.000875182, None, 0.00252223, None, -0.000875182, None, 0.265921, None, 0.00499776, None, 0.265921, None, 0.00499776, None)

reports.append(Report(604017432, ("CSC", 1, 1, 4, 35), "MEp14_35"))
reports[-1].posNum = 118600
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000475695, 0.000760766, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.60303e-05, 1.85461e-05, 0), \
                           -9010.81, 118600, 118600, -nan)
reports[-1].sigmaresid = ValErr(0.261071, 0.000536046, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00175767, None, 0.000329588, None, 0.000386104, None, 0.000371281, None, 0.000386104, None, 0.000371281, None, 0.00113058, None, 0.000312341, None, 0.00113058, None, 0.000312341, None, 0.261073, None, 0.00528575, None, 0.261073, None, 0.00528575, None)

reports.append(Report(604017168, ("CSC", 1, 1, 4, 2), "MEp14_02"))
reports[-1].posNum = 120768
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000335141, 0.000672445, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.49833e-05, 1.61505e-05, 0), \
                           4717.65, 120768, 120768, -nan)
reports[-1].sigmaresid = ValErr(0.232701, 0.000473485, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-2.88534e-05, None, -0.0028276, None, 0.000239722, None, -0.00269796, None, 0.000239722, None, -0.00269796, None, -0.000487017, None, -0.00285197, None, -0.000487017, None, -0.00285197, None, 0.232703, None, 0.00537796, None, 0.232703, None, 0.00537796, None)

reports.append(Report(604017184, ("CSC", 1, 1, 4, 4), "MEp14_04"))
reports[-1].posNum = 123430
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(9.86305e-05, 0.000673568, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.89294e-06, 1.59616e-05, 0), \
                           3748.25, 123430, 123430, -nan)
reports[-1].sigmaresid = ValErr(0.234733, 0.000472443, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000370061, None, 0.00124894, None, 0.000135502, None, 0.00118722, None, 0.000135502, None, 0.00118722, None, 0.000666055, None, 0.00113649, None, 0.000666055, None, 0.00113649, None, 0.234733, None, 0.00538725, None, 0.234733, None, 0.00538725, None)

reports.append(Report(604017200, ("CSC", 1, 1, 4, 6), "MEp14_06"))
reports[-1].posNum = 114328
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000128627, 0.000691731, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.65161e-06, 1.63881e-05, 0), \
                           4588.1, 114328, 114328, -nan)
reports[-1].sigmaresid = ValErr(0.232452, 0.000486118, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000120283, None, 0.00167559, None, 9.74322e-05, None, 0.00162512, None, 9.74322e-05, None, 0.00162512, None, 0.000399434, None, 0.00156821, None, 0.000399434, None, 0.00156821, None, 0.232453, None, 0.00549014, None, 0.232453, None, 0.00549014, None)

reports.append(Report(604017216, ("CSC", 1, 1, 4, 8), "MEp14_08"))
reports[-1].posNum = 126762
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000182005, 0.000654482, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(8.80326e-06, 1.54296e-05, 0), \
                           5794.02, 126762, 126762, -nan)
reports[-1].sigmaresid = ValErr(0.23116, 0.000459095, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-9.94809e-05, None, -9.57857e-06, None, -0.000134922, None, -7.33293e-05, None, -0.000134922, None, -7.33293e-05, None, 0.00152432, None, -0.000141974, None, 0.00152432, None, -0.000141974, None, 0.23116, None, 0.00534043, None, 0.23116, None, 0.00534043, None)

reports.append(Report(604017232, ("CSC", 1, 1, 4, 10), "MEp14_10"))
reports[-1].posNum = 125272
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000307783, 0.000674938, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.27429e-06, 1.61163e-05, 0), \
                           2158.46, 125272, 125272, -nan)
reports[-1].sigmaresid = ValErr(0.237837, 0.000475157, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000654685, None, -0.000269726, None, 0.000319949, None, -0.000275826, None, 0.000319949, None, -0.000275826, None, 0.00121291, None, -0.000292794, None, 0.00121291, None, -0.000292794, None, 0.237837, None, 0.00549149, None, 0.237837, None, 0.00549149, None)

reports.append(Report(604017248, ("CSC", 1, 1, 4, 12), "MEp14_12"))
reports[-1].posNum = 127034
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000450404, 0.00066135, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.54522e-06, 1.55719e-05, 0), \
                           4268.06, 127034, 127034, -nan)
reports[-1].sigmaresid = ValErr(0.233977, 0.000464194, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00110314, None, -0.000201972, None, -0.000483934, None, -0.000268842, None, -0.000483934, None, -0.000268842, None, -6.45895e-05, None, -0.000298397, None, -6.45895e-05, None, -0.000298397, None, 0.233976, None, 0.00556263, None, 0.233976, None, 0.00556263, None)

reports.append(Report(604017264, ("CSC", 1, 1, 4, 14), "MEp14_14"))
reports[-1].posNum = 125074
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000115282, 0.00066657, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.13489e-05, 1.59559e-05, 0), \
                           3979.41, 125074, 125074, -nan)
reports[-1].sigmaresid = ValErr(0.234393, 0.000468648, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000241692, None, 0.000174226, None, 6.47193e-05, None, 0.000209433, None, 6.47193e-05, None, 0.000209433, None, 0.000183169, None, 0.000180701, None, 0.000183169, None, 0.000180701, None, 0.234394, None, 0.00520756, None, 0.234394, None, 0.00520756, None)

reports.append(Report(604017280, ("CSC", 1, 1, 4, 16), "MEp14_16"))
reports[-1].posNum = 121232
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000179444, 0.000679012, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.30155e-05, 1.66951e-05, 0), \
                           3278.02, 121232, 121232, -nan)
reports[-1].sigmaresid = ValErr(0.235516, 0.000478295, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-1.47468e-05, None, 0.00018722, None, 0.000133162, None, 0.000173286, None, 0.000133162, None, 0.000173286, None, 0.000760051, None, 0.000164611, None, 0.000760051, None, 0.000164611, None, 0.235516, None, 0.00529772, None, 0.235516, None, 0.00529772, None)

reports.append(Report(604017296, ("CSC", 1, 1, 4, 18), "MEp14_18"))
reports[-1].posNum = 122858
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000505916, 0.000605662, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.08183e-05, 1.64078e-05, 0), \
                           2644.18, 122858, 122858, -nan)
reports[-1].sigmaresid = ValErr(0.236819, 0.000477525, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000379114, None, 0.000551301, None, 0.000481084, None, 0.000499503, None, 0.000481084, None, 0.000499503, None, 0.000375904, None, 0.000499791, None, 0.000375904, None, 0.000499791, None, 0.236819, None, 0.00520143, None, 0.236819, None, 0.00520143, None)

reports.append(Report(604017312, ("CSC", 1, 1, 4, 20), "MEp14_20"))
reports[-1].posNum = 115722
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00123445, 0.000569163, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.29077e-05, 1.52129e-05, 0), \
                           2449.27, 115722, 115722, -nan)
reports[-1].sigmaresid = ValErr(0.236903, 0.000490108, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000610412, None, 0.00209017, None, 0.00116644, None, 0.00197666, None, 0.00116644, None, 0.00197666, None, 0.00258719, None, 0.00205713, None, 0.00258719, None, 0.00205713, None, 0.236905, None, 0.00520782, None, 0.236905, None, 0.00520782, None)

reports.append(Report(604017328, ("CSC", 1, 1, 4, 22), "MEp14_22"))
reports[-1].posNum = 115732
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00070883, 0.0007045, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.20383e-05, 1.70989e-05, 0), \
                           1245.1, 115732, 115732, -nan)
reports[-1].sigmaresid = ValErr(0.239381, 0.000497564, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000835676, None, -0.00552452, None, 0.000684636, None, -0.00529686, None, 0.000684636, None, -0.00529686, None, 0.00202564, None, -0.00544302, None, 0.00202564, None, -0.00544302, None, 0.239382, None, 0.0052257, None, 0.239382, None, 0.0052257, None)

reports.append(Report(604017344, ("CSC", 1, 1, 4, 24), "MEp14_24"))
reports[-1].posNum = 119668
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000301343, 0.000691081, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.78363e-06, 1.67546e-05, 0), \
                           1697.62, 119668, 119668, -nan)
reports[-1].sigmaresid = ValErr(0.238562, 0.000487638, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000156107, None, 0.00106178, None, 0.000277839, None, 0.0010701, None, 0.000277839, None, 0.0010701, None, -0.000264797, None, 0.00112626, None, -0.000264797, None, 0.00112626, None, 0.238563, None, 0.00563339, None, 0.238563, None, 0.00563339, None)

reports.append(Report(604017360, ("CSC", 1, 1, 4, 26), "MEp14_26"))
reports[-1].posNum = 125462
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000685549, 0.000666219, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.05098e-05, 1.58195e-05, 0), \
                           4115.43, 125462, 125462, -nan)
reports[-1].sigmaresid = ValErr(0.234162, 0.000467462, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000171892, None, -0.000123949, None, -0.000578487, None, -0.000106593, None, -0.000578487, None, -0.000106593, None, -0.00069598, None, -0.000158671, None, -0.00069598, None, -0.000158671, None, 0.234164, None, 0.00579588, None, 0.234164, None, 0.00579588, None)

reports.append(Report(604017376, ("CSC", 1, 1, 4, 28), "MEp14_28"))
reports[-1].posNum = 123420
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000190165, 0.000680835, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(7.99864e-06, 1.6477e-05, 0), \
                           1916.78, 123420, 123420, -nan)
reports[-1].sigmaresid = ValErr(0.238242, 0.000479524, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000703712, None, 0.000427411, None, -0.000160827, None, 0.000445522, None, -0.000160827, None, 0.000445522, None, 0.00109023, None, 0.000442783, None, 0.00109023, None, 0.000442783, None, 0.238242, None, 0.00537563, None, 0.238242, None, 0.00537563, None)

reports.append(Report(604017392, ("CSC", 1, 1, 4, 30), "MEp14_30"))
reports[-1].posNum = 129114
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000639197, 0.000654341, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.20147e-05, 1.56284e-05, 0), \
                           4730.65, 129114, 129114, -nan)
reports[-1].sigmaresid = ValErr(0.233266, 0.000459038, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000185108, None, 0.000408331, None, -0.000576134, None, 0.000372805, None, -0.000576134, None, 0.000372805, None, 0.000956079, None, 0.000313729, None, 0.000956079, None, 0.000313729, None, 0.233266, None, 0.00517038, None, 0.233266, None, 0.00517038, None)

reports.append(Report(604017408, ("CSC", 1, 1, 4, 32), "MEp14_32"))
reports[-1].posNum = 119410
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00030191, 0.000463417, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.25272e-05, 1.63322e-05, 0), \
                           3734.55, 119410, 119410, -nan)
reports[-1].sigmaresid = ValErr(0.23452, 0.000479766, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000711507, None, 0.00115163, None, -0.000247693, None, 0.00103263, None, -0.000247693, None, 0.00103263, None, -0.000365352, None, 0.00111914, None, -0.000365352, None, 0.00111914, None, 0.234521, None, 0.00531483, None, 0.234521, None, 0.00531483, None)

reports.append(Report(604017424, ("CSC", 1, 1, 4, 34), "MEp14_34"))
reports[-1].posNum = 113646
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000438262, 0.000584224, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.37362e-06, 1.58532e-05, 0), \
                           5413.47, 113646, 113646, -nan)
reports[-1].sigmaresid = ValErr(0.230715, 0.000483907, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00199665, None, 0.000249187, None, 0.000363483, None, 0.000248441, None, 0.000363483, None, 0.000248441, None, -0.00043688, None, 0.000154998, None, -0.00043688, None, 0.000154998, None, 0.230715, None, 0.00628728, None, 0.230715, None, 0.00628728, None)

reports.append(Report(604017440, ("CSC", 1, 1, 4, 36), "MEp14_36"))
reports[-1].posNum = 125090
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000462568, 0.000663473, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.10059e-06, 1.58485e-05, 0), \
                           4628.82, 125090, 125090, -nan)
reports[-1].sigmaresid = ValErr(0.23318, 0.000466192, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00157615, None, 0.00057322, None, 0.000457679, None, 0.000564876, None, 0.000457679, None, 0.000564876, None, 0.00276466, None, 0.000561152, None, 0.00276466, None, 0.000561152, None, 0.233181, None, 0.00546178, None, 0.233181, None, 0.00546178, None)

reports.append(Report(604021256, ("CSC", 1, 2, 1, 1), "MEp21_01"))
reports[-1].posNum = 159430
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00240213, 0.00142666, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.77383e-05, 2.67994e-05, 0), \
                           -135424, 159430, 159430, -nan)
reports[-1].sigmaresid = ValErr(0.565804, 0.001002, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00439446, None, 0.00042041, None, 0.00210788, None, 0.000270817, None, 0.00210788, None, 0.000270817, None, 0.00185909, None, 0.000283501, None, 0.00185909, None, 0.000283501, None, 0.565809, None, 0.00700533, None, 0.565809, None, 0.00700533, None)

reports.append(Report(604021272, ("CSC", 1, 2, 1, 3), "MEp21_03"))
reports[-1].posNum = 169656
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000849727, 0.00139177, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.09873e-06, 2.63773e-05, 0), \
                           -144820, 169656, 169656, -nan)
reports[-1].sigmaresid = ValErr(0.568175, 0.000975401, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00476173, None, -0.000138827, None, 0.000870786, None, -0.000535543, None, 0.000870786, None, -0.000535543, None, -0.000105461, None, -0.000516868, None, -0.000105461, None, -0.000516868, None, 0.568175, None, 0.00719469, None, 0.568175, None, 0.00719469, None)

reports.append(Report(604021288, ("CSC", 1, 2, 1, 5), "MEp21_05"))
reports[-1].posNum = 215580
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000195925, 0.00124168, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.48963e-06, 2.35089e-05, 0), \
                           -184940, 215580, 215580, -nan)
reports[-1].sigmaresid = ValErr(0.5706, 0.000868986, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00281298, None, -0.000240501, None, 0.00022259, None, -0.000522113, None, 0.00022259, None, -0.000522113, None, 0.00131216, None, -0.000539987, None, 0.00131216, None, -0.000539987, None, 0.570599, None, 0.00710822, None, 0.570599, None, 0.00710822, None)

reports.append(Report(604021304, ("CSC", 1, 2, 1, 7), "MEp21_07"))
reports[-1].posNum = 207476
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00103107, 0.00125702, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.03987e-05, 2.383e-05, 0), \
                           -176299, 207476, 207476, -nan)
reports[-1].sigmaresid = ValErr(0.565975, 0.000878617, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000235883, None, -0.000728676, None, 0.000867825, None, -0.00103423, None, 0.000867825, None, -0.00103423, None, -0.000500814, None, -0.00107473, None, -0.000500814, None, -0.00107473, None, 0.565975, None, 0.00712118, None, 0.565975, None, 0.00712118, None)

reports.append(Report(604021320, ("CSC", 1, 2, 1, 9), "MEp21_09"))
reports[-1].posNum = 201314
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.001482, 0.00129166, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.66409e-05, 2.50723e-05, 0), \
                           -175111, 201314, 201314, -nan)
reports[-1].sigmaresid = ValErr(0.57747, 0.000910076, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000904771, None, -0.000132453, None, 0.00140936, None, -0.000372591, None, 0.00140936, None, -0.000372591, None, 0.00247499, None, -0.000439892, None, 0.00247499, None, -0.000439892, None, 0.577471, None, 0.00753098, None, 0.577471, None, 0.00753098, None)

reports.append(Report(604021336, ("CSC", 1, 2, 1, 11), "MEp21_11"))
reports[-1].posNum = 188862
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000551828, 0.00132663, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.82371e-06, 2.5572e-05, 0), \
                           -163264, 188862, 188862, -nan)
reports[-1].sigmaresid = ValErr(0.574375, 0.000934564, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000696993, None, -0.000359842, None, 0.000520107, None, -0.000704141, None, 0.000520107, None, -0.000704141, None, 0.000536691, None, -0.000784231, None, 0.000536691, None, -0.000784231, None, 0.574374, None, 0.00753107, None, 0.574374, None, 0.00753107, None)

reports.append(Report(604021352, ("CSC", 1, 2, 1, 13), "MEp21_13"))
reports[-1].posNum = 205832
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00106616, 0.0012667, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.99861e-05, 2.38635e-05, 0), \
                           -176071, 205832, 205832, -nan)
reports[-1].sigmaresid = ValErr(0.569197, 0.000887138, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000755403, None, -0.000223377, None, -0.000846791, None, -0.000575564, None, -0.000846791, None, -0.000575564, None, -0.000641699, None, -0.000644033, None, -0.000641699, None, -0.000644033, None, 0.5692, None, 0.00729574, None, 0.5692, None, 0.00729574, None)

reports.append(Report(604021368, ("CSC", 1, 2, 1, 15), "MEp21_15"))
reports[-1].posNum = 214212
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000645984, 0.00124411, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.23424e-05, 2.36151e-05, 0), \
                           -183734, 214212, 214212, -nan)
reports[-1].sigmaresid = ValErr(0.570516, 0.00087163, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00305179, None, -0.000240137, None, 0.000556961, None, -0.000553551, None, 0.000556961, None, -0.000553551, None, 0.0012427, None, -0.000576285, None, 0.0012427, None, -0.000576285, None, 0.570515, None, 0.00729766, None, 0.570515, None, 0.00729766, None)

reports.append(Report(604021384, ("CSC", 1, 2, 1, 17), "MEp21_17"))
reports[-1].posNum = 211028
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000431984, 0.00124189, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.29591e-05, 2.37448e-05, 0), \
                           -179318, 211028, 211028, -nan)
reports[-1].sigmaresid = ValErr(0.565976, 0.000871191, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00620967, None, 0.000458634, None, 0.000517606, None, 0.000264852, None, 0.000517606, None, 0.000264852, None, 3.66324e-05, None, 0.000257003, None, 3.66324e-05, None, 0.000257003, None, 0.565976, None, 0.00710474, None, 0.565976, None, 0.00710474, None)

reports.append(Report(604021264, ("CSC", 1, 2, 1, 2), "MEp21_02"))
reports[-1].posNum = 218246
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000420114, 0.00117357, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.46927e-06, 2.1337e-05, 0), \
                           -173302, 218246, 218246, -nan)
reports[-1].sigmaresid = ValErr(0.535331, 0.000810279, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00132254, None, 0.000857929, None, 0.00030756, None, 0.000811723, None, 0.00030756, None, 0.000811723, None, -0.000428313, None, 0.000823327, None, -0.000428313, None, 0.000823327, None, 0.535331, None, 0.00745109, None, 0.535331, None, 0.00745109, None)

reports.append(Report(604021280, ("CSC", 1, 2, 1, 4), "MEp21_04"))
reports[-1].posNum = 220788
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000355774, 0.00116392, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.01471e-06, 2.11974e-05, 0), \
                           -175208, 220788, 220788, -nan)
reports[-1].sigmaresid = ValErr(0.535059, 0.000805191, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000358167, None, 0.000461092, None, -0.000400538, None, 0.000302719, None, -0.000400538, None, 0.000302719, None, -7.34713e-05, None, 0.00029867, None, -7.34713e-05, None, 0.00029867, None, 0.535059, None, 0.00748899, None, 0.535059, None, 0.00748899, None)

reports.append(Report(604021296, ("CSC", 1, 2, 1, 6), "MEp21_06"))
reports[-1].posNum = 221506
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000171653, 0.00117142, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.41381e-05, 2.15013e-05, 0), \
                           -178164, 221506, 221506, -nan)
reports[-1].sigmaresid = ValErr(0.540854, 0.000812592, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000632103, None, -0.000679634, None, 0.000319105, None, -0.000991704, None, 0.000319105, None, -0.000991704, None, 0.00155857, None, -0.00107701, None, 0.00155857, None, -0.00107701, None, 0.540854, None, 0.00725356, None, 0.540854, None, 0.00725356, None)

reports.append(Report(604021312, ("CSC", 1, 2, 1, 8), "MEp21_08"))
reports[-1].posNum = 217822
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000724626, 0.00118646, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.31003e-05, 2.22099e-05, 0), \
                           -177473, 217822, 217822, -nan)
reports[-1].sigmaresid = ValErr(0.546524, 0.000828026, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000127328, None, 0.000154786, None, 0.000611975, None, 6.94809e-05, None, 0.000611975, None, 6.94809e-05, None, 0.000503625, None, 3.75797e-05, None, 0.000503625, None, 3.75797e-05, None, 0.546524, None, 0.00740901, None, 0.546524, None, 0.00740901, None)

reports.append(Report(604021328, ("CSC", 1, 2, 1, 10), "MEp21_10"))
reports[-1].posNum = 208256
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(9.61978e-05, 0.00120561, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.83121e-05, 2.27277e-05, 0), \
                           -168864, 208256, 208256, -nan)
reports[-1].sigmaresid = ValErr(0.54439, 0.000843522, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000559653, None, -0.00127574, None, -0.000120942, None, -0.00170528, None, -0.000120942, None, -0.00170528, None, -0.00169177, None, -0.0017691, None, -0.00169177, None, -0.0017691, None, 0.544392, None, 0.00758507, None, 0.544392, None, 0.00758507, None)

reports.append(Report(604021344, ("CSC", 1, 2, 1, 12), "MEp21_12"))
reports[-1].posNum = 205740
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000334937, 0.0012228, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.29753e-05, 2.29885e-05, 0), \
                           -168187, 205740, 205740, -nan)
reports[-1].sigmaresid = ValErr(0.548008, 0.000854304, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00282364, None, -0.000241118, None, -0.000228321, None, -0.000501258, None, -0.000228321, None, -0.000501258, None, -0.000750847, None, -0.000566102, None, -0.000750847, None, -0.000566102, None, 0.548008, None, 0.00739069, None, 0.548008, None, 0.00739069, None)

reports.append(Report(604021360, ("CSC", 1, 2, 1, 14), "MEp21_14"))
reports[-1].posNum = 217534
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00164726, 0.00119138, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.5892e-05, 2.21858e-05, 0), \
                           -176981, 217534, 217534, -nan)
reports[-1].sigmaresid = ValErr(0.545879, 0.000827595, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00103288, None, 0.000445051, None, -0.00128708, None, 0.000254886, None, -0.00128708, None, 0.000254886, None, -0.00221424, None, 0.000267134, None, -0.00221424, None, 0.000267134, None, 0.545882, None, 0.0073705, None, 0.545882, None, 0.0073705, None)

reports.append(Report(604021376, ("CSC", 1, 2, 1, 16), "MEp21_16"))
reports[-1].posNum = 214792
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000414485, 0.00118558, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.91465e-06, 2.20792e-05, 0), \
                           -172322, 214792, 214792, -nan)
reports[-1].sigmaresid = ValErr(0.539741, 0.000823497, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000787728, None, 0.000602365, None, -0.000355831, None, 0.000443352, None, -0.000355831, None, 0.000443352, None, 0.000270648, None, 0.000418081, None, 0.000270648, None, 0.000418081, None, 0.539741, None, 0.00750009, None, 0.539741, None, 0.00750009, None)

reports.append(Report(604021392, ("CSC", 1, 2, 1, 18), "MEp21_18"))
reports[-1].posNum = 224450
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000798654, 0.00115275, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.65953e-05, 2.11246e-05, 0), \
                           -177883, 224450, 224450, -nan)
reports[-1].sigmaresid = ValErr(0.534506, 0.000797771, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00258721, None, -8.88586e-05, None, 0.000500773, None, -0.000340535, None, 0.000500773, None, -0.000340535, None, 0.00123298, None, -0.000388927, None, 0.00123298, None, -0.000388927, None, 0.534508, None, 0.00726356, None, 0.534508, None, 0.00726356, None)

reports.append(Report(604021768, ("CSC", 1, 2, 2, 1), "MEp22_01"))
reports[-1].posNum = 53220
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0129578, 0.00724009, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000150542, 6.93737e-05, 0), \
                           -86884.7, 53220, 53220, -nan)
reports[-1].sigmaresid = ValErr(1.23815, 0.00379508, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00154937, None, 0.000158698, None, -0.00241264, None, 0.000156239, None, -0.00241264, None, 0.000156239, None, -0.000495914, None, 0.00028188, None, -0.000495914, None, 0.00028188, None, 1.23821, None, 0.00831694, None, 1.23821, None, 0.00831694, None)

reports.append(Report(604021784, ("CSC", 1, 2, 2, 3), "MEp22_03"))
reports[-1].posNum = 45752
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0150326, 0.00848412, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000141644, 7.58784e-05, 0), \
                           -70283.9, 45752, 45752, -nan)
reports[-1].sigmaresid = ValErr(1.12441, 0.00371709, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00159162, None, -1.45357e-06, None, -0.00260147, None, -9.12505e-05, None, -0.00260147, None, -9.12505e-05, None, -0.00717324, None, -6.65686e-05, None, -0.00717324, None, -6.65686e-05, None, 1.12445, None, 0.00718069, None, 1.12445, None, 0.00718069, None)

reports.append(Report(604021800, ("CSC", 1, 2, 2, 5), "MEp22_05"))
reports[-1].posNum = 39676
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00680378, 0.00885831, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.77722e-05, 8.21555e-05, 0), \
                           -62502.8, 39676, 39676, -nan)
reports[-1].sigmaresid = ValErr(1.16928, 0.00415089, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00774472, None, 0.000524258, None, -0.00294648, None, 0.000360414, None, -0.00294648, None, 0.000360414, None, -0.00759642, None, 0.000414704, None, -0.00759642, None, 0.000414704, None, 1.16929, None, 0.00707217, None, 1.16929, None, 0.00707217, None)

reports.append(Report(604021816, ("CSC", 1, 2, 2, 7), "MEp22_07"))
reports[-1].posNum = 55502
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000602946, 0.00712411, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.22452e-06, 6.76709e-05, 0), \
                           -90693.1, 55502, 55502, -nan)
reports[-1].sigmaresid = ValErr(1.24, 0.00372181, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00633466, None, -8.10955e-05, None, 0.000220475, None, -0.000285453, None, 0.000220475, None, -0.000285453, None, 0.000526647, None, -0.00029567, None, 0.000526647, None, -0.00029567, None, 1.24, None, 0.00757887, None, 1.24, None, 0.00757887, None)

reports.append(Report(604021832, ("CSC", 1, 2, 2, 9), "MEp22_09"))
reports[-1].posNum = 55376
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00658346, 0.00675862, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.77732e-05, 6.45205e-05, 0), \
                           -91953, 55376, 55376, -nan)
reports[-1].sigmaresid = ValErr(1.27326, 0.00382596, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00576728, None, 0.000133617, None, -0.00358619, None, -0.000237268, None, -0.00358619, None, -0.000237268, None, -0.00800657, None, -0.000217397, None, -0.00800657, None, -0.000217397, None, 1.27327, None, 0.00783141, None, 1.27327, None, 0.00783141, None)

reports.append(Report(604021848, ("CSC", 1, 2, 2, 11), "MEp22_11"))
reports[-1].posNum = 57862
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0127255, 0.00659684, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000121263, 6.22326e-05, 0), \
                           -96098.8, 57862, 57862, -nan)
reports[-1].sigmaresid = ValErr(1.27365, 0.00374402, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0103607, None, 0.000128696, None, 0.00505826, None, -7.04027e-05, None, 0.00505826, None, -7.04027e-05, None, 0.0118705, None, -0.000220848, None, 0.0118705, None, -0.000220848, None, 1.27369, None, 0.00750002, None, 1.27369, None, 0.00750002, None)

reports.append(Report(604021864, ("CSC", 1, 2, 2, 13), "MEp22_13"))
reports[-1].posNum = 55142
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00583638, 0.00667062, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.42387e-05, 6.29168e-05, 0), \
                           -91495.1, 55142, 55142, -nan)
reports[-1].sigmaresid = ValErr(1.27166, 0.00382924, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-6.83273e-05, None, 9.36097e-07, None, 0.000615782, None, -0.000337419, None, 0.000615782, None, -0.000337419, None, -0.00378478, None, -0.000294279, None, -0.00378478, None, -0.000294279, None, 1.27168, None, 0.00797603, None, 1.27168, None, 0.00797603, None)

reports.append(Report(604021880, ("CSC", 1, 2, 2, 15), "MEp22_15"))
reports[-1].posNum = 53852
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00633495, 0.0067177, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000101103, 6.50646e-05, 0), \
                           -90561.7, 53852, 53852, -nan)
reports[-1].sigmaresid = ValErr(1.30049, 0.00396269, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00322895, None, -0.000429185, None, 0.00057891, None, -0.000600674, None, 0.00057891, None, -0.000600674, None, 0.0132483, None, -0.000673784, None, 0.0132483, None, -0.000673784, None, 1.30052, None, 0.00757098, None, 1.30052, None, 0.00757098, None)

reports.append(Report(604021896, ("CSC", 1, 2, 2, 17), "MEp22_17"))
reports[-1].posNum = 57846
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00301845, 0.00637318, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.07053e-05, 5.95076e-05, 0), \
                           -94108.5, 57846, 57846, -nan)
reports[-1].sigmaresid = ValErr(1.23114, 0.00361956, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00395802, None, -0.000931156, None, 0.00105921, None, -0.00116174, None, 0.00105921, None, -0.00116174, None, 0.00958896, None, -0.00122432, None, 0.00958896, None, -0.00122432, None, 1.23114, None, 0.00822163, None, 1.23114, None, 0.00822163, None)

reports.append(Report(604021912, ("CSC", 1, 2, 2, 19), "MEp22_19"))
reports[-1].posNum = 56074
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0047623, 0.00649431, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.09529e-05, 6.41685e-05, 0), \
                           -94954.1, 56074, 56074, -nan)
reports[-1].sigmaresid = ValErr(1.31578, 0.00392905, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00348181, None, 0.000359366, None, 0.00156757, None, 9.59911e-05, None, 0.00156757, None, 9.59911e-05, None, -0.000365717, None, 8.76281e-05, None, -0.000365717, None, 8.76281e-05, None, 1.3158, None, 0.00781639, None, 1.3158, None, 0.00781639, None)

reports.append(Report(604021928, ("CSC", 1, 2, 2, 21), "MEp22_21"))
reports[-1].posNum = 58016
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0108468, 0.00641311, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000110978, 6.06544e-05, 0), \
                           -95801.8, 58016, 58016, -nan)
reports[-1].sigmaresid = ValErr(1.26158, 0.0037036, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00712299, None, -0.000263771, None, 0.0040756, None, -0.000319195, None, 0.0040756, None, -0.000319195, None, -5.02836e-05, None, -0.000294681, None, -5.02836e-05, None, -0.000294681, None, 1.26161, None, 0.00838815, None, 1.26161, None, 0.00838815, None)

reports.append(Report(604021944, ("CSC", 1, 2, 2, 23), "MEp22_23"))
reports[-1].posNum = 63324
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000778749, 0.0061805, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.12705e-06, 6.04183e-05, 0), \
                           -105719, 63324, 63324, -nan)
reports[-1].sigmaresid = ValErr(1.28474, 0.00361006, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000277025, None, -0.000274544, None, 0.000366874, None, -0.000382702, None, 0.000366874, None, -0.000382702, None, 0.00518282, None, -0.000428844, None, 0.00518282, None, -0.000428844, None, 1.28474, None, 0.00759857, None, 1.28474, None, 0.00759857, None)

reports.append(Report(604021960, ("CSC", 1, 2, 2, 25), "MEp22_25"))
reports[-1].posNum = 51832
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0191455, 0.00762397, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000197638, 7.0552e-05, 0), \
                           -82814.6, 51832, 51832, -nan)
reports[-1].sigmaresid = ValErr(1.1958, 0.00371401, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00475802, None, 0.000214407, None, 0.00366528, None, 6.66198e-06, None, 0.00366528, None, 6.66198e-06, None, -0.00217066, None, 2.01707e-05, None, -0.00217066, None, 2.01707e-05, None, 1.19589, None, 0.00765847, None, 1.19589, None, 0.00765847, None)

reports.append(Report(604021976, ("CSC", 1, 2, 2, 27), "MEp22_27"))
reports[-1].posNum = 44192
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00759377, 0.00778661, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.46479e-05, 7.33435e-05, 0), \
                           -73073.9, 44192, 44192, -nan)
reports[-1].sigmaresid = ValErr(1.26442, 0.00425309, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00387856, None, 0.000838113, None, -0.00525757, None, 0.000464769, None, -0.00525757, None, 0.000464769, None, -0.00751682, None, 0.000520488, None, -0.00751682, None, 0.000520488, None, 1.26443, None, 0.00829719, None, 1.26443, None, 0.00829719, None)

reports.append(Report(604021992, ("CSC", 1, 2, 2, 29), "MEp22_29"))
reports[-1].posNum = 59652
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00836657, 0.00634723, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.00011379, 5.99234e-05, 0), \
                           -98918.2, 59652, 59652, -nan)
reports[-1].sigmaresid = ValErr(1.27038, 0.00367794, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00271985, None, -0.000565263, None, -0.00145482, None, -0.000772737, None, -0.00145482, None, -0.000772737, None, 0.00125129, None, -0.000774322, None, 0.00125129, None, -0.000774322, None, 1.27042, None, 0.00784554, None, 1.27042, None, 0.00784554, None)

reports.append(Report(604022008, ("CSC", 1, 2, 2, 31), "MEp22_31"))
reports[-1].posNum = 51130
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0157665, 0.0068763, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000155802, 6.43498e-05, 0), \
                           -84443.1, 51130, 51130, -nan)
reports[-1].sigmaresid = ValErr(1.26188, 0.00394606, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00852654, None, 0.000231531, None, -0.006039, None, -4.02906e-05, None, -0.006039, None, -4.02906e-05, None, -0.00494897, None, -6.48945e-05, None, -0.00494897, None, -6.48945e-05, None, 1.26195, None, 0.00773067, None, 1.26195, None, 0.00773067, None)

reports.append(Report(604022024, ("CSC", 1, 2, 2, 33), "MEp22_33"))
reports[-1].posNum = 63622
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00969621, 0.00605304, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000111539, 5.85164e-05, 0), \
                           -105996, 63622, 63622, -nan)
reports[-1].sigmaresid = ValErr(1.2803, 0.00358915, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00104951, None, -0.000856807, None, -0.00340941, None, -0.000947802, None, -0.00340941, None, -0.000947802, None, 0.00969007, None, -0.000951, None, 0.00969007, None, -0.000951, None, 1.28033, None, 0.00796819, None, 1.28033, None, 0.00796819, None)

reports.append(Report(604022040, ("CSC", 1, 2, 2, 35), "MEp22_35"))
reports[-1].posNum = 47122
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00682499, 0.00724729, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.93079e-05, 6.57054e-05, 0), \
                           -77523.3, 47122, 47122, -nan)
reports[-1].sigmaresid = ValErr(1.25385, 0.00408431, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00433212, None, 0.00037567, None, 0.000871691, None, 0.000114715, None, 0.000871691, None, 0.000114715, None, -0.00192673, None, 0.000125867, None, -0.00192673, None, 0.000125867, None, 1.25388, None, 0.00742203, None, 1.25388, None, 0.00742203, None)

reports.append(Report(604021776, ("CSC", 1, 2, 2, 2), "MEp22_02"))
reports[-1].posNum = 22876
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00804427, 0.0107387, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000106194, 0.000117496, 0), \
                           -39239.8, 22876, 22876, -nan)
reports[-1].sigmaresid = ValErr(1.34498, 0.00628794, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00161634, None, 0.00158235, None, -0.00259882, None, 0.00122725, None, -0.00259882, None, 0.00122725, None, 0.000376909, None, 0.00138673, None, 0.000376909, None, 0.00138673, None, 1.34502, None, 0.00840966, None, 1.34502, None, 0.00840966, None)

reports.append(Report(604021792, ("CSC", 1, 2, 2, 4), "MEp22_04"))
reports[-1].posNum = 38028
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0332078, 0.00886413, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000272893, 7.56374e-05, 0), \
                           -58155.6, 38028, 38028, -nan)
reports[-1].sigmaresid = ValErr(1.11666, 0.00404904, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00615825, None, 0.00122997, None, -0.00879795, None, 0.00102342, None, -0.00879795, None, 0.00102342, None, -0.00970242, None, 0.00102541, None, -0.00970242, None, 0.00102541, None, 1.11685, None, 0.00835664, None, 1.11685, None, 0.00835664, None)

reports.append(Report(604021808, ("CSC", 1, 2, 2, 6), "MEp22_06"))
reports[-1].posNum = 48324
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0174305, 0.00781656, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000194402, 7.33659e-05, 0), \
                           -76519.8, 48324, 48324, -nan)
reports[-1].sigmaresid = ValErr(1.17884, 0.0037919, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00674728, None, 0.000543492, None, 0.00235746, None, 0.000285185, None, 0.00235746, None, 0.000285185, None, -0.00251522, None, 0.000303365, None, -0.00251522, None, 0.000303365, None, 1.17893, None, 0.0083256, None, 1.17893, None, 0.0083256, None)

reports.append(Report(604021824, ("CSC", 1, 2, 2, 8), "MEp22_08"))
reports[-1].posNum = 49152
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0108541, 0.00690347, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000107685, 6.39924e-05, 0), \
                           -80053.6, 49152, 49152, -nan)
reports[-1].sigmaresid = ValErr(1.23338, 0.00393378, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00594619, None, 0.000207494, None, 0.0039754, None, -0.000309687, None, 0.0039754, None, -0.000309687, None, 0.0121233, None, -0.000436144, None, 0.0121233, None, -0.000436144, None, 1.23341, None, 0.00885843, None, 1.23341, None, 0.00885843, None)

reports.append(Report(604021840, ("CSC", 1, 2, 2, 10), "MEp22_10"))
reports[-1].posNum = 57900
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00684264, 0.00642925, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.34102e-05, 6.14749e-05, 0), \
                           -95734, 57900, 57900, -nan)
reports[-1].sigmaresid = ValErr(1.26427, 0.00371524, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00225499, None, 4.44104e-05, None, -0.00302059, None, 0.000113904, None, -0.00302059, None, 0.000113904, None, 0.00187626, None, 0.00016788, None, 0.00187626, None, 0.00016788, None, 1.26429, None, 0.00869816, None, 1.26429, None, 0.00869816, None)

reports.append(Report(604021856, ("CSC", 1, 2, 2, 12), "MEp22_12"))
reports[-1].posNum = 51498
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0180899, 0.00682548, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000180859, 6.38119e-05, 0), \
                           -84346.3, 51498, 51498, -nan)
reports[-1].sigmaresid = ValErr(1.24473, 0.0038785, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0046478, None, -2.0803e-05, None, 0.0065763, None, -2.05526e-05, None, 0.0065763, None, -2.05526e-05, None, 0.00167826, None, -5.24113e-06, None, 0.00167826, None, -5.24113e-06, None, 1.24483, None, 0.00844769, None, 1.24483, None, 0.00844769, None)

reports.append(Report(604021872, ("CSC", 1, 2, 2, 14), "MEp22_14"))
reports[-1].posNum = 61616
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0169514, 0.0061252, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000180441, 6.01871e-05, 0), \
                           -103163, 61616, 61616, -nan)
reports[-1].sigmaresid = ValErr(1.29091, 0.00367735, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00732708, None, -0.0015193, None, 0.00724871, None, -0.00155087, None, 0.00724871, None, -0.00155087, None, 0.000735444, None, -0.00163494, None, 0.000735444, None, -0.00163494, None, 1.29101, None, 0.00832053, None, 1.29101, None, 0.00832053, None)

reports.append(Report(604021888, ("CSC", 1, 2, 2, 16), "MEp22_16"))
reports[-1].posNum = 59022
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0200962, 0.00614254, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000199179, 5.76262e-05, 0), \
                           -99084.1, 59022, 59022, -nan)
reports[-1].sigmaresid = ValErr(1.2967, 0.00377414, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00743646, None, -0.000759276, None, 0.00958579, None, -0.000832931, None, 0.00958579, None, -0.000832931, None, 0.00879265, None, -0.000918448, None, 0.00879265, None, -0.000918448, None, 1.29684, None, 0.0086191, None, 1.29684, None, 0.0086191, None)

reports.append(Report(604021904, ("CSC", 1, 2, 2, 18), "MEp22_18"))
reports[-1].posNum = 56674
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0146714, 0.00638172, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000156032, 6.12753e-05, 0), \
                           -93348.3, 56674, 56674, -nan)
reports[-1].sigmaresid = ValErr(1.2563, 0.00373153, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00388678, None, 0.000388217, None, 0.00553303, None, 0.000191407, None, 0.00553303, None, 0.000191407, None, 0.010833, None, 0.000236216, None, 0.010833, None, 0.000236216, None, 1.25637, None, 0.00874446, None, 1.25637, None, 0.00874446, None)

reports.append(Report(604021920, ("CSC", 1, 2, 2, 20), "MEp22_20"))
reports[-1].posNum = 55538
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00588869, 0.00642643, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.61977e-05, 6.36446e-05, 0), \
                           -97209.3, 55538, 55538, -nan)
reports[-1].sigmaresid = ValErr(1.39289, 0.00417933, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00852878, None, 0.000666573, None, 0.00286695, None, 0.00041577, None, 0.00286695, None, 0.00041577, None, 0.00385277, None, 0.000416958, None, 0.00385277, None, 0.000416958, None, 1.39291, None, 0.00914857, None, 1.39291, None, 0.00914857, None)

reports.append(Report(604021936, ("CSC", 1, 2, 2, 22), "MEp22_22"))
reports[-1].posNum = 49934
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00359803, 0.0068814, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.65074e-05, 6.50474e-05, 0), \
                           -82753.1, 49934, 49934, -nan)
reports[-1].sigmaresid = ValErr(1.2691, 0.00401591, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00261124, None, 0.00046553, None, 0.000818787, None, 0.000210902, None, 0.000818787, None, 0.000210902, None, 0.00482522, None, 0.000183334, None, 0.00482522, None, 0.000183334, None, 1.26911, None, 0.00800591, None, 1.26911, None, 0.00800591, None)

reports.append(Report(604021952, ("CSC", 1, 2, 2, 24), "MEp22_24"))
reports[-1].posNum = 56456
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0036541, 0.00668496, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.47273e-05, 6.49006e-05, 0), \
                           -92269, 56456, 56456, -nan)
reports[-1].sigmaresid = ValErr(1.24038, 0.00369133, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00106213, None, 0.000215977, None, -0.000510682, None, -1.72898e-05, None, -0.000510682, None, -1.72898e-05, None, 0.00169899, None, 1.50432e-07, None, 0.00169899, None, 1.50432e-07, None, 1.24039, None, 0.0098702, None, 1.24039, None, 0.0098702, None)

reports.append(Report(604021968, ("CSC", 1, 2, 2, 26), "MEp22_26"))
reports[-1].posNum = 41744
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0161592, 0.00785975, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000154275, 6.96564e-05, 0), \
                           -65256.1, 41744, 41744, -nan)
reports[-1].sigmaresid = ValErr(1.15525, 0.00399821, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00112856, None, -0.000124914, None, -0.00406937, None, -0.000313762, None, -0.00406937, None, -0.000313762, None, -0.00228618, None, -0.000275319, None, -0.00228618, None, -0.000275319, None, 1.15531, None, 0.00841606, None, 1.15531, None, 0.00841606, None)

reports.append(Report(604021984, ("CSC", 1, 2, 2, 28), "MEp22_28"))
reports[-1].posNum = 64126
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0046253, 0.00599815, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.00724e-05, 5.87336e-05, 0), \
                           -108211, 64126, 64126, -nan)
reports[-1].sigmaresid = ValErr(1.30805, 0.00365251, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00303008, None, 2.91589e-05, None, 0.00150562, None, -0.000219569, None, 0.00150562, None, -0.000219569, None, -0.00034541, None, -0.000249089, None, -0.00034541, None, -0.000249089, None, 1.30806, None, 0.00849551, None, 1.30806, None, 0.00849551, None)

reports.append(Report(604022000, ("CSC", 1, 2, 2, 30), "MEp22_30"))
reports[-1].posNum = 40586
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.029001, 0.00760861, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000245272, 6.76463e-05, 0), \
                           -66483.5, 40586, 40586, -nan)
reports[-1].sigmaresid = ValErr(1.24502, 0.00436992, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0119581, None, 2.09288e-05, None, -0.0129086, None, -4.40657e-05, None, -0.0129086, None, -4.40657e-05, None, -0.0168831, None, -2.32838e-05, None, -0.0168831, None, -2.32838e-05, None, 1.24522, None, 0.00818549, None, 1.24522, None, 0.00818549, None)

reports.append(Report(604022016, ("CSC", 1, 2, 2, 32), "MEp22_32"))
reports[-1].posNum = 59646
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00407769, 0.00623162, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(7.41472e-05, 5.96206e-05, 0), \
                           -100089, 59646, 59646, -nan)
reports[-1].sigmaresid = ValErr(1.29576, 0.00375161, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0011761, None, -0.000225988, None, -4.79824e-06, None, -0.000333451, None, -4.79824e-06, None, -0.000333451, None, -0.00479542, None, -0.000338341, None, -0.00479542, None, -0.000338341, None, 1.29579, None, 0.00850279, None, 1.29579, None, 0.00850279, None)

reports.append(Report(604022032, ("CSC", 1, 2, 2, 34), "MEp22_34"))
reports[-1].posNum = 50206
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00791356, 0.00670338, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000101898, 6.21864e-05, 0), \
                           -85054.7, 50206, 50206, -nan)
reports[-1].sigmaresid = ValErr(1.31676, 0.00415539, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0072179, None, 0.000396747, None, -0.00262616, None, 0.00018291, None, -0.00262616, None, 0.00018291, None, -0.00839701, None, 0.00028177, None, -0.00839701, None, 0.00028177, None, 1.3168, None, 0.00835976, None, 1.3168, None, 0.00835976, None)

reports.append(Report(604022048, ("CSC", 1, 2, 2, 36), "MEp22_36"))
reports[-1].posNum = 40844
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000818656, 0.00772048, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.94999e-06, 7.4173e-05, 0), \
                           -67326.9, 40844, 40844, -nan)
reports[-1].sigmaresid = ValErr(1.25792, 0.00440123, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0016111, None, 0.000609865, None, 0.00104592, None, 0.000479423, None, 0.00104592, None, 0.000479423, None, -0.000148668, None, 0.000484589, None, -0.000148668, None, 0.000484589, None, 1.25791, None, 0.00893698, None, 1.25791, None, 0.00893698, None)

reports.append(Report(604025352, ("CSC", 1, 3, 1, 1), "MEp31_01"))
reports[-1].posNum = 154616
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000990291, 0.00170396, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.7329e-05, 3.54265e-05, 0), \
                           -156244, 154616, 154616, -nan)
reports[-1].sigmaresid = ValErr(0.664706, 0.00119533, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00367911, None, -0.000510027, None, -0.000766587, None, -0.00084441, None, -0.000766587, None, -0.00084441, None, -0.000959749, None, -0.000910158, None, -0.000959749, None, -0.000910158, None, 0.664709, None, 0.00815772, None, 0.664709, None, 0.00815772, None)

reports.append(Report(604025368, ("CSC", 1, 3, 1, 3), "MEp31_03"))
reports[-1].posNum = 164554
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000764548, 0.00166091, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.35528e-05, 3.44745e-05, 0), \
                           -166814, 164554, 164554, -nan)
reports[-1].sigmaresid = ValErr(0.66684, 0.00116239, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00408274, None, -0.000533191, None, -0.00067081, None, -0.00100808, None, -0.00067081, None, -0.00100808, None, -0.000188968, None, -0.00112307, None, -0.000188968, None, -0.00112307, None, 0.66684, None, 0.00810661, None, 0.66684, None, 0.00810661, None)

reports.append(Report(604025384, ("CSC", 1, 3, 1, 5), "MEp31_05"))
reports[-1].posNum = 174792
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00197609, 0.00161773, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.72729e-05, 3.34022e-05, 0), \
                           -177969, 174792, 174792, -nan)
reports[-1].sigmaresid = ValErr(0.669808, 0.00113286, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00417437, None, 0.000115872, None, -0.00178951, None, -0.000252885, None, -0.00178951, None, -0.000252885, None, -0.00188698, None, -0.000311058, None, -0.00188698, None, -0.000311058, None, 0.66981, None, 0.008004, None, 0.66981, None, 0.008004, None)

reports.append(Report(604025400, ("CSC", 1, 3, 1, 7), "MEp31_07"))
reports[-1].posNum = 135328
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00136495, 0.0018259, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.13409e-06, 3.76166e-05, 0), \
                           -137015, 135328, 135328, -nan)
reports[-1].sigmaresid = ValErr(0.665997, 0.00128016, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00158573, None, -0.000487893, None, -0.00132822, None, -0.000927256, None, -0.00132822, None, -0.000927256, None, -0.00435354, None, -0.00104048, None, -0.00435354, None, -0.00104048, None, 0.665997, None, 0.00825784, None, 0.665997, None, 0.00825784, None)

reports.append(Report(604025416, ("CSC", 1, 3, 1, 9), "MEp31_09"))
reports[-1].posNum = 162378
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00115553, 0.00169743, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.67e-05, 3.59678e-05, 0), \
                           -168255, 162378, 162378, -nan)
reports[-1].sigmaresid = ValErr(0.681986, 0.00119673, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00117106, None, -0.000338402, None, -0.00102341, None, -0.000660757, None, -0.00102341, None, -0.000660757, None, -0.00208217, None, -0.000747379, None, -0.00208217, None, -0.000747379, None, 0.681988, None, 0.00800272, None, 0.681988, None, 0.00800272, None)

reports.append(Report(604025432, ("CSC", 1, 3, 1, 11), "MEp31_11"))
reports[-1].posNum = 126778
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00041179, 0.00190608, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.62946e-05, 4.02812e-05, 0), \
                           -130313, 126778, 126778, -nan)
reports[-1].sigmaresid = ValErr(0.676345, 0.00134317, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00166635, None, -0.000339434, None, -0.000231723, None, -0.000704478, None, -0.000231723, None, -0.000704478, None, -0.00212652, None, -0.000768224, None, -0.00212652, None, -0.000768224, None, 0.676349, None, 0.00812605, None, 0.676349, None, 0.00812605, None)

reports.append(Report(604025448, ("CSC", 1, 3, 1, 13), "MEp31_13"))
reports[-1].posNum = 169308
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00124793, 0.00164577, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.73508e-05, 3.41295e-05, 0), \
                           -172645, 169308, 169308, -nan)
reports[-1].sigmaresid = ValErr(0.670837, 0.00115283, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000250363, None, 0.000301176, None, 0.000935948, None, -5.87765e-05, None, 0.000935948, None, -5.87765e-05, None, 0.00251479, None, -8.15567e-05, None, 0.00251479, None, -8.15567e-05, None, 0.670841, None, 0.00835647, None, 0.670841, None, 0.00835647, None)

reports.append(Report(604025464, ("CSC", 1, 3, 1, 15), "MEp31_15"))
reports[-1].posNum = 173488
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000382059, 0.00162844, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.22093e-06, 3.37016e-05, 0), \
                           -177016, 173488, 173488, -nan)
reports[-1].sigmaresid = ValErr(0.671256, 0.00113956, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00245324, None, 0.000374778, None, -0.000396102, None, 0.00017002, None, -0.000396102, None, 0.00017002, None, 0.00120757, None, 0.000186504, None, 0.00120757, None, 0.000186504, None, 0.671256, None, 0.0081111, None, 0.671256, None, 0.0081111, None)

reports.append(Report(604025480, ("CSC", 1, 3, 1, 17), "MEp31_17"))
reports[-1].posNum = 171576
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000602316, 0.00161583, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.5445e-05, 3.36685e-05, 0), \
                           -173306, 171576, 171576, -nan)
reports[-1].sigmaresid = ValErr(0.664411, 0.00113421, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00645272, None, -8.15644e-05, None, -0.000513437, None, -0.000416313, None, -0.000513437, None, -0.000416313, None, 0.00018708, None, -0.00045825, None, 0.00018708, None, -0.00045825, None, 0.664412, None, 0.00812414, None, 0.664412, None, 0.00812414, None)

reports.append(Report(604025360, ("CSC", 1, 3, 1, 2), "MEp31_02"))
reports[-1].posNum = 168364
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000682165, 0.0016979, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.48004e-05, 3.59375e-05, 0), \
                           -176457, 168364, 168364, -nan)
reports[-1].sigmaresid = ValErr(0.690135, 0.00118931, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00258069, None, -3.60832e-06, None, -0.000843674, None, -0.000398994, None, -0.000843674, None, -0.000398994, None, -0.00168071, None, -0.000441146, None, -0.00168071, None, -0.000441146, None, 0.690136, None, 0.00751096, None, 0.690136, None, 0.00751096, None)

reports.append(Report(604025376, ("CSC", 1, 3, 1, 4), "MEp31_04"))
reports[-1].posNum = 170240
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00131407, 0.00168179, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.2593e-05, 3.56381e-05, 0), \
                           -177958, 170240, 170240, -nan)
reports[-1].sigmaresid = ValErr(0.688251, 0.00117951, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00531406, None, -0.000139453, None, -0.00123482, None, -0.000512784, None, -0.00123482, None, -0.000512784, None, 9.70228e-05, None, -0.000597961, None, 9.70228e-05, None, -0.000597961, None, 0.688251, None, 0.00736935, None, 0.688251, None, 0.00736935, None)

reports.append(Report(604025392, ("CSC", 1, 3, 1, 6), "MEp31_06"))
reports[-1].posNum = 166156
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000491841, 0.00171636, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(8.18157e-06, 3.66034e-05, 0), \
                           -175380, 166156, 166156, -nan)
reports[-1].sigmaresid = ValErr(0.695292, 0.00120613, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00132882, None, -5.70544e-05, None, -0.000448962, None, -0.000428357, None, -0.000448962, None, -0.000428357, None, -0.00448727, None, -0.000464602, None, -0.00448727, None, -0.000464602, None, 0.695292, None, 0.0076014, None, 0.695292, None, 0.0076014, None)

reports.append(Report(604025408, ("CSC", 1, 3, 1, 8), "MEp31_08"))
reports[-1].posNum = 164320
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000194965, 0.00173798, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.17296e-05, 3.81448e-05, 0), \
                           -175277, 164320, 164320, -nan)
reports[-1].sigmaresid = ValErr(0.7031, 0.00122648, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00082604, None, -0.000372155, None, -0.000159907, None, -0.000692037, None, -0.000159907, None, -0.000692037, None, -0.00159438, None, -0.000740161, None, -0.00159438, None, -0.000740161, None, 0.703097, None, 0.00732736, None, 0.703097, None, 0.00732736, None)

reports.append(Report(604025424, ("CSC", 1, 3, 1, 10), "MEp31_10"))
reports[-1].posNum = 157094
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000233219, 0.00178131, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.40299e-05, 3.93851e-05, 0), \
                           -168091, 157094, 157094, -nan)
reports[-1].sigmaresid = ValErr(0.705441, 0.00125854, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000592416, None, -0.000547962, None, 0.000260062, None, -0.00089793, None, 0.000260062, None, -0.00089793, None, -0.0025813, None, -0.000982201, None, -0.0025813, None, -0.000982201, None, 0.70544, None, 0.00771956, None, 0.70544, None, 0.00771956, None)

reports.append(Report(604025440, ("CSC", 1, 3, 1, 12), "MEp31_12"))
reports[-1].posNum = 149718
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000841453, 0.00182827, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.16863e-06, 4.04265e-05, 0), \
                           -160456, 149718, 149718, -nan)
reports[-1].sigmaresid = ValErr(0.706651, 0.00129138, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00363513, None, 0.000276702, None, 0.000826456, None, -0.000141207, None, 0.000826456, None, -0.000141207, None, 0.00521221, None, -0.000190196, None, 0.00521221, None, -0.000190196, None, 0.706651, None, 0.00773062, None, 0.706651, None, 0.00773062, None)

reports.append(Report(604025456, ("CSC", 1, 3, 1, 14), "MEp31_14"))
reports[-1].posNum = 163426
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00140587, 0.00174847, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.3145e-05, 3.83188e-05, 0), \
                           -174285, 163426, 163426, -nan)
reports[-1].sigmaresid = ValErr(0.702934, 0.00122953, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-9.64059e-05, None, 6.05498e-05, None, 0.00120089, None, -0.000352987, None, 0.00120089, None, -0.000352987, None, 0.000878964, None, -0.000421648, None, 0.000878964, None, -0.000421648, None, 0.702937, None, 0.00759945, None, 0.702937, None, 0.00759945, None)

reports.append(Report(604025472, ("CSC", 1, 3, 1, 16), "MEp31_16"))
reports[-1].posNum = 166308
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000280765, 0.00172009, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.46926e-05, 3.73395e-05, 0), \
                           -176450, 166308, 166308, -nan)
reports[-1].sigmaresid = ValErr(0.699105, 0.00121219, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00214409, None, 0.000294336, None, 0.000337635, None, 6.41787e-05, None, 0.000337635, None, 6.41787e-05, None, 0.000562265, None, 8.47195e-05, None, 0.000562265, None, 8.47195e-05, None, 0.699103, None, 0.00811778, None, 0.699103, None, 0.00811778, None)

reports.append(Report(604025488, ("CSC", 1, 3, 1, 18), "MEp31_18"))
reports[-1].posNum = 171472
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(8.19053e-05, 0.00166702, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.18269e-05, 3.53786e-05, 0), \
                           -178570, 171472, 171472, -nan)
reports[-1].sigmaresid = ValErr(0.685543, 0.00117064, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00519365, None, 0.000113452, None, 0.000147087, None, -0.000188645, None, 0.000147087, None, -0.000188645, None, -0.00229886, None, -0.000228359, None, -0.00229886, None, -0.000228359, None, 0.685543, None, 0.00748927, None, 0.685543, None, 0.00748927, None)

reports.append(Report(604025864, ("CSC", 1, 3, 2, 1), "MEp32_01"))
reports[-1].posNum = 62604
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00702504, 0.00668837, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000118396, 6.59846e-05, 0), \
                           -105755, 62604, 62604, -nan)
reports[-1].sigmaresid = ValErr(1.3104, 0.0037033, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00324684, None, 0.000285117, None, -0.000438734, None, -7.31685e-05, None, -0.000438734, None, -7.31685e-05, None, 0.00202843, None, -1.1859e-05, None, 0.00202843, None, -1.1859e-05, None, 1.31044, None, 0.0105293, None, 1.31044, None, 0.0105293, None)

reports.append(Report(604025880, ("CSC", 1, 3, 2, 3), "MEp32_03"))
reports[-1].posNum = 54994
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0130602, 0.00832083, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000126691, 8.03315e-05, 0), \
                           -88893.2, 54994, 54994, -nan)
reports[-1].sigmaresid = ValErr(1.21833, 0.00367359, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00524602, None, -9.70629e-05, None, 0.0028099, None, -0.000248247, None, 0.0028099, None, -0.000248247, None, 0.00793882, None, -0.00019218, None, 0.00793882, None, -0.00019218, None, 1.21835, None, 0.00955927, None, 1.21835, None, 0.00955927, None)

reports.append(Report(604025896, ("CSC", 1, 3, 2, 5), "MEp32_05"))
reports[-1].posNum = 55982
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00500689, 0.00768832, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.38234e-05, 7.59731e-05, 0), \
                           -92483.6, 55982, 55982, -nan)
reports[-1].sigmaresid = ValErr(1.26249, 0.00377259, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0047894, None, 0.000568075, None, 0.00181433, None, 0.000306518, None, 0.00181433, None, 0.000306518, None, -0.0019022, None, 0.000325147, None, -0.0019022, None, 0.000325147, None, 1.26249, None, 0.00942262, None, 1.26249, None, 0.00942262, None)

reports.append(Report(604025912, ("CSC", 1, 3, 2, 7), "MEp32_07"))
reports[-1].posNum = 63002
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00713827, 0.00680482, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(7.15113e-05, 6.78483e-05, 0), \
                           -106402, 63002, 63002, -nan)
reports[-1].sigmaresid = ValErr(1.30986, 0.00369006, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00297998, None, -7.34207e-05, None, -0.00253639, None, -0.000307087, None, -0.00253639, None, -0.000307087, None, -0.0131651, None, -0.000323389, None, -0.0131651, None, -0.000323389, None, 1.30987, None, 0.0109883, None, 1.30987, None, 0.0109883, None)

reports.append(Report(604025928, ("CSC", 1, 3, 2, 9), "MEp32_09"))
reports[-1].posNum = 62412
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00145271, 0.0066315, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.20558e-06, 6.55117e-05, 0), \
                           -106887, 62412, 62412, -nan)
reports[-1].sigmaresid = ValErr(1.34133, 0.00379653, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00416298, None, -0.000635601, None, -0.00170296, None, -0.000857609, None, -0.00170296, None, -0.000857609, None, 0.00729211, None, -0.000892538, None, 0.00729211, None, -0.000892538, None, 1.34133, None, 0.00991058, None, 1.34133, None, 0.00991058, None)

reports.append(Report(604025944, ("CSC", 1, 3, 2, 11), "MEp32_11"))
reports[-1].posNum = 63892
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0021881, 0.00675246, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.96303e-05, 6.69329e-05, 0), \
                           -108662, 63892, 63892, -nan)
reports[-1].sigmaresid = ValErr(1.32547, 0.00370794, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00623235, None, 0.000325768, None, -0.000331439, None, 0.000204204, None, -0.000331439, None, 0.000204204, None, -0.00500087, None, 0.000236954, None, -0.00500087, None, 0.000236954, None, 1.32548, None, 0.00935136, None, 1.32548, None, 0.00935136, None)

reports.append(Report(604025960, ("CSC", 1, 3, 2, 13), "MEp32_13"))
reports[-1].posNum = 62076
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00251657, 0.00650005, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.63201e-05, 6.31346e-05, 0), \
                           -105589, 62076, 62076, -nan)
reports[-1].sigmaresid = ValErr(1.3258, 0.00376272, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00215622, None, -0.000946911, None, -0.000960338, None, -0.00107006, None, -0.000960338, None, -0.00107006, None, 0.00172098, None, -0.00115804, None, 0.00172098, None, -0.00115804, None, 1.3258, None, 0.00966781, None, 1.3258, None, 0.00966781, None)

reports.append(Report(604025976, ("CSC", 1, 3, 2, 15), "MEp32_15"))
reports[-1].posNum = 73226
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00173302, 0.00587154, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.59797e-05, 5.86834e-05, 0), \
                           -126032, 73226, 73226, -nan)
reports[-1].sigmaresid = ValErr(1.35284, 0.00353507, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00205916, None, -0.00018282, None, 0.000680619, None, -0.000291935, None, 0.000680619, None, -0.000291935, None, 0.00540449, None, -0.000321034, None, 0.00540449, None, -0.000321034, None, 1.35284, None, 0.00964525, None, 1.35284, None, 0.00964525, None)

reports.append(Report(604025992, ("CSC", 1, 3, 2, 17), "MEp32_17"))
reports[-1].posNum = 63286
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00130529, 0.00647077, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.45878e-05, 6.28067e-05, 0), \
                           -106288, 63286, 63286, -nan)
reports[-1].sigmaresid = ValErr(1.29765, 0.00364745, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00325096, None, -0.000939557, None, -0.00407591, None, -0.00124355, None, -0.00407591, None, -0.00124355, None, -0.00420387, None, -0.00125134, None, -0.00420387, None, -0.00125134, None, 1.29765, None, 0.00965839, None, 1.29765, None, 0.00965839, None)

reports.append(Report(604026008, ("CSC", 1, 3, 2, 19), "MEp32_19"))
reports[-1].posNum = 59632
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00584839, 0.0063926, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.698e-05, 6.27753e-05, 0), \
                           -102836, 59632, 59632, -nan)
reports[-1].sigmaresid = ValErr(1.35741, 0.00393058, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00598108, None, 0.00105332, None, -0.0024795, None, 0.00106434, None, -0.0024795, None, 0.00106434, None, -0.00663491, None, 0.00114017, None, -0.00663491, None, 0.00114017, None, 1.35743, None, 0.0119204, None, 1.35743, None, 0.0119204, None)

reports.append(Report(604026024, ("CSC", 1, 3, 2, 21), "MEp32_21"))
reports[-1].posNum = 62330
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00905027, 0.00647346, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000131015, 6.33706e-05, 0), \
                           -106329, 62330, 62330, -nan)
reports[-1].sigmaresid = ValErr(1.33238, 0.00377367, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00787455, None, 0.000369907, None, -0.00147523, None, 0.00024892, None, -0.00147523, None, 0.00024892, None, -0.00506786, None, 0.000257473, None, -0.00506786, None, 0.000257473, None, 1.33243, None, 0.0102889, None, 1.33243, None, 0.0102889, None)

reports.append(Report(604026040, ("CSC", 1, 3, 2, 23), "MEp32_23"))
reports[-1].posNum = 70504
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00620879, 0.00601401, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.74518e-05, 5.96874e-05, 0), \
                           -122045, 70504, 70504, -nan)
reports[-1].sigmaresid = ValErr(1.3663, 0.0036385, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00083794, None, -0.000416771, None, -0.0032118, None, -0.000522706, None, -0.0032118, None, -0.000522706, None, -0.0104302, None, -0.000593611, None, -0.0104302, None, -0.000593611, None, 1.36631, None, 0.00979861, None, 1.36631, None, 0.00979861, None)

reports.append(Report(604026056, ("CSC", 1, 3, 2, 25), "MEp32_25"))
reports[-1].posNum = 63222
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00718469, 0.00689319, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(7.83789e-05, 6.78161e-05, 0), \
                           -105891, 63222, 63222, -nan)
reports[-1].sigmaresid = ValErr(1.29171, 0.00363258, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00593286, None, 0.000301898, None, -0.00187224, None, 0.000256327, None, -0.00187224, None, 0.000256327, None, -0.00280053, None, 0.000206602, None, -0.00280053, None, 0.000206602, None, 1.29172, None, 0.00913463, None, 1.29172, None, 0.00913463, None)

reports.append(Report(604026072, ("CSC", 1, 3, 2, 27), "MEp32_27"))
reports[-1].posNum = 53648
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0117815, 0.00730786, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(8.37023e-05, 6.98067e-05, 0), \
                           -91233.7, 53648, 53648, -nan)
reports[-1].sigmaresid = ValErr(1.32533, 0.00404605, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0044082, None, 0.00051256, None, -0.00633059, None, -0.00031018, None, -0.00633059, None, -0.00031018, None, -0.00584401, None, -0.000373295, None, -0.00584401, None, -0.000373295, None, 1.32535, None, 0.0103604, None, 1.32535, None, 0.0103604, None)

reports.append(Report(604026088, ("CSC", 1, 3, 2, 29), "MEp32_29"))
reports[-1].posNum = 53362
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0116864, 0.00706517, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.48434e-05, 6.75685e-05, 0), \
                           -90970.2, 53362, 53362, -nan)
reports[-1].sigmaresid = ValErr(1.33087, 0.00407383, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00471551, None, -0.000808178, None, 0.00594726, None, -0.00120679, None, 0.00594726, None, -0.00120679, None, 0.00973771, None, -0.0013373, None, 0.00973771, None, -0.0013373, None, 1.3309, None, 0.0104948, None, 1.3309, None, 0.0104948, None)

reports.append(Report(604026104, ("CSC", 1, 3, 2, 31), "MEp32_31"))
reports[-1].posNum = 57706
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0132233, 0.00683961, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000124284, 6.5826e-05, 0), \
                           -98125, 57706, 57706, -nan)
reports[-1].sigmaresid = ValErr(1.3251, 0.00390051, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00852628, None, 0.000904713, None, 0.00558689, None, 0.000862808, None, 0.00558689, None, 0.000862808, None, -0.00158188, None, 0.000859918, None, -0.00158188, None, 0.000859918, None, 1.32515, None, 0.0112165, None, 1.32515, None, 0.0112165, None)

reports.append(Report(604026120, ("CSC", 1, 3, 2, 33), "MEp32_33"))
reports[-1].posNum = 69528
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0102972, 0.00606725, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.78662e-05, 6.04986e-05, 0), \
                           -119116, 69528, 69528, -nan)
reports[-1].sigmaresid = ValErr(1.34214, 0.00359918, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000985328, None, -4.57192e-05, None, 0.00495548, None, -0.00030972, None, 0.00495548, None, -0.00030972, None, 0.00400326, None, -0.000343717, None, 0.00400326, None, -0.000343717, None, 1.34217, None, 0.010068, None, 1.34217, None, 0.010068, None)

reports.append(Report(604026136, ("CSC", 1, 3, 2, 35), "MEp32_35"))
reports[-1].posNum = 53308
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0128598, 0.00766069, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(9.04707e-05, 7.20625e-05, 0), \
                           -88838.6, 53308, 53308, -nan)
reports[-1].sigmaresid = ValErr(1.28092, 0.00392292, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.010628, None, -0.000388705, None, -0.00622706, None, -0.000789204, None, -0.00622706, None, -0.000789204, None, -0.00375384, None, -0.000883719, None, -0.00375384, None, -0.000883719, None, 1.28094, None, 0.00940518, None, 1.28094, None, 0.00940518, None)

reports.append(Report(604025872, ("CSC", 1, 3, 2, 2), "MEp32_02"))
reports[-1].posNum = 58356
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00596566, 0.00733159, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.60187e-05, 7.22097e-05, 0), \
                           -98641.6, 58356, 58356, -nan)
reports[-1].sigmaresid = ValErr(1.3118, 0.00383982, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0059333, None, -0.000179737, None, 0.00282664, None, -0.000364339, None, 0.00282664, None, -0.000364339, None, 0.0134069, None, -0.000335227, None, 0.0134069, None, -0.000335227, None, 1.31181, None, 0.00830457, None, 1.31181, None, 0.00830457, None)

reports.append(Report(604025888, ("CSC", 1, 3, 2, 4), "MEp32_04"))
reports[-1].posNum = 57074
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00969955, 0.00858587, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000114261, 8.42384e-05, 0), \
                           -95096.8, 57074, 57074, -nan)
reports[-1].sigmaresid = ValErr(1.28052, 0.0037901, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00601891, None, 0.000793592, None, 0.000602068, None, 0.000613732, None, 0.000602068, None, 0.000613732, None, 0.000493118, None, 0.000684873, None, 0.000493118, None, 0.000684873, None, 1.28054, None, 0.00787592, None, 1.28054, None, 0.00787592, None)

reports.append(Report(604025904, ("CSC", 1, 3, 2, 6), "MEp32_06"))
reports[-1].posNum = 67980
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000157586, 0.006649, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.08608e-05, 6.82293e-05, 0), \
                           -116405, 67980, 67980, -nan)
reports[-1].sigmaresid = ValErr(1.34098, 0.00363677, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00352802, None, 0.000599001, None, 0.00144614, None, 0.000275896, None, 0.00144614, None, 0.000275896, None, -0.00718862, None, 0.000256912, None, -0.00718862, None, 0.000256912, None, 1.34098, None, 0.00901948, None, 1.34098, None, 0.00901948, None)

reports.append(Report(604025920, ("CSC", 1, 3, 2, 8), "MEp32_08"))
reports[-1].posNum = 65744
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00133852, 0.00647807, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.8982e-05, 6.3969e-05, 0), \
                           -112549, 65744, 65744, -nan)
reports[-1].sigmaresid = ValErr(1.34043, 0.0036966, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00163705, None, 6.36515e-05, None, -0.000993598, None, -0.000340524, None, -0.000993598, None, -0.000340524, None, -0.00355597, None, -0.00035279, None, -0.00355597, None, -0.00035279, None, 1.34044, None, 0.00892304, None, 1.34044, None, 0.00892304, None)

reports.append(Report(604025936, ("CSC", 1, 3, 2, 10), "MEp32_10"))
reports[-1].posNum = 70526
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00548124, 0.00625578, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.05163e-05, 6.3422e-05, 0), \
                           -122497, 70526, 70526, -nan)
reports[-1].sigmaresid = ValErr(1.37433, 0.00365932, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00612004, None, -0.000769055, None, -0.00268126, None, -0.000629265, None, -0.00268126, None, -0.000629265, None, -0.00310189, None, -0.000611747, None, -0.00310189, None, -0.000611747, None, 1.37433, None, 0.00918904, None, 1.37433, None, 0.00918904, None)

reports.append(Report(604025952, ("CSC", 1, 3, 2, 12), "MEp32_12"))
reports[-1].posNum = 69070
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00589307, 0.00634086, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(7.38488e-05, 6.17849e-05, 0), \
                           -119136, 69070, 69070, -nan)
reports[-1].sigmaresid = ValErr(1.35787, 0.0036534, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00630088, None, 0.00032626, None, -0.00149861, None, 0.000167875, None, -0.00149861, None, 0.000167875, None, -0.00210196, None, 0.000202652, None, -0.00210196, None, 0.000202652, None, 1.35788, None, 0.00848129, None, 1.35788, None, 0.00848129, None)

reports.append(Report(604025968, ("CSC", 1, 3, 2, 14), "MEp32_14"))
reports[-1].posNum = 80970
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00119614, 0.00562809, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.52828e-05, 5.73771e-05, 0), \
                           -141636, 80970, 80970, -nan)
reports[-1].sigmaresid = ValErr(1.39139, 0.00345758, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0037223, None, -0.000133836, None, 0.000519206, None, -0.000177482, None, 0.000519206, None, -0.000177482, None, -0.0023782, None, -0.000215939, None, -0.0023782, None, -0.000215939, None, 1.3914, None, 0.00853116, None, 1.3914, None, 0.00853116, None)

reports.append(Report(604025984, ("CSC", 1, 3, 2, 16), "MEp32_16"))
reports[-1].posNum = 71630
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0133123, 0.00610449, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000148547, 5.99407e-05, 0), \
                           -124152, 71630, 71630, -nan)
reports[-1].sigmaresid = ValErr(1.3693, 0.00361772, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00353332, None, -0.000264233, None, -0.00505982, None, -0.000342926, None, -0.00505982, None, -0.000342926, None, -0.0037315, None, -0.000372744, None, -0.0037315, None, -0.000372744, None, 1.36936, None, 0.0101798, None, 1.36936, None, 0.0101798, None)

reports.append(Report(604026000, ("CSC", 1, 3, 2, 18), "MEp32_18"))
reports[-1].posNum = 72860
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0241059, 0.00600402, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000263855, 5.99185e-05, 0), \
                           -126052, 72860, 72860, -nan)
reports[-1].sigmaresid = ValErr(1.36495, 0.00357566, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00793215, None, -0.000277974, None, -0.00985186, None, -0.000522999, None, -0.00985186, None, -0.000522999, None, -0.0130329, None, -0.000568596, None, -0.0130329, None, -0.000568596, None, 1.36513, None, 0.00869086, None, 1.36513, None, 0.00869086, None)

reports.append(Report(604026016, ("CSC", 1, 3, 2, 20), "MEp32_20"))
reports[-1].posNum = 65856
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00202556, 0.00630966, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.19922e-05, 6.07073e-05, 0), \
                           -115419, 65856, 65856, -nan)
reports[-1].sigmaresid = ValErr(1.39608, 0.00384679, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00260454, None, -0.000455076, None, -0.00086747, None, -0.000651369, None, -0.00086747, None, -0.000651369, None, -0.000996827, None, -0.00070941, None, -0.000996827, None, -0.00070941, None, 1.39608, None, 0.00976269, None, 1.39608, None, 0.00976269, None)

reports.append(Report(604026032, ("CSC", 1, 3, 2, 22), "MEp32_22"))
reports[-1].posNum = 65940
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0057497, 0.00645763, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(8.28642e-05, 6.32764e-05, 0), \
                           -114186, 65940, 65940, -nan)
reports[-1].sigmaresid = ValErr(1.36714, 0.00376463, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00176346, None, 0.000422779, None, -0.000962453, None, 0.000236432, None, -0.000962453, None, 0.000236432, None, 0.00552256, None, 0.000232116, None, 0.00552256, None, 0.000232116, None, 1.36716, None, 0.008601, None, 1.36716, None, 0.008601, None)

reports.append(Report(604026048, ("CSC", 1, 3, 2, 24), "MEp32_24"))
reports[-1].posNum = 73426
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00246397, 0.00602577, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.12625e-06, 6.04155e-05, 0), \
                           -127776, 73426, 73426, -nan)
reports[-1].sigmaresid = ValErr(1.37887, 0.0035982, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00590088, None, 0.00081621, None, 0.00251998, None, 0.000670856, None, 0.00251998, None, 0.000670856, None, -0.00145216, None, 0.000668689, None, -0.00145216, None, 0.000668689, None, 1.37886, None, 0.00965109, None, 1.37886, None, 0.00965109, None)

reports.append(Report(604026064, ("CSC", 1, 3, 2, 26), "MEp32_26"))
reports[-1].posNum = 60582
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00169587, 0.00730371, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.10478e-05, 6.98625e-05, 0), \
                           -101899, 60582, 60582, -nan)
reports[-1].sigmaresid = ValErr(1.30091, 0.00373733, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000724566, None, 0.000167283, None, -0.00017647, None, 8.26642e-05, None, -0.00017647, None, 8.26642e-05, None, 0.00623235, None, 9.1243e-05, None, 0.00623235, None, 9.1243e-05, None, 1.30091, None, 0.00835614, None, 1.30091, None, 0.00835614, None)

reports.append(Report(604026080, ("CSC", 1, 3, 2, 28), "MEp32_28"))
reports[-1].posNum = 75928
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00547732, 0.00589127, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.82485e-05, 5.94839e-05, 0), \
                           -133144, 75928, 75928, -nan)
reports[-1].sigmaresid = ValErr(1.39741, 0.00358599, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00248303, None, 3.0225e-06, None, 0.00254206, None, -0.000245241, None, 0.00254206, None, -0.000245241, None, -1.47048e-05, None, -0.000231159, None, -1.47048e-05, None, -0.000231159, None, 1.39742, None, 0.00926841, None, 1.39742, None, 0.00926841, None)

reports.append(Report(604026096, ("CSC", 1, 3, 2, 30), "MEp32_30"))
reports[-1].posNum = 57822
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0241135, 0.0071959, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00022154, 6.67713e-05, 0), \
                           -97965.4, 57822, 57822, -nan)
reports[-1].sigmaresid = ValErr(1.31695, 0.00387262, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00302004, None, 0.000366272, None, 0.008626, None, 3.71638e-05, None, 0.008626, None, 3.71638e-05, None, 0.0132699, None, 8.12904e-05, None, 0.0132699, None, 8.12904e-05, None, 1.31708, None, 0.0088729, None, 1.31708, None, 0.0088729, None)

reports.append(Report(604026112, ("CSC", 1, 3, 2, 32), "MEp32_32"))
reports[-1].posNum = 72788
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0135936, 0.0060938, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000164236, 6.1837e-05, 0), \
                           -125959, 72788, 72788, -nan)
reports[-1].sigmaresid = ValErr(1.36555, 0.00357901, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00173934, None, 0.000676003, None, 0.00458072, None, 0.0005002, None, 0.00458072, None, 0.0005002, None, 0.0080665, None, 0.000534942, None, 0.0080665, None, 0.000534942, None, 1.36562, None, 0.00984523, None, 1.36562, None, 0.00984523, None)

reports.append(Report(604026128, ("CSC", 1, 3, 2, 34), "MEp32_34"))
reports[-1].posNum = 62552
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.011975, 0.00687013, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0001359, 6.70747e-05, 0), \
                           -108045, 62552, 62552, -nan)
reports[-1].sigmaresid = ValErr(1.36116, 0.00384835, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00640543, None, 0.000616689, None, 0.00347901, None, 0.000523864, None, 0.00347901, None, 0.000523864, None, 0.00676633, None, 0.000532354, None, 0.00676633, None, 0.000532354, None, 1.36121, None, 0.00883599, None, 1.36121, None, 0.00883599, None)

reports.append(Report(604026144, ("CSC", 1, 3, 2, 36), "MEp32_36"))
reports[-1].posNum = 59050
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00155604, 0.00688685, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.2294e-05, 6.59416e-05, 0), \
                           -101049, 59050, 59050, -nan)
reports[-1].sigmaresid = ValErr(1.33951, 0.00389782, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00554096, None, -0.000573442, None, 0.000159721, None, -0.000782437, None, 0.000159721, None, -0.000782437, None, 0.00784633, None, -0.000735664, None, 0.00784633, None, -0.000735664, None, 1.33951, None, 0.00875046, None, 1.33951, None, 0.00875046, None)

reports.append(Report(604029448, ("CSC", 1, 4, 1, 1), "MEp41_01"))
reports[-1].posNum = 131518
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000195631, 0.00213801, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.55367e-05, 4.97357e-05, 0), \
                           -152200, 131518, 131518, -nan)
reports[-1].sigmaresid = ValErr(0.769757, 0.00150088, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0083577, None, -0.000660921, None, 0.00011678, None, -0.00104921, None, 0.00011678, None, -0.00104921, None, 0.00195249, None, -0.00110156, None, 0.00195249, None, -0.00110156, None, 0.769757, None, 0.00825761, None, 0.769757, None, 0.00825761, None)

reports.append(Report(604029464, ("CSC", 1, 4, 1, 3), "MEp41_03"))
reports[-1].posNum = 133734
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000475902, 0.00214838, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.24605e-05, 4.98261e-05, 0), \
                           -156655, 133734, 133734, -nan)
reports[-1].sigmaresid = ValErr(0.780714, 0.00150958, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00445418, None, -2.11261e-05, None, -0.000369305, None, -0.000260723, None, -0.000369305, None, -0.000260723, None, -0.00122303, None, -0.000325131, None, -0.00122303, None, -0.000325131, None, 0.780714, None, 0.0095542, None, 0.780714, None, 0.0095542, None)

reports.append(Report(604029480, ("CSC", 1, 4, 1, 5), "MEp41_05"))
reports[-1].posNum = 138036
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000545179, 0.00211528, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.84442e-05, 4.88443e-05, 0), \
                           -161378, 138036, 138036, -nan)
reports[-1].sigmaresid = ValErr(0.778926, 0.00148247, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00226017, None, -0.000439005, None, -0.000440804, None, -0.000768355, None, -0.000440804, None, -0.000768355, None, -0.00361501, None, -0.000834767, None, -0.00361501, None, -0.000834767, None, 0.778925, None, 0.00790956, None, 0.778925, None, 0.00790956, None)

reports.append(Report(604029496, ("CSC", 1, 4, 1, 7), "MEp41_07"))
reports[-1].posNum = 135000
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00137089, 0.00213146, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.24158e-05, 4.94531e-05, 0), \
                           -157423, 135000, 135000, -nan)
reports[-1].sigmaresid = ValErr(0.776592, 0.00149455, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00349564, None, -0.00026108, None, 0.00113802, None, -0.000630813, None, 0.00113802, None, -0.000630813, None, 0.000709564, None, -0.000675231, None, 0.000709564, None, -0.000675231, None, 0.776593, None, 0.00812639, None, 0.776593, None, 0.00812639, None)

reports.append(Report(604029512, ("CSC", 1, 4, 1, 9), "MEp41_09"))
reports[-1].posNum = 125560
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000413919, 0.00223041, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(8.61004e-05, 5.27887e-05, 0), \
                           -148323, 125560, 125560, -nan)
reports[-1].sigmaresid = ValErr(0.788484, 0.00157345, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000315088, None, -0.00077661, None, -0.00016753, None, -0.00115904, None, -0.00016753, None, -0.00115904, None, -0.000602367, None, -0.00122154, None, -0.000602367, None, -0.00122154, None, 0.788491, None, 0.00803992, None, 0.788491, None, 0.00803992, None)

reports.append(Report(604029528, ("CSC", 1, 4, 1, 11), "MEp41_11"))
reports[-1].posNum = 116590
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00185593, 0.00230174, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(9.65735e-05, 5.40691e-05, 0), \
                           -136979, 116590, 116590, -nan)
reports[-1].sigmaresid = ValErr(0.783443, 0.00162242, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00140757, None, -0.000401673, None, -0.00153212, None, -0.000709735, None, -0.00153212, None, -0.000709735, None, -0.00253975, None, -0.000774681, None, -0.00253975, None, -0.000774681, None, 0.783452, None, 0.00813035, None, 0.783452, None, 0.00813035, None)

reports.append(Report(604029544, ("CSC", 1, 4, 1, 13), "MEp41_13"))
reports[-1].posNum = 127836
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(6.77521e-05, 0.00221313, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.13676e-05, 5.11296e-05, 0), \
                           -150486, 127836, 127836, -nan)
reports[-1].sigmaresid = ValErr(0.785247, 0.00155298, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000688771, None, -8.10417e-06, None, 0.000181406, None, -0.000195901, None, 0.000181406, None, -0.000195901, None, -0.00158375, None, -0.000180131, None, -0.00158375, None, -0.000180131, None, 0.785246, None, 0.00827904, None, 0.785246, None, 0.00827904, None)

reports.append(Report(604029560, ("CSC", 1, 4, 1, 15), "MEp41_15"))
reports[-1].posNum = 90172
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000136182, 0.00262724, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.24654e-05, 6.08851e-05, 0), \
                           -105888, 90172, 90172, -nan)
reports[-1].sigmaresid = ValErr(0.782979, 0.00184373, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00344535, None, -0.000167616, None, 0.000413713, None, -6.97271e-05, None, 0.000413713, None, -6.97271e-05, None, 0.000201223, None, -0.000360589, None, 0.000201223, None, -0.000360589, None, 0.782983, None, 0.0107102, None, 0.782983, None, 0.0107102, None)

reports.append(Report(604029576, ("CSC", 1, 4, 1, 17), "MEp41_17"))
reports[-1].posNum = 135306
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000328101, 0.00211806, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(8.88473e-07, 4.9231e-05, 0), \
                           -157439, 135306, 135306, -nan)
reports[-1].sigmaresid = ValErr(0.774637, 0.00148911, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0114544, None, 0.000507356, None, -0.000323012, None, 0.000218109, None, -0.000323012, None, 0.000218109, None, 0.00300425, None, 0.000267581, None, 0.00300425, None, 0.000267581, None, 0.774635, None, 0.00814731, None, 0.774635, None, 0.00814731, None)

reports.append(Report(604029456, ("CSC", 1, 4, 1, 2), "MEp41_02"))
reports[-1].posNum = 131536
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000455261, 0.00221035, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.15512e-05, 5.11601e-05, 0), \
                           -156537, 131536, 131536, -nan)
reports[-1].sigmaresid = ValErr(0.795431, 0.00155084, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00209442, None, -0.000212544, None, 0.000289949, None, -0.00056992, None, 0.000289949, None, -0.00056992, None, 0.001267, None, -0.000587642, None, 0.001267, None, -0.000587642, None, 0.795431, None, 0.00727544, None, 0.795431, None, 0.00727544, None)

reports.append(Report(604029472, ("CSC", 1, 4, 1, 4), "MEp41_04"))
reports[-1].posNum = 139740
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00206484, 0.00213601, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.25617e-06, 4.93524e-05, 0), \
                           -165970, 139740, 139740, -nan)
reports[-1].sigmaresid = ValErr(0.793556, 0.00150107, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00495678, None, -0.000163364, None, -0.00203942, None, -0.000610435, None, -0.00203942, None, -0.000610435, None, -0.00256741, None, -0.000663738, None, -0.00256741, None, -0.000663738, None, 0.793556, None, 0.00749865, None, 0.793556, None, 0.00749865, None)

reports.append(Report(604029488, ("CSC", 1, 4, 1, 6), "MEp41_06"))
reports[-1].posNum = 138964
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(4.90145e-05, 0.00216689, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.80871e-06, 5.05436e-05, 0), \
                           -166705, 138964, 138964, -nan)
reports[-1].sigmaresid = ValErr(0.803076, 0.00152332, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00146335, None, 3.3297e-05, None, 7.02099e-05, None, -0.000136749, None, 7.02099e-05, None, -0.000136749, None, -0.000563935, None, -0.00014122, None, -0.000563935, None, -0.00014122, None, 0.803075, None, 0.0076181, None, 0.803075, None, 0.0076181, None)

reports.append(Report(604029504, ("CSC", 1, 4, 1, 8), "MEp41_08"))
reports[-1].posNum = 132764
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00096696, 0.00223435, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(9.76757e-05, 5.36274e-05, 0), \
                           -160911, 132764, 132764, -nan)
reports[-1].sigmaresid = ValErr(0.813075, 0.00157789, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000506445, None, -1.73636e-05, None, -0.000759993, None, -0.000261316, None, -0.000759993, None, -0.000261316, None, -0.000540526, None, -0.000292552, None, -0.000540526, None, -0.000292552, None, 0.813085, None, 0.00746422, None, 0.813085, None, 0.00746422, None)

reports.append(Report(604029520, ("CSC", 1, 4, 1, 10), "MEp41_10"))
reports[-1].posNum = 126352
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00111439, 0.00228587, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.6824e-05, 5.51058e-05, 0), \
                           -153020, 126352, 126352, -nan)
reports[-1].sigmaresid = ValErr(0.812306, 0.0016159, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00162519, None, -0.000645855, None, -0.00104788, None, -0.000926865, None, -0.00104788, None, -0.000926865, None, -0.00430247, None, -0.000986756, None, -0.00430247, None, -0.000986756, None, 0.81231, None, 0.00737316, None, 0.81231, None, 0.00737316, None)

reports.append(Report(604029536, ("CSC", 1, 4, 1, 12), "MEp41_12"))
reports[-1].posNum = 120528
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0016542, 0.00236222, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.25275e-05, 5.71237e-05, 0), \
                           -147047, 120528, 120528, -nan)
reports[-1].sigmaresid = ValErr(0.819619, 0.00166937, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00524027, None, -0.000707321, None, 0.00153734, None, -0.00116215, None, 0.00153734, None, -0.00116215, None, 0.00307953, None, -0.00114504, None, 0.00307953, None, -0.00114504, None, 0.819625, None, 0.00861261, None, 0.819625, None, 0.00861261, None)

reports.append(Report(604029552, ("CSC", 1, 4, 1, 14), "MEp41_14"))
reports[-1].posNum = 135112
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000732236, 0.00222686, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.84237e-05, 5.31715e-05, 0), \
                           -164318, 135112, 135112, -nan)
reports[-1].sigmaresid = ValErr(0.816458, 0.00157062, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00392416, None, -0.000371669, None, -0.0008164, None, -0.000724252, None, -0.0008164, None, -0.000724252, None, -0.000803336, None, -0.000782683, None, -0.000803336, None, -0.000782683, None, 0.816459, None, 0.00755994, None, 0.816459, None, 0.00755994, None)

reports.append(Report(604029568, ("CSC", 1, 4, 1, 16), "MEp41_16"))
reports[-1].posNum = 135608
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00222436, 0.00218866, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.33507e-05, 5.16947e-05, 0), \
                           -162843, 135608, 135608, -nan)
reports[-1].sigmaresid = ValErr(0.804042, 0.00154391, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00132707, None, 0.000795888, None, 0.00229061, None, 0.000621609, None, 0.00229061, None, 0.000621609, None, 0.000240456, None, 0.000665333, None, 0.000240456, None, 0.000665333, None, 0.804042, None, 0.00781164, None, 0.804042, None, 0.00781164, None)

reports.append(Report(604029584, ("CSC", 1, 4, 1, 18), "MEp41_18"))
reports[-1].posNum = 140624
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000364832, 0.00212225, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.22012e-05, 4.93184e-05, 0), \
                           -166582, 140624, 140624, -nan)
reports[-1].sigmaresid = ValErr(0.791088, 0.00149169, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0068162, None, 0.000310924, None, 0.000563553, None, -4.85235e-05, None, 0.000563553, None, -4.85235e-05, None, 0.00391618, None, -6.02732e-05, None, 0.00391618, None, -6.02732e-05, None, 0.79109, None, 0.00770211, None, 0.79109, None, 0.00770211, None)

reports.append(Report(604029960, ("CSC", 1, 4, 2, 1), "MEp42_01"))
reports[-1].posNum = 66620
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0182361, 0.00667675, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000259601, 6.78998e-05, 0), \
                           -117990, 66620, 66620, -nan)
reports[-1].sigmaresid = ValErr(1.42213, 0.00389602, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00590694, None, -0.00216158, None, 0.00381822, None, -0.00220926, None, 0.00381822, None, -0.00220926, None, 0.00824274, None, -0.00229434, None, 0.00824274, None, -0.00229434, None, 1.42228, None, 0.00891197, None, 1.42228, None, 0.00891197, None)

reports.append(Report(604029976, ("CSC", 1, 4, 2, 3), "MEp42_03"))
reports[-1].posNum = 63678
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00979848, 0.00731937, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000134782, 7.5416e-05, 0), \
                           -110368, 63678, 63678, -nan)
reports[-1].sigmaresid = ValErr(1.36929, 0.00383693, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00489648, None, -0.00176671, None, 0.00101885, None, -0.00181124, None, 0.00101885, None, -0.00181124, None, -0.00497359, None, -0.00191367, None, -0.00497359, None, -0.00191367, None, 1.36932, None, 0.00914304, None, 1.36932, None, 0.00914304, None)

reports.append(Report(604029992, ("CSC", 1, 4, 2, 5), "MEp42_05"))
reports[-1].posNum = 64908
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(3.13774e-05, 0.00705772, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.12863e-05, 7.32473e-05, 0), \
                           -114318, 64908, 64908, -nan)
reports[-1].sigmaresid = ValErr(1.40818, 0.00390836, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00485154, None, 0.000129512, None, 0.00370337, None, -4.75343e-05, None, 0.00370337, None, -4.75343e-05, None, 0.00780124, None, -8.43403e-06, None, 0.00780124, None, -8.43403e-06, None, 1.40819, None, 0.00909409, None, 1.40819, None, 0.00909409, None)

reports.append(Report(604030008, ("CSC", 1, 4, 2, 7), "MEp42_07"))
reports[-1].posNum = 71310
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00762912, 0.00645498, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(9.05088e-05, 6.6643e-05, 0), \
                           -127403, 71310, 71310, -nan)
reports[-1].sigmaresid = ValErr(1.44436, 0.00382458, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000711972, None, 0.000168362, None, -0.00284102, None, -1.72014e-05, None, -0.00284102, None, -1.72014e-05, None, -0.00124214, None, -2.30273e-06, None, -0.00124214, None, -2.30273e-06, None, 1.44438, None, 0.00906248, None, 1.44438, None, 0.00906248, None)

reports.append(Report(604030024, ("CSC", 1, 4, 2, 9), "MEp42_09"))
reports[-1].posNum = 70064
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0028424, 0.00642262, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.90279e-05, 6.56715e-05, 0), \
                           -124859, 70064, 70064, -nan)
reports[-1].sigmaresid = ValErr(1.43782, 0.00384098, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.006382, None, -0.000144945, None, 0.0018496, None, -0.000165231, None, 0.0018496, None, -0.000165231, None, -0.000682899, None, -0.000207935, None, -0.000682899, None, -0.000207935, None, 1.43782, None, 0.00947751, None, 1.43782, None, 0.00947751, None)

reports.append(Report(604030040, ("CSC", 1, 4, 2, 11), "MEp42_11"))
reports[-1].posNum = 66346
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00189199, 0.00696801, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.88569e-05, 7.14014e-05, 0), \
                           -117670, 66346, 66346, -nan)
reports[-1].sigmaresid = ValErr(1.42568, 0.0039138, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00284546, None, -0.000476045, None, -0.00100408, None, -0.000581111, None, -0.00100408, None, -0.000581111, None, 0.0118433, None, -0.000572111, None, 0.0118433, None, -0.000572111, None, 1.42568, None, 0.00904107, None, 1.42568, None, 0.00904107, None)

reports.append(Report(604030056, ("CSC", 1, 4, 2, 13), "MEp42_13"))
reports[-1].posNum = 66350
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00649948, 0.00667208, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.32285e-05, 6.8017e-05, 0), \
                           -117058, 66350, 66350, -nan)
reports[-1].sigmaresid = ValErr(1.41242, 0.0038773, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00236267, None, -0.000474318, None, 0.00296273, None, -0.000746563, None, 0.00296273, None, -0.000746563, None, 0.00202607, None, -0.000765686, None, 0.00202607, None, -0.000765686, None, 1.41243, None, 0.00924672, None, 1.41243, None, 0.00924672, None)

reports.append(Report(604030072, ("CSC", 1, 4, 2, 15), "MEp42_15"))
reports[-1].posNum = 73832
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00367143, 0.00605983, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.86796e-05, 6.33114e-05, 0), \
                           -132740, 73832, 73832, -nan)
reports[-1].sigmaresid = ValErr(1.46071, 0.00380123, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000216118, None, 0.0022987, None, 0.00240393, None, 0.0020544, None, 0.00240393, None, 0.0020544, None, -0.00116137, None, 0.00225018, None, -0.00116137, None, 0.00225018, None, 1.46071, None, 0.00964472, None, 1.46071, None, 0.00964472, None)

reports.append(Report(604030088, ("CSC", 1, 4, 2, 17), "MEp42_17"))
reports[-1].posNum = 51294
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00752365, 0.00754475, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.37489e-05, 7.73479e-05, 0), \
                           -90853, 51294, 51294, -nan)
reports[-1].sigmaresid = ValErr(1.42231, 0.00444064, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00449546, None, -0.00220565, None, 0.0046192, None, -0.00228404, None, 0.0046192, None, -0.00228404, None, 0.00891745, None, -0.00244568, None, 0.00891745, None, -0.00244568, None, 1.42232, None, 0.0110787, None, 1.42232, None, 0.0110787, None)

reports.append(Report(604030104, ("CSC", 1, 4, 2, 19), "MEp42_19"))
reports[-1].posNum = 75300
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0134589, 0.00604302, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000186985, 6.27396e-05, 0), \
                           -135571, 75300, 75300, -nan)
reports[-1].sigmaresid = ValErr(1.46445, 0.00377364, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00117305, None, 0.000273894, None, -0.00500913, None, 0.000106783, None, -0.00500913, None, 0.000106783, None, -0.0147561, None, 0.00010203, None, -0.0147561, None, 0.00010203, None, 1.46453, None, 0.00969039, None, 1.46453, None, 0.00969039, None)

reports.append(Report(604030120, ("CSC", 1, 4, 2, 21), "MEp42_21"))
reports[-1].posNum = 66360
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.016319, 0.00657803, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000170782, 6.62489e-05, 0), \
                           -117625, 66360, 66360, -nan)
reports[-1].sigmaresid = ValErr(1.42418, 0.00390928, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00701135, None, -0.00348129, None, -0.00712822, None, -0.0034655, None, -0.00712822, None, -0.0034655, None, 0.00259845, None, -0.00362656, None, 0.00259845, None, -0.00362656, None, 1.42425, None, 0.012082, None, 1.42425, None, 0.012082, None)

reports.append(Report(604030136, ("CSC", 1, 4, 2, 23), "MEp42_23"))
reports[-1].posNum = 72030
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00286569, 0.00618459, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.41669e-05, 6.36687e-05, 0), \
                           -130025, 72030, 72030, -nan)
reports[-1].sigmaresid = ValErr(1.4714, 0.00387666, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00189974, None, 0.002398, None, 0.00177901, None, 0.00211027, None, 0.00177901, None, 0.00211027, None, 0.000634204, None, 0.0022185, None, 0.000634204, None, 0.0022185, None, 1.4714, None, 0.0111192, None, 1.4714, None, 0.0111192, None)

reports.append(Report(604030152, ("CSC", 1, 4, 2, 25), "MEp42_25"))
reports[-1].posNum = 69286
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000688306, 0.00654218, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.64066e-05, 6.76761e-05, 0), \
                           -123429, 69286, 69286, -nan)
reports[-1].sigmaresid = ValErr(1.43693, 0.0038601, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00180308, None, -0.000887959, None, 0.00071856, None, -0.000975433, None, 0.00071856, None, -0.000975433, None, 0.00218102, None, -0.000982206, None, 0.00218102, None, -0.000982206, None, 1.43693, None, 0.00996156, None, 1.43693, None, 0.00996156, None)

reports.append(Report(604030168, ("CSC", 1, 4, 2, 27), "MEp42_27"))
reports[-1].posNum = 61474
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.010378, 0.00706755, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000118884, 7.07974e-05, 0), \
                           -109503, 61474, 61474, -nan)
reports[-1].sigmaresid = ValErr(1.4367, 0.00409736, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00276319, None, -0.000206059, None, -0.00357914, None, -0.000347062, None, -0.00357914, None, -0.000347062, None, -0.00904052, None, -0.000390139, None, -0.00904052, None, -0.000390139, None, 1.43673, None, 0.00921538, None, 1.43673, None, 0.00921538, None)

reports.append(Report(604030184, ("CSC", 1, 4, 2, 29), "MEp42_29"))
reports[-1].posNum = 71680
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0152204, 0.00651827, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000194925, 6.60292e-05, 0), \
                           -127672, 71680, 71680, -nan)
reports[-1].sigmaresid = ValErr(1.43648, 0.0037939, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00310574, None, 0.000458761, None, 0.00428335, None, 0.000311257, None, 0.00428335, None, 0.000311257, None, 0.00454095, None, 0.000311594, None, 0.00454095, None, 0.000311594, None, 1.43657, None, 0.00911391, None, 1.43657, None, 0.00911391, None)

reports.append(Report(604030200, ("CSC", 1, 4, 2, 31), "MEp42_31"))
reports[-1].posNum = 63110
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0171452, 0.00686377, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000185357, 6.88062e-05, 0), \
                           -112007, 63110, 63110, -nan)
reports[-1].sigmaresid = ValErr(1.42739, 0.00401771, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00158399, None, 0.0019185, None, 0.00676799, None, 0.00154466, None, 0.00676799, None, 0.00154466, None, 0.000675836, None, 0.00164569, None, 0.000675836, None, 0.00164569, None, 1.42747, None, 0.00978737, None, 1.42747, None, 0.00978737, None)

reports.append(Report(604030216, ("CSC", 1, 4, 2, 33), "MEp42_33"))
reports[-1].posNum = 69454
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.020309, 0.00662007, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000240158, 6.79219e-05, 0), \
                           -123590, 69454, 69454, -nan)
reports[-1].sigmaresid = ValErr(1.43407, 0.00384774, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00210721, None, -0.000888634, None, 0.00696899, None, -0.000948108, None, 0.00696899, None, -0.000948108, None, 0.0104141, None, -0.00102561, None, 0.0104141, None, -0.00102561, None, 1.43419, None, 0.00977157, None, 1.43419, None, 0.00977157, None)

reports.append(Report(604030232, ("CSC", 1, 4, 2, 35), "MEp42_35"))
reports[-1].posNum = 61126
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0054605, 0.00722275, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.08119e-05, 7.09419e-05, 0), \
                           -107883, 61126, 61126, -nan)
reports[-1].sigmaresid = ValErr(1.41338, 0.00404231, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00244113, None, 0.000504181, None, -0.00167488, None, 0.000329032, None, -0.00167488, None, 0.000329032, None, 0.0106358, None, 0.000379816, None, 0.0106358, None, 0.000379816, None, 1.41339, None, 0.00875298, None, 1.41339, None, 0.00875298, None)

reports.append(Report(604029968, ("CSC", 1, 4, 2, 2), "MEp42_02"))
reports[-1].posNum = 69040
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00291421, 0.00674164, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.97472e-05, 6.94341e-05, 0), \
                           -123475, 69040, 69040, -nan)
reports[-1].sigmaresid = ValErr(1.44704, 0.00389416, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00169021, None, -0.000585826, None, -0.000431834, None, -0.000697513, None, -0.000431834, None, -0.000697513, None, -0.00536549, None, -0.000681, None, -0.00536549, None, -0.000681, None, 1.44704, None, 0.0137337, None, 1.44704, None, 0.0137337, None)

reports.append(Report(604029984, ("CSC", 1, 4, 2, 4), "MEp42_04"))
reports[-1].posNum = 49566
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00639344, 0.00876863, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(8.42719e-05, 9.23237e-05, 0), \
                           -88476, 49566, 49566, -nan)
reports[-1].sigmaresid = ValErr(1.44206, 0.00458013, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000147203, None, -0.00206258, None, -0.000998434, None, -0.00212525, None, -0.000998434, None, -0.00212525, None, -0.00858289, None, -0.00215611, None, -0.00858289, None, -0.00215611, None, 1.44208, None, 0.00865495, None, 1.44208, None, 0.00865495, None)

reports.append(Report(604030000, ("CSC", 1, 4, 2, 6), "MEp42_06"))
reports[-1].posNum = 73524
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00108263, 0.0062152, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.52981e-05, 6.76354e-05, 0), \
                           -133507, 73524, 73524, -nan)
reports[-1].sigmaresid = ValErr(1.4872, 0.00387828, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00200559, None, -0.00153843, None, 0.000443845, None, -0.0016309, None, 0.000443845, None, -0.0016309, None, 0.0030324, None, -0.00168516, None, 0.0030324, None, -0.00168516, None, 1.4872, None, 0.00800735, None, 1.4872, None, 0.00800735, None)

reports.append(Report(604030016, ("CSC", 1, 4, 2, 8), "MEp42_08"))
reports[-1].posNum = 70678
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00289657, 0.00662802, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.29942e-05, 6.8481e-05, 0), \
                           -126830, 70678, 70678, -nan)
reports[-1].sigmaresid = ValErr(1.45577, 0.00387197, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00128082, None, -0.00209818, None, -0.000547063, None, -0.00223969, None, -0.000547063, None, -0.00223969, None, -0.0071201, None, -0.00232733, None, -0.0071201, None, -0.00232733, None, 1.45578, None, 0.0082878, None, 1.45578, None, 0.0082878, None)

reports.append(Report(604030032, ("CSC", 1, 4, 2, 10), "MEp42_10"))
reports[-1].posNum = 76224
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00321335, 0.00620838, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.08674e-05, 6.54314e-05, 0), \
                           -138362, 76224, 76224, -nan)
reports[-1].sigmaresid = ValErr(1.48625, 0.00380655, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00173124, None, -0.000877711, None, 0.00269979, None, -0.00116316, None, 0.00269979, None, -0.00116316, None, 0.000981535, None, -0.00121481, None, 0.000981535, None, -0.00121481, None, 1.48625, None, 0.0084784, None, 1.48625, None, 0.0084784, None)

reports.append(Report(604030048, ("CSC", 1, 4, 2, 12), "MEp42_12"))
reports[-1].posNum = 72048
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000628344, 0.00661222, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.46027e-05, 6.72008e-05, 0), \
                           -130282, 72048, 72048, -nan)
reports[-1].sigmaresid = ValErr(1.476, 0.0038883, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000282095, None, -0.000818849, None, 0.00235569, None, -0.00102932, None, 0.00235569, None, -0.00102932, None, -0.00160463, None, -0.00104748, None, -0.00160463, None, -0.00104748, None, 1.476, None, 0.00909542, None, 1.476, None, 0.00909542, None)

reports.append(Report(604030064, ("CSC", 1, 4, 2, 14), "MEp42_14"))
reports[-1].posNum = 83448
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00159467, 0.00579014, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.06003e-05, 6.1001e-05, 0), \
                           -151726, 83448, 83448, -nan)
reports[-1].sigmaresid = ValErr(1.49073, 0.00364902, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00178822, None, -5.14522e-05, None, 0.00015376, None, -0.000244392, None, 0.00015376, None, -0.000244392, None, 0.00259813, None, -0.000263784, None, 0.00259813, None, -0.000263784, None, 1.49073, None, 0.00947154, None, 1.49073, None, 0.00947154, None)

reports.append(Report(604030080, ("CSC", 1, 4, 2, 16), "MEp42_16"))
reports[-1].posNum = 75784
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0092676, 0.00631515, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.00010544, 6.51663e-05, 0), \
                           -137292, 75784, 75784, -nan)
reports[-1].sigmaresid = ValErr(1.48095, 0.00380396, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0051745, None, -0.00326019, None, -0.00391438, None, -0.00332821, None, -0.00391438, None, -0.00332821, None, -0.000592739, None, -0.0034281, None, -0.000592739, None, -0.0034281, None, 1.48098, None, 0.00805229, None, 1.48098, None, 0.00805229, None)

reports.append(Report(604030096, ("CSC", 1, 4, 2, 18), "MEp42_18"))
reports[-1].posNum = 56840
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00369958, 0.00729591, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(9.9276e-05, 7.69664e-05, 0), \
                           -102694, 56840, 56840, -nan)
reports[-1].sigmaresid = ValErr(1.4737, 0.00437085, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00186115, None, -0.00190938, None, 0.0013001, None, -0.00198486, None, 0.0013001, None, -0.00198486, None, -0.000758506, None, -0.00209761, None, -0.000758506, None, -0.00209761, None, 1.47372, None, 0.00839892, None, 1.47372, None, 0.00839892, None)

reports.append(Report(604030112, ("CSC", 1, 4, 2, 20), "MEp42_20"))
reports[-1].posNum = 69542
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.010264, 0.00657889, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000144129, 6.56503e-05, 0), \
                           -126141, 69542, 69542, -nan)
reports[-1].sigmaresid = ValErr(1.4843, 0.00398001, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00459319, None, 0.00266388, None, -0.00278647, None, 0.00232808, None, -0.00278647, None, 0.00232808, None, -0.00182831, None, 0.00241586, None, -0.00182831, None, 0.00241586, None, 1.48435, None, 0.0105839, None, 1.48435, None, 0.0105839, None)

reports.append(Report(604030128, ("CSC", 1, 4, 2, 22), "MEp42_22"))
reports[-1].posNum = 71826
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000111879, 0.00654423, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.58287e-06, 6.69798e-05, 0), \
                           -129878, 71826, 71826, -nan)
reports[-1].sigmaresid = ValErr(1.47595, 0.0038942, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00105325, None, -0.00223433, None, 0.000197686, None, -0.00225242, None, 0.000197686, None, -0.00225242, None, 0.00829694, None, -0.00234257, None, 0.00829694, None, -0.00234257, None, 1.47594, None, 0.00800875, None, 1.47594, None, 0.00800875, None)

reports.append(Report(604030144, ("CSC", 1, 4, 2, 24), "MEp42_24"))
reports[-1].posNum = 79136
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000405474, 0.00601021, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.6801e-07, 6.24686e-05, 0), \
                           -144068, 79136, 79136, -nan)
reports[-1].sigmaresid = ValErr(1.49418, 0.00375579, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000598343, None, -0.00139876, None, -0.000443649, None, -0.0015543, None, -0.000443649, None, -0.0015543, None, -0.000781183, None, -0.00161651, None, -0.000781183, None, -0.00161651, None, 1.49417, None, 0.00882281, None, 1.49417, None, 0.00882281, None)

reports.append(Report(604030160, ("CSC", 1, 4, 2, 26), "MEp42_26"))
reports[-1].posNum = 66272
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00169059, 0.0072235, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.97317e-05, 7.35131e-05, 0), \
                           -117777, 66272, 66272, -nan)
reports[-1].sigmaresid = ValErr(1.4308, 0.00393007, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00881645, None, 0.000502522, None, -0.00143072, None, 0.000416915, None, -0.00143072, None, 0.000416915, None, -0.00248864, None, 0.000417175, None, -0.00248864, None, 0.000417175, None, 1.43081, None, 0.00858759, None, 1.43081, None, 0.00858759, None)

reports.append(Report(604030176, ("CSC", 1, 4, 2, 28), "MEp42_28"))
reports[-1].posNum = 77860
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00587024, 0.00608482, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.53802e-05, 6.40139e-05, 0), \
                           -142637, 77860, 77860, -nan)
reports[-1].sigmaresid = ValErr(1.5114, 0.00383007, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00172356, None, -0.000692167, None, 0.00173938, None, -0.00075294, None, 0.00173938, None, -0.00075294, None, 0.00323357, None, -0.000805365, None, 0.00323357, None, -0.000805365, None, 1.51142, None, 0.00845153, None, 1.51142, None, 0.00845153, None)

reports.append(Report(604030192, ("CSC", 1, 4, 2, 30), "MEp42_30"))
reports[-1].posNum = 63088
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0254836, 0.00742588, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000272907, 7.47395e-05, 0), \
                           -111678, 63088, 63088, -nan)
reports[-1].sigmaresid = ValErr(1.42086, 0.00400001, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00497529, None, 0.00100161, None, 0.00791303, None, 0.000908162, None, 0.00791303, None, 0.000908162, None, 0.00205907, None, 0.000915582, None, 0.00205907, None, 0.000915582, None, 1.42101, None, 0.00807628, None, 1.42101, None, 0.00807628, None)

reports.append(Report(604030208, ("CSC", 1, 4, 2, 32), "MEp42_32"))
reports[-1].posNum = 60468
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000516488, 0.00694697, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.73807e-05, 7.34894e-05, 0), \
                           -109755, 60468, 60468, -nan)
reports[-1].sigmaresid = ValErr(1.4861, 0.00427337, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00259844, None, -0.00150957, None, -0.0027264, None, -0.00162789, None, -0.0027264, None, -0.00162789, None, 0.00281552, None, -0.00161043, None, 0.00281552, None, -0.00161043, None, 1.48611, None, 0.00859062, None, 1.48611, None, 0.00859062, None)

reports.append(Report(604030224, ("CSC", 1, 4, 2, 34), "MEp42_34"))
reports[-1].posNum = 47834
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00971144, 0.00858738, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000145043, 8.46684e-05, 0), \
                           -87558.7, 47834, 47834, -nan)
reports[-1].sigmaresid = ValErr(1.50913, 0.00487912, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00862378, None, -9.03102e-05, None, 0.000953592, None, -0.000189412, None, 0.000953592, None, -0.000189412, None, 0.00612686, None, -0.000220735, None, 0.00612686, None, -0.000220735, None, 1.50917, None, 0.00867015, None, 1.50917, None, 0.00867015, None)

reports.append(Report(604030240, ("CSC", 1, 4, 2, 36), "MEp42_36"))
reports[-1].posNum = 49888
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00313, 0.0078979, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.88756e-05, 7.89459e-05, 0), \
                           -89863.8, 49888, 49888, -nan)
reports[-1].sigmaresid = ValErr(1.46576, 0.00464032, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00382109, None, -0.00058054, None, -0.00152236, None, -0.000751966, None, -0.00152236, None, -0.000751966, None, -0.0119537, None, -0.000812747, None, -0.0119537, None, -0.000812747, None, 1.46576, None, 0.00846667, None, 1.46576, None, 0.00846667, None)

reports.append(Report(604050440, ("CSC", 2, 1, 1, 1), "MEm11_01"))
reports[-1].posNum = 118028
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000178316, 0.000764336, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.47571e-05, 1.9125e-05, 0), \
                           -9585.22, 118028, 118028, -nan)
reports[-1].sigmaresid = ValErr(0.262441, 0.000540163, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000325231, None, 0.000856136, None, 0.00014513, None, 0.000811622, None, 0.00014513, None, 0.000811622, None, -0.000269147, None, 0.000776733, None, -0.000269147, None, 0.000776733, None, 0.262443, None, 0.00534729, None, 0.262443, None, 0.00534729, None)

reports.append(Report(604050456, ("CSC", 2, 1, 1, 3), "MEm11_03"))
reports[-1].posNum = 120750
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000238496, 0.00126558, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.407e-08, 2.41161e-05, 0), \
                           -8602.13, 120750, 120750, -nan)
reports[-1].sigmaresid = ValErr(0.259837, 0.00052926, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000607642, None, 0.000492416, None, -0.000237752, None, 0.000491169, None, -0.000237752, None, 0.000491169, None, 0.000992797, None, 0.000474291, None, 0.000992797, None, 0.000474291, None, 0.259837, None, 0.00543467, None, 0.259837, None, 0.00543467, None)

reports.append(Report(604050472, ("CSC", 2, 1, 1, 5), "MEm11_05"))
reports[-1].posNum = 94094
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000818843, 0.000844176, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.30474e-05, 2.15854e-05, 0), \
                           -5039.64, 94094, 94094, -nan)
reports[-1].sigmaresid = ValErr(0.255284, 0.000588474, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000622498, None, 0.000341753, None, 0.000667734, None, 0.000353894, None, 0.000667734, None, 0.000353894, None, 0.000402574, None, 0.000354548, None, 0.000402574, None, 0.000354548, None, 0.255285, None, 0.00509826, None, 0.255285, None, 0.00509826, None)

reports.append(Report(604050488, ("CSC", 2, 1, 1, 7), "MEm11_07"))
reports[-1].posNum = 95254
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000164985, 0.000907269, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.84185e-06, 2.36248e-05, 0), \
                           -12999.3, 95254, 95254, -nan)
reports[-1].sigmaresid = ValErr(0.277351, 0.000635434, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000362661, None, 0.00986175, None, 0.000154814, None, 0.00945904, None, 0.000154814, None, 0.00945904, None, -0.000289987, None, 0.00964812, None, -0.000289987, None, 0.00964812, None, 0.277352, None, 0.00529856, None, 0.277352, None, 0.00529856, None)

reports.append(Report(604050504, ("CSC", 2, 1, 1, 9), "MEm11_09"))
reports[-1].posNum = 113414
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000108175, 0.000783899, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.13076e-05, 1.96458e-05, 0), \
                           -9879.2, 113414, 113414, -nan)
reports[-1].sigmaresid = ValErr(0.263993, 0.0005543, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000640582, None, -0.000378534, None, -0.000106927, None, -0.00040469, None, -0.000106927, None, -0.00040469, None, -0.0003944, None, -0.000421433, None, -0.0003944, None, -0.000421433, None, 0.263995, None, 0.00502804, None, 0.263995, None, 0.00502804, None)

reports.append(Report(604050520, ("CSC", 2, 1, 1, 11), "MEm11_11"))
reports[-1].posNum = 114592
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00102936, 0.000776407, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.01766e-05, 1.91113e-05, 0), \
                           -9225.87, 114592, 114592, -nan)
reports[-1].sigmaresid = ValErr(0.262258, 0.000547818, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(9.33167e-05, None, 0.00124382, None, -0.000975392, None, 0.00121502, None, -0.000975392, None, 0.00121502, None, -0.00130786, None, 0.00122929, None, -0.00130786, None, 0.00122929, None, 0.262259, None, 0.00554023, None, 0.262259, None, 0.00554023, None)

reports.append(Report(604050536, ("CSC", 2, 1, 1, 13), "MEm11_13"))
reports[-1].posNum = 115366
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000181969, 0.000774413, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.77625e-05, 1.92443e-05, 0), \
                           -9606.37, 115366, 115366, -nan)
reports[-1].sigmaresid = ValErr(0.262982, 0.000547485, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00143847, None, -0.000681881, None, 0.000167763, None, -0.000661393, None, 0.000167763, None, -0.000661393, None, 0.00164669, None, -0.00069618, None, 0.00164669, None, -0.00069618, None, 0.262983, None, 0.00475721, None, 0.262983, None, 0.00475721, None)

reports.append(Report(604050552, ("CSC", 2, 1, 1, 15), "MEm11_15"))
reports[-1].posNum = 116406
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-7.6495e-05, 0.000787148, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.9416e-06, 1.93389e-05, 0), \
                           -12083.6, 116406, 116406, -nan)
reports[-1].sigmaresid = ValErr(0.268439, 0.000556342, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000233217, None, 0.000762147, None, -8.00565e-05, None, 0.000633889, None, -8.00565e-05, None, 0.000633889, None, -0.00186804, None, 0.000704048, None, -0.00186804, None, 0.000704048, None, 0.268439, None, 0.00597974, None, 0.268439, None, 0.00597974, None)

reports.append(Report(604050568, ("CSC", 2, 1, 1, 17), "MEm11_17"))
reports[-1].posNum = 117978
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00011685, 0.00076796, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.79314e-05, 1.86848e-05, 0), \
                           -9937.39, 117978, 117978, -nan)
reports[-1].sigmaresid = ValErr(0.263234, 0.000541908, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000406217, None, -0.000452185, None, 4.34177e-05, None, -0.000459803, None, 4.34177e-05, None, -0.000459803, None, -0.00205357, None, -0.000467764, None, -0.00205357, None, -0.000467764, None, 0.263238, None, 0.00471338, None, 0.263238, None, 0.00471338, None)

reports.append(Report(604050584, ("CSC", 2, 1, 1, 19), "MEm11_19"))
reports[-1].posNum = 104086
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0003275, 0.000830527, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.81202e-05, 2.08219e-05, 0), \
                           -10569.7, 104086, 104086, -nan)
reports[-1].sigmaresid = ValErr(0.267832, 0.000587015, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000395085, None, -4.6822e-06, None, 0.000348345, None, 8.46324e-05, None, 0.000348345, None, 8.46324e-05, None, 0.000633101, None, 6.96008e-05, None, 0.000633101, None, 6.96008e-05, None, 0.267834, None, 0.00570171, None, 0.267834, None, 0.00570171, None)

reports.append(Report(604050600, ("CSC", 2, 1, 1, 21), "MEm11_21"))
reports[-1].posNum = 105336
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00044016, 0.000836121, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(7.54059e-06, 2.13456e-05, 0), \
                           -11659.8, 105336, 105336, -nan)
reports[-1].sigmaresid = ValErr(0.270293, 0.000588887, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00166688, None, 0.00046566, None, -0.000466422, None, 0.000348799, None, -0.000466422, None, 0.000348799, None, -0.00201452, None, 0.000401897, None, -0.00201452, None, 0.000401897, None, 0.270294, None, 0.00508532, None, 0.270294, None, 0.00508532, None)

reports.append(Report(604050616, ("CSC", 2, 1, 1, 23), "MEm11_23"))
reports[-1].posNum = 110232
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00027433, 0.000794905, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.9515e-05, 2.013e-05, 0), \
                           -9472.71, 110232, 110232, -nan)
reports[-1].sigmaresid = ValErr(0.263684, 0.000561584, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00103042, None, -0.000808078, None, -0.000241883, None, -0.000760505, None, -0.000241883, None, -0.000760505, None, -0.00338888, None, -0.000776973, None, -0.00338888, None, -0.000776973, None, 0.263685, None, 0.0051704, None, 0.263685, None, 0.0051704, None)

reports.append(Report(604050632, ("CSC", 2, 1, 1, 25), "MEm11_25"))
reports[-1].posNum = 85952
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000386753, 0.000915429, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.53639e-06, 2.32937e-05, 0), \
                           -8808.82, 85952, 85952, -nan)
reports[-1].sigmaresid = ValErr(0.268084, 0.000646589, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000323579, None, -0.00100976, None, -0.000396027, None, -0.000960928, None, -0.000396027, None, -0.000960928, None, 0.000282841, None, -0.000929604, None, 0.000282841, None, -0.000929604, None, 0.268085, None, 0.00552273, None, 0.268085, None, 0.00552273, None)

reports.append(Report(604050648, ("CSC", 2, 1, 1, 27), "MEm11_27"))
reports[-1].posNum = 114532
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000373075, 0.00077869, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(7.98338e-07, 1.96706e-05, 0), \
                           -9732.9, 114532, 114532, -nan)
reports[-1].sigmaresid = ValErr(0.263432, 0.000550415, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00116598, None, -0.000392946, None, 0.000373929, None, -0.000342327, None, 0.000373929, None, -0.000342327, None, 0.000602746, None, -0.00034824, None, 0.000602746, None, -0.00034824, None, 0.263432, None, 0.00545539, None, 0.263432, None, 0.00545539, None)

reports.append(Report(604050664, ("CSC", 2, 1, 1, 29), "MEm11_29"))
reports[-1].posNum = 123540
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000166614, 0.000747963, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.60865e-05, 1.90509e-05, 0), \
                           -10104, 123540, 123540, -nan)
reports[-1].sigmaresid = ValErr(0.262593, 0.000528279, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00166541, None, 5.06213e-05, None, -0.000136292, None, 1.46412e-05, None, -0.000136292, None, 1.46412e-05, None, 0.000150534, None, 3.63721e-05, None, 0.000150534, None, 3.63721e-05, None, 0.262593, None, 0.00477622, None, 0.262593, None, 0.00477622, None)

reports.append(Report(604050680, ("CSC", 2, 1, 1, 31), "MEm11_31"))
reports[-1].posNum = 118692
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00024578, 0.000758174, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(8.07967e-06, 1.89032e-05, 0), \
                           -8843.58, 118692, 118692, -nan)
reports[-1].sigmaresid = ValErr(0.260688, 0.000535052, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00141953, None, -0.000558346, None, -0.000225429, None, -0.000565427, None, -0.000225429, None, -0.000565427, None, -0.000406767, None, -0.000552049, None, -0.000406767, None, -0.000552049, None, 0.260688, None, 0.00486616, None, 0.260688, None, 0.00486616, None)

reports.append(Report(604050696, ("CSC", 2, 1, 1, 33), "MEm11_33"))
reports[-1].posNum = 116600
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000630976, 0.000765274, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.08924e-05, 1.91997e-05, 0), \
                           -8905.7, 116600, 116600, -nan)
reports[-1].sigmaresid = ValErr(0.261176, 0.00054084, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000314214, None, -0.000433215, None, 0.000603932, None, -0.000453381, None, 0.000603932, None, -0.000453381, None, -7.57259e-05, None, -0.000394668, None, -7.57259e-05, None, -0.000394668, None, 0.261177, None, 0.00498176, None, 0.261177, None, 0.00498176, None)

reports.append(Report(604050712, ("CSC", 2, 1, 1, 35), "MEm11_35"))
reports[-1].posNum = 117662
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000851015, 0.000768516, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.46432e-06, 1.86778e-05, 0), \
                           -9653.09, 117662, 117662, -nan)
reports[-1].sigmaresid = ValErr(0.262659, 0.000541452, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000213763, None, -0.000700015, None, 0.000831896, None, -0.000694144, None, 0.000831896, None, -0.000694144, None, 0.00206781, None, -0.000715496, None, 0.00206781, None, -0.000715496, None, 0.262659, None, 0.00525766, None, 0.262659, None, 0.00525766, None)

reports.append(Report(604050448, ("CSC", 2, 1, 1, 2), "MEm11_02"))
reports[-1].posNum = 127456
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(4.20858e-06, 0.000669018, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.69908e-06, 1.61323e-05, 0), \
                           2269.51, 127456, 127456, -nan)
reports[-1].sigmaresid = ValErr(0.2377, 0.000470798, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000385012, None, 0.000316896, None, -6.74415e-06, None, 0.000348007, None, -6.74415e-06, None, 0.000348007, None, 0.00143536, None, 0.000348366, None, 0.00143536, None, 0.000348366, None, 0.2377, None, 0.00538234, None, 0.2377, None, 0.00538234, None)

reports.append(Report(604050464, ("CSC", 2, 1, 1, 4), "MEm11_04"))
reports[-1].posNum = 126046
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000261459, 0.000667881, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.45285e-06, 1.59269e-05, 0), \
                           3433.04, 126046, 126046, -nan)
reports[-1].sigmaresid = ValErr(0.235469, 0.00046898, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000440341, None, 0.000557087, None, 0.000229609, None, 0.000569325, None, 0.000229609, None, 0.000569325, None, 0.00148622, None, 0.000597256, None, 0.00148622, None, 0.000597256, None, 0.235469, None, 0.00537008, None, 0.235469, None, 0.00537008, None)

reports.append(Report(604050480, ("CSC", 2, 1, 1, 6), "MEm11_06"))
reports[-1].posNum = 107562
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000505287, 0.000720254, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.75031e-05, 1.69724e-05, 0), \
                           3836.99, 107562, 107562, -nan)
reports[-1].sigmaresid = ValErr(0.233491, 0.000503415, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00133735, None, 0.000307495, None, 0.000392724, None, 0.000244793, None, 0.000392724, None, 0.000244793, None, -0.0016227, None, 0.00029133, None, -0.0016227, None, 0.00029133, None, 0.233492, None, 0.00527296, None, 0.233492, None, 0.00527296, None)

reports.append(Report(604050496, ("CSC", 2, 1, 1, 8), "MEm11_08"))
reports[-1].posNum = 122006
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000217776, 0.000671539, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.19105e-05, 1.58074e-05, 0), \
                           5044.19, 122006, 122006, -nan)
reports[-1].sigmaresid = ValErr(0.232171, 0.000470004, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000272818, None, -0.000502066, None, -0.00028988, None, -0.000527938, None, -0.00028988, None, -0.000527938, None, 0.000257114, None, -0.000520806, None, 0.000257114, None, -0.000520806, None, 0.232171, None, 0.00562385, None, 0.232171, None, 0.00562385, None)

reports.append(Report(604050512, ("CSC", 2, 1, 1, 10), "MEm11_10"))
reports[-1].posNum = 124476
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-8.4747e-05, 0.000670297, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.53283e-06, 1.61532e-05, 0), \
                           3670.94, 124476, 124476, -nan)
reports[-1].sigmaresid = ValErr(0.234939, 0.000470866, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000648736, None, -0.000624268, None, -6.79872e-05, None, -0.000635848, None, -6.79872e-05, None, -0.000635848, None, -0.00200017, None, -0.000628459, None, -0.00200017, None, -0.000628459, None, 0.234939, None, 0.00532593, None, 0.234939, None, 0.00532593, None)

reports.append(Report(604050528, ("CSC", 2, 1, 1, 12), "MEm11_12"))
reports[-1].posNum = 125256
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000111304, 0.000662289, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.02862e-06, 1.55273e-05, 0), \
                           5109.76, 125256, 125256, -nan)
reports[-1].sigmaresid = ValErr(0.232298, 0.000464122, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(1.3764e-08, None, -0.000298311, None, -8.83756e-05, None, -0.000236895, None, -8.83756e-05, None, -0.000236895, None, -0.000928987, None, -0.000247821, None, -0.000928987, None, -0.000247821, None, 0.232298, None, 0.0052013, None, 0.232298, None, 0.0052013, None)

reports.append(Report(604050544, ("CSC", 2, 1, 1, 14), "MEm11_14"))
reports[-1].posNum = 124128
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000824126, 0.000444659, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.83141e-06, 1.07129e-05, 0), \
                           2646.35, 124128, 124128, -nan)
reports[-1].sigmaresid = ValErr(0.236867, 0.000473075, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000674073, None, -0.000683743, None, 0.000806183, None, -0.00073722, None, 0.000806183, None, -0.00073722, None, -0.000497917, None, -0.000782321, None, -0.000497917, None, -0.000782321, None, 0.236867, None, 0.00534952, None, 0.236867, None, 0.00534952, None)

reports.append(Report(604050560, ("CSC", 2, 1, 1, 16), "MEm11_16"))
reports[-1].posNum = 127278
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000824348, 0.000672094, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.75145e-05, 1.58623e-05, 0), \
                           1779.75, 127278, 127278, -nan)
reports[-1].sigmaresid = ValErr(0.238611, 0.000472932, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00110001, None, -0.000476978, None, 0.000751241, None, -0.000406902, None, 0.000751241, None, -0.000406902, None, -0.000390688, None, -0.000468954, None, -0.000390688, None, -0.000468954, None, 0.238612, None, 0.00501492, None, 0.238612, None, 0.00501492, None)

reports.append(Report(604050576, ("CSC", 2, 1, 1, 18), "MEm11_18"))
reports[-1].posNum = 117304
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000441934, 0.000695659, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.35938e-06, 1.65261e-05, 0), \
                           2323.44, 117304, 117304, -nan)
reports[-1].sigmaresid = ValErr(0.237225, 0.000489767, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000814824, None, -0.00070416, None, -0.00044729, None, -0.000666781, None, -0.00044729, None, -0.000666781, None, -0.00183814, None, -0.000739194, None, -0.00183814, None, -0.000739194, None, 0.237225, None, 0.00529186, None, 0.237225, None, 0.00529186, None)

reports.append(Report(604050592, ("CSC", 2, 1, 1, 20), "MEm11_20"))
reports[-1].posNum = 119506
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000246384, 0.000687861, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.43102e-06, 1.6591e-05, 0), \
                           2547.73, 119506, 119506, -nan)
reports[-1].sigmaresid = ValErr(0.236867, 0.000484501, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000207935, None, -0.000141116, None, 0.000211941, None, -0.00017857, None, 0.000211941, None, -0.00017857, None, 0.00229389, None, -0.000195226, None, 0.00229389, None, -0.000195226, None, 0.236867, None, 0.00521351, None, 0.236867, None, 0.00521351, None)

reports.append(Report(604050608, ("CSC", 2, 1, 1, 22), "MEm11_22"))
reports[-1].posNum = 123540
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000640418, 0.000673608, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.62264e-05, 1.62208e-05, 0), \
                           3408.36, 123540, 123540, -nan)
reports[-1].sigmaresid = ValErr(0.235386, 0.000473546, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00125068, None, -0.000637848, None, -0.000523197, None, -0.000648181, None, -0.000523197, None, -0.000648181, None, -0.00154567, None, -0.000661789, None, -0.00154567, None, -0.000661789, None, 0.235389, None, 0.00585148, None, 0.235389, None, 0.00585148, None)

reports.append(Report(604050624, ("CSC", 2, 1, 1, 24), "MEm11_24"))
reports[-1].posNum = 122402
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000768332, 0.000683543, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.48158e-05, 1.65943e-05, 0), \
                           1893.54, 122402, 122402, -nan)
reports[-1].sigmaresid = ValErr(0.238256, 0.000481543, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000174832, None, -0.00119461, None, -0.000680315, None, -0.00118151, None, -0.000680315, None, -0.00118151, None, -0.00076462, None, -0.00126628, None, -0.00076462, None, -0.00126628, None, 0.238258, None, 0.00513761, None, 0.238258, None, 0.00513761, None)

reports.append(Report(604050640, ("CSC", 2, 1, 1, 26), "MEm11_26"))
reports[-1].posNum = 99532
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000420258, 0.000785267, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(8.78358e-06, 1.98764e-05, 0), \
                           -1871.05, 99532, 99532, -nan)
reports[-1].sigmaresid = ValErr(0.246562, 0.000552625, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000519036, None, -0.00737682, None, 0.000386037, None, -0.00708414, None, 0.000386037, None, -0.00708414, None, -0.000403835, None, -0.00739558, None, -0.000403835, None, -0.00739558, None, 0.246563, None, 0.00574305, None, 0.246563, None, 0.00574305, None)

reports.append(Report(604050656, ("CSC", 2, 1, 1, 28), "MEm11_28"))
reports[-1].posNum = 125022
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000121209, 0.000671149, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.00881e-05, 1.62663e-05, 0), \
                           3104.17, 125022, 125022, -nan)
reports[-1].sigmaresid = ValErr(0.236038, 0.000472036, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00066383, None, -0.000345497, None, -3.54755e-05, None, -0.000419195, None, -3.54755e-05, None, -0.000419195, None, -0.000785107, None, -0.000400508, None, -0.000785107, None, -0.000400508, None, 0.236038, None, 0.00582678, None, 0.236038, None, 0.00582678, None)

reports.append(Report(604050672, ("CSC", 2, 1, 1, 30), "MEm11_30"))
reports[-1].posNum = 128392
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000480536, 0.000657227, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.02313e-06, 1.57582e-05, 0), \
                           4165.3, 128392, 128392, -nan)
reports[-1].sigmaresid = ValErr(0.234247, 0.000462263, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000721064, None, -0.00266111, None, 0.000463274, None, -0.00258415, None, 0.000463274, None, -0.00258415, None, 0.000162889, None, -0.002642, None, 0.000162889, None, -0.002642, None, 0.234247, None, 0.00546825, None, 0.234247, None, 0.00546825, None)

reports.append(Report(604050688, ("CSC", 2, 1, 1, 32), "MEm11_32"))
reports[-1].posNum = 125010
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000143112, 0.000671428, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.97103e-06, 1.62248e-05, 0), \
                           2945.88, 125010, 125010, -nan)
reports[-1].sigmaresid = ValErr(0.236335, 0.000472651, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00102616, None, -0.000542889, None, -0.000162494, None, -0.000571752, None, -0.000162494, None, -0.000571752, None, -0.000408332, None, -0.000577884, None, -0.000408332, None, -0.000577884, None, 0.236335, None, 0.00519903, None, 0.236335, None, 0.00519903, None)

reports.append(Report(604050704, ("CSC", 2, 1, 1, 34), "MEm11_34"))
reports[-1].posNum = 126998
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000232714, 0.000662566, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.40549e-06, 1.58652e-05, 0), \
                           4221.8, 126998, 126998, -nan)
reports[-1].sigmaresid = ValErr(0.234059, 0.000464421, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00180452, None, 0.00107007, None, -0.000219479, None, 0.000977572, None, -0.000219479, None, 0.000977572, None, -0.00253755, None, 0.000998456, None, -0.00253755, None, 0.000998456, None, 0.234059, None, 0.00556206, None, 0.234059, None, 0.00556206, None)

reports.append(Report(604050720, ("CSC", 2, 1, 1, 36), "MEm11_36"))
reports[-1].posNum = 128190
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000297344, 0.000659934, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(8.03921e-06, 1.5817e-05, 0), \
                           3788.28, 128190, 128190, -nan)
reports[-1].sigmaresid = ValErr(0.234925, 0.000463968, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00135105, None, 0.000121638, None, -0.000261913, None, 9.84765e-05, None, -0.000261913, None, 9.84765e-05, None, 2.56065e-05, None, 0.000105476, None, 2.56065e-05, None, 0.000105476, None, 0.234925, None, 0.00528915, None, 0.234925, None, 0.00528915, None)

reports.append(Report(604050952, ("CSC", 2, 1, 2, 1), "MEm12_01"))
reports[-1].posNum = 69220
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00469768, 0.00309901, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000138777, 6.22616e-05, 0), \
                           -77476.3, 69220, 69220, -nan)
reports[-1].sigmaresid = ValErr(0.741068, 0.00199172, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00152126, None, -0.000367834, None, 0.00181627, None, -0.000490346, None, 0.00181627, None, -0.000490346, None, 0.000465571, None, -0.00055518, None, 0.000465571, None, -0.00055518, None, 0.741095, None, 0.00600661, None, 0.741095, None, 0.00600661, None)

reports.append(Report(604050968, ("CSC", 2, 1, 2, 3), "MEm12_03"))
reports[-1].posNum = 66038
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00291445, 0.00325306, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.19626e-05, 6.45243e-05, 0), \
                           -72440.4, 66038, 66038, -nan)
reports[-1].sigmaresid = ValErr(0.724706, 0.00199411, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00144036, None, -7.93601e-05, None, 0.00135727, None, -0.000135395, None, 0.00135727, None, -0.000135395, None, 0.00427215, None, -0.000224409, None, 0.00427215, None, -0.000224409, None, 0.724711, None, 0.00605651, None, 0.724711, None, 0.00605651, None)

reports.append(Report(604050984, ("CSC", 2, 1, 2, 5), "MEm12_05"))
reports[-1].posNum = 64028
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00180936, 0.00334236, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.81132e-06, 6.67998e-05, 0), \
                           -69410.7, 64028, 64028, -nan)
reports[-1].sigmaresid = ValErr(0.715431, 0.00199926, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000948846, None, -0.00168995, None, 0.00193857, None, -0.00175439, None, 0.00193857, None, -0.00175439, None, 0.00491216, None, -0.00180849, None, 0.00491216, None, -0.00180849, None, 0.715431, None, 0.0058548, None, 0.715431, None, 0.0058548, None)

reports.append(Report(604051000, ("CSC", 2, 1, 2, 7), "MEm12_07"))
reports[-1].posNum = 65072
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00079211, 0.00333161, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.46682e-05, 6.67798e-05, 0), \
                           -71424.3, 65072, 65072, -nan)
reports[-1].sigmaresid = ValErr(0.725192, 0.00201021, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00206872, None, -0.000620794, None, 0.0011741, None, -0.000795736, None, 0.0011741, None, -0.000795736, None, -0.000706139, None, -0.000797615, None, -0.000706139, None, -0.000797615, None, 0.725192, None, 0.0058735, None, 0.725192, None, 0.0058735, None)

reports.append(Report(604051016, ("CSC", 2, 1, 2, 9), "MEm12_09"))
reports[-1].posNum = 65236
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00178183, 0.00325574, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.3113e-05, 6.42855e-05, 0), \
                           -72276.1, 65236, 65236, -nan)
reports[-1].sigmaresid = ValErr(0.732695, 0.00202844, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00129513, None, -0.000300874, None, 0.000985437, None, -0.000394273, None, 0.000985437, None, -0.000394273, None, 0.00617377, None, -0.000446466, None, 0.00617377, None, -0.000446466, None, 0.732699, None, 0.00635878, None, 0.732699, None, 0.00635878, None)

reports.append(Report(604051032, ("CSC", 2, 1, 2, 11), "MEm12_11"))
reports[-1].posNum = 64180
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00369456, 0.00333548, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(8.18487e-05, 6.48836e-05, 0), \
                           -71585.8, 64180, 64180, -nan)
reports[-1].sigmaresid = ValErr(0.738195, 0.00206042, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000816629, None, 0.000392398, None, -0.00164653, None, 0.000204945, None, -0.00164653, None, 0.000204945, None, -0.00195275, None, 0.000231843, None, -0.00195275, None, 0.000231843, None, 0.738204, None, 0.00593289, None, 0.738204, None, 0.00593289, None)

reports.append(Report(604051048, ("CSC", 2, 1, 2, 13), "MEm12_13"))
reports[-1].posNum = 61384
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00160086, 0.00344957, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000101345, 6.85453e-05, 0), \
                           -67409.8, 61384, 61384, -nan)
reports[-1].sigmaresid = ValErr(0.725588, 0.00207084, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0030743, None, -0.000523181, None, -0.00109487, None, -0.000647439, None, -0.00109487, None, -0.000647439, None, -0.00535189, None, -0.000681168, None, -0.00535189, None, -0.000681168, None, 0.7256, None, 0.00598384, None, 0.7256, None, 0.00598384, None)

reports.append(Report(604051064, ("CSC", 2, 1, 2, 15), "MEm12_15"))
reports[-1].posNum = 67304
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000331599, 0.00329521, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(7.56574e-06, 6.51059e-05, 0), \
                           -74857.1, 67304, 67304, -nan)
reports[-1].sigmaresid = ValErr(0.735864, 0.00200569, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00153376, None, -0.000409143, None, -0.00014192, None, -0.000447463, None, -0.00014192, None, -0.000447463, None, 0.00198302, None, -0.000514114, None, 0.00198302, None, -0.000514114, None, 0.735861, None, 0.00609702, None, 0.735861, None, 0.00609702, None)

reports.append(Report(604051080, ("CSC", 2, 1, 2, 17), "MEm12_17"))
reports[-1].posNum = 51752
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00384496, 0.00391703, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(9.66361e-05, 7.57933e-05, 0), \
                           -55894.8, 51752, 51752, -nan)
reports[-1].sigmaresid = ValErr(0.712563, 0.00221485, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00204248, None, 0.000171513, None, -0.000846222, None, 5.96851e-05, None, -0.000846222, None, 5.96851e-05, None, 0.00386129, None, 5.87216e-05, None, 0.00386129, None, 5.87216e-05, None, 0.712574, None, 0.00622383, None, 0.712574, None, 0.00622383, None)

reports.append(Report(604051096, ("CSC", 2, 1, 2, 19), "MEm12_19"))
reports[-1].posNum = 69132
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00313925, 0.00310846, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(7.10021e-05, 6.26312e-05, 0), \
                           -77123.1, 69132, 69132, -nan)
reports[-1].sigmaresid = ValErr(0.738343, 0.00198565, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00685762, None, -0.000144578, None, -0.00162759, None, -0.000349961, None, -0.00162759, None, -0.000349961, None, -0.000119834, None, -0.000365649, None, -0.000119834, None, -0.000365649, None, 0.73835, None, 0.00606492, None, 0.73835, None, 0.00606492, None)

reports.append(Report(604051112, ("CSC", 2, 1, 2, 21), "MEm12_21"))
reports[-1].posNum = 64528
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00406222, 0.00331292, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000143259, 6.59583e-05, 0), \
                           -70724.2, 64528, 64528, -nan)
reports[-1].sigmaresid = ValErr(0.724036, 0.00201544, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00144724, None, -0.000682926, None, -0.000394285, None, -0.000818006, None, -0.000394285, None, -0.000818006, None, 0.00143611, None, -0.000805233, None, 0.00143611, None, -0.000805233, None, 0.724062, None, 0.00607748, None, 0.724062, None, 0.00607748, None)

reports.append(Report(604051128, ("CSC", 2, 1, 2, 23), "MEm12_23"))
reports[-1].posNum = 67676
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00223235, 0.00310497, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.81196e-05, 6.20167e-05, 0), \
                           -75362.7, 67676, 67676, -nan)
reports[-1].sigmaresid = ValErr(0.736859, 0.00200287, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0021277, None, -0.000662834, None, -0.00103966, None, -0.000759116, None, -0.00103966, None, -0.000759116, None, 0.00214666, None, -0.000783273, None, 0.00214666, None, -0.000783273, None, 0.736864, None, 0.00619906, None, 0.736864, None, 0.00619906, None)

reports.append(Report(604051144, ("CSC", 2, 1, 2, 25), "MEm12_25"))
reports[-1].posNum = 55856
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00444431, 0.00375742, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.20954e-05, 7.14508e-05, 0), \
                           -59273.2, 55856, 55856, -nan)
reports[-1].sigmaresid = ValErr(0.699241, 0.00209207, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00090489, None, -0.000548446, None, 0.00178302, None, -0.000752388, None, 0.00178302, None, -0.000752388, None, 0.00365031, None, -0.000694159, None, 0.00365031, None, -0.000694159, None, 0.699249, None, 0.00621962, None, 0.699249, None, 0.00621962, None)

reports.append(Report(604051160, ("CSC", 2, 1, 2, 27), "MEm12_27"))
reports[-1].posNum = 52364
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000625565, 0.00385459, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.15708e-05, 7.30845e-05, 0), \
                           -54832.5, 52364, 52364, -nan)
reports[-1].sigmaresid = ValErr(0.689494, 0.00213058, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00370584, None, -0.00108799, None, 8.38116e-05, None, -0.00112833, None, 8.38116e-05, None, -0.00112833, None, 0.00777388, None, -0.00117191, None, 0.00777388, None, -0.00117191, None, 0.689494, None, 0.00604378, None, 0.689494, None, 0.00604378, None)

reports.append(Report(604051176, ("CSC", 2, 1, 2, 29), "MEm12_29"))
reports[-1].posNum = 55276
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000237934, 0.00375817, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.80353e-06, 7.0979e-05, 0), \
                           -58717.7, 55276, 55276, -nan)
reports[-1].sigmaresid = ValErr(0.700001, 0.00210531, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00186792, None, -0.00119537, None, -4.65034e-05, None, -0.0012424, None, -4.65034e-05, None, -0.0012424, None, 0.00425295, None, -0.00130901, None, 0.00425295, None, -0.00130901, None, 0.700001, None, 0.0059843, None, 0.700001, None, 0.0059843, None)

reports.append(Report(604051192, ("CSC", 2, 1, 2, 31), "MEm12_31"))
reports[-1].posNum = 50846
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00526843, 0.00390825, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00012314, 7.32041e-05, 0), \
                           -53388.2, 50846, 50846, -nan)
reports[-1].sigmaresid = ValErr(0.691465, 0.00216833, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00204861, None, -0.000979513, None, 0.00119345, None, -0.00104054, None, 0.00119345, None, -0.00104054, None, -0.00140316, None, -0.00105072, None, -0.00140316, None, -0.00105072, None, 0.691485, None, 0.0060047, None, 0.691485, None, 0.0060047, None)

reports.append(Report(604051208, ("CSC", 2, 1, 2, 33), "MEm12_33"))
reports[-1].posNum = 52120
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000660936, 0.00370632, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.36472e-05, 7.41685e-05, 0), \
                           -56902.2, 52120, 52120, -nan)
reports[-1].sigmaresid = ValErr(0.72095, 0.002233, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00230194, None, -0.000631103, None, 0.000305354, None, -0.000737506, None, 0.000305354, None, -0.000737506, None, 0.0025428, None, -0.000711443, None, 0.0025428, None, -0.000711443, None, 0.720951, None, 0.00651496, None, 0.720951, None, 0.00651496, None)

reports.append(Report(604051224, ("CSC", 2, 1, 2, 35), "MEm12_35"))
reports[-1].posNum = 65798
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00054706, 0.00326638, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.62939e-05, 6.4475e-05, 0), \
                           -71476.5, 65798, 65798, -nan)
reports[-1].sigmaresid = ValErr(0.717031, 0.00197659, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0029998, None, -0.00033828, None, -0.000142353, None, -0.000460948, None, -0.000142353, None, -0.000460948, None, -0.000433478, None, -0.000483361, None, -0.000433478, None, -0.000483361, None, 0.717031, None, 0.00608094, None, 0.717031, None, 0.00608094, None)

reports.append(Report(604050960, ("CSC", 2, 1, 2, 2), "MEm12_02"))
reports[-1].posNum = 64744
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00329655, 0.00316118, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000114268, 6.11098e-05, 0), \
                           -69960.6, 64744, 64744, -nan)
reports[-1].sigmaresid = ValErr(0.712935, 0.00198123, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000468117, None, -7.69547e-05, None, 0.000559352, None, -0.000204428, None, 0.000559352, None, -0.000204428, None, -0.00137521, None, -0.000244391, None, -0.00137521, None, -0.000244391, None, 0.712954, None, 0.00574058, None, 0.712954, None, 0.00574058, None)

reports.append(Report(604050976, ("CSC", 2, 1, 2, 4), "MEm12_04"))
reports[-1].posNum = 56774
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00410058, 0.00356006, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000123165, 6.8806e-05, 0), \
                           -59180.3, 56774, 56774, -nan)
reports[-1].sigmaresid = ValErr(0.68622, 0.00203645, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00235059, None, -0.000986771, None, 0.000355812, None, -0.00106888, None, 0.000355812, None, -0.00106888, None, 0.000757224, None, -0.00117651, None, 0.000757224, None, -0.00117651, None, 0.68624, None, 0.00589151, None, 0.68624, None, 0.00589151, None)

reports.append(Report(604050992, ("CSC", 2, 1, 2, 6), "MEm12_06"))
reports[-1].posNum = 60434
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00214643, 0.00327406, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.06648e-05, 6.42439e-05, 0), \
                           -63531.1, 60434, 60434, -nan)
reports[-1].sigmaresid = ValErr(0.692331, 0.0019914, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000265278, None, -0.000728265, None, 0.00108955, None, -0.000751232, None, 0.00108955, None, -0.000751232, None, 0.000698583, None, -0.000801471, None, 0.000698583, None, -0.000801471, None, 0.692333, None, 0.00659555, None, 0.692333, None, 0.00659555, None)

reports.append(Report(604051008, ("CSC", 2, 1, 2, 8), "MEm12_08"))
reports[-1].posNum = 55740
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00707478, 0.00341712, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000144369, 6.56959e-05, 0), \
                           -56782.5, 55740, 55740, -nan)
reports[-1].sigmaresid = ValErr(0.670162, 0.00200716, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000533432, None, -0.000452609, None, 0.00289416, None, -0.000450251, None, 0.00289416, None, -0.000450251, None, 0.00260993, None, -0.000509935, None, 0.00260993, None, -0.000509935, None, 0.670192, None, 0.00601104, None, 0.670192, None, 0.00601104, None)

reports.append(Report(604051024, ("CSC", 2, 1, 2, 10), "MEm12_10"))
reports[-1].posNum = 65528
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000103156, 0.00314145, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.37526e-05, 6.16753e-05, 0), \
                           -71969, 65528, 65528, -nan)
reports[-1].sigmaresid = ValErr(0.725681, 0.00200455, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000984657, None, -0.000457443, None, 0.000418883, None, -0.000603342, None, 0.000418883, None, -0.000603342, None, 0.00477309, None, -0.000605232, None, 0.00477309, None, -0.000605232, None, 0.725682, None, 0.00588839, None, 0.725682, None, 0.00588839, None)

reports.append(Report(604051040, ("CSC", 2, 1, 2, 12), "MEm12_12"))
reports[-1].posNum = 60688
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00724722, 0.00325273, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.00013004, 6.25301e-05, 0), \
                           -62311.9, 60688, 60688, -nan)
reports[-1].sigmaresid = ValErr(0.675582, 0.00193915, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000462193, None, 1.20771e-05, None, -0.00360945, None, -0.000190056, None, -0.00360945, None, -0.000190056, None, -0.00376357, None, -0.000131382, None, -0.00376357, None, -0.000131382, None, 0.675606, None, 0.00596643, None, 0.675606, None, 0.00596643, None)

reports.append(Report(604051056, ("CSC", 2, 1, 2, 14), "MEm12_14"))
reports[-1].posNum = 65994
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00206887, 0.00313731, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.299e-05, 6.12514e-05, 0), \
                           -70796.1, 65994, 65994, -nan)
reports[-1].sigmaresid = ValErr(0.70739, 0.00194712, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00147968, None, 0.000562222, None, -0.000768299, None, 0.000350869, None, -0.000768299, None, 0.000350869, None, -0.00251068, None, 0.00040967, None, -0.00251068, None, 0.00040967, None, 0.707394, None, 0.00597852, None, 0.707394, None, 0.00597852, None)

reports.append(Report(604051072, ("CSC", 2, 1, 2, 16), "MEm12_16"))
reports[-1].posNum = 56936
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00211511, 0.00379278, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.6324e-07, 7.15541e-05, 0), \
                           -59649.2, 56936, 56936, -nan)
reports[-1].sigmaresid = ValErr(0.689847, 0.0020443, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00379424, None, 0.000226793, None, -0.00209938, None, 4.80157e-05, None, -0.00209938, None, 4.80157e-05, None, 0.000689845, None, 2.89477e-05, None, 0.000689845, None, 2.89477e-05, None, 0.689847, None, 0.00599188, None, 0.689847, None, 0.00599188, None)

reports.append(Report(604051088, ("CSC", 2, 1, 2, 18), "MEm12_18"))
reports[-1].posNum = 55512
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00578809, 0.00343034, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000138605, 6.47784e-05, 0), \
                           -59388.2, 55512, 55512, -nan)
reports[-1].sigmaresid = ValErr(0.705314, 0.00211677, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00218149, None, -0.000162699, None, -0.00220419, None, -0.000198393, None, -0.00220419, None, -0.000198393, None, -0.00259971, None, -0.000109032, None, -0.00259971, None, -0.000109032, None, 0.705344, None, 0.0057916, None, 0.705344, None, 0.0057916, None)

reports.append(Report(604051104, ("CSC", 2, 1, 2, 20), "MEm12_20"))
reports[-1].posNum = 58690
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000685397, 0.00341078, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.09973e-05, 6.6155e-05, 0), \
                           -62510.8, 58690, 58690, -nan)
reports[-1].sigmaresid = ValErr(0.701989, 0.00204896, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00152482, None, -1.66206e-05, None, 0.000386589, None, -0.000123766, None, 0.000386589, None, -0.000123766, None, -0.000491458, None, -0.00014028, None, -0.000491458, None, -0.00014028, None, 0.701989, None, 0.00607088, None, 0.701989, None, 0.00607088, None)

reports.append(Report(604051120, ("CSC", 2, 1, 2, 22), "MEm12_22"))
reports[-1].posNum = 38930
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00126432, 0.00409088, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.90326e-05, 7.94273e-05, 0), \
                           -41839.9, 38930, 38930, -nan)
reports[-1].sigmaresid = ValErr(0.708794, 0.00254017, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00154786, None, -0.000614055, None, 0.000795901, None, -0.00078873, None, 0.000795901, None, -0.00078873, None, -0.000242309, None, -0.000741936, None, -0.000242309, None, -0.000741936, None, 0.708794, None, 0.00615464, None, 0.708794, None, 0.00615464, None)

reports.append(Report(604051136, ("CSC", 2, 1, 2, 24), "MEm12_24"))
reports[-1].posNum = 65080
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00196338, 0.00311721, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.35222e-05, 6.05075e-05, 0), \
                           -69203.2, 65080, 65080, -nan)
reports[-1].sigmaresid = ValErr(0.700765, 0.00194238, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00186722, None, -0.000585259, None, -0.000903569, None, -0.000756792, None, -0.000903569, None, -0.000756792, None, -0.0018792, None, -0.000735682, None, -0.0018792, None, -0.000735682, None, 0.700768, None, 0.00594119, None, 0.700768, None, 0.00594119, None)

reports.append(Report(604051152, ("CSC", 2, 1, 2, 26), "MEm12_26"))
reports[-1].posNum = 46172
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0072593, 0.00401976, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000105687, 7.07742e-05, 0), \
                           -44778, 46172, 46172, -nan)
reports[-1].sigmaresid = ValErr(0.638184, 0.00210011, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00296067, None, -0.00173784, None, 0.00321424, None, -0.00173407, None, 0.00321424, None, -0.00173407, None, 0.00248951, None, -0.00175648, None, 0.00248951, None, -0.00175648, None, 0.638199, None, 0.00597881, None, 0.638199, None, 0.00597881, None)

reports.append(Report(604051168, ("CSC", 2, 1, 2, 28), "MEm12_28"))
reports[-1].posNum = 55138
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00294736, 0.00350021, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.42876e-05, 6.51376e-05, 0), \
                           -57189.3, 55138, 55138, -nan)
reports[-1].sigmaresid = ValErr(0.682675, 0.00205576, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00291274, None, -0.00101255, None, 0.00102428, None, -0.00112469, None, 0.00102428, None, -0.00112469, None, -0.00102593, None, -0.00110616, None, -0.00102593, None, -0.00110616, None, 0.682682, None, 0.00573232, None, 0.682682, None, 0.00573232, None)

reports.append(Report(604051184, ("CSC", 2, 1, 2, 30), "MEm12_30"))
reports[-1].posNum = 46200
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00169042, 0.00390231, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.92779e-05, 6.72936e-05, 0), \
                           -45720, 46200, 46200, -nan)
reports[-1].sigmaresid = ValErr(0.650947, 0.00214146, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00248246, None, -0.000820262, None, 0.000477332, None, -0.000911777, None, 0.000477332, None, -0.000911777, None, 0.00102906, None, -0.000937852, None, 0.00102906, None, -0.000937852, None, 0.650952, None, 0.00626814, None, 0.650952, None, 0.00626814, None)

reports.append(Report(604051200, ("CSC", 2, 1, 2, 32), "MEm12_32"))
reports[-1].posNum = 55346
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00686355, 0.00345494, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000163712, 6.46257e-05, 0), \
                           -56309.2, 55346, 55346, -nan)
reports[-1].sigmaresid = ValErr(0.669292, 0.00201167, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00031337, None, -0.00062724, None, 0.00189777, None, -0.000799643, None, 0.00189777, None, -0.000799643, None, -0.00109103, None, -0.000844805, None, -0.00109103, None, -0.000844805, None, 0.669331, None, 0.00606104, None, 0.669331, None, 0.00606104, None)

reports.append(Report(604051216, ("CSC", 2, 1, 2, 34), "MEm12_34"))
reports[-1].posNum = 61554
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00429257, 0.00323891, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.08613e-05, 6.25539e-05, 0), \
                           -65387.5, 61554, 61554, -nan)
reports[-1].sigmaresid = ValErr(0.70001, 0.00199508, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00153006, None, -0.000175925, None, 0.00198247, None, -0.000283117, None, 0.00198247, None, -0.000283117, None, 0.00338297, None, -0.000330424, None, 0.00338297, None, -0.000330424, None, 0.700022, None, 0.00606307, None, 0.700022, None, 0.00606307, None)

reports.append(Report(604051232, ("CSC", 2, 1, 2, 36), "MEm12_36"))
reports[-1].posNum = 63880
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0020227, 0.00315093, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.18945e-05, 6.09538e-05, 0), \
                           -68787.2, 63880, 63880, -nan)
reports[-1].sigmaresid = ValErr(0.710263, 0.00198711, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00111178, None, -5.26998e-05, None, 0.0010431, None, -0.00013745, None, 0.0010431, None, -0.00013745, None, 0.00343361, None, -0.000122792, None, 0.00343361, None, -0.000122792, None, 0.710266, None, 0.00611717, None, 0.710266, None, 0.00611717, None)

reports.append(Report(604051464, ("CSC", 2, 1, 3, 1), "MEm13_01"))
reports[-1].posNum = 17500
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00603398, 0.0148506, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.79239e-05, 0.00030372, 0), \
                           -36612.5, 17500, 17500, -nan)
reports[-1].sigmaresid = ValErr(1.96051, 0.0104794, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0229714, None, -0.00162517, None, -0.00608861, None, -0.00141547, None, -0.00608861, None, -0.00141547, None, 0.00164031, None, -0.0013782, None, 0.00164031, None, -0.0013782, None, 1.96051, None, 0.00929837, None, 1.96051, None, 0.00929837, None)

reports.append(Report(604051472, ("CSC", 2, 1, 3, 2), "MEm13_02"))
reports[-1].posNum = 15008
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00307991, 0.0159391, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.99354e-05, 0.000329077, 0), \
                           -31315.3, 15008, 15008, -nan)
reports[-1].sigmaresid = ValErr(1.94962, 0.0112531, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00956113, None, -0.00256974, None, 0.00284833, None, -0.00244181, None, 0.00284833, None, -0.00244181, None, 0.0207171, None, -0.00255025, None, 0.0207171, None, -0.00255025, None, 1.94963, None, 0.00882399, None, 1.94963, None, 0.00882399, None)

reports.append(Report(604051480, ("CSC", 2, 1, 3, 3), "MEm13_03"))
reports[-1].posNum = 11616
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0136611, 0.0188047, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000341784, 0.000408038, 0), \
                           -24543, 11616, 11616, -nan)
reports[-1].sigmaresid = ValErr(2.00157, 0.013132, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0067855, None, 0.00075454, None, 0.0111899, None, 0.000832919, None, 0.0111899, None, 0.000832919, None, 0.000724211, None, 0.000821132, None, 0.000724211, None, 0.000821132, None, 2.00161, None, 0.00913184, None, 2.00161, None, 0.00913184, None)

reports.append(Report(604051488, ("CSC", 2, 1, 3, 4), "MEm13_04"))
reports[-1].posNum = 10310
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.012411, 0.0224155, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.85714e-05, 0.00046848, 0), \
                           -22788.4, 10310, 10310, -nan)
reports[-1].sigmaresid = ValErr(2.20644, 0.0153655, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0248097, None, 0.00103862, None, -0.0114886, None, 0.00103284, None, -0.0114886, None, 0.00103284, None, 0.00342592, None, 0.00108357, None, 0.00342592, None, 0.00108357, None, 2.20644, None, 0.00958126, None, 2.20644, None, 0.00958126, None)

reports.append(Report(604051496, ("CSC", 2, 1, 3, 5), "MEm13_05"))
reports[-1].posNum = 7662
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0205885, 0.0216822, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00056759, 0.000446162, 0), \
                           -15645.3, 7662, 7662, -nan)
reports[-1].sigmaresid = ValErr(1.86452, 0.0150621, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0176488, None, 6.38054e-06, None, -0.0154299, None, 7.26484e-06, None, -0.0154299, None, 7.26484e-06, None, -0.015225, None, 0.000120008, None, -0.015225, None, 0.000120008, None, 1.8647, None, 0.0092219, None, 1.8647, None, 0.0092219, None)

reports.append(Report(604051504, ("CSC", 2, 1, 3, 6), "MEm13_06"))
reports[-1].posNum = 6060
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0030182, 0.0278363, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000175601, 0.000573323, 0), \
                           -13000.3, 6060, 6060, -nan)
reports[-1].sigmaresid = ValErr(2.0675, 0.0187803, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00334115, None, 0.00165377, None, 0.000433126, None, 0.0015003, None, 0.000433126, None, 0.0015003, None, -0.0302056, None, 0.00173685, None, -0.0302056, None, 0.00173685, None, 2.06749, None, 0.0093684, None, 2.06749, None, 0.0093684, None)

reports.append(Report(604051512, ("CSC", 2, 1, 3, 7), "MEm13_07"))
reports[-1].posNum = 7586
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0341521, 0.0257941, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000224522, 0.000546267, 0), \
                           -16531.8, 7586, 7586, -nan)
reports[-1].sigmaresid = ValErr(2.13896, 0.0173652, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0356414, None, 0.00165246, None, 0.0309143, None, 0.0017151, None, 0.0309143, None, 0.0017151, None, 0.0299369, None, 0.00176797, None, 0.0299369, None, 0.00176797, None, 2.13898, None, 0.00950627, None, 2.13898, None, 0.00950627, None)

reports.append(Report(604051520, ("CSC", 2, 1, 3, 8), "MEm13_08"))
reports[-1].posNum = 9044
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0171385, 0.0203282, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000435097, 0.000439205, 0), \
                           -18684.3, 9044, 9044, -nan)
reports[-1].sigmaresid = ValErr(1.90979, 0.0142001, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0334107, None, 0.00102049, None, 0.0140219, None, 0.00112312, None, 0.0140219, None, 0.00112312, None, 0.0187039, None, 0.00111076, None, 0.0187039, None, 0.00111076, None, 1.90989, None, 0.00920114, None, 1.90989, None, 0.00920114, None)

reports.append(Report(604051528, ("CSC", 2, 1, 3, 9), "MEm13_09"))
reports[-1].posNum = 13578
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00392822, 0.0179721, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000179381, 0.000379562, 0), \
                           -29215.3, 13578, 13578, -nan)
reports[-1].sigmaresid = ValErr(2.08075, 0.0126266, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00235441, None, 0.00226199, None, -0.00494172, None, 0.00236242, None, -0.00494172, None, 0.00236242, None, -0.0402764, None, 0.00258991, None, -0.0402764, None, 0.00258991, None, 2.08076, None, 0.00917555, None, 2.08076, None, 0.00917555, None)

reports.append(Report(604051536, ("CSC", 2, 1, 3, 10), "MEm13_10"))
reports[-1].posNum = 16186
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0011269, 0.0156294, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000153632, 0.000317677, 0), \
                           -34091, 16186, 16186, -nan)
reports[-1].sigmaresid = ValErr(1.98826, 0.0110507, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00806298, None, 0.00272497, None, 0.00120423, None, 0.00277676, None, 0.00120423, None, 0.00277676, None, 0.0122967, None, 0.00277232, None, 0.0122967, None, 0.00277232, None, 1.98828, None, 0.00860695, None, 1.98828, None, 0.00860695, None)

reports.append(Report(604051544, ("CSC", 2, 1, 3, 11), "MEm13_11"))
reports[-1].posNum = 10606
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000836762, 0.0196217, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000103677, 0.000397401, 0), \
                           -22443.2, 10606, 10606, -nan)
reports[-1].sigmaresid = ValErr(2.00802, 0.0137872, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0161365, None, 0.00117193, None, -0.00020083, None, 0.00136143, None, -0.00020083, None, 0.00136143, None, 0.0161591, None, 0.00132421, None, 0.0161591, None, 0.00132421, None, 2.00803, None, 0.00993947, None, 2.00803, None, 0.00993947, None)

reports.append(Report(604051552, ("CSC", 2, 1, 3, 12), "MEm13_12"))
reports[-1].posNum = 9360
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00150154, 0.0225333, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.99989e-05, 0.000475098, 0), \
                           -19938.1, 9360, 9360, -nan)
reports[-1].sigmaresid = ValErr(2.03646, 0.0148844, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00540952, None, 0.00180351, None, -0.000647097, None, 0.00184023, None, -0.000647097, None, 0.00184023, None, 0.0175445, None, 0.00189783, None, 0.0175445, None, 0.00189783, None, 2.03643, None, 0.00963498, None, 2.03643, None, 0.00963498, None)

reports.append(Report(604051560, ("CSC", 2, 1, 3, 13), "MEm13_13"))
reports[-1].posNum = 8396
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000252599, 0.0233545, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000444955, 0.000482406, 0), \
                           -17963.8, 8396, 8396, -nan)
reports[-1].sigmaresid = ValErr(2.05572, 0.015864, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0245744, None, 0.000874279, None, 0.00623925, None, 0.000893649, None, 0.00623925, None, 0.000893649, None, -0.0136947, None, 0.00109614, None, -0.0136947, None, 0.00109614, None, 2.05582, None, 0.0091366, None, 2.05582, None, 0.0091366, None)

reports.append(Report(604051568, ("CSC", 2, 1, 3, 14), "MEm13_14"))
reports[-1].posNum = 10384
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0202121, 0.0193549, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(7.06942e-05, 0.00038159, 0), \
                           -21782, 10384, 10384, -nan)
reports[-1].sigmaresid = ValErr(1.97131, 0.013679, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00770113, None, 0.000915524, None, 0.0201314, None, 0.000778414, None, 0.0201314, None, 0.000778414, None, 0.0110024, None, 0.000948993, None, 0.0110024, None, 0.000948993, None, 1.97133, None, 0.00894849, None, 1.97133, None, 0.00894849, None)

reports.append(Report(604051576, ("CSC", 2, 1, 3, 15), "MEm13_15"))
reports[-1].posNum = 6152
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00718809, 0.0282466, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(8.44886e-07, 0.000555835, 0), \
                           -13389.6, 6152, 6152, -nan)
reports[-1].sigmaresid = ValErr(2.13299, 0.0192294, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00254866, None, -0.0017766, None, 0.00717687, None, -0.00161582, None, 0.00717687, None, -0.00161582, None, 0.0247301, None, -0.00187898, None, 0.0247301, None, -0.00187898, None, 2.13299, None, 0.00926964, None, 2.13299, None, 0.00926964, None)

reports.append(Report(604051584, ("CSC", 2, 1, 3, 16), "MEm13_16"))
reports[-1].posNum = 6908
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0275177, 0.0272185, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.68131e-06, 0.000561183, 0), \
                           -15004.4, 6908, 6908, -nan)
reports[-1].sigmaresid = ValErr(2.12355, 0.0180663, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.029841, None, 0.00119541, None, -0.027482, None, 0.00138675, None, -0.027482, None, 0.00138675, None, -0.0198609, None, 0.00131108, None, -0.0198609, None, 0.00131108, None, 2.12356, None, 0.00926602, None, 2.12356, None, 0.00926602, None)

reports.append(Report(604051592, ("CSC", 2, 1, 3, 17), "MEm13_17"))
reports[-1].posNum = 11426
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00330159, 0.0186909, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.91564e-05, 0.000407598, 0), \
                           -23993.9, 11426, 11426, -nan)
reports[-1].sigmaresid = ValErr(1.97587, 0.0130708, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00392, None, 0.00256351, None, 0.00316735, None, 0.00275974, None, 0.00316735, None, 0.00275974, None, -0.0417022, None, 0.00297666, None, -0.0417022, None, 0.00297666, None, 1.97585, None, 0.0104462, None, 1.97585, None, 0.0104462, None)

reports.append(Report(604051600, ("CSC", 2, 1, 3, 18), "MEm13_18"))
reports[-1].posNum = 15766
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000591127, 0.0157695, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000115426, 0.00033966, 0), \
                           -33114.1, 15766, 15766, -nan)
reports[-1].sigmaresid = ValErr(1.97667, 0.0111316, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000166489, None, -0.00096423, None, -0.000897746, None, -0.000956371, None, -0.000897746, None, -0.000956371, None, -0.016461, None, -0.000965497, None, -0.016461, None, -0.000965497, None, 1.97667, None, 0.00899442, None, 1.97667, None, 0.00899442, None)

reports.append(Report(604051608, ("CSC", 2, 1, 3, 19), "MEm13_19"))
reports[-1].posNum = 16676
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00976277, 0.0155458, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.36782e-05, 0.000327547, 0), \
                           -35272.7, 16676, 16676, -nan)
reports[-1].sigmaresid = ValErr(2.00619, 0.0109852, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00895452, None, -0.000814337, None, 0.00976801, None, -0.000569783, None, 0.00976801, None, -0.000569783, None, -0.00785619, None, -0.000436586, None, -0.00785619, None, -0.000436586, None, 2.00619, None, 0.00969719, None, 2.00619, None, 0.00969719, None)

reports.append(Report(604051616, ("CSC", 2, 1, 3, 20), "MEm13_20"))
reports[-1].posNum = 17934
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00898452, 0.0146572, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.10602e-05, 0.000310492, 0), \
                           -37540.8, 17934, 17934, -nan)
reports[-1].sigmaresid = ValErr(1.96273, 0.0103635, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00972358, None, 0.000505432, None, -0.00895487, None, 0.000684372, None, -0.00895487, None, 0.000684372, None, 0.00973942, None, 0.000638364, None, 0.00973942, None, 0.000638364, None, 1.96273, None, 0.00892393, None, 1.96273, None, 0.00892393, None)

reports.append(Report(604051624, ("CSC", 2, 1, 3, 21), "MEm13_21"))
reports[-1].posNum = 15110
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00608969, 0.0168088, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000165881, 0.000375754, 0), \
                           -32230.8, 15110, 15110, -nan)
reports[-1].sigmaresid = ValErr(2.04244, 0.0117492, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0051265, None, -0.000341076, None, 0.00496558, None, -0.000284818, None, 0.00496558, None, -0.000284818, None, 0.00432711, None, -0.000167706, None, 0.00432711, None, -0.000167706, None, 2.04243, None, 0.00900622, None, 2.04243, None, 0.00900622, None)

reports.append(Report(604051632, ("CSC", 2, 1, 3, 22), "MEm13_22"))
reports[-1].posNum = 15502
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00880779, 0.0161997, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.84712e-05, 0.000349879, 0), \
                           -32859.2, 15502, 15502, -nan)
reports[-1].sigmaresid = ValErr(2.01523, 0.011445, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0260517, None, 0.00163371, None, 0.00880189, None, 0.00168079, None, 0.00880189, None, 0.00168079, None, 0.0310876, None, 0.00169283, None, 0.0310876, None, 0.00169283, None, 2.01523, None, 0.0100985, None, 2.01523, None, 0.0100985, None)

reports.append(Report(604051640, ("CSC", 2, 1, 3, 23), "MEm13_23"))
reports[-1].posNum = 15458
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00188894, 0.0153858, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.39443e-05, 0.000315142, 0), \
                           -31956.1, 15458, 15458, -nan)
reports[-1].sigmaresid = ValErr(1.91238, 0.0108763, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0116247, None, -0.000209145, None, -0.00193856, None, 0.000131181, None, -0.00193856, None, 0.000131181, None, 0.0101672, None, -2.38858e-05, None, 0.0101672, None, -2.38858e-05, None, 1.91238, None, 0.00963733, None, 1.91238, None, 0.00963733, None)

reports.append(Report(604051648, ("CSC", 2, 1, 3, 24), "MEm13_24"))
reports[-1].posNum = 10478
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00534969, 0.0196265, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000118043, 0.00038842, 0), \
                           -22136.2, 10478, 10478, -nan)
reports[-1].sigmaresid = ValErr(2.00111, 0.0138235, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0185945, None, -0.000126654, None, 0.00483478, None, 2.49381e-05, None, 0.00483478, None, 2.49381e-05, None, 0.0114529, None, 5.99911e-06, None, 0.0114529, None, 5.99911e-06, None, 2.00112, None, 0.00925594, None, 2.00112, None, 0.00925594, None)

reports.append(Report(604051656, ("CSC", 2, 1, 3, 25), "MEm13_25"))
reports[-1].posNum = 6920
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0105604, 0.0240925, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000261747, 0.000489284, 0), \
                           -14627.6, 6920, 6920, -nan)
reports[-1].sigmaresid = ValErr(2.00345, 0.0170298, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00402505, None, 0.00162808, None, 0.0108956, None, 0.00179246, None, 0.0108956, None, 0.00179246, None, -0.0127461, None, 0.00195155, None, -0.0127461, None, 0.00195155, None, 2.00349, None, 0.00915902, None, 2.00349, None, 0.00915902, None)

reports.append(Report(604051664, ("CSC", 2, 1, 3, 26), "MEm13_26"))
reports[-1].posNum = 6246
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0115157, 0.0254025, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000387295, 0.000528101, 0), \
                           -13182.3, 6246, 6246, -nan)
reports[-1].sigmaresid = ValErr(1.99688, 0.0178665, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00714052, None, 0.00109298, None, -0.00959142, None, 0.00112276, None, -0.00959142, None, 0.00112276, None, 0.0105604, None, 0.00121887, None, 0.0105604, None, 0.00121887, None, 1.99694, None, 0.00940772, None, 1.99694, None, 0.00940772, None)

reports.append(Report(604051672, ("CSC", 2, 1, 3, 27), "MEm13_27"))
reports[-1].posNum = 5886
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00263073, 0.0260256, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000229318, 0.000503247, 0), \
                           -12411.1, 5886, 5886, -nan)
reports[-1].sigmaresid = ValErr(1.99301, 0.0183689, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.018896, None, 0.000601131, None, -0.00334338, None, 0.000664457, None, -0.00334338, None, 0.000664457, None, 0.0245426, None, 0.000659007, None, 0.0245426, None, 0.000659007, None, 1.99305, None, 0.00879384, None, 1.99305, None, 0.00879384, None)

reports.append(Report(604051680, ("CSC", 2, 1, 3, 28), "MEm13_28"))
reports[-1].posNum = 8086
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0115131, 0.022389, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.76417e-05, 0.00042049, 0), \
                           -16994.7, 8086, 8086, -nan)
reports[-1].sigmaresid = ValErr(1.97944, 0.0155656, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.035474, None, 0.000833286, None, 0.0107553, None, 0.00118257, None, 0.0107553, None, 0.00118257, None, -0.00605232, None, 0.00126808, None, -0.00605232, None, 0.00126808, None, 1.97943, None, 0.00864627, None, 1.97943, None, 0.00864627, None)

reports.append(Report(604051688, ("CSC", 2, 1, 3, 29), "MEm13_29"))
reports[-1].posNum = 7136
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0171352, 0.0234585, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.90574e-05, 0.000447784, 0), \
                           -14938.1, 7136, 7136, -nan)
reports[-1].sigmaresid = ValErr(1.96289, 0.0164308, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00265297, None, -0.00188252, None, 0.0165003, None, -0.00150179, None, 0.0165003, None, -0.00150179, None, 0.0083827, None, -0.00143941, None, 0.0083827, None, -0.00143941, None, 1.96288, None, 0.00954272, None, 1.96288, None, 0.00954272, None)

reports.append(Report(604051696, ("CSC", 2, 1, 3, 30), "MEm13_30"))
reports[-1].posNum = 4998
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000448457, 0.0285304, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000202778, 0.000590638, 0), \
                           -10577.8, 4998, 4998, -nan)
reports[-1].sigmaresid = ValErr(2.00868, 0.0200909, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0191375, None, 0.000823946, None, 0.000495904, None, 0.000931545, None, 0.000495904, None, 0.000931545, None, 0.0409325, None, 0.000968391, None, 0.0409325, None, 0.000968391, None, 2.0087, None, 0.00890261, None, 2.0087, None, 0.00890261, None)

reports.append(Report(604051704, ("CSC", 2, 1, 3, 31), "MEm13_31"))
reports[-1].posNum = 5542
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0134537, 0.0264064, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(8.43438e-05, 0.000529324, 0), \
                           -11602.4, 5542, 5542, -nan)
reports[-1].sigmaresid = ValErr(1.96324, 0.0186475, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0167096, None, 0.000121624, None, 0.0132639, None, 0.000394447, None, 0.0132639, None, 0.000394447, None, 0.0471899, None, 0.000144869, None, 0.0471899, None, 0.000144869, None, 1.96325, None, 0.0112617, None, 1.96325, None, 0.0112617, None)

reports.append(Report(604051712, ("CSC", 2, 1, 3, 32), "MEm13_32"))
reports[-1].posNum = 9436
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00608107, 0.0200601, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.93845e-06, 0.000389445, 0), \
                           -19667.1, 9436, 9436, -nan)
reports[-1].sigmaresid = ValErr(1.94512, 0.0141591, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00380689, None, -0.00235848, None, -0.0060721, None, -0.0020386, None, -0.0060721, None, -0.0020386, None, 0.011577, None, -0.0021564, None, 0.011577, None, -0.0021564, None, 1.94512, None, 0.00901085, None, 1.94512, None, 0.00901085, None)

reports.append(Report(604051720, ("CSC", 2, 1, 3, 33), "MEm13_33"))
reports[-1].posNum = 8750
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.036859, 0.0213799, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000120878, 0.000442017, 0), \
                           -18478.2, 8750, 8750, -nan)
reports[-1].sigmaresid = ValErr(1.99941, 0.015114, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0510761, None, 0.000656755, None, 0.0370275, None, 0.000816909, None, 0.0370275, None, 0.000816909, None, 0.014688, None, 0.000963412, None, 0.014688, None, 0.000963412, None, 1.99943, None, 0.00862267, None, 1.99943, None, 0.00862267, None)

reports.append(Report(604051728, ("CSC", 2, 1, 3, 34), "MEm13_34"))
reports[-1].posNum = 16706
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00719256, 0.0153757, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000152805, 0.000327787, 0), \
                           -35178.3, 16706, 16706, -nan)
reports[-1].sigmaresid = ValErr(1.98733, 0.0108722, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0148749, None, -0.000379955, None, -0.0072029, None, -0.000108173, None, -0.0072029, None, -0.000108173, None, -0.0325944, None, -3.98069e-05, None, -0.0325944, None, -3.98069e-05, None, 1.98734, None, 0.00941016, None, 1.98734, None, 0.00941016, None)

reports.append(Report(604051736, ("CSC", 2, 1, 3, 35), "MEm13_35"))
reports[-1].posNum = 16526
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00213466, 0.0157388, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(7.19862e-06, 0.000339478, 0), \
                           -35092.8, 16526, 16526, -nan)
reports[-1].sigmaresid = ValErr(2.02294, 0.0111271, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00543257, None, 0.000160918, None, -0.00214287, None, 0.000313091, None, -0.00214287, None, 0.000313091, None, -0.000948874, None, 0.000392892, None, -0.000948874, None, 0.000392892, None, 2.02294, None, 0.00927797, None, 2.02294, None, 0.00927797, None)

reports.append(Report(604051744, ("CSC", 2, 1, 3, 36), "MEm13_36"))
reports[-1].posNum = 14266
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0157621, 0.0163501, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000113149, 0.000342783, 0), \
                           -29789.6, 14266, 14266, -nan)
reports[-1].sigmaresid = ValErr(1.9527, 0.0115603, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0108421, None, 0.000932999, None, 0.0156879, None, 0.0010954, None, 0.0156879, None, 0.0010954, None, 0.0224276, None, 0.0010579, None, 0.0224276, None, 0.0010579, None, 1.95271, None, 0.00867905, None, 1.95271, None, 0.00867905, None)

reports.append(Report(604049928, ("CSC", 2, 1, 4, 1), "MEm14_01"))
reports[-1].posNum = 118028
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000178316, 0.000764336, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.47571e-05, 1.9125e-05, 0), \
                           -9585.22, 118028, 118028, -nan)
reports[-1].sigmaresid = ValErr(0.262441, 0.000540163, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000325231, None, 0.000856136, None, 0.00014513, None, 0.000811622, None, 0.00014513, None, 0.000811622, None, -0.000269147, None, 0.000776733, None, -0.000269147, None, 0.000776733, None, 0.262443, None, 0.00534729, None, 0.262443, None, 0.00534729, None)

reports.append(Report(604049944, ("CSC", 2, 1, 4, 3), "MEm14_03"))
reports[-1].posNum = 120750
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000238496, 0.00126558, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.407e-08, 2.41161e-05, 0), \
                           -8602.13, 120750, 120750, -nan)
reports[-1].sigmaresid = ValErr(0.259837, 0.00052926, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000607642, None, 0.000492416, None, -0.000237752, None, 0.000491169, None, -0.000237752, None, 0.000491169, None, 0.000992797, None, 0.000474291, None, 0.000992797, None, 0.000474291, None, 0.259837, None, 0.00543467, None, 0.259837, None, 0.00543467, None)

reports.append(Report(604049960, ("CSC", 2, 1, 4, 5), "MEm14_05"))
reports[-1].posNum = 94094
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000818843, 0.000844176, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.30474e-05, 2.15854e-05, 0), \
                           -5039.64, 94094, 94094, -nan)
reports[-1].sigmaresid = ValErr(0.255284, 0.000588474, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000622498, None, 0.000341753, None, 0.000667734, None, 0.000353894, None, 0.000667734, None, 0.000353894, None, 0.000402574, None, 0.000354548, None, 0.000402574, None, 0.000354548, None, 0.255285, None, 0.00509826, None, 0.255285, None, 0.00509826, None)

reports.append(Report(604049976, ("CSC", 2, 1, 4, 7), "MEm14_07"))
reports[-1].posNum = 95254
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000164985, 0.000907269, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.84185e-06, 2.36248e-05, 0), \
                           -12999.3, 95254, 95254, -nan)
reports[-1].sigmaresid = ValErr(0.277351, 0.000635434, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000362661, None, 0.00986175, None, 0.000154814, None, 0.00945904, None, 0.000154814, None, 0.00945904, None, -0.000289987, None, 0.00964812, None, -0.000289987, None, 0.00964812, None, 0.277352, None, 0.00529856, None, 0.277352, None, 0.00529856, None)

reports.append(Report(604049992, ("CSC", 2, 1, 4, 9), "MEm14_09"))
reports[-1].posNum = 113414
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000108175, 0.000783899, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.13076e-05, 1.96458e-05, 0), \
                           -9879.2, 113414, 113414, -nan)
reports[-1].sigmaresid = ValErr(0.263993, 0.0005543, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000640582, None, -0.000378534, None, -0.000106927, None, -0.00040469, None, -0.000106927, None, -0.00040469, None, -0.0003944, None, -0.000421433, None, -0.0003944, None, -0.000421433, None, 0.263995, None, 0.00502804, None, 0.263995, None, 0.00502804, None)

reports.append(Report(604050008, ("CSC", 2, 1, 4, 11), "MEm14_11"))
reports[-1].posNum = 114592
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00102936, 0.000776407, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.01766e-05, 1.91113e-05, 0), \
                           -9225.87, 114592, 114592, -nan)
reports[-1].sigmaresid = ValErr(0.262258, 0.000547818, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(9.33167e-05, None, 0.00124382, None, -0.000975392, None, 0.00121502, None, -0.000975392, None, 0.00121502, None, -0.00130786, None, 0.00122929, None, -0.00130786, None, 0.00122929, None, 0.262259, None, 0.00554023, None, 0.262259, None, 0.00554023, None)

reports.append(Report(604050024, ("CSC", 2, 1, 4, 13), "MEm14_13"))
reports[-1].posNum = 115366
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000181969, 0.000774413, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.77625e-05, 1.92443e-05, 0), \
                           -9606.37, 115366, 115366, -nan)
reports[-1].sigmaresid = ValErr(0.262982, 0.000547485, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00143847, None, -0.000681881, None, 0.000167763, None, -0.000661393, None, 0.000167763, None, -0.000661393, None, 0.00164669, None, -0.00069618, None, 0.00164669, None, -0.00069618, None, 0.262983, None, 0.00475721, None, 0.262983, None, 0.00475721, None)

reports.append(Report(604050040, ("CSC", 2, 1, 4, 15), "MEm14_15"))
reports[-1].posNum = 116406
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-7.6495e-05, 0.000787148, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.9416e-06, 1.93389e-05, 0), \
                           -12083.6, 116406, 116406, -nan)
reports[-1].sigmaresid = ValErr(0.268439, 0.000556342, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000233217, None, 0.000762147, None, -8.00565e-05, None, 0.000633889, None, -8.00565e-05, None, 0.000633889, None, -0.00186804, None, 0.000704048, None, -0.00186804, None, 0.000704048, None, 0.268439, None, 0.00597974, None, 0.268439, None, 0.00597974, None)

reports.append(Report(604050056, ("CSC", 2, 1, 4, 17), "MEm14_17"))
reports[-1].posNum = 117978
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00011685, 0.00076796, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.79314e-05, 1.86848e-05, 0), \
                           -9937.39, 117978, 117978, -nan)
reports[-1].sigmaresid = ValErr(0.263234, 0.000541908, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000406217, None, -0.000452185, None, 4.34177e-05, None, -0.000459803, None, 4.34177e-05, None, -0.000459803, None, -0.00205357, None, -0.000467764, None, -0.00205357, None, -0.000467764, None, 0.263238, None, 0.00471338, None, 0.263238, None, 0.00471338, None)

reports.append(Report(604050072, ("CSC", 2, 1, 4, 19), "MEm14_19"))
reports[-1].posNum = 104086
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0003275, 0.000830527, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.81202e-05, 2.08219e-05, 0), \
                           -10569.7, 104086, 104086, -nan)
reports[-1].sigmaresid = ValErr(0.267832, 0.000587015, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000395085, None, -4.6822e-06, None, 0.000348345, None, 8.46324e-05, None, 0.000348345, None, 8.46324e-05, None, 0.000633101, None, 6.96008e-05, None, 0.000633101, None, 6.96008e-05, None, 0.267834, None, 0.00570171, None, 0.267834, None, 0.00570171, None)

reports.append(Report(604050088, ("CSC", 2, 1, 4, 21), "MEm14_21"))
reports[-1].posNum = 105336
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00044016, 0.000836121, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(7.54059e-06, 2.13456e-05, 0), \
                           -11659.8, 105336, 105336, -nan)
reports[-1].sigmaresid = ValErr(0.270293, 0.000588887, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00166688, None, 0.00046566, None, -0.000466422, None, 0.000348799, None, -0.000466422, None, 0.000348799, None, -0.00201452, None, 0.000401897, None, -0.00201452, None, 0.000401897, None, 0.270294, None, 0.00508532, None, 0.270294, None, 0.00508532, None)

reports.append(Report(604050104, ("CSC", 2, 1, 4, 23), "MEm14_23"))
reports[-1].posNum = 110232
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00027433, 0.000794905, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.9515e-05, 2.013e-05, 0), \
                           -9472.71, 110232, 110232, -nan)
reports[-1].sigmaresid = ValErr(0.263684, 0.000561584, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00103042, None, -0.000808078, None, -0.000241883, None, -0.000760505, None, -0.000241883, None, -0.000760505, None, -0.00338888, None, -0.000776973, None, -0.00338888, None, -0.000776973, None, 0.263685, None, 0.0051704, None, 0.263685, None, 0.0051704, None)

reports.append(Report(604050120, ("CSC", 2, 1, 4, 25), "MEm14_25"))
reports[-1].posNum = 85952
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000386753, 0.000915429, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.53639e-06, 2.32937e-05, 0), \
                           -8808.82, 85952, 85952, -nan)
reports[-1].sigmaresid = ValErr(0.268084, 0.000646589, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000323579, None, -0.00100976, None, -0.000396027, None, -0.000960928, None, -0.000396027, None, -0.000960928, None, 0.000282841, None, -0.000929604, None, 0.000282841, None, -0.000929604, None, 0.268085, None, 0.00552273, None, 0.268085, None, 0.00552273, None)

reports.append(Report(604050136, ("CSC", 2, 1, 4, 27), "MEm14_27"))
reports[-1].posNum = 114532
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000373075, 0.00077869, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(7.98338e-07, 1.96706e-05, 0), \
                           -9732.9, 114532, 114532, -nan)
reports[-1].sigmaresid = ValErr(0.263432, 0.000550415, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00116598, None, -0.000392946, None, 0.000373929, None, -0.000342327, None, 0.000373929, None, -0.000342327, None, 0.000602746, None, -0.00034824, None, 0.000602746, None, -0.00034824, None, 0.263432, None, 0.00545539, None, 0.263432, None, 0.00545539, None)

reports.append(Report(604050152, ("CSC", 2, 1, 4, 29), "MEm14_29"))
reports[-1].posNum = 123540
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000166614, 0.000747963, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.60865e-05, 1.90509e-05, 0), \
                           -10104, 123540, 123540, -nan)
reports[-1].sigmaresid = ValErr(0.262593, 0.000528279, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00166541, None, 5.06213e-05, None, -0.000136292, None, 1.46412e-05, None, -0.000136292, None, 1.46412e-05, None, 0.000150534, None, 3.63721e-05, None, 0.000150534, None, 3.63721e-05, None, 0.262593, None, 0.00477622, None, 0.262593, None, 0.00477622, None)

reports.append(Report(604050168, ("CSC", 2, 1, 4, 31), "MEm14_31"))
reports[-1].posNum = 118692
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00024578, 0.000758174, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(8.07967e-06, 1.89032e-05, 0), \
                           -8843.58, 118692, 118692, -nan)
reports[-1].sigmaresid = ValErr(0.260688, 0.000535052, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00141953, None, -0.000558346, None, -0.000225429, None, -0.000565427, None, -0.000225429, None, -0.000565427, None, -0.000406767, None, -0.000552049, None, -0.000406767, None, -0.000552049, None, 0.260688, None, 0.00486616, None, 0.260688, None, 0.00486616, None)

reports.append(Report(604050184, ("CSC", 2, 1, 4, 33), "MEm14_33"))
reports[-1].posNum = 116600
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000630976, 0.000765274, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.08924e-05, 1.91997e-05, 0), \
                           -8905.7, 116600, 116600, -nan)
reports[-1].sigmaresid = ValErr(0.261176, 0.00054084, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000314214, None, -0.000433215, None, 0.000603932, None, -0.000453381, None, 0.000603932, None, -0.000453381, None, -7.57259e-05, None, -0.000394668, None, -7.57259e-05, None, -0.000394668, None, 0.261177, None, 0.00498176, None, 0.261177, None, 0.00498176, None)

reports.append(Report(604050200, ("CSC", 2, 1, 4, 35), "MEm14_35"))
reports[-1].posNum = 117662
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000851015, 0.000768516, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.46432e-06, 1.86778e-05, 0), \
                           -9653.09, 117662, 117662, -nan)
reports[-1].sigmaresid = ValErr(0.262659, 0.000541452, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000213763, None, -0.000700015, None, 0.000831896, None, -0.000694144, None, 0.000831896, None, -0.000694144, None, 0.00206781, None, -0.000715496, None, 0.00206781, None, -0.000715496, None, 0.262659, None, 0.00525766, None, 0.262659, None, 0.00525766, None)

reports.append(Report(604049936, ("CSC", 2, 1, 4, 2), "MEm14_02"))
reports[-1].posNum = 127456
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(4.20858e-06, 0.000669018, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.69908e-06, 1.61323e-05, 0), \
                           2269.51, 127456, 127456, -nan)
reports[-1].sigmaresid = ValErr(0.2377, 0.000470798, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000385012, None, 0.000316896, None, -6.74415e-06, None, 0.000348007, None, -6.74415e-06, None, 0.000348007, None, 0.00143536, None, 0.000348366, None, 0.00143536, None, 0.000348366, None, 0.2377, None, 0.00538234, None, 0.2377, None, 0.00538234, None)

reports.append(Report(604049952, ("CSC", 2, 1, 4, 4), "MEm14_04"))
reports[-1].posNum = 126046
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000261459, 0.000667881, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.45285e-06, 1.59269e-05, 0), \
                           3433.04, 126046, 126046, -nan)
reports[-1].sigmaresid = ValErr(0.235469, 0.00046898, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000440341, None, 0.000557087, None, 0.000229609, None, 0.000569325, None, 0.000229609, None, 0.000569325, None, 0.00148622, None, 0.000597256, None, 0.00148622, None, 0.000597256, None, 0.235469, None, 0.00537008, None, 0.235469, None, 0.00537008, None)

reports.append(Report(604049968, ("CSC", 2, 1, 4, 6), "MEm14_06"))
reports[-1].posNum = 107562
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000505287, 0.000720254, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.75031e-05, 1.69724e-05, 0), \
                           3836.99, 107562, 107562, -nan)
reports[-1].sigmaresid = ValErr(0.233491, 0.000503415, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00133735, None, 0.000307495, None, 0.000392724, None, 0.000244793, None, 0.000392724, None, 0.000244793, None, -0.0016227, None, 0.00029133, None, -0.0016227, None, 0.00029133, None, 0.233492, None, 0.00527296, None, 0.233492, None, 0.00527296, None)

reports.append(Report(604049984, ("CSC", 2, 1, 4, 8), "MEm14_08"))
reports[-1].posNum = 122006
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000217776, 0.000671539, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.19105e-05, 1.58074e-05, 0), \
                           5044.19, 122006, 122006, -nan)
reports[-1].sigmaresid = ValErr(0.232171, 0.000470004, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000272818, None, -0.000502066, None, -0.00028988, None, -0.000527938, None, -0.00028988, None, -0.000527938, None, 0.000257114, None, -0.000520806, None, 0.000257114, None, -0.000520806, None, 0.232171, None, 0.00562385, None, 0.232171, None, 0.00562385, None)

reports.append(Report(604050000, ("CSC", 2, 1, 4, 10), "MEm14_10"))
reports[-1].posNum = 124476
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-8.4747e-05, 0.000670297, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.53283e-06, 1.61532e-05, 0), \
                           3670.94, 124476, 124476, -nan)
reports[-1].sigmaresid = ValErr(0.234939, 0.000470866, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000648736, None, -0.000624268, None, -6.79872e-05, None, -0.000635848, None, -6.79872e-05, None, -0.000635848, None, -0.00200017, None, -0.000628459, None, -0.00200017, None, -0.000628459, None, 0.234939, None, 0.00532593, None, 0.234939, None, 0.00532593, None)

reports.append(Report(604050016, ("CSC", 2, 1, 4, 12), "MEm14_12"))
reports[-1].posNum = 125256
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000111304, 0.000662289, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.02862e-06, 1.55273e-05, 0), \
                           5109.76, 125256, 125256, -nan)
reports[-1].sigmaresid = ValErr(0.232298, 0.000464122, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(1.3764e-08, None, -0.000298311, None, -8.83756e-05, None, -0.000236895, None, -8.83756e-05, None, -0.000236895, None, -0.000928987, None, -0.000247821, None, -0.000928987, None, -0.000247821, None, 0.232298, None, 0.0052013, None, 0.232298, None, 0.0052013, None)

reports.append(Report(604050032, ("CSC", 2, 1, 4, 14), "MEm14_14"))
reports[-1].posNum = 124128
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000824126, 0.000444659, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.83141e-06, 1.07129e-05, 0), \
                           2646.35, 124128, 124128, -nan)
reports[-1].sigmaresid = ValErr(0.236867, 0.000473075, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000674073, None, -0.000683743, None, 0.000806183, None, -0.00073722, None, 0.000806183, None, -0.00073722, None, -0.000497917, None, -0.000782321, None, -0.000497917, None, -0.000782321, None, 0.236867, None, 0.00534952, None, 0.236867, None, 0.00534952, None)

reports.append(Report(604050048, ("CSC", 2, 1, 4, 16), "MEm14_16"))
reports[-1].posNum = 127278
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000824348, 0.000672094, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.75145e-05, 1.58623e-05, 0), \
                           1779.75, 127278, 127278, -nan)
reports[-1].sigmaresid = ValErr(0.238611, 0.000472932, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00110001, None, -0.000476978, None, 0.000751241, None, -0.000406902, None, 0.000751241, None, -0.000406902, None, -0.000390688, None, -0.000468954, None, -0.000390688, None, -0.000468954, None, 0.238612, None, 0.00501492, None, 0.238612, None, 0.00501492, None)

reports.append(Report(604050064, ("CSC", 2, 1, 4, 18), "MEm14_18"))
reports[-1].posNum = 117304
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000441934, 0.000695659, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.35938e-06, 1.65261e-05, 0), \
                           2323.44, 117304, 117304, -nan)
reports[-1].sigmaresid = ValErr(0.237225, 0.000489767, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000814824, None, -0.00070416, None, -0.00044729, None, -0.000666781, None, -0.00044729, None, -0.000666781, None, -0.00183814, None, -0.000739194, None, -0.00183814, None, -0.000739194, None, 0.237225, None, 0.00529186, None, 0.237225, None, 0.00529186, None)

reports.append(Report(604050080, ("CSC", 2, 1, 4, 20), "MEm14_20"))
reports[-1].posNum = 119506
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000246384, 0.000687861, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.43102e-06, 1.6591e-05, 0), \
                           2547.73, 119506, 119506, -nan)
reports[-1].sigmaresid = ValErr(0.236867, 0.000484501, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000207935, None, -0.000141116, None, 0.000211941, None, -0.00017857, None, 0.000211941, None, -0.00017857, None, 0.00229389, None, -0.000195226, None, 0.00229389, None, -0.000195226, None, 0.236867, None, 0.00521351, None, 0.236867, None, 0.00521351, None)

reports.append(Report(604050096, ("CSC", 2, 1, 4, 22), "MEm14_22"))
reports[-1].posNum = 123540
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000640418, 0.000673608, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.62264e-05, 1.62208e-05, 0), \
                           3408.36, 123540, 123540, -nan)
reports[-1].sigmaresid = ValErr(0.235386, 0.000473546, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00125068, None, -0.000637848, None, -0.000523197, None, -0.000648181, None, -0.000523197, None, -0.000648181, None, -0.00154567, None, -0.000661789, None, -0.00154567, None, -0.000661789, None, 0.235389, None, 0.00585148, None, 0.235389, None, 0.00585148, None)

reports.append(Report(604050112, ("CSC", 2, 1, 4, 24), "MEm14_24"))
reports[-1].posNum = 122402
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000768332, 0.000683543, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.48158e-05, 1.65943e-05, 0), \
                           1893.54, 122402, 122402, -nan)
reports[-1].sigmaresid = ValErr(0.238256, 0.000481543, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000174832, None, -0.00119461, None, -0.000680315, None, -0.00118151, None, -0.000680315, None, -0.00118151, None, -0.00076462, None, -0.00126628, None, -0.00076462, None, -0.00126628, None, 0.238258, None, 0.00513761, None, 0.238258, None, 0.00513761, None)

reports.append(Report(604050128, ("CSC", 2, 1, 4, 26), "MEm14_26"))
reports[-1].posNum = 99532
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000420258, 0.000785267, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(8.78358e-06, 1.98764e-05, 0), \
                           -1871.05, 99532, 99532, -nan)
reports[-1].sigmaresid = ValErr(0.246562, 0.000552625, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000519036, None, -0.00737682, None, 0.000386037, None, -0.00708414, None, 0.000386037, None, -0.00708414, None, -0.000403835, None, -0.00739558, None, -0.000403835, None, -0.00739558, None, 0.246563, None, 0.00574305, None, 0.246563, None, 0.00574305, None)

reports.append(Report(604050144, ("CSC", 2, 1, 4, 28), "MEm14_28"))
reports[-1].posNum = 125022
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000121209, 0.000671149, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.00881e-05, 1.62663e-05, 0), \
                           3104.17, 125022, 125022, -nan)
reports[-1].sigmaresid = ValErr(0.236038, 0.000472036, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00066383, None, -0.000345497, None, -3.54755e-05, None, -0.000419195, None, -3.54755e-05, None, -0.000419195, None, -0.000785107, None, -0.000400508, None, -0.000785107, None, -0.000400508, None, 0.236038, None, 0.00582678, None, 0.236038, None, 0.00582678, None)

reports.append(Report(604050160, ("CSC", 2, 1, 4, 30), "MEm14_30"))
reports[-1].posNum = 128392
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000480536, 0.000657227, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.02313e-06, 1.57582e-05, 0), \
                           4165.3, 128392, 128392, -nan)
reports[-1].sigmaresid = ValErr(0.234247, 0.000462263, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000721064, None, -0.00266111, None, 0.000463274, None, -0.00258415, None, 0.000463274, None, -0.00258415, None, 0.000162889, None, -0.002642, None, 0.000162889, None, -0.002642, None, 0.234247, None, 0.00546825, None, 0.234247, None, 0.00546825, None)

reports.append(Report(604050176, ("CSC", 2, 1, 4, 32), "MEm14_32"))
reports[-1].posNum = 125010
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000143112, 0.000671428, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.97103e-06, 1.62248e-05, 0), \
                           2945.88, 125010, 125010, -nan)
reports[-1].sigmaresid = ValErr(0.236335, 0.000472651, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00102616, None, -0.000542889, None, -0.000162494, None, -0.000571752, None, -0.000162494, None, -0.000571752, None, -0.000408332, None, -0.000577884, None, -0.000408332, None, -0.000577884, None, 0.236335, None, 0.00519903, None, 0.236335, None, 0.00519903, None)

reports.append(Report(604050192, ("CSC", 2, 1, 4, 34), "MEm14_34"))
reports[-1].posNum = 126998
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000232714, 0.000662566, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.40549e-06, 1.58652e-05, 0), \
                           4221.8, 126998, 126998, -nan)
reports[-1].sigmaresid = ValErr(0.234059, 0.000464421, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00180452, None, 0.00107007, None, -0.000219479, None, 0.000977572, None, -0.000219479, None, 0.000977572, None, -0.00253755, None, 0.000998456, None, -0.00253755, None, 0.000998456, None, 0.234059, None, 0.00556206, None, 0.234059, None, 0.00556206, None)

reports.append(Report(604050208, ("CSC", 2, 1, 4, 36), "MEm14_36"))
reports[-1].posNum = 128190
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000297344, 0.000659934, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(8.03921e-06, 1.5817e-05, 0), \
                           3788.28, 128190, 128190, -nan)
reports[-1].sigmaresid = ValErr(0.234925, 0.000463968, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00135105, None, 0.000121638, None, -0.000261913, None, 9.84765e-05, None, -0.000261913, None, 9.84765e-05, None, 2.56065e-05, None, 0.000105476, None, 2.56065e-05, None, 0.000105476, None, 0.234925, None, 0.00528915, None, 0.234925, None, 0.00528915, None)

reports.append(Report(604054024, ("CSC", 2, 2, 1, 1), "MEm21_01"))
reports[-1].posNum = 212852
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000375281, 0.00125516, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.92172e-06, 2.38069e-05, 0), \
                           -184034, 212852, 212852, -nan)
reports[-1].sigmaresid = ValErr(0.574459, 0.000880453, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00138937, None, -8.4098e-05, None, -0.00040161, None, -0.000510138, None, -0.00040161, None, -0.000510138, None, 0.000253454, None, -0.000545675, None, 0.000253454, None, -0.000545675, None, 0.574459, None, 0.00724935, None, 0.574459, None, 0.00724935, None)

reports.append(Report(604054040, ("CSC", 2, 2, 1, 3), "MEm21_03"))
reports[-1].posNum = 60068
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00173054, 0.00233127, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(9.92198e-06, 4.51187e-05, 0), \
                           -51211.8, 60068, 60068, -nan)
reports[-1].sigmaresid = ValErr(0.56758, 0.00163754, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0012702, None, -4.21761e-05, None, -0.00166866, None, -0.000348207, None, -0.00166866, None, -0.000348207, None, -0.00418009, None, -0.000380949, None, -0.00418009, None, -0.000380949, None, 0.567579, None, 0.00693463, None, 0.567579, None, 0.00693463, None)

reports.append(Report(604054056, ("CSC", 2, 2, 1, 5), "MEm21_05"))
reports[-1].posNum = 197834
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000772864, 0.00128423, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.70944e-05, 2.44149e-05, 0), \
                           -168644, 197834, 197834, -nan)
reports[-1].sigmaresid = ValErr(0.567516, 0.000902223, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00209777, None, -0.000340008, None, 0.000670521, None, -0.000730659, None, 0.000670521, None, -0.000730659, None, 0.00123542, None, -0.00075029, None, 0.00123542, None, -0.00075029, None, 0.567515, None, 0.00708538, None, 0.567515, None, 0.00708538, None)

reports.append(Report(604054072, ("CSC", 2, 2, 1, 7), "MEm21_07"))
reports[-1].posNum = 210186
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000476813, 0.00125256, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.90923e-06, 2.39364e-05, 0), \
                           -180040, 210186, 210186, -nan)
reports[-1].sigmaresid = ValErr(0.569861, 0.000878927, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000164475, None, -0.000560317, None, -0.000437699, None, -0.000905697, None, -0.000437699, None, -0.000905697, None, -0.00136263, None, -0.000955352, None, -0.00136263, None, -0.000955352, None, 0.56986, None, 0.00700475, None, 0.56986, None, 0.00700475, None)

reports.append(Report(604054088, ("CSC", 2, 2, 1, 9), "MEm21_09"))
reports[-1].posNum = 178064
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000434835, 0.00138012, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.4077e-07, 2.57794e-05, 0), \
                           -156014, 178064, 178064, -nan)
reports[-1].sigmaresid = ValErr(0.581135, 0.00097381, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000371976, None, 0.000224071, None, 0.000436468, None, 3.51868e-05, None, 0.000436468, None, 3.51868e-05, None, -0.00246327, None, 6.25309e-05, None, -0.00246327, None, 6.25309e-05, None, 0.581135, None, 0.0074018, None, 0.581135, None, 0.0074018, None)

reports.append(Report(604054104, ("CSC", 2, 2, 1, 11), "MEm21_11"))
reports[-1].posNum = 208510
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000354768, 0.00125184, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.39586e-05, 2.37322e-05, 0), \
                           -177391, 208510, 208510, -nan)
reports[-1].sigmaresid = ValErr(0.566553, 0.000877329, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00127523, None, -0.00018799, None, 0.000453221, None, -0.000480492, None, 0.000453221, None, -0.000480492, None, -0.00041214, None, -0.000461353, None, -0.00041214, None, -0.000461353, None, 0.566553, None, 0.00704387, None, 0.566553, None, 0.00704387, None)

reports.append(Report(604054120, ("CSC", 2, 2, 1, 13), "MEm21_13"))
reports[-1].posNum = 181284
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000817743, 0.00136696, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.04446e-05, 2.68362e-05, 0), \
                           -159093, 181284, 181284, -nan)
reports[-1].sigmaresid = ValErr(0.581965, 0.000966503, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00356638, None, -3.39317e-05, None, -0.000802146, None, -0.00031372, None, -0.000802146, None, -0.00031372, None, 0.00081137, None, -0.000326316, None, 0.00081137, None, -0.000326316, None, 0.581964, None, 0.00757098, None, 0.581964, None, 0.00757098, None)

reports.append(Report(604054136, ("CSC", 2, 2, 1, 15), "MEm21_15"))
reports[-1].posNum = 218156
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00053548, 0.00122305, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.14455e-06, 2.33081e-05, 0), \
                           -185262, 218156, 218156, -nan)
reports[-1].sigmaresid = ValErr(0.565685, 0.000856399, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00423111, None, -0.00065209, None, 0.000580327, None, -0.0010526, None, 0.000580327, None, -0.0010526, None, 0.000815388, None, -0.0010978, None, 0.000815388, None, -0.0010978, None, 0.565684, None, 0.00718489, None, 0.565684, None, 0.00718489, None)

reports.append(Report(604054152, ("CSC", 2, 2, 1, 17), "MEm21_17"))
reports[-1].posNum = 147672
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000895461, 0.0014834, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.24834e-05, 2.77426e-05, 0), \
                           -125789, 147672, 147672, -nan)
reports[-1].sigmaresid = ValErr(0.567153, 0.00104361, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00373168, None, -0.000652795, None, 0.000774609, None, -0.000961571, None, 0.000774609, None, -0.000961571, None, 0.00103523, None, -0.000995367, None, 0.00103523, None, -0.000995367, None, 0.567153, None, 0.00770118, None, 0.567153, None, 0.00770118, None)

reports.append(Report(604054032, ("CSC", 2, 2, 1, 2), "MEm21_02"))
reports[-1].posNum = 225632
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000134781, 0.00115893, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.57348e-06, 2.10162e-05, 0), \
                           -180003, 225632, 225632, -nan)
reports[-1].sigmaresid = ValErr(0.537317, 0.000799863, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00212238, None, -1.62124e-05, None, 0.000176603, None, -0.000323193, None, 0.000176603, None, -0.000323193, None, 0.000337801, None, -0.000318315, None, 0.000337801, None, -0.000318315, None, 0.537317, None, 0.00766398, None, 0.537317, None, 0.00766398, None)

reports.append(Report(604054048, ("CSC", 2, 2, 1, 4), "MEm21_04"))
reports[-1].posNum = 212882
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000858333, 0.00119206, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.00591e-05, 2.21647e-05, 0), \
                           -171464, 212882, 212882, -nan)
reports[-1].sigmaresid = ValErr(0.541454, 0.000829807, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000346269, None, 0.000614297, None, 0.000480272, None, 0.000478859, None, 0.000480272, None, 0.000478859, None, -0.000830759, None, 0.000471361, None, -0.000830759, None, 0.000471361, None, 0.541458, None, 0.00735765, None, 0.541458, None, 0.00735765, None)

reports.append(Report(604054064, ("CSC", 2, 2, 1, 6), "MEm21_06"))
reports[-1].posNum = 216914
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000802292, 0.00117287, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.79458e-05, 2.13211e-05, 0), \
                           -171805, 216914, 216914, -nan)
reports[-1].sigmaresid = ValErr(0.534248, 0.000811119, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000679659, None, 5.95598e-05, None, -0.000596356, None, -0.000206669, None, -0.000596356, None, -0.000206669, None, -0.000795911, None, -0.000196219, None, -0.000795911, None, -0.000196219, None, 0.534249, None, 0.00705493, None, 0.534249, None, 0.00705493, None)

reports.append(Report(604054080, ("CSC", 2, 2, 1, 8), "MEm21_08"))
reports[-1].posNum = 198408
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000240405, 0.00125092, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(9.3895e-06, 2.26343e-05, 0), \
                           -163514, 198408, 198408, -nan)
reports[-1].sigmaresid = ValErr(0.551669, 0.000875758, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00082011, None, -0.000788359, None, -0.000167276, None, -0.00112029, None, -0.000167276, None, -0.00112029, None, 0.000883009, None, -0.00118486, None, 0.000883009, None, -0.00118486, None, 0.551669, None, 0.00752452, None, 0.551669, None, 0.00752452, None)

reports.append(Report(604054096, ("CSC", 2, 2, 1, 10), "MEm21_10"))
reports[-1].posNum = 181082
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000902468, 0.00130907, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.06932e-05, 2.42376e-05, 0), \
                           -150122, 181082, 181082, -nan)
reports[-1].sigmaresid = ValErr(0.554377, 0.000921197, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000600873, None, 0.000717535, None, 0.000844955, None, 0.000581862, None, 0.000844955, None, 0.000581862, None, 0.00062491, None, 0.000654156, None, 0.00062491, None, 0.000654156, None, 0.554377, None, 0.00778776, None, 0.554377, None, 0.00778776, None)

reports.append(Report(604054112, ("CSC", 2, 2, 1, 12), "MEm21_12"))
reports[-1].posNum = 212698
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000118344, 0.00119206, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.82464e-06, 2.24646e-05, 0), \
                           -171448, 212698, 212698, -nan)
reports[-1].sigmaresid = ValErr(0.541792, 0.000830683, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00257088, None, -0.0011189, None, 0.000134824, None, -0.00151502, None, 0.000134824, None, -0.00151502, None, 0.000750826, None, -0.00155144, None, 0.000750826, None, -0.00155144, None, 0.541792, None, 0.00740266, None, 0.541792, None, 0.00740266, None)

reports.append(Report(604054128, ("CSC", 2, 2, 1, 14), "MEm21_14"))
reports[-1].posNum = 217160
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00132124, 0.00118172, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.40321e-05, 2.21808e-05, 0), \
                           -175342, 217160, 217160, -nan)
reports[-1].sigmaresid = ValErr(0.542534, 0.000823233, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00511818, None, -0.00117045, None, -0.00119284, None, -0.00151088, None, -0.00119284, None, -0.00151088, None, -0.000422262, None, -0.00156697, None, -0.000422262, None, -0.00156697, None, 0.542535, None, 0.00740815, None, 0.542535, None, 0.00740815, None)

reports.append(Report(604054144, ("CSC", 2, 2, 1, 16), "MEm21_16"))
reports[-1].posNum = 221052
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000910937, 0.00116543, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.32905e-05, 2.15447e-05, 0), \
                           -176697, 221052, 221052, -nan)
reports[-1].sigmaresid = ValErr(0.538163, 0.000809379, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00186379, None, -0.000557544, None, 0.000673893, None, -0.000805057, None, 0.000673893, None, -0.000805057, None, 0.000776081, None, -0.00084123, None, 0.000776081, None, -0.00084123, None, 0.538165, None, 0.00735988, None, 0.538165, None, 0.00735988, None)

reports.append(Report(604054160, ("CSC", 2, 2, 1, 18), "MEm21_18"))
reports[-1].posNum = 178862
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-5.93162e-06, 0.00131024, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.98579e-06, 2.4024e-05, 0), \
                           -144733, 178862, 178862, -nan)
reports[-1].sigmaresid = ValErr(0.543486, 0.000908687, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000835098, None, -0.000567273, None, -3.72992e-05, None, -0.000938873, None, -3.72992e-05, None, -0.000938873, None, 0.00137096, None, -0.00089662, None, 0.00137096, None, -0.00089662, None, 0.543486, None, 0.00752996, None, 0.543486, None, 0.00752996, None)

reports.append(Report(604054536, ("CSC", 2, 2, 2, 1), "MEm22_01"))
reports[-1].posNum = 75534
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00549479, 0.005561, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.44376e-05, 5.60049e-05, 0), \
                           -129953, 75534, 75534, -nan)
reports[-1].sigmaresid = ValErr(1.35191, 0.00347827, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0081006, None, -0.000678182, None, 0.00389983, None, -0.00066341, None, 0.00389983, None, -0.00066341, None, 0.00282349, None, -0.000658242, None, 0.00282349, None, -0.000658242, None, 1.35192, None, 0.00837137, None, 1.35192, None, 0.00837137, None)

reports.append(Report(604054552, ("CSC", 2, 2, 2, 3), "MEm22_03"))
reports[-1].posNum = 48726
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00278398, 0.00715934, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.53334e-05, 6.91936e-05, 0), \
                           -80028.5, 48726, 48726, -nan)
reports[-1].sigmaresid = ValErr(1.25042, 0.00400553, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00358469, None, 0.000804739, None, 0.00118087, None, 0.000573823, None, 0.00118087, None, 0.000573823, None, -0.00189011, None, 0.000776098, None, -0.00189011, None, 0.000776098, None, 1.25042, None, 0.00815427, None, 1.25042, None, 0.00815427, None)

reports.append(Report(604054568, ("CSC", 2, 2, 2, 5), "MEm22_05"))
reports[-1].posNum = 57186
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00789915, 0.00702564, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.03781e-05, 6.65733e-05, 0), \
                           -91409.2, 57186, 57186, -nan)
reports[-1].sigmaresid = ValErr(1.19664, 0.00353836, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00289813, None, -0.00111789, None, 0.00268617, None, -0.00123566, None, 0.00268617, None, -0.00123566, None, -0.00325337, None, -0.00131375, None, -0.00325337, None, -0.00131375, None, 1.19665, None, 0.00737999, None, 1.19665, None, 0.00737999, None)

reports.append(Report(604054584, ("CSC", 2, 2, 2, 7), "MEm22_07"))
reports[-1].posNum = 58002
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00632934, 0.0071328, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.92426e-05, 6.77059e-05, 0), \
                           -93120.8, 58002, 58002, -nan)
reports[-1].sigmaresid = ValErr(1.20507, 0.00353815, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00293915, None, -0.000238258, None, -0.00263246, None, -0.000374673, None, -0.00263246, None, -0.000374673, None, 0.00155115, None, -0.000325021, None, 0.00155115, None, -0.000325021, None, 1.20508, None, 0.00744715, None, 1.20508, None, 0.00744715, None)

reports.append(Report(604054600, ("CSC", 2, 2, 2, 9), "MEm22_09"))
reports[-1].posNum = 64324
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0074377, 0.00620607, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.64077e-05, 6.10275e-05, 0), \
                           -107463, 64324, 64324, -nan)
reports[-1].sigmaresid = ValErr(1.28623, 0.00358605, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00256505, None, -0.000187407, None, 0.002372, None, -0.000347397, None, 0.002372, None, -0.000347397, None, 0.00213896, None, -0.000348284, None, 0.00213896, None, -0.000348284, None, 1.28625, None, 0.00881164, None, 1.28625, None, 0.00881164, None)

reports.append(Report(604054616, ("CSC", 2, 2, 2, 11), "MEm22_11"))
reports[-1].posNum = 65520
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00055069, 0.00625607, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.77048e-06, 6.13221e-05, 0), \
                           -110208, 65520, 65520, -nan)
reports[-1].sigmaresid = ValErr(1.30098, 0.00359394, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000399182, None, -6.82365e-05, None, -0.00113109, None, -0.000110908, None, -0.00113109, None, -0.000110908, None, -0.00239817, None, -0.00011049, None, -0.00239817, None, -0.00011049, None, 1.30098, None, 0.0082645, None, 1.30098, None, 0.0082645, None)

reports.append(Report(604054632, ("CSC", 2, 2, 2, 13), "MEm22_13"))
reports[-1].posNum = 54490
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0109477, 0.00709203, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.50337e-05, 6.77944e-05, 0), \
                           -88472.2, 54490, 54490, -nan)
reports[-1].sigmaresid = ValErr(1.22716, 0.0037173, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00539903, None, -0.000160437, None, 0.00567904, None, -0.000157748, None, 0.00567904, None, -0.000157748, None, 0.0100468, None, -0.000181635, None, 0.0100468, None, -0.000181635, None, 1.22717, None, 0.00778629, None, 1.22717, None, 0.00778629, None)

reports.append(Report(604054648, ("CSC", 2, 2, 2, 15), "MEm22_15"))
reports[-1].posNum = 60164
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00533434, 0.00725901, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.29094e-05, 6.94846e-05, 0), \
                           -97896.2, 60164, 60164, -nan)
reports[-1].sigmaresid = ValErr(1.23148, 0.00355013, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00500446, None, 0.000235176, None, -0.000587475, None, 0.0001869, None, -0.000587475, None, 0.0001869, None, -0.000545403, None, 0.000261675, None, -0.000545403, None, 0.000261675, None, 1.23149, None, 0.00719038, None, 1.23149, None, 0.00719038, None)

reports.append(Report(604054664, ("CSC", 2, 2, 2, 17), "MEm22_17"))
reports[-1].posNum = 54426
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0139742, 0.00690745, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000128598, 6.34133e-05, 0), \
                           -88631.3, 54426, 54426, -nan)
reports[-1].sigmaresid = ValErr(1.23311, 0.0037375, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00183911, None, 0.000131735, None, -0.00495637, None, 6.88347e-05, None, -0.00495637, None, 6.88347e-05, None, -0.0127126, None, 0.000107528, None, -0.0127126, None, 0.000107528, None, 1.23315, None, 0.00910081, None, 1.23315, None, 0.00910081, None)

reports.append(Report(604054680, ("CSC", 2, 2, 2, 19), "MEm22_19"))
reports[-1].posNum = 71832
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0114718, 0.00572204, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000139055, 5.69458e-05, 0), \
                           -121202, 71832, 71832, -nan)
reports[-1].sigmaresid = ValErr(1.30782, 0.00345043, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00385979, None, -5.74681e-05, None, -0.0041722, None, -0.000369961, None, -0.0041722, None, -0.000369961, None, 0.000747837, None, -0.000406667, None, 0.000747837, None, -0.000406667, None, 1.30788, None, 0.00811915, None, 1.30788, None, 0.00811915, None)

reports.append(Report(604054696, ("CSC", 2, 2, 2, 21), "MEm22_21"))
reports[-1].posNum = 63606
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0283085, 0.00619034, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000260836, 5.97235e-05, 0), \
                           -104249, 63606, 63606, -nan)
reports[-1].sigmaresid = ValErr(1.24613, 0.00349381, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00349908, None, -0.00102619, None, -0.0120217, None, -0.00127441, None, -0.0120217, None, -0.00127441, None, -0.00235498, None, -0.00128207, None, -0.00235498, None, -0.00128207, None, 1.24632, None, 0.00768129, None, 1.24632, None, 0.00768129, None)

reports.append(Report(604054712, ("CSC", 2, 2, 2, 23), "MEm22_23"))
reports[-1].posNum = 72410
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00294095, 0.00563089, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.7635e-05, 5.66499e-05, 0), \
                           -121566, 72410, 72410, -nan)
reports[-1].sigmaresid = ValErr(1.29683, 0.00340776, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0011709, None, -0.000442764, None, -0.00152001, None, -0.000546009, None, -0.00152001, None, -0.000546009, None, -0.00584835, None, -0.00055529, None, -0.00584835, None, -0.00055529, None, 1.29683, None, 0.00824971, None, 1.29683, None, 0.00824971, None)

reports.append(Report(604054728, ("CSC", 2, 2, 2, 25), "MEm22_25"))
reports[-1].posNum = 52856
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0128348, 0.0069204, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000166538, 6.43034e-05, 0), \
                           -86101.8, 52856, 52856, -nan)
reports[-1].sigmaresid = ValErr(1.23374, 0.00379455, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00302773, None, -0.000170136, None, -0.00151747, None, -0.000298588, None, -0.00151747, None, -0.000298588, None, 0.000938854, None, -0.000277398, None, 0.000938854, None, -0.000277398, None, 1.23382, None, 0.0077378, None, 1.23382, None, 0.0077378, None)

reports.append(Report(604054744, ("CSC", 2, 2, 2, 27), "MEm22_27"))
reports[-1].posNum = 46424
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0164339, 0.00756209, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000125878, 7.00903e-05, 0), \
                           -74600.6, 46424, 46424, -nan)
reports[-1].sigmaresid = ValErr(1.20683, 0.0039606, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0070792, None, -0.000269194, None, -0.00731035, None, -0.000225264, None, -0.00731035, None, -0.000225264, None, -0.0029311, None, -0.000233014, None, -0.0029311, None, -0.000233014, None, 1.20688, None, 0.0080634, None, 1.20688, None, 0.0080634, None)

reports.append(Report(604054760, ("CSC", 2, 2, 2, 29), "MEm22_29"))
reports[-1].posNum = 55682
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00655711, 0.00659834, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.11605e-05, 6.20999e-05, 0), \
                           -91917.7, 55682, 55682, -nan)
reports[-1].sigmaresid = ValErr(1.2609, 0.00377839, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00508404, None, -0.000517843, None, 0.00274415, None, -0.000651923, None, 0.00274415, None, -0.000651923, None, 0.00550137, None, -0.000661664, None, 0.00550137, None, -0.000661664, None, 1.26091, None, 0.00762107, None, 1.26091, None, 0.00762107, None)

reports.append(Report(604054776, ("CSC", 2, 2, 2, 31), "MEm22_31"))
reports[-1].posNum = 44822
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0175799, 0.00753859, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000124288, 7.03993e-05, 0), \
                           -73173.6, 44822, 44822, -nan)
reports[-1].sigmaresid = ValErr(1.23813, 0.00413527, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.010439, None, 0.000346157, None, -0.0091816, None, 0.000274431, None, -0.0091816, None, 0.000274431, None, -0.00974717, None, 0.000343244, None, -0.00974717, None, 0.000343244, None, 1.23817, None, 0.0077543, None, 1.23817, None, 0.0077543, None)

reports.append(Report(604054792, ("CSC", 2, 2, 2, 33), "MEm22_33"))
reports[-1].posNum = 60094
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0136079, 0.00649496, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000112817, 6.21337e-05, 0), \
                           -98208.8, 60094, 60094, -nan)
reports[-1].sigmaresid = ValErr(1.24025, 0.00357749, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00841804, None, -9.69277e-05, None, 0.00621345, None, -0.000108373, None, 0.00621345, None, -0.000108373, None, 0.0163865, None, -0.000163661, None, 0.0163865, None, -0.000163661, None, 1.24029, None, 0.00790595, None, 1.24029, None, 0.00790595, None)

reports.append(Report(604054808, ("CSC", 2, 2, 2, 35), "MEm22_35"))
reports[-1].posNum = 65554
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00330601, 0.00598837, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.87803e-05, 5.78174e-05, 0), \
                           -109955, 65554, 65554, -nan)
reports[-1].sigmaresid = ValErr(1.29484, 0.00357602, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00077128, None, 0.000179093, None, 0.00115433, None, 0.000171298, None, 0.00115433, None, 0.000171298, None, 0.00371166, None, 0.000147573, None, 0.00371166, None, 0.000147573, None, 1.29484, None, 0.00812583, None, 1.29484, None, 0.00812583, None)

reports.append(Report(604054544, ("CSC", 2, 2, 2, 2), "MEm22_02"))
reports[-1].posNum = 68596
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00402288, 0.00577852, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.56617e-05, 5.69424e-05, 0), \
                           -117108, 68596, 68596, -nan)
reports[-1].sigmaresid = ValErr(1.33412, 0.00360187, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00238843, None, -0.00060088, None, 0.00135356, None, -0.00073473, None, 0.00135356, None, -0.00073473, None, 0.000749146, None, -0.000766775, None, 0.000749146, None, -0.000766775, None, 1.33414, None, 0.00883245, None, 1.33414, None, 0.00883245, None)

reports.append(Report(604054560, ("CSC", 2, 2, 2, 4), "MEm22_04"))
reports[-1].posNum = 50466
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00990508, 0.00748896, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.80593e-05, 6.91731e-05, 0), \
                           -80610.7, 50466, 50466, -nan)
reports[-1].sigmaresid = ValErr(1.19529, 0.00376234, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00190216, None, -0.0010885, None, 0.00243408, None, -0.00112378, None, 0.00243408, None, -0.00112378, None, 0.000975849, None, -0.00108796, None, 0.000975849, None, -0.00108796, None, 1.19531, None, 0.00815067, None, 1.19531, None, 0.00815067, None)

reports.append(Report(604054576, ("CSC", 2, 2, 2, 6), "MEm22_06"))
reports[-1].posNum = 51536
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00496329, 0.00751579, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.84967e-05, 7.16327e-05, 0), \
                           -81602.4, 51536, 51536, -nan)
reports[-1].sigmaresid = ValErr(1.17877, 0.00367161, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00467088, None, -0.00064151, None, -0.00128444, None, -0.000762969, None, -0.00128444, None, -0.000762969, None, 0.0051168, None, -0.000804454, None, 0.0051168, None, -0.000804454, None, 1.17877, None, 0.00793934, None, 1.17877, None, 0.00793934, None)

reports.append(Report(604054592, ("CSC", 2, 2, 2, 8), "MEm22_08"))
reports[-1].posNum = 49604
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00366271, 0.00706235, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.29847e-05, 6.59689e-05, 0), \
                           -79517, 49604, 49604, -nan)
reports[-1].sigmaresid = ValErr(1.20213, 0.00381662, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000712334, None, 0.000508708, None, 0.000686082, None, 0.000200326, None, 0.000686082, None, 0.000200326, None, 0.000570496, None, 0.000183468, None, 0.000570496, None, 0.000183468, None, 1.20214, None, 0.00811555, None, 1.20214, None, 0.00811555, None)

reports.append(Report(604054608, ("CSC", 2, 2, 2, 10), "MEm22_10"))
reports[-1].posNum = 67232
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00797049, 0.00592148, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.14076e-05, 5.9139e-05, 0), \
                           -112933, 67232, 67232, -nan)
reports[-1].sigmaresid = ValErr(1.29797, 0.00353967, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00143209, None, -6.54212e-05, None, 0.00415111, None, -7.82025e-05, None, 0.00415111, None, -7.82025e-05, None, 0.00854191, None, -9.73658e-05, None, 0.00854191, None, -9.73658e-05, None, 1.29799, None, 0.00849745, None, 1.29799, None, 0.00849745, None)

reports.append(Report(604054624, ("CSC", 2, 2, 2, 12), "MEm22_12"))
reports[-1].posNum = 54724
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00235328, 0.0071053, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.34278e-06, 6.68121e-05, 0), \
                           -86681.8, 54724, 54724, -nan)
reports[-1].sigmaresid = ValErr(1.17945, 0.00356513, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00750949, None, -0.000138648, None, 0.00173667, None, -0.000233366, None, 0.00173667, None, -0.000233366, None, 0.0150188, None, -0.000306319, None, 0.0150188, None, -0.000306319, None, 1.17944, None, 0.00796855, None, 1.17944, None, 0.00796855, None)

reports.append(Report(604054640, ("CSC", 2, 2, 2, 14), "MEm22_14"))
reports[-1].posNum = 64806
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000521088, 0.00622207, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.05462e-05, 6.10183e-05, 0), \
                           -106034, 64806, 64806, -nan)
reports[-1].sigmaresid = ValErr(1.24264, 0.00345163, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0021498, None, 0.000504549, None, -0.00182054, None, 0.000118041, None, -0.00182054, None, 0.000118041, None, -0.00157979, None, 0.000130421, None, -0.00157979, None, 0.000130421, None, 1.24264, None, 0.00837906, None, 1.24264, None, 0.00837906, None)

reports.append(Report(604054656, ("CSC", 2, 2, 2, 16), "MEm22_16"))
reports[-1].posNum = 47034
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0298398, 0.00832038, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000254955, 7.45376e-05, 0), \
                           -75197.8, 47034, 47034, -nan)
reports[-1].sigmaresid = ValErr(1.19705, 0.00390291, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00329878, None, -0.000817694, None, -0.0085454, None, -0.000991024, None, -0.0085454, None, -0.000991024, None, -0.0025619, None, -0.00102006, None, -0.0025619, None, -0.00102006, None, 1.1972, None, 0.00763033, None, 1.1972, None, 0.00763033, None)

reports.append(Report(604054672, ("CSC", 2, 2, 2, 18), "MEm22_18"))
reports[-1].posNum = 58756
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00583396, 0.00622113, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.3954e-05, 6.01221e-05, 0), \
                           -98313.7, 58756, 58756, -nan)
reports[-1].sigmaresid = ValErr(1.28958, 0.00376188, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00604629, None, 0.000291122, None, -0.00293948, None, 0.00022955, None, -0.00293948, None, 0.00022955, None, 0.00476394, None, 0.000263187, None, 0.00476394, None, 0.000263187, None, 1.28959, None, 0.00878898, None, 1.28959, None, 0.00878898, None)

reports.append(Report(604054688, ("CSC", 2, 2, 2, 20), "MEm22_20"))
reports[-1].posNum = 57190
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00995118, 0.00638034, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(9.42753e-05, 6.0801e-05, 0), \
                           -96207.3, 57190, 57190, -nan)
reports[-1].sigmaresid = ValErr(1.30122, 0.00384747, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00715111, None, -0.00138069, None, -0.00478316, None, -0.00168468, None, -0.00478316, None, -0.00168468, None, 0.00609713, None, -0.00185337, None, 0.00609713, None, -0.00185337, None, 1.30125, None, 0.00859709, None, 1.30125, None, 0.00859709, None)

reports.append(Report(604054704, ("CSC", 2, 2, 2, 22), "MEm22_22"))
reports[-1].posNum = 59796
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0236133, 0.00634801, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.00023033, 6.13762e-05, 0), \
                           -100235, 59796, 59796, -nan)
reports[-1].sigmaresid = ValErr(1.2935, 0.00374036, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00338553, None, 0.000515902, None, -0.0104429, None, 0.000169268, None, -0.0104429, None, 0.000169268, None, -0.0121842, None, 0.000135228, None, -0.0121842, None, 0.000135228, None, 1.29365, None, 0.00849529, None, 1.29365, None, 0.00849529, None)

reports.append(Report(604054720, ("CSC", 2, 2, 2, 24), "MEm22_24"))
reports[-1].posNum = 64092
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0129789, 0.00634615, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000135857, 6.28693e-05, 0), \
                           -105211, 64092, 64092, -nan)
reports[-1].sigmaresid = ValErr(1.24935, 0.00348954, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00257676, None, -4.0073e-05, None, -0.00435657, None, -0.000259298, None, -0.00435657, None, -0.000259298, None, -0.00256773, None, -0.000207234, None, -0.00256773, None, -0.000207234, None, 1.2494, None, 0.00863257, None, 1.2494, None, 0.00863257, None)

reports.append(Report(604054736, ("CSC", 2, 2, 2, 26), "MEm22_26"))
reports[-1].posNum = 39918
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0178461, 0.00807249, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000152427, 7.18229e-05, 0), \
                           -63216.1, 39918, 39918, -nan)
reports[-1].sigmaresid = ValErr(1.17905, 0.00417285, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000479831, None, -0.00086205, None, 0.00615679, None, -0.000846684, None, 0.00615679, None, -0.000846684, None, 0.00714511, None, -0.000823516, None, 0.00714511, None, -0.000823516, None, 1.17912, None, 0.00761733, None, 1.17912, None, 0.00761733, None)

reports.append(Report(604054752, ("CSC", 2, 2, 2, 28), "MEm22_28"))
reports[-1].posNum = 52034
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00870226, 0.00695418, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.75963e-05, 6.74003e-05, 0), \
                           -86017.1, 52034, 52034, -nan)
reports[-1].sigmaresid = ValErr(1.26384, 0.00391772, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000881391, None, -0.000666081, None, 0.00324, None, -0.000739918, None, 0.00324, None, -0.000739918, None, 0.0051529, None, -0.000802333, None, 0.0051529, None, -0.000802333, None, 1.26386, None, 0.00843794, None, 1.26386, None, 0.00843794, None)

reports.append(Report(604054768, ("CSC", 2, 2, 2, 30), "MEm22_30"))
reports[-1].posNum = 40210
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00404324, 0.00787177, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.49758e-05, 7.21902e-05, 0), \
                           -64605.9, 40210, 40210, -nan)
reports[-1].sigmaresid = ValErr(1.20656, 0.00425468, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00267123, None, 0.000145217, None, 0.000177554, None, -0.000240182, None, 0.000177554, None, -0.000240182, None, 0.000757057, None, -0.000281386, None, 0.000757057, None, -0.000281386, None, 1.20657, None, 0.00861997, None, 1.20657, None, 0.00861997, None)

reports.append(Report(604054784, ("CSC", 2, 2, 2, 32), "MEm22_32"))
reports[-1].posNum = 53978
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00417982, 0.0066014, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.68072e-05, 6.32153e-05, 0), \
                           -87992.1, 53978, 53978, -nan)
reports[-1].sigmaresid = ValErr(1.23517, 0.00375927, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000800744, None, -3.14877e-05, None, 0.000662147, None, 0.000113727, None, 0.000662147, None, 0.000113727, None, 0.00960836, None, 5.50308e-05, None, 0.00960836, None, 5.50308e-05, None, 1.23518, None, 0.00845892, None, 1.23518, None, 0.00845892, None)

reports.append(Report(604054800, ("CSC", 2, 2, 2, 34), "MEm22_34"))
reports[-1].posNum = 62436
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00302618, 0.00597881, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.667e-05, 5.74152e-05, 0), \
                           -103971, 62436, 62436, -nan)
reports[-1].sigmaresid = ValErr(1.27928, 0.0036202, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00514978, None, -0.00109206, None, 0.00159147, None, -0.000992688, None, 0.00159147, None, -0.000992688, None, 0.00732105, None, -0.000982546, None, 0.00732105, None, -0.000982546, None, 1.27928, None, 0.0086204, None, 1.27928, None, 0.0086204, None)

reports.append(Report(604054816, ("CSC", 2, 2, 2, 36), "MEm22_36"))
reports[-1].posNum = 62876
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00231836, 0.00604817, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.48755e-05, 5.95111e-05, 0), \
                           -105503, 62876, 62876, -nan)
reports[-1].sigmaresid = ValErr(1.29564, 0.00365363, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00193206, None, 0.000262091, None, -5.66048e-05, None, 0.000169134, None, -5.66048e-05, None, 0.000169134, None, 0.00114446, None, 0.000210987, None, 0.00114446, None, 0.000210987, None, 1.29565, None, 0.00855287, None, 1.29565, None, 0.00855287, None)

reports.append(Report(604058120, ("CSC", 2, 3, 1, 1), "MEm31_01"))
reports[-1].posNum = 163926
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000548901, 0.00168295, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.08747e-05, 3.46379e-05, 0), \
                           -168509, 163926, 163926, -nan)
reports[-1].sigmaresid = ValErr(0.676392, 0.0011813, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-1.89497e-05, None, 0.000464654, None, 0.000612571, None, 0.000223545, None, 0.000612571, None, 0.000223545, None, 0.00154462, None, 0.000230866, None, 0.00154462, None, 0.000230866, None, 0.676392, None, 0.00811472, None, 0.676392, None, 0.00811472, None)

reports.append(Report(604058136, ("CSC", 2, 3, 1, 3), "MEm31_03"))
reports[-1].posNum = 153010
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000588592, 0.00173268, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.44112e-05, 3.7387e-05, 0), \
                           -154224, 153010, 153010, -nan)
reports[-1].sigmaresid = ValErr(0.662983, 0.00119847, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00212056, None, 0.000208545, None, -0.000450986, None, -0.000199347, None, -0.000450986, None, -0.000199347, None, -0.00171387, None, -0.000226313, None, -0.00171387, None, -0.000226313, None, 0.662983, None, 0.00804048, None, 0.662983, None, 0.00804048, None)

reports.append(Report(604058152, ("CSC", 2, 3, 1, 5), "MEm31_05"))
reports[-1].posNum = 167072
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000409868, 0.00163981, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.13821e-06, 3.42042e-05, 0), \
                           -169138, 167072, 167072, -nan)
reports[-1].sigmaresid = ValErr(0.66593, 0.00115202, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00389447, None, 0.000706433, None, 0.000426021, None, 0.000482433, None, 0.000426021, None, 0.000482433, None, 0.00173267, None, 0.000490964, None, 0.00173267, None, 0.000490964, None, 0.665929, None, 0.00824925, None, 0.665929, None, 0.00824925, None)

reports.append(Report(604058168, ("CSC", 2, 3, 1, 7), "MEm31_07"))
reports[-1].posNum = 170286
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000342279, 0.00163391, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(7.04191e-06, 3.4044e-05, 0), \
                           -173298, 170286, 170286, -nan)
reports[-1].sigmaresid = ValErr(0.669481, 0.00114719, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00080627, None, -0.000111877, None, 0.000382253, None, -0.000473551, None, 0.000382253, None, -0.000473551, None, 0.000110488, None, -0.000540214, None, 0.000110488, None, -0.000540214, None, 0.669481, None, 0.00788495, None, 0.669481, None, 0.00788495, None)

reports.append(Report(604058184, ("CSC", 2, 3, 1, 9), "MEm31_09"))
reports[-1].posNum = 86694
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00185953, 0.00228996, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.88398e-05, 4.66925e-05, 0), \
                           -87781.3, 86694, 86694, -nan)
reports[-1].sigmaresid = ValErr(0.666046, 0.00159954, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00317268, None, -0.000302208, None, -0.0013344, None, -0.000515799, None, -0.0013344, None, -0.000515799, None, -0.00385139, None, -0.000508988, None, -0.00385139, None, -0.000508988, None, 0.666054, None, 0.0075293, None, 0.666054, None, 0.0075293, None)

reports.append(Report(604058200, ("CSC", 2, 3, 1, 11), "MEm31_11"))
reports[-1].posNum = 167234
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00106229, 0.00164272, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.89112e-06, 3.38768e-05, 0), \
                           -169139, 167234, 167234, -nan)
reports[-1].sigmaresid = ValErr(0.665279, 0.00115034, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00109123, None, 0.00025776, None, -0.00107118, None, 0.000111103, None, -0.00107118, None, 0.000111103, None, -0.00129855, None, 0.000160039, None, -0.00129855, None, 0.000160039, None, 0.66528, None, 0.00834141, None, 0.66528, None, 0.00834141, None)

reports.append(Report(604058216, ("CSC", 2, 3, 1, 13), "MEm31_13"))
reports[-1].posNum = 124074
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0016887, 0.00192959, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.43574e-05, 4.12103e-05, 0), \
                           -128108, 124074, 124074, -nan)
reports[-1].sigmaresid = ValErr(0.679479, 0.00136402, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0043467, None, -0.000120598, None, 0.00163797, None, -0.000526646, None, 0.00163797, None, -0.000526646, None, 0.00311156, None, -0.000551624, None, 0.00311156, None, -0.000551624, None, 0.679482, None, 0.00845689, None, 0.679482, None, 0.00845689, None)

reports.append(Report(604058232, ("CSC", 2, 3, 1, 15), "MEm31_15"))
reports[-1].posNum = 178356
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000732813, 0.00159421, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.16785e-05, 3.29832e-05, 0), \
                           -181071, 178356, 178356, -nan)
reports[-1].sigmaresid = ValErr(0.667834, 0.00111817, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00451139, None, -0.000307271, None, 0.000660711, None, -0.000498416, None, 0.000660711, None, -0.000498416, None, 0.0031478, None, -0.000530555, None, 0.0031478, None, -0.000530555, None, 0.667834, None, 0.00804264, None, 0.667834, None, 0.00804264, None)

reports.append(Report(604058248, ("CSC", 2, 3, 1, 17), "MEm31_17"))
reports[-1].posNum = 171928
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(8.71775e-05, 0.00162114, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.57193e-05, 3.35544e-05, 0), \
                           -173980, 171928, 171928, -nan)
reports[-1].sigmaresid = ValErr(0.665643, 0.00113515, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0020763, None, -0.000570615, None, -1.80439e-05, None, -0.000985039, None, -1.80439e-05, None, -0.000985039, None, 0.00366995, None, -0.00102285, None, 0.00366995, None, -0.00102285, None, 0.665644, None, 0.00805553, None, 0.665644, None, 0.00805553, None)

reports.append(Report(604058128, ("CSC", 2, 3, 1, 2), "MEm31_02"))
reports[-1].posNum = 174262
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000281924, 0.00168011, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.15411e-06, 3.56403e-05, 0), \
                           -183653, 174262, 174262, -nan)
reports[-1].sigmaresid = ValErr(0.694167, 0.00117584, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00153037, None, -0.000106129, None, -0.000246123, None, -0.000459326, None, -0.000246123, None, -0.000459326, None, 0.00108585, None, -0.000529615, None, 0.00108585, None, -0.000529615, None, 0.694165, None, 0.00753685, None, 0.694165, None, 0.00753685, None)

reports.append(Report(604058144, ("CSC", 2, 3, 1, 4), "MEm31_04"))
reports[-1].posNum = 164420
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(2.00224e-05, 0.00173024, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.04253e-05, 3.73388e-05, 0), \
                           -174605, 164420, 164420, -nan)
reports[-1].sigmaresid = ValErr(0.699776, 0.0012203, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00051303, None, 1.02042e-05, None, 8.77241e-05, None, -0.000359809, None, 8.77241e-05, None, -0.000359809, None, 4.20581e-05, None, -0.000423246, None, 4.20581e-05, None, -0.000423246, None, 0.699776, None, 0.00757314, None, 0.699776, None, 0.00757314, None)

reports.append(Report(604058160, ("CSC", 2, 3, 1, 6), "MEm31_06"))
reports[-1].posNum = 170062
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(8.54899e-05, 0.00168661, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(7.79499e-06, 3.5815e-05, 0), \
                           -178079, 170062, 170062, -nan)
reports[-1].sigmaresid = ValErr(0.689496, 0.00118226, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00155148, None, 0.000619523, None, 0.000134909, None, 0.000492954, None, 0.000134909, None, 0.000492954, None, 0.00172217, None, 0.000557489, None, 0.00172217, None, 0.000557489, None, 0.689495, None, 0.00767992, None, 0.689495, None, 0.00767992, None)

reports.append(Report(604058176, ("CSC", 2, 3, 1, 8), "MEm31_08"))
reports[-1].posNum = 165868
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000488271, 0.00172905, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.47898e-05, 3.7126e-05, 0), \
                           -176248, 165868, 165868, -nan)
reports[-1].sigmaresid = ValErr(0.700221, 0.00121574, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00134139, None, 0.000948462, None, -0.00041592, None, 0.000844386, None, -0.00041592, None, 0.000844386, None, -0.00275893, None, 0.00088588, None, -0.00275893, None, 0.00088588, None, 0.700221, None, 0.0075937, None, 0.700221, None, 0.0075937, None)

reports.append(Report(604058192, ("CSC", 2, 3, 1, 10), "MEm31_10"))
reports[-1].posNum = 159976
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00164476, 0.00177092, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(9.51289e-07, 3.86429e-05, 0), \
                           -171503, 159976, 159976, -nan)
reports[-1].sigmaresid = ValErr(0.706888, 0.00124971, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000477896, None, 0.00042693, None, -0.00164142, None, 2.79383e-05, None, -0.00164142, None, 2.79383e-05, None, -0.00192579, None, 2.07867e-05, None, -0.00192579, None, 2.07867e-05, None, 0.706888, None, 0.00780403, None, 0.706888, None, 0.00780403, None)

reports.append(Report(604058208, ("CSC", 2, 3, 1, 12), "MEm31_12"))
reports[-1].posNum = 163394
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000342332, 0.00173815, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.9697e-05, 3.83998e-05, 0), \
                           -173874, 163394, 163394, -nan)
reports[-1].sigmaresid = ValErr(0.701316, 0.00122682, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0028777, None, 8.46273e-05, None, -0.000397341, None, 1.69359e-05, None, -0.000397341, None, 1.69359e-05, None, -0.0033524, None, 4.87696e-05, None, -0.0033524, None, 4.87696e-05, None, 0.701314, None, 0.00779003, None, 0.701314, None, 0.00779003, None)

reports.append(Report(604058224, ("CSC", 2, 3, 1, 14), "MEm31_14"))
reports[-1].posNum = 166266
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000734347, 0.00171958, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.56687e-05, 3.77183e-05, 0), \
                           -176621, 166266, 166266, -nan)
reports[-1].sigmaresid = ValErr(0.700012, 0.00121392, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00588323, None, -0.000213943, None, 0.000693402, None, -0.000519268, None, 0.000693402, None, -0.000519268, None, -0.000931987, None, -0.00055968, None, -0.000931987, None, -0.00055968, None, 0.700012, None, 0.00762886, None, 0.700012, None, 0.00762886, None)

reports.append(Report(604058240, ("CSC", 2, 3, 1, 16), "MEm31_16"))
reports[-1].posNum = 169498
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000133364, 0.00168938, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.89291e-06, 3.65597e-05, 0), \
                           -178183, 169498, 169498, -nan)
reports[-1].sigmaresid = ValErr(0.692325, 0.00118908, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00320524, None, -0.000362377, None, 0.000148615, None, -0.00059512, None, 0.000148615, None, -0.00059512, None, 0.000707445, None, -0.000628092, None, 0.000707445, None, -0.000628092, None, 0.692326, None, 0.00742203, None, 0.692326, None, 0.00742203, None)

reports.append(Report(604058256, ("CSC", 2, 3, 1, 18), "MEm31_18"))
reports[-1].posNum = 117962
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000222135, 0.00206213, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.10887e-05, 4.34382e-05, 0), \
                           -126107, 117962, 117962, -nan)
reports[-1].sigmaresid = ValErr(0.704769, 0.00145099, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00479192, None, -0.000279149, None, 0.000168697, None, -0.000702441, None, 0.000168697, None, -0.000702441, None, 0.00225244, None, -0.000816973, None, 0.00225244, None, -0.000816973, None, 0.704766, None, 0.00818928, None, 0.704766, None, 0.00818928, None)

reports.append(Report(604058632, ("CSC", 2, 3, 2, 1), "MEm32_01"))
reports[-1].posNum = 78686
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00839534, 0.0055928, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(8.3204e-05, 5.74342e-05, 0), \
                           -139132, 78686, 78686, -nan)
reports[-1].sigmaresid = ValErr(1.41802, 0.00357453, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00553821, None, -0.000346506, None, -0.00492558, None, -0.000616794, None, -0.00492558, None, -0.000616794, None, -0.0010059, None, -0.000597045, None, -0.0010059, None, -0.000597045, None, 1.41804, None, 0.0114712, None, 1.41804, None, 0.0114712, None)

reports.append(Report(604058648, ("CSC", 2, 3, 2, 3), "MEm32_03"))
reports[-1].posNum = 38362
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00072636, 0.00840595, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(7.22769e-05, 0.00012465, 0), \
                           -73446.1, 38362, 38362, -nan)
reports[-1].sigmaresid = ValErr(1.64151, 0.00592336, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00690108, None, -0.00149688, None, -0.00110085, None, -0.00165851, None, -0.00110085, None, -0.00165851, None, -0.00267121, None, -0.00174783, None, -0.00267121, None, -0.00174783, None, 1.64151, None, 0.0108982, None, 1.64151, None, 0.0108982, None)

reports.append(Report(604058664, ("CSC", 2, 3, 2, 5), "MEm32_05"))
reports[-1].posNum = 66152
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00119831, 0.00658811, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.29607e-05, 6.59298e-05, 0), \
                           -111115, 66152, 66152, -nan)
reports[-1].sigmaresid = ValErr(1.29791, 0.00356826, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00131795, None, -3.78777e-05, None, -0.000365475, None, -0.000333554, None, -0.000365475, None, -0.000333554, None, -0.000959816, None, -0.000428378, None, -0.000959816, None, -0.000428378, None, 1.29791, None, 0.00922452, None, 1.29791, None, 0.00922452, None)

reports.append(Report(604058680, ("CSC", 2, 3, 2, 7), "MEm32_07"))
reports[-1].posNum = 66612
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00833744, 0.00668224, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(7.79762e-05, 6.71286e-05, 0), \
                           -112718, 66612, 66612, -nan)
reports[-1].sigmaresid = ValErr(1.31418, 0.00360048, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00159257, None, -5.00384e-05, None, -0.00331095, None, -0.000107782, None, -0.00331095, None, -0.000107782, None, -0.00180348, None, -0.00016086, None, -0.00180348, None, -0.00016086, None, 1.3142, None, 0.00960279, None, 1.3142, None, 0.00960279, None)

reports.append(Report(604058696, ("CSC", 2, 3, 2, 9), "MEm32_09"))
reports[-1].posNum = 70726
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0015668, 0.00603144, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.79051e-07, 6.08083e-05, 0), \
                           -122530, 70726, 70726, -nan)
reports[-1].sigmaresid = ValErr(1.36825, 0.003638, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000447823, None, 0.000286687, None, 0.00159639, None, 5.23771e-05, None, 0.00159639, None, 5.23771e-05, None, 0.00629629, None, 6.14934e-05, None, 0.00629629, None, 6.14934e-05, None, 1.36824, None, 0.0100356, None, 1.36824, None, 0.0100356, None)

reports.append(Report(604058712, ("CSC", 2, 3, 2, 11), "MEm32_11"))
reports[-1].posNum = 73106
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000619658, 0.00595055, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.20328e-05, 5.93045e-05, 0), \
                           -127619, 73106, 73106, -nan)
reports[-1].sigmaresid = ValErr(1.38644, 0.00362584, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00114641, None, 0.000406649, None, 0.00123207, None, 0.00046121, None, 0.00123207, None, 0.00046121, None, 0.00139959, None, 0.000479714, None, 0.00139959, None, 0.000479714, None, 1.38644, None, 0.00994129, None, 1.38644, None, 0.00994129, None)

reports.append(Report(604058728, ("CSC", 2, 3, 2, 13), "MEm32_13"))
reports[-1].posNum = 63602
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.004905, 0.00651935, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.61343e-05, 6.4686e-05, 0), \
                           -107599, 63602, 63602, -nan)
reports[-1].sigmaresid = ValErr(1.31367, 0.00368328, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00462757, None, 0.00022715, None, -0.00392674, None, 0.000109912, None, -0.00392674, None, 0.000109912, None, -0.008877, None, 7.89458e-05, None, -0.008877, None, 7.89458e-05, None, 1.31367, None, 0.00940921, None, 1.31367, None, 0.00940921, None)

reports.append(Report(604058744, ("CSC", 2, 3, 2, 15), "MEm32_15"))
reports[-1].posNum = 70298
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00441278, 0.00641992, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.48074e-05, 6.4688e-05, 0), \
                           -120373, 70298, 70298, -nan)
reports[-1].sigmaresid = ValErr(1.34095, 0.00357625, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00305225, None, 0.000116613, None, 0.00167534, None, -1.31835e-05, None, 0.00167534, None, -1.31835e-05, None, 0.00375185, None, -3.54267e-05, None, 0.00375185, None, -3.54267e-05, None, 1.34096, None, 0.00985944, None, 1.34096, None, 0.00985944, None)

reports.append(Report(604058760, ("CSC", 2, 3, 2, 17), "MEm32_17"))
reports[-1].posNum = 61616
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0111403, 0.00679181, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000126718, 6.53562e-05, 0), \
                           -104065, 61616, 61616, -nan)
reports[-1].sigmaresid = ValErr(1.30995, 0.00373155, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00478037, None, -0.000120171, None, 0.00284323, None, -0.000414449, None, 0.00284323, None, -0.000414449, None, 0.00848878, None, -0.000395705, None, 0.00848878, None, -0.000395705, None, 1.31, None, 0.00981821, None, 1.31, None, 0.00981821, None)

reports.append(Report(604058776, ("CSC", 2, 3, 2, 19), "MEm32_19"))
reports[-1].posNum = 75044
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0182423, 0.00576763, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000221236, 5.9291e-05, 0), \
                           -130295, 75044, 75044, -nan)
reports[-1].sigmaresid = ValErr(1.37343, 0.00354514, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00989332, None, -0.000144997, None, 0.00760335, None, -0.000445117, None, 0.00760335, None, -0.000445117, None, 0.0106374, None, -0.000425084, None, 0.0106374, None, -0.000425084, None, 1.37356, None, 0.00926816, None, 1.37356, None, 0.00926816, None)

reports.append(Report(604058792, ("CSC", 2, 3, 2, 21), "MEm32_21"))
reports[-1].posNum = 70478
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0118058, 0.00601589, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000176244, 6.04656e-05, 0), \
                           -120415, 70478, 70478, -nan)
reports[-1].sigmaresid = ValErr(1.3359, 0.00355822, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00526283, None, -0.00076222, None, 0.00219647, None, -0.000929693, None, 0.00219647, None, -0.000929693, None, 0.000746058, None, -0.000962375, None, 0.000746058, None, -0.000962375, None, 1.33598, None, 0.00978585, None, 1.33598, None, 0.00978585, None)

reports.append(Report(604058808, ("CSC", 2, 3, 2, 23), "MEm32_23"))
reports[-1].posNum = 76434
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00690609, 0.00559602, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.98592e-05, 5.75072e-05, 0), \
                           -133242, 76434, 76434, -nan)
reports[-1].sigmaresid = ValErr(1.38305, 0.00353737, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00386042, None, 0.000541921, None, 0.00429512, None, 0.000465276, None, 0.00429512, None, 0.000465276, None, 0.0106995, None, 0.000522722, None, 0.0106995, None, 0.000522722, None, 1.38306, None, 0.0103502, None, 1.38306, None, 0.0103502, None)

reports.append(Report(604058824, ("CSC", 2, 3, 2, 25), "MEm32_25"))
reports[-1].posNum = 60510
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00545408, 0.00659658, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.62295e-05, 6.28658e-05, 0), \
                           -102174, 60510, 60510, -nan)
reports[-1].sigmaresid = ValErr(1.30945, 0.00376407, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00714213, None, -0.000749004, None, 0.00134607, None, -0.000879332, None, 0.00134607, None, -0.000879332, None, -0.0010877, None, -0.000918695, None, -0.0010877, None, -0.000918695, None, 1.30946, None, 0.0105108, None, 1.30946, None, 0.0105108, None)

reports.append(Report(604058840, ("CSC", 2, 3, 2, 27), "MEm32_27"))
reports[-1].posNum = 56396
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0054037, 0.00699835, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.21166e-05, 6.67717e-05, 0), \
                           -94228.8, 56396, 56396, -nan)
reports[-1].sigmaresid = ValErr(1.28647, 0.00383054, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00865775, None, -0.000333301, None, 0.00459902, None, -0.000687494, None, 0.00459902, None, -0.000687494, None, 0.00280155, None, -0.000613187, None, 0.00280155, None, -0.000613187, None, 1.28647, None, 0.011797, None, 1.28647, None, 0.011797, None)

reports.append(Report(604058856, ("CSC", 2, 3, 2, 29), "MEm32_29"))
reports[-1].posNum = 59660
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0048418, 0.00651467, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.21383e-05, 6.20394e-05, 0), \
                           -102031, 59660, 59660, -nan)
reports[-1].sigmaresid = ValErr(1.33813, 0.00387383, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.003724, None, -0.00011127, None, -0.00244707, None, -0.000729212, None, -0.00244707, None, -0.000729212, None, -0.00528681, None, -0.000675472, None, -0.00528681, None, -0.000675472, None, 1.33813, None, 0.0104503, None, 1.33813, None, 0.0104503, None)

reports.append(Report(604058872, ("CSC", 2, 3, 2, 31), "MEm32_31"))
reports[-1].posNum = 54264
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00074407, 0.00699632, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.5469e-05, 6.59332e-05, 0), \
                           -92166.8, 54264, 54264, -nan)
reports[-1].sigmaresid = ValErr(1.32254, 0.00401457, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0061155, None, 0.000230336, None, 0.0035611, None, 6.29784e-05, None, 0.0035611, None, 6.29784e-05, None, -0.0090519, None, 6.74286e-05, None, -0.0090519, None, 6.74286e-05, None, 1.32254, None, 0.0098204, None, 1.32254, None, 0.0098204, None)

reports.append(Report(604058888, ("CSC", 2, 3, 2, 33), "MEm32_33"))
reports[-1].posNum = 67276
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00912775, 0.00630755, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(8.02274e-05, 6.33582e-05, 0), \
                           -114712, 67276, 67276, -nan)
reports[-1].sigmaresid = ValErr(1.3313, 0.00362935, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00259705, None, 0.00013029, None, -0.00448572, None, 9.68428e-05, None, -0.00448572, None, 9.68428e-05, None, -0.00393496, None, 0.000131139, None, -0.00393496, None, 0.000131139, None, 1.33132, None, 0.00938068, None, 1.33132, None, 0.00938068, None)

reports.append(Report(604058904, ("CSC", 2, 3, 2, 35), "MEm32_35"))
reports[-1].posNum = 71574
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000865475, 0.00591314, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.18593e-05, 5.83817e-05, 0), \
                           -123764, 71574, 71574, -nan)
reports[-1].sigmaresid = ValErr(1.36375, 0.00360448, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00136114, None, 0.00030506, None, -0.000255664, None, -0.00035812, None, -0.000255664, None, -0.00035812, None, -0.0023788, None, -0.000386082, None, -0.0023788, None, -0.000386082, None, 1.36375, None, 0.00989181, None, 1.36375, None, 0.00989181, None)

reports.append(Report(604058640, ("CSC", 2, 3, 2, 2), "MEm32_02"))
reports[-1].posNum = 79970
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0125562, 0.00561698, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000138179, 5.67155e-05, 0), \
                           -141395, 79970, 79970, -nan)
reports[-1].sigmaresid = ValErr(1.41788, 0.00354538, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0030442, None, -5.31449e-05, None, -0.00638735, None, -0.000206579, None, -0.00638735, None, -0.000206579, None, -0.00431068, None, -0.000201362, None, -0.00431068, None, -0.000201362, None, 1.41794, None, 0.00848006, None, 1.41794, None, 0.00848006, None)

reports.append(Report(604058656, ("CSC", 2, 3, 2, 4), "MEm32_04"))
reports[-1].posNum = 68534
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00667479, 0.00653583, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(7.88466e-05, 6.55669e-05, 0), \
                           -118226, 68534, 68534, -nan)
reports[-1].sigmaresid = ValErr(1.35817, 0.00366847, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00324831, None, -6.47103e-05, None, -0.0018943, None, -0.000230088, None, -0.0018943, None, -0.000230088, None, -0.00198985, None, -0.000273316, None, -0.00198985, None, -0.000273316, None, 1.35818, None, 0.0107688, None, 1.35818, None, 0.0107688, None)

reports.append(Report(604058672, ("CSC", 2, 3, 2, 6), "MEm32_06"))
reports[-1].posNum = 70200
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00415127, 0.00620456, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.02291e-05, 6.41667e-05, 0), \
                           -121151, 70200, 70200, -nan)
reports[-1].sigmaresid = ValErr(1.35915, 0.00362729, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00032226, None, -0.00031374, None, -0.00196247, None, -0.000573989, None, -0.00196247, None, -0.000573989, None, 0.00233287, None, -0.000595657, None, 0.00233287, None, -0.000595657, None, 1.35915, None, 0.00848357, None, 1.35915, None, 0.00848357, None)

reports.append(Report(604058688, ("CSC", 2, 3, 2, 8), "MEm32_08"))
reports[-1].posNum = 67264
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00949841, 0.00644615, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000108122, 6.48099e-05, 0), \
                           -115382, 67264, 67264, -nan)
reports[-1].sigmaresid = ValErr(1.34504, 0.00366716, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00155861, None, 0.000225167, None, -0.00311126, None, 0.000124981, None, -0.00311126, None, 0.000124981, None, -0.00527002, None, 0.000117852, None, -0.00527002, None, 0.000117852, None, 1.34507, None, 0.00844593, None, 1.34507, None, 0.00844593, None)

reports.append(Report(604058704, ("CSC", 2, 3, 2, 10), "MEm32_10"))
reports[-1].posNum = 79388
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00137874, 0.00561652, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.6071e-06, 5.77231e-05, 0), \
                           -140840, 79388, 79388, -nan)
reports[-1].sigmaresid = ValErr(1.42637, 0.00357967, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000178329, None, -0.000295852, None, 0.000972338, None, -0.000445156, None, 0.000972338, None, -0.000445156, None, -0.00394206, None, -0.000445268, None, -0.00394206, None, -0.000445268, None, 1.42636, None, 0.00887388, None, 1.42636, None, 0.00887388, None)

reports.append(Report(604058720, ("CSC", 2, 3, 2, 12), "MEm32_12"))
reports[-1].posNum = 74090
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00800061, 0.00603686, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000100892, 6.08531e-05, 0), \
                           -127290, 74090, 74090, -nan)
reports[-1].sigmaresid = ValErr(1.34865, 0.00350351, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000264264, None, 0.000469344, None, 0.00228176, None, 0.00026878, None, 0.00228176, None, 0.00026878, None, 0.00371002, None, 0.000281489, None, 0.00371002, None, 0.000281489, None, 1.34867, None, 0.00877222, None, 1.34867, None, 0.00877222, None)

reports.append(Report(604058736, ("CSC", 2, 3, 2, 14), "MEm32_14"))
reports[-1].posNum = 79574
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000887836, 0.00565992, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.49662e-05, 5.80231e-05, 0), \
                           -139627, 79574, 79574, -nan)
reports[-1].sigmaresid = ValErr(1.39898, 0.00350679, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00200803, None, 0.000699958, None, 0.00253153, None, 0.000400515, None, 0.00253153, None, 0.000400515, None, 0.00524647, None, 0.000476842, None, 0.00524647, None, 0.000476842, None, 1.39898, None, 0.00865149, None, 1.39898, None, 0.00865149, None)

reports.append(Report(604058752, ("CSC", 2, 3, 2, 16), "MEm32_16"))
reports[-1].posNum = 69308
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.013113, 0.00696633, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000162898, 6.88107e-05, 0), \
                           -119953, 69308, 69308, -nan)
reports[-1].sigmaresid = ValErr(1.36586, 0.0036686, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0022301, None, 0.000184943, None, 0.00210702, None, 0.00017091, None, 0.00210702, None, 0.00017091, None, 0.00948862, None, 0.000212474, None, 0.00948862, None, 0.000212474, None, 1.36592, None, 0.00882629, None, 1.36592, None, 0.00882629, None)

reports.append(Report(604058768, ("CSC", 2, 3, 2, 18), "MEm32_18"))
reports[-1].posNum = 70948
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00392746, 0.00600404, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.04912e-05, 6.03006e-05, 0), \
                           -124253, 70948, 70948, -nan)
reports[-1].sigmaresid = ValErr(1.3943, 0.00370144, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00738363, None, 0.000312799, None, 0.00244, None, 0.000132769, None, 0.00244, None, 0.000132769, None, 0.000119475, None, 0.000146487, None, 0.000119475, None, 0.000146487, None, 1.3943, None, 0.00897114, None, 1.3943, None, 0.00897114, None)

reports.append(Report(604058784, ("CSC", 2, 3, 2, 20), "MEm32_20"))
reports[-1].posNum = 73306
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00514887, 0.00604146, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.75677e-05, 6.11164e-05, 0), \
                           -127736, 73306, 73306, -nan)
reports[-1].sigmaresid = ValErr(1.38205, 0.00360942, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00445404, None, 1.611e-07, None, 0.00157545, None, -0.000313026, None, 0.00157545, None, -0.000313026, None, -0.00674453, None, -0.000298133, None, -0.00674453, None, -0.000298133, None, 1.38206, None, 0.00842384, None, 1.38206, None, 0.00842384, None)

reports.append(Report(604058800, ("CSC", 2, 3, 2, 22), "MEm32_22"))
reports[-1].posNum = 72272
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00570574, 0.00599334, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.775e-05, 6.09211e-05, 0), \
                           -126554, 72272, 72272, -nan)
reports[-1].sigmaresid = ValErr(1.39395, 0.00366646, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00539867, None, -0.000932511, None, 0.00433727, None, -0.00123943, None, 0.00433727, None, -0.00123943, None, 0.00107483, None, -0.00128299, None, 0.00107483, None, -0.00128299, None, 1.39395, None, 0.00881195, None, 1.39395, None, 0.00881195, None)

reports.append(Report(604058816, ("CSC", 2, 3, 2, 24), "MEm32_24"))
reports[-1].posNum = 77414
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00594948, 0.00568814, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.37932e-05, 5.79789e-05, 0), \
                           -135531, 77414, 77414, -nan)
reports[-1].sigmaresid = ValErr(1.39347, 0.00354138, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00256985, None, -0.00147512, None, 0.00205037, None, -0.00194538, None, 0.00205037, None, -0.00194538, None, 0.00215712, None, -0.00197488, None, 0.00215712, None, -0.00197488, None, 1.39349, None, 0.00868705, None, 1.39349, None, 0.00868705, None)

reports.append(Report(604058832, ("CSC", 2, 3, 2, 26), "MEm32_26"))
reports[-1].posNum = 58312
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00962568, 0.00711775, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.13832e-05, 6.71265e-05, 0), \
                           -98296.3, 58312, 58312, -nan)
reports[-1].sigmaresid = ValErr(1.30572, 0.00382346, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00920994, None, -0.000263256, None, 0.00332474, None, -0.000318484, None, 0.00332474, None, -0.000318484, None, 0.0143917, None, -0.000316975, None, 0.0143917, None, -0.000316975, None, 1.30574, None, 0.00970383, None, 1.30574, None, 0.00970383, None)

reports.append(Report(604058848, ("CSC", 2, 3, 2, 28), "MEm32_28"))
reports[-1].posNum = 69764
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000818176, 0.00622228, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.43122e-05, 6.13811e-05, 0), \
                           -121733, 69764, 69764, -nan)
reports[-1].sigmaresid = ValErr(1.38541, 0.00370891, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00849685, None, 0.000238853, None, 0.00159854, None, -0.00026667, None, 0.00159854, None, -0.00026667, None, -0.00242645, None, -0.000224747, None, -0.00242645, None, -0.000224747, None, 1.38541, None, 0.00890097, None, 1.38541, None, 0.00890097, None)

reports.append(Report(604058864, ("CSC", 2, 3, 2, 30), "MEm32_30"))
reports[-1].posNum = 58964
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0125621, 0.00687403, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000111521, 6.40084e-05, 0), \
                           -100661, 58964, 58964, -nan)
reports[-1].sigmaresid = ValErr(1.33404, 0.00388471, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(7.00067e-05, None, -4.50097e-05, None, -0.00536286, None, -0.000127817, None, -0.00536286, None, -0.000127817, None, -0.0109043, None, -0.000119877, None, -0.0109043, None, -0.000119877, None, 1.33408, None, 0.00830206, None, 1.33408, None, 0.00830206, None)

reports.append(Report(604058880, ("CSC", 2, 3, 2, 32), "MEm32_32"))
reports[-1].posNum = 70510
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0146194, 0.00603711, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.00014587, 5.92218e-05, 0), \
                           -121802, 70510, 70510, -nan)
reports[-1].sigmaresid = ValErr(1.36139, 0.00362529, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00857597, None, -0.000178135, None, -0.00676796, None, -0.000363878, None, -0.00676796, None, -0.000363878, None, -0.00211315, None, -0.000410566, None, -0.00211315, None, -0.000410566, None, 1.36145, None, 0.00825389, None, 1.36145, None, 0.00825389, None)

reports.append(Report(604058896, ("CSC", 2, 3, 2, 34), "MEm32_34"))
reports[-1].posNum = 74952
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00705483, 0.00585924, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.93112e-05, 5.97097e-05, 0), \
                           -131163, 74952, 74952, -nan)
reports[-1].sigmaresid = ValErr(1.39239, 0.00359629, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00177752, None, 0.000226889, None, -0.00416463, None, -0.000118915, None, -0.00416463, None, -0.000118915, None, 0.000978472, None, -9.72123e-05, None, 0.000978472, None, -9.72123e-05, None, 1.3924, None, 0.00869884, None, 1.3924, None, 0.00869884, None)

reports.append(Report(604058912, ("CSC", 2, 3, 2, 36), "MEm32_36"))
reports[-1].posNum = 77858
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000552451, 0.00568573, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.24032e-05, 5.76397e-05, 0), \
                           -137212, 77858, 77858, -nan)
reports[-1].sigmaresid = ValErr(1.40974, 0.00357254, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00233051, None, 0.000516396, None, 1.14988e-05, None, 0.000309915, None, 1.14988e-05, None, 0.000309915, None, -0.00101031, None, 0.000345542, None, -0.00101031, None, 0.000345542, None, 1.40974, None, 0.00877843, None, 1.40974, None, 0.00877843, None)

reports.append(Report(604062216, ("CSC", 2, 4, 1, 1), "MEm41_01"))
reports[-1].posNum = 108688
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000139319, 0.00241633, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.89402e-06, 5.58218e-05, 0), \
                           -128728, 108688, 108688, -nan)
reports[-1].sigmaresid = ValErr(0.790922, 0.0016964, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00220132, None, 0.00040295, None, 0.000165496, None, 5.57358e-05, None, 0.000165496, None, 5.57358e-05, None, 0.000695046, None, 4.40733e-05, None, 0.000695046, None, 4.40733e-05, None, 0.790921, None, 0.00803497, None, 0.790921, None, 0.00803497, None)

reports.append(Report(604062232, ("CSC", 2, 4, 1, 3), "MEm41_03"))
reports[-1].posNum = 129932
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000322809, 0.00218323, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.99859e-05, 5.09797e-05, 0), \
                           -152384, 129932, 129932, -nan)
reports[-1].sigmaresid = ValErr(0.781812, 0.00153366, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000971475, None, -6.31071e-05, None, -0.000127129, None, -0.000443724, None, -0.000127129, None, -0.000443724, None, 0.00200718, None, -0.000471336, None, 0.00200718, None, -0.000471336, None, 0.781815, None, 0.00781672, None, 0.781815, None, 0.00781672, None)

reports.append(Report(604062248, ("CSC", 2, 4, 1, 5), "MEm41_05"))
reports[-1].posNum = 130134
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000731612, 0.00215243, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.33533e-05, 5.01477e-05, 0), \
                           -150931, 130134, 130134, -nan)
reports[-1].sigmaresid = ValErr(0.771725, 0.0015127, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00676049, None, 0.000188399, None, -0.000842563, None, -0.000115806, None, -0.000842563, None, -0.000115806, None, 0.00153297, None, -0.000133912, None, 0.00153297, None, -0.000133912, None, 0.771726, None, 0.00821239, None, 0.771726, None, 0.00821239, None)

reports.append(Report(604062264, ("CSC", 2, 4, 1, 7), "MEm41_07"))
reports[-1].posNum = 132692
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000712555, 0.00213777, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.78364e-05, 4.96765e-05, 0), \
                           -154203, 132692, 132692, -nan)
reports[-1].sigmaresid = ValErr(0.773504, 0.0015015, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000360489, None, -0.000640352, None, 0.000474542, None, -0.00100223, None, 0.000474542, None, -0.00100223, None, 0.00084323, None, -0.0010638, None, 0.00084323, None, -0.0010638, None, 0.773508, None, 0.00824389, None, 0.773508, None, 0.00824389, None)

reports.append(Report(604062280, ("CSC", 2, 4, 1, 9), "MEm41_09"))
reports[-1].posNum = 132484
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000379334, 0.00217169, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.74225e-05, 5.01317e-05, 0), \
                           -155672, 132484, 132484, -nan)
reports[-1].sigmaresid = ValErr(0.783559, 0.00152222, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00048172, None, -0.000104954, None, -0.000281884, None, -0.000507406, None, -0.000281884, None, -0.000507406, None, 0.00126754, None, -0.000522069, None, 0.00126754, None, -0.000522069, None, 0.783558, None, 0.00855223, None, 0.783558, None, 0.00855223, None)

reports.append(Report(604062296, ("CSC", 2, 4, 1, 11), "MEm41_11"))
reports[-1].posNum = 105952
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00444499, 0.00239302, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00011087, 5.523e-05, 0), \
                           -122916, 105952, 105952, -nan)
reports[-1].sigmaresid = ValErr(0.771953, 0.00167696, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00690191, None, -0.00069152, None, 0.00380672, None, -0.00113546, None, 0.00380672, None, -0.00113546, None, 0.000343482, None, -0.0011148, None, 0.000343482, None, -0.0011148, None, 0.771967, None, 0.0079507, None, 0.771967, None, 0.0079507, None)

reports.append(Report(604062312, ("CSC", 2, 4, 1, 13), "MEm41_13"))
reports[-1].posNum = 110942
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00173975, 0.00238331, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.26029e-05, 5.68204e-05, 0), \
                           -131800, 110942, 110942, -nan)
reports[-1].sigmaresid = ValErr(0.793793, 0.00168517, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00414286, None, -0.000959703, None, 0.00176693, None, -0.00138429, None, 0.00176693, None, -0.00138429, None, 0.00218575, None, -0.00146645, None, 0.00218575, None, -0.00146645, None, 0.793797, None, 0.00823314, None, 0.793797, None, 0.00823314, None)

reports.append(Report(604062328, ("CSC", 2, 4, 1, 15), "MEm41_15"))
reports[-1].posNum = 114486
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00149385, 0.0022902, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.97444e-06, 5.32366e-05, 0), \
                           -132105, 114486, 114486, -nan)
reports[-1].sigmaresid = ValErr(0.767172, 0.00160325, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00363195, None, -0.00114811, None, -0.00145144, None, -0.00145684, None, -0.00145144, None, -0.00145684, None, -0.000876653, None, -0.00151179, None, -0.000876653, None, -0.00151179, None, 0.767173, None, 0.00806616, None, 0.767173, None, 0.00806616, None)

reports.append(Report(604062344, ("CSC", 2, 4, 1, 17), "MEm41_17"))
reports[-1].posNum = 136942
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000241567, 0.00210437, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.93861e-05, 4.863e-05, 0), \
                           -158856, 136942, 136942, -nan)
reports[-1].sigmaresid = ValErr(0.771889, 0.00147493, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0030804, None, -0.000392275, None, -0.000352509, None, -0.0006597, None, -0.000352509, None, -0.0006597, None, -0.000964706, None, -0.000680787, None, -0.000964706, None, -0.000680787, None, 0.771889, None, 0.00827974, None, 0.771889, None, 0.00827974, None)

reports.append(Report(604062224, ("CSC", 2, 4, 1, 2), "MEm41_02"))
reports[-1].posNum = 141352
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00095689, 0.00215592, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.69822e-05, 4.96882e-05, 0), \
                           -169770, 141352, 141352, -nan)
reports[-1].sigmaresid = ValErr(0.804211, 0.00151253, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00240926, None, -0.000412229, None, 0.000863428, None, -0.000720806, None, 0.000863428, None, -0.000720806, None, 0.0061827, None, -0.000746546, None, 0.0061827, None, -0.000746546, None, 0.804211, None, 0.00733694, None, 0.804211, None, 0.00733694, None)

reports.append(Report(604062240, ("CSC", 2, 4, 1, 4), "MEm41_04"))
reports[-1].posNum = 133430
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000877052, 0.00221266, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.28214e-05, 5.20861e-05, 0), \
                           -160764, 133430, 133430, -nan)
reports[-1].sigmaresid = ValErr(0.807283, 0.00156273, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000492227, None, -0.000368989, None, 0.000945278, None, -0.000818453, None, 0.000945278, None, -0.000818453, None, 0.00388879, None, -0.000877699, None, 0.00388879, None, -0.000877699, None, 0.807284, None, 0.00766937, None, 0.807284, None, 0.00766937, None)

reports.append(Report(604062256, ("CSC", 2, 4, 1, 6), "MEm41_06"))
reports[-1].posNum = 138682
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000659456, 0.00214531, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.13789e-05, 4.97685e-05, 0), \
                           -164585, 138682, 138682, -nan)
reports[-1].sigmaresid = ValErr(0.792823, 0.0015054, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000345559, None, -5.84318e-06, None, 0.000718294, None, -0.000399882, None, 0.000718294, None, -0.000399882, None, 0.00120455, None, -0.000428295, None, 0.00120455, None, -0.000428295, None, 0.792823, None, 0.00759878, None, 0.792823, None, 0.00759878, None)

reports.append(Report(604062272, ("CSC", 2, 4, 1, 8), "MEm41_08"))
reports[-1].posNum = 136590
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00136972, 0.00219959, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.30548e-05, 5.15038e-05, 0), \
                           -164894, 136590, 136590, -nan)
reports[-1].sigmaresid = ValErr(0.809194, 0.0015482, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00105677, None, -0.000409551, None, 0.00127463, None, -0.00077697, None, 0.00127463, None, -0.00077697, None, 0.00125828, None, -0.000830501, None, 0.00125828, None, -0.000830501, None, 0.809194, None, 0.00763551, None, 0.809194, None, 0.00763551, None)

reports.append(Report(604062288, ("CSC", 2, 4, 1, 10), "MEm41_10"))
reports[-1].posNum = 130672
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000329175, 0.00226039, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.82431e-05, 5.38037e-05, 0), \
                           -158852, 130672, 130672, -nan)
reports[-1].sigmaresid = ValErr(0.816046, 0.00159628, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00224396, None, -0.000120249, None, -0.000247539, None, -0.000619184, None, -0.000247539, None, -0.000619184, None, 0.00131453, None, -0.000677436, None, 0.00131453, None, -0.000677436, None, 0.816047, None, 0.00780409, None, 0.816047, None, 0.00780409, None)

reports.append(Report(604062304, ("CSC", 2, 4, 1, 12), "MEm41_12"))
reports[-1].posNum = 134128
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000947628, 0.00221197, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.16725e-05, 5.3207e-05, 0), \
                           -161936, 134128, 134128, -nan)
reports[-1].sigmaresid = ValErr(0.80928, 0.00156252, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00506322, None, -8.2454e-05, None, 0.000907365, None, -0.000406777, None, 0.000907365, None, -0.000406777, None, 0.000815931, None, -0.000426536, None, 0.000815931, None, -0.000426536, None, 0.80928, None, 0.00751973, None, 0.80928, None, 0.00751973, None)

reports.append(Report(604062320, ("CSC", 2, 4, 1, 14), "MEm41_14"))
reports[-1].posNum = 136072
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00016108, 0.00219165, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.32681e-05, 5.25276e-05, 0), \
                           -163926, 136072, 136072, -nan)
reports[-1].sigmaresid = ValErr(0.807155, 0.00154724, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0055721, None, -0.00011176, None, 5.90933e-05, None, -0.000330858, None, 5.90933e-05, None, -0.000330858, None, -0.000613461, None, -0.000367819, None, -0.000613461, None, -0.000367819, None, 0.807157, None, 0.00784035, None, 0.807157, None, 0.00784035, None)

reports.append(Report(604062336, ("CSC", 2, 4, 1, 16), "MEm41_16"))
reports[-1].posNum = 139682
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(7.98343e-05, 0.00215013, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.75369e-05, 5.08269e-05, 0), \
                           -167164, 139682, 139682, -nan)
reports[-1].sigmaresid = ValErr(0.800765, 0.00151503, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00298613, None, -0.000751574, None, -1.62258e-05, None, -0.000987968, None, -1.62258e-05, None, -0.000987968, None, 0.00224755, None, -0.00103126, None, 0.00224755, None, -0.00103126, None, 0.800766, None, 0.00741747, None, 0.800766, None, 0.00741747, None)

reports.append(Report(604062352, ("CSC", 2, 4, 1, 18), "MEm41_18"))
reports[-1].posNum = 140392
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000757428, 0.0021653, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.29779e-05, 5.03176e-05, 0), \
                           -168983, 140392, 140392, -nan)
reports[-1].sigmaresid = ValErr(0.806307, 0.00152165, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00414365, None, -0.00024501, None, 0.000456002, None, -0.000295463, None, 0.000456002, None, -0.000295463, None, 0.00364102, None, -0.000329431, None, 0.00364102, None, -0.000329431, None, 0.806312, None, 0.00787661, None, 0.806312, None, 0.00787661, None)

reports.append(Report(604062728, ("CSC", 2, 4, 2, 1), "MEm42_01"))
reports[-1].posNum = 42182
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0100062, 0.00785015, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000109505, 8.35791e-05, 0), \
                           -77247.8, 42182, 42182, -nan)
reports[-1].sigmaresid = ValErr(1.51038, 0.00520006, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00229511, None, -0.000945858, None, -0.00641039, None, -0.00103363, None, -0.00641039, None, -0.00103363, None, 0.00519751, None, -0.000984845, None, 0.00519751, None, -0.000984845, None, 1.51041, None, 0.0105727, None, 1.51041, None, 0.0105727, None)

reports.append(Report(604062744, ("CSC", 2, 4, 2, 3), "MEm42_03"))
reports[-1].posNum = 73352
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00420942, 0.00624516, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.5004e-05, 6.47337e-05, 0), \
                           -131590, 73352, 73352, -nan)
reports[-1].sigmaresid = ValErr(1.45502, 0.0037988, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0021984, None, -2.81204e-05, None, -0.0010082, None, -0.000166422, None, -0.0010082, None, -0.000166422, None, 0.00774695, None, -0.000206781, None, 0.00774695, None, -0.000206781, None, 1.45503, None, 0.00979158, None, 1.45503, None, 0.00979158, None)

reports.append(Report(604062760, ("CSC", 2, 4, 2, 5), "MEm42_05"))
reports[-1].posNum = 64278
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00205011, 0.00654492, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.75398e-05, 7.55008e-05, 0), \
                           -115411, 64278, 64278, -nan)
reports[-1].sigmaresid = ValErr(1.45725, 0.00406431, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00130367, None, -0.00103838, None, 0.000491351, None, -0.00117486, None, 0.000491351, None, -0.00117486, None, 0.0064048, None, -0.00121055, None, 0.0064048, None, -0.00121055, None, 1.45726, None, 0.00954807, None, 1.45726, None, 0.00954807, None)

reports.append(Report(604062776, ("CSC", 2, 4, 2, 7), "MEm42_07"))
reports[-1].posNum = 72614
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00358808, 0.00644909, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.77489e-05, 6.79844e-05, 0), \
                           -129566, 72614, 72614, -nan)
reports[-1].sigmaresid = ValErr(1.44104, 0.00378139, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000456426, None, -0.00209342, None, -0.00211683, None, -0.00211473, None, -0.00211683, None, -0.00211473, None, -0.000395073, None, -0.00222213, None, -0.000395073, None, -0.00222213, None, 1.44104, None, 0.0110759, None, 1.44104, None, 0.0110759, None)

reports.append(Report(604062792, ("CSC", 2, 4, 2, 9), "MEm42_09"))
reports[-1].posNum = 75048
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00287117, 0.00609429, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.04836e-05, 6.31229e-05, 0), \
                           -135492, 75048, 75048, -nan)
reports[-1].sigmaresid = ValErr(1.47178, 0.00379889, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00246529, None, -0.000750199, None, -0.0023934, None, -0.000829099, None, -0.0023934, None, -0.000829099, None, 0.007335, None, -0.000895553, None, 0.007335, None, -0.000895553, None, 1.47178, None, 0.00948214, None, 1.47178, None, 0.00948214, None)

reports.append(Report(604062808, ("CSC", 2, 4, 2, 11), "MEm42_11"))
reports[-1].posNum = 74700
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00731409, 0.00619366, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.50235e-05, 6.36453e-05, 0), \
                           -135539, 74700, 74700, -nan)
reports[-1].sigmaresid = ValErr(1.48512, 0.00384225, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00802793, None, -0.0016413, None, 0.00427636, None, -0.00173865, None, 0.00427636, None, -0.00173865, None, 0.00827516, None, -0.00178324, None, 0.00827516, None, -0.00178324, None, 1.48514, None, 0.0100795, None, 1.48514, None, 0.0100795, None)

reports.append(Report(604062824, ("CSC", 2, 4, 2, 13), "MEm42_13"))
reports[-1].posNum = 68886
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00533575, 0.00648631, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.75925e-05, 6.72988e-05, 0), \
                           -122500, 68886, 68886, -nan)
reports[-1].sigmaresid = ValErr(1.43242, 0.00385914, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-4.77299e-05, None, -0.000417068, None, 0.00129038, None, -0.000473096, None, 0.00129038, None, -0.000473096, None, 0.002244, None, -0.000493807, None, 0.002244, None, -0.000493807, None, 1.43244, None, 0.0104148, None, 1.43244, None, 0.0104148, None)

reports.append(Report(604062840, ("CSC", 2, 4, 2, 15), "MEm42_15"))
reports[-1].posNum = 75580
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00710065, 0.00633154, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.86018e-05, 6.58485e-05, 0), \
                           -135680, 75580, 75580, -nan)
reports[-1].sigmaresid = ValErr(1.45681, 0.00374699, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00835482, None, -0.000400657, None, 0.00190667, None, -0.000540517, None, 0.00190667, None, -0.000540517, None, 0.00764935, None, -0.000548434, None, 0.00764935, None, -0.000548434, None, 1.45683, None, 0.00911424, None, 1.45683, None, 0.00911424, None)

reports.append(Report(604062856, ("CSC", 2, 4, 2, 17), "MEm42_17"))
reports[-1].posNum = 69662
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00460658, 0.00665006, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.91223e-05, 6.83378e-05, 0), \
                           -123272, 69662, 69662, -nan)
reports[-1].sigmaresid = ValErr(1.41997, 0.00380423, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00109947, None, -0.000288529, None, 0.000649267, None, -0.000437039, None, 0.000649267, None, -0.000437039, None, 0.00916875, None, -0.000480781, None, 0.00916875, None, -0.000480781, None, 1.41998, None, 0.00944974, None, 1.41998, None, 0.00944974, None)

reports.append(Report(604062872, ("CSC", 2, 4, 2, 19), "MEm42_19"))
reports[-1].posNum = 75432
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00134446, 0.00607996, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.91198e-05, 6.53059e-05, 0), \
                           -135601, 75432, 75432, -nan)
reports[-1].sigmaresid = ValErr(1.46041, 0.00375994, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00330475, None, 0.00181994, None, -2.93611e-05, None, 0.00145412, None, -2.93611e-05, None, 0.00145412, None, -0.0012128, None, 0.00160247, None, -0.0012128, None, 0.00160247, None, 1.46041, None, 0.00968882, None, 1.46041, None, 0.00968882, None)

reports.append(Report(604062888, ("CSC", 2, 4, 2, 21), "MEm42_21"))
reports[-1].posNum = 72834
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.010866, 0.00625725, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000149113, 6.484e-05, 0), \
                           -130284, 72834, 72834, -nan)
reports[-1].sigmaresid = ValErr(1.4475, 0.00379261, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00208185, None, 0.000697344, None, 0.00344567, None, 0.000448606, None, 0.00344567, None, 0.000448606, None, -0.000698398, None, 0.000469427, None, -0.000698398, None, 0.000469427, None, 1.44756, None, 0.00969993, None, 1.44756, None, 0.00969993, None)

reports.append(Report(604062904, ("CSC", 2, 4, 2, 23), "MEm42_23"))
reports[-1].posNum = 76788
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000128854, 0.00585756, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.83792e-06, 6.20522e-05, 0), \
                           -139299, 76788, 76788, -nan)
reports[-1].sigmaresid = ValErr(1.48457, 0.00378826, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00361729, None, -0.00115214, None, 6.87706e-05, None, -0.00124101, None, 6.87706e-05, None, -0.00124101, None, -0.000501821, None, -0.00126592, None, -0.000501821, None, -0.00126592, None, 1.48458, None, 0.0101474, None, 1.48458, None, 0.0101474, None)

reports.append(Report(604062920, ("CSC", 2, 4, 2, 25), "MEm42_25"))
reports[-1].posNum = 65316
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00513579, 0.00685052, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000109982, 6.85992e-05, 0), \
                           -114958, 65316, 65316, -nan)
reports[-1].sigmaresid = ValErr(1.40647, 0.00389141, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000782463, None, 0.000192653, None, -0.00141061, None, -6.55004e-06, None, -0.00141061, None, -6.55004e-06, None, 1.87345e-05, None, 4.76982e-05, None, 1.87345e-05, None, 4.76982e-05, None, 1.4065, None, 0.00987615, None, 1.4065, None, 0.00987615, None)

reports.append(Report(604062936, ("CSC", 2, 4, 2, 27), "MEm42_27"))
reports[-1].posNum = 60810
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00197915, 0.00733049, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.49423e-06, 7.28352e-05, 0), \
                           -106769, 60810, 60810, -nan)
reports[-1].sigmaresid = ValErr(1.40052, 0.00401592, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00804756, None, -0.00218446, None, 0.00188422, None, -0.00217203, None, 0.00188422, None, -0.00217203, None, -0.00432381, None, -0.00230418, None, -0.00432381, None, -0.00230418, None, 1.40052, None, 0.00902366, None, 1.40052, None, 0.00902366, None)

reports.append(Report(604062952, ("CSC", 2, 4, 2, 29), "MEm42_29"))
reports[-1].posNum = 64606
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0192548, 0.00673436, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000225857, 6.75036e-05, 0), \
                           -114917, 64606, 64606, -nan)
reports[-1].sigmaresid = ValErr(1.43303, 0.00398662, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000105936, None, -0.000482162, None, -0.00692287, None, -0.000670954, None, -0.00692287, None, -0.000670954, None, -0.00210582, None, -0.000699831, None, -0.00210582, None, -0.000699831, None, 1.43316, None, 0.00902209, None, 1.43316, None, 0.00902209, None)

reports.append(Report(604062968, ("CSC", 2, 4, 2, 31), "MEm42_31"))
reports[-1].posNum = 60116
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00921364, 0.00743152, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.39919e-05, 7.35555e-05, 0), \
                           -105661, 60116, 60116, -nan)
reports[-1].sigmaresid = ValErr(1.4031, 0.00404649, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00557822, None, -0.00239778, None, 0.00444518, None, -0.00248332, None, 0.00444518, None, -0.00248332, None, 0.00647091, None, -0.00257914, None, 0.00647091, None, -0.00257914, None, 1.40311, None, 0.00896801, None, 1.40311, None, 0.00896801, None)

reports.append(Report(604062984, ("CSC", 2, 4, 2, 33), "MEm42_33"))
reports[-1].posNum = 71224
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00562881, 0.00624044, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.32121e-05, 6.63882e-05, 0), \
                           -126624, 71224, 71224, -nan)
reports[-1].sigmaresid = ValErr(1.43174, 0.00379345, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00417721, None, -0.00265538, None, 0.00211084, None, -0.00270949, None, 0.00211084, None, -0.00270949, None, 0.00541847, None, -0.00280859, None, 0.00541847, None, -0.00280859, None, 1.43175, None, 0.00962892, None, 1.43175, None, 0.00962892, None)

reports.append(Report(604063000, ("CSC", 2, 4, 2, 35), "MEm42_35"))
reports[-1].posNum = 76096
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00273742, 0.00606656, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.44873e-05, 6.23176e-05, 0), \
                           -136612, 76096, 76096, -nan)
reports[-1].sigmaresid = ValErr(1.4569, 0.00373451, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000244382, None, -0.00158765, None, -0.00156284, None, -0.001722, None, -0.00156284, None, -0.001722, None, -0.00304805, None, -0.00184721, None, -0.00304805, None, -0.00184721, None, 1.45691, None, 0.0100807, None, 1.45691, None, 0.0100807, None)

reports.append(Report(604062736, ("CSC", 2, 4, 2, 2), "MEm42_02"))
reports[-1].posNum = 58366
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00519525, 0.00694457, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(8.60907e-05, 7.33831e-05, 0), \
                           -107430, 58366, 58366, -nan)
reports[-1].sigmaresid = ValErr(1.52452, 0.0044621, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00725046, None, -0.00299889, None, -0.00179235, None, -0.00300288, None, -0.00179235, None, -0.00300288, None, -0.0029328, None, -0.00317954, None, -0.0029328, None, -0.00317954, None, 1.52454, None, 0.00879935, None, 1.52454, None, 0.00879935, None)

reports.append(Report(604062752, ("CSC", 2, 4, 2, 4), "MEm42_04"))
reports[-1].posNum = 75014
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00555564, 0.006477, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.00077e-05, 6.85367e-05, 0), \
                           -135662, 75014, 75014, -nan)
reports[-1].sigmaresid = ValErr(1.47632, 0.00381147, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0016071, None, -0.00164417, None, -0.00293495, None, -0.00177762, None, -0.00293495, None, -0.00177762, None, 0.000930944, None, -0.00185948, None, 0.000930944, None, -0.00185948, None, 1.47633, None, 0.00814631, None, 1.47633, None, 0.00814631, None)

reports.append(Report(604062768, ("CSC", 2, 4, 2, 6), "MEm42_06"))
reports[-1].posNum = 62586
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000404701, 0.00657355, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.98648e-05, 7.32014e-05, 0), \
                           -114544, 62586, 62586, -nan)
reports[-1].sigmaresid = ValErr(1.50869, 0.00426428, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00124128, None, -0.00435012, None, 0.00030593, None, -0.00431643, None, 0.00030593, None, -0.00431643, None, 0.00165299, None, -0.00449196, None, 0.00165299, None, -0.00449196, None, 1.50869, None, 0.00876221, None, 1.50869, None, 0.00876221, None)

reports.append(Report(604062784, ("CSC", 2, 4, 2, 8), "MEm42_08"))
reports[-1].posNum = 55170
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000754201, 0.00733662, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.5686e-05, 7.71085e-05, 0), \
                           -100319, 55170, 55170, -nan)
reports[-1].sigmaresid = ValErr(1.49097, 0.00448854, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00422907, None, -0.00223492, None, 0.00150304, None, -0.00238275, None, 0.00150304, None, -0.00238275, None, 0.000483429, None, -0.00227121, None, 0.000483429, None, -0.00227121, None, 1.49096, None, 0.00956853, None, 1.49096, None, 0.00956853, None)

reports.append(Report(604062800, ("CSC", 2, 4, 2, 10), "MEm42_10"))
reports[-1].posNum = 76490
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00139748, 0.00603465, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.40344e-05, 6.36841e-05, 0), \
                           -140324, 76490, 76490, -nan)
reports[-1].sigmaresid = ValErr(1.51528, 0.00387413, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000476085, None, -0.000713099, None, -0.00114785, None, -0.000876035, None, -0.00114785, None, -0.000876035, None, -0.0121219, None, -0.000909479, None, -0.0121219, None, -0.000909479, None, 1.51529, None, 0.00840443, None, 1.51529, None, 0.00840443, None)

reports.append(Report(604062816, ("CSC", 2, 4, 2, 12), "MEm42_12"))
reports[-1].posNum = 77370
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00198153, 0.00617525, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.68618e-05, 6.56971e-05, 0), \
                           -139926, 77370, 77370, -nan)
reports[-1].sigmaresid = ValErr(1.47637, 0.00375314, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00073968, None, -0.000279492, None, -0.000690778, None, -0.000311046, None, -0.000690778, None, -0.000311046, None, -0.00306198, None, -0.000380595, None, -0.00306198, None, -0.000380595, None, 1.47637, None, 0.00823682, None, 1.47637, None, 0.00823682, None)

reports.append(Report(604062832, ("CSC", 2, 4, 2, 14), "MEm42_14"))
reports[-1].posNum = 76468
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00922287, 0.00617049, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000111625, 6.53162e-05, 0), \
                           -139654, 76468, 76468, -nan)
reports[-1].sigmaresid = ValErr(1.50285, 0.00384288, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00308564, None, 0.00027209, None, -0.00422637, None, 8.45254e-05, None, -0.00422637, None, 8.45254e-05, None, -0.0032693, None, 0.000125907, None, -0.0032693, None, 0.000125907, None, 1.50288, None, 0.00854471, None, 1.50288, None, 0.00854471, None)

reports.append(Report(604062848, ("CSC", 2, 4, 2, 16), "MEm42_16"))
reports[-1].posNum = 75448
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00144046, 0.00682645, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(9.96889e-06, 7.23319e-05, 0), \
                           -137769, 75448, 75448, -nan)
reports[-1].sigmaresid = ValErr(1.50242, 0.0038677, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.005445, None, -0.00170226, None, -0.000876895, None, -0.00183097, None, -0.000876895, None, -0.00183097, None, -0.00665307, None, -0.00194474, None, -0.00665307, None, -0.00194474, None, 1.50242, None, 0.00861826, None, 1.50242, None, 0.00861826, None)

reports.append(Report(604062864, ("CSC", 2, 4, 2, 18), "MEm42_18"))
reports[-1].posNum = 76010
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00894035, 0.00617878, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.60395e-05, 6.39626e-05, 0), \
                           -138509, 76010, 76010, -nan)
reports[-1].sigmaresid = ValErr(1.49676, 0.00383886, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00890136, None, 0.00105913, None, 0.00451044, None, 0.000831511, None, 0.00451044, None, 0.000831511, None, -0.00423263, None, 0.000825163, None, -0.00423263, None, 0.000825163, None, 1.49679, None, 0.00859859, None, 1.49679, None, 0.00859859, None)

reports.append(Report(604062880, ("CSC", 2, 4, 2, 20), "MEm42_20"))
reports[-1].posNum = 77958
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00555004, 0.00615977, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000111255, 6.5339e-05, 0), \
                           -141599, 77958, 77958, -nan)
reports[-1].sigmaresid = ValErr(1.48796, 0.0037683, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00159073, None, 0.000264292, None, 0.000290544, None, 5.55985e-05, None, 0.000290544, None, 5.55985e-05, None, -0.00407948, None, 8.68507e-05, None, -0.00407948, None, 8.68507e-05, None, 1.48799, None, 0.00829161, None, 1.48799, None, 0.00829161, None)

reports.append(Report(604062896, ("CSC", 2, 4, 2, 22), "MEm42_22"))
reports[-1].posNum = 77356
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00469564, 0.006069, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.73876e-05, 6.35436e-05, 0), \
                           -140587, 77356, 77356, -nan)
reports[-1].sigmaresid = ValErr(1.48953, 0.00378692, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0051635, None, 4.35515e-05, None, -0.00346519, None, -0.00011914, None, -0.00346519, None, -0.00011914, None, -0.0168162, None, -0.000144482, None, -0.0168162, None, -0.000144482, None, 1.48953, None, 0.00871176, None, 1.48953, None, 0.00871176, None)

reports.append(Report(604062912, ("CSC", 2, 4, 2, 24), "MEm42_24"))
reports[-1].posNum = 80260
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00359467, 0.00599784, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.62268e-05, 6.32168e-05, 0), \
                           -147153, 80260, 80260, -nan)
reports[-1].sigmaresid = ValErr(1.51364, 0.00377796, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00134062, None, -0.00148539, None, 0.00116977, None, -0.00156588, None, 0.00116977, None, -0.00156588, None, 0.00142003, None, -0.0016745, None, 0.00142003, None, -0.0016745, None, 1.51365, None, 0.00884895, None, 1.51365, None, 0.00884895, None)

reports.append(Report(604062928, ("CSC", 2, 4, 2, 26), "MEm42_26"))
reports[-1].posNum = 56880
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0127037, 0.00772008, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000152699, 7.84727e-05, 0), \
                           -100571, 56880, 56880, -nan)
reports[-1].sigmaresid = ValErr(1.41793, 0.00420396, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0023138, None, 0.00103723, None, 0.00311604, None, 0.000933414, None, 0.00311604, None, 0.000933414, None, -0.00346147, None, 0.000955385, None, -0.00346147, None, 0.000955385, None, 1.41797, None, 0.00837018, None, 1.41797, None, 0.00837018, None)

reports.append(Report(604062944, ("CSC", 2, 4, 2, 28), "MEm42_28"))
reports[-1].posNum = 65524
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0204272, 0.00756586, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000188041, 7.77693e-05, 0), \
                           -118251, 65524, 65524, -nan)
reports[-1].sigmaresid = ValErr(1.47074, 0.00406275, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00507255, None, 0.00128088, None, -0.008525, None, 0.000921756, None, -0.008525, None, 0.000921756, None, -0.00417871, None, 0.00104525, None, -0.00417871, None, 0.00104525, None, 1.4708, None, 0.00799424, None, 1.4708, None, 0.00799424, None)

reports.append(Report(604062960, ("CSC", 2, 4, 2, 30), "MEm42_30"))
reports[-1].posNum = 59034
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00665654, 0.00802852, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000115805, 7.96842e-05, 0), \
                           -104064, 59034, 59034, -nan)
reports[-1].sigmaresid = ValErr(1.41036, 0.00410453, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-8.0612e-05, None, -0.00249252, None, -0.00140403, None, -0.00256153, None, -0.00140403, None, -0.00256153, None, -0.00505969, None, -0.00268322, None, -0.00505969, None, -0.00268322, None, 1.41038, None, 0.00829331, None, 1.41038, None, 0.00829331, None)

reports.append(Report(604062976, ("CSC", 2, 4, 2, 32), "MEm42_32"))
reports[-1].posNum = 66908
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00318388, 0.00714037, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.64166e-05, 7.45224e-05, 0), \
                           -119819, 66908, 66908, -nan)
reports[-1].sigmaresid = ValErr(1.45043, 0.00396499, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00540159, None, 7.00406e-05, None, -0.000163134, None, -5.34951e-05, None, -0.000163134, None, -5.34951e-05, None, -0.00692937, None, -7.85591e-05, None, -0.00692937, None, -7.85591e-05, None, 1.45043, None, 0.00794986, None, 1.45043, None, 0.00794986, None)

reports.append(Report(604062992, ("CSC", 2, 4, 2, 34), "MEm42_34"))
reports[-1].posNum = 64784
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00210996, 0.00661494, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.2476e-05, 7.02068e-05, 0), \
                           -117826, 64784, 64784, -nan)
reports[-1].sigmaresid = ValErr(1.49155, 0.00414369, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00353884, None, 0.000283882, None, -0.000621844, None, 4.19165e-05, None, -0.000621844, None, 4.19165e-05, None, -0.000948951, None, 9.50394e-05, None, -0.000948951, None, 9.50394e-05, None, 1.49155, None, 0.00809755, None, 1.49155, None, 0.00809755, None)

reports.append(Report(604063008, ("CSC", 2, 4, 2, 36), "MEm42_36"))
reports[-1].posNum = 81728
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00614885, 0.00586204, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0001096, 6.12546e-05, 0), \
                           -149584, 81728, 81728, -nan)
reports[-1].sigmaresid = ValErr(1.50882, 0.00373196, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00271059, None, -0.00232923, None, -0.00158269, None, -0.00238859, None, -0.00158269, None, -0.00238859, None, 0.00125456, None, -0.00243627, None, 0.00125456, None, -0.00243627, None, 1.50885, None, 0.00845506, None, 1.50885, None, 0.00845506, None)

