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
reports[-1].posNum = 104626
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00119675, 0.000605829, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.120976, 0.0477544, 0), \
                           ValErr(0.000923165, 0.00126576, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.35475e-05, 1.58672e-05, 0), \
                           24808.7, 104626, 104626, -nan)
reports[-1].sigmaresid = ValErr(0.19089, 0.000417301, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000921349, None, -1.2182e-06, None, -0.00099792, None, 9.36572e-06, None, -0.00099792, None, 9.36572e-06, None, 0.000118007, None, 5.02253e-06, None, 0.000118007, None, 5.02253e-06, None, 0.1909, None, 0.004165, None, 0.1909, None, 0.004165, None)

reports.append(Report(604017688, ("CSC", 1, 1, 1, 3), "MEp11_03"))
reports[-1].posNum = 105037
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00173429, 0.000601585, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0443993, 0.0471044, 0), \
                           ValErr(0.000368832, 0.0012467, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.82719e-05, 1.55954e-05, 0), \
                           25862, 105037, 105037, -nan)
reports[-1].sigmaresid = ValErr(0.189161, 0.00041271, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00131936, None, 1.21896e-06, None, -0.00156145, None, -6.13476e-06, None, -0.00156145, None, -6.13476e-06, None, -0.00154292, None, 1.19795e-05, None, -0.00154292, None, 1.19795e-05, None, 0.189163, None, 0.00431122, None, 0.189163, None, 0.00431122, None)

reports.append(Report(604017704, ("CSC", 1, 1, 1, 5), "MEp11_05"))
reports[-1].posNum = 104849
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00143846, 0.000604449, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0711737, 0.047659, 0), \
                           ValErr(-0.00130612, 0.00125539, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.89401e-05, 1.57148e-05, 0), \
                           24969.8, 104849, 104849, -nan)
reports[-1].sigmaresid = ValErr(0.190693, 0.000416427, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00141488, None, -6.40944e-06, None, -0.00127307, None, -7.77799e-07, None, -0.00127307, None, -7.77799e-07, None, -0.00133553, None, 1.69937e-07, None, -0.00133553, None, 1.69937e-07, None, 0.190697, None, 0.00415817, None, 0.190697, None, 0.00415817, None)

reports.append(Report(604017720, ("CSC", 1, 1, 1, 7), "MEp11_07"))
reports[-1].posNum = 105244
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00124454, 0.000602823, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.102333, 0.0473858, 0), \
                           ValErr(-0.00177376, 0.001254, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.32636e-05, 1.57048e-05, 0), \
                           25196.6, 105244, 105244, -nan)
reports[-1].sigmaresid = ValErr(0.190453, 0.000415121, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00115528, None, -6.61322e-06, None, -0.00160904, None, -6.82259e-06, None, -0.00160904, None, -6.82259e-06, None, -0.0020207, None, 1.81362e-05, None, -0.0020207, None, 1.81362e-05, None, 0.190465, None, 0.00419258, None, 0.190465, None, 0.00419258, None)

reports.append(Report(604017736, ("CSC", 1, 1, 1, 9), "MEp11_09"))
reports[-1].posNum = 104531
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00177987, 0.000602837, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0862456, 0.0473674, 0), \
                           ValErr(-0.000322426, 0.00125473, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.62969e-05, 1.57664e-05, 0), \
                           25411.3, 104531, 104531, -nan)
reports[-1].sigmaresid = ValErr(0.189752, 0.000414998, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000327877, None, 6.06972e-06, None, -0.00137566, None, 7.51328e-06, None, -0.00137566, None, 7.51328e-06, None, -0.000217536, None, -2.67879e-05, None, -0.000217536, None, -2.67879e-05, None, 0.189763, None, 0.00438794, None, 0.189763, None, 0.00438794, None)

reports.append(Report(604017752, ("CSC", 1, 1, 1, 11), "MEp11_11"))
reports[-1].posNum = 104551
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00120835, 0.000608085, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.165322, 0.0478547, 0), \
                           ValErr(-0.00220064, 0.00126423, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.37387e-05, 1.58999e-05, 0), \
                           24327, 104551, 104551, -nan)
reports[-1].sigmaresid = ValErr(0.191739, 0.000419307, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00175535, None, -1.2347e-05, None, -0.0010825, None, -3.54079e-05, None, -0.0010825, None, -3.54079e-05, None, -0.00164685, None, -6.86336e-06, None, -0.00164685, None, -6.86336e-06, None, 0.191751, None, 0.00451606, None, 0.191751, None, 0.00451606, None)

reports.append(Report(604017768, ("CSC", 1, 1, 1, 13), "MEp11_13"))
reports[-1].posNum = 105188
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0030527, 0.000600934, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0859368, 0.0471602, 0), \
                           ValErr(-0.000750973, 0.00125061, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.32788e-06, 1.56519e-05, 0), \
                           25741.9, 105188, 105188, -nan)
reports[-1].sigmaresid = ValErr(0.189444, 0.00041303, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0028218, None, -3.51849e-06, None, -0.00300936, None, 2.91817e-06, None, -0.00300936, None, 2.91817e-06, None, -0.00295166, None, -1.83854e-06, None, -0.00295166, None, -1.83854e-06, None, 0.189447, None, 0.00417552, None, 0.189447, None, 0.00417552, None)

reports.append(Report(604017784, ("CSC", 1, 1, 1, 15), "MEp11_15"))
reports[-1].posNum = 103541
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00137489, 0.000606669, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0706364, 0.0476613, 0), \
                           ValErr(-0.000640574, 0.00126337, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.40778e-05, 1.58631e-05, 0), \
                           24980.1, 103541, 103541, -nan)
reports[-1].sigmaresid = ValErr(0.190101, 0.000417747, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00113049, None, 5.5454e-07, None, -0.00125019, None, -1.02747e-05, None, -0.00125019, None, -1.02747e-05, None, -0.000277701, None, -9.70578e-06, None, -0.000277701, None, -9.70578e-06, None, 0.190104, None, 0.00449203, None, 0.190104, None, 0.00449203, None)

reports.append(Report(604017800, ("CSC", 1, 1, 1, 17), "MEp11_17"))
reports[-1].posNum = 105291
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00174287, 0.000599213, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0668451, 0.0471784, 0), \
                           ValErr(-0.000774096, 0.00124738, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.51874e-05, 1.55719e-05, 0), \
                           26098.1, 105291, 105291, -nan)
reports[-1].sigmaresid = ValErr(0.188849, 0.000411532, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00235403, None, 4.34365e-06, None, -0.00160256, None, -1.55996e-06, None, -0.00160256, None, -1.55996e-06, None, -0.00127411, None, -1.26768e-05, None, -0.00127411, None, -1.26768e-05, None, 0.188852, None, 0.0041933, None, 0.188852, None, 0.0041933, None)

reports.append(Report(604017816, ("CSC", 1, 1, 1, 19), "MEp11_19"))
reports[-1].posNum = 104391
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00139544, 0.000603691, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0505896, 0.0474511, 0), \
                           ValErr(-0.00112868, 0.00125452, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.33322e-07, 1.58205e-05, 0), \
                           25202.5, 104391, 104391, -nan)
reports[-1].sigmaresid = ValErr(0.19007, 0.000415972, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00129946, None, 4.1548e-06, None, -0.00140163, None, -1.84302e-06, None, -0.00140163, None, -1.84302e-06, None, -0.000655179, None, -2.2598e-05, None, -0.000655179, None, -2.2598e-05, None, 0.190071, None, 0.00421781, None, 0.190071, None, 0.00421781, None)

reports.append(Report(604017832, ("CSC", 1, 1, 1, 21), "MEp11_21"))
reports[-1].posNum = 105217
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00203054, 0.000598277, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0516388, 0.0471007, 0), \
                           ValErr(-0.000738558, 0.00124269, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(8.41032e-06, 1.55337e-05, 0), \
                           26168.6, 105217, 105217, -nan)
reports[-1].sigmaresid = ValErr(0.18869, 0.000411329, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00165871, None, 4.77876e-06, None, -0.00195125, None, -1.92618e-05, None, -0.00195125, None, -1.92618e-05, None, -0.00405509, None, -2.57078e-05, None, -0.00405509, None, -2.57078e-05, None, 0.188691, None, 0.00427305, None, 0.188691, None, 0.00427305, None)

reports.append(Report(604017848, ("CSC", 1, 1, 1, 23), "MEp11_23"))
reports[-1].posNum = 104455
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00271121, 0.000606942, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0651366, 0.0477439, 0), \
                           ValErr(0.000809668, 0.0012618, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.65793e-05, 1.58532e-05, 0), \
                           24691.2, 104455, 104455, -nan)
reports[-1].sigmaresid = ValErr(0.191031, 0.00041795, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00193242, None, 5.43552e-06, None, -0.00248433, None, -1.02017e-06, None, -0.00248433, None, -1.02017e-06, None, -0.00248163, None, -7.20405e-06, None, -0.00248163, None, -7.20405e-06, None, 0.191036, None, 0.00486636, None, 0.191036, None, 0.00486636, None)

reports.append(Report(604017864, ("CSC", 1, 1, 1, 25), "MEp11_25"))
reports[-1].posNum = 104829
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00263233, 0.00060361, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0508792, 0.0473433, 0), \
                           ValErr(-0.00158971, 0.0012525, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.72029e-05, 1.57303e-05, 0), \
                           25280.6, 104829, 104829, -nan)
reports[-1].sigmaresid = ValErr(0.19012, 0.000415211, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00148603, None, 6.88696e-06, None, -0.00230368, None, 7.43128e-06, None, -0.00230368, None, 7.43128e-06, None, 0.00073207, None, -1.08494e-05, None, 0.00073207, None, -1.08494e-05, None, 0.190127, None, 0.00471496, None, 0.190127, None, 0.00471496, None)

reports.append(Report(604017880, ("CSC", 1, 1, 1, 27), "MEp11_27"))
reports[-1].posNum = 104735
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0014474, 0.000602291, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0594963, 0.0473757, 0), \
                           ValErr(-0.00315169, 0.0012549, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.29164e-06, 1.57364e-05, 0), \
                           25492, 104735, 104735, -nan)
reports[-1].sigmaresid = ValErr(0.189695, 0.000414471, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00142026, None, 4.59781e-06, None, -0.00140948, None, -1.42339e-05, None, -0.00140948, None, -1.42339e-05, None, -0.00137759, None, -2.23854e-05, None, -0.00137759, None, -2.23854e-05, None, 0.189702, None, 0.00416098, None, 0.189702, None, 0.00416098, None)

reports.append(Report(604017896, ("CSC", 1, 1, 1, 29), "MEp11_29"))
reports[-1].posNum = 103763
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00399395, 0.000606801, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.150633, 0.0478146, 0), \
                           ValErr(-0.00136648, 0.00127698, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.12714e-05, 1.59054e-05, 0), \
                           24736.8, 103763, 103763, -nan)
reports[-1].sigmaresid = ValErr(0.190646, 0.000418497, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00416104, None, 1.51336e-05, None, -0.00381263, None, 1.85958e-05, None, -0.00381263, None, 1.85958e-05, None, -0.00289701, None, 1.80414e-05, None, -0.00289701, None, 1.80414e-05, None, 0.190657, None, 0.00418458, None, 0.190657, None, 0.00418458, None)

reports.append(Report(604017912, ("CSC", 1, 1, 1, 31), "MEp11_31"))
reports[-1].posNum = 104844
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000627352, 0.000603208, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0777906, 0.0475075, 0), \
                           ValErr(-0.00261706, 0.00125422, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.98353e-05, 1.56865e-05, 0), \
                           25215.3, 104844, 104844, -nan)
reports[-1].sigmaresid = ValErr(0.190245, 0.000415458, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00101284, None, -3.50192e-06, None, -0.000810729, None, -4.93282e-06, None, -0.000810729, None, -4.93282e-06, None, -0.000444619, None, -1.99427e-05, None, -0.000444619, None, -1.99427e-05, None, 0.190252, None, 0.00410769, None, 0.190252, None, 0.00410769, None)

reports.append(Report(604017928, ("CSC", 1, 1, 1, 33), "MEp11_33"))
reports[-1].posNum = 104179
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00168593, 0.000608643, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.110794, 0.0477641, 0), \
                           ValErr(-0.00225542, 0.00127068, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.47075e-07, 1.5969e-05, 0), \
                           24412, 104179, 104179, -nan)
reports[-1].sigmaresid = ValErr(0.191424, 0.000419364, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00197828, None, -8.22603e-06, None, -0.00169649, None, -1.61086e-05, None, -0.00169649, None, -1.61086e-05, None, 0.000763948, None, -1.8105e-05, None, 0.000763948, None, -1.8105e-05, None, 0.19143, None, 0.00434496, None, 0.19143, None, 0.00434496, None)

reports.append(Report(604017944, ("CSC", 1, 1, 1, 35), "MEp11_35"))
reports[-1].posNum = 105248
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00172175, 0.000598238, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0597798, 0.0469182, 0), \
                           ValErr(0.000903613, 0.00123673, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(7.27668e-06, 1.55463e-05, 0), \
                           26265.6, 105248, 105248, -nan)
reports[-1].sigmaresid = ValErr(0.18853, 0.000410921, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00148952, None, -2.38614e-06, None, -0.0016586, None, -7.52373e-06, None, -0.0016586, None, -7.52373e-06, None, -0.00136246, None, -1.46141e-05, None, -0.00136246, None, -1.46141e-05, None, 0.188533, None, 0.0042252, None, 0.188533, None, 0.0042252, None)

reports.append(Report(604017680, ("CSC", 1, 1, 1, 2), "MEp11_02"))
reports[-1].posNum = 104404
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000767389, 0.000543695, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0686402, 0.0402699, 0), \
                           ValErr(0.000698481, 0.0010683, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.62312e-05, 1.40812e-05, 0), \
                           36525.2, 104404, 104404, -nan)
reports[-1].sigmaresid = ValErr(0.17054, 0.00037321, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000962466, None, 8.93555e-06, None, -0.000918631, None, 4.76053e-05, None, -0.000918631, None, 4.76053e-05, None, -0.000740874, None, 3.70375e-05, None, -0.000740874, None, 3.70375e-05, None, 0.170545, None, 0.00446884, None, 0.170545, None, 0.00446884, None)

reports.append(Report(604017696, ("CSC", 1, 1, 1, 4), "MEp11_04"))
reports[-1].posNum = 104492
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000816608, 0.000539779, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.119614, 0.0401431, 0), \
                           ValErr(-0.00134121, 0.00106317, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.1786e-06, 1.39772e-05, 0), \
                           37189.4, 104492, 104492, -nan)
reports[-1].sigmaresid = ValErr(0.16951, 0.000370799, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000585618, None, -8.87045e-06, None, -0.000863715, None, -9.56083e-06, None, -0.000863715, None, -9.56083e-06, None, 0.000379708, None, -2.43417e-05, None, 0.000379708, None, -2.43417e-05, None, 0.169517, None, 0.00528226, None, 0.169517, None, 0.00528226, None)

reports.append(Report(604017712, ("CSC", 1, 1, 1, 6), "MEp11_06"))
reports[-1].posNum = 104691
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00156289, 0.00054356, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.044424, 0.0402968, 0), \
                           ValErr(-0.000100005, 0.00106827, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.779e-06, 1.4106e-05, 0), \
                           36503.3, 104691, 104691, -nan)
reports[-1].sigmaresid = ValErr(0.17074, 0.000373134, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00187768, None, 8.47162e-06, None, -0.001579, None, 2.76261e-05, None, -0.001579, None, 2.76261e-05, None, -0.00152747, None, 2.93894e-05, None, -0.00152747, None, 2.93894e-05, None, 0.170741, None, 0.00442216, None, 0.170741, None, 0.00442216, None)

reports.append(Report(604017728, ("CSC", 1, 1, 1, 8), "MEp11_08"))
reports[-1].posNum = 103808
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000744291, 0.00054329, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0536157, 0.0402864, 0), \
                           ValErr(-0.000925653, 0.00106569, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.94885e-06, 1.40504e-05, 0), \
                           36841.2, 103808, 103808, -nan)
reports[-1].sigmaresid = ValErr(0.169681, 0.000372394, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000188369, None, -2.47582e-06, None, -0.0007704, None, -9.66833e-06, None, -0.0007704, None, -9.66833e-06, None, 0.000734164, None, -1.15114e-05, None, 0.000734164, None, -1.15114e-05, None, 0.169683, None, 0.00447815, None, 0.169683, None, 0.00447815, None)

reports.append(Report(604017744, ("CSC", 1, 1, 1, 10), "MEp11_10"))
reports[-1].posNum = 104532
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000472327, 0.000544378, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0944354, 0.0403807, 0), \
                           ValErr(-0.000153574, 0.00106989, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.76177e-06, 1.40984e-05, 0), \
                           36349.6, 104532, 104532, -nan)
reports[-1].sigmaresid = ValErr(0.1709, 0.000373769, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000690821, None, 1.49633e-06, None, -0.000446385, None, 1.92601e-05, None, -0.000446385, None, 1.92601e-05, None, 0.000474721, None, -9.71185e-06, None, 0.000474721, None, -9.71185e-06, None, 0.170905, None, 0.00443444, None, 0.170905, None, 0.00443444, None)

reports.append(Report(604017760, ("CSC", 1, 1, 1, 12), "MEp11_12"))
reports[-1].posNum = 104555
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00165471, 0.000538651, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0591435, 0.0401149, 0), \
                           ValErr(-0.00061779, 0.00105889, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.82793e-06, 1.39394e-05, 0), \
                           37386.2, 104555, 104555, -nan)
reports[-1].sigmaresid = ValErr(0.169227, 0.000370069, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00184958, None, 1.14745e-05, None, -0.00169589, None, 2.53467e-05, None, -0.00169589, None, 2.53467e-05, None, -0.00191299, None, 7.06734e-06, None, -0.00191299, None, 7.06734e-06, None, 0.169229, None, 0.00438702, None, 0.169229, None, 0.00438702, None)

reports.append(Report(604017776, ("CSC", 1, 1, 1, 14), "MEp11_14"))
reports[-1].posNum = 104126
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000549996, 0.000542697, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.106124, 0.0403057, 0), \
                           ValErr(0.0012142, 0.0010687, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.76556e-06, 1.40574e-05, 0), \
                           36805.4, 104126, 104126, -nan)
reports[-1].sigmaresid = ValErr(0.169923, 0.000372356, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00107578, None, -1.59633e-06, None, -0.000527108, None, 2.33039e-06, None, -0.000527108, None, 2.33039e-06, None, -3.80815e-05, None, 3.38546e-06, None, -3.80815e-05, None, 3.38546e-06, None, 0.169932, None, 0.00528304, None, 0.169932, None, 0.00528304, None)

reports.append(Report(604017792, ("CSC", 1, 1, 1, 16), "MEp11_16"))
reports[-1].posNum = 103739
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00310693, 0.000543765, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.118561, 0.0404792, 0), \
                           ValErr(-0.0027799, 0.00107196, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.62698e-05, 1.4101e-05, 0), \
                           36588.2, 103739, 103739, -nan)
reports[-1].sigmaresid = ValErr(0.170055, 0.000373339, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00256091, None, 1.56215e-05, None, -0.00296189, None, 3.60015e-05, None, -0.00296189, None, 3.60015e-05, None, -0.0037904, None, 3.18605e-05, None, -0.0037904, None, 3.18605e-05, None, 0.170066, None, 0.00465666, None, 0.170066, None, 0.00465666, None)

reports.append(Report(604017808, ("CSC", 1, 1, 1, 18), "MEp11_18"))
reports[-1].posNum = 104767
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00164671, 0.000540178, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.10346, 0.0401873, 0), \
                           ValErr(0.000258787, 0.0010606, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.93338e-05, 1.39798e-05, 0), \
                           37110.4, 104767, 104767, -nan)
reports[-1].sigmaresid = ValErr(0.169796, 0.000370937, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00139804, None, 2.00746e-05, None, -0.00147269, None, 3.84985e-05, None, -0.00147269, None, 3.84985e-05, None, -0.001455, None, 3.25688e-05, None, -0.001455, None, 3.25688e-05, None, 0.169804, None, 0.00458801, None, 0.169804, None, 0.00458801, None)

reports.append(Report(604017824, ("CSC", 1, 1, 1, 20), "MEp11_20"))
reports[-1].posNum = 104613
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0019071, 0.000541577, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0759033, 0.0402461, 0), \
                           ValErr(-0.00158442, 0.00106341, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.13201e-05, 1.40242e-05, 0), \
                           36972.6, 104613, 104613, -nan)
reports[-1].sigmaresid = ValErr(0.169931, 0.000371505, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00150392, None, 1.65374e-05, None, -0.00162153, None, 3.8153e-05, None, -0.00162153, None, 3.8153e-05, None, -0.00181719, None, 3.34061e-05, None, -0.00181719, None, 3.34061e-05, None, 0.169939, None, 0.00493613, None, 0.169939, None, 0.00493613, None)

reports.append(Report(604017840, ("CSC", 1, 1, 1, 22), "MEp11_22"))
reports[-1].posNum = 103890
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00188797, 0.000541537, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.103459, 0.0400889, 0), \
                           ValErr(-0.000705725, 0.00106371, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.56426e-05, 1.40298e-05, 0), \
                           37168, 103890, 103890, -nan)
reports[-1].sigmaresid = ValErr(0.169195, 0.000371182, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00225383, None, 7.42668e-06, None, -0.00204811, None, -2.20642e-05, None, -0.00204811, None, -2.20642e-05, None, -0.00186888, None, 3.85626e-07, None, -0.00186888, None, 3.85626e-07, None, 0.169202, None, 0.00474286, None, 0.169202, None, 0.00474286, None)

reports.append(Report(604017856, ("CSC", 1, 1, 1, 24), "MEp11_24"))
reports[-1].posNum = 103930
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00260978, 0.000543371, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0472737, 0.0404521, 0), \
                           ValErr(-0.000861276, 0.00106446, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.29088e-05, 1.40627e-05, 0), \
                           36588.8, 103930, 103930, -nan)
reports[-1].sigmaresid = ValErr(0.170164, 0.000373236, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00226801, None, 1.50373e-05, None, -0.0027332, None, 2.77824e-05, None, -0.0027332, None, 2.77824e-05, None, -0.00121685, None, 1.47953e-05, None, -0.00121685, None, 1.47953e-05, None, 0.170166, None, 0.00461124, None, 0.170166, None, 0.00461124, None)

reports.append(Report(604017872, ("CSC", 1, 1, 1, 26), "MEp11_26"))
reports[-1].posNum = 104364
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000925634, 0.000542389, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.105702, 0.0403338, 0), \
                           ValErr(0.00286621, 0.00106444, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.77296e-06, 1.40428e-05, 0), \
                           36824.1, 104364, 104364, -nan)
reports[-1].sigmaresid = ValErr(0.17003, 0.000372164, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00104209, None, 3.18294e-06, None, -0.000954098, None, 3.50013e-05, None, -0.000954098, None, 3.50013e-05, None, -0.00068473, None, 4.78905e-06, None, -0.00068473, None, 4.78905e-06, None, 0.170045, None, 0.00502994, None, 0.170045, None, 0.00502994, None)

reports.append(Report(604017888, ("CSC", 1, 1, 1, 28), "MEp11_28"))
reports[-1].posNum = 103981
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000204647, 0.000546782, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0973003, 0.0406259, 0), \
                           ValErr(-0.00128674, 0.00107316, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.6163e-05, 1.41145e-05, 0), \
                           36063.2, 103981, 103981, -nan)
reports[-1].sigmaresid = ValErr(0.171056, 0.0003751, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000334816, None, 6.21542e-06, None, -0.000459341, None, 2.72995e-05, None, -0.000459341, None, 2.72995e-05, None, -0.00141954, None, 2.24788e-05, None, -0.00141954, None, 2.24788e-05, None, 0.171064, None, 0.0043154, None, 0.171064, None, 0.0043154, None)

reports.append(Report(604017904, ("CSC", 1, 1, 1, 30), "MEp11_30"))
reports[-1].posNum = 103574
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00104043, 0.000542147, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.136727, 0.0403513, 0), \
                           ValErr(8.44291e-05, 0.00106816, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.48535e-07, 1.40581e-05, 0), \
                           36939, 103574, 103574, -nan)
reports[-1].sigmaresid = ValErr(0.169385, 0.000372164, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000937152, None, -1.2331e-06, None, -0.00106538, None, 1.95218e-05, None, -0.00106538, None, 1.95218e-05, None, -0.000739922, None, 3.7204e-06, None, -0.000739922, None, 3.7204e-06, None, 0.169395, None, 0.00455981, None, 0.169395, None, 0.00455981, None)

reports.append(Report(604017920, ("CSC", 1, 1, 1, 32), "MEp11_32"))
reports[-1].posNum = 104443
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00217088, 0.000543068, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0731247, 0.0404186, 0), \
                           ValErr(-0.000755381, 0.00106636, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.91957e-05, 1.40382e-05, 0), \
                           36631.4, 104443, 104443, -nan)
reports[-1].sigmaresid = ValErr(0.170389, 0.00037281, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00155956, None, 1.27043e-05, None, -0.00199974, None, 2.99817e-05, None, -0.00199974, None, 2.99817e-05, None, -0.000672345, None, 2.61092e-05, None, -0.000672345, None, 2.61092e-05, None, 0.170393, None, 0.00435934, None, 0.170393, None, 0.00435934, None)

reports.append(Report(604017936, ("CSC", 1, 1, 1, 34), "MEp11_34"))
reports[-1].posNum = 97404
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00175778, 0.000565716, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0825406, 0.0411021, 0), \
                           ValErr(-0.000110601, 0.00108351, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(8.81033e-06, 1.44459e-05, 0), \
                           34919, 97404, 97404, -nan)
reports[-1].sigmaresid = ValErr(0.169071, 0.00038306, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00208498, None, -3.24584e-05, None, -0.00170435, None, -7.11806e-05, None, -0.00170435, None, -7.11806e-05, None, -0.000812705, None, -3.32919e-05, None, -0.000812705, None, -3.32919e-05, None, 0.169075, None, 0.00556716, None, 0.169075, None, 0.00556716, None)

reports.append(Report(604017952, ("CSC", 1, 1, 1, 36), "MEp11_36"))
reports[-1].posNum = 104716
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00298627, 0.000542192, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.13088, 0.0402075, 0), \
                           ValErr(0.000159361, 0.00106336, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.229e-05, 1.40463e-05, 0), \
                           36878.4, 104716, 104716, -nan)
reports[-1].sigmaresid = ValErr(0.170143, 0.000371786, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00264189, None, 1.38688e-05, None, -0.00269131, None, 6.4379e-05, None, -0.00269131, None, 6.4379e-05, None, -0.00244136, None, 3.86862e-05, None, -0.00244136, None, 3.86862e-05, None, 0.170157, None, 0.0052188, None, 0.170157, None, 0.0052188, None)

reports.append(Report(604018184, ("CSC", 1, 1, 2, 1), "MEp12_01"))
reports[-1].posNum = 49185
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00249817, 0.00267257, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.177812, 0.107337, 0), \
                           ValErr(0.00427157, 0.00230962, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.54749e-05, 5.62465e-05, 0), \
                           -41275.2, 49185, 49185, -nan)
reports[-1].sigmaresid = ValErr(0.560036, 0.0017856, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00257353, None, -1.2609e-05, None, -0.00197153, None, 2.88425e-06, None, -0.00197153, None, 2.88425e-06, None, 0.000436356, None, -9.73601e-06, None, 0.000436356, None, -9.73601e-06, None, 0.560076, None, 0.00435999, None, 0.560076, None, 0.00435999, None)

reports.append(Report(604018200, ("CSC", 1, 1, 2, 3), "MEp12_03"))
reports[-1].posNum = 43691
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0045992, 0.00280403, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.111832, 0.113223, 0), \
                           ValErr(-0.00655223, 0.00235722, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.19792e-05, 5.74145e-05, 0), \
                           -34667.2, 43691, 43691, -nan)
reports[-1].sigmaresid = ValErr(0.535006, 0.00180987, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00105335, None, -7.87786e-06, None, 0.00295321, None, 2.44051e-06, None, 0.00295321, None, 2.44051e-06, None, 0.00920264, None, -3.42879e-05, None, 0.00920264, None, -3.42879e-05, None, 0.535068, None, 0.00411553, None, 0.535068, None, 0.00411553, None)

reports.append(Report(604018216, ("CSC", 1, 1, 2, 5), "MEp12_05"))
reports[-1].posNum = 48980
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00218765, 0.00262143, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.140906, 0.107174, 0), \
                           ValErr(-0.00332484, 0.00228991, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.12129e-05, 5.46604e-05, 0), \
                           -40200.2, 48980, 48980, -nan)
reports[-1].sigmaresid = ValErr(0.549809, 0.00175667, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00326165, None, 1.32911e-05, None, 0.00187696, None, 2.54444e-05, None, 0.00187696, None, 2.54444e-05, None, 0.00827782, None, -1.98857e-05, None, 0.00827782, None, -1.98857e-05, None, 0.54983, None, 0.00401312, None, 0.54983, None, 0.00401312, None)

reports.append(Report(604018232, ("CSC", 1, 1, 2, 7), "MEp12_07"))
reports[-1].posNum = 43596
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00623771, 0.00284102, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.294104, 0.112519, 0), \
                           ValErr(-0.00480036, 0.00239656, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(9.70914e-05, 5.86306e-05, 0), \
                           -35243.5, 43596, 43596, -nan)
reports[-1].sigmaresid = ValErr(0.543064, 0.00183913, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00227912, None, -2.05353e-05, None, -0.00411576, None, -2.5142e-05, None, -0.00411576, None, -2.5142e-05, None, -0.0046772, None, 2.45227e-06, None, -0.0046772, None, 2.45227e-06, None, 0.543137, None, 0.0042804, None, 0.543137, None, 0.0042804, None)

reports.append(Report(604018248, ("CSC", 1, 1, 2, 9), "MEp12_09"))
reports[-1].posNum = 44696
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0019945, 0.00276789, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.257553, 0.114411, 0), \
                           ValErr(-0.00443724, 0.00240137, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.42751e-05, 5.67375e-05, 0), \
                           -36286.9, 44696, 44696, -nan)
reports[-1].sigmaresid = ValErr(0.544941, 0.00182264, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00216206, None, 4.85955e-06, None, -0.0025817, None, 7.05987e-06, None, -0.0025817, None, 7.05987e-06, None, -0.00232206, None, 1.90893e-05, None, -0.00232206, None, 1.90893e-05, None, 0.544986, None, 0.00413966, None, 0.544986, None, 0.00413966, None)

reports.append(Report(604018264, ("CSC", 1, 1, 2, 11), "MEp12_11"))
reports[-1].posNum = 45054
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00258542, 0.00274352, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.173382, 0.114585, 0), \
                           ValErr(-0.00172106, 0.00245217, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.17752e-05, 5.67291e-05, 0), \
                           -36239.8, 45054, 45054, -nan)
reports[-1].sigmaresid = ValErr(0.54087, 0.00180182, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00502396, None, -1.46931e-05, None, 0.00123787, None, 6.37888e-06, None, 0.00123787, None, 6.37888e-06, None, 0.000961449, None, 1.13377e-05, None, 0.000961449, None, 1.13377e-05, None, 0.540899, None, 0.00420554, None, 0.540899, None, 0.00420554, None)

reports.append(Report(604018280, ("CSC", 1, 1, 2, 13), "MEp12_13"))
reports[-1].posNum = 43411
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00435734, 0.00285449, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0359875, 0.112364, 0), \
                           ValErr(-0.000992357, 0.0024027, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.96799e-05, 5.88441e-05, 0), \
                           -34801.8, 43411, 43411, -nan)
reports[-1].sigmaresid = ValErr(0.539423, 0.00183069, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00298569, None, 4.65913e-05, None, -0.00398878, None, 3.7209e-05, None, -0.00398878, None, 3.7209e-05, None, -0.00282581, None, 3.05089e-05, None, -0.00282581, None, 3.05089e-05, None, 0.539425, None, 0.00425528, None, 0.539425, None, 0.00425528, None)

reports.append(Report(604018296, ("CSC", 1, 1, 2, 15), "MEp12_15"))
reports[-1].posNum = 48513
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00125384, 0.00262909, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00346316, 0.106751, 0), \
                           ValErr(-0.00205099, 0.00229385, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.12867e-06, 5.49675e-05, 0), \
                           -39857.8, 48513, 48513, -nan)
reports[-1].sigmaresid = ValErr(0.550269, 0.00176657, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00199033, None, -1.02989e-05, None, 0.0011358, None, 6.25949e-07, None, 0.0011358, None, 6.25949e-07, None, 0.000992524, None, -1.19671e-05, None, 0.000992524, None, -1.19671e-05, None, 0.550273, None, 0.0044815, None, 0.550273, None, 0.0044815, None)

reports.append(Report(604018312, ("CSC", 1, 1, 2, 17), "MEp12_17"))
reports[-1].posNum = 43576
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00448904, 0.00280761, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.321936, 0.113041, 0), \
                           ValErr(0.00526077, 0.00239969, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.81915e-05, 5.75691e-05, 0), \
                           -34275.7, 43576, 43576, -nan)
reports[-1].sigmaresid = ValErr(0.531333, 0.00179981, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00399863, None, 2.78236e-05, None, -0.0055381, None, 3.06369e-05, None, -0.0055381, None, 3.06369e-05, None, -0.006844, None, 5.5894e-05, None, -0.006844, None, 5.5894e-05, None, 0.531403, None, 0.00417094, None, 0.531403, None, 0.00417094, None)

reports.append(Report(604018328, ("CSC", 1, 1, 2, 19), "MEp12_19"))
reports[-1].posNum = 49548
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00439133, 0.00264491, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0248111, 0.106271, 0), \
                           ValErr(-0.00355432, 0.00227766, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.77062e-05, 5.54941e-05, 0), \
                           -41272.8, 49548, 49548, -nan)
reports[-1].sigmaresid = ValErr(0.556577, 0.00176806, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00245458, None, 7.78365e-06, None, -0.00348466, None, -7.51602e-06, None, -0.00348466, None, -7.51602e-06, None, -0.00191104, None, -1.10046e-05, None, -0.00191104, None, -1.10046e-05, None, 0.556596, None, 0.00431069, None, 0.556596, None, 0.00431069, None)

reports.append(Report(604018344, ("CSC", 1, 1, 2, 21), "MEp12_21"))
reports[-1].posNum = 43223
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00264502, 0.00280694, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00769744, 0.114402, 0), \
                           ValErr(0.00248925, 0.00237328, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.52859e-07, 5.71791e-05, 0), \
                           -33715.4, 43223, 43223, -nan)
reports[-1].sigmaresid = ValErr(0.52787, 0.00179537, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00203243, None, -3.09604e-06, None, -0.00264278, None, 1.06517e-05, None, -0.00264278, None, 1.06517e-05, None, -0.00269723, None, 1.33392e-05, None, -0.00269723, None, 1.33392e-05, None, 0.527877, None, 0.00401238, None, 0.527877, None, 0.00401238, None)

reports.append(Report(604018360, ("CSC", 1, 1, 2, 23), "MEp12_23"))
reports[-1].posNum = 48559
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00591991, 0.00263524, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.240102, 0.107489, 0), \
                           ValErr(-0.00486184, 0.00230501, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.81529e-05, 5.5036e-05, 0), \
                           -39802.1, 48559, 48559, -nan)
reports[-1].sigmaresid = ValErr(0.549209, 0.00176233, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00945909, None, 4.44314e-06, None, -0.00517664, None, -1.40657e-06, None, -0.00517664, None, -1.40657e-06, None, -0.00535751, None, 5.4283e-06, None, -0.00535751, None, 5.4283e-06, None, 0.549262, None, 0.00420665, None, 0.549262, None, 0.00420665, None)

reports.append(Report(604018376, ("CSC", 1, 1, 2, 25), "MEp12_25"))
reports[-1].posNum = 43884
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00231012, 0.00282819, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.00884071, 0.111833, 0), \
                           ValErr(0.00341033, 0.00238513, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.34645e-05, 5.84346e-05, 0), \
                           -35389, 43884, 43884, -nan)
reports[-1].sigmaresid = ValErr(0.541985, 0.00182944, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00313916, None, 1.26636e-05, None, -0.00338093, None, 1.49355e-05, None, -0.00338093, None, 1.49355e-05, None, -0.00420151, None, 2.42506e-05, None, -0.00420151, None, 2.42506e-05, None, 0.542002, None, 0.00424674, None, 0.542002, None, 0.00424674, None)

reports.append(Report(604018392, ("CSC", 1, 1, 2, 27), "MEp12_27"))
reports[-1].posNum = 44996
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000975072, 0.0027698, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0464134, 0.112288, 0), \
                           ValErr(-0.000205042, 0.00237234, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(7.69709e-07, 5.69629e-05, 0), \
                           -36616.2, 44996, 44996, -nan)
reports[-1].sigmaresid = ValErr(0.54598, 0.00182002, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00219996, None, -3.018e-06, None, 0.000955807, None, 2.76065e-06, None, 0.000955807, None, 2.76065e-06, None, 0.00294028, None, -1.23087e-05, None, 0.00294028, None, -1.23087e-05, None, 0.545981, None, 0.00411834, None, 0.545981, None, 0.00411834, None)

reports.append(Report(604018408, ("CSC", 1, 1, 2, 29), "MEp12_29"))
reports[-1].posNum = 46010
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000420657, 0.00272225, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0699366, 0.11101, 0), \
                           ValErr(-0.0024216, 0.00237723, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.8304e-05, 5.63576e-05, 0), \
                           -37245.7, 46010, 46010, -nan)
reports[-1].sigmaresid = ValErr(0.543665, 0.00179222, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000712527, None, 6.02342e-06, None, -0.00063354, None, 9.10042e-06, None, -0.00063354, None, 9.10042e-06, None, 0.000672418, None, -3.7431e-06, None, 0.000672418, None, -3.7431e-06, None, 0.543672, None, 0.00437503, None, 0.543672, None, 0.00437503, None)

reports.append(Report(604018424, ("CSC", 1, 1, 2, 31), "MEp12_31"))
reports[-1].posNum = 44843
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00582386, 0.00280989, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.044314, 0.109938, 0), \
                           ValErr(-0.000157326, 0.00235208, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000102397, 5.80404e-05, 0), \
                           -36612.8, 44843, 44843, -nan)
reports[-1].sigmaresid = ValErr(0.547458, 0.00182806, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00211413, None, -3.94969e-06, None, -0.00387863, None, 9.60123e-06, None, -0.00387863, None, 9.60123e-06, None, -0.00554077, None, 1.1875e-05, None, -0.00554077, None, 1.1875e-05, None, 0.547477, None, 0.0040231, None, 0.547477, None, 0.0040231, None)

reports.append(Report(604018440, ("CSC", 1, 1, 2, 33), "MEp12_33"))
reports[-1].posNum = 48186
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000203105, 0.00262666, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0824503, 0.106368, 0), \
                           ValErr(-0.00301706, 0.00228042, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(9.33776e-05, 5.46612e-05, 0), \
                           -39228.7, 48186, 48186, -nan)
reports[-1].sigmaresid = ValErr(0.546168, 0.00175934, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00261152, None, -6.20451e-06, None, 0.0012562, None, -4.78596e-06, None, 0.0012562, None, -4.78596e-06, None, -0.000363669, None, 1.03564e-05, None, -0.000363669, None, 1.03564e-05, None, 0.546196, None, 0.00422716, None, 0.546196, None, 0.00422716, None)

reports.append(Report(604018456, ("CSC", 1, 1, 2, 35), "MEp12_35"))
reports[-1].posNum = 43126
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00459373, 0.00281011, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0953816, 0.114368, 0), \
                           ValErr(-0.000239871, 0.00242081, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.99947e-05, 5.73939e-05, 0), \
                           -33425.3, 43126, 43126, -nan)
reports[-1].sigmaresid = ValErr(0.525252, 0.00178847, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00420572, None, -5.94176e-06, None, 0.00329495, None, -4.65116e-06, None, 0.00329495, None, -4.65116e-06, None, -0.00387657, None, 2.06111e-06, None, -0.00387657, None, 2.06111e-06, None, 0.525263, None, 0.00418721, None, 0.525263, None, 0.00418721, None)

reports.append(Report(604018192, ("CSC", 1, 1, 2, 2), "MEp12_02"))
reports[-1].posNum = 43838
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00247386, 0.00269962, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.161129, 0.10564, 0), \
                           ValErr(-0.00331785, 0.00219742, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.22734e-05, 5.48369e-05, 0), \
                           -33660.8, 43838, 43838, -nan)
reports[-1].sigmaresid = ValErr(0.521475, 0.00176114, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00156605, None, -3.18169e-05, None, 0.000834172, None, -1.22081e-05, None, 0.000834172, None, -1.22081e-05, None, -0.00578182, None, -7.32142e-06, None, -0.00578182, None, -7.32142e-06, None, 0.521516, None, 0.00386478, None, 0.521516, None, 0.00386478, None)

reports.append(Report(604018208, ("CSC", 1, 1, 2, 4), "MEp12_04"))
reports[-1].posNum = 42559
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000492765, 0.00278123, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0541968, 0.110482, 0), \
                           ValErr(7.46923e-05, 0.00224178, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.21735e-05, 5.57769e-05, 0), \
                           -33031.8, 42559, 42559, -nan)
reports[-1].sigmaresid = ValErr(0.52582, 0.0018023, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00138362, None, -8.39389e-06, None, 0.00169193, None, -3.027e-05, None, 0.00169193, None, -3.027e-05, None, -0.000269949, None, -1.2256e-05, None, -0.000269949, None, -1.2256e-05, None, 0.525829, None, 0.00393857, None, 0.525829, None, 0.00393857, None)

reports.append(Report(604018224, ("CSC", 1, 1, 2, 6), "MEp12_06"))
reports[-1].posNum = 46469
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00345788, 0.00258688, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0544358, 0.0999455, 0), \
                           ValErr(-0.00209193, 0.00210934, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.63814e-05, 5.31277e-05, 0), \
                           -35793.9, 46469, 46469, -nan)
reports[-1].sigmaresid = ValErr(0.522744, 0.00171472, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000290158, None, -9.69354e-06, None, 0.00231449, None, -1.92841e-05, None, 0.00231449, None, -1.92841e-05, None, -0.00130569, None, -2.43592e-06, None, -0.00130569, None, -2.43592e-06, None, 0.522761, None, 0.00415995, None, 0.522761, None, 0.00415995, None)

reports.append(Report(604018240, ("CSC", 1, 1, 2, 8), "MEp12_08"))
reports[-1].posNum = 40892
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00103723, 0.00278549, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.150072, 0.1061, 0), \
                           ValErr(-0.00303541, 0.00218791, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.71808e-05, 5.56792e-05, 0), \
                           -30100.8, 40892, 40892, -nan)
reports[-1].sigmaresid = ValErr(0.505183, 0.0017665, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000514402, None, 7.37286e-07, None, -0.000613648, None, -2.21395e-05, None, -0.000613648, None, -2.21395e-05, None, -0.0048684, None, 2.75663e-05, None, -0.0048684, None, 2.75663e-05, None, 0.505216, None, 0.00733565, None, 0.505216, None, 0.00733565, None)

reports.append(Report(604018256, ("CSC", 1, 1, 2, 10), "MEp12_10"))
reports[-1].posNum = 48209
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000311229, 0.00256957, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(8.76759e-05, 0.100594, 0), \
                           ValErr(-0.00287827, 0.00214014, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.78415e-05, 5.32308e-05, 0), \
                           -38046.7, 48209, 48209, -nan)
reports[-1].sigmaresid = ValErr(0.532733, 0.00171566, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000413452, None, -6.52036e-06, None, 0.000111474, None, -7.291e-06, None, 0.000111474, None, -7.291e-06, None, 0.0049976, None, -2.10227e-05, None, 0.0049976, None, -2.10227e-05, None, 0.532745, None, 0.00398913, None, 0.532745, None, 0.00398913, None)

reports.append(Report(604018272, ("CSC", 1, 1, 2, 12), "MEp12_12"))
reports[-1].posNum = 40949
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00448981, 0.00274818, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.38814, 0.104694, 0), \
                           ValErr(0.00235291, 0.00216748, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.63929e-05, 5.50888e-05, 0), \
                           -30275.3, 40949, 40949, -nan)
reports[-1].sigmaresid = ValErr(0.50682, 0.00177099, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00298105, None, -1.49097e-05, None, 0.00323824, None, -1.94362e-05, None, 0.00323824, None, -1.94362e-05, None, 0.00152787, None, 1.05013e-06, None, 0.00152787, None, 1.05013e-06, None, 0.50691, None, 0.00435912, None, 0.50691, None, 0.00435912, None)

reports.append(Report(604018288, ("CSC", 1, 1, 2, 14), "MEp12_14"))
reports[-1].posNum = 47192
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00876279, 0.00258217, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.190155, 0.0989522, 0), \
                           ValErr(0.00211103, 0.00210912, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(8.4025e-05, 5.31848e-05, 0), \
                           -36556.5, 47192, 47192, -nan)
reports[-1].sigmaresid = ValErr(0.525027, 0.00170896, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.010235, None, 2.77299e-05, None, -0.00737711, None, 2.23798e-05, None, -0.00737711, None, 2.23798e-05, None, -0.00649719, None, 1.04456e-05, None, -0.00649719, None, 1.04456e-05, None, 0.525065, None, 0.00416374, None, 0.525065, None, 0.00416374, None)

reports.append(Report(604018304, ("CSC", 1, 1, 2, 16), "MEp12_16"))
reports[-1].posNum = 42119
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0023508, 0.00274989, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0643396, 0.109725, 0), \
                           ValErr(-0.00289763, 0.00224133, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.02512e-05, 5.49603e-05, 0), \
                           -31844.4, 42119, 42119, -nan)
reports[-1].sigmaresid = ValErr(0.515364, 0.00177566, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00298153, None, -3.0447e-07, None, -0.00172541, None, -2.26108e-05, None, -0.00172541, None, -2.26108e-05, None, -5.9483e-05, None, -7.45452e-07, None, -5.9483e-05, None, -7.45452e-07, None, 0.515382, None, 0.00441182, None, 0.515382, None, 0.00441182, None)

reports.append(Report(604018320, ("CSC", 1, 1, 2, 18), "MEp12_18"))
reports[-1].posNum = 43785
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00261877, 0.0027076, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0750506, 0.104275, 0), \
                           ValErr(-0.00120455, 0.0021519, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.23334e-06, 5.47076e-05, 0), \
                           -34146.7, 43785, 43785, -nan)
reports[-1].sigmaresid = ValErr(0.527785, 0.00178353, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00284787, None, -3.84071e-06, None, 0.00261688, None, 3.16644e-05, None, 0.00261688, None, 3.16644e-05, None, 0.00153778, None, 1.76095e-05, None, 0.00153778, None, 1.76095e-05, None, 0.527791, None, 0.00468773, None, 0.527791, None, 0.00468773, None)

reports.append(Report(604018336, ("CSC", 1, 1, 2, 20), "MEp12_20"))
reports[-1].posNum = 44225
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00182511, 0.00270922, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0990253, 0.104903, 0), \
                           ValErr(-0.00415963, 0.00220308, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.02847e-05, 5.52905e-05, 0), \
                           -34311.3, 44225, 44225, -nan)
reports[-1].sigmaresid = ValErr(0.525657, 0.00176747, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00134137, None, 1.54636e-05, None, 0.000917617, None, 8.6062e-07, None, 0.000917617, None, 8.6062e-07, None, 0.00265161, None, 1.9458e-05, None, 0.00265161, None, 1.9458e-05, None, 0.525686, None, 0.00430938, None, 0.525686, None, 0.00430938, None)

reports.append(Report(604018352, ("CSC", 1, 1, 2, 22), "MEp12_22"))
reports[-1].posNum = 42894
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00208276, 0.00275051, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.164824, 0.107715, 0), \
                           ValErr(-0.00109322, 0.00222827, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(9.94247e-06, 5.55942e-05, 0), \
                           -32956.9, 42894, 42894, -nan)
reports[-1].sigmaresid = ValErr(0.521729, 0.00178128, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00207236, None, -2.42738e-05, None, 0.00221032, None, -3.15782e-06, None, 0.00221032, None, -3.15782e-06, None, 0.000201795, None, -8.0148e-06, None, 0.000201795, None, -8.0148e-06, None, 0.521744, None, 0.00408615, None, 0.521744, None, 0.00408615, None)

reports.append(Report(604018368, ("CSC", 1, 1, 2, 24), "MEp12_24"))
reports[-1].posNum = 47026
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00211883, 0.00257129, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.105693, 0.0989209, 0), \
                           ValErr(0.000842279, 0.00210605, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.1231e-05, 5.31555e-05, 0), \
                           -36335.8, 47026, 47026, -nan)
reports[-1].sigmaresid = ValErr(0.524002, 0.00170864, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00277933, None, 2.77791e-06, None, 0.00187938, None, -9.067e-06, None, 0.00187938, None, -9.067e-06, None, 0.0068142, None, -1.43218e-05, None, 0.0068142, None, -1.43218e-05, None, 0.524006, None, 0.00385881, None, 0.524006, None, 0.00385881, None)

reports.append(Report(604018384, ("CSC", 1, 1, 2, 26), "MEp12_26"))
reports[-1].posNum = 41528
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00043351, 0.00273455, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0532717, 0.104068, 0), \
                           ValErr(0.000700467, 0.0021443, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000133516, 5.46722e-05, 0), \
                           -30412.1, 41528, 41528, -nan)
reports[-1].sigmaresid = ValErr(0.503279, 0.00174632, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00323865, None, -2.37729e-05, None, 0.00242675, None, -2.73629e-05, None, 0.00242675, None, -2.73629e-05, None, 0.00319767, None, -3.24431e-05, None, 0.00319767, None, -3.24431e-05, None, 0.503317, None, 0.00408878, None, 0.503317, None, 0.00408878, None)

reports.append(Report(604018400, ("CSC", 1, 1, 2, 28), "MEp12_28"))
reports[-1].posNum = 48124
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000190494, 0.00257555, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.115035, 0.100724, 0), \
                           ValErr(0.00158554, 0.00215043, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.70617e-07, 5.34856e-05, 0), \
                           -37872.4, 48124, 48124, -nan)
reports[-1].sigmaresid = ValErr(0.531548, 0.00171335, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000545802, None, -1.33112e-05, None, 0.000215625, None, 7.68284e-06, None, 0.000215625, None, 7.68284e-06, None, -0.00134688, None, 4.0239e-05, None, -0.00134688, None, 4.0239e-05, None, 0.531559, None, 0.00387652, None, 0.531559, None, 0.00387652, None)

reports.append(Report(604018416, ("CSC", 1, 1, 2, 30), "MEp12_30"))
reports[-1].posNum = 40785
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00378001, 0.00274339, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0865285, 0.10398, 0), \
                           ValErr(-0.0021471, 0.00210775, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.44212e-05, 5.43244e-05, 0), \
                           -29608.9, 40785, 40785, -nan)
reports[-1].sigmaresid = ValErr(0.500093, 0.001751, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00299397, None, 6.24135e-07, None, -0.00347368, None, 9.88464e-06, None, -0.00347368, None, 9.88464e-06, None, -0.00447695, None, 8.61959e-06, None, -0.00447695, None, 8.61959e-06, None, 0.500106, None, 0.00398791, None, 0.500106, None, 0.00398791, None)

reports.append(Report(604018432, ("CSC", 1, 1, 2, 32), "MEp12_32"))
reports[-1].posNum = 47132
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000261359, 0.00257852, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.152581, 0.0992053, 0), \
                           ValErr(-0.00356828, 0.00211481, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.36212e-05, 5.3125e-05, 0), \
                           -36317.2, 47132, 47132, -nan)
reports[-1].sigmaresid = ValErr(0.522883, 0.00170307, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000390331, None, -1.45047e-06, None, 0.000402618, None, -7.66836e-06, None, 0.000402618, None, -7.66836e-06, None, -0.00067171, None, -1.33378e-05, None, -0.00067171, None, -1.33378e-05, None, 0.52292, None, 0.00424111, None, 0.52292, None, 0.00424111, None)

reports.append(Report(604018448, ("CSC", 1, 1, 2, 34), "MEp12_34"))
reports[-1].posNum = 43342
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00706028, 0.00272299, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0359181, 0.107545, 0), \
                           ValErr(-0.000894963, 0.00223624, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.67689e-05, 5.50888e-05, 0), \
                           -33165.7, 43342, 43342, -nan)
reports[-1].sigmaresid = ValErr(0.520103, 0.00176653, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00609372, None, -5.36037e-06, None, 0.00573719, None, -1.95323e-05, None, 0.00573719, None, -1.95323e-05, None, 0.00481363, None, -1.63208e-05, None, 0.00481363, None, -1.63208e-05, None, 0.520114, None, 0.00404131, None, 0.520114, None, 0.00404131, None)

reports.append(Report(604018464, ("CSC", 1, 1, 2, 36), "MEp12_36"))
reports[-1].posNum = 45236
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00166111, 0.00264872, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.210951, 0.101733, 0), \
                           ValErr(-0.00313335, 0.00212364, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.49476e-05, 5.38516e-05, 0), \
                           -35108.8, 45236, 45236, -nan)
reports[-1].sigmaresid = ValErr(0.52581, 0.00174812, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00143177, None, 1.35736e-05, None, -0.00201483, None, 4.20199e-06, None, -0.00201483, None, 4.20199e-06, None, 0.00428544, None, -1.95116e-05, None, 0.00428544, None, -1.95116e-05, None, 0.525845, None, 0.00412691, None, 0.525845, None, 0.00412691, None)

reports.append(Report(604018696, ("CSC", 1, 1, 3, 1), "MEp13_01"))
reports[-1].posNum = 20026
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.013374, 0.0107324, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.79168, 0.30758, 0), \
                           ValErr(-0.00205622, 0.0069192, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000327807, 0.00024009, 0), \
                           -36672.7, 20026, 20026, -nan)
reports[-1].sigmaresid = ValErr(1.5103, 0.00754655, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0247374, None, 1.96519e-05, None, -0.0116534, None, -2.10943e-05, None, -0.0116534, None, -2.10943e-05, None, -0.0159435, None, 3.18427e-06, None, -0.0159435, None, 3.18427e-06, None, 1.51348, None, 0.00628995, None, 1.51348, None, 0.00628995, None)

reports.append(Report(604018704, ("CSC", 1, 1, 3, 2), "MEp13_02"))
reports[-1].posNum = 19737
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0106975, 0.0107932, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.46306, 0.315515, 0), \
                           ValErr(-0.0147808, 0.00712987, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00026648, 0.000244808, 0), \
                           -36154.9, 19737, 19737, -nan)
reports[-1].sigmaresid = ValErr(1.51119, 0.00760612, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0143659, None, -3.67164e-05, None, 0.00921349, None, -0.000105399, None, 0.00921349, None, -0.000105399, None, 0.00590884, None, -3.19361e-05, None, 0.00590884, None, -3.19361e-05, None, 1.51368, None, 0.00671004, None, 1.51368, None, 0.00671004, None)

reports.append(Report(604018712, ("CSC", 1, 1, 3, 3), "MEp13_03"))
reports[-1].posNum = 18287
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00389262, 0.0112095, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.6976, 0.330017, 0), \
                           ValErr(-0.0136337, 0.00773783, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.04264e-05, 0.00026129, 0), \
                           -33548.6, 18287, 18287, -nan)
reports[-1].sigmaresid = ValErr(1.51531, 0.00792347, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0201488, None, -9.39547e-05, None, 0.00496789, None, -0.000140766, None, 0.00496789, None, -0.000140766, None, -0.0218094, None, -1.81448e-05, None, -0.0218094, None, -1.81448e-05, None, 1.51811, None, 0.00662559, None, 1.51811, None, 0.00662559, None)

reports.append(Report(604018720, ("CSC", 1, 1, 3, 4), "MEp13_04"))
reports[-1].posNum = 18420
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0289614, 0.011366, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.98924, 0.343801, 0), \
                           ValErr(-0.0121755, 0.00811213, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000286204, 0.000265039, 0), \
                           -34109.4, 18420, 18420, -nan)
reports[-1].sigmaresid = ValErr(1.54159, 0.00803161, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.04329, None, -9.93934e-05, None, 0.0308053, None, -0.000105319, None, 0.0308053, None, -0.000105319, None, 0.0291663, None, -6.98019e-05, None, 0.0291663, None, -6.98019e-05, None, 1.54485, None, 0.00751133, None, 1.54485, None, 0.00751133, None)

reports.append(Report(604018728, ("CSC", 1, 1, 3, 5), "MEp13_05"))
reports[-1].posNum = 20525
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0111462, 0.0105294, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.00615, 0.307722, 0), \
                           ValErr(-0.0108681, 0.00695835, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000351044, 0.000236045, 0), \
                           -37383.2, 20525, 20525, -nan)
reports[-1].sigmaresid = ValErr(1.49543, 0.00738092, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0116406, None, -3.71456e-05, None, 0.0125031, None, -9.21921e-05, None, 0.0125031, None, -9.21921e-05, None, 0.00873878, None, -2.93059e-05, None, 0.00873878, None, -2.93059e-05, None, 1.49906, None, 0.00671185, None, 1.49906, None, 0.00671185, None)

reports.append(Report(604018736, ("CSC", 1, 1, 3, 6), "MEp13_06"))
reports[-1].posNum = 20294
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0187172, 0.0105887, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.81003, 0.30434, 0), \
                           ValErr(-0.00645504, 0.00688685, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.89227e-05, 0.000237743, 0), \
                           -36983.9, 20294, 20294, -nan)
reports[-1].sigmaresid = ValErr(1.49701, 0.00743069, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00576245, None, -6.84216e-05, None, 0.0192677, None, -7.85928e-05, None, 0.0192677, None, -7.85928e-05, None, 0.00382698, None, -8.13969e-05, None, 0.00382698, None, -8.13969e-05, None, 1.50017, None, 0.00658664, None, 1.50017, None, 0.00658664, None)

reports.append(Report(604018744, ("CSC", 1, 1, 3, 7), "MEp13_07"))
reports[-1].posNum = 19067
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0143707, 0.0109613, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.80724, 0.318431, 0), \
                           ValErr(0.000602218, 0.00736546, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.81906e-05, 0.000253179, 0), \
                           -34924.7, 19067, 19067, -nan)
reports[-1].sigmaresid = ValErr(1.51095, 0.00773739, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0156481, None, 3.29646e-05, None, -0.0152691, None, -5.68253e-05, None, -0.0152691, None, -5.68253e-05, None, -0.0059915, None, -4.66016e-05, None, -0.0059915, None, -4.66016e-05, None, 1.51406, None, 0.00663488, None, 1.51406, None, 0.00663488, None)

reports.append(Report(604018752, ("CSC", 1, 1, 3, 8), "MEp13_08"))
reports[-1].posNum = 18372
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00295804, 0.0111871, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.3229, 0.329565, 0), \
                           ValErr(0.0145944, 0.00767068, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000257845, 0.000260565, 0), \
                           -33712.9, 18372, 18372, -nan)
reports[-1].sigmaresid = ValErr(1.51599, 0.00790859, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0183645, None, -1.71628e-05, None, -0.00246263, None, -6.35682e-05, None, -0.00246263, None, -6.35682e-05, None, -0.0126571, None, 3.96672e-05, None, -0.0126571, None, 3.96672e-05, None, 1.5184, None, 0.00674149, None, 1.5184, None, 0.00674149, None)

reports.append(Report(604018760, ("CSC", 1, 1, 3, 9), "MEp13_09"))
reports[-1].posNum = 18874
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00772694, 0.0110717, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.83614, 0.323335, 0), \
                           ValErr(-0.0137317, 0.00731994, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000681825, 0.000249558, 0), \
                           -34608.4, 18874, 18874, -nan)
reports[-1].sigmaresid = ValErr(1.51395, 0.00779228, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0259183, None, -3.64828e-05, None, 0.0111424, None, -0.000123056, None, 0.0111424, None, -0.000123056, None, 0.0211649, None, -0.00014649, None, 0.0211649, None, -0.00014649, None, 1.5174, None, 0.00656819, None, 1.5174, None, 0.00656819, None)

reports.append(Report(604018768, ("CSC", 1, 1, 3, 10), "MEp13_10"))
reports[-1].posNum = 20647
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0105282, 0.0105575, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.82364, 0.311025, 0), \
                           ValErr(-0.000903449, 0.00703597, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000228092, 0.000235218, 0), \
                           -37739.5, 20647, 20647, -nan)
reports[-1].sigmaresid = ValErr(1.50518, 0.0074071, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0150127, None, -3.79372e-05, None, 0.0122722, None, -0.000162864, None, 0.0122722, None, -0.000162864, None, 0.0246942, None, -0.000164527, None, 0.0246942, None, -0.000164527, None, 1.50821, None, 0.0065583, None, 1.50821, None, 0.0065583, None)

reports.append(Report(604018776, ("CSC", 1, 1, 3, 11), "MEp13_11"))
reports[-1].posNum = 19221
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0124922, 0.0111748, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.59041, 0.326144, 0), \
                           ValErr(-0.014629, 0.00746581, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(7.00485e-05, 0.000255424, 0), \
                           -35637.5, 19221, 19221, -nan)
reports[-1].sigmaresid = ValErr(1.5452, 0.00788102, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0119248, None, -2.10883e-06, None, -0.0142722, None, -1.6832e-05, None, -0.0142722, None, -1.6832e-05, None, -0.00196389, None, 8.26358e-05, None, -0.00196389, None, 8.26358e-05, None, 1.54781, None, 0.00682836, None, 1.54781, None, 0.00682836, None)

reports.append(Report(604018784, ("CSC", 1, 1, 3, 12), "MEp13_12"))
reports[-1].posNum = 18582
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00856777, 0.0112475, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.74022, 0.324728, 0), \
                           ValErr(0.0037631, 0.0075262, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000196038, 0.000261228, 0), \
                           -34307.3, 18582, 18582, -nan)
reports[-1].sigmaresid = ValErr(1.53315, 0.0079528, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000600159, None, -2.9031e-05, None, 0.00826148, None, -8.72959e-05, None, 0.00826148, None, -8.72959e-05, None, -0.01138, None, -4.36775e-05, None, -0.01138, None, -4.36775e-05, None, 1.53621, None, 0.00693695, None, 1.53621, None, 0.00693695, None)

reports.append(Report(604018792, ("CSC", 1, 1, 3, 13), "MEp13_13"))
reports[-1].posNum = 18197
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0103203, 0.0111707, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.53738, 0.323494, 0), \
                           ValErr(-0.000157301, 0.00749159, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000393138, 0.000259892, 0), \
                           -33273.4, 18197, 18197, -nan)
reports[-1].sigmaresid = ValErr(1.50616, 0.00789495, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0240001, None, 7.50145e-07, None, -0.00813331, None, 1.86413e-06, None, -0.00813331, None, 1.86413e-06, None, -0.00290916, None, 2.91816e-05, None, -0.00290916, None, 2.91816e-05, None, 1.50885, None, 0.00721345, None, 1.50885, None, 0.00721345, None)

reports.append(Report(604018800, ("CSC", 1, 1, 3, 14), "MEp13_14"))
reports[-1].posNum = 20209
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00885114, 0.0106862, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.31554, 0.311797, 0), \
                           ValErr(0.00294486, 0.00697247, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000172867, 0.00023869, 0), \
                           -36968.3, 20209, 20209, -nan)
reports[-1].sigmaresid = ValErr(1.50736, 0.00749767, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0127078, None, -2.14503e-05, None, 0.0082295, None, -1.08194e-05, None, 0.0082295, None, -1.08194e-05, None, -0.00570077, None, 2.02897e-05, None, -0.00570077, None, 2.02897e-05, None, 1.50946, None, 0.006926, None, 1.50946, None, 0.006926, None)

reports.append(Report(604018808, ("CSC", 1, 1, 3, 15), "MEp13_15"))
reports[-1].posNum = 20013
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0098795, 0.0107739, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.42073, 0.311834, 0), \
                           ValErr(-0.00201567, 0.00703508, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.96102e-05, 0.000239527, 0), \
                           -36619.4, 20013, 20013, -nan)
reports[-1].sigmaresid = ValErr(1.50809, 0.00753802, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00048443, None, -5.3792e-05, None, 0.00825579, None, -7.05315e-05, None, 0.00825579, None, -7.05315e-05, None, 0.00735712, None, -2.95154e-05, None, 0.00735712, None, -2.95154e-05, None, 1.51037, None, 0.00638634, None, 1.51037, None, 0.00638634, None)

reports.append(Report(604018816, ("CSC", 1, 1, 3, 16), "MEp13_16"))
reports[-1].posNum = 18382
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00690487, 0.0112091, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.75605, 0.335607, 0), \
                           ValErr(-0.00363441, 0.00782198, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.98409e-05, 0.000258583, 0), \
                           -33771.3, 18382, 18382, -nan)
reports[-1].sigmaresid = ValErr(1.5193, 0.00792375, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00693272, None, 1.61426e-05, None, 0.00726087, None, -6.19615e-05, None, 0.00726087, None, -6.19615e-05, None, -0.00362625, None, -2.08043e-05, None, -0.00362625, None, -2.08043e-05, None, 1.52214, None, 0.00644776, None, 1.52214, None, 0.00644776, None)

reports.append(Report(604018824, ("CSC", 1, 1, 3, 17), "MEp13_17"))
reports[-1].posNum = 18045
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00602044, 0.0112497, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.10006, 0.331776, 0), \
                           ValErr(-0.00279614, 0.00778082, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000461616, 0.00026334, 0), \
                           -33050.2, 18045, 18045, -nan)
reports[-1].sigmaresid = ValErr(1.51075, 0.00795235, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0226147, None, 2.40625e-05, None, -0.00769206, None, -0.000125135, None, -0.00769206, None, -0.000125135, None, 0.0248679, None, -0.000135461, None, 0.0248679, None, -0.000135461, None, 1.51455, None, 0.00764961, None, 1.51455, None, 0.00764961, None)

reports.append(Report(604018832, ("CSC", 1, 1, 3, 18), "MEp13_18"))
reports[-1].posNum = 19107
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00147542, 0.0107985, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.27431, 0.308499, 0), \
                           ValErr(-0.0111107, 0.00698791, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(8.01187e-05, 0.000244804, 0), \
                           -34682.4, 19107, 19107, -nan)
reports[-1].sigmaresid = ValErr(1.48621, 0.00760274, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00402885, None, -1.66766e-05, None, 0.0023843, None, -2.63683e-05, None, 0.0023843, None, -2.63683e-05, None, -0.00189197, None, 1.81461e-05, None, -0.00189197, None, 1.81461e-05, None, 1.48841, None, 0.00665085, None, 1.48841, None, 0.00665085, None)

reports.append(Report(604018840, ("CSC", 1, 1, 3, 19), "MEp13_19"))
reports[-1].posNum = 20532
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00106457, 0.0106559, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.82026, 0.307741, 0), \
                           ValErr(0.000116068, 0.00700135, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000154875, 0.000239385, 0), \
                           -37653.4, 20532, 20532, -nan)
reports[-1].sigmaresid = ValErr(1.5143, 0.0074728, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000676995, None, -8.60351e-06, None, 0.00223226, None, -0.000114235, None, 0.00223226, None, -0.000114235, None, -0.00127156, None, -7.96113e-05, None, -0.00127156, None, -7.96113e-05, None, 1.5174, None, 0.00677921, None, 1.5174, None, 0.00677921, None)

reports.append(Report(604018848, ("CSC", 1, 1, 3, 20), "MEp13_20"))
reports[-1].posNum = 19723
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00181283, 0.0107519, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.48912, 0.312669, 0), \
                           ValErr(-0.000820335, 0.00713473, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000331047, 0.000244938, 0), \
                           -36021.5, 19723, 19723, -nan)
reports[-1].sigmaresid = ValErr(1.50295, 0.00756736, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00393906, None, -3.6692e-05, None, -0.00417149, None, -8.06616e-07, None, -0.00417149, None, -8.06616e-07, None, 0.00338524, None, -4.5275e-06, None, 0.00338524, None, -4.5275e-06, None, 1.50543, None, 0.00637472, None, 1.50543, None, 0.00637472, None)

reports.append(Report(604018856, ("CSC", 1, 1, 3, 21), "MEp13_21"))
reports[-1].posNum = 18062
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00648397, 0.0112556, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.28466, 0.333015, 0), \
                           ValErr(0.000747483, 0.00782649, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000336342, 0.000261931, 0), \
                           -33100.8, 18062, 18062, -nan)
reports[-1].sigmaresid = ValErr(1.51237, 0.00795719, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0073181, None, -1.64549e-05, None, 0.0061426, None, -5.92229e-05, None, 0.0061426, None, -5.92229e-05, None, 0.0193291, None, -8.15837e-05, None, 0.0193291, None, -8.15837e-05, None, 1.51446, None, 0.00648459, None, 1.51446, None, 0.00648459, None)

reports.append(Report(604018864, ("CSC", 1, 1, 3, 22), "MEp13_22"))
reports[-1].posNum = 18903
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0194621, 0.0112291, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.68392, 0.338024, 0), \
                           ValErr(-0.00372582, 0.00790357, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.47489e-05, 0.00025985, 0), \
                           -35009.5, 18903, 18903, -nan)
reports[-1].sigmaresid = ValErr(1.54206, 0.0079308, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0190326, None, 1.28664e-05, None, -0.0176567, None, -5.21754e-05, None, -0.0176567, None, -5.21754e-05, None, -0.0172962, None, 1.53254e-05, None, -0.0172962, None, 1.53254e-05, None, 1.54467, None, 0.00665991, None, 1.54467, None, 0.00665991, None)

reports.append(Report(604018872, ("CSC", 1, 1, 3, 23), "MEp13_23"))
reports[-1].posNum = 20573
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00509263, 0.0105392, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.5283, 0.307556, 0), \
                           ValErr(-0.00754065, 0.00697805, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000230467, 0.000235909, 0), \
                           -37514.7, 20573, 20573, -nan)
reports[-1].sigmaresid = ValErr(1.49864, 0.00738813, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00310779, None, -2.74359e-05, None, -0.00462189, None, -5.57452e-05, None, -0.00462189, None, -5.57452e-05, None, -0.0142476, None, 7.79209e-06, None, -0.0142476, None, 7.79209e-06, None, 1.50116, None, 0.00666631, None, 1.50116, None, 0.00666631, None)

reports.append(Report(604018880, ("CSC", 1, 1, 3, 24), "MEp13_24"))
reports[-1].posNum = 20092
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000473679, 0.0105345, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.7748, 0.304368, 0), \
                           ValErr(-0.00120384, 0.0068737, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.58635e-05, 0.000235961, 0), \
                           -36399.3, 20092, 20092, -nan)
reports[-1].sigmaresid = ValErr(1.48097, 0.00738788, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00251268, None, -5.54526e-05, None, -0.000703371, None, -3.41739e-05, None, -0.000703371, None, -3.41739e-05, None, 0.00362273, None, -5.59477e-05, None, 0.00362273, None, -5.59477e-05, None, 1.48403, None, 0.00665947, None, 1.48403, None, 0.00665947, None)

reports.append(Report(604018888, ("CSC", 1, 1, 3, 25), "MEp13_25"))
reports[-1].posNum = 18519
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0206539, 0.0110764, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.28325, 0.31933, 0), \
                           ValErr(-2.88649e-05, 0.00740854, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.66925e-05, 0.000255683, 0), \
                           -33863.4, 18519, 18519, -nan)
reports[-1].sigmaresid = ValErr(1.50627, 0.00782668, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0190474, None, 4.51713e-06, None, -0.0214651, None, -3.91278e-05, None, -0.0214651, None, -3.91278e-05, None, -0.0224554, None, 1.1881e-05, None, -0.0224554, None, 1.1881e-05, None, 1.50837, None, 0.00687904, None, 1.50837, None, 0.00687904, None)

reports.append(Report(604018896, ("CSC", 1, 1, 3, 26), "MEp13_26"))
reports[-1].posNum = 18501
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0104859, 0.0112176, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.24115, 0.327808, 0), \
                           ValErr(-0.0157057, 0.00764494, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000221706, 0.000261409, 0), \
                           -34065.6, 18501, 18501, -nan)
reports[-1].sigmaresid = ValErr(1.52553, 0.0079306, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0182151, None, -2.22942e-05, None, 0.0101478, None, -0.000124033, None, 0.0101478, None, -0.000124033, None, 0.0189715, None, -0.000186371, None, 0.0189715, None, -0.000186371, None, 1.52756, None, 0.00696781, None, 1.52756, None, 0.00696781, None)

reports.append(Report(604018904, ("CSC", 1, 1, 3, 27), "MEp13_27"))
reports[-1].posNum = 19057
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00509768, 0.010918, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.41135, 0.316672, 0), \
                           ValErr(-0.00198053, 0.00721351, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.45341e-06, 0.000248323, 0), \
                           -34792.1, 19057, 19057, -nan)
reports[-1].sigmaresid = ValErr(1.50192, 0.00769315, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00693386, None, -4.35512e-06, None, -0.00584862, None, -0.000120773, None, -0.00584862, None, -0.000120773, None, -0.00399478, None, -3.37681e-05, None, -0.00399478, None, -3.37681e-05, None, 1.50421, None, 0.00660769, None, 1.50421, None, 0.00660769, None)

reports.append(Report(604018912, ("CSC", 1, 1, 3, 28), "MEp13_28"))
reports[-1].posNum = 19594
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0153814, 0.0108472, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.3726, 0.318733, 0), \
                           ValErr(-0.0036489, 0.00719754, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.33993e-05, 0.000243149, 0), \
                           -35875.3, 19594, 19594, -nan)
reports[-1].sigmaresid = ValErr(1.50982, 0.00762693, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0235512, None, 3.798e-05, None, -0.0150742, None, -5.30401e-05, None, -0.0150742, None, -5.30401e-05, None, -0.000588968, None, -7.56694e-05, None, -0.000588968, None, -7.56694e-05, None, 1.51414, None, 0.00642654, None, 1.51414, None, 0.00642654, None)

reports.append(Report(604018920, ("CSC", 1, 1, 3, 29), "MEp13_29"))
reports[-1].posNum = 18762
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0387415, 0.0109486, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.23058, 0.316859, 0), \
                           ValErr(-0.0238943, 0.00722782, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000163592, 0.00024889, 0), \
                           -34148.4, 18762, 18762, -nan)
reports[-1].sigmaresid = ValErr(1.49353, 0.00771008, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0427342, None, -8.52323e-05, None, 0.0350453, None, -0.000159099, None, 0.0350453, None, -0.000159099, None, 0.0575277, None, -0.000220599, None, 0.0575277, None, -0.000220599, None, 1.4959, None, 0.00681406, None, 1.4959, None, 0.00681406, None)

reports.append(Report(604018928, ("CSC", 1, 1, 3, 30), "MEp13_30"))
reports[-1].posNum = 18438
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0107069, 0.0110975, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.26655, 0.317359, 0), \
                           ValErr(-0.0148203, 0.00736026, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.61226e-05, 0.000258003, 0), \
                           -33721.1, 18438, 18438, -nan)
reports[-1].sigmaresid = ValErr(1.50675, 0.00784635, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0104037, None, 2.34697e-05, None, 0.0111241, None, -5.98699e-05, None, 0.0111241, None, -5.98699e-05, None, -0.00274347, None, -1.02673e-05, None, -0.00274347, None, -1.02673e-05, None, 1.5089, None, 0.00740388, None, 1.5089, None, 0.00740388, None)

reports.append(Report(604018936, ("CSC", 1, 1, 3, 31), "MEp13_31"))
reports[-1].posNum = 18520
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0103061, 0.0112041, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.35001, 0.322375, 0), \
                           ValErr(0.0052723, 0.00749664, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000139827, 0.000260181, 0), \
                           -34063.1, 18520, 18520, -nan)
reports[-1].sigmaresid = ValErr(1.52246, 0.00791064, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0100934, None, -8.37384e-05, None, 0.0133173, None, -7.91168e-05, None, 0.0133173, None, -7.91168e-05, None, 0.0116771, None, -7.80972e-05, None, 0.0116771, None, -7.80972e-05, None, 1.52704, None, 0.00846652, None, 1.52704, None, 0.00846652, None)

reports.append(Report(604018944, ("CSC", 1, 1, 3, 32), "MEp13_32"))
reports[-1].posNum = 20234
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0241451, 0.0105468, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.33983, 0.306763, 0), \
                           ValErr(-0.0101895, 0.00695102, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.44281e-05, 0.000237291, 0), \
                           -36758.7, 20234, 20234, -nan)
reports[-1].sigmaresid = ValErr(1.48847, 0.00739921, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0333373, None, -0.000102377, None, 0.0228295, None, -0.000166962, None, 0.0228295, None, -0.000166962, None, 0.0314987, None, -0.000135945, None, 0.0314987, None, -0.000135945, None, 1.49066, None, 0.00646823, None, 1.49066, None, 0.00646823, None)

reports.append(Report(604018952, ("CSC", 1, 1, 3, 33), "MEp13_33"))
reports[-1].posNum = 20119
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000545927, 0.0106668, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.49179, 0.308119, 0), \
                           ValErr(-0.00284795, 0.00696144, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000250459, 0.000238985, 0), \
                           -36697.5, 20119, 20119, -nan)
reports[-1].sigmaresid = ValErr(1.49943, 0.00747493, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00285449, None, -4.7051e-05, None, -0.00140632, None, -7.30248e-05, None, -0.00140632, None, -7.30248e-05, None, -0.00465228, None, 1.68873e-06, None, -0.00465228, None, 1.68873e-06, None, 1.5019, None, 0.00692695, None, 1.5019, None, 0.00692695, None)

reports.append(Report(604018960, ("CSC", 1, 1, 3, 34), "MEp13_34"))
reports[-1].posNum = 19202
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00496337, 0.0110142, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.63188, 0.328937, 0), \
                           ValErr(-0.00377558, 0.00765142, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000187175, 0.000254687, 0), \
                           -35351.3, 19202, 19202, -nan)
reports[-1].sigmaresid = ValErr(1.52514, 0.00778252, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0068426, None, -1.61792e-05, None, -0.00569769, None, -7.3277e-05, None, -0.00569769, None, -7.3277e-05, None, -0.0170893, None, 2.51512e-05, None, -0.0170893, None, 2.51512e-05, None, 1.52772, None, 0.00635659, None, 1.52772, None, 0.00635659, None)

reports.append(Report(604018968, ("CSC", 1, 1, 3, 35), "MEp13_35"))
reports[-1].posNum = 18447
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0137749, 0.0111942, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.06054, 0.333798, 0), \
                           ValErr(-0.0146199, 0.00779027, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000487333, 0.000260631, 0), \
                           -33902, 18447, 18447, -nan)
reports[-1].sigmaresid = ValErr(1.52023, 0.00791459, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00988043, None, -7.36316e-06, None, -0.0135368, None, -7.84954e-05, None, -0.0135368, None, -7.84954e-05, None, -0.0319067, None, -2.76224e-05, None, -0.0319067, None, -2.76224e-05, None, 1.52383, None, 0.00720479, None, 1.52383, None, 0.00720479, None)

reports.append(Report(604018976, ("CSC", 1, 1, 3, 36), "MEp13_36"))
reports[-1].posNum = 19313
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00902846, 0.0108721, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.32217, 0.310092, 0), \
                           ValErr(0.0050616, 0.00703596, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.00018188, 0.000246855, 0), \
                           -35312.8, 19313, 19313, -nan)
reports[-1].sigmaresid = ValErr(1.50608, 0.00766318, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0145616, None, -0.000104071, None, 0.00968677, None, -8.81743e-05, None, 0.00968677, None, -8.81743e-05, None, 0.00237729, None, -5.04038e-05, None, 0.00237729, None, -5.04038e-05, None, 1.50832, None, 0.00673188, None, 1.50832, None, 0.00673188, None)

reports.append(Report(604017160, ("CSC", 1, 1, 4, 1), "MEp14_01"))
reports[-1].posNum = 104626
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00119675, 0.000605829, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.120976, 0.0477544, 0), \
                           ValErr(0.000923165, 0.00126576, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.35475e-05, 1.58672e-05, 0), \
                           24808.7, 104626, 104626, -nan)
reports[-1].sigmaresid = ValErr(0.19089, 0.000417301, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000921349, None, -1.2182e-06, None, -0.00099792, None, 9.36572e-06, None, -0.00099792, None, 9.36572e-06, None, 0.000118007, None, 5.02253e-06, None, 0.000118007, None, 5.02253e-06, None, 0.1909, None, 0.004165, None, 0.1909, None, 0.004165, None)

reports.append(Report(604017176, ("CSC", 1, 1, 4, 3), "MEp14_03"))
reports[-1].posNum = 105037
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00173429, 0.000601585, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0443993, 0.0471044, 0), \
                           ValErr(0.000368832, 0.0012467, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.82719e-05, 1.55954e-05, 0), \
                           25862, 105037, 105037, -nan)
reports[-1].sigmaresid = ValErr(0.189161, 0.00041271, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00131936, None, 1.21896e-06, None, -0.00156145, None, -6.13476e-06, None, -0.00156145, None, -6.13476e-06, None, -0.00154292, None, 1.19795e-05, None, -0.00154292, None, 1.19795e-05, None, 0.189163, None, 0.00431122, None, 0.189163, None, 0.00431122, None)

reports.append(Report(604017192, ("CSC", 1, 1, 4, 5), "MEp14_05"))
reports[-1].posNum = 104849
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00143846, 0.000604449, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0711737, 0.047659, 0), \
                           ValErr(-0.00130612, 0.00125539, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.89401e-05, 1.57148e-05, 0), \
                           24969.8, 104849, 104849, -nan)
reports[-1].sigmaresid = ValErr(0.190693, 0.000416427, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00141488, None, -6.40944e-06, None, -0.00127307, None, -7.77799e-07, None, -0.00127307, None, -7.77799e-07, None, -0.00133553, None, 1.69937e-07, None, -0.00133553, None, 1.69937e-07, None, 0.190697, None, 0.00415817, None, 0.190697, None, 0.00415817, None)

reports.append(Report(604017208, ("CSC", 1, 1, 4, 7), "MEp14_07"))
reports[-1].posNum = 105244
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00124454, 0.000602823, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.102333, 0.0473858, 0), \
                           ValErr(-0.00177376, 0.001254, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.32636e-05, 1.57048e-05, 0), \
                           25196.6, 105244, 105244, -nan)
reports[-1].sigmaresid = ValErr(0.190453, 0.000415121, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00115528, None, -6.61322e-06, None, -0.00160904, None, -6.82259e-06, None, -0.00160904, None, -6.82259e-06, None, -0.0020207, None, 1.81362e-05, None, -0.0020207, None, 1.81362e-05, None, 0.190465, None, 0.00419258, None, 0.190465, None, 0.00419258, None)

reports.append(Report(604017224, ("CSC", 1, 1, 4, 9), "MEp14_09"))
reports[-1].posNum = 104531
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00177987, 0.000602837, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0862456, 0.0473674, 0), \
                           ValErr(-0.000322426, 0.00125473, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.62969e-05, 1.57664e-05, 0), \
                           25411.3, 104531, 104531, -nan)
reports[-1].sigmaresid = ValErr(0.189752, 0.000414998, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000327877, None, 6.06972e-06, None, -0.00137566, None, 7.51328e-06, None, -0.00137566, None, 7.51328e-06, None, -0.000217536, None, -2.67879e-05, None, -0.000217536, None, -2.67879e-05, None, 0.189763, None, 0.00438794, None, 0.189763, None, 0.00438794, None)

reports.append(Report(604017240, ("CSC", 1, 1, 4, 11), "MEp14_11"))
reports[-1].posNum = 104551
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00120835, 0.000608085, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.165322, 0.0478547, 0), \
                           ValErr(-0.00220064, 0.00126423, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.37387e-05, 1.58999e-05, 0), \
                           24327, 104551, 104551, -nan)
reports[-1].sigmaresid = ValErr(0.191739, 0.000419307, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00175535, None, -1.2347e-05, None, -0.0010825, None, -3.54079e-05, None, -0.0010825, None, -3.54079e-05, None, -0.00164685, None, -6.86336e-06, None, -0.00164685, None, -6.86336e-06, None, 0.191751, None, 0.00451606, None, 0.191751, None, 0.00451606, None)

reports.append(Report(604017256, ("CSC", 1, 1, 4, 13), "MEp14_13"))
reports[-1].posNum = 105188
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0030527, 0.000600934, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0859368, 0.0471602, 0), \
                           ValErr(-0.000750973, 0.00125061, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.32788e-06, 1.56519e-05, 0), \
                           25741.9, 105188, 105188, -nan)
reports[-1].sigmaresid = ValErr(0.189444, 0.00041303, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0028218, None, -3.51849e-06, None, -0.00300936, None, 2.91817e-06, None, -0.00300936, None, 2.91817e-06, None, -0.00295166, None, -1.83854e-06, None, -0.00295166, None, -1.83854e-06, None, 0.189447, None, 0.00417552, None, 0.189447, None, 0.00417552, None)

reports.append(Report(604017272, ("CSC", 1, 1, 4, 15), "MEp14_15"))
reports[-1].posNum = 103541
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00137489, 0.000606669, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0706364, 0.0476613, 0), \
                           ValErr(-0.000640574, 0.00126337, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.40778e-05, 1.58631e-05, 0), \
                           24980.1, 103541, 103541, -nan)
reports[-1].sigmaresid = ValErr(0.190101, 0.000417747, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00113049, None, 5.5454e-07, None, -0.00125019, None, -1.02747e-05, None, -0.00125019, None, -1.02747e-05, None, -0.000277701, None, -9.70578e-06, None, -0.000277701, None, -9.70578e-06, None, 0.190104, None, 0.00449203, None, 0.190104, None, 0.00449203, None)

reports.append(Report(604017288, ("CSC", 1, 1, 4, 17), "MEp14_17"))
reports[-1].posNum = 105291
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00174287, 0.000599213, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0668451, 0.0471784, 0), \
                           ValErr(-0.000774096, 0.00124738, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.51874e-05, 1.55719e-05, 0), \
                           26098.1, 105291, 105291, -nan)
reports[-1].sigmaresid = ValErr(0.188849, 0.000411532, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00235403, None, 4.34365e-06, None, -0.00160256, None, -1.55996e-06, None, -0.00160256, None, -1.55996e-06, None, -0.00127411, None, -1.26768e-05, None, -0.00127411, None, -1.26768e-05, None, 0.188852, None, 0.0041933, None, 0.188852, None, 0.0041933, None)

reports.append(Report(604017304, ("CSC", 1, 1, 4, 19), "MEp14_19"))
reports[-1].posNum = 104391
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00139544, 0.000603691, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0505896, 0.0474511, 0), \
                           ValErr(-0.00112868, 0.00125452, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.33322e-07, 1.58205e-05, 0), \
                           25202.5, 104391, 104391, -nan)
reports[-1].sigmaresid = ValErr(0.19007, 0.000415972, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00129946, None, 4.1548e-06, None, -0.00140163, None, -1.84302e-06, None, -0.00140163, None, -1.84302e-06, None, -0.000655179, None, -2.2598e-05, None, -0.000655179, None, -2.2598e-05, None, 0.190071, None, 0.00421781, None, 0.190071, None, 0.00421781, None)

reports.append(Report(604017320, ("CSC", 1, 1, 4, 21), "MEp14_21"))
reports[-1].posNum = 105217
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00203054, 0.000598277, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0516388, 0.0471007, 0), \
                           ValErr(-0.000738558, 0.00124269, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(8.41032e-06, 1.55337e-05, 0), \
                           26168.6, 105217, 105217, -nan)
reports[-1].sigmaresid = ValErr(0.18869, 0.000411329, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00165871, None, 4.77876e-06, None, -0.00195125, None, -1.92618e-05, None, -0.00195125, None, -1.92618e-05, None, -0.00405509, None, -2.57078e-05, None, -0.00405509, None, -2.57078e-05, None, 0.188691, None, 0.00427305, None, 0.188691, None, 0.00427305, None)

reports.append(Report(604017336, ("CSC", 1, 1, 4, 23), "MEp14_23"))
reports[-1].posNum = 104455
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00271121, 0.000606942, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0651366, 0.0477439, 0), \
                           ValErr(0.000809668, 0.0012618, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.65793e-05, 1.58532e-05, 0), \
                           24691.2, 104455, 104455, -nan)
reports[-1].sigmaresid = ValErr(0.191031, 0.00041795, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00193242, None, 5.43552e-06, None, -0.00248433, None, -1.02017e-06, None, -0.00248433, None, -1.02017e-06, None, -0.00248163, None, -7.20405e-06, None, -0.00248163, None, -7.20405e-06, None, 0.191036, None, 0.00486636, None, 0.191036, None, 0.00486636, None)

reports.append(Report(604017352, ("CSC", 1, 1, 4, 25), "MEp14_25"))
reports[-1].posNum = 104829
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00263233, 0.00060361, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0508792, 0.0473433, 0), \
                           ValErr(-0.00158971, 0.0012525, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.72029e-05, 1.57303e-05, 0), \
                           25280.6, 104829, 104829, -nan)
reports[-1].sigmaresid = ValErr(0.19012, 0.000415211, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00148603, None, 6.88696e-06, None, -0.00230368, None, 7.43128e-06, None, -0.00230368, None, 7.43128e-06, None, 0.00073207, None, -1.08494e-05, None, 0.00073207, None, -1.08494e-05, None, 0.190127, None, 0.00471496, None, 0.190127, None, 0.00471496, None)

reports.append(Report(604017368, ("CSC", 1, 1, 4, 27), "MEp14_27"))
reports[-1].posNum = 104735
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0014474, 0.000602291, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0594963, 0.0473757, 0), \
                           ValErr(-0.00315169, 0.0012549, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.29164e-06, 1.57364e-05, 0), \
                           25492, 104735, 104735, -nan)
reports[-1].sigmaresid = ValErr(0.189695, 0.000414471, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00142026, None, 4.59781e-06, None, -0.00140948, None, -1.42339e-05, None, -0.00140948, None, -1.42339e-05, None, -0.00137759, None, -2.23854e-05, None, -0.00137759, None, -2.23854e-05, None, 0.189702, None, 0.00416098, None, 0.189702, None, 0.00416098, None)

reports.append(Report(604017384, ("CSC", 1, 1, 4, 29), "MEp14_29"))
reports[-1].posNum = 103763
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00399395, 0.000606801, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.150633, 0.0478146, 0), \
                           ValErr(-0.00136648, 0.00127698, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.12714e-05, 1.59054e-05, 0), \
                           24736.8, 103763, 103763, -nan)
reports[-1].sigmaresid = ValErr(0.190646, 0.000418497, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00416104, None, 1.51336e-05, None, -0.00381263, None, 1.85958e-05, None, -0.00381263, None, 1.85958e-05, None, -0.00289701, None, 1.80414e-05, None, -0.00289701, None, 1.80414e-05, None, 0.190657, None, 0.00418458, None, 0.190657, None, 0.00418458, None)

reports.append(Report(604017400, ("CSC", 1, 1, 4, 31), "MEp14_31"))
reports[-1].posNum = 104844
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000627352, 0.000603208, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0777906, 0.0475075, 0), \
                           ValErr(-0.00261706, 0.00125422, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.98353e-05, 1.56865e-05, 0), \
                           25215.3, 104844, 104844, -nan)
reports[-1].sigmaresid = ValErr(0.190245, 0.000415458, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00101284, None, -3.50192e-06, None, -0.000810729, None, -4.93282e-06, None, -0.000810729, None, -4.93282e-06, None, -0.000444619, None, -1.99427e-05, None, -0.000444619, None, -1.99427e-05, None, 0.190252, None, 0.00410769, None, 0.190252, None, 0.00410769, None)

reports.append(Report(604017416, ("CSC", 1, 1, 4, 33), "MEp14_33"))
reports[-1].posNum = 104179
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00168593, 0.000608643, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.110794, 0.0477641, 0), \
                           ValErr(-0.00225542, 0.00127068, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.47075e-07, 1.5969e-05, 0), \
                           24412, 104179, 104179, -nan)
reports[-1].sigmaresid = ValErr(0.191424, 0.000419364, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00197828, None, -8.22603e-06, None, -0.00169649, None, -1.61086e-05, None, -0.00169649, None, -1.61086e-05, None, 0.000763948, None, -1.8105e-05, None, 0.000763948, None, -1.8105e-05, None, 0.19143, None, 0.00434496, None, 0.19143, None, 0.00434496, None)

reports.append(Report(604017432, ("CSC", 1, 1, 4, 35), "MEp14_35"))
reports[-1].posNum = 105248
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00172175, 0.000598238, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0597798, 0.0469182, 0), \
                           ValErr(0.000903613, 0.00123673, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(7.27668e-06, 1.55463e-05, 0), \
                           26265.6, 105248, 105248, -nan)
reports[-1].sigmaresid = ValErr(0.18853, 0.000410921, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00148952, None, -2.38614e-06, None, -0.0016586, None, -7.52373e-06, None, -0.0016586, None, -7.52373e-06, None, -0.00136246, None, -1.46141e-05, None, -0.00136246, None, -1.46141e-05, None, 0.188533, None, 0.0042252, None, 0.188533, None, 0.0042252, None)

reports.append(Report(604017168, ("CSC", 1, 1, 4, 2), "MEp14_02"))
reports[-1].posNum = 104404
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000767389, 0.000543695, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0686402, 0.0402699, 0), \
                           ValErr(0.000698481, 0.0010683, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.62312e-05, 1.40812e-05, 0), \
                           36525.2, 104404, 104404, -nan)
reports[-1].sigmaresid = ValErr(0.17054, 0.00037321, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000962466, None, 8.93555e-06, None, -0.000918631, None, 4.76053e-05, None, -0.000918631, None, 4.76053e-05, None, -0.000740874, None, 3.70375e-05, None, -0.000740874, None, 3.70375e-05, None, 0.170545, None, 0.00446884, None, 0.170545, None, 0.00446884, None)

reports.append(Report(604017184, ("CSC", 1, 1, 4, 4), "MEp14_04"))
reports[-1].posNum = 104492
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000816608, 0.000539779, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.119614, 0.0401431, 0), \
                           ValErr(-0.00134121, 0.00106317, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.1786e-06, 1.39772e-05, 0), \
                           37189.4, 104492, 104492, -nan)
reports[-1].sigmaresid = ValErr(0.16951, 0.000370799, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000585618, None, -8.87045e-06, None, -0.000863715, None, -9.56083e-06, None, -0.000863715, None, -9.56083e-06, None, 0.000379708, None, -2.43417e-05, None, 0.000379708, None, -2.43417e-05, None, 0.169517, None, 0.00528226, None, 0.169517, None, 0.00528226, None)

reports.append(Report(604017200, ("CSC", 1, 1, 4, 6), "MEp14_06"))
reports[-1].posNum = 104691
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00156289, 0.00054356, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.044424, 0.0402968, 0), \
                           ValErr(-0.000100005, 0.00106827, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.779e-06, 1.4106e-05, 0), \
                           36503.3, 104691, 104691, -nan)
reports[-1].sigmaresid = ValErr(0.17074, 0.000373134, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00187768, None, 8.47162e-06, None, -0.001579, None, 2.76261e-05, None, -0.001579, None, 2.76261e-05, None, -0.00152747, None, 2.93894e-05, None, -0.00152747, None, 2.93894e-05, None, 0.170741, None, 0.00442216, None, 0.170741, None, 0.00442216, None)

reports.append(Report(604017216, ("CSC", 1, 1, 4, 8), "MEp14_08"))
reports[-1].posNum = 103808
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000744291, 0.00054329, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0536157, 0.0402864, 0), \
                           ValErr(-0.000925653, 0.00106569, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.94885e-06, 1.40504e-05, 0), \
                           36841.2, 103808, 103808, -nan)
reports[-1].sigmaresid = ValErr(0.169681, 0.000372394, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000188369, None, -2.47582e-06, None, -0.0007704, None, -9.66833e-06, None, -0.0007704, None, -9.66833e-06, None, 0.000734164, None, -1.15114e-05, None, 0.000734164, None, -1.15114e-05, None, 0.169683, None, 0.00447815, None, 0.169683, None, 0.00447815, None)

reports.append(Report(604017232, ("CSC", 1, 1, 4, 10), "MEp14_10"))
reports[-1].posNum = 104532
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000472327, 0.000544378, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0944354, 0.0403807, 0), \
                           ValErr(-0.000153574, 0.00106989, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.76177e-06, 1.40984e-05, 0), \
                           36349.6, 104532, 104532, -nan)
reports[-1].sigmaresid = ValErr(0.1709, 0.000373769, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000690821, None, 1.49633e-06, None, -0.000446385, None, 1.92601e-05, None, -0.000446385, None, 1.92601e-05, None, 0.000474721, None, -9.71185e-06, None, 0.000474721, None, -9.71185e-06, None, 0.170905, None, 0.00443444, None, 0.170905, None, 0.00443444, None)

reports.append(Report(604017248, ("CSC", 1, 1, 4, 12), "MEp14_12"))
reports[-1].posNum = 104555
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00165471, 0.000538651, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0591435, 0.0401149, 0), \
                           ValErr(-0.00061779, 0.00105889, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.82793e-06, 1.39394e-05, 0), \
                           37386.2, 104555, 104555, -nan)
reports[-1].sigmaresid = ValErr(0.169227, 0.000370069, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00184958, None, 1.14745e-05, None, -0.00169589, None, 2.53467e-05, None, -0.00169589, None, 2.53467e-05, None, -0.00191299, None, 7.06734e-06, None, -0.00191299, None, 7.06734e-06, None, 0.169229, None, 0.00438702, None, 0.169229, None, 0.00438702, None)

reports.append(Report(604017264, ("CSC", 1, 1, 4, 14), "MEp14_14"))
reports[-1].posNum = 104126
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000549996, 0.000542697, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.106124, 0.0403057, 0), \
                           ValErr(0.0012142, 0.0010687, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.76556e-06, 1.40574e-05, 0), \
                           36805.4, 104126, 104126, -nan)
reports[-1].sigmaresid = ValErr(0.169923, 0.000372356, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00107578, None, -1.59633e-06, None, -0.000527108, None, 2.33039e-06, None, -0.000527108, None, 2.33039e-06, None, -3.80815e-05, None, 3.38546e-06, None, -3.80815e-05, None, 3.38546e-06, None, 0.169932, None, 0.00528304, None, 0.169932, None, 0.00528304, None)

reports.append(Report(604017280, ("CSC", 1, 1, 4, 16), "MEp14_16"))
reports[-1].posNum = 103739
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00310693, 0.000543765, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.118561, 0.0404792, 0), \
                           ValErr(-0.0027799, 0.00107196, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.62698e-05, 1.4101e-05, 0), \
                           36588.2, 103739, 103739, -nan)
reports[-1].sigmaresid = ValErr(0.170055, 0.000373339, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00256091, None, 1.56215e-05, None, -0.00296189, None, 3.60015e-05, None, -0.00296189, None, 3.60015e-05, None, -0.0037904, None, 3.18605e-05, None, -0.0037904, None, 3.18605e-05, None, 0.170066, None, 0.00465666, None, 0.170066, None, 0.00465666, None)

reports.append(Report(604017296, ("CSC", 1, 1, 4, 18), "MEp14_18"))
reports[-1].posNum = 104767
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00164671, 0.000540178, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.10346, 0.0401873, 0), \
                           ValErr(0.000258787, 0.0010606, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.93338e-05, 1.39798e-05, 0), \
                           37110.4, 104767, 104767, -nan)
reports[-1].sigmaresid = ValErr(0.169796, 0.000370937, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00139804, None, 2.00746e-05, None, -0.00147269, None, 3.84985e-05, None, -0.00147269, None, 3.84985e-05, None, -0.001455, None, 3.25688e-05, None, -0.001455, None, 3.25688e-05, None, 0.169804, None, 0.00458801, None, 0.169804, None, 0.00458801, None)

reports.append(Report(604017312, ("CSC", 1, 1, 4, 20), "MEp14_20"))
reports[-1].posNum = 104613
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0019071, 0.000541577, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0759033, 0.0402461, 0), \
                           ValErr(-0.00158442, 0.00106341, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.13201e-05, 1.40242e-05, 0), \
                           36972.6, 104613, 104613, -nan)
reports[-1].sigmaresid = ValErr(0.169931, 0.000371505, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00150392, None, 1.65374e-05, None, -0.00162153, None, 3.8153e-05, None, -0.00162153, None, 3.8153e-05, None, -0.00181719, None, 3.34061e-05, None, -0.00181719, None, 3.34061e-05, None, 0.169939, None, 0.00493613, None, 0.169939, None, 0.00493613, None)

reports.append(Report(604017328, ("CSC", 1, 1, 4, 22), "MEp14_22"))
reports[-1].posNum = 103890
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00188797, 0.000541537, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.103459, 0.0400889, 0), \
                           ValErr(-0.000705725, 0.00106371, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.56426e-05, 1.40298e-05, 0), \
                           37168, 103890, 103890, -nan)
reports[-1].sigmaresid = ValErr(0.169195, 0.000371182, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00225383, None, 7.42668e-06, None, -0.00204811, None, -2.20642e-05, None, -0.00204811, None, -2.20642e-05, None, -0.00186888, None, 3.85626e-07, None, -0.00186888, None, 3.85626e-07, None, 0.169202, None, 0.00474286, None, 0.169202, None, 0.00474286, None)

reports.append(Report(604017344, ("CSC", 1, 1, 4, 24), "MEp14_24"))
reports[-1].posNum = 103930
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00260978, 0.000543371, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0472737, 0.0404521, 0), \
                           ValErr(-0.000861276, 0.00106446, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.29088e-05, 1.40627e-05, 0), \
                           36588.8, 103930, 103930, -nan)
reports[-1].sigmaresid = ValErr(0.170164, 0.000373236, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00226801, None, 1.50373e-05, None, -0.0027332, None, 2.77824e-05, None, -0.0027332, None, 2.77824e-05, None, -0.00121685, None, 1.47953e-05, None, -0.00121685, None, 1.47953e-05, None, 0.170166, None, 0.00461124, None, 0.170166, None, 0.00461124, None)

reports.append(Report(604017360, ("CSC", 1, 1, 4, 26), "MEp14_26"))
reports[-1].posNum = 104364
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000925634, 0.000542389, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.105702, 0.0403338, 0), \
                           ValErr(0.00286621, 0.00106444, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.77296e-06, 1.40428e-05, 0), \
                           36824.1, 104364, 104364, -nan)
reports[-1].sigmaresid = ValErr(0.17003, 0.000372164, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00104209, None, 3.18294e-06, None, -0.000954098, None, 3.50013e-05, None, -0.000954098, None, 3.50013e-05, None, -0.00068473, None, 4.78905e-06, None, -0.00068473, None, 4.78905e-06, None, 0.170045, None, 0.00502994, None, 0.170045, None, 0.00502994, None)

reports.append(Report(604017376, ("CSC", 1, 1, 4, 28), "MEp14_28"))
reports[-1].posNum = 103981
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000204647, 0.000546782, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0973003, 0.0406259, 0), \
                           ValErr(-0.00128674, 0.00107316, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.6163e-05, 1.41145e-05, 0), \
                           36063.2, 103981, 103981, -nan)
reports[-1].sigmaresid = ValErr(0.171056, 0.0003751, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000334816, None, 6.21542e-06, None, -0.000459341, None, 2.72995e-05, None, -0.000459341, None, 2.72995e-05, None, -0.00141954, None, 2.24788e-05, None, -0.00141954, None, 2.24788e-05, None, 0.171064, None, 0.0043154, None, 0.171064, None, 0.0043154, None)

reports.append(Report(604017392, ("CSC", 1, 1, 4, 30), "MEp14_30"))
reports[-1].posNum = 103574
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00104043, 0.000542147, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.136727, 0.0403513, 0), \
                           ValErr(8.44291e-05, 0.00106816, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.48535e-07, 1.40581e-05, 0), \
                           36939, 103574, 103574, -nan)
reports[-1].sigmaresid = ValErr(0.169385, 0.000372164, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000937152, None, -1.2331e-06, None, -0.00106538, None, 1.95218e-05, None, -0.00106538, None, 1.95218e-05, None, -0.000739922, None, 3.7204e-06, None, -0.000739922, None, 3.7204e-06, None, 0.169395, None, 0.00455981, None, 0.169395, None, 0.00455981, None)

reports.append(Report(604017408, ("CSC", 1, 1, 4, 32), "MEp14_32"))
reports[-1].posNum = 104443
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00217088, 0.000543068, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0731247, 0.0404186, 0), \
                           ValErr(-0.000755381, 0.00106636, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.91957e-05, 1.40382e-05, 0), \
                           36631.4, 104443, 104443, -nan)
reports[-1].sigmaresid = ValErr(0.170389, 0.00037281, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00155956, None, 1.27043e-05, None, -0.00199974, None, 2.99817e-05, None, -0.00199974, None, 2.99817e-05, None, -0.000672345, None, 2.61092e-05, None, -0.000672345, None, 2.61092e-05, None, 0.170393, None, 0.00435934, None, 0.170393, None, 0.00435934, None)

reports.append(Report(604017424, ("CSC", 1, 1, 4, 34), "MEp14_34"))
reports[-1].posNum = 97404
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00175778, 0.000565716, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0825406, 0.0411021, 0), \
                           ValErr(-0.000110601, 0.00108351, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(8.81033e-06, 1.44459e-05, 0), \
                           34919, 97404, 97404, -nan)
reports[-1].sigmaresid = ValErr(0.169071, 0.00038306, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00208498, None, -3.24584e-05, None, -0.00170435, None, -7.11806e-05, None, -0.00170435, None, -7.11806e-05, None, -0.000812705, None, -3.32919e-05, None, -0.000812705, None, -3.32919e-05, None, 0.169075, None, 0.00556716, None, 0.169075, None, 0.00556716, None)

reports.append(Report(604017440, ("CSC", 1, 1, 4, 36), "MEp14_36"))
reports[-1].posNum = 104716
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00298627, 0.000542192, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.13088, 0.0402075, 0), \
                           ValErr(0.000159361, 0.00106336, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.229e-05, 1.40463e-05, 0), \
                           36878.4, 104716, 104716, -nan)
reports[-1].sigmaresid = ValErr(0.170143, 0.000371786, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00264189, None, 1.38688e-05, None, -0.00269131, None, 6.4379e-05, None, -0.00269131, None, 6.4379e-05, None, -0.00244136, None, 3.86862e-05, None, -0.00244136, None, 3.86862e-05, None, 0.170157, None, 0.0052188, None, 0.170157, None, 0.0052188, None)

reports.append(Report(604021256, ("CSC", 1, 2, 1, 1), "MEp21_01"))
reports[-1].posNum = 209504
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000693812, 0.000929964, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.00850003, 0.0359232, 0), \
                           ValErr(0.00141744, 0.0007094, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.64332e-05, 1.8634e-05, 0), \
                           -114785, 209504, 209504, -nan)
reports[-1].sigmaresid = ValErr(0.418512, 0.000646542, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000974402, None, 9.68583e-06, None, -0.000543672, None, 2.44008e-05, None, -0.000543672, None, 2.44008e-05, None, 0.00030866, None, 1.13111e-05, None, 0.00030866, None, 1.13111e-05, None, 0.418517, None, 0.00546322, None, 0.418517, None, 0.00546322, None)

reports.append(Report(604021272, ("CSC", 1, 2, 1, 3), "MEp21_03"))
reports[-1].posNum = 210208
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00111366, 0.000927408, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.017524, 0.0358565, 0), \
                           ValErr(0.000372168, 0.000705415, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.48674e-05, 1.85255e-05, 0), \
                           -114969, 210208, 210208, -nan)
reports[-1].sigmaresid = ValErr(0.418112, 0.000644841, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000775643, None, 2.09514e-05, None, -0.000886159, None, 3.164e-05, None, -0.000886159, None, 3.164e-05, None, -0.000854823, None, 1.68809e-05, None, -0.000854823, None, 1.68809e-05, None, 0.418114, None, 0.00557403, None, 0.418114, None, 0.00557403, None)

reports.append(Report(604021288, ("CSC", 1, 2, 1, 5), "MEp21_05"))
reports[-1].posNum = 210791
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000410493, 0.000926868, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0631939, 0.0357721, 0), \
                           ValErr(0.00200098, 0.000705961, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.6931e-06, 1.85534e-05, 0), \
                           -115276, 210791, 210791, -nan)
reports[-1].sigmaresid = ValErr(0.418087, 0.000643911, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000915453, None, -1.96978e-05, None, 0.000449313, None, 6.41689e-06, None, 0.000449313, None, 6.41689e-06, None, 0.00136615, None, -6.84732e-06, None, 0.00136615, None, -6.84732e-06, None, 0.418101, None, 0.00570551, None, 0.418101, None, 0.00570551, None)

reports.append(Report(604021304, ("CSC", 1, 2, 1, 7), "MEp21_07"))
reports[-1].posNum = 209564
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00238122, 0.000925749, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0291796, 0.0357381, 0), \
                           ValErr(0.000224822, 0.000705886, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.46004e-05, 1.85175e-05, 0), \
                           -113645, 209564, 209564, -nan)
reports[-1].sigmaresid = ValErr(0.416177, 0.000642843, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00152943, None, 1.65346e-05, None, -0.00205321, None, 3.8424e-05, None, -0.00205321, None, 3.8424e-05, None, -0.00131751, None, 1.56094e-05, None, -0.00131751, None, 1.56094e-05, None, 0.416181, None, 0.00567118, None, 0.416181, None, 0.00567118, None)

reports.append(Report(604021320, ("CSC", 1, 2, 1, 9), "MEp21_09"))
reports[-1].posNum = 209663
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00235166, 0.00091899, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0178021, 0.0355027, 0), \
                           ValErr(-0.00040089, 0.000699943, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.11822e-05, 1.83716e-05, 0), \
                           -112458, 209663, 209663, -nan)
reports[-1].sigmaresid = ValErr(0.413722, 0.0006389, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00313691, None, 1.70661e-05, None, -0.00206819, None, 1.46467e-05, None, -0.00206819, None, 1.46467e-05, None, -0.00123013, None, 9.57808e-06, None, -0.00123013, None, 9.57808e-06, None, 0.413725, None, 0.00558473, None, 0.413725, None, 0.00558473, None)

reports.append(Report(604021336, ("CSC", 1, 2, 1, 11), "MEp21_11"))
reports[-1].posNum = 210078
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000102385, 0.000920198, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0405483, 0.0355764, 0), \
                           ValErr(0.000412561, 0.000701813, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.64979e-05, 1.83831e-05, 0), \
                           -113030, 210078, 210078, -nan)
reports[-1].sigmaresid = ValErr(0.414409, 0.000639328, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000738003, None, 3.85948e-08, None, -0.000442378, None, 2.66124e-05, None, -0.000442378, None, 2.66124e-05, None, -0.00154765, None, -4.6121e-06, None, -0.00154765, None, -4.6121e-06, None, 0.414415, None, 0.00565085, None, 0.414415, None, 0.00565085, None)

reports.append(Report(604021352, ("CSC", 1, 2, 1, 13), "MEp21_13"))
reports[-1].posNum = 209156
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0021505, 0.000924167, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.01576, 0.0357031, 0), \
                           ValErr(0.000318792, 0.000706019, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(9.7312e-06, 1.84867e-05, 0), \
                           -112839, 209156, 209156, -nan)
reports[-1].sigmaresid = ValErr(0.415014, 0.000641672, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0017126, None, 8.16266e-07, None, -0.00205925, None, 1.67121e-05, None, -0.00205925, None, 1.67121e-05, None, -0.00090423, None, -2.12688e-06, None, -0.00090423, None, -2.12688e-06, None, 0.415015, None, 0.00563564, None, 0.415015, None, 0.00563564, None)

reports.append(Report(604021368, ("CSC", 1, 2, 1, 15), "MEp21_15"))
reports[-1].posNum = 209131
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00220847, 0.00092415, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0765298, 0.0357804, 0), \
                           ValErr(0.000846543, 0.000707494, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.45813e-05, 1.85103e-05, 0), \
                           -112973, 209131, 209131, -nan)
reports[-1].sigmaresid = ValErr(0.415307, 0.000642163, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00291722, None, 2.37372e-05, None, -0.0023396, None, 4.72543e-05, None, -0.0023396, None, 4.72543e-05, None, -0.00141011, None, 8.38294e-06, None, -0.00141011, None, 8.38294e-06, None, 0.415315, None, 0.0057213, None, 0.415315, None, 0.0057213, None)

reports.append(Report(604021384, ("CSC", 1, 2, 1, 17), "MEp21_17"))
reports[-1].posNum = 209310
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000489922, 0.000930783, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0382117, 0.0358862, 0), \
                           ValErr(0.000712299, 0.000708398, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.3257e-06, 1.86375e-05, 0), \
                           -114468, 209310, 209310, -nan)
reports[-1].sigmaresid = ValErr(0.418092, 0.000646192, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000199836, None, 8.37759e-06, None, 0.000544425, None, 1.54384e-05, None, 0.000544425, None, 1.54384e-05, None, 0.00226871, None, 6.60088e-06, None, 0.00226871, None, 6.60088e-06, None, 0.418095, None, 0.00553646, None, 0.418095, None, 0.00553646, None)

reports.append(Report(604021264, ("CSC", 1, 2, 1, 2), "MEp21_02"))
reports[-1].posNum = 209329
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00115285, 0.000878731, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0207749, 0.0328871, 0), \
                           ValErr(-0.000194988, 0.00064693, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.12128e-06, 1.74859e-05, 0), \
                           -101997, 209329, 209329, -nan)
reports[-1].sigmaresid = ValErr(0.393891, 0.000608762, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000595293, None, -1.10007e-05, None, 0.00119651, None, 1.04849e-06, None, 0.00119651, None, 1.04849e-06, None, 0.00191214, None, -1.6143e-05, None, 0.00191214, None, -1.6143e-05, None, 0.393891, None, 0.00615139, None, 0.393891, None, 0.00615139, None)

reports.append(Report(604021280, ("CSC", 1, 2, 1, 4), "MEp21_04"))
reports[-1].posNum = 208901
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00149581, 0.000882912, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.00939598, 0.032995, 0), \
                           ValErr(-0.000261723, 0.000649479, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.29719e-05, 1.75827e-05, 0), \
                           -102647, 208901, 208901, -nan)
reports[-1].sigmaresid = ValErr(0.395513, 0.000611893, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00177114, None, 3.55702e-06, None, 0.00136778, None, -9.13151e-06, None, 0.00136778, None, -9.13151e-06, None, 0.000840101, None, -2.36742e-05, None, 0.000840101, None, -2.36742e-05, None, 0.395513, None, 0.00598699, None, 0.395513, None, 0.00598699, None)

reports.append(Report(604021296, ("CSC", 1, 2, 1, 6), "MEp21_06"))
reports[-1].posNum = 208639
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00105806, 0.000882208, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0169913, 0.0329656, 0), \
                           ValErr(0.000443979, 0.000649761, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.7122e-05, 1.75806e-05, 0), \
                           -102374, 208639, 208639, -nan)
reports[-1].sigmaresid = ValErr(0.39524, 0.000611855, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00102653, None, 1.0689e-05, None, 0.00088765, None, 1.47222e-05, None, 0.00088765, None, 1.47222e-05, None, 0.00124179, None, 4.32526e-07, None, 0.00124179, None, 4.32526e-07, None, 0.395241, None, 0.00606391, None, 0.395241, None, 0.00606391, None)

reports.append(Report(604021312, ("CSC", 1, 2, 1, 8), "MEp21_08"))
reports[-1].posNum = 208549
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00224534, 0.000881972, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.039523, 0.0330253, 0), \
                           ValErr(0.000540435, 0.000650546, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.20493e-05, 1.75832e-05, 0), \
                           -102266, 208549, 208549, -nan)
reports[-1].sigmaresid = ValErr(0.395119, 0.000611799, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00169024, None, -5.88134e-06, None, -0.00193455, None, 1.19129e-05, None, -0.00193455, None, 1.19129e-05, None, -0.000356989, None, -1.30438e-05, None, -0.000356989, None, -1.30438e-05, None, 0.395123, None, 0.00606809, None, 0.395123, None, 0.00606809, None)

reports.append(Report(604021328, ("CSC", 1, 2, 1, 10), "MEp21_10"))
reports[-1].posNum = 209486
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000524739, 0.00088512, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0131387, 0.0331486, 0), \
                           ValErr(-0.00084122, 0.000651936, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.06822e-06, 1.76357e-05, 0), \
                           -103795, 209486, 209486, -nan)
reports[-1].sigmaresid = ValErr(0.397141, 0.000613554, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000247544, None, -4.67019e-06, None, -0.000491833, None, 1.40433e-05, None, -0.000491833, None, 1.40433e-05, None, -6.13474e-05, None, 6.55286e-06, None, -6.13474e-05, None, 6.55286e-06, None, 0.397143, None, 0.00610675, None, 0.397143, None, 0.00610675, None)

reports.append(Report(604021344, ("CSC", 1, 2, 1, 12), "MEp21_12"))
reports[-1].posNum = 209439
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00275686, 0.000885566, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0100414, 0.0330393, 0), \
                           ValErr(0.000265046, 0.000650136, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.06415e-05, 1.7634e-05, 0), \
                           -103733, 209439, 209439, -nan)
reports[-1].sigmaresid = ValErr(0.397068, 0.000613509, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0021702, None, 2.49549e-05, None, -0.00264893, None, 5.88209e-05, None, -0.00264893, None, 5.88209e-05, None, -0.000197006, None, 2.88666e-05, None, -0.000197006, None, 2.88666e-05, None, 0.397068, None, 0.00598391, None, 0.397068, None, 0.00598391, None)

reports.append(Report(604021360, ("CSC", 1, 2, 1, 14), "MEp21_14"))
reports[-1].posNum = 210154
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00135958, 0.000882849, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00923488, 0.0330015, 0), \
                           ValErr(-0.000198269, 0.000649296, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.52368e-05, 1.75787e-05, 0), \
                           -104012, 210154, 210154, -nan)
reports[-1].sigmaresid = ValErr(0.396925, 0.000612244, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000487729, None, -4.83109e-06, None, 0.00101561, None, 3.90747e-05, None, 0.00101561, None, 3.90747e-05, None, 0.00206865, None, 2.15934e-05, None, 0.00206865, None, 2.15934e-05, None, 0.396929, None, 0.00604967, None, 0.396929, None, 0.00604967, None)

reports.append(Report(604021376, ("CSC", 1, 2, 1, 16), "MEp21_16"))
reports[-1].posNum = 209730
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000545744, 0.0008863, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.00843896, 0.0331345, 0), \
                           ValErr(-0.0015171, 0.000651531, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.54546e-06, 1.76412e-05, 0), \
                           -104434, 209730, 209730, -nan)
reports[-1].sigmaresid = ValErr(0.398124, 0.000614714, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00051202, None, -1.58071e-05, None, -0.000600229, None, -6.24441e-07, None, -0.000600229, None, -6.24441e-07, None, -0.000926062, None, -1.2401e-05, None, -0.000926062, None, -1.2401e-05, None, 0.398129, None, 0.0059579, None, 0.398129, None, 0.0059579, None)

reports.append(Report(604021392, ("CSC", 1, 2, 1, 18), "MEp21_18"))
reports[-1].posNum = 209515
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00168749, 0.000882878, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0323106, 0.0329728, 0), \
                           ValErr(0.000284519, 0.000648977, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.12479e-06, 1.75715e-05, 0), \
                           -103155, 209515, 209515, -nan)
reports[-1].sigmaresid = ValErr(0.395902, 0.000611597, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00229637, None, 9.23278e-06, None, -0.00166455, None, 3.12239e-06, None, -0.00166455, None, 3.12239e-06, None, -0.00104097, None, -3.21641e-06, None, -0.00104097, None, -3.21641e-06, None, 0.395903, None, 0.00612085, None, 0.395903, None, 0.00612085, None)

reports.append(Report(604021768, ("CSC", 1, 2, 2, 1), "MEp22_01"))
reports[-1].posNum = 54602
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000624599, 0.00478242, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0388063, 0.177408, 0), \
                           ValErr(0.0026085, 0.00197637, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.18721e-05, 5.11068e-05, 0), \
                           -78616.3, 54602, 54602, -nan)
reports[-1].sigmaresid = ValErr(1.02109, 0.0030899, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000727621, None, 1.35803e-05, None, 0.0014272, None, 2.0308e-05, None, 0.0014272, None, 2.0308e-05, None, 0.00563853, None, -8.45658e-07, None, 0.00563853, None, -8.45658e-07, None, 1.02111, None, 0.00677369, None, 1.02111, None, 0.00677369, None)

reports.append(Report(604021784, ("CSC", 1, 2, 2, 3), "MEp22_03"))
reports[-1].posNum = 47039
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00496707, 0.00512825, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.18138, 0.190326, 0), \
                           ValErr(0.000104153, 0.00208673, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.92274e-06, 5.3371e-05, 0), \
                           -66037.5, 47039, 47039, -nan)
reports[-1].sigmaresid = ValErr(0.985059, 0.00321156, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00354805, None, -2.7939e-05, None, 0.0050307, None, -3.42161e-05, None, 0.0050307, None, -3.42161e-05, None, 0.0013338, None, -4.42301e-05, None, 0.0013338, None, -4.42301e-05, None, 0.985073, None, 0.00690565, None, 0.985073, None, 0.00690565, None)

reports.append(Report(604021800, ("CSC", 1, 2, 2, 5), "MEp22_05"))
reports[-1].posNum = 54736
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0121082, 0.00471216, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.455022, 0.179258, 0), \
                           ValErr(0.00179521, 0.00199438, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.68416e-05, 5.0429e-05, 0), \
                           -78111.4, 54736, 54736, -nan)
reports[-1].sigmaresid = ValErr(1.00815, 0.003047, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00634134, None, -1.88911e-05, None, 0.00874141, None, -6.44902e-05, None, 0.00874141, None, -6.44902e-05, None, 0.0112718, None, -1.84078e-05, None, 0.0112718, None, -1.84078e-05, None, 1.00824, None, 0.00683383, None, 1.00824, None, 0.00683383, None)

reports.append(Report(604021816, ("CSC", 1, 2, 2, 7), "MEp22_07"))
reports[-1].posNum = 46941
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00797516, 0.00515777, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.169406, 0.189371, 0), \
                           ValErr(-0.00120527, 0.0020724, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.98469e-05, 5.36092e-05, 0), \
                           -66504.5, 46941, 46941, -nan)
reports[-1].sigmaresid = ValErr(0.997832, 0.00325662, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00579304, None, 3.09479e-06, None, -0.00996775, None, 1.72753e-05, None, -0.00996775, None, 1.72753e-05, None, -0.012395, None, 2.71202e-05, None, -0.012395, None, 2.71202e-05, None, 0.997852, None, 0.00646341, None, 0.997852, None, 0.00646341, None)

reports.append(Report(604021832, ("CSC", 1, 2, 2, 9), "MEp22_09"))
reports[-1].posNum = 49531
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00856898, 0.00501013, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.184463, 0.190213, 0), \
                           ValErr(0.00263883, 0.00209213, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.28684e-05, 5.2881e-05, 0), \
                           -71121.6, 49531, 49531, -nan)
reports[-1].sigmaresid = ValErr(1.01711, 0.00323157, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0050669, None, 5.39617e-05, None, -0.00780271, None, 6.48984e-05, None, -0.00780271, None, 6.48984e-05, None, -0.00646259, None, 1.57625e-05, None, -0.00646259, None, 1.57625e-05, None, 1.01714, None, 0.00834473, None, 1.01714, None, 0.00834473, None)

reports.append(Report(604021848, ("CSC", 1, 2, 2, 11), "MEp22_11"))
reports[-1].posNum = 49386
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00192063, 0.00501819, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.250795, 0.191264, 0), \
                           ValErr(-0.000493275, 0.00207273, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.06977e-05, 5.25877e-05, 0), \
                           -70499.2, 49386, 49386, -nan)
reports[-1].sigmaresid = ValErr(1.00861, 0.00320926, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00789064, None, -2.1662e-06, None, -8.55481e-05, None, 1.58489e-05, None, -8.55481e-05, None, 1.58489e-05, None, -0.00590958, None, 4.96151e-06, None, -0.00590958, None, 4.96151e-06, None, 1.00864, None, 0.00660802, None, 1.00864, None, 0.00660802, None)

reports.append(Report(604021864, ("CSC", 1, 2, 2, 13), "MEp22_13"))
reports[-1].posNum = 45942
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0136227, 0.0052428, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0408191, 0.190787, 0), \
                           ValErr(-0.00111532, 0.00209013, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.91788e-05, 5.41779e-05, 0), \
                           -64980, 45942, 45942, -nan)
reports[-1].sigmaresid = ValErr(0.995463, 0.00328401, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0128218, None, -1.32582e-05, None, -0.0118433, None, -2.58377e-05, None, -0.0118433, None, -2.58377e-05, None, -0.0145796, None, 5.61195e-05, None, -0.0145796, None, 5.61195e-05, None, 0.995475, None, 0.00663598, None, 0.995475, None, 0.00663598, None)

reports.append(Report(604021880, ("CSC", 1, 2, 2, 15), "MEp22_15"))
reports[-1].posNum = 55673
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00223774, 0.00471003, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.126352, 0.17757, 0), \
                           ValErr(-0.00123581, 0.00198548, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.69686e-05, 5.06258e-05, 0), \
                           -80289.1, 55673, 55673, -nan)
reports[-1].sigmaresid = ValErr(1.02349, 0.00306723, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00660529, None, 3.08597e-05, None, -0.00125959, None, 1.74467e-05, None, -0.00125959, None, 1.74467e-05, None, 0.00652502, None, 1.79577e-05, None, 0.00652502, None, 1.79577e-05, None, 1.0235, None, 0.00716109, None, 1.0235, None, 0.00716109, None)

reports.append(Report(604021896, ("CSC", 1, 2, 2, 17), "MEp22_17"))
reports[-1].posNum = 46308
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0106171, 0.005163, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.649582, 0.193049, 0), \
                           ValErr(0.00392555, 0.00209449, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(9.66147e-05, 5.34314e-05, 0), \
                           -65006.9, 46308, 46308, -nan)
reports[-1].sigmaresid = ValErr(0.98497, 0.00323653, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00288505, None, -5.82002e-06, None, -0.00635848, None, -3.89139e-05, None, -0.00635848, None, -3.89139e-05, None, -0.00243131, None, 5.10532e-06, None, -0.00243131, None, 5.10532e-06, None, 0.985144, None, 0.00658525, None, 0.985144, None, 0.00658525, None)

reports.append(Report(604021912, ("CSC", 1, 2, 2, 19), "MEp22_19"))
reports[-1].posNum = 54830
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00209287, 0.00476464, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.185471, 0.176487, 0), \
                           ValErr(0.000225407, 0.00196321, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.15689e-05, 5.0843e-05, 0), \
                           -78897, 54830, 54830, -nan)
reports[-1].sigmaresid = ValErr(1.0202, 0.00308079, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000505475, None, -2.71225e-05, None, 0.000505726, None, -1.57381e-06, None, 0.000505726, None, -1.57381e-06, None, -0.00888504, None, 3.35783e-05, None, -0.00888504, None, 3.35783e-05, None, 1.02022, None, 0.00670663, None, 1.02022, None, 0.00670663, None)

reports.append(Report(604021928, ("CSC", 1, 2, 2, 21), "MEp22_21"))
reports[-1].posNum = 46060
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00422187, 0.00516143, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.123366, 0.193196, 0), \
                           ValErr(0.00230002, 0.00210756, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.62238e-05, 5.34359e-05, 0), \
                           -64613.7, 46060, 46060, -nan)
reports[-1].sigmaresid = ValErr(0.984004, 0.00324204, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00310988, None, -1.47725e-06, None, 0.00313368, None, 1.97181e-05, None, 0.00313368, None, 1.97181e-05, None, 0.00340976, None, 3.0466e-05, None, 0.00340976, None, 3.0466e-05, None, 0.984028, None, 0.00708366, None, 0.984028, None, 0.00708366, None)

reports.append(Report(604021944, ("CSC", 1, 2, 2, 23), "MEp22_23"))
reports[-1].posNum = 54858
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00747449, 0.00470065, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0998561, 0.0931443, 0), \
                           ValErr(0.000865029, 0.00111294, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.29072e-05, 5.01512e-05, 0), \
                           -78675.2, 54858, 54858, -nan)
reports[-1].sigmaresid = ValErr(1.01534, 0.00294697, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0134287, None, 4.4302e-06, None, -0.00833896, None, -4.98451e-06, None, -0.00833896, None, -4.98451e-06, None, -0.00935198, None, 2.76302e-05, None, -0.00935198, None, 2.76302e-05, None, 1.01535, None, 0.00661949, None, 1.01535, None, 0.00661949, None)

reports.append(Report(604021960, ("CSC", 1, 2, 2, 25), "MEp22_25"))
reports[-1].posNum = 47717
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00429327, 0.00511358, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.253821, 0.187006, 0), \
                           ValErr(-0.00337801, 0.00205513, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.95789e-05, 5.34266e-05, 0), \
                           -67546, 47717, 47717, -nan)
reports[-1].sigmaresid = ValErr(0.996622, 0.00322611, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00341603, None, -8.83371e-07, None, -0.00496661, None, -8.81617e-06, None, -0.00496661, None, -8.81617e-06, None, -0.0135626, None, 3.75756e-05, None, -0.0135626, None, 3.75756e-05, None, 0.996665, None, 0.00652495, None, 0.996665, None, 0.00652495, None)

reports.append(Report(604021976, ("CSC", 1, 2, 2, 27), "MEp22_27"))
reports[-1].posNum = 49707
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00626383, 0.00499802, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.20106, 0.188462, 0), \
                           ValErr(-0.00132266, 0.00208322, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.91721e-05, 5.28893e-05, 0), \
                           -71098.8, 49707, 49707, -nan)
reports[-1].sigmaresid = ValErr(1.01149, 0.00320801, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00371812, None, 6.33959e-06, None, -0.00411459, None, -2.82414e-07, None, -0.00411459, None, -2.82414e-07, None, -0.00437471, None, 4.96027e-05, None, -0.00437471, None, 4.96027e-05, None, 1.01151, None, 0.00654902, None, 1.01151, None, 0.00654902, None)

reports.append(Report(604021992, ("CSC", 1, 2, 2, 29), "MEp22_29"))
reports[-1].posNum = 50584
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000163926, 0.00494066, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.300462, 0.186245, 0), \
                           ValErr(0.00089699, 0.00206042, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.61701e-06, 5.23332e-05, 0), \
                           -72122.6, 50584, 50584, -nan)
reports[-1].sigmaresid = ValErr(1.00689, 0.00316567, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00651707, None, -2.80711e-06, None, 0.000180768, None, -1.67679e-05, None, 0.000180768, None, -1.67679e-05, None, -0.00296375, None, 1.30705e-05, None, -0.00296375, None, 1.30705e-05, None, 1.00691, None, 0.00636047, None, 1.00691, None, 0.00636047, None)

reports.append(Report(604022008, ("CSC", 1, 2, 2, 31), "MEp22_31"))
reports[-1].posNum = 47698
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0101672, 0.00515261, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0622258, 0.188152, 0), \
                           ValErr(0.0010702, 0.00207571, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.7965e-05, 5.36292e-05, 0), \
                           -67389.6, 47698, 47698, -nan)
reports[-1].sigmaresid = ValErr(0.993918, 0.00321799, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0101268, None, 2.16431e-05, None, -0.00846422, None, 7.83016e-05, None, -0.00846422, None, 7.83016e-05, None, -0.00805662, None, 7.26173e-05, None, -0.00805662, None, 7.26173e-05, None, 0.993928, None, 0.00661891, None, 0.993928, None, 0.00661891, None)

reports.append(Report(604022024, ("CSC", 1, 2, 2, 33), "MEp22_33"))
reports[-1].posNum = 54559
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00617455, 0.00472305, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0805812, 0.177679, 0), \
                           ValErr(-0.000384644, 0.00197762, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.63333e-05, 5.04681e-05, 0), \
                           -78171.6, 54559, 54559, -nan)
reports[-1].sigmaresid = ValErr(1.01395, 0.00306951, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000956506, None, 2.39094e-06, None, -0.00371714, None, -9.63066e-06, None, -0.00371714, None, -9.63066e-06, None, -0.00771871, None, 2.61771e-05, None, -0.00771871, None, 2.61771e-05, None, 1.01397, None, 0.00666309, None, 1.01397, None, 0.00666309, None)

reports.append(Report(604022040, ("CSC", 1, 2, 2, 35), "MEp22_35"))
reports[-1].posNum = 45385
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00270916, 0.00517398, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.262583, 0.194598, 0), \
                           ValErr(0.00390342, 0.0020957, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.15223e-05, 5.30932e-05, 0), \
                           -63223.3, 45385, 45385, -nan)
reports[-1].sigmaresid = ValErr(0.974434, 0.0032343, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00117884, None, -1.82772e-05, None, -0.000729108, None, -7.98768e-06, None, -0.000729108, None, -7.98768e-06, None, -0.00124271, None, -5.81441e-05, None, -0.00124271, None, -5.81441e-05, None, 0.974492, None, 0.00652845, None, 0.974492, None, 0.00652845, None)

reports.append(Report(604021776, ("CSC", 1, 2, 2, 2), "MEp22_02"))
reports[-1].posNum = 48838
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0059358, 0.00498214, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0670683, 0.182052, 0), \
                           ValErr(0.00208205, 0.0019873, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.85922e-05, 5.22984e-05, 0), \
                           -69459.3, 48838, 48838, -nan)
reports[-1].sigmaresid = ValErr(1.0033, 0.00321025, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0003202, None, 1.63667e-05, None, 0.0037936, None, -1.52282e-05, None, 0.0037936, None, -1.52282e-05, None, 0.00372829, None, -1.49127e-05, None, 0.00372829, None, -1.49127e-05, None, 1.00333, None, 0.00676411, None, 1.00333, None, 0.00676411, None)

reports.append(Report(604021792, ("CSC", 1, 2, 2, 4), "MEp22_04"))
reports[-1].posNum = 45093
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0119952, 0.00527015, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.127226, 0.124798, 0), \
                           ValErr(-0.000703964, 0.00205283, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000103114, 5.41055e-05, 0), \
                           -63902.5, 45093, 45093, -nan)
reports[-1].sigmaresid = ValErr(0.998191, 0.00331101, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00769487, None, 1.55537e-05, None, 0.00738621, None, 4.27941e-06, None, 0.00738621, None, 4.27941e-06, None, 0.0095052, None, -1.12357e-05, None, 0.0095052, None, -1.12357e-05, None, 0.998235, None, 0.00647263, None, 0.998235, None, 0.00647263, None)

reports.append(Report(604021808, ("CSC", 1, 2, 2, 6), "MEp22_06"))
reports[-1].posNum = 52892
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000158829, 0.00478361, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.475529, 0.174142, 0), \
                           ValErr(0.00429166, 0.00194091, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.64131e-06, 5.10765e-05, 0), \
                           -75504.7, 52892, 52892, -nan)
reports[-1].sigmaresid = ValErr(1.00863, 0.00310113, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00267284, None, 3.02102e-05, None, 3.34291e-05, None, 2.08208e-05, None, 3.34291e-05, None, 2.08208e-05, None, 0.0096284, None, -3.51148e-05, None, 0.0096284, None, -3.51148e-05, None, 1.00873, None, 0.0068959, None, 1.00873, None, 0.0068959, None)

reports.append(Report(604021824, ("CSC", 1, 2, 2, 8), "MEp22_08"))
reports[-1].posNum = 43157
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00680839, 0.00528199, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.17952, 0.107721, 0), \
                           ValErr(-0.000725919, 0.00202623, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.89453e-05, 5.39879e-05, 0), \
                           -60742.8, 43157, 43157, -nan)
reports[-1].sigmaresid = ValErr(0.98861, 0.00326577, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00317903, None, 4.97009e-06, None, 0.00259583, None, 4.71593e-06, None, 0.00259583, None, 4.71593e-06, None, 0.00920443, None, 3.61966e-05, None, 0.00920443, None, 3.61966e-05, None, 0.988662, None, 0.00659344, None, 0.988662, None, 0.00659344, None)

reports.append(Report(604021840, ("CSC", 1, 2, 2, 10), "MEp22_10"))
reports[-1].posNum = 54976
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00298184, 0.00472737, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.159964, 0.17309, 0), \
                           ValErr(-0.000313746, 0.00192757, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.04318e-05, 5.06511e-05, 0), \
                           -78659.2, 54976, 54976, -nan)
reports[-1].sigmaresid = ValErr(1.01193, 0.00305175, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00633651, None, 4.77333e-05, None, -0.00379263, None, 3.40577e-05, None, -0.00379263, None, 3.40577e-05, None, -0.000754963, None, 4.45613e-05, None, -0.000754963, None, 4.45613e-05, None, 1.01193, None, 0.00692599, None, 1.01193, None, 0.00692599, None)

reports.append(Report(604021856, ("CSC", 1, 2, 2, 12), "MEp22_12"))
reports[-1].posNum = 44167
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00206248, 0.00518797, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.144225, 0.187485, 0), \
                           ValErr(-0.00353211, 0.0020224, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.51497e-05, 5.36402e-05, 0), \
                           -61811.6, 44167, 44167, -nan)
reports[-1].sigmaresid = ValErr(0.980744, 0.00329982, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00103319, None, 3.14919e-05, None, 2.29789e-06, None, -3.01554e-06, None, 2.29789e-06, None, -3.01554e-06, None, -0.00886093, None, 4.1211e-05, None, -0.00886093, None, 4.1211e-05, None, 0.980791, None, 0.00664551, None, 0.980791, None, 0.00664551, None)

reports.append(Report(604021872, ("CSC", 1, 2, 2, 14), "MEp22_14"))
reports[-1].posNum = 53236
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0057241, 0.0048013, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0155274, 0.175024, 0), \
                           ValErr(-0.00189715, 0.00194393, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.35865e-05, 5.12018e-05, 0), \
                           -76204.6, 53236, 53236, -nan)
reports[-1].sigmaresid = ValErr(1.01259, 0.00310324, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00715902, None, 1.73094e-05, None, -0.00482436, None, -4.73681e-06, None, -0.00482436, None, -4.73681e-06, None, -0.00505577, None, 9.8484e-06, None, -0.00505577, None, 9.8484e-06, None, 1.0126, None, 0.00649746, None, 1.0126, None, 0.00649746, None)

reports.append(Report(604021888, ("CSC", 1, 2, 2, 16), "MEp22_16"))
reports[-1].posNum = 45112
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00764378, 0.00520848, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0359686, 0.193841, 0), \
                           ValErr(-0.00110472, 0.00206726, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.27244e-06, 5.38321e-05, 0), \
                           -63793.3, 45112, 45112, -nan)
reports[-1].sigmaresid = ValErr(0.995182, 0.00331315, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00984591, None, -1.89319e-05, None, 0.00735584, None, -3.33865e-05, None, 0.00735584, None, -3.33865e-05, None, -0.000819072, None, 1.24563e-05, None, -0.000819072, None, 1.24563e-05, None, 0.995187, None, 0.00660676, None, 0.995187, None, 0.00660676, None)

reports.append(Report(604021904, ("CSC", 1, 2, 2, 18), "MEp22_18"))
reports[-1].posNum = 48106
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0106326, 0.00501175, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.106442, 0.0947876, 0), \
                           ValErr(-0.00188707, 0.00103909, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.64223e-05, 5.29185e-05, 0), \
                           -68905.2, 48106, 48106, -nan)
reports[-1].sigmaresid = ValErr(1.01351, 0.00319005, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00310267, None, -2.98995e-06, None, 0.00796107, None, -5.25223e-05, None, 0.00796107, None, -5.25223e-05, None, 0.00959872, None, -1.98153e-05, None, 0.00959872, None, -1.98153e-05, None, 1.01355, None, 0.00701569, None, 1.01355, None, 0.00701569, None)

reports.append(Report(604021920, ("CSC", 1, 2, 2, 20), "MEp22_20"))
reports[-1].posNum = 49286
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0155904, 0.00497204, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.124028, 0.18145, 0), \
                           ValErr(-0.00169665, 0.00198549, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.37352e-05, 5.23643e-05, 0), \
                           -70208.7, 49286, 49286, -nan)
reports[-1].sigmaresid = ValErr(1.00559, 0.00320292, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0145197, None, -5.58562e-05, None, 0.0128162, None, -6.91136e-05, None, 0.0128162, None, -6.91136e-05, None, 0.0222875, None, -3.84739e-05, None, 0.0222875, None, -3.84739e-05, None, 1.00562, None, 0.00662478, None, 1.00562, None, 0.00662478, None)

reports.append(Report(604021936, ("CSC", 1, 2, 2, 22), "MEp22_22"))
reports[-1].posNum = 45602
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00138885, 0.00517753, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0802645, 0.189998, 0), \
                           ValErr(-0.00120098, 0.00204167, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.283e-05, 5.36717e-05, 0), \
                           -64467.2, 45602, 45602, -nan)
reports[-1].sigmaresid = ValErr(0.994768, 0.00329393, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00210443, None, 1.52734e-05, None, -0.000507577, None, 2.02753e-05, None, -0.000507577, None, 2.02753e-05, None, -0.00779458, None, 3.25786e-05, None, -0.00779458, None, 3.25786e-05, None, 0.994779, None, 0.00683896, None, 0.994779, None, 0.00683896, None)

reports.append(Report(604021952, ("CSC", 1, 2, 2, 24), "MEp22_24"))
reports[-1].posNum = 53100
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0133195, 0.00479556, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.187147, 0.134422, 0), \
                           ValErr(0.00105642, 0.00166669, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.30175e-05, 5.10962e-05, 0), \
                           -75915.9, 53100, 53100, -nan)
reports[-1].sigmaresid = ValErr(1.0108, 0.00308667, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00766209, None, -2.71173e-05, None, 0.00970689, None, -4.55342e-05, None, 0.00970689, None, -4.55342e-05, None, 0.0106674, None, -3.07453e-07, None, 0.0106674, None, -3.07453e-07, None, 1.01084, None, 0.0071887, None, 1.01084, None, 0.0071887, None)

reports.append(Report(604021968, ("CSC", 1, 2, 2, 26), "MEp22_26"))
reports[-1].posNum = 44078
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0125465, 0.00523133, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0057721, 0.188582, 0), \
                           ValErr(-0.00137935, 0.00202199, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000109738, 5.33507e-05, 0), \
                           -61901.6, 44078, 44078, -nan)
reports[-1].sigmaresid = ValErr(0.985532, 0.00331928, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000929401, None, 1.54632e-05, None, -0.00784213, None, -1.97685e-05, None, -0.00784213, None, -1.97685e-05, None, -0.0143248, None, -2.03049e-05, None, -0.0143248, None, -2.03049e-05, None, 0.985585, None, 0.00676837, None, 0.985585, None, 0.00676837, None)

reports.append(Report(604021984, ("CSC", 1, 2, 2, 28), "MEp22_28"))
reports[-1].posNum = 54390
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0122274, 0.00475946, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.12268, 0.17338, 0), \
                           ValErr(0.00410649, 0.00193794, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(9.91679e-05, 5.10953e-05, 0), \
                           -77675.8, 54390, 54390, -nan)
reports[-1].sigmaresid = ValErr(1.00923, 0.00305994, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00608847, None, -1.83517e-05, None, -0.00837244, None, -2.89549e-05, None, -0.00837244, None, -2.89549e-05, None, -0.00550115, None, -4.22104e-05, None, -0.00550115, None, -4.22104e-05, None, 1.00931, None, 0.00694012, None, 1.00931, None, 0.00694012, None)

reports.append(Report(604022000, ("CSC", 1, 2, 2, 30), "MEp22_30"))
reports[-1].posNum = 43218
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0137657, 0.00524089, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.412479, 0.188977, 0), \
                           ValErr(0.000161384, 0.00202408, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.1748e-05, 5.38483e-05, 0), \
                           -60523.8, 43218, 43218, -nan)
reports[-1].sigmaresid = ValErr(0.981659, 0.00333897, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0154147, None, 2.18399e-06, None, -0.011302, None, -5.44943e-07, None, -0.011302, None, -5.44943e-07, None, -0.0145107, None, 2.43698e-05, None, -0.0145107, None, 2.43698e-05, None, 0.981732, None, 0.00667416, None, 0.981732, None, 0.00667416, None)

reports.append(Report(604022016, ("CSC", 1, 2, 2, 32), "MEp22_32"))
reports[-1].posNum = 52868
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00657198, 0.0048134, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.332755, 0.175987, 0), \
                           ValErr(1.54435e-05, 0.00194189, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(9.82615e-06, 5.11666e-05, 0), \
                           -75652.6, 52868, 52868, -nan)
reports[-1].sigmaresid = ValErr(1.01211, 0.00311254, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00464947, None, -7.83325e-06, None, 0.00702363, None, -1.84902e-06, None, 0.00702363, None, -1.84902e-06, None, -0.00273219, None, 4.92795e-05, None, -0.00273219, None, 4.92795e-05, None, 1.01214, None, 0.00667057, None, 1.01214, None, 0.00667057, None)

reports.append(Report(604022032, ("CSC", 1, 2, 2, 34), "MEp22_34"))
reports[-1].posNum = 46467
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00793918, 0.00499768, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.180608, 0.107643, 0), \
                           ValErr(0.000821639, 0.00201762, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.01923e-05, 5.23708e-05, 0), \
                           -65820.1, 46467, 46467, -nan)
reports[-1].sigmaresid = ValErr(0.997556, 0.00321026, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0130945, None, -3.61569e-05, None, 0.0100868, None, -2.14576e-05, None, 0.0100868, None, -2.14576e-05, None, 0.0161368, None, -1.52448e-05, None, 0.0161368, None, -1.52448e-05, None, 0.997578, None, 0.00646018, None, 0.997578, None, 0.00646018, None)

reports.append(Report(604022048, ("CSC", 1, 2, 2, 36), "MEp22_36"))
reports[-1].posNum = 49918
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0071081, 0.00493198, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0292098, 0.178401, 0), \
                           ValErr(0.00118034, 0.00196641, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.13231e-05, 5.21025e-05, 0), \
                           -71055.8, 49918, 49918, -nan)
reports[-1].sigmaresid = ValErr(1.00452, 0.00317919, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00483893, None, 2.10769e-05, None, -0.00953075, None, 1.98089e-05, None, -0.00953075, None, 1.98089e-05, None, -0.0122873, None, 6.92669e-05, None, -0.0122873, None, 6.92669e-05, None, 1.00454, None, 0.00684627, None, 1.00454, None, 0.00684627, None)

reports.append(Report(604025352, ("CSC", 1, 3, 1, 1), "MEp31_01"))
reports[-1].posNum = 168385
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00207065, 0.00122756, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0285113, 0.0501279, 0), \
                           ValErr(-0.000877828, 0.0011253, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.03572e-05, 2.80442e-05, 0), \
                           -122468, 168385, 168385, -nan)
reports[-1].sigmaresid = ValErr(0.500759, 0.000862902, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000882514, None, 1.73651e-05, None, 0.00202314, None, 6.25652e-05, None, 0.00202314, None, 6.25652e-05, None, -0.00194362, None, 2.46922e-05, None, -0.00194362, None, 2.46922e-05, None, 0.50076, None, 0.00635056, None, 0.50076, None, 0.00635056, None)

reports.append(Report(604025368, ("CSC", 1, 3, 1, 3), "MEp31_03"))
reports[-1].posNum = 168876
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00164444, 0.0012269, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0078275, 0.0501619, 0), \
                           ValErr(0.000842853, 0.00112097, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.28559e-06, 2.79395e-05, 0), \
                           -122915, 168876, 168876, -nan)
reports[-1].sigmaresid = ValErr(0.501027, 0.000862109, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00189374, None, -9.00488e-06, None, 0.00165477, None, 6.91708e-06, None, 0.00165477, None, 6.91708e-06, None, -3.75858e-05, None, -9.06713e-06, None, -3.75858e-05, None, -9.06713e-06, None, 0.501028, None, 0.00659822, None, 0.501028, None, 0.00659822, None)

reports.append(Report(604025384, ("CSC", 1, 3, 1, 5), "MEp31_05"))
reports[-1].posNum = 168851
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000197061, 0.00122152, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0461656, 0.0498692, 0), \
                           ValErr(-0.00187722, 0.00111442, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.19975e-05, 2.78334e-05, 0), \
                           -122160, 168851, 168851, -nan)
reports[-1].sigmaresid = ValErr(0.498844, 0.000858416, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00130919, None, -1.62322e-05, None, 0.000143231, None, -1.17682e-06, None, 0.000143231, None, -1.17682e-06, None, 0.000295156, None, -7.81553e-06, None, 0.000295156, None, -7.81553e-06, None, 0.498849, None, 0.00597775, None, 0.498849, None, 0.00597775, None)

reports.append(Report(604025400, ("CSC", 1, 3, 1, 7), "MEp31_07"))
reports[-1].posNum = 168712
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00131065, 0.00122548, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0542254, 0.0502065, 0), \
                           ValErr(-0.00131336, 0.00112317, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.45318e-05, 2.79253e-05, 0), \
                           -122601, 168712, 168712, -nan)
reports[-1].sigmaresid = ValErr(0.500449, 0.000861533, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000705042, None, -6.65959e-06, None, 0.00123898, None, -8.82286e-06, None, 0.00123898, None, -8.82286e-06, None, 0.000568834, None, -9.73209e-06, None, 0.000568834, None, -9.73209e-06, None, 0.500454, None, 0.00616435, None, 0.500454, None, 0.00616435, None)

reports.append(Report(604025416, ("CSC", 1, 3, 1, 9), "MEp31_09"))
reports[-1].posNum = 168044
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000859289, 0.00121687, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0045074, 0.0497883, 0), \
                           ValErr(-0.00176414, 0.00111193, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.06156e-06, 2.77354e-05, 0), \
                           -120583, 168044, 168044, -nan)
reports[-1].sigmaresid = ValErr(0.495907, 0.000855408, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00145338, None, 6.89356e-06, None, 0.000839588, None, 1.49038e-05, None, 0.000839588, None, 1.49038e-05, None, -0.00103402, None, -2.07929e-05, None, -0.00103402, None, -2.07929e-05, None, 0.495911, None, 0.00612805, None, 0.495911, None, 0.00612805, None)

reports.append(Report(604025432, ("CSC", 1, 3, 1, 11), "MEp31_11"))
reports[-1].posNum = 167735
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00144411, 0.00122046, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0604711, 0.0499835, 0), \
                           ValErr(-0.00158097, 0.0011179, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(9.6779e-06, 2.7829e-05, 0), \
                           -120688, 167735, 167735, -nan)
reports[-1].sigmaresid = ValErr(0.496872, 0.000857864, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00178388, None, -7.80542e-06, None, -0.00139446, None, -7.14094e-06, None, -0.00139446, None, -7.14094e-06, None, -2.96892e-05, None, -8.5427e-06, None, -2.96892e-05, None, -8.5427e-06, None, 0.496876, None, 0.00605416, None, 0.496876, None, 0.00605416, None)

reports.append(Report(604025448, ("CSC", 1, 3, 1, 13), "MEp31_13"))
reports[-1].posNum = 167363
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000666072, 0.0012224, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0188823, 0.0499921, 0), \
                           ValErr(0.00156138, 0.00111585, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.64557e-05, 2.78619e-05, 0), \
                           -120503, 167363, 167363, -nan)
reports[-1].sigmaresid = ValErr(0.497119, 0.000859242, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-7.17832e-05, None, -2.01445e-05, None, 0.000533661, None, -2.15029e-05, None, 0.000533661, None, -2.15029e-05, None, 0.00223773, None, -5.27394e-06, None, 0.00223773, None, -5.27394e-06, None, 0.497123, None, 0.00588198, None, 0.497123, None, 0.00588198, None)

reports.append(Report(604025464, ("CSC", 1, 3, 1, 15), "MEp31_15"))
reports[-1].posNum = 166884
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0024247, 0.00122552, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0171475, 0.0502321, 0), \
                           ValErr(0.000204644, 0.00112446, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.1362e-05, 2.79602e-05, 0), \
                           -120400, 166884, 166884, -nan)
reports[-1].sigmaresid = ValErr(0.497839, 0.000861721, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00302156, None, 1.29259e-05, None, 0.00261775, None, -5.89306e-07, None, 0.00261775, None, -5.89306e-07, None, 0.00429488, None, -7.52718e-06, None, 0.00429488, None, -7.52718e-06, None, 0.497842, None, 0.00593717, None, 0.497842, None, 0.00593717, None)

reports.append(Report(604025480, ("CSC", 1, 3, 1, 17), "MEp31_17"))
reports[-1].posNum = 167510
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0010081, 0.00123267, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0564456, 0.0504086, 0), \
                           ValErr(-0.00130836, 0.00112775, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.14416e-05, 2.81573e-05, 0), \
                           -122066, 167510, 167510, -nan)
reports[-1].sigmaresid = ValErr(0.501461, 0.000866367, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(4.48388e-05, None, -6.34627e-06, None, -0.000948693, None, -1.26423e-05, None, -0.000948693, None, -1.26423e-05, None, -0.00179532, None, -2.5509e-05, None, -0.00179532, None, -2.5509e-05, None, 0.501466, None, 0.00597512, None, 0.501466, None, 0.00597512, None)

reports.append(Report(604025360, ("CSC", 1, 3, 1, 2), "MEp31_02"))
reports[-1].posNum = 173126
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00192618, 0.00124192, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0359576, 0.0521927, 0), \
                           ValErr(-0.000623684, 0.00116689, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.48788e-05, 2.83134e-05, 0), \
                           -130259, 173126, 173126, -nan)
reports[-1].sigmaresid = ValErr(0.513481, 0.000872627, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00141273, None, -1.18216e-05, None, -0.00170823, None, -1.10642e-05, None, -0.00170823, None, -1.10642e-05, None, -0.00437176, None, -1.37382e-05, None, -0.00437176, None, -1.37382e-05, None, 0.513486, None, 0.00583084, None, 0.513486, None, 0.00583084, None)

reports.append(Report(604025376, ("CSC", 1, 3, 1, 4), "MEp31_04"))
reports[-1].posNum = 173048
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00199649, 0.00124581, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0288028, 0.0524355, 0), \
                           ValErr(0.00078029, 0.0011693, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.24185e-05, 2.84037e-05, 0), \
                           -130780, 173048, 173048, -nan)
reports[-1].sigmaresid = ValErr(0.515204, 0.000875753, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000417428, None, -7.6138e-06, None, -0.00189175, None, -8.8082e-07, None, -0.00189175, None, -8.8082e-07, None, -0.000476251, None, 1.11178e-05, None, -0.000476251, None, 1.11178e-05, None, 0.515206, None, 0.00572539, None, 0.515206, None, 0.00572539, None)

reports.append(Report(604025392, ("CSC", 1, 3, 1, 6), "MEp31_06"))
reports[-1].posNum = 172132
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000246772, 0.00125295, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00694261, 0.0525661, 0), \
                           ValErr(-0.00186656, 0.00117447, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.89513e-06, 2.85848e-05, 0), \
                           -130633, 172132, 172132, -nan)
reports[-1].sigmaresid = ValErr(0.516837, 0.000880863, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000524341, None, 6.12942e-06, None, -0.000282228, None, 1.35046e-05, None, -0.000282228, None, 1.35046e-05, None, 0.000962366, None, 8.51833e-06, None, 0.000962366, None, 8.51833e-06, None, 0.516841, None, 0.00583331, None, 0.516841, None, 0.00583331, None)

reports.append(Report(604025408, ("CSC", 1, 3, 1, 8), "MEp31_08"))
reports[-1].posNum = 171624
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0005304, 0.00125351, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0225687, 0.0526089, 0), \
                           ValErr(0.000789348, 0.0011765, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.30204e-05, 2.86495e-05, 0), \
                           -130174, 171624, 171624, -nan)
reports[-1].sigmaresid = ValErr(0.516618, 0.000881791, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00131274, None, -1.17456e-06, None, 0.000476673, None, 1.82802e-05, None, 0.000476673, None, 1.82802e-05, None, 0.00153662, None, 1.09056e-05, None, 0.00153662, None, 1.09056e-05, None, 0.516619, None, 0.00590447, None, 0.516619, None, 0.00590447, None)

reports.append(Report(604025424, ("CSC", 1, 3, 1, 10), "MEp31_10"))
reports[-1].posNum = 172412
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(9.03958e-05, 0.00125522, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0645837, 0.0528313, 0), \
                           ValErr(0.0013716, 0.00118216, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.06196e-05, 2.87027e-05, 0), \
                           -131411, 172412, 172412, -nan)
reports[-1].sigmaresid = ValErr(0.518534, 0.000883032, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000591718, None, -1.22119e-05, None, 0.000136536, None, -2.15891e-05, None, 0.000136536, None, -2.15891e-05, None, -0.00233906, None, -3.18322e-05, None, -0.00233906, None, -3.18322e-05, None, 0.518541, None, 0.0058826, None, 0.518541, None, 0.0058826, None)

reports.append(Report(604025440, ("CSC", 1, 3, 1, 12), "MEp31_12"))
reports[-1].posNum = 171853
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000707784, 0.00125722, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0578145, 0.0527064, 0), \
                           ValErr(0.00143838, 0.00117815, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.41787e-07, 2.87285e-05, 0), \
                           -130808, 171853, 171853, -nan)
reports[-1].sigmaresid = ValErr(0.518, 0.000883558, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00231267, None, -6.03165e-06, None, 0.000716507, None, 3.48143e-08, None, 0.000716507, None, 3.48143e-08, None, -0.00146901, None, -4.87507e-06, None, -0.00146901, None, -4.87507e-06, None, 0.518007, None, 0.00571895, None, 0.518007, None, 0.00571895, None)

reports.append(Report(604025456, ("CSC", 1, 3, 1, 14), "MEp31_14"))
reports[-1].posNum = 173175
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000971241, 0.00125101, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.052159, 0.0525136, 0), \
                           ValErr(-0.000909884, 0.00117333, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.87752e-05, 2.85788e-05, 0), \
                           -131723, 173175, 173175, -nan)
reports[-1].sigmaresid = ValErr(0.51773, 0.000879723, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(2.68183e-05, None, -9.82549e-06, None, -0.000880996, None, -1.80522e-05, None, -0.000880996, None, -1.80522e-05, None, -0.00140025, None, -1.94656e-05, None, -0.00140025, None, -1.94656e-05, None, 0.517734, None, 0.00589949, None, 0.517734, None, 0.00589949, None)

reports.append(Report(604025472, ("CSC", 1, 3, 1, 16), "MEp31_16"))
reports[-1].posNum = 172255
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000781699, 0.00125518, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.00189468, 0.0527527, 0), \
                           ValErr(1.01785e-05, 0.0011783, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.41233e-05, 2.86629e-05, 0), \
                           -131139, 172255, 172255, -nan)
reports[-1].sigmaresid = ValErr(0.518077, 0.000882661, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000879166, None, 9.22661e-06, None, 0.000846147, None, 2.31841e-05, None, 0.000846147, None, 2.31841e-05, None, 0.00200649, None, 3.57838e-05, None, 0.00200649, None, 3.57838e-05, None, 0.518078, None, 0.00577052, None, 0.518078, None, 0.00577052, None)

reports.append(Report(604025488, ("CSC", 1, 3, 1, 18), "MEp31_18"))
reports[-1].posNum = 172486
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00123162, 0.00125339, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0667543, 0.0525357, 0), \
                           ValErr(0.000757449, 0.0011799, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.4139e-05, 2.86609e-05, 0), \
                           -131076, 172486, 172486, -nan)
reports[-1].sigmaresid = ValErr(0.517361, 0.000880851, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00195279, None, -1.23001e-06, None, 0.00101623, None, -8.54772e-07, None, 0.00101623, None, -8.54772e-07, None, 0.000457787, None, 4.02276e-06, None, 0.000457787, None, 4.02276e-06, None, 0.517368, None, 0.00569082, None, 0.517368, None, 0.00569082, None)

reports.append(Report(604025864, ("CSC", 1, 3, 2, 1), "MEp32_01"))
reports[-1].posNum = 57172
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00045411, 0.00478528, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.1293, 0.102615, 0), \
                           ValErr(-0.00164251, 0.00114446, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.71449e-05, 5.22011e-05, 0), \
                           -83762.5, 57172, 57172, -nan)
reports[-1].sigmaresid = ValErr(1.04724, 0.00301791, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-6.30857e-05, None, 2.06173e-05, None, -0.00290685, None, 9.93555e-06, None, -0.00290685, None, 9.93555e-06, None, -0.00983099, None, -1.74315e-05, None, -0.00983099, None, -1.74315e-05, None, 1.04726, None, 0.00731759, None, 1.04726, None, 0.00731759, None)

reports.append(Report(604025880, ("CSC", 1, 3, 2, 3), "MEp32_03"))
reports[-1].posNum = 50000
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00993426, 0.00511755, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.125027, 0.211482, 0), \
                           ValErr(0.00242557, 0.00233495, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(8.63899e-05, 5.41545e-05, 0), \
                           -71384.3, 50000, 50000, -nan)
reports[-1].sigmaresid = ValErr(1.00878, 0.00319005, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00539264, None, -2.63563e-05, None, -0.00611339, None, -2.71152e-05, None, -0.00611339, None, -2.71152e-05, None, -0.000433256, None, 9.64104e-06, None, -0.000433256, None, 9.64104e-06, None, 1.00883, None, 0.00754797, None, 1.00883, None, 0.00754797, None)

reports.append(Report(604025896, ("CSC", 1, 3, 2, 5), "MEp32_05"))
reports[-1].posNum = 57422
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00135483, 0.00474984, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.00172061, 0.201715, 0), \
                           ValErr(0.00529936, 0.00228007, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.82e-05, 5.17417e-05, 0), \
                           -83727.9, 57422, 57422, -nan)
reports[-1].sigmaresid = ValErr(1.03995, 0.00306873, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0040924, None, 5.17561e-06, None, 0.000605105, None, 2.84323e-06, None, 0.000605105, None, 2.84323e-06, None, 0.00260567, None, 9.59882e-06, None, 0.00260567, None, 9.59882e-06, None, 1.04001, None, 0.00758689, None, 1.04001, None, 0.00758689, None)

reports.append(Report(604025912, ("CSC", 1, 3, 2, 7), "MEp32_07"))
reports[-1].posNum = 50277
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00762691, 0.00514411, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0743637, 0.211021, 0), \
                           ValErr(0.00147724, 0.00235618, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(9.31164e-05, 5.4717e-05, 0), \
                           -72414.6, 50277, 50277, -nan)
reports[-1].sigmaresid = ValErr(1.0216, 0.00322168, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00350129, None, 2.67317e-06, None, -0.00363795, None, -6.87772e-06, None, -0.00363795, None, -6.87772e-06, None, -0.00443986, None, -3.51368e-05, None, -0.00443986, None, -3.51368e-05, None, 1.02164, None, 0.00726996, None, 1.02164, None, 0.00726996, None)

reports.append(Report(604025928, ("CSC", 1, 3, 2, 9), "MEp32_09"))
reports[-1].posNum = 52766
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0167496, 0.00494446, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0512346, 0.15531, 0), \
                           ValErr(-9.19341e-05, 0.00203399, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000111666, 5.28297e-05, 0), \
                           -76622.1, 52766, 52766, -nan)
reports[-1].sigmaresid = ValErr(1.03373, 0.0031778, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0108291, None, 1.5538e-05, None, 0.0124621, None, 1.35913e-05, None, 0.0124621, None, 1.35913e-05, None, 0.0201566, None, 6.54974e-05, None, 0.0201566, None, 6.54974e-05, None, 1.03377, None, 0.00780725, None, 1.03377, None, 0.00780725, None)

reports.append(Report(604025944, ("CSC", 1, 3, 2, 11), "MEp32_11"))
reports[-1].posNum = 52688
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00682015, 0.00497115, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.264503, 0.210952, 0), \
                           ValErr(-0.000799463, 0.0023299, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.94455e-06, 5.30721e-05, 0), \
                           -76268.5, 52688, 52688, -nan)
reports[-1].sigmaresid = ValErr(1.02902, 0.00316996, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0123418, None, -5.23924e-05, None, -0.00653109, None, -2.08738e-05, None, -0.00653109, None, -2.08738e-05, None, -0.00393543, None, -6.58489e-07, None, -0.00393543, None, -6.58489e-07, None, 1.02904, None, 0.00779927, None, 1.02904, None, 0.00779927, None)

reports.append(Report(604025960, ("CSC", 1, 3, 2, 13), "MEp32_13"))
reports[-1].posNum = 49807
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0100748, 0.00515266, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0361681, 0.211117, 0), \
                           ValErr(0.00326822, 0.00235256, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.68978e-05, 5.43967e-05, 0), \
                           -71249, 49807, 49807, -nan)
reports[-1].sigmaresid = ValErr(1.01163, 0.00320525, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00919964, None, 7.62442e-06, None, 0.00939416, None, -1.90811e-06, None, 0.00939416, None, -1.90811e-06, None, 0.0103217, None, -1.99987e-05, None, 0.0103217, None, -1.99987e-05, None, 1.01165, None, 0.00751357, None, 1.01165, None, 0.00751357, None)

reports.append(Report(604025976, ("CSC", 1, 3, 2, 15), "MEp32_15"))
reports[-1].posNum = 57504
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000136803, 0.00471525, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.274129, 0.199171, 0), \
                           ValErr(-0.000961162, 0.00225495, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.59954e-05, 5.1514e-05, 0), \
                           -83798.1, 57504, 57504, -nan)
reports[-1].sigmaresid = ValErr(1.03906, 0.00306393, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00114327, None, 2.33699e-05, None, -0.00041871, None, 1.89356e-05, None, -0.00041871, None, 1.89356e-05, None, 0.00611679, None, -1.55259e-05, None, 0.00611679, None, -1.55259e-05, None, 1.03908, None, 0.00736385, None, 1.03908, None, 0.00736385, None)

reports.append(Report(604025992, ("CSC", 1, 3, 2, 17), "MEp32_17"))
reports[-1].posNum = 50128
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000884564, 0.00513363, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.271769, 0.213041, 0), \
                           ValErr(-0.000993164, 0.00234485, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(7.5089e-05, 5.41323e-05, 0), \
                           -71564.3, 50128, 50128, -nan)
reports[-1].sigmaresid = ValErr(1.00873, 0.00318581, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000274461, None, 1.37473e-05, None, 0.00256625, None, 9.01707e-06, None, 0.00256625, None, 9.01707e-06, None, 0.00719547, None, 1.48405e-05, None, 0.00719547, None, 1.48405e-05, None, 1.00877, None, 0.00748352, None, 1.00877, None, 0.00748352, None)

reports.append(Report(604026008, ("CSC", 1, 3, 2, 19), "MEp32_19"))
reports[-1].posNum = 57718
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0016739, 0.00475697, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.047893, 0.197918, 0), \
                           ValErr(-0.000818612, 0.00225054, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.10707e-07, 5.1908e-05, 0), \
                           -84196.1, 57718, 57718, -nan)
reports[-1].sigmaresid = ValErr(1.04062, 0.00306282, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00290968, None, 2.24054e-05, None, 0.00168771, None, 1.9049e-05, None, 0.00168771, None, 1.9049e-05, None, 0.000612015, None, 3.96509e-05, None, 0.000612015, None, 3.96509e-05, None, 1.04062, None, 0.00832988, None, 1.04062, None, 0.00832988, None)

reports.append(Report(604026024, ("CSC", 1, 3, 2, 21), "MEp32_21"))
reports[-1].posNum = 50388
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00443063, 0.00508678, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.149019, 0.210626, 0), \
                           ValErr(0.00113354, 0.00229916, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.62744e-05, 5.3319e-05, 0), \
                           -71908.1, 50388, 50388, -nan)
reports[-1].sigmaresid = ValErr(1.00818, 0.00317585, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00224005, None, -1.05127e-05, None, -0.00278372, None, -7.86002e-05, None, -0.00278372, None, -7.86002e-05, None, -0.00545431, None, -6.38751e-05, None, -0.00545431, None, -6.38751e-05, None, 1.00819, None, 0.00785227, None, 1.00819, None, 0.00785227, None)

reports.append(Report(604026040, ("CSC", 1, 3, 2, 23), "MEp32_23"))
reports[-1].posNum = 56929
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0130049, 0.00477735, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0128668, 0.185147, 0), \
                           ValErr(-0.00181221, 0.00156497, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.60269e-05, 5.19221e-05, 0), \
                           -83059.7, 56929, 56929, -nan)
reports[-1].sigmaresid = ValErr(1.04088, 0.00306203, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0125353, None, 1.37926e-05, None, 0.0105371, None, 4.05703e-06, None, 0.0105371, None, 4.05703e-06, None, 0.0101112, None, -1.33749e-05, None, 0.0101112, None, -1.33749e-05, None, 1.0409, None, 0.00730334, None, 1.0409, None, 0.00730334, None)

reports.append(Report(604026056, ("CSC", 1, 3, 2, 25), "MEp32_25"))
reports[-1].posNum = 50882
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00873876, 0.00511837, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.3682, 0.210278, 0), \
                           ValErr(0.00298379, 0.00234155, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.11542e-05, 5.43638e-05, 0), \
                           -73605.7, 50882, 50882, -nan)
reports[-1].sigmaresid = ValErr(1.02804, 0.00322267, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00477252, None, 2.092e-05, None, 0.00944009, None, 5.80862e-05, None, 0.00944009, None, 5.80862e-05, None, 0.00866673, None, 4.07627e-05, None, 0.00866673, None, 4.07627e-05, None, 1.02809, None, 0.00782831, None, 1.02809, None, 0.00782831, None)

reports.append(Report(604026072, ("CSC", 1, 3, 2, 27), "MEp32_27"))
reports[-1].posNum = 52936
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00232861, 0.00497972, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.140203, 0.209668, 0), \
                           ValErr(0.00200587, 0.00234518, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.07228e-05, 5.35384e-05, 0), \
                           -77056.2, 52936, 52936, -nan)
reports[-1].sigmaresid = ValErr(1.03739, 0.00318826, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00346516, None, 5.9152e-05, None, -0.00323718, None, 1.61684e-05, None, -0.00323718, None, 1.61684e-05, None, -0.00939227, None, 2.25491e-05, None, -0.00939227, None, 2.25491e-05, None, 1.03741, None, 0.00821212, None, 1.03741, None, 0.00821212, None)

reports.append(Report(604026088, ("CSC", 1, 3, 2, 29), "MEp32_29"))
reports[-1].posNum = 53716
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00606442, 0.00494671, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.241884, 0.208597, 0), \
                           ValErr(-0.000210275, 0.00232543, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.13608e-07, 5.31027e-05, 0), \
                           -78082.8, 53716, 53716, -nan)
reports[-1].sigmaresid = ValErr(1.03529, 0.00315861, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00573215, None, 1.32253e-05, None, 0.00583201, None, 1.0319e-05, None, 0.00583201, None, 1.0319e-05, None, 0.00757165, None, 5.72079e-05, None, 0.00757165, None, 5.72079e-05, None, 1.03531, None, 0.00831257, None, 1.03531, None, 0.00831257, None)

reports.append(Report(604026104, ("CSC", 1, 3, 2, 31), "MEp32_31"))
reports[-1].posNum = 50964
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00199181, 0.00512991, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.168411, 0.210495, 0), \
                           ValErr(0.00225544, 0.00235958, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.77767e-05, 5.46095e-05, 0), \
                           -73586.5, 50964, 50964, -nan)
reports[-1].sigmaresid = ValErr(1.02527, 0.00321138, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00229911, None, 3.67701e-05, None, 0.00426371, None, 3.80533e-05, None, 0.00426371, None, 3.80533e-05, None, 0.00800649, None, 4.48554e-05, None, 0.00800649, None, 4.48554e-05, None, 1.02529, None, 0.00762823, None, 1.02529, None, 0.00762823, None)

reports.append(Report(604026120, ("CSC", 1, 3, 2, 33), "MEp32_33"))
reports[-1].posNum = 56831
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0062671, 0.00472429, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0596813, 0.199018, 0), \
                           ValErr(0.00312862, 0.00226447, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.97973e-05, 5.14835e-05, 0), \
                           -82448.1, 56831, 56831, -nan)
reports[-1].sigmaresid = ValErr(1.03233, 0.00306205, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00287983, None, 1.96166e-05, None, 0.0029529, None, 1.92546e-05, None, 0.0029529, None, 1.92546e-05, None, -0.00301529, None, -1.65704e-05, None, -0.00301529, None, -1.65704e-05, None, 1.03238, None, 0.00768728, None, 1.03238, None, 0.00768728, None)

reports.append(Report(604026136, ("CSC", 1, 3, 2, 35), "MEp32_35"))
reports[-1].posNum = 49291
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00324531, 0.00512866, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.221325, 0.212068, 0), \
                           ValErr(-0.00113901, 0.00233782, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.54563e-05, 5.37565e-05, 0), \
                           -69501.5, 49291, 49291, -nan)
reports[-1].sigmaresid = ValErr(0.991121, 0.00315664, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00711566, None, -1.31291e-05, None, -0.00202902, None, -1.21542e-05, None, -0.00202902, None, -1.21542e-05, None, 0.00227084, None, -2.02212e-05, None, 0.00227084, None, -2.02212e-05, None, 0.99114, None, 0.00703349, None, 0.99114, None, 0.00703349, None)

reports.append(Report(604025872, ("CSC", 1, 3, 2, 2), "MEp32_02"))
reports[-1].posNum = 54849
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00623798, 0.0047675, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.200585, 0.159179, 0), \
                           ValErr(0.00063321, 0.0023199, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.793e-05, 5.22897e-05, 0), \
                           -79861.2, 54849, 54849, -nan)
reports[-1].sigmaresid = ValErr(1.03778, 0.00310029, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00300881, None, -8.9354e-06, None, -0.00354399, None, -1.98428e-05, None, -0.00354399, None, -1.98428e-05, None, 0.00134994, None, -2.74513e-05, None, 0.00134994, None, -2.74513e-05, None, 1.0378, None, 0.00743173, None, 1.0378, None, 0.00743173, None)

reports.append(Report(604025888, ("CSC", 1, 3, 2, 4), "MEp32_04"))
reports[-1].posNum = 52865
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00385273, 0.00512546, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.252778, 0.221108, 0), \
                           ValErr(0.00450005, 0.00246085, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.82445e-05, 5.4661e-05, 0), \
                           -76951.2, 52865, 52865, -nan)
reports[-1].sigmaresid = ValErr(1.03736, 0.00319029, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00073807, None, 3.73434e-05, None, 0.00198665, None, 2.06325e-05, None, 0.00198665, None, 2.06325e-05, None, 0.0032715, None, 3.29515e-05, None, 0.0032715, None, 3.29515e-05, None, 1.03741, None, 0.00694699, None, 1.03741, None, 0.00694699, None)

reports.append(Report(604025904, ("CSC", 1, 3, 2, 6), "MEp32_06"))
reports[-1].posNum = 57846
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00592778, 0.00477365, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0278753, 0.207299, 0), \
                           ValErr(0.0028382, 0.00234545, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.54455e-05, 5.21513e-05, 0), \
                           -85043.8, 57846, 57846, -nan)
reports[-1].sigmaresid = ValErr(1.05257, 0.00309457, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0030284, None, -1.37147e-05, None, -0.00351922, None, -3.67435e-05, None, -0.00351922, None, -3.67435e-05, None, -0.003638, None, -3.65491e-05, None, -0.003638, None, -3.65491e-05, None, 1.0526, None, 0.00741093, None, 1.0526, None, 0.00741093, None)

reports.append(Report(604025920, ("CSC", 1, 3, 2, 8), "MEp32_08"))
reports[-1].posNum = 50592
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00271366, 0.00522181, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.10701, 0.221253, 0), \
                           ValErr(-0.000286853, 0.00246166, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.25022e-05, 5.54489e-05, 0), \
                           -72536.4, 50592, 50592, -nan)
reports[-1].sigmaresid = ValErr(1.01492, 0.00319062, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000482937, None, 4.03846e-06, None, -0.00118734, None, -3.94915e-05, None, -0.00118734, None, -3.94915e-05, None, 0.00254093, None, 1.89387e-05, None, 0.00254093, None, 1.89387e-05, None, 1.01493, None, 0.00805358, None, 1.01493, None, 0.00805358, None)

reports.append(Report(604025936, ("CSC", 1, 3, 2, 10), "MEp32_10"))
reports[-1].posNum = 59699
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00858627, 0.00472317, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.126925, 0.204984, 0), \
                           ValErr(0.0048047, 0.00233384, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.54729e-05, 5.17849e-05, 0), \
                           -88268, 59699, 59699, -nan)
reports[-1].sigmaresid = ValErr(1.06143, 0.00307179, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00813392, None, 8.25705e-06, None, 0.00741176, None, 4.89066e-05, None, 0.00741176, None, 4.89066e-05, None, 0.00766, None, 3.94877e-05, None, 0.00766, None, 3.94877e-05, None, 1.06147, None, 0.0101845, None, 1.06147, None, 0.0101845, None)

reports.append(Report(604025952, ("CSC", 1, 3, 2, 12), "MEp32_12"))
reports[-1].posNum = 51462
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00306136, 0.00517693, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.068494, 0.221487, 0), \
                           ValErr(0.0042649, 0.00246386, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.99048e-05, 5.51454e-05, 0), \
                           -74201.3, 51462, 51462, -nan)
reports[-1].sigmaresid = ValErr(1.02319, 0.00318934, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00518719, None, -3.85725e-05, None, 0.000190052, None, -1.12216e-05, None, 0.000190052, None, -1.12216e-05, None, -0.000335556, None, -1.24469e-05, None, -0.000335556, None, -1.24469e-05, None, 1.02324, None, 0.00794566, None, 1.02324, None, 0.00794566, None)

reports.append(Report(604025968, ("CSC", 1, 3, 2, 14), "MEp32_14"))
reports[-1].posNum = 58515
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0142771, 0.00478098, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.350183, 0.206278, 0), \
                           ValErr(-0.00373748, 0.00233294, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000132736, 5.2035e-05, 0), \
                           -86153, 58515, 58515, -nan)
reports[-1].sigmaresid = ValErr(1.05484, 0.00308345, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0080967, None, -3.53682e-06, None, 0.00926408, None, 2.08163e-05, None, 0.00926408, None, 2.08163e-05, None, 0.00883712, None, -6.19052e-06, None, 0.00883712, None, -6.19052e-06, None, 1.05494, None, 0.00748882, None, 1.05494, None, 0.00748882, None)

reports.append(Report(604025984, ("CSC", 1, 3, 2, 16), "MEp32_16"))
reports[-1].posNum = 52195
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00116528, 0.00510886, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.273085, 0.220653, 0), \
                           ValErr(-0.00191108, 0.00247183, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.50653e-05, 5.45657e-05, 0), \
                           -75317, 52195, 52195, -nan)
reports[-1].sigmaresid = ValErr(1.02434, 0.00317041, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000780815, None, 3.07397e-05, None, 0.000137479, None, 5.89861e-05, None, 0.000137479, None, 5.89861e-05, None, -0.000571063, None, 3.94702e-05, None, -0.000571063, None, 3.94702e-05, None, 1.02437, None, 0.00694172, None, 1.02437, None, 0.00694172, None)

reports.append(Report(604026000, ("CSC", 1, 3, 2, 18), "MEp32_18"))
reports[-1].posNum = 54405
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00712583, 0.00495846, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.193022, 0.213747, 0), \
                           ValErr(0.00185042, 0.00237185, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.32853e-05, 5.30738e-05, 0), \
                           -79415.9, 54405, 54405, -nan)
reports[-1].sigmaresid = ValErr(1.04162, 0.00315774, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00934338, None, 1.77073e-05, None, -0.00629627, None, 7.86519e-06, None, -0.00629627, None, 7.86519e-06, None, -0.0100698, None, 2.57862e-05, None, -0.0100698, None, 2.57862e-05, None, 1.04164, None, 0.008137, None, 1.04164, None, 0.008137, None)

reports.append(Report(604026016, ("CSC", 1, 3, 2, 20), "MEp32_20"))
reports[-1].posNum = 55754
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.017189, 0.00489222, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0467432, 0.208311, 0), \
                           ValErr(0.0020442, 0.00140102, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000140949, 5.28229e-05, 0), \
                           -81351.3, 55754, 55754, -nan)
reports[-1].sigmaresid = ValErr(1.04099, 0.00306976, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0116545, None, 9.22247e-06, None, -0.0115514, None, -1.12994e-05, None, -0.0115514, None, -1.12994e-05, None, -0.00740699, None, 3.67118e-05, None, -0.00740699, None, 3.67118e-05, None, 1.04107, None, 0.00704251, None, 1.04107, None, 0.00704251, None)

reports.append(Report(604026032, ("CSC", 1, 3, 2, 22), "MEp32_22"))
reports[-1].posNum = 52710
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00646553, 0.00508156, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0870398, 0.218663, 0), \
                           ValErr(-0.00117231, 0.00246771, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.29555e-05, 5.46292e-05, 0), \
                           -76295.7, 52710, 52710, -nan)
reports[-1].sigmaresid = ValErr(1.02893, 0.00316902, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00166487, None, -1.23848e-06, None, 0.00283467, None, -3.21581e-06, None, 0.00283467, None, -3.21581e-06, None, 0.00373786, None, -4.39628e-05, None, 0.00373786, None, -4.39628e-05, None, 1.02896, None, 0.00705074, None, 1.02896, None, 0.00705074, None)

reports.append(Report(604026048, ("CSC", 1, 3, 2, 24), "MEp32_24"))
reports[-1].posNum = 57847
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0114894, 0.00476062, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.147572, 0.125914, 0), \
                           ValErr(0.000899421, 0.00206419, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.42142e-05, 5.14154e-05, 0), \
                           -84665.3, 57847, 57847, -nan)
reports[-1].sigmaresid = ValErr(1.04569, 0.00283146, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00781755, None, 4.87543e-06, None, -0.0101561, None, 5.53817e-06, None, -0.0101561, None, 5.53817e-06, None, -0.00776026, None, -2.16038e-05, None, -0.00776026, None, -2.16038e-05, None, 1.04569, None, 0.00728314, None, 1.04569, None, 0.00728314, None)

reports.append(Report(604026064, ("CSC", 1, 3, 2, 26), "MEp32_26"))
reports[-1].posNum = 51823
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00103661, 0.0051464, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.513236, 0.218752, 0), \
                           ValErr(-0.00426852, 0.00244338, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.96315e-05, 5.4868e-05, 0), \
                           -74624.9, 51823, 51823, -nan)
reports[-1].sigmaresid = ValErr(1.02128, 0.00315539, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00561779, None, 8.21624e-06, None, -0.00281533, None, -1.83291e-05, None, -0.00281533, None, -1.83291e-05, None, -0.00206622, None, -1.18756e-05, None, -0.00206622, None, -1.18756e-05, None, 1.02137, None, 0.00720495, None, 1.02137, None, 0.00720495, None)

reports.append(Report(604026080, ("CSC", 1, 3, 2, 28), "MEp32_28"))
reports[-1].posNum = 59790
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000109013, 0.0047213, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.430301, 0.204308, 0), \
                           ValErr(0.000757128, 0.00231853, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.80535e-05, 5.15983e-05, 0), \
                           -88412.5, 59790, 59790, -nan)
reports[-1].sigmaresid = ValErr(1.0616, 0.00306997, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00304103, None, -2.11754e-05, None, -0.000559062, None, -4.99809e-06, None, -0.000559062, None, -4.99809e-06, None, 0.00563464, None, -2.02895e-05, None, 0.00563464, None, -2.02895e-05, None, 1.06164, None, 0.00856577, None, 1.06164, None, 0.00856577, None)

reports.append(Report(604026096, ("CSC", 1, 3, 2, 30), "MEp32_30"))
reports[-1].posNum = 50997
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00263006, 0.00512991, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.105983, 0.219281, 0), \
                           ValErr(0.00150458, 0.0024225, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.72018e-06, 5.42129e-05, 0), \
                           -72829.5, 50997, 50997, -nan)
reports[-1].sigmaresid = ValErr(1.00922, 0.00316008, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00720701, None, -3.49617e-06, None, 0.00266675, None, 3.00753e-05, None, 0.00266675, None, 3.00753e-05, None, -0.00164937, None, 7.89188e-06, None, -0.00164937, None, 7.89188e-06, None, 1.00922, None, 0.0073467, None, 1.00922, None, 0.0073467, None)

reports.append(Report(604026112, ("CSC", 1, 3, 2, 32), "MEp32_32"))
reports[-1].posNum = 58011
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00176009, 0.00477801, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.185987, 0.207041, 0), \
                           ValErr(0.0036487, 0.00234614, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.72245e-05, 5.21468e-05, 0), \
                           -85129.3, 58011, 58011, -nan)
reports[-1].sigmaresid = ValErr(1.04973, 0.00308181, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00622731, None, 1.65905e-05, None, 0.000681697, None, 3.54674e-06, None, 0.000681697, None, 3.54674e-06, None, 0.000327569, None, -6.60729e-06, None, 0.000327569, None, -6.60729e-06, None, 1.04977, None, 0.0074361, None, 1.04977, None, 0.0074361, None)

reports.append(Report(604026128, ("CSC", 1, 3, 2, 34), "MEp32_34"))
reports[-1].posNum = 53468
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00891433, 0.00510215, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.243599, 0.220526, 0), \
                           ValErr(0.00629162, 0.00249016, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.93531e-05, 5.47298e-05, 0), \
                           -77756.7, 53468, 53468, -nan)
reports[-1].sigmaresid = ValErr(1.03596, 0.00316795, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.014261, None, -7.94717e-05, None, -0.0116436, None, -6.25061e-05, None, -0.0116436, None, -6.25061e-05, None, -0.011603, None, -8.7381e-05, None, -0.011603, None, -8.7381e-05, None, 1.03603, None, 0.00714134, None, 1.03603, None, 0.00714134, None)

reports.append(Report(604026144, ("CSC", 1, 3, 2, 36), "MEp32_36"))
reports[-1].posNum = 56164
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00422112, 0.00484826, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00864064, 0.209931, 0), \
                           ValErr(0.000412259, 0.0023713, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.0449e-05, 5.24662e-05, 0), \
                           -81632.7, 56164, 56164, -nan)
reports[-1].sigmaresid = ValErr(1.03514, 0.00308854, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00609004, None, -2.2979e-05, None, 0.00542812, None, -5.74856e-05, None, 0.00542812, None, -5.74856e-05, None, 0.000745028, None, -9.0808e-05, None, 0.000745028, None, -9.0808e-05, None, 1.03514, None, 0.00748656, None, 1.03514, None, 0.00748656, None)

reports.append(Report(604029448, ("CSC", 1, 4, 1, 1), "MEp41_01"))
reports[-1].posNum = 135450
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00247453, 0.0015861, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.185553, 0.0680982, 0), \
                           ValErr(-0.000568263, 0.00174441, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.84127e-05, 4.15726e-05, 0), \
                           -119033, 135450, 135450, -nan)
reports[-1].sigmaresid = ValErr(0.582665, 0.00111947, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00132731, None, 2.72894e-06, None, 0.00251779, None, 3.78833e-06, None, 0.00251779, None, 3.78833e-06, None, 0.000740614, None, 3.97824e-05, None, 0.000740614, None, 3.97824e-05, None, 0.582682, None, 0.00602471, None, 0.582682, None, 0.00602471, None)

reports.append(Report(604029464, ("CSC", 1, 4, 1, 3), "MEp41_03"))
reports[-1].posNum = 135631
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00204428, 0.00159358, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.022988, 0.0685473, 0), \
                           ValErr(0.000878903, 0.00175207, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.5075e-05, 4.16056e-05, 0), \
                           -119921, 135631, 135631, -nan)
reports[-1].sigmaresid = ValErr(0.585807, 0.00112476, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00273726, None, -1.50547e-06, None, 0.00196921, None, 3.41711e-05, None, 0.00196921, None, 3.41711e-05, None, 0.00130781, None, 6.59281e-06, None, 0.00130781, None, 6.59281e-06, None, 0.58581, None, 0.00599863, None, 0.58581, None, 0.00599863, None)

reports.append(Report(604029480, ("CSC", 1, 4, 1, 5), "MEp41_05"))
reports[-1].posNum = 135940
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00082141, 0.00159329, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0641218, 0.0684665, 0), \
                           ValErr(-0.00359901, 0.00175219, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.30173e-06, 4.17196e-05, 0), \
                           -120315, 135940, 135940, -nan)
reports[-1].sigmaresid = ValErr(0.586327, 0.00112448, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000128583, None, -4.64882e-06, None, -0.000802149, None, 9.30655e-06, None, -0.000802149, None, 9.30655e-06, None, -0.00217642, None, 3.36519e-06, None, -0.00217642, None, 3.36519e-06, None, 0.586337, None, 0.00575515, None, 0.586337, None, 0.00575515, None)

reports.append(Report(604029496, ("CSC", 1, 4, 1, 7), "MEp41_07"))
reports[-1].posNum = 136341
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00138198, 0.00158567, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000298209, 0.0682856, 0), \
                           ValErr(-0.00105188, 0.00174529, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.75613e-05, 4.14647e-05, 0), \
                           -120205, 136341, 136341, -nan)
reports[-1].sigmaresid = ValErr(0.58433, 0.001119, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000686158, None, -2.74116e-07, None, -0.00122179, None, 3.89962e-06, None, -0.00122179, None, 3.89962e-06, None, 0.000184401, None, 1.98891e-05, None, 0.000184401, None, 1.98891e-05, None, 0.584337, None, 0.00590648, None, 0.584337, None, 0.00590648, None)

reports.append(Report(604029512, ("CSC", 1, 4, 1, 9), "MEp41_09"))
reports[-1].posNum = 135723
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000292335, 0.00158517, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0072393, 0.0681716, 0), \
                           ValErr(-0.00093224, 0.00174444, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.80282e-06, 4.14809e-05, 0), \
                           -119368, 135723, 135723, -nan)
reports[-1].sigmaresid = ValErr(0.583075, 0.00111914, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00114721, None, 7.68457e-06, None, -0.00027572, None, 8.47697e-05, None, -0.00027572, None, 8.47697e-05, None, -0.00393955, None, 3.72591e-05, None, -0.00393955, None, 3.72591e-05, None, 0.583075, None, 0.0145247, None, 0.583075, None, 0.0145247, None)

reports.append(Report(604029528, ("CSC", 1, 4, 1, 11), "MEp41_11"))
reports[-1].posNum = 136514
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00148612, 0.00157464, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0295307, 0.0677927, 0), \
                           ValErr(-9.49351e-05, 0.00173262, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(8.92729e-05, 4.1137e-05, 0), \
                           -119520, 136514, 136514, -nan)
reports[-1].sigmaresid = ValErr(0.580755, 0.00111145, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00202765, None, -2.4881e-06, None, -0.00128372, None, -1.26392e-05, None, -0.00128372, None, -1.26392e-05, None, -0.00211887, None, -1.7585e-05, None, -0.00211887, None, -1.7585e-05, None, 0.580766, None, 0.00586929, None, 0.580766, None, 0.00586929, None)

reports.append(Report(604029544, ("CSC", 1, 4, 1, 13), "MEp41_13"))
reports[-1].posNum = 135855
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00128974, 0.00157818, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0415855, 0.0680008, 0), \
                           ValErr(0.00116533, 0.00173868, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.21931e-05, 4.1288e-05, 0), \
                           -118908, 135855, 135855, -nan)
reports[-1].sigmaresid = ValErr(0.580606, 0.00111386, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(6.88831e-05, None, 2.67085e-06, None, 0.00123446, None, 1.52406e-05, None, 0.00123446, None, 1.52406e-05, None, 0.000712939, None, -5.133e-06, None, 0.000712939, None, -5.133e-06, None, 0.580608, None, 0.00585715, None, 0.580608, None, 0.00585715, None)

reports.append(Report(604029560, ("CSC", 1, 4, 1, 15), "MEp41_15"))
reports[-1].posNum = 114454
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00106779, 0.00174547, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.00970169, 0.0732941, 0), \
                           ValErr(-0.000573783, 0.00188071, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000104105, 4.56632e-05, 0), \
                           -100556, 114454, 114454, -nan)
reports[-1].sigmaresid = ValErr(0.582536, 0.00121757, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00126101, None, -1.61323e-05, None, -0.000767777, None, -8.58671e-05, None, -0.000767777, None, -8.58671e-05, None, -0.000149986, None, 6.17991e-05, None, -0.000149986, None, 6.17991e-05, None, 0.58255, None, 0.00835221, None, 0.58255, None, 0.00835221, None)

reports.append(Report(604029576, ("CSC", 1, 4, 1, 17), "MEp41_17"))
reports[-1].posNum = 135688
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0011063, 0.0015986, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0391796, 0.0687754, 0), \
                           ValErr(-0.000629899, 0.0017642, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.83051e-05, 4.1857e-05, 0), \
                           -120411, 135688, 135688, -nan)
reports[-1].sigmaresid = ValErr(0.587707, 0.00112817, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000261333, None, -1.83683e-05, None, -0.0010381, None, 3.36645e-05, None, -0.0010381, None, 3.36645e-05, None, -0.00266544, None, 2.07063e-05, None, -0.00266544, None, 2.07063e-05, None, 0.587709, None, 0.00579167, None, 0.587709, None, 0.00579167, None)

reports.append(Report(604029456, ("CSC", 1, 4, 1, 2), "MEp41_02"))
reports[-1].posNum = 138490
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-8.36585e-05, 0.00160209, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0109473, 0.0705431, 0), \
                           ValErr(-0.000380755, 0.00180609, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(8.64957e-05, 4.20013e-05, 0), \
                           -124568, 138490, 138490, -nan)
reports[-1].sigmaresid = ValErr(0.594839, 0.00113025, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00150431, None, -1.06228e-05, None, 0.000139333, None, -5.20873e-06, None, 0.000139333, None, -5.20873e-06, None, 3.80604e-05, None, -9.99532e-06, None, 3.80604e-05, None, -9.99532e-06, None, 0.594849, None, 0.00564533, None, 0.594849, None, 0.00564533, None)

reports.append(Report(604029472, ("CSC", 1, 4, 1, 4), "MEp41_04"))
reports[-1].posNum = 138330
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00412486, 0.00160987, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0368014, 0.0710213, 0), \
                           ValErr(0.000743912, 0.00181752, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.20783e-05, 4.21853e-05, 0), \
                           -125050, 138330, 138330, -nan)
reports[-1].sigmaresid = ValErr(0.597533, 0.00113602, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00276322, None, -2.17525e-05, None, -0.00399641, None, -2.57114e-05, None, -0.00399641, None, -2.57114e-05, None, -0.00401447, None, -1.89927e-05, None, -0.00401447, None, -1.89927e-05, None, 0.597539, None, 0.00543319, None, 0.597539, None, 0.00543319, None)

reports.append(Report(604029488, ("CSC", 1, 4, 1, 6), "MEp41_06"))
reports[-1].posNum = 137796
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000205696, 0.00162052, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.017238, 0.0713446, 0), \
                           ValErr(-0.00235507, 0.00182591, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.09016e-05, 4.24672e-05, 0), \
                           -125255, 137796, 137796, -nan)
reports[-1].sigmaresid = ValErr(0.600523, 0.00114392, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000185231, None, -9.04257e-06, None, 0.000263077, None, 2.79817e-05, None, 0.000263077, None, 2.79817e-05, None, -0.00242051, None, 3.49875e-06, None, -0.00242051, None, 3.49875e-06, None, 0.600529, None, 0.00587801, None, 0.600529, None, 0.00587801, None)

reports.append(Report(604029504, ("CSC", 1, 4, 1, 8), "MEp41_08"))
reports[-1].posNum = 137751
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00141026, 0.00161637, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0227079, 0.071285, 0), \
                           ValErr(-0.00262361, 0.00182362, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.08868e-05, 4.2382e-05, 0), \
                           -124873, 137751, 137751, -nan)
reports[-1].sigmaresid = ValErr(0.599041, 0.00114128, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00280637, None, -1.28916e-05, None, -0.00151106, None, -7.46631e-06, None, -0.00151106, None, -7.46631e-06, None, -0.00118274, None, 5.66038e-06, None, -0.00118274, None, 5.66038e-06, None, 0.59905, None, 0.00537839, None, 0.59905, None, 0.00537839, None)

reports.append(Report(604029520, ("CSC", 1, 4, 1, 10), "MEp41_10"))
reports[-1].posNum = 138414
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00237283, 0.00161759, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0222195, 0.0713762, 0), \
                           ValErr(0.0012406, 0.00183208, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(7.66444e-06, 4.24678e-05, 0), \
                           -125875, 138414, 138414, -nan)
reports[-1].sigmaresid = ValErr(0.600779, 0.00114185, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00310833, None, -6.31128e-06, None, -0.00235268, None, -9.43733e-06, None, -0.00235268, None, -9.43733e-06, None, -0.00480978, None, -3.96774e-05, None, -0.00480978, None, -3.96774e-05, None, 0.600781, None, 0.00546319, None, 0.600781, None, 0.00546319, None)

reports.append(Report(604029536, ("CSC", 1, 4, 1, 12), "MEp41_12"))
reports[-1].posNum = 138347
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00253159, 0.00162192, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.117389, 0.0714679, 0), \
                           ValErr(-0.000140712, 0.00183016, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.92547e-05, 4.25614e-05, 0), \
                           -126116, 138347, 138347, -nan)
reports[-1].sigmaresid = ValErr(0.602092, 0.00114462, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00256453, None, -4.81808e-06, None, 0.00247945, None, -2.6858e-06, None, 0.00247945, None, -2.6858e-06, None, -0.000516825, None, -3.1434e-05, None, -0.000516825, None, -3.1434e-05, None, 0.6021, None, 0.00555459, None, 0.6021, None, 0.00555459, None)

reports.append(Report(604029552, ("CSC", 1, 4, 1, 14), "MEp41_14"))
reports[-1].posNum = 139026
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00173847, 0.00161588, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0271507, 0.0710525, 0), \
                           ValErr(0.000480429, 0.00182003, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(7.59998e-05, 4.23531e-05, 0), \
                           -126567, 139026, 139026, -nan)
reports[-1].sigmaresid = ValErr(0.601363, 0.00114044, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00181654, None, -2.11626e-05, None, -0.00156214, None, -1.13535e-05, None, -0.00156214, None, -1.13535e-05, None, -0.000392375, None, -2.91606e-05, None, -0.000392375, None, -2.91606e-05, None, 0.601372, None, 0.00566855, None, 0.601372, None, 0.00566855, None)

reports.append(Report(604029568, ("CSC", 1, 4, 1, 16), "MEp41_16"))
reports[-1].posNum = 138572
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000386739, 0.00161441, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00518247, 0.071286, 0), \
                           ValErr(0.00114625, 0.00182222, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.5324e-06, 4.23359e-05, 0), \
                           -125801, 138572, 138572, -nan)
reports[-1].sigmaresid = ValErr(0.599833, 0.0011394, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00234356, None, -7.14713e-06, None, -0.000411699, None, -3.41322e-06, None, -0.000411699, None, -3.41322e-06, None, 0.000750727, None, 1.72308e-05, None, 0.000750727, None, 1.72308e-05, None, 0.599834, None, 0.00554464, None, 0.599834, None, 0.00554464, None)

reports.append(Report(604029584, ("CSC", 1, 4, 1, 18), "MEp41_18"))
reports[-1].posNum = 138299
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00205394, 0.00161803, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0454394, 0.0712235, 0), \
                           ValErr(0.000290058, 0.00182238, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.29535e-05, 4.23879e-05, 0), \
                           -125722, 138299, 138299, -nan)
reports[-1].sigmaresid = ValErr(0.600569, 0.00114192, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0035618, None, -9.98001e-07, None, 0.00200186, None, -1.4882e-05, None, 0.00200186, None, -1.4882e-05, None, 0.00275891, None, -1.87044e-05, None, 0.00275891, None, -1.87044e-05, None, 0.600571, None, 0.00578462, None, 0.600571, None, 0.00578462, None)

reports.append(Report(604029960, ("CSC", 1, 4, 2, 1), "MEp42_01"))
reports[-1].posNum = 60279
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00205175, 0.00488471, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.223695, 0.225469, 0), \
                           ValErr(-0.00340565, 0.00262688, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.95996e-06, 5.46305e-05, 0), \
                           -91326, 60279, 60279, -nan)
reports[-1].sigmaresid = ValErr(1.10089, 0.00317066, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00444914, None, -4.78942e-05, None, -0.00181106, None, -4.32543e-06, None, -0.00181106, None, -4.32543e-06, None, 0.00609037, None, -5.74976e-05, None, 0.00609037, None, -5.74976e-05, None, 1.10091, None, 0.00753908, None, 1.10091, None, 0.00753908, None)

reports.append(Report(604029976, ("CSC", 1, 4, 2, 3), "MEp42_03"))
reports[-1].posNum = 55083
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00832754, 0.00514426, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.61281, 0.234358, 0), \
                           ValErr(0.0031583, 0.00267309, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(9.61329e-05, 5.63064e-05, 0), \
                           -81537.5, 55083, 55083, -nan)
reports[-1].sigmaresid = ValErr(1.06325, 0.00320339, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000141969, None, 8.01147e-06, None, -0.00408477, None, 7.01395e-05, None, -0.00408477, None, 7.01395e-05, None, -0.00479289, None, 4.22739e-05, None, -0.00479289, None, 4.22739e-05, None, 1.06335, None, 0.0072084, None, 1.06335, None, 0.0072084, None)

reports.append(Report(604029992, ("CSC", 1, 4, 2, 5), "MEp42_05"))
reports[-1].posNum = 60722
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00485267, 0.00483733, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.223255, 0.225812, 0), \
                           ValErr(0.000858603, 0.00260618, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.53583e-06, 5.37221e-05, 0), \
                           -91589.9, 60722, 60722, -nan)
reports[-1].sigmaresid = ValErr(1.09353, 0.00313793, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00639397, None, 1.74441e-05, None, 0.00459965, None, 4.03156e-05, None, 0.00459965, None, 4.03156e-05, None, 0.000462462, None, 2.14252e-05, None, 0.000462462, None, 2.14252e-05, None, 1.09354, None, 0.00733192, None, 1.09354, None, 0.00733192, None)

reports.append(Report(604030008, ("CSC", 1, 4, 2, 7), "MEp42_07"))
reports[-1].posNum = 54903
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00410642, 0.00513894, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.478177, 0.234376, 0), \
                           ValErr(-0.00141161, 0.00268656, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.91048e-05, 5.68722e-05, 0), \
                           -81817, 54903, 54903, -nan)
reports[-1].sigmaresid = ValErr(1.07387, 0.0032349, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0051955, None, -1.9145e-05, None, -0.00168324, None, -1.33621e-05, None, -0.00168324, None, -1.33621e-05, None, -0.00142435, None, -1.14799e-05, None, -0.00142435, None, -1.14799e-05, None, 1.07393, None, 0.00724871, None, 1.07393, None, 0.00724871, None)

reports.append(Report(604030024, ("CSC", 1, 4, 2, 9), "MEp42_09"))
reports[-1].posNum = 56454
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00737123, 0.00504392, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.601029, 0.217643, 0), \
                           ValErr(-0.0024454, 0.00250935, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.57825e-05, 5.43001e-05, 0), \
                           -84632.6, 56454, 56454, -nan)
reports[-1].sigmaresid = ValErr(1.0835, 0.00290086, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00572865, None, -6.9657e-06, None, 0.00816603, None, 4.05401e-05, None, 0.00816603, None, 4.05401e-05, None, 0.0126514, None, 1.36459e-05, None, 0.0126514, None, 1.36459e-05, None, 1.08359, None, 0.00708662, None, 1.08359, None, 0.00708662, None)

reports.append(Report(604030040, ("CSC", 1, 4, 2, 11), "MEp42_11"))
reports[-1].posNum = 56045
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.011305, 0.0050413, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0148123, 0.23454, 0), \
                           ValErr(-0.00587807, 0.00270993, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.47685e-05, 5.55644e-05, 0), \
                           -83487.9, 56045, 56045, -nan)
reports[-1].sigmaresid = ValErr(1.07328, 0.00320574, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00897296, None, -3.03398e-05, None, -0.00898647, None, -1.4066e-06, None, -0.00898647, None, -1.4066e-06, None, -0.00652684, None, 8.21588e-06, None, -0.00652684, None, 8.21588e-06, None, 1.07334, None, 0.00717837, None, 1.07334, None, 0.00717837, None)

reports.append(Report(604030056, ("CSC", 1, 4, 2, 13), "MEp42_13"))
reports[-1].posNum = 54431
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0063988, 0.0052326, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.189209, 0.234631, 0), \
                           ValErr(0.00182808, 0.00268819, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.3366e-06, 5.72594e-05, 0), \
                           -81079.1, 54431, 54431, -nan)
reports[-1].sigmaresid = ValErr(1.07319, 0.00325268, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00661951, None, 2.27437e-05, None, 0.0067059, None, 6.16446e-05, None, 0.0067059, None, 6.16446e-05, None, 0.00762422, None, 3.8577e-05, None, 0.00762422, None, 3.8577e-05, None, 1.0732, None, 0.0073397, None, 1.0732, None, 0.0073397, None)

reports.append(Report(604030072, ("CSC", 1, 4, 2, 15), "MEp42_15"))
reports[-1].posNum = 60717
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000394808, 0.0047951, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.433579, 0.223548, 0), \
                           ValErr(-0.00013802, 0.00257735, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.87089e-06, 5.33293e-05, 0), \
                           -91406.9, 60717, 60717, -nan)
reports[-1].sigmaresid = ValErr(1.09037, 0.003129, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00250028, None, -1.87137e-06, None, 0.000517356, None, -2.98067e-06, None, 0.000517356, None, -2.98067e-06, None, -0.000312091, None, -9.85929e-06, None, -0.000312091, None, -9.85929e-06, None, 1.09041, None, 0.00750195, None, 1.09041, None, 0.00750195, None)

reports.append(Report(604030088, ("CSC", 1, 4, 2, 17), "MEp42_17"))
reports[-1].posNum = 54853
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000147853, 0.00522179, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00564782, 0.238193, 0), \
                           ValErr(-0.00617111, 0.00273623, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.67047e-06, 5.72698e-05, 0), \
                           -81532.4, 54853, 54853, -nan)
reports[-1].sigmaresid = ValErr(1.06977, 0.00322979, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00374606, None, -2.08632e-05, None, -0.000216918, None, 3.03892e-06, None, -0.000216918, None, 3.03892e-06, None, 0.00328028, None, -4.72299e-05, None, 0.00328028, None, -4.72299e-05, None, 1.06982, None, 0.00751363, None, 1.06982, None, 0.00751363, None)

reports.append(Report(604030104, ("CSC", 1, 4, 2, 19), "MEp42_19"))
reports[-1].posNum = 61067
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00429716, 0.00485486, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.501851, 0.223698, 0), \
                           ValErr(-0.003048, 0.00261379, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.06027e-05, 5.43496e-05, 0), \
                           -92346.7, 61067, 61067, -nan)
reports[-1].sigmaresid = ValErr(1.09777, 0.00314118, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0116007, None, 7.51112e-06, None, -0.00721017, None, 2.98379e-05, None, -0.00721017, None, 2.98379e-05, None, -0.00383711, None, 1.5597e-05, None, -0.00383711, None, 1.5597e-05, None, 1.09785, None, 0.00730284, None, 1.09785, None, 0.00730284, None)

reports.append(Report(604030120, ("CSC", 1, 4, 2, 21), "MEp42_21"))
reports[-1].posNum = 55377
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00770242, 0.00514627, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.167628, 0.234427, 0), \
                           ValErr(-0.00756577, 0.00265887, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.97245e-05, 5.6016e-05, 0), \
                           -81857.5, 55377, 55377, -nan)
reports[-1].sigmaresid = ValErr(1.06104, 0.00318824, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00381888, None, 1.37695e-06, None, 0.00470463, None, 4.14148e-05, None, 0.00470463, None, 4.14148e-05, None, 0.00319806, None, 9.44351e-06, None, 0.00319806, None, 9.44351e-06, None, 1.06115, None, 0.00719478, None, 1.06115, None, 0.00719478, None)

reports.append(Report(604030136, ("CSC", 1, 4, 2, 23), "MEp42_23"))
reports[-1].posNum = 60473
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0111917, 0.00483057, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.200124, 0.22331, 0), \
                           ValErr(-0.00389355, 0.00129659, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.4191e-05, 5.38682e-05, 0), \
                           -91091.6, 60473, 60473, -nan)
reports[-1].sigmaresid = ValErr(1.09131, 0.00307417, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0072535, None, -4.18755e-05, None, 0.00856225, None, -4.04584e-05, None, 0.00856225, None, -4.04584e-05, None, 0.0101347, None, -2.72796e-05, None, 0.0101347, None, -2.72796e-05, None, 1.09136, None, 0.00836767, None, 1.09136, None, 0.00836767, None)

reports.append(Report(604030152, ("CSC", 1, 4, 2, 25), "MEp42_25"))
reports[-1].posNum = 56413
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00300437, 0.00508752, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.297784, 0.230174, 0), \
                           ValErr(-0.00261637, 0.00264641, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.63523e-05, 5.59014e-05, 0), \
                           -84253.8, 56413, 56413, -nan)
reports[-1].sigmaresid = ValErr(1.07743, 0.00320763, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000572695, None, 4.63759e-05, None, 0.000605072, None, 7.87263e-05, None, 0.000605072, None, 7.87263e-05, None, -0.00410117, None, 5.7119e-05, None, -0.00410117, None, 5.7119e-05, None, 1.07747, None, 0.00721856, None, 1.07747, None, 0.00721856, None)

reports.append(Report(604030168, ("CSC", 1, 4, 2, 27), "MEp42_27"))
reports[-1].posNum = 57583
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00341536, 0.00499515, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.39007, 0.232157, 0), \
                           ValErr(0.00252591, 0.00265489, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.78006e-05, 5.48871e-05, 0), \
                           -86409.7, 57583, 57583, -nan)
reports[-1].sigmaresid = ValErr(1.0851, 0.00319749, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00968643, None, 5.74857e-06, None, -0.00564025, None, 1.69274e-05, None, -0.00564025, None, 1.69274e-05, None, -0.0129882, None, -3.68379e-05, None, -0.0129882, None, -3.68379e-05, None, 1.08515, None, 0.00712441, None, 1.08515, None, 0.00712441, None)

reports.append(Report(604030184, ("CSC", 1, 4, 2, 29), "MEp42_29"))
reports[-1].posNum = 58102
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00154313, 0.00498985, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.445134, 0.23138, 0), \
                           ValErr(-0.00173277, 0.00265285, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.99691e-05, 5.50367e-05, 0), \
                           -87157.2, 58102, 58102, -nan)
reports[-1].sigmaresid = ValErr(1.08451, 0.00318144, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00556731, None, 2.77257e-05, None, 0.00360072, None, 5.73373e-05, None, 0.00360072, None, 5.73373e-05, None, 0.00389564, None, 4.08912e-05, None, 0.00389564, None, 4.08912e-05, None, 1.08457, None, 0.00715055, None, 1.08457, None, 0.00715055, None)

reports.append(Report(604030200, ("CSC", 1, 4, 2, 31), "MEp42_31"))
reports[-1].posNum = 55955
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0047852, 0.00508421, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.698702, 0.232247, 0), \
                           ValErr(-0.00186634, 0.00269216, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.7922e-05, 5.63207e-05, 0), \
                           -83413.1, 55955, 55955, -nan)
reports[-1].sigmaresid = ValErr(1.07442, 0.00320942, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00285806, None, -9.12098e-06, None, 0.00198909, None, 8.27127e-05, None, 0.00198909, None, 8.27127e-05, None, -0.00237772, None, 2.38915e-05, None, -0.00237772, None, 2.38915e-05, None, 1.07453, None, 0.0091545, None, 1.07453, None, 0.0091545, None)

reports.append(Report(604030216, ("CSC", 1, 4, 2, 33), "MEp42_33"))
reports[-1].posNum = 60242
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0055748, 0.00483423, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.25471, 0.10949, 0), \
                           ValErr(-0.00155827, 0.00255195, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.90679e-05, 5.36728e-05, 0), \
                           -90638.4, 60242, 60242, -nan)
reports[-1].sigmaresid = ValErr(1.08941, 0.00310844, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00786049, None, 5.83811e-05, None, 0.00235715, None, 0.000130041, None, 0.00235715, None, 0.000130041, None, 0.000985588, None, 6.84798e-05, None, 0.000985588, None, 6.84798e-05, None, 1.08945, None, 0.00736979, None, 1.08945, None, 0.00736979, None)

reports.append(Report(604030232, ("CSC", 1, 4, 2, 35), "MEp42_35"))
reports[-1].posNum = 54139
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00733318, 0.00519611, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.375339, 0.23562, 0), \
                           ValErr(-0.00338817, 0.00271575, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(7.69072e-05, 5.68833e-05, 0), \
                           -79507, 54139, 54139, -nan)
reports[-1].sigmaresid = ValErr(1.05089, 0.00319364, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00864584, None, 5.95701e-05, None, -0.00384138, None, 6.8834e-05, None, -0.00384138, None, 6.8834e-05, None, -0.00665735, None, 5.92423e-05, None, -0.00665735, None, 5.92423e-05, None, 1.05095, None, 0.0075509, None, 1.05095, None, 0.0075509, None)

reports.append(Report(604029968, ("CSC", 1, 4, 2, 2), "MEp42_02"))
reports[-1].posNum = 58801
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00602915, 0.00498727, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.848606, 0.240495, 0), \
                           ValErr(0.00607505, 0.00277035, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.57429e-05, 5.54339e-05, 0), \
                           -89282.8, 58801, 58801, -nan)
reports[-1].sigmaresid = ValErr(1.10456, 0.00319157, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000525441, None, -4.96149e-05, None, -0.00401866, None, -7.12694e-05, None, -0.00401866, None, -7.12694e-05, None, -0.0123909, None, -0.0001158, None, -0.0123909, None, -0.0001158, None, 1.10472, None, 0.00724267, None, 1.10472, None, 0.00724267, None)

reports.append(Report(604029984, ("CSC", 1, 4, 2, 4), "MEp42_04"))
reports[-1].posNum = 57740
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00602872, 0.00510757, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.306976, 0.245016, 0), \
                           ValErr(-0.00123238, 0.00283928, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.34255e-05, 5.72217e-05, 0), \
                           -87585.7, 57740, 57740, -nan)
reports[-1].sigmaresid = ValErr(1.10291, 0.00321993, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00375062, None, -3.54355e-05, None, 0.00261005, None, -1.94739e-06, None, 0.00261005, None, -1.94739e-06, None, 0.00302647, None, -2.82871e-05, None, 0.00302647, None, -2.82871e-05, None, 1.10296, None, 0.00694586, None, 1.10296, None, 0.00694586, None)

reports.append(Report(604030000, ("CSC", 1, 4, 2, 6), "MEp42_06"))
reports[-1].posNum = 60929
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00106658, 0.004885, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.153927, 0.232485, 0), \
                           ValErr(0.000713834, 0.00270976, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.08343e-05, 5.45892e-05, 0), \
                           -92528.3, 60929, 60929, -nan)
reports[-1].sigmaresid = ValErr(1.10483, 0.00316496, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0015638, None, -4.59476e-06, None, 0.00213778, None, -3.78662e-05, None, 0.00213778, None, -3.78662e-05, None, 0.00457403, None, -3.83952e-06, None, 0.00457403, None, -3.83952e-06, None, 1.10483, None, 0.00723168, None, 1.10483, None, 0.00723168, None)

reports.append(Report(604030016, ("CSC", 1, 4, 2, 8), "MEp42_08"))
reports[-1].posNum = 55165
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00111482, 0.00529695, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0137083, 0.245359, 0), \
                           ValErr(-0.00222673, 0.00283996, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.64729e-05, 5.86013e-05, 0), \
                           -82478.9, 55165, 55165, -nan)
reports[-1].sigmaresid = ValErr(1.07917, 0.00324892, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00595375, None, -5.73404e-05, None, -0.00187965, None, -5.43434e-05, None, -0.00187965, None, -5.43434e-05, None, -0.00279151, None, -4.57452e-05, None, -0.00279151, None, -4.57452e-05, None, 1.07919, None, 0.00710973, None, 1.07919, None, 0.00710973, None)

reports.append(Report(604030032, ("CSC", 1, 4, 2, 10), "MEp42_10"))
reports[-1].posNum = 62793
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0099529, 0.0048234, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0520444, 0.166075, 0), \
                           ValErr(-0.00285128, 0.00230373, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.42175e-05, 5.41269e-05, 0), \
                           -96527.4, 62793, 62793, -nan)
reports[-1].sigmaresid = ValErr(1.12558, 0.00315167, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00851865, None, -5.44459e-07, None, 0.00850836, None, -4.29679e-06, None, 0.00850836, None, -4.29679e-06, None, 0.0105505, None, 3.10553e-06, None, 0.0105505, None, 3.10553e-06, None, 1.12559, None, 0.00693285, None, 1.12559, None, 0.00693285, None)

reports.append(Report(604030048, ("CSC", 1, 4, 2, 12), "MEp42_12"))
reports[-1].posNum = 55716
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00296002, 0.00516437, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.129281, 0.243687, 0), \
                           ValErr(-0.00125478, 0.0028344, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.42188e-06, 5.70443e-05, 0), \
                           -83214.4, 55716, 55716, -nan)
reports[-1].sigmaresid = ValErr(1.07746, 0.00322774, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0080977, None, -7.68113e-06, None, -0.00304495, None, -1.01464e-05, None, -0.00304495, None, -1.01464e-05, None, 0.00480011, None, -3.8407e-05, None, 0.00480011, None, -3.8407e-05, None, 1.07746, None, 0.00712625, None, 1.07746, None, 0.00712625, None)

reports.append(Report(604030064, ("CSC", 1, 4, 2, 14), "MEp42_14"))
reports[-1].posNum = 61550
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00760937, 0.00485975, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.399112, 0.116104, 0), \
                           ValErr(-0.00184015, 0.00270014, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.91319e-05, 5.45547e-05, 0), \
                           -93626.4, 61550, 61550, -nan)
reports[-1].sigmaresid = ValErr(1.10761, 0.00308871, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00406553, None, 6.12541e-06, None, 0.00655022, None, 5.54345e-05, None, 0.00655022, None, 5.54345e-05, None, 0.00794102, None, 2.31529e-05, None, 0.00794102, None, 2.31529e-05, None, 1.10765, None, 0.00734595, None, 1.10765, None, 0.00734595, None)

reports.append(Report(604030080, ("CSC", 1, 4, 2, 16), "MEp42_16"))
reports[-1].posNum = 57036
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00801274, 0.00517355, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0335101, 0.243648, 0), \
                           ValErr(-0.00178457, 0.00284009, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.08226e-05, 5.71198e-05, 0), \
                           -85719.4, 57036, 57036, -nan)
reports[-1].sigmaresid = ValErr(1.08759, 0.00322014, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00810947, None, -1.30141e-05, None, 0.00713789, None, -1.14924e-05, None, 0.00713789, None, -1.14924e-05, None, 0.0177151, None, 1.02653e-06, None, 0.0177151, None, 1.02653e-06, None, 1.08759, None, 0.00721577, None, 1.08759, None, 0.00721577, None)

reports.append(Report(604030096, ("CSC", 1, 4, 2, 18), "MEp42_18"))
reports[-1].posNum = 58265
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000581216, 0.00509673, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.276378, 0.241202, 0), \
                           ValErr(-0.00749839, 0.00277569, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.48058e-05, 5.61701e-05, 0), \
                           -88454.4, 58265, 58265, -nan)
reports[-1].sigmaresid = ValErr(1.10429, 0.00323492, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00188402, None, -1.75467e-06, None, -0.000199609, None, -1.80842e-06, None, -0.000199609, None, -1.80842e-06, None, -0.000586621, None, 1.26464e-05, None, -0.000586621, None, 1.26464e-05, None, 1.10436, None, 0.00798493, None, 1.10436, None, 0.00798493, None)

reports.append(Report(604030112, ("CSC", 1, 4, 2, 20), "MEp42_20"))
reports[-1].posNum = 59720
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0084252, 0.00496832, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.46025, 0.237185, 0), \
                           ValErr(-6.05017e-05, 0.00276843, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.39987e-05, 5.35167e-05, 0), \
                           -90607.5, 59720, 59720, -nan)
reports[-1].sigmaresid = ValErr(1.10325, 0.00311709, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00324316, None, 8.77921e-06, None, -0.00684305, None, 2.07208e-05, None, -0.00684305, None, 2.07208e-05, None, -0.0126066, None, -3.01764e-07, None, -0.0126066, None, -3.01764e-07, None, 1.1033, None, 0.00710117, None, 1.1033, None, 0.00710117, None)

reports.append(Report(604030128, ("CSC", 1, 4, 2, 22), "MEp42_22"))
reports[-1].posNum = 57361
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00684084, 0.00510186, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.717436, 0.240924, 0), \
                           ValErr(0.000424456, 0.00281799, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.39702e-05, 5.63109e-05, 0), \
                           -86444.6, 57361, 57361, -nan)
reports[-1].sigmaresid = ValErr(1.09208, 0.00321602, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00877911, None, 2.47588e-05, None, 0.00477597, None, -1.12948e-05, None, 0.00477597, None, -1.12948e-05, None, 0.00935679, None, 8.03339e-06, None, 0.00935679, None, 8.03339e-06, None, 1.09218, None, 0.00723708, None, 1.09218, None, 0.00723708, None)

reports.append(Report(604030144, ("CSC", 1, 4, 2, 24), "MEp42_24"))
reports[-1].posNum = 61587
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0073995, 0.00481981, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.190534, 0.230632, 0), \
                           ValErr(-0.00366734, 0.00270498, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.81205e-06, 5.39859e-05, 0), \
                           -93267.4, 61587, 61587, -nan)
reports[-1].sigmaresid = ValErr(1.10017, 0.00313473, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0066, None, -4.6362e-05, None, -0.00722677, None, -4.2247e-05, None, -0.00722677, None, -4.2247e-05, None, -0.00718683, None, -1.47584e-05, None, -0.00718683, None, -1.47584e-05, None, 1.10019, None, 0.00716727, None, 1.10019, None, 0.00716727, None)

reports.append(Report(604030160, ("CSC", 1, 4, 2, 26), "MEp42_26"))
reports[-1].posNum = 56621
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00193423, 0.00522795, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.363404, 0.243626, 0), \
                           ValErr(-0.000127673, 0.00282822, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.37915e-05, 5.79352e-05, 0), \
                           -85119.7, 56621, 56621, -nan)
reports[-1].sigmaresid = ValErr(1.08805, 0.00323329, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00652809, None, -1.23974e-05, None, -0.00608086, None, -2.13341e-06, None, -0.00608086, None, -2.13341e-06, None, 0.000902739, None, -2.50037e-05, None, 0.000902739, None, -2.50037e-05, None, 1.0881, None, 0.00736176, None, 1.0881, None, 0.00736176, None)

reports.append(Report(604030176, ("CSC", 1, 4, 2, 28), "MEp42_28"))
reports[-1].posNum = 62275
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00683062, 0.00487032, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.852328, 0.230768, 0), \
                           ValErr(-0.00136453, 0.0027166, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.20291e-05, 5.49105e-05, 0), \
                           -95532.1, 62275, 62275, -nan)
reports[-1].sigmaresid = ValErr(1.12198, 0.00317917, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0127579, None, -3.62647e-05, None, -0.00758822, None, -7.43354e-05, None, -0.00758822, None, -7.43354e-05, None, -0.00477389, None, -7.32328e-05, None, -0.00477389, None, -7.32328e-05, None, 1.12211, None, 0.00709735, None, 1.12211, None, 0.00709735, None)

reports.append(Report(604030192, ("CSC", 1, 4, 2, 30), "MEp42_30"))
reports[-1].posNum = 55231
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00566967, 0.0052261, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0678613, 0.244116, 0), \
                           ValErr(-0.00623986, 0.00280938, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.11065e-06, 5.75938e-05, 0), \
                           -82166, 55231, 55231, -nan)
reports[-1].sigmaresid = ValErr(1.07116, 0.00322289, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0112694, None, 3.69884e-05, None, 0.00555162, None, 7.90381e-05, None, 0.00555162, None, 7.90381e-05, None, 0.00791841, None, 9.69164e-05, None, 0.00791841, None, 9.69164e-05, None, 1.07121, None, 0.00730815, None, 1.07121, None, 0.00730815, None)

reports.append(Report(604030208, ("CSC", 1, 4, 2, 32), "MEp42_32"))
reports[-1].posNum = 61235
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0161142, 0.00489918, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.010581, 0.105649, 0), \
                           ValErr(7.03421e-05, 0.00122778, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000136683, 5.49404e-05, 0), \
                           -93126.7, 61235, 61235, -nan)
reports[-1].sigmaresid = ValErr(1.10724, 0.003164, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00781325, None, 1.66366e-05, None, -0.011156, None, -2.48218e-05, None, -0.011156, None, -2.48218e-05, None, -0.0122387, None, -1.69923e-05, None, -0.0122387, None, -1.69923e-05, None, 1.1073, None, 0.00718487, None, 1.1073, None, 0.00718487, None)

reports.append(Report(604030224, ("CSC", 1, 4, 2, 34), "MEp42_34"))
reports[-1].posNum = 58102
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0143329, 0.00516292, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.167103, 0.122716, 0), \
                           ValErr(-0.00103694, 0.00263472, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000129074, 5.75622e-05, 0), \
                           -88418.7, 58102, 58102, -nan)
reports[-1].sigmaresid = ValErr(1.10832, 0.00324086, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0065474, None, -6.34984e-05, None, -0.00906609, None, -0.000102966, None, -0.00906609, None, -0.000102966, None, -0.0122455, None, -7.36259e-05, None, -0.0122455, None, -7.36259e-05, None, 1.10838, None, 0.00719403, None, 1.10838, None, 0.00719403, None)

reports.append(Report(604030240, ("CSC", 1, 4, 2, 36), "MEp42_36"))
reports[-1].posNum = 59899
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0101035, 0.00494646, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.605936, 0.194793, 0), \
                           ValErr(0.00389578, 0.00233892, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.4049e-05, 5.42689e-05, 0), \
                           -90796.5, 59899, 59899, -nan)
reports[-1].sigmaresid = ValErr(1.10174, 0.00314072, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0106005, None, 3.40135e-05, None, 0.01235, None, 7.19801e-05, None, 0.01235, None, 7.19801e-05, None, 0.0137312, None, 7.77175e-05, None, 0.0137312, None, 7.77175e-05, None, 1.10182, None, 0.00711512, None, 1.10182, None, 0.00711512, None)

reports.append(Report(604050440, ("CSC", 2, 1, 1, 1), "MEm11_01"))
reports[-1].posNum = 104153
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00264028, 0.000604762, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.140946, 0.0475555, 0), \
                           ValErr(-0.00319839, 0.00126019, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.30867e-06, 1.58124e-05, 0), \
                           25023.7, 104153, 104153, -nan)
reports[-1].sigmaresid = ValErr(0.190292, 0.000416936, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00218461, None, 2.80053e-06, None, 0.0026347, None, -4.44374e-06, None, 0.0026347, None, -4.44374e-06, None, 0.00302419, None, -1.46965e-07, None, 0.00302419, None, -1.46965e-07, None, 0.190303, None, 0.00419987, None, 0.190303, None, 0.00419987, None)

reports.append(Report(604050456, ("CSC", 2, 1, 1, 3), "MEm11_03"))
reports[-1].posNum = 105526
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00300264, 0.000595172, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.133954, 0.0466646, 0), \
                           ValErr(-0.00232546, 0.00123766, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.35666e-05, 1.54821e-05, 0), \
                           26750, 105526, 105526, -nan)
reports[-1].sigmaresid = ValErr(0.18779, 0.000408769, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00226939, None, -1.44095e-05, None, 0.00288202, None, -8.48868e-06, None, 0.00288202, None, -8.48868e-06, None, 0.00236452, None, -5.72046e-06, None, 0.00236452, None, -5.72046e-06, None, 0.187799, None, 0.00416508, None, 0.187799, None, 0.00416508, None)

reports.append(Report(604050472, ("CSC", 2, 1, 1, 5), "MEm11_05"))
reports[-1].posNum = 104239
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00112617, 0.000607271, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0283153, 0.0477957, 0), \
                           ValErr(0.000157885, 0.00127523, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.52742e-05, 1.59529e-05, 0), \
                           24720.7, 104239, 104239, -nan)
reports[-1].sigmaresid = ValErr(0.190883, 0.000418057, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000359678, None, 8.64586e-06, None, 0.000821205, None, -2.89475e-05, None, 0.000821205, None, -2.89475e-05, None, -0.00105139, None, -1.21259e-05, None, -0.00105139, None, -1.21259e-05, None, 0.190888, None, 0.0045458, None, 0.190888, None, 0.0045458, None)

reports.append(Report(604050488, ("CSC", 2, 1, 1, 7), "MEm11_07"))
reports[-1].posNum = 104673
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00200704, 0.000603281, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0305201, 0.0475218, 0), \
                           ValErr(0.000699526, 0.00125362, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.89401e-06, 1.5696e-05, 0), \
                           25409.5, 104673, 104673, -nan)
reports[-1].sigmaresid = ValErr(0.189818, 0.000414862, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00174575, None, 9.31025e-06, None, 0.00193688, None, 2.24119e-05, None, 0.00193688, None, 2.24119e-05, None, 0.00166353, None, 2.16669e-05, None, 0.00166353, None, 2.16669e-05, None, 0.189819, None, 0.00409024, None, 0.189819, None, 0.00409024, None)

reports.append(Report(604050504, ("CSC", 2, 1, 1, 9), "MEm11_09"))
reports[-1].posNum = 104493
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00134645, 0.000607921, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0516703, 0.0477075, 0), \
                           ValErr(-6.44378e-05, 0.00126681, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.2923e-06, 1.59338e-05, 0), \
                           24437.8, 104493, 104493, -nan)
reports[-1].sigmaresid = ValErr(0.191511, 0.000418922, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00143383, None, -5.21584e-06, None, 0.00129161, None, -2.51359e-05, None, 0.00129161, None, -2.51359e-05, None, -0.000435691, None, 1.41916e-05, None, -0.000435691, None, 1.41916e-05, None, 0.191513, None, 0.00469314, None, 0.191513, None, 0.00469314, None)

reports.append(Report(604050520, ("CSC", 2, 1, 1, 11), "MEm11_11"))
reports[-1].posNum = 104691
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00136185, 0.000608463, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.118946, 0.0476877, 0), \
                           ValErr(0.000525442, 0.0012693, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(7.64402e-06, 1.59359e-05, 0), \
                           24345.2, 104691, 104691, -nan)
reports[-1].sigmaresid = ValErr(0.191765, 0.000419082, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00152084, None, 9.35094e-06, None, 0.00142983, None, 2.38145e-05, None, 0.00142983, None, 2.38145e-05, None, -0.000983616, None, 2.3443e-05, None, -0.000983616, None, 2.3443e-05, None, 0.191773, None, 0.00423863, None, 0.191773, None, 0.00423863, None)

reports.append(Report(604050536, ("CSC", 2, 1, 1, 13), "MEm11_13"))
reports[-1].posNum = 104968
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00111121, 0.000606186, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.19572, 0.0476163, 0), \
                           ValErr(-0.00131733, 0.00126202, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.47562e-05, 1.58017e-05, 0), \
                           24785.9, 104968, 104968, -nan)
reports[-1].sigmaresid = ValErr(0.191079, 0.000417033, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00124508, None, 4.17183e-06, None, 0.00134939, None, 4.03583e-06, None, 0.00134939, None, 4.03583e-06, None, 0.00181595, None, 7.43004e-06, None, 0.00181595, None, 7.43004e-06, None, 0.191097, None, 0.00423389, None, 0.191097, None, 0.00423389, None)

reports.append(Report(604050552, ("CSC", 2, 1, 1, 15), "MEm11_15"))
reports[-1].posNum = 104714
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0024239, 0.000604579, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.130973, 0.0475181, 0), \
                           ValErr(-0.00152488, 0.00125692, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.07589e-05, 1.5788e-05, 0), \
                           24939.6, 104714, 104714, -nan)
reports[-1].sigmaresid = ValErr(0.19069, 0.000416688, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00231383, None, 7.87667e-06, None, 0.00232878, None, -4.05191e-06, None, 0.00232878, None, -4.05191e-06, None, 0.00150425, None, -4.18414e-07, None, 0.00150425, None, -4.18414e-07, None, 0.190697, None, 0.00488756, None, 0.190697, None, 0.00488756, None)

reports.append(Report(604050568, ("CSC", 2, 1, 1, 17), "MEm11_17"))
reports[-1].posNum = 104442
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00242166, 0.000601751, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0187702, 0.0472114, 0), \
                           ValErr(-0.000735277, 0.00125108, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.18861e-05, 1.56513e-05, 0), \
                           25889.9, 104442, 104442, -nan)
reports[-1].sigmaresid = ValErr(0.188845, 0.000413193, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00194501, None, -5.34149e-06, None, 0.00212814, None, 1.18036e-05, None, 0.00212814, None, 1.18036e-05, None, 0.00215885, None, 3.18528e-05, None, 0.00215885, None, 3.18528e-05, None, 0.18885, None, 0.00423622, None, 0.18885, None, 0.00423622, None)

reports.append(Report(604050584, ("CSC", 2, 1, 1, 19), "MEm11_19"))
reports[-1].posNum = 104992
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00268043, 0.000603481, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.162162, 0.0476516, 0), \
                           ValErr(-0.00154128, 0.00126047, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.19094e-05, 1.58033e-05, 0), \
                           24889.3, 104992, 104992, -nan)
reports[-1].sigmaresid = ValErr(0.190902, 0.000416598, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00283395, None, 3.1761e-06, None, 0.00250975, None, -4.62052e-06, None, 0.00250975, None, -4.62052e-06, None, 0.00117258, None, 1.48955e-05, None, 0.00117258, None, 1.48955e-05, None, 0.190914, None, 0.00426737, None, 0.190914, None, 0.00426737, None)

reports.append(Report(604050600, ("CSC", 2, 1, 1, 21), "MEm11_21"))
reports[-1].posNum = 104669
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00270964, 0.000603313, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00681251, 0.0474212, 0), \
                           ValErr(-0.000622963, 0.00125791, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.3876e-06, 1.56888e-05, 0), \
                           25387, 104669, 104669, -nan)
reports[-1].sigmaresid = ValErr(0.189857, 0.000414955, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00280334, None, -5.34139e-06, None, 0.0026246, None, -2.05969e-06, None, 0.0026246, None, -2.05969e-06, None, 0.00167262, None, 2.03686e-05, None, 0.00167262, None, 2.03686e-05, None, 0.189858, None, 0.00411444, None, 0.189858, None, 0.00411444, None)

reports.append(Report(604050616, ("CSC", 2, 1, 1, 23), "MEm11_23"))
reports[-1].posNum = 104222
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00214114, 0.00060681, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.157602, 0.0477141, 0), \
                           ValErr(-0.000850554, 0.00126249, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.86733e-05, 1.58759e-05, 0), \
                           24530.1, 104222, 104222, -nan)
reports[-1].sigmaresid = ValErr(0.191226, 0.000418843, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00100925, None, 4.45896e-06, None, 0.00200163, None, 9.9664e-06, None, 0.00200163, None, 9.9664e-06, None, 0.000125849, None, 1.07704e-05, None, 0.000125849, None, 1.07704e-05, None, 0.191237, None, 0.00423019, None, 0.191237, None, 0.00423019, None)

reports.append(Report(604050632, ("CSC", 2, 1, 1, 25), "MEm11_25"))
reports[-1].posNum = 104719
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00354137, 0.000601324, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0752989, 0.0472681, 0), \
                           ValErr(-0.00127132, 0.00125104, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.71544e-05, 1.56522e-05, 0), \
                           25654.1, 104719, 104719, -nan)
reports[-1].sigmaresid = ValErr(0.189395, 0.000413849, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0024167, None, -1.00345e-07, None, 0.00312652, None, -7.22849e-06, None, 0.00312652, None, -7.22849e-06, None, 0.00165463, None, 1.85443e-06, None, 0.00165463, None, 1.85443e-06, None, 0.189406, None, 0.00498251, None, 0.189406, None, 0.00498251, None)

reports.append(Report(604050648, ("CSC", 2, 1, 1, 27), "MEm11_27"))
reports[-1].posNum = 103908
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00309189, 0.000609031, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0236229, 0.04781, 0), \
                           ValErr(-0.00297671, 0.00126847, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.62409e-05, 1.59167e-05, 0), \
                           24421.2, 103908, 103908, -nan)
reports[-1].sigmaresid = ValErr(0.19129, 0.000419617, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00234163, None, 3.54945e-06, None, 0.0028772, None, -2.463e-05, None, 0.0028772, None, -2.463e-05, None, 0.00257239, None, 1.14493e-05, None, 0.00257239, None, 1.14493e-05, None, 0.191297, None, 0.00659041, None, 0.191297, None, 0.00659041, None)

reports.append(Report(604050664, ("CSC", 2, 1, 1, 29), "MEm11_29"))
reports[-1].posNum = 104252
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00147165, 0.000606103, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.139618, 0.0476858, 0), \
                           ValErr(-0.00115315, 0.00126456, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.59325e-06, 1.58559e-05, 0), \
                           24735.9, 104252, 104252, -nan)
reports[-1].sigmaresid = ValErr(0.190861, 0.000417986, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00173994, None, 9.01532e-06, None, 0.00146237, None, 2.80363e-06, None, 0.00146237, None, 2.80363e-06, None, 0.00100523, None, 1.82402e-05, None, 0.00100523, None, 1.82402e-05, None, 0.190869, None, 0.0040809, None, 0.190869, None, 0.0040809, None)

reports.append(Report(604050680, ("CSC", 2, 1, 1, 31), "MEm11_31"))
reports[-1].posNum = 104844
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00331585, 0.000603558, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0685763, 0.0472921, 0), \
                           ValErr(-0.000860417, 0.00125314, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.27585e-05, 1.57238e-05, 0), \
                           25295.4, 104844, 104844, -nan)
reports[-1].sigmaresid = ValErr(0.1901, 0.000415141, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00276626, None, 6.01799e-06, None, 0.00312514, None, 2.2305e-05, None, 0.00312514, None, 2.2305e-05, None, 0.00139071, None, 5.39736e-05, None, 0.00139071, None, 5.39736e-05, None, 0.190104, None, 0.00472139, None, 0.190104, None, 0.00472139, None)

reports.append(Report(604050696, ("CSC", 2, 1, 1, 33), "MEm11_33"))
reports[-1].posNum = 105101
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0021295, 0.000607325, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0378554, 0.0477738, 0), \
                           ValErr(-0.00100544, 0.00126082, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.13502e-06, 1.58619e-05, 0), \
                           24340.4, 105101, 105101, -nan)
reports[-1].sigmaresid = ValErr(0.191948, 0.000418664, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00167737, None, 5.33967e-07, None, 0.0020637, None, 1.3076e-05, None, 0.0020637, None, 1.3076e-05, None, 0.00156006, None, 1.88081e-05, None, 0.00156006, None, 1.88081e-05, None, 0.191949, None, 0.0044653, None, 0.191949, None, 0.0044653, None)

reports.append(Report(604050712, ("CSC", 2, 1, 1, 35), "MEm11_35"))
reports[-1].posNum = 105329
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00273882, 0.00059602, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0767513, 0.0467959, 0), \
                           ValErr(-0.000677597, 0.0012413, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.33382e-05, 1.54761e-05, 0), \
                           26762.4, 105329, 105329, -nan)
reports[-1].sigmaresid = ValErr(0.187679, 0.000408908, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00235546, None, -2.13864e-06, None, 0.00286714, None, -1.17333e-06, None, 0.00286714, None, -1.17333e-06, None, 0.00292416, None, 3.34953e-05, None, 0.00292416, None, 3.34953e-05, None, 0.187682, None, 0.0049382, None, 0.187682, None, 0.0049382, None)

reports.append(Report(604050448, ("CSC", 2, 1, 1, 2), "MEm11_02"))
reports[-1].posNum = 104697
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00258811, 0.000542335, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.033286, 0.0402365, 0), \
                           ValErr(0.000133542, 0.0010711, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.79782e-05, 1.40964e-05, 0), \
                           36752.2, 104697, 104697, -nan)
reports[-1].sigmaresid = ValErr(0.170337, 0.000372243, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00171466, None, -1.64785e-05, None, 0.00233047, None, -3.08931e-05, None, 0.00233047, None, -3.08931e-05, None, 0.0025223, None, -2.27744e-05, None, 0.0025223, None, -2.27744e-05, None, 0.170341, None, 0.00438312, None, 0.170341, None, 0.00438312, None)

reports.append(Report(604050464, ("CSC", 2, 1, 1, 4), "MEm11_04"))
reports[-1].posNum = 103722
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00208925, 0.000541508, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.13077, 0.0401677, 0), \
                           ValErr(-0.000284532, 0.00106297, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.76769e-06, 1.40257e-05, 0), \
                           37096.1, 103722, 103722, -nan)
reports[-1].sigmaresid = ValErr(0.169214, 0.000371524, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00129563, None, -7.55472e-06, None, 0.00210837, None, -3.03648e-05, None, 0.00210837, None, -3.03648e-05, None, 0.0025727, None, -1.83905e-05, None, 0.0025727, None, -1.83905e-05, None, 0.169224, None, 0.00438864, None, 0.169224, None, 0.00438864, None)

reports.append(Report(604050480, ("CSC", 2, 1, 1, 6), "MEm11_06"))
reports[-1].posNum = 104996
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00137433, 0.000543512, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0735279, 0.0402178, 0), \
                           ValErr(0.0010898, 0.00106525, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.12339e-05, 1.40664e-05, 0), \
                           36575.7, 104996, 104996, -nan)
reports[-1].sigmaresid = ValErr(0.170795, 0.000372712, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00117357, None, 4.52605e-06, None, 0.0011743, None, -2.28495e-05, None, 0.0011743, None, -2.28495e-05, None, 0.000104691, None, 1.47363e-05, None, 0.000104691, None, 1.47363e-05, None, 0.170802, None, 0.00455218, None, 0.170802, None, 0.00455218, None)

reports.append(Report(604050496, ("CSC", 2, 1, 1, 8), "MEm11_08"))
reports[-1].posNum = 103859
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00187068, 0.000540974, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0793897, 0.0401706, 0), \
                           ValErr(-0.00109853, 0.0010609, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.81056e-07, 1.39805e-05, 0), \
                           37151.8, 103859, 103859, -nan)
reports[-1].sigmaresid = ValErr(0.169204, 0.000371255, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00151657, None, -4.94765e-06, None, 0.00187133, None, -1.99931e-05, None, 0.00187133, None, -1.99931e-05, None, 0.0010232, None, -1.20979e-05, None, 0.0010232, None, -1.20979e-05, None, 0.169207, None, 0.00460681, None, 0.169207, None, 0.00460681, None)

reports.append(Report(604050512, ("CSC", 2, 1, 1, 10), "MEm11_10"))
reports[-1].posNum = 104077
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00369643, 0.000544944, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0985885, 0.0403166, 0), \
                           ValErr(0.000196363, 0.00106487, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.19843e-05, 1.4115e-05, 0), \
                           36470, 104077, 104077, -nan)
reports[-1].sigmaresid = ValErr(0.170443, 0.000373583, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0032225, None, -2.24305e-05, None, 0.00358258, None, -4.05678e-05, None, 0.00358258, None, -4.05678e-05, None, 0.00460214, None, -3.4876e-05, None, 0.00460214, None, -3.4876e-05, None, 0.170449, None, 0.00451863, None, 0.170449, None, 0.00451863, None)

reports.append(Report(604050528, ("CSC", 2, 1, 1, 12), "MEm11_12"))
reports[-1].posNum = 103976
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00274351, 0.000541601, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0581261, 0.0402639, 0), \
                           ValErr(-0.000920252, 0.00106384, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.28226e-05, 1.39899e-05, 0), \
                           37051.9, 103976, 103976, -nan)
reports[-1].sigmaresid = ValErr(0.169434, 0.000371552, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00250499, None, -9.72714e-06, None, 0.00252222, None, -2.40427e-05, None, 0.00252222, None, -2.40427e-05, None, 0.00111366, None, -6.55565e-06, None, 0.00111366, None, -6.55565e-06, None, 0.169438, None, 0.00502913, None, 0.169438, None, 0.00502913, None)

reports.append(Report(604050544, ("CSC", 2, 1, 1, 14), "MEm11_14"))
reports[-1].posNum = 104106
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00188661, 0.000541966, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.141727, 0.0402732, 0), \
                           ValErr(-0.00197484, 0.0010604, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.78247e-06, 1.40125e-05, 0), \
                           36915.6, 104106, 104106, -nan)
reports[-1].sigmaresid = ValErr(0.169732, 0.000371973, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00131533, None, 2.23181e-06, None, 0.00184504, None, -2.80079e-05, None, 0.00184504, None, -2.80079e-05, None, 0.00140548, None, -2.45249e-05, None, 0.00140548, None, -2.45249e-05, None, 0.169743, None, 0.00470956, None, 0.169743, None, 0.00470956, None)

reports.append(Report(604050560, ("CSC", 2, 1, 1, 16), "MEm11_16"))
reports[-1].posNum = 104248
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00151526, 0.00054242, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0831594, 0.0402029, 0), \
                           ValErr(-0.00057611, 0.00106135, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.78055e-06, 1.40093e-05, 0), \
                           37039.3, 104248, 104248, -nan)
reports[-1].sigmaresid = ValErr(0.169613, 0.000371458, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00132754, None, -5.15569e-06, None, 0.00149417, None, -1.39744e-05, None, 0.00149417, None, -1.39744e-05, None, 0.00049308, None, -7.52116e-06, None, 0.00049308, None, -7.52116e-06, None, 0.169616, None, 0.00434613, None, 0.169616, None, 0.00434613, None)

reports.append(Report(604050576, ("CSC", 2, 1, 1, 18), "MEm11_18"))
reports[-1].posNum = 104452
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0016055, 0.000541396, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0714125, 0.0401567, 0), \
                           ValErr(-0.000634714, 0.00105684, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.07076e-05, 1.40176e-05, 0), \
                           37054.3, 104452, 104452, -nan)
reports[-1].sigmaresid = ValErr(0.169706, 0.000371299, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00107044, None, -1.22542e-06, None, 0.00141032, None, -3.80646e-05, None, 0.00141032, None, -3.80646e-05, None, 3.96117e-05, None, -2.33827e-07, None, 3.96117e-05, None, -2.33827e-07, None, 0.16971, None, 0.00454271, None, 0.16971, None, 0.00454271, None)

reports.append(Report(604050592, ("CSC", 2, 1, 1, 20), "MEm11_20"))
reports[-1].posNum = 104066
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00191307, 0.000543683, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0668346, 0.0402917, 0), \
                           ValErr(-0.001206, 0.00106596, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.11413e-05, 1.40486e-05, 0), \
                           36651, 104066, 104066, -nan)
reports[-1].sigmaresid = ValErr(0.170141, 0.000372941, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00225106, None, -6.69283e-06, None, 0.00181193, None, -3.25984e-05, None, 0.00181193, None, -3.25984e-05, None, 0.0014741, None, -2.14116e-05, None, 0.0014741, None, -2.14116e-05, None, 0.170144, None, 0.00434101, None, 0.170144, None, 0.00434101, None)

reports.append(Report(604050608, ("CSC", 2, 1, 1, 22), "MEm11_22"))
reports[-1].posNum = 103876
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00239762, 0.000542112, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.168127, 0.0402444, 0), \
                           ValErr(-0.00154074, 0.00106678, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.83647e-05, 1.4074e-05, 0), \
                           36938.1, 103876, 103876, -nan)
reports[-1].sigmaresid = ValErr(0.169562, 0.000372011, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00262475, None, -1.24275e-05, None, 0.00268099, None, -2.61316e-05, None, 0.00268099, None, -2.61316e-05, None, 0.00186422, None, -2.85428e-05, None, 0.00186422, None, -2.85428e-05, None, 0.16958, None, 0.00457571, None, 0.16958, None, 0.00457571, None)

reports.append(Report(604050624, ("CSC", 2, 1, 1, 24), "MEm11_24"))
reports[-1].posNum = 103893
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00290315, 0.000543432, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.106489, 0.0402429, 0), \
                           ValErr(-0.00112285, 0.00106009, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.72151e-05, 1.40331e-05, 0), \
                           36664.9, 103893, 103893, -nan)
reports[-1].sigmaresid = ValErr(0.170018, 0.000372982, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00287093, None, -1.41802e-05, None, 0.00265273, None, -2.75945e-05, None, 0.00265273, None, -2.75945e-05, None, 0.00067562, None, 2.40243e-06, None, 0.00067562, None, 2.40243e-06, None, 0.170027, None, 0.00593431, None, 0.170027, None, 0.00593431, None)

reports.append(Report(604050640, ("CSC", 2, 1, 1, 26), "MEm11_26"))
reports[-1].posNum = 104486
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00173008, 0.000539936, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.193544, 0.0400302, 0), \
                           ValErr(-0.00311579, 0.0010592, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.11528e-06, 1.39774e-05, 0), \
                           37318.9, 104486, 104486, -nan)
reports[-1].sigmaresid = ValErr(0.169296, 0.000370343, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00181168, None, -6.5485e-06, None, 0.00166973, None, -2.78531e-05, None, 0.00166973, None, -2.78531e-05, None, -0.000383069, None, -7.18402e-06, None, -0.000383069, None, -7.18402e-06, None, 0.169318, None, 0.00445645, None, 0.169318, None, 0.00445645, None)

reports.append(Report(604050656, ("CSC", 2, 1, 1, 28), "MEm11_28"))
reports[-1].posNum = 104353
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00237258, 0.000542646, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0806849, 0.0403098, 0), \
                           ValErr(-0.00153248, 0.00106421, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.09271e-08, 1.4056e-05, 0), \
                           36709.2, 104353, 104353, -nan)
reports[-1].sigmaresid = ValErr(0.170211, 0.00037258, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00296752, None, -3.41587e-06, None, 0.00237468, None, -9.70208e-06, None, 0.00237468, None, -9.70208e-06, None, 0.00170987, None, -3.51369e-06, None, 0.00170987, None, -3.51369e-06, None, 0.170215, None, 0.00434614, None, 0.170215, None, 0.00434614, None)

reports.append(Report(604050672, ("CSC", 2, 1, 1, 30), "MEm11_30"))
reports[-1].posNum = 104184
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00152451, 0.000541965, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.107566, 0.0401324, 0), \
                           ValErr(-0.00225094, 0.00106255, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.32509e-05, 1.40418e-05, 0), \
                           36954.6, 104184, 104184, -nan)
reports[-1].sigmaresid = ValErr(0.169714, 0.000371793, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00211622, None, -9.1978e-06, None, 0.00175009, None, -3.74025e-05, None, 0.00175009, None, -3.74025e-05, None, 0.00199454, None, -2.40639e-05, None, 0.00199454, None, -2.40639e-05, None, 0.169723, None, 0.00440324, None, 0.169723, None, 0.00440324, None)

reports.append(Report(604050688, ("CSC", 2, 1, 1, 32), "MEm11_32"))
reports[-1].posNum = 104627
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00183428, 0.000542533, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.199158, 0.0404152, 0), \
                           ValErr(-0.00211174, 0.00106591, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(8.47218e-06, 1.40226e-05, 0), \
                           36662.9, 104627, 104627, -nan)
reports[-1].sigmaresid = ValErr(0.170443, 0.0003726, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00206205, None, -1.68738e-05, None, 0.00192883, None, -3.24092e-05, None, 0.00192883, None, -3.24092e-05, None, 0.00158478, None, -2.17524e-05, None, 0.00158478, None, -2.17524e-05, None, 0.170463, None, 0.00426505, None, 0.170463, None, 0.00426505, None)

reports.append(Report(604050704, ("CSC", 2, 1, 1, 34), "MEm11_34"))
reports[-1].posNum = 104034
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00195854, 0.000540367, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.123829, 0.0400208, 0), \
                           ValErr(-0.00227864, 0.00105911, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.17169e-05, 1.40059e-05, 0), \
                           37233, 104034, 104034, -nan)
reports[-1].sigmaresid = ValErr(0.169173, 0.000370877, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00101865, None, 6.0495e-06, None, 0.00186829, None, -1.85098e-05, None, 0.00186829, None, -1.85098e-05, None, 0.00224109, None, -1.89329e-05, None, 0.00224109, None, -1.89329e-05, None, 0.169183, None, 0.00491552, None, 0.169183, None, 0.00491552, None)

reports.append(Report(604050720, ("CSC", 2, 1, 1, 36), "MEm11_36"))
reports[-1].posNum = 104555
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0022891, 0.00054506, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0412702, 0.0404649, 0), \
                           ValErr(-0.000852956, 0.00106602, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.78079e-06, 1.40837e-05, 0), \
                           36278.6, 104555, 104555, -nan)
reports[-1].sigmaresid = ValErr(0.171029, 0.00037401, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00213323, None, -5.36013e-06, None, 0.00220062, None, -1.42244e-05, None, 0.00220062, None, -1.42244e-05, None, 0.00037167, None, -2.83137e-05, None, 0.00037167, None, -2.83137e-05, None, 0.171031, None, 0.00450462, None, 0.171031, None, 0.00450462, None)

reports.append(Report(604050952, ("CSC", 2, 1, 2, 1), "MEm12_01"))
reports[-1].posNum = 50496
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00166478, 0.00262871, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.035731, 0.106411, 0), \
                           ValErr(0.00052821, 0.0022874, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.0973e-05, 5.55092e-05, 0), \
                           -42646.8, 50496, 50496, -nan)
reports[-1].sigmaresid = ValErr(0.563054, 0.00177177, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000224156, None, -1.17677e-05, None, -0.00107046, None, -2.25516e-05, None, -0.00107046, None, -2.25516e-05, None, 0.00169213, None, -8.01809e-06, None, 0.00169213, None, -8.01809e-06, None, 0.563058, None, 0.00423302, None, 0.563058, None, 0.00423302, None)

reports.append(Report(604050968, ("CSC", 2, 1, 2, 3), "MEm12_03"))
reports[-1].posNum = 47525
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00435608, 0.0026487, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.072651, 0.106118, 0), \
                           ValErr(0.00244414, 0.00228103, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.53583e-06, 5.55694e-05, 0), \
                           -38005, 47525, 47525, -nan)
reports[-1].sigmaresid = ValErr(0.538345, 0.00174616, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00412357, None, -5.82448e-06, None, 0.00446421, None, -1.78309e-05, None, 0.00446421, None, -1.78309e-05, None, 0.0091068, None, -1.74844e-05, None, 0.0091068, None, -1.74844e-05, None, 0.538354, None, 0.00457257, None, 0.538354, None, 0.00457257, None)

reports.append(Report(604050984, ("CSC", 2, 1, 2, 5), "MEm12_05"))
reports[-1].posNum = 50025
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000191027, 0.00260176, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.111256, 0.107309, 0), \
                           ValErr(-0.00369907, 0.00235386, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.52027e-05, 5.51367e-05, 0), \
                           -41501.9, 50025, 50025, -nan)
reports[-1].sigmaresid = ValErr(0.554707, 0.0017537, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00207266, None, 2.05739e-06, None, -0.000556576, None, 2.27381e-05, None, -0.000556576, None, 2.27381e-05, None, 0.00307105, None, -3.09917e-05, None, 0.00307105, None, -3.09917e-05, None, 0.55473, None, 0.00423599, None, 0.55473, None, 0.00423599, None)

reports.append(Report(604051000, ("CSC", 2, 1, 2, 7), "MEm12_07"))
reports[-1].posNum = 47779
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00151417, 0.00269838, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0483035, 0.107877, 0), \
                           ValErr(-0.00324345, 0.00232676, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.49473e-05, 5.67927e-05, 0), \
                           -39469.3, 47779, 47779, -nan)
reports[-1].sigmaresid = ValErr(0.552747, 0.00178811, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(8.07736e-05, None, 6.53693e-06, None, -0.000667524, None, 5.97537e-06, None, -0.000667524, None, 5.97537e-06, None, -0.00330367, None, 3.56126e-06, None, -0.00330367, None, 3.56126e-06, None, 0.552763, None, 0.00421954, None, 0.552763, None, 0.00421954, None)

reports.append(Report(604051016, ("CSC", 2, 1, 2, 9), "MEm12_09"))
reports[-1].posNum = 49041
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00111688, 0.00265175, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.184905, 0.109772, 0), \
                           ValErr(-0.00383288, 0.00238051, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.37535e-05, 5.57475e-05, 0), \
                           -40706.4, 49041, 49041, -nan)
reports[-1].sigmaresid = ValErr(0.554944, 0.00177197, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00221379, None, 1.15308e-05, None, 0.00206383, None, 2.45581e-05, None, 0.00206383, None, 2.45581e-05, None, 0.00335223, None, 5.30969e-06, None, 0.00335223, None, 5.30969e-06, None, 0.554975, None, 0.00423122, None, 0.554975, None, 0.00423122, None)

reports.append(Report(604051032, ("CSC", 2, 1, 2, 11), "MEm12_11"))
reports[-1].posNum = 48917
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000769656, 0.00264313, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.00778889, 0.109373, 0), \
                           ValErr(-0.00122176, 0.00238436, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.25263e-05, 5.56286e-05, 0), \
                           -40127.6, 48917, 48917, -nan)
reports[-1].sigmaresid = ValErr(0.549571, 0.00175703, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000418079, None, 1.5267e-05, None, 0.000392544, None, 1.222e-05, None, 0.000392544, None, 1.222e-05, None, 0.000203593, None, 7.51323e-06, None, 0.000203593, None, 7.51323e-06, None, 0.549573, None, 0.00420991, None, 0.549573, None, 0.00420991, None)

reports.append(Report(604051048, ("CSC", 2, 1, 2, 13), "MEm12_13"))
reports[-1].posNum = 47013
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00201456, 0.00272796, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.139551, 0.108561, 0), \
                           ValErr(-0.000303232, 0.00234952, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(9.67663e-05, 5.73658e-05, 0), \
                           -38406.4, 47013, 47013, -nan)
reports[-1].sigmaresid = ValErr(0.547711, 0.00178619, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00216552, None, 5.64283e-06, None, -0.000185267, None, 1.79248e-06, None, -0.000185267, None, 1.79248e-06, None, -0.00172872, None, -2.1048e-05, None, -0.00172872, None, -2.1048e-05, None, 0.547737, None, 0.00415015, None, 0.547737, None, 0.00415015, None)

reports.append(Report(604051064, ("CSC", 2, 1, 2, 15), "MEm12_15"))
reports[-1].posNum = 50576
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00624416, 0.00257374, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0459676, 0.104731, 0), \
                           ValErr(-0.00164964, 0.00226796, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.42494e-05, 5.41691e-05, 0), \
                           -41763.1, 50576, 50576, -nan)
reports[-1].sigmaresid = ValErr(0.552562, 0.00173738, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00527784, None, 6.16191e-06, None, -0.00533685, None, -7.75372e-06, None, -0.00533685, None, -7.75372e-06, None, -0.00808856, None, 2.36877e-05, None, -0.00808856, None, 2.36877e-05, None, 0.552574, None, 0.0042215, None, 0.552574, None, 0.0042215, None)

reports.append(Report(604051080, ("CSC", 2, 1, 2, 17), "MEm12_17"))
reports[-1].posNum = 47654
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000453329, 0.00267323, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0752123, 0.10883, 0), \
                           ValErr(0.000796074, 0.00237041, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.67285e-05, 5.65429e-05, 0), \
                           -38379.8, 47654, 47654, -nan)
reports[-1].sigmaresid = ValErr(0.541423, 0.00175377, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000324168, None, 1.97041e-05, None, 0.000555859, None, 3.1123e-06, None, 0.000555859, None, 3.1123e-06, None, -0.00685625, None, -6.17006e-06, None, -0.00685625, None, -6.17006e-06, None, 0.541432, None, 0.00424907, None, 0.541432, None, 0.00424907, None)

reports.append(Report(604051096, ("CSC", 2, 1, 2, 19), "MEm12_19"))
reports[-1].posNum = 50578
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00273806, 0.00259971, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.105634, 0.105444, 0), \
                           ValErr(0.00381033, 0.00227258, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.97106e-05, 5.50277e-05, 0), \
                           -42338.3, 50578, 50578, -nan)
reports[-1].sigmaresid = ValErr(0.558866, 0.00175717, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00629275, None, 3.00033e-06, None, 0.00218604, None, -2.66565e-06, None, 0.00218604, None, -2.66565e-06, None, 0.00326285, None, 3.48061e-06, None, 0.00326285, None, 3.48061e-06, None, 0.558889, None, 0.00409234, None, 0.558889, None, 0.00409234, None)

reports.append(Report(604051112, ("CSC", 2, 1, 2, 21), "MEm12_21"))
reports[-1].posNum = 46786
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000899635, 0.0026993, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.135293, 0.110066, 0), \
                           ValErr(-0.00292852, 0.0023946, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.93397e-05, 5.67771e-05, 0), \
                           -37264.4, 46786, 46786, -nan)
reports[-1].sigmaresid = ValErr(0.536627, 0.00175428, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00279603, None, 6.09257e-06, None, 0.000428923, None, 1.03369e-05, None, 0.000428923, None, 1.03369e-05, None, 0.000441372, None, 3.86689e-06, None, 0.000441372, None, 3.86689e-06, None, 0.536658, None, 0.0041882, None, 0.536658, None, 0.0041882, None)

reports.append(Report(604051128, ("CSC", 2, 1, 2, 23), "MEm12_23"))
reports[-1].posNum = 50504
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000454181, 0.00258417, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0305121, 0.106367, 0), \
                           ValErr(0.000454337, 0.00231439, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000157544, 5.44956e-05, 0), \
                           -41908.1, 50504, 50504, -nan)
reports[-1].sigmaresid = ValErr(0.554807, 0.00174569, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00184046, None, -1.95858e-05, None, 0.00176149, None, -1.98979e-05, None, 0.00176149, None, -1.98979e-05, None, 0.00263809, None, 6.67696e-06, None, 0.00263809, None, 6.67696e-06, None, 0.554851, None, 0.00421912, None, 0.554851, None, 0.00421912, None)

reports.append(Report(604051144, ("CSC", 2, 1, 2, 25), "MEm12_25"))
reports[-1].posNum = 48313
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00156448, 0.00268156, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.12247, 0.10826, 0), \
                           ValErr(0.00130285, 0.00233676, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.97893e-05, 5.64647e-05, 0), \
                           -39732.9, 48313, 48313, -nan)
reports[-1].sigmaresid = ValErr(0.550718, 0.00177167, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00524075, None, -3.53042e-05, None, 0.0025765, None, -2.33823e-05, None, 0.0025765, None, -2.33823e-05, None, 0.00490599, None, -1.48631e-05, None, 0.00490599, None, -1.48631e-05, None, 0.550735, None, 0.00414865, None, 0.550735, None, 0.00414865, None)

reports.append(Report(604051160, ("CSC", 2, 1, 2, 27), "MEm12_27"))
reports[-1].posNum = 48813
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00849823, 0.00264499, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.133022, 0.10717, 0), \
                           ValErr(-0.00142688, 0.0023156, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(8.48255e-05, 5.55961e-05, 0), \
                           -40179.3, 48813, 48813, -nan)
reports[-1].sigmaresid = ValErr(0.551116, 0.00176385, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00438096, None, 3.16802e-05, None, -0.00707372, None, 3.67945e-05, None, -0.00707372, None, 3.67945e-05, None, -0.00834893, None, 2.36465e-05, None, -0.00834893, None, 2.36465e-05, None, 0.551137, None, 0.00427287, None, 0.551137, None, 0.00427287, None)

reports.append(Report(604051176, ("CSC", 2, 1, 2, 29), "MEm12_29"))
reports[-1].posNum = 48895
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00113932, 0.00265019, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.19523, 0.108283, 0), \
                           ValErr(0.0022894, 0.00236185, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.62683e-05, 5.58558e-05, 0), \
                           -40505, 48895, 48895, -nan)
reports[-1].sigmaresid = ValErr(0.554034, 0.0017717, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000366478, None, 8.0777e-07, None, -0.0014668, None, -2.41723e-05, None, -0.0014668, None, -2.41723e-05, None, 0.000987296, None, 7.75616e-06, None, 0.000987296, None, 7.75616e-06, None, 0.55406, None, 0.00422168, None, 0.55406, None, 0.00422168, None)

reports.append(Report(604051192, ("CSC", 2, 1, 2, 31), "MEm12_31"))
reports[-1].posNum = 48510
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00295551, 0.00266873, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0725925, 0.106501, 0), \
                           ValErr(0.0025991, 0.00229805, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.80271e-05, 5.63613e-05, 0), \
                           -39792.6, 48510, 48510, -nan)
reports[-1].sigmaresid = ValErr(0.549558, 0.00176434, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00499806, None, -1.26701e-05, None, 0.00249548, None, -3.81122e-06, None, 0.00249548, None, -3.81122e-06, None, 0.0032899, None, 2.44578e-06, None, 0.0032899, None, 2.44578e-06, None, 0.54957, None, 0.00414791, None, 0.54957, None, 0.00414791, None)

reports.append(Report(604051208, ("CSC", 2, 1, 2, 33), "MEm12_33"))
reports[-1].posNum = 50113
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00109619, 0.00261036, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0870695, 0.106241, 0), \
                           ValErr(-0.00362229, 0.0022756, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.15752e-05, 5.48757e-05, 0), \
                           -41772.8, 50113, 50113, -nan)
reports[-1].sigmaresid = ValErr(0.556903, 0.0017591, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00167842, None, -1.09431e-05, None, 0.000635416, None, -3.10814e-05, None, 0.000635416, None, -3.10814e-05, None, -0.00483799, None, -2.61715e-06, None, -0.00483799, None, -2.61715e-06, None, 0.556922, None, 0.00432399, None, 0.556922, None, 0.00432399, None)

reports.append(Report(604051224, ("CSC", 2, 1, 2, 35), "MEm12_35"))
reports[-1].posNum = 46447
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00664138, 0.0027349, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0123405, 0.112537, 0), \
                           ValErr(0.00305676, 0.00246594, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.93566e-05, 5.7535e-05, 0), \
                           -37096.9, 46447, 46447, -nan)
reports[-1].sigmaresid = ValErr(0.537813, 0.00176456, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00492615, None, -7.77789e-06, None, -0.00549988, None, -2.06171e-06, None, -0.00549988, None, -2.06171e-06, None, -0.00558198, None, 1.49085e-05, None, -0.00558198, None, 1.49085e-05, None, 0.537829, None, 0.00410394, None, 0.537829, None, 0.00410394, None)

reports.append(Report(604050960, ("CSC", 2, 1, 2, 2), "MEm12_02"))
reports[-1].posNum = 47397
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00223593, 0.00261471, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0406605, 0.102778, 0), \
                           ValErr(-0.000786894, 0.00219562, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000128353, 5.4178e-05, 0), \
                           -37517.2, 47397, 47397, -nan)
reports[-1].sigmaresid = ValErr(0.533986, 0.00173436, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00578189, None, -5.7474e-05, None, 0.00435271, None, -4.08256e-05, None, 0.00435271, None, -4.08256e-05, None, 0.00505273, None, -3.99255e-05, None, 0.00505273, None, -3.99255e-05, None, 0.534019, None, 0.00424701, None, 0.534019, None, 0.00424701, None)

reports.append(Report(604050976, ("CSC", 2, 1, 2, 4), "MEm12_04"))
reports[-1].posNum = 44951
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00441632, 0.00268283, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0228598, 0.103695, 0), \
                           ValErr(-0.00163316, 0.00217429, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.92744e-05, 5.51066e-05, 0), \
                           -35018, 44951, 44951, -nan)
reports[-1].sigmaresid = ValErr(0.527339, 0.00175875, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00607298, None, -6.49529e-05, None, 0.00552527, None, -3.55242e-05, None, 0.00552527, None, -3.55242e-05, None, 0.00341601, None, 1.50028e-05, None, 0.00341601, None, 1.50028e-05, None, 0.527349, None, 0.00533708, None, 0.527349, None, 0.00533708, None)

reports.append(Report(604050992, ("CSC", 2, 1, 2, 6), "MEm12_06"))
reports[-1].posNum = 49543
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00215066, 0.00254682, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0177705, 0.0991013, 0), \
                           ValErr(-0.00252005, 0.00210507, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.58583e-05, 5.30166e-05, 0), \
                           -39834.3, 49543, 49543, -nan)
reports[-1].sigmaresid = ValErr(0.540694, 0.00171769, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00178788, None, -1.78378e-05, None, 0.00161872, None, -5.1843e-06, None, 0.00161872, None, -5.1843e-06, None, 0.00103122, None, -1.05649e-05, None, 0.00103122, None, -1.05649e-05, None, 0.540704, None, 0.00400954, None, 0.540704, None, 0.00400954, None)

reports.append(Report(604051008, ("CSC", 2, 1, 2, 8), "MEm12_08"))
reports[-1].posNum = 45308
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0012443, 0.00264981, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0999495, 0.101256, 0), \
                           ValErr(-0.00543284, 0.00213146, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.64001e-05, 5.43014e-05, 0), \
                           -34505.5, 45308, 45308, -nan)
reports[-1].sigmaresid = ValErr(0.518216, 0.0017215, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000583307, None, 1.31405e-07, None, 0.000765043, None, 1.6919e-05, None, 0.000765043, None, 1.6919e-05, None, 0.00166593, None, -2.1667e-05, None, 0.00166593, None, -2.1667e-05, None, 0.518256, None, 0.00413213, None, 0.518256, None, 0.00413213, None)

reports.append(Report(604051024, ("CSC", 2, 1, 2, 10), "MEm12_10"))
reports[-1].posNum = 50962
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00127804, 0.00249459, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.136011, 0.0975453, 0), \
                           ValErr(-0.00168722, 0.00207802, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.3545e-06, 5.21472e-05, 0), \
                           -40951.1, 50962, 50962, -nan)
reports[-1].sigmaresid = ValErr(0.540438, 0.00169281, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00253202, None, 5.07472e-06, None, -0.00135332, None, 2.12384e-05, None, -0.00135332, None, 2.12384e-05, None, 0.0069662, None, -1.50276e-05, None, 0.0069662, None, -1.50276e-05, None, 0.54045, None, 0.00394061, None, 0.54045, None, 0.00394061, None)

reports.append(Report(604051040, ("CSC", 2, 1, 2, 12), "MEm12_12"))
reports[-1].posNum = 46527
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000486434, 0.00258518, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0494859, 0.0982438, 0), \
                           ValErr(-0.000531525, 0.00207561, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.26859e-06, 5.3139e-05, 0), \
                           -35461.8, 46527, 46527, -nan)
reports[-1].sigmaresid = ValErr(0.518528, 0.00169983, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000341326, None, 6.81805e-06, None, 0.000497957, None, 1.23818e-05, None, 0.000497957, None, 1.23818e-05, None, 0.00208121, None, -9.04589e-06, None, 0.00208121, None, -9.04589e-06, None, 0.51853, None, 0.00408167, None, 0.51853, None, 0.00408167, None)

reports.append(Report(604051056, ("CSC", 2, 1, 2, 14), "MEm12_14"))
reports[-1].posNum = 49841
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000786586, 0.00249958, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.102631, 0.0970904, 0), \
                           ValErr(-0.00133462, 0.0020742, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.2863e-05, 5.18443e-05, 0), \
                           -39058.7, 49841, 49841, -nan)
reports[-1].sigmaresid = ValErr(0.529791, 0.00167802, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00410326, None, 3.26537e-06, None, 0.000131452, None, 4.19011e-05, None, 0.000131452, None, 4.19011e-05, None, 0.00545253, None, -1.11006e-05, None, 0.00545253, None, -1.11006e-05, None, 0.529804, None, 0.00407596, None, 0.529804, None, 0.00407596, None)

reports.append(Report(604051072, ("CSC", 2, 1, 2, 16), "MEm12_16"))
reports[-1].posNum = 47112
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000136845, 0.00261512, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.106889, 0.10296, 0), \
                           ValErr(-0.000719466, 0.00214382, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(9.06072e-05, 5.35514e-05, 0), \
                           -37025.5, 47112, 47112, -nan)
reports[-1].sigmaresid = ValErr(0.530978, 0.0017298, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00428368, None, -3.24151e-05, None, 0.00173521, None, -3.35983e-05, None, 0.00173521, None, -3.35983e-05, None, 0.000122402, None, -1.59051e-05, None, 0.000122402, None, -1.59051e-05, None, 0.531002, None, 0.00428439, None, 0.531002, None, 0.00428439, None)

reports.append(Report(604051088, ("CSC", 2, 1, 2, 18), "MEm12_18"))
reports[-1].posNum = 47948
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0030278, 0.00256315, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0671054, 0.0994295, 0), \
                           ValErr(-0.00146635, 0.0020884, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.58953e-05, 5.27548e-05, 0), \
                           -37451.6, 47948, 47948, -nan)
reports[-1].sigmaresid = ValErr(0.528427, 0.00170642, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00314134, None, 2.01986e-05, None, -0.00277734, None, 2.38191e-05, None, -0.00277734, None, 2.38191e-05, None, 0.00269432, None, -1.22374e-05, None, 0.00269432, None, -1.22374e-05, None, 0.528433, None, 0.0039408, None, 0.528433, None, 0.0039408, None)

reports.append(Report(604051104, ("CSC", 2, 1, 2, 20), "MEm12_20"))
reports[-1].posNum = 49390
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00076106, 0.00255746, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.03378, 0.0995494, 0), \
                           ValErr(0.00233884, 0.00213744, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.59641e-05, 5.33095e-05, 0), \
                           -39408.9, 49390, 49390, -nan)
reports[-1].sigmaresid = ValErr(0.537394, 0.00170985, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00053682, None, 1.36043e-05, None, -0.000101545, None, 2.00304e-05, None, -0.000101545, None, 2.00304e-05, None, -0.000498826, None, 1.95493e-05, None, -0.000498826, None, 1.95493e-05, None, 0.537406, None, 0.00395693, None, 0.537406, None, 0.00395693, None)

reports.append(Report(604051120, ("CSC", 2, 1, 2, 22), "MEm12_22"))
reports[-1].posNum = 46502
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000356896, 0.0026338, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.018144, 0.101726, 0), \
                           ValErr(-0.000846556, 0.00216712, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.02106e-05, 5.45293e-05, 0), \
                           -36795.6, 46502, 46502, -nan)
reports[-1].sigmaresid = ValErr(0.533834, 0.00175047, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00110466, None, -2.04308e-05, None, 0.000468384, None, -1.87212e-05, None, 0.000468384, None, -1.87212e-05, None, -0.00294868, None, -2.51312e-05, None, -0.00294868, None, -2.51312e-05, None, 0.533841, None, 0.00417466, None, 0.533841, None, 0.00417466, None)

reports.append(Report(604051136, ("CSC", 2, 1, 2, 24), "MEm12_24"))
reports[-1].posNum = 49159
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000206629, 0.00250441, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0286204, 0.0967079, 0), \
                           ValErr(0.00035316, 0.00207518, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.26259e-05, 5.22419e-05, 0), \
                           -37993.2, 49159, 49159, -nan)
reports[-1].sigmaresid = ValErr(0.524101, 0.00167147, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00109959, None, 3.35682e-06, None, 0.0003261, None, 1.56959e-07, None, 0.0003261, None, 1.56959e-07, None, 0.000154992, None, -7.21528e-06, None, 0.000154992, None, -7.21528e-06, None, 0.524102, None, 0.00384636, None, 0.524102, None, 0.00384636, None)

reports.append(Report(604051152, ("CSC", 2, 1, 2, 26), "MEm12_26"))
reports[-1].posNum = 45564
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000956479, 0.00260505, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0774839, 0.100218, 0), \
                           ValErr(-0.00193269, 0.00213152, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.92712e-05, 5.37887e-05, 0), \
                           -34175.8, 45564, 45564, -nan)
reports[-1].sigmaresid = ValErr(0.512283, 0.00169701, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00474972, None, -1.8907e-05, None, 0.000157242, None, 6.53253e-06, None, 0.000157242, None, 6.53253e-06, None, 0.000810028, None, -8.29295e-06, None, 0.000810028, None, -8.29295e-06, None, 0.5123, None, 0.00401913, None, 0.5123, None, 0.00401913, None)

reports.append(Report(604051168, ("CSC", 2, 1, 2, 28), "MEm12_28"))
reports[-1].posNum = 50460
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00251109, 0.00252747, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0902748, 0.0983599, 0), \
                           ValErr(0.00230956, 0.00210455, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.41193e-05, 5.26749e-05, 0), \
                           -40694.9, 50460, 50460, -nan)
reports[-1].sigmaresid = ValErr(0.542016, 0.00170618, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00363801, None, -1.87985e-06, None, 0.00270853, None, 7.62982e-06, None, 0.00270853, None, 7.62982e-06, None, 0.00403312, None, -2.50311e-06, None, 0.00403312, None, -2.50311e-06, None, 0.542029, None, 0.00385893, None, 0.542029, None, 0.00385893, None)

reports.append(Report(604051184, ("CSC", 2, 1, 2, 30), "MEm12_30"))
reports[-1].posNum = 45515
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0104616, 0.0026029, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0241716, 0.100508, 0), \
                           ValErr(-0.00253717, 0.00209387, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.37503e-05, 5.30856e-05, 0), \
                           -34145, 45515, 45515, -nan)
reports[-1].sigmaresid = ValErr(0.512351, 0.00169815, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00704977, None, -5.11641e-05, None, 0.00942119, None, -6.19645e-05, None, 0.00942119, None, -6.19645e-05, None, 0.0120574, None, -8.30231e-05, None, 0.0120574, None, -8.30231e-05, None, 0.512365, None, 0.00423292, None, 0.512365, None, 0.00423292, None)

reports.append(Report(604051200, ("CSC", 2, 1, 2, 32), "MEm12_32"))
reports[-1].posNum = 50068
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00160407, 0.00252252, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0783199, 0.0977271, 0), \
                           ValErr(-0.000306762, 0.0020872, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.35944e-05, 5.23491e-05, 0), \
                           -39964.6, 50068, 50068, -nan)
reports[-1].sigmaresid = ValErr(0.537551, 0.00169873, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00360075, None, 2.00657e-05, None, -0.000823161, None, 2.2249e-06, None, -0.000823161, None, 2.2249e-06, None, 0.000751671, None, -5.81816e-06, None, 0.000751671, None, -5.81816e-06, None, 0.53756, None, 0.00419538, None, 0.53756, None, 0.00419538, None)

reports.append(Report(604051216, ("CSC", 2, 1, 2, 34), "MEm12_34"))
reports[-1].posNum = 48322
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0042038, 0.0025878, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.120922, 0.100986, 0), \
                           ValErr(-0.00244911, 0.00213456, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.14794e-05, 5.35734e-05, 0), \
                           -38506, 48322, 48322, -nan)
reports[-1].sigmaresid = ValErr(0.53683, 0.00172683, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000505049, None, -3.64986e-05, None, 0.00288706, None, -2.59944e-05, None, 0.00288706, None, -2.59944e-05, None, 0.00465035, None, -4.95975e-05, None, 0.00465035, None, -4.95975e-05, None, 0.53686, None, 0.00423715, None, 0.53686, None, 0.00423715, None)

reports.append(Report(604051232, ("CSC", 2, 1, 2, 36), "MEm12_36"))
reports[-1].posNum = 49360
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00334766, 0.00252876, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0758913, 0.0972866, 0), \
                           ValErr(0.00244633, 0.00207773, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.59033e-06, 5.2653e-05, 0), \
                           -39094.5, 49360, 49360, -nan)
reports[-1].sigmaresid = ValErr(0.534239, 0.00170033, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00116654, None, 2.12015e-05, None, -0.00336767, None, 2.64318e-05, None, -0.00336767, None, 2.64318e-05, None, -0.00289253, None, 2.84392e-05, None, -0.00289253, None, 2.84392e-05, None, 0.534251, None, 0.00421237, None, 0.534251, None, 0.00421237, None)

reports.append(Report(604051464, ("CSC", 2, 1, 3, 1), "MEm13_01"))
reports[-1].posNum = 19871
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0256033, 0.010734, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.31918, 0.30653, 0), \
                           ValErr(-0.00586101, 0.00689361, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000252213, 0.000240217, 0), \
                           -36284.5, 19871, 19871, -nan)
reports[-1].sigmaresid = ValErr(1.50241, 0.00753646, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0229124, None, 8.86601e-05, None, -0.0267205, None, 0.000134508, None, -0.0267205, None, 0.000134508, None, -0.0345424, None, 6.85438e-05, None, -0.0345424, None, 6.85438e-05, None, 1.50462, None, 0.00643308, None, 1.50462, None, 0.00643308, None)

reports.append(Report(604051472, ("CSC", 2, 1, 3, 2), "MEm13_02"))
reports[-1].posNum = 19217
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0110778, 0.0108994, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.75023, 0.31741, 0), \
                           ValErr(-0.00237003, 0.00720922, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000160972, 0.000246705, 0), \
                           -35121.5, 19217, 19217, -nan)
reports[-1].sigmaresid = ValErr(1.50484, 0.00767595, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0190821, None, -9.20788e-06, None, -0.0114062, None, 7.7245e-05, None, -0.0114062, None, 7.7245e-05, None, -0.0142802, None, 7.65742e-05, None, -0.0142802, None, 7.65742e-05, None, 1.50779, None, 0.00687177, None, 1.50779, None, 0.00687177, None)

reports.append(Report(604051480, ("CSC", 2, 1, 3, 3), "MEm13_03"))
reports[-1].posNum = 18235
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0207206, 0.0113587, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.50145, 0.336601, 0), \
                           ValErr(4.1709e-05, 0.00776925, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.94099e-05, 0.000261919, 0), \
                           -33665.9, 18235, 18235, -nan)
reports[-1].sigmaresid = ValErr(1.53309, 0.00802784, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0237705, None, 0.000139602, None, -0.0220496, None, 0.000164079, None, -0.0220496, None, 0.000164079, None, -0.0243896, None, 0.000149667, None, -0.0243896, None, 0.000149667, None, 1.53547, None, 0.00699712, None, 1.53547, None, 0.00699712, None)

reports.append(Report(604051488, ("CSC", 2, 1, 3, 4), "MEm13_04"))
reports[-1].posNum = 18498
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0103657, 0.0113135, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.63132, 0.343342, 0), \
                           ValErr(-0.016229, 0.00800085, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000292441, 0.000260728, 0), \
                           -34200.7, 18498, 18498, -nan)
reports[-1].sigmaresid = ValErr(1.53718, 0.00799186, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0359809, None, 4.14007e-05, None, -0.0108235, None, 8.30856e-05, None, -0.0108235, None, 8.30856e-05, None, -0.00982294, None, 8.46724e-05, None, -0.00982294, None, 8.46724e-05, None, 1.53966, None, 0.00660891, None, 1.53966, None, 0.00660891, None)

reports.append(Report(604051496, ("CSC", 2, 1, 3, 5), "MEm13_05"))
reports[-1].posNum = 19498
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00929299, 0.0107279, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.02152, 0.311953, 0), \
                           ValErr(0.0063872, 0.00697706, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000121672, 0.000238862, 0), \
                           -35356.7, 19498, 19498, -nan)
reports[-1].sigmaresid = ValErr(1.48354, 0.00751279, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00111414, None, 3.8521e-05, None, -0.00692097, None, 9.93849e-05, None, -0.00692097, None, 9.93849e-05, None, 0.00995329, None, 3.96688e-05, None, 0.00995329, None, 3.96688e-05, None, 1.48711, None, 0.00648308, None, 1.48711, None, 0.00648308, None)

reports.append(Report(604051504, ("CSC", 2, 1, 3, 6), "MEm13_06"))
reports[-1].posNum = 19580
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0123271, 0.0106342, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.42189, 0.303707, 0), \
                           ValErr(0.0078394, 0.00685219, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000216897, 0.000237403, 0), \
                           -35403.6, 19580, 19580, -nan)
reports[-1].sigmaresid = ValErr(1.47584, 0.00745804, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00390481, None, 0.000136992, None, -0.0114341, None, 4.13817e-05, None, -0.0114341, None, 4.13817e-05, None, -0.0154812, None, 1.75955e-05, None, -0.0154812, None, 1.75955e-05, None, 1.47829, None, 0.00672569, None, 1.47829, None, 0.00672569, None)

reports.append(Report(604051512, ("CSC", 2, 1, 3, 7), "MEm13_07"))
reports[-1].posNum = 18584
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000783455, 0.0109597, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.48713, 0.315949, 0), \
                           ValErr(0.000466983, 0.00726687, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000147752, 0.000251482, 0), \
                           -33788.2, 18584, 18584, -nan)
reports[-1].sigmaresid = ValErr(1.49062, 0.00773177, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0145304, None, 2.33237e-05, None, 0.00385705, None, 2.48726e-05, None, 0.00385705, None, 2.48726e-05, None, -0.00440258, None, 1.60604e-05, None, -0.00440258, None, 1.60604e-05, None, 1.49315, None, 0.00619675, None, 1.49315, None, 0.00619675, None)

reports.append(Report(604051520, ("CSC", 2, 1, 3, 8), "MEm13_08"))
reports[-1].posNum = 17859
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00476394, 0.0113373, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.21669, 0.333149, 0), \
                           ValErr(-0.00669639, 0.00767646, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.43696e-05, 0.000263092, 0), \
                           -32753.1, 17859, 17859, -nan)
reports[-1].sigmaresid = ValErr(1.51444, 0.00801319, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00625671, None, 5.65705e-05, None, 0.00347825, None, 8.55596e-05, None, 0.00347825, None, 8.55596e-05, None, 0.0171516, None, 9.0508e-06, None, 0.0171516, None, 9.0508e-06, None, 1.51839, None, 0.00642543, None, 1.51839, None, 0.00642543, None)

reports.append(Report(604051528, ("CSC", 2, 1, 3, 9), "MEm13_09"))
reports[-1].posNum = 18631
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00568324, 0.0110495, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.49165, 0.323557, 0), \
                           ValErr(-0.00713923, 0.0072765, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000148751, 0.000248509, 0), \
                           -33973.4, 18631, 18631, -nan)
reports[-1].sigmaresid = ValErr(1.49861, 0.00776343, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000348275, None, -5.7125e-05, None, 0.00451413, None, 4.32841e-06, None, 0.00451413, None, 4.32841e-06, None, 0.0121375, None, -3.77121e-05, None, 0.0121375, None, -3.77121e-05, None, 1.50104, None, 0.0063643, None, 1.50104, None, 0.0063643, None)

reports.append(Report(604051536, ("CSC", 2, 1, 3, 10), "MEm13_10"))
reports[-1].posNum = 19671
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0145011, 0.010701, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.74304, 0.316827, 0), \
                           ValErr(0.00485402, 0.00718281, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000517564, 0.000238346, 0), \
                           -35768.9, 19671, 19671, -nan)
reports[-1].sigmaresid = ValErr(1.49096, 0.00751687, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0249482, None, 3.27725e-05, None, 0.0112031, None, 8.7505e-05, None, 0.0112031, None, 8.7505e-05, None, 0.0209524, None, 2.61195e-06, None, 0.0209524, None, 2.61195e-06, None, 1.49408, None, 0.0065733, None, 1.49408, None, 0.0065733, None)

reports.append(Report(604051544, ("CSC", 2, 1, 3, 11), "MEm13_11"))
reports[-1].posNum = 18785
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0146254, 0.01109, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.04068, 0.327552, 0), \
                           ValErr(-0.00309311, 0.00742997, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000415605, 0.000250825, 0), \
                           -34421.6, 18785, 18785, -nan)
reports[-1].sigmaresid = ValErr(1.51204, 0.00780086, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00575786, None, 6.08351e-05, None, -0.0103853, None, 0.000107034, None, -0.0103853, None, 0.000107034, None, -0.00689446, None, 2.59625e-05, None, -0.00689446, None, 2.59625e-05, None, 1.51372, None, 0.00689035, None, 1.51372, None, 0.00689035, None)

reports.append(Report(604051552, ("CSC", 2, 1, 3, 12), "MEm13_12"))
reports[-1].posNum = 17672
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0130838, 0.0114577, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.15027, 0.329197, 0), \
                           ValErr(-0.00774346, 0.00764325, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000477668, 0.000265608, 0), \
                           -32507, 17672, 17672, -nan)
reports[-1].sigmaresid = ValErr(1.52278, 0.00810001, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00394309, None, 0.000101376, None, -0.0115214, None, 0.000111283, None, -0.0115214, None, 0.000111283, None, -0.00298856, None, 7.32717e-05, None, -0.00298856, None, 7.32717e-05, None, 1.52685, None, 0.00676211, None, 1.52685, None, 0.00676211, None)

reports.append(Report(604051560, ("CSC", 2, 1, 3, 13), "MEm13_13"))
reports[-1].posNum = 18160
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0197138, 0.0112658, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.71026, 0.322037, 0), \
                           ValErr(-0.0082292, 0.00725418, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000117675, 0.000255257, 0), \
                           -33324.3, 18160, 18160, -nan)
reports[-1].sigmaresid = ValErr(1.51604, 0.00795493, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0245165, None, 0.000106474, None, -0.0233185, None, 0.000150526, None, -0.0233185, None, 0.000150526, None, 0.00425838, None, 3.39374e-05, None, 0.00425838, None, 3.39374e-05, None, 1.51901, None, 0.00648065, None, 1.51901, None, 0.00648065, None)

reports.append(Report(604051568, ("CSC", 2, 1, 3, 14), "MEm13_14"))
reports[-1].posNum = 19686
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00886981, 0.0106013, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.51288, 0.311002, 0), \
                           ValErr(-0.00368969, 0.0069997, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000151774, 0.000236773, 0), \
                           -35634.7, 19686, 19686, -nan)
reports[-1].sigmaresid = ValErr(1.47879, 0.00745271, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00665281, None, 5.42623e-05, None, -0.0108852, None, 8.49622e-05, None, -0.0108852, None, 8.49622e-05, None, 0.0203074, None, 6.77156e-05, None, 0.0203074, None, 6.77156e-05, None, 1.48125, None, 0.00667855, None, 1.48125, None, 0.00667855, None)

reports.append(Report(604051576, ("CSC", 2, 1, 3, 15), "MEm13_15"))
reports[-1].posNum = 19576
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00262771, 0.0108417, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.01073, 0.319031, 0), \
                           ValErr(-0.00995705, 0.00712408, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.00020404, 0.000239955, 0), \
                           -35747.2, 19576, 19576, -nan)
reports[-1].sigmaresid = ValErr(1.50251, 0.00759354, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0065029, None, -3.5612e-05, None, 0.00397712, None, 3.75018e-05, None, 0.00397712, None, 3.75018e-05, None, 0.01653, None, -7.02677e-05, None, 0.01653, None, -7.02677e-05, None, 1.50598, None, 0.00687426, None, 1.50598, None, 0.00687426, None)

reports.append(Report(604051584, ("CSC", 2, 1, 3, 16), "MEm13_16"))
reports[-1].posNum = 17846
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.007048, 0.0114611, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.138, 0.346763, 0), \
                           ValErr(0.0124008, 0.00805206, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.198e-05, 0.000262654, 0), \
                           -32905.2, 17846, 17846, -nan)
reports[-1].sigmaresid = ValErr(1.52943, 0.00809547, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00370139, None, -1.08159e-05, None, -0.00554817, None, 9.6463e-05, None, -0.00554817, None, 9.6463e-05, None, -0.015149, None, 6.67635e-05, None, -0.015149, None, 6.67635e-05, None, 1.53337, None, 0.00640206, None, 1.53337, None, 0.00640206, None)

reports.append(Report(604051592, ("CSC", 2, 1, 3, 17), "MEm13_17"))
reports[-1].posNum = 18443
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00475822, 0.0110849, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.85051, 0.325835, 0), \
                           ValErr(0.00270337, 0.00757801, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000243202, 0.000255321, 0), \
                           -33694, 18443, 18443, -nan)
reports[-1].sigmaresid = ValErr(1.50378, 0.00782982, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.010473, None, 0.000110556, None, 0.0072325, None, 8.93586e-05, None, 0.0072325, None, 8.93586e-05, None, -0.00692631, None, 8.12324e-05, None, -0.00692631, None, 8.12324e-05, None, 1.50701, None, 0.00691809, None, 1.50701, None, 0.00691809, None)

reports.append(Report(604051600, ("CSC", 2, 1, 3, 18), "MEm13_18"))
reports[-1].posNum = 18697
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0171525, 0.0110184, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.63932, 0.312344, 0), \
                           ValErr(0.00284639, 0.0070378, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000203077, 0.000247623, 0), \
                           -34091.6, 18697, 18697, -nan)
reports[-1].sigmaresid = ValErr(1.49846, 0.00774903, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0167509, None, 7.02993e-05, None, -0.0169883, None, 8.76835e-05, None, -0.0169883, None, 8.76835e-05, None, -0.0152298, None, 5.13204e-05, None, -0.0152298, None, 5.13204e-05, None, 1.50135, None, 0.0062752, None, 1.50135, None, 0.0062752, None)

reports.append(Report(604051608, ("CSC", 2, 1, 3, 19), "MEm13_19"))
reports[-1].posNum = 19151
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0171295, 0.0107049, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.93979, 0.306851, 0), \
                           ValErr(-0.00895416, 0.00688989, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000313909, 0.000238427, 0), \
                           -34561.4, 19151, 19151, -nan)
reports[-1].sigmaresid = ValErr(1.47071, 0.00751484, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00512702, None, 2.92879e-05, None, -0.0155803, None, 0.000124634, None, -0.0155803, None, 0.000124634, None, -0.0120709, None, 9.94746e-05, None, -0.0120709, None, 9.94746e-05, None, 1.47236, None, 0.00656874, None, 1.47236, None, 0.00656874, None)

reports.append(Report(604051616, ("CSC", 2, 1, 3, 20), "MEm13_20"))
reports[-1].posNum = 19638
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00434241, 0.0108227, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.44521, 0.317354, 0), \
                           ValErr(-0.00266752, 0.00718945, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.42062e-05, 0.000243096, 0), \
                           -35934.1, 19638, 19638, -nan)
reports[-1].sigmaresid = ValErr(1.50815, 0.0076099, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00905568, None, -3.50683e-05, None, 0.00480177, None, -2.92415e-05, None, 0.00480177, None, -2.92415e-05, None, -0.00649217, None, -6.18633e-05, None, -0.00649217, None, -6.18633e-05, None, 1.51043, None, 0.00655285, None, 1.51043, None, 0.00655285, None)

reports.append(Report(604051624, ("CSC", 2, 1, 3, 21), "MEm13_21"))
reports[-1].posNum = 18653
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0118903, 0.0109848, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.13511, 0.325244, 0), \
                           ValErr(0.00623875, 0.00761813, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000186207, 0.000254114, 0), \
                           -34014.7, 18653, 18653, -nan)
reports[-1].sigmaresid = ValErr(1.49872, 0.0077594, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00584718, None, 4.6164e-05, None, -0.0137989, None, 0.000124148, None, -0.0137989, None, 0.000124148, None, -0.0310046, None, 0.000144478, None, -0.0310046, None, 0.000144478, None, 1.50059, None, 0.00659236, None, 1.50059, None, 0.00659236, None)

reports.append(Report(604051632, ("CSC", 2, 1, 3, 22), "MEm13_22"))
reports[-1].posNum = 18308
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0111587, 0.011178, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.50717, 0.340377, 0), \
                           ValErr(-0.0205259, 0.00787983, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.80767e-05, 0.000255809, 0), \
                           -33533.6, 18308, 18308, -nan)
reports[-1].sigmaresid = ValErr(1.51088, 0.00789572, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0129673, None, 2.92619e-05, None, 0.00924696, None, 5.72619e-05, None, 0.00924696, None, 5.72619e-05, None, 0.0146679, None, -1.88806e-05, None, 0.0146679, None, -1.88806e-05, None, 1.51529, None, 0.00653519, None, 1.51529, None, 0.00653519, None)

reports.append(Report(604051640, ("CSC", 2, 1, 3, 23), "MEm13_23"))
reports[-1].posNum = 19305
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0208384, 0.0108112, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.44798, 0.314595, 0), \
                           ValErr(0.00148986, 0.00710898, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(9.02159e-05, 0.000240678, 0), \
                           -35087, 19305, 19305, -nan)
reports[-1].sigmaresid = ValErr(1.4897, 0.00758139, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0146473, None, 4.18399e-05, None, -0.0186589, None, 8.50772e-05, None, -0.0186589, None, 8.50772e-05, None, -0.0177224, None, 9.33679e-05, None, -0.0177224, None, 9.33679e-05, None, 1.49204, None, 0.00657128, None, 1.49204, None, 0.00657128, None)

reports.append(Report(604051648, ("CSC", 2, 1, 3, 24), "MEm13_24"))
reports[-1].posNum = 19562
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.021273, 0.0105878, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.02925, 0.302677, 0), \
                           ValErr(0.00151238, 0.00686494, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.22148e-05, 0.000235127, 0), \
                           -35261.3, 19562, 19562, -nan)
reports[-1].sigmaresid = ValErr(1.46757, 0.00741967, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0133417, None, -2.65251e-05, None, -0.0214172, None, 0.000124106, None, -0.0214172, None, 0.000124106, None, -0.0170495, None, 4.54415e-05, None, -0.0170495, None, 4.54415e-05, None, 1.46925, None, 0.00643078, None, 1.46925, None, 0.00643078, None)

reports.append(Report(604051656, ("CSC", 2, 1, 3, 25), "MEm13_25"))
reports[-1].posNum = 18714
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00416134, 0.0112673, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.13821, 0.321674, 0), \
                           ValErr(-0.0108662, 0.00728402, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.61013e-05, 0.000257165, 0), \
                           -34621.2, 18714, 18714, -nan)
reports[-1].sigmaresid = ValErr(1.53891, 0.00795455, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00609318, None, 2.92468e-05, None, 0.00551833, None, 2.36651e-05, None, 0.00551833, None, 2.36651e-05, None, 0.0213811, None, -3.64323e-05, None, 0.0213811, None, -3.64323e-05, None, 1.54079, None, 0.00651373, None, 1.54079, None, 0.00651373, None)

reports.append(Report(604051664, ("CSC", 2, 1, 3, 26), "MEm13_26"))
reports[-1].posNum = 17807
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00843109, 0.0114687, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.57045, 0.335681, 0), \
                           ValErr(-0.014194, 0.00782441, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.98868e-05, 0.000266104, 0), \
                           -32843.4, 17807, 17807, -nan)
reports[-1].sigmaresid = ValErr(1.53031, 0.00810899, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0116143, None, 5.54489e-05, None, -0.00929163, None, 9.12567e-05, None, -0.00929163, None, 9.12567e-05, None, -0.0188279, None, 8.09959e-05, None, -0.0188279, None, 8.09959e-05, None, 1.53286, None, 0.00639513, None, 1.53286, None, 0.00639513, None)

reports.append(Report(604051672, ("CSC", 2, 1, 3, 27), "MEm13_27"))
reports[-1].posNum = 18603
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00749941, 0.0112369, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.83364, 0.328261, 0), \
                           ValErr(0.00809913, 0.00746855, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000237933, 0.000255241, 0), \
                           -34258.6, 18603, 18603, -nan)
reports[-1].sigmaresid = ValErr(1.52595, 0.00791101, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00649049, None, -1.69384e-05, None, 0.00672657, None, 5.25489e-05, None, 0.00672657, None, 5.25489e-05, None, 0.00121177, None, 3.47212e-05, None, 0.00121177, None, 3.47212e-05, None, 1.52917, None, 0.006633, None, 1.52917, None, 0.006633, None)

reports.append(Report(604051680, ("CSC", 2, 1, 3, 28), "MEm13_28"))
reports[-1].posNum = 19386
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0171565, 0.010935, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.04685, 0.32124, 0), \
                           ValErr(-0.00815173, 0.00731127, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000129443, 0.000245172, 0), \
                           -35545.3, 19386, 19386, -nan)
reports[-1].sigmaresid = ValErr(1.51379, 0.00768788, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0245849, None, 2.36225e-05, None, 0.0159545, None, 3.04786e-05, None, 0.0159545, None, 3.04786e-05, None, 0.0185981, None, -1.26363e-05, None, 0.0185981, None, -1.26363e-05, None, 1.5173, None, 0.00692426, None, 1.5173, None, 0.00692426, None)

reports.append(Report(604051688, ("CSC", 2, 1, 3, 29), "MEm13_29"))
reports[-1].posNum = 18667
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0154414, 0.0110662, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.25911, 0.319856, 0), \
                           ValErr(0.00462702, 0.00720687, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(9.0421e-05, 0.000249544, 0), \
                           -34119, 18667, 18667, -nan)
reports[-1].sigmaresid = ValErr(1.50506, 0.00778932, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0135991, None, 5.3933e-05, None, -0.0144395, None, 0.000117293, None, -0.0144395, None, 0.000117293, None, -0.00516481, None, 4.59654e-05, None, -0.00516481, None, 4.59654e-05, None, 1.50712, None, 0.00680803, None, 1.50712, None, 0.00680803, None)

reports.append(Report(604051696, ("CSC", 2, 1, 3, 30), "MEm13_30"))
reports[-1].posNum = 17877
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.015537, 0.0112416, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.58926, 0.323667, 0), \
                           ValErr(-0.00651496, 0.00746623, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000260119, 0.000259136, 0), \
                           -32646.8, 17877, 17877, -nan)
reports[-1].sigmaresid = ValErr(1.50267, 0.00794689, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0275851, None, 6.72069e-05, None, -0.0148394, None, 6.01441e-07, None, -0.0148394, None, 6.01441e-07, None, -0.0271164, None, -2.57707e-05, None, -0.0271164, None, -2.57707e-05, None, 1.50541, None, 0.00648284, None, 1.50541, None, 0.00648284, None)

reports.append(Report(604051704, ("CSC", 2, 1, 3, 31), "MEm13_31"))
reports[-1].posNum = 18429
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00292643, 0.0111505, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.21128, 0.318079, 0), \
                           ValErr(-0.0103153, 0.00727196, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000301117, 0.000254339, 0), \
                           -33757.9, 18429, 18429, -nan)
reports[-1].sigmaresid = ValErr(1.51111, 0.007871, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00248163, None, 8.73048e-06, None, -0.00609022, None, 4.22237e-05, None, -0.00609022, None, 4.22237e-05, None, -0.0151942, None, 3.99237e-05, None, -0.0151942, None, 3.99237e-05, None, 1.5132, None, 0.006371, None, 1.5132, None, 0.006371, None)

reports.append(Report(604051712, ("CSC", 2, 1, 3, 32), "MEm13_32"))
reports[-1].posNum = 20071
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00729983, 0.0108156, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.52462, 0.319315, 0), \
                           ValErr(0.0130479, 0.00711798, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.57912e-05, 0.000240571, 0), \
                           -36871.4, 20071, 20071, -nan)
reports[-1].sigmaresid = ValErr(1.5191, 0.00758216, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00707302, None, 2.97772e-05, None, 0.00747312, None, 1.38201e-05, None, 0.00747312, None, 1.38201e-05, None, 0.00938421, None, 5.1111e-05, None, 0.00938421, None, 5.1111e-05, None, 1.5216, None, 0.00695815, None, 1.5216, None, 0.00695815, None)

reports.append(Report(604051720, ("CSC", 2, 1, 3, 33), "MEm13_33"))
reports[-1].posNum = 20051
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00792747, 0.0107822, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.89356, 0.316003, 0), \
                           ValErr(-0.00311207, 0.00708944, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000605761, 0.000240709, 0), \
                           -36776.4, 20051, 20051, -nan)
reports[-1].sigmaresid = ValErr(1.51469, 0.00756386, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0210914, None, -8.24055e-05, None, 0.0104514, None, -1.74249e-05, None, 0.0104514, None, -1.74249e-05, None, 0.00298682, None, -2.28331e-05, None, 0.00298682, None, -2.28331e-05, None, 1.51807, None, 0.00635084, None, 1.51807, None, 0.00635084, None)

reports.append(Report(604051728, ("CSC", 2, 1, 3, 34), "MEm13_34"))
reports[-1].posNum = 18291
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0146012, 0.0113199, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.0547, 0.342626, 0), \
                           ValErr(-0.00614532, 0.00794475, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000308093, 0.000259113, 0), \
                           -33734.3, 18291, 18291, -nan)
reports[-1].sigmaresid = ValErr(1.53016, 0.00800024, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0134104, None, 5.80024e-05, None, -0.0149521, None, 9.80608e-05, None, -0.0149521, None, 9.80608e-05, None, -0.00762117, None, 2.76909e-05, None, -0.00762117, None, 2.76909e-05, None, 1.53356, None, 0.00661992, None, 1.53356, None, 0.00661992, None)

reports.append(Report(604051736, ("CSC", 2, 1, 3, 35), "MEm13_35"))
reports[-1].posNum = 18302
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00891895, 0.0111442, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.01491, 0.332131, 0), \
                           ValErr(-0.0183597, 0.00769171, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.97466e-05, 0.000256842, 0), \
                           -33479.6, 18302, 18302, -nan)
reports[-1].sigmaresid = ValErr(1.50734, 0.00787856, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0170565, None, -4.73335e-05, None, 0.00896485, None, -4.22834e-05, None, 0.00896485, None, -4.22834e-05, None, 0.00878066, None, -2.09015e-05, None, 0.00878066, None, -2.09015e-05, None, 1.51077, None, 0.00670375, None, 1.51077, None, 0.00670375, None)

reports.append(Report(604051744, ("CSC", 2, 1, 3, 36), "MEm13_36"))
reports[-1].posNum = 19119
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00308009, 0.0108084, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.25266, 0.309646, 0), \
                           ValErr(-0.0145725, 0.00697769, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00049225, 0.000244183, 0), \
                           -34753.2, 19119, 19119, -nan)
reports[-1].sigmaresid = ValErr(1.49002, 0.00761983, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0154371, None, 2.09044e-06, None, -0.00487208, None, 9.53149e-05, None, -0.00487208, None, 9.53149e-05, None, -0.0141593, None, 0.000132562, None, -0.0141593, None, 0.000132562, None, 1.49237, None, 0.00653364, None, 1.49237, None, 0.00653364, None)

reports.append(Report(604049928, ("CSC", 2, 1, 4, 1), "MEm14_01"))
reports[-1].posNum = 104153
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00264028, 0.000604762, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.140946, 0.0475555, 0), \
                           ValErr(-0.00319839, 0.00126019, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.30867e-06, 1.58124e-05, 0), \
                           25023.7, 104153, 104153, -nan)
reports[-1].sigmaresid = ValErr(0.190292, 0.000416936, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00218461, None, 2.80053e-06, None, 0.0026347, None, -4.44374e-06, None, 0.0026347, None, -4.44374e-06, None, 0.00302419, None, -1.46965e-07, None, 0.00302419, None, -1.46965e-07, None, 0.190303, None, 0.00419987, None, 0.190303, None, 0.00419987, None)

reports.append(Report(604049944, ("CSC", 2, 1, 4, 3), "MEm14_03"))
reports[-1].posNum = 105526
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00300264, 0.000595172, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.133954, 0.0466646, 0), \
                           ValErr(-0.00232546, 0.00123766, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.35666e-05, 1.54821e-05, 0), \
                           26750, 105526, 105526, -nan)
reports[-1].sigmaresid = ValErr(0.18779, 0.000408769, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00226939, None, -1.44095e-05, None, 0.00288202, None, -8.48868e-06, None, 0.00288202, None, -8.48868e-06, None, 0.00236452, None, -5.72046e-06, None, 0.00236452, None, -5.72046e-06, None, 0.187799, None, 0.00416508, None, 0.187799, None, 0.00416508, None)

reports.append(Report(604049960, ("CSC", 2, 1, 4, 5), "MEm14_05"))
reports[-1].posNum = 104239
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00112617, 0.000607271, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0283153, 0.0477957, 0), \
                           ValErr(0.000157885, 0.00127523, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.52742e-05, 1.59529e-05, 0), \
                           24720.7, 104239, 104239, -nan)
reports[-1].sigmaresid = ValErr(0.190883, 0.000418057, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000359678, None, 8.64586e-06, None, 0.000821205, None, -2.89475e-05, None, 0.000821205, None, -2.89475e-05, None, -0.00105139, None, -1.21259e-05, None, -0.00105139, None, -1.21259e-05, None, 0.190888, None, 0.0045458, None, 0.190888, None, 0.0045458, None)

reports.append(Report(604049976, ("CSC", 2, 1, 4, 7), "MEm14_07"))
reports[-1].posNum = 104673
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00200704, 0.000603281, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0305201, 0.0475218, 0), \
                           ValErr(0.000699526, 0.00125362, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.89401e-06, 1.5696e-05, 0), \
                           25409.5, 104673, 104673, -nan)
reports[-1].sigmaresid = ValErr(0.189818, 0.000414862, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00174575, None, 9.31025e-06, None, 0.00193688, None, 2.24119e-05, None, 0.00193688, None, 2.24119e-05, None, 0.00166353, None, 2.16669e-05, None, 0.00166353, None, 2.16669e-05, None, 0.189819, None, 0.00409024, None, 0.189819, None, 0.00409024, None)

reports.append(Report(604049992, ("CSC", 2, 1, 4, 9), "MEm14_09"))
reports[-1].posNum = 104493
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00134645, 0.000607921, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0516703, 0.0477075, 0), \
                           ValErr(-6.44378e-05, 0.00126681, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.2923e-06, 1.59338e-05, 0), \
                           24437.8, 104493, 104493, -nan)
reports[-1].sigmaresid = ValErr(0.191511, 0.000418922, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00143383, None, -5.21584e-06, None, 0.00129161, None, -2.51359e-05, None, 0.00129161, None, -2.51359e-05, None, -0.000435691, None, 1.41916e-05, None, -0.000435691, None, 1.41916e-05, None, 0.191513, None, 0.00469314, None, 0.191513, None, 0.00469314, None)

reports.append(Report(604050008, ("CSC", 2, 1, 4, 11), "MEm14_11"))
reports[-1].posNum = 104691
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00136185, 0.000608463, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.118946, 0.0476877, 0), \
                           ValErr(0.000525442, 0.0012693, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(7.64402e-06, 1.59359e-05, 0), \
                           24345.2, 104691, 104691, -nan)
reports[-1].sigmaresid = ValErr(0.191765, 0.000419082, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00152084, None, 9.35094e-06, None, 0.00142983, None, 2.38145e-05, None, 0.00142983, None, 2.38145e-05, None, -0.000983616, None, 2.3443e-05, None, -0.000983616, None, 2.3443e-05, None, 0.191773, None, 0.00423863, None, 0.191773, None, 0.00423863, None)

reports.append(Report(604050024, ("CSC", 2, 1, 4, 13), "MEm14_13"))
reports[-1].posNum = 104968
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00111121, 0.000606186, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.19572, 0.0476163, 0), \
                           ValErr(-0.00131733, 0.00126202, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.47562e-05, 1.58017e-05, 0), \
                           24785.9, 104968, 104968, -nan)
reports[-1].sigmaresid = ValErr(0.191079, 0.000417033, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00124508, None, 4.17183e-06, None, 0.00134939, None, 4.03583e-06, None, 0.00134939, None, 4.03583e-06, None, 0.00181595, None, 7.43004e-06, None, 0.00181595, None, 7.43004e-06, None, 0.191097, None, 0.00423389, None, 0.191097, None, 0.00423389, None)

reports.append(Report(604050040, ("CSC", 2, 1, 4, 15), "MEm14_15"))
reports[-1].posNum = 104714
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0024239, 0.000604579, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.130973, 0.0475181, 0), \
                           ValErr(-0.00152488, 0.00125692, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.07589e-05, 1.5788e-05, 0), \
                           24939.6, 104714, 104714, -nan)
reports[-1].sigmaresid = ValErr(0.19069, 0.000416688, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00231383, None, 7.87667e-06, None, 0.00232878, None, -4.05191e-06, None, 0.00232878, None, -4.05191e-06, None, 0.00150425, None, -4.18414e-07, None, 0.00150425, None, -4.18414e-07, None, 0.190697, None, 0.00488756, None, 0.190697, None, 0.00488756, None)

reports.append(Report(604050056, ("CSC", 2, 1, 4, 17), "MEm14_17"))
reports[-1].posNum = 104442
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00242166, 0.000601751, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0187702, 0.0472114, 0), \
                           ValErr(-0.000735277, 0.00125108, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.18861e-05, 1.56513e-05, 0), \
                           25889.9, 104442, 104442, -nan)
reports[-1].sigmaresid = ValErr(0.188845, 0.000413193, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00194501, None, -5.34149e-06, None, 0.00212814, None, 1.18036e-05, None, 0.00212814, None, 1.18036e-05, None, 0.00215885, None, 3.18528e-05, None, 0.00215885, None, 3.18528e-05, None, 0.18885, None, 0.00423622, None, 0.18885, None, 0.00423622, None)

reports.append(Report(604050072, ("CSC", 2, 1, 4, 19), "MEm14_19"))
reports[-1].posNum = 104992
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00268043, 0.000603481, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.162162, 0.0476516, 0), \
                           ValErr(-0.00154128, 0.00126047, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.19094e-05, 1.58033e-05, 0), \
                           24889.3, 104992, 104992, -nan)
reports[-1].sigmaresid = ValErr(0.190902, 0.000416598, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00283395, None, 3.1761e-06, None, 0.00250975, None, -4.62052e-06, None, 0.00250975, None, -4.62052e-06, None, 0.00117258, None, 1.48955e-05, None, 0.00117258, None, 1.48955e-05, None, 0.190914, None, 0.00426737, None, 0.190914, None, 0.00426737, None)

reports.append(Report(604050088, ("CSC", 2, 1, 4, 21), "MEm14_21"))
reports[-1].posNum = 104669
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00270964, 0.000603313, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00681251, 0.0474212, 0), \
                           ValErr(-0.000622963, 0.00125791, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.3876e-06, 1.56888e-05, 0), \
                           25387, 104669, 104669, -nan)
reports[-1].sigmaresid = ValErr(0.189857, 0.000414955, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00280334, None, -5.34139e-06, None, 0.0026246, None, -2.05969e-06, None, 0.0026246, None, -2.05969e-06, None, 0.00167262, None, 2.03686e-05, None, 0.00167262, None, 2.03686e-05, None, 0.189858, None, 0.00411444, None, 0.189858, None, 0.00411444, None)

reports.append(Report(604050104, ("CSC", 2, 1, 4, 23), "MEm14_23"))
reports[-1].posNum = 104222
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00214114, 0.00060681, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.157602, 0.0477141, 0), \
                           ValErr(-0.000850554, 0.00126249, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.86733e-05, 1.58759e-05, 0), \
                           24530.1, 104222, 104222, -nan)
reports[-1].sigmaresid = ValErr(0.191226, 0.000418843, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00100925, None, 4.45896e-06, None, 0.00200163, None, 9.9664e-06, None, 0.00200163, None, 9.9664e-06, None, 0.000125849, None, 1.07704e-05, None, 0.000125849, None, 1.07704e-05, None, 0.191237, None, 0.00423019, None, 0.191237, None, 0.00423019, None)

reports.append(Report(604050120, ("CSC", 2, 1, 4, 25), "MEm14_25"))
reports[-1].posNum = 104719
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00354137, 0.000601324, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0752989, 0.0472681, 0), \
                           ValErr(-0.00127132, 0.00125104, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.71544e-05, 1.56522e-05, 0), \
                           25654.1, 104719, 104719, -nan)
reports[-1].sigmaresid = ValErr(0.189395, 0.000413849, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0024167, None, -1.00345e-07, None, 0.00312652, None, -7.22849e-06, None, 0.00312652, None, -7.22849e-06, None, 0.00165463, None, 1.85443e-06, None, 0.00165463, None, 1.85443e-06, None, 0.189406, None, 0.00498251, None, 0.189406, None, 0.00498251, None)

reports.append(Report(604050136, ("CSC", 2, 1, 4, 27), "MEm14_27"))
reports[-1].posNum = 103908
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00309189, 0.000609031, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0236229, 0.04781, 0), \
                           ValErr(-0.00297671, 0.00126847, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.62409e-05, 1.59167e-05, 0), \
                           24421.2, 103908, 103908, -nan)
reports[-1].sigmaresid = ValErr(0.19129, 0.000419617, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00234163, None, 3.54945e-06, None, 0.0028772, None, -2.463e-05, None, 0.0028772, None, -2.463e-05, None, 0.00257239, None, 1.14493e-05, None, 0.00257239, None, 1.14493e-05, None, 0.191297, None, 0.00659041, None, 0.191297, None, 0.00659041, None)

reports.append(Report(604050152, ("CSC", 2, 1, 4, 29), "MEm14_29"))
reports[-1].posNum = 104252
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00147165, 0.000606103, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.139618, 0.0476858, 0), \
                           ValErr(-0.00115315, 0.00126456, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.59325e-06, 1.58559e-05, 0), \
                           24735.9, 104252, 104252, -nan)
reports[-1].sigmaresid = ValErr(0.190861, 0.000417986, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00173994, None, 9.01532e-06, None, 0.00146237, None, 2.80363e-06, None, 0.00146237, None, 2.80363e-06, None, 0.00100523, None, 1.82402e-05, None, 0.00100523, None, 1.82402e-05, None, 0.190869, None, 0.0040809, None, 0.190869, None, 0.0040809, None)

reports.append(Report(604050168, ("CSC", 2, 1, 4, 31), "MEm14_31"))
reports[-1].posNum = 104844
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00331585, 0.000603558, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0685763, 0.0472921, 0), \
                           ValErr(-0.000860417, 0.00125314, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.27585e-05, 1.57238e-05, 0), \
                           25295.4, 104844, 104844, -nan)
reports[-1].sigmaresid = ValErr(0.1901, 0.000415141, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00276626, None, 6.01799e-06, None, 0.00312514, None, 2.2305e-05, None, 0.00312514, None, 2.2305e-05, None, 0.00139071, None, 5.39736e-05, None, 0.00139071, None, 5.39736e-05, None, 0.190104, None, 0.00472139, None, 0.190104, None, 0.00472139, None)

reports.append(Report(604050184, ("CSC", 2, 1, 4, 33), "MEm14_33"))
reports[-1].posNum = 105101
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0021295, 0.000607325, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0378554, 0.0477738, 0), \
                           ValErr(-0.00100544, 0.00126082, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.13502e-06, 1.58619e-05, 0), \
                           24340.4, 105101, 105101, -nan)
reports[-1].sigmaresid = ValErr(0.191948, 0.000418664, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00167737, None, 5.33967e-07, None, 0.0020637, None, 1.3076e-05, None, 0.0020637, None, 1.3076e-05, None, 0.00156006, None, 1.88081e-05, None, 0.00156006, None, 1.88081e-05, None, 0.191949, None, 0.0044653, None, 0.191949, None, 0.0044653, None)

reports.append(Report(604050200, ("CSC", 2, 1, 4, 35), "MEm14_35"))
reports[-1].posNum = 105329
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00273882, 0.00059602, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0767513, 0.0467959, 0), \
                           ValErr(-0.000677597, 0.0012413, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.33382e-05, 1.54761e-05, 0), \
                           26762.4, 105329, 105329, -nan)
reports[-1].sigmaresid = ValErr(0.187679, 0.000408908, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00235546, None, -2.13864e-06, None, 0.00286714, None, -1.17333e-06, None, 0.00286714, None, -1.17333e-06, None, 0.00292416, None, 3.34953e-05, None, 0.00292416, None, 3.34953e-05, None, 0.187682, None, 0.0049382, None, 0.187682, None, 0.0049382, None)

reports.append(Report(604049936, ("CSC", 2, 1, 4, 2), "MEm14_02"))
reports[-1].posNum = 104697
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00258811, 0.000542335, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.033286, 0.0402365, 0), \
                           ValErr(0.000133542, 0.0010711, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.79782e-05, 1.40964e-05, 0), \
                           36752.2, 104697, 104697, -nan)
reports[-1].sigmaresid = ValErr(0.170337, 0.000372243, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00171466, None, -1.64785e-05, None, 0.00233047, None, -3.08931e-05, None, 0.00233047, None, -3.08931e-05, None, 0.0025223, None, -2.27744e-05, None, 0.0025223, None, -2.27744e-05, None, 0.170341, None, 0.00438312, None, 0.170341, None, 0.00438312, None)

reports.append(Report(604049952, ("CSC", 2, 1, 4, 4), "MEm14_04"))
reports[-1].posNum = 103722
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00208925, 0.000541508, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.13077, 0.0401677, 0), \
                           ValErr(-0.000284532, 0.00106297, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.76769e-06, 1.40257e-05, 0), \
                           37096.1, 103722, 103722, -nan)
reports[-1].sigmaresid = ValErr(0.169214, 0.000371524, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00129563, None, -7.55472e-06, None, 0.00210837, None, -3.03648e-05, None, 0.00210837, None, -3.03648e-05, None, 0.0025727, None, -1.83905e-05, None, 0.0025727, None, -1.83905e-05, None, 0.169224, None, 0.00438864, None, 0.169224, None, 0.00438864, None)

reports.append(Report(604049968, ("CSC", 2, 1, 4, 6), "MEm14_06"))
reports[-1].posNum = 104996
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00137433, 0.000543512, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0735279, 0.0402178, 0), \
                           ValErr(0.0010898, 0.00106525, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.12339e-05, 1.40664e-05, 0), \
                           36575.7, 104996, 104996, -nan)
reports[-1].sigmaresid = ValErr(0.170795, 0.000372712, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00117357, None, 4.52605e-06, None, 0.0011743, None, -2.28495e-05, None, 0.0011743, None, -2.28495e-05, None, 0.000104691, None, 1.47363e-05, None, 0.000104691, None, 1.47363e-05, None, 0.170802, None, 0.00455218, None, 0.170802, None, 0.00455218, None)

reports.append(Report(604049984, ("CSC", 2, 1, 4, 8), "MEm14_08"))
reports[-1].posNum = 103859
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00187068, 0.000540974, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0793897, 0.0401706, 0), \
                           ValErr(-0.00109853, 0.0010609, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.81056e-07, 1.39805e-05, 0), \
                           37151.8, 103859, 103859, -nan)
reports[-1].sigmaresid = ValErr(0.169204, 0.000371255, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00151657, None, -4.94765e-06, None, 0.00187133, None, -1.99931e-05, None, 0.00187133, None, -1.99931e-05, None, 0.0010232, None, -1.20979e-05, None, 0.0010232, None, -1.20979e-05, None, 0.169207, None, 0.00460681, None, 0.169207, None, 0.00460681, None)

reports.append(Report(604050000, ("CSC", 2, 1, 4, 10), "MEm14_10"))
reports[-1].posNum = 104077
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00369643, 0.000544944, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0985885, 0.0403166, 0), \
                           ValErr(0.000196363, 0.00106487, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.19843e-05, 1.4115e-05, 0), \
                           36470, 104077, 104077, -nan)
reports[-1].sigmaresid = ValErr(0.170443, 0.000373583, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0032225, None, -2.24305e-05, None, 0.00358258, None, -4.05678e-05, None, 0.00358258, None, -4.05678e-05, None, 0.00460214, None, -3.4876e-05, None, 0.00460214, None, -3.4876e-05, None, 0.170449, None, 0.00451863, None, 0.170449, None, 0.00451863, None)

reports.append(Report(604050016, ("CSC", 2, 1, 4, 12), "MEm14_12"))
reports[-1].posNum = 103976
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00274351, 0.000541601, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0581261, 0.0402639, 0), \
                           ValErr(-0.000920252, 0.00106384, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.28226e-05, 1.39899e-05, 0), \
                           37051.9, 103976, 103976, -nan)
reports[-1].sigmaresid = ValErr(0.169434, 0.000371552, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00250499, None, -9.72714e-06, None, 0.00252222, None, -2.40427e-05, None, 0.00252222, None, -2.40427e-05, None, 0.00111366, None, -6.55565e-06, None, 0.00111366, None, -6.55565e-06, None, 0.169438, None, 0.00502913, None, 0.169438, None, 0.00502913, None)

reports.append(Report(604050032, ("CSC", 2, 1, 4, 14), "MEm14_14"))
reports[-1].posNum = 104106
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00188661, 0.000541966, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.141727, 0.0402732, 0), \
                           ValErr(-0.00197484, 0.0010604, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.78247e-06, 1.40125e-05, 0), \
                           36915.6, 104106, 104106, -nan)
reports[-1].sigmaresid = ValErr(0.169732, 0.000371973, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00131533, None, 2.23181e-06, None, 0.00184504, None, -2.80079e-05, None, 0.00184504, None, -2.80079e-05, None, 0.00140548, None, -2.45249e-05, None, 0.00140548, None, -2.45249e-05, None, 0.169743, None, 0.00470956, None, 0.169743, None, 0.00470956, None)

reports.append(Report(604050048, ("CSC", 2, 1, 4, 16), "MEm14_16"))
reports[-1].posNum = 104248
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00151526, 0.00054242, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0831594, 0.0402029, 0), \
                           ValErr(-0.00057611, 0.00106135, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.78055e-06, 1.40093e-05, 0), \
                           37039.3, 104248, 104248, -nan)
reports[-1].sigmaresid = ValErr(0.169613, 0.000371458, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00132754, None, -5.15569e-06, None, 0.00149417, None, -1.39744e-05, None, 0.00149417, None, -1.39744e-05, None, 0.00049308, None, -7.52116e-06, None, 0.00049308, None, -7.52116e-06, None, 0.169616, None, 0.00434613, None, 0.169616, None, 0.00434613, None)

reports.append(Report(604050064, ("CSC", 2, 1, 4, 18), "MEm14_18"))
reports[-1].posNum = 104452
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0016055, 0.000541396, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0714125, 0.0401567, 0), \
                           ValErr(-0.000634714, 0.00105684, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.07076e-05, 1.40176e-05, 0), \
                           37054.3, 104452, 104452, -nan)
reports[-1].sigmaresid = ValErr(0.169706, 0.000371299, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00107044, None, -1.22542e-06, None, 0.00141032, None, -3.80646e-05, None, 0.00141032, None, -3.80646e-05, None, 3.96117e-05, None, -2.33827e-07, None, 3.96117e-05, None, -2.33827e-07, None, 0.16971, None, 0.00454271, None, 0.16971, None, 0.00454271, None)

reports.append(Report(604050080, ("CSC", 2, 1, 4, 20), "MEm14_20"))
reports[-1].posNum = 104066
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00191307, 0.000543683, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0668346, 0.0402917, 0), \
                           ValErr(-0.001206, 0.00106596, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.11413e-05, 1.40486e-05, 0), \
                           36651, 104066, 104066, -nan)
reports[-1].sigmaresid = ValErr(0.170141, 0.000372941, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00225106, None, -6.69283e-06, None, 0.00181193, None, -3.25984e-05, None, 0.00181193, None, -3.25984e-05, None, 0.0014741, None, -2.14116e-05, None, 0.0014741, None, -2.14116e-05, None, 0.170144, None, 0.00434101, None, 0.170144, None, 0.00434101, None)

reports.append(Report(604050096, ("CSC", 2, 1, 4, 22), "MEm14_22"))
reports[-1].posNum = 103876
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00239762, 0.000542112, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.168127, 0.0402444, 0), \
                           ValErr(-0.00154074, 0.00106678, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.83647e-05, 1.4074e-05, 0), \
                           36938.1, 103876, 103876, -nan)
reports[-1].sigmaresid = ValErr(0.169562, 0.000372011, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00262475, None, -1.24275e-05, None, 0.00268099, None, -2.61316e-05, None, 0.00268099, None, -2.61316e-05, None, 0.00186422, None, -2.85428e-05, None, 0.00186422, None, -2.85428e-05, None, 0.16958, None, 0.00457571, None, 0.16958, None, 0.00457571, None)

reports.append(Report(604050112, ("CSC", 2, 1, 4, 24), "MEm14_24"))
reports[-1].posNum = 103893
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00290315, 0.000543432, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.106489, 0.0402429, 0), \
                           ValErr(-0.00112285, 0.00106009, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.72151e-05, 1.40331e-05, 0), \
                           36664.9, 103893, 103893, -nan)
reports[-1].sigmaresid = ValErr(0.170018, 0.000372982, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00287093, None, -1.41802e-05, None, 0.00265273, None, -2.75945e-05, None, 0.00265273, None, -2.75945e-05, None, 0.00067562, None, 2.40243e-06, None, 0.00067562, None, 2.40243e-06, None, 0.170027, None, 0.00593431, None, 0.170027, None, 0.00593431, None)

reports.append(Report(604050128, ("CSC", 2, 1, 4, 26), "MEm14_26"))
reports[-1].posNum = 104486
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00173008, 0.000539936, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.193544, 0.0400302, 0), \
                           ValErr(-0.00311579, 0.0010592, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.11528e-06, 1.39774e-05, 0), \
                           37318.9, 104486, 104486, -nan)
reports[-1].sigmaresid = ValErr(0.169296, 0.000370343, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00181168, None, -6.5485e-06, None, 0.00166973, None, -2.78531e-05, None, 0.00166973, None, -2.78531e-05, None, -0.000383069, None, -7.18402e-06, None, -0.000383069, None, -7.18402e-06, None, 0.169318, None, 0.00445645, None, 0.169318, None, 0.00445645, None)

reports.append(Report(604050144, ("CSC", 2, 1, 4, 28), "MEm14_28"))
reports[-1].posNum = 104353
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00237258, 0.000542646, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0806849, 0.0403098, 0), \
                           ValErr(-0.00153248, 0.00106421, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.09271e-08, 1.4056e-05, 0), \
                           36709.2, 104353, 104353, -nan)
reports[-1].sigmaresid = ValErr(0.170211, 0.00037258, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00296752, None, -3.41587e-06, None, 0.00237468, None, -9.70208e-06, None, 0.00237468, None, -9.70208e-06, None, 0.00170987, None, -3.51369e-06, None, 0.00170987, None, -3.51369e-06, None, 0.170215, None, 0.00434614, None, 0.170215, None, 0.00434614, None)

reports.append(Report(604050160, ("CSC", 2, 1, 4, 30), "MEm14_30"))
reports[-1].posNum = 104184
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00152451, 0.000541965, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.107566, 0.0401324, 0), \
                           ValErr(-0.00225094, 0.00106255, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.32509e-05, 1.40418e-05, 0), \
                           36954.6, 104184, 104184, -nan)
reports[-1].sigmaresid = ValErr(0.169714, 0.000371793, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00211622, None, -9.1978e-06, None, 0.00175009, None, -3.74025e-05, None, 0.00175009, None, -3.74025e-05, None, 0.00199454, None, -2.40639e-05, None, 0.00199454, None, -2.40639e-05, None, 0.169723, None, 0.00440324, None, 0.169723, None, 0.00440324, None)

reports.append(Report(604050176, ("CSC", 2, 1, 4, 32), "MEm14_32"))
reports[-1].posNum = 104627
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00183428, 0.000542533, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.199158, 0.0404152, 0), \
                           ValErr(-0.00211174, 0.00106591, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(8.47218e-06, 1.40226e-05, 0), \
                           36662.9, 104627, 104627, -nan)
reports[-1].sigmaresid = ValErr(0.170443, 0.0003726, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00206205, None, -1.68738e-05, None, 0.00192883, None, -3.24092e-05, None, 0.00192883, None, -3.24092e-05, None, 0.00158478, None, -2.17524e-05, None, 0.00158478, None, -2.17524e-05, None, 0.170463, None, 0.00426505, None, 0.170463, None, 0.00426505, None)

reports.append(Report(604050192, ("CSC", 2, 1, 4, 34), "MEm14_34"))
reports[-1].posNum = 104034
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00195854, 0.000540367, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.123829, 0.0400208, 0), \
                           ValErr(-0.00227864, 0.00105911, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.17169e-05, 1.40059e-05, 0), \
                           37233, 104034, 104034, -nan)
reports[-1].sigmaresid = ValErr(0.169173, 0.000370877, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00101865, None, 6.0495e-06, None, 0.00186829, None, -1.85098e-05, None, 0.00186829, None, -1.85098e-05, None, 0.00224109, None, -1.89329e-05, None, 0.00224109, None, -1.89329e-05, None, 0.169183, None, 0.00491552, None, 0.169183, None, 0.00491552, None)

reports.append(Report(604050208, ("CSC", 2, 1, 4, 36), "MEm14_36"))
reports[-1].posNum = 104555
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0022891, 0.00054506, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0412702, 0.0404649, 0), \
                           ValErr(-0.000852956, 0.00106602, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.78079e-06, 1.40837e-05, 0), \
                           36278.6, 104555, 104555, -nan)
reports[-1].sigmaresid = ValErr(0.171029, 0.00037401, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00213323, None, -5.36013e-06, None, 0.00220062, None, -1.42244e-05, None, 0.00220062, None, -1.42244e-05, None, 0.00037167, None, -2.83137e-05, None, 0.00037167, None, -2.83137e-05, None, 0.171031, None, 0.00450462, None, 0.171031, None, 0.00450462, None)

reports.append(Report(604054024, ("CSC", 2, 2, 1, 1), "MEm21_01"))
reports[-1].posNum = 209713
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000140805, 0.000930026, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0315379, 0.0359501, 0), \
                           ValErr(-0.00172285, 0.00070922, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.08917e-06, 1.8626e-05, 0), \
                           -115105, 209713, 209713, -nan)
reports[-1].sigmaresid = ValErr(0.418923, 0.000646855, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00170798, None, 5.15379e-06, None, 0.000119987, None, -1.11723e-05, None, 0.000119987, None, -1.11723e-05, None, -0.000406802, None, 9.96871e-06, None, -0.000406802, None, 9.96871e-06, None, 0.418929, None, 0.0059574, None, 0.418929, None, 0.0059574, None)

reports.append(Report(604054040, ("CSC", 2, 2, 1, 3), "MEm21_03"))
reports[-1].posNum = 210887
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000610158, 0.000927023, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0274864, 0.0357786, 0), \
                           ValErr(0.000241319, 0.00070831, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.35305e-06, 1.85769e-05, 0), \
                           -115375, 210887, 210887, -nan)
reports[-1].sigmaresid = ValErr(0.418179, 0.000643905, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00132782, None, 4.32117e-06, None, -0.000696628, None, -7.61919e-06, None, -0.000696628, None, -7.61919e-06, None, -0.000220386, None, 1.96066e-06, None, -0.000220386, None, 1.96066e-06, None, 0.41818, None, 0.00571104, None, 0.41818, None, 0.00571104, None)

reports.append(Report(604054056, ("CSC", 2, 2, 1, 5), "MEm21_05"))
reports[-1].posNum = 208946
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00276497, 0.0009326, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0850641, 0.0360188, 0), \
                           ValErr(0.00072568, 0.000712089, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.42131e-05, 1.87076e-05, 0), \
                           -114707, 208946, 208946, -nan)
reports[-1].sigmaresid = ValErr(0.418969, 0.000648111, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00473691, None, -1.30423e-05, None, 0.00263804, None, -1.81847e-05, None, 0.00263804, None, -1.81847e-05, None, 0.00171548, None, 1.38119e-05, None, 0.00171548, None, 1.38119e-05, None, 0.418975, None, 0.00579644, None, 0.418975, None, 0.00579644, None)

reports.append(Report(604054072, ("CSC", 2, 2, 1, 7), "MEm21_07"))
reports[-1].posNum = 209024
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000292828, 0.000923802, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0134869, 0.035594, 0), \
                           ValErr(-0.00103486, 0.00070233, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.53628e-05, 1.84753e-05, 0), \
                           -112771, 209024, 209024, -nan)
reports[-1].sigmaresid = ValErr(0.41502, 0.000641884, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000444025, None, 2.29476e-07, None, 0.00043767, None, -2.0373e-05, None, 0.00043767, None, -2.0373e-05, None, -0.000631014, None, 1.88092e-05, None, -0.000631014, None, 1.88092e-05, None, 0.415023, None, 0.00560422, None, 0.415023, None, 0.00560422, None)

reports.append(Report(604054088, ("CSC", 2, 2, 1, 9), "MEm21_09"))
reports[-1].posNum = 209622
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000878072, 0.000924504, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0243665, 0.0356624, 0), \
                           ValErr(0.00104989, 0.000705559, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.15934e-05, 1.85091e-05, 0), \
                           -113413, 209622, 209622, -nan)
reports[-1].sigmaresid = ValErr(0.415654, 0.000641946, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00164979, None, 2.40866e-06, None, 0.000766918, None, -1.62629e-05, None, 0.000766918, None, -1.62629e-05, None, 0.000875018, None, -1.37997e-05, None, 0.000875018, None, -1.37997e-05, None, 0.415657, None, 0.00564298, None, 0.415657, None, 0.00564298, None)

reports.append(Report(604054104, ("CSC", 2, 2, 1, 11), "MEm21_11"))
reports[-1].posNum = 209182
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00332114, 0.000924147, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0228141, 0.0357271, 0), \
                           ValErr(9.18408e-05, 0.000704684, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.57205e-05, 1.8488e-05, 0), \
                           -113033, 209182, 209182, -nan)
reports[-1].sigmaresid = ValErr(0.415373, 0.000642186, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00259063, None, -1.29407e-05, None, 0.00346688, None, -3.07179e-05, None, 0.00346688, None, -3.07179e-05, None, 0.00398203, None, -3.19397e-05, None, 0.00398203, None, -3.19397e-05, None, 0.415374, None, 0.00563453, None, 0.415374, None, 0.00563453, None)

reports.append(Report(604054120, ("CSC", 2, 2, 1, 13), "MEm21_13"))
reports[-1].posNum = 209807
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00166061, 0.000922651, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00875123, 0.0356032, 0), \
                           ValErr(0.000873535, 0.000702721, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.30467e-05, 1.84327e-05, 0), \
                           -113315, 209807, 209807, -nan)
reports[-1].sigmaresid = ValErr(0.415261, 0.000641057, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00131856, None, 3.45409e-06, None, 0.00154109, None, -2.72487e-05, None, 0.00154109, None, -2.72487e-05, None, 0.00122377, None, -1.29381e-05, None, 0.00122377, None, -1.29381e-05, None, 0.415264, None, 0.00566588, None, 0.415264, None, 0.00566588, None)

reports.append(Report(604054136, ("CSC", 2, 2, 1, 15), "MEm21_15"))
reports[-1].posNum = 209553
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00141197, 0.000922632, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.00364253, 0.035645, 0), \
                           ValErr(0.000475369, 0.000703014, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.78492e-05, 1.84253e-05, 0), \
                           -113155, 209553, 209553, -nan)
reports[-1].sigmaresid = ValErr(0.415216, 0.000641375, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00115284, None, -2.80587e-06, None, 0.0012502, None, -1.75904e-05, None, 0.0012502, None, -1.75904e-05, None, 0.00162994, None, 6.56684e-06, None, 0.00162994, None, 6.56684e-06, None, 0.415218, None, 0.00563289, None, 0.415218, None, 0.00563289, None)

reports.append(Report(604054152, ("CSC", 2, 2, 1, 17), "MEm21_17"))
reports[-1].posNum = 210283
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000877235, 0.000925471, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.00200989, 0.0357432, 0), \
                           ValErr(0.000353458, 0.000704629, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.44498e-05, 1.85107e-05, 0), \
                           -114434, 210283, 210283, -nan)
reports[-1].sigmaresid = ValErr(0.416968, 0.000642962, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000205455, None, 3.2474e-07, None, 0.000745072, None, -2.37958e-05, None, 0.000745072, None, -2.37958e-05, None, 0.000243339, None, -9.51277e-06, None, 0.000243339, None, -9.51277e-06, None, 0.416968, None, 0.00576206, None, 0.416968, None, 0.00576206, None)

reports.append(Report(604054032, ("CSC", 2, 2, 1, 2), "MEm21_02"))
reports[-1].posNum = 208969
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00083178, 0.000880729, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0431498, 0.0329176, 0), \
                           ValErr(-0.000396578, 0.000647212, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.57336e-05, 1.75484e-05, 0), \
                           -102254, 208969, 208969, -nan)
reports[-1].sigmaresid = ValErr(0.394706, 0.000610546, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000983515, None, -2.10153e-05, None, 0.000988757, None, -1.98955e-05, None, 0.000988757, None, -1.98955e-05, None, 0.000308018, None, -9.64027e-06, None, 0.000308018, None, -9.64027e-06, None, 0.394708, None, 0.00594004, None, 0.394708, None, 0.00594004, None)

reports.append(Report(604054048, ("CSC", 2, 2, 1, 4), "MEm21_04"))
reports[-1].posNum = 208870
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000709261, 0.000882473, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00916655, 0.032955, 0), \
                           ValErr(0.000202879, 0.000648599, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.63488e-06, 1.75666e-05, 0), \
                           -102478, 208870, 208870, -nan)
reports[-1].sigmaresid = ValErr(0.395222, 0.000611488, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000503795, None, -2.38312e-05, None, 0.000614766, None, -2.83464e-05, None, 0.000614766, None, -2.83464e-05, None, 0.00197322, None, -2.02944e-05, None, 0.00197322, None, -2.02944e-05, None, 0.395222, None, 0.00630621, None, 0.395222, None, 0.00630621, None)

reports.append(Report(604054064, ("CSC", 2, 2, 1, 6), "MEm21_06"))
reports[-1].posNum = 209043
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00192335, 0.000886767, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0294124, 0.0330947, 0), \
                           ValErr(-0.00113465, 0.000651989, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.3314e-05, 1.76531e-05, 0), \
                           -103775, 209043, 209043, -nan)
reports[-1].sigmaresid = ValErr(0.39752, 0.000614789, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00158827, None, -1.49513e-05, None, 0.00159972, None, -3.68041e-05, None, 0.00159972, None, -3.68041e-05, None, 0.000992287, None, -1.9016e-05, None, 0.000992287, None, -1.9016e-05, None, 0.397528, None, 0.00593088, None, 0.397528, None, 0.00593088, None)

reports.append(Report(604054080, ("CSC", 2, 2, 1, 8), "MEm21_08"))
reports[-1].posNum = 210162
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000687203, 0.000884323, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.03687, 0.0329866, 0), \
                           ValErr(-0.000669359, 0.000648357, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.30658e-05, 1.75903e-05, 0), \
                           -104183, 210162, 210162, -nan)
reports[-1].sigmaresid = ValErr(0.397242, 0.000612721, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000479499, None, -3.66548e-06, None, 0.000551798, None, -8.36824e-06, None, 0.000551798, None, -8.36824e-06, None, 0.000139996, None, -3.38241e-06, None, 0.000139996, None, -3.38241e-06, None, 0.397244, None, 0.00635418, None, 0.397244, None, 0.00635418, None)

reports.append(Report(604054096, ("CSC", 2, 2, 1, 10), "MEm21_10"))
reports[-1].posNum = 209341
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000794668, 0.000887493, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0226335, 0.0331758, 0), \
                           ValErr(-0.00093123, 0.000652482, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.24283e-05, 1.76716e-05, 0), \
                           -104498, 209341, 209341, -nan)
reports[-1].sigmaresid = ValErr(0.398614, 0.000616043, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000785216, None, -7.7121e-06, None, 0.00057886, None, -3.36357e-05, None, 0.00057886, None, -3.36357e-05, None, -0.000608524, None, -9.80961e-06, None, -0.000608524, None, -9.80961e-06, None, 0.398618, None, 0.0060536, None, 0.398618, None, 0.0060536, None)

reports.append(Report(604054112, ("CSC", 2, 2, 1, 12), "MEm21_12"))
reports[-1].posNum = 209399
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000415117, 0.000885876, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00571479, 0.0330717, 0), \
                           ValErr(-0.000518691, 0.000650392, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.46051e-05, 1.76428e-05, 0), \
                           -103997, 209399, 209399, -nan)
reports[-1].sigmaresid = ValErr(0.397605, 0.000614398, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00122094, None, 7.07774e-06, None, -2.28545e-05, None, -1.55764e-05, None, -2.28545e-05, None, -1.55764e-05, None, -0.000563964, None, 6.96123e-06, None, -0.000563964, None, 6.96123e-06, None, 0.397612, None, 0.00604935, None, 0.397612, None, 0.00604935, None)

reports.append(Report(604054128, ("CSC", 2, 2, 1, 14), "MEm21_14"))
reports[-1].posNum = 209719
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000523635, 0.000883259, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0127579, 0.0329782, 0), \
                           ValErr(0.000861612, 0.000648035, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.54364e-05, 1.75849e-05, 0), \
                           -103711, 209719, 209719, -nan)
reports[-1].sigmaresid = ValErr(0.396763, 0.000612629, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000451052, None, -1.51213e-05, None, -0.000178762, None, -1.39008e-05, None, -0.000178762, None, -1.39008e-05, None, 0.000219815, None, -3.50079e-06, None, 0.000219815, None, -3.50079e-06, None, 0.396769, None, 0.00607806, None, 0.396769, None, 0.00607806, None)

reports.append(Report(604054144, ("CSC", 2, 2, 1, 16), "MEm21_16"))
reports[-1].posNum = 209261
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00188018, 0.000885671, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0584332, 0.0330339, 0), \
                           ValErr(-0.000209768, 0.000651591, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.07085e-05, 1.76575e-05, 0), \
                           -103752, 209261, 209261, -nan)
reports[-1].sigmaresid = ValErr(0.397271, 0.000614084, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00224234, None, -1.21165e-05, None, 0.00208793, None, -1.01502e-05, None, 0.00208793, None, -1.01502e-05, None, 0.00150878, None, -1.71817e-05, None, 0.00150878, None, -1.71817e-05, None, 0.397275, None, 0.00610986, None, 0.397275, None, 0.00610986, None)

reports.append(Report(604054160, ("CSC", 2, 2, 1, 18), "MEm21_18"))
reports[-1].posNum = 209480
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00175418, 0.000881777, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0182901, 0.0329738, 0), \
                           ValErr(-0.000611189, 0.000649145, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(8.55998e-06, 1.75834e-05, 0), \
                           -102868, 209480, 209480, -nan)
reports[-1].sigmaresid = ValErr(0.395394, 0.000610863, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00153793, None, -7.83375e-06, None, 0.00183913, None, -3.21544e-05, None, 0.00183913, None, -3.21544e-05, None, 0.000712405, None, -1.79283e-05, None, 0.000712405, None, -1.79283e-05, None, 0.395395, None, 0.00610427, None, 0.395395, None, 0.00610427, None)

reports.append(Report(604054536, ("CSC", 2, 2, 2, 1), "MEm22_01"))
reports[-1].posNum = 57906
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00300707, 0.00467032, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.140481, 0.174017, 0), \
                           ValErr(-0.0021272, 0.00196122, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.6348e-05, 5.04616e-05, 0), \
                           -83645.5, 57906, 57906, -nan)
reports[-1].sigmaresid = ValErr(1.0259, 0.00301458, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00267932, None, 2.13745e-05, None, -0.00237571, None, 1.3814e-05, None, -0.00237571, None, 1.3814e-05, None, -0.000817362, None, -3.64042e-05, None, -0.000817362, None, -3.64042e-05, None, 1.02591, None, 0.0066356, None, 1.02591, None, 0.0066356, None)

reports.append(Report(604054552, ("CSC", 2, 2, 2, 3), "MEm22_03"))
reports[-1].posNum = 51505
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0136816, 0.00485542, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.164192, 0.104034, 0), \
                           ValErr(-0.00027205, 0.00201774, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000170536, 5.17284e-05, 0), \
                           -72135.4, 51505, 51505, -nan)
reports[-1].sigmaresid = ValErr(0.981777, 0.00297619, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00126812, None, 1.72304e-05, None, -0.00630819, None, 2.13874e-05, None, -0.00630819, None, 2.13874e-05, None, -0.00788898, None, 5.91342e-05, None, -0.00788898, None, 5.91342e-05, None, 0.981892, None, 0.00736637, None, 0.981892, None, 0.00736637, None)

reports.append(Report(604054568, ("CSC", 2, 2, 2, 5), "MEm22_05"))
reports[-1].posNum = 57396
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00636727, 0.00460804, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.294553, 0.174672, 0), \
                           ValErr(-0.00424246, 0.0019542, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.62234e-06, 4.97375e-05, 0), \
                           -82037.9, 57396, 57396, -nan)
reports[-1].sigmaresid = ValErr(1.01045, 0.00298235, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00590334, None, -2.07268e-05, None, 0.00620762, None, 1.36732e-05, None, 0.00620762, None, 1.36732e-05, None, 0.0114426, None, -1.36689e-05, None, 0.0114426, None, -1.36689e-05, None, 1.01051, None, 0.00659065, None, 1.01051, None, 0.00659065, None)

reports.append(Report(604054584, ("CSC", 2, 2, 2, 7), "MEm22_07"))
reports[-1].posNum = 51955
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00403556, 0.00491802, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.157065, 0.179857, 0), \
                           ValErr(-0.000309179, 0.0020182, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.31516e-05, 5.23545e-05, 0), \
                           -73517.4, 51955, 51955, -nan)
reports[-1].sigmaresid = ValErr(0.996088, 0.00309007, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0047093, None, -6.45684e-05, None, 0.00205549, None, -6.88397e-05, None, 0.00205549, None, -6.88397e-05, None, -0.00230123, None, -4.85735e-05, None, -0.00230123, None, -4.85735e-05, None, 0.996103, None, 0.00673161, None, 0.996103, None, 0.00673161, None)

reports.append(Report(604054600, ("CSC", 2, 2, 2, 9), "MEm22_09"))
reports[-1].posNum = 54426
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000840856, 0.00478693, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.376638, 0.181004, 0), \
                           ValErr(-0.00288347, 0.00201379, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.05255e-05, 5.14439e-05, 0), \
                           -77927.6, 54426, 54426, -nan)
reports[-1].sigmaresid = ValErr(1.01295, 0.00307023, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00151883, None, -2.68329e-06, None, 0.00185199, None, -1.35159e-05, None, 0.00185199, None, -1.35159e-05, None, -0.00109638, None, -1.99832e-05, None, -0.00109638, None, -1.99832e-05, None, 1.01302, None, 0.00694953, None, 1.01302, None, 0.00694953, None)

reports.append(Report(604054616, ("CSC", 2, 2, 2, 11), "MEm22_11"))
reports[-1].posNum = 54308
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00943346, 0.00480931, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.385874, 0.183408, 0), \
                           ValErr(-0.00273153, 0.00203987, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.93061e-06, 5.14768e-05, 0), \
                           -78062.8, 54308, 54308, -nan)
reports[-1].sigmaresid = ValErr(1.01864, 0.00309083, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0108503, None, -2.65893e-05, None, 0.00903931, None, -7.79987e-06, None, 0.00903931, None, -7.79987e-06, None, 0.0089776, None, -7.60719e-06, None, 0.0089776, None, -7.60719e-06, None, 1.01869, None, 0.0069374, None, 1.01869, None, 0.0069374, None)

reports.append(Report(604054632, ("CSC", 2, 2, 2, 13), "MEm22_13"))
reports[-1].posNum = 50713
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00608341, 0.00499118, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.139139, 0.182773, 0), \
                           ValErr(0.00151289, 0.00203568, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.51438e-05, 5.2922e-05, 0), \
                           -72061.7, 50713, 50713, -nan)
reports[-1].sigmaresid = ValErr(1.00203, 0.00314636, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00357232, None, 9.42596e-06, None, 0.00485842, None, -1.42042e-05, None, 0.00485842, None, -1.42042e-05, None, 0.00134633, None, 5.93454e-06, None, 0.00134633, None, 5.93454e-06, None, 1.00205, None, 0.00641827, None, 1.00205, None, 0.00641827, None)

reports.append(Report(604054648, ("CSC", 2, 2, 2, 15), "MEm22_15"))
reports[-1].posNum = 57335
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00511246, 0.00465066, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.13044, 0.176513, 0), \
                           ValErr(0.00442429, 0.00199592, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.66102e-05, 5.03732e-05, 0), \
                           -82394.2, 57335, 57335, -nan)
reports[-1].sigmaresid = ValErr(1.01829, 0.00300709, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00594016, None, 2.52397e-06, None, -0.00452128, None, 8.89482e-07, None, -0.00452128, None, 8.89482e-07, None, -0.00426788, None, 3.61606e-05, None, -0.00426788, None, 3.61606e-05, None, 1.01834, None, 0.00686459, None, 1.01834, None, 0.00686459, None)

reports.append(Report(604054664, ("CSC", 2, 2, 2, 17), "MEm22_17"))
reports[-1].posNum = 51704
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0138049, 0.00490713, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.413948, 0.184108, 0), \
                           ValErr(-0.00172108, 0.00205522, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000117015, 5.21117e-05, 0), \
                           -72799.7, 51704, 51704, -nan)
reports[-1].sigmaresid = ValErr(0.98913, 0.00307593, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00811433, None, 2.10945e-05, None, -0.00873876, None, 2.96502e-05, None, -0.00873876, None, 2.96502e-05, None, -0.0109667, None, -1.12301e-05, None, -0.0109667, None, -1.12301e-05, None, 0.989229, None, 0.00688716, None, 0.989229, None, 0.00688716, None)

reports.append(Report(604054680, ("CSC", 2, 2, 2, 19), "MEm22_19"))
reports[-1].posNum = 57378
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0142301, 0.00466887, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.392452, 0.173595, 0), \
                           ValErr(-0.00239226, 0.00196733, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000111518, 5.06376e-05, 0), \
                           -82538.8, 57378, 57378, -nan)
reports[-1].sigmaresid = ValErr(1.01976, 0.00301031, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00283544, None, 3.59958e-06, None, -0.00996629, None, 5.81803e-05, None, -0.00996629, None, 5.81803e-05, None, -0.0134813, None, 6.87465e-05, None, -0.0134813, None, 6.87465e-05, None, 1.01986, None, 0.00651513, None, 1.01986, None, 0.00651513, None)

reports.append(Report(604054696, ("CSC", 2, 2, 2, 21), "MEm22_21"))
reports[-1].posNum = 50748
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00429168, 0.00487183, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.207071, 0.182647, 0), \
                           ValErr(-0.000952226, 0.00201512, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.8886e-05, 5.13461e-05, 0), \
                           -71056.5, 50748, 50748, -nan)
reports[-1].sigmaresid = ValErr(0.981418, 0.00308056, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00591131, None, 3.63135e-05, None, -0.00810438, None, 3.18224e-06, None, -0.00810438, None, 3.18224e-06, None, -0.0167603, None, 1.66927e-05, None, -0.0167603, None, 1.66927e-05, None, 0.981461, None, 0.00672022, None, 0.981461, None, 0.00672022, None)

reports.append(Report(604054712, ("CSC", 2, 2, 2, 23), "MEm22_23"))
reports[-1].posNum = 57619
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00169368, 0.00466624, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.124002, 0.106158, 0), \
                           ValErr(-6.64741e-05, 0.00194394, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(7.25872e-05, 5.05724e-05, 0), \
                           -83104.1, 57619, 57619, -nan)
reports[-1].sigmaresid = ValErr(1.02364, 0.00299391, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000327831, None, -8.57142e-06, None, 0.00104691, None, 2.10456e-05, None, 0.00104691, None, 2.10456e-05, None, 0.000190933, None, 1.35908e-05, None, 0.000190933, None, 1.35908e-05, None, 1.02366, None, 0.00669491, None, 1.02366, None, 0.00669491, None)

reports.append(Report(604054728, ("CSC", 2, 2, 2, 25), "MEm22_25"))
reports[-1].posNum = 52043
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00632751, 0.00490608, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0336536, 0.180197, 0), \
                           ValErr(-0.00164321, 0.00200958, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.15331e-05, 5.2307e-05, 0), \
                           -73737.9, 52043, 52043, -nan)
reports[-1].sigmaresid = ValErr(0.997926, 0.00309315, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00188902, None, 2.81337e-05, None, -0.0042344, None, 1.15454e-05, None, -0.0042344, None, 1.15454e-05, None, -0.0103877, None, 5.09514e-05, None, -0.0103877, None, 5.09514e-05, None, 0.997944, None, 0.00647953, None, 0.997944, None, 0.00647953, None)

reports.append(Report(604054744, ("CSC", 2, 2, 2, 27), "MEm22_27"))
reports[-1].posNum = 54576
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00874745, 0.00478196, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.258321, 0.180294, 0), \
                           ValErr(-0.000635624, 0.00202965, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.77489e-06, 5.15526e-05, 0), \
                           -78265.9, 54576, 54576, -nan)
reports[-1].sigmaresid = ValErr(1.01525, 0.00307295, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0079635, None, 1.86986e-05, None, -0.00882928, None, 1.63874e-05, None, -0.00882928, None, 1.63874e-05, None, -0.00386966, None, -7.56099e-06, None, -0.00386966, None, -7.56099e-06, None, 1.01527, None, 0.00684037, None, 1.01527, None, 0.00684037, None)

reports.append(Report(604054760, ("CSC", 2, 2, 2, 29), "MEm22_29"))
reports[-1].posNum = 54891
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0067052, 0.00478546, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.228797, 0.10402, 0), \
                           ValErr(0.00081643, 0.00197512, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.45585e-05, 5.07864e-05, 0), \
                           -78881.9, 54891, 54891, -nan)
reports[-1].sigmaresid = ValErr(1.01829, 0.0030029, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000631881, None, -3.7789e-06, None, 0.00366272, None, -3.67536e-05, None, 0.00366272, None, -3.67536e-05, None, -0.00116156, None, -3.78336e-05, None, -0.00116156, None, -3.78336e-05, None, 1.01833, None, 0.00676115, None, 1.01833, None, 0.00676115, None)

reports.append(Report(604054776, ("CSC", 2, 2, 2, 31), "MEm22_31"))
reports[-1].posNum = 52101
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00175344, 0.00498025, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0486754, 0.118413, 0), \
                           ValErr(-0.000103986, 0.00194897, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.96909e-05, 5.30173e-05, 0), \
                           -74426.6, 52101, 52101, -nan)
reports[-1].sigmaresid = ValErr(1.00961, 0.00312188, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00448212, None, -1.10871e-05, None, -0.000357908, None, -7.669e-05, None, -0.000357908, None, -7.669e-05, None, -0.00648094, None, -3.80044e-05, None, -0.00648094, None, -3.80044e-05, None, 1.00962, None, 0.00674822, None, 1.00962, None, 0.00674822, None)

reports.append(Report(604054792, ("CSC", 2, 2, 2, 33), "MEm22_33"))
reports[-1].posNum = 57397
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0029897, 0.00463002, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0850452, 0.175137, 0), \
                           ValErr(-0.00416106, 0.00198494, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.74652e-05, 5.01982e-05, 0), \
                           -82554.6, 57397, 57397, -nan)
reports[-1].sigmaresid = ValErr(1.01956, 0.0030092, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00482876, None, 1.05261e-06, None, 0.00132825, None, -1.22175e-07, None, 0.00132825, None, -1.22175e-07, None, 0.00604882, None, -1.3849e-05, None, 0.00604882, None, -1.3849e-05, None, 1.01961, None, 0.00702032, None, 1.01961, None, 0.00702032, None)

reports.append(Report(604054808, ("CSC", 2, 2, 2, 35), "MEm22_35"))
reports[-1].posNum = 50421
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00728837, 0.00490656, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.140147, 0.110504, 0), \
                           ValErr(-0.000511688, 0.00189671, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(7.01456e-06, 5.14251e-05, 0), \
                           -71021.8, 50421, 50421, -nan)
reports[-1].sigmaresid = ValErr(0.98969, 0.00308058, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00927967, None, -1.19981e-05, None, -0.00694679, None, 6.86134e-06, None, -0.00694679, None, 6.86134e-06, None, -0.00743386, None, -4.40746e-06, None, -0.00743386, None, -4.40746e-06, None, 0.989699, None, 0.0069018, None, 0.989699, None, 0.0069018, None)

reports.append(Report(604054544, ("CSC", 2, 2, 2, 2), "MEm22_02"))
reports[-1].posNum = 53962
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0115622, 0.00477085, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0835788, 0.140631, 0), \
                           ValErr(-0.00104509, 0.00135413, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(8.78341e-05, 5.07357e-05, 0), \
                           -77116.3, 53962, 53962, -nan)
reports[-1].sigmaresid = ValErr(1.0102, 0.00307501, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00574678, None, 2.29208e-05, None, -0.00810112, None, 4.81635e-05, None, -0.00810112, None, 4.81635e-05, None, -0.00883796, None, 7.16071e-05, None, -0.00883796, None, 7.16071e-05, None, 1.01023, None, 0.00719921, None, 1.01023, None, 0.00719921, None)

reports.append(Report(604054560, ("CSC", 2, 2, 2, 4), "MEm22_04"))
reports[-1].posNum = 50259
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00142928, 0.00494756, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0479108, 0.182011, 0), \
                           ValErr(-0.000748589, 0.00200988, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.332e-06, 5.21247e-05, 0), \
                           -70793.3, 50259, 50259, -nan)
reports[-1].sigmaresid = ValErr(0.989685, 0.00312159, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00319239, None, -3.54044e-05, None, 0.0011824, None, -1.90147e-05, None, 0.0011824, None, -1.90147e-05, None, 0.0013629, None, -4.62869e-05, None, 0.0013629, None, -4.62869e-05, None, 0.989686, None, 0.0066434, None, 0.989686, None, 0.0066434, None)

reports.append(Report(604054576, ("CSC", 2, 2, 2, 6), "MEm22_06"))
reports[-1].posNum = 56106
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00317682, 0.00470756, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.241272, 0.170773, 0), \
                           ValErr(0.000583758, 0.0019309, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.86172e-05, 5.10955e-05, 0), \
                           -80446.5, 56106, 56106, -nan)
reports[-1].sigmaresid = ValErr(1.015, 0.00303003, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000330896, None, -1.78088e-05, None, 0.00214177, None, -2.18386e-05, None, 0.00214177, None, -2.18386e-05, None, 0.00572018, None, -3.05595e-05, None, 0.00572018, None, -3.05595e-05, None, 1.01503, None, 0.00691556, None, 1.01503, None, 0.00691556, None)

reports.append(Report(604054592, ("CSC", 2, 2, 2, 8), "MEm22_08"))
reports[-1].posNum = 48253
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0072736, 0.00491723, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.239896, 0.111938, 0), \
                           ValErr(-0.000654699, 0.00194563, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.15107e-05, 5.14866e-05, 0), \
                           -67733.5, 48253, 48253, -nan)
reports[-1].sigmaresid = ValErr(0.984887, 0.00305002, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000519435, None, -5.38418e-06, None, 0.00583453, None, 7.16927e-06, None, 0.00583453, None, 7.16927e-06, None, 0.0176948, None, -3.7751e-05, None, 0.0176948, None, -3.7751e-05, None, 0.984917, None, 0.00670376, None, 0.984917, None, 0.00670376, None)

reports.append(Report(604054608, ("CSC", 2, 2, 2, 10), "MEm22_10"))
reports[-1].posNum = 57470
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00704926, 0.00465254, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0786582, 0.170321, 0), \
                           ValErr(-0.00215862, 0.00191817, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.67302e-06, 5.05188e-05, 0), \
                           -82357.8, 57470, 57470, -nan)
reports[-1].sigmaresid = ValErr(1.01422, 0.00299155, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00817512, None, -1.0931e-05, None, 0.00683267, None, 7.81482e-06, None, 0.00683267, None, 7.81482e-06, None, 0.00454603, None, -1.0424e-05, None, 0.00454603, None, -1.0424e-05, None, 1.01423, None, 0.00683494, None, 1.01423, None, 0.00683494, None)

reports.append(Report(604054624, ("CSC", 2, 2, 2, 12), "MEm22_12"))
reports[-1].posNum = 49700
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00504544, 0.00494969, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.255354, 0.177361, 0), \
                           ValErr(-0.00175302, 0.00195107, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.7542e-05, 5.194e-05, 0), \
                           -69349.7, 49700, 49700, -nan)
reports[-1].sigmaresid = ValErr(0.9767, 0.00309789, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00224186, None, 1.0031e-05, None, 0.0036284, None, 3.44617e-05, None, 0.0036284, None, 3.44617e-05, None, 0.00572043, None, 2.45722e-05, None, 0.00572043, None, 2.45722e-05, None, 0.976743, None, 0.00686176, None, 0.976743, None, 0.00686176, None)

reports.append(Report(604054640, ("CSC", 2, 2, 2, 14), "MEm22_14"))
reports[-1].posNum = 55797
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0032531, 0.00466374, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.216721, 0.170883, 0), \
                           ValErr(-0.00514606, 0.00192249, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.56486e-05, 5.03203e-05, 0), \
                           -79480.1, 55797, 55797, -nan)
reports[-1].sigmaresid = ValErr(1.00553, 0.00301004, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00187612, None, 1.42782e-05, None, 0.000859713, None, -9.31671e-06, None, 0.000859713, None, -9.31671e-06, None, 0.000106624, None, 1.7236e-07, None, 0.000106624, None, 1.7236e-07, None, 1.00562, None, 0.00676337, None, 1.00562, None, 0.00676337, None)

reports.append(Report(604054656, ("CSC", 2, 2, 2, 16), "MEm22_16"))
reports[-1].posNum = 50032
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000193776, 0.00496039, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.234354, 0.182976, 0), \
                           ValErr(5.21352e-05, 0.00200465, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.46166e-05, 5.2142e-05, 0), \
                           -70767.4, 50032, 50032, -nan)
reports[-1].sigmaresid = ValErr(0.99551, 0.00314706, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00790972, None, 1.36707e-05, None, 0.000740619, None, -2.92089e-06, None, 0.000740619, None, -2.92089e-06, None, 6.88851e-05, None, -4.98929e-06, None, 6.88851e-05, None, -4.98929e-06, None, 0.995533, None, 0.00656794, None, 0.995533, None, 0.00656794, None)

reports.append(Report(604054672, ("CSC", 2, 2, 2, 18), "MEm22_18"))
reports[-1].posNum = 52789
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00665325, 0.00480806, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.193547, 0.174746, 0), \
                           ValErr(0.00118073, 0.00193412, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.69383e-05, 5.10746e-05, 0), \
                           -75012, 52789, 52789, -nan)
reports[-1].sigmaresid = ValErr(1.00204, 0.00308389, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00545488, None, -4.06752e-05, None, -0.00483643, None, -1.79232e-05, None, -0.00483643, None, -1.79232e-05, None, -0.0108616, None, -5.04531e-05, None, -0.0108616, None, -5.04531e-05, None, 1.00206, None, 0.00718766, None, 1.00206, None, 0.00718766, None)

reports.append(Report(604054688, ("CSC", 2, 2, 2, 20), "MEm22_20"))
reports[-1].posNum = 54392
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00319683, 0.00478943, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0671411, 0.173889, 0), \
                           ValErr(0.00400397, 0.00194097, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.09719e-05, 5.10871e-05, 0), \
                           -77665.8, 54392, 54392, -nan)
reports[-1].sigmaresid = ValErr(1.00899, 0.00305914, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00340074, None, 6.26706e-06, None, 0.0012467, None, 7.44231e-05, None, 0.0012467, None, 7.44231e-05, None, 0.00510923, None, 3.45382e-07, None, 0.00510923, None, 3.45382e-07, None, 1.00904, None, 0.00650367, None, 1.00904, None, 0.00650367, None)

reports.append(Report(604054704, ("CSC", 2, 2, 2, 22), "MEm22_22"))
reports[-1].posNum = 50207
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00148119, 0.00499606, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.194454, 0.183069, 0), \
                           ValErr(-0.000518774, 0.00202072, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.27625e-06, 5.27198e-05, 0), \
                           -71054.2, 50207, 50207, -nan)
reports[-1].sigmaresid = ValErr(0.996293, 0.00314405, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00227722, None, 1.125e-06, None, 0.00188742, None, -1.87739e-06, None, 0.00188742, None, -1.87739e-06, None, 0.0127334, None, -2.66697e-05, None, 0.0127334, None, -2.66697e-05, None, 0.996305, None, 0.00684776, None, 0.996305, None, 0.00684776, None)

reports.append(Report(604054720, ("CSC", 2, 2, 2, 24), "MEm22_24"))
reports[-1].posNum = 55526
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0113063, 0.00470045, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0139563, 0.08534, 0), \
                           ValErr(0.000314789, 0.000949634, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.71214e-05, 5.02953e-05, 0), \
                           -78929.2, 55526, 55526, -nan)
reports[-1].sigmaresid = ValErr(1.00255, 0.00300414, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00774811, None, 7.27492e-06, None, -0.00944866, None, -1.13974e-05, None, -0.00944866, None, -1.13974e-05, None, -0.00510786, None, -7.17183e-05, None, -0.00510786, None, -7.17183e-05, None, 1.00255, None, 0.00673643, None, 1.00255, None, 0.00673643, None)

reports.append(Report(604054736, ("CSC", 2, 2, 2, 26), "MEm22_26"))
reports[-1].posNum = 49238
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00256511, 0.0050301, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.105305, 0.180821, 0), \
                           ValErr(-0.00110379, 0.00197606, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.16324e-05, 5.24772e-05, 0), \
                           -69333.4, 49238, 49238, -nan)
reports[-1].sigmaresid = ValErr(0.989248, 0.00315239, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00248896, None, 9.23698e-07, None, -0.000684444, None, 2.69535e-05, None, -0.000684444, None, 2.69535e-05, None, 0.00290458, None, -2.91057e-05, None, 0.00290458, None, -2.91057e-05, None, 0.98926, None, 0.00651861, None, 0.98926, None, 0.00651861, None)

reports.append(Report(604054752, ("CSC", 2, 2, 2, 28), "MEm22_28"))
reports[-1].posNum = 57299
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00168913, 0.0046544, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0503306, 0.170271, 0), \
                           ValErr(0.000786721, 0.00193022, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.57639e-05, 5.04854e-05, 0), \
                           -82250.5, 57299, 57299, -nan)
reports[-1].sigmaresid = ValErr(1.01666, 0.00300322, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(4.82152e-06, None, -5.60484e-08, None, 0.00033621, None, 4.03004e-05, None, 0.00033621, None, 4.03004e-05, None, 0.00392297, None, -2.54203e-05, None, 0.00392297, None, -2.54203e-05, None, 1.01667, None, 0.00663417, None, 1.01667, None, 0.00663417, None)

reports.append(Report(604054768, ("CSC", 2, 2, 2, 30), "MEm22_30"))
reports[-1].posNum = 49031
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0154621, 0.00497544, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.115164, 0.179222, 0), \
                           ValErr(-0.00159535, 0.00195782, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.30878e-05, 5.19038e-05, 0), \
                           -68918.7, 49031, 49031, -nan)
reports[-1].sigmaresid = ValErr(0.986766, 0.00315111, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0116098, None, -1.12491e-05, None, 0.0164686, None, -4.5934e-05, None, 0.0164686, None, -4.5934e-05, None, 0.0122665, None, -6.53386e-05, None, 0.0122665, None, -6.53386e-05, None, 0.98678, None, 0.00680024, None, 0.98678, None, 0.00680024, None)

reports.append(Report(604054784, ("CSC", 2, 2, 2, 32), "MEm22_32"))
reports[-1].posNum = 56668
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00465877, 0.00468189, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0345095, 0.17115, 0), \
                           ValErr(-0.00249206, 0.0019287, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.57834e-05, 5.05097e-05, 0), \
                           -81461.8, 56668, 56668, -nan)
reports[-1].sigmaresid = ValErr(1.01876, 0.00302613, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000995349, None, 3.54609e-05, None, 0.0028682, None, 5.28253e-05, None, 0.0028682, None, 5.28253e-05, None, 0.00920479, None, 7.26832e-06, None, 0.00920479, None, 7.26832e-06, None, 1.01879, None, 0.00666283, None, 1.01879, None, 0.00666283, None)

reports.append(Report(604054800, ("CSC", 2, 2, 2, 34), "MEm22_34"))
reports[-1].posNum = 51509
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00355115, 0.0048811, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.197569, 0.179585, 0), \
                           ValErr(-0.000955499, 0.00196585, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.25084e-05, 5.13737e-05, 0), \
                           -72323.8, 51509, 51509, -nan)
reports[-1].sigmaresid = ValErr(0.985277, 0.00306976, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00551418, None, 1.09956e-05, None, 0.00578205, None, 1.44462e-05, None, 0.00578205, None, 1.44462e-05, None, -0.00316115, None, 6.95092e-05, None, -0.00316115, None, 6.95092e-05, None, 0.985295, None, 0.00647067, None, 0.985295, None, 0.00647067, None)

reports.append(Report(604054816, ("CSC", 2, 2, 2, 36), "MEm22_36"))
reports[-1].posNum = 54728
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000926748, 0.00476789, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.122085, 0.171741, 0), \
                           ValErr(0.00191646, 0.0019207, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.37123e-05, 5.11667e-05, 0), \
                           -78021.4, 54728, 54728, -nan)
reports[-1].sigmaresid = ValErr(1.0067, 0.00304286, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00661077, None, 2.14707e-05, None, -0.00118495, None, -1.88057e-05, None, -0.00118495, None, -1.88057e-05, None, 0.0017911, None, -3.8585e-05, None, 0.0017911, None, -3.8585e-05, None, 1.00673, None, 0.00683894, None, 1.00673, None, 0.00683894, None)

reports.append(Report(604058120, ("CSC", 2, 3, 1, 1), "MEm31_01"))
reports[-1].posNum = 166860
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000739352, 0.00122985, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0549379, 0.0502945, 0), \
                           ValErr(0.00180579, 0.00112635, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.21491e-05, 2.80683e-05, 0), \
                           -120945, 166860, 166860, -nan)
reports[-1].sigmaresid = ValErr(0.499518, 0.000864691, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00111558, None, -6.55102e-06, None, 0.000979347, None, -2.10886e-05, None, 0.000979347, None, -2.10886e-05, None, 0.00043998, None, -1.20108e-06, None, 0.00043998, None, -1.20108e-06, None, 0.499528, None, 0.00590934, None, 0.499528, None, 0.00590934, None)

reports.append(Report(604058136, ("CSC", 2, 3, 1, 3), "MEm31_03"))
reports[-1].posNum = 169339
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00301739, 0.00122329, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.04877, 0.0500358, 0), \
                           ValErr(-0.00184543, 0.00112374, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.25154e-05, 2.79641e-05, 0), \
                           -123079, 169339, 169339, -nan)
reports[-1].sigmaresid = ValErr(0.500516, 0.000860051, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00453361, None, 3.98884e-06, None, 0.0029521, None, 3.17334e-06, None, 0.0029521, None, 3.17334e-06, None, 0.00372082, None, -4.28855e-06, None, 0.00372082, None, -4.28855e-06, None, 0.500521, None, 0.00598844, None, 0.500521, None, 0.00598844, None)

reports.append(Report(604058152, ("CSC", 2, 3, 1, 5), "MEm31_05"))
reports[-1].posNum = 169032
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0011536, 0.00122571, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0940657, 0.0501338, 0), \
                           ValErr(-0.000640455, 0.0011243, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.671e-05, 2.803e-05, 0), \
                           -122955, 169032, 169032, -nan)
reports[-1].sigmaresid = ValErr(0.500808, 0.000861333, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00239995, None, -2.08041e-05, None, -0.00108444, None, -2.85107e-05, None, -0.00108444, None, -2.85107e-05, None, 6.02683e-05, None, -9.88103e-06, None, 6.02683e-05, None, -9.88103e-06, None, 0.500813, None, 0.00594948, None, 0.500813, None, 0.00594948, None)

reports.append(Report(604058168, ("CSC", 2, 3, 1, 7), "MEm31_07"))
reports[-1].posNum = 167358
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00249522, 0.00122384, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0145697, 0.0499439, 0), \
                           ValErr(0.00204254, 0.00111597, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.71684e-05, 2.79093e-05, 0), \
                           -120648, 167358, 167358, -nan)
reports[-1].sigmaresid = ValErr(0.497558, 0.000860016, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00238299, None, 2.21059e-05, None, 0.00240816, None, 3.07716e-05, None, 0.00240816, None, 3.07716e-05, None, 0.00361885, None, 1.24041e-05, None, 0.00361885, None, 1.24041e-05, None, 0.497564, None, 0.00584376, None, 0.497564, None, 0.00584376, None)

reports.append(Report(604058184, ("CSC", 2, 3, 1, 9), "MEm31_09"))
reports[-1].posNum = 167223
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000778352, 0.00122592, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.00800255, 0.05028, 0), \
                           ValErr(-0.00109345, 0.00112492, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.63213e-05, 2.80055e-05, 0), \
                           -120782, 167223, 167223, -nan)
reports[-1].sigmaresid = ValErr(0.498248, 0.000861556, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000280773, None, -2.74468e-05, None, -0.000554887, None, -2.42259e-05, None, -0.000554887, None, -2.42259e-05, None, -0.000345057, None, -2.83117e-05, None, -0.000345057, None, -2.83117e-05, None, 0.498254, None, 0.00616201, None, 0.498254, None, 0.00616201, None)

reports.append(Report(604058200, ("CSC", 2, 3, 1, 11), "MEm31_11"))
reports[-1].posNum = 166953
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00289192, 0.0012277, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0528508, 0.0502801, 0), \
                           ValErr(-0.000358496, 0.00112282, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.02185e-05, 2.80073e-05, 0), \
                           -120786, 166953, 166953, -nan)
reports[-1].sigmaresid = ValErr(0.498841, 0.000863279, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0028037, None, -3.10491e-05, None, -0.00284703, None, -4.75405e-05, None, -0.00284703, None, -4.75405e-05, None, -0.00384065, None, -3.70248e-05, None, -0.00384065, None, -3.70248e-05, None, 0.498843, None, 0.00595482, None, 0.498843, None, 0.00595482, None)

reports.append(Report(604058216, ("CSC", 2, 3, 1, 13), "MEm31_13"))
reports[-1].posNum = 168158
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00199975, 0.00122036, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.115925, 0.049882, 0), \
                           ValErr(0.000571291, 0.00111312, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.44071e-05, 2.77885e-05, 0), \
                           -121188, 168158, 168158, -nan)
reports[-1].sigmaresid = ValErr(0.497451, 0.000857782, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00113248, None, -8.84195e-06, None, -0.00175306, None, -1.90682e-06, None, -0.00175306, None, -1.90682e-06, None, -0.00129568, None, 6.55989e-06, None, -0.00129568, None, 6.55989e-06, None, 0.497467, None, 0.00605773, None, 0.497467, None, 0.00605773, None)

reports.append(Report(604058232, ("CSC", 2, 3, 1, 15), "MEm31_15"))
reports[-1].posNum = 167458
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00188078, 0.00122458, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.043034, 0.0500742, 0), \
                           ValErr(-2.25296e-05, 0.0011155, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.21393e-05, 2.78828e-05, 0), \
                           -120977, 167458, 167458, -nan)
reports[-1].sigmaresid = ValErr(0.498324, 0.000861082, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00152481, None, 8.20136e-06, None, 0.00178652, None, -1.56101e-05, None, 0.00178652, None, -1.56101e-05, None, 0.00154638, None, -3.00122e-06, None, 0.00154638, None, -3.00122e-06, None, 0.498326, None, 0.00598625, None, 0.498326, None, 0.00598625, None)

reports.append(Report(604058248, ("CSC", 2, 3, 1, 17), "MEm31_17"))
reports[-1].posNum = 168016
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000146218, 0.00122256, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0132414, 0.0500459, 0), \
                           ValErr(0.000610156, 0.00111657, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.43765e-05, 2.78507e-05, 0), \
                           -121329, 168016, 168016, -nan)
reports[-1].sigmaresid = ValErr(0.498173, 0.000859389, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000208822, None, -1.07749e-05, None, -3.03448e-05, None, -1.1416e-05, None, -3.03448e-05, None, -1.1416e-05, None, 0.00215062, None, -1.0707e-05, None, 0.00215062, None, -1.0707e-05, None, 0.498175, None, 0.00596814, None, 0.498175, None, 0.00596814, None)

reports.append(Report(604058128, ("CSC", 2, 3, 1, 2), "MEm31_02"))
reports[-1].posNum = 172595
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00182601, 0.00124843, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.00672131, 0.0524407, 0), \
                           ValErr(-0.000119362, 0.00117546, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.05643e-05, 2.84876e-05, 0), \
                           -130564, 172595, 172595, -nan)
reports[-1].sigmaresid = ValErr(0.51558, 0.000877541, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00173644, None, -1.28424e-05, None, -0.00172715, None, -6.33506e-06, None, -0.00172715, None, -6.33506e-06, None, -0.00202008, None, -1.79976e-05, None, -0.00202008, None, -1.79976e-05, None, 0.515581, None, 0.00587229, None, 0.515581, None, 0.00587229, None)

reports.append(Report(604058144, ("CSC", 2, 3, 1, 4), "MEm31_04"))
reports[-1].posNum = 172132
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000970541, 0.00124681, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.112989, 0.0522592, 0), \
                           ValErr(0.00134846, 0.00116671, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.56096e-05, 2.83901e-05, 0), \
                           -129727, 172132, 172132, -nan)
reports[-1].sigmaresid = ValErr(0.514123, 0.000876238, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-6.39987e-05, None, 7.29807e-07, None, 0.000789886, None, 3.54181e-06, None, 0.000789886, None, 3.54181e-06, None, -0.000638296, None, -4.52224e-06, None, -0.000638296, None, -4.52224e-06, None, 0.514137, None, 0.00597262, None, 0.514137, None, 0.00597262, None)

reports.append(Report(604058160, ("CSC", 2, 3, 1, 6), "MEm31_06"))
reports[-1].posNum = 171998
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000931678, 0.00125794, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0493843, 0.052664, 0), \
                           ValErr(-0.000385826, 0.00117659, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.49649e-06, 2.86901e-05, 0), \
                           -131123, 171998, 171998, -nan)
reports[-1].sigmaresid = ValErr(0.518619, 0.000884244, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00233433, None, -1.14983e-05, None, 0.000921389, None, -2.36321e-05, None, 0.000921389, None, -2.36321e-05, None, -0.00166337, None, -2.94273e-05, None, -0.00166337, None, -2.94273e-05, None, 0.51862, None, 0.00577549, None, 0.51862, None, 0.00577549, None)

reports.append(Report(604058176, ("CSC", 2, 3, 1, 8), "MEm31_08"))
reports[-1].posNum = 172594
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000209399, 0.00125345, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.104593, 0.0526065, 0), \
                           ValErr(0.000222162, 0.00117482, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.1366e-05, 2.86129e-05, 0), \
                           -131272, 172594, 172594, -nan)
reports[-1].sigmaresid = ValErr(0.517704, 0.00088116, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00121956, None, -3.29974e-06, None, -5.13382e-05, None, -1.02028e-05, None, -5.13382e-05, None, -1.02028e-05, None, -0.000946331, None, -1.75752e-05, None, -0.000946331, None, -1.75752e-05, None, 0.517711, None, 0.0057442, None, 0.517711, None, 0.0057442, None)

reports.append(Report(604058192, ("CSC", 2, 3, 1, 10), "MEm31_10"))
reports[-1].posNum = 171597
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00242892, 0.00126455, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.00138818, 0.0531249, 0), \
                           ValErr(0.000407912, 0.00118506, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.79072e-06, 2.88705e-05, 0), \
                           -131669, 171597, 171597, -nan)
reports[-1].sigmaresid = ValErr(0.521198, 0.000889679, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00242264, None, 1.33012e-05, None, 0.00240853, None, -1.76272e-06, None, 0.00240853, None, -1.76272e-06, None, 0.00413969, None, 5.5565e-06, None, 0.00413969, None, 5.5565e-06, None, 0.521199, None, 0.00589315, None, 0.521199, None, 0.00589315, None)

reports.append(Report(604058208, ("CSC", 2, 3, 1, 12), "MEm31_12"))
reports[-1].posNum = 171852
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00299365, 0.00126081, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.00522883, 0.0529076, 0), \
                           ValErr(-0.000216697, 0.00118038, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(9.38528e-06, 2.87862e-05, 0), \
                           -131372, 171852, 171852, -nan)
reports[-1].sigmaresid = ValErr(0.519707, 0.000886475, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00326668, None, 5.22334e-06, None, 0.00303682, None, -1.07163e-06, None, 0.00303682, None, -1.07163e-06, None, 0.00401786, None, 1.75792e-05, None, 0.00401786, None, 1.75792e-05, None, 0.519707, None, 0.00582033, None, 0.519707, None, 0.00582033, None)

reports.append(Report(604058224, ("CSC", 2, 3, 1, 14), "MEm31_14"))
reports[-1].posNum = 171987
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00130793, 0.00125795, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0194859, 0.0527514, 0), \
                           ValErr(-0.00213942, 0.00117675, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.19549e-05, 2.8754e-05, 0), \
                           -131237, 171987, 171987, -nan)
reports[-1].sigmaresid = ValErr(0.518988, 0.000884901, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00121126, None, -7.72094e-06, None, -0.00125209, None, -1.75495e-05, None, -0.00125209, None, -1.75495e-05, None, -0.00171422, None, -1.13506e-05, None, -0.00171422, None, -1.13506e-05, None, 0.518993, None, 0.00587659, None, 0.518993, None, 0.00587659, None)

reports.append(Report(604058240, ("CSC", 2, 3, 1, 16), "MEm31_16"))
reports[-1].posNum = 172187
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0030083, 0.00125471, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0117764, 0.0526336, 0), \
                           ValErr(0.000861711, 0.0011796, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.04597e-05, 2.87029e-05, 0), \
                           -131001, 172187, 172187, -nan)
reports[-1].sigmaresid = ValErr(0.517816, 0.00088239, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00291736, None, 1.15729e-05, None, -0.00282324, None, -2.51677e-06, None, -0.00282324, None, -2.51677e-06, None, -0.00178873, None, 1.61088e-05, None, -0.00178873, None, 1.61088e-05, None, 0.51782, None, 0.00588066, None, 0.51782, None, 0.00588066, None)

reports.append(Report(604058256, ("CSC", 2, 3, 1, 18), "MEm31_18"))
reports[-1].posNum = 173442
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00122282, 0.00124901, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0947284, 0.0524942, 0), \
                           ValErr(-0.000927176, 0.00117232, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.17228e-06, 2.85047e-05, 0), \
                           -131740, 173442, 173442, -nan)
reports[-1].sigmaresid = ValErr(0.517175, 0.000878102, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00123942, None, 1.15113e-06, None, -0.00126687, None, -2.17652e-05, None, -0.00126687, None, -2.17652e-05, None, -0.00258293, None, -2.95165e-05, None, -0.00258293, None, -2.95165e-05, None, 0.517182, None, 0.00582965, None, 0.517182, None, 0.00582965, None)

reports.append(Report(604058632, ("CSC", 2, 3, 2, 1), "MEm32_01"))
reports[-1].posNum = 59928
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00461576, 0.00470465, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.243583, 0.198335, 0), \
                           ValErr(0.00388981, 0.00225894, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.65043e-05, 5.1721e-05, 0), \
                           -88786, 59928, 59928, -nan)
reports[-1].sigmaresid = ValErr(1.06461, 0.00307511, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0062864, None, -1.95287e-05, None, 0.00517837, None, -7.50188e-06, None, 0.00517837, None, -7.50188e-06, None, 0.00403905, None, -1.18713e-06, None, 0.00403905, None, -1.18713e-06, None, 1.06465, None, 0.00777559, None, 1.06465, None, 0.00777559, None)

reports.append(Report(604058648, ("CSC", 2, 3, 2, 3), "MEm32_03"))
reports[-1].posNum = 55059
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00297729, 0.00482057, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.233838, 0.200063, 0), \
                           ValErr(-0.00108799, 0.00225412, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.44089e-05, 5.21212e-05, 0), \
                           -79216, 55059, 55059, -nan)
reports[-1].sigmaresid = ValErr(1.02001, 0.00307379, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00525806, None, -3.04274e-05, None, -1.46531e-05, None, 4.99992e-06, None, -1.46531e-05, None, 4.99992e-06, None, -0.00457153, None, 1.39971e-05, None, -0.00457153, None, 1.39971e-05, None, 1.02004, None, 0.00784538, None, 1.02004, None, 0.00784538, None)

reports.append(Report(604058664, ("CSC", 2, 3, 2, 5), "MEm32_05"))
reports[-1].posNum = 58877
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00657441, 0.0046737, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.426838, 0.19885, 0), \
                           ValErr(0.00396583, 0.00225832, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.88685e-05, 5.13181e-05, 0), \
                           -86398.4, 58877, 58877, -nan)
reports[-1].sigmaresid = ValErr(1.0497, 0.00305898, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00140532, None, -1.0112e-05, None, -0.00421909, None, -1.44682e-05, None, -0.00421909, None, -1.44682e-05, None, -0.0022024, None, 7.81977e-06, None, -0.0022024, None, 7.81977e-06, None, 1.04978, None, 0.00752962, None, 1.04978, None, 0.00752962, None)

reports.append(Report(604058680, ("CSC", 2, 3, 2, 7), "MEm32_07"))
reports[-1].posNum = 54984
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00107153, 0.00490366, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.185136, 0.202834, 0), \
                           ValErr(0.00290224, 0.00229811, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.77579e-05, 5.32709e-05, 0), \
                           -80171.2, 54984, 54984, -nan)
reports[-1].sigmaresid = ValErr(1.03992, 0.00313594, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000869086, None, -1.30063e-05, None, 0.00168871, None, -4.08098e-05, None, 0.00168871, None, -4.08098e-05, None, 0.00699733, None, -1.3897e-05, None, 0.00699733, None, -1.3897e-05, None, 1.03996, None, 0.00820978, None, 1.03996, None, 0.00820978, None)

reports.append(Report(604058696, ("CSC", 2, 3, 2, 9), "MEm32_09"))
reports[-1].posNum = 57490
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-2.34207e-05, 0.00476458, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.24142, 0.104167, 0), \
                           ValErr(0.00159022, 0.00225815, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.22408e-05, 5.18032e-05, 0), \
                           -84195.2, 57490, 57490, -nan)
reports[-1].sigmaresid = ValErr(1.04664, 0.00302577, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000150665, None, 3.2612e-05, None, -0.00117872, None, 8.11635e-06, None, -0.00117872, None, 8.11635e-06, None, 0.000931285, None, 6.43903e-05, None, 0.000931285, None, 6.43903e-05, None, 1.04666, None, 0.00763096, None, 1.04666, None, 0.00763096, None)

reports.append(Report(604058712, ("CSC", 2, 3, 2, 11), "MEm32_11"))
reports[-1].posNum = 57333
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00375532, 0.00478785, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00803882, 0.203363, 0), \
                           ValErr(0.00310633, 0.00229642, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.72227e-05, 5.19942e-05, 0), \
                           -83880.7, 57333, 57333, -nan)
reports[-1].sigmaresid = ValErr(1.04509, 0.00308629, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00461249, None, 1.24592e-05, None, -0.00193157, None, -3.06587e-05, None, -0.00193157, None, -3.06587e-05, None, -0.0025766, None, -1.15945e-05, None, -0.0025766, None, -1.15945e-05, None, 1.04512, None, 0.0077635, None, 1.04512, None, 0.0077635, None)

reports.append(Report(604058728, ("CSC", 2, 3, 2, 13), "MEm32_13"))
reports[-1].posNum = 53988
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00713738, 0.00495618, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0338066, 0.199476, 0), \
                           ValErr(-0.000674439, 0.00135177, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.56947e-05, 5.32261e-05, 0), \
                           -78670.2, 53988, 53988, -nan)
reports[-1].sigmaresid = ValErr(1.03898, 0.00315021, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0104393, None, 7.49629e-07, None, 0.00569871, None, 4.08449e-06, None, 0.00569871, None, 4.08449e-06, None, -0.00040319, None, 3.77845e-05, None, -0.00040319, None, 3.77845e-05, None, 1.03899, None, 0.00751225, None, 1.03899, None, 0.00751225, None)

reports.append(Report(604058744, ("CSC", 2, 3, 2, 15), "MEm32_15"))
reports[-1].posNum = 58434
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0135741, 0.00466902, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.08357, 0.166783, 0), \
                           ValErr(-0.00259832, 0.00180517, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.31496e-05, 5.14268e-05, 0), \
                           -85352.3, 58434, 58434, -nan)
reports[-1].sigmaresid = ValErr(1.04261, 0.00304293, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0105581, None, 4.58694e-05, None, 0.0120296, None, -7.55337e-06, None, 0.0120296, None, -7.55337e-06, None, 0.0144787, None, 2.87554e-05, None, 0.0144787, None, 2.87554e-05, None, 1.04262, None, 0.00811369, None, 1.04262, None, 0.00811369, None)

reports.append(Report(604058760, ("CSC", 2, 3, 2, 17), "MEm32_17"))
reports[-1].posNum = 54978
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0111786, 0.00485244, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.214733, 0.202892, 0), \
                           ValErr(0.00476545, 0.00227585, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000174114, 5.24349e-05, 0), \
                           -79295.7, 54978, 54978, -nan)
reports[-1].sigmaresid = ValErr(1.02365, 0.00308705, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00824746, None, 1.5209e-05, None, 0.00412381, None, -2.36676e-07, None, 0.00412381, None, -2.36676e-07, None, 0.00825092, None, 5.67056e-05, None, 0.00825092, None, 5.67056e-05, None, 1.0238, None, 0.0073068, None, 1.0238, None, 0.0073068, None)

reports.append(Report(604058776, ("CSC", 2, 3, 2, 19), "MEm32_19"))
reports[-1].posNum = 59645
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00652459, 0.00466872, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.163308, 0.155392, 0), \
                           ValErr(0.00305192, 0.00180063, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.49904e-05, 5.14803e-05, 0), \
                           -87781.7, 59645, 59645, -nan)
reports[-1].sigmaresid = ValErr(1.05422, 0.00304663, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0016211, None, 1.69467e-05, None, 0.00453072, None, 1.6251e-05, None, 0.00453072, None, 1.6251e-05, None, 0.00522099, None, 5.40295e-06, None, 0.00522099, None, 5.40295e-06, None, 1.05425, None, 0.00763687, None, 1.05425, None, 0.00763687, None)

reports.append(Report(604058792, ("CSC", 2, 3, 2, 21), "MEm32_21"))
reports[-1].posNum = 54161
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00802773, 0.00484972, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0384048, 0.20338, 0), \
                           ValErr(0.00512732, 0.00225615, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.37271e-05, 5.18108e-05, 0), \
                           -77758.2, 54161, 54161, -nan)
reports[-1].sigmaresid = ValErr(1.01688, 0.00308967, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00609963, None, -1.53444e-06, None, 0.00755637, None, -7.6099e-05, None, 0.00755637, None, -7.6099e-05, None, 0.00447975, None, -2.34341e-05, None, 0.00447975, None, -2.34341e-05, None, 1.01694, None, 0.00929121, None, 1.01694, None, 0.00929121, None)

reports.append(Report(604058808, ("CSC", 2, 3, 2, 23), "MEm32_23"))
reports[-1].posNum = 59725
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000885334, 0.00463644, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.392621, 0.196909, 0), \
                           ValErr(-0.0030964, 0.00223857, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000121105, 5.09344e-05, 0), \
                           -87720.3, 59725, 59725, -nan)
reports[-1].sigmaresid = ValErr(1.05106, 0.00304113, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00183072, None, -1.25577e-05, None, -0.00498858, None, 1.25361e-05, None, -0.00498858, None, 1.25361e-05, None, -0.00623459, None, 2.49406e-05, None, -0.00623459, None, 2.49406e-05, None, 1.05116, None, 0.00754504, None, 1.05116, None, 0.00754504, None)

reports.append(Report(604058824, ("CSC", 2, 3, 2, 25), "MEm32_25"))
reports[-1].posNum = 55806
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00215226, 0.00482799, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.165529, 0.20101, 0), \
                           ValErr(-0.000218392, 0.00227099, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.46677e-05, 5.24341e-05, 0), \
                           -80858.4, 55806, 55806, -nan)
reports[-1].sigmaresid = ValErr(1.03044, 0.00308436, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00133984, None, 2.06614e-05, None, -3.18814e-05, None, -2.06643e-05, None, -3.18814e-05, None, -2.06643e-05, None, -0.000912789, None, 2.28686e-05, None, -0.000912789, None, 2.28686e-05, None, 1.03045, None, 0.00737744, None, 1.03045, None, 0.00737744, None)

reports.append(Report(604058840, ("CSC", 2, 3, 2, 27), "MEm32_27"))
reports[-1].posNum = 56950
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-6.57291e-05, 0.00478212, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.37464, 0.202452, 0), \
                           ValErr(0.000273338, 0.00227574, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.86093e-06, 5.20018e-05, 0), \
                           -83571.1, 56950, 56950, -nan)
reports[-1].sigmaresid = ValErr(1.04971, 0.00311034, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00445257, None, 1.39107e-06, None, -0.000475039, None, -3.30551e-05, None, -0.000475039, None, -3.30551e-05, None, 0.00383278, None, -7.01022e-06, None, 0.00383278, None, -7.01022e-06, None, 1.04974, None, 0.00798329, None, 1.04974, None, 0.00798329, None)

reports.append(Report(604058856, ("CSC", 2, 3, 2, 29), "MEm32_29"))
reports[-1].posNum = 57100
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00922415, 0.00475846, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0766127, 0.0976354, 0), \
                           ValErr(3.39301e-05, 0.00110298, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000114999, 5.17929e-05, 0), \
                           -83472.2, 57100, 57100, -nan)
reports[-1].sigmaresid = ValErr(1.04386, 0.00308547, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00719327, None, -3.47357e-05, None, -0.00500724, None, -4.41142e-05, None, -0.00500724, None, -4.41142e-05, None, -0.00828882, None, -7.72885e-05, None, -0.00828882, None, -7.72885e-05, None, 1.0439, None, 0.00736034, None, 1.0439, None, 0.00736034, None)

reports.append(Report(604058872, ("CSC", 2, 3, 2, 31), "MEm32_31"))
reports[-1].posNum = 56019
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00363869, 0.00489043, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.156375, 0.201613, 0), \
                           ValErr(0.000296916, 0.00228037, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.26069e-05, 5.30533e-05, 0), \
                           -81915.9, 56019, 56019, -nan)
reports[-1].sigmaresid = ValErr(1.0443, 0.00311993, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0041523, None, -2.06806e-05, None, 0.00267591, None, -5.13525e-05, None, 0.00267591, None, -5.13525e-05, None, -0.000780184, None, -3.98425e-05, None, -0.000780184, None, -3.98425e-05, None, 1.04431, None, 0.00764192, None, 1.04431, None, 0.00764192, None)

reports.append(Report(604058888, ("CSC", 2, 3, 2, 33), "MEm32_33"))
reports[-1].posNum = 59428
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0104562, 0.00463416, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.410069, 0.196871, 0), \
                           ValErr(-0.000585939, 0.00223337, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.77913e-05, 5.08366e-05, 0), \
                           -87094.8, 59428, 59428, -nan)
reports[-1].sigmaresid = ValErr(1.04772, 0.00303903, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0136712, None, 8.92879e-06, None, 0.00870997, None, -2.23066e-05, None, 0.00870997, None, -2.23066e-05, None, 0.0123146, None, -1.65413e-05, None, 0.0123146, None, -1.65413e-05, None, 1.04776, None, 0.00769431, None, 1.04776, None, 0.00769431, None)

reports.append(Report(604058904, ("CSC", 2, 3, 2, 35), "MEm32_35"))
reports[-1].posNum = 54182
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0158964, 0.004905, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0542039, 0.181575, 0), \
                           ValErr(-0.000984657, 0.00169285, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.79185e-05, 5.23449e-05, 0), \
                           -78247.8, 54182, 54182, -nan)
reports[-1].sigmaresid = ValErr(1.02555, 0.00311282, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0160117, None, 5.53238e-05, None, 0.0122566, None, 3.57045e-05, None, 0.0122566, None, 3.57045e-05, None, 0.0199211, None, 4.32878e-05, None, 0.0199211, None, 4.32878e-05, None, 1.02558, None, 0.00763577, None, 1.02558, None, 0.00763577, None)

reports.append(Report(604058640, ("CSC", 2, 3, 2, 2), "MEm32_02"))
reports[-1].posNum = 59017
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00228153, 0.00474614, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.203714, 0.101705, 0), \
                           ValErr(0.00133866, 0.00120332, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.98656e-05, 5.17304e-05, 0), \
                           -87332.6, 59017, 59017, -nan)
reports[-1].sigmaresid = ValErr(1.06274, 0.00301878, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00260613, None, -3.14518e-05, None, -0.000353416, None, -2.76793e-05, None, -0.000353416, None, -2.76793e-05, None, 0.00464273, None, -1.58384e-05, None, 0.00464273, None, -1.58384e-05, None, 1.06277, None, 0.00725394, None, 1.06277, None, 0.00725394, None)

reports.append(Report(604058656, ("CSC", 2, 3, 2, 4), "MEm32_04"))
reports[-1].posNum = 57442
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00201814, 0.00482704, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.200515, 0.208632, 0), \
                           ValErr(-0.000106472, 0.00236374, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.56848e-05, 5.24692e-05, 0), \
                           -84119.2, 57442, 57442, -nan)
reports[-1].sigmaresid = ValErr(1.04653, 0.00308762, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00267331, None, 2.97531e-05, None, -0.00295593, None, 2.78969e-05, None, -0.00295593, None, 2.78969e-05, None, -0.00418647, None, 1.98174e-05, None, -0.00418647, None, 1.98174e-05, None, 1.04654, None, 0.00697676, None, 1.04654, None, 0.00697676, None)

reports.append(Report(604058672, ("CSC", 2, 3, 2, 6), "MEm32_06"))
reports[-1].posNum = 61616
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000340919, 0.00465173, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.277205, 0.203769, 0), \
                           ValErr(-0.000118097, 0.00232015, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.7051e-05, 5.12171e-05, 0), \
                           -91772.5, 61616, 61616, -nan)
reports[-1].sigmaresid = ValErr(1.07303, 0.0030567, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00744477, None, 9.26916e-06, None, -0.00191066, None, 4.54343e-05, None, -0.00191066, None, 4.54343e-05, None, -0.000892287, None, 2.6388e-05, None, -0.000892287, None, 2.6388e-05, None, 1.07306, None, 0.00743756, None, 1.07306, None, 0.00743756, None)

reports.append(Report(604058688, ("CSC", 2, 3, 2, 8), "MEm32_08"))
reports[-1].posNum = 55649
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00589357, 0.00486724, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.210795, 0.208098, 0), \
                           ValErr(0.00516364, 0.00236071, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.33924e-05, 5.28069e-05, 0), \
                           -80564, 55649, 55649, -nan)
reports[-1].sigmaresid = ValErr(1.02919, 0.00308498, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00335426, None, 1.60398e-05, None, 0.00488148, None, 2.49314e-05, None, 0.00488148, None, 2.49314e-05, None, -0.00602277, None, 1.85262e-06, None, -0.00602277, None, 1.85262e-06, None, 1.02925, None, 0.00684671, None, 1.02925, None, 0.00684671, None)

reports.append(Report(604058704, ("CSC", 2, 3, 2, 10), "MEm32_10"))
reports[-1].posNum = 62343
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00797311, 0.00461837, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0466417, 0.152358, 0), \
                           ValErr(0.00130829, 0.00190019, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.33374e-05, 5.1064e-05, 0), \
                           -93214.8, 62343, 62343, -nan)
reports[-1].sigmaresid = ValErr(1.07924, 0.00304852, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00304282, None, 5.75604e-06, None, -0.00597969, None, -5.81775e-05, None, -0.00597969, None, -5.81775e-05, None, -0.000347136, None, -2.96042e-05, None, -0.000347136, None, -2.96042e-05, None, 1.07925, None, 0.00736173, None, 1.07925, None, 0.00736173, None)

reports.append(Report(604058720, ("CSC", 2, 3, 2, 12), "MEm32_12"))
reports[-1].posNum = 57104
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00415857, 0.00481825, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.321866, 0.207727, 0), \
                           ValErr(0.00375681, 0.00235909, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.86909e-05, 5.26114e-05, 0), \
                           -83193.2, 57104, 57104, -nan)
reports[-1].sigmaresid = ValErr(1.03866, 0.00307346, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00227059, None, 3.61109e-05, None, -0.00463651, None, 3.86863e-06, None, -0.00463651, None, 3.86863e-06, None, -0.00928839, None, -2.49053e-05, None, -0.00928839, None, -2.49053e-05, None, 1.0387, None, 0.00747135, None, 1.0387, None, 0.00747135, None)

reports.append(Report(604058736, ("CSC", 2, 3, 2, 14), "MEm32_14"))
reports[-1].posNum = 60918
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00655175, 0.0046153, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.298995, 0.176215, 0), \
                           ValErr(0.00190822, 0.00169798, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(8.00084e-05, 5.06931e-05, 0), \
                           -89785.6, 60918, 60918, -nan)
reports[-1].sigmaresid = ValErr(1.05648, 0.00293233, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000710766, None, 2.72657e-05, None, -0.00379282, None, -9.21401e-06, None, -0.00379282, None, -9.21401e-06, None, -0.00261027, None, 4.80535e-05, None, -0.00261027, None, 4.80535e-05, None, 1.05652, None, 0.00724196, None, 1.05652, None, 0.00724196, None)

reports.append(Report(604058752, ("CSC", 2, 3, 2, 16), "MEm32_16"))
reports[-1].posNum = 57336
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00828467, 0.00482468, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0444283, 0.209028, 0), \
                           ValErr(0.00134489, 0.00235686, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.81229e-05, 5.23977e-05, 0), \
                           -84000.6, 57336, 57336, -nan)
reports[-1].sigmaresid = ValErr(1.0472, 0.00309245, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00368443, None, 5.50015e-05, None, 0.00450626, None, 2.62545e-05, None, 0.00450626, None, 2.62545e-05, None, 0.00967899, None, 3.70828e-05, None, 0.00967899, None, 3.70828e-05, None, 1.04724, None, 0.0071535, None, 1.04724, None, 0.0071535, None)

reports.append(Report(604058768, ("CSC", 2, 3, 2, 18), "MEm32_18"))
reports[-1].posNum = 58489
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0126051, 0.00475203, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.00742208, 0.0975885, 0), \
                           ValErr(0.000121294, 0.00109473, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.03593e-05, 5.18044e-05, 0), \
                           -86038.6, 58489, 58489, -nan)
reports[-1].sigmaresid = ValErr(1.05346, 0.00308038, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0067519, None, -2.6045e-05, None, -0.0107626, None, -3.17712e-05, None, -0.0107626, None, -3.17712e-05, None, -0.0138443, None, -3.363e-05, None, -0.0138443, None, -3.363e-05, None, 1.05347, None, 0.00763627, None, 1.05347, None, 0.00763627, None)

reports.append(Report(604058784, ("CSC", 2, 3, 2, 20), "MEm32_20"))
reports[-1].posNum = 60200
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0030504, 0.00471491, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.340969, 0.203973, 0), \
                           ValErr(-0.00506559, 0.00233626, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.78213e-05, 5.19527e-05, 0), \
                           -89001.9, 60200, 60200, -nan)
reports[-1].sigmaresid = ValErr(1.06131, 0.00305865, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00598435, None, -1.82687e-05, None, -0.00446472, None, 2.55652e-05, None, -0.00446472, None, 2.55652e-05, None, -0.00748343, None, -2.09176e-06, None, -0.00748343, None, -2.09176e-06, None, 1.06138, None, 0.00759415, None, 1.06138, None, 0.00759415, None)

reports.append(Report(604058800, ("CSC", 2, 3, 2, 22), "MEm32_22"))
reports[-1].posNum = 56960
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00856242, 0.00486208, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0796636, 0.102967, 0), \
                           ValErr(0.000517915, 0.00122899, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.85309e-05, 5.34817e-05, 0), \
                           -83632.2, 56960, 56960, -nan)
reports[-1].sigmaresid = ValErr(1.05056, 0.00309672, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00310671, None, 2.7803e-05, None, 0.0046221, None, 1.28583e-05, None, 0.0046221, None, 1.28583e-05, None, 0.00226517, None, 1.41492e-06, None, 0.00226517, None, 1.41492e-06, None, 1.05059, None, 0.0076943, None, 1.05059, None, 0.0076943, None)

reports.append(Report(604058816, ("CSC", 2, 3, 2, 24), "MEm32_24"))
reports[-1].posNum = 61184
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00701353, 0.00463345, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.157751, 0.160555, 0), \
                           ValErr(-0.000390892, 0.00183256, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.77298e-05, 5.10694e-05, 0), \
                           -90362.4, 61184, 61184, -nan)
reports[-1].sigmaresid = ValErr(1.05967, 0.00301601, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00190054, None, -1.73949e-05, None, 0.0046099, None, 1.79306e-05, None, 0.0046099, None, 1.79306e-05, None, 0.00721211, None, 1.17528e-05, None, 0.00721211, None, 1.17528e-05, None, 1.05969, None, 0.00723427, None, 1.05969, None, 0.00723427, None)

reports.append(Report(604058832, ("CSC", 2, 3, 2, 26), "MEm32_26"))
reports[-1].posNum = 56806
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00409179, 0.00484549, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.191868, 0.207537, 0), \
                           ValErr(-0.00237087, 0.00235254, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.73454e-05, 5.26898e-05, 0), \
                           -82601.8, 56806, 56806, -nan)
reports[-1].sigmaresid = ValErr(1.03579, 0.00307299, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00266107, None, 2.74077e-05, None, 0.00181053, None, 4.78794e-05, None, 0.00181053, None, 4.78794e-05, None, -0.00107283, None, 4.60116e-05, None, -0.00107283, None, 4.60116e-05, None, 1.03582, None, 0.00708897, None, 1.03582, None, 0.00708897, None)

reports.append(Report(604058848, ("CSC", 2, 3, 2, 28), "MEm32_28"))
reports[-1].posNum = 62199
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00443246, 0.00465944, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.00737837, 0.0937657, 0), \
                           ValErr(-0.000229364, 0.00107382, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.84491e-05, 5.13836e-05, 0), \
                           -93137.3, 62199, 62199, -nan)
reports[-1].sigmaresid = ValErr(1.08163, 0.00306628, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000756224, None, -2.65068e-05, None, -0.00381797, None, -3.06756e-05, None, -0.00381797, None, -3.06756e-05, None, 0.00145721, None, -8.32936e-06, None, 0.00145721, None, -8.32936e-06, None, 1.08163, None, 0.00739972, None, 1.08163, None, 0.00739972, None)

reports.append(Report(604058864, ("CSC", 2, 3, 2, 30), "MEm32_30"))
reports[-1].posNum = 56207
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00793786, 0.00485155, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0338987, 0.207255, 0), \
                           ValErr(-0.000659298, 0.00113857, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.25116e-05, 5.23924e-05, 0), \
                           -81560.2, 56207, 56207, -nan)
reports[-1].sigmaresid = ValErr(1.03265, 0.00306845, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00486616, None, -7.08756e-07, None, -0.0088597, None, -1.929e-05, None, -0.0088597, None, -1.929e-05, None, -0.00069395, None, -1.37331e-06, None, -0.00069395, None, -1.37331e-06, None, 1.03265, None, 0.00753588, None, 1.03265, None, 0.00753588, None)

reports.append(Report(604058880, ("CSC", 2, 3, 2, 32), "MEm32_32"))
reports[-1].posNum = 61572
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00560173, 0.00462927, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.271771, 0.20172, 0), \
                           ValErr(-0.00234637, 0.00229031, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.33339e-06, 5.0966e-05, 0), \
                           -91258.4, 61572, 61572, -nan)
reports[-1].sigmaresid = ValErr(1.06524, 0.00303559, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00531141, None, 1.83703e-05, None, 0.00554782, None, 2.88697e-05, None, 0.00554782, None, 2.88697e-05, None, 0.0056779, None, 3.1487e-05, None, 0.0056779, None, 3.1487e-05, None, 1.06527, None, 0.00748472, None, 1.06527, None, 0.00748472, None)

reports.append(Report(604058896, ("CSC", 2, 3, 2, 34), "MEm32_34"))
reports[-1].posNum = 58363
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00845686, 0.00482897, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0687654, 0.209727, 0), \
                           ValErr(0.0038672, 0.00240279, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.81438e-05, 5.30766e-05, 0), \
                           -85914.6, 58363, 58363, -nan)
reports[-1].sigmaresid = ValErr(1.05457, 0.00308667, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(9.05859e-05, None, -1.27934e-05, None, -0.0069431, None, -4.5636e-05, None, -0.0069431, None, -4.5636e-05, None, -0.0142985, None, -7.23437e-05, None, -0.0142985, None, -7.23437e-05, None, 1.0546, None, 0.00754777, None, 1.0546, None, 0.00754777, None)

reports.append(Report(604058912, ("CSC", 2, 3, 2, 36), "MEm32_36"))
reports[-1].posNum = 60109
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00703889, 0.00469609, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.317224, 0.20431, 0), \
                           ValErr(0.0020614, 0.00232608, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.29618e-05, 5.15468e-05, 0), \
                           -88858, 60109, 60109, -nan)
reports[-1].sigmaresid = ValErr(1.06114, 0.00306048, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00479597, None, 2.59743e-05, None, 0.00885503, None, -1.03996e-05, None, 0.00885503, None, -1.03996e-05, None, 0.00851077, None, 5.8499e-05, None, 0.00851077, None, 5.8499e-05, None, 1.06118, None, 0.0072689, None, 1.06118, None, 0.0072689, None)

reports.append(Report(604062216, ("CSC", 2, 4, 1, 1), "MEm41_01"))
reports[-1].posNum = 136893
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000410478, 0.0015895, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00674909, 0.0683587, 0), \
                           ValErr(0.0032728, 0.00174676, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.82747e-05, 4.15686e-05, 0), \
                           -121353, 136893, 136893, -nan)
reports[-1].sigmaresid = ValErr(0.587159, 0.00112215, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000451725, None, -1.20201e-05, None, 0.000523579, None, -4.47149e-05, None, 0.000523579, None, -4.47149e-05, None, 0.00286399, None, -5.96908e-05, None, 0.00286399, None, -5.96908e-05, None, 0.587171, None, 0.00571844, None, 0.587171, None, 0.00571844, None)

reports.append(Report(604062232, ("CSC", 2, 4, 1, 3), "MEm41_03"))
reports[-1].posNum = 137850
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00279851, 0.0015789, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.066905, 0.0678823, 0), \
                           ValErr(-0.00037632, 0.00173362, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.08168e-05, 4.13001e-05, 0), \
                           -121762, 137850, 137850, -nan)
reports[-1].sigmaresid = ValErr(0.585293, 0.00111469, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0037482, None, -7.6535e-06, None, 0.00288054, None, -2.02663e-05, None, 0.00288054, None, -2.02663e-05, None, -0.00164603, None, -6.39343e-05, None, -0.00164603, None, -6.39343e-05, None, 0.585297, None, 0.00573816, None, 0.585297, None, 0.00573816, None)

reports.append(Report(604062248, ("CSC", 2, 4, 1, 5), "MEm41_05"))
reports[-1].posNum = 137278
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000125983, 0.00158334, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.148779, 0.0682124, 0), \
                           ValErr(-0.00158368, 0.00174936, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.15002e-06, 4.15837e-05, 0), \
                           -121324, 137278, 137278, -nan)
reports[-1].sigmaresid = ValErr(0.585579, 0.00111756, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.002227, None, 3.34847e-06, None, 0.000107925, None, -4.31364e-05, None, 0.000107925, None, -4.31364e-05, None, -0.00523783, None, -4.9972e-05, None, -0.00523783, None, -4.9972e-05, None, 0.585588, None, 0.00589405, None, 0.585588, None, 0.00589405, None)

reports.append(Report(604062264, ("CSC", 2, 4, 1, 7), "MEm41_07"))
reports[-1].posNum = 136085
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00246249, 0.00158161, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00755654, 0.0679527, 0), \
                           ValErr(0.000108266, 0.00173418, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.7063e-05, 4.14042e-05, 0), \
                           -119502, 136085, 136085, -nan)
reports[-1].sigmaresid = ValErr(0.582284, 0.00111613, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00248868, None, -8.04178e-06, None, 0.00232452, None, -3.66056e-06, None, 0.00232452, None, -3.66056e-06, None, 0.000600869, None, 1.76609e-05, None, 0.000600869, None, 1.76609e-05, None, 0.582288, None, 0.00576967, None, 0.582288, None, 0.00576967, None)

reports.append(Report(604062280, ("CSC", 2, 4, 1, 9), "MEm41_09"))
reports[-1].posNum = 137082
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00121352, 0.00157822, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.035975, 0.0680336, 0), \
                           ValErr(-0.000339644, 0.00173548, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.49329e-05, 4.12718e-05, 0), \
                           -120624, 137082, 137082, -nan)
reports[-1].sigmaresid = ValErr(0.583334, 0.00111407, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00290297, None, 3.0963e-06, None, 0.00131671, None, -8.97363e-06, None, 0.00131671, None, -8.97363e-06, None, -0.00396931, None, -1.43277e-05, None, -0.00396931, None, -1.43277e-05, None, 0.583336, None, 0.00575805, None, 0.583336, None, 0.00575805, None)

reports.append(Report(604062296, ("CSC", 2, 4, 1, 11), "MEm41_11"))
reports[-1].posNum = 136809
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00438086, 0.00158107, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0455856, 0.0682101, 0), \
                           ValErr(-0.000925298, 0.00174228, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.77731e-05, 4.13834e-05, 0), \
                           -120528, 136809, 136809, -nan)
reports[-1].sigmaresid = ValErr(0.583949, 0.00111636, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00613587, None, -1.34485e-05, None, -0.0043211, None, -3.63157e-05, None, -0.0043211, None, -3.63157e-05, None, -0.0027872, None, -1.27534e-05, None, -0.0027872, None, -1.27534e-05, None, 0.583951, None, 0.00568541, None, 0.583951, None, 0.00568541, None)

reports.append(Report(604062312, ("CSC", 2, 4, 1, 13), "MEm41_13"))
reports[-1].posNum = 138412
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000908281, 0.0015688, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0436011, 0.0673904, 0), \
                           ValErr(-0.000532811, 0.0017258, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.661e-05, 4.10967e-05, 0), \
                           -121625, 138412, 138412, -nan)
reports[-1].sigmaresid = ValErr(0.582619, 0.00110734, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000343197, None, 5.92808e-06, None, -0.000871239, None, -2.55319e-05, None, -0.000871239, None, -2.55319e-05, None, 0.00132093, None, -8.48566e-06, None, 0.00132093, None, -8.48566e-06, None, 0.58262, None, 0.00603876, None, 0.58262, None, 0.00603876, None)

reports.append(Report(604062328, ("CSC", 2, 4, 1, 15), "MEm41_15"))
reports[-1].posNum = 138308
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000181539, 0.0015722, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0165949, 0.067585, 0), \
                           ValErr(-0.00132399, 0.00172991, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.702e-05, 4.12115e-05, 0), \
                           -121784, 138308, 138308, -nan)
reports[-1].sigmaresid = ValErr(0.583676, 0.00110977, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000926443, None, -1.69929e-07, None, 0.000306714, None, -2.07338e-05, None, 0.000306714, None, -2.07338e-05, None, -0.00286118, None, -5.03476e-05, None, -0.00286118, None, -5.03476e-05, None, 0.583682, None, 0.00558169, None, 0.583682, None, 0.00558169, None)

reports.append(Report(604062344, ("CSC", 2, 4, 1, 17), "MEm41_17"))
reports[-1].posNum = 137018
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00018309, 0.00157658, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0953729, 0.0679298, 0), \
                           ValErr(0.00240496, 0.00173761, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.87154e-05, 4.12376e-05, 0), \
                           -120344, 137018, 137018, -nan)
reports[-1].sigmaresid = ValErr(0.58238, 0.00111251, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000649576, None, -7.50746e-06, None, -0.000103732, None, -3.16628e-05, None, -0.000103732, None, -3.16628e-05, None, -0.00083858, None, -2.46587e-05, None, -0.00083858, None, -2.46587e-05, None, 0.582391, None, 0.00555864, None, 0.582391, None, 0.00555864, None)

reports.append(Report(604062224, ("CSC", 2, 4, 1, 2), "MEm41_02"))
reports[-1].posNum = 138322
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00393035, 0.00161261, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.121073, 0.0709724, 0), \
                           ValErr(-0.000134877, 0.00182501, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.68742e-05, 4.23564e-05, 0), \
                           -125271, 138322, 138322, -nan)
reports[-1].sigmaresid = ValErr(0.598522, 0.00113794, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00278069, None, -1.91953e-05, None, -0.00379485, None, -1.78988e-05, None, -0.00379485, None, -1.78988e-05, None, -0.00811543, None, -4.95956e-06, None, -0.00811543, None, -4.95956e-06, None, 0.598534, None, 0.00558296, None, 0.598534, None, 0.00558296, None)

reports.append(Report(604062240, ("CSC", 2, 4, 1, 4), "MEm41_04"))
reports[-1].posNum = 137666
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00040447, 0.00161151, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.102503, 0.0708769, 0), \
                           ValErr(-0.000425602, 0.00181559, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.7598e-05, 4.22352e-05, 0), \
                           -124250, 137666, 137666, -nan)
reports[-1].sigmaresid = ValErr(0.596667, 0.00113711, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000858791, None, -1.86358e-05, None, 0.000292771, None, -2.15475e-05, None, 0.000292771, None, -2.15475e-05, None, -0.00425579, None, -4.58055e-05, None, -0.00425579, None, -4.58055e-05, None, 0.596674, None, 0.00562057, None, 0.596674, None, 0.00562057, None)

reports.append(Report(604062256, ("CSC", 2, 4, 1, 6), "MEm41_06"))
reports[-1].posNum = 137998
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0012131, 0.00162199, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0672334, 0.0713591, 0), \
                           ValErr(-0.00198804, 0.00182555, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.67861e-05, 4.2493e-05, 0), \
                           -125628, 137998, 137998, -nan)
reports[-1].sigmaresid = ValErr(0.60135, 0.00114466, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00166139, None, -1.64578e-05, None, 0.0011378, None, -2.40878e-05, None, 0.0011378, None, -2.40878e-05, None, 0.00290059, None, -1.47515e-05, None, 0.00290059, None, -1.47515e-05, None, 0.601358, None, 0.00559413, None, 0.601358, None, 0.00559413, None)

reports.append(Report(604062272, ("CSC", 2, 4, 1, 8), "MEm41_08"))
reports[-1].posNum = 138975
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(9.10342e-05, 0.00161668, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0617212, 0.0712892, 0), \
                           ValErr(-0.00122001, 0.00182682, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.02478e-05, 4.23626e-05, 0), \
                           -126542, 138975, 138975, -nan)
reports[-1].sigmaresid = ValErr(0.601454, 0.00114082, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00198996, None, -7.87555e-06, None, 0.00024132, None, -1.32191e-05, None, 0.00024132, None, -1.32191e-05, None, -0.00110774, None, -2.19587e-05, None, -0.00110774, None, -2.19587e-05, None, 0.601463, None, 0.00561356, None, 0.601463, None, 0.00561356, None)

reports.append(Report(604062288, ("CSC", 2, 4, 1, 10), "MEm41_10"))
reports[-1].posNum = 138350
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00263695, 0.0016319, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0356573, 0.0717669, 0), \
                           ValErr(-0.000481112, 0.00183801, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(6.90401e-06, 4.27458e-05, 0), \
                           -127002, 138350, 138350, -nan)
reports[-1].sigmaresid = ValErr(0.605947, 0.00115194, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00294454, None, 2.15597e-05, None, 0.00264778, None, -5.93006e-07, None, 0.00264778, None, -5.93006e-07, None, 0.00169861, None, -5.35905e-06, None, 0.00169861, None, -5.35905e-06, None, 0.605949, None, 0.0056931, None, 0.605949, None, 0.0056931, None)

reports.append(Report(604062304, ("CSC", 2, 4, 1, 12), "MEm41_12"))
reports[-1].posNum = 138509
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00169251, 0.00162258, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0362139, 0.0713907, 0), \
                           ValErr(-1.12109e-05, 0.00182975, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.07576e-05, 4.25263e-05, 0), \
                           -126441, 138509, 138509, -nan)
reports[-1].sigmaresid = ValErr(0.602863, 0.00114542, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00212463, None, 1.40613e-05, None, 0.00173771, None, -1.02581e-05, None, 0.00173771, None, -1.02581e-05, None, 0.00313777, None, -6.24059e-06, None, 0.00313777, None, -6.24059e-06, None, 0.602864, None, 0.00568131, None, 0.602864, None, 0.00568131, None)

reports.append(Report(604062320, ("CSC", 2, 4, 1, 14), "MEm41_14"))
reports[-1].posNum = 138438
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00167038, 0.00162124, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0895894, 0.0712872, 0), \
                           ValErr(-0.00136645, 0.00182749, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.76757e-05, 4.2591e-05, 0), \
                           -126212, 138438, 138438, -nan)
reports[-1].sigmaresid = ValErr(0.602147, 0.00114435, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00193881, None, -2.49894e-06, None, 0.00173317, None, -2.2834e-05, None, 0.00173317, None, -2.2834e-05, None, 1.358e-05, None, -3.61639e-05, None, 1.358e-05, None, -3.61639e-05, None, 0.602152, None, 0.00555445, None, 0.602152, None, 0.00555445, None)

reports.append(Report(604062336, ("CSC", 2, 4, 1, 16), "MEm41_16"))
reports[-1].posNum = 137997
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00190593, 0.00161864, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0574932, 0.0713433, 0), \
                           ValErr(-0.000313172, 0.00182494, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.84732e-05, 4.24655e-05, 0), \
                           -125352, 137997, 137997, -nan)
reports[-1].sigmaresid = ValErr(0.600152, 0.00114238, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00273588, None, 8.22705e-06, None, -0.00181521, None, 2.08485e-05, None, -0.00181521, None, 2.08485e-05, None, -0.00283478, None, 2.10244e-05, None, -0.00283478, None, 2.10244e-05, None, 0.600156, None, 0.00560482, None, 0.600156, None, 0.00560482, None)

reports.append(Report(604062352, ("CSC", 2, 4, 1, 18), "MEm41_18"))
reports[-1].posNum = 139340
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0037152, 0.00161142, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0472482, 0.0709781, 0), \
                           ValErr(-0.000206226, 0.00181383, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.29584e-05, 4.22045e-05, 0), \
                           -126636, 139340, 139340, -nan)
reports[-1].sigmaresid = ValErr(0.600427, 0.00113738, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00238515, None, -1.27008e-05, None, -0.00368547, None, -2.05483e-05, None, -0.00368547, None, -2.05483e-05, None, -0.00232139, None, -7.53882e-07, None, -0.00232139, None, -7.53882e-07, None, 0.60043, None, 0.00551363, None, 0.60043, None, 0.00551363, None)

reports.append(Report(604062728, ("CSC", 2, 4, 2, 1), "MEm42_01"))
reports[-1].posNum = 63263
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00155157, 0.00476476, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.337436, 0.144919, 0), \
                           ValErr(-0.00220526, 0.0023939, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.86539e-05, 5.31653e-05, 0), \
                           -96645.2, 63263, 63263, -nan)
reports[-1].sigmaresid = ValErr(1.11487, 0.00306292, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000402528, None, -2.98156e-05, None, 0.000596185, None, -5.11106e-05, None, 0.000596185, None, -5.11106e-05, None, 0.00801141, None, -5.19031e-05, None, 0.00801141, None, -5.19031e-05, None, 1.1149, None, 0.00762348, None, 1.1149, None, 0.00762348, None)

reports.append(Report(604062744, ("CSC", 2, 4, 2, 3), "MEm42_03"))
reports[-1].posNum = 59598
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00246353, 0.00486512, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.351293, 0.223362, 0), \
                           ValErr(-0.00341959, 0.00258543, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.13538e-05, 5.4e-05, 0), \
                           -88996.3, 59598, 59598, -nan)
reports[-1].sigmaresid = ValErr(1.07717, 0.00312, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00134683, None, -8.28942e-05, None, -0.000534922, None, -7.85919e-05, None, -0.000534922, None, -7.85919e-05, None, 0.00261386, None, -6.48229e-05, None, 0.00261386, None, -6.48229e-05, None, 1.07722, None, 0.00756595, None, 1.07722, None, 0.00756595, None)

reports.append(Report(604062760, ("CSC", 2, 4, 2, 5), "MEm42_05"))
reports[-1].posNum = 62458
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00192793, 0.00473689, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.41434, 0.221142, 0), \
                           ValErr(0.00140136, 0.0025733, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(8.03072e-05, 5.31237e-05, 0), \
                           -94567.3, 62458, 62458, -nan)
reports[-1].sigmaresid = ValErr(1.09983, 0.00311185, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0124671, None, 3.202e-06, None, 0.00454797, None, -4.42384e-05, None, 0.00454797, None, -4.42384e-05, None, 0.00408535, None, -8.49606e-06, None, 0.00408535, None, -8.49606e-06, None, 1.09988, None, 0.00794399, None, 1.09988, None, 0.00794399, None)

reports.append(Report(604062776, ("CSC", 2, 4, 2, 7), "MEm42_07"))
reports[-1].posNum = 59190
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000430945, 0.00493347, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.471048, 0.226096, 0), \
                           ValErr(0.00249794, 0.00260864, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.74768e-05, 5.47467e-05, 0), \
                           -89325, 59190, 59190, -nan)
reports[-1].sigmaresid = ValErr(1.09438, 0.00318075, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000372795, None, 4.05055e-05, None, 0.00273845, None, 1.11118e-05, None, 0.00273845, None, 1.11118e-05, None, -0.00157371, None, -1.01771e-06, None, -0.00157371, None, -1.01771e-06, None, 1.09443, None, 0.00754529, None, 1.09443, None, 0.00754529, None)

reports.append(Report(604062792, ("CSC", 2, 4, 2, 9), "MEm42_09"))
reports[-1].posNum = 61316
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000854683, 0.00484119, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.173927, 0.226062, 0), \
                           ValErr(-0.0042057, 0.00261332, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.61584e-06, 5.3837e-05, 0), \
                           -93121.2, 61316, 61316, -nan)
reports[-1].sigmaresid = ValErr(1.10492, 0.0031552, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00149068, None, -4.47084e-05, None, 0.000673437, None, -3.38305e-05, None, 0.000673437, None, -3.38305e-05, None, -0.00575917, None, -6.76358e-05, None, -0.00575917, None, -6.76358e-05, None, 1.10495, None, 0.00783021, None, 1.10495, None, 0.00783021, None)

reports.append(Report(604062808, ("CSC", 2, 4, 2, 11), "MEm42_11"))
reports[-1].posNum = 60538
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00403759, 0.00484523, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.359558, 0.114417, 0), \
                           ValErr(-0.00175836, 0.00259084, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000101522, 5.40337e-05, 0), \
                           -91542.4, 60538, 60538, -nan)
reports[-1].sigmaresid = ValErr(1.09769, 0.00311044, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00198621, None, -2.28548e-05, None, -0.00042304, None, -3.91215e-05, None, -0.00042304, None, -3.91215e-05, None, 5.51249e-05, None, -2.6482e-05, None, 5.51249e-05, None, -2.6482e-05, None, 1.09775, None, 0.00723879, None, 1.09775, None, 0.00723879, None)

reports.append(Report(604062824, ("CSC", 2, 4, 2, 13), "MEm42_13"))
reports[-1].posNum = 58885
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00579052, 0.00498318, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.510284, 0.128424, 0), \
                           ValErr(-0.00362958, 0.00251656, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(9.09433e-05, 5.51809e-05, 0), \
                           -88567.1, 58885, 58885, -nan)
reports[-1].sigmaresid = ValErr(1.08885, 0.00305947, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00596976, None, -7.8303e-05, None, -0.00236515, None, -0.000147311, None, -0.00236515, None, -0.000147311, None, -0.00998916, None, -0.000119854, None, -0.00998916, None, -0.000119854, None, 1.08896, None, 0.00732273, None, 1.08896, None, 0.00732273, None)

reports.append(Report(604062840, ("CSC", 2, 4, 2, 15), "MEm42_15"))
reports[-1].posNum = 62719
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00553275, 0.00470279, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.825126, 0.219642, 0), \
                           ValErr(0.00502245, 0.00255165, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.96648e-05, 5.25725e-05, 0), \
                           -94580.3, 62719, 62719, -nan)
reports[-1].sigmaresid = ValErr(1.09315, 0.0030865, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00993509, None, -1.4437e-05, None, 0.00666166, None, -2.84496e-05, None, 0.00666166, None, -2.84496e-05, None, 0.00872378, None, -2.71706e-05, None, 0.00872378, None, -2.71706e-05, None, 1.0933, None, 0.00721883, None, 1.0933, None, 0.00721883, None)

reports.append(Report(604062856, ("CSC", 2, 4, 2, 17), "MEm42_17"))
reports[-1].posNum = 59469
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00767615, 0.00490071, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.73528, 0.225709, 0), \
                           ValErr(0.00384408, 0.0026198, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000158373, 5.46448e-05, 0), \
                           -88930.3, 59469, 59469, -nan)
reports[-1].sigmaresid = ValErr(1.07946, 0.00313001, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00173478, None, -3.99626e-05, None, 0.00164081, None, -5.07303e-05, None, 0.00164081, None, -5.07303e-05, None, -0.00157419, None, -5.59877e-05, None, -0.00157419, None, -5.59877e-05, None, 1.07965, None, 0.00759792, None, 1.07965, None, 0.00759792, None)

reports.append(Report(604062872, ("CSC", 2, 4, 2, 19), "MEm42_19"))
reports[-1].posNum = 63235
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00211903, 0.00471658, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.387077, 0.219665, 0), \
                           ValErr(-0.00235475, 0.00254973, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.22062e-05, 5.27519e-05, 0), \
                           -96014, 63235, 63235, -nan)
reports[-1].sigmaresid = ValErr(1.10454, 0.00310591, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00416297, None, 1.06679e-05, None, -0.00169038, None, -1.06673e-05, None, -0.00169038, None, -1.06673e-05, None, -0.0107807, None, -3.57135e-05, None, -0.0107807, None, -3.57135e-05, None, 1.10458, None, 0.00771506, None, 1.10458, None, 0.00771506, None)

reports.append(Report(604062888, ("CSC", 2, 4, 2, 21), "MEm42_21"))
reports[-1].posNum = 58883
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0132103, 0.00493758, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.24815, 0.227626, 0), \
                           ValErr(-0.00323228, 0.00263021, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000100954, 5.47186e-05, 0), \
                           -87742.9, 58883, 58883, -nan)
reports[-1].sigmaresid = ValErr(1.07378, 0.00312899, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00125057, None, 6.0753e-05, None, 0.0091382, None, 4.79933e-05, None, 0.0091382, None, 4.79933e-05, None, 0.0084023, None, 7.11104e-05, None, 0.0084023, None, 7.11104e-05, None, 1.07384, None, 0.00741546, None, 1.07384, None, 0.00741546, None)

reports.append(Report(604062904, ("CSC", 2, 4, 2, 23), "MEm42_23"))
reports[-1].posNum = 63338
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00694297, 0.00472651, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.277352, 0.220751, 0), \
                           ValErr(0.000161829, 0.00256262, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.87345e-05, 5.28904e-05, 0), \
                           -96165.7, 63338, 63338, -nan)
reports[-1].sigmaresid = ValErr(1.10446, 0.00310316, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00758754, None, -8.64314e-05, None, -0.00750286, None, -0.000104438, None, -0.00750286, None, -0.000104438, None, -0.00711631, None, -6.69186e-05, None, -0.00711631, None, -6.69186e-05, None, 1.10447, None, 0.00722824, None, 1.10447, None, 0.00722824, None)

reports.append(Report(604062920, ("CSC", 2, 4, 2, 25), "MEm42_25"))
reports[-1].posNum = 60974
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000840005, 0.00483278, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.605687, 0.222222, 0), \
                           ValErr(-0.00139787, 0.00258007, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.1567e-05, 5.3661e-05, 0), \
                           -91649.8, 60974, 60974, -nan)
reports[-1].sigmaresid = ValErr(1.0878, 0.00311501, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0067743, None, 1.62255e-05, None, -0.000715766, None, -1.7177e-05, None, -0.000715766, None, -1.7177e-05, None, -0.000830433, None, 2.35432e-05, None, -0.000830433, None, 2.35432e-05, None, 1.08788, None, 0.00722172, None, 1.08788, None, 0.00722172, None)

reports.append(Report(604062936, ("CSC", 2, 4, 2, 27), "MEm42_27"))
reports[-1].posNum = 61810
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00760164, 0.00477882, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.561564, 0.22293, 0), \
                           ValErr(-0.00500777, 0.00256211, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.7339e-05, 5.29465e-05, 0), \
                           -93392.5, 61810, 61810, -nan)
reports[-1].sigmaresid = ValErr(1.09639, 0.00311832, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0079807, None, -4.48834e-05, None, 0.00582926, None, -5.58101e-05, None, 0.00582926, None, -5.58101e-05, None, 0.000636439, None, -8.12184e-05, None, 0.000636439, None, -8.12184e-05, None, 1.09649, None, 0.00695307, None, 1.09649, None, 0.00695307, None)

reports.append(Report(604062952, ("CSC", 2, 4, 2, 29), "MEm42_29"))
reports[-1].posNum = 61899
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00194434, 0.00474161, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.275926, 0.107405, 0), \
                           ValErr(-0.00154316, 0.00126274, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000125075, 5.30097e-05, 0), \
                           -93443.3, 61899, 61899, -nan)
reports[-1].sigmaresid = ValErr(1.09491, 0.00305943, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00423446, None, 3.39225e-05, None, 0.00249355, None, -1.81998e-05, None, 0.00249355, None, -1.81998e-05, None, -0.00119824, None, 1.23615e-05, None, -0.00119824, None, 1.23615e-05, None, 1.09497, None, 0.00720845, None, 1.09497, None, 0.00720845, None)

reports.append(Report(604062968, ("CSC", 2, 4, 2, 31), "MEm42_31"))
reports[-1].posNum = 61060
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00232995, 0.00489293, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.247332, 0.224124, 0), \
                           ValErr(-0.00283767, 0.0026003, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-8.36084e-07, 5.45658e-05, 0), \
                           -92531.9, 61060, 61060, -nan)
reports[-1].sigmaresid = ValErr(1.1013, 0.00315148, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00235255, None, -2.27813e-06, None, -0.00234947, None, -3.28907e-05, None, -0.00234947, None, -3.28907e-05, None, -0.00407266, None, -1.87991e-05, None, -0.00407266, None, -1.87991e-05, None, 1.10132, None, 0.00712241, None, 1.10132, None, 0.00712241, None)

reports.append(Report(604062984, ("CSC", 2, 4, 2, 33), "MEm42_33"))
reports[-1].posNum = 62994
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00567788, 0.00470781, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.177784, 0.161577, 0), \
                           ValErr(-0.000646422, 0.00216032, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.98337e-06, 5.2444e-05, 0), \
                           -95137.9, 62994, 62994, -nan)
reports[-1].sigmaresid = ValErr(1.09563, 0.00306019, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00619492, None, -9.20771e-06, None, 0.00564967, None, -4.82602e-05, None, 0.00564967, None, -4.82602e-05, None, 0.0102485, None, -3.25429e-05, None, 0.0102485, None, -3.25429e-05, None, 1.09564, None, 0.0078675, None, 1.09564, None, 0.0078675, None)

reports.append(Report(604063000, ("CSC", 2, 4, 2, 35), "MEm42_35"))
reports[-1].posNum = 58612
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0137918, 0.00496503, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.112576, 0.22604, 0), \
                           ValErr(-0.00257747, 0.00261132, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-7.76592e-05, 5.49376e-05, 0), \
                           -87353.4, 58612, 58612, -nan)
reports[-1].sigmaresid = ValErr(1.07404, 0.00313699, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0179574, None, -4.068e-05, None, 0.0106295, None, -3.629e-05, None, 0.0106295, None, -3.629e-05, None, 0.0102809, None, -2.66461e-05, None, 0.0102809, None, -2.66461e-05, None, 1.07407, None, 0.00714776, None, 1.07407, None, 0.00714776, None)

reports.append(Report(604062736, ("CSC", 2, 4, 2, 2), "MEm42_02"))
reports[-1].posNum = 61509
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00538803, 0.0049463, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.390904, 0.235979, 0), \
                           ValErr(-0.00011055, 0.00277107, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.16734e-06, 5.56023e-05, 0), \
                           -94360.1, 61509, 61509, -nan)
reports[-1].sigmaresid = ValErr(1.12204, 0.00319907, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00475761, None, 8.98657e-06, None, -0.00528585, None, 1.43977e-05, None, -0.00528585, None, 1.43977e-05, None, -0.00299307, None, 5.18285e-05, None, -0.00299307, None, 5.18285e-05, None, 1.12206, None, 0.00718316, None, 1.12206, None, 0.00718316, None)

reports.append(Report(604062752, ("CSC", 2, 4, 2, 4), "MEm42_04"))
reports[-1].posNum = 60765
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00454768, 0.00495191, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.18342, 0.233681, 0), \
                           ValErr(-0.000188833, 0.00274195, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.35195e-05, 5.56158e-05, 0), \
                           -92626.1, 60765, 60765, -nan)
reports[-1].sigmaresid = ValErr(1.11115, 0.00318734, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0043875, None, -1.75438e-05, None, -0.00691398, None, -3.16115e-05, None, -0.00691398, None, -3.16115e-05, None, -0.00384891, None, 5.4516e-06, None, -0.00384891, None, 5.4516e-06, None, 1.11117, None, 0.00704875, None, 1.11117, None, 0.00704875, None)

reports.append(Report(604062768, ("CSC", 2, 4, 2, 6), "MEm42_06"))
reports[-1].posNum = 63253
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00257949, 0.0048051, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.284703, 0.230731, 0), \
                           ValErr(-0.00504661, 0.00269375, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-6.79094e-06, 5.41113e-05, 0), \
                           -97327.4, 63253, 63253, -nan)
reports[-1].sigmaresid = ValErr(1.12723, 0.00316925, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00997217, None, 4.98586e-05, None, -0.00283158, None, 4.72207e-05, None, -0.00283158, None, 4.72207e-05, None, -0.000804385, None, 5.95512e-05, None, -0.000804385, None, 5.95512e-05, None, 1.12727, None, 0.00726095, None, 1.12727, None, 0.00726095, None)

reports.append(Report(604062784, ("CSC", 2, 4, 2, 8), "MEm42_08"))
reports[-1].posNum = 59378
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00608428, 0.0049904, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.182606, 0.118972, 0), \
                           ValErr(-0.000537413, 0.00263177, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.2095e-05, 5.59276e-05, 0), \
                           -89747.2, 59378, 59378, -nan)
reports[-1].sigmaresid = ValErr(1.09693, 0.00317206, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00704329, None, -2.19364e-06, None, 0.00517582, None, -3.34948e-05, None, 0.00517582, None, -3.34948e-05, None, 0.00566125, None, -2.27187e-05, None, 0.00566125, None, -2.27187e-05, None, 1.09694, None, 0.00708933, None, 1.09694, None, 0.00708933, None)

reports.append(Report(604062800, ("CSC", 2, 4, 2, 10), "MEm42_10"))
reports[-1].posNum = 64245
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00490815, 0.00473881, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.286259, 0.205939, 0), \
                           ValErr(-0.000383484, 0.0016758, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(8.92752e-05, 5.33579e-05, 0), \
                           -98981.5, 64245, 64245, -nan)
reports[-1].sigmaresid = ValErr(1.12947, 0.00313446, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00185959, None, -7.62657e-05, None, -0.00223263, None, -0.000105446, None, -0.00223263, None, -0.000105446, None, -0.0013096, None, -6.49035e-05, None, -0.0013096, None, -6.49035e-05, None, 1.12951, None, 0.00743045, None, 1.12951, None, 0.00743045, None)

reports.append(Report(604062816, ("CSC", 2, 4, 2, 12), "MEm42_12"))
reports[-1].posNum = 60408
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000144255, 0.00492953, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.382953, 0.130502, 0), \
                           ValErr(-0.00359617, 0.00251312, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000149888, 5.53653e-05, 0), \
                           -91432.7, 60408, 60408, -nan)
reports[-1].sigmaresid = ValErr(1.09927, 0.0031264, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00584868, None, -4.36384e-05, None, -0.00572744, None, -4.95176e-05, None, -0.00572744, None, -4.95176e-05, None, -0.00212582, None, -1.91137e-05, None, -0.00212582, None, -1.91137e-05, None, 1.09938, None, 0.00707348, None, 1.09938, None, 0.00707348, None)

reports.append(Report(604062832, ("CSC", 2, 4, 2, 14), "MEm42_14"))
reports[-1].posNum = 63380
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00127399, 0.00472659, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.3588, 0.168773, 0), \
                           ValErr(-0.00130928, 0.00226577, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(4.93098e-05, 5.25729e-05, 0), \
                           -96706.4, 63380, 63380, -nan)
reports[-1].sigmaresid = ValErr(1.11281, 0.00299626, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0059299, None, -7.08742e-06, None, 0.00292413, None, 4.90885e-06, None, 0.00292413, None, 4.90885e-06, None, 0.00219775, None, 2.08306e-05, None, 0.00219775, None, 2.08306e-05, None, 1.11283, None, 0.00749127, None, 1.11283, None, 0.00749127, None)

reports.append(Report(604062848, ("CSC", 2, 4, 2, 16), "MEm42_16"))
reports[-1].posNum = 60698
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00119472, 0.00495619, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.732603, 0.235507, 0), \
                           ValErr(0.00276438, 0.00274639, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-2.04675e-05, 5.5503e-05, 0), \
                           -92561.6, 60698, 60698, -nan)
reports[-1].sigmaresid = ValErr(1.11184, 0.0031911, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00411856, None, -3.68097e-05, None, -0.0018366, None, -1.38969e-05, None, -0.0018366, None, -1.38969e-05, None, -0.000694789, None, -5.08988e-06, None, -0.000694789, None, -5.08988e-06, None, 1.11193, None, 0.00697786, None, 1.11193, None, 0.00697786, None)

reports.append(Report(604062864, ("CSC", 2, 4, 2, 18), "MEm42_18"))
reports[-1].posNum = 61418
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00584873, 0.00490524, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0483386, 0.233124, 0), \
                           ValErr(-0.00437653, 0.00273064, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-5.0715e-05, 5.50832e-05, 0), \
                           -93821.6, 61418, 61418, -nan)
reports[-1].sigmaresid = ValErr(1.11477, 0.00318071, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00826587, None, -7.46094e-08, None, -0.00760023, None, 3.19167e-05, None, -0.00760023, None, 3.19167e-05, None, -0.00318593, None, 2.28914e-05, None, -0.00318593, None, 2.28914e-05, None, 1.11481, None, 0.00771054, None, 1.11481, None, 0.00771054, None)

reports.append(Report(604062880, ("CSC", 2, 4, 2, 20), "MEm42_20"))
reports[-1].posNum = 63171
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0121373, 0.00482567, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.494863, 0.172365, 0), \
                           ValErr(0.000964721, 0.00228219, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.14614e-05, 5.42443e-05, 0), \
                           -96791.5, 63171, 63171, -nan)
reports[-1].sigmaresid = ValErr(1.11994, 0.00310504, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00743103, None, -9.00856e-06, None, -0.0113588, None, -2.14727e-05, None, -0.0113588, None, -2.14727e-05, None, -0.0138724, None, 6.16365e-06, None, -0.0138724, None, 6.16365e-06, None, 1.11998, None, 0.00737303, None, 1.11998, None, 0.00737303, None)

reports.append(Report(604062896, ("CSC", 2, 4, 2, 22), "MEm42_22"))
reports[-1].posNum = 59995
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0118001, 0.00496308, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.504132, 0.236467, 0), \
                           ValErr(0.00214347, 0.00278964, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-9.07065e-05, 5.5711e-05, 0), \
                           -91321.2, 59995, 59995, -nan)
reports[-1].sigmaresid = ValErr(1.10872, 0.00320074, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0126513, None, 4.58473e-05, None, 0.00823735, None, 2.72577e-05, None, 0.00823735, None, 2.72577e-05, None, 0.0182618, None, 3.90919e-05, None, 0.0182618, None, 3.90919e-05, None, 1.10879, None, 0.00694102, None, 1.10879, None, 0.00694102, None)

reports.append(Report(604062912, ("CSC", 2, 4, 2, 24), "MEm42_24"))
reports[-1].posNum = 63639
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.004779, 0.0047562, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.255765, 0.107734, 0), \
                           ValErr(-0.00311911, 0.00129667, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-1.55346e-05, 5.3767e-05, 0), \
                           -97441.7, 63639, 63639, -nan)
reports[-1].sigmaresid = ValErr(1.11877, 0.00306621, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0100023, None, 1.79267e-05, None, -0.00526157, None, -9.32596e-06, None, -0.00526157, None, -9.32596e-06, None, -0.00393006, None, 5.29741e-05, None, -0.00393006, None, 5.29741e-05, None, 1.11879, None, 0.00714635, None, 1.11879, None, 0.00714635, None)

reports.append(Report(604062928, ("CSC", 2, 4, 2, 26), "MEm42_26"))
reports[-1].posNum = 60456
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000990154, 0.00494267, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.361173, 0.23181, 0), \
                           ValErr(0.0018713, 0.00272271, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.4951e-05, 5.55768e-05, 0), \
                           -91129.4, 60456, 60456, -nan)
reports[-1].sigmaresid = ValErr(1.09246, 0.00314174, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000481592, None, 3.18934e-05, None, 0.00203825, None, 3.72339e-06, None, 0.00203825, None, 3.72339e-06, None, -0.00224401, None, -9.39555e-06, None, -0.00224401, None, -9.39555e-06, None, 1.09248, None, 0.00699657, None, 1.09248, None, 0.00699657, None)

reports.append(Report(604062944, ("CSC", 2, 4, 2, 28), "MEm42_28"))
reports[-1].posNum = 64546
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00622471, 0.00477584, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.584905, 0.227637, 0), \
                           ValErr(-0.00360433, 0.00265618, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.53223e-05, 5.37558e-05, 0), \
                           -99717.8, 64546, 64546, -nan)
reports[-1].sigmaresid = ValErr(1.13425, 0.00315686, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00726312, None, -2.51831e-05, None, 0.00704985, None, 1.10834e-06, None, 0.00704985, None, 1.10834e-06, None, 0.00765721, None, -1.39331e-05, None, 0.00765721, None, -1.39331e-05, None, 1.13433, None, 0.00768534, None, 1.13433, None, 0.00768534, None)

reports.append(Report(604062960, ("CSC", 2, 4, 2, 30), "MEm42_30"))
reports[-1].posNum = 59790
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0024936, 0.00497241, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.180185, 0.234717, 0), \
                           ValErr(-0.00702969, 0.00275325, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-3.59509e-05, 5.57609e-05, 0), \
                           -90245.1, 59790, 59790, -nan)
reports[-1].sigmaresid = ValErr(1.09464, 0.00316551, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000750285, None, -3.52027e-06, None, -0.00397756, None, -4.9866e-07, None, -0.00397756, None, -4.9866e-07, None, -0.00949239, None, -2.01147e-05, None, -0.00949239, None, -2.01147e-05, None, 1.09472, None, 0.00735147, None, 1.09472, None, 0.00735147, None)

reports.append(Report(604062976, ("CSC", 2, 4, 2, 32), "MEm42_32"))
reports[-1].posNum = 63898
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00219466, 0.00474471, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.131035, 0.104134, 0), \
                           ValErr(-0.00112603, 0.0012198, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.03822e-07, 5.32638e-05, 0), \
                           -98000.9, 63898, 63898, -nan)
reports[-1].sigmaresid = ValErr(1.12162, 0.00312596, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00212041, None, -5.58667e-05, None, 0.00218653, None, -4.47513e-05, None, 0.00218653, None, -4.47513e-05, None, 0.00338391, None, -5.35288e-05, None, 0.00338391, None, -5.35288e-05, None, 1.12162, None, 0.00766618, None, 1.12162, None, 0.00766618, None)

reports.append(Report(604062992, ("CSC", 2, 4, 2, 34), "MEm42_34"))
reports[-1].posNum = 61807
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00368417, 0.00490209, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.376974, 0.234526, 0), \
                           ValErr(0.00174736, 0.00274772, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(5.24878e-05, 5.50688e-05, 0), \
                           -94686.2, 61807, 61807, -nan)
reports[-1].sigmaresid = ValErr(1.11966, 0.00318459, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00560885, None, -1.95534e-05, None, -0.00185883, None, -1.98516e-05, None, -0.00185883, None, -1.98516e-05, None, -0.00169945, None, -3.85698e-06, None, -0.00169945, None, -3.85698e-06, None, 1.1197, None, 0.00715933, None, 1.1197, None, 0.00715933, None)

reports.append(Report(604063008, ("CSC", 2, 4, 2, 36), "MEm42_36"))
reports[-1].posNum = 63081
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0100094, 0.00478508, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.406036, 0.126641, 0), \
                           ValErr(-0.00350534, 0.0026221, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-4.05984e-06, 5.30062e-05, 0), \
                           -96467.8, 63081, 63081, -nan)
reports[-1].sigmaresid = ValErr(1.11665, 0.00304792, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0065783, None, 8.12286e-06, None, 0.0098699, None, 4.9442e-05, None, 0.0098699, None, 4.9442e-05, None, 0.0137001, None, 8.29331e-05, None, 0.0137001, None, 8.29331e-05, None, 1.11669, None, 0.00724399, None, 1.11669, None, 0.00724399, None)

