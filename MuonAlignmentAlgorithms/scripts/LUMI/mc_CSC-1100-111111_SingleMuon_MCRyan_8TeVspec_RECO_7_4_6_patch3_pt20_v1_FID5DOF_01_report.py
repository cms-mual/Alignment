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
reports[-1].posNum = 101473
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000219393, 0.00081911, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.101135, 0.0495197, 0), \
                           ValErr(0.000991005, 0.00126194, 0), \
                           ValErr(0.0106922, 0.00612715, 0), \
                           ValErr(2.13499e-05, 1.74372e-05, 0), \
                           22641.7, 101473, 101473, -nan)
reports[-1].sigmaresid = ValErr(0.19358, 0.000429705, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000750638, None, -1.50902e-06, None, -0.00104748, None, 8.48321e-06, None, -0.00104748, None, 8.48321e-06, None, -7.60451e-05, None, 7.06637e-06, None, -7.60451e-05, None, 7.06637e-06, None, 0.193592, None, 0.00418802, None, 0.193592, None, 0.00418802, None)

reports.append(Report(604017688, ("CSC", 1, 1, 1, 3), "MEp11_03"))
reports[-1].posNum = 100847
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00201542, 0.000815858, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0414295, 0.0489955, 0), \
                           ValErr(0.000716712, 0.0012535, 0), \
                           ValErr(-0.00317272, 0.00610514, 0), \
                           ValErr(2.25542e-05, 1.72948e-05, 0), \
                           23478.3, 100847, 100847, -nan)
reports[-1].sigmaresid = ValErr(0.191714, 0.000426881, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0015107, None, -4.78122e-07, None, -0.0016483, None, -7.6589e-06, None, -0.0016483, None, -7.6589e-06, None, -0.00148273, None, 7.59367e-06, None, -0.00148273, None, 7.59367e-06, None, 0.191717, None, 0.00431532, None, 0.191717, None, 0.00431532, None)

reports.append(Report(604017704, ("CSC", 1, 1, 1, 5), "MEp11_05"))
reports[-1].posNum = 101454
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00144645, 0.000817606, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0502428, 0.0494603, 0), \
                           ValErr(-0.00119093, 0.00125698, 0), \
                           ValErr(0.00138915, 0.00612451, 0), \
                           ValErr(1.56853e-05, 1.72853e-05, 0), \
                           22789.4, 101454, 101454, -nan)
reports[-1].sigmaresid = ValErr(0.19329, 0.000429101, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00139603, None, -3.03644e-06, None, -0.00150612, None, 5.45039e-06, None, -0.00150612, None, 5.45039e-06, None, -0.00132942, None, 4.96135e-06, None, -0.00132942, None, 4.96135e-06, None, 0.193292, None, 0.00415749, None, 0.193292, None, 0.00415749, None)

reports.append(Report(604017720, ("CSC", 1, 1, 1, 7), "MEp11_07"))
reports[-1].posNum = 101477
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00183764, 0.000818312, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0963453, 0.0492249, 0), \
                           ValErr(-0.0021603, 0.00125583, 0), \
                           ValErr(-0.00215517, 0.00610704, 0), \
                           ValErr(-3.69716e-05, 1.73775e-05, 0), \
                           22874.4, 101477, 101477, -nan)
reports[-1].sigmaresid = ValErr(0.193137, 0.000428714, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0013219, None, -6.15632e-06, None, -0.00178024, None, -1.31228e-06, None, -0.00178024, None, -1.31228e-06, None, -0.00216955, None, 2.55606e-05, None, -0.00216955, None, 2.55606e-05, None, 0.193148, None, 0.00417913, None, 0.193148, None, 0.00417913, None)

reports.append(Report(604017736, ("CSC", 1, 1, 1, 9), "MEp11_09"))
reports[-1].posNum = 101238
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00190882, 0.00081471, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0710842, 0.0490712, 0), \
                           ValErr(-0.00107362, 0.00125289, 0), \
                           ValErr(-0.00194484, 0.0061054, 0), \
                           ValErr(3.51865e-05, 1.72911e-05, 0), \
                           23281.5, 101238, 101238, -nan)
reports[-1].sigmaresid = ValErr(0.19226, 0.000427269, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000640139, None, 5.6391e-06, None, -0.0016079, None, 7.28437e-06, None, -0.0016079, None, 7.28437e-06, None, -0.000228574, None, -2.95149e-05, None, -0.000228574, None, -2.95149e-05, None, 0.192266, None, 0.00415239, None, 0.192266, None, 0.00415239, None)

reports.append(Report(604017752, ("CSC", 1, 1, 1, 11), "MEp11_11"))
reports[-1].posNum = 101432
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000368417, 0.000822012, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.162786, 0.0496057, 0), \
                           ValErr(-0.00154993, 0.00126257, 0), \
                           ValErr(0.0082905, 0.00612746, 0), \
                           ValErr(5.62998e-06, 1.74492e-05, 0), \
                           22220.9, 101432, 101432, -nan)
reports[-1].sigmaresid = ValErr(0.194367, 0.000431539, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00171791, None, -1.31597e-05, None, -0.00105265, None, -3.45026e-05, None, -0.00105265, None, -3.45026e-05, None, -0.00167488, None, -1.16724e-05, None, -0.00167488, None, -1.16724e-05, None, 0.194379, None, 0.00442109, None, 0.194379, None, 0.00442109, None)

reports.append(Report(604017768, ("CSC", 1, 1, 1, 13), "MEp11_13"))
reports[-1].posNum = 101481
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00291607, 0.000815146, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.072233, 0.0489659, 0), \
                           ValErr(-0.000149785, 0.00125173, 0), \
                           ValErr(0.000990833, 0.00609356, 0), \
                           ValErr(7.1984e-06, 1.72861e-05, 0), \
                           23380.7, 101481, 101481, -nan)
reports[-1].sigmaresid = ValErr(0.192178, 0.000426576, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00281117, None, -9.13318e-06, None, -0.00297236, None, -7.21799e-06, None, -0.00297236, None, -7.21799e-06, None, -0.00297302, None, -1.23923e-05, None, -0.00297302, None, -1.23923e-05, None, 0.192181, None, 0.00419137, None, 0.192181, None, 0.00419137, None)

reports.append(Report(604017784, ("CSC", 1, 1, 1, 15), "MEp11_15"))
reports[-1].posNum = 100433
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00218619, 0.00082006, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0644298, 0.0494147, 0), \
                           ValErr(-0.000626725, 0.00125931, 0), \
                           ValErr(-0.00803072, 0.00613083, 0), \
                           ValErr(2.59728e-05, 1.73758e-05, 0), \
                           22852.3, 100433, 100433, -nan)
reports[-1].sigmaresid = ValErr(0.192728, 0.000430023, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00110764, None, 8.21056e-07, None, -0.00139948, None, -1.08533e-05, None, -0.00139948, None, -1.08533e-05, None, -0.000288965, None, -9.37113e-06, None, -0.000288965, None, -9.37113e-06, None, 0.192732, None, 0.00448848, None, 0.192732, None, 0.00448848, None)

reports.append(Report(604017800, ("CSC", 1, 1, 1, 17), "MEp11_17"))
reports[-1].posNum = 101267
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0009627, 0.000812973, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0593736, 0.0490891, 0), \
                           ValErr(-0.000218262, 0.00125068, 0), \
                           ValErr(0.00552189, 0.00612595, 0), \
                           ValErr(-4.65148e-06, 1.72391e-05, 0), \
                           23657.2, 101267, 101267, -nan)
reports[-1].sigmaresid = ValErr(0.191561, 0.000425654, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00215679, None, 4.34365e-06, None, -0.0014474, None, -3.01333e-06, None, -0.0014474, None, -3.01333e-06, None, -0.00129541, None, -1.04058e-05, None, -0.00129541, None, -1.04058e-05, None, 0.191563, None, 0.00420546, None, 0.191563, None, 0.00420546, None)

reports.append(Report(604017816, ("CSC", 1, 1, 1, 19), "MEp11_19"))
reports[-1].posNum = 101464
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00192577, 0.000817183, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0505298, 0.0490643, 0), \
                           ValErr(-0.00175609, 0.00125072, 0), \
                           ValErr(-0.00633575, 0.00612362, 0), \
                           ValErr(-1.76758e-05, 1.73133e-05, 0), \
                           23223.9, 101464, 101464, -nan)
reports[-1].sigmaresid = ValErr(0.192467, 0.000427254, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00139486, None, 1.85382e-06, None, -0.00145572, None, -8.93119e-06, None, -0.00145572, None, -8.93119e-06, None, -0.000747133, None, -2.76467e-05, None, -0.000747133, None, -2.76467e-05, None, 0.192473, None, 0.0042075, None, 0.192473, None, 0.0042075, None)

reports.append(Report(604017832, ("CSC", 1, 1, 1, 21), "MEp11_21"))
reports[-1].posNum = 101189
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00137511, 0.000809382, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0366044, 0.0489749, 0), \
                           ValErr(-0.00112519, 0.001247, 0), \
                           ValErr(0.00588857, 0.00606672, 0), \
                           ValErr(6.86612e-06, 1.7193e-05, 0), \
                           23861, 101189, 101189, -nan)
reports[-1].sigmaresid = ValErr(0.191141, 0.000424885, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00146556, None, 8.13478e-06, None, -0.00184821, None, -1.56316e-05, None, -0.00184821, None, -1.56316e-05, None, -0.00348723, None, -2.34493e-05, None, -0.00348723, None, -2.34493e-05, None, 0.191143, None, 0.00425097, None, 0.191143, None, 0.00425097, None)

reports.append(Report(604017848, ("CSC", 1, 1, 1, 23), "MEp11_23"))
reports[-1].posNum = 101254
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00237674, 0.000820227, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0674304, 0.0494529, 0), \
                           ValErr(0.000959941, 0.00126157, 0), \
                           ValErr(0.00139101, 0.00616842, 0), \
                           ValErr(2.91532e-05, 1.73646e-05, 0), \
                           22604.4, 101254, 101254, -nan)
reports[-1].sigmaresid = ValErr(0.193557, 0.000430119, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00167942, None, 6.41598e-06, None, -0.00238147, None, 2.52873e-06, None, -0.00238147, None, 2.52873e-06, None, -0.00188391, None, -7.41874e-06, None, -0.00188391, None, -7.41874e-06, None, 0.193564, None, 0.00472597, None, 0.193564, None, 0.00472597, None)

reports.append(Report(604017864, ("CSC", 1, 1, 1, 25), "MEp11_25"))
reports[-1].posNum = 101182
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00225629, 0.000819165, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0509614, 0.049184, 0), \
                           ValErr(-0.000675535, 0.001253, 0), \
                           ValErr(0.00108255, 0.00611861, 0), \
                           ValErr(2.82086e-05, 1.73584e-05, 0), \
                           22933.6, 101182, 101182, -nan)
reports[-1].sigmaresid = ValErr(0.192898, 0.000428806, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00132021, None, 8.00835e-06, None, -0.00224931, None, 2.43471e-06, None, -0.00224931, None, 2.43471e-06, None, 0.000880608, None, -1.50553e-05, None, 0.000880608, None, -1.50553e-05, None, 0.192902, None, 0.00471814, None, 0.192902, None, 0.00471814, None)

reports.append(Report(604017880, ("CSC", 1, 1, 1, 27), "MEp11_27"))
reports[-1].posNum = 101538
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00196712, 0.000812645, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0744158, 0.0491101, 0), \
                           ValErr(-0.00305828, 0.00125139, 0), \
                           ValErr(-0.0052241, 0.00610539, 0), \
                           ValErr(-2.49663e-06, 1.72239e-05, 0), \
                           23307.2, 101538, 101538, -nan)
reports[-1].sigmaresid = ValErr(0.192342, 0.00042682, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00149264, None, 8.10008e-06, None, -0.00154869, None, -9.23058e-06, None, -0.00154869, None, -9.23058e-06, None, -0.001737, None, -1.89653e-05, None, -0.001737, None, -1.89653e-05, None, 0.192349, None, 0.00416715, None, 0.192349, None, 0.00416715, None)

reports.append(Report(604017896, ("CSC", 1, 1, 1, 29), "MEp11_29"))
reports[-1].posNum = 100725
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00401536, 0.000821628, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.152965, 0.0494833, 0), \
                           ValErr(-0.00193956, 0.00127256, 0), \
                           ValErr(-0.000902352, 0.00617621, 0), \
                           ValErr(9.68825e-06, 1.74046e-05, 0), \
                           22698.9, 100725, 100725, -nan)
reports[-1].sigmaresid = ValErr(0.193149, 0.000430337, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00443628, None, 1.50487e-05, None, -0.00389988, None, 1.63612e-05, None, -0.00389988, None, 1.63612e-05, None, -0.00280161, None, 1.55939e-05, None, -0.00280161, None, 1.55939e-05, None, 0.193159, None, 0.00418779, None, 0.193159, None, 0.00418779, None)

reports.append(Report(604017912, ("CSC", 1, 1, 1, 31), "MEp11_31"))
reports[-1].posNum = 101037
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00159162, 0.000816046, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0810032, 0.0494222, 0), \
                           ValErr(-0.00275479, 0.00126042, 0), \
                           ValErr(-0.0102742, 0.00612203, 0), \
                           ValErr(-1.35501e-05, 1.73169e-05, 0), \
                           22861.3, 101037, 101037, -nan)
reports[-1].sigmaresid = ValErr(0.192973, 0.00042928, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00116551, None, -4.11089e-06, None, -0.000771488, None, -5.51714e-06, None, -0.000771488, None, -5.51714e-06, None, -0.000579069, None, -1.55029e-05, None, -0.000579069, None, -1.55029e-05, None, 0.192983, None, 0.00411683, None, 0.192983, None, 0.00411683, None)

reports.append(Report(604017928, ("CSC", 1, 1, 1, 33), "MEp11_33"))
reports[-1].posNum = 101187
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00142131, 0.000823769, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0963502, 0.0494342, 0), \
                           ValErr(-0.00272424, 0.00126664, 0), \
                           ValErr(0.00309804, 0.00617359, 0), \
                           ValErr(-2.84331e-06, 1.74565e-05, 0), \
                           22350.5, 101187, 101187, -nan)
reports[-1].sigmaresid = ValErr(0.194015, 0.000431278, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00194115, None, -4.62772e-06, None, -0.00170781, None, -1.31994e-05, None, -0.00170781, None, -1.31994e-05, None, 0.00103098, None, -2.23113e-05, None, 0.00103098, None, -2.23113e-05, None, 0.194021, None, 0.00436928, None, 0.194021, None, 0.00436928, None)

reports.append(Report(604017944, ("CSC", 1, 1, 1, 35), "MEp11_35"))
reports[-1].posNum = 101272
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00136523, 0.000810555, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0707279, 0.0487848, 0), \
                           ValErr(0.00139351, 0.00124234, 0), \
                           ValErr(0.00420634, 0.00603494, 0), \
                           ValErr(-1.28575e-06, 1.72403e-05, 0), \
                           23888.2, 101272, 101272, -nan)
reports[-1].sigmaresid = ValErr(0.191126, 0.000424679, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00176524, None, -1.15569e-06, None, -0.00172635, None, -4.40746e-06, None, -0.00172635, None, -4.40746e-06, None, -0.00190518, None, -1.40494e-05, None, -0.00190518, None, -1.40494e-05, None, 0.191132, None, 0.00422688, None, 0.191132, None, 0.00422688, None)

reports.append(Report(604017680, ("CSC", 1, 1, 1, 2), "MEp11_02"))
reports[-1].posNum = 100251
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000643799, 0.000737362, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0784317, 0.0419354, 0), \
                           ValErr(0.000372984, 0.00107269, 0), \
                           ValErr(0.000429221, 0.00521242, 0), \
                           ValErr(-1.26878e-05, 1.56171e-05, 0), \
                           33687.2, 100251, 100251, -nan)
reports[-1].sigmaresid = ValErr(0.172913, 0.000386159, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000434499, None, 8.98289e-06, None, -0.000728694, None, 4.65778e-05, None, -0.000728694, None, 4.65778e-05, None, -0.000358011, None, 4.10868e-05, None, -0.000358011, None, 4.10868e-05, None, 0.172918, None, 0.00444122, None, 0.172918, None, 0.00444122, None)

reports.append(Report(604017696, ("CSC", 1, 1, 1, 4), "MEp11_04"))
reports[-1].posNum = 100406
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00190121, 0.000730696, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.114609, 0.0417795, 0), \
                           ValErr(-0.00119148, 0.00106848, 0), \
                           ValErr(-0.00924577, 0.00518774, 0), \
                           ValErr(2.1953e-05, 1.54792e-05, 0), \
                           34308.7, 100406, 100406, -nan)
reports[-1].sigmaresid = ValErr(0.171935, 0.00038368, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000647152, None, -6.17676e-06, None, -0.000986836, None, -1.544e-05, None, -0.000986836, None, -1.544e-05, None, 0.000348507, None, -3.09724e-05, None, 0.000348507, None, -3.09724e-05, None, 0.171945, None, 0.00530762, None, 0.171945, None, 0.00530762, None)

reports.append(Report(604017712, ("CSC", 1, 1, 1, 6), "MEp11_06"))
reports[-1].posNum = 100408
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00178087, 0.000735781, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0311483, 0.0419779, 0), \
                           ValErr(-0.00037317, 0.00107853, 0), \
                           ValErr(-0.00220048, 0.00521113, 0), \
                           ValErr(-5.50234e-06, 1.56572e-05, 0), \
                           33626, 100408, 100408, -nan)
reports[-1].sigmaresid = ValErr(0.173109, 0.000386297, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00173286, None, 7.1568e-06, None, -0.00160341, None, 2.87334e-05, None, -0.00160341, None, 2.87334e-05, None, -0.00166411, None, 3.33258e-05, None, -0.00166411, None, 3.33258e-05, None, 0.17311, None, 0.00439007, None, 0.17311, None, 0.00439007, None)

reports.append(Report(604017728, ("CSC", 1, 1, 1, 8), "MEp11_08"))
reports[-1].posNum = 99540
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0006633, 0.000736737, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0427329, 0.0419631, 0), \
                           ValErr(-0.00113948, 0.00107492, 0), \
                           ValErr(0.00206078, 0.00524648, 0), \
                           ValErr(-1.55872e-06, 1.55868e-05, 0), \
                           33909.1, 99540, 99540, -nan)
reports[-1].sigmaresid = ValErr(0.172114, 0.000385748, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000277495, None, -3.12312e-07, None, -0.000854348, None, -7.90807e-07, None, -0.000854348, None, -7.90807e-07, None, 0.000681902, None, -1.02321e-05, None, 0.000681902, None, -1.02321e-05, None, 0.172116, None, 0.00441092, None, 0.172116, None, 0.00441092, None)

reports.append(Report(604017744, ("CSC", 1, 1, 1, 10), "MEp11_10"))
reports[-1].posNum = 100381
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000149243, 0.000737761, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.104502, 0.042029, 0), \
                           ValErr(-2.44443e-05, 0.00107704, 0), \
                           ValErr(0.00458461, 0.00522043, 0), \
                           ValErr(2.80798e-06, 1.56334e-05, 0), \
                           33506.5, 100381, 100381, -nan)
reports[-1].sigmaresid = ValErr(0.1733, 0.000386772, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000660874, None, 3.97244e-06, None, -0.000547997, None, 2.07619e-05, None, -0.000547997, None, 2.07619e-05, None, 0.000409112, None, -3.33032e-06, None, 0.000409112, None, -3.33032e-06, None, 0.173307, None, 0.00437894, None, 0.173307, None, 0.00437894, None)

reports.append(Report(604017760, ("CSC", 1, 1, 1, 12), "MEp11_12"))
reports[-1].posNum = 100375
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00219841, 0.000729037, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0635088, 0.0417751, 0), \
                           ValErr(-0.000586129, 0.00106812, 0), \
                           ValErr(-0.00589461, 0.00521669, 0), \
                           ValErr(2.65485e-07, 1.54272e-05, 0), \
                           34410.3, 100375, 100375, -nan)
reports[-1].sigmaresid = ValErr(0.171743, 0.000383311, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00172477, None, 9.1983e-06, None, -0.0016697, None, 2.24098e-05, None, -0.0016697, None, 2.24098e-05, None, -0.00179143, None, 3.47059e-06, None, -0.00179143, None, 3.47059e-06, None, 0.171746, None, 0.00435151, None, 0.171746, None, 0.00435151, None)

reports.append(Report(604017776, ("CSC", 1, 1, 1, 14), "MEp11_14"))
reports[-1].posNum = 99966
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000122489, 0.00073558, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.10617, 0.0419171, 0), \
                           ValErr(0.00101388, 0.00107465, 0), \
                           ValErr(0.00646178, 0.00524181, 0), \
                           ValErr(8.41787e-07, 1.55668e-05, 0), \
                           33894.7, 99966, 99966, -nan)
reports[-1].sigmaresid = ValErr(0.172389, 0.00038554, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00100522, None, -2.58839e-06, None, -0.000450258, None, -7.71508e-07, None, -0.000450258, None, -7.71508e-07, None, -1.22154e-05, None, -4.4134e-06, None, -1.22154e-05, None, -4.4134e-06, None, 0.1724, None, 0.00528261, None, 0.1724, None, 0.00528261, None)

reports.append(Report(604017792, ("CSC", 1, 1, 1, 16), "MEp11_16"))
reports[-1].posNum = 99606
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00339459, 0.000733612, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.119025, 0.0421641, 0), \
                           ValErr(-0.00339399, 0.00108076, 0), \
                           ValErr(-0.00296371, 0.00523037, 0), \
                           ValErr(1.05065e-05, 1.55961e-05, 0), \
                           33763.5, 99606, 99606, -nan)
reports[-1].sigmaresid = ValErr(0.172405, 0.000386271, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00262873, None, 2.09807e-05, None, -0.00309858, None, 4.06927e-05, None, -0.00309858, None, 4.06927e-05, None, -0.00401907, None, 3.55683e-05, None, -0.00401907, None, 3.55683e-05, None, 0.172417, None, 0.00463712, None, 0.172417, None, 0.00463712, None)

reports.append(Report(604017808, ("CSC", 1, 1, 1, 18), "MEp11_18"))
reports[-1].posNum = 100398
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00153083, 0.000732415, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.106457, 0.0418692, 0), \
                           ValErr(8.18485e-05, 0.00107054, 0), \
                           ValErr(-0.00252655, 0.00520724, 0), \
                           ValErr(1.04388e-05, 1.55584e-05, 0), \
                           34116.7, 100398, 100398, -nan)
reports[-1].sigmaresid = ValErr(0.17226, 0.00038442, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00124331, None, 1.64535e-05, None, -0.0012664, None, 3.7025e-05, None, -0.0012664, None, 3.7025e-05, None, -0.00106156, None, 3.20033e-05, None, -0.00106156, None, 3.20033e-05, None, 0.172267, None, 0.00450037, None, 0.172267, None, 0.00450037, None)

reports.append(Report(604017824, ("CSC", 1, 1, 1, 20), "MEp11_20"))
reports[-1].posNum = 100418
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00094979, 0.000734084, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0923013, 0.0418784, 0), \
                           ValErr(-0.00189071, 0.00106843, 0), \
                           ValErr(0.0100998, 0.00522845, 0), \
                           ValErr(2.63737e-05, 1.55695e-05, 0), \
                           34097.5, 100418, 100418, -nan)
reports[-1].sigmaresid = ValErr(0.172304, 0.000384481, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00148606, None, 2.16068e-05, None, -0.00175675, None, 2.83505e-05, None, -0.00175675, None, 2.83505e-05, None, -0.00192126, None, 3.91948e-05, None, -0.00192126, None, 3.91948e-05, None, 0.172318, None, 0.00453837, None, 0.172318, None, 0.00453837, None)

reports.append(Report(604017840, ("CSC", 1, 1, 1, 22), "MEp11_22"))
reports[-1].posNum = 99616
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00259433, 0.000735111, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0990083, 0.0417383, 0), \
                           ValErr(-0.00131768, 0.00106975, 0), \
                           ValErr(-0.00449666, 0.00522133, 0), \
                           ValErr(-8.64086e-06, 1.55864e-05, 0), \
                           34175.6, 99616, 99616, -nan)
reports[-1].sigmaresid = ValErr(0.171699, 0.000384669, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00245026, None, 1.40057e-05, None, -0.00223638, None, -1.56769e-05, None, -0.00223638, None, -1.56769e-05, None, -0.00222494, None, 1.10711e-05, None, -0.00222494, None, 1.10711e-05, None, 0.171705, None, 0.00473029, None, 0.171705, None, 0.00473029, None)

reports.append(Report(604017856, ("CSC", 1, 1, 1, 24), "MEp11_24"))
reports[-1].posNum = 99806
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00322363, 0.000735911, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0450336, 0.0421246, 0), \
                           ValErr(-0.00153192, 0.00107065, 0), \
                           ValErr(-0.00579038, 0.00521608, 0), \
                           ValErr(-9.19233e-06, 1.56229e-05, 0), \
                           33740.7, 99806, 99806, -nan)
reports[-1].sigmaresid = ValErr(0.172561, 0.000386234, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00221784, None, 1.65922e-05, None, -0.00274452, None, 3.07226e-05, None, -0.00274452, None, 3.07226e-05, None, -0.00170513, None, 2.14579e-05, None, -0.00170513, None, 2.14579e-05, None, 0.172566, None, 0.00458602, None, 0.172566, None, 0.00458602, None)

reports.append(Report(604017872, ("CSC", 1, 1, 1, 26), "MEp11_26"))
reports[-1].posNum = 100062
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000806137, 0.000732999, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0965226, 0.0420371, 0), \
                           ValErr(0.00289606, 0.00107318, 0), \
                           ValErr(0.00381688, 0.00522065, 0), \
                           ValErr(-4.97033e-06, 1.55812e-05, 0), \
                           33871.5, 100062, 100062, -nan)
reports[-1].sigmaresid = ValErr(0.172485, 0.000385569, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00113918, None, 5.80901e-07, None, -0.00116033, None, 3.68442e-05, None, -0.00116033, None, 3.68442e-05, None, -0.00110124, None, 1.11483e-05, None, -0.00110124, None, 1.11483e-05, None, 0.172503, None, 0.00501857, None, 0.172503, None, 0.00501857, None)

reports.append(Report(604017888, ("CSC", 1, 1, 1, 28), "MEp11_28"))
reports[-1].posNum = 99589
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000505133, 0.000742429, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0865749, 0.042372, 0), \
                           ValErr(-0.00138593, 0.00108493, 0), \
                           ValErr(-0.00136504, 0.00528348, 0), \
                           ValErr(-1.76865e-05, 1.57055e-05, 0), \
                           33059.2, 99589, 99589, -nan)
reports[-1].sigmaresid = ValErr(0.173618, 0.000389023, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000380554, None, 7.82136e-06, None, -0.000461479, None, 2.09842e-05, None, -0.000461479, None, 2.09842e-05, None, -0.00160891, None, 1.69338e-05, None, -0.00160891, None, 1.69338e-05, None, 0.173624, None, 0.00435308, None, 0.173624, None, 0.00435308, None)

reports.append(Report(604017904, ("CSC", 1, 1, 1, 30), "MEp11_30"))
reports[-1].posNum = 99352
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00110743, 0.000732957, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.140784, 0.0420875, 0), \
                           ValErr(0.000398134, 0.00107466, 0), \
                           ValErr(0.00072971, 0.00520341, 0), \
                           ValErr(-2.13848e-06, 1.56096e-05, 0), \
                           33955.4, 99352, 99352, -nan)
reports[-1].sigmaresid = ValErr(0.171923, 0.000385684, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00124521, None, 1.10679e-06, None, -0.00119652, None, 1.75386e-05, None, -0.00119652, None, 1.75386e-05, None, -0.000605826, None, -4.30094e-06, None, -0.000605826, None, -4.30094e-06, None, 0.171936, None, 0.00462482, None, 0.171936, None, 0.00462482, None)

reports.append(Report(604017920, ("CSC", 1, 1, 1, 32), "MEp11_32"))
reports[-1].posNum = 100127
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00335831, 0.000737427, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0894799, 0.0421618, 0), \
                           ValErr(-0.000638131, 0.00107606, 0), \
                           ValErr(-0.0143538, 0.00522319, 0), \
                           ValErr(2.85176e-05, 1.67413e-05, 0), \
                           33706.5, 100127, 100127, -nan)
reports[-1].sigmaresid = ValErr(0.172808, 0.000386182, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00156909, None, 1.3964e-05, None, -0.00196999, None, 3.63584e-05, None, -0.00196999, None, 3.63584e-05, None, -0.000352719, None, 2.66603e-05, None, -0.000352719, None, 2.66603e-05, None, 0.172819, None, 0.00431509, None, 0.172819, None, 0.00431509, None)

reports.append(Report(604017936, ("CSC", 1, 1, 1, 34), "MEp11_34"))
reports[-1].posNum = 92800
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00261991, 0.000777268, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0886291, 0.0430005, 0), \
                           ValErr(2.13288e-05, 0.00109222, 0), \
                           ValErr(-0.00871394, 0.00536002, 0), \
                           ValErr(3.78152e-06, 1.76682e-05, 0), \
                           31929, 92800, 92800, -nan)
reports[-1].sigmaresid = ValErr(0.171529, 0.000397941, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00236407, None, -3.4075e-05, None, -0.00185097, None, -8.07922e-05, None, -0.00185097, None, -8.07922e-05, None, -0.000765956, None, -4.33289e-05, None, -0.000765956, None, -4.33289e-05, None, 0.171536, None, 0.00559274, None, 0.171536, None, 0.00559274, None)

reports.append(Report(604017952, ("CSC", 1, 1, 1, 36), "MEp11_36"))
reports[-1].posNum = 100432
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00240483, 0.000734633, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.142671, 0.0418102, 0), \
                           ValErr(-0.00042909, 0.00107036, 0), \
                           ValErr(0.0064853, 0.005231, 0), \
                           ValErr(1.30481e-05, 1.55746e-05, 0), \
                           33991.4, 100432, 100432, -nan)
reports[-1].sigmaresid = ValErr(0.172494, 0.000384879, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00307017, None, 1.29217e-05, None, -0.00293758, None, 6.05114e-05, None, -0.00293758, None, 6.05114e-05, None, -0.00279766, None, 4.21445e-05, None, -0.00279766, None, 4.21445e-05, None, 0.172508, None, 0.00522889, None, 0.172508, None, 0.00522889, None)

reports.append(Report(604018184, ("CSC", 1, 1, 2, 1), "MEp12_01"))
reports[-1].posNum = 49189
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00553879, 0.00371515, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.175677, 0.107354, 0), \
                           ValErr(0.00427858, 0.00230984, 0), \
                           ValErr(-0.00908251, 0.0078628, 0), \
                           ValErr(5.33059e-05, 5.81884e-05, 0), \
                           -41282, 49189, 49189, -nan)
reports[-1].sigmaresid = ValErr(0.560074, 0.00178565, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00258445, None, -1.2609e-05, None, -0.0020202, None, 2.30396e-06, None, -0.0020202, None, 2.30396e-06, None, 0.000548454, None, -9.61114e-06, None, 0.000548454, None, -9.61114e-06, None, 0.560122, None, 0.00436126, None, 0.560122, None, 0.00436126, None)

reports.append(Report(604018200, ("CSC", 1, 1, 2, 3), "MEp12_03"))
reports[-1].posNum = 43691
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00644187, 0.00385021, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.113794, 0.113264, 0), \
                           ValErr(-0.006603, 0.00235841, 0), \
                           ValErr(0.0057549, 0.00823977, 0), \
                           ValErr(-9.19248e-05, 5.91449e-05, 0), \
                           -34667, 43691, 43691, -nan)
reports[-1].sigmaresid = ValErr(0.535004, 0.00180987, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00105335, None, -7.76198e-06, None, 0.00295311, None, 2.44201e-06, None, 0.00295311, None, 2.44201e-06, None, 0.00914766, None, -3.37642e-05, None, 0.00914766, None, -3.37642e-05, None, 0.535068, None, 0.00411553, None, 0.535068, None, 0.00411553, None)

reports.append(Report(604018216, ("CSC", 1, 1, 2, 5), "MEp12_05"))
reports[-1].posNum = 48982
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00497303, 0.00358726, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.140882, 0.107167, 0), \
                           ValErr(-0.00327288, 0.00228962, 0), \
                           ValErr(0.00890717, 0.00775891, 0), \
                           ValErr(-3.51666e-05, 5.61012e-05, 0), \
                           -40204.7, 48982, 48982, -nan)
reports[-1].sigmaresid = ValErr(0.549837, 0.00175671, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0032218, None, 1.34715e-05, None, 0.00185767, None, 2.58424e-05, None, 0.00185767, None, 2.58424e-05, None, 0.00825015, None, -1.93925e-05, None, 0.00825015, None, -1.93925e-05, None, 0.549869, None, 0.00401296, None, 0.549869, None, 0.00401296, None)

reports.append(Report(604018232, ("CSC", 1, 1, 2, 7), "MEp12_07"))
reports[-1].posNum = 43590
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00541235, 0.0039565, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.298206, 0.112608, 0), \
                           ValErr(-0.00494063, 0.00239701, 0), \
                           ValErr(0.00200815, 0.00831802, 0), \
                           ValErr(9.24573e-05, 6.07737e-05, 0), \
                           -35238.3, 43590, 43590, -nan)
reports[-1].sigmaresid = ValErr(0.543061, 0.00183925, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00227799, None, -2.05353e-05, None, -0.00396706, None, -2.50628e-05, None, -0.00396706, None, -2.50628e-05, None, -0.00456705, None, 2.85385e-06, None, -0.00456705, None, 2.85385e-06, None, 0.543136, None, 0.0042813, None, 0.543136, None, 0.0042813, None)

reports.append(Report(604018248, ("CSC", 1, 1, 2, 9), "MEp12_09"))
reports[-1].posNum = 44701
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00314144, 0.0037537, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.262304, 0.114459, 0), \
                           ValErr(-0.00430928, 0.00240133, 0), \
                           ValErr(-0.00358084, 0.00820231, 0), \
                           ValErr(-1.62431e-05, 5.81366e-05, 0), \
                           -36289.8, 44701, 44701, -nan)
reports[-1].sigmaresid = ValErr(0.544927, 0.00182249, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00216206, None, 5.16553e-06, None, -0.00257922, None, 7.40793e-06, None, -0.00257922, None, 7.40793e-06, None, -0.00235686, None, 1.98285e-05, None, -0.00235686, None, 1.98285e-05, None, 0.544973, None, 0.00413884, None, 0.544973, None, 0.00413884, None)

reports.append(Report(604018264, ("CSC", 1, 1, 2, 11), "MEp12_11"))
reports[-1].posNum = 45071
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00200395, 0.00369496, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.171404, 0.114606, 0), \
                           ValErr(-0.00166418, 0.00245174, 0), \
                           ValErr(-0.00185514, 0.00815218, 0), \
                           ValErr(-7.82006e-05, 5.78148e-05, 0), \
                           -36249.2, 45071, 45071, -nan)
reports[-1].sigmaresid = ValErr(0.54082, 0.00180131, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00492627, None, -1.55156e-05, None, 0.00123625, None, 7.141e-06, None, 0.00123625, None, 7.141e-06, None, 0.000920528, None, 1.14525e-05, None, 0.000920528, None, 1.14525e-05, None, 0.540847, None, 0.00419986, None, 0.540847, None, 0.00419986, None)

reports.append(Report(604018280, ("CSC", 1, 1, 2, 13), "MEp12_13"))
reports[-1].posNum = 43415
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000288757, 0.00397601, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0265631, 0.112807, 0), \
                           ValErr(-0.000921145, 0.00240775, 0), \
                           ValErr(0.0119483, 0.00830708, 0), \
                           ValErr(-9.31892e-07, 6.10773e-05, 0), \
                           -34808.4, 43415, 43415, -nan)
reports[-1].sigmaresid = ValErr(0.539465, 0.00183075, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00283106, None, 4.61399e-05, None, -0.00384538, None, 3.67298e-05, None, -0.00384538, None, 3.67298e-05, None, -0.00257259, None, 3.08865e-05, None, -0.00257259, None, 3.08865e-05, None, 0.539481, None, 0.00425346, None, 0.539481, None, 0.00425346, None)

reports.append(Report(604018296, ("CSC", 1, 1, 2, 15), "MEp12_15"))
reports[-1].posNum = 48522
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00186973, 0.00361084, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0297631, 0.10678, 0), \
                           ValErr(-0.00236441, 0.00229443, 0), \
                           ValErr(0.00179817, 0.00777414, 0), \
                           ValErr(-1.1013e-05, 5.65307e-05, 0), \
                           -39872.8, 48522, 48522, -nan)
reports[-1].sigmaresid = ValErr(0.550354, 0.00176668, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00193156, None, -8.63814e-06, None, 0.00116517, None, 3.22423e-06, None, 0.00116517, None, 3.22423e-06, None, 0.000947684, None, -1.09737e-05, None, 0.000947684, None, -1.09737e-05, None, 0.550362, None, 0.00448886, None, 0.550362, None, 0.00448886, None)

reports.append(Report(604018312, ("CSC", 1, 1, 2, 17), "MEp12_17"))
reports[-1].posNum = 43556
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00166246, 0.00384483, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.313946, 0.112967, 0), \
                           ValErr(0.00507443, 0.00239689, 0), \
                           ValErr(0.00886267, 0.00822412, 0), \
                           ValErr(-6.43484e-05, 5.92375e-05, 0), \
                           -34254.4, 43556, 43556, -nan)
reports[-1].sigmaresid = ValErr(0.531265, 0.0018, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0041861, None, 2.71987e-05, None, -0.00556164, None, 2.98727e-05, None, -0.00556164, None, 2.98727e-05, None, -0.00702407, None, 5.56256e-05, None, -0.00702407, None, 5.56256e-05, None, 0.531339, None, 0.00417151, None, 0.531339, None, 0.00417151, None)

reports.append(Report(604018328, ("CSC", 1, 1, 2, 19), "MEp12_19"))
reports[-1].posNum = 49540
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00916144, 0.00368102, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00747153, 0.106281, 0), \
                           ValErr(-0.00307711, 0.00227761, 0), \
                           ValErr(-0.0134865, 0.0077985, 0), \
                           ValErr(8.79659e-05, 5.74522e-05, 0), \
                           -41275.4, 49540, 49540, -nan)
reports[-1].sigmaresid = ValErr(0.556679, 0.00176852, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00270637, None, 9.20321e-06, None, -0.00375993, None, -7.25516e-06, None, -0.00375993, None, -7.25516e-06, None, -0.00209542, None, -1.0221e-05, None, -0.00209542, None, -1.0221e-05, None, 0.556714, None, 0.00431754, None, 0.556714, None, 0.00431754, None)

reports.append(Report(604018344, ("CSC", 1, 1, 2, 21), "MEp12_21"))
reports[-1].posNum = 43225
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00370756, 0.00384228, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0410138, 0.114521, 0), \
                           ValErr(0.0016029, 0.00237403, 0), \
                           ValErr(0.0211458, 0.00830135, 0), \
                           ValErr(-3.25137e-05, 5.87569e-05, 0), \
                           -33681.7, 43225, 43225, -nan)
reports[-1].sigmaresid = ValErr(0.527441, 0.00179387, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00243743, None, -3.09604e-06, None, -0.00293269, None, 1.10345e-05, None, -0.00293269, None, 1.10345e-05, None, -0.00283472, None, 1.22066e-05, None, -0.00283472, None, 1.22066e-05, None, 0.527485, None, 0.0040116, None, 0.527485, None, 0.0040116, None)

reports.append(Report(604018360, ("CSC", 1, 1, 2, 23), "MEp12_23"))
reports[-1].posNum = 48538
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00619152, 0.00363116, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.240502, 0.107564, 0), \
                           ValErr(-0.00520068, 0.00230558, 0), \
                           ValErr(-0.00106899, 0.00784053, 0), \
                           ValErr(4.81056e-05, 5.66559e-05, 0), \
                           -39803.2, 48538, 48538, -nan)
reports[-1].sigmaresid = ValErr(0.549417, 0.00176338, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00945909, None, 2.03962e-06, None, -0.00513597, None, -3.94999e-06, None, -0.00513597, None, -3.94999e-06, None, -0.00522664, None, 3.54182e-06, None, -0.00522664, None, 3.54182e-06, None, 0.549473, None, 0.00420434, None, 0.549473, None, 0.00420434, None)

reports.append(Report(604018376, ("CSC", 1, 1, 2, 25), "MEp12_25"))
reports[-1].posNum = 43867
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00110597, 0.00393026, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.00455843, 0.110787, 0), \
                           ValErr(0.00271472, 0.00237081, 0), \
                           ValErr(0.00302231, 0.00810167, 0), \
                           ValErr(-5.232e-05, 5.71449e-05, 0), \
                           -35386.1, 43867, 43867, -nan)
reports[-1].sigmaresid = ValErr(0.542119, 0.00182685, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00275596, None, 1.00157e-05, None, -0.00304172, None, 1.08224e-05, None, -0.00304172, None, 1.08224e-05, None, -0.00373195, None, 2.04688e-05, None, -0.00373195, None, 2.04688e-05, None, 0.542132, None, 0.00425195, None, 0.542132, None, 0.00425195, None)

reports.append(Report(604018392, ("CSC", 1, 1, 2, 27), "MEp12_27"))
reports[-1].posNum = 44979
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00104194, 0.00379397, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0381566, 0.112467, 0), \
                           ValErr(0.000363674, 0.00237576, 0), \
                           ValErr(-0.0062735, 0.00815745, 0), \
                           ValErr(1.69616e-05, 5.85559e-05, 0), \
                           -36615, 44979, 44979, -nan)
reports[-1].sigmaresid = ValErr(0.546133, 0.00182087, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00209871, None, -4.3158e-06, None, 0.00105591, None, 1.46006e-06, None, 0.00105591, None, 1.46006e-06, None, 0.00291997, None, -1.34706e-05, None, 0.00291997, None, -1.34706e-05, None, 0.546138, None, 0.00411929, None, 0.546138, None, 0.00411929, None)

reports.append(Report(604018408, ("CSC", 1, 1, 2, 29), "MEp12_29"))
reports[-1].posNum = 46022
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000319968, 0.00369302, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0466562, 0.111172, 0), \
                           ValErr(-0.00174147, 0.00237907, 0), \
                           ValErr(-0.000179969, 0.00796376, 0), \
                           ValErr(-1.95974e-05, 5.77633e-05, 0), \
                           -37235.6, 46022, 46022, -nan)
reports[-1].sigmaresid = ValErr(0.54343, 0.00179121, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000152486, None, 6.6718e-06, None, -0.000532524, None, 9.18465e-06, None, -0.000532524, None, 9.18465e-06, None, 0.00110763, None, -3.52653e-06, None, 0.00110763, None, -3.52653e-06, None, 0.543433, None, 0.00437254, None, 0.543433, None, 0.00437254, None)

reports.append(Report(604018424, ("CSC", 1, 1, 2, 31), "MEp12_31"))
reports[-1].posNum = 44845
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00942673, 0.00395591, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0418327, 0.109988, 0), \
                           ValErr(-0.00022577, 0.00235315, 0), \
                           ValErr(-0.0100444, 0.00817445, 0), \
                           ValErr(0.000126761, 6.05129e-05, 0), \
                           -36623.5, 44845, 44845, -nan)
reports[-1].sigmaresid = ValErr(0.547566, 0.00182837, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00252259, None, -3.51828e-06, None, -0.00399247, None, 1.19948e-05, None, -0.00399247, None, 1.19948e-05, None, -0.00556469, None, 1.36169e-05, None, -0.00556469, None, 1.36169e-05, None, 0.547598, None, 0.00402709, None, 0.547598, None, 0.00402709, None)

reports.append(Report(604018440, ("CSC", 1, 1, 2, 33), "MEp12_33"))
reports[-1].posNum = 48189
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000873352, 0.00360932, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.108005, 0.106403, 0), \
                           ValErr(-0.00312531, 0.00228202, 0), \
                           ValErr(-0.00157654, 0.00769701, 0), \
                           ValErr(0.000102597, 5.62913e-05, 0), \
                           -39233.1, 48189, 48189, -nan)
reports[-1].sigmaresid = ValErr(0.54619, 0.00175936, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00268649, None, -7.60646e-06, None, 0.00119405, None, -6.68162e-06, None, 0.00119405, None, -6.68162e-06, None, -0.000530181, None, 9.19667e-06, None, -0.000530181, None, 9.19667e-06, None, 0.546225, None, 0.00422856, None, 0.546225, None, 0.00422856, None)

reports.append(Report(604018456, ("CSC", 1, 1, 2, 35), "MEp12_35"))
reports[-1].posNum = 43121
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00689222, 0.00387013, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.103575, 0.114344, 0), \
                           ValErr(-0.000232378, 0.0024209, 0), \
                           ValErr(0.00703285, 0.00833713, 0), \
                           ValErr(-7.09944e-05, 5.91454e-05, 0), \
                           -33414.3, 43121, 43121, -nan)
reports[-1].sigmaresid = ValErr(0.525165, 0.00178828, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00421087, None, -6.54704e-06, None, 0.00336896, None, -4.26158e-06, None, 0.00336896, None, -4.26158e-06, None, -0.00349907, None, -6.74473e-07, None, -0.00349907, None, -6.74473e-07, None, 0.525182, None, 0.00418892, None, 0.525182, None, 0.00418892, None)

reports.append(Report(604018192, ("CSC", 1, 1, 2, 2), "MEp12_02"))
reports[-1].posNum = 43841
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00158336, 0.00364374, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.160349, 0.105835, 0), \
                           ValErr(-0.0032757, 0.00219842, 0), \
                           ValErr(-0.0118864, 0.0075689, 0), \
                           ValErr(-7.2204e-05, 5.61691e-05, 0), \
                           -33671.9, 43841, 43841, -nan)
reports[-1].sigmaresid = ValErr(0.52158, 0.00176143, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00147577, None, -3.18242e-05, None, 0.000645785, None, -1.23651e-05, None, 0.000645785, None, -1.23651e-05, None, -0.0061426, None, -6.89308e-06, None, -0.0061426, None, -6.89308e-06, None, 0.521636, None, 0.00386471, None, 0.521636, None, 0.00386471, None)

reports.append(Report(604018208, ("CSC", 1, 1, 2, 4), "MEp12_04"))
reports[-1].posNum = 42561
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00338402, 0.00375818, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0534249, 0.110523, 0), \
                           ValErr(0.00010378, 0.00224168, 0), \
                           ValErr(0.00902382, 0.00794007, 0), \
                           ValErr(4.74512e-05, 5.71392e-05, 0), \
                           -33029.3, 42561, 42561, -nan)
reports[-1].sigmaresid = ValErr(0.525769, 0.00180208, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00138362, None, -8.71136e-06, None, 0.00169632, None, -3.04225e-05, None, 0.00169632, None, -3.04225e-05, None, -0.000251902, None, -1.25108e-05, None, -0.000251902, None, -1.25108e-05, None, 0.525787, None, 0.00393865, None, 0.525787, None, 0.00393865, None)

reports.append(Report(604018224, ("CSC", 1, 1, 2, 6), "MEp12_06"))
reports[-1].posNum = 46466
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000697062, 0.00352868, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0613284, 0.0999597, 0), \
                           ValErr(-0.00195861, 0.00210993, 0), \
                           ValErr(-0.00810574, 0.00726009, 0), \
                           ValErr(-5.17776e-05, 5.46693e-05, 0), \
                           -35799, 46466, 46466, -nan)
reports[-1].sigmaresid = ValErr(0.522827, 0.00171504, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000264632, None, -9.73702e-06, None, 0.00223649, None, -1.97512e-05, None, 0.00223649, None, -1.97512e-05, None, -0.00144254, None, -2.39447e-06, None, -0.00144254, None, -2.39447e-06, None, 0.522851, None, 0.00416044, None, 0.522851, None, 0.00416044, None)

reports.append(Report(604018240, ("CSC", 1, 1, 2, 8), "MEp12_08"))
reports[-1].posNum = 40893
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000153298, 0.00382639, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.149181, 0.106122, 0), \
                           ValErr(-0.00304707, 0.00218844, 0), \
                           ValErr(0.00349643, 0.00778162, 0), \
                           ValErr(1.07761e-05, 5.75398e-05, 0), \
                           -30101.4, 40893, 40893, -nan)
reports[-1].sigmaresid = ValErr(0.505181, 0.00176647, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000514402, None, 7.11997e-07, None, -0.00060197, None, -2.22826e-05, None, -0.00060197, None, -2.22826e-05, None, -0.00473951, None, 2.69068e-05, None, -0.00473951, None, 2.69068e-05, None, 0.505215, None, 0.00733552, None, 0.505215, None, 0.00733552, None)

reports.append(Report(604018256, ("CSC", 1, 1, 2, 10), "MEp12_10"))
reports[-1].posNum = 48204
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00116755, 0.00352599, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00708222, 0.100624, 0), \
                           ValErr(-0.00284588, 0.00214076, 0), \
                           ValErr(-0.0026259, 0.00734381, 0), \
                           ValErr(3.17396e-05, 5.46565e-05, 0), \
                           -38044.6, 48204, 48204, -nan)
reports[-1].sigmaresid = ValErr(0.532753, 0.00171581, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000460191, None, -5.93634e-06, None, 0.000108843, None, -7.08936e-06, None, 0.000108843, None, -7.08936e-06, None, 0.00493557, None, -2.01922e-05, None, 0.00493557, None, -2.01922e-05, None, 0.532765, None, 0.00398912, None, 0.532765, None, 0.00398912, None)

reports.append(Report(604018272, ("CSC", 1, 1, 2, 12), "MEp12_12"))
reports[-1].posNum = 40959
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00554877, 0.00374799, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.380574, 0.104736, 0), \
                           ValErr(0.00241224, 0.00216792, 0), \
                           ValErr(0.00338586, 0.00766286, 0), \
                           ValErr(-6.00588e-05, 5.66049e-05, 0), \
                           -30275.5, 40959, 40959, -nan)
reports[-1].sigmaresid = ValErr(0.506732, 0.00177047, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00278234, None, -1.47038e-05, None, 0.00300929, None, -1.84846e-05, None, 0.00300929, None, -1.84846e-05, None, 0.00128956, None, 1.25779e-06, None, 0.00128956, None, 1.25779e-06, None, 0.506821, None, 0.00435938, None, 0.506821, None, 0.00435938, None)

reports.append(Report(604018288, ("CSC", 1, 1, 2, 14), "MEp12_14"))
reports[-1].posNum = 47171
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00656087, 0.00354951, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.194832, 0.0989607, 0), \
                           ValErr(0.00189078, 0.00210948, 0), \
                           ValErr(0.00681927, 0.00725369, 0), \
                           ValErr(6.92729e-05, 5.4759e-05, 0), \
                           -36528, 47171, 47171, -nan)
reports[-1].sigmaresid = ValErr(0.524891, 0.0017089, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0104083, None, 2.84778e-05, None, -0.00750765, None, 1.87124e-05, None, -0.00750765, None, 1.87124e-05, None, -0.00706391, None, 1.00385e-05, None, -0.00706391, None, 1.00385e-05, None, 0.524934, None, 0.00403347, None, 0.524934, None, 0.00403347, None)

reports.append(Report(604018304, ("CSC", 1, 1, 2, 16), "MEp12_16"))
reports[-1].posNum = 42115
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000542386, 0.00370732, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.067798, 0.10975, 0), \
                           ValErr(-0.00281878, 0.00224106, 0), \
                           ValErr(0.00480957, 0.00785554, 0), \
                           ValErr(1.75803e-05, 5.60369e-05, 0), \
                           -31837.7, 42115, 42115, -nan)
reports[-1].sigmaresid = ValErr(0.51532, 0.0017756, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00268282, None, -8.90057e-07, None, -0.00156424, None, -2.43028e-05, None, -0.00156424, None, -2.43028e-05, None, 9.48852e-05, None, -3.63948e-06, None, 9.48852e-05, None, -3.63948e-06, None, 0.515339, None, 0.00441226, None, 0.515339, None, 0.00441226, None)

reports.append(Report(604018320, ("CSC", 1, 1, 2, 18), "MEp12_18"))
reports[-1].posNum = 43794
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0102325, 0.00369427, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0871498, 0.104212, 0), \
                           ValErr(-0.00123301, 0.00215082, 0), \
                           ValErr(0.0240593, 0.00756521, 0), \
                           ValErr(-3.59852e-05, 5.6302e-05, 0), \
                           -34143.1, 43794, 43794, -nan)
reports[-1].sigmaresid = ValErr(0.527657, 0.00178291, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00279794, None, -1.89138e-06, None, 0.00239631, None, 3.44197e-05, None, 0.00239631, None, 3.44197e-05, None, 0.00110331, None, 1.8046e-05, None, 0.00110331, None, 1.8046e-05, None, 0.527724, None, 0.00467485, None, 0.527724, None, 0.00467485, None)

reports.append(Report(604018336, ("CSC", 1, 1, 2, 20), "MEp12_20"))
reports[-1].posNum = 44226
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000392557, 0.00367329, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.100726, 0.105015, 0), \
                           ValErr(-0.00406034, 0.00220455, 0), \
                           ValErr(-0.00398439, 0.00756933, 0), \
                           ValErr(-4.37484e-05, 5.66415e-05, 0), \
                           -34302.8, 44226, 44226, -nan)
reports[-1].sigmaresid = ValErr(0.525549, 0.00176709, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00141047, None, 1.49903e-05, None, 0.000792367, None, 4.16174e-07, None, 0.000792367, None, 4.16174e-07, None, 0.00277773, None, 2.05257e-05, None, 0.00277773, None, 2.05257e-05, None, 0.525578, None, 0.00430966, None, 0.525578, None, 0.00430966, None)

reports.append(Report(604018352, ("CSC", 1, 1, 2, 22), "MEp12_22"))
reports[-1].posNum = 42880
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00216709, 0.00374941, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.142714, 0.107639, 0), \
                           ValErr(-0.000809249, 0.00222663, 0), \
                           ValErr(0.00118964, 0.00778533, 0), \
                           ValErr(8.11962e-06, 5.72095e-05, 0), \
                           -32931.1, 42880, 42880, -nan)
reports[-1].sigmaresid = ValErr(0.521547, 0.00178095, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00157996, None, -2.56485e-05, None, 0.00191965, None, -3.05799e-06, None, 0.00191965, None, -3.05799e-06, None, -8.77449e-05, None, -6.06081e-06, None, -8.77449e-05, None, -6.06081e-06, None, 0.521558, None, 0.00407961, None, 0.521558, None, 0.00407961, None)

reports.append(Report(604018368, ("CSC", 1, 1, 2, 24), "MEp12_24"))
reports[-1].posNum = 47010
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000641279, 0.00350354, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.13657, 0.0989409, 0), \
                           ValErr(0.00133819, 0.00210657, 0), \
                           ValErr(-0.00690076, 0.00719183, 0), \
                           ValErr(-7.97065e-06, 5.46063e-05, 0), \
                           -36285.8, 47010, 47010, -nan)
reports[-1].sigmaresid = ValErr(0.523579, 0.00170754, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00369407, None, -8.35623e-07, None, 0.00251932, None, -1.18482e-05, None, 0.00251932, None, -1.18482e-05, None, 0.00716435, None, -1.72047e-05, None, 0.00716435, None, -1.72047e-05, None, 0.523598, None, 0.00386168, None, 0.523598, None, 0.00386168, None)

reports.append(Report(604018384, ("CSC", 1, 1, 2, 26), "MEp12_26"))
reports[-1].posNum = 41528
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000945996, 0.00377027, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0605226, 0.104027, 0), \
                           ValErr(0.000496902, 0.00214481, 0), \
                           ValErr(-0.00301323, 0.00765733, 0), \
                           ValErr(0.000127035, 5.65381e-05, 0), \
                           -30428.9, 41528, 41528, -nan)
reports[-1].sigmaresid = ValErr(0.503483, 0.00174703, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00356524, None, -2.22002e-05, None, 0.00266994, None, -2.75892e-05, None, 0.00266994, None, -2.75892e-05, None, 0.0038525, None, -3.26639e-05, None, 0.0038525, None, -3.26639e-05, None, 0.503516, None, 0.00408536, None, 0.503516, None, 0.00408536, None)

reports.append(Report(604018400, ("CSC", 1, 1, 2, 28), "MEp12_28"))
reports[-1].posNum = 48132
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00445063, 0.00353295, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.110969, 0.100678, 0), \
                           ValErr(0.00158845, 0.00215031, 0), \
                           ValErr(-0.015205, 0.00734326, 0), \
                           ValErr(1.62753e-05, 5.48885e-05, 0), \
                           -37877, 48132, 48132, -nan)
reports[-1].sigmaresid = ValErr(0.531529, 0.00171315, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000404704, None, -1.54653e-05, None, 0.000418906, None, 6.66025e-06, None, 0.000418906, None, 6.66025e-06, None, -0.00132322, None, 3.93828e-05, None, -0.00132322, None, 3.93828e-05, None, 0.531563, None, 0.00387907, None, 0.531563, None, 0.00387907, None)

reports.append(Report(604018416, ("CSC", 1, 1, 2, 30), "MEp12_30"))
reports[-1].posNum = 40801
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000444965, 0.00375659, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0714789, 0.10396, 0), \
                           ValErr(-0.00242572, 0.00210664, 0), \
                           ValErr(0.00902383, 0.00757161, 0), \
                           ValErr(-1.11419e-05, 5.61128e-05, 0), \
                           -29618.3, 40801, 40801, -nan)
reports[-1].sigmaresid = ValErr(0.500064, 0.00175056, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00279265, None, -1.89859e-07, None, -0.00338072, None, 1.03928e-05, None, -0.00338072, None, 1.03928e-05, None, -0.00441705, None, 6.58834e-06, None, -0.00441705, None, 6.58834e-06, None, 0.500087, None, 0.003984, None, 0.500087, None, 0.003984, None)

reports.append(Report(604018432, ("CSC", 1, 1, 2, 32), "MEp12_32"))
reports[-1].posNum = 47126
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00320328, 0.00353403, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.143574, 0.0992666, 0), \
                           ValErr(-0.00386447, 0.00211581, 0), \
                           ValErr(-0.00907988, 0.00724118, 0), \
                           ValErr(4.64775e-05, 5.46459e-05, 0), \
                           -36326.2, 47126, 47126, -nan)
reports[-1].sigmaresid = ValErr(0.523036, 0.00170368, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000222912, None, -1.05207e-06, None, 0.000436858, None, -5.50441e-06, None, 0.000436858, None, -5.50441e-06, None, -0.000633219, None, -1.39061e-05, None, -0.000633219, None, -1.39061e-05, None, 0.523081, None, 0.00423333, None, 0.523081, None, 0.00423333, None)

reports.append(Report(604018448, ("CSC", 1, 1, 2, 34), "MEp12_34"))
reports[-1].posNum = 43343
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00809824, 0.00367868, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0289142, 0.107523, 0), \
                           ValErr(-0.000952188, 0.00223747, 0), \
                           ValErr(0.00580825, 0.00770736, 0), \
                           ValErr(-6.56964e-05, 5.63935e-05, 0), \
                           -33154, 43343, 43343, -nan)
reports[-1].sigmaresid = ValErr(0.519953, 0.001766, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00595308, None, -4.98918e-06, None, 0.00511212, None, -2.02693e-05, None, 0.00511212, None, -2.02693e-05, None, 0.00407072, None, -1.65497e-05, None, 0.00407072, None, -1.65497e-05, None, 0.519965, None, 0.0040389, None, 0.519965, None, 0.0040389, None)

reports.append(Report(604018464, ("CSC", 1, 1, 2, 36), "MEp12_36"))
reports[-1].posNum = 45218
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00431645, 0.00361407, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.231371, 0.101804, 0), \
                           ValErr(-0.00337993, 0.00212272, 0), \
                           ValErr(-0.00786056, 0.00740606, 0), \
                           ValErr(5.34111e-06, 5.54863e-05, 0), \
                           -35099.1, 45218, 45218, -nan)
reports[-1].sigmaresid = ValErr(0.525861, 0.00174864, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00115109, None, 1.26073e-05, None, -0.0019614, None, 2.83706e-06, None, -0.0019614, None, 2.83706e-06, None, 0.00404865, None, -1.75893e-05, None, 0.00404865, None, -1.75893e-05, None, 0.525907, None, 0.00413228, None, 0.525907, None, 0.00413228, None)

reports.append(Report(604018696, ("CSC", 1, 1, 3, 1), "MEp13_01"))
reports[-1].posNum = 20021
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00695832, 0.0156246, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.79252, 0.307495, 0), \
                           ValErr(-0.00488039, 0.0069174, 0), \
                           ValErr(0.0105154, 0.0149251, 0), \
                           ValErr(0.000277442, 0.000244339, 0), \
                           -36659.2, 20021, 20021, -nan)
reports[-1].sigmaresid = ValErr(1.51002, 0.00754634, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0255303, None, 2.76678e-05, None, -0.0134539, None, -1.80031e-05, None, -0.0134539, None, -1.80031e-05, None, -0.0209158, None, 1.10188e-05, None, -0.0209158, None, 1.10188e-05, None, 1.51318, None, 0.00629612, None, 1.51318, None, 0.00629612, None)

reports.append(Report(604018704, ("CSC", 1, 1, 3, 2), "MEp13_02"))
reports[-1].posNum = 19736
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00874205, 0.0158981, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.43019, 0.315244, 0), \
                           ValErr(-0.0156841, 0.00711761, 0), \
                           ValErr(-0.00162288, 0.0155978, 0), \
                           ValErr(-0.000247505, 0.000249598, 0), \
                           -36155.7, 19736, 19736, -nan)
reports[-1].sigmaresid = ValErr(1.51139, 0.00760963, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0143721, None, -2.504e-05, None, 0.00840096, None, -8.22065e-05, None, 0.00840096, None, -8.22065e-05, None, 0.00608633, None, -2.30835e-05, None, 0.00608633, None, -2.30835e-05, None, 1.51383, None, 0.00664587, None, 1.51383, None, 0.00664587, None)

reports.append(Report(604018712, ("CSC", 1, 1, 3, 3), "MEp13_03"))
reports[-1].posNum = 18296
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00822116, 0.0161156, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.75984, 0.329063, 0), \
                           ValErr(-0.0134888, 0.00771689, 0), \
                           ValErr(-0.0140866, 0.0157755, 0), \
                           ValErr(-6.09814e-06, 0.000110576, 0), \
                           -33552.3, 18296, 18296, -nan)
reports[-1].sigmaresid = ValErr(1.51425, 0.00788708, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0251626, None, -9.34175e-05, None, 0.00335783, None, -0.000138265, None, 0.00335783, None, -0.000138265, None, -0.0218946, None, -2.49183e-05, None, -0.0218946, None, -2.49183e-05, None, 1.51721, None, 0.00666825, None, 1.51721, None, 0.00666825, None)

reports.append(Report(604018720, ("CSC", 1, 1, 3, 4), "MEp13_04"))
reports[-1].posNum = 18418
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0352006, 0.0159717, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.02785, 0.342592, 0), \
                           ValErr(-0.0119055, 0.00795485, 0), \
                           ValErr(0.00590753, 0.0159973, 0), \
                           ValErr(0.000276422, 0.000206585, 0), \
                           -34108.4, 18418, 18418, -nan)
reports[-1].sigmaresid = ValErr(1.54185, 0.00667243, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0452803, None, -0.000103594, None, 0.0327743, None, -0.000116098, None, 0.0327743, None, -0.000116098, None, 0.0330777, None, -8.48146e-05, None, 0.0330777, None, -8.48146e-05, None, 1.54517, None, 0.00750967, None, 1.54517, None, 0.00750967, None)

reports.append(Report(604018728, ("CSC", 1, 1, 3, 5), "MEp13_05"))
reports[-1].posNum = 20527
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0153266, 0.0137147, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.05884, 0.297103, 0), \
                           ValErr(-0.0112379, 0.00426757, 0), \
                           ValErr(0.00425554, 0.0132573, 0), \
                           ValErr(0.000324028, 0.000159357, 0), \
                           -37382.5, 20527, 20527, -nan)
reports[-1].sigmaresid = ValErr(1.49509, 0.00663499, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0105812, None, -4.70771e-05, None, 0.0133994, None, -9.9563e-05, None, 0.0133994, None, -9.9563e-05, None, 0.0101402, None, -3.68905e-05, None, 0.0101402, None, -3.68905e-05, None, 1.49888, None, 0.00670559, None, 1.49888, None, 0.00670559, None)

reports.append(Report(604018736, ("CSC", 1, 1, 3, 6), "MEp13_06"))
reports[-1].posNum = 20296
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0254088, 0.015515, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.87156, 0.296452, 0), \
                           ValErr(-0.00572119, 0.00680584, 0), \
                           ValErr(0.00903859, 0.014856, 0), \
                           ValErr(-0.000129766, 0.000186805, 0), \
                           -36991, 20296, 20296, -nan)
reports[-1].sigmaresid = ValErr(1.49726, 0.00596275, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00434013, None, -7.3339e-05, None, 0.0189901, None, -8.63351e-05, None, 0.0189901, None, -8.63351e-05, None, 0.0028764, None, -8.28996e-05, None, 0.0028764, None, -8.28996e-05, None, 1.50057, None, 0.00659108, None, 1.50057, None, 0.00659108, None)

reports.append(Report(604018744, ("CSC", 1, 1, 3, 7), "MEp13_07"))
reports[-1].posNum = 19056
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0220947, 0.0159088, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.83915, 0.318994, 0), \
                           ValErr(0.000858991, 0.00737641, 0), \
                           ValErr(-0.013856, 0.0152702, 0), \
                           ValErr(0.000137242, 0.000257761, 0), \
                           -34920.7, 19056, 19056, -nan)
reports[-1].sigmaresid = ValErr(1.51226, 0.00774639, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0119837, None, 2.25037e-05, None, -0.0123166, None, -7.06263e-05, None, -0.0123166, None, -7.06263e-05, None, -0.00257626, None, -7.00583e-05, None, -0.00257626, None, -7.00583e-05, None, 1.51545, None, 0.00665315, None, 1.51545, None, 0.00665315, None)

reports.append(Report(604018752, ("CSC", 1, 1, 3, 8), "MEp13_08"))
reports[-1].posNum = 18358
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0025685, 0.0163433, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.27579, 0.329561, 0), \
                           ValErr(0.0125051, 0.00766381, 0), \
                           ValErr(0.00373763, 0.0160068, 0), \
                           ValErr(0.000229343, 0.000265417, 0), \
                           -33696.2, 18358, 18358, -nan)
reports[-1].sigmaresid = ValErr(1.51674, 0.00791561, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0187758, None, -1.37628e-05, None, -0.00485252, None, -5.03517e-05, None, -0.00485252, None, -5.03517e-05, None, -0.0116813, None, 4.50637e-05, None, -0.0116813, None, 4.50637e-05, None, 1.519, None, 0.0067274, None, 1.519, None, 0.0067274, None)

reports.append(Report(604018760, ("CSC", 1, 1, 3, 9), "MEp13_09"))
reports[-1].posNum = 18877
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000373338, 0.0160593, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.84464, 0.323098, 0), \
                           ValErr(-0.0129618, 0.00693523, 0), \
                           ValErr(-0.0121505, 0.0155973, 0), \
                           ValErr(0.000687698, 0.000206031, 0), \
                           -34612.1, 18877, 18877, -nan)
reports[-1].sigmaresid = ValErr(1.5138, 0.00600132, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0259161, None, -4.05224e-05, None, 0.0120258, None, -0.000131424, None, 0.0120258, None, -0.000131424, None, 0.0215403, None, -0.000155658, None, 0.0215403, None, -0.000155658, None, 1.51726, None, 0.00654739, None, 1.51726, None, 0.00654739, None)

reports.append(Report(604018768, ("CSC", 1, 1, 3, 10), "MEp13_10"))
reports[-1].posNum = 20643
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0109861, 0.0152405, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.75957, 0.310814, 0), \
                           ValErr(-0.00112035, 0.00692769, 0), \
                           ValErr(-0.0306651, 0.0149842, 0), \
                           ValErr(0.000269643, 0.000115789, 0), \
                           -37730.7, 20643, 20643, -nan)
reports[-1].sigmaresid = ValErr(1.50506, 0.0073999, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0163906, None, -3.68305e-05, None, 0.0126643, None, -0.000176, None, 0.0126643, None, -0.000176, None, 0.0257447, None, -0.000172303, None, 0.0257447, None, -0.000172303, None, 1.50808, None, 0.00655948, None, 1.50808, None, 0.00655948, None)

reports.append(Report(604018776, ("CSC", 1, 1, 3, 11), "MEp13_11"))
reports[-1].posNum = 19221
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0294415, 0.016327, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.51115, 0.317048, 0), \
                           ValErr(-0.0143019, 0.00718135, 0), \
                           ValErr(-0.0209038, 0.0159245, 0), \
                           ValErr(6.53632e-05, 0.000228505, 0), \
                           -35638.3, 19221, 19221, -nan)
reports[-1].sigmaresid = ValErr(1.54527, 0.00550021, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0134963, None, 3.96287e-06, None, -0.0157112, None, -3.63828e-06, None, -0.0157112, None, -3.63828e-06, None, -0.00585946, None, 0.000102699, None, -0.00585946, None, 0.000102699, None, 1.54776, None, 0.00683582, None, 1.54776, None, 0.00683582, None)

reports.append(Report(604018784, ("CSC", 1, 1, 3, 12), "MEp13_12"))
reports[-1].posNum = 18582
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00777104, 0.0164102, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.70002, 0.324874, 0), \
                           ValErr(0.00364842, 0.00752623, 0), \
                           ValErr(-0.00197669, 0.0157254, 0), \
                           ValErr(-0.000164984, 0.00026628, 0), \
                           -34321.6, 18582, 18582, -nan)
reports[-1].sigmaresid = ValErr(1.53433, 0.00796029, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0015541, None, -2.72876e-05, None, 0.00902116, None, -8.23362e-05, None, 0.00902116, None, -8.23362e-05, None, -0.0066203, None, -4.85622e-05, None, -0.0066203, None, -4.85622e-05, None, 1.53729, None, 0.00691384, None, 1.53729, None, 0.00691384, None)

reports.append(Report(604018792, ("CSC", 1, 1, 3, 13), "MEp13_13"))
reports[-1].posNum = 18201
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00807211, 0.0162635, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.43695, 0.32416, 0), \
                           ValErr(-0.00190219, 0.00750577, 0), \
                           ValErr(0.00209568, 0.0155634, 0), \
                           ValErr(0.000369446, 0.000264166, 0), \
                           -33304.1, 18201, 18201, -nan)
reports[-1].sigmaresid = ValErr(1.50811, 0.00790389, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0215549, None, -5.17233e-06, None, -0.00754054, None, -8.18001e-06, None, -0.00754054, None, -8.18001e-06, None, -0.00217578, None, 2.19386e-05, None, -0.00217578, None, 2.19386e-05, None, 1.51055, None, 0.00720435, None, 1.51055, None, 0.00720435, None)

reports.append(Report(604018800, ("CSC", 1, 1, 3, 14), "MEp13_14"))
reports[-1].posNum = 20198
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0350101, 0.0157166, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.43381, 0.311106, 0), \
                           ValErr(0.00333905, 0.00683225, 0), \
                           ValErr(0.0378258, 0.0153852, 0), \
                           ValErr(-0.000316498, 0.000124089, 0), \
                           -36971.5, 20198, 20198, -nan)
reports[-1].sigmaresid = ValErr(1.50911, 0.00746993, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0120516, None, -1.157e-05, None, 0.00618313, None, -7.05581e-06, None, 0.00618313, None, -7.05581e-06, None, -0.00647862, None, 2.95183e-05, None, -0.00647862, None, 2.95183e-05, None, 1.51166, None, 0.00692517, None, 1.51166, None, 0.00692517, None)

reports.append(Report(604018808, ("CSC", 1, 1, 3, 15), "MEp13_15"))
reports[-1].posNum = 19999
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00453947, 0.0157717, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.38812, 0.312278, 0), \
                           ValErr(-0.00460253, 0.00704099, 0), \
                           ValErr(-0.00880571, 0.015344, 0), \
                           ValErr(-0.000143683, 0.000245122, 0), \
                           -36612.1, 19999, 19999, -nan)
reports[-1].sigmaresid = ValErr(1.50948, 0.00754763, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00172438, None, -5.66001e-05, None, 0.00904362, None, -7.86377e-05, None, 0.00904362, None, -7.86377e-05, None, 0.0120036, None, -4.17486e-05, None, 0.0120036, None, -4.17486e-05, None, 1.51172, None, 0.00641034, None, 1.51172, None, 0.00641034, None)

reports.append(Report(604018816, ("CSC", 1, 1, 3, 16), "MEp13_16"))
reports[-1].posNum = 18371
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0100097, 0.0161192, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.74837, 0.33527, 0), \
                           ValErr(-0.00530908, 0.00776907, 0), \
                           ValErr(-0.0260542, 0.015884, 0), \
                           ValErr(0.00020096, 0.00011947, 0), \
                           -33730.4, 18371, 18371, -nan)
reports[-1].sigmaresid = ValErr(1.5176, 0.00784993, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00871205, None, 1.46322e-05, None, 0.00950765, None, -6.48321e-05, None, 0.00950765, None, -6.48321e-05, None, -0.00086999, None, -2.44024e-05, None, -0.00086999, None, -2.44024e-05, None, 1.52051, None, 0.00645408, None, 1.52051, None, 0.00645408, None)

reports.append(Report(604018824, ("CSC", 1, 1, 3, 17), "MEp13_17"))
reports[-1].posNum = 18028
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000861966, 0.0163239, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.18636, 0.331695, 0), \
                           ValErr(-0.00387471, 0.00776992, 0), \
                           ValErr(0.00144677, 0.0160238, 0), \
                           ValErr(-0.000413733, 0.000268201, 0), \
                           -33007, 18028, 18028, -nan)
reports[-1].sigmaresid = ValErr(1.50974, 0.00795081, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0158743, None, 2.49219e-05, None, -0.00365227, None, -0.000128035, None, -0.00365227, None, -0.000128035, None, 0.0272188, None, -0.000130949, None, 0.0272188, None, -0.000130949, None, 1.51372, None, 0.00765923, None, 1.51372, None, 0.00765923, None)

reports.append(Report(604018832, ("CSC", 1, 1, 3, 18), "MEp13_18"))
reports[-1].posNum = 19112
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00227452, 0.0158142, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.29983, 0.308846, 0), \
                           ValErr(-0.0111644, 0.00699053, 0), \
                           ValErr(0.00303195, 0.0151811, 0), \
                           ValErr(2.35728e-05, 0.000248719, 0), \
                           -34693.3, 19112, 19112, -nan)
reports[-1].sigmaresid = ValErr(1.48635, 0.00758872, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00295994, None, -1.57432e-05, None, 0.000786769, None, -3.28016e-05, None, 0.000786769, None, -3.28016e-05, None, -0.00245496, None, 5.69668e-06, None, -0.00245496, None, 5.69668e-06, None, 1.48859, None, 0.00667282, None, 1.48859, None, 0.00667282, None)

reports.append(Report(604018840, ("CSC", 1, 1, 3, 19), "MEp13_19"))
reports[-1].posNum = 20536
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00314644, 0.0135893, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.86843, 0.302972, 0), \
                           ValErr(0.000342035, 0.00506049, 0), \
                           ValErr(-0.00909144, 0.013108, 0), \
                           ValErr(0.000168442, 0.000127255, 0), \
                           -37664.2, 20536, 20536, -nan)
reports[-1].sigmaresid = ValErr(1.51452, 0.00660643, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00156526, None, -1.19026e-05, None, 0.00465631, None, -0.000115924, None, 0.00465631, None, -0.000115924, None, 0.00186438, None, -8.98165e-05, None, 0.00186438, None, -8.98165e-05, None, 1.51778, None, 0.00678453, None, 1.51778, None, 0.00678453, None)

reports.append(Report(604018848, ("CSC", 1, 1, 3, 20), "MEp13_20"))
reports[-1].posNum = 19726
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0109498, 0.015868, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.4817, 0.312827, 0), \
                           ValErr(0.000847973, 0.00713135, 0), \
                           ValErr(-0.014361, 0.015496, 0), \
                           ValErr(-0.00034988, 0.00024933, 0), \
                           -36021.5, 19726, 19726, -nan)
reports[-1].sigmaresid = ValErr(1.50254, 0.00756472, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00539185, None, -3.73347e-05, None, -0.00262612, None, -1.17781e-05, None, -0.00262612, None, -1.17781e-05, None, 0.00775775, None, -1.86919e-05, None, 0.00775775, None, -1.86919e-05, None, 1.50505, None, 0.00636963, None, 1.50505, None, 0.00636963, None)

reports.append(Report(604018856, ("CSC", 1, 1, 3, 21), "MEp13_21"))
reports[-1].posNum = 18052
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0189793, 0.0162608, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.28123, 0.333205, 0), \
                           ValErr(0.00197512, 0.00782989, 0), \
                           ValErr(0.0157454, 0.0159207, 0), \
                           ValErr(-0.000532664, 0.000267393, 0), \
                           -33086.7, 18052, 18052, -nan)
reports[-1].sigmaresid = ValErr(1.51274, 0.00796142, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00789346, None, -2.19623e-05, None, 0.00700422, None, -5.79944e-05, None, 0.00700422, None, -5.79944e-05, None, 0.0230294, None, -9.99594e-05, None, 0.0230294, None, -9.99594e-05, None, 1.51494, None, 0.00638534, None, 1.51494, None, 0.00638534, None)

reports.append(Report(604018864, ("CSC", 1, 1, 3, 22), "MEp13_22"))
reports[-1].posNum = 18897
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0261948, 0.0161541, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.67398, 0.334486, 0), \
                           ValErr(-0.00423854, 0.00770257, 0), \
                           ValErr(-0.0088248, 0.0161926, 0), \
                           ValErr(6.61564e-05, 0.000159379, 0), \
                           -34995.7, 18897, 18897, -nan)
reports[-1].sigmaresid = ValErr(1.54185, 0.00745526, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.020072, None, 1.93456e-05, None, -0.0177679, None, -5.46254e-05, None, -0.0177679, None, -5.46254e-05, None, -0.0206984, None, 1.6419e-05, None, -0.0206984, None, 1.6419e-05, None, 1.54443, None, 0.00671392, None, 1.54443, None, 0.00671392, None)

reports.append(Report(604018872, ("CSC", 1, 1, 3, 23), "MEp13_23"))
reports[-1].posNum = 20570
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0161484, 0.0153913, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.56248, 0.300355, 0), \
                           ValErr(-0.00856642, 0.00658018, 0), \
                           ValErr(-0.0156001, 0.0149999, 0), \
                           ValErr(0.000287712, 0.000150939, 0), \
                           -37500.1, 20570, 20570, -nan)
reports[-1].sigmaresid = ValErr(1.49797, 0.00721786, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00327548, None, -2.40837e-05, None, -0.0039476, None, -4.37607e-05, None, -0.0039476, None, -4.37607e-05, None, -0.0148588, None, 1.32382e-05, None, -0.0148588, None, 1.32382e-05, None, 1.50059, None, 0.00660706, None, 1.50059, None, 0.00660706, None)

reports.append(Report(604018880, ("CSC", 1, 1, 3, 24), "MEp13_24"))
reports[-1].posNum = 20096
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0102653, 0.0153453, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.76491, 0.304239, 0), \
                           ValErr(-0.00129772, 0.00687019, 0), \
                           ValErr(0.0131167, 0.0148675, 0), \
                           ValErr(-9.04081e-05, 0.000241175, 0), \
                           -36398.5, 20096, 20096, -nan)
reports[-1].sigmaresid = ValErr(1.48037, 0.00738418, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00369586, None, -5.99257e-05, None, -0.000549609, None, -4.253e-05, None, -0.000549609, None, -4.253e-05, None, 0.00484223, None, -6.56954e-05, None, 0.00484223, None, -6.56954e-05, None, 1.48345, None, 0.00668603, None, 1.48345, None, 0.00668603, None)

reports.append(Report(604018888, ("CSC", 1, 1, 3, 25), "MEp13_25"))
reports[-1].posNum = 18523
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000195029, 0.0160966, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.27742, 0.318107, 0), \
                           ValErr(0.000566787, 0.00736899, 0), \
                           ValErr(0.0266616, 0.0154014, 0), \
                           ValErr(-0.000200638, 0.000140177, 0), \
                           -33848.5, 18523, 18523, -nan)
reports[-1].sigmaresid = ValErr(1.50447, 0.00728832, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0193329, None, -5.80061e-07, None, -0.0214054, None, -4.73464e-05, None, -0.0214054, None, -4.73464e-05, None, -0.023851, None, 1.94067e-05, None, -0.023851, None, 1.94067e-05, None, 1.50669, None, 0.00687141, None, 1.50669, None, 0.00687141, None)

reports.append(Report(604018896, ("CSC", 1, 1, 3, 26), "MEp13_26"))
reports[-1].posNum = 18508
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0107887, 0.0164454, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.18734, 0.32823, 0), \
                           ValErr(-0.0158873, 0.00766154, 0), \
                           ValErr(0.00283186, 0.0159944, 0), \
                           ValErr(-0.00023344, 0.000265806, 0), \
                           -34086.1, 18508, 18508, -nan)
reports[-1].sigmaresid = ValErr(1.52617, 0.00793251, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0165929, None, -1.37365e-05, None, 0.00839749, None, -0.000115102, None, 0.00839749, None, -0.000115102, None, 0.0181825, None, -0.000184114, None, 0.0181825, None, -0.000184114, None, 1.5281, None, 0.00697461, None, 1.5281, None, 0.00697461, None)

reports.append(Report(604018904, ("CSC", 1, 1, 3, 27), "MEp13_27"))
reports[-1].posNum = 19047
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0188578, 0.0159327, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.51725, 0.317269, 0), \
                           ValErr(-0.00157289, 0.00721909, 0), \
                           ValErr(0.0305011, 0.0153258, 0), \
                           ValErr(-9.80937e-05, 0.00025457, 0), \
                           -34796.4, 19047, 19047, -nan)
reports[-1].sigmaresid = ValErr(1.50371, 0.00770442, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00529837, None, -2.03155e-05, None, -0.00486313, None, -0.000131439, None, -0.00486313, None, -0.000131439, None, -0.00199171, None, -5.06041e-05, None, -0.00199171, None, -5.06041e-05, None, 1.50635, None, 0.0066041, None, 1.50635, None, 0.0066041, None)

reports.append(Report(604018912, ("CSC", 1, 1, 3, 28), "MEp13_28"))
reports[-1].posNum = 19586
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00328276, 0.0157701, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.41332, 0.319364, 0), \
                           ValErr(-0.00514633, 0.00721327, 0), \
                           ValErr(0.0203434, 0.0154457, 0), \
                           ValErr(-0.000101102, 0.000248857, 0), \
                           -35888.6, 19586, 19586, -nan)
reports[-1].sigmaresid = ValErr(1.51199, 0.00763951, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0166332, None, 4.27938e-05, None, -0.0115993, None, -4.62959e-05, None, -0.0115993, None, -4.62959e-05, None, 0.00219458, None, -6.30057e-05, None, 0.00219458, None, -6.30057e-05, None, 1.51648, None, 0.0064146, None, 1.51648, None, 0.0064146, None)

reports.append(Report(604018920, ("CSC", 1, 1, 3, 29), "MEp13_29"))
reports[-1].posNum = 18760
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0531567, 0.0159877, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.12534, 0.308052, 0), \
                           ValErr(-0.0225612, 0.00540796, 0), \
                           ValErr(0.0207481, 0.0155409, 0), \
                           ValErr(-0.000213151, 0.000211507, 0), \
                           -34129.4, 18760, 18760, -nan)
reports[-1].sigmaresid = ValErr(1.49231, 0.007549, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0397967, None, -7.22432e-05, None, 0.0341116, None, -0.000147361, None, 0.0341116, None, -0.000147361, None, 0.0578861, None, -0.00022047, None, 0.0578861, None, -0.00022047, None, 1.49457, None, 0.00681896, None, 1.49457, None, 0.00681896, None)

reports.append(Report(604018928, ("CSC", 1, 1, 3, 30), "MEp13_30"))
reports[-1].posNum = 18435
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00876454, 0.0161986, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.29006, 0.316747, 0), \
                           ValErr(-0.0179923, 0.00733619, 0), \
                           ValErr(-0.00265067, 0.0153686, 0), \
                           ValErr(-8.96243e-05, 0.000261653, 0), \
                           -33685.8, 18435, 18435, -nan)
reports[-1].sigmaresid = ValErr(1.50431, 0.00784575, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0117693, None, 2.09103e-05, None, 0.0110078, None, -5.65164e-05, None, 0.0110078, None, -5.65164e-05, None, -0.000706393, None, -1.70525e-05, None, -0.000706393, None, -1.70525e-05, None, 1.50657, None, 0.00737737, None, 1.50657, None, 0.00737737, None)

reports.append(Report(604018936, ("CSC", 1, 1, 3, 31), "MEp13_31"))
reports[-1].posNum = 18513
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0125509, 0.0162633, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.32165, 0.316683, 0), \
                           ValErr(0.00331429, 0.00719536, 0), \
                           ValErr(-0.0291956, 0.0153957, 0), \
                           ValErr(-0.000146723, 0.000155372, 0), \
                           -34043.6, 18513, 18513, -nan)
reports[-1].sigmaresid = ValErr(1.5219, 0.00762331, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00551024, None, -8.03605e-05, None, 0.0128067, None, -7.04182e-05, None, 0.0128067, None, -7.04182e-05, None, 0.0159159, None, -6.99934e-05, None, 0.0159159, None, -6.99934e-05, None, 1.52656, None, 0.00846528, None, 1.52656, None, 0.00846528, None)

reports.append(Report(604018944, ("CSC", 1, 1, 3, 32), "MEp13_32"))
reports[-1].posNum = 20220
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0280402, 0.014935, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.37074, 0.299865, 0), \
                           ValErr(-0.0117384, 0.00590349, 0), \
                           ValErr(0.00901464, 0.0145805, 0), \
                           ValErr(-2.72154e-05, 0.000111511, 0), \
                           -36729.6, 20220, 20220, -nan)
reports[-1].sigmaresid = ValErr(1.48814, 0.00490913, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0308449, None, -9.56923e-05, None, 0.0200711, None, -0.000155633, None, 0.0200711, None, -0.000155633, None, 0.0297137, None, -0.000129633, None, 0.0297137, None, -0.000129633, None, 1.4905, None, 0.00646255, None, 1.4905, None, 0.00646255, None)

reports.append(Report(604018952, ("CSC", 1, 1, 3, 33), "MEp13_33"))
reports[-1].posNum = 20118
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.004343, 0.0155058, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.46018, 0.307895, 0), \
                           ValErr(-0.00323847, 0.00695157, 0), \
                           ValErr(-0.00632172, 0.0149733, 0), \
                           ValErr(-0.000224403, 0.000243884, 0), \
                           -36680.4, 20118, 20118, -nan)
reports[-1].sigmaresid = ValErr(1.49829, 0.00746467, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00533955, None, -4.5068e-05, None, -0.000296381, None, -7.47209e-05, None, -0.000296381, None, -7.47209e-05, None, -0.00347181, None, 5.1123e-06, None, -0.00347181, None, 5.1123e-06, None, 1.50072, None, 0.00694893, None, 1.50072, None, 0.00694893, None)

reports.append(Report(604018960, ("CSC", 1, 1, 3, 34), "MEp13_34"))
reports[-1].posNum = 19211
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00204708, 0.0159072, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.55064, 0.328972, 0), \
                           ValErr(-0.00536449, 0.00765032, 0), \
                           ValErr(0.00455024, 0.0157026, 0), \
                           ValErr(-0.000308907, 0.000259822, 0), \
                           -35367.9, 19211, 19211, -nan)
reports[-1].sigmaresid = ValErr(1.52514, 0.00778071, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00657852, None, 1.69186e-06, None, -0.00621559, None, -6.1618e-05, None, -0.00621559, None, -6.1618e-05, None, -0.0132125, None, 9.02285e-06, None, -0.0132125, None, 9.02285e-06, None, 1.5276, None, 0.00635483, None, 1.5276, None, 0.00635483, None)

reports.append(Report(604018968, ("CSC", 1, 1, 3, 35), "MEp13_35"))
reports[-1].posNum = 18445
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00036176, 0.0161554, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.12803, 0.333106, 0), \
                           ValErr(-0.0142277, 0.00778771, 0), \
                           ValErr(0.018802, 0.0157258, 0), \
                           ValErr(-0.000580978, 0.000143444, 0), \
                           -33907.3, 18445, 18445, -nan)
reports[-1].sigmaresid = ValErr(1.52099, 0.00727718, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00770941, None, -1.48545e-05, None, -0.0130647, None, -8.22884e-05, None, -0.0130647, None, -8.22884e-05, None, -0.03458, None, -2.86734e-05, None, -0.03458, None, -2.86734e-05, None, 1.52483, None, 0.00722279, None, 1.52483, None, 0.00722279, None)

reports.append(Report(604018976, ("CSC", 1, 1, 3, 36), "MEp13_36"))
reports[-1].posNum = 19306
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-2.27519e-05, 0.0159286, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.3284, 0.310185, 0), \
                           ValErr(0.00594915, 0.00703775, 0), \
                           ValErr(-0.012206, 0.0152014, 0), \
                           ValErr(0.000147161, 0.000250864, 0), \
                           -35291.1, 19306, 19306, -nan)
reports[-1].sigmaresid = ValErr(1.50538, 0.00766101, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0143223, None, -9.92455e-05, None, 0.00986917, None, -8.85355e-05, None, 0.00986917, None, -8.85355e-05, None, 0.00419198, None, -5.29168e-05, None, 0.00419198, None, -5.29168e-05, None, 1.50766, None, 0.00672249, None, 1.50766, None, 0.00672249, None)

reports.append(Report(604017160, ("CSC", 1, 1, 4, 1), "MEp14_01"))
reports[-1].posNum = 101473
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000219393, 0.00081911, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.101135, 0.0495197, 0), \
                           ValErr(0.000991005, 0.00126194, 0), \
                           ValErr(0.0106922, 0.00612715, 0), \
                           ValErr(2.13499e-05, 1.74372e-05, 0), \
                           22641.7, 101473, 101473, -nan)
reports[-1].sigmaresid = ValErr(0.19358, 0.000429705, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000750638, None, -1.50902e-06, None, -0.00104748, None, 8.48321e-06, None, -0.00104748, None, 8.48321e-06, None, -7.60451e-05, None, 7.06637e-06, None, -7.60451e-05, None, 7.06637e-06, None, 0.193592, None, 0.00418802, None, 0.193592, None, 0.00418802, None)

reports.append(Report(604017176, ("CSC", 1, 1, 4, 3), "MEp14_03"))
reports[-1].posNum = 100847
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00201542, 0.000815858, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0414295, 0.0489955, 0), \
                           ValErr(0.000716712, 0.0012535, 0), \
                           ValErr(-0.00317272, 0.00610514, 0), \
                           ValErr(2.25542e-05, 1.72948e-05, 0), \
                           23478.3, 100847, 100847, -nan)
reports[-1].sigmaresid = ValErr(0.191714, 0.000426881, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0015107, None, -4.78122e-07, None, -0.0016483, None, -7.6589e-06, None, -0.0016483, None, -7.6589e-06, None, -0.00148273, None, 7.59367e-06, None, -0.00148273, None, 7.59367e-06, None, 0.191717, None, 0.00431532, None, 0.191717, None, 0.00431532, None)

reports.append(Report(604017192, ("CSC", 1, 1, 4, 5), "MEp14_05"))
reports[-1].posNum = 101454
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00144645, 0.000817606, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0502428, 0.0494603, 0), \
                           ValErr(-0.00119093, 0.00125698, 0), \
                           ValErr(0.00138915, 0.00612451, 0), \
                           ValErr(1.56853e-05, 1.72853e-05, 0), \
                           22789.4, 101454, 101454, -nan)
reports[-1].sigmaresid = ValErr(0.19329, 0.000429101, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00139603, None, -3.03644e-06, None, -0.00150612, None, 5.45039e-06, None, -0.00150612, None, 5.45039e-06, None, -0.00132942, None, 4.96135e-06, None, -0.00132942, None, 4.96135e-06, None, 0.193292, None, 0.00415749, None, 0.193292, None, 0.00415749, None)

reports.append(Report(604017208, ("CSC", 1, 1, 4, 7), "MEp14_07"))
reports[-1].posNum = 101477
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00183764, 0.000818312, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0963453, 0.0492249, 0), \
                           ValErr(-0.0021603, 0.00125583, 0), \
                           ValErr(-0.00215517, 0.00610704, 0), \
                           ValErr(-3.69716e-05, 1.73775e-05, 0), \
                           22874.4, 101477, 101477, -nan)
reports[-1].sigmaresid = ValErr(0.193137, 0.000428714, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0013219, None, -6.15632e-06, None, -0.00178024, None, -1.31228e-06, None, -0.00178024, None, -1.31228e-06, None, -0.00216955, None, 2.55606e-05, None, -0.00216955, None, 2.55606e-05, None, 0.193148, None, 0.00417913, None, 0.193148, None, 0.00417913, None)

reports.append(Report(604017224, ("CSC", 1, 1, 4, 9), "MEp14_09"))
reports[-1].posNum = 101238
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00190882, 0.00081471, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0710842, 0.0490712, 0), \
                           ValErr(-0.00107362, 0.00125289, 0), \
                           ValErr(-0.00194484, 0.0061054, 0), \
                           ValErr(3.51865e-05, 1.72911e-05, 0), \
                           23281.5, 101238, 101238, -nan)
reports[-1].sigmaresid = ValErr(0.19226, 0.000427269, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000640139, None, 5.6391e-06, None, -0.0016079, None, 7.28437e-06, None, -0.0016079, None, 7.28437e-06, None, -0.000228574, None, -2.95149e-05, None, -0.000228574, None, -2.95149e-05, None, 0.192266, None, 0.00415239, None, 0.192266, None, 0.00415239, None)

reports.append(Report(604017240, ("CSC", 1, 1, 4, 11), "MEp14_11"))
reports[-1].posNum = 101432
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000368417, 0.000822012, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.162786, 0.0496057, 0), \
                           ValErr(-0.00154993, 0.00126257, 0), \
                           ValErr(0.0082905, 0.00612746, 0), \
                           ValErr(5.62998e-06, 1.74492e-05, 0), \
                           22220.9, 101432, 101432, -nan)
reports[-1].sigmaresid = ValErr(0.194367, 0.000431539, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00171791, None, -1.31597e-05, None, -0.00105265, None, -3.45026e-05, None, -0.00105265, None, -3.45026e-05, None, -0.00167488, None, -1.16724e-05, None, -0.00167488, None, -1.16724e-05, None, 0.194379, None, 0.00442109, None, 0.194379, None, 0.00442109, None)

reports.append(Report(604017256, ("CSC", 1, 1, 4, 13), "MEp14_13"))
reports[-1].posNum = 101481
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00291607, 0.000815146, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.072233, 0.0489659, 0), \
                           ValErr(-0.000149785, 0.00125173, 0), \
                           ValErr(0.000990833, 0.00609356, 0), \
                           ValErr(7.1984e-06, 1.72861e-05, 0), \
                           23380.7, 101481, 101481, -nan)
reports[-1].sigmaresid = ValErr(0.192178, 0.000426576, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00281117, None, -9.13318e-06, None, -0.00297236, None, -7.21799e-06, None, -0.00297236, None, -7.21799e-06, None, -0.00297302, None, -1.23923e-05, None, -0.00297302, None, -1.23923e-05, None, 0.192181, None, 0.00419137, None, 0.192181, None, 0.00419137, None)

reports.append(Report(604017272, ("CSC", 1, 1, 4, 15), "MEp14_15"))
reports[-1].posNum = 100433
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00218619, 0.00082006, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0644298, 0.0494147, 0), \
                           ValErr(-0.000626725, 0.00125931, 0), \
                           ValErr(-0.00803072, 0.00613083, 0), \
                           ValErr(2.59728e-05, 1.73758e-05, 0), \
                           22852.3, 100433, 100433, -nan)
reports[-1].sigmaresid = ValErr(0.192728, 0.000430023, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00110764, None, 8.21056e-07, None, -0.00139948, None, -1.08533e-05, None, -0.00139948, None, -1.08533e-05, None, -0.000288965, None, -9.37113e-06, None, -0.000288965, None, -9.37113e-06, None, 0.192732, None, 0.00448848, None, 0.192732, None, 0.00448848, None)

reports.append(Report(604017288, ("CSC", 1, 1, 4, 17), "MEp14_17"))
reports[-1].posNum = 101267
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0009627, 0.000812973, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0593736, 0.0490891, 0), \
                           ValErr(-0.000218262, 0.00125068, 0), \
                           ValErr(0.00552189, 0.00612595, 0), \
                           ValErr(-4.65148e-06, 1.72391e-05, 0), \
                           23657.2, 101267, 101267, -nan)
reports[-1].sigmaresid = ValErr(0.191561, 0.000425654, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00215679, None, 4.34365e-06, None, -0.0014474, None, -3.01333e-06, None, -0.0014474, None, -3.01333e-06, None, -0.00129541, None, -1.04058e-05, None, -0.00129541, None, -1.04058e-05, None, 0.191563, None, 0.00420546, None, 0.191563, None, 0.00420546, None)

reports.append(Report(604017304, ("CSC", 1, 1, 4, 19), "MEp14_19"))
reports[-1].posNum = 101464
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00192577, 0.000817183, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0505298, 0.0490643, 0), \
                           ValErr(-0.00175609, 0.00125072, 0), \
                           ValErr(-0.00633575, 0.00612362, 0), \
                           ValErr(-1.76758e-05, 1.73133e-05, 0), \
                           23223.9, 101464, 101464, -nan)
reports[-1].sigmaresid = ValErr(0.192467, 0.000427254, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00139486, None, 1.85382e-06, None, -0.00145572, None, -8.93119e-06, None, -0.00145572, None, -8.93119e-06, None, -0.000747133, None, -2.76467e-05, None, -0.000747133, None, -2.76467e-05, None, 0.192473, None, 0.0042075, None, 0.192473, None, 0.0042075, None)

reports.append(Report(604017320, ("CSC", 1, 1, 4, 21), "MEp14_21"))
reports[-1].posNum = 101189
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00137511, 0.000809382, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0366044, 0.0489749, 0), \
                           ValErr(-0.00112519, 0.001247, 0), \
                           ValErr(0.00588857, 0.00606672, 0), \
                           ValErr(6.86612e-06, 1.7193e-05, 0), \
                           23861, 101189, 101189, -nan)
reports[-1].sigmaresid = ValErr(0.191141, 0.000424885, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00146556, None, 8.13478e-06, None, -0.00184821, None, -1.56316e-05, None, -0.00184821, None, -1.56316e-05, None, -0.00348723, None, -2.34493e-05, None, -0.00348723, None, -2.34493e-05, None, 0.191143, None, 0.00425097, None, 0.191143, None, 0.00425097, None)

reports.append(Report(604017336, ("CSC", 1, 1, 4, 23), "MEp14_23"))
reports[-1].posNum = 101254
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00237674, 0.000820227, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0674304, 0.0494529, 0), \
                           ValErr(0.000959941, 0.00126157, 0), \
                           ValErr(0.00139101, 0.00616842, 0), \
                           ValErr(2.91532e-05, 1.73646e-05, 0), \
                           22604.4, 101254, 101254, -nan)
reports[-1].sigmaresid = ValErr(0.193557, 0.000430119, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00167942, None, 6.41598e-06, None, -0.00238147, None, 2.52873e-06, None, -0.00238147, None, 2.52873e-06, None, -0.00188391, None, -7.41874e-06, None, -0.00188391, None, -7.41874e-06, None, 0.193564, None, 0.00472597, None, 0.193564, None, 0.00472597, None)

reports.append(Report(604017352, ("CSC", 1, 1, 4, 25), "MEp14_25"))
reports[-1].posNum = 101182
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00225629, 0.000819165, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0509614, 0.049184, 0), \
                           ValErr(-0.000675535, 0.001253, 0), \
                           ValErr(0.00108255, 0.00611861, 0), \
                           ValErr(2.82086e-05, 1.73584e-05, 0), \
                           22933.6, 101182, 101182, -nan)
reports[-1].sigmaresid = ValErr(0.192898, 0.000428806, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00132021, None, 8.00835e-06, None, -0.00224931, None, 2.43471e-06, None, -0.00224931, None, 2.43471e-06, None, 0.000880608, None, -1.50553e-05, None, 0.000880608, None, -1.50553e-05, None, 0.192902, None, 0.00471814, None, 0.192902, None, 0.00471814, None)

reports.append(Report(604017368, ("CSC", 1, 1, 4, 27), "MEp14_27"))
reports[-1].posNum = 101538
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00196712, 0.000812645, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0744158, 0.0491101, 0), \
                           ValErr(-0.00305828, 0.00125139, 0), \
                           ValErr(-0.0052241, 0.00610539, 0), \
                           ValErr(-2.49663e-06, 1.72239e-05, 0), \
                           23307.2, 101538, 101538, -nan)
reports[-1].sigmaresid = ValErr(0.192342, 0.00042682, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00149264, None, 8.10008e-06, None, -0.00154869, None, -9.23058e-06, None, -0.00154869, None, -9.23058e-06, None, -0.001737, None, -1.89653e-05, None, -0.001737, None, -1.89653e-05, None, 0.192349, None, 0.00416715, None, 0.192349, None, 0.00416715, None)

reports.append(Report(604017384, ("CSC", 1, 1, 4, 29), "MEp14_29"))
reports[-1].posNum = 100725
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00401536, 0.000821628, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.152965, 0.0494833, 0), \
                           ValErr(-0.00193956, 0.00127256, 0), \
                           ValErr(-0.000902352, 0.00617621, 0), \
                           ValErr(9.68825e-06, 1.74046e-05, 0), \
                           22698.9, 100725, 100725, -nan)
reports[-1].sigmaresid = ValErr(0.193149, 0.000430337, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00443628, None, 1.50487e-05, None, -0.00389988, None, 1.63612e-05, None, -0.00389988, None, 1.63612e-05, None, -0.00280161, None, 1.55939e-05, None, -0.00280161, None, 1.55939e-05, None, 0.193159, None, 0.00418779, None, 0.193159, None, 0.00418779, None)

reports.append(Report(604017400, ("CSC", 1, 1, 4, 31), "MEp14_31"))
reports[-1].posNum = 101037
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00159162, 0.000816046, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0810032, 0.0494222, 0), \
                           ValErr(-0.00275479, 0.00126042, 0), \
                           ValErr(-0.0102742, 0.00612203, 0), \
                           ValErr(-1.35501e-05, 1.73169e-05, 0), \
                           22861.3, 101037, 101037, -nan)
reports[-1].sigmaresid = ValErr(0.192973, 0.00042928, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00116551, None, -4.11089e-06, None, -0.000771488, None, -5.51714e-06, None, -0.000771488, None, -5.51714e-06, None, -0.000579069, None, -1.55029e-05, None, -0.000579069, None, -1.55029e-05, None, 0.192983, None, 0.00411683, None, 0.192983, None, 0.00411683, None)

reports.append(Report(604017416, ("CSC", 1, 1, 4, 33), "MEp14_33"))
reports[-1].posNum = 101187
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00142131, 0.000823769, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0963502, 0.0494342, 0), \
                           ValErr(-0.00272424, 0.00126664, 0), \
                           ValErr(0.00309804, 0.00617359, 0), \
                           ValErr(-2.84331e-06, 1.74565e-05, 0), \
                           22350.5, 101187, 101187, -nan)
reports[-1].sigmaresid = ValErr(0.194015, 0.000431278, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00194115, None, -4.62772e-06, None, -0.00170781, None, -1.31994e-05, None, -0.00170781, None, -1.31994e-05, None, 0.00103098, None, -2.23113e-05, None, 0.00103098, None, -2.23113e-05, None, 0.194021, None, 0.00436928, None, 0.194021, None, 0.00436928, None)

reports.append(Report(604017432, ("CSC", 1, 1, 4, 35), "MEp14_35"))
reports[-1].posNum = 101272
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00136523, 0.000810555, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0707279, 0.0487848, 0), \
                           ValErr(0.00139351, 0.00124234, 0), \
                           ValErr(0.00420634, 0.00603494, 0), \
                           ValErr(-1.28575e-06, 1.72403e-05, 0), \
                           23888.2, 101272, 101272, -nan)
reports[-1].sigmaresid = ValErr(0.191126, 0.000424679, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00176524, None, -1.15569e-06, None, -0.00172635, None, -4.40746e-06, None, -0.00172635, None, -4.40746e-06, None, -0.00190518, None, -1.40494e-05, None, -0.00190518, None, -1.40494e-05, None, 0.191132, None, 0.00422688, None, 0.191132, None, 0.00422688, None)

reports.append(Report(604017168, ("CSC", 1, 1, 4, 2), "MEp14_02"))
reports[-1].posNum = 100251
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000643799, 0.000737362, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0784317, 0.0419354, 0), \
                           ValErr(0.000372984, 0.00107269, 0), \
                           ValErr(0.000429221, 0.00521242, 0), \
                           ValErr(-1.26878e-05, 1.56171e-05, 0), \
                           33687.2, 100251, 100251, -nan)
reports[-1].sigmaresid = ValErr(0.172913, 0.000386159, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000434499, None, 8.98289e-06, None, -0.000728694, None, 4.65778e-05, None, -0.000728694, None, 4.65778e-05, None, -0.000358011, None, 4.10868e-05, None, -0.000358011, None, 4.10868e-05, None, 0.172918, None, 0.00444122, None, 0.172918, None, 0.00444122, None)

reports.append(Report(604017184, ("CSC", 1, 1, 4, 4), "MEp14_04"))
reports[-1].posNum = 100406
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00190121, 0.000730696, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.114609, 0.0417795, 0), \
                           ValErr(-0.00119148, 0.00106848, 0), \
                           ValErr(-0.00924577, 0.00518774, 0), \
                           ValErr(2.1953e-05, 1.54792e-05, 0), \
                           34308.7, 100406, 100406, -nan)
reports[-1].sigmaresid = ValErr(0.171935, 0.00038368, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000647152, None, -6.17676e-06, None, -0.000986836, None, -1.544e-05, None, -0.000986836, None, -1.544e-05, None, 0.000348507, None, -3.09724e-05, None, 0.000348507, None, -3.09724e-05, None, 0.171945, None, 0.00530762, None, 0.171945, None, 0.00530762, None)

reports.append(Report(604017200, ("CSC", 1, 1, 4, 6), "MEp14_06"))
reports[-1].posNum = 100408
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00178087, 0.000735781, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0311483, 0.0419779, 0), \
                           ValErr(-0.00037317, 0.00107853, 0), \
                           ValErr(-0.00220048, 0.00521113, 0), \
                           ValErr(-5.50234e-06, 1.56572e-05, 0), \
                           33626, 100408, 100408, -nan)
reports[-1].sigmaresid = ValErr(0.173109, 0.000386297, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00173286, None, 7.1568e-06, None, -0.00160341, None, 2.87334e-05, None, -0.00160341, None, 2.87334e-05, None, -0.00166411, None, 3.33258e-05, None, -0.00166411, None, 3.33258e-05, None, 0.17311, None, 0.00439007, None, 0.17311, None, 0.00439007, None)

reports.append(Report(604017216, ("CSC", 1, 1, 4, 8), "MEp14_08"))
reports[-1].posNum = 99540
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0006633, 0.000736737, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0427329, 0.0419631, 0), \
                           ValErr(-0.00113948, 0.00107492, 0), \
                           ValErr(0.00206078, 0.00524648, 0), \
                           ValErr(-1.55872e-06, 1.55868e-05, 0), \
                           33909.1, 99540, 99540, -nan)
reports[-1].sigmaresid = ValErr(0.172114, 0.000385748, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000277495, None, -3.12312e-07, None, -0.000854348, None, -7.90807e-07, None, -0.000854348, None, -7.90807e-07, None, 0.000681902, None, -1.02321e-05, None, 0.000681902, None, -1.02321e-05, None, 0.172116, None, 0.00441092, None, 0.172116, None, 0.00441092, None)

reports.append(Report(604017232, ("CSC", 1, 1, 4, 10), "MEp14_10"))
reports[-1].posNum = 100381
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000149243, 0.000737761, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.104502, 0.042029, 0), \
                           ValErr(-2.44443e-05, 0.00107704, 0), \
                           ValErr(0.00458461, 0.00522043, 0), \
                           ValErr(2.80798e-06, 1.56334e-05, 0), \
                           33506.5, 100381, 100381, -nan)
reports[-1].sigmaresid = ValErr(0.1733, 0.000386772, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000660874, None, 3.97244e-06, None, -0.000547997, None, 2.07619e-05, None, -0.000547997, None, 2.07619e-05, None, 0.000409112, None, -3.33032e-06, None, 0.000409112, None, -3.33032e-06, None, 0.173307, None, 0.00437894, None, 0.173307, None, 0.00437894, None)

reports.append(Report(604017248, ("CSC", 1, 1, 4, 12), "MEp14_12"))
reports[-1].posNum = 100375
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00219841, 0.000729037, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0635088, 0.0417751, 0), \
                           ValErr(-0.000586129, 0.00106812, 0), \
                           ValErr(-0.00589461, 0.00521669, 0), \
                           ValErr(2.65485e-07, 1.54272e-05, 0), \
                           34410.3, 100375, 100375, -nan)
reports[-1].sigmaresid = ValErr(0.171743, 0.000383311, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00172477, None, 9.1983e-06, None, -0.0016697, None, 2.24098e-05, None, -0.0016697, None, 2.24098e-05, None, -0.00179143, None, 3.47059e-06, None, -0.00179143, None, 3.47059e-06, None, 0.171746, None, 0.00435151, None, 0.171746, None, 0.00435151, None)

reports.append(Report(604017264, ("CSC", 1, 1, 4, 14), "MEp14_14"))
reports[-1].posNum = 99966
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000122489, 0.00073558, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.10617, 0.0419171, 0), \
                           ValErr(0.00101388, 0.00107465, 0), \
                           ValErr(0.00646178, 0.00524181, 0), \
                           ValErr(8.41787e-07, 1.55668e-05, 0), \
                           33894.7, 99966, 99966, -nan)
reports[-1].sigmaresid = ValErr(0.172389, 0.00038554, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00100522, None, -2.58839e-06, None, -0.000450258, None, -7.71508e-07, None, -0.000450258, None, -7.71508e-07, None, -1.22154e-05, None, -4.4134e-06, None, -1.22154e-05, None, -4.4134e-06, None, 0.1724, None, 0.00528261, None, 0.1724, None, 0.00528261, None)

reports.append(Report(604017280, ("CSC", 1, 1, 4, 16), "MEp14_16"))
reports[-1].posNum = 99606
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00339459, 0.000733612, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.119025, 0.0421641, 0), \
                           ValErr(-0.00339399, 0.00108076, 0), \
                           ValErr(-0.00296371, 0.00523037, 0), \
                           ValErr(1.05065e-05, 1.55961e-05, 0), \
                           33763.5, 99606, 99606, -nan)
reports[-1].sigmaresid = ValErr(0.172405, 0.000386271, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00262873, None, 2.09807e-05, None, -0.00309858, None, 4.06927e-05, None, -0.00309858, None, 4.06927e-05, None, -0.00401907, None, 3.55683e-05, None, -0.00401907, None, 3.55683e-05, None, 0.172417, None, 0.00463712, None, 0.172417, None, 0.00463712, None)

reports.append(Report(604017296, ("CSC", 1, 1, 4, 18), "MEp14_18"))
reports[-1].posNum = 100398
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00153083, 0.000732415, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.106457, 0.0418692, 0), \
                           ValErr(8.18485e-05, 0.00107054, 0), \
                           ValErr(-0.00252655, 0.00520724, 0), \
                           ValErr(1.04388e-05, 1.55584e-05, 0), \
                           34116.7, 100398, 100398, -nan)
reports[-1].sigmaresid = ValErr(0.17226, 0.00038442, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00124331, None, 1.64535e-05, None, -0.0012664, None, 3.7025e-05, None, -0.0012664, None, 3.7025e-05, None, -0.00106156, None, 3.20033e-05, None, -0.00106156, None, 3.20033e-05, None, 0.172267, None, 0.00450037, None, 0.172267, None, 0.00450037, None)

reports.append(Report(604017312, ("CSC", 1, 1, 4, 20), "MEp14_20"))
reports[-1].posNum = 100418
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00094979, 0.000734084, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0923013, 0.0418784, 0), \
                           ValErr(-0.00189071, 0.00106843, 0), \
                           ValErr(0.0100998, 0.00522845, 0), \
                           ValErr(2.63737e-05, 1.55695e-05, 0), \
                           34097.5, 100418, 100418, -nan)
reports[-1].sigmaresid = ValErr(0.172304, 0.000384481, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00148606, None, 2.16068e-05, None, -0.00175675, None, 2.83505e-05, None, -0.00175675, None, 2.83505e-05, None, -0.00192126, None, 3.91948e-05, None, -0.00192126, None, 3.91948e-05, None, 0.172318, None, 0.00453837, None, 0.172318, None, 0.00453837, None)

reports.append(Report(604017328, ("CSC", 1, 1, 4, 22), "MEp14_22"))
reports[-1].posNum = 99616
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00259433, 0.000735111, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0990083, 0.0417383, 0), \
                           ValErr(-0.00131768, 0.00106975, 0), \
                           ValErr(-0.00449666, 0.00522133, 0), \
                           ValErr(-8.64086e-06, 1.55864e-05, 0), \
                           34175.6, 99616, 99616, -nan)
reports[-1].sigmaresid = ValErr(0.171699, 0.000384669, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00245026, None, 1.40057e-05, None, -0.00223638, None, -1.56769e-05, None, -0.00223638, None, -1.56769e-05, None, -0.00222494, None, 1.10711e-05, None, -0.00222494, None, 1.10711e-05, None, 0.171705, None, 0.00473029, None, 0.171705, None, 0.00473029, None)

reports.append(Report(604017344, ("CSC", 1, 1, 4, 24), "MEp14_24"))
reports[-1].posNum = 99806
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00322363, 0.000735911, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0450336, 0.0421246, 0), \
                           ValErr(-0.00153192, 0.00107065, 0), \
                           ValErr(-0.00579038, 0.00521608, 0), \
                           ValErr(-9.19233e-06, 1.56229e-05, 0), \
                           33740.7, 99806, 99806, -nan)
reports[-1].sigmaresid = ValErr(0.172561, 0.000386234, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00221784, None, 1.65922e-05, None, -0.00274452, None, 3.07226e-05, None, -0.00274452, None, 3.07226e-05, None, -0.00170513, None, 2.14579e-05, None, -0.00170513, None, 2.14579e-05, None, 0.172566, None, 0.00458602, None, 0.172566, None, 0.00458602, None)

reports.append(Report(604017360, ("CSC", 1, 1, 4, 26), "MEp14_26"))
reports[-1].posNum = 100062
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000806137, 0.000732999, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0965226, 0.0420371, 0), \
                           ValErr(0.00289606, 0.00107318, 0), \
                           ValErr(0.00381688, 0.00522065, 0), \
                           ValErr(-4.97033e-06, 1.55812e-05, 0), \
                           33871.5, 100062, 100062, -nan)
reports[-1].sigmaresid = ValErr(0.172485, 0.000385569, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00113918, None, 5.80901e-07, None, -0.00116033, None, 3.68442e-05, None, -0.00116033, None, 3.68442e-05, None, -0.00110124, None, 1.11483e-05, None, -0.00110124, None, 1.11483e-05, None, 0.172503, None, 0.00501857, None, 0.172503, None, 0.00501857, None)

reports.append(Report(604017376, ("CSC", 1, 1, 4, 28), "MEp14_28"))
reports[-1].posNum = 99589
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000505133, 0.000742429, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0865749, 0.042372, 0), \
                           ValErr(-0.00138593, 0.00108493, 0), \
                           ValErr(-0.00136504, 0.00528348, 0), \
                           ValErr(-1.76865e-05, 1.57055e-05, 0), \
                           33059.2, 99589, 99589, -nan)
reports[-1].sigmaresid = ValErr(0.173618, 0.000389023, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000380554, None, 7.82136e-06, None, -0.000461479, None, 2.09842e-05, None, -0.000461479, None, 2.09842e-05, None, -0.00160891, None, 1.69338e-05, None, -0.00160891, None, 1.69338e-05, None, 0.173624, None, 0.00435308, None, 0.173624, None, 0.00435308, None)

reports.append(Report(604017392, ("CSC", 1, 1, 4, 30), "MEp14_30"))
reports[-1].posNum = 99352
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00110743, 0.000732957, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.140784, 0.0420875, 0), \
                           ValErr(0.000398134, 0.00107466, 0), \
                           ValErr(0.00072971, 0.00520341, 0), \
                           ValErr(-2.13848e-06, 1.56096e-05, 0), \
                           33955.4, 99352, 99352, -nan)
reports[-1].sigmaresid = ValErr(0.171923, 0.000385684, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00124521, None, 1.10679e-06, None, -0.00119652, None, 1.75386e-05, None, -0.00119652, None, 1.75386e-05, None, -0.000605826, None, -4.30094e-06, None, -0.000605826, None, -4.30094e-06, None, 0.171936, None, 0.00462482, None, 0.171936, None, 0.00462482, None)

reports.append(Report(604017408, ("CSC", 1, 1, 4, 32), "MEp14_32"))
reports[-1].posNum = 100127
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00335831, 0.000737427, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0894799, 0.0421618, 0), \
                           ValErr(-0.000638131, 0.00107606, 0), \
                           ValErr(-0.0143538, 0.00522319, 0), \
                           ValErr(2.85176e-05, 1.67413e-05, 0), \
                           33706.5, 100127, 100127, -nan)
reports[-1].sigmaresid = ValErr(0.172808, 0.000386182, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00156909, None, 1.3964e-05, None, -0.00196999, None, 3.63584e-05, None, -0.00196999, None, 3.63584e-05, None, -0.000352719, None, 2.66603e-05, None, -0.000352719, None, 2.66603e-05, None, 0.172819, None, 0.00431509, None, 0.172819, None, 0.00431509, None)

reports.append(Report(604017424, ("CSC", 1, 1, 4, 34), "MEp14_34"))
reports[-1].posNum = 92800
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00261991, 0.000777268, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0886291, 0.0430005, 0), \
                           ValErr(2.13288e-05, 0.00109222, 0), \
                           ValErr(-0.00871394, 0.00536002, 0), \
                           ValErr(3.78152e-06, 1.76682e-05, 0), \
                           31929, 92800, 92800, -nan)
reports[-1].sigmaresid = ValErr(0.171529, 0.000397941, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00236407, None, -3.4075e-05, None, -0.00185097, None, -8.07922e-05, None, -0.00185097, None, -8.07922e-05, None, -0.000765956, None, -4.33289e-05, None, -0.000765956, None, -4.33289e-05, None, 0.171536, None, 0.00559274, None, 0.171536, None, 0.00559274, None)

reports.append(Report(604017440, ("CSC", 1, 1, 4, 36), "MEp14_36"))
reports[-1].posNum = 100432
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00240483, 0.000734633, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.142671, 0.0418102, 0), \
                           ValErr(-0.00042909, 0.00107036, 0), \
                           ValErr(0.0064853, 0.005231, 0), \
                           ValErr(1.30481e-05, 1.55746e-05, 0), \
                           33991.4, 100432, 100432, -nan)
reports[-1].sigmaresid = ValErr(0.172494, 0.000384879, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00307017, None, 1.29217e-05, None, -0.00293758, None, 6.05114e-05, None, -0.00293758, None, 6.05114e-05, None, -0.00279766, None, 4.21445e-05, None, -0.00279766, None, 4.21445e-05, None, 0.172508, None, 0.00522889, None, 0.172508, None, 0.00522889, None)

reports.append(Report(604021256, ("CSC", 1, 2, 1, 1), "MEp21_01"))
reports[-1].posNum = 209491
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000848464, 0.00137006, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0123968, 0.0359251, 0), \
                           ValErr(0.00152179, 0.000709456, 0), \
                           ValErr(-0.000207688, 0.00165055, 0), \
                           ValErr(1.65936e-05, 2.02443e-05, 0), \
                           -114770, 209491, 209491, -nan)
reports[-1].sigmaresid = ValErr(0.418497, 0.000646539, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0010372, None, 1.05316e-05, None, -0.000579516, None, 2.48279e-05, None, -0.000579516, None, 2.48279e-05, None, 0.000290207, None, 1.16845e-05, None, 0.000290207, None, 1.16845e-05, None, 0.418503, None, 0.00546389, None, 0.418503, None, 0.00546389, None)

reports.append(Report(604021272, ("CSC", 1, 2, 1, 3), "MEp21_03"))
reports[-1].posNum = 210210
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000902371, 0.00136688, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.018838, 0.0358609, 0), \
                           ValErr(0.000345439, 0.000705534, 0), \
                           ValErr(9.623e-05, 0.00164921, 0), \
                           ValErr(2.14929e-05, 2.01351e-05, 0), \
                           -114985, 210210, 210210, -nan)
reports[-1].sigmaresid = ValErr(0.418141, 0.000644884, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000683299, None, 2.04376e-05, None, -0.000759727, None, 3.10847e-05, None, -0.000759727, None, 3.10847e-05, None, -0.000777003, None, 1.65854e-05, None, -0.000777003, None, 1.65854e-05, None, 0.418143, None, 0.00557321, None, 0.418143, None, 0.00557321, None)

reports.append(Report(604021288, ("CSC", 1, 2, 1, 5), "MEp21_05"))
reports[-1].posNum = 210800
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0021369, 0.00136627, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0637008, 0.035773, 0), \
                           ValErr(0.00193633, 0.00070585, 0), \
                           ValErr(0.00255279, 0.00164592, 0), \
                           ValErr(-9.93091e-06, 2.01637e-05, 0), \
                           -115284, 210800, 210800, -nan)
reports[-1].sigmaresid = ValErr(0.418094, 0.000643907, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00113534, None, -2.01179e-05, None, 0.000596507, None, 6.38971e-06, None, 0.000596507, None, 6.38971e-06, None, 0.00149315, None, -6.4174e-06, None, 0.00149315, None, -6.4174e-06, None, 0.418109, None, 0.0057051, None, 0.418109, None, 0.0057051, None)

reports.append(Report(604021304, ("CSC", 1, 2, 1, 7), "MEp21_07"))
reports[-1].posNum = 209586
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00280247, 0.00136739, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.028218, 0.0357355, 0), \
                           ValErr(0.00017473, 0.000773403, 0), \
                           ValErr(-0.000795658, 0.00165145, 0), \
                           ValErr(3.63959e-05, 2.17738e-05, 0), \
                           -113661, 209586, 209586, -nan)
reports[-1].sigmaresid = ValErr(0.416184, 0.000653188, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00143112, None, 1.64799e-05, None, -0.00200874, None, 3.87098e-05, None, -0.00200874, None, 3.87098e-05, None, -0.00130499, None, 1.60347e-05, None, -0.00130499, None, 1.60347e-05, None, 0.416189, None, 0.00568078, None, 0.416189, None, 0.00568078, None)

reports.append(Report(604021320, ("CSC", 1, 2, 1, 9), "MEp21_09"))
reports[-1].posNum = 209680
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00167391, 0.00135503, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0156488, 0.0355002, 0), \
                           ValErr(-0.000358908, 0.000699928, 0), \
                           ValErr(0.000916033, 0.00163163, 0), \
                           ValErr(2.5599e-05, 1.99812e-05, 0), \
                           -112459, 209680, 209680, -nan)
reports[-1].sigmaresid = ValErr(0.413704, 0.000638846, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00295638, None, 1.69899e-05, None, -0.00195996, None, 1.47021e-05, None, -0.00195996, None, 1.47021e-05, None, -0.00109087, None, 9.00691e-06, None, -0.00109087, None, 9.00691e-06, None, 0.413708, None, 0.00558389, None, 0.413708, None, 0.00558389, None)

reports.append(Report(604021336, ("CSC", 1, 2, 1, 11), "MEp21_11"))
reports[-1].posNum = 210075
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00141594, 0.00135514, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0420953, 0.0368877, 0), \
                           ValErr(0.000363531, 0.000764755, 0), \
                           ValErr(-0.00219093, 0.00163491, 0), \
                           ValErr(-2.46605e-05, 2.04998e-05, 0), \
                           -113035, 210075, 210075, -nan)
reports[-1].sigmaresid = ValErr(0.414423, 0.000697164, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000789685, None, -4.36859e-07, None, -0.000410753, None, 2.5865e-05, None, -0.000410753, None, 2.5865e-05, None, -0.00166173, None, -4.41586e-06, None, -0.00166173, None, -4.41586e-06, None, 0.41443, None, 0.00565205, None, 0.41443, None, 0.00565205, None)

reports.append(Report(604021352, ("CSC", 1, 2, 1, 13), "MEp21_13"))
reports[-1].posNum = 209146
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00112043, 0.00136315, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0198856, 0.0357033, 0), \
                           ValErr(0.000432456, 0.000706043, 0), \
                           ValErr(0.00173625, 0.00164718, 0), \
                           ValErr(-1.55785e-07, 2.01015e-05, 0), \
                           -112825, 209146, 209146, -nan)
reports[-1].sigmaresid = ValErr(0.414998, 0.000641662, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00180608, None, 4.3225e-07, None, -0.00210053, None, 1.70201e-05, None, -0.00210053, None, 1.70201e-05, None, -0.000954364, None, -1.49984e-06, None, -0.000954364, None, -1.49984e-06, None, 0.415, None, 0.00563838, None, 0.415, None, 0.00563838, None)

reports.append(Report(604021368, ("CSC", 1, 2, 1, 15), "MEp21_15"))
reports[-1].posNum = 209138
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0022162, 0.00135972, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0757333, 0.0357773, 0), \
                           ValErr(0.000820098, 0.000707439, 0), \
                           ValErr(5.22992e-05, 0.00164641, 0), \
                           ValErr(-1.42281e-05, 2.00862e-05, 0), \
                           -112982, 209138, 209138, -nan)
reports[-1].sigmaresid = ValErr(0.415318, 0.000642168, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00297762, None, 2.29887e-05, None, -0.00237274, None, 4.66745e-05, None, -0.00237274, None, 4.66745e-05, None, -0.00146942, None, 7.26694e-06, None, -0.00146942, None, 7.26694e-06, None, 0.415326, None, 0.00572077, None, 0.415326, None, 0.00572077, None)

reports.append(Report(604021384, ("CSC", 1, 2, 1, 17), "MEp21_17"))
reports[-1].posNum = 209308
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00013301, 0.00137448, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0356988, 0.0358932, 0), \
                           ValErr(0.000627772, 0.000708736, 0), \
                           ValErr(-0.00108875, 0.00165869, 0), \
                           ValErr(1.13034e-05, 2.02587e-05, 0), \
                           -114486, 209308, 209308, -nan)
reports[-1].sigmaresid = ValErr(0.41813, 0.000646255, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00012705, None, 8.65534e-06, None, 0.000583725, None, 1.48903e-05, None, 0.000583725, None, 1.48903e-05, None, 0.00225362, None, 6.47335e-06, None, 0.00225362, None, 6.47335e-06, None, 0.418133, None, 0.00553974, None, 0.418133, None, 0.00553974, None)

reports.append(Report(604021264, ("CSC", 1, 2, 1, 2), "MEp21_02"))
reports[-1].posNum = 209328
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000966255, 0.00130135, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0193892, 0.0337766, 0), \
                           ValErr(-0.000250276, 0.000682569, 0), \
                           ValErr(-0.00338794, 0.00153058, 0), \
                           ValErr(2.16121e-05, 2.24736e-05, 0), \
                           -101987, 209328, 209328, -nan)
reports[-1].sigmaresid = ValErr(0.393872, 0.000619658, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000613472, None, -1.0803e-05, None, 0.00121012, None, 1.80564e-06, None, 0.00121012, None, 1.80564e-06, None, 0.00193652, None, -1.4619e-05, None, 0.00193652, None, -1.4619e-05, None, 0.393877, None, 0.00614677, None, 0.393877, None, 0.00614677, None)

reports.append(Report(604021280, ("CSC", 1, 2, 1, 4), "MEp21_04"))
reports[-1].posNum = 208934
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00304088, 0.00130391, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.00922465, 0.0329901, 0), \
                           ValErr(-0.000231657, 0.000649499, 0), \
                           ValErr(0.00229392, 0.00152125, 0), \
                           ValErr(-2.52108e-05, 1.91599e-05, 0), \
                           -102654, 208934, 208934, -nan)
reports[-1].sigmaresid = ValErr(0.395496, 0.000611818, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00183673, None, 3.19984e-06, None, 0.00145823, None, -8.37048e-06, None, 0.00145823, None, -8.37048e-06, None, 0.000921835, None, -2.27188e-05, None, 0.000921835, None, -2.27188e-05, None, 0.395498, None, 0.00598472, None, 0.395498, None, 0.00598472, None)

reports.append(Report(604021296, ("CSC", 1, 2, 1, 6), "MEp21_06"))
reports[-1].posNum = 208688
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00110736, 0.00130345, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0214508, 0.0387066, 0), \
                           ValErr(0.000438626, 0.000757018, 0), \
                           ValErr(0.000258546, 0.00152403, 0), \
                           ValErr(-1.60029e-05, 1.91533e-05, 0), \
                           -102374, 208688, 208688, -nan)
reports[-1].sigmaresid = ValErr(0.395194, 0.000619989, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000996874, None, 1.03552e-05, None, 0.000797672, None, 1.52807e-05, None, 0.000797672, None, 1.52807e-05, None, 0.00122829, None, 1.31273e-06, None, 0.00122829, None, 1.31273e-06, None, 0.395196, None, 0.0060623, None, 0.395196, None, 0.0060623, None)

reports.append(Report(604021312, ("CSC", 1, 2, 1, 8), "MEp21_08"))
reports[-1].posNum = 208559
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00374076, 0.00130362, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0377446, 0.0362969, 0), \
                           ValErr(0.000563484, 0.00075844, 0), \
                           ValErr(-0.00241621, 0.00153307, 0), \
                           ValErr(4.28529e-05, 2.01714e-05, 0), \
                           -102291, 208559, 208559, -nan)
reports[-1].sigmaresid = ValErr(0.395157, 0.00062012, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00165218, None, -6.18546e-06, None, -0.00192686, None, 1.10562e-05, None, -0.00192686, None, 1.10562e-05, None, -0.000383637, None, -1.37518e-05, None, -0.000383637, None, -1.37518e-05, None, 0.395164, None, 0.00607013, None, 0.395164, None, 0.00607013, None)

reports.append(Report(604021328, ("CSC", 1, 2, 1, 10), "MEp21_10"))
reports[-1].posNum = 209483
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000658373, 0.00130514, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0118317, 0.0331497, 0), \
                           ValErr(-0.000884548, 0.000651854, 0), \
                           ValErr(0.00183908, 0.00152931, 0), \
                           ValErr(-5.87523e-06, 1.91927e-05, 0), \
                           -103799, 209483, 209483, -nan)
reports[-1].sigmaresid = ValErr(0.397152, 0.000613575, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000262549, None, -5.20589e-06, None, -0.00046031, None, 1.46468e-05, None, -0.00046031, None, 1.46468e-05, None, -5.93465e-06, None, 5.81377e-06, None, -5.93465e-06, None, 5.81377e-06, None, 0.397156, None, 0.00610652, None, 0.397156, None, 0.00610652, None)

reports.append(Report(604021344, ("CSC", 1, 2, 1, 12), "MEp21_12"))
reports[-1].posNum = 209449
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.001512, 0.00130868, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00823259, 0.0330514, 0), \
                           ValErr(0.000225852, 0.000650289, 0), \
                           ValErr(0.00190761, 0.00152619, 0), \
                           ValErr(3.39869e-07, 1.92095e-05, 0), \
                           -103799, 209449, 209449, -nan)
reports[-1].sigmaresid = ValErr(0.397183, 0.000613672, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00211592, None, 2.48478e-05, None, -0.00261639, None, 5.89578e-05, None, -0.00261639, None, 5.89578e-05, None, -0.000235888, None, 2.93038e-05, None, -0.000235888, None, 2.93038e-05, None, 0.397184, None, 0.00598271, None, 0.397184, None, 0.00598271, None)

reports.append(Report(604021360, ("CSC", 1, 2, 1, 14), "MEp21_14"))
reports[-1].posNum = 210181
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000604679, 0.00130373, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00738782, 0.0354957, 0), \
                           ValErr(-0.000156825, 0.000694059, 0), \
                           ValErr(-0.00109913, 0.00152436, 0), \
                           ValErr(-2.92954e-05, 1.91276e-05, 0), \
                           -104037, 210181, 210181, -nan)
reports[-1].sigmaresid = ValErr(0.396948, 0.000619435, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000360684, None, -4.25083e-06, None, 0.000957152, None, 3.96583e-05, None, 0.000957152, None, 3.96583e-05, None, 0.00208173, None, 2.17447e-05, None, 0.00208173, None, 2.17447e-05, None, 0.396952, None, 0.00604955, None, 0.396952, None, 0.00604955, None)

reports.append(Report(604021376, ("CSC", 1, 2, 1, 16), "MEp21_16"))
reports[-1].posNum = 209726
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000348286, 0.00131132, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.00364194, 0.0331306, 0), \
                           ValErr(-0.00155546, 0.000651463, 0), \
                           ValErr(0.00030956, 0.0015321, 0), \
                           ValErr(-9.20834e-06, 1.92277e-05, 0), \
                           -104416, 209726, 209726, -nan)
reports[-1].sigmaresid = ValErr(0.398093, 0.000614672, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000520619, None, -1.59467e-05, None, -0.000618073, None, -4.53461e-07, None, -0.000618073, None, -4.53461e-07, None, -0.000933405, None, -1.21904e-05, None, -0.000933405, None, -1.21904e-05, None, 0.398098, None, 0.00596293, None, 0.398098, None, 0.00596293, None)

reports.append(Report(604021392, ("CSC", 1, 2, 1, 18), "MEp21_18"))
reports[-1].posNum = 209510
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000620339, 0.00130972, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0333554, 0.0329766, 0), \
                           ValErr(0.000283299, 0.000649028, 0), \
                           ValErr(0.0017772, 0.0015413, 0), \
                           ValErr(-6.4985e-06, 2.33114e-05, 0), \
                           -103150, 209510, 209510, -nan)
reports[-1].sigmaresid = ValErr(0.395897, 0.000619268, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00230297, None, 8.69692e-06, None, -0.00171366, None, 4.1684e-06, None, -0.00171366, None, 4.1684e-06, None, -0.0010405, None, -2.60338e-06, None, -0.0010405, None, -2.60338e-06, None, 0.3959, None, 0.00612385, None, 0.3959, None, 0.00612385, None)

reports.append(Report(604021768, ("CSC", 1, 2, 2, 1), "MEp22_01"))
reports[-1].posNum = 54603
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00324675, 0.00715453, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0393757, 0.177447, 0), \
                           ValErr(0.00271396, 0.00197621, 0), \
                           ValErr(0.00568067, 0.00932744, 0), \
                           ValErr(1.81068e-05, 5.48637e-05, 0), \
                           -78621.5, 54603, 54603, -nan)
reports[-1].sigmaresid = ValErr(1.02116, 0.00309009, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000165439, None, 1.56978e-05, None, 0.00112902, None, 1.99828e-05, None, 0.00112902, None, 1.99828e-05, None, 0.00641432, None, 1.4062e-06, None, 0.00641432, None, 1.4062e-06, None, 1.02118, None, 0.00681586, None, 1.02118, None, 0.00681586, None)

reports.append(Report(604021784, ("CSC", 1, 2, 2, 3), "MEp22_03"))
reports[-1].posNum = 47045
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0105567, 0.00766376, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.182092, 0.186244, 0), \
                           ValErr(0.000241228, 0.00194783, 0), \
                           ValErr(0.00990851, 0.00965241, 0), \
                           ValErr(-2.14482e-05, 4.74556e-05, 0), \
                           -66054.7, 47045, 47045, -nan)
reports[-1].sigmaresid = ValErr(0.985246, 0.00320971, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00384696, None, -2.59715e-05, None, 0.00490733, None, -3.65574e-05, None, 0.00490733, None, -3.65574e-05, None, 0.00178622, None, -5.14628e-05, None, 0.00178622, None, -5.14628e-05, None, 0.985266, None, 0.00691019, None, 0.985266, None, 0.00691019, None)

reports.append(Report(604021800, ("CSC", 1, 2, 2, 5), "MEp22_05"))
reports[-1].posNum = 54727
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00384991, 0.0069073, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.4244, 0.179225, 0), \
                           ValErr(0.0016558, 0.00199489, 0), \
                           ValErr(-0.0142846, 0.0093054, 0), \
                           ValErr(-6.16431e-05, 5.35375e-05, 0), \
                           -78093.5, 54727, 54727, -nan)
reports[-1].sigmaresid = ValErr(1.00806, 0.00304699, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0048601, None, -1.34682e-05, None, 0.00816253, None, -6.11877e-05, None, 0.00816253, None, -6.11877e-05, None, 0.0106208, None, -1.24689e-05, None, 0.0106208, None, -1.24689e-05, None, 1.00816, None, 0.00684984, None, 1.00816, None, 0.00684984, None)

reports.append(Report(604021816, ("CSC", 1, 2, 2, 7), "MEp22_07"))
reports[-1].posNum = 46962
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00896775, 0.0077778, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.133032, 0.189279, 0), \
                           ValErr(-0.000737341, 0.00207174, 0), \
                           ValErr(-0.00082111, 0.0100522, 0), \
                           ValErr(-5.03982e-05, 5.78909e-05, 0), \
                           -66552.6, 46962, 46962, -nan)
reports[-1].sigmaresid = ValErr(0.998217, 0.00325713, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00635198, None, 1.33876e-06, None, -0.0106238, None, 4.60609e-06, None, -0.0106238, None, 4.60609e-06, None, -0.0137041, None, 2.51444e-05, None, -0.0137041, None, 2.51444e-05, None, 0.998238, None, 0.00649526, None, 0.998238, None, 0.00649526, None)

reports.append(Report(604021832, ("CSC", 1, 2, 2, 9), "MEp22_09"))
reports[-1].posNum = 49540
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0111054, 0.00737789, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.196345, 0.190346, 0), \
                           ValErr(0.00332073, 0.00209156, 0), \
                           ValErr(-0.00151134, 0.00989582, 0), \
                           ValErr(2.9256e-05, 5.64625e-05, 0), \
                           -71147.1, 49540, 49540, -nan)
reports[-1].sigmaresid = ValErr(1.01736, 0.00323208, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00688537, None, 5.51065e-05, None, -0.00938983, None, 7.12042e-05, None, -0.00938983, None, 7.12042e-05, None, -0.00873123, None, 3.38475e-05, None, -0.00873123, None, 3.38475e-05, None, 1.01741, None, 0.00833765, None, 1.01741, None, 0.00833765, None)

reports.append(Report(604021848, ("CSC", 1, 2, 2, 11), "MEp22_11"))
reports[-1].posNum = 49386
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00390508, 0.00739319, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.231913, 0.191358, 0), \
                           ValErr(1.87809e-05, 0.00207345, 0), \
                           ValErr(-0.00808361, 0.00997415, 0), \
                           ValErr(3.51567e-05, 5.61721e-05, 0), \
                           -70526.2, 49386, 49386, -nan)
reports[-1].sigmaresid = ValErr(1.00916, 0.00321104, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00915783, None, -4.79027e-07, None, 0.00107323, None, 1.98795e-05, None, 0.00107323, None, 1.98795e-05, None, -0.00452815, None, 9.09242e-06, None, -0.00452815, None, 9.09242e-06, None, 1.00919, None, 0.00659107, None, 1.00919, None, 0.00659107, None)

reports.append(Report(604021864, ("CSC", 1, 2, 2, 13), "MEp22_13"))
reports[-1].posNum = 45975
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00461956, 0.00791389, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0571544, 0.191408, 0), \
                           ValErr(-0.000749333, 0.00209432, 0), \
                           ValErr(0.0115759, 0.0102044, 0), \
                           ValErr(-4.29182e-06, 5.84845e-05, 0), \
                           -65045.2, 45975, 45975, -nan)
reports[-1].sigmaresid = ValErr(0.995867, 0.00328418, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0123084, None, -1.55918e-05, None, -0.0103813, None, -2.71356e-05, None, -0.0103813, None, -2.71356e-05, None, -0.0136381, None, 5.47809e-05, None, -0.0136381, None, 5.47809e-05, None, 0.995883, None, 0.00663081, None, 0.995883, None, 0.00663081, None)

reports.append(Report(604021880, ("CSC", 1, 2, 2, 15), "MEp22_15"))
reports[-1].posNum = 55661
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00342379, 0.00699135, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.142041, 0.177645, 0), \
                           ValErr(-0.00125461, 0.00198606, 0), \
                           ValErr(-0.00202059, 0.00925963, 0), \
                           ValErr(3.57611e-05, 5.40831e-05, 0), \
                           -80288.5, 55661, 55661, -nan)
reports[-1].sigmaresid = ValErr(1.0238, 0.00306848, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00597646, None, 3.05592e-05, None, -0.0011491, None, 1.6142e-05, None, -0.0011491, None, 1.6142e-05, None, 0.00672343, None, 1.61665e-05, None, 0.00672343, None, 1.61665e-05, None, 1.02381, None, 0.00713295, None, 1.02381, None, 0.00713295, None)

reports.append(Report(604021896, ("CSC", 1, 2, 2, 17), "MEp22_17"))
reports[-1].posNum = 46307
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0127172, 0.00763985, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.62101, 0.192958, 0), \
                           ValErr(0.00430744, 0.00209292, 0), \
                           ValErr(-0.000545, 0.0101677, 0), \
                           ValErr(0.000110112, 5.70724e-05, 0), \
                           -64997, 46307, 46307, -nan)
reports[-1].sigmaresid = ValErr(0.984791, 0.00323599, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00389896, None, -5.82002e-06, None, -0.00759553, None, -3.84863e-05, None, -0.00759553, None, -3.84863e-05, None, -0.00283572, None, 5.62083e-06, None, -0.00283572, None, 5.62083e-06, None, 0.984969, None, 0.00659622, None, 0.984969, None, 0.00659622, None)

reports.append(Report(604021912, ("CSC", 1, 2, 2, 19), "MEp22_19"))
reports[-1].posNum = 54836
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00795422, 0.00717833, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.189742, 0.176477, 0), \
                           ValErr(0.000519591, 0.00196273, 0), \
                           ValErr(0.0104766, 0.00931979, 0), \
                           ValErr(-4.88717e-05, 5.4705e-05, 0), \
                           -78914.9, 54836, 54836, -nan)
reports[-1].sigmaresid = ValErr(1.02037, 0.00308114, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00142262, None, -2.28698e-05, None, 0.000918042, None, 5.33211e-06, None, 0.000918042, None, 5.33211e-06, None, -0.00864174, None, 3.74932e-05, None, -0.00864174, None, 3.74932e-05, None, 1.0204, None, 0.0067184, None, 1.0204, None, 0.0067184, None)

reports.append(Report(604021928, ("CSC", 1, 2, 2, 21), "MEp22_21"))
reports[-1].posNum = 46046
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0111788, 0.00764711, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.131061, 0.193478, 0), \
                           ValErr(0.00205519, 0.00210704, 0), \
                           ValErr(0.00965266, 0.0101815, 0), \
                           ValErr(-5.62058e-05, 5.7081e-05, 0), \
                           -64597.6, 46046, 46046, -nan)
reports[-1].sigmaresid = ValErr(0.984081, 0.0032428, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00413999, None, -4.36064e-06, None, 0.00425819, None, 2.84477e-05, None, 0.00425819, None, 2.84477e-05, None, 0.00369433, None, 3.73134e-05, None, 0.00369433, None, 3.73134e-05, None, 0.984113, None, 0.00711483, None, 0.984113, None, 0.00711483, None)

reports.append(Report(604021944, ("CSC", 1, 2, 2, 23), "MEp22_23"))
reports[-1].posNum = 54868
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0132533, 0.0069834, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.125278, 0.152207, 0), \
                           ValErr(0.00113247, 0.00136865, 0), \
                           ValErr(-0.0117387, 0.00929937, 0), \
                           ValErr(1.01411e-06, 5.29481e-05, 0), \
                           -78690.7, 54868, 54868, -nan)
reports[-1].sigmaresid = ValErr(1.01536, 0.00305645, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0127029, None, 6.50281e-06, None, -0.0076296, None, -3.53161e-06, None, -0.0076296, None, -3.53161e-06, None, -0.00872692, None, 2.98704e-05, None, -0.00872692, None, 2.98704e-05, None, 1.01538, None, 0.00662439, None, 1.01538, None, 0.00662439, None)

reports.append(Report(604021960, ("CSC", 1, 2, 2, 25), "MEp22_25"))
reports[-1].posNum = 47704
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00165196, 0.00770432, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.254943, 0.158669, 0), \
                           ValErr(-0.00316568, 0.00174265, 0), \
                           ValErr(0.00325441, 0.00991619, 0), \
                           ValErr(-3.22156e-05, 5.69716e-05, 0), \
                           -67515.1, 47704, 47704, -nan)
reports[-1].sigmaresid = ValErr(0.99636, 0.00321183, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00248015, None, -3.93665e-06, None, -0.00444172, None, -1.09168e-05, None, -0.00444172, None, -1.09168e-05, None, -0.0106171, None, 2.97101e-05, None, -0.0106171, None, 2.97101e-05, None, 0.996402, None, 0.00651986, None, 0.996402, None, 0.00651986, None)

reports.append(Report(604021976, ("CSC", 1, 2, 2, 27), "MEp22_27"))
reports[-1].posNum = 49702
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00560401, 0.00739143, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.175617, 0.188479, 0), \
                           ValErr(-0.00151283, 0.00208139, 0), \
                           ValErr(0.0202977, 0.0098288, 0), \
                           ValErr(1.56544e-05, 5.64403e-05, 0), \
                           -71101, 49702, 49702, -nan)
reports[-1].sigmaresid = ValErr(1.01167, 0.00320878, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00423801, None, 1.01956e-05, None, -0.00356927, None, 1.46269e-06, None, -0.00356927, None, 1.46269e-06, None, -0.00395419, None, 5.26616e-05, None, -0.00395419, None, 5.26616e-05, None, 1.01174, None, 0.00658063, None, 1.01174, None, 0.00658063, None)

reports.append(Report(604021992, ("CSC", 1, 2, 2, 29), "MEp22_29"))
reports[-1].posNum = 50604
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.003491, 0.0072668, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.282956, 0.186276, 0), \
                           ValErr(0.00116285, 0.00205959, 0), \
                           ValErr(0.00527148, 0.00968254, 0), \
                           ValErr(-9.19651e-06, 5.57749e-05, 0), \
                           -72142.3, 50604, 50604, -nan)
reports[-1].sigmaresid = ValErr(1.00671, 0.00316444, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00796627, None, 3.21485e-06, None, 0.00102027, None, -1.20383e-05, None, 0.00102027, None, -1.20383e-05, None, -0.00289295, None, 1.47805e-05, None, -0.00289295, None, 1.47805e-05, None, 1.00674, None, 0.00639126, None, 1.00674, None, 0.00639126, None)

reports.append(Report(604022008, ("CSC", 1, 2, 2, 31), "MEp22_31"))
reports[-1].posNum = 47679
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0121587, 0.00772566, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0437435, 0.169375, 0), \
                           ValErr(0.00131133, 0.00193344, 0), \
                           ValErr(-0.00413833, 0.00995676, 0), \
                           ValErr(4.70447e-05, 4.9227e-05, 0), \
                           -67316, 47679, 47679, -nan)
reports[-1].sigmaresid = ValErr(0.992946, 0.0031908, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00823968, None, 3.00668e-05, None, -0.00800662, None, 8.2906e-05, None, -0.00800662, None, 8.2906e-05, None, -0.00684172, None, 7.00565e-05, None, -0.00684172, None, 7.00565e-05, None, 0.992958, None, 0.00663599, None, 0.992958, None, 0.00663599, None)

reports.append(Report(604022024, ("CSC", 1, 2, 2, 33), "MEp22_33"))
reports[-1].posNum = 54564
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0042825, 0.00698226, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0576224, 0.0898231, 0), \
                           ValErr(-6.20703e-06, 0.00100256, 0), \
                           ValErr(0.0064692, 0.00921645, 0), \
                           ValErr(6.94479e-05, 5.365e-05, 0), \
                           -78217.3, 54564, 54564, -nan)
reports[-1].sigmaresid = ValErr(1.01467, 0.00306775, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000802944, None, 6.75927e-06, None, -0.00483683, None, -9.80815e-06, None, -0.00483683, None, -9.80815e-06, None, -0.00722857, None, 2.12321e-05, None, -0.00722857, None, 2.12321e-05, None, 1.01469, None, 0.00666213, None, 1.01469, None, 0.00666213, None)

reports.append(Report(604022040, ("CSC", 1, 2, 2, 35), "MEp22_35"))
reports[-1].posNum = 45373
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00195678, 0.0076726, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.253193, 0.194708, 0), \
                           ValErr(0.00398814, 0.00209795, 0), \
                           ValErr(0.00233693, 0.0102471, 0), \
                           ValErr(3.72287e-05, 5.6646e-05, 0), \
                           -63215.6, 45373, 45373, -nan)
reports[-1].sigmaresid = ValErr(0.974633, 0.0032354, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000817264, None, -1.44692e-05, None, -0.00125442, None, -4.32127e-07, None, -0.00125442, None, -4.32127e-07, None, -0.0022009, None, -5.31268e-05, None, -0.0022009, None, -5.31268e-05, None, 0.974688, None, 0.00653374, None, 0.974688, None, 0.00653374, None)

reports.append(Report(604021776, ("CSC", 1, 2, 2, 2), "MEp22_02"))
reports[-1].posNum = 48814
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000722142, 0.00739517, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0862282, 0.102344, 0), \
                           ValErr(0.00184279, 0.00106553, 0), \
                           ValErr(-0.0129581, 0.00952007, 0), \
                           ValErr(-4.37644e-05, 5.51869e-05, 0), \
                           -69434.9, 48814, 48814, -nan)
reports[-1].sigmaresid = ValErr(1.00351, 0.0031193, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000238909, None, 1.63667e-05, None, 0.00408953, None, -1.56109e-05, None, 0.00408953, None, -1.56109e-05, None, 0.00377312, None, -1.05373e-05, None, 0.00377312, None, -1.05373e-05, None, 1.00356, None, 0.00677947, None, 1.00356, None, 0.00677947, None)

reports.append(Report(604021792, ("CSC", 1, 2, 2, 4), "MEp22_04"))
reports[-1].posNum = 45076
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0137534, 0.00777688, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.122225, 0.190367, 0), \
                           ValErr(-0.000936604, 0.00143451, 0), \
                           ValErr(0.00530519, 0.0100927, 0), \
                           ValErr(-0.000102532, 5.70172e-05, 0), \
                           -63874.1, 45076, 45076, -nan)
reports[-1].sigmaresid = ValErr(0.998094, 0.00331121, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00735583, None, 1.78846e-05, None, 0.00664794, None, 3.10863e-06, None, 0.00664794, None, 3.10863e-06, None, 0.00765959, None, -4.45703e-06, None, 0.00765959, None, -4.45703e-06, None, 0.998133, None, 0.00645339, None, 0.998133, None, 0.00645339, None)

reports.append(Report(604021808, ("CSC", 1, 2, 2, 6), "MEp22_06"))
reports[-1].posNum = 52913
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0100042, 0.00711458, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.470702, 0.174025, 0), \
                           ValErr(0.00466447, 0.00193924, 0), \
                           ValErr(-0.0204251, 0.00911719, 0), \
                           ValErr(1.55496e-05, 5.45772e-05, 0), \
                           -75527.7, 52913, 52913, -nan)
reports[-1].sigmaresid = ValErr(1.00849, 0.00310009, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00195922, None, 3.58466e-05, None, 0.00084339, None, 2.46274e-05, None, 0.00084339, None, 2.46274e-05, None, 0.00968093, None, -2.78624e-05, None, 0.00968093, None, -2.78624e-05, None, 1.00866, None, 0.00689152, None, 1.00866, None, 0.00689152, None)

reports.append(Report(604021824, ("CSC", 1, 2, 2, 8), "MEp22_08"))
reports[-1].posNum = 43156
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0142579, 0.00793205, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.204275, 0.182233, 0), \
                           ValErr(-0.000592756, 0.00156239, 0), \
                           ValErr(0.0137078, 0.00993818, 0), \
                           ValErr(-0.000128192, 5.39996e-05, 0), \
                           -60759.3, 43156, 43156, -nan)
reports[-1].sigmaresid = ValErr(0.989021, 0.00331915, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00283915, None, 1.54058e-05, None, 0.00204549, None, 1.2347e-05, None, 0.00204549, None, 1.2347e-05, None, 0.00825574, None, 4.51013e-05, None, 0.00825574, None, 4.51013e-05, None, 0.989095, None, 0.00659255, None, 0.989095, None, 0.00659255, None)

reports.append(Report(604021840, ("CSC", 1, 2, 2, 10), "MEp22_10"))
reports[-1].posNum = 54988
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00316294, 0.00706343, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.161876, 0.173107, 0), \
                           ValErr(6.24514e-05, 0.00192944, 0), \
                           ValErr(0.000270904, 0.00912137, 0), \
                           ValErr(-9.79465e-06, 5.42024e-05, 0), \
                           -78683.4, 54988, 54988, -nan)
reports[-1].sigmaresid = ValErr(1.01205, 0.00305179, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00599142, None, 4.98478e-05, None, -0.00371096, None, 2.95237e-05, None, -0.00371096, None, 2.95237e-05, None, -0.00129397, None, 3.93141e-05, None, -0.00129397, None, 3.93141e-05, None, 1.01206, None, 0.00691361, None, 1.01206, None, 0.00691361, None)

reports.append(Report(604021856, ("CSC", 1, 2, 2, 12), "MEp22_12"))
reports[-1].posNum = 44163
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000871619, 0.00770355, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.165927, 0.187815, 0), \
                           ValErr(-0.0035117, 0.00202388, 0), \
                           ValErr(0.00271642, 0.00988517, 0), \
                           ValErr(2.93442e-05, 5.75844e-05, 0), \
                           -61817.1, 44163, 44163, -nan)
reports[-1].sigmaresid = ValErr(0.98099, 0.0033008, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00136461, None, 3.5608e-05, None, -0.000784138, None, -9.57733e-07, None, -0.000784138, None, -9.57733e-07, None, -0.00947208, None, 4.30812e-05, None, -0.00947208, None, 4.30812e-05, None, 0.981037, None, 0.00670995, None, 0.981037, None, 0.00670995, None)

reports.append(Report(604021872, ("CSC", 1, 2, 2, 14), "MEp22_14"))
reports[-1].posNum = 53236
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000671224, 0.00716345, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0235334, 0.175131, 0), \
                           ValErr(-0.00179407, 0.00194495, 0), \
                           ValErr(0.00726785, 0.0092297, 0), \
                           ValErr(-2.91454e-06, 5.47134e-05, 0), \
                           -76225.1, 53236, 53236, -nan)
reports[-1].sigmaresid = ValErr(1.01297, 0.0031044, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0069578, None, 1.27873e-05, None, -0.00438726, None, -7.87943e-06, None, -0.00438726, None, -7.87943e-06, None, -0.00397554, None, 5.10124e-06, None, -0.00397554, None, 5.10124e-06, None, 1.01299, None, 0.00650378, None, 1.01299, None, 0.00650378, None)

reports.append(Report(604021888, ("CSC", 1, 2, 2, 16), "MEp22_16"))
reports[-1].posNum = 45082
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000388016, 0.00771026, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0342296, 0.193922, 0), \
                           ValErr(-0.00117215, 0.00206615, 0), \
                           ValErr(-0.0147443, 0.0101622, 0), \
                           ValErr(1.82446e-05, 5.74917e-05, 0), \
                           -63754, 45082, 45082, -nan)
reports[-1].sigmaresid = ValErr(0.99525, 0.00331448, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0115009, None, -2.31632e-05, None, 0.00815398, None, -4.11739e-05, None, 0.00815398, None, -4.11739e-05, None, 0.000261241, None, 3.12822e-06, None, 0.000261241, None, 3.12822e-06, None, 0.99528, None, 0.00663008, None, 0.99528, None, 0.00663008, None)

reports.append(Report(604021904, ("CSC", 1, 2, 2, 18), "MEp22_18"))
reports[-1].posNum = 48097
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0171214, 0.00752891, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.120865, 0.0971537, 0), \
                           ValErr(-0.00191335, 0.00114155, 0), \
                           ValErr(0.00847558, 0.00951653, 0), \
                           ValErr(-0.000110835, 5.59358e-05, 0), \
                           -68890.8, 48097, 48097, -nan)
reports[-1].sigmaresid = ValErr(1.01348, 0.003207, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00304583, None, -7.1675e-06, None, 0.00889507, None, -6.00967e-05, None, 0.00889507, None, -6.00967e-05, None, 0.00941082, None, -2.15128e-05, None, 0.00941082, None, -2.15128e-05, None, 1.01354, None, 0.00700388, None, 1.01354, None, 0.00700388, None)

reports.append(Report(604021920, ("CSC", 1, 2, 2, 20), "MEp22_20"))
reports[-1].posNum = 49318
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0199851, 0.00742236, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0912388, 0.181457, 0), \
                           ValErr(-0.00191368, 0.00198334, 0), \
                           ValErr(0.00646934, 0.00955852, 0), \
                           ValErr(-8.71263e-05, 5.62404e-05, 0), \
                           -70245.8, 49318, 49318, -nan)
reports[-1].sigmaresid = ValErr(1.00542, 0.00320132, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0155879, None, -6.43254e-05, None, 0.0134694, None, -7.66151e-05, None, 0.0134694, None, -7.66151e-05, None, 0.0209362, None, -3.54222e-05, None, 0.0209362, None, -3.54222e-05, None, 1.00546, None, 0.0066359, None, 1.00546, None, 0.0066359, None)

reports.append(Report(604021936, ("CSC", 1, 2, 2, 22), "MEp22_22"))
reports[-1].posNum = 45599
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00777915, 0.00768638, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.10135, 0.190302, 0), \
                           ValErr(-0.00144259, 0.00204342, 0), \
                           ValErr(0.0109116, 0.00997406, 0), \
                           ValErr(-6.68953e-05, 5.74124e-05, 0), \
                           -64496.3, 45599, 45599, -nan)
reports[-1].sigmaresid = ValErr(0.995496, 0.00329645, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00187591, None, 1.84006e-05, None, -0.000435025, None, 2.33137e-05, None, -0.000435025, None, 2.33137e-05, None, -0.00938138, None, 2.96962e-05, None, -0.00938138, None, 2.96962e-05, None, 0.995524, None, 0.00681224, None, 0.995524, None, 0.00681224, None)

reports.append(Report(604021952, ("CSC", 1, 2, 2, 24), "MEp22_24"))
reports[-1].posNum = 53089
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0137238, 0.0071201, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.162446, 0.174604, 0), \
                           ValErr(0.000963358, 0.00193115, 0), \
                           ValErr(0.00333513, 0.0091189, 0), \
                           ValErr(-9.01819e-05, 5.47904e-05, 0), \
                           -75918.7, 53089, 53089, -nan)
reports[-1].sigmaresid = ValErr(1.01115, 0.00310312, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00612692, None, -1.40224e-05, None, 0.00858306, None, -3.53387e-05, None, 0.00858306, None, -3.53387e-05, None, 0.00923583, None, 1.23095e-05, None, 0.00923583, None, 1.23095e-05, None, 1.01119, None, 0.00719263, None, 1.01119, None, 0.00719263, None)

reports.append(Report(604021968, ("CSC", 1, 2, 2, 26), "MEp22_26"))
reports[-1].posNum = 44053
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0183481, 0.00788633, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.00527712, 0.188505, 0), \
                           ValErr(-0.00158459, 0.00202137, 0), \
                           ValErr(-0.0114553, 0.0101021, 0), \
                           ValErr(0.000120949, 5.74252e-05, 0), \
                           -61822.2, 44053, 44053, -nan)
reports[-1].sigmaresid = ValErr(0.984543, 0.0033169, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00124319, None, 1.54632e-05, None, -0.00751311, None, -2.46871e-05, None, -0.00751311, None, -2.46871e-05, None, -0.0149585, None, -2.70545e-05, None, -0.0149585, None, -2.70545e-05, None, 0.984601, None, 0.00671608, None, 0.984601, None, 0.00671608, None)

reports.append(Report(604021984, ("CSC", 1, 2, 2, 28), "MEp22_28"))
reports[-1].posNum = 54413
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0140033, 0.00714574, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.119676, 0.173279, 0), \
                           ValErr(0.00399814, 0.00193641, 0), \
                           ValErr(-0.00217563, 0.00914974, 0), \
                           ValErr(0.000105502, 5.46741e-05, 0), \
                           -77698.5, 54413, 54413, -nan)
reports[-1].sigmaresid = ValErr(1.00904, 0.00305876, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00639939, None, -1.75014e-05, None, -0.00881244, None, -2.95827e-05, None, -0.00881244, None, -2.95827e-05, None, -0.00521121, None, -4.73732e-05, None, -0.00521121, None, -4.73732e-05, None, 1.00912, None, 0.00692001, None, 1.00912, None, 0.00692001, None)

reports.append(Report(604022000, ("CSC", 1, 2, 2, 30), "MEp22_30"))
reports[-1].posNum = 43220
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0101939, 0.00785112, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.415492, 0.189114, 0), \
                           ValErr(0.000324327, 0.00202445, 0), \
                           ValErr(0.00570905, 0.0100117, 0), \
                           ValErr(3.57692e-05, 5.81305e-05, 0), \
                           -60552.4, 43220, 43220, -nan)
reports[-1].sigmaresid = ValErr(0.982246, 0.00334089, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0152837, None, 6.12482e-06, None, -0.0116258, None, -3.64204e-06, None, -0.0116258, None, -3.64204e-06, None, -0.0150575, None, 3.05308e-05, None, -0.0150575, None, 3.05308e-05, None, 0.982316, None, 0.00670129, None, 0.982316, None, 0.00670129, None)

reports.append(Report(604022016, ("CSC", 1, 2, 2, 32), "MEp22_32"))
reports[-1].posNum = 52849
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000132098, 0.00716697, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.299905, 0.175922, 0), \
                           ValErr(0.000230617, 0.00194021, 0), \
                           ValErr(-0.0124278, 0.00924949, 0), \
                           ValErr(3.86743e-05, 5.47876e-05, 0), \
                           -75609.3, 52849, 52849, -nan)
reports[-1].sigmaresid = ValErr(1.01179, 0.00311212, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00556078, None, -7.06749e-06, None, 0.00754046, None, -7.17427e-06, None, 0.00754046, None, -7.17427e-06, None, -0.00125257, None, 4.45188e-05, None, -0.00125257, None, 4.45188e-05, None, 1.01184, None, 0.00671028, None, 1.01184, None, 0.00671028, None)

reports.append(Report(604022032, ("CSC", 1, 2, 2, 34), "MEp22_34"))
reports[-1].posNum = 46460
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00670116, 0.00756065, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.243661, 0.18967, 0), \
                           ValErr(0.000383994, 0.0020296, 0), \
                           ValErr(-0.000733398, 0.00992043, 0), \
                           ValErr(6.36003e-05, 5.66541e-05, 0), \
                           -65770.6, 46460, 46460, -nan)
reports[-1].sigmaresid = ValErr(0.996707, 0.00326974, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0128414, None, -4.23485e-05, None, 0.00977344, None, -3.87698e-05, None, 0.00977344, None, -3.87698e-05, None, 0.0159324, None, -2.90236e-05, None, 0.0159324, None, -2.90236e-05, None, 0.99674, None, 0.00644467, None, 0.99674, None, 0.00644467, None)

reports.append(Report(604022048, ("CSC", 1, 2, 2, 36), "MEp22_36"))
reports[-1].posNum = 49924
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0138592, 0.00732856, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0192364, 0.178349, 0), \
                           ValErr(0.000830829, 0.00196756, 0), \
                           ValErr(-0.0110007, 0.00931673, 0), \
                           ValErr(-3.88111e-05, 5.59132e-05, 0), \
                           -71060.1, 49924, 49924, -nan)
reports[-1].sigmaresid = ValErr(1.00444, 0.00317873, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00577533, None, 3.11693e-05, None, -0.00994601, None, 2.96884e-05, None, -0.00994601, None, 2.96884e-05, None, -0.0133938, None, 7.7161e-05, None, -0.0133938, None, 7.7161e-05, None, 1.00447, None, 0.00685863, None, 1.00447, None, 0.00685863, None)

reports.append(Report(604025352, ("CSC", 1, 3, 1, 1), "MEp31_01"))
reports[-1].posNum = 168408
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00383575, 0.00181861, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.027358, 0.0501247, 0), \
                           ValErr(-0.00104328, 0.00112524, 0), \
                           ValErr(-0.00269322, 0.00224526, 0), \
                           ValErr(-2.63127e-05, 2.98285e-05, 0), \
                           -122487, 168408, 168408, -nan)
reports[-1].sigmaresid = ValErr(0.500767, 0.000862858, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00103948, None, 1.72985e-05, None, 0.00216155, None, 6.35096e-05, None, 0.00216155, None, 6.35096e-05, None, -0.00178934, None, 2.54752e-05, None, -0.00178934, None, 2.54752e-05, None, 0.500771, None, 0.00637022, None, 0.500771, None, 0.00637022, None)

reports.append(Report(604025368, ("CSC", 1, 3, 1, 3), "MEp31_03"))
reports[-1].posNum = 168881
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00201527, 0.00181515, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.00466786, 0.0501593, 0), \
                           ValErr(0.000796004, 0.00112086, 0), \
                           ValErr(-0.000645527, 0.00224493, 0), \
                           ValErr(1.61417e-06, 2.97236e-05, 0), \
                           -122900, 168881, 168881, -nan)
reports[-1].sigmaresid = ValErr(0.500971, 0.000861999, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00186477, None, -8.10572e-06, None, 0.00165617, None, 8.6834e-06, None, 0.00165617, None, 8.6834e-06, None, -0.000119885, None, -8.3638e-06, None, -0.000119885, None, -8.3638e-06, None, 0.500972, None, 0.00659839, None, 0.500972, None, 0.00659839, None)

reports.append(Report(604025384, ("CSC", 1, 3, 1, 5), "MEp31_05"))
reports[-1].posNum = 168843
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000387041, 0.00181039, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0409935, 0.0498923, 0), \
                           ValErr(-0.00187137, 0.0011146, 0), \
                           ValErr(0.00117647, 0.0022346, 0), \
                           ValErr(-9.43624e-06, 2.96256e-05, 0), \
                           -122203, 168843, 168843, -nan)
reports[-1].sigmaresid = ValErr(0.498989, 0.000858688, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00134829, None, -1.65829e-05, None, 0.000249093, None, 4.30831e-08, None, 0.000249093, None, 4.30831e-08, None, 0.00038326, None, -6.04432e-06, None, 0.00038326, None, -6.04432e-06, None, 0.498994, None, 0.00599145, None, 0.498994, None, 0.00599145, None)

reports.append(Report(604025400, ("CSC", 1, 3, 1, 7), "MEp31_07"))
reports[-1].posNum = 168714
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00268188, 0.00181087, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0570553, 0.0502243, 0), \
                           ValErr(-0.00108072, 0.00112351, 0), \
                           ValErr(-0.00241616, 0.00224202, 0), \
                           ValErr(-2.26205e-05, 2.97148e-05, 0), \
                           -122645, 168714, 168714, -nan)
reports[-1].sigmaresid = ValErr(0.500576, 0.000861745, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000711428, None, -5.93293e-06, None, 0.00118618, None, -9.32671e-06, None, 0.00118618, None, -9.32671e-06, None, 0.00045776, None, -1.24975e-05, None, 0.00045776, None, -1.24975e-05, None, 0.500582, None, 0.00616394, None, 0.500582, None, 0.00616394, None)

reports.append(Report(604025416, ("CSC", 1, 3, 1, 9), "MEp31_09"))
reports[-1].posNum = 168030
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000834232, 0.00180402, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00130278, 0.0497779, 0), \
                           ValErr(-0.00161799, 0.0011118, 0), \
                           ValErr(0.000187792, 0.00222904, 0), \
                           ValErr(-4.28494e-06, 3.02874e-05, 0), \
                           -120570, 168030, 168030, -nan)
reports[-1].sigmaresid = ValErr(0.495895, 0.000855379, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00144568, None, 6.80914e-06, None, 0.000926243, None, 1.54075e-05, None, 0.000926243, None, 1.54075e-05, None, -0.00118669, None, -2.20828e-05, None, -0.00118669, None, -2.20828e-05, None, 0.495899, None, 0.00611821, None, 0.495899, None, 0.00611821, None)

reports.append(Report(604025432, ("CSC", 1, 3, 1, 11), "MEp31_11"))
reports[-1].posNum = 167736
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-1.25298e-05, 0.00180545, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0624677, 0.049978, 0), \
                           ValErr(-0.00159536, 0.0011178, 0), \
                           ValErr(-0.00226196, 0.00223307, 0), \
                           ValErr(-1.13058e-06, 2.96379e-05, 0), \
                           -120701, 167736, 167736, -nan)
reports[-1].sigmaresid = ValErr(0.496909, 0.000857924, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0017051, None, -7.73375e-06, None, -0.00131273, None, -9.08813e-06, None, -0.00131273, None, -9.08813e-06, None, -2.88571e-05, None, -8.11943e-06, None, -2.88571e-05, None, -8.11943e-06, None, 0.496916, None, 0.00604548, None, 0.496916, None, 0.00604548, None)

reports.append(Report(604025448, ("CSC", 1, 3, 1, 13), "MEp31_13"))
reports[-1].posNum = 167352
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00105264, 0.00181124, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0219539, 0.05, 0), \
                           ValErr(0.00150572, 0.00111607, 0), \
                           ValErr(0.00276769, 0.00223519, 0), \
                           ValErr(-1.06547e-05, 2.97066e-05, 0), \
                           -120504, 167352, 167352, -nan)
reports[-1].sigmaresid = ValErr(0.497146, 0.000859317, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000146546, None, -1.90626e-05, None, 0.000484972, None, -1.98817e-05, None, 0.000484972, None, -1.98817e-05, None, 0.00222714, None, -5.50141e-06, None, 0.00222714, None, -5.50141e-06, None, 0.497152, None, 0.00587992, None, 0.497152, None, 0.00587992, None)

reports.append(Report(604025464, ("CSC", 1, 3, 1, 15), "MEp31_15"))
reports[-1].posNum = 166904
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00313196, 0.00181112, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0215251, 0.0502206, 0), \
                           ValErr(0.000405626, 0.00112451, 0), \
                           ValErr(-0.00129068, 0.00224448, 0), \
                           ValErr(3.77604e-05, 2.97369e-05, 0), \
                           -120390, 166904, 166904, -nan)
reports[-1].sigmaresid = ValErr(0.497766, 0.000861543, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00306841, None, 1.38577e-05, None, 0.00256903, None, 9.82492e-07, None, 0.00256903, None, 9.82492e-07, None, 0.00395222, None, -5.29438e-06, None, 0.00395222, None, -5.29438e-06, None, 0.49777, None, 0.00594692, None, 0.49777, None, 0.00594692, None)

reports.append(Report(604025480, ("CSC", 1, 3, 1, 17), "MEp31_17"))
reports[-1].posNum = 167498
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00167695, 0.00182603, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0509035, 0.0504067, 0), \
                           ValErr(-0.00109674, 0.00112815, 0), \
                           ValErr(0.0010346, 0.00225754, 0), \
                           ValErr(1.83543e-05, 2.99833e-05, 0), \
                           -122067, 167498, 167498, -nan)
reports[-1].sigmaresid = ValErr(0.50149, 0.000866448, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-9.93865e-05, None, -7.31114e-06, None, -0.000988612, None, -1.36621e-05, None, -0.000988612, None, -1.36621e-05, None, -0.00162718, None, -2.59039e-05, None, -0.00162718, None, -2.59039e-05, None, 0.501494, None, 0.00597591, None, 0.501494, None, 0.00597591, None)

reports.append(Report(604025360, ("CSC", 1, 3, 1, 2), "MEp31_02"))
reports[-1].posNum = 173139
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00096329, 0.00183827, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0406017, 0.0521866, 0), \
                           ValErr(-0.000694639, 0.00116654, 0), \
                           ValErr(-0.00141131, 0.00233445, 0), \
                           ValErr(3.3752e-05, 3.01627e-05, 0), \
                           -130260, 173139, 173139, -nan)
reports[-1].sigmaresid = ValErr(0.513455, 0.000872548, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00123834, None, -1.19499e-05, None, -0.00158968, None, -1.14433e-05, None, -0.00158968, None, -1.14433e-05, None, -0.00423872, None, -1.489e-05, None, -0.00423872, None, -1.489e-05, None, 0.51346, None, 0.00581534, None, 0.51346, None, 0.00581534, None)

reports.append(Report(604025376, ("CSC", 1, 3, 1, 4), "MEp31_04"))
reports[-1].posNum = 173052
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000240337, 0.00184246, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0310565, 0.0524411, 0), \
                           ValErr(0.000710227, 0.00116926, 0), \
                           ValErr(-0.00297808, 0.0023356, 0), \
                           ValErr(7.25822e-06, 3.03119e-05, 0), \
                           -130805, 173052, 173052, -nan)
reports[-1].sigmaresid = ValErr(0.515269, 0.00087585, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000370496, None, -8.83131e-06, None, -0.00187472, None, -2.22439e-06, None, -0.00187472, None, -2.22439e-06, None, -0.000457156, None, 8.59344e-06, None, -0.000457156, None, 8.59344e-06, None, 0.515274, None, 0.00573766, None, 0.515274, None, 0.00573766, None)

reports.append(Report(604025392, ("CSC", 1, 3, 1, 6), "MEp31_06"))
reports[-1].posNum = 172118
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00288273, 0.00185897, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0102927, 0.0525683, 0), \
                           ValErr(-0.00191528, 0.00117471, 0), \
                           ValErr(0.00445876, 0.00235388, 0), \
                           ValErr(1.12247e-05, 3.04774e-05, 0), \
                           -130630, 172118, 172118, -nan)
reports[-1].sigmaresid = ValErr(0.516861, 0.000880939, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000414924, None, 6.02971e-06, None, -0.000316081, None, 1.36465e-05, None, -0.000316081, None, 1.36465e-05, None, 0.00123446, None, 8.38391e-06, None, 0.00123446, None, 8.38391e-06, None, 0.516871, None, 0.00583863, None, 0.516871, None, 0.00583863, None)

reports.append(Report(604025408, ("CSC", 1, 3, 1, 8), "MEp31_08"))
reports[-1].posNum = 171607
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000995267, 0.0018561, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0159539, 0.0511302, 0), \
                           ValErr(0.000791037, 0.00107847, 0), \
                           ValErr(-0.00101071, 0.00235135, 0), \
                           ValErr(-1.74883e-05, 3.02122e-05, 0), \
                           -130155, 171607, 171607, -nan)
reports[-1].sigmaresid = ValErr(0.516599, 0.00086757, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00115079, None, -1.5613e-06, None, 0.000352387, None, 1.78267e-05, None, 0.000352387, None, 1.78267e-05, None, 0.00119468, None, 1.03455e-05, None, 0.00119468, None, 1.03455e-05, None, 0.516601, None, 0.00590651, None, 0.516601, None, 0.00590651, None)

reports.append(Report(604025424, ("CSC", 1, 3, 1, 10), "MEp31_10"))
reports[-1].posNum = 172368
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000168098, 0.00185464, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0654582, 0.0528369, 0), \
                           ValErr(0.00164745, 0.00118222, 0), \
                           ValErr(0.000156799, 0.00235762, 0), \
                           ValErr(1.14777e-05, 3.05192e-05, 0), \
                           -131377, 172368, 172368, -nan)
reports[-1].sigmaresid = ValErr(0.518534, 0.000883151, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000757926, None, -1.26372e-05, None, -2.98084e-05, None, -2.3513e-05, None, -2.98084e-05, None, -2.3513e-05, None, -0.00255474, None, -3.20822e-05, None, -0.00255474, None, -3.20822e-05, None, 0.51854, None, 0.0058827, None, 0.51854, None, 0.0058827, None)

reports.append(Report(604025440, ("CSC", 1, 3, 1, 12), "MEp31_12"))
reports[-1].posNum = 171875
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000259431, 0.00186331, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0628406, 0.0527159, 0), \
                           ValErr(0.00145069, 0.00117815, 0), \
                           ValErr(0.000966344, 0.0023607, 0), \
                           ValErr(4.37845e-06, 3.05831e-05, 0), \
                           -130845, 171875, 171875, -nan)
reports[-1].sigmaresid = ValErr(0.518065, 0.000883615, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00247782, None, -6.22806e-06, None, 0.000829287, None, -2.03504e-06, None, 0.000829287, None, -2.03504e-06, None, -0.00131639, None, -7.10287e-06, None, -0.00131639, None, -7.10287e-06, None, 0.51807, None, 0.00571541, None, 0.51807, None, 0.00571541, None)

reports.append(Report(604025456, ("CSC", 1, 3, 1, 14), "MEp31_14"))
reports[-1].posNum = 173202
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00129552, 0.00185297, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0516498, 0.0525026, 0), \
                           ValErr(-0.000958684, 0.00117326, 0), \
                           ValErr(0.000394972, 0.0023445, 0), \
                           ValErr(1.56974e-05, 3.04498e-05, 0), \
                           -131736, 173202, 173202, -nan)
reports[-1].sigmaresid = ValErr(0.517708, 0.000879617, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00017708, None, -1.03789e-05, None, -0.000996415, None, -1.99847e-05, None, -0.000996415, None, -1.99847e-05, None, -0.0014835, None, -2.09726e-05, None, -0.0014835, None, -2.09726e-05, None, 0.517711, None, 0.00589685, None, 0.517711, None, 0.00589685, None)

reports.append(Report(604025472, ("CSC", 1, 3, 1, 16), "MEp31_16"))
reports[-1].posNum = 172230
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000237588, 0.00186072, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(7.07992e-05, 0.0527658, 0), \
                           ValErr(4.89005e-05, 0.00117846, 0), \
                           ValErr(0.00153042, 0.0023596, 0), \
                           ValErr(2.41522e-05, 3.05647e-05, 0), \
                           -131125, 172230, 172230, -nan)
reports[-1].sigmaresid = ValErr(0.518091, 0.000882748, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00104727, None, 1.02386e-05, None, 0.000732208, None, 2.32888e-05, None, 0.000732208, None, 2.32888e-05, None, 0.00185068, None, 3.46093e-05, None, 0.00185068, None, 3.46093e-05, None, 0.518092, None, 0.0057845, None, 0.518092, None, 0.0057845, None)

reports.append(Report(604025488, ("CSC", 1, 3, 1, 18), "MEp31_18"))
reports[-1].posNum = 172483
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000122287, 0.00185844, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0600301, 0.0525264, 0), \
                           ValErr(0.000509453, 0.00117954, 0), \
                           ValErr(0.00180866, 0.00235278, 0), \
                           ValErr(-4.07694e-05, 3.05204e-05, 0), \
                           -131069, 172483, 172483, -nan)
reports[-1].sigmaresid = ValErr(0.517347, 0.000880833, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00185299, None, 3.64835e-07, None, 0.000938901, None, -2.19534e-07, None, 0.000938901, None, -2.19534e-07, None, 0.000256653, None, 2.6534e-06, None, 0.000256653, None, 2.6534e-06, None, 0.517355, None, 0.00568296, None, 0.517355, None, 0.00568296, None)

reports.append(Report(604025864, ("CSC", 1, 3, 2, 1), "MEp32_01"))
reports[-1].posNum = 57174
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00510242, 0.00709271, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.122027, 0.112373, 0), \
                           ValErr(-0.00186094, 0.00134693, 0), \
                           ValErr(0.0100428, 0.0104959, 0), \
                           ValErr(-5.23196e-05, 5.56761e-05, 0), \
                           -83782.4, 57174, 57174, -nan)
reports[-1].sigmaresid = ValErr(1.04755, 0.00293966, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-6.30857e-05, None, 2.32662e-05, None, -0.00261663, None, 7.37819e-06, None, -0.00261663, None, 7.37819e-06, None, -0.00893744, None, -1.35286e-05, None, -0.00893744, None, -1.35286e-05, None, 1.04759, None, 0.00728792, None, 1.04759, None, 0.00728792, None)

reports.append(Report(604025880, ("CSC", 1, 3, 2, 3), "MEp32_03"))
reports[-1].posNum = 50001
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0119625, 0.00770431, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.11135, 0.133157, 0), \
                           ValErr(0.00180578, 0.00229176, 0), \
                           ValErr(0.002512, 0.0110276, 0), \
                           ValErr(9.63715e-05, 5.55921e-05, 0), \
                           -71398.5, 50001, 50001, -nan)
reports[-1].sigmaresid = ValErr(1.00904, 0.00318719, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00487175, None, -2.64279e-05, None, -0.00661331, None, -3.63995e-05, None, -0.00661331, None, -3.63995e-05, None, -0.000190673, None, 1.90068e-06, None, -0.000190673, None, 1.90068e-06, None, 1.00908, None, 0.00756257, None, 1.00908, None, 0.00756257, None)

reports.append(Report(604025896, ("CSC", 1, 3, 2, 5), "MEp32_05"))
reports[-1].posNum = 57430
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00120369, 0.00704226, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0155915, 0.195251, 0), \
                           ValErr(0.00485254, 0.00225331, 0), \
                           ValErr(0.00164391, 0.0100153, 0), \
                           ValErr(-2.31457e-05, 4.26282e-05, 0), \
                           -83743.4, 57430, 57430, -nan)
reports[-1].sigmaresid = ValErr(1.04002, 0.00306602, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00410249, None, 7.65153e-06, None, 0.000984463, None, 5.16425e-06, None, 0.000984463, None, 5.16425e-06, None, 0.00272247, None, 1.12627e-05, None, 0.00272247, None, 1.12627e-05, None, 1.04007, None, 0.00757559, None, 1.04007, None, 0.00757559, None)

reports.append(Report(604025912, ("CSC", 1, 3, 2, 7), "MEp32_07"))
reports[-1].posNum = 50298
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0038833, 0.00783435, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.166842, 0.143449, 0), \
                           ValErr(0.0028306, 0.00233338, 0), \
                           ValErr(-0.0064814, 0.0110756, 0), \
                           ValErr(7.39933e-05, 5.75983e-05, 0), \
                           -72446.1, 50298, 50298, -nan)
reports[-1].sigmaresid = ValErr(1.02163, 0.00318482, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00347972, None, 2.67317e-06, None, -0.00364203, None, 1.37709e-06, None, -0.00364203, None, 1.37709e-06, None, -0.00663017, None, -3.64079e-05, None, -0.00663017, None, -3.64079e-05, None, 1.02168, None, 0.00734944, None, 1.02168, None, 0.00734944, None)

reports.append(Report(604025928, ("CSC", 1, 3, 2, 9), "MEp32_09"))
reports[-1].posNum = 52771
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0172883, 0.0073197, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.00360352, 0.209544, 0), \
                           ValErr(-0.000353043, 0.00231354, 0), \
                           ValErr(0.00101498, 0.01087, 0), \
                           ValErr(-0.000122766, 5.63482e-05, 0), \
                           -76590.6, 52771, 52771, -nan)
reports[-1].sigmaresid = ValErr(1.03297, 0.00317962, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0122711, None, 1.04956e-05, None, 0.0129847, None, 8.66841e-06, None, 0.0129847, None, 8.66841e-06, None, 0.0219545, None, 6.03228e-05, None, 0.0219545, None, 6.03228e-05, None, 1.03303, None, 0.00782302, None, 1.03303, None, 0.00782302, None)

reports.append(Report(604025944, ("CSC", 1, 3, 2, 11), "MEp32_11"))
reports[-1].posNum = 52693
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00451392, 0.00735304, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.307923, 0.211162, 0), \
                           ValErr(-0.000935986, 0.00233426, 0), \
                           ValErr(-0.00360386, 0.0109736, 0), \
                           ValErr(-1.4055e-05, 5.64859e-05, 0), \
                           -76299.3, 52693, 52693, -nan)
reports[-1].sigmaresid = ValErr(1.02949, 0.00317124, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0120697, None, -5.58116e-05, None, -0.00641073, None, -2.78241e-05, None, -0.00641073, None, -2.78241e-05, None, -0.00355749, None, -5.37597e-06, None, -0.00355749, None, -5.37597e-06, None, 1.02951, None, 0.0077752, None, 1.02951, None, 0.0077752, None)

reports.append(Report(604025960, ("CSC", 1, 3, 2, 13), "MEp32_13"))
reports[-1].posNum = 49792
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0065249, 0.00781009, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00769598, 0.205571, 0), \
                           ValErr(0.00295428, 0.00234562, 0), \
                           ValErr(0.00551824, 0.0106313, 0), \
                           ValErr(7.35315e-06, 4.8731e-05, 0), \
                           -71242.6, 49792, 49792, -nan)
reports[-1].sigmaresid = ValErr(1.01194, 0.00312641, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00933006, None, 1.04343e-05, None, 0.00933188, None, -2.17076e-07, None, 0.00933188, None, -2.17076e-07, None, 0.00964375, None, -1.98627e-05, None, 0.00964375, None, -1.98627e-05, None, 1.01196, None, 0.00751108, None, 1.01196, None, 0.00751108, None)

reports.append(Report(604025976, ("CSC", 1, 3, 2, 15), "MEp32_15"))
reports[-1].posNum = 57499
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00104032, 0.00707932, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.293528, 0.199142, 0), \
                           ValErr(-0.00161598, 0.00225436, 0), \
                           ValErr(-0.00142358, 0.0104713, 0), \
                           ValErr(-2.23101e-05, 5.50903e-05, 0), \
                           -83792, 57499, 57499, -nan)
reports[-1].sigmaresid = ValErr(1.03908, 0.00306411, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000818854, None, 2.18856e-05, None, -0.000368321, None, 1.98975e-05, None, -0.000368321, None, 1.98975e-05, None, 0.00697279, None, -1.05969e-05, None, 0.00697279, None, -1.05969e-05, None, 1.03911, None, 0.00736892, None, 1.03911, None, 0.00736892, None)

reports.append(Report(604025992, ("CSC", 1, 3, 2, 17), "MEp32_17"))
reports[-1].posNum = 50129
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00256849, 0.00770624, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.304079, 0.213037, 0), \
                           ValErr(-0.00109546, 0.0023465, 0), \
                           ValErr(0.00407126, 0.0113128, 0), \
                           ValErr(7.90021e-05, 5.81893e-05, 0), \
                           -71568.2, 50129, 50129, -nan)
reports[-1].sigmaresid = ValErr(1.00878, 0.00318594, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000385257, None, 1.55009e-05, None, 0.00277787, None, 1.40591e-05, None, 0.00277787, None, 1.40591e-05, None, 0.00797274, None, 1.3427e-05, None, 0.00797274, None, 1.3427e-05, None, 1.00882, None, 0.00747648, None, 1.00882, None, 0.00747648, None)

reports.append(Report(604026008, ("CSC", 1, 3, 2, 19), "MEp32_19"))
reports[-1].posNum = 57727
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0111347, 0.00721508, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0495661, 0.19796, 0), \
                           ValErr(-0.000989841, 0.00225102, 0), \
                           ValErr(-0.0178338, 0.0105012, 0), \
                           ValErr(-2.65977e-05, 5.5788e-05, 0), \
                           -84211.5, 57727, 57727, -nan)
reports[-1].sigmaresid = ValErr(1.04065, 0.00306267, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00369429, None, 2.24054e-05, None, 0.0022244, None, 1.67168e-05, None, 0.0022244, None, 1.67168e-05, None, 0.0012162, None, 3.65383e-05, None, 0.0012162, None, 3.65383e-05, None, 1.04068, None, 0.00832242, None, 1.04068, None, 0.00832242, None)

reports.append(Report(604026024, ("CSC", 1, 3, 2, 21), "MEp32_21"))
reports[-1].posNum = 50366
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00985243, 0.00764299, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.18218, 0.211144, 0), \
                           ValErr(0.00115443, 0.00230347, 0), \
                           ValErr(0.00855465, 0.0111502, 0), \
                           ValErr(6.03007e-05, 5.72882e-05, 0), \
                           -71909, 50366, 50366, -nan)
reports[-1].sigmaresid = ValErr(1.00883, 0.00317859, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00353507, None, -1.06045e-05, None, -0.0034593, None, -7.23543e-05, None, -0.0034593, None, -7.23543e-05, None, -0.00660546, None, -6.59228e-05, None, -0.00660546, None, -6.59228e-05, None, 1.00885, None, 0.00803899, None, 1.00885, None, 0.00803899, None)

reports.append(Report(604026040, ("CSC", 1, 3, 2, 23), "MEp32_23"))
reports[-1].posNum = 56952
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0148305, 0.00716045, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0478359, 0.104511, 0), \
                           ValErr(-0.000975239, 0.00110635, 0), \
                           ValErr(-0.00353871, 0.0105564, 0), \
                           ValErr(-7.89146e-05, 5.48157e-05, 0), \
                           -83105.9, 56952, 56952, -nan)
reports[-1].sigmaresid = ValErr(1.04111, 0.00306142, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0122829, None, 1.22061e-05, None, 0.0103325, None, 4.12365e-06, None, 0.0103325, None, 4.12365e-06, None, 0.00975513, None, -1.36895e-05, None, 0.00975513, None, -1.36895e-05, None, 1.04113, None, 0.00728865, None, 1.04113, None, 0.00728865, None)

reports.append(Report(604026056, ("CSC", 1, 3, 2, 25), "MEp32_25"))
reports[-1].posNum = 50879
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000818147, 0.0077613, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.375811, 0.210536, 0), \
                           ValErr(0.00291583, 0.00234425, 0), \
                           ValErr(0.0178933, 0.0111861, 0), \
                           ValErr(5.37195e-05, 5.87004e-05, 0), \
                           -73608.4, 50879, 50879, -nan)
reports[-1].sigmaresid = ValErr(1.02819, 0.00322321, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00470492, None, 1.78704e-05, None, 0.00910123, None, 5.41023e-05, None, 0.00910123, None, 5.41023e-05, None, 0.00840955, None, 4.02121e-05, None, 0.00840955, None, 4.02121e-05, None, 1.02825, None, 0.00781496, None, 1.02825, None, 0.00781496, None)

reports.append(Report(604026072, ("CSC", 1, 3, 2, 27), "MEp32_27"))
reports[-1].posNum = 52925
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00788829, 0.00744421, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.173938, 0.180619, 0), \
                           ValErr(0.00185426, 0.00159154, 0), \
                           ValErr(0.0103161, 0.010952, 0), \
                           ValErr(3.83707e-06, 5.63334e-05, 0), \
                           -77065.1, 52925, 52925, -nan)
reports[-1].sigmaresid = ValErr(1.03788, 0.00318028, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00376208, None, 5.84297e-05, None, -0.00340456, None, 1.61931e-05, None, -0.00340456, None, 1.61931e-05, None, -0.00998729, None, 2.12456e-05, None, -0.00998729, None, 2.12456e-05, None, 1.0379, None, 0.00822996, None, 1.0379, None, 0.00822996, None)

reports.append(Report(604026088, ("CSC", 1, 3, 2, 29), "MEp32_29"))
reports[-1].posNum = 53720
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00400093, 0.00736531, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.279793, 0.208598, 0), \
                           ValErr(-0.000178284, 0.00232492, 0), \
                           ValErr(0.00597102, 0.0108736, 0), \
                           ValErr(-1.02387e-05, 5.67763e-05, 0), \
                           -78086.8, 53720, 53720, -nan)
reports[-1].sigmaresid = ValErr(1.03526, 0.00315839, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00575497, None, 1.23859e-05, None, 0.00589377, None, 8.24709e-06, None, 0.00589377, None, 8.24709e-06, None, 0.00681434, None, 5.31342e-05, None, 0.00681434, None, 5.31342e-05, None, 1.03528, None, 0.00830337, None, 1.03528, None, 0.00830337, None)

reports.append(Report(604026104, ("CSC", 1, 3, 2, 31), "MEp32_31"))
reports[-1].posNum = 50971
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00150084, 0.00781433, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.224035, 0.210461, 0), \
                           ValErr(0.0028193, 0.00235933, 0), \
                           ValErr(-0.00138189, 0.0112829, 0), \
                           ValErr(6.03603e-05, 5.89514e-05, 0), \
                           -73591.2, 50971, 50971, -nan)
reports[-1].sigmaresid = ValErr(1.02516, 0.00321072, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00189738, None, 3.36024e-05, None, 0.00376883, None, 3.9576e-05, None, 0.00376883, None, 3.9576e-05, None, 0.00725916, None, 4.28496e-05, None, 0.00725916, None, 4.28496e-05, None, 1.02519, None, 0.00764336, None, 1.02519, None, 0.00764336, None)

reports.append(Report(604026120, ("CSC", 1, 3, 2, 33), "MEp32_33"))
reports[-1].posNum = 56808
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00825925, 0.00704603, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0374075, 0.199206, 0), \
                           ValErr(0.00302797, 0.00226628, 0), \
                           ValErr(-0.00480967, 0.0103686, 0), \
                           ValErr(-8.71834e-05, 5.48866e-05, 0), \
                           -82431.6, 56808, 56808, -nan)
reports[-1].sigmaresid = ValErr(1.03264, 0.00306358, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00276161, None, 2.05968e-05, None, 0.00293312, None, 2.17219e-05, None, 0.00293312, None, 2.17219e-05, None, -0.00376743, None, -1.44299e-05, None, -0.00376743, None, -1.44299e-05, None, 1.03268, None, 0.00768204, None, 1.03268, None, 0.00768204, None)

reports.append(Report(604026136, ("CSC", 1, 3, 2, 35), "MEp32_35"))
reports[-1].posNum = 49318
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.012716, 0.00772209, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.22321, 0.211866, 0), \
                           ValErr(-0.00165998, 0.00233624, 0), \
                           ValErr(0.0185569, 0.01128, 0), \
                           ValErr(5.1586e-05, 5.78617e-05, 0), \
                           -69518.3, 49318, 49318, -nan)
reports[-1].sigmaresid = ValErr(0.990697, 0.00315445, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00733036, None, -1.45562e-05, None, -0.00243707, None, -1.56633e-05, None, -0.00243707, None, -1.56633e-05, None, 0.00191134, None, -2.50789e-05, None, 0.00191134, None, -2.50789e-05, None, 0.990739, None, 0.00703589, None, 0.990739, None, 0.00703589, None)

reports.append(Report(604025872, ("CSC", 1, 3, 2, 2), "MEp32_02"))
reports[-1].posNum = 54809
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(6.46703e-05, 0.00734083, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.244938, 0.213625, 0), \
                           ValErr(0.000304315, 0.00238816, 0), \
                           ValErr(-0.0112899, 0.011139, 0), \
                           ValErr(4.03421e-05, 5.67864e-05, 0), \
                           -79838, 54809, 54809, -nan)
reports[-1].sigmaresid = ValErr(1.03844, 0.00313647, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00300938, None, -6.28271e-06, None, -0.00308725, None, -1.68863e-05, None, -0.00308725, None, -1.68863e-05, None, 0.00258953, None, -1.46764e-05, None, 0.00258953, None, -1.46764e-05, None, 1.03848, None, 0.0074282, None, 1.03848, None, 0.0074282, None)

reports.append(Report(604025888, ("CSC", 1, 3, 2, 4), "MEp32_04"))
reports[-1].posNum = 52887
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0050291, 0.00758557, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.235543, 0.221234, 0), \
                           ValErr(0.0038917, 0.0024622, 0), \
                           ValErr(-0.00224237, 0.0115152, 0), \
                           ValErr(-5.25574e-05, 5.66003e-05, 0), \
                           -77007.8, 52887, 52887, -nan)
reports[-1].sigmaresid = ValErr(1.03785, 0.0031317, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0007345, None, 3.53809e-05, None, 0.00204157, None, 1.46389e-05, None, 0.00204157, None, 1.46389e-05, None, 0.00361793, None, 3.08586e-05, None, 0.00361793, None, 3.08586e-05, None, 1.03788, None, 0.00703567, None, 1.03788, None, 0.00703567, None)

reports.append(Report(604025904, ("CSC", 1, 3, 2, 6), "MEp32_06"))
reports[-1].posNum = 57874
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00667041, 0.00712471, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.043351, 0.207182, 0), \
                           ValErr(0.00267208, 0.00234376, 0), \
                           ValErr(-0.0258741, 0.0108162, 0), \
                           ValErr(3.45225e-05, 5.56407e-05, 0), \
                           -85096.1, 57874, 57874, -nan)
reports[-1].sigmaresid = ValErr(1.05278, 0.00309443, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00201705, None, -1.2361e-05, None, -0.00300846, None, -3.8491e-05, None, -0.00300846, None, -3.8491e-05, None, -0.00355281, None, -4.47429e-05, None, -0.00355281, None, -4.47429e-05, None, 1.05286, None, 0.00742248, None, 1.05286, None, 0.00742248, None)

reports.append(Report(604025920, ("CSC", 1, 3, 2, 8), "MEp32_08"))
reports[-1].posNum = 50569
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00344498, 0.00783707, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.195184, 0.221686, 0), \
                           ValErr(-0.000900219, 0.00246747, 0), \
                           ValErr(0.00189845, 0.0118217, 0), \
                           ValErr(2.84475e-05, 5.95946e-05, 0), \
                           -72498, 50569, 50569, -nan)
reports[-1].sigmaresid = ValErr(1.01482, 0.00319102, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00186036, None, 2.19746e-06, None, -0.00134859, None, -4.60948e-05, None, -0.00134859, None, -4.60948e-05, None, 0.00377755, None, 1.3651e-05, None, 0.00377755, None, 1.3651e-05, None, 1.01483, None, 0.0080624, None, 1.01483, None, 0.0080624, None)

reports.append(Report(604025936, ("CSC", 1, 3, 2, 10), "MEp32_10"))
reports[-1].posNum = 59698
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0116945, 0.00711044, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0895461, 0.205019, 0), \
                           ValErr(0.00465638, 0.00233414, 0), \
                           ValErr(-0.00482115, 0.0108223, 0), \
                           ValErr(-5.09129e-05, 5.53151e-05, 0), \
                           -88257.3, 59698, 59698, -nan)
reports[-1].sigmaresid = ValErr(1.06126, 0.00307134, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00791524, None, 1.107e-05, None, 0.00790257, None, 5.12519e-05, None, 0.00790257, None, 5.12519e-05, None, 0.00818192, None, 4.3636e-05, None, 0.00818192, None, 4.3636e-05, None, 1.06131, None, 0.0101896, None, 1.06131, None, 0.0101896, None)

reports.append(Report(604025952, ("CSC", 1, 3, 2, 12), "MEp32_12"))
reports[-1].posNum = 51455
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00218693, 0.00767894, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0891055, 0.221514, 0), \
                           ValErr(0.00379219, 0.00246396, 0), \
                           ValErr(0.00134063, 0.011688, 0), \
                           ValErr(-5.81629e-05, 5.8839e-05, 0), \
                           -74177.6, 51455, 51455, -nan)
reports[-1].sigmaresid = ValErr(1.02293, 0.00318873, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00467957, None, -3.76496e-05, None, -1.27062e-05, None, -1.59857e-05, None, -1.27062e-05, None, -1.59857e-05, None, -0.000564742, None, -1.65408e-05, None, -0.000564742, None, -1.65408e-05, None, 1.02296, None, 0.00795775, None, 1.02296, None, 0.00795775, None)

reports.append(Report(604025968, ("CSC", 1, 3, 2, 14), "MEp32_14"))
reports[-1].posNum = 58528
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0143515, 0.00720189, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.330257, 0.206283, 0), \
                           ValErr(-0.00369904, 0.00233237, 0), \
                           ValErr(-0.000592579, 0.0108898, 0), \
                           ValErr(-0.000136911, 5.58259e-05, 0), \
                           -86195.5, 58528, 58528, -nan)
reports[-1].sigmaresid = ValErr(1.05526, 0.00308433, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00665924, None, -4.64137e-06, None, 0.00893247, None, 2.05141e-05, None, 0.00893247, None, 2.05141e-05, None, 0.00796602, None, -3.62944e-06, None, 0.00796602, None, -3.62944e-06, None, 1.05536, None, 0.00749052, None, 1.05536, None, 0.00749052, None)

reports.append(Report(604025984, ("CSC", 1, 3, 2, 16), "MEp32_16"))
reports[-1].posNum = 52180
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000275883, 0.00759125, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.311606, 0.220905, 0), \
                           ValErr(-0.00189583, 0.00247555, 0), \
                           ValErr(0.0051852, 0.011647, 0), \
                           ValErr(-2.57234e-05, 5.79623e-05, 0), \
                           -75312.9, 52180, 52180, -nan)
reports[-1].sigmaresid = ValErr(1.02469, 0.00317194, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000374368, None, 3.18704e-05, None, 0.000798773, None, 6.05574e-05, None, 0.000798773, None, 6.05574e-05, None, -6.79649e-05, None, 4.12393e-05, None, -6.79649e-05, None, 4.12393e-05, None, 1.02472, None, 0.0069661, None, 1.02472, None, 0.0069661, None)

reports.append(Report(604026000, ("CSC", 1, 3, 2, 18), "MEp32_18"))
reports[-1].posNum = 54379
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0190299, 0.00737844, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.203663, 0.191783, 0), \
                           ValErr(0.00151638, 0.00192402, 0), \
                           ValErr(0.0261335, 0.0109706, 0), \
                           ValErr(6.40017e-05, 5.17068e-05, 0), \
                           -79352.4, 54379, 54379, -nan)
reports[-1].sigmaresid = ValErr(1.04113, 0.0031502, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0081671, None, 2.16123e-05, None, -0.00564905, None, 1.07378e-05, None, -0.00564905, None, 1.07378e-05, None, -0.0100729, None, 2.82302e-05, None, -0.0100729, None, 2.82302e-05, None, 1.0412, None, 0.00813531, None, 1.0412, None, 0.00813531, None)

reports.append(Report(604026016, ("CSC", 1, 3, 2, 20), "MEp32_20"))
reports[-1].posNum = 55782
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00719064, 0.00726673, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0468921, 0.21149, 0), \
                           ValErr(0.00206193, 0.00236839, 0), \
                           ValErr(-0.0209831, 0.0110395, 0), \
                           ValErr(0.000100526, 5.6272e-05, 0), \
                           -81375.9, 55782, 55782, -nan)
reports[-1].sigmaresid = ValErr(1.04069, 0.00311573, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0126091, None, 3.90309e-06, None, -0.0119215, None, -1.91392e-05, None, -0.0119215, None, -1.91392e-05, None, -0.00751338, None, 2.2507e-05, None, -0.00751338, None, 2.2507e-05, None, 1.04079, None, 0.00702404, None, 1.04079, None, 0.00702404, None)

reports.append(Report(604026032, ("CSC", 1, 3, 2, 22), "MEp32_22"))
reports[-1].posNum = 52707
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0026646, 0.00725539, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0756116, 0.201739, 0), \
                           ValErr(-0.000881778, 0.00241185, 0), \
                           ValErr(0.0179983, 0.0114603, 0), \
                           ValErr(-3.57657e-05, 5.82034e-05, 0), \
                           -76273.1, 52707, 52707, -nan)
reports[-1].sigmaresid = ValErr(1.02858, 0.0030664, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.001772, None, 3.76956e-06, None, 0.00316816, None, -1.63744e-06, None, 0.00316816, None, -1.63744e-06, None, 0.00283541, None, -4.57449e-05, None, 0.00283541, None, -4.57449e-05, None, 1.02862, None, 0.00704949, None, 1.02862, None, 0.00704949, None)

reports.append(Report(604026048, ("CSC", 1, 3, 2, 24), "MEp32_24"))
reports[-1].posNum = 57830
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00818119, 0.00707049, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.141953, 0.207099, 0), \
                           ValErr(0.00110834, 0.0023528, 0), \
                           ValErr(-0.00532536, 0.0107762, 0), \
                           ValErr(1.38113e-05, 5.54107e-05, 0), \
                           -84625.4, 57830, 57830, -nan)
reports[-1].sigmaresid = ValErr(1.04541, 0.00307394, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00772852, None, 3.28051e-06, None, -0.00984936, None, 6.65739e-06, None, -0.00984936, None, 6.65739e-06, None, -0.00744946, None, -2.0889e-05, None, -0.00744946, None, -2.0889e-05, None, 1.04542, None, 0.00728306, None, 1.04542, None, 0.00728306, None)

reports.append(Report(604026064, ("CSC", 1, 3, 2, 26), "MEp32_26"))
reports[-1].posNum = 51819
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00280119, 0.0078191, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.552365, 0.219029, 0), \
                           ValErr(-0.00479207, 0.00244353, 0), \
                           ValErr(0.00859368, 0.0117335, 0), \
                           ValErr(-6.12747e-05, 5.93483e-05, 0), \
                           -74648.9, 51819, 51819, -nan)
reports[-1].sigmaresid = ValErr(1.02186, 0.00317419, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00515975, None, 6.815e-06, None, -0.00226274, None, -1.58482e-05, None, -0.00226274, None, -1.58482e-05, None, -0.00201454, None, -1.19848e-05, None, -0.00201454, None, -1.19848e-05, None, 1.02198, None, 0.00719424, None, 1.02198, None, 0.00719424, None)

reports.append(Report(604026080, ("CSC", 1, 3, 2, 28), "MEp32_28"))
reports[-1].posNum = 59800
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000634542, 0.00713262, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.428845, 0.204253, 0), \
                           ValErr(0.0010847, 0.00231761, 0), \
                           ValErr(0.00167015, 0.010778, 0), \
                           ValErr(-2.03119e-05, 5.53452e-05, 0), \
                           -88429.5, 59800, 59800, -nan)
reports[-1].sigmaresid = ValErr(1.06164, 0.00306964, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00323627, None, -2.11754e-05, None, -0.000663125, None, -4.99168e-06, None, -0.000663125, None, -4.99168e-06, None, 0.00567925, None, -1.56158e-05, None, 0.00567925, None, -1.56158e-05, None, 1.06168, None, 0.00858798, None, 1.06168, None, 0.00858798, None)

reports.append(Report(604026096, ("CSC", 1, 3, 2, 30), "MEp32_30"))
reports[-1].posNum = 50992
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00263123, 0.00762963, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0597979, 0.219423, 0), \
                           ValErr(0.00136393, 0.00242343, 0), \
                           ValErr(0.0125804, 0.0115763, 0), \
                           ValErr(1.79194e-05, 5.78716e-05, 0), \
                           -72812.2, 50992, 50992, -nan)
reports[-1].sigmaresid = ValErr(1.00902, 0.0031596, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00762354, None, -2.94127e-06, None, 0.0032512, None, 2.97114e-05, None, 0.0032512, None, 2.97114e-05, None, -0.00152057, None, 1.17334e-05, None, -0.00152057, None, 1.17334e-05, None, 1.00903, None, 0.00735866, None, 1.00903, None, 0.00735866, None)

reports.append(Report(604026112, ("CSC", 1, 3, 2, 32), "MEp32_32"))
reports[-1].posNum = 57999
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00019845, 0.00715505, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.207386, 0.206984, 0), \
                           ValErr(0.00317724, 0.00234372, 0), \
                           ValErr(-0.00452705, 0.010877, 0), \
                           ValErr(6.65459e-05, 5.56918e-05, 0), \
                           -85108, 57999, 57999, -nan)
reports[-1].sigmaresid = ValErr(1.04966, 0.00308249, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00582878, None, 1.5673e-05, None, 0.000303679, None, 5.43309e-06, None, 0.000303679, None, 5.43309e-06, None, 9.29127e-05, None, -1.95318e-06, None, 9.29127e-05, None, -1.95318e-06, None, 1.04971, None, 0.00743609, None, 1.04971, None, 0.00743609, None)

reports.append(Report(604026128, ("CSC", 1, 3, 2, 34), "MEp32_34"))
reports[-1].posNum = 53484
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00957686, 0.00755349, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.233687, 0.215906, 0), \
                           ValErr(0.00625446, 0.00243525, 0), \
                           ValErr(0.00163645, 0.0109339, 0), \
                           ValErr(-4.91088e-05, 4.56899e-05, 0), \
                           -77787.9, 53484, 53484, -nan)
reports[-1].sigmaresid = ValErr(1.03611, 0.00316778, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0140154, None, -8.06883e-05, None, -0.0112124, None, -5.95871e-05, None, -0.0112124, None, -5.95871e-05, None, -0.0113131, None, -6.72808e-05, None, -0.0113131, None, -6.72808e-05, None, 1.03618, None, 0.00688744, None, 1.03618, None, 0.00688744, None)

reports.append(Report(604026144, ("CSC", 1, 3, 2, 36), "MEp32_36"))
reports[-1].posNum = 56164
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00902702, 0.00721195, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0150256, 0.118957, 0), \
                           ValErr(0.000563557, 0.00116238, 0), \
                           ValErr(-0.00864102, 0.010938, 0), \
                           ValErr(1.38611e-05, 5.44151e-05, 0), \
                           -81625.8, 56164, 56164, -nan)
reports[-1].sigmaresid = ValErr(1.03501, 0.00308396, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00682266, None, -2.32847e-05, None, 0.00599701, None, -5.47288e-05, None, 0.00599701, None, -5.47288e-05, None, 0.00178853, None, -8.81308e-05, None, 0.00178853, None, -8.81308e-05, None, 1.03502, None, 0.00749689, None, 1.03502, None, 0.00749689, None)

reports.append(Report(604029448, ("CSC", 1, 4, 1, 1), "MEp41_01"))
reports[-1].posNum = 135449
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00217382, 0.00235654, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.191207, 0.0680968, 0), \
                           ValErr(-0.000580782, 0.00174426, 0), \
                           ValErr(0.000576528, 0.00297786, 0), \
                           ValErr(1.81118e-05, 4.35341e-05, 0), \
                           -119030, 135449, 135449, -nan)
reports[-1].sigmaresid = ValErr(0.582654, 0.00111946, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00128635, None, 2.58045e-06, None, 0.00254897, None, 3.92268e-06, None, 0.00254897, None, 3.92268e-06, None, 0.00076356, None, 3.84288e-05, None, 0.00076356, None, 3.84288e-05, None, 0.582672, None, 0.0060258, None, 0.582672, None, 0.0060258, None)

reports.append(Report(604029464, ("CSC", 1, 4, 1, 3), "MEp41_03"))
reports[-1].posNum = 135627
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00389878, 0.00235902, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0252965, 0.0685469, 0), \
                           ValErr(0.000937472, 0.00175235, 0), \
                           ValErr(-0.0032159, 0.00298576, 0), \
                           ValErr(-4.67769e-05, 4.35277e-05, 0), \
                           -119919, 135627, 135627, -nan)
reports[-1].sigmaresid = ValErr(0.585812, 0.00112479, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0025914, None, -1.16382e-06, None, 0.00195491, None, 3.49591e-05, None, 0.00195491, None, 3.49591e-05, None, 0.00111967, None, 6.19582e-06, None, 0.00111967, None, 6.19582e-06, None, 0.585819, None, 0.00600607, None, 0.585819, None, 0.00600607, None)

reports.append(Report(604029480, ("CSC", 1, 4, 1, 5), "MEp41_05"))
reports[-1].posNum = 135908
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00129823, 0.00236244, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0644884, 0.0684848, 0), \
                           ValErr(-0.00355905, 0.00175269, 0), \
                           ValErr(0.000670026, 0.0029875, 0), \
                           ValErr(9.57662e-06, 4.36774e-05, 0), \
                           -120307, 135908, 135908, -nan)
reports[-1].sigmaresid = ValErr(0.586411, 0.00112477, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000276226, None, -5.77085e-06, None, -0.000880239, None, 8.82414e-06, None, -0.000880239, None, 8.82414e-06, None, -0.00229568, None, 2.383e-06, None, -0.00229568, None, 2.383e-06, None, 0.586422, None, 0.00574917, None, 0.586422, None, 0.00574917, None)

reports.append(Report(604029496, ("CSC", 1, 4, 1, 7), "MEp41_07"))
reports[-1].posNum = 136338
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00126716, 0.00234825, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00497364, 0.0682836, 0), \
                           ValErr(-0.000964181, 0.0017453, 0), \
                           ValErr(-0.000340663, 0.00297483, 0), \
                           ValErr(6.71317e-05, 4.34533e-05, 0), \
                           -120194, 136338, 136338, -nan)
reports[-1].sigmaresid = ValErr(0.584292, 0.00111894, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000722607, None, 1.01992e-07, None, -0.00130238, None, 5.02863e-06, None, -0.00130238, None, 5.02863e-06, None, -0.000158539, None, 2.03682e-05, None, -0.000158539, None, 2.03682e-05, None, 0.584299, None, 0.00590631, None, 0.584299, None, 0.00590631, None)

reports.append(Report(604029512, ("CSC", 1, 4, 1, 9), "MEp41_09"))
reports[-1].posNum = 135720
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000516963, 0.00235333, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0115968, 0.0681622, 0), \
                           ValErr(-0.00097075, 0.00174433, 0), \
                           ValErr(0.000514135, 0.00297521, 0), \
                           ValErr(7.97925e-06, 4.34554e-05, 0), \
                           -119356, 135720, 135720, -nan)
reports[-1].sigmaresid = ValErr(0.583033, 0.00111907, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00113478, None, 8.37288e-06, None, -0.000200571, None, 8.57058e-05, None, -0.000200571, None, 8.57058e-05, None, -0.00399538, None, 3.82842e-05, None, -0.00399538, None, 3.82842e-05, None, 0.583035, None, 0.0145238, None, 0.583035, None, 0.0145238, None)

reports.append(Report(604029528, ("CSC", 1, 4, 1, 11), "MEp41_11"))
reports[-1].posNum = 136525
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000947372, 0.00233068, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0326777, 0.0677817, 0), \
                           ValErr(5.09228e-05, 0.00173208, 0), \
                           ValErr(-0.00447397, 0.0029528, 0), \
                           ValErr(7.43372e-05, 4.30338e-05, 0), \
                           -119526, 136525, 136525, -nan)
reports[-1].sigmaresid = ValErr(0.58074, 0.00111137, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00219468, None, -2.56522e-06, None, -0.0014441, None, -1.33408e-05, None, -0.0014441, None, -1.33408e-05, None, -0.00227283, None, -1.85202e-05, None, -0.00227283, None, -1.85202e-05, None, 0.580757, None, 0.00586831, None, 0.580757, None, 0.00586831, None)

reports.append(Report(604029544, ("CSC", 1, 4, 1, 13), "MEp41_13"))
reports[-1].posNum = 135849
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00185032, 0.00233206, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0368461, 0.0568059, 0), \
                           ValErr(0.00123859, 0.00151238, 0), \
                           ValErr(0.00564823, 0.00296113, 0), \
                           ValErr(4.27515e-06, 3.8725e-05, 0), \
                           -118879, 135849, 135849, -nan)
reports[-1].sigmaresid = ValErr(0.580504, 0.00110332, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000357588, None, 2.85813e-06, None, 0.00138751, None, 1.52497e-05, None, 0.00138751, None, 1.52497e-05, None, 0.000990419, None, -5.3538e-06, None, 0.000990419, None, -5.3538e-06, None, 0.580514, None, 0.0058564, None, 0.580514, None, 0.0058564, None)

reports.append(Report(604029560, ("CSC", 1, 4, 1, 15), "MEp41_15"))
reports[-1].posNum = 114438
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00683614, 0.00256249, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00248675, 0.0733276, 0), \
                           ValErr(-0.000702339, 0.00188049, 0), \
                           ValErr(0.00917988, 0.0030674, 0), \
                           ValErr(0.000152808, 4.77579e-05, 0), \
                           -100532, 114438, 114438, -nan)
reports[-1].sigmaresid = ValErr(0.582482, 0.00121753, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00146002, None, -1.66698e-05, None, -0.000885494, None, -8.66594e-05, None, -0.000885494, None, -8.66594e-05, None, -0.000270351, None, 5.88966e-05, None, -0.000270351, None, 5.88966e-05, None, 0.582522, None, 0.00834953, None, 0.582522, None, 0.00834953, None)

reports.append(Report(604029576, ("CSC", 1, 4, 1, 17), "MEp41_17"))
reports[-1].posNum = 135684
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000446915, 0.00236686, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0370135, 0.0687656, 0), \
                           ValErr(-0.000660927, 0.00176386, 0), \
                           ValErr(-0.00119601, 0.00300269, 0), \
                           ValErr(1.83154e-05, 4.37463e-05, 0), \
                           -120387, 135684, 135684, -nan)
reports[-1].sigmaresid = ValErr(0.587619, 0.00112802, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00037077, None, -1.86863e-05, None, -0.00108522, None, 3.29526e-05, None, -0.00108522, None, 3.29526e-05, None, -0.00259609, None, 2.01401e-05, None, -0.00259609, None, 2.01401e-05, None, 0.587622, None, 0.00578829, None, 0.587622, None, 0.00578829, None)

reports.append(Report(604029456, ("CSC", 1, 4, 1, 2), "MEp41_02"))
reports[-1].posNum = 138482
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0040561, 0.00237942, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00122647, 0.0705547, 0), \
                           ValErr(-0.000364173, 0.00180624, 0), \
                           ValErr(-0.00747159, 0.00308287, 0), \
                           ValErr(5.57157e-05, 4.40708e-05, 0), \
                           -124579, 138482, 138482, -nan)
reports[-1].sigmaresid = ValErr(0.594915, 0.00113043, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00147077, None, -1.06228e-05, None, 2.05407e-05, None, -5.8977e-06, None, 2.05407e-05, None, -5.8977e-06, None, 8.37315e-05, None, -1.02648e-05, None, 8.37315e-05, None, -1.02648e-05, None, 0.594939, None, 0.00565319, None, 0.594939, None, 0.00565319, None)

reports.append(Report(604029472, ("CSC", 1, 4, 1, 4), "MEp41_04"))
reports[-1].posNum = 138329
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00262293, 0.00237572, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0389729, 0.0599081, 0), \
                           ValErr(0.000740266, 0.00155456, 0), \
                           ValErr(-0.00272952, 0.00308826, 0), \
                           ValErr(4.64158e-05, 3.87078e-05, 0), \
                           -125038, 138329, 138329, -nan)
reports[-1].sigmaresid = ValErr(0.597487, 0.00113391, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00286798, None, -2.18627e-05, None, -0.00403284, None, -2.63498e-05, None, -0.00403284, None, -2.63498e-05, None, -0.00413829, None, -1.94247e-05, None, -0.00413829, None, -1.94247e-05, None, 0.597494, None, 0.00543151, None, 0.597494, None, 0.00543151, None)

reports.append(Report(604029488, ("CSC", 1, 4, 1, 6), "MEp41_06"))
reports[-1].posNum = 137800
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000319699, 0.00240422, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0202465, 0.0713452, 0), \
                           ValErr(-0.00228044, 0.00182602, 0), \
                           ValErr(-4.48004e-07, 0.00311146, 0), \
                           ValErr(3.49402e-05, 4.44836e-05, 0), \
                           -125250, 137800, 137800, -nan)
reports[-1].sigmaresid = ValErr(0.600487, 0.00114383, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(2.32431e-05, None, -1.03217e-05, None, 0.000381365, None, 2.64e-05, None, 0.000381365, None, 2.64e-05, None, -0.00244577, None, 6.37933e-07, None, -0.00244577, None, 6.37933e-07, None, 0.600495, None, 0.00588108, None, 0.600495, None, 0.00588108, None)

reports.append(Report(604029504, ("CSC", 1, 4, 1, 8), "MEp41_08"))
reports[-1].posNum = 137760
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00166578, 0.00239519, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.017525, 0.0713039, 0), \
                           ValErr(-0.00244087, 0.0018244, 0), \
                           ValErr(0.000417961, 0.00310762, 0), \
                           ValErr(-4.89957e-05, 4.43665e-05, 0), \
                           -124889, 137760, 137760, -nan)
reports[-1].sigmaresid = ValErr(0.599075, 0.00114132, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00283784, None, -1.27973e-05, None, -0.00152904, None, -6.49107e-06, None, -0.00152904, None, -6.49107e-06, None, -0.00117494, None, 6.20482e-06, None, -0.00117494, None, 6.20482e-06, None, 0.599081, None, 0.0053792, None, 0.599081, None, 0.0053792, None)

reports.append(Report(604029520, ("CSC", 1, 4, 1, 10), "MEp41_10"))
reports[-1].posNum = 138412
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00348136, 0.00239604, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0205648, 0.0713848, 0), \
                           ValErr(0.0011338, 0.0018323, 0), \
                           ValErr(0.00197492, 0.00311194, 0), \
                           ValErr(1.81108e-05, 4.4456e-05, 0), \
                           -125887, 138412, 138412, -nan)
reports[-1].sigmaresid = ValErr(0.600836, 0.00114197, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00281667, None, -5.67066e-06, None, -0.00233596, None, -7.92798e-06, None, -0.00233596, None, -7.92798e-06, None, -0.00459721, None, -3.77782e-05, None, -0.00459721, None, -3.77782e-05, None, 0.600839, None, 0.00547133, None, 0.600839, None, 0.00547133, None)

reports.append(Report(604029536, ("CSC", 1, 4, 1, 12), "MEp41_12"))
reports[-1].posNum = 138341
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00175845, 0.00239676, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.121261, 0.057992, 0), \
                           ValErr(-6.52094e-05, 0.00165849, 0), \
                           ValErr(0.00140909, 0.00310911, 0), \
                           ValErr(-1.50076e-05, 3.87391e-05, 0), \
                           -126106, 138341, 138341, -nan)
reports[-1].sigmaresid = ValErr(0.602072, 0.001139, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00253157, None, -5.02343e-06, None, 0.0025045, None, -2.03447e-06, None, 0.0025045, None, -2.03447e-06, None, -0.000367401, None, -2.92429e-05, None, -0.000367401, None, -2.92429e-05, None, 0.602079, None, 0.00555193, None, 0.602079, None, 0.00555193, None)

reports.append(Report(604029552, ("CSC", 1, 4, 1, 14), "MEp41_14"))
reports[-1].posNum = 139033
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00438943, 0.00239909, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0246607, 0.0710431, 0), \
                           ValErr(0.000519779, 0.00181941, 0), \
                           ValErr(0.00469559, 0.00310527, 0), \
                           ValErr(9.56304e-05, 4.43153e-05, 0), \
                           -126563, 139033, 139033, -nan)
reports[-1].sigmaresid = ValErr(0.60132, 0.00114033, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00183118, None, -2.03186e-05, None, -0.00153204, None, -1.02399e-05, None, -0.00153204, None, -1.02399e-05, None, -0.000442499, None, -2.78439e-05, None, -0.000442499, None, -2.78439e-05, None, 0.601332, None, 0.00566765, None, 0.601332, None, 0.00566765, None)

reports.append(Report(604029568, ("CSC", 1, 4, 1, 16), "MEp41_16"))
reports[-1].posNum = 138557
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00262554, 0.00239325, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.00050961, 0.071296, 0), \
                           ValErr(0.00121454, 0.00182253, 0), \
                           ValErr(0.00394422, 0.00311525, 0), \
                           ValErr(4.17107e-06, 4.43424e-05, 0), \
                           -125780, 138557, 138557, -nan)
reports[-1].sigmaresid = ValErr(0.599803, 0.00113941, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00238568, None, -7.0599e-06, None, -0.000420573, None, -4.0762e-06, None, -0.000420573, None, -4.0762e-06, None, 0.000757584, None, 1.72753e-05, None, 0.000757584, None, 1.72753e-05, None, 0.599808, None, 0.00554572, None, 0.599808, None, 0.00554572, None)

reports.append(Report(604029584, ("CSC", 1, 4, 1, 18), "MEp41_18"))
reports[-1].posNum = 138276
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00276293, 0.00240277, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0476443, 0.071223, 0), \
                           ValErr(0.000410026, 0.00182223, 0), \
                           ValErr(-0.00141264, 0.00310637, 0), \
                           ValErr(-2.58258e-05, 4.44655e-05, 0), \
                           -125687, 138276, 138276, -nan)
reports[-1].sigmaresid = ValErr(0.600507, 0.0011419, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00348633, None, -1.57393e-06, None, 0.00191251, None, -1.55301e-05, None, 0.00191251, None, -1.55301e-05, None, 0.00264324, None, -1.98083e-05, None, 0.00264324, None, -1.98083e-05, None, 0.600509, None, 0.00578948, None, 0.600509, None, 0.00578948, None)

reports.append(Report(604029960, ("CSC", 1, 4, 2, 1), "MEp42_01"))
reports[-1].posNum = 60289
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0175502, 0.00736138, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.241122, 0.225476, 0), \
                           ValErr(-0.0034034, 0.00262705, 0), \
                           ValErr(0.0323544, 0.0118985, 0), \
                           ValErr(7.33147e-05, 5.83738e-05, 0), \
                           -91343.8, 60289, 60289, -nan)
reports[-1].sigmaresid = ValErr(1.10094, 0.0031705, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00421662, None, -4.61077e-05, None, -0.00196186, None, -3.5928e-06, None, -0.00196186, None, -3.5928e-06, None, 0.00616136, None, -5.50647e-05, None, 0.00616136, None, -5.50647e-05, None, 1.10103, None, 0.00752706, None, 1.10103, None, 0.00752706, None)

reports.append(Report(604029976, ("CSC", 1, 4, 2, 3), "MEp42_03"))
reports[-1].posNum = 55090
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0130653, 0.0077252, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.618774, 0.234302, 0), \
                           ValErr(0.00298705, 0.00267473, 0), \
                           ValErr(0.0095508, 0.0124457, 0), \
                           ValErr(0.000114735, 6.02103e-05, 0), \
                           -81525.1, 55090, 55090, -nan)
reports[-1].sigmaresid = ValErr(1.06281, 0.00320187, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000245819, None, 8.01147e-06, None, -0.00430235, None, 7.11632e-05, None, -0.00430235, None, 7.11632e-05, None, -0.00441688, None, 4.33668e-05, None, -0.00441688, None, 4.33668e-05, None, 1.06291, None, 0.00720606, None, 1.06291, None, 0.00720606, None)

reports.append(Report(604029992, ("CSC", 1, 4, 2, 5), "MEp42_05"))
reports[-1].posNum = 60728
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000406032, 0.00720037, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.240398, 0.225892, 0), \
                           ValErr(0.00146802, 0.00260809, 0), \
                           ValErr(0.0103662, 0.0118059, 0), \
                           ValErr(1.64871e-05, 5.70444e-05, 0), \
                           -91604, 60728, 60728, -nan)
reports[-1].sigmaresid = ValErr(1.09362, 0.00313802, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00608686, None, 1.74667e-05, None, 0.00427876, None, 3.7803e-05, None, 0.00427876, None, 3.7803e-05, None, -0.000148932, None, 2.4969e-05, None, -0.000148932, None, 2.4969e-05, None, 1.09364, None, 0.00732442, None, 1.09364, None, 0.00732442, None)

reports.append(Report(604030008, ("CSC", 1, 4, 2, 7), "MEp42_07"))
reports[-1].posNum = 54919
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00952203, 0.00789293, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.440057, 0.234591, 0), \
                           ValErr(-0.00213085, 0.00269607, 0), \
                           ValErr(0.0122026, 0.0125228, 0), \
                           ValErr(8.88636e-05, 6.14173e-05, 0), \
                           -81852.6, 54919, 54919, -nan)
reports[-1].sigmaresid = ValErr(1.07411, 0.00324095, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00510424, None, -1.62944e-05, None, -0.000978966, None, -7.08314e-06, None, -0.000978966, None, -7.08314e-06, None, -0.000165103, None, -2.93921e-06, None, -0.000165103, None, -2.93921e-06, None, 1.07417, None, 0.00723645, None, 1.07417, None, 0.00723645, None)

reports.append(Report(604030024, ("CSC", 1, 4, 2, 9), "MEp42_09"))
reports[-1].posNum = 56434
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00225056, 0.00746264, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.640191, 0.235167, 0), \
                           ValErr(-0.00181161, 0.00267965, 0), \
                           ValErr(0.0213052, 0.012243, 0), \
                           ValErr(5.22208e-05, 5.87525e-05, 0), \
                           -84582.2, 56434, 56434, -nan)
reports[-1].sigmaresid = ValErr(1.08312, 0.00322397, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00586775, None, -1.2838e-05, None, 0.00825807, None, 2.84629e-05, None, 0.00825807, None, 2.84629e-05, None, 0.0136043, None, 9.26898e-06, None, 0.0136043, None, 9.26898e-06, None, 1.08323, None, 0.00725438, None, 1.08323, None, 0.00725438, None)

reports.append(Report(604030040, ("CSC", 1, 4, 2, 11), "MEp42_11"))
reports[-1].posNum = 56065
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0118087, 0.00745106, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0330652, 0.210169, 0), \
                           ValErr(-0.00545895, 0.00254483, 0), \
                           ValErr(-0.00262509, 0.0118509, 0), \
                           ValErr(6.82538e-05, 5.02599e-05, 0), \
                           -83530.4, 56065, 56065, -nan)
reports[-1].sigmaresid = ValErr(1.07352, 0.00318808, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00921773, None, -3.1696e-05, None, -0.0100004, None, -4.61167e-06, None, -0.0100004, None, -4.61167e-06, None, -0.00777701, None, 6.32739e-06, None, -0.00777701, None, 6.32739e-06, None, 1.07358, None, 0.00714855, None, 1.07358, None, 0.00714855, None)

reports.append(Report(604030056, ("CSC", 1, 4, 2, 13), "MEp42_13"))
reports[-1].posNum = 54469
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000783952, 0.00795191, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.124687, 0.234811, 0), \
                           ValErr(0.00144135, 0.00269051, 0), \
                           ValErr(0.0153487, 0.0125398, 0), \
                           ValErr(3.3828e-05, 6.19884e-05, 0), \
                           -81148.8, 54469, 54469, -nan)
reports[-1].sigmaresid = ValErr(1.07345, 0.00325231, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00665845, None, 2.39559e-05, None, 0.00690805, None, 6.20673e-05, None, 0.00690805, None, 6.20673e-05, None, 0.00814155, None, 4.22897e-05, None, 0.00814155, None, 4.22897e-05, None, 1.07347, None, 0.00731791, None, 1.07347, None, 0.00731791, None)

reports.append(Report(604030072, ("CSC", 1, 4, 2, 15), "MEp42_15"))
reports[-1].posNum = 60719
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00141349, 0.00716224, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.378029, 0.223538, 0), \
                           ValErr(-0.000414126, 0.00257717, 0), \
                           ValErr(-0.00152354, 0.0116899, 0), \
                           ValErr(-2.71533e-06, 5.68068e-05, 0), \
                           -91380.9, 60719, 60719, -nan)
reports[-1].sigmaresid = ValErr(1.08984, 0.0031274, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00270128, None, 1.90675e-06, None, 0.000708329, None, -1.23425e-06, None, 0.000708329, None, -1.23425e-06, None, -0.000539726, None, -9.48814e-06, None, -0.000539726, None, -9.48814e-06, None, 1.08988, None, 0.00750312, None, 1.08988, None, 0.00750312, None)

reports.append(Report(604030088, ("CSC", 1, 4, 2, 17), "MEp42_17"))
reports[-1].posNum = 54848
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00246226, 0.00781854, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0561146, 0.238007, 0), \
                           ValErr(-0.00533908, 0.00273519, 0), \
                           ValErr(0.00545622, 0.0118293, 0), \
                           ValErr(2.34843e-05, 4.67711e-05, 0), \
                           -81523, 54848, 54848, -nan)
reports[-1].sigmaresid = ValErr(1.06973, 0.00323052, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00268591, None, -2.06025e-05, None, 0.000668172, None, 2.42978e-06, None, 0.000668172, None, 2.42978e-06, None, 0.00395094, None, -4.81877e-05, None, 0.00395094, None, -4.81877e-05, None, 1.06977, None, 0.00750177, None, 1.06977, None, 0.00750177, None)

reports.append(Report(604030104, ("CSC", 1, 4, 2, 19), "MEp42_19"))
reports[-1].posNum = 61079
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-5.41221e-07, 0.00732509, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.526073, 0.223612, 0), \
                           ValErr(-0.00325052, 0.00261144, 0), \
                           ValErr(-0.00781879, 0.0118518, 0), \
                           ValErr(-0.000114631, 5.79835e-05, 0), \
                           -92339.5, 61079, 61079, -nan)
reports[-1].sigmaresid = ValErr(1.09732, 0.00313957, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0118236, None, 5.14366e-06, None, -0.00728473, None, 3.48331e-05, None, -0.00728473, None, 3.48331e-05, None, -0.00408814, None, 2.1587e-05, None, -0.00408814, None, 2.1587e-05, None, 1.09742, None, 0.00730395, None, 1.09742, None, 0.00730395, None)

reports.append(Report(604030120, ("CSC", 1, 4, 2, 21), "MEp42_21"))
reports[-1].posNum = 55387
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00107678, 0.0076967, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.265446, 0.181999, 0), \
                           ValErr(-0.00613631, 0.00205597, 0), \
                           ValErr(0.013039, 0.012235, 0), \
                           ValErr(-4.94081e-05, 5.72783e-05, 0), \
                           -81868.9, 55387, 55387, -nan)
reports[-1].sigmaresid = ValErr(1.06097, 0.00318825, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00274703, None, 1.38356e-07, None, 0.00397157, None, 3.90277e-05, None, 0.00397157, None, 3.90277e-05, None, 0.00174006, None, 1.34259e-05, None, 0.00174006, None, 1.34259e-05, None, 1.06108, None, 0.00719766, None, 1.06108, None, 0.00719766, None)

reports.append(Report(604030136, ("CSC", 1, 4, 2, 23), "MEp42_23"))
reports[-1].posNum = 60437
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0105455, 0.00727851, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.119492, 0.224317, 0), \
                           ValErr(-0.00460383, 0.00260108, 0), \
                           ValErr(-0.00225694, 0.011837, 0), \
                           ValErr(-6.43535e-05, 5.75532e-05, 0), \
                           -91080.5, 60437, 60437, -nan)
reports[-1].sigmaresid = ValErr(1.09209, 0.00314118, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00677185, None, -4.31011e-05, None, 0.00736623, None, -3.86813e-05, None, 0.00736623, None, -3.86813e-05, None, 0.00882049, None, -2.85925e-05, None, 0.00882049, None, -2.85925e-05, None, 1.09214, None, 0.00836625, None, 1.09214, None, 0.00836625, None)

reports.append(Report(604030152, ("CSC", 1, 4, 2, 25), "MEp42_25"))
reports[-1].posNum = 56380
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0055397, 0.00772358, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.278545, 0.230332, 0), \
                           ValErr(-0.00301315, 0.00264879, 0), \
                           ValErr(-0.00425496, 0.0122501, 0), \
                           ValErr(-5.64832e-05, 6.02808e-05, 0), \
                           -84191.9, 56380, 56380, -nan)
reports[-1].sigmaresid = ValErr(1.07719, 0.00320787, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000746453, None, 4.71884e-05, None, 0.00144486, None, 7.68614e-05, None, 0.00144486, None, 7.68614e-05, None, -0.0024499, None, 5.74398e-05, None, -0.0024499, None, 5.74398e-05, None, 1.07723, None, 0.0072156, None, 1.07723, None, 0.0072156, None)

reports.append(Report(604030168, ("CSC", 1, 4, 2, 27), "MEp42_27"))
reports[-1].posNum = 57587
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00181792, 0.00743435, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.444944, 0.232062, 0), \
                           ValErr(0.00339561, 0.00264851, 0), \
                           ValErr(-0.00391165, 0.0121725, 0), \
                           ValErr(-6.39404e-05, 5.82953e-05, 0), \
                           -86391.3, 57587, 57587, -nan)
reports[-1].sigmaresid = ValErr(1.08464, 0.00319602, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00960632, None, 1.73232e-06, None, -0.00532941, None, 1.47798e-05, None, -0.00532941, None, 1.47798e-05, None, -0.0126106, None, -3.70722e-05, None, -0.0126106, None, -3.70722e-05, None, 1.0847, None, 0.0071085, None, 1.0847, None, 0.0071085, None)

reports.append(Report(604030184, ("CSC", 1, 4, 2, 29), "MEp42_29"))
reports[-1].posNum = 58126
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00814502, 0.00740002, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.430971, 0.231427, 0), \
                           ValErr(-0.00138231, 0.00265285, 0), \
                           ValErr(0.0210254, 0.0120915, 0), \
                           ValErr(8.92583e-05, 5.84797e-05, 0), \
                           -87165, 58126, 58126, -nan)
reports[-1].sigmaresid = ValErr(1.08399, 0.00317926, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00378267, None, 2.40802e-05, None, 0.00320889, None, 5.53039e-05, None, 0.00320889, None, 5.53039e-05, None, 0.00310845, None, 3.17522e-05, None, 0.00310845, None, 3.17522e-05, None, 1.08406, None, 0.00712614, None, 1.08406, None, 0.00712614, None)

reports.append(Report(604030200, ("CSC", 1, 4, 2, 31), "MEp42_31"))
reports[-1].posNum = 55942
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.010285, 0.00782264, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.650686, 0.23225, 0), \
                           ValErr(-0.00263295, 0.00269088, 0), \
                           ValErr(-0.0093929, 0.0124396, 0), \
                           ValErr(-9.87872e-05, 6.09845e-05, 0), \
                           -83419.7, 55942, 55942, -nan)
reports[-1].sigmaresid = ValErr(1.07492, 0.0032136, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00283573, None, -1.14919e-05, None, 0.00242609, None, 8.32518e-05, None, 0.00242609, None, 8.32518e-05, None, -0.00167166, None, 2.00566e-05, None, -0.00167166, None, 2.00566e-05, None, 1.07504, None, 0.00916399, None, 1.07504, None, 0.00916399, None)

reports.append(Report(604030216, ("CSC", 1, 4, 2, 33), "MEp42_33"))
reports[-1].posNum = 60206
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0147457, 0.00723309, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.19565, 0.224885, 0), \
                           ValErr(-0.00157066, 0.00259371, 0), \
                           ValErr(-0.0229135, 0.0117673, 0), \
                           ValErr(-0.000123313, 5.73226e-05, 0), \
                           -90602.7, 60206, 60206, -nan)
reports[-1].sigmaresid = ValErr(1.08974, 0.00314042, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0060374, None, 6.16939e-05, None, 0.00121949, None, 0.000130465, None, 0.00121949, None, 0.000130465, None, -0.000822095, None, 6.33644e-05, None, -0.000822095, None, 6.33644e-05, None, 1.08981, None, 0.00737881, None, 1.08981, None, 0.00737881, None)

reports.append(Report(604030232, ("CSC", 1, 4, 2, 35), "MEp42_35"))
reports[-1].posNum = 54160
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00821192, 0.00782116, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.377595, 0.235595, 0), \
                           ValErr(-0.00275876, 0.00271441, 0), \
                           ValErr(0.00312516, 0.0125702, 0), \
                           ValErr(6.45502e-05, 6.09535e-05, 0), \
                           -79500.3, 54160, 54160, -nan)
reports[-1].sigmaresid = ValErr(1.05016, 0.00319081, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00878544, None, 5.50854e-05, None, -0.00407332, None, 6.53173e-05, None, -0.00407332, None, 6.53173e-05, None, -0.00673279, None, 6.18254e-05, None, -0.00673279, None, 6.18254e-05, None, 1.05021, None, 0.00754743, None, 1.05021, None, 0.00754743, None)

reports.append(Report(604029968, ("CSC", 1, 4, 2, 2), "MEp42_02"))
reports[-1].posNum = 58797
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0112908, 0.00751212, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.871573, 0.241383, 0), \
                           ValErr(0.00633316, 0.00280004, 0), \
                           ValErr(0.0128622, 0.0126139, 0), \
                           ValErr(8.2579e-05, 5.96948e-05, 0), \
                           -89272.9, 58797, 58797, -nan)
reports[-1].sigmaresid = ValErr(1.10449, 0.00322085, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000541115, None, -5.08589e-05, None, -0.00377684, None, -6.94248e-05, None, -0.00377684, None, -6.94248e-05, None, -0.0116854, None, -0.000113099, None, -0.0116854, None, -0.000113099, None, 1.10466, None, 0.00728407, None, 1.10466, None, 0.00728407, None)

reports.append(Report(604029984, ("CSC", 1, 4, 2, 4), "MEp42_04"))
reports[-1].posNum = 57712
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00842571, 0.00772928, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.299805, 0.170566, 0), \
                           ValErr(-0.00168898, 0.00223918, 0), \
                           ValErr(-0.00256605, 0.0128492, 0), \
                           ValErr(-9.80712e-05, 6.11518e-05, 0), \
                           -87558.9, 57712, 57712, -nan)
reports[-1].sigmaresid = ValErr(1.10322, 0.0031965, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00510848, None, -3.09387e-05, None, 0.00341936, None, -5.05059e-06, None, 0.00341936, None, -5.05059e-06, None, 0.00433683, None, -2.51063e-05, None, 0.00433683, None, -2.51063e-05, None, 1.10326, None, 0.00692954, None, 1.10326, None, 0.00692954, None)

reports.append(Report(604030000, ("CSC", 1, 4, 2, 6), "MEp42_06"))
reports[-1].posNum = 60922
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0045189, 0.0072805, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.107001, 0.123238, 0), \
                           ValErr(0.000332828, 0.0018893, 0), \
                           ValErr(-0.00654407, 0.0119105, 0), \
                           ValErr(1.46668e-05, 5.15436e-05, 0), \
                           -92550.4, 60922, 60922, -nan)
reports[-1].sigmaresid = ValErr(1.10542, 0.0031631, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0027144, None, -3.90564e-07, None, 0.00248909, None, -3.61395e-05, None, 0.00248909, None, -3.61395e-05, None, 0.00586418, None, 4.31497e-06, None, 0.00586418, None, 4.31497e-06, None, 1.10542, None, 0.00723075, None, 1.10542, None, 0.00723075, None)

reports.append(Report(604030016, ("CSC", 1, 4, 2, 8), "MEp42_08"))
reports[-1].posNum = 55141
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00217852, 0.00795762, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0673517, 0.191115, 0), \
                           ValErr(-0.00206223, 0.00238217, 0), \
                           ValErr(-0.00440424, 0.0128179, 0), \
                           ValErr(-6.22446e-05, 5.96355e-05, 0), \
                           -82428.8, 55141, 55141, -nan)
reports[-1].sigmaresid = ValErr(1.07889, 0.0032331, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00639116, None, -6.05973e-05, None, -0.00226531, None, -5.89108e-05, None, -0.00226531, None, -5.89108e-05, None, -0.00369959, None, -5.07936e-05, None, -0.00369959, None, -5.07936e-05, None, 1.07891, None, 0.00710655, None, 1.07891, None, 0.00710655, None)

reports.append(Report(604030032, ("CSC", 1, 4, 2, 10), "MEp42_10"))
reports[-1].posNum = 62794
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.015565, 0.00728535, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0230559, 0.140949, 0), \
                           ValErr(-0.00263398, 0.00201238, 0), \
                           ValErr(-0.0119126, 0.0118552, 0), \
                           ValErr(-6.53886e-05, 4.85619e-05, 0), \
                           -96531, 62794, 62794, -nan)
reports[-1].sigmaresid = ValErr(1.12561, 0.00316849, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00869893, None, 4.65647e-07, None, 0.00872647, None, -4.46799e-06, None, 0.00872647, None, -4.46799e-06, None, 0.00987143, None, -2.71638e-06, None, 0.00987143, None, -2.71638e-06, None, 1.12563, None, 0.00691112, None, 1.12563, None, 0.00691112, None)

reports.append(Report(604030048, ("CSC", 1, 4, 2, 12), "MEp42_12"))
reports[-1].posNum = 55696
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00322196, 0.00765888, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.15222, 0.203119, 0), \
                           ValErr(-0.00161836, 0.00239201, 0), \
                           ValErr(0.00132358, 0.0128205, 0), \
                           ValErr(-7.81431e-06, 5.99567e-05, 0), \
                           -83162.1, 55696, 55696, -nan)
reports[-1].sigmaresid = ValErr(1.07703, 0.0032247, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0083338, None, -9.04483e-06, None, -0.00293248, None, -3.87269e-06, None, -0.00293248, None, -3.87269e-06, None, 0.00322996, None, -3.37036e-05, None, 0.00322996, None, -3.37036e-05, None, 1.07703, None, 0.00712297, None, 1.07703, None, 0.00712297, None)

reports.append(Report(604030064, ("CSC", 1, 4, 2, 14), "MEp42_14"))
reports[-1].posNum = 61561
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(5.78141e-05, 0.00729964, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.366486, 0.231122, 0), \
                           ValErr(-0.00205002, 0.00269983, 0), \
                           ValErr(0.0172439, 0.0121602, 0), \
                           ValErr(2.1165e-06, 5.8226e-05, 0), \
                           -93635, 61561, 61561, -nan)
reports[-1].sigmaresid = ValErr(1.10746, 0.00315619, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00465702, None, 6.41913e-06, None, 0.00680556, None, 5.30122e-05, None, 0.00680556, None, 5.30122e-05, None, 0.00760025, None, 2.54392e-05, None, 0.00760025, None, 2.54392e-05, None, 1.10751, None, 0.00730523, None, 1.10751, None, 0.00730523, None)

reports.append(Report(604030080, ("CSC", 1, 4, 2, 16), "MEp42_16"))
reports[-1].posNum = 57031
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000286558, 0.00771422, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0301612, 0.243839, 0), \
                           ValErr(-0.00196042, 0.00284129, 0), \
                           ValErr(0.012457, 0.0128608, 0), \
                           ValErr(1.70372e-05, 6.07561e-05, 0), \
                           -85744.7, 57031, 57031, -nan)
reports[-1].sigmaresid = ValErr(1.08821, 0.00322213, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00667305, None, -1.35507e-05, None, 0.00572916, None, -1.28169e-05, None, 0.00572916, None, -1.28169e-05, None, 0.015307, None, -5.6346e-07, None, 0.015307, None, -5.6346e-07, None, 1.08823, None, 0.00723277, None, 1.08823, None, 0.00723277, None)

reports.append(Report(604030096, ("CSC", 1, 4, 2, 18), "MEp42_18"))
reports[-1].posNum = 58303
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00756039, 0.00756512, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.232779, 0.241208, 0), \
                           ValErr(-0.00694227, 0.00277523, 0), \
                           ValErr(0.0165464, 0.0126093, 0), \
                           ValErr(4.05467e-05, 5.96028e-05, 0), \
                           -88517.4, 58303, 58303, -nan)
reports[-1].sigmaresid = ValErr(1.10439, 0.00323416, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00282979, None, -2.92594e-06, None, 0.000160306, None, 1.45537e-06, None, 0.000160306, None, 1.45537e-06, None, 0.000355652, None, 1.66728e-05, None, 0.000355652, None, 1.66728e-05, None, 1.10447, None, 0.00798688, None, 1.10447, None, 0.00798688, None)

reports.append(Report(604030112, ("CSC", 1, 4, 2, 20), "MEp42_20"))
reports[-1].posNum = 59736
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00227316, 0.00744159, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.458395, 0.23771, 0), \
                           ValErr(0.000293927, 0.00276981, 0), \
                           ValErr(-0.0132924, 0.0124284, 0), \
                           ValErr(2.28212e-05, 5.91242e-05, 0), \
                           -90624, 59736, 59736, -nan)
reports[-1].sigmaresid = ValErr(1.10311, 0.00319145, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00188202, None, 1.02e-05, None, -0.00658848, None, 1.38583e-05, None, -0.00658848, None, 1.38583e-05, None, -0.0117272, None, -2.49101e-06, None, -0.0117272, None, -2.49101e-06, None, 1.10317, None, 0.00709399, None, 1.10317, None, 0.00709399, None)

reports.append(Report(604030128, ("CSC", 1, 4, 2, 22), "MEp42_22"))
reports[-1].posNum = 57349
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0141971, 0.00767577, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.756355, 0.24123, 0), \
                           ValErr(0.000487844, 0.00281859, 0), \
                           ValErr(-0.0151211, 0.0127318, 0), \
                           ValErr(-7.00775e-05, 6.06884e-05, 0), \
                           -86428.8, 57349, 57349, -nan)
reports[-1].sigmaresid = ValErr(1.09213, 0.00322475, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00965353, None, 2.97909e-05, None, 0.00570232, None, -1.06726e-05, None, 0.00570232, None, -1.06726e-05, None, 0.00988428, None, 8.65306e-06, None, 0.00988428, None, 8.65306e-06, None, 1.09224, None, 0.00724123, None, 1.09224, None, 0.00724123, None)

reports.append(Report(604030144, ("CSC", 1, 4, 2, 24), "MEp42_24"))
reports[-1].posNum = 61577
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00281234, 0.00716667, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.178191, 0.23054, 0), \
                           ValErr(-0.00471133, 0.00270326, 0), \
                           ValErr(-0.012854, 0.012032, 0), \
                           ValErr(-6.80549e-06, 5.71781e-05, 0), \
                           -93258.9, 61577, 61577, -nan)
reports[-1].sigmaresid = ValErr(1.10029, 0.00313532, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00708495, None, -4.30657e-05, None, -0.00803259, None, -4.06642e-05, None, -0.00803259, None, -4.06642e-05, None, -0.00784268, None, -1.62649e-05, None, -0.00784268, None, -1.62649e-05, None, 1.10033, None, 0.00719251, None, 1.10033, None, 0.00719251, None)

reports.append(Report(604030160, ("CSC", 1, 4, 2, 26), "MEp42_26"))
reports[-1].posNum = 56591
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00718217, 0.00787397, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.3805, 0.243655, 0), \
                           ValErr(-0.000347025, 0.00283078, 0), \
                           ValErr(0.0115552, 0.0130124, 0), \
                           ValErr(-7.64517e-05, 6.20476e-05, 0), \
                           -85026.2, 56591, 56591, -nan)
reports[-1].sigmaresid = ValErr(1.08712, 0.00323139, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0059996, None, -1.08294e-05, None, -0.00620635, None, -2.08749e-06, None, -0.00620635, None, -2.08749e-06, None, 0.000812322, None, -2.69085e-05, None, 0.000812322, None, -2.69085e-05, None, 1.08718, None, 0.00736173, None, 1.08718, None, 0.00736173, None)

reports.append(Report(604030176, ("CSC", 1, 4, 2, 28), "MEp42_28"))
reports[-1].posNum = 62266
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00622406, 0.00734489, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.859591, 0.230757, 0), \
                           ValErr(-0.00143863, 0.00271708, 0), \
                           ValErr(-0.0020502, 0.0121505, 0), \
                           ValErr(-3.39909e-05, 5.8711e-05, 0), \
                           -95524.5, 62266, 62266, -nan)
reports[-1].sigmaresid = ValErr(1.12209, 0.00317972, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0131602, None, -3.48318e-05, None, -0.00820356, None, -7.30541e-05, None, -0.00820356, None, -7.30541e-05, None, -0.00479341, None, -6.96907e-05, None, -0.00479341, None, -6.96907e-05, None, 1.12223, None, 0.00708987, None, 1.12223, None, 0.00708987, None)

reports.append(Report(604030192, ("CSC", 1, 4, 2, 30), "MEp42_30"))
reports[-1].posNum = 55207
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00350198, 0.00778885, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.136504, 0.244131, 0), \
                           ValErr(-0.00576113, 0.00280805, 0), \
                           ValErr(0.00696312, 0.0128542, 0), \
                           ValErr(-7.81922e-07, 6.13628e-05, 0), \
                           -82129, 55207, 55207, -nan)
reports[-1].sigmaresid = ValErr(1.07113, 0.00322354, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0117123, None, 3.78041e-05, None, 0.00620737, None, 8.00466e-05, None, 0.00620737, None, 8.00466e-05, None, 0.0088208, None, 9.7549e-05, None, 0.0088208, None, 9.7549e-05, None, 1.07119, None, 0.00731105, None, 1.07119, None, 0.00731105, None)

reports.append(Report(604030208, ("CSC", 1, 4, 2, 32), "MEp42_32"))
reports[-1].posNum = 61222
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0149925, 0.00732796, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0371426, 0.164022, 0), \
                           ValErr(-7.18007e-05, 0.00244691, 0), \
                           ValErr(-0.00448704, 0.0122417, 0), \
                           ValErr(0.000122162, 5.83009e-05, 0), \
                           -93116.6, 61222, 61222, -nan)
reports[-1].sigmaresid = ValErr(1.10742, 0.00316028, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00935797, None, 2.15815e-05, None, -0.0123027, None, -2.26568e-05, None, -0.0123027, None, -2.26568e-05, None, -0.0138668, None, -1.73957e-05, None, -0.0138668, None, -1.73957e-05, None, 1.10747, None, 0.00719568, None, 1.10747, None, 0.00719568, None)

reports.append(Report(604030224, ("CSC", 1, 4, 2, 34), "MEp42_34"))
reports[-1].posNum = 58104
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.019029, 0.00769962, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.155001, 0.244073, 0), \
                           ValErr(-0.00170196, 0.00285734, 0), \
                           ValErr(0.0130946, 0.0128554, 0), \
                           ValErr(0.000135596, 6.10984e-05, 0), \
                           -88425.8, 58104, 58104, -nan)
reports[-1].sigmaresid = ValErr(1.1084, 0.00325145, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0065474, None, -5.65932e-05, None, -0.00852688, None, -9.84336e-05, None, -0.00852688, None, -9.84336e-05, None, -0.0113742, None, -6.76547e-05, None, -0.0113742, None, -6.76547e-05, None, 1.10845, None, 0.00718036, None, 1.10845, None, 0.00718036, None)

reports.append(Report(604030240, ("CSC", 1, 4, 2, 36), "MEp42_36"))
reports[-1].posNum = 59913
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0099057, 0.0073757, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.669972, 0.236073, 0), \
                           ValErr(0.00424042, 0.0027505, 0), \
                           ValErr(-0.00127988, 0.0123364, 0), \
                           ValErr(5.34596e-05, 5.86802e-05, 0), \
                           -90796.4, 59913, 59913, -nan)
reports[-1].sigmaresid = ValErr(1.10135, 0.00318162, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0106733, None, 3.40135e-05, None, 0.0116677, None, 6.91127e-05, None, 0.0116677, None, 6.91127e-05, None, 0.0132808, None, 7.45211e-05, None, 0.0132808, None, 7.45211e-05, None, 1.10144, None, 0.0071934, None, 1.10144, None, 0.0071934, None)

reports.append(Report(604050440, ("CSC", 2, 1, 1, 1), "MEm11_01"))
reports[-1].posNum = 101176
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00230271, 0.000817334, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.165732, 0.0492389, 0), \
                           ValErr(-0.00250291, 0.00125322, 0), \
                           ValErr(-0.00319209, 0.00609956, 0), \
                           ValErr(3.36858e-06, 1.73087e-05, 0), \
                           22975.5, 101176, 101176, -nan)
reports[-1].sigmaresid = ValErr(0.192815, 0.000428635, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00218461, None, 3.16293e-06, None, 0.00259342, None, -5.50186e-06, None, 0.00259342, None, -5.50186e-06, None, 0.00278227, None, -4.84552e-06, None, 0.00278227, None, -4.84552e-06, None, 0.192827, None, 0.00421437, None, 0.192827, None, 0.00421437, None)

reports.append(Report(604050456, ("CSC", 2, 1, 1, 3), "MEm11_03"))
reports[-1].posNum = 101415
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00339544, 0.000806338, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.128882, 0.0485761, 0), \
                           ValErr(-0.00246269, 0.00124365, 0), \
                           ValErr(0.00535015, 0.00603763, 0), \
                           ValErr(-1.42011e-05, 1.71462e-05, 0), \
                           24223.4, 101415, 101415, -nan)
reports[-1].sigmaresid = ValErr(0.190559, 0.000423119, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00248256, None, -1.44227e-05, None, 0.00288982, None, -3.5851e-06, None, 0.00288982, None, -3.5851e-06, None, 0.00251611, None, -2.5598e-06, None, 0.00251611, None, -2.5598e-06, None, 0.190568, None, 0.00416835, None, 0.190568, None, 0.00416835, None)

reports.append(Report(604050472, ("CSC", 2, 1, 1, 5), "MEm11_05"))
reports[-1].posNum = 101188
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000541788, 0.000821369, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0105343, 0.0495512, 0), \
                           ValErr(0.00063261, 0.00127106, 0), \
                           ValErr(-0.00544419, 0.00615855, 0), \
                           ValErr(-2.63466e-05, 1.74925e-05, 0), \
                           22555.6, 101188, 101188, -nan)
reports[-1].sigmaresid = ValErr(0.193622, 0.000430403, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000574936, None, 5.65287e-06, None, 0.000902375, None, -3.39214e-05, None, 0.000902375, None, -3.39214e-05, None, -0.00112639, None, -1.18255e-05, None, -0.00112639, None, -1.18255e-05, None, 0.193627, None, 0.00454542, None, 0.193627, None, 0.00454542, None)

reports.append(Report(604050488, ("CSC", 2, 1, 1, 7), "MEm11_07"))
reports[-1].posNum = 101073
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00123095, 0.000816094, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0213431, 0.0493025, 0), \
                           ValErr(0.000526165, 0.00125381, 0), \
                           ValErr(-0.00823196, 0.00613291, 0), \
                           ValErr(-5.30696e-06, 1.72985e-05, 0), \
                           23179.6, 101073, 101073, -nan)
reports[-1].sigmaresid = ValErr(0.192382, 0.000427889, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00156902, None, 1.10668e-05, None, 0.00190724, None, 1.78245e-05, None, 0.00190724, None, 1.78245e-05, None, 0.00167969, None, 1.64397e-05, None, 0.00167969, None, 1.64397e-05, None, 0.192385, None, 0.00409993, None, 0.192385, None, 0.00409993, None)

reports.append(Report(604050504, ("CSC", 2, 1, 1, 9), "MEm11_09"))
reports[-1].posNum = 101368
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000267157, 0.00082375, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0742679, 0.0493297, 0), \
                           ValErr(0.000232311, 0.00126175, 0), \
                           ValErr(-0.0107081, 0.00614928, 0), \
                           ValErr(-1.16261e-06, 1.74708e-05, 0), \
                           22454.7, 101368, 101368, -nan)
reports[-1].sigmaresid = ValErr(0.193892, 0.000430621, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00137152, None, -7.13301e-06, None, 0.00118003, None, -2.58424e-05, None, 0.00118003, None, -2.58424e-05, None, -0.000452209, None, 1.71683e-05, None, -0.000452209, None, 1.71683e-05, None, 0.193898, None, 0.00468673, None, 0.193898, None, 0.00468673, None)

reports.append(Report(604050520, ("CSC", 2, 1, 1, 11), "MEm11_11"))
reports[-1].posNum = 101467
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00137322, 0.000822555, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.103744, 0.0493256, 0), \
                           ValErr(4.50501e-05, 0.00126485, 0), \
                           ValErr(0.00108879, 0.00612475, 0), \
                           ValErr(3.98626e-06, 1.74688e-05, 0), \
                           22390.3, 101467, 101467, -nan)
reports[-1].sigmaresid = ValErr(0.194057, 0.000430777, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00125472, None, 8.25262e-06, None, 0.00129309, None, 1.97264e-05, None, 0.00129309, None, 1.97264e-05, None, -0.000880912, None, 2.09487e-05, None, -0.000880912, None, 2.09487e-05, None, 0.194062, None, 0.00423606, None, 0.194062, None, 0.00423606, None)

reports.append(Report(604050536, ("CSC", 2, 1, 1, 13), "MEm11_13"))
reports[-1].posNum = 101317
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000946452, 0.000821461, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.188847, 0.0494249, 0), \
                           ValErr(-0.000964093, 0.00126152, 0), \
                           ValErr(-0.00432751, 0.00614384, 0), \
                           ValErr(2.62407e-05, 1.74277e-05, 0), \
                           22561.2, 101317, 101317, -nan)
reports[-1].sigmaresid = ValErr(0.193666, 0.000430227, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.001392, None, 2.30545e-06, None, 0.00142657, None, 4.82485e-06, None, 0.00142657, None, 4.82485e-06, None, 0.00163755, None, 1.33279e-05, None, 0.00163755, None, 1.33279e-05, None, 0.193683, None, 0.00422271, None, 0.193683, None, 0.00422271, None)

reports.append(Report(604050552, ("CSC", 2, 1, 1, 15), "MEm11_15"))
reports[-1].posNum = 101595
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00263283, 0.000818553, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.119695, 0.0492597, 0), \
                           ValErr(-0.0010159, 0.00125391, 0), \
                           ValErr(0.000729534, 0.006115, 0), \
                           ValErr(-2.2606e-05, 1.73182e-05, 0), \
                           22878.6, 101595, 101595, -nan)
reports[-1].sigmaresid = ValErr(0.19318, 0.00042856, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00240251, None, 1.35507e-05, None, 0.00248509, None, -6.56038e-06, None, 0.00248509, None, -6.56038e-06, None, 0.00160502, None, 1.71582e-06, None, 0.00160502, None, 1.71582e-06, None, 0.193187, None, 0.00490626, None, 0.193187, None, 0.00490626, None)

reports.append(Report(604050568, ("CSC", 2, 1, 1, 17), "MEm11_17"))
reports[-1].posNum = 100511
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00275589, 0.000815587, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0132865, 0.0490042, 0), \
                           ValErr(0.000176917, 0.00125335, 0), \
                           ValErr(0.00180458, 0.00613015, 0), \
                           ValErr(-3.35019e-05, 1.72949e-05, 0), \
                           23633.6, 100511, 100511, -nan)
reports[-1].sigmaresid = ValErr(0.191269, 0.000426603, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00256161, None, -4.54609e-06, None, 0.00246862, None, 7.92349e-06, None, 0.00246862, None, 7.92349e-06, None, 0.00241415, None, 2.79091e-05, None, 0.00241415, None, 2.79091e-05, None, 0.191273, None, 0.0041688, None, 0.191273, None, 0.0041688, None)

reports.append(Report(604050584, ("CSC", 2, 1, 1, 19), "MEm11_19"))
reports[-1].posNum = 102098
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00297879, 0.000814822, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.17381, 0.0493088, 0), \
                           ValErr(-0.00118127, 0.00125303, 0), \
                           ValErr(0.00491734, 0.00612147, 0), \
                           ValErr(-3.74899e-05, 1.72732e-05, 0), \
                           22890.8, 102098, 102098, -nan)
reports[-1].sigmaresid = ValErr(0.193372, 0.000427927, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00287644, None, 5.81931e-07, None, 0.00243948, None, -9.13559e-06, None, 0.00243948, None, -9.13559e-06, None, 0.000876051, None, 1.51748e-05, None, 0.000876051, None, 1.51748e-05, None, 0.193388, None, 0.00430959, None, 0.193388, None, 0.00430959, None)

reports.append(Report(604050600, ("CSC", 2, 1, 1, 21), "MEm11_21"))
reports[-1].posNum = 100831
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00209746, 0.000816497, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0140467, 0.0492608, 0), \
                           ValErr(-0.000424525, 0.00125967, 0), \
                           ValErr(-0.00616249, 0.00609844, 0), \
                           ValErr(-8.07311e-06, 1.73333e-05, 0), \
                           23106.8, 100831, 100831, -nan)
reports[-1].sigmaresid = ValErr(0.192415, 0.000428476, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00275496, None, -5.50731e-06, None, 0.00259455, None, 2.7854e-06, None, 0.00259455, None, 2.7854e-06, None, 0.0011469, None, 2.52638e-05, None, 0.0011469, None, 2.52638e-05, None, 0.192417, None, 0.00412737, None, 0.192417, None, 0.00412737, None)

reports.append(Report(604050616, ("CSC", 2, 1, 1, 23), "MEm11_23"))
reports[-1].posNum = 101314
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0018166, 0.000817805, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.157494, 0.0493387, 0), \
                           ValErr(-3.33556e-05, 0.00125672, 0), \
                           ValErr(-0.00390397, 0.00609905, 0), \
                           ValErr(-1.43952e-05, 1.73408e-05, 0), \
                           22642.1, 101314, 101314, -nan)
reports[-1].sigmaresid = ValErr(0.193511, 0.000429888, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00122928, None, 1.27663e-06, None, 0.00211023, None, 1.03749e-05, None, 0.00211023, None, 1.03749e-05, None, 7.26888e-05, None, 5.81058e-06, None, 7.26888e-05, None, 5.81058e-06, None, 0.193524, None, 0.00423513, None, 0.193524, None, 0.00423513, None)

reports.append(Report(604050632, ("CSC", 2, 1, 1, 25), "MEm11_25"))
reports[-1].posNum = 101082
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00338386, 0.000815401, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0634015, 0.0491242, 0), \
                           ValErr(-0.000759356, 0.00125429, 0), \
                           ValErr(0.00160397, 0.00609791, 0), \
                           ValErr(-4.68831e-05, 1.7278e-05, 0), \
                           23358.2, 101082, 101082, -nan)
reports[-1].sigmaresid = ValErr(0.192046, 0.000427123, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00213889, None, 3.05224e-06, None, 0.00307368, None, -6.45276e-06, None, 0.00307368, None, -6.45276e-06, None, 0.00173606, None, 6.90499e-06, None, 0.00173606, None, 6.90499e-06, None, 0.192055, None, 0.00471253, None, 0.192055, None, 0.00471253, None)

reports.append(Report(604050648, ("CSC", 2, 1, 1, 27), "MEm11_27"))
reports[-1].posNum = 100775
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0014878, 0.000824811, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0142345, 0.049539, 0), \
                           ValErr(-0.00193754, 0.00126266, 0), \
                           ValErr(-0.0138763, 0.00613486, 0), \
                           ValErr(8.05406e-06, 1.74926e-05, 0), \
                           22377.9, 100775, 100775, -nan)
reports[-1].sigmaresid = ValErr(0.193787, 0.000431651, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00234092, None, 8.53035e-06, None, 0.00272181, None, -2.61051e-05, None, 0.00272181, None, -2.61051e-05, None, 0.00225181, None, 1.7597e-05, None, 0.00225181, None, 1.7597e-05, None, 0.193794, None, 0.00666312, None, 0.193794, None, 0.00666312, None)

reports.append(Report(604050664, ("CSC", 2, 1, 1, 29), "MEm11_29"))
reports[-1].posNum = 101009
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00179876, 0.000820761, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.149405, 0.0493848, 0), \
                           ValErr(-0.00156478, 0.00126241, 0), \
                           ValErr(0.00566633, 0.00614486, 0), \
                           ValErr(-2.29455e-06, 1.74011e-05, 0), \
                           22702.9, 101009, 101009, -nan)
reports[-1].sigmaresid = ValErr(0.193264, 0.000429987, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00175736, None, 7.40435e-06, None, 0.00132597, None, 1.6765e-06, None, 0.00132597, None, 1.6765e-06, None, 0.000644143, None, 1.88037e-05, None, 0.000644143, None, 1.88037e-05, None, 0.193273, None, 0.00407373, None, 0.193273, None, 0.00407373, None)

reports.append(Report(604050680, ("CSC", 2, 1, 1, 31), "MEm11_31"))
reports[-1].posNum = 101085
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00237323, 0.000821049, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0582014, 0.0491308, 0), \
                           ValErr(-0.00113621, 0.00125554, 0), \
                           ValErr(-0.00670135, 0.00612963, 0), \
                           ValErr(-2.59844e-05, 1.7383e-05, 0), \
                           22976.7, 101085, 101085, -nan)
reports[-1].sigmaresid = ValErr(0.192774, 0.000428735, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00247636, None, 5.49972e-06, None, 0.00285633, None, 1.86375e-05, None, 0.00285633, None, 1.86375e-05, None, 0.0010847, None, 5.82748e-05, None, 0.0010847, None, 5.82748e-05, None, 0.19278, None, 0.0047609, None, 0.19278, None, 0.0047609, None)

reports.append(Report(604050696, ("CSC", 2, 1, 1, 33), "MEm11_33"))
reports[-1].posNum = 101915
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00191496, 0.000821315, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.039099, 0.0495079, 0), \
                           ValErr(-0.00048186, 0.00125478, 0), \
                           ValErr(-0.000567728, 0.00611379, 0), \
                           ValErr(-3.75418e-06, 1.7425e-05, 0), \
                           22236.4, 101915, 101915, -nan)
reports[-1].sigmaresid = ValErr(0.194539, 0.000430895, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00160814, None, 8.33557e-07, None, 0.0019529, None, 8.88457e-06, None, 0.0019529, None, 8.88457e-06, None, 0.00162256, None, 1.61901e-05, None, 0.00162256, None, 1.61901e-05, None, 0.194539, None, 0.00444715, None, 0.194539, None, 0.00444715, None)

reports.append(Report(604050712, ("CSC", 2, 1, 1, 35), "MEm11_35"))
reports[-1].posNum = 101238
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00176872, 0.000808367, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0721509, 0.0486252, 0), \
                           ValErr(0.000478167, 0.00124701, 0), \
                           ValErr(-0.0104562, 0.0061002, 0), \
                           ValErr(2.19322e-05, 1.71087e-05, 0), \
                           24331.4, 101238, 101238, -nan)
reports[-1].sigmaresid = ValErr(0.190277, 0.000422862, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00217474, None, -1.28798e-06, None, 0.00274567, None, -1.73347e-06, None, 0.00274567, None, -1.73347e-06, None, 0.00317024, None, 3.50803e-05, None, 0.00317024, None, 3.50803e-05, None, 0.190283, None, 0.00495235, None, 0.190283, None, 0.00495235, None)

reports.append(Report(604050448, ("CSC", 2, 1, 1, 2), "MEm11_02"))
reports[-1].posNum = 100455
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00262917, 0.000737973, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0416747, 0.0419089, 0), \
                           ValErr(0.000178334, 0.00108028, 0), \
                           ValErr(-0.000113949, 0.00523949, 0), \
                           ValErr(-2.4801e-05, 1.67742e-05, 0), \
                           33820.8, 100455, 100455, -nan)
reports[-1].sigmaresid = ValErr(0.172801, 0.000385494, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0018844, None, -1.91115e-05, None, 0.00254252, None, -3.47894e-05, None, 0.00254252, None, -3.47894e-05, None, 0.00260131, None, -2.55114e-05, None, 0.00260131, None, -2.55114e-05, None, 0.172805, None, 0.00437461, None, 0.172805, None, 0.00437461, None)

reports.append(Report(604050464, ("CSC", 2, 1, 1, 4), "MEm11_04"))
reports[-1].posNum = 99541
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0017786, 0.000734227, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.122372, 0.0417986, 0), \
                           ValErr(-0.000218139, 0.00106928, 0), \
                           ValErr(-0.00240785, 0.0052043, 0), \
                           ValErr(4.68658e-06, 1.55714e-05, 0), \
                           34240.6, 99541, 99541, -nan)
reports[-1].sigmaresid = ValErr(0.171543, 0.000384465, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00117737, None, -1.00851e-05, None, 0.00201087, None, -2.73583e-05, None, 0.00201087, None, -2.73583e-05, None, 0.0026039, None, -1.80629e-05, None, 0.0026039, None, -1.80629e-05, None, 0.171551, None, 0.00437037, None, 0.171551, None, 0.00437037, None)

reports.append(Report(604050480, ("CSC", 2, 1, 1, 6), "MEm11_06"))
reports[-1].posNum = 100542
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00230654, 0.000737273, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0630826, 0.0419342, 0), \
                           ValErr(0.000368037, 0.0010765, 0), \
                           ValErr(0.00812835, 0.0051997, 0), \
                           ValErr(-3.07883e-05, 1.56734e-05, 0), \
                           33659.4, 100542, 100542, -nan)
reports[-1].sigmaresid = ValErr(0.173129, 0.000386082, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00140951, None, 1.49475e-06, None, 0.00144458, None, -2.36067e-05, None, 0.00144458, None, -2.36067e-05, None, 0.000480527, None, 1.3995e-05, None, 0.000480527, None, 1.3995e-05, None, 0.173136, None, 0.00448722, None, 0.173136, None, 0.00448722, None)

reports.append(Report(604050496, ("CSC", 2, 1, 1, 8), "MEm11_08"))
reports[-1].posNum = 99695
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00248247, 0.00073317, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.075328, 0.0418632, 0), \
                           ValErr(-0.00145342, 0.00106697, 0), \
                           ValErr(0.00622464, 0.00519049, 0), \
                           ValErr(8.22008e-06, 1.55276e-05, 0), \
                           34218.6, 99695, 99695, -nan)
reports[-1].sigmaresid = ValErr(0.171672, 0.000384456, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00170302, None, -1.00986e-05, None, 0.00195263, None, -2.81387e-05, None, 0.00195263, None, -2.81387e-05, None, 0.00118002, None, -1.59084e-05, None, 0.00118002, None, -1.59084e-05, None, 0.171677, None, 0.00457326, None, 0.171677, None, 0.00457326, None)

reports.append(Report(604050512, ("CSC", 2, 1, 1, 10), "MEm11_10"))
reports[-1].posNum = 99827
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00340874, 0.000739224, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.109563, 0.0419542, 0), \
                           ValErr(1.42846e-05, 0.00107112, 0), \
                           ValErr(-0.00389388, 0.00524899, 0), \
                           ValErr(4.05185e-07, 1.56685e-05, 0), \
                           33620.5, 99827, 99827, -nan)
reports[-1].sigmaresid = ValErr(0.172782, 0.000386687, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00355932, None, -2.26463e-05, None, 0.00375461, None, -4.1828e-05, None, 0.00375461, None, -4.1828e-05, None, 0.00478016, None, -4.14968e-05, None, 0.00478016, None, -4.14968e-05, None, 0.172789, None, 0.00451128, None, 0.172789, None, 0.00451128, None)

reports.append(Report(604050528, ("CSC", 2, 1, 1, 12), "MEm11_12"))
reports[-1].posNum = 99700
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00261951, 0.000734348, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0594298, 0.041979, 0), \
                           ValErr(0.000308209, 0.00107265, 0), \
                           ValErr(0.000153683, 0.00522743, 0), \
                           ValErr(-1.78599e-05, 1.55323e-05, 0), \
                           34039.1, 99700, 99700, -nan)
reports[-1].sigmaresid = ValErr(0.171984, 0.000385146, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00261945, None, -6.73572e-06, None, 0.00252465, None, -2.56689e-05, None, 0.00252465, None, -2.56689e-05, None, 0.00101876, None, -3.64894e-06, None, 0.00101876, None, -3.64894e-06, None, 0.171988, None, 0.00475026, None, 0.171988, None, 0.00475026, None)

reports.append(Report(604050544, ("CSC", 2, 1, 1, 14), "MEm11_14"))
reports[-1].posNum = 99971
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00151604, 0.000732144, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.144895, 0.0419799, 0), \
                           ValErr(-0.00163591, 0.00106955, 0), \
                           ValErr(-0.00471608, 0.00519503, 0), \
                           ValErr(3.95417e-06, 1.55354e-05, 0), \
                           34026.5, 99971, 99971, -nan)
reports[-1].sigmaresid = ValErr(0.172165, 0.000385028, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0013439, None, 2.52794e-06, None, 0.00194815, None, -3.14843e-05, None, 0.00194815, None, -3.14843e-05, None, 0.0015809, None, -2.28985e-05, None, 0.0015809, None, -2.28985e-05, None, 0.172176, None, 0.00466665, None, 0.172176, None, 0.00466665, None)

reports.append(Report(604050560, ("CSC", 2, 1, 1, 16), "MEm11_16"))
reports[-1].posNum = 99907
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00252648, 0.000733805, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.105653, 0.0418976, 0), \
                           ValErr(-0.000951871, 0.00106779, 0), \
                           ValErr(0.00792217, 0.00521627, 0), \
                           ValErr(-4.89842e-06, 1.55558e-05, 0), \
                           34031, 99907, 99907, -nan)
reports[-1].sigmaresid = ValErr(0.17212, 0.00038505, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00177769, None, -3.98495e-06, None, 0.00179216, None, -1.31719e-05, None, 0.00179216, None, -1.31719e-05, None, 0.00103617, None, -1.04029e-05, None, 0.00103617, None, -1.04029e-05, None, 0.172127, None, 0.00435164, None, 0.172127, None, 0.00435164, None)

reports.append(Report(604050576, ("CSC", 2, 1, 1, 18), "MEm11_18"))
reports[-1].posNum = 100295
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00110066, 0.00073857, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0828565, 0.04183, 0), \
                           ValErr(-0.000338524, 0.0010652, 0), \
                           ValErr(-0.00277764, 0.00516197, 0), \
                           ValErr(-2.17085e-05, 1.65651e-05, 0), \
                           34223.5, 100295, 100295, -nan)
reports[-1].sigmaresid = ValErr(0.172016, 0.000385539, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000806818, None, 8.56819e-07, None, 0.00125921, None, -4.31587e-05, None, 0.00125921, None, -4.31587e-05, None, -0.000219131, None, -5.42732e-06, None, -0.000219131, None, -5.42732e-06, None, 0.172022, None, 0.00453471, None, 0.172022, None, 0.00453471, None)

reports.append(Report(604050592, ("CSC", 2, 1, 1, 20), "MEm11_20"))
reports[-1].posNum = 99610
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.002077, 0.000738004, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0738692, 0.0419856, 0), \
                           ValErr(-0.000777694, 0.00107453, 0), \
                           ValErr(0.000755185, 0.00524057, 0), \
                           ValErr(-1.14609e-05, 1.56263e-05, 0), \
                           33675, 99610, 99610, -nan)
reports[-1].sigmaresid = ValErr(0.17256, 0.000386612, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00252136, None, -9.53154e-06, None, 0.00196561, None, -2.95222e-05, None, 0.00196561, None, -2.95222e-05, None, 0.00137294, None, -1.73103e-05, None, 0.00137294, None, -1.73103e-05, None, 0.172564, None, 0.0044911, None, 0.172564, None, 0.0044911, None)

reports.append(Report(604050608, ("CSC", 2, 1, 1, 22), "MEm11_22"))
reports[-1].posNum = 99655
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00247558, 0.000732994, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.163941, 0.0419281, 0), \
                           ValErr(-0.00132841, 0.00107656, 0), \
                           ValErr(0.000364522, 0.00521552, 0), \
                           ValErr(2.53274e-05, 1.56044e-05, 0), \
                           34047.9, 99655, 99655, -nan)
reports[-1].sigmaresid = ValErr(0.171942, 0.000385139, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00244913, None, -9.37206e-06, None, 0.00256067, None, -2.41455e-05, None, 0.00256067, None, -2.41455e-05, None, 0.00198418, None, -2.50923e-05, None, 0.00198418, None, -2.50923e-05, None, 0.171958, None, 0.00453527, None, 0.171958, None, 0.00453527, None)

reports.append(Report(604050624, ("CSC", 2, 1, 1, 24), "MEm11_24"))
reports[-1].posNum = 99741
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00349319, 0.000736125, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.104811, 0.041906, 0), \
                           ValErr(-0.000210302, 0.00106598, 0), \
                           ValErr(0.00553472, 0.00519856, 0), \
                           ValErr(-3.59484e-05, 1.55621e-05, 0), \
                           33788.9, 99741, 99741, -nan)
reports[-1].sigmaresid = ValErr(0.17244, 0.000386088, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0032156, None, -1.5589e-05, None, 0.00285357, None, -1.2277e-05, None, 0.00285357, None, -1.2277e-05, None, 0.000935793, None, 3.77128e-06, None, 0.000935793, None, 3.77128e-06, None, 0.172451, None, 0.00462105, None, 0.172451, None, 0.00462105, None)

reports.append(Report(604050640, ("CSC", 2, 1, 1, 26), "MEm11_26"))
reports[-1].posNum = 100304
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0023118, 0.0007311, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.186665, 0.0416226, 0), \
                           ValErr(-0.00224405, 0.00106357, 0), \
                           ValErr(0.00537842, 0.00519434, 0), \
                           ValErr(-1.08779e-05, 1.54773e-05, 0), \
                           34453.9, 100304, 100304, -nan)
reports[-1].sigmaresid = ValErr(0.171627, 0.000383187, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00185987, None, -6.31917e-06, None, 0.001795, None, -2.9108e-05, None, 0.001795, None, -2.9108e-05, None, -0.00065407, None, -7.45536e-06, None, -0.00065407, None, -7.45536e-06, None, 0.171645, None, 0.0044208, None, 0.171645, None, 0.0044208, None)

reports.append(Report(604050656, ("CSC", 2, 1, 1, 28), "MEm11_28"))
reports[-1].posNum = 100208
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00221741, 0.000735052, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0699826, 0.0420142, 0), \
                           ValErr(-0.00151172, 0.00107277, 0), \
                           ValErr(-0.00332048, 0.00520069, 0), \
                           ValErr(-1.00999e-08, 1.561e-05, 0), \
                           33808.2, 100208, 100208, -nan)
reports[-1].sigmaresid = ValErr(0.172679, 0.000385722, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00315731, None, -5.80918e-06, None, 0.00251937, None, -1.65472e-05, None, 0.00251937, None, -1.65472e-05, None, 0.00199681, None, -1.13756e-05, None, 0.00199681, None, -1.13756e-05, None, 0.172683, None, 0.00431361, None, 0.172683, None, 0.00431361, None)

reports.append(Report(604050672, ("CSC", 2, 1, 1, 30), "MEm11_30"))
reports[-1].posNum = 100071
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000676427, 0.000733905, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.128597, 0.0417408, 0), \
                           ValErr(-0.00147173, 0.00106641, 0), \
                           ValErr(-0.00701343, 0.00518775, 0), \
                           ValErr(3.60693e-05, 1.55487e-05, 0), \
                           34113.2, 100071, 100071, -nan)
reports[-1].sigmaresid = ValErr(0.172074, 0.000384633, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00174795, None, -7.0886e-06, None, 0.00146425, None, -2.9919e-05, None, 0.00146425, None, -2.9919e-05, None, 0.00187907, None, -1.84899e-05, None, 0.00187907, None, -1.84899e-05, None, 0.172088, None, 0.00442001, None, 0.172088, None, 0.00442001, None)

reports.append(Report(604050688, ("CSC", 2, 1, 1, 32), "MEm11_32"))
reports[-1].posNum = 100336
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00222545, 0.000735039, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.210325, 0.0420382, 0), \
                           ValErr(-0.0022313, 0.0010719, 0), \
                           ValErr(0.00188883, 0.00522869, 0), \
                           ValErr(9.37567e-06, 1.55692e-05, 0), \
                           33780.3, 100336, 100336, -nan)
reports[-1].sigmaresid = ValErr(0.172802, 0.000385749, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00233371, None, -2.0564e-05, None, 0.00210588, None, -3.91778e-05, None, 0.00210588, None, -3.91778e-05, None, 0.00177393, None, -2.64328e-05, None, 0.00177393, None, -2.64328e-05, None, 0.172824, None, 0.00427236, None, 0.172824, None, 0.00427236, None)

reports.append(Report(604050704, ("CSC", 2, 1, 1, 34), "MEm11_34"))
reports[-1].posNum = 99839
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00156104, 0.000732256, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.1224, 0.0417096, 0), \
                           ValErr(-0.00167684, 0.00106788, 0), \
                           ValErr(-0.0069338, 0.00518049, 0), \
                           ValErr(-4.33642e-06, 1.55499e-05, 0), \
                           34250, 99839, 99839, -nan)
reports[-1].sigmaresid = ValErr(0.171702, 0.000384247, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00131108, None, 8.36442e-06, None, 0.00218316, None, -2.32876e-05, None, 0.00218316, None, -2.32876e-05, None, 0.00278171, None, -2.18512e-05, None, 0.00278171, None, -2.18512e-05, None, 0.171713, None, 0.0048512, None, 0.171713, None, 0.0048512, None)

reports.append(Report(604050720, ("CSC", 2, 1, 1, 36), "MEm11_36"))
reports[-1].posNum = 100175
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00201248, 0.00073854, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0507257, 0.0421625, 0), \
                           ValErr(-0.0011638, 0.00107727, 0), \
                           ValErr(-0.00209845, 0.00523764, 0), \
                           ValErr(-8.52136e-06, 1.56526e-05, 0), \
                           33402, 100175, 100175, -nan)
reports[-1].sigmaresid = ValErr(0.173362, 0.00038731, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00222171, None, -2.49945e-06, None, 0.00217102, None, -6.55403e-06, None, 0.00217102, None, -6.55403e-06, None, 0.000460557, None, -1.87969e-05, None, 0.000460557, None, -1.87969e-05, None, 0.173364, None, 0.00441549, None, 0.173364, None, 0.00441549, None)

reports.append(Report(604050952, ("CSC", 2, 1, 2, 1), "MEm12_01"))
reports[-1].posNum = 50471
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00161794, 0.00364277, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0217177, 0.106452, 0), \
                           ValErr(0.000584741, 0.00228757, 0), \
                           ValErr(0.00066976, 0.00779056, 0), \
                           ValErr(3.72789e-05, 5.732e-05, 0), \
                           -42602.9, 50471, 50471, -nan)
reports[-1].sigmaresid = ValErr(0.562799, 0.0017714, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000394233, None, -1.41116e-05, None, -0.0012764, None, -2.16226e-05, None, -0.0012764, None, -2.16226e-05, None, 0.00122768, None, -7.72262e-06, None, 0.00122768, None, -7.72262e-06, None, 0.562803, None, 0.00422907, None, 0.562803, None, 0.00422907, None)

reports.append(Report(604050968, ("CSC", 2, 1, 2, 3), "MEm12_03"))
reports[-1].posNum = 47541
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-5.57393e-05, 0.00367857, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0743519, 0.106217, 0), \
                           ValErr(0.00299542, 0.00228549, 0), \
                           ValErr(-0.0152176, 0.00784434, 0), \
                           ValErr(3.32961e-05, 5.7443e-05, 0), \
                           -38042.5, 47541, 47541, -nan)
reports[-1].sigmaresid = ValErr(0.538625, 0.00174677, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0051134, None, -9.93125e-06, None, 0.00502542, None, -1.57051e-05, None, 0.00502542, None, -1.57051e-05, None, 0.00997978, None, -2.10077e-05, None, 0.00997978, None, -2.10077e-05, None, 0.53866, None, 0.00414326, None, 0.53866, None, 0.00414326, None)

reports.append(Report(604050984, ("CSC", 2, 1, 2, 5), "MEm12_05"))
reports[-1].posNum = 50015
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00431838, 0.0035587, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.110398, 0.10728, 0), \
                           ValErr(-0.00364323, 0.00235406, 0), \
                           ValErr(0.0137332, 0.00778426, 0), \
                           ValErr(-8.06749e-05, 5.64242e-05, 0), \
                           -41464.2, 50015, 50015, -nan)
reports[-1].sigmaresid = ValErr(0.554379, 0.00175284, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00238755, None, 1.37944e-06, None, -0.000775314, None, 2.2029e-05, None, -0.000775314, None, 2.2029e-05, None, 0.00280505, None, -3.18283e-05, None, 0.00280505, None, -3.18283e-05, None, 0.554421, None, 0.00425555, None, 0.554421, None, 0.00425555, None)

reports.append(Report(604051000, ("CSC", 2, 1, 2, 7), "MEm12_07"))
reports[-1].posNum = 47794
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0013646, 0.00375476, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.110856, 0.108049, 0), \
                           ValErr(-0.00510502, 0.00233371, 0), \
                           ValErr(-0.00620517, 0.00791798, 0), \
                           ValErr(2.26553e-05, 5.88239e-05, 0), \
                           -39529.5, 47794, 47794, -nan)
reports[-1].sigmaresid = ValErr(0.553297, 0.0017896, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000560328, None, -1.73968e-07, None, 0.000750868, None, 3.24273e-07, None, 0.000750868, None, 3.24273e-07, None, -0.00193144, None, 1.81005e-06, None, -0.00193144, None, 1.81005e-06, None, 0.553333, None, 0.00423832, None, 0.553333, None, 0.00423832, None)

reports.append(Report(604051016, ("CSC", 2, 1, 2, 9), "MEm12_09"))
reports[-1].posNum = 49034
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000388841, 0.00360901, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.201185, 0.109918, 0), \
                           ValErr(-0.00365075, 0.00238499, 0), \
                           ValErr(-0.00138001, 0.00788179, 0), \
                           ValErr(4.17234e-05, 5.70792e-05, 0), \
                           -40733.5, 49034, 49034, -nan)
reports[-1].sigmaresid = ValErr(0.555315, 0.00177327, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00153071, None, 1.56164e-05, None, 0.0015495, None, 2.54702e-05, None, 0.0015495, None, 2.54702e-05, None, 0.00274053, None, 4.55163e-06, None, 0.00274053, None, 4.55163e-06, None, 0.555347, None, 0.00423896, None, 0.555347, None, 0.00423896, None)

reports.append(Report(604051032, ("CSC", 2, 1, 2, 11), "MEm12_11"))
reports[-1].posNum = 48923
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00193454, 0.00360641, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0216579, 0.109414, 0), \
                           ValErr(-0.000577839, 0.00238722, 0), \
                           ValErr(0.000253356, 0.0078646, 0), \
                           ValErr(-3.67212e-05, 5.70571e-05, 0), \
                           -40149, 48923, 48923, -nan)
reports[-1].sigmaresid = ValErr(0.549755, 0.00175751, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000603553, None, 1.51861e-05, None, 0.00126658, None, 1.15409e-05, None, 0.00126658, None, 1.15409e-05, None, 0.000486352, None, 6.74941e-06, None, 0.000486352, None, 6.74941e-06, None, 0.549759, None, 0.00422276, None, 0.549759, None, 0.00422276, None)

reports.append(Report(604051048, ("CSC", 2, 1, 2, 13), "MEm12_13"))
reports[-1].posNum = 47004
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00395219, 0.00379756, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.136527, 0.108745, 0), \
                           ValErr(5.00051e-06, 0.00235254, 0), \
                           ValErr(-0.00668517, 0.00802185, 0), \
                           ValErr(0.000101672, 5.93707e-05, 0), \
                           -38370.6, 47004, 47004, -nan)
reports[-1].sigmaresid = ValErr(0.547378, 0.00178527, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00174126, None, 1.24828e-05, None, -6.51651e-05, None, 6.06744e-06, None, -6.51651e-05, None, 6.06744e-06, None, -0.00133679, None, -1.2686e-05, None, -0.00133679, None, -1.2686e-05, None, 0.547407, None, 0.00413112, None, 0.547407, None, 0.00413112, None)

reports.append(Report(604051064, ("CSC", 2, 1, 2, 15), "MEm12_15"))
reports[-1].posNum = 50592
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000890373, 0.00355405, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0627742, 0.104841, 0), \
                           ValErr(-0.00201588, 0.00227051, 0), \
                           ValErr(0.0169604, 0.00766457, 0), \
                           ValErr(4.27276e-05, 5.57462e-05, 0), \
                           -41827.9, 50592, 50592, -nan)
reports[-1].sigmaresid = ValErr(0.553125, 0.00173887, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00438725, None, 9.70981e-06, None, -0.0052993, None, -7.86866e-06, None, -0.0052993, None, -7.86866e-06, None, -0.00810603, None, 2.51544e-05, None, -0.00810603, None, 2.51544e-05, None, 0.553168, None, 0.0042195, None, 0.553168, None, 0.0042195, None)

reports.append(Report(604051080, ("CSC", 2, 1, 2, 17), "MEm12_17"))
reports[-1].posNum = 47654
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000560261, 0.0036809, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0798444, 0.108935, 0), \
                           ValErr(0.00113632, 0.00237532, 0), \
                           ValErr(-0.00109467, 0.00795516, 0), \
                           ValErr(5.50482e-05, 5.82307e-05, 0), \
                           -38395.7, 47654, 47654, -nan)
reports[-1].sigmaresid = ValErr(0.541605, 0.00175436, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000454948, None, 2.10952e-05, None, 0.000736943, None, 4.90547e-06, None, 0.000736943, None, 4.90547e-06, None, -0.00654555, None, -3.84528e-06, None, -0.00654555, None, -3.84528e-06, None, 0.541613, None, 0.00424846, None, 0.541613, None, 0.00424846, None)

reports.append(Report(604051096, ("CSC", 2, 1, 2, 19), "MEm12_19"))
reports[-1].posNum = 50593
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00733758, 0.00359809, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.159365, 0.105399, 0), \
                           ValErr(0.00297962, 0.00227064, 0), \
                           ValErr(0.014108, 0.00770081, 0), \
                           ValErr(-6.35555e-05, 5.66665e-05, 0), \
                           -42345.4, 50593, 50593, -nan)
reports[-1].sigmaresid = ValErr(0.558803, 0.0017567, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00596886, None, 5.63817e-06, None, 0.00223847, None, 1.67555e-07, None, 0.00223847, None, 1.67555e-07, None, 0.0036188, None, 4.81128e-06, None, 0.0036188, None, 4.81128e-06, None, 0.558848, None, 0.00409325, None, 0.558848, None, 0.00409325, None)

reports.append(Report(604051112, ("CSC", 2, 1, 2, 21), "MEm12_21"))
reports[-1].posNum = 46784
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000319903, 0.00368352, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.135077, 0.110542, 0), \
                           ValErr(-0.00245468, 0.00240475, 0), \
                           ValErr(0.00260477, 0.00801191, 0), \
                           ValErr(6.1189e-05, 5.81154e-05, 0), \
                           -37279.7, 46784, 46784, -nan)
reports[-1].sigmaresid = ValErr(0.536821, 0.00175496, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00282042, None, 6.02133e-06, None, 0.000764416, None, 1.35856e-05, None, 0.000764416, None, 1.35856e-05, None, 0.000736901, None, 7.7011e-06, None, 0.000736901, None, 7.7011e-06, None, 0.536847, None, 0.00420168, None, 0.536847, None, 0.00420168, None)

reports.append(Report(604051128, ("CSC", 2, 1, 2, 23), "MEm12_23"))
reports[-1].posNum = 50513
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000165691, 0.00354303, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0308161, 0.10633, 0), \
                           ValErr(0.000732553, 0.00231253, 0), \
                           ValErr(0.00104244, 0.00767534, 0), \
                           ValErr(0.000148421, 5.58571e-05, 0), \
                           -41907.7, 50513, 50513, -nan)
reports[-1].sigmaresid = ValErr(0.554717, 0.00174524, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00208161, None, -1.93006e-05, None, 0.0016149, None, -2.32106e-05, None, 0.0016149, None, -2.32106e-05, None, 0.00190581, None, 9.38003e-06, None, 0.00190581, None, 9.38003e-06, None, 0.55476, None, 0.00420704, None, 0.55476, None, 0.00420704, None)

reports.append(Report(604051144, ("CSC", 2, 1, 2, 25), "MEm12_25"))
reports[-1].posNum = 48299
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00121959, 0.00370229, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.128701, 0.108276, 0), \
                           ValErr(0.00190862, 0.00233514, 0), \
                           ValErr(-0.00910247, 0.00786694, 0), \
                           ValErr(7.41824e-05, 5.82077e-05, 0), \
                           -39737.8, 48299, 48299, -nan)
reports[-1].sigmaresid = ValErr(0.550905, 0.00177252, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00549606, None, -3.8348e-05, None, 0.00270823, None, -2.39241e-05, None, 0.00270823, None, -2.39241e-05, None, 0.00527874, None, -1.56443e-05, None, 0.00527874, None, -1.56443e-05, None, 0.550932, None, 0.00415431, None, 0.550932, None, 0.00415431, None)

reports.append(Report(604051160, ("CSC", 2, 1, 2, 27), "MEm12_27"))
reports[-1].posNum = 48824
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0112196, 0.00363708, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.112154, 0.107056, 0), \
                           ValErr(-0.00166463, 0.00231373, 0), \
                           ValErr(-0.00856828, 0.00778917, 0), \
                           ValErr(0.000112999, 5.70515e-05, 0), \
                           -40187.6, 48824, 48824, -nan)
reports[-1].sigmaresid = ValErr(0.551106, 0.00176361, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00409252, None, 3.00533e-05, None, -0.00683614, None, 3.69735e-05, None, -0.00683614, None, 3.69735e-05, None, -0.00763403, None, 2.12149e-05, None, -0.00763403, None, 2.12149e-05, None, 0.551139, None, 0.00427195, None, 0.551139, None, 0.00427195, None)

reports.append(Report(604051176, ("CSC", 2, 1, 2, 29), "MEm12_29"))
reports[-1].posNum = 48877
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00167636, 0.00364051, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.137007, 0.108309, 0), \
                           ValErr(0.00256175, 0.00236087, 0), \
                           ValErr(0.00261538, 0.00787425, 0), \
                           ValErr(-3.88933e-06, 5.73547e-05, 0), \
                           -40499.1, 48877, 48877, -nan)
reports[-1].sigmaresid = ValErr(0.554135, 0.00177234, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.001655, None, -1.06719e-06, None, -0.00254189, None, -3.15785e-05, None, -0.00254189, None, -3.15785e-05, None, -0.000265798, None, 2.38347e-06, None, -0.000265798, None, 2.38347e-06, None, 0.554153, None, 0.00425173, None, 0.554153, None, 0.00425173, None)

reports.append(Report(604051192, ("CSC", 2, 1, 2, 31), "MEm12_31"))
reports[-1].posNum = 48519
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0014525, 0.00371834, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.112061, 0.106422, 0), \
                           ValErr(0.00235109, 0.00229773, 0), \
                           ValErr(-0.00352138, 0.00783332, 0), \
                           ValErr(-2.33688e-05, 5.83105e-05, 0), \
                           -39787.1, 48519, 48519, -nan)
reports[-1].sigmaresid = ValErr(0.549412, 0.00176371, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00438385, None, -1.2202e-05, None, 0.00212509, None, -5.80887e-06, None, 0.00212509, None, -5.80887e-06, None, 0.00248313, None, 3.74159e-06, None, 0.00248313, None, 3.74159e-06, None, 0.549429, None, 0.00417975, None, 0.549429, None, 0.00417975, None)

reports.append(Report(604051208, ("CSC", 2, 1, 2, 33), "MEm12_33"))
reports[-1].posNum = 50082
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00599128, 0.00359315, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0785902, 0.106187, 0), \
                           ValErr(-0.00419517, 0.0022755, 0), \
                           ValErr(0.0139727, 0.00773266, 0), \
                           ValErr(-5.89908e-05, 5.64623e-05, 0), \
                           -41747.5, 50082, 50082, -nan)
reports[-1].sigmaresid = ValErr(0.556907, 0.00175965, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00188009, None, -1.09265e-05, None, 0.00101151, None, -2.94672e-05, None, 0.00101151, None, -2.94672e-05, None, -0.00433905, None, -4.37079e-06, None, -0.00433905, None, -4.37079e-06, None, 0.556952, None, 0.00429261, None, 0.556952, None, 0.00429261, None)

reports.append(Report(604051224, ("CSC", 2, 1, 2, 35), "MEm12_35"))
reports[-1].posNum = 46439
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00892831, 0.00377932, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0224348, 0.11264, 0), \
                           ValErr(0.00233388, 0.00247015, 0), \
                           ValErr(-0.00759217, 0.00821055, 0), \
                           ValErr(5.96718e-05, 5.91161e-05, 0), \
                           -37070.2, 46439, 46439, -nan)
reports[-1].sigmaresid = ValErr(0.537577, 0.00176394, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00519564, None, -6.62397e-06, None, -0.00561285, None, -2.25689e-06, None, -0.00561285, None, -2.25689e-06, None, -0.00532455, None, 1.36253e-05, None, -0.00532455, None, 1.36253e-05, None, 0.537592, None, 0.0041438, None, 0.537592, None, 0.0041438, None)

reports.append(Report(604050960, ("CSC", 2, 1, 2, 2), "MEm12_02"))
reports[-1].posNum = 47401
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000864646, 0.00354571, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0420721, 0.102681, 0), \
                           ValErr(-0.000563288, 0.00219431, 0), \
                           ValErr(-0.00933322, 0.00743367, 0), \
                           ValErr(0.000136647, 5.54383e-05, 0), \
                           -37472.8, 47401, 47401, -nan)
reports[-1].sigmaresid = ValErr(0.533451, 0.00173255, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00574641, None, -5.7705e-05, None, 0.00415347, None, -4.18907e-05, None, 0.00415347, None, -4.18907e-05, None, 0.0056176, None, -4.21384e-05, None, 0.0056176, None, -4.21384e-05, None, 0.533489, None, 0.0042504, None, 0.533489, None, 0.0042504, None)

reports.append(Report(604050976, ("CSC", 2, 1, 2, 4), "MEm12_04"))
reports[-1].posNum = 44946
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0112936, 0.00365477, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0481259, 0.103792, 0), \
                           ValErr(-0.00165152, 0.0021757, 0), \
                           ValErr(0.0208174, 0.00744178, 0), \
                           ValErr(1.77772e-05, 5.66864e-05, 0), \
                           -35010.6, 44946, 44946, -nan)
reports[-1].sigmaresid = ValErr(0.527298, 0.00175872, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00558545, None, -6.82963e-05, None, 0.00540879, None, -3.76585e-05, None, 0.00540879, None, -3.76585e-05, None, 0.00283735, None, 1.41953e-05, None, 0.00283735, None, 1.41953e-05, None, 0.527353, None, 0.0053326, None, 0.527353, None, 0.0053326, None)

reports.append(Report(604050992, ("CSC", 2, 1, 2, 6), "MEm12_06"))
reports[-1].posNum = 49544
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00941674, 0.0034861, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0340332, 0.0990862, 0), \
                           ValErr(-0.00180233, 0.00210419, 0), \
                           ValErr(0.0224216, 0.00721533, 0), \
                           ValErr(-7.96277e-05, 5.45485e-05, 0), \
                           -39830.6, 49544, 49544, -nan)
reports[-1].sigmaresid = ValErr(0.540643, 0.00171751, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0015784, None, -1.76044e-05, None, 0.00143539, None, -5.75906e-06, None, 0.00143539, None, -5.75906e-06, None, 0.000963217, None, -9.03961e-06, None, 0.000963217, None, -9.03961e-06, None, 0.540705, None, 0.00401558, None, 0.540705, None, 0.00401558, None)

reports.append(Report(604051008, ("CSC", 2, 1, 2, 8), "MEm12_08"))
reports[-1].posNum = 45300
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00471975, 0.00365653, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.161391, 0.101184, 0), \
                           ValErr(-0.00664211, 0.0021271, 0), \
                           ValErr(0.0129452, 0.00737401, 0), \
                           ValErr(-2.98024e-05, 5.3488e-05, 0), \
                           -34521.8, 45300, 45300, -nan)
reports[-1].sigmaresid = ValErr(0.518472, 0.00172126, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00046739, None, -8.22786e-07, None, 0.000268109, None, 1.4101e-05, None, 0.000268109, None, 1.4101e-05, None, 0.000986229, None, -2.28153e-05, None, 0.000986229, None, -2.28153e-05, None, 0.51855, None, 0.00410094, None, 0.51855, None, 0.00410094, None)

reports.append(Report(604051024, ("CSC", 2, 1, 2, 10), "MEm12_10"))
reports[-1].posNum = 50971
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00952716, 0.00341503, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.131841, 0.0975027, 0), \
                           ValErr(-0.00155927, 0.00207951, 0), \
                           ValErr(-0.0234945, 0.00707048, 0), \
                           ValErr(4.30136e-05, 5.34453e-05, 0), \
                           -40935, 50971, 50971, -nan)
reports[-1].sigmaresid = ValErr(0.540189, 0.00169188, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00271422, None, 7.11544e-06, None, -0.00169608, None, 2.35385e-05, None, -0.00169608, None, 2.35385e-05, None, 0.00632698, None, -1.31967e-05, None, 0.00632698, None, -1.31967e-05, None, 0.540261, None, 0.00393924, None, 0.540261, None, 0.00393924, None)

reports.append(Report(604051040, ("CSC", 2, 1, 2, 12), "MEm12_12"))
reports[-1].posNum = 46554
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00189598, 0.00355712, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0615089, 0.0982346, 0), \
                           ValErr(-0.000475333, 0.00207309, 0), \
                           ValErr(0.00440563, 0.00721323, 0), \
                           ValErr(-1.25454e-05, 5.47564e-05, 0), \
                           -35459.9, 46554, 46554, -nan)
reports[-1].sigmaresid = ValErr(0.518277, 0.00169851, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000690571, None, 4.25485e-06, None, 0.000361591, None, 1.05277e-05, None, 0.000361591, None, 1.05277e-05, None, 0.0016069, None, -8.75203e-06, None, 0.0016069, None, -8.75203e-06, None, 0.518282, None, 0.00405194, None, 0.518282, None, 0.00405194, None)

reports.append(Report(604051056, ("CSC", 2, 1, 2, 14), "MEm12_14"))
reports[-1].posNum = 49843
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00296267, 0.0034278, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0975997, 0.0971142, 0), \
                           ValErr(-0.00153259, 0.00207479, 0), \
                           ValErr(0.0062876, 0.00708398, 0), \
                           ValErr(-6.04898e-05, 5.32138e-05, 0), \
                           -39058.1, 49843, 49843, -nan)
reports[-1].sigmaresid = ValErr(0.529769, 0.00167792, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00410452, None, 3.98905e-06, None, 0.000118223, None, 4.23565e-05, None, 0.000118223, None, 4.23565e-05, None, 0.00527253, None, -9.98092e-06, None, 0.00527253, None, -9.98092e-06, None, 0.529786, None, 0.00404597, None, 0.529786, None, 0.00404597, None)

reports.append(Report(604051072, ("CSC", 2, 1, 2, 16), "MEm12_16"))
reports[-1].posNum = 47134
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000961204, 0.00356139, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.126814, 0.102924, 0), \
                           ValErr(-0.000589039, 0.00214346, 0), \
                           ValErr(-0.002077, 0.00746439, 0), \
                           ValErr(0.000102215, 5.49609e-05, 0), \
                           -37033.6, 47134, 47134, -nan)
reports[-1].sigmaresid = ValErr(0.530874, 0.00172905, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00407577, None, -3.35272e-05, None, 0.00145672, None, -3.54335e-05, None, 0.00145672, None, -3.54335e-05, None, 0.000139969, None, -1.97312e-05, None, 0.000139969, None, -1.97312e-05, None, 0.530904, None, 0.00428267, None, 0.530904, None, 0.00428267, None)

reports.append(Report(604051088, ("CSC", 2, 1, 2, 18), "MEm12_18"))
reports[-1].posNum = 47964
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(7.30704e-05, 0.00349693, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0435709, 0.0994127, 0), \
                           ValErr(-0.00142806, 0.00208608, 0), \
                           ValErr(0.0102099, 0.00719989, 0), \
                           ValErr(-9.08409e-07, 5.41637e-05, 0), \
                           -37474.5, 47964, 47964, -nan)
reports[-1].sigmaresid = ValErr(0.528541, 0.0017065, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00360095, None, 1.93782e-05, None, -0.00303265, None, 2.32283e-05, None, -0.00303265, None, 2.32283e-05, None, 0.00230436, None, -1.21961e-05, None, 0.00230436, None, -1.21961e-05, None, 0.528557, None, 0.0039279, None, 0.528557, None, 0.0039279, None)

reports.append(Report(604051104, ("CSC", 2, 1, 2, 20), "MEm12_20"))
reports[-1].posNum = 49385
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0012021, 0.00351694, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0402958, 0.0995308, 0), \
                           ValErr(0.00265741, 0.00213754, 0), \
                           ValErr(0.00162829, 0.00727994, 0), \
                           ValErr(-4.70776e-05, 5.48605e-05, 0), \
                           -39415.3, 49385, 49385, -nan)
reports[-1].sigmaresid = ValErr(0.537506, 0.00171029, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000619717, None, 1.18545e-05, None, -1.28898e-05, None, 1.78478e-05, None, -1.28898e-05, None, 1.78478e-05, None, -0.000469684, None, 1.56052e-05, None, -0.000469684, None, 1.56052e-05, None, 0.537519, None, 0.00394506, None, 0.537519, None, 0.00394506, None)

reports.append(Report(604051120, ("CSC", 2, 1, 2, 22), "MEm12_22"))
reports[-1].posNum = 46480
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00170109, 0.0036038, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00746126, 0.101862, 0), \
                           ValErr(-0.00135711, 0.00217098, 0), \
                           ValErr(-0.00341728, 0.00741878, 0), \
                           ValErr(6.08211e-05, 5.6101e-05, 0), \
                           -36780.5, 46480, 46480, -nan)
reports[-1].sigmaresid = ValErr(0.533861, 0.00175098, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.001321, None, -2.36381e-05, None, 0.000352866, None, -1.65698e-05, None, 0.000352866, None, -1.65698e-05, None, -0.00197167, None, -2.83372e-05, None, -0.00197167, None, -2.83372e-05, None, 0.53387, None, 0.0041739, None, 0.53387, None, 0.0041739, None)

reports.append(Report(604051136, ("CSC", 2, 1, 2, 24), "MEm12_24"))
reports[-1].posNum = 49173
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00226359, 0.00344193, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0298232, 0.0966928, 0), \
                           ValErr(0.000195494, 0.00207459, 0), \
                           ValErr(-0.00612134, 0.00705645, 0), \
                           ValErr(4.98204e-05, 5.37574e-05, 0), \
                           -38009.6, 49173, 49173, -nan)
reports[-1].sigmaresid = ValErr(0.524159, 0.00167142, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000704214, None, 5.95296e-06, None, 0.000414385, None, 4.60362e-06, None, 0.000414385, None, 4.60362e-06, None, 0.00018807, None, -3.67616e-06, None, 0.00018807, None, -3.67616e-06, None, 0.524166, None, 0.00383865, None, 0.524166, None, 0.00383865, None)

reports.append(Report(604051152, ("CSC", 2, 1, 2, 26), "MEm12_26"))
reports[-1].posNum = 45548
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000372198, 0.00359177, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0993479, 0.100226, 0), \
                           ValErr(-0.00133478, 0.00213149, 0), \
                           ValErr(0.00775584, 0.00733893, 0), \
                           ValErr(5.80697e-05, 5.54222e-05, 0), \
                           -34164.9, 45548, 45548, -nan)
reports[-1].sigmaresid = ValErr(0.512296, 0.00169735, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00337977, None, -1.58541e-05, None, -0.000874754, None, 9.80838e-06, None, -0.000874754, None, 9.80838e-06, None, -0.000125583, None, -6.31393e-06, None, -0.000125583, None, -6.31393e-06, None, 0.512321, None, 0.00403056, None, 0.512321, None, 0.00403056, None)

reports.append(Report(604051168, ("CSC", 2, 1, 2, 28), "MEm12_28"))
reports[-1].posNum = 50432
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00104821, 0.00347701, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0752707, 0.0983067, 0), \
                           ValErr(0.00274347, 0.00210297, 0), \
                           ValErr(-0.00389099, 0.00714755, 0), \
                           ValErr(1.40561e-05, 5.41635e-05, 0), \
                           -40669.9, 50432, 50432, -nan)
reports[-1].sigmaresid = ValErr(0.541992, 0.00170658, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00285105, None, -2.56402e-06, None, 0.00244347, None, 8.69215e-06, None, 0.00244347, None, 8.69215e-06, None, 0.00341247, None, -7.14816e-07, None, 0.00341247, None, -7.14816e-07, None, 0.542005, None, 0.00385182, None, 0.542005, None, 0.00385182, None)

reports.append(Report(604051184, ("CSC", 2, 1, 2, 30), "MEm12_30"))
reports[-1].posNum = 45510
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00955547, 0.00355102, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0333438, 0.100443, 0), \
                           ValErr(-0.00170901, 0.0020923, 0), \
                           ValErr(-0.00334975, 0.00734322, 0), \
                           ValErr(-4.54255e-05, 5.44411e-05, 0), \
                           -34089.5, 45510, 45510, -nan)
reports[-1].sigmaresid = ValErr(0.511769, 0.00169631, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00706482, None, -4.85055e-05, None, 0.00968092, None, -6.10058e-05, None, 0.00968092, None, -6.10058e-05, None, 0.0120117, None, -8.146e-05, None, 0.0120117, None, -8.146e-05, None, 0.51178, None, 0.00423462, None, 0.51178, None, 0.00423462, None)

reports.append(Report(604051200, ("CSC", 2, 1, 2, 32), "MEm12_32"))
reports[-1].posNum = 50083
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-3.66651e-05, 0.00345916, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0577267, 0.0976481, 0), \
                           ValErr(-0.000919482, 0.00208562, 0), \
                           ValErr(0.00407703, 0.00712545, 0), \
                           ValErr(4.41939e-05, 5.38147e-05, 0), \
                           -39962.6, 50083, 50083, -nan)
reports[-1].sigmaresid = ValErr(0.5374, 0.001698, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00415908, None, 2.13854e-05, None, -0.000639598, None, 3.66105e-07, None, -0.000639598, None, 3.66105e-07, None, 0.000752546, None, -9.25413e-06, None, 0.000752546, None, -9.25413e-06, None, 0.537411, None, 0.00420385, None, 0.537411, None, 0.00420385, None)

reports.append(Report(604051216, ("CSC", 2, 1, 2, 34), "MEm12_34"))
reports[-1].posNum = 48325
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00360733, 0.00351887, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.113715, 0.100836, 0), \
                           ValErr(-0.00271528, 0.00213031, 0), \
                           ValErr(-0.000597144, 0.0072745, 0), \
                           ValErr(-7.70633e-05, 5.49404e-05, 0), \
                           -38475.8, 48325, 48325, -nan)
reports[-1].sigmaresid = ValErr(0.536467, 0.00172561, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000635566, None, -3.49851e-05, None, 0.00253307, None, -1.8121e-05, None, 0.00253307, None, -1.8121e-05, None, 0.00440502, None, -4.60835e-05, None, 0.00440502, None, -4.60835e-05, None, 0.536497, None, 0.00430452, None, 0.536497, None, 0.00430452, None)

reports.append(Report(604051232, ("CSC", 2, 1, 2, 36), "MEm12_36"))
reports[-1].posNum = 49345
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00300966, 0.00347262, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0623228, 0.0972949, 0), \
                           ValErr(0.00272114, 0.00207844, 0), \
                           ValErr(0.00175024, 0.00706103, 0), \
                           ValErr(-7.87917e-07, 5.42597e-05, 0), \
                           -39076.5, 49345, 49345, -nan)
reports[-1].sigmaresid = ValErr(0.534173, 0.00170038, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00130984, None, 2.18385e-05, None, -0.00353307, None, 3.03633e-05, None, -0.00353307, None, 3.03633e-05, None, -0.00340472, None, 3.19304e-05, None, -0.00340472, None, 3.19304e-05, None, 0.534186, None, 0.00421425, None, 0.534186, None, 0.00421425, None)

reports.append(Report(604051464, ("CSC", 2, 1, 3, 1), "MEm13_01"))
reports[-1].posNum = 19874
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0131489, 0.0156801, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.29883, 0.306727, 0), \
                           ValErr(-0.00544039, 0.00689397, 0), \
                           ValErr(0.0155431, 0.0149213, 0), \
                           ValErr(-0.000322322, 0.000244454, 0), \
                           -36306.7, 19874, 19874, -nan)
reports[-1].sigmaresid = ValErr(1.50367, 0.00753535, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0232759, None, 8.20882e-05, None, -0.0263242, None, 0.000132421, None, -0.0263242, None, 0.000132421, None, -0.0308161, None, 6.00986e-05, None, -0.0308161, None, 6.00986e-05, None, 1.50589, None, 0.00640622, None, 1.50589, None, 0.00640622, None)

reports.append(Report(604051472, ("CSC", 2, 1, 3, 2), "MEm13_02"))
reports[-1].posNum = 19218
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00099901, 0.0158692, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.81642, 0.315232, 0), \
                           ValErr(-0.00557512, 0.00670081, 0), \
                           ValErr(0.0165756, 0.0154219, 0), \
                           ValErr(-0.000129331, 0.000161066, 0), \
                           -35108, 19218, 19218, -nan)
reports[-1].sigmaresid = ValErr(1.50364, 0.00731049, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0210555, None, -2.43734e-06, None, -0.0130991, None, 7.53663e-05, None, -0.0130991, None, 7.53663e-05, None, -0.0169134, None, 8.7501e-05, None, -0.0169134, None, 8.7501e-05, None, 1.50677, None, 0.00689423, None, 1.50677, None, 0.00689423, None)

reports.append(Report(604051480, ("CSC", 2, 1, 3, 3), "MEm13_03"))
reports[-1].posNum = 18229
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00214411, 0.0164208, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.48467, 0.333071, 0), \
                           ValErr(0.00151021, 0.00772508, 0), \
                           ValErr(0.0184728, 0.01586, 0), \
                           ValErr(-0.000120068, 0.000152288, 0), \
                           -33651.3, 18229, 18229, -nan)
reports[-1].sigmaresid = ValErr(1.5328, 0.00738229, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0180717, None, 0.000130111, None, -0.0174882, None, 0.000147576, None, -0.0174882, None, 0.000147576, None, -0.018506, None, 0.000139968, None, -0.018506, None, 0.000139968, None, 1.53524, None, 0.00699238, None, 1.53524, None, 0.00699238, None)

reports.append(Report(604051488, ("CSC", 2, 1, 3, 4), "MEm13_04"))
reports[-1].posNum = 18497
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00584848, 0.0163598, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.73015, 0.343551, 0), \
                           ValErr(-0.0166702, 0.00800311, 0), \
                           ValErr(0.00315928, 0.0161787, 0), \
                           ValErr(0.000319853, 0.000268137, 0), \
                           -34229, 18497, 18497, -nan)
reports[-1].sigmaresid = ValErr(1.53968, 0.00800507, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0311739, None, 2.7e-05, None, -0.00869996, None, 7.92898e-05, None, -0.00869996, None, 7.92898e-05, None, -0.0098137, None, 7.5518e-05, None, -0.0098137, None, 7.5518e-05, None, 1.54237, None, 0.00661785, None, 1.54237, None, 0.00661785, None)

reports.append(Report(604051496, ("CSC", 2, 1, 3, 5), "MEm13_05"))
reports[-1].posNum = 19498
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00216192, 0.0155536, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.90415, 0.311754, 0), \
                           ValErr(0.00649892, 0.00697259, 0), \
                           ValErr(0.00476733, 0.0152951, 0), \
                           ValErr(0.000121105, 0.000243409, 0), \
                           -35341.8, 19498, 19498, -nan)
reports[-1].sigmaresid = ValErr(1.48238, 0.00750677, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0109236, None, 1.7218e-05, None, -0.00361156, None, 8.264e-05, None, -0.00361156, None, 8.264e-05, None, 0.0161761, None, 2.08153e-05, None, 0.0161761, None, 2.08153e-05, None, 1.48571, None, 0.00643749, None, 1.48571, None, 0.00643749, None)

reports.append(Report(604051504, ("CSC", 2, 1, 3, 6), "MEm13_06"))
reports[-1].posNum = 19587
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0228486, 0.0153135, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.40558, 0.296603, 0), \
                           ValErr(0.00812614, 0.00318645, 0), \
                           ValErr(-0.0152861, 0.0144937, 0), \
                           ValErr(0.000284874, 0.000140879, 0), \
                           -35404.5, 19587, 19587, -nan)
reports[-1].sigmaresid = ValErr(1.47492, 0.00693509, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00209401, None, 0.000128169, None, -0.0101876, None, 4.19959e-05, None, -0.0101876, None, 4.19959e-05, None, -0.0128747, None, 3.89733e-06, None, -0.0128747, None, 3.89733e-06, None, 1.47743, None, 0.00672982, None, 1.47743, None, 0.00672982, None)

reports.append(Report(604051512, ("CSC", 2, 1, 3, 7), "MEm13_07"))
reports[-1].posNum = 18582
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00265381, 0.0159118, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.56943, 0.315074, 0), \
                           ValErr(-0.00192641, 0.00723788, 0), \
                           ValErr(0.00762475, 0.0151771, 0), \
                           ValErr(2.48926e-05, 0.000254652, 0), \
                           -33754.5, 18582, 18582, -nan)
reports[-1].sigmaresid = ValErr(1.48822, 0.00772418, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0189112, None, 3.92337e-05, None, -0.000115908, None, 2.30225e-05, None, -0.000115908, None, 2.30225e-05, None, -0.00499128, None, 1.23695e-05, None, -0.00499128, None, 1.23695e-05, None, 1.49089, None, 0.00619723, None, 1.49089, None, 0.00619723, None)

reports.append(Report(604051520, ("CSC", 2, 1, 3, 8), "MEm13_08"))
reports[-1].posNum = 17859
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000174618, 0.016555, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.18329, 0.333298, 0), \
                           ValErr(-0.00518698, 0.0076885, 0), \
                           ValErr(-0.00891274, 0.0162172, 0), \
                           ValErr(1.3512e-05, 0.000267548, 0), \
                           -32757.7, 17859, 17859, -nan)
reports[-1].sigmaresid = ValErr(1.51483, 0.00801867, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00302431, None, 6.77543e-05, None, 0.00555809, None, 8.80847e-05, None, 0.00555809, None, 8.80847e-05, None, 0.0278332, None, -3.77137e-06, None, 0.0278332, None, -3.77137e-06, None, 1.51871, None, 0.00644541, None, 1.51871, None, 0.00644541, None)

reports.append(Report(604051528, ("CSC", 2, 1, 3, 9), "MEm13_09"))
reports[-1].posNum = 18645
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00213637, 0.0160885, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.59504, 0.323636, 0), \
                           ValErr(-0.00529463, 0.00728073, 0), \
                           ValErr(-0.0119625, 0.01582, 0), \
                           ValErr(0.000193545, 0.00025362, 0), \
                           -34030, 18645, 18645, -nan)
reports[-1].sigmaresid = ValErr(1.50113, 0.00778052, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00745001, None, -7.64504e-05, None, 0.00999192, None, -1.30731e-05, None, 0.00999192, None, -1.30731e-05, None, 0.0189506, None, -6.02878e-05, None, 0.0189506, None, -6.02878e-05, None, 1.50375, None, 0.00634179, None, 1.50375, None, 0.00634179, None)

reports.append(Report(604051536, ("CSC", 2, 1, 3, 10), "MEm13_10"))
reports[-1].posNum = 19676
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0273415, 0.0155495, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.79726, 0.316952, 0), \
                           ValErr(0.00570831, 0.00717934, 0), \
                           ValErr(0.0191913, 0.0152659, 0), \
                           ValErr(-0.000496119, 0.00024413, 0), \
                           -35783.4, 19676, 19676, -nan)
reports[-1].sigmaresid = ValErr(1.49137, 0.00751806, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0238335, None, 3.90988e-05, None, 0.0103074, None, 8.81029e-05, None, 0.0103074, None, 8.81029e-05, None, 0.0221721, None, 2.34957e-06, None, 0.0221721, None, 2.34957e-06, None, 1.49458, None, 0.0067007, None, 1.49458, None, 0.0067007, None)

reports.append(Report(604051544, ("CSC", 2, 1, 3, 11), "MEm13_11"))
reports[-1].posNum = 18783
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0227457, 0.0160611, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.17543, 0.327554, 0), \
                           ValErr(0.000515389, 0.00739746, 0), \
                           ValErr(-0.00997521, 0.016046, 0), \
                           ValErr(0.000554191, 0.00025473, 0), \
                           -34369, 18783, 18783, -nan)
reports[-1].sigmaresid = ValErr(1.50811, 0.00778098, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00599511, None, 6.31203e-05, None, -0.0106611, None, 0.000118599, None, -0.0106611, None, 0.000118599, None, -0.00821529, None, 3.78537e-05, None, -0.00821529, None, 3.78537e-05, None, 1.5101, None, 0.00693071, None, 1.5101, None, 0.00693071, None)

reports.append(Report(604051552, ("CSC", 2, 1, 3, 12), "MEm13_12"))
reports[-1].posNum = 17688
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00137667, 0.0166682, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.10454, 0.328675, 0), \
                           ValErr(-0.00499094, 0.00762878, 0), \
                           ValErr(0.012674, 0.0159041, 0), \
                           ValErr(0.000495532, 0.000269089, 0), \
                           -32527.7, 17688, 17688, -nan)
reports[-1].sigmaresid = ValErr(1.52201, 0.00809823, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00720024, None, 0.000105849, None, -0.0097315, None, 0.000107413, None, -0.0097315, None, 0.000107413, None, -0.000519484, None, 5.45842e-05, None, -0.000519484, None, 5.45842e-05, None, 1.52605, None, 0.00679381, None, 1.52605, None, 0.00679381, None)

reports.append(Report(604051560, ("CSC", 2, 1, 3, 13), "MEm13_13"))
reports[-1].posNum = 18153
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0468129, 0.0163955, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.6086, 0.314675, 0), \
                           ValErr(-0.00658425, 0.00708401, 0), \
                           ValErr(-0.0289101, 0.0155676, 0), \
                           ValErr(-0.000111549, 0.000228858, 0), \
                           -33286.2, 18153, 18153, -nan)
reports[-1].sigmaresid = ValErr(1.51393, 0.00525885, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0254458, None, 0.00010674, None, -0.0283687, None, 0.00017572, None, -0.0283687, None, 0.00017572, None, -0.00204821, None, 6.12505e-05, None, -0.00204821, None, 6.12505e-05, None, 1.51681, None, 0.00646998, None, 1.51681, None, 0.00646998, None)

reports.append(Report(604051568, ("CSC", 2, 1, 3, 14), "MEm13_14"))
reports[-1].posNum = 19687
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00467332, 0.015562, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.4483, 0.31113, 0), \
                           ValErr(-0.00458897, 0.00674508, 0), \
                           ValErr(0.0191636, 0.0153129, 0), \
                           ValErr(-0.00027169, 0.000149496, 0), \
                           -35654.2, 19687, 19687, -nan)
reports[-1].sigmaresid = ValErr(1.48011, 0.00698593, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00953819, None, 4.55084e-05, None, -0.0117323, None, 8.7829e-05, None, -0.0117323, None, 8.7829e-05, None, 0.0112245, None, 8.28081e-05, None, 0.0112245, None, 8.28081e-05, None, 1.48254, None, 0.00666312, None, 1.48254, None, 0.00666312, None)

reports.append(Report(604051576, ("CSC", 2, 1, 3, 15), "MEm13_15"))
reports[-1].posNum = 19580
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00223678, 0.0156829, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.97275, 0.319035, 0), \
                           ValErr(-0.00996647, 0.00712561, 0), \
                           ValErr(-0.00210169, 0.015411, 0), \
                           ValErr(0.000226676, 0.000246008, 0), \
                           -35742.4, 19580, 19580, -nan)
reports[-1].sigmaresid = ValErr(1.50157, 0.00758785, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000706283, None, -2.54804e-05, None, 0.000786443, None, 3.95248e-05, None, 0.000786443, None, 3.95248e-05, None, 0.0152169, None, -6.53411e-05, None, 0.0152169, None, -6.53411e-05, None, 1.50498, None, 0.00678862, None, 1.50498, None, 0.00678862, None)

reports.append(Report(604051584, ("CSC", 2, 1, 3, 16), "MEm13_16"))
reports[-1].posNum = 17837
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0289556, 0.0163971, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.97845, 0.345015, 0), \
                           ValErr(0.0134709, 0.00803642, 0), \
                           ValErr(-0.0263092, 0.0163626, 0), \
                           ValErr(7.37043e-05, 0.000122367, 0), \
                           -32867.3, 17837, 17837, -nan)
reports[-1].sigmaresid = ValErr(1.52762, 0.00803441, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000230389, None, 1.0857e-05, None, -0.00867825, None, 0.000104186, None, -0.00867825, None, 0.000104186, None, -0.0151878, None, 4.8725e-05, None, -0.0151878, None, 4.8725e-05, None, 1.53136, None, 0.00639472, None, 1.53136, None, 0.00639472, None)

reports.append(Report(604051592, ("CSC", 2, 1, 3, 17), "MEm13_17"))
reports[-1].posNum = 18434
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0107566, 0.0160128, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.84683, 0.326518, 0), \
                           ValErr(0.00354676, 0.00757149, 0), \
                           ValErr(-0.0253265, 0.015626, 0), \
                           ValErr(0.000248303, 0.000260607, 0), \
                           -33677.9, 18434, 18434, -nan)
reports[-1].sigmaresid = ValErr(1.50382, 0.00783199, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0137953, None, 9.28648e-05, None, 0.0103615, None, 6.70595e-05, None, 0.0103615, None, 6.70595e-05, None, -0.00429686, None, 6.51193e-05, None, -0.00429686, None, 6.51193e-05, None, 1.5072, None, 0.0067937, None, 1.5072, None, 0.0067937, None)

reports.append(Report(604051600, ("CSC", 2, 1, 3, 18), "MEm13_18"))
reports[-1].posNum = 18714
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00843356, 0.0162397, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.57506, 0.312521, 0), \
                           ValErr(0.000832865, 0.00705055, 0), \
                           ValErr(0.00620586, 0.0154704, 0), \
                           ValErr(7.06496e-05, 0.000251929, 0), \
                           -34122.6, 18714, 18714, -nan)
reports[-1].sigmaresid = ValErr(1.49848, 0.00774576, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0139071, None, 7.02993e-05, None, -0.0138487, None, 8.0491e-05, None, -0.0138487, None, 8.0491e-05, None, -0.0146362, None, 4.984e-05, None, -0.0146362, None, 4.984e-05, None, 1.50118, None, 0.0062602, None, 1.50118, None, 0.0062602, None)

reports.append(Report(604051608, ("CSC", 2, 1, 3, 19), "MEm13_19"))
reports[-1].posNum = 19144
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0184886, 0.0156134, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(1.90338, 0.307328, 0), \
                           ValErr(-0.00880083, 0.00690074, 0), \
                           ValErr(-0.00301179, 0.014936, 0), \
                           ValErr(0.000376632, 0.000243035, 0), \
                           -34585.2, 19144, 19144, -nan)
reports[-1].sigmaresid = ValErr(1.47348, 0.00753022, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00914914, None, 5.83545e-05, None, -0.0144491, None, 0.000128934, None, -0.0144491, None, 0.000128934, None, -0.00999096, None, 0.000105988, None, -0.00999096, None, 0.000105988, None, 1.47512, None, 0.00659302, None, 1.47512, None, 0.00659302, None)

reports.append(Report(604051616, ("CSC", 2, 1, 3, 20), "MEm13_20"))
reports[-1].posNum = 19642
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0137406, 0.0158247, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.49392, 0.310977, 0), \
                           ValErr(-0.00258352, 0.00692582, 0), \
                           ValErr(0.0140541, 0.0155466, 0), \
                           ValErr(-0.00011879, 0.000178953, 0), \
                           -35947.4, 19642, 19642, -nan)
reports[-1].sigmaresid = ValErr(1.50861, 0.00664514, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00729566, None, -3.53851e-05, None, 0.0039557, None, -4.80016e-05, None, 0.0039557, None, -4.80016e-05, None, -0.00529879, None, -7.62209e-05, None, -0.00529879, None, -7.62209e-05, None, 1.511, None, 0.00660625, None, 1.511, None, 0.00660625, None)

reports.append(Report(604051624, ("CSC", 2, 1, 3, 21), "MEm13_21"))
reports[-1].posNum = 18644
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0273173, 0.0157988, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.13164, 0.325488, 0), \
                           ValErr(0.00814166, 0.0076156, 0), \
                           ValErr(0.0514692, 0.0154149, 0), \
                           ValErr(-5.73174e-05, 0.000259701, 0), \
                           -34008, 18644, 18644, -nan)
reports[-1].sigmaresid = ValErr(1.49951, 0.00776553, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00563402, None, 4.49212e-05, None, -0.0126902, None, 0.000121421, None, -0.0126902, None, 0.000121421, None, -0.0311921, None, 0.00014964, None, -0.0311921, None, 0.00014964, None, 1.50189, None, 0.00657939, None, 1.50189, None, 0.00657939, None)

reports.append(Report(604051632, ("CSC", 2, 1, 3, 22), "MEm13_22"))
reports[-1].posNum = 18310
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0151654, 0.0159947, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.46951, 0.338241, 0), \
                           ValErr(-0.0189765, 0.00780724, 0), \
                           ValErr(0.0099555, 0.0160546, 0), \
                           ValErr(4.34112e-05, 0.000148831, 0), \
                           -33512.9, 18310, 18310, -nan)
reports[-1].sigmaresid = ValErr(1.50888, 0.00740171, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00863497, None, 2.90159e-05, None, 0.00611209, None, 6.35118e-05, None, 0.00611209, None, 6.35118e-05, None, 0.0113573, None, -2.67666e-05, None, 0.0113573, None, -2.67666e-05, None, 1.51319, None, 0.00653859, None, 1.51319, None, 0.00653859, None)

reports.append(Report(604051640, ("CSC", 2, 1, 3, 23), "MEm13_23"))
reports[-1].posNum = 19307
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00100743, 0.0157231, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.50508, 0.313849, 0), \
                           ValErr(0.0016753, 0.0059961, 0), \
                           ValErr(0.0250929, 0.0153043, 0), \
                           ValErr(-7.86159e-06, 0.000172595, 0), \
                           -35100.9, 19307, 19307, -nan)
reports[-1].sigmaresid = ValErr(1.49049, 0.00752041, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0127083, None, 2.99421e-05, None, -0.0154933, None, 7.27174e-05, None, -0.0154933, None, 7.27174e-05, None, -0.0109051, None, 7.12473e-05, None, -0.0109051, None, 7.12473e-05, None, 1.49301, None, 0.00658797, None, 1.49301, None, 0.00658797, None)

reports.append(Report(604051648, ("CSC", 2, 1, 3, 24), "MEm13_24"))
reports[-1].posNum = 19560
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0235842, 0.0149576, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.10278, 0.290708, 0), \
                           ValErr(0.00335347, 0.00538558, 0), \
                           ValErr(-0.00133141, 0.0141587, 0), \
                           ValErr(9.17635e-05, 0.000117168, 0), \
                           -35258.4, 19560, 19560, -nan)
reports[-1].sigmaresid = ValErr(1.4676, 0.00590983, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0124258, None, -2.22901e-05, None, -0.0221695, None, 0.000123905, None, -0.0221695, None, 0.000123905, None, -0.0151598, None, 4.00887e-05, None, -0.0151598, None, 4.00887e-05, None, 1.46944, None, 0.00642939, None, 1.46944, None, 0.00642939, None)

reports.append(Report(604051656, ("CSC", 2, 1, 3, 25), "MEm13_25"))
reports[-1].posNum = 18708
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0134926, 0.0164591, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.17424, 0.316387, 0), \
                           ValErr(-0.00753114, 0.00668392, 0), \
                           ValErr(0.0150655, 0.0156634, 0), \
                           ValErr(-0.000121164, 0.000196083, 0), \
                           -34610.4, 18708, 18708, -nan)
reports[-1].sigmaresid = ValErr(1.53894, 0.00698008, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00588874, None, 2.35745e-05, None, 0.00324932, None, 2.3232e-05, None, 0.00324932, None, 2.3232e-05, None, 0.0198979, None, -4.51221e-05, None, 0.0198979, None, -4.51221e-05, None, 1.54088, None, 0.00651002, None, 1.54088, None, 0.00651002, None)

reports.append(Report(604051664, ("CSC", 2, 1, 3, 26), "MEm13_26"))
reports[-1].posNum = 17817
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0190117, 0.0167518, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.67284, 0.334955, 0), \
                           ValErr(-0.00999294, 0.00784743, 0), \
                           ValErr(-0.0116945, 0.0163351, 0), \
                           ValErr(0.000139954, 0.000121958, 0), \
                           -32867.9, 17817, 17817, -nan)
reports[-1].sigmaresid = ValErr(1.53084, 0.00791772, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00756743, None, 7.01766e-05, None, -0.0107884, None, 8.42291e-05, None, -0.0107884, None, 8.42291e-05, None, -0.0180209, None, 8.0525e-05, None, -0.0180209, None, 8.0525e-05, None, 1.53358, None, 0.00640509, None, 1.53358, None, 0.00640509, None)

reports.append(Report(604051672, ("CSC", 2, 1, 3, 27), "MEm13_27"))
reports[-1].posNum = 18621
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0033376, 0.0163198, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.66115, 0.328447, 0), \
                           ValErr(0.0120356, 0.00746293, 0), \
                           ValErr(-0.00420149, 0.0158348, 0), \
                           ValErr(-0.000181362, 0.000260513, 0), \
                           -34300.3, 18621, 18621, -nan)
reports[-1].sigmaresid = ValErr(1.52666, 0.0079105, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00724489, None, 1.61465e-05, None, -0.000787411, None, 7.46237e-05, None, -0.000787411, None, 7.46237e-05, None, -0.00276367, None, 6.40414e-05, None, -0.00276367, None, 6.40414e-05, None, 1.52957, None, 0.00663975, None, 1.52957, None, 0.00663975, None)

reports.append(Report(604051680, ("CSC", 2, 1, 3, 28), "MEm13_28"))
reports[-1].posNum = 19392
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0409947, 0.0158448, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.10713, 0.321153, 0), \
                           ValErr(-0.00814609, 0.00730769, 0), \
                           ValErr(0.0290871, 0.0153748, 0), \
                           ValErr(6.71654e-05, 0.000251084, 0), \
                           -35526.3, 19392, 19392, -nan)
reports[-1].sigmaresid = ValErr(1.51146, 0.00767491, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0263567, None, 1.95406e-05, None, 0.0184298, None, 1.92872e-05, None, 0.0184298, None, 1.92872e-05, None, 0.0182452, None, 9.636e-06, None, 0.0182452, None, 9.636e-06, None, 1.51522, None, 0.0064907, None, 1.51522, None, 0.0064907, None)

reports.append(Report(604051688, ("CSC", 2, 1, 3, 29), "MEm13_29"))
reports[-1].posNum = 18658
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0263125, 0.0161929, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.26864, 0.32032, 0), \
                           ValErr(0.00263574, 0.00721978, 0), \
                           ValErr(-0.0163497, 0.0156967, 0), \
                           ValErr(0.00021059, 0.000254749, 0), \
                           -34097, 18658, 18658, -nan)
reports[-1].sigmaresid = ValErr(1.50462, 0.00778896, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0125481, None, 3.08437e-05, None, -0.0125422, None, 9.72506e-05, None, -0.0125422, None, 9.72506e-05, None, -0.00259779, None, 2.88658e-05, None, -0.00259779, None, 2.88658e-05, None, 1.50675, None, 0.00677239, None, 1.50675, None, 0.00677239, None)

reports.append(Report(604051696, ("CSC", 2, 1, 3, 30), "MEm13_30"))
reports[-1].posNum = 17881
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0175509, 0.0163991, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.6814, 0.323641, 0), \
                           ValErr(-0.00341531, 0.00744962, 0), \
                           ValErr(-0.00461119, 0.0158618, 0), \
                           ValErr(0.000318625, 0.000262125, 0), \
                           -32617.6, 17881, 17881, -nan)
reports[-1].sigmaresid = ValErr(1.49964, 0.00793014, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.024085, None, 7.10382e-05, None, -0.0129906, None, -8.35788e-06, None, -0.0129906, None, -8.35788e-06, None, -0.0252057, None, -3.73631e-05, None, -0.0252057, None, -3.73631e-05, None, 1.50256, None, 0.00651296, None, 1.50256, None, 0.00651296, None)

reports.append(Report(604051704, ("CSC", 2, 1, 3, 31), "MEm13_31"))
reports[-1].posNum = 18442
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0175046, 0.0163093, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.25749, 0.318495, 0), \
                           ValErr(-0.00837935, 0.00728067, 0), \
                           ValErr(-0.0172681, 0.0154598, 0), \
                           ValErr(-0.000121463, 0.000258291, 0), \
                           -33792.8, 18442, 18442, -nan)
reports[-1].sigmaresid = ValErr(1.51202, 0.00787298, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00362988, None, 1.08074e-05, None, -0.00702373, None, 4.29762e-05, None, -0.00702373, None, 4.29762e-05, None, -0.0182339, None, 3.22896e-05, None, -0.0182339, None, 3.22896e-05, None, 1.51416, None, 0.00634112, None, 1.51416, None, 0.00634112, None)

reports.append(Report(604051712, ("CSC", 2, 1, 3, 32), "MEm13_32"))
reports[-1].posNum = 20075
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00658807, 0.0127124, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.57962, 0.307154, 0), \
                           ValErr(0.0124143, 0.0058973, 0), \
                           ValErr(0.00172444, 0.012569, 0), \
                           ValErr(-0.000140882, 0.000107903, 0), \
                           -36881.5, 20075, 20075, -nan)
reports[-1].sigmaresid = ValErr(1.51927, 0.00691131, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00688171, None, 5.15371e-05, None, 0.0053877, None, 3.36196e-05, None, 0.0053877, None, 3.36196e-05, None, 0.0101564, None, 6.17304e-05, None, 0.0101564, None, 6.17304e-05, None, 1.52191, None, 0.00694826, None, 1.52191, None, 0.00694826, None)

reports.append(Report(604051720, ("CSC", 2, 1, 3, 33), "MEm13_33"))
reports[-1].posNum = 20047
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0292291, 0.0156359, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.90878, 0.31188, 0), \
                           ValErr(-0.00322858, 0.00705898, 0), \
                           ValErr(0.0325578, 0.0152705, 0), \
                           ValErr(0.000468733, 0.000134117, 0), \
                           -36783.8, 20047, 20047, -nan)
reports[-1].sigmaresid = ValErr(1.51579, 0.00734773, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0184952, None, -7.4447e-05, None, 0.00756361, None, -1.25326e-05, None, 0.00756361, None, -1.25326e-05, None, -0.00207916, None, -1.47935e-05, None, -0.00207916, None, -1.47935e-05, None, 1.51934, None, 0.00634999, None, 1.51934, None, 0.00634999, None)

reports.append(Report(604051728, ("CSC", 2, 1, 3, 34), "MEm13_34"))
reports[-1].posNum = 18290
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0237904, 0.0160544, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.04931, 0.342004, 0), \
                           ValErr(-0.00422507, 0.00791472, 0), \
                           ValErr(-0.0148872, 0.0160871, 0), \
                           ValErr(-0.000281486, 0.000154528, 0), \
                           -33706.2, 18290, 18290, -nan)
reports[-1].sigmaresid = ValErr(1.52797, 0.00751439, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0118689, None, 5.48229e-05, None, -0.0133486, None, 0.000101023, None, -0.0133486, None, 0.000101023, None, -0.00628309, None, 2.54964e-05, None, -0.00628309, None, 2.54964e-05, None, 1.53143, None, 0.00659345, None, 1.53143, None, 0.00659345, None)

reports.append(Report(604051736, ("CSC", 2, 1, 3, 35), "MEm13_35"))
reports[-1].posNum = 18304
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00369394, 0.0159093, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.92152, 0.332025, 0), \
                           ValErr(-0.0191215, 0.00764746, 0), \
                           ValErr(-0.0170784, 0.0158559, 0), \
                           ValErr(-2.35598e-06, 0.000127592, 0), \
                           -33481.6, 18304, 18304, -nan)
reports[-1].sigmaresid = ValErr(1.5072, 0.00782216, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0178727, None, -3.33736e-05, None, 0.00870963, None, -7.1946e-07, None, 0.00870963, None, -7.1946e-07, None, 0.0106989, None, 6.05191e-06, None, 0.0106989, None, 6.05191e-06, None, 1.5105, None, 0.00629669, None, 1.5105, None, 0.00629669, None)

reports.append(Report(604051744, ("CSC", 2, 1, 3, 36), "MEm13_36"))
reports[-1].posNum = 19112
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0281871, 0.0157795, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.26611, 0.30367, 0), \
                           ValErr(-0.0143461, 0.00668196, 0), \
                           ValErr(-0.0290845, 0.015107, 0), \
                           ValErr(-0.00032898, 0.000146427, 0), \
                           -34743.6, 19112, 19112, -nan)
reports[-1].sigmaresid = ValErr(1.49027, 0.0073883, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0187885, None, 5.21923e-10, None, -0.00763556, None, 9.67306e-05, None, -0.00763556, None, 9.67306e-05, None, -0.0175817, None, 0.000146099, None, -0.0175817, None, 0.000146099, None, 1.49272, None, 0.00658846, None, 1.49272, None, 0.00658846, None)

reports.append(Report(604049928, ("CSC", 2, 1, 4, 1), "MEm14_01"))
reports[-1].posNum = 101176
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00230271, 0.000817334, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.165732, 0.0492389, 0), \
                           ValErr(-0.00250291, 0.00125322, 0), \
                           ValErr(-0.00319209, 0.00609956, 0), \
                           ValErr(3.36858e-06, 1.73087e-05, 0), \
                           22975.5, 101176, 101176, -nan)
reports[-1].sigmaresid = ValErr(0.192815, 0.000428635, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00218461, None, 3.16293e-06, None, 0.00259342, None, -5.50186e-06, None, 0.00259342, None, -5.50186e-06, None, 0.00278227, None, -4.84552e-06, None, 0.00278227, None, -4.84552e-06, None, 0.192827, None, 0.00421437, None, 0.192827, None, 0.00421437, None)

reports.append(Report(604049944, ("CSC", 2, 1, 4, 3), "MEm14_03"))
reports[-1].posNum = 101415
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00339544, 0.000806338, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.128882, 0.0485761, 0), \
                           ValErr(-0.00246269, 0.00124365, 0), \
                           ValErr(0.00535015, 0.00603763, 0), \
                           ValErr(-1.42011e-05, 1.71462e-05, 0), \
                           24223.4, 101415, 101415, -nan)
reports[-1].sigmaresid = ValErr(0.190559, 0.000423119, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00248256, None, -1.44227e-05, None, 0.00288982, None, -3.5851e-06, None, 0.00288982, None, -3.5851e-06, None, 0.00251611, None, -2.5598e-06, None, 0.00251611, None, -2.5598e-06, None, 0.190568, None, 0.00416835, None, 0.190568, None, 0.00416835, None)

reports.append(Report(604049960, ("CSC", 2, 1, 4, 5), "MEm14_05"))
reports[-1].posNum = 101188
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000541788, 0.000821369, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0105343, 0.0495512, 0), \
                           ValErr(0.00063261, 0.00127106, 0), \
                           ValErr(-0.00544419, 0.00615855, 0), \
                           ValErr(-2.63466e-05, 1.74925e-05, 0), \
                           22555.6, 101188, 101188, -nan)
reports[-1].sigmaresid = ValErr(0.193622, 0.000430403, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000574936, None, 5.65287e-06, None, 0.000902375, None, -3.39214e-05, None, 0.000902375, None, -3.39214e-05, None, -0.00112639, None, -1.18255e-05, None, -0.00112639, None, -1.18255e-05, None, 0.193627, None, 0.00454542, None, 0.193627, None, 0.00454542, None)

reports.append(Report(604049976, ("CSC", 2, 1, 4, 7), "MEm14_07"))
reports[-1].posNum = 101073
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00123095, 0.000816094, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0213431, 0.0493025, 0), \
                           ValErr(0.000526165, 0.00125381, 0), \
                           ValErr(-0.00823196, 0.00613291, 0), \
                           ValErr(-5.30696e-06, 1.72985e-05, 0), \
                           23179.6, 101073, 101073, -nan)
reports[-1].sigmaresid = ValErr(0.192382, 0.000427889, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00156902, None, 1.10668e-05, None, 0.00190724, None, 1.78245e-05, None, 0.00190724, None, 1.78245e-05, None, 0.00167969, None, 1.64397e-05, None, 0.00167969, None, 1.64397e-05, None, 0.192385, None, 0.00409993, None, 0.192385, None, 0.00409993, None)

reports.append(Report(604049992, ("CSC", 2, 1, 4, 9), "MEm14_09"))
reports[-1].posNum = 101368
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000267157, 0.00082375, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0742679, 0.0493297, 0), \
                           ValErr(0.000232311, 0.00126175, 0), \
                           ValErr(-0.0107081, 0.00614928, 0), \
                           ValErr(-1.16261e-06, 1.74708e-05, 0), \
                           22454.7, 101368, 101368, -nan)
reports[-1].sigmaresid = ValErr(0.193892, 0.000430621, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00137152, None, -7.13301e-06, None, 0.00118003, None, -2.58424e-05, None, 0.00118003, None, -2.58424e-05, None, -0.000452209, None, 1.71683e-05, None, -0.000452209, None, 1.71683e-05, None, 0.193898, None, 0.00468673, None, 0.193898, None, 0.00468673, None)

reports.append(Report(604050008, ("CSC", 2, 1, 4, 11), "MEm14_11"))
reports[-1].posNum = 101467
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00137322, 0.000822555, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.103744, 0.0493256, 0), \
                           ValErr(4.50501e-05, 0.00126485, 0), \
                           ValErr(0.00108879, 0.00612475, 0), \
                           ValErr(3.98626e-06, 1.74688e-05, 0), \
                           22390.3, 101467, 101467, -nan)
reports[-1].sigmaresid = ValErr(0.194057, 0.000430777, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00125472, None, 8.25262e-06, None, 0.00129309, None, 1.97264e-05, None, 0.00129309, None, 1.97264e-05, None, -0.000880912, None, 2.09487e-05, None, -0.000880912, None, 2.09487e-05, None, 0.194062, None, 0.00423606, None, 0.194062, None, 0.00423606, None)

reports.append(Report(604050024, ("CSC", 2, 1, 4, 13), "MEm14_13"))
reports[-1].posNum = 101317
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000946452, 0.000821461, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.188847, 0.0494249, 0), \
                           ValErr(-0.000964093, 0.00126152, 0), \
                           ValErr(-0.00432751, 0.00614384, 0), \
                           ValErr(2.62407e-05, 1.74277e-05, 0), \
                           22561.2, 101317, 101317, -nan)
reports[-1].sigmaresid = ValErr(0.193666, 0.000430227, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.001392, None, 2.30545e-06, None, 0.00142657, None, 4.82485e-06, None, 0.00142657, None, 4.82485e-06, None, 0.00163755, None, 1.33279e-05, None, 0.00163755, None, 1.33279e-05, None, 0.193683, None, 0.00422271, None, 0.193683, None, 0.00422271, None)

reports.append(Report(604050040, ("CSC", 2, 1, 4, 15), "MEm14_15"))
reports[-1].posNum = 101595
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00263283, 0.000818553, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.119695, 0.0492597, 0), \
                           ValErr(-0.0010159, 0.00125391, 0), \
                           ValErr(0.000729534, 0.006115, 0), \
                           ValErr(-2.2606e-05, 1.73182e-05, 0), \
                           22878.6, 101595, 101595, -nan)
reports[-1].sigmaresid = ValErr(0.19318, 0.00042856, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00240251, None, 1.35507e-05, None, 0.00248509, None, -6.56038e-06, None, 0.00248509, None, -6.56038e-06, None, 0.00160502, None, 1.71582e-06, None, 0.00160502, None, 1.71582e-06, None, 0.193187, None, 0.00490626, None, 0.193187, None, 0.00490626, None)

reports.append(Report(604050056, ("CSC", 2, 1, 4, 17), "MEm14_17"))
reports[-1].posNum = 100511
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00275589, 0.000815587, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0132865, 0.0490042, 0), \
                           ValErr(0.000176917, 0.00125335, 0), \
                           ValErr(0.00180458, 0.00613015, 0), \
                           ValErr(-3.35019e-05, 1.72949e-05, 0), \
                           23633.6, 100511, 100511, -nan)
reports[-1].sigmaresid = ValErr(0.191269, 0.000426603, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00256161, None, -4.54609e-06, None, 0.00246862, None, 7.92349e-06, None, 0.00246862, None, 7.92349e-06, None, 0.00241415, None, 2.79091e-05, None, 0.00241415, None, 2.79091e-05, None, 0.191273, None, 0.0041688, None, 0.191273, None, 0.0041688, None)

reports.append(Report(604050072, ("CSC", 2, 1, 4, 19), "MEm14_19"))
reports[-1].posNum = 102098
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00297879, 0.000814822, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.17381, 0.0493088, 0), \
                           ValErr(-0.00118127, 0.00125303, 0), \
                           ValErr(0.00491734, 0.00612147, 0), \
                           ValErr(-3.74899e-05, 1.72732e-05, 0), \
                           22890.8, 102098, 102098, -nan)
reports[-1].sigmaresid = ValErr(0.193372, 0.000427927, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00287644, None, 5.81931e-07, None, 0.00243948, None, -9.13559e-06, None, 0.00243948, None, -9.13559e-06, None, 0.000876051, None, 1.51748e-05, None, 0.000876051, None, 1.51748e-05, None, 0.193388, None, 0.00430959, None, 0.193388, None, 0.00430959, None)

reports.append(Report(604050088, ("CSC", 2, 1, 4, 21), "MEm14_21"))
reports[-1].posNum = 100831
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00209746, 0.000816497, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0140467, 0.0492608, 0), \
                           ValErr(-0.000424525, 0.00125967, 0), \
                           ValErr(-0.00616249, 0.00609844, 0), \
                           ValErr(-8.07311e-06, 1.73333e-05, 0), \
                           23106.8, 100831, 100831, -nan)
reports[-1].sigmaresid = ValErr(0.192415, 0.000428476, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00275496, None, -5.50731e-06, None, 0.00259455, None, 2.7854e-06, None, 0.00259455, None, 2.7854e-06, None, 0.0011469, None, 2.52638e-05, None, 0.0011469, None, 2.52638e-05, None, 0.192417, None, 0.00412737, None, 0.192417, None, 0.00412737, None)

reports.append(Report(604050104, ("CSC", 2, 1, 4, 23), "MEm14_23"))
reports[-1].posNum = 101314
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0018166, 0.000817805, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.157494, 0.0493387, 0), \
                           ValErr(-3.33556e-05, 0.00125672, 0), \
                           ValErr(-0.00390397, 0.00609905, 0), \
                           ValErr(-1.43952e-05, 1.73408e-05, 0), \
                           22642.1, 101314, 101314, -nan)
reports[-1].sigmaresid = ValErr(0.193511, 0.000429888, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00122928, None, 1.27663e-06, None, 0.00211023, None, 1.03749e-05, None, 0.00211023, None, 1.03749e-05, None, 7.26888e-05, None, 5.81058e-06, None, 7.26888e-05, None, 5.81058e-06, None, 0.193524, None, 0.00423513, None, 0.193524, None, 0.00423513, None)

reports.append(Report(604050120, ("CSC", 2, 1, 4, 25), "MEm14_25"))
reports[-1].posNum = 101082
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00338386, 0.000815401, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0634015, 0.0491242, 0), \
                           ValErr(-0.000759356, 0.00125429, 0), \
                           ValErr(0.00160397, 0.00609791, 0), \
                           ValErr(-4.68831e-05, 1.7278e-05, 0), \
                           23358.2, 101082, 101082, -nan)
reports[-1].sigmaresid = ValErr(0.192046, 0.000427123, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00213889, None, 3.05224e-06, None, 0.00307368, None, -6.45276e-06, None, 0.00307368, None, -6.45276e-06, None, 0.00173606, None, 6.90499e-06, None, 0.00173606, None, 6.90499e-06, None, 0.192055, None, 0.00471253, None, 0.192055, None, 0.00471253, None)

reports.append(Report(604050136, ("CSC", 2, 1, 4, 27), "MEm14_27"))
reports[-1].posNum = 100775
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0014878, 0.000824811, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0142345, 0.049539, 0), \
                           ValErr(-0.00193754, 0.00126266, 0), \
                           ValErr(-0.0138763, 0.00613486, 0), \
                           ValErr(8.05406e-06, 1.74926e-05, 0), \
                           22377.9, 100775, 100775, -nan)
reports[-1].sigmaresid = ValErr(0.193787, 0.000431651, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00234092, None, 8.53035e-06, None, 0.00272181, None, -2.61051e-05, None, 0.00272181, None, -2.61051e-05, None, 0.00225181, None, 1.7597e-05, None, 0.00225181, None, 1.7597e-05, None, 0.193794, None, 0.00666312, None, 0.193794, None, 0.00666312, None)

reports.append(Report(604050152, ("CSC", 2, 1, 4, 29), "MEm14_29"))
reports[-1].posNum = 101009
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00179876, 0.000820761, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.149405, 0.0493848, 0), \
                           ValErr(-0.00156478, 0.00126241, 0), \
                           ValErr(0.00566633, 0.00614486, 0), \
                           ValErr(-2.29455e-06, 1.74011e-05, 0), \
                           22702.9, 101009, 101009, -nan)
reports[-1].sigmaresid = ValErr(0.193264, 0.000429987, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00175736, None, 7.40435e-06, None, 0.00132597, None, 1.6765e-06, None, 0.00132597, None, 1.6765e-06, None, 0.000644143, None, 1.88037e-05, None, 0.000644143, None, 1.88037e-05, None, 0.193273, None, 0.00407373, None, 0.193273, None, 0.00407373, None)

reports.append(Report(604050168, ("CSC", 2, 1, 4, 31), "MEm14_31"))
reports[-1].posNum = 101085
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00237323, 0.000821049, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0582014, 0.0491308, 0), \
                           ValErr(-0.00113621, 0.00125554, 0), \
                           ValErr(-0.00670135, 0.00612963, 0), \
                           ValErr(-2.59844e-05, 1.7383e-05, 0), \
                           22976.7, 101085, 101085, -nan)
reports[-1].sigmaresid = ValErr(0.192774, 0.000428735, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00247636, None, 5.49972e-06, None, 0.00285633, None, 1.86375e-05, None, 0.00285633, None, 1.86375e-05, None, 0.0010847, None, 5.82748e-05, None, 0.0010847, None, 5.82748e-05, None, 0.19278, None, 0.0047609, None, 0.19278, None, 0.0047609, None)

reports.append(Report(604050184, ("CSC", 2, 1, 4, 33), "MEm14_33"))
reports[-1].posNum = 101915
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00191496, 0.000821315, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.039099, 0.0495079, 0), \
                           ValErr(-0.00048186, 0.00125478, 0), \
                           ValErr(-0.000567728, 0.00611379, 0), \
                           ValErr(-3.75418e-06, 1.7425e-05, 0), \
                           22236.4, 101915, 101915, -nan)
reports[-1].sigmaresid = ValErr(0.194539, 0.000430895, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00160814, None, 8.33557e-07, None, 0.0019529, None, 8.88457e-06, None, 0.0019529, None, 8.88457e-06, None, 0.00162256, None, 1.61901e-05, None, 0.00162256, None, 1.61901e-05, None, 0.194539, None, 0.00444715, None, 0.194539, None, 0.00444715, None)

reports.append(Report(604050200, ("CSC", 2, 1, 4, 35), "MEm14_35"))
reports[-1].posNum = 101238
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00176872, 0.000808367, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0721509, 0.0486252, 0), \
                           ValErr(0.000478167, 0.00124701, 0), \
                           ValErr(-0.0104562, 0.0061002, 0), \
                           ValErr(2.19322e-05, 1.71087e-05, 0), \
                           24331.4, 101238, 101238, -nan)
reports[-1].sigmaresid = ValErr(0.190277, 0.000422862, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00217474, None, -1.28798e-06, None, 0.00274567, None, -1.73347e-06, None, 0.00274567, None, -1.73347e-06, None, 0.00317024, None, 3.50803e-05, None, 0.00317024, None, 3.50803e-05, None, 0.190283, None, 0.00495235, None, 0.190283, None, 0.00495235, None)

reports.append(Report(604049936, ("CSC", 2, 1, 4, 2), "MEm14_02"))
reports[-1].posNum = 100455
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00262917, 0.000737973, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0416747, 0.0419089, 0), \
                           ValErr(0.000178334, 0.00108028, 0), \
                           ValErr(-0.000113949, 0.00523949, 0), \
                           ValErr(-2.4801e-05, 1.67742e-05, 0), \
                           33820.8, 100455, 100455, -nan)
reports[-1].sigmaresid = ValErr(0.172801, 0.000385494, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0018844, None, -1.91115e-05, None, 0.00254252, None, -3.47894e-05, None, 0.00254252, None, -3.47894e-05, None, 0.00260131, None, -2.55114e-05, None, 0.00260131, None, -2.55114e-05, None, 0.172805, None, 0.00437461, None, 0.172805, None, 0.00437461, None)

reports.append(Report(604049952, ("CSC", 2, 1, 4, 4), "MEm14_04"))
reports[-1].posNum = 99541
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0017786, 0.000734227, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.122372, 0.0417986, 0), \
                           ValErr(-0.000218139, 0.00106928, 0), \
                           ValErr(-0.00240785, 0.0052043, 0), \
                           ValErr(4.68658e-06, 1.55714e-05, 0), \
                           34240.6, 99541, 99541, -nan)
reports[-1].sigmaresid = ValErr(0.171543, 0.000384465, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00117737, None, -1.00851e-05, None, 0.00201087, None, -2.73583e-05, None, 0.00201087, None, -2.73583e-05, None, 0.0026039, None, -1.80629e-05, None, 0.0026039, None, -1.80629e-05, None, 0.171551, None, 0.00437037, None, 0.171551, None, 0.00437037, None)

reports.append(Report(604049968, ("CSC", 2, 1, 4, 6), "MEm14_06"))
reports[-1].posNum = 100542
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00230654, 0.000737273, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0630826, 0.0419342, 0), \
                           ValErr(0.000368037, 0.0010765, 0), \
                           ValErr(0.00812835, 0.0051997, 0), \
                           ValErr(-3.07883e-05, 1.56734e-05, 0), \
                           33659.4, 100542, 100542, -nan)
reports[-1].sigmaresid = ValErr(0.173129, 0.000386082, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00140951, None, 1.49475e-06, None, 0.00144458, None, -2.36067e-05, None, 0.00144458, None, -2.36067e-05, None, 0.000480527, None, 1.3995e-05, None, 0.000480527, None, 1.3995e-05, None, 0.173136, None, 0.00448722, None, 0.173136, None, 0.00448722, None)

reports.append(Report(604049984, ("CSC", 2, 1, 4, 8), "MEm14_08"))
reports[-1].posNum = 99695
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00248247, 0.00073317, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.075328, 0.0418632, 0), \
                           ValErr(-0.00145342, 0.00106697, 0), \
                           ValErr(0.00622464, 0.00519049, 0), \
                           ValErr(8.22008e-06, 1.55276e-05, 0), \
                           34218.6, 99695, 99695, -nan)
reports[-1].sigmaresid = ValErr(0.171672, 0.000384456, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00170302, None, -1.00986e-05, None, 0.00195263, None, -2.81387e-05, None, 0.00195263, None, -2.81387e-05, None, 0.00118002, None, -1.59084e-05, None, 0.00118002, None, -1.59084e-05, None, 0.171677, None, 0.00457326, None, 0.171677, None, 0.00457326, None)

reports.append(Report(604050000, ("CSC", 2, 1, 4, 10), "MEm14_10"))
reports[-1].posNum = 99827
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00340874, 0.000739224, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.109563, 0.0419542, 0), \
                           ValErr(1.42846e-05, 0.00107112, 0), \
                           ValErr(-0.00389388, 0.00524899, 0), \
                           ValErr(4.05185e-07, 1.56685e-05, 0), \
                           33620.5, 99827, 99827, -nan)
reports[-1].sigmaresid = ValErr(0.172782, 0.000386687, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00355932, None, -2.26463e-05, None, 0.00375461, None, -4.1828e-05, None, 0.00375461, None, -4.1828e-05, None, 0.00478016, None, -4.14968e-05, None, 0.00478016, None, -4.14968e-05, None, 0.172789, None, 0.00451128, None, 0.172789, None, 0.00451128, None)

reports.append(Report(604050016, ("CSC", 2, 1, 4, 12), "MEm14_12"))
reports[-1].posNum = 99700
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00261951, 0.000734348, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0594298, 0.041979, 0), \
                           ValErr(0.000308209, 0.00107265, 0), \
                           ValErr(0.000153683, 0.00522743, 0), \
                           ValErr(-1.78599e-05, 1.55323e-05, 0), \
                           34039.1, 99700, 99700, -nan)
reports[-1].sigmaresid = ValErr(0.171984, 0.000385146, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00261945, None, -6.73572e-06, None, 0.00252465, None, -2.56689e-05, None, 0.00252465, None, -2.56689e-05, None, 0.00101876, None, -3.64894e-06, None, 0.00101876, None, -3.64894e-06, None, 0.171988, None, 0.00475026, None, 0.171988, None, 0.00475026, None)

reports.append(Report(604050032, ("CSC", 2, 1, 4, 14), "MEm14_14"))
reports[-1].posNum = 99971
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00151604, 0.000732144, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.144895, 0.0419799, 0), \
                           ValErr(-0.00163591, 0.00106955, 0), \
                           ValErr(-0.00471608, 0.00519503, 0), \
                           ValErr(3.95417e-06, 1.55354e-05, 0), \
                           34026.5, 99971, 99971, -nan)
reports[-1].sigmaresid = ValErr(0.172165, 0.000385028, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0013439, None, 2.52794e-06, None, 0.00194815, None, -3.14843e-05, None, 0.00194815, None, -3.14843e-05, None, 0.0015809, None, -2.28985e-05, None, 0.0015809, None, -2.28985e-05, None, 0.172176, None, 0.00466665, None, 0.172176, None, 0.00466665, None)

reports.append(Report(604050048, ("CSC", 2, 1, 4, 16), "MEm14_16"))
reports[-1].posNum = 99907
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00252648, 0.000733805, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.105653, 0.0418976, 0), \
                           ValErr(-0.000951871, 0.00106779, 0), \
                           ValErr(0.00792217, 0.00521627, 0), \
                           ValErr(-4.89842e-06, 1.55558e-05, 0), \
                           34031, 99907, 99907, -nan)
reports[-1].sigmaresid = ValErr(0.17212, 0.00038505, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00177769, None, -3.98495e-06, None, 0.00179216, None, -1.31719e-05, None, 0.00179216, None, -1.31719e-05, None, 0.00103617, None, -1.04029e-05, None, 0.00103617, None, -1.04029e-05, None, 0.172127, None, 0.00435164, None, 0.172127, None, 0.00435164, None)

reports.append(Report(604050064, ("CSC", 2, 1, 4, 18), "MEm14_18"))
reports[-1].posNum = 100295
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00110066, 0.00073857, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0828565, 0.04183, 0), \
                           ValErr(-0.000338524, 0.0010652, 0), \
                           ValErr(-0.00277764, 0.00516197, 0), \
                           ValErr(-2.17085e-05, 1.65651e-05, 0), \
                           34223.5, 100295, 100295, -nan)
reports[-1].sigmaresid = ValErr(0.172016, 0.000385539, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000806818, None, 8.56819e-07, None, 0.00125921, None, -4.31587e-05, None, 0.00125921, None, -4.31587e-05, None, -0.000219131, None, -5.42732e-06, None, -0.000219131, None, -5.42732e-06, None, 0.172022, None, 0.00453471, None, 0.172022, None, 0.00453471, None)

reports.append(Report(604050080, ("CSC", 2, 1, 4, 20), "MEm14_20"))
reports[-1].posNum = 99610
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.002077, 0.000738004, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0738692, 0.0419856, 0), \
                           ValErr(-0.000777694, 0.00107453, 0), \
                           ValErr(0.000755185, 0.00524057, 0), \
                           ValErr(-1.14609e-05, 1.56263e-05, 0), \
                           33675, 99610, 99610, -nan)
reports[-1].sigmaresid = ValErr(0.17256, 0.000386612, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00252136, None, -9.53154e-06, None, 0.00196561, None, -2.95222e-05, None, 0.00196561, None, -2.95222e-05, None, 0.00137294, None, -1.73103e-05, None, 0.00137294, None, -1.73103e-05, None, 0.172564, None, 0.0044911, None, 0.172564, None, 0.0044911, None)

reports.append(Report(604050096, ("CSC", 2, 1, 4, 22), "MEm14_22"))
reports[-1].posNum = 99655
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00247558, 0.000732994, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.163941, 0.0419281, 0), \
                           ValErr(-0.00132841, 0.00107656, 0), \
                           ValErr(0.000364522, 0.00521552, 0), \
                           ValErr(2.53274e-05, 1.56044e-05, 0), \
                           34047.9, 99655, 99655, -nan)
reports[-1].sigmaresid = ValErr(0.171942, 0.000385139, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00244913, None, -9.37206e-06, None, 0.00256067, None, -2.41455e-05, None, 0.00256067, None, -2.41455e-05, None, 0.00198418, None, -2.50923e-05, None, 0.00198418, None, -2.50923e-05, None, 0.171958, None, 0.00453527, None, 0.171958, None, 0.00453527, None)

reports.append(Report(604050112, ("CSC", 2, 1, 4, 24), "MEm14_24"))
reports[-1].posNum = 99741
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00349319, 0.000736125, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.104811, 0.041906, 0), \
                           ValErr(-0.000210302, 0.00106598, 0), \
                           ValErr(0.00553472, 0.00519856, 0), \
                           ValErr(-3.59484e-05, 1.55621e-05, 0), \
                           33788.9, 99741, 99741, -nan)
reports[-1].sigmaresid = ValErr(0.17244, 0.000386088, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0032156, None, -1.5589e-05, None, 0.00285357, None, -1.2277e-05, None, 0.00285357, None, -1.2277e-05, None, 0.000935793, None, 3.77128e-06, None, 0.000935793, None, 3.77128e-06, None, 0.172451, None, 0.00462105, None, 0.172451, None, 0.00462105, None)

reports.append(Report(604050128, ("CSC", 2, 1, 4, 26), "MEm14_26"))
reports[-1].posNum = 100304
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0023118, 0.0007311, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.186665, 0.0416226, 0), \
                           ValErr(-0.00224405, 0.00106357, 0), \
                           ValErr(0.00537842, 0.00519434, 0), \
                           ValErr(-1.08779e-05, 1.54773e-05, 0), \
                           34453.9, 100304, 100304, -nan)
reports[-1].sigmaresid = ValErr(0.171627, 0.000383187, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00185987, None, -6.31917e-06, None, 0.001795, None, -2.9108e-05, None, 0.001795, None, -2.9108e-05, None, -0.00065407, None, -7.45536e-06, None, -0.00065407, None, -7.45536e-06, None, 0.171645, None, 0.0044208, None, 0.171645, None, 0.0044208, None)

reports.append(Report(604050144, ("CSC", 2, 1, 4, 28), "MEm14_28"))
reports[-1].posNum = 100208
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00221741, 0.000735052, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0699826, 0.0420142, 0), \
                           ValErr(-0.00151172, 0.00107277, 0), \
                           ValErr(-0.00332048, 0.00520069, 0), \
                           ValErr(-1.00999e-08, 1.561e-05, 0), \
                           33808.2, 100208, 100208, -nan)
reports[-1].sigmaresid = ValErr(0.172679, 0.000385722, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00315731, None, -5.80918e-06, None, 0.00251937, None, -1.65472e-05, None, 0.00251937, None, -1.65472e-05, None, 0.00199681, None, -1.13756e-05, None, 0.00199681, None, -1.13756e-05, None, 0.172683, None, 0.00431361, None, 0.172683, None, 0.00431361, None)

reports.append(Report(604050160, ("CSC", 2, 1, 4, 30), "MEm14_30"))
reports[-1].posNum = 100071
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000676427, 0.000733905, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.128597, 0.0417408, 0), \
                           ValErr(-0.00147173, 0.00106641, 0), \
                           ValErr(-0.00701343, 0.00518775, 0), \
                           ValErr(3.60693e-05, 1.55487e-05, 0), \
                           34113.2, 100071, 100071, -nan)
reports[-1].sigmaresid = ValErr(0.172074, 0.000384633, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00174795, None, -7.0886e-06, None, 0.00146425, None, -2.9919e-05, None, 0.00146425, None, -2.9919e-05, None, 0.00187907, None, -1.84899e-05, None, 0.00187907, None, -1.84899e-05, None, 0.172088, None, 0.00442001, None, 0.172088, None, 0.00442001, None)

reports.append(Report(604050176, ("CSC", 2, 1, 4, 32), "MEm14_32"))
reports[-1].posNum = 100336
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00222545, 0.000735039, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.210325, 0.0420382, 0), \
                           ValErr(-0.0022313, 0.0010719, 0), \
                           ValErr(0.00188883, 0.00522869, 0), \
                           ValErr(9.37567e-06, 1.55692e-05, 0), \
                           33780.3, 100336, 100336, -nan)
reports[-1].sigmaresid = ValErr(0.172802, 0.000385749, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00233371, None, -2.0564e-05, None, 0.00210588, None, -3.91778e-05, None, 0.00210588, None, -3.91778e-05, None, 0.00177393, None, -2.64328e-05, None, 0.00177393, None, -2.64328e-05, None, 0.172824, None, 0.00427236, None, 0.172824, None, 0.00427236, None)

reports.append(Report(604050192, ("CSC", 2, 1, 4, 34), "MEm14_34"))
reports[-1].posNum = 99839
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00156104, 0.000732256, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.1224, 0.0417096, 0), \
                           ValErr(-0.00167684, 0.00106788, 0), \
                           ValErr(-0.0069338, 0.00518049, 0), \
                           ValErr(-4.33642e-06, 1.55499e-05, 0), \
                           34250, 99839, 99839, -nan)
reports[-1].sigmaresid = ValErr(0.171702, 0.000384247, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00131108, None, 8.36442e-06, None, 0.00218316, None, -2.32876e-05, None, 0.00218316, None, -2.32876e-05, None, 0.00278171, None, -2.18512e-05, None, 0.00278171, None, -2.18512e-05, None, 0.171713, None, 0.0048512, None, 0.171713, None, 0.0048512, None)

reports.append(Report(604050208, ("CSC", 2, 1, 4, 36), "MEm14_36"))
reports[-1].posNum = 100175
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00201248, 0.00073854, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0507257, 0.0421625, 0), \
                           ValErr(-0.0011638, 0.00107727, 0), \
                           ValErr(-0.00209845, 0.00523764, 0), \
                           ValErr(-8.52136e-06, 1.56526e-05, 0), \
                           33402, 100175, 100175, -nan)
reports[-1].sigmaresid = ValErr(0.173362, 0.00038731, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00222171, None, -2.49945e-06, None, 0.00217102, None, -6.55403e-06, None, 0.00217102, None, -6.55403e-06, None, 0.000460557, None, -1.87969e-05, None, 0.000460557, None, -1.87969e-05, None, 0.173364, None, 0.00441549, None, 0.173364, None, 0.00441549, None)

reports.append(Report(604054024, ("CSC", 2, 2, 1, 1), "MEm21_01"))
reports[-1].posNum = 209727
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00167104, 0.00137047, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0328617, 0.035956, 0), \
                           ValErr(-0.00170031, 0.000709142, 0), \
                           ValErr(-0.0028999, 0.00165102, 0), \
                           ValErr(1.43374e-05, 2.02392e-05, 0), \
                           -115142, 209727, 209727, -nan)
reports[-1].sigmaresid = ValErr(0.418981, 0.000646923, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00184854, None, 5.96674e-06, None, 9.80682e-05, None, -9.00687e-06, None, 9.80682e-05, None, -9.00687e-06, None, -0.000545742, None, 1.39256e-05, None, -0.000545742, None, 1.39256e-05, None, 0.41899, None, 0.00595589, None, 0.41899, None, 0.00595589, None)

reports.append(Report(604054040, ("CSC", 2, 2, 1, 3), "MEm21_03"))
reports[-1].posNum = 210894
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00158783, 0.00136937, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0294266, 0.0366861, 0), \
                           ValErr(0.000223507, 0.000750591, 0), \
                           ValErr(-0.0014129, 0.00165408, 0), \
                           ValErr(3.68425e-07, 2.26176e-05, 0), \
                           -115369, 210894, 210894, -nan)
reports[-1].sigmaresid = ValErr(0.418161, 0.000644426, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00143417, None, 4.47465e-06, None, -0.000785485, None, -6.6608e-06, None, -0.000785485, None, -6.6608e-06, None, -0.000231205, None, 2.60326e-06, None, -0.000231205, None, 2.60326e-06, None, 0.418162, None, 0.00571128, None, 0.418162, None, 0.00571128, None)

reports.append(Report(604054056, ("CSC", 2, 2, 1, 5), "MEm21_05"))
reports[-1].posNum = 208933
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00315927, 0.00137595, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0885952, 0.0360181, 0), \
                           ValErr(0.000647527, 0.000711968, 0), \
                           ValErr(0.000829873, 0.00165784, 0), \
                           ValErr(-1.64505e-05, 2.03492e-05, 0), \
                           -114695, 208933, 208933, -nan)
reports[-1].sigmaresid = ValErr(0.41896, 0.000648118, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00473265, None, -1.18822e-05, None, 0.00254317, None, -1.76163e-05, None, 0.00254317, None, -1.76163e-05, None, 0.00167303, None, 1.43036e-05, None, 0.00167303, None, 1.43036e-05, None, 0.418967, None, 0.00579218, None, 0.418967, None, 0.00579218, None)

reports.append(Report(604054072, ("CSC", 2, 2, 1, 7), "MEm21_07"))
reports[-1].posNum = 209042
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00055481, 0.00136428, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.00947226, 0.035601, 0), \
                           ValErr(-0.00111874, 0.000702451, 0), \
                           ValErr(0.000566713, 0.00163867, 0), \
                           ValErr(1.53463e-05, 2.00967e-05, 0), \
                           -112808, 209042, 209042, -nan)
reports[-1].sigmaresid = ValErr(0.415075, 0.00064194, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000523833, None, 1.1908e-07, None, 0.000378134, None, -1.9923e-05, None, 0.000378134, None, -1.9923e-05, None, -0.000656184, None, 1.8401e-05, None, -0.000656184, None, 1.8401e-05, None, 0.415079, None, 0.00560577, None, 0.415079, None, 0.00560577, None)

reports.append(Report(604054088, ("CSC", 2, 2, 1, 9), "MEm21_09"))
reports[-1].posNum = 209638
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000281284, 0.00136596, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0216689, 0.0356681, 0), \
                           ValErr(0.00106699, 0.000705695, 0), \
                           ValErr(-0.000896685, 0.00164536, 0), \
                           ValErr(-8.27431e-06, 2.01482e-05, 0), \
                           -113462, 209638, 209638, -nan)
reports[-1].sigmaresid = ValErr(0.415735, 0.000642046, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00157693, None, 1.87221e-06, None, 0.000708788, None, -1.54171e-05, None, 0.000708788, None, -1.54171e-05, None, 0.00085622, None, -1.24427e-05, None, 0.00085622, None, -1.24427e-05, None, 0.415739, None, 0.00563849, None, 0.415739, None, 0.00563849, None)

reports.append(Report(604054104, ("CSC", 2, 2, 1, 11), "MEm21_11"))
reports[-1].posNum = 209202
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0040699, 0.00136511, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0245665, 0.0369764, 0), \
                           ValErr(5.9431e-05, 0.00080657, 0), \
                           ValErr(0.00113726, 0.0016466, 0), \
                           ValErr(8.91322e-06, 2.09488e-05, 0), \
                           -113071, 209202, 209202, -nan)
reports[-1].sigmaresid = ValErr(0.415426, 0.000658294, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00257616, None, -1.18552e-05, None, 0.00351056, None, -2.94425e-05, None, 0.00351056, None, -2.94425e-05, None, 0.00401804, None, -3.02768e-05, None, 0.00401804, None, -3.02768e-05, None, 0.415427, None, 0.00563139, None, 0.415427, None, 0.00563139, None)

reports.append(Report(604054120, ("CSC", 2, 2, 1, 13), "MEm21_13"))
reports[-1].posNum = 209792
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00150557, 0.0013605, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00378213, 0.035606, 0), \
                           ValErr(0.000895045, 0.000702799, 0), \
                           ValErr(-0.000209819, 0.00163884, 0), \
                           ValErr(-1.31468e-05, 2.00258e-05, 0), \
                           -113297, 209792, 209792, -nan)
reports[-1].sigmaresid = ValErr(0.415241, 0.000641049, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0012477, None, 6.03207e-06, None, 0.00150397, None, -2.59986e-05, None, 0.00150397, None, -2.59986e-05, None, 0.00132051, None, -1.17683e-05, None, 0.00132051, None, -1.17683e-05, None, 0.415244, None, 0.0056637, None, 0.415244, None, 0.0056637, None)

reports.append(Report(604054136, ("CSC", 2, 2, 1, 15), "MEm21_15"))
reports[-1].posNum = 209601
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000557352, 0.0013592, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.00216196, 0.0356464, 0), \
                           ValErr(0.000559121, 0.000702984, 0), \
                           ValErr(-0.00162154, 0.00163829, 0), \
                           ValErr(-1.19249e-05, 2.00133e-05, 0), \
                           -113207, 209601, 209601, -nan)
reports[-1].sigmaresid = ValErr(0.415269, 0.000641383, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00124054, None, -2.56381e-06, None, 0.00136678, None, -1.8498e-05, None, 0.00136678, None, -1.8498e-05, None, 0.00164923, None, 6.04639e-06, None, 0.00164923, None, 6.04639e-06, None, 0.415272, None, 0.0056266, None, 0.415272, None, 0.0056266, None)

reports.append(Report(604054152, ("CSC", 2, 2, 1, 17), "MEm21_17"))
reports[-1].posNum = 210262
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00152224, 0.00136573, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.00291215, 0.0357533, 0), \
                           ValErr(0.000449059, 0.000704765, 0), \
                           ValErr(0.00104051, 0.001647, 0), \
                           ValErr(-2.19722e-05, 2.01452e-05, 0), \
                           -114431, 210262, 210262, -nan)
reports[-1].sigmaresid = ValErr(0.416984, 0.00064302, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000168259, None, -8.80449e-07, None, 0.000733498, None, -2.34841e-05, None, 0.000733498, None, -2.34841e-05, None, 0.000127239, None, -8.63497e-06, None, 0.000127239, None, -8.63497e-06, None, 0.416986, None, 0.00576853, None, 0.416986, None, 0.00576853, None)

reports.append(Report(604054032, ("CSC", 2, 2, 1, 2), "MEm21_02"))
reports[-1].posNum = 208987
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00150721, 0.00130126, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0461912, 0.0329222, 0), \
                           ValErr(-0.000269108, 0.000647279, 0), \
                           ValErr(0.00117796, 0.00152038, 0), \
                           ValErr(1.02637e-05, 1.91161e-05, 0), \
                           -102265, 208987, 208987, -nan)
reports[-1].sigmaresid = ValErr(0.39471, 0.000610526, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000910478, None, -2.05948e-05, None, 0.000925936, None, -1.85344e-05, None, 0.000925936, None, -1.85344e-05, None, 0.000186778, None, -8.79702e-06, None, 0.000186778, None, -8.79702e-06, None, 0.394714, None, 0.0059436, None, 0.394714, None, 0.0059436, None)

reports.append(Report(604054048, ("CSC", 2, 2, 1, 4), "MEm21_04"))
reports[-1].posNum = 208853
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00280097, 0.00130583, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00768594, 0.0329618, 0), \
                           ValErr(0.000254571, 0.000648821, 0), \
                           ValErr(0.00331533, 0.00152487, 0), \
                           ValErr(-2.56283e-05, 1.91554e-05, 0), \
                           -102477, 208853, 208853, -nan)
reports[-1].sigmaresid = ValErr(0.395235, 0.000611533, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000489581, None, -2.47439e-05, None, 0.000619952, None, -2.81581e-05, None, 0.000619952, None, -2.81581e-05, None, 0.00197034, None, -1.88597e-05, None, 0.00197034, None, -1.88597e-05, None, 0.39524, None, 0.0062993, None, 0.39524, None, 0.0062993, None)

reports.append(Report(604054064, ("CSC", 2, 2, 1, 6), "MEm21_06"))
reports[-1].posNum = 209082
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00251205, 0.00131188, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0304601, 0.0330866, 0), \
                           ValErr(-0.00119261, 0.000651785, 0), \
                           ValErr(0.000979223, 0.00152928, 0), \
                           ValErr(-3.91194e-05, 1.92321e-05, 0), \
                           -103749, 209082, 209082, -nan)
reports[-1].sigmaresid = ValErr(0.397433, 0.000614598, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00161608, None, -1.6158e-05, None, 0.00156094, None, -3.81541e-05, None, 0.00156094, None, -3.81541e-05, None, 0.0010439, None, -1.99696e-05, None, 0.0010439, None, -1.99696e-05, None, 0.397442, None, 0.00593287, None, 0.397442, None, 0.00593287, None)

reports.append(Report(604054080, ("CSC", 2, 2, 1, 8), "MEm21_08"))
reports[-1].posNum = 210132
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00122663, 0.00131177, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0385115, 0.0351534, 0), \
                           ValErr(-0.000607626, 0.000711484, 0), \
                           ValErr(0.000799862, 0.00153244, 0), \
                           ValErr(-1.54985e-05, 2.14647e-05, 0), \
                           -104156, 210132, 210132, -nan)
reports[-1].sigmaresid = ValErr(0.397218, 0.000619548, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000508337, None, -3.17586e-06, None, 0.000602076, None, -7.11699e-06, None, 0.000602076, None, -7.11699e-06, None, 0.000316894, None, -2.94512e-06, None, 0.000316894, None, -2.94512e-06, None, 0.397221, None, 0.00635544, None, 0.397221, None, 0.00635544, None)

reports.append(Report(604054096, ("CSC", 2, 2, 1, 10), "MEm21_10"))
reports[-1].posNum = 209325
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000600022, 0.00131109, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0224368, 0.0331802, 0), \
                           ValErr(-0.000903693, 0.000652633, 0), \
                           ValErr(-0.000432543, 0.00152924, 0), \
                           ValErr(-2.02721e-05, 1.92384e-05, 0), \
                           -104503, 209325, 209325, -nan)
reports[-1].sigmaresid = ValErr(0.398638, 0.000622078, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000850646, None, -8.42661e-06, None, 0.000657964, None, -3.51949e-05, None, 0.000657964, None, -3.51949e-05, None, -0.000597099, None, -1.06513e-05, None, -0.000597099, None, -1.06513e-05, None, 0.398642, None, 0.00604362, None, 0.398642, None, 0.00604362, None)

reports.append(Report(604054112, ("CSC", 2, 2, 1, 12), "MEm21_12"))
reports[-1].posNum = 209400
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000401519, 0.0013087, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00635797, 0.0330732, 0), \
                           ValErr(-0.000468808, 0.00065043, 0), \
                           ValErr(-0.00140672, 0.0015263, 0), \
                           ValErr(-3.79118e-05, 1.92038e-05, 0), \
                           -103997, 209400, 209400, -nan)
reports[-1].sigmaresid = ValErr(0.397606, 0.000620936, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00118947, None, 7.72064e-06, None, 4.61488e-05, None, -1.50924e-05, None, 4.61488e-05, None, -1.50924e-05, None, -0.000582162, None, 7.73071e-06, None, -0.000582162, None, 7.73071e-06, None, 0.397613, None, 0.00604647, None, 0.397613, None, 0.00604647, None)

reports.append(Report(604054128, ("CSC", 2, 2, 1, 14), "MEm21_14"))
reports[-1].posNum = 209736
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000701408, 0.00130354, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0140607, 0.0329698, 0), \
                           ValErr(0.000906922, 0.000647963, 0), \
                           ValErr(-0.000265528, 0.00151957, 0), \
                           ValErr(3.65493e-05, 1.91331e-05, 0), \
                           -103682, 209736, 209736, -nan)
reports[-1].sigmaresid = ValErr(0.396693, 0.00061966, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000356676, None, -1.55951e-05, None, -0.000191836, None, -1.39053e-05, None, -0.000191836, None, -1.39053e-05, None, 0.000253138, None, -3.7481e-06, None, 0.000253138, None, -3.7481e-06, None, 0.396699, None, 0.00606634, None, 0.396699, None, 0.00606634, None)

reports.append(Report(604054144, ("CSC", 2, 2, 1, 16), "MEm21_16"))
reports[-1].posNum = 209292
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00160537, 0.00130987, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0580825, 0.0330232, 0), \
                           ValErr(-0.000225106, 0.000651251, 0), \
                           ValErr(-0.000324651, 0.00152385, 0), \
                           ValErr(2.46911e-05, 1.92367e-05, 0), \
                           -103710, 209292, 209292, -nan)
reports[-1].sigmaresid = ValErr(0.397162, 0.00061387, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00215643, None, -1.04687e-05, None, 0.00204086, None, -7.41803e-06, None, 0.00204086, None, -7.41803e-06, None, 0.00142079, None, -1.55753e-05, None, 0.00142079, None, -1.55753e-05, None, 0.397167, None, 0.00609656, None, 0.397167, None, 0.00609656, None)

reports.append(Report(604054160, ("CSC", 2, 2, 1, 18), "MEm21_18"))
reports[-1].posNum = 209463
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000406637, 0.00130319, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0160231, 0.0329725, 0), \
                           ValErr(-0.000617401, 0.0006492, 0), \
                           ValErr(-0.00221721, 0.00152777, 0), \
                           ValErr(1.71608e-05, 1.91443e-05, 0), \
                           -102848, 209463, 209463, -nan)
reports[-1].sigmaresid = ValErr(0.39537, 0.000610851, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00162605, None, -8.10832e-06, None, 0.00186011, None, -3.26671e-05, None, 0.00186011, None, -3.26671e-05, None, 0.000548059, None, -1.80568e-05, None, 0.000548059, None, -1.80568e-05, None, 0.395373, None, 0.00609973, None, 0.395373, None, 0.00609973, None)

reports.append(Report(604054536, ("CSC", 2, 2, 2, 1), "MEm22_01"))
reports[-1].posNum = 57883
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000993753, 0.00698878, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.14455, 0.17416, 0), \
                           ValErr(-0.00241253, 0.00196147, 0), \
                           ValErr(0.00669764, 0.00917914, 0), \
                           ValErr(1.17439e-06, 5.4115e-05, 0), \
                           -83653.1, 57883, 57883, -nan)
reports[-1].sigmaresid = ValErr(1.02662, 0.00301728, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00208192, None, 2.14559e-05, None, -0.00220343, None, 1.61336e-05, None, -0.00220343, None, 1.61336e-05, None, -0.000761329, None, -3.33778e-05, None, -0.000761329, None, -3.33778e-05, None, 1.02664, None, 0.00663407, None, 1.02664, None, 0.00663407, None)

reports.append(Report(604054552, ("CSC", 2, 2, 2, 3), "MEm22_03"))
reports[-1].posNum = 51520
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0242508, 0.00726426, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0819962, 0.131418, 0), \
                           ValErr(-0.000818704, 0.00151721, 0), \
                           ValErr(-0.0220021, 0.00953226, 0), \
                           ValErr(0.00019811, 5.55608e-05, 0), \
                           -72166.2, 51520, 51520, -nan)
reports[-1].sigmaresid = ValErr(0.981966, 0.00306202, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-7.16231e-05, None, 1.82555e-05, None, -0.00522572, None, 2.33303e-05, None, -0.00522572, None, 2.33303e-05, None, -0.00722231, None, 6.46748e-05, None, -0.00722231, None, 6.46748e-05, None, 0.982104, None, 0.00736176, None, 0.982104, None, 0.00736176, None)

reports.append(Report(604054568, ("CSC", 2, 2, 2, 5), "MEm22_05"))
reports[-1].posNum = 57413
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00707711, 0.00678845, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.292132, 0.174668, 0), \
                           ValErr(-0.00459929, 0.00195415, 0), \
                           ValErr(0.00252404, 0.00910836, 0), \
                           ValErr(-4.52452e-06, 5.27964e-05, 0), \
                           -82053, 57413, 57413, -nan)
reports[-1].sigmaresid = ValErr(1.01028, 0.00298142, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.005064, None, -2.12805e-05, None, 0.00560529, None, 1.13581e-05, None, 0.00560529, None, 1.13581e-05, None, 0.0108994, None, -1.21599e-05, None, 0.0108994, None, -1.21599e-05, None, 1.01035, None, 0.00660341, None, 1.01035, None, 0.00660341, None)

reports.append(Report(604054584, ("CSC", 2, 2, 2, 7), "MEm22_07"))
reports[-1].posNum = 51946
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0038351, 0.00740626, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.195167, 0.179916, 0), \
                           ValErr(-9.57018e-05, 0.00201668, 0), \
                           ValErr(-0.00129894, 0.00954028, 0), \
                           ValErr(-4.47524e-05, 5.64592e-05, 0), \
                           -73534.6, 51946, 51946, -nan)
reports[-1].sigmaresid = ValErr(0.996664, 0.00309213, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0039564, None, -6.45684e-05, None, 0.00239089, None, -7.98394e-05, None, 0.00239089, None, -7.98394e-05, None, -0.00163941, None, -5.6006e-05, None, -0.00163941, None, -5.6006e-05, None, 0.996682, None, 0.00669676, None, 0.996682, None, 0.00669676, None)

reports.append(Report(604054600, ("CSC", 2, 2, 2, 9), "MEm22_09"))
reports[-1].posNum = 54466
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00105711, 0.00708524, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.343895, 0.180714, 0), \
                           ValErr(-0.00233263, 0.00201235, 0), \
                           ValErr(0.000616205, 0.00945617, 0), \
                           ValErr(6.51551e-05, 5.49134e-05, 0), \
                           -77988.2, 54466, 54466, -nan)
reports[-1].sigmaresid = ValErr(1.01301, 0.00306927, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00145817, None, -2.79197e-06, None, 0.00147677, None, -1.11309e-05, None, 0.00147677, None, -1.11309e-05, None, 0.0012392, None, -2.31675e-05, None, 0.0012392, None, -2.31675e-05, None, 1.01307, None, 0.0069239, None, 1.01307, None, 0.0069239, None)

reports.append(Report(604054616, ("CSC", 2, 2, 2, 11), "MEm22_11"))
reports[-1].posNum = 54327
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00245463, 0.00705529, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.316285, 0.183445, 0), \
                           ValErr(-0.00191847, 0.00203979, 0), \
                           ValErr(-0.0120198, 0.00954894, 0), \
                           ValErr(2.67953e-05, 5.45701e-05, 0), \
                           -78079.2, 54327, 54327, -nan)
reports[-1].sigmaresid = ValErr(1.01844, 0.00308967, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0099265, None, -2.66333e-05, None, 0.00890052, None, -2.9979e-06, None, 0.00890052, None, -2.9979e-06, None, 0.00985391, None, -6.41123e-06, None, 0.00985391, None, -6.41123e-06, None, 1.01848, None, 0.00690975, None, 1.01848, None, 0.00690975, None)

reports.append(Report(604054632, ("CSC", 2, 2, 2, 13), "MEm22_13"))
reports[-1].posNum = 50722
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0115931, 0.00754603, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.185871, 0.182866, 0), \
                           ValErr(0.00223899, 0.00203682, 0), \
                           ValErr(0.00673504, 0.0097697, 0), \
                           ValErr(-4.94971e-05, 5.72597e-05, 0), \
                           -72070.8, 50722, 50722, -nan)
reports[-1].sigmaresid = ValErr(1.00196, 0.00314585, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00435357, None, 6.89735e-06, None, 0.00600874, None, -1.6552e-05, None, 0.00600874, None, -1.6552e-05, None, 0.000924897, None, 2.69452e-06, None, 0.000924897, None, 2.69452e-06, None, 1.00199, None, 0.00643711, None, 1.00199, None, 0.00643711, None)

reports.append(Report(604054648, ("CSC", 2, 2, 2, 15), "MEm22_15"))
reports[-1].posNum = 57341
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00019721, 0.00687456, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.129462, 0.17645, 0), \
                           ValErr(0.00467277, 0.00199535, 0), \
                           ValErr(0.0119457, 0.00926769, 0), \
                           ValErr(7.04111e-06, 5.34785e-05, 0), \
                           -82383.6, 57341, 57341, -nan)
reports[-1].sigmaresid = ValErr(1.01795, 0.00300594, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00665604, None, 5.32022e-06, None, -0.0056346, None, 1.75302e-06, None, -0.0056346, None, 1.75302e-06, None, -0.00560489, None, 4.13868e-05, None, -0.00560489, None, 4.13868e-05, None, 1.01802, None, 0.00681419, None, 1.01802, None, 0.00681419, None)

reports.append(Report(604054664, ("CSC", 2, 2, 2, 17), "MEm22_17"))
reports[-1].posNum = 51721
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0180399, 0.00723244, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.400426, 0.184132, 0), \
                           ValErr(-0.00124816, 0.00205566, 0), \
                           ValErr(-0.00855815, 0.00967133, 0), \
                           ValErr(0.000132319, 5.54327e-05, 0), \
                           -72823.3, 51721, 51721, -nan)
reports[-1].sigmaresid = ValErr(0.989127, 0.00307543, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00788641, None, 1.64529e-05, None, -0.00833956, None, 1.84194e-05, None, -0.00833956, None, 1.84194e-05, None, -0.0115956, None, -1.54349e-05, None, -0.0115956, None, -1.54349e-05, None, 0.989225, None, 0.00683734, None, 0.989225, None, 0.00683734, None)

reports.append(Report(604054680, ("CSC", 2, 2, 2, 19), "MEm22_19"))
reports[-1].posNum = 57412
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0167649, 0.00698293, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.331719, 0.173379, 0), \
                           ValErr(-0.0020385, 0.00196453, 0), \
                           ValErr(-0.00554803, 0.00912535, 0), \
                           ValErr(0.000113099, 5.42052e-05, 0), \
                           -82562, 57412, 57412, -nan)
reports[-1].sigmaresid = ValErr(1.01931, 0.00300809, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0027475, None, 9.36592e-07, None, -0.00974198, None, 5.72251e-05, None, -0.00974198, None, 5.72251e-05, None, -0.0145807, None, 7.63866e-05, None, -0.0145807, None, 7.63866e-05, None, 1.01939, None, 0.00651505, None, 1.01939, None, 0.00651505, None)

reports.append(Report(604054696, ("CSC", 2, 2, 2, 21), "MEm22_21"))
reports[-1].posNum = 50771
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00421642, 0.00718812, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.208111, 0.182769, 0), \
                           ValErr(-0.000942277, 0.00201528, 0), \
                           ValErr(0.00155006, 0.00956876, 0), \
                           ValErr(-8.69233e-05, 5.48089e-05, 0), \
                           -71058.5, 50771, 50771, -nan)
reports[-1].sigmaresid = ValErr(0.980836, 0.00307804, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00785533, None, 4.30237e-05, None, -0.00865516, None, 1.20939e-05, None, -0.00865516, None, 1.20939e-05, None, -0.0155981, None, 2.12249e-05, None, -0.0155981, None, 2.12249e-05, None, 0.980876, None, 0.00682572, None, 0.980876, None, 0.00682572, None)

reports.append(Report(604054712, ("CSC", 2, 2, 2, 23), "MEm22_23"))
reports[-1].posNum = 57605
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00112205, 0.00684686, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.111947, 0.173209, 0), \
                           ValErr(-6.68381e-05, 0.00132682, 0), \
                           ValErr(0.000439417, 0.00887716, 0), \
                           ValErr(7.02607e-05, 5.10111e-05, 0), \
                           -83081.4, 57605, 57605, -nan)
reports[-1].sigmaresid = ValErr(1.02359, 0.0029572, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00044142, None, -6.79444e-06, None, 0.00132101, None, 2.08926e-05, None, 0.00132101, None, 2.08926e-05, None, 0.000990629, None, 1.57303e-05, None, 0.000990629, None, 1.57303e-05, None, 1.02362, None, 0.00671191, None, 1.02362, None, 0.00671191, None)

reports.append(Report(604054728, ("CSC", 2, 2, 2, 25), "MEm22_25"))
reports[-1].posNum = 52049
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00467047, 0.00735496, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0486172, 0.18025, 0), \
                           ValErr(-0.00201307, 0.00200901, 0), \
                           ValErr(0.0027298, 0.00955218, 0), \
                           ValErr(5.17416e-05, 5.61955e-05, 0), \
                           -73775.6, 52049, 52049, -nan)
reports[-1].sigmaresid = ValErr(0.998485, 0.0030947, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00188902, None, 3.21081e-05, None, -0.00390574, None, 1.10206e-05, None, -0.00390574, None, 1.10206e-05, None, -0.0102871, None, 5.07401e-05, None, -0.0102871, None, 5.07401e-05, None, 0.998512, None, 0.00651228, None, 0.998512, None, 0.00651228, None)

reports.append(Report(604054744, ("CSC", 2, 2, 2, 27), "MEm22_27"))
reports[-1].posNum = 54576
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00958348, 0.00709687, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.293757, 0.180119, 0), \
                           ValErr(-0.000968814, 0.00202831, 0), \
                           ValErr(0.00200913, 0.00942744, 0), \
                           ValErr(7.63145e-06, 5.51504e-05, 0), \
                           -78280.8, 54576, 54576, -nan)
reports[-1].sigmaresid = ValErr(1.01552, 0.0030738, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00811144, None, 2.21259e-05, None, -0.0100466, None, 2.23216e-05, None, -0.0100466, None, 2.23216e-05, None, -0.00439584, None, -1.56032e-06, None, -0.00439584, None, -1.56032e-06, None, 1.01555, None, 0.00684389, None, 1.01555, None, 0.00684389, None)

reports.append(Report(604054760, ("CSC", 2, 2, 2, 29), "MEm22_29"))
reports[-1].posNum = 54896
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00811041, 0.0070802, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.243707, 0.172439, 0), \
                           ValErr(0.000845128, 0.00171053, 0), \
                           ValErr(0.00293304, 0.00917564, 0), \
                           ValErr(-6.86825e-05, 4.8422e-05, 0), \
                           -78880.4, 54896, 54896, -nan)
reports[-1].sigmaresid = ValErr(1.01813, 0.00304639, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00121065, None, -9.11281e-07, None, 0.00388227, None, -3.45545e-05, None, 0.00388227, None, -3.45545e-05, None, -0.000187239, None, -3.89352e-05, None, -0.000187239, None, -3.89352e-05, None, 1.01816, None, 0.00673841, None, 1.01816, None, 0.00673841, None)

reports.append(Report(604054776, ("CSC", 2, 2, 2, 31), "MEm22_31"))
reports[-1].posNum = 52106
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00631228, 0.0075458, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0216703, 0.104122, 0), \
                           ValErr(0.000465194, 0.00202672, 0), \
                           ValErr(0.00234513, 0.00964325, 0), \
                           ValErr(-8.21718e-05, 5.65387e-05, 0), \
                           -74447.4, 52106, 52106, -nan)
reports[-1].sigmaresid = ValErr(1.00988, 0.00310686, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00304978, None, -1.04299e-05, None, 0.00161928, None, -7.10238e-05, None, 0.00161928, None, -7.10238e-05, None, -0.00447558, None, -3.85342e-05, None, -0.00447558, None, -3.85342e-05, None, 1.0099, None, 0.00672546, None, 1.0099, None, 0.00672546, None)

reports.append(Report(604054792, ("CSC", 2, 2, 2, 33), "MEm22_33"))
reports[-1].posNum = 57374
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00960094, 0.00683595, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.078675, 0.175163, 0), \
                           ValErr(-0.00391939, 0.00198416, 0), \
                           ValErr(0.0114693, 0.0091328, 0), \
                           ValErr(-8.15005e-05, 5.34221e-05, 0), \
                           -82498, 57374, 57374, -nan)
reports[-1].sigmaresid = ValErr(1.01914, 0.00300858, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0048595, None, 1.05261e-06, None, 0.00121515, None, -6.25744e-06, None, 0.00121515, None, -6.25744e-06, None, 0.00575772, None, -1.76188e-05, None, 0.00575772, None, -1.76188e-05, None, 1.01921, None, 0.00700954, None, 1.01921, None, 0.00700954, None)

reports.append(Report(604054808, ("CSC", 2, 2, 2, 35), "MEm22_35"))
reports[-1].posNum = 50398
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0147569, 0.00734319, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.154524, 0.175292, 0), \
                           ValErr(-0.000400283, 0.00185952, 0), \
                           ValErr(-0.0141891, 0.00945053, 0), \
                           ValErr(2.65245e-05, 4.68284e-05, 0), \
                           -71015.5, 50398, 50398, -nan)
reports[-1].sigmaresid = ValErr(0.990204, 0.00311424, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00919678, None, -1.58299e-05, None, -0.0069038, None, 3.19382e-06, None, -0.0069038, None, 3.19382e-06, None, -0.00819504, None, -6.15848e-06, None, -0.00819504, None, -6.15848e-06, None, 0.990232, None, 0.00690202, None, 0.990232, None, 0.00690202, None)

reports.append(Report(604054544, ("CSC", 2, 2, 2, 2), "MEm22_02"))
reports[-1].posNum = 53950
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0233485, 0.0070869, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.060889, 0.174229, 0), \
                           ValErr(-0.00106794, 0.00192872, 0), \
                           ValErr(-0.0209333, 0.00912502, 0), \
                           ValErr(0.000125716, 5.4254e-05, 0), \
                           -77106.5, 53950, 53950, -nan)
reports[-1].sigmaresid = ValErr(1.01034, 0.00307577, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00610311, None, 1.70602e-05, None, -0.00810236, None, 4.08463e-05, None, -0.00810236, None, 4.08463e-05, None, -0.00851547, None, 6.40174e-05, None, -0.00851547, None, 6.40174e-05, None, 1.01042, None, 0.00717044, None, 1.01042, None, 0.00717044, None)

reports.append(Report(604054560, ("CSC", 2, 2, 2, 4), "MEm22_04"))
reports[-1].posNum = 50215
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00341562, 0.00732315, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0805308, 0.182196, 0), \
                           ValErr(-0.000718433, 0.00201186, 0), \
                           ValErr(0.0037872, 0.00957769, 0), \
                           ValErr(-1.30728e-05, 5.54355e-05, 0), \
                           -70741, 50215, 50215, -nan)
reports[-1].sigmaresid = ValErr(0.989875, 0.00312356, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00342729, None, -2.25166e-05, None, 0.00107446, None, -1.06007e-05, None, 0.00107446, None, -1.06007e-05, None, 5.76956e-05, None, -3.44189e-05, None, 5.76956e-05, None, -3.44189e-05, None, 0.989879, None, 0.00663705, None, 0.989879, None, 0.00663705, None)

reports.append(Report(604054576, ("CSC", 2, 2, 2, 6), "MEm22_06"))
reports[-1].posNum = 56084
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0194713, 0.0070214, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.310707, 0.17106, 0), \
                           ValErr(0.000808349, 0.00193326, 0), \
                           ValErr(0.0299832, 0.00900995, 0), \
                           ValErr(-9.36329e-05, 5.47362e-05, 0), \
                           -80479.5, 56084, 56084, -nan)
reports[-1].sigmaresid = ValErr(1.01617, 0.00303411, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00128925, None, -1.30725e-05, None, 0.00112605, None, -1.56502e-05, None, 0.00112605, None, -1.56502e-05, None, 0.00614785, None, -2.65239e-05, None, 0.00614785, None, -2.65239e-05, None, 1.0163, None, 0.00690286, None, 1.0163, None, 0.00690286, None)

reports.append(Report(604054592, ("CSC", 2, 2, 2, 8), "MEm22_08"))
reports[-1].posNum = 48232
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.012174, 0.00753054, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.191552, 0.182332, 0), \
                           ValErr(-0.0011316, 0.00199421, 0), \
                           ValErr(0.00670093, 0.00967536, 0), \
                           ValErr(-5.77476e-05, 5.62603e-05, 0), \
                           -67770.9, 48232, 48232, -nan)
reports[-1].sigmaresid = ValErr(0.986259, 0.00317548, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0011066, None, -4.91181e-06, None, 0.00632336, None, 1.88255e-05, None, 0.00632336, None, 1.88255e-05, None, 0.0182911, None, -3.11139e-05, None, 0.0182911, None, -3.11139e-05, None, 0.986288, None, 0.00672512, None, 0.986288, None, 0.00672512, None)

reports.append(Report(604054608, ("CSC", 2, 2, 2, 10), "MEm22_10"))
reports[-1].posNum = 57446
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00791553, 0.00691981, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.116995, 0.170408, 0), \
                           ValErr(-0.00242134, 0.00191927, 0), \
                           ValErr(0.000448343, 0.00892855, 0), \
                           ValErr(-1.86385e-05, 5.38993e-05, 0), \
                           -82337.3, 57446, 57446, -nan)
reports[-1].sigmaresid = ValErr(1.01446, 0.0029929, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00764569, None, -1.10214e-05, None, 0.00703175, None, 2.23054e-06, None, 0.00703175, None, 2.23054e-06, None, 0.00407629, None, -1.0603e-05, None, 0.00407629, None, -1.0603e-05, None, 1.01448, None, 0.00680192, None, 1.01448, None, 0.00680192, None)

reports.append(Report(604054624, ("CSC", 2, 2, 2, 12), "MEm22_12"))
reports[-1].posNum = 49716
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0016438, 0.00734528, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.253847, 0.177382, 0), \
                           ValErr(-0.00155418, 0.00195161, 0), \
                           ValErr(-0.0143993, 0.00934488, 0), \
                           ValErr(-1.95277e-05, 5.55636e-05, 0), \
                           -69403.7, 49716, 49716, -nan)
reports[-1].sigmaresid = ValErr(0.977327, 0.0030994, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000624548, None, 5.42808e-06, None, 0.00476141, None, 2.84764e-05, None, 0.00476141, None, 2.84764e-05, None, 0.00707312, None, 1.27373e-05, None, 0.00707312, None, 1.27373e-05, None, 0.977391, None, 0.00690012, None, 0.977391, None, 0.00690012, None)

reports.append(Report(604054640, ("CSC", 2, 2, 2, 14), "MEm22_14"))
reports[-1].posNum = 55780
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000621494, 0.00692562, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.236383, 0.170905, 0), \
                           ValErr(-0.00578947, 0.00192129, 0), \
                           ValErr(-0.00296486, 0.00898466, 0), \
                           ValErr(-4.22662e-05, 5.35741e-05, 0), \
                           -79454.1, 55780, 55780, -nan)
reports[-1].sigmaresid = ValErr(1.0055, 0.00301041, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0016266, None, 1.39816e-05, None, -0.000650753, None, -7.86883e-06, None, -0.000650753, None, -7.86883e-06, None, -0.000817756, None, -7.96856e-07, None, -0.000817756, None, -7.96856e-07, None, 1.0056, None, 0.00674903, None, 1.0056, None, 0.00674903, None)

reports.append(Report(604054656, ("CSC", 2, 2, 2, 16), "MEm22_16"))
reports[-1].posNum = 50017
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000993996, 0.00736566, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.184122, 0.182768, 0), \
                           ValErr(0.000309278, 0.00200292, 0), \
                           ValErr(-0.00225633, 0.00962047, 0), \
                           ValErr(1.41604e-05, 5.5648e-05, 0), \
                           -70709.8, 50017, 50017, -nan)
reports[-1].sigmaresid = ValErr(0.994791, 0.00314528, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00732793, None, 1.40858e-05, None, 0.000602692, None, -1.21354e-06, None, 0.000602692, None, -1.21354e-06, None, 6.96534e-05, None, -1.14543e-05, None, 6.96534e-05, None, -1.14543e-05, None, 0.994803, None, 0.00657163, None, 0.994803, None, 0.00657163, None)

reports.append(Report(604054672, ("CSC", 2, 2, 2, 18), "MEm22_18"))
reports[-1].posNum = 52800
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00289052, 0.00714119, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.139852, 0.174698, 0), \
                           ValErr(0.000640233, 0.00193495, 0), \
                           ValErr(0.0107331, 0.009166, 0), \
                           ValErr(3.95824e-05, 5.47141e-05, 0), \
                           -75043.9, 52800, 52800, -nan)
reports[-1].sigmaresid = ValErr(1.00235, 0.00308453, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00708145, None, -3.56526e-05, None, -0.00662842, None, -1.53236e-05, None, -0.00662842, None, -1.53236e-05, None, -0.0135421, None, -4.44206e-05, None, -0.0135421, None, -4.44206e-05, None, 1.00239, None, 0.00718973, None, 1.00239, None, 0.00718973, None)

reports.append(Report(604054688, ("CSC", 2, 2, 2, 20), "MEm22_20"))
reports[-1].posNum = 54415
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0027244, 0.00713727, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0169192, 0.173777, 0), \
                           ValErr(0.00364387, 0.00193838, 0), \
                           ValErr(-0.000999105, 0.00916245, 0), \
                           ValErr(-5.17351e-05, 5.45175e-05, 0), \
                           -77726.9, 54415, 54415, -nan)
reports[-1].sigmaresid = ValErr(1.00952, 0.00306014, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00327578, None, 7.91607e-06, None, 0.00120752, None, 7.51666e-05, None, 0.00120752, None, 7.51666e-05, None, 0.00413218, None, -1.40365e-06, None, 0.00413218, None, -1.40365e-06, None, 1.00956, None, 0.00651068, None, 1.00956, None, 0.00651068, None)

reports.append(Report(604054704, ("CSC", 2, 2, 2, 22), "MEm22_22"))
reports[-1].posNum = 50240
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00324497, 0.00737742, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.232633, 0.182733, 0), \
                           ValErr(-0.000827699, 0.00201476, 0), \
                           ValErr(0.00566791, 0.00961054, 0), \
                           ValErr(2.36239e-06, 5.59711e-05, 0), \
                           -71053.3, 50240, 50240, -nan)
reports[-1].sigmaresid = ValErr(0.995351, 0.00314005, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00106246, None, -1.18287e-08, None, 0.000792783, None, -3.50742e-06, None, 0.000792783, None, -3.50742e-06, None, 0.0113049, None, -2.25945e-05, None, 0.0113049, None, -2.25945e-05, None, 0.995371, None, 0.00683692, None, 0.995371, None, 0.00683692, None)

reports.append(Report(604054720, ("CSC", 2, 2, 2, 24), "MEm22_24"))
reports[-1].posNum = 55534
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0102705, 0.00681739, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0324978, 0.163361, 0), \
                           ValErr(0.000289768, 0.00127088, 0), \
                           ValErr(0.00175299, 0.00885235, 0), \
                           ValErr(4.24381e-05, 5.27023e-05, 0), \
                           -78917.3, 55534, 55534, -nan)
reports[-1].sigmaresid = ValErr(1.00212, 0.0029904, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00831148, None, 1.36546e-05, None, -0.00943646, None, -3.12921e-06, None, -0.00943646, None, -3.12921e-06, None, -0.00538977, None, -6.30959e-05, None, -0.00538977, None, -6.30959e-05, None, 1.00213, None, 0.00672854, None, 1.00213, None, 0.00672854, None)

reports.append(Report(604054736, ("CSC", 2, 2, 2, 26), "MEm22_26"))
reports[-1].posNum = 49219
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00403778, 0.00755088, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0578032, 0.180873, 0), \
                           ValErr(-0.000643523, 0.00197957, 0), \
                           ValErr(0.00768292, 0.00964849, 0), \
                           ValErr(-5.79432e-06, 5.64171e-05, 0), \
                           -69306.1, 49219, 49219, -nan)
reports[-1].sigmaresid = ValErr(0.989236, 0.00315296, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00321445, None, 3.34464e-07, None, 4.69004e-05, None, 2.72665e-05, None, 4.69004e-05, None, 2.72665e-05, None, 0.00294643, None, -2.5831e-05, None, 0.00294643, None, -2.5831e-05, None, 0.989245, None, 0.00651854, None, 0.989245, None, 0.00651854, None)

reports.append(Report(604054752, ("CSC", 2, 2, 2, 28), "MEm22_28"))
reports[-1].posNum = 57291
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00900832, 0.00694901, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0582417, 0.170125, 0), \
                           ValErr(0.00071138, 0.00192895, 0), \
                           ValErr(0.013674, 0.00894364, 0), \
                           ValErr(-5.81553e-05, 5.37657e-05, 0), \
                           -82221.2, 57291, 57291, -nan)
reports[-1].sigmaresid = ValErr(1.01634, 0.0030025, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00074364, None, 2.85012e-06, None, -1.37797e-05, None, 4.18802e-05, None, -1.37797e-05, None, 4.18802e-05, None, 0.00298024, None, -2.20569e-05, None, 0.00298024, None, -2.20569e-05, None, 1.01637, None, 0.00661592, None, 1.01637, None, 0.00661592, None)

reports.append(Report(604054768, ("CSC", 2, 2, 2, 30), "MEm22_30"))
reports[-1].posNum = 49007
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00866497, 0.00742404, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0406513, 0.179473, 0), \
                           ValErr(-0.00155908, 0.00196074, 0), \
                           ValErr(-0.0115489, 0.00949872, 0), \
                           ValErr(5.36609e-05, 5.57223e-05, 0), \
                           -68874.3, 49007, 49007, -nan)
reports[-1].sigmaresid = ValErr(0.986551, 0.00315122, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0122172, None, -9.75656e-06, None, 0.0165941, None, -4.2172e-05, None, 0.0165941, None, -4.2172e-05, None, 0.0125796, None, -6.61457e-05, None, 0.0125796, None, -6.61457e-05, None, 0.986576, None, 0.00681884, None, 0.986576, None, 0.00681884, None)

reports.append(Report(604054784, ("CSC", 2, 2, 2, 32), "MEm22_32"))
reports[-1].posNum = 56663
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00491054, 0.00694643, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0575092, 0.171112, 0), \
                           ValErr(-0.00247437, 0.00192772, 0), \
                           ValErr(-0.000361025, 0.00896988, 0), \
                           ValErr(-4.6625e-05, 5.38027e-05, 0), \
                           -81448.1, 56663, 56663, -nan)
reports[-1].sigmaresid = ValErr(1.01865, 0.00302593, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000622444, None, 3.82501e-05, None, 0.00326922, None, 5.66265e-05, None, 0.00326922, None, 5.66265e-05, None, 0.00995438, None, 8.1877e-06, None, 0.00995438, None, 8.1877e-06, None, 1.01867, None, 0.00664146, None, 1.01867, None, 0.00664146, None)

reports.append(Report(604054800, ("CSC", 2, 2, 2, 34), "MEm22_34"))
reports[-1].posNum = 51538
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00437696, 0.0071988, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.242751, 0.17956, 0), \
                           ValErr(-0.00140908, 0.00196743, 0), \
                           ValErr(-0.0173055, 0.00939858, 0), \
                           ValErr(7.3447e-05, 5.47382e-05, 0), \
                           -72366.6, 51538, 51538, -nan)
reports[-1].sigmaresid = ValErr(0.985313, 0.003069, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00672527, None, 3.62069e-06, None, 0.00696996, None, 8.38639e-06, None, 0.00696996, None, 8.38639e-06, None, -0.00304119, None, 6.21474e-05, None, -0.00304119, None, 6.21474e-05, None, 0.985368, None, 0.0065058, None, 0.985368, None, 0.0065058, None)

reports.append(Report(604054816, ("CSC", 2, 2, 2, 36), "MEm22_36"))
reports[-1].posNum = 54717
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00797341, 0.00711799, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0223638, 0.171702, 0), \
                           ValErr(0.00268751, 0.00192118, 0), \
                           ValErr(0.01129, 0.00907385, 0), \
                           ValErr(-8.01576e-05, 5.47547e-05, 0), \
                           -77996.6, 54717, 54717, -nan)
reports[-1].sigmaresid = ValErr(1.00654, 0.00304267, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00768324, None, 1.40128e-05, None, -0.000804978, None, -2.38624e-05, None, -0.000804978, None, -2.38624e-05, None, 0.00289554, None, -4.42535e-05, None, 0.00289554, None, -4.42535e-05, None, 1.00658, None, 0.00683241, None, 1.00658, None, 0.00683241, None)

reports.append(Report(604058120, ("CSC", 2, 3, 1, 1), "MEm31_01"))
reports[-1].posNum = 166847
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0032846, 0.00182045, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0461199, 0.0502757, 0), \
                           ValErr(0.00194805, 0.00112579, 0), \
                           ValErr(-0.00487455, 0.00224832, 0), \
                           ValErr(3.45261e-05, 2.98621e-05, 0), \
                           -120915, 166847, 166847, -nan)
reports[-1].sigmaresid = ValErr(0.499456, 0.000864616, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000753989, None, -6.79557e-06, None, 0.000633166, None, -2.04618e-05, None, 0.000633166, None, -2.04618e-05, None, -0.000168801, None, -8.73964e-07, None, -0.000168801, None, -8.73964e-07, None, 0.499474, None, 0.00590586, None, 0.499474, None, 0.00590586, None)

reports.append(Report(604058136, ("CSC", 2, 3, 1, 3), "MEm31_03"))
reports[-1].posNum = 169358
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00500756, 0.00180957, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0450641, 0.0500327, 0), \
                           ValErr(-0.00183224, 0.00112383, 0), \
                           ValErr(-0.0034028, 0.00223401, 0), \
                           ValErr(-2.61745e-05, 2.97594e-05, 0), \
                           -123068, 169358, 169358, -nan)
reports[-1].sigmaresid = ValErr(0.500443, 0.00085988, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00453231, None, 3.98884e-06, None, 0.00291952, None, 3.23883e-06, None, 0.00291952, None, 3.23883e-06, None, 0.0035437, None, -4.80546e-06, None, 0.0035437, None, -4.80546e-06, None, 0.500451, None, 0.00597719, None, 0.500451, None, 0.00597719, None)

reports.append(Report(604058152, ("CSC", 2, 3, 1, 5), "MEm31_05"))
reports[-1].posNum = 169031
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000989991, 0.00181497, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0959034, 0.0501364, 0), \
                           ValErr(-0.000566862, 0.00112421, 0), \
                           ValErr(-0.000173095, 0.00224343, 0), \
                           ValErr(1.48738e-05, 2.98585e-05, 0), \
                           -122948, 169031, 169031, -nan)
reports[-1].sigmaresid = ValErr(0.500789, 0.000861304, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00238031, None, -2.16417e-05, None, -0.00103036, None, -3.01694e-05, None, -0.00103036, None, -3.01694e-05, None, 0.000267269, None, -1.09859e-05, None, 0.000267269, None, -1.09859e-05, None, 0.500795, None, 0.00594893, None, 0.500795, None, 0.00594893, None)

reports.append(Report(604058168, ("CSC", 2, 3, 1, 7), "MEm31_07"))
reports[-1].posNum = 167387
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0043974, 0.00181757, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0163541, 0.0499608, 0), \
                           ValErr(0.00216573, 0.00111621, 0), \
                           ValErr(-0.00303277, 0.00223698, 0), \
                           ValErr(-3.091e-05, 2.97903e-05, 0), \
                           -120702, 167387, 167387, -nan)
reports[-1].sigmaresid = ValErr(0.497657, 0.00086011, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00237082, None, 2.21287e-05, None, 0.00249105, None, 3.09511e-05, None, 0.00249105, None, 3.09511e-05, None, 0.00358655, None, 1.21013e-05, None, 0.00358655, None, 1.21013e-05, None, 0.497666, None, 0.00585013, None, 0.497666, None, 0.00585013, None)

reports.append(Report(604058184, ("CSC", 2, 3, 1, 9), "MEm31_09"))
reports[-1].posNum = 167212
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000843489, 0.00181425, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0140794, 0.0502756, 0), \
                           ValErr(-0.00113029, 0.00112486, 0), \
                           ValErr(-0.000200975, 0.00224866, 0), \
                           ValErr(4.12355e-05, 2.98643e-05, 0), \
                           -120754, 167212, 167212, -nan)
reports[-1].sigmaresid = ValErr(0.498189, 0.000861481, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000541602, None, -2.9281e-05, None, -0.000760069, None, -2.83865e-05, None, -0.000760069, None, -2.83865e-05, None, -0.000441794, None, -2.63144e-05, None, -0.000441794, None, -2.63144e-05, None, 0.498194, None, 0.00616706, None, 0.498194, None, 0.00616706, None)

reports.append(Report(604058200, ("CSC", 2, 3, 1, 11), "MEm31_11"))
reports[-1].posNum = 166924
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00573336, 0.00181776, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0532979, 0.0502868, 0), \
                           ValErr(-0.000133135, 0.00112301, 0), \
                           ValErr(0.00483112, 0.00224499, 0), \
                           ValErr(3.34583e-05, 2.98566e-05, 0), \
                           -120792, 166924, 166924, -nan)
reports[-1].sigmaresid = ValErr(0.498923, 0.000863494, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00272444, None, -2.95628e-05, None, -0.00280001, None, -4.62181e-05, None, -0.00280001, None, -4.62181e-05, None, -0.00372247, None, -3.61577e-05, None, -0.00372247, None, -3.61577e-05, None, 0.498931, None, 0.0059577, None, 0.498931, None, 0.0059577, None)

reports.append(Report(604058216, ("CSC", 2, 3, 1, 13), "MEm31_13"))
reports[-1].posNum = 168133
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00151174, 0.00180951, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.107851, 0.0498924, 0), \
                           ValErr(0.000499143, 0.00111348, 0), \
                           ValErr(-0.0011081, 0.00223272, 0), \
                           ValErr(5.09836e-05, 2.96238e-05, 0), \
                           -121193, 168133, 168133, -nan)
reports[-1].sigmaresid = ValErr(0.497518, 0.000857961, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00126507, None, -8.43903e-06, None, -0.00191811, None, -5.58711e-08, None, -0.00191811, None, -5.58711e-08, None, -0.00149389, None, 6.11642e-06, None, -0.00149389, None, 6.11642e-06, None, 0.497533, None, 0.00606296, None, 0.497533, None, 0.00606296, None)

reports.append(Report(604058232, ("CSC", 2, 3, 1, 15), "MEm31_15"))
reports[-1].posNum = 167415
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-1.33292e-05, 0.00181225, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0385311, 0.0500839, 0), \
                           ValErr(-9.64162e-05, 0.00111584, 0), \
                           ValErr(0.0030009, 0.00223431, 0), \
                           ValErr(-6.51329e-06, 2.9696e-05, 0), \
                           -120951, 167415, 167415, -nan)
reports[-1].sigmaresid = ValErr(0.498338, 0.000861215, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00138172, None, 8.23832e-06, None, 0.00169463, None, -1.51383e-05, None, 0.00169463, None, -1.51383e-05, None, 0.00150283, None, -2.93187e-06, None, 0.00150283, None, -2.93187e-06, None, 0.498342, None, 0.0059863, None, 0.498342, None, 0.0059863, None)

reports.append(Report(604058248, ("CSC", 2, 3, 1, 17), "MEm31_17"))
reports[-1].posNum = 167992
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00240077, 0.00180903, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0134207, 0.0500499, 0), \
                           ValErr(0.000424371, 0.00111677, 0), \
                           ValErr(0.00370964, 0.00223518, 0), \
                           ValErr(3.90226e-05, 2.96726e-05, 0), \
                           -121325, 167992, 167992, -nan)
reports[-1].sigmaresid = ValErr(0.498213, 0.000859521, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00032514, None, -1.11024e-05, None, -8.26175e-05, None, -1.21657e-05, None, -8.26175e-05, None, -1.21657e-05, None, 0.00205551, None, -1.23008e-05, None, 0.00205551, None, -1.23008e-05, None, 0.498217, None, 0.00597277, None, 0.498217, None, 0.00597277, None)

reports.append(Report(604058128, ("CSC", 2, 3, 1, 2), "MEm31_02"))
reports[-1].posNum = 172610
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00140069, 0.00184996, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0136312, 0.052439, 0), \
                           ValErr(-1.22607e-05, 0.00117514, 0), \
                           ValErr(-0.000709374, 0.00234738, 0), \
                           ValErr(1.45787e-05, 3.03494e-05, 0), \
                           -130605, 172610, 172610, -nan)
reports[-1].sigmaresid = ValErr(0.51567, 0.000877656, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00176014, None, -1.15325e-05, None, -0.00172807, None, -4.87427e-06, None, -0.00172807, None, -4.87427e-06, None, -0.00208868, None, -1.48242e-05, None, -0.00208868, None, -1.48242e-05, None, 0.515671, None, 0.00588376, None, 0.515671, None, 0.00588376, None)

reports.append(Report(604058144, ("CSC", 2, 3, 1, 4), "MEm31_04"))
reports[-1].posNum = 172127
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000110075, 0.00184974, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.117068, 0.0522718, 0), \
                           ValErr(0.00141898, 0.00116689, 0), \
                           ValErr(0.00137792, 0.00233608, 0), \
                           ValErr(-3.18e-05, 3.01523e-05, 0), \
                           -129775, 172127, 172127, -nan)
reports[-1].sigmaresid = ValErr(0.514278, 0.000875807, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000191396, None, 1.4047e-06, None, 0.000722328, None, 3.14494e-06, None, 0.000722328, None, 3.14494e-06, None, -0.000662853, None, -4.0724e-06, None, -0.000662853, None, -4.0724e-06, None, 0.514294, None, 0.00597334, None, 0.514294, None, 0.00597334, None)

reports.append(Report(604058160, ("CSC", 2, 3, 1, 6), "MEm31_06"))
reports[-1].posNum = 172016
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000517978, 0.00186594, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0541097, 0.0526558, 0), \
                           ValErr(-0.000384422, 0.00117636, 0), \
                           ValErr(0.000518251, 0.00235731, 0), \
                           ValErr(5.88171e-06, 3.05515e-05, 0), \
                           -131104, 172016, 172016, -nan)
reports[-1].sigmaresid = ValErr(0.51852, 0.000884029, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00233863, None, -1.02993e-05, None, 0.000835066, None, -2.20979e-05, None, 0.000835066, None, -2.20979e-05, None, -0.00173417, None, -2.84581e-05, None, -0.00173417, None, -2.84581e-05, None, 0.518522, None, 0.00578106, None, 0.518522, None, 0.00578106, None)

reports.append(Report(604058176, ("CSC", 2, 3, 1, 8), "MEm31_08"))
reports[-1].posNum = 172584
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00115766, 0.00185641, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.105881, 0.0526217, 0), \
                           ValErr(0.000320663, 0.00117501, 0), \
                           ValErr(-0.00223188, 0.00234749, 0), \
                           ValErr(2.31344e-05, 3.05133e-05, 0), \
                           -131275, 172584, 172584, -nan)
reports[-1].sigmaresid = ValErr(0.517736, 0.00088124, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00106242, None, -2.90086e-06, None, 2.31391e-05, None, -1.09044e-05, None, 2.31391e-05, None, -1.09044e-05, None, -0.000912166, None, -1.81426e-05, None, -0.000912166, None, -1.81426e-05, None, 0.517744, None, 0.00574572, None, 0.517744, None, 0.00574572, None)

reports.append(Report(604058192, ("CSC", 2, 3, 1, 10), "MEm31_10"))
reports[-1].posNum = 171637
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00321775, 0.00187231, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.00466949, 0.053112, 0), \
                           ValErr(0.00026426, 0.00118472, 0), \
                           ValErr(-0.00145555, 0.00236851, 0), \
                           ValErr(-1.21337e-05, 3.07561e-05, 0), \
                           -131672, 171637, 171637, -nan)
reports[-1].sigmaresid = ValErr(0.521115, 0.000889434, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00241945, None, 1.49706e-05, None, 0.0023454, None, -6.16669e-07, None, 0.0023454, None, -6.16669e-07, None, 0.00404274, None, 7.35015e-06, None, 0.00404274, None, 7.35015e-06, None, 0.521115, None, 0.0058931, None, 0.521115, None, 0.0058931, None)

reports.append(Report(604058208, ("CSC", 2, 3, 1, 12), "MEm31_12"))
reports[-1].posNum = 171852
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00535886, 0.00186675, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.00613573, 0.0528957, 0), \
                           ValErr(7.2668e-05, 0.00118024, 0), \
                           ValErr(-0.00432767, 0.00235627, 0), \
                           ValErr(-9.51064e-06, 3.07046e-05, 0), \
                           -131349, 171852, 171852, -nan)
reports[-1].sigmaresid = ValErr(0.519639, 0.000886359, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00307975, None, 3.78345e-06, None, 0.0028768, None, -2.87671e-07, None, 0.0028768, None, -2.87671e-07, None, 0.00372843, None, 1.80426e-05, None, 0.00372843, None, 1.80426e-05, None, 0.519644, None, 0.00582166, None, 0.519644, None, 0.00582166, None)

reports.append(Report(604058224, ("CSC", 2, 3, 1, 14), "MEm31_14"))
reports[-1].posNum = 171961
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00136553, 0.0018645, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0216238, 0.0527625, 0), \
                           ValErr(-0.00229656, 0.00117712, 0), \
                           ValErr(0.000176463, 0.00235661, 0), \
                           ValErr(1.01182e-05, 3.06291e-05, 0), \
                           -131245, 171961, 171961, -nan)
reports[-1].sigmaresid = ValErr(0.519071, 0.000885109, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00110008, None, -7.40383e-06, None, -0.00121884, None, -1.65837e-05, None, -0.00121884, None, -1.65837e-05, None, -0.00139572, None, -1.00711e-05, None, -0.00139572, None, -1.00711e-05, None, 0.519077, None, 0.00588166, None, 0.519077, None, 0.00588166, None)

reports.append(Report(604058240, ("CSC", 2, 3, 1, 16), "MEm31_16"))
reports[-1].posNum = 172203
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00191823, 0.00185834, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0139109, 0.0526407, 0), \
                           ValErr(0.000782862, 0.00118009, 0), \
                           ValErr(-0.00170791, 0.00234422, 0), \
                           ValErr(3.36968e-05, 3.06118e-05, 0), \
                           -131026, 172203, 172203, -nan)
reports[-1].sigmaresid = ValErr(0.517857, 0.000882419, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00289528, None, 1.09388e-05, None, -0.00272881, None, -3.68232e-06, None, -0.00272881, None, -3.68232e-06, None, -0.00151558, None, 1.43916e-05, None, -0.00151558, None, 1.43916e-05, None, 0.517862, None, 0.00587613, None, 0.517862, None, 0.00587613, None)

reports.append(Report(604058256, ("CSC", 2, 3, 1, 18), "MEm31_18"))
reports[-1].posNum = 173444
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000852566, 0.00184522, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0972847, 0.0525032, 0), \
                           ValErr(-0.00111346, 0.0011725, 0), \
                           ValErr(-0.000849234, 0.00233993, 0), \
                           ValErr(-9.60775e-06, 3.03356e-05, 0), \
                           -131750, 173444, 173444, -nan)
reports[-1].sigmaresid = ValErr(0.5172, 0.00087814, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00140631, None, 9.07654e-07, None, -0.00137477, None, -2.01528e-05, None, -0.00137477, None, -2.01528e-05, None, -0.00269386, None, -2.83337e-05, None, -0.00269386, None, -2.83337e-05, None, 0.517208, None, 0.00582888, None, 0.517208, None, 0.00582888, None)

reports.append(Report(604058632, ("CSC", 2, 3, 2, 1), "MEm32_01"))
reports[-1].posNum = 59943
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00265155, 0.00709117, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.214357, 0.198364, 0), \
                           ValErr(0.00358486, 0.00226011, 0), \
                           ValErr(0.0157869, 0.0104444, 0), \
                           ValErr(4.61084e-05, 5.5345e-05, 0), \
                           -88816.8, 59943, 59943, -nan)
reports[-1].sigmaresid = ValErr(1.06476, 0.00307519, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.007002, None, -2.02942e-05, None, 0.00592527, None, -8.34702e-06, None, 0.00592527, None, -8.34702e-06, None, 0.00517664, None, -8.99305e-06, None, 0.00517664, None, -8.99305e-06, None, 1.06481, None, 0.00776526, None, 1.06481, None, 0.00776526, None)

reports.append(Report(604058648, ("CSC", 2, 3, 2, 3), "MEm32_03"))
reports[-1].posNum = 55059
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0193962, 0.0073074, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.190269, 0.200295, 0), \
                           ValErr(-0.000923961, 0.0022562, 0), \
                           ValErr(-0.0309827, 0.0106634, 0), \
                           ValErr(-0.000128996, 5.60939e-05, 0), \
                           -79205.7, 55059, 55059, -nan)
reports[-1].sigmaresid = ValErr(1.01981, 0.0030732, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00517362, None, -2.85884e-05, None, 0.000690027, None, 4.19929e-06, None, 0.000690027, None, 4.19929e-06, None, -0.00454805, None, 1.20656e-05, None, -0.00454805, None, 1.20656e-05, None, 1.01992, None, 0.00783822, None, 1.01992, None, 0.00783822, None)

reports.append(Report(604058664, ("CSC", 2, 3, 2, 5), "MEm32_05"))
reports[-1].posNum = 58888
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00523077, 0.00697104, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.394577, 0.198495, 0), \
                           ValErr(0.00383897, 0.00225368, 0), \
                           ValErr(-0.00299372, 0.0103842, 0), \
                           ValErr(6.68864e-05, 5.44803e-05, 0), \
                           -86363.4, 58888, 58888, -nan)
reports[-1].sigmaresid = ValErr(1.04878, 0.003056, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00186765, None, -1.09324e-05, None, -0.00426757, None, -1.72737e-05, None, -0.00426757, None, -1.72737e-05, None, -0.00260839, None, -1.78302e-06, None, -0.00260839, None, -1.78302e-06, None, 1.04886, None, 0.00751954, None, 1.04886, None, 0.00751954, None)

reports.append(Report(604058680, ("CSC", 2, 3, 2, 7), "MEm32_07"))
reports[-1].posNum = 54978
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00333069, 0.00745401, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.214807, 0.20276, 0), \
                           ValErr(0.00276235, 0.00229651, 0), \
                           ValErr(0.00386278, 0.0107569, 0), \
                           ValErr(6.49331e-05, 5.74982e-05, 0), \
                           -80158.9, 54978, 54978, -nan)
reports[-1].sigmaresid = ValErr(1.03985, 0.00313591, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00169583, None, -1.73933e-05, None, 0.00103951, None, -4.12834e-05, None, 0.00103951, None, -4.12834e-05, None, 0.00761875, None, -1.41127e-05, None, 0.00761875, None, -1.41127e-05, None, 1.03989, None, 0.00821891, None, 1.03989, None, 0.00821891, None)

reports.append(Report(604058696, ("CSC", 2, 3, 2, 9), "MEm32_09"))
reports[-1].posNum = 57478
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00326697, 0.00710237, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.218308, 0.202202, 0), \
                           ValErr(0.00193813, 0.00227828, 0), \
                           ValErr(0.00652588, 0.0105429, 0), \
                           ValErr(-1.72048e-05, 5.52733e-05, 0), \
                           -84185.3, 57478, 57478, -nan)
reports[-1].sigmaresid = ValErr(1.04678, 0.00308737, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000451468, None, 3.73956e-05, None, -0.00106177, None, 9.17883e-06, None, -0.00106177, None, 9.17883e-06, None, 0.000677985, None, 7.21398e-05, None, 0.000677985, None, 7.21398e-05, None, 1.0468, None, 0.00763102, None, 1.0468, None, 0.00763102, None)

reports.append(Report(604058712, ("CSC", 2, 3, 2, 11), "MEm32_11"))
reports[-1].posNum = 57374
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0016573, 0.00709432, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0729703, 0.203404, 0), \
                           ValErr(0.00334466, 0.00229702, 0), \
                           ValErr(-0.00162168, 0.0105987, 0), \
                           ValErr(3.24766e-05, 5.51155e-05, 0), \
                           -83960.6, 57374, 57374, -nan)
reports[-1].sigmaresid = ValErr(1.04545, 0.00308626, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00389149, None, 1.05154e-05, None, -0.00104387, None, -2.25977e-05, None, -0.00104387, None, -2.25977e-05, None, -0.00129875, None, -2.51835e-06, None, -0.00129875, None, -2.51835e-06, None, 1.04548, None, 0.00773232, None, 1.04548, None, 0.00773232, None)

reports.append(Report(604058728, ("CSC", 2, 3, 2, 13), "MEm32_13"))
reports[-1].posNum = 54024
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0105828, 0.00753114, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00371346, 0.205198, 0), \
                           ValErr(-0.00161067, 0.00229447, 0), \
                           ValErr(-0.00857536, 0.0109116, 0), \
                           ValErr(-4.48608e-05, 5.74433e-05, 0), \
                           -78722.5, 54024, 54024, -nan)
reports[-1].sigmaresid = ValErr(1.03897, 0.00316078, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00886316, None, -5.32226e-07, None, 0.00504371, None, 1.52461e-05, None, 0.00504371, None, 1.52461e-05, None, -0.00314684, None, 2.80257e-05, None, -0.00314684, None, 2.80257e-05, None, 1.03899, None, 0.00762268, None, 1.03899, None, 0.00762268, None)

reports.append(Report(604058744, ("CSC", 2, 3, 2, 15), "MEm32_15"))
reports[-1].posNum = 58477
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0172244, 0.00691796, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0486257, 0.199901, 0), \
                           ValErr(-0.0023562, 0.00229449, 0), \
                           ValErr(-0.00375567, 0.0103826, 0), \
                           ValErr(-6.69346e-05, 5.45227e-05, 0), \
                           -85410.9, 58477, 58477, -nan)
reports[-1].sigmaresid = ValErr(1.04253, 0.00304846, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0131002, None, 4.77905e-05, None, 0.0132617, None, -3.48778e-06, None, 0.0132617, None, -3.48778e-06, None, 0.0173403, None, 3.94014e-05, None, 0.0173403, None, 3.94014e-05, None, 1.04255, None, 0.00807573, None, 1.04255, None, 0.00807573, None)

reports.append(Report(604058760, ("CSC", 2, 3, 2, 17), "MEm32_17"))
reports[-1].posNum = 54992
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0129994, 0.00730511, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.222631, 0.202962, 0), \
                           ValErr(0.00495697, 0.00227538, 0), \
                           ValErr(-0.00423869, 0.0107557, 0), \
                           ValErr(-0.000191472, 5.62218e-05, 0), \
                           -79341.4, 54992, 54992, -nan)
reports[-1].sigmaresid = ValErr(1.02413, 0.00308809, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00761526, None, 1.37125e-05, None, 0.00341384, None, 2.93784e-06, None, 0.00341384, None, 2.93784e-06, None, 0.00755868, None, 5.24686e-05, None, 0.00755868, None, 5.24686e-05, None, 1.02429, None, 0.00732347, None, 1.02429, None, 0.00732347, None)

reports.append(Report(604058776, ("CSC", 2, 3, 2, 19), "MEm32_19"))
reports[-1].posNum = 59652
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0159417, 0.00704801, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0960839, 0.196603, 0), \
                           ValErr(0.00240168, 0.00224117, 0), \
                           ValErr(-0.0139791, 0.0103314, 0), \
                           ValErr(-0.000100134, 5.51937e-05, 0), \
                           -87810.4, 59652, 59652, -nan)
reports[-1].sigmaresid = ValErr(1.05454, 0.00305308, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00308472, None, 1.81434e-05, None, 0.00618873, None, 2.08716e-05, None, 0.00618873, None, 2.08716e-05, None, 0.00668279, None, 4.21838e-06, None, 0.00668279, None, 4.21838e-06, None, 1.05459, None, 0.00762004, None, 1.05459, None, 0.00762004, None)

reports.append(Report(604058792, ("CSC", 2, 3, 2, 21), "MEm32_21"))
reports[-1].posNum = 54209
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0116153, 0.00725313, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.136323, 0.203558, 0), \
                           ValErr(0.00548967, 0.00225811, 0), \
                           ValErr(-0.00606099, 0.0107035, 0), \
                           ValErr(-3.19554e-05, 5.54973e-05, 0), \
                           -77847.4, 54209, 54209, -nan)
reports[-1].sigmaresid = ValErr(1.01727, 0.00308949, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00758513, None, -5.97405e-06, None, 0.00783375, None, -8.30374e-05, None, 0.00783375, None, -8.30374e-05, None, 0.00532536, None, -2.53161e-05, None, 0.00532536, None, -2.53161e-05, None, 1.01733, None, 0.00928952, None, 1.01733, None, 0.00928952, None)

reports.append(Report(604058808, ("CSC", 2, 3, 2, 23), "MEm32_23"))
reports[-1].posNum = 59715
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00219059, 0.00694391, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.342629, 0.196776, 0), \
                           ValErr(-0.00292699, 0.00223716, 0), \
                           ValErr(-0.000648621, 0.0102613, 0), \
                           ValErr(-0.000100245, 5.44129e-05, 0), \
                           -87695.8, 59715, 59715, -nan)
reports[-1].sigmaresid = ValErr(1.05088, 0.00304086, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0021167, None, -1.38131e-05, None, -0.00586426, None, 7.96957e-06, None, -0.00586426, None, 7.96957e-06, None, -0.00641168, None, 1.90338e-05, None, -0.00641168, None, 1.90338e-05, None, 1.05096, None, 0.00755255, None, 1.05096, None, 0.00755255, None)

reports.append(Report(604058824, ("CSC", 2, 3, 2, 25), "MEm32_25"))
reports[-1].posNum = 55790
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00122016, 0.00727248, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.145744, 0.201059, 0), \
                           ValErr(-0.000416818, 0.0022708, 0), \
                           ValErr(0.00642291, 0.0106044, 0), \
                           ValErr(-4.81666e-05, 5.62019e-05, 0), \
                           -80856.8, 55790, 55790, -nan)
reports[-1].sigmaresid = ValErr(1.03083, 0.003086, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00218293, None, 1.71689e-05, None, -0.000329538, None, -2.30783e-05, None, -0.000329538, None, -2.30783e-05, None, 0.000178755, None, 2.56056e-05, None, 0.000178755, None, 2.56056e-05, None, 1.03085, None, 0.00737583, None, 1.03085, None, 0.00737583, None)

reports.append(Report(604058840, ("CSC", 2, 3, 2, 27), "MEm32_27"))
reports[-1].posNum = 56949
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00111785, 0.00717346, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.292535, 0.20255, 0), \
                           ValErr(-0.000940552, 0.00227682, 0), \
                           ValErr(-0.000747964, 0.0106145, 0), \
                           ValErr(-7.59292e-06, 5.56031e-05, 0), \
                           -83606, 56949, 56949, -nan)
reports[-1].sigmaresid = ValErr(1.05037, 0.00311233, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00522459, None, -2.39183e-06, None, 0.000398584, None, -2.21751e-05, None, 0.000398584, None, -2.21751e-05, None, 0.00466417, None, -3.98423e-06, None, 0.00466417, None, -3.98423e-06, None, 1.0504, None, 0.00799696, None, 1.0504, None, 0.00799696, None)

reports.append(Report(604058856, ("CSC", 2, 3, 2, 29), "MEm32_29"))
reports[-1].posNum = 57129
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0094658, 0.00713514, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0450184, 0.17348, 0), \
                           ValErr(-0.000411697, 0.00169998, 0), \
                           ValErr(0.00522354, 0.0105336, 0), \
                           ValErr(0.000121041, 5.53535e-05, 0), \
                           -83507.2, 57129, 57129, -nan)
reports[-1].sigmaresid = ValErr(1.04372, 0.00308249, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00508322, None, -3.1779e-05, None, -0.00276701, None, -3.64806e-05, None, -0.00276701, None, -3.64806e-05, None, -0.00565482, None, -6.20889e-05, None, -0.00565482, None, -6.20889e-05, None, 1.04377, None, 0.00740958, None, 1.04377, None, 0.00740958, None)

reports.append(Report(604058872, ("CSC", 2, 3, 2, 31), "MEm32_31"))
reports[-1].posNum = 56007
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00379502, 0.00747164, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.197168, 0.201497, 0), \
                           ValErr(0.000977691, 0.00227956, 0), \
                           ValErr(0.00070402, 0.0107954, 0), \
                           ValErr(-2.25556e-05, 5.72785e-05, 0), \
                           -81823.5, 56007, 56007, -nan)
reports[-1].sigmaresid = ValErr(1.04291, 0.00311609, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00460696, None, -2.21655e-05, None, 0.00310721, None, -5.25267e-05, None, 0.00310721, None, -5.25267e-05, None, -0.00103508, None, -4.08122e-05, None, -0.00103508, None, -4.08122e-05, None, 1.04292, None, 0.00760998, None, 1.04292, None, 0.00760998, None)

reports.append(Report(604058888, ("CSC", 2, 3, 2, 33), "MEm32_33"))
reports[-1].posNum = 59433
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0061602, 0.00690351, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.380247, 0.196751, 0), \
                           ValErr(-0.000502815, 0.00223247, 0), \
                           ValErr(0.00934923, 0.0102283, 0), \
                           ValErr(-3.22771e-05, 5.40905e-05, 0), \
                           -87071.1, 59433, 59433, -nan)
reports[-1].sigmaresid = ValErr(1.04717, 0.0030373, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0143882, None, 1.34838e-05, None, 0.0090567, None, -1.01395e-05, None, 0.0090567, None, -1.01395e-05, None, 0.0112837, None, -1.24205e-05, None, 0.0112837, None, -1.24205e-05, None, 1.04722, None, 0.00773434, None, 1.04722, None, 0.00773434, None)

reports.append(Report(604058904, ("CSC", 2, 3, 2, 35), "MEm32_35"))
reports[-1].posNum = 54163
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.030562, 0.0074394, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0951037, 0.203954, 0), \
                           ValErr(-0.000651698, 0.00227523, 0), \
                           ValErr(-0.0295429, 0.0108846, 0), \
                           ValErr(-0.000133863, 5.6197e-05, 0), \
                           -78191.7, 54163, 54163, -nan)
reports[-1].sigmaresid = ValErr(1.02501, 0.00311429, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0151635, None, 4.98326e-05, None, 0.0121404, None, 2.9695e-05, None, 0.0121404, None, 2.9695e-05, None, 0.0199811, None, 3.86567e-05, None, 0.0199811, None, 3.86567e-05, None, 1.0251, None, 0.00760014, None, 1.0251, None, 0.00760014, None)

reports.append(Report(604058640, ("CSC", 2, 3, 2, 2), "MEm32_02"))
reports[-1].posNum = 59023
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0110044, 0.00711979, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.144353, 0.0997613, 0), \
                           ValErr(0.00154844, 0.00116629, 0), \
                           ValErr(-0.0175416, 0.0108211, 0), \
                           ValErr(-0.000108983, 5.52734e-05, 0), \
                           -87381.2, 59023, 59023, -nan)
reports[-1].sigmaresid = ValErr(1.06345, 0.00305567, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00317115, None, -3.77231e-05, None, -0.000440874, None, -3.37093e-05, None, -0.000440874, None, -3.37093e-05, None, 0.00357667, None, -2.22314e-05, None, 0.00357667, None, -2.22314e-05, None, 1.06351, None, 0.00726926, None, 1.06351, None, 0.00726926, None)

reports.append(Report(604058656, ("CSC", 2, 3, 2, 4), "MEm32_04"))
reports[-1].posNum = 57433
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00341726, 0.00723399, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.260251, 0.20854, 0), \
                           ValErr(-0.000480908, 0.00236229, 0), \
                           ValErr(0.00431843, 0.0109998, 0), \
                           ValErr(-1.39745e-05, 5.60508e-05, 0), \
                           -84086, 57433, 57433, -nan)
reports[-1].sigmaresid = ValErr(1.04616, 0.00308674, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00299164, None, 2.49188e-05, None, -0.00207077, None, 2.22789e-05, None, -0.00207077, None, 2.22789e-05, None, -0.00190959, None, 2.17382e-05, None, -0.00190959, None, 2.17382e-05, None, 1.04618, None, 0.0069876, None, 1.04618, None, 0.0069876, None)

reports.append(Report(604058672, ("CSC", 2, 3, 2, 6), "MEm32_06"))
reports[-1].posNum = 61621
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0119642, 0.00695237, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.311553, 0.203866, 0), \
                           ValErr(-0.000578378, 0.00232109, 0), \
                           ValErr(0.0237807, 0.0106517, 0), \
                           ValErr(-2.05561e-05, 5.46127e-05, 0), \
                           -91797.3, 61621, 61621, -nan)
reports[-1].sigmaresid = ValErr(1.07334, 0.00305743, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00779658, None, 6.4568e-06, None, -0.00253915, None, 4.22359e-05, None, -0.00253915, None, 4.22359e-05, None, -0.00148205, None, 2.32028e-05, None, -0.00148205, None, 2.32028e-05, None, 1.07341, None, 0.00743872, None, 1.07341, None, 0.00743872, None)

reports.append(Report(604058688, ("CSC", 2, 3, 2, 8), "MEm32_08"))
reports[-1].posNum = 55660
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00500548, 0.00735098, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.23856, 0.208159, 0), \
                           ValErr(0.00546521, 0.0023622, 0), \
                           ValErr(0.0212797, 0.0110836, 0), \
                           ValErr(1.36621e-05, 5.67228e-05, 0), \
                           -80596.3, 55660, 55660, -nan)
reports[-1].sigmaresid = ValErr(1.0295, 0.0030856, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00324319, None, 1.58652e-05, None, 0.00443494, None, 2.3451e-05, None, 0.00443494, None, 2.3451e-05, None, -0.00607175, None, 7.12046e-07, None, -0.00607175, None, 7.12046e-07, None, 1.02959, None, 0.00678107, None, 1.02959, None, 0.00678107, None)

reports.append(Report(604058704, ("CSC", 2, 3, 2, 10), "MEm32_10"))
reports[-1].posNum = 62338
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000894473, 0.00683071, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00216028, 0.11042, 0), \
                           ValErr(0.00104134, 0.00142171, 0), \
                           ValErr(-0.0140885, 0.0105454, 0), \
                           ValErr(3.76185e-05, 5.09629e-05, 0), \
                           -93227.4, 62338, 62338, -nan)
reports[-1].sigmaresid = ValErr(1.07959, 0.00305367, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.002809, None, 6.33705e-06, None, -0.00581279, None, -5.1568e-05, None, -0.00581279, None, -5.1568e-05, None, 2.83052e-05, None, -2.95998e-05, None, 2.83052e-05, None, -2.95998e-05, None, 1.07962, None, 0.00729127, None, 1.07962, None, 0.00729127, None)

reports.append(Report(604058720, ("CSC", 2, 3, 2, 12), "MEm32_12"))
reports[-1].posNum = 57088
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00786403, 0.00719828, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.307779, 0.172036, 0), \
                           ValErr(0.0040234, 0.00194609, 0), \
                           ValErr(0.0057342, 0.0109328, 0), \
                           ValErr(-1.68659e-05, 5.58887e-05, 0), \
                           -83217.2, 57088, 57088, -nan)
reports[-1].sigmaresid = ValErr(1.03952, 0.00307003, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00308969, None, 2.67055e-05, None, -0.00585807, None, -1.06985e-05, None, -0.00585807, None, -1.06985e-05, None, -0.00971906, None, -3.82399e-05, None, -0.00971906, None, -3.82399e-05, None, 1.03957, None, 0.00742788, None, 1.03957, None, 0.00742788, None)

reports.append(Report(604058736, ("CSC", 2, 3, 2, 14), "MEm32_14"))
reports[-1].posNum = 60925
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0134428, 0.00693775, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.280685, 0.200983, 0), \
                           ValErr(0.00200913, 0.00228458, 0), \
                           ValErr(0.0122887, 0.0105297, 0), \
                           ValErr(9.68497e-05, 5.41736e-05, 0), \
                           -89839.2, 60925, 60925, -nan)
reports[-1].sigmaresid = ValErr(1.05723, 0.00302871, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000875877, None, 2.62066e-05, None, -0.00481976, None, -1.33952e-05, None, -0.00481976, None, -1.33952e-05, None, -0.00375539, None, 4.1954e-05, None, -0.00375539, None, 4.1954e-05, None, 1.05728, None, 0.00725108, None, 1.05728, None, 0.00725108, None)

reports.append(Report(604058752, ("CSC", 2, 3, 2, 16), "MEm32_16"))
reports[-1].posNum = 57338
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00838138, 0.00721085, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.142255, 0.209164, 0), \
                           ValErr(0.00183364, 0.00235737, 0), \
                           ValErr(-0.00142447, 0.0109733, 0), \
                           ValErr(-8.47675e-05, 5.59116e-05, 0), \
                           -84008.4, 57338, 57338, -nan)
reports[-1].sigmaresid = ValErr(1.04728, 0.00309261, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00327241, None, 5.73001e-05, None, 0.00454923, None, 3.22298e-05, None, 0.00454923, None, 3.22298e-05, None, 0.00933577, None, 4.43347e-05, None, 0.00933577, None, 4.43347e-05, None, 1.04732, None, 0.0071643, None, 1.04732, None, 0.0071643, None)

reports.append(Report(604058768, ("CSC", 2, 3, 2, 18), "MEm32_18"))
reports[-1].posNum = 58519
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0216903, 0.00711149, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0517097, 0.107871, 0), \
                           ValErr(0.000296279, 0.00128425, 0), \
                           ValErr(0.0129389, 0.0106798, 0), \
                           ValErr(8.00322e-05, 5.32996e-05, 0), \
                           -86049.8, 58519, 58519, -nan)
reports[-1].sigmaresid = ValErr(1.05287, 0.00307593, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00904487, None, -3.03539e-05, None, -0.0132677, None, -4.18581e-05, None, -0.0132677, None, -4.18581e-05, None, -0.0166292, None, -4.08456e-05, None, -0.0166292, None, -4.08456e-05, None, 1.0529, None, 0.00763696, None, 1.0529, None, 0.00763696, None)

reports.append(Report(604058784, ("CSC", 2, 3, 2, 20), "MEm32_20"))
reports[-1].posNum = 60213
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00931792, 0.00709002, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.36343, 0.141419, 0), \
                           ValErr(-0.00454658, 0.00224863, 0), \
                           ValErr(0.0126473, 0.0106204, 0), \
                           ValErr(-1.93278e-05, 5.34364e-05, 0), \
                           -89024, 60213, 60213, -nan)
reports[-1].sigmaresid = ValErr(1.06136, 0.00295699, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00572828, None, -1.76247e-05, None, -0.00462385, None, 2.50303e-05, None, -0.00462385, None, 2.50303e-05, None, -0.00729648, None, -2.87461e-06, None, -0.00729648, None, -2.87461e-06, None, 1.06144, None, 0.00760001, None, 1.06144, None, 0.00760001, None)

reports.append(Report(604058800, ("CSC", 2, 3, 2, 22), "MEm32_22"))
reports[-1].posNum = 56950
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0150155, 0.00731291, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0951441, 0.20014, 0), \
                           ValErr(0.000275519, 0.00160244, 0), \
                           ValErr(-0.014414, 0.0110704, 0), \
                           ValErr(-0.000133848, 5.67991e-05, 0), \
                           -83639.3, 56950, 56950, -nan)
reports[-1].sigmaresid = ValErr(1.05096, 0.00310764, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00277735, None, 2.38011e-05, None, 0.00362684, None, 5.92697e-06, None, 0.00362684, None, 5.92697e-06, None, 0.00107926, None, -7.81076e-06, None, 0.00107926, None, -7.81076e-06, None, 1.05102, None, 0.00769348, None, 1.05102, None, 0.00769348, None)

reports.append(Report(604058816, ("CSC", 2, 3, 2, 24), "MEm32_24"))
reports[-1].posNum = 61167
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00653633, 0.00695903, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.134343, 0.200797, 0), \
                           ValErr(0.000352161, 0.00229205, 0), \
                           ValErr(0.0259476, 0.0105162, 0), \
                           ValErr(-1.63948e-05, 5.45462e-05, 0), \
                           -90297, 61167, 61167, -nan)
reports[-1].sigmaresid = ValErr(1.05897, 0.00302769, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00168523, None, -1.99021e-05, None, 0.00402502, None, 1.33557e-05, None, 0.00402502, None, 1.33557e-05, None, 0.0068319, None, 1.03634e-05, None, 0.0068319, None, 1.03634e-05, None, 1.05904, None, 0.00723937, None, 1.05904, None, 0.00723937, None)

reports.append(Report(604058832, ("CSC", 2, 3, 2, 26), "MEm32_26"))
reports[-1].posNum = 56819
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00250342, 0.0073334, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.202248, 0.207496, 0), \
                           ValErr(-0.00180917, 0.00235119, 0), \
                           ValErr(0.00603825, 0.0110742, 0), \
                           ValErr(-5.62688e-05, 5.65507e-05, 0), \
                           -82657.4, 56819, 56819, -nan)
reports[-1].sigmaresid = ValErr(1.03646, 0.00307462, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00268141, None, 2.72874e-05, None, 0.0027987, None, 4.76155e-05, None, 0.0027987, None, 4.76155e-05, None, 0.000358629, None, 4.18649e-05, None, 0.000358629, None, 4.18649e-05, None, 1.03649, None, 0.00706601, None, 1.03649, None, 0.00706601, None)

reports.append(Report(604058848, ("CSC", 2, 3, 2, 28), "MEm32_28"))
reports[-1].posNum = 62172
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00548665, 0.00702157, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0318769, 0.119092, 0), \
                           ValErr(0.000261559, 0.00144774, 0), \
                           ValErr(0.00190234, 0.0105028, 0), \
                           ValErr(2.33431e-05, 4.98855e-05, 0), \
                           -93064.3, 62172, 62172, -nan)
reports[-1].sigmaresid = ValErr(1.08107, 0.00306678, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00100414, None, -2.30516e-05, None, -0.00388782, None, -2.73731e-05, None, -0.00388782, None, -2.73731e-05, None, 0.00164393, None, -5.4767e-06, None, 0.00164393, None, -5.4767e-06, None, 1.08107, None, 0.00740273, None, 1.08107, None, 0.00740273, None)

reports.append(Report(604058864, ("CSC", 2, 3, 2, 30), "MEm32_30"))
reports[-1].posNum = 56186
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00338194, 0.00727629, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0845185, 0.208577, 0), \
                           ValErr(-0.000145166, 0.00234228, 0), \
                           ValErr(-0.0120557, 0.0110157, 0), \
                           ValErr(-2.73261e-05, 5.60088e-05, 0), \
                           -81519.3, 56186, 56186, -nan)
reports[-1].sigmaresid = ValErr(1.03246, 0.00307996, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00524875, None, 5.52576e-07, None, -0.00953263, None, -2.06176e-05, None, -0.00953263, None, -2.06176e-05, None, -0.00393369, None, -1.74918e-05, None, -0.00393369, None, -1.74918e-05, None, 1.03247, None, 0.00746977, None, 1.03247, None, 0.00746977, None)

reports.append(Report(604058880, ("CSC", 2, 3, 2, 32), "MEm32_32"))
reports[-1].posNum = 61591
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00855587, 0.00693395, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.302527, 0.20167, 0), \
                           ValErr(-0.00179521, 0.00229018, 0), \
                           ValErr(-0.00700566, 0.0105209, 0), \
                           ValErr(-1.02257e-05, 5.45233e-05, 0), \
                           -91272.1, 61591, 61591, -nan)
reports[-1].sigmaresid = ValErr(1.065, 0.00303443, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00500075, None, 1.7824e-05, None, 0.0052266, None, 2.2892e-05, None, 0.0052266, None, 2.2892e-05, None, 0.00570768, None, 2.68633e-05, None, 0.00570768, None, 2.68633e-05, None, 1.06502, None, 0.00750895, None, 1.06502, None, 0.00750895, None)

reports.append(Report(604058896, ("CSC", 2, 3, 2, 34), "MEm32_34"))
reports[-1].posNum = 58372
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00786721, 0.00718715, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0843903, 0.209666, 0), \
                           ValErr(0.00412147, 0.00240071, 0), \
                           ValErr(0.00323144, 0.0110024, 0), \
                           ValErr(2.92639e-05, 5.63897e-05, 0), \
                           -85906.6, 58372, 58372, -nan)
reports[-1].sigmaresid = ValErr(1.05419, 0.00308532, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00090976, None, -1.17558e-05, None, -0.00534265, None, -5.05989e-05, None, -0.00534265, None, -5.05989e-05, None, -0.0113369, None, -6.95826e-05, None, -0.0113369, None, -6.95826e-05, None, 1.05422, None, 0.00759279, None, 1.05422, None, 0.00759279, None)

reports.append(Report(604058912, ("CSC", 2, 3, 2, 36), "MEm32_36"))
reports[-1].posNum = 60106
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00794926, 0.00703442, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.264768, 0.204187, 0), \
                           ValErr(0.00148277, 0.00232477, 0), \
                           ValErr(-0.00231091, 0.0107303, 0), \
                           ValErr(4.64551e-05, 5.49341e-05, 0), \
                           -88832.3, 60106, 60106, -nan)
reports[-1].sigmaresid = ValErr(1.06076, 0.00305944, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00418873, None, 2.59438e-05, None, 0.00856758, None, -1.22597e-05, None, 0.00856758, None, -1.22597e-05, None, 0.00937373, None, 5.5387e-05, None, 0.00937373, None, 5.5387e-05, None, 1.06079, None, 0.00728672, None, 1.06079, None, 0.00728672, None)

reports.append(Report(604062216, ("CSC", 2, 4, 1, 1), "MEm41_01"))
reports[-1].posNum = 136882
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0033187, 0.00235661, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0109194, 0.0683648, 0), \
                           ValErr(0.00285497, 0.0017471, 0), \
                           ValErr(-0.00488707, 0.00297594, 0), \
                           ValErr(3.23406e-05, 4.35414e-05, 0), \
                           -121381, 136882, 136882, -nan)
reports[-1].sigmaresid = ValErr(0.587322, 0.0011225, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000524751, None, -1.07216e-05, None, 0.000565811, None, -4.44595e-05, None, 0.000565811, None, -4.44595e-05, None, 0.00315118, None, -6.0458e-05, None, 0.00315118, None, -6.0458e-05, None, 0.587339, None, 0.00571604, None, 0.587339, None, 0.00571604, None)

reports.append(Report(604062232, ("CSC", 2, 4, 1, 3), "MEm41_03"))
reports[-1].posNum = 137832
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00106787, 0.00234303, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0745273, 0.0678772, 0), \
                           ValErr(-0.000426137, 0.00173349, 0), \
                           ValErr(0.00265685, 0.00295344, 0), \
                           ValErr(4.71172e-05, 4.33106e-05, 0), \
                           -121751, 137832, 137832, -nan)
reports[-1].sigmaresid = ValErr(0.58531, 0.0011148, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00330344, None, -8.9193e-06, None, 0.0026962, None, -2.12271e-05, None, 0.0026962, None, -2.12271e-05, None, -0.0019871, None, -6.49187e-05, None, -0.0019871, None, -6.49187e-05, None, 0.585316, None, 0.00575639, None, 0.585316, None, 0.00575639, None)

reports.append(Report(604062248, ("CSC", 2, 4, 1, 5), "MEm41_05"))
reports[-1].posNum = 137237
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000272987, 0.00234458, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.145564, 0.0682142, 0), \
                           ValErr(-0.00178354, 0.00174899, 0), \
                           ValErr(0.000302293, 0.00297418, 0), \
                           ValErr(-2.84368e-06, 4.35343e-05, 0), \
                           -121284, 137237, 137237, -nan)
reports[-1].sigmaresid = ValErr(0.585561, 0.00111769, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00239524, None, 2.75342e-06, None, -0.000107797, None, -4.49246e-05, None, -0.000107797, None, -4.49246e-05, None, -0.0055234, None, -5.42614e-05, None, -0.0055234, None, -5.42614e-05, None, 0.585571, None, 0.0058753, None, 0.585571, None, 0.0058753, None)

reports.append(Report(604062264, ("CSC", 2, 4, 1, 7), "MEm41_07"))
reports[-1].posNum = 136089
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00598761, 0.00235064, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00563668, 0.0679746, 0), \
                           ValErr(0.000350886, 0.00173498, 0), \
                           ValErr(-0.00562122, 0.00297196, 0), \
                           ValErr(-8.3521e-05, 4.34366e-05, 0), \
                           -119539, 136089, 136089, -nan)
reports[-1].sigmaresid = ValErr(0.582429, 0.00111639, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00251313, None, -7.28728e-06, None, 0.00255644, None, -3.63259e-06, None, 0.00255644, None, -3.63259e-06, None, 0.000901346, None, 1.97929e-05, None, 0.000901346, None, 1.97929e-05, None, 0.582441, None, 0.00578701, None, 0.582441, None, 0.00578701, None)

reports.append(Report(604062280, ("CSC", 2, 4, 1, 9), "MEm41_09"))
reports[-1].posNum = 137059
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00190596, 0.0023392, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0313943, 0.0680543, 0), \
                           ValErr(5.451e-05, 0.00173615, 0), \
                           ValErr(-0.00118352, 0.00296542, 0), \
                           ValErr(3.699e-05, 4.32767e-05, 0), \
                           -120614, 137059, 137059, -nan)
reports[-1].sigmaresid = ValErr(0.583376, 0.00111424, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00310216, None, 5.83909e-06, None, 0.00130852, None, -5.88399e-06, None, 0.00130852, None, -5.88399e-06, None, -0.00397366, None, -1.27378e-05, None, -0.00397366, None, -1.27378e-05, None, 0.58338, None, 0.00575792, None, 0.58338, None, 0.00575792, None)

reports.append(Report(604062296, ("CSC", 2, 4, 1, 11), "MEm41_11"))
reports[-1].posNum = 136780
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00722402, 0.00234233, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0370803, 0.0682094, 0), \
                           ValErr(-0.00100486, 0.00174248, 0), \
                           ValErr(0.00523745, 0.00297042, 0), \
                           ValErr(5.60371e-05, 4.33687e-05, 0), \
                           -120508, 136780, 136780, -nan)
reports[-1].sigmaresid = ValErr(0.583974, 0.00111652, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00575865, None, -1.25625e-05, None, -0.00410856, None, -3.47997e-05, None, -0.00410856, None, -3.47997e-05, None, -0.00262189, None, -1.33946e-05, None, -0.00262189, None, -1.33946e-05, None, 0.583982, None, 0.00568234, None, 0.583982, None, 0.00568234, None)

reports.append(Report(604062312, ("CSC", 2, 4, 1, 13), "MEm41_13"))
reports[-1].posNum = 138409
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00142085, 0.00232816, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0435752, 0.0673966, 0), \
                           ValErr(-0.000672252, 0.00172604, 0), \
                           ValErr(-0.00411328, 0.00293874, 0), \
                           ValErr(-3.29878e-06, 4.30505e-05, 0), \
                           -121644, 138409, 138409, -nan)
reports[-1].sigmaresid = ValErr(0.582711, 0.00110753, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000460415, None, 5.48923e-06, None, -0.000953583, None, -2.41563e-05, None, -0.000953583, None, -2.41563e-05, None, 0.000709411, None, -9.23174e-06, None, 0.000709411, None, -9.23174e-06, None, 0.582717, None, 0.0060263, None, 0.582717, None, 0.0060263, None)

reports.append(Report(604062328, ("CSC", 2, 4, 1, 15), "MEm41_15"))
reports[-1].posNum = 138316
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(9.66714e-05, 0.0023326, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.016709, 0.0676, 0), \
                           ValErr(-0.00157979, 0.00173003, 0), \
                           ValErr(-0.000384519, 0.00294993, 0), \
                           ValErr(5.94816e-05, 4.31443e-05, 0), \
                           -121826, 138316, 138316, -nan)
reports[-1].sigmaresid = ValErr(0.58382, 0.00111001, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000466855, None, -9.37771e-07, None, 6.05168e-06, None, -2.3607e-05, None, 6.05168e-06, None, -2.3607e-05, None, -0.00327693, None, -5.3075e-05, None, -0.00327693, None, -5.3075e-05, None, 0.583828, None, 0.00558812, None, 0.583828, None, 0.00558812, None)

reports.append(Report(604062344, ("CSC", 2, 4, 1, 17), "MEm41_17"))
reports[-1].posNum = 137061
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00286379, 0.00233527, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0907457, 0.0679229, 0), \
                           ValErr(0.00236464, 0.00173709, 0), \
                           ValErr(0.00518002, 0.0029673, 0), \
                           ValErr(4.6909e-05, 4.31651e-05, 0), \
                           -120369, 137061, 137061, -nan)
reports[-1].sigmaresid = ValErr(0.582327, 0.00111223, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0012134, None, -5.46542e-06, None, 0.000213233, None, -3.02852e-05, None, 0.000213233, None, -3.02852e-05, None, -0.000437631, None, -2.25956e-05, None, -0.000437631, None, -2.25956e-05, None, 0.582345, None, 0.00555232, None, 0.582345, None, 0.00555232, None)

reports.append(Report(604062224, ("CSC", 2, 4, 1, 2), "MEm41_02"))
reports[-1].posNum = 138315
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00329907, 0.00239465, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.120193, 0.0709746, 0), \
                           ValErr(-9.15625e-05, 0.00182507, 0), \
                           ValErr(-0.00132155, 0.00309943, 0), \
                           ValErr(4.77567e-05, 4.43877e-05, 0), \
                           -125280, 138315, 138315, -nan)
reports[-1].sigmaresid = ValErr(0.598591, 0.0011381, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00299015, None, -1.9001e-05, None, -0.00392884, None, -1.84449e-05, None, -0.00392884, None, -1.84449e-05, None, -0.00809072, None, -7.92952e-06, None, -0.00809072, None, -7.92952e-06, None, 0.598601, None, 0.00558827, None, 0.598601, None, 0.00558827, None)

reports.append(Report(604062240, ("CSC", 2, 4, 1, 4), "MEm41_04"))
reports[-1].posNum = 137661
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000208151, 0.00239298, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.102541, 0.0708767, 0), \
                           ValErr(-0.000694093, 0.00181537, 0), \
                           ValErr(-0.000259734, 0.00309108, 0), \
                           ValErr(-3.29417e-05, 4.42897e-05, 0), \
                           -124259, 137661, 137661, -nan)
reports[-1].sigmaresid = ValErr(0.596727, 0.00113725, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0011052, None, -2.13398e-05, None, -3.84017e-05, None, -2.22333e-05, None, -3.84017e-05, None, -2.22333e-05, None, -0.00468459, None, -4.78953e-05, None, -0.00468459, None, -4.78953e-05, None, 0.596732, None, 0.00561792, None, 0.596732, None, 0.00561792, None)

reports.append(Report(604062256, ("CSC", 2, 4, 1, 6), "MEm41_06"))
reports[-1].posNum = 137986
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000166486, 0.00240639, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0684263, 0.0713457, 0), \
                           ValErr(-0.00218073, 0.00182528, 0), \
                           ValErr(0.00255108, 0.00311437, 0), \
                           ValErr(-1.16154e-05, 4.44982e-05, 0), \
                           -125584, 137986, 137986, -nan)
reports[-1].sigmaresid = ValErr(0.601205, 0.00114443, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00179703, None, -1.62623e-05, None, 0.0012258, None, -2.29869e-05, None, 0.0012258, None, -2.29869e-05, None, 0.00311182, None, -1.32037e-05, None, 0.00311182, None, -1.32037e-05, None, 0.601214, None, 0.00559726, None, 0.601214, None, 0.00559726, None)

reports.append(Report(604062272, ("CSC", 2, 4, 1, 8), "MEm41_08"))
reports[-1].posNum = 138996
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(8.91905e-05, 0.00239613, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0406712, 0.0712944, 0), \
                           ValErr(-0.000909143, 0.00182729, 0), \
                           ValErr(8.72564e-05, 0.00310971, 0), \
                           ValErr(6.48723e-05, 4.43963e-05, 0), \
                           -126573, 138996, 138996, -nan)
reports[-1].sigmaresid = ValErr(0.601509, 0.00114084, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00203656, None, -7.38995e-06, None, 0.000296516, None, -1.12624e-05, None, 0.000296516, None, -1.12624e-05, None, -0.00105248, None, -1.86169e-05, None, -0.00105248, None, -1.86169e-05, None, 0.601516, None, 0.00562163, None, 0.601516, None, 0.00562163, None)

reports.append(Report(604062288, ("CSC", 2, 4, 1, 10), "MEm41_10"))
reports[-1].posNum = 138320
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00434821, 0.00241528, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0288602, 0.0598508, 0), \
                           ValErr(-0.000501828, 0.00156824, 0), \
                           ValErr(-0.00254825, 0.00312778, 0), \
                           ValErr(-4.26985e-06, 3.87316e-05, 0), \
                           -126947, 138320, 138320, -nan)
reports[-1].sigmaresid = ValErr(0.605827, 0.0011461, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00308586, None, 2.13276e-05, None, 0.00290194, None, 1.85144e-06, None, 0.00290194, None, 1.85144e-06, None, 0.0023192, None, -4.4655e-06, None, 0.0023192, None, -4.4655e-06, None, 0.605829, None, 0.00570147, None, 0.605829, None, 0.00570147, None)

reports.append(Report(604062304, ("CSC", 2, 4, 1, 12), "MEm41_12"))
reports[-1].posNum = 138514
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00416703, 0.00240471, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0376566, 0.0713835, 0), \
                           ValErr(-0.000268331, 0.00182955, 0), \
                           ValErr(-0.00459162, 0.00310875, 0), \
                           ValErr(-3.36146e-06, 4.44935e-05, 0), \
                           -126447, 138514, 138514, -nan)
reports[-1].sigmaresid = ValErr(0.60287, 0.00114541, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00175064, None, 1.34213e-05, None, 0.00158112, None, -1.01507e-05, None, 0.00158112, None, -1.01507e-05, None, 0.00307082, None, -5.15555e-06, None, 0.00307082, None, -5.15555e-06, None, 0.602876, None, 0.00568033, None, 0.602876, None, 0.00568033, None)

reports.append(Report(604062320, ("CSC", 2, 4, 1, 14), "MEm41_14"))
reports[-1].posNum = 138488
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0010121, 0.00240323, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0894587, 0.0712467, 0), \
                           ValErr(-0.00110062, 0.00182616, 0), \
                           ValErr(0.00148005, 0.00311004, 0), \
                           ValErr(2.49271e-05, 4.45159e-05, 0), \
                           -126205, 138488, 138488, -nan)
reports[-1].sigmaresid = ValErr(0.60192, 0.00114372, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00186882, None, -1.66917e-06, None, 0.00189921, None, -2.14798e-05, None, 0.00189921, None, -2.14798e-05, None, 9.77812e-05, None, -3.48719e-05, None, 9.77812e-05, None, -3.48719e-05, None, 0.601923, None, 0.00555679, None, 0.601923, None, 0.00555679, None)

reports.append(Report(604062336, ("CSC", 2, 4, 1, 16), "MEm41_16"))
reports[-1].posNum = 138003
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00104953, 0.00239936, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.079639, 0.0713419, 0), \
                           ValErr(-0.000370817, 0.00182377, 0), \
                           ValErr(-0.00158942, 0.00309885, 0), \
                           ValErr(3.12037e-05, 4.45725e-05, 0), \
                           -125371, 138003, 138003, -nan)
reports[-1].sigmaresid = ValErr(0.600214, 0.00114247, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0027855, None, 8.17371e-06, None, -0.00186926, None, 1.9759e-05, None, -0.00186926, None, 1.9759e-05, None, -0.00313669, None, 2.18893e-05, None, -0.00313669, None, 2.18893e-05, None, 0.600219, None, 0.00560605, None, 0.600219, None, 0.00560605, None)

reports.append(Report(604062352, ("CSC", 2, 4, 1, 18), "MEm41_18"))
reports[-1].posNum = 139370
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00391239, 0.00238765, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0490252, 0.0709636, 0), \
                           ValErr(-0.000255499, 0.00181325, 0), \
                           ValErr(0.000229718, 0.00309489, 0), \
                           ValErr(1.45932e-05, 4.41505e-05, 0), \
                           -126648, 139370, 139370, -nan)
reports[-1].sigmaresid = ValErr(0.60036, 0.00113713, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00247379, None, -8.99265e-06, None, -0.00375295, None, -1.95762e-05, None, -0.00375295, None, -1.95762e-05, None, -0.00272544, None, 2.44941e-06, None, -0.00272544, None, 2.44941e-06, None, 0.600363, None, 0.00549871, None, 0.600363, None, 0.00549871, None)

reports.append(Report(604062728, ("CSC", 2, 4, 2, 1), "MEm42_01"))
reports[-1].posNum = 63267
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0018243, 0.00718214, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.353446, 0.222128, 0), \
                           ValErr(-0.00211226, 0.00258757, 0), \
                           ValErr(0.0059352, 0.0117034, 0), \
                           ValErr(-1.51311e-05, 5.70152e-05, 0), \
                           -96637.4, 63267, 63267, -nan)
reports[-1].sigmaresid = ValErr(1.11463, 0.00313349, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000754452, None, -2.82001e-05, None, 5.54014e-05, None, -5.26464e-05, None, 5.54014e-05, None, -5.26464e-05, None, 0.00703275, None, -5.41572e-05, None, 0.00703275, None, -5.41572e-05, None, 1.11466, None, 0.00762165, None, 1.11466, None, 0.00762165, None)

reports.append(Report(604062744, ("CSC", 2, 4, 2, 3), "MEm42_03"))
reports[-1].posNum = 59573
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00404926, 0.00735045, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.352332, 0.223514, 0), \
                           ValErr(-0.00391476, 0.00258822, 0), \
                           ValErr(-0.000420903, 0.0118631, 0), \
                           ValErr(6.80872e-05, 5.78529e-05, 0), \
                           -88969.5, 59573, 59573, -nan)
reports[-1].sigmaresid = ValErr(1.07736, 0.00312121, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00187258, None, -7.99309e-05, None, -0.0016602, None, -7.40934e-05, None, -0.0016602, None, -7.40934e-05, None, 0.00157443, None, -6.14294e-05, None, 0.00157443, None, -6.14294e-05, None, 1.07742, None, 0.00757484, None, 1.07742, None, 0.00757484, None)

reports.append(Report(604062760, ("CSC", 2, 4, 2, 5), "MEm42_05"))
reports[-1].posNum = 62470
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00470635, 0.00708062, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.368524, 0.221304, 0), \
                           ValErr(0.00155465, 0.00257532, 0), \
                           ValErr(-0.00393731, 0.0115431, 0), \
                           ValErr(6.96731e-05, 5.64424e-05, 0), \
                           -94615.9, 62470, 62470, -nan)
reports[-1].sigmaresid = ValErr(1.10036, 0.00311305, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0132113, None, 5.97317e-06, None, 0.00539316, None, -4.06238e-05, None, 0.00539316, None, -4.06238e-05, None, 0.00481435, None, -1.02491e-05, None, 0.00481435, None, -1.02491e-05, None, 1.10041, None, 0.0079403, None, 1.10041, None, 0.0079403, None)

reports.append(Report(604062776, ("CSC", 2, 4, 2, 7), "MEm42_07"))
reports[-1].posNum = 59157
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00838675, 0.00746472, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.367327, 0.226332, 0), \
                           ValErr(0.00221468, 0.00261615, 0), \
                           ValErr(-0.0202588, 0.0119878, 0), \
                           ValErr(3.72791e-05, 5.87634e-05, 0), \
                           -89230.2, 59157, 59157, -nan)
reports[-1].sigmaresid = ValErr(1.09355, 0.00317922, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000410969, None, 4.45875e-05, None, 0.0017918, None, 1.38764e-05, None, 0.0017918, None, 1.38764e-05, None, 8.05837e-05, None, 1.16353e-05, None, 8.05837e-05, None, 1.16353e-05, None, 1.09361, None, 0.00752742, None, 1.09361, None, 0.00752742, None)

reports.append(Report(604062792, ("CSC", 2, 4, 2, 9), "MEm42_09"))
reports[-1].posNum = 61338
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00167913, 0.00720932, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.198064, 0.226106, 0), \
                           ValErr(-0.00331977, 0.00261127, 0), \
                           ValErr(0.00629663, 0.0117809, 0), \
                           ValErr(3.77687e-06, 5.71415e-05, 0), \
                           -93191.3, 61338, 61338, -nan)
reports[-1].sigmaresid = ValErr(1.10558, 0.00315653, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0012449, None, -4.67125e-05, None, 0.000965119, None, -3.5481e-05, None, 0.000965119, None, -3.5481e-05, None, -0.00449471, None, -7.01753e-05, None, -0.00449471, None, -7.01753e-05, None, 1.10561, None, 0.00782823, None, 1.10561, None, 0.00782823, None)

reports.append(Report(604062808, ("CSC", 2, 4, 2, 11), "MEm42_11"))
reports[-1].posNum = 60533
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00156813, 0.00722908, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.336081, 0.226764, 0), \
                           ValErr(-0.00221374, 0.00264108, 0), \
                           ValErr(-0.0051709, 0.011837, 0), \
                           ValErr(8.94023e-05, 5.75516e-05, 0), \
                           -91547.6, 60533, 60533, -nan)
reports[-1].sigmaresid = ValErr(1.09792, 0.00315545, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00209369, None, -2.293e-05, None, -0.000440222, None, -4.4566e-05, None, -0.000440222, None, -4.4566e-05, None, -0.000686985, None, -3.39079e-05, None, -0.000686985, None, -3.39079e-05, None, 1.09798, None, 0.00724307, None, 1.09798, None, 0.00724307, None)

reports.append(Report(604062824, ("CSC", 2, 4, 2, 13), "MEm42_13"))
reports[-1].posNum = 58927
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00696803, 0.0075081, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.545907, 0.165646, 0), \
                           ValErr(-0.00351539, 0.00207101, 0), \
                           ValErr(0.00497495, 0.0120166, 0), \
                           ValErr(8.74497e-05, 5.80215e-05, 0), \
                           -88674, 58927, 58927, -nan)
reports[-1].sigmaresid = ValErr(1.08967, 0.00316448, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00637807, None, -7.93667e-05, None, -0.00170364, None, -0.000143993, None, -0.00170364, None, -0.000143993, None, -0.0123917, None, -0.000119302, None, -0.0123917, None, -0.000119302, None, 1.08977, None, 0.00733178, None, 1.08977, None, 0.00733178, None)

reports.append(Report(604062840, ("CSC", 2, 4, 2, 15), "MEm42_15"))
reports[-1].posNum = 62723
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00245768, 0.00703923, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.807686, 0.181099, 0), \
                           ValErr(0.00523855, 0.00205839, 0), \
                           ValErr(0.0178481, 0.0114852, 0), \
                           ValErr(6.21135e-05, 5.49758e-05, 0), \
                           -94572.5, 62723, 62723, -nan)
reports[-1].sigmaresid = ValErr(1.09291, 0.00305343, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0107917, None, -1.44494e-05, None, 0.0069019, None, -2.66832e-05, None, 0.0069019, None, -2.66832e-05, None, 0.00916984, None, -2.78833e-05, None, 0.00916984, None, -2.78833e-05, None, 1.09308, None, 0.0072347, None, 1.09308, None, 0.0072347, None)

reports.append(Report(604062856, ("CSC", 2, 4, 2, 17), "MEm42_17"))
reports[-1].posNum = 59481
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00656407, 0.00738129, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.777018, 0.225679, 0), \
                           ValErr(0.00361209, 0.00262013, 0), \
                           ValErr(-0.00107695, 0.0119975, 0), \
                           ValErr(-0.000148753, 5.83113e-05, 0), \
                           -88930, 59481, 59481, -nan)
reports[-1].sigmaresid = ValErr(1.07914, 0.00312879, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000656517, None, -4.10767e-05, None, 0.00048201, None, -5.94925e-05, None, 0.00048201, None, -5.94925e-05, None, -0.00271931, None, -6.03472e-05, None, -0.00271931, None, -6.03472e-05, None, 1.07932, None, 0.00757461, None, 1.07932, None, 0.00757461, None)

reports.append(Report(604062872, ("CSC", 2, 4, 2, 19), "MEm42_19"))
reports[-1].posNum = 63209
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00748454, 0.00710747, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.336391, 0.219759, 0), \
                           ValErr(-0.0028332, 0.00255017, 0), \
                           ValErr(0.0127611, 0.011565, 0), \
                           ValErr(3.69969e-05, 5.62827e-05, 0), \
                           -95977.1, 63209, 63209, -nan)
reports[-1].sigmaresid = ValErr(1.10459, 0.00310669, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00395929, None, 1.52617e-05, None, -0.00107274, None, -6.36096e-06, None, -0.00107274, None, -6.36096e-06, None, -0.0105651, None, -3.61215e-05, None, -0.0105651, None, -3.61215e-05, None, 1.10463, None, 0.00771661, None, 1.10463, None, 0.00771661, None)

reports.append(Report(604062888, ("CSC", 2, 4, 2, 21), "MEm42_21"))
reports[-1].posNum = 58903
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00929793, 0.00737846, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.174623, 0.173567, 0), \
                           ValErr(-0.00399449, 0.00247865, 0), \
                           ValErr(0.00729648, 0.011858, 0), \
                           ValErr(-8.46706e-05, 5.53556e-05, 0), \
                           -87757.6, 58903, 58903, -nan)
reports[-1].sigmaresid = ValErr(1.07351, 0.00300118, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00120381, None, 6.51501e-05, None, 0.00868326, None, 4.63384e-05, None, 0.00868326, None, 4.63384e-05, None, 0.0079044, None, 7.36383e-05, None, 0.0079044, None, 7.36383e-05, None, 1.07356, None, 0.00744052, None, 1.07356, None, 0.00744052, None)

reports.append(Report(604062904, ("CSC", 2, 4, 2, 23), "MEm42_23"))
reports[-1].posNum = 63296
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0098194, 0.0070862, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.244045, 0.221024, 0), \
                           ValErr(-0.00025523, 0.00256592, 0), \
                           ValErr(0.00463769, 0.0115523, 0), \
                           ValErr(-3.89549e-06, 5.63611e-05, 0), \
                           -96156.9, 63296, 63296, -nan)
reports[-1].sigmaresid = ValErr(1.10542, 0.00310689, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00877452, None, -8.77438e-05, None, -0.00803263, None, -0.000106266, None, -0.00803263, None, -0.000106266, None, -0.00714824, None, -6.83242e-05, None, -0.00714824, None, -6.83242e-05, None, 1.10543, None, 0.00722806, None, 1.10543, None, 0.00722806, None)

reports.append(Report(604062920, ("CSC", 2, 4, 2, 25), "MEm42_25"))
reports[-1].posNum = 60990
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00212781, 0.00728845, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.649941, 0.222295, 0), \
                           ValErr(-0.00132785, 0.00257962, 0), \
                           ValErr(-0.000353461, 0.0117368, 0), \
                           ValErr(-6.56034e-05, 5.73517e-05, 0), \
                           -91692.4, 60990, 60990, -nan)
reports[-1].sigmaresid = ValErr(1.08813, 0.00311557, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00713816, None, 1.15638e-05, None, -0.000465076, None, -2.58531e-05, None, -0.000465076, None, -2.58531e-05, None, -0.000638815, None, 1.66208e-05, None, -0.000638815, None, 1.66208e-05, None, 1.08823, None, 0.00722122, None, 1.08823, None, 0.00722122, None)

reports.append(Report(604062936, ("CSC", 2, 4, 2, 27), "MEm42_27"))
reports[-1].posNum = 61784
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00837985, 0.00715545, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.507192, 0.222999, 0), \
                           ValErr(-0.0048514, 0.00256411, 0), \
                           ValErr(-0.00320511, 0.0116892, 0), \
                           ValErr(-3.97032e-05, 5.63563e-05, 0), \
                           -93340.3, 61784, 61784, -nan)
reports[-1].sigmaresid = ValErr(1.09616, 0.00311832, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00769297, None, -3.98873e-05, None, 0.00560297, None, -5.85464e-05, None, 0.00560297, None, -5.85464e-05, None, 0.000485458, None, -6.69169e-05, None, 0.000485458, None, -6.69169e-05, None, 1.09625, None, 0.00694951, None, 1.09625, None, 0.00694951, None)

reports.append(Report(604062952, ("CSC", 2, 4, 2, 29), "MEm42_29"))
reports[-1].posNum = 61901
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000718196, 0.00716021, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.309617, 0.221518, 0), \
                           ValErr(-0.0016251, 0.00256105, 0), \
                           ValErr(-0.00406639, 0.0116295, 0), \
                           ValErr(0.0001174, 5.67313e-05, 0), \
                           -93428.8, 61901, 61901, -nan)
reports[-1].sigmaresid = ValErr(1.0946, 0.00311094, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00485062, None, 3.50129e-05, None, 0.00327259, None, -1.82029e-05, None, 0.00327259, None, -1.82029e-05, None, 0.00086027, None, 1.69793e-05, None, 0.00086027, None, 1.69793e-05, None, 1.09467, None, 0.00722662, None, 1.09467, None, 0.00722662, None)

reports.append(Report(604062968, ("CSC", 2, 4, 2, 31), "MEm42_31"))
reports[-1].posNum = 61027
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0018407, 0.00741454, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.210983, 0.224328, 0), \
                           ValErr(-0.00345294, 0.00260259, 0), \
                           ValErr(0.00158252, 0.0118871, 0), \
                           ValErr(-1.6351e-06, 5.85983e-05, 0), \
                           -92483.6, 61027, 61027, -nan)
reports[-1].sigmaresid = ValErr(1.10133, 0.0031524, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00152437, None, -5.00852e-06, None, -0.00124286, None, -3.11027e-05, None, -0.00124286, None, -3.11027e-05, None, -0.00289696, None, -1.40887e-05, None, -0.00289696, None, -1.40887e-05, None, 1.10135, None, 0.00713937, None, 1.10135, None, 0.00713937, None)

reports.append(Report(604062984, ("CSC", 2, 4, 2, 33), "MEm42_33"))
reports[-1].posNum = 62978
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00272157, 0.00703442, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.16187, 0.102993, 0), \
                           ValErr(-0.00130437, 0.00119265, 0), \
                           ValErr(0.0210834, 0.0114313, 0), \
                           ValErr(1.99963e-05, 5.56435e-05, 0), \
                           -95114.1, 62978, 62978, -nan)
reports[-1].sigmaresid = ValErr(1.09564, 0.00306736, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00680034, None, -9.20771e-06, None, 0.006428, None, -4.33079e-05, None, 0.006428, None, -4.33079e-05, None, 0.0105997, None, -3.25307e-05, None, 0.0105997, None, -3.25307e-05, None, 1.09568, None, 0.00792998, None, 1.09568, None, 0.00792998, None)

reports.append(Report(604063000, ("CSC", 2, 4, 2, 35), "MEm42_35"))
reports[-1].posNum = 58649
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0209066, 0.00756606, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.126165, 0.22591, 0), \
                           ValErr(-0.00248661, 0.00260927, 0), \
                           ValErr(-0.0155273, 0.0121258, 0), \
                           ValErr(-0.000107923, 5.91874e-05, 0), \
                           -87412.8, 58649, 58649, -nan)
reports[-1].sigmaresid = ValErr(1.07412, 0.00313623, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0173402, None, -4.02559e-05, None, 0.010354, None, -3.1898e-05, None, 0.010354, None, -3.1898e-05, None, 0.0102937, None, -2.16614e-05, None, 0.0102937, None, -2.16614e-05, None, 1.07417, None, 0.00713066, None, 1.07417, None, 0.00713066, None)

reports.append(Report(604062736, ("CSC", 2, 4, 2, 2), "MEm42_02"))
reports[-1].posNum = 61483
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00755469, 0.00736345, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.285647, 0.236008, 0), \
                           ValErr(0.000607187, 0.00277099, 0), \
                           ValErr(-0.0283154, 0.0123522, 0), \
                           ValErr(-3.88658e-05, 5.89492e-05, 0), \
                           -94303, 61483, 61483, -nan)
reports[-1].sigmaresid = ValErr(1.12172, 0.00319885, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00379281, None, 1.32166e-05, None, -0.00462977, None, 2.23061e-05, None, -0.00462977, None, 2.23061e-05, None, -0.00156461, None, 4.94749e-05, None, -0.00156461, None, 4.94749e-05, None, 1.12178, None, 0.0071967, None, 1.12178, None, 0.0071967, None)

reports.append(Report(604062752, ("CSC", 2, 4, 2, 4), "MEm42_04"))
reports[-1].posNum = 60748
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.001943, 0.00745217, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.21751, 0.233703, 0), \
                           ValErr(0.000642754, 0.00274009, 0), \
                           ValErr(-0.0054552, 0.0123344, 0), \
                           ValErr(-7.72326e-05, 5.93767e-05, 0), \
                           -92584.4, 60748, 60748, -nan)
reports[-1].sigmaresid = ValErr(1.11086, 0.00318698, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00459159, None, -1.27265e-05, None, -0.00695579, None, -3.46243e-05, None, -0.00695579, None, -3.46243e-05, None, -0.00393145, None, 9.06654e-06, None, -0.00393145, None, 9.06654e-06, None, 1.11088, None, 0.00703857, None, 1.11088, None, 0.00703857, None)

reports.append(Report(604062768, ("CSC", 2, 4, 2, 6), "MEm42_06"))
reports[-1].posNum = 63295
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0129942, 0.00716724, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.299529, 0.230658, 0), \
                           ValErr(-0.0044674, 0.00269366, 0), \
                           ValErr(0.0236231, 0.0120181, 0), \
                           ValErr(2.92394e-05, 5.74384e-05, 0), \
                           -97369.3, 63295, 63295, -nan)
reports[-1].sigmaresid = ValErr(1.12682, 0.00316705, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00977283, None, 4.76627e-05, None, -0.00284237, None, 4.64759e-05, None, -0.00284237, None, 4.64759e-05, None, -0.00206168, None, 5.72332e-05, None, -0.00206168, None, 5.72332e-05, None, 1.1269, None, 0.00726236, None, 1.1269, None, 0.00726236, None)

reports.append(Report(604062784, ("CSC", 2, 4, 2, 8), "MEm42_08"))
reports[-1].posNum = 59323
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00893089, 0.00757724, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.177247, 0.235267, 0), \
                           ValErr(-0.000923995, 0.00274585, 0), \
                           ValErr(0.0308847, 0.0125247, 0), \
                           ValErr(4.58614e-05, 6.01819e-05, 0), \
                           -89610.7, 59323, 59323, -nan)
reports[-1].sigmaresid = ValErr(1.09595, 0.00318173, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00734406, None, 1.66048e-06, None, 0.00474424, None, -3.0975e-05, None, 0.00474424, None, -3.0975e-05, None, 0.00380219, None, -1.80079e-05, None, 0.00380219, None, -1.80079e-05, None, 1.09601, None, 0.00707948, None, 1.09601, None, 0.00707948, None)

reports.append(Report(604062800, ("CSC", 2, 4, 2, 10), "MEm42_10"))
reports[-1].posNum = 64252
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00346247, 0.00713649, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.299762, 0.226892, 0), \
                           ValErr(0.000100116, 0.00264624, 0), \
                           ValErr(-0.0142772, 0.0118647, 0), \
                           ValErr(3.9126e-05, 5.67157e-05, 0), \
                           -99012.1, 64252, 64252, -nan)
reports[-1].sigmaresid = ValErr(1.12982, 0.00315176, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0030861, None, -7.50922e-05, None, -0.00111466, None, -0.000103212, None, -0.00111466, None, -0.000103212, None, -0.000718279, None, -6.7093e-05, None, -0.000718279, None, -6.7093e-05, None, 1.12986, None, 0.00743323, None, 1.12986, None, 0.00743323, None)

reports.append(Report(604062816, ("CSC", 2, 4, 2, 12), "MEm42_12"))
reports[-1].posNum = 60394
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00238308, 0.0073681, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.413431, 0.144452, 0), \
                           ValErr(-0.0032025, 0.00256303, 0), \
                           ValErr(-0.00921596, 0.0123204, 0), \
                           ValErr(-0.000148731, 5.82107e-05, 0), \
                           -91369.6, 60394, 60394, -nan)
reports[-1].sigmaresid = ValErr(1.09851, 0.00306192, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00695461, None, -4.99905e-05, None, -0.00668438, None, -5.55883e-05, None, -0.00668438, None, -5.55883e-05, None, -0.00332444, None, -2.72907e-05, None, -0.00332444, None, -2.72907e-05, None, 1.09861, None, 0.00704946, None, 1.09861, None, 0.00704946, None)

reports.append(Report(604062832, ("CSC", 2, 4, 2, 14), "MEm42_14"))
reports[-1].posNum = 63388
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00509273, 0.00711798, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.393268, 0.227367, 0), \
                           ValErr(-0.00125746, 0.00264828, 0), \
                           ValErr(0.0123507, 0.0119025, 0), \
                           ValErr(6.27794e-05, 5.67107e-05, 0), \
                           -96689.6, 63388, 63388, -nan)
reports[-1].sigmaresid = ValErr(1.11229, 0.00312394, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00479236, None, -9.76484e-06, None, 0.00184641, None, 4.59454e-06, None, 0.00184641, None, 4.59454e-06, None, 0.00243442, None, 2.15176e-05, None, 0.00243442, None, 2.15176e-05, None, 1.11234, None, 0.00751684, None, 1.11234, None, 0.00751684, None)

reports.append(Report(604062848, ("CSC", 2, 4, 2, 16), "MEm42_16"))
reports[-1].posNum = 60720
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00641783, 0.00740274, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.710168, 0.23562, 0), \
                           ValErr(0.00232382, 0.0027471, 0), \
                           ValErr(0.0140331, 0.0123671, 0), \
                           ValErr(-1.00301e-05, 5.89843e-05, 0), \
                           -92601, 60720, 60720, -nan)
reports[-1].sigmaresid = ValErr(1.11195, 0.00319083, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00335609, None, -3.35155e-05, None, -0.00127472, None, -1.86998e-05, None, -0.00127472, None, -1.86998e-05, None, -0.000101973, None, -6.26103e-06, None, -0.000101973, None, -6.26103e-06, None, 1.11205, None, 0.0069527, None, 1.11205, None, 0.0069527, None)

reports.append(Report(604062864, ("CSC", 2, 4, 2, 18), "MEm42_18"))
reports[-1].posNum = 61433
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0136034, 0.00731529, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0882338, 0.233028, 0), \
                           ValErr(-0.00449884, 0.00272581, 0), \
                           ValErr(0.0194465, 0.0121627, 0), \
                           ValErr(-3.01652e-05, 5.84126e-05, 0), \
                           -93843.2, 61433, 61433, -nan)
reports[-1].sigmaresid = ValErr(1.11475, 0.00318026, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00814498, None, 1.12096e-06, None, -0.00706489, None, 3.17982e-05, None, -0.00706489, None, 3.17982e-05, None, -0.00217033, None, 3.15457e-05, None, -0.00217033, None, 3.15457e-05, None, 1.11481, None, 0.0077214, None, 1.11481, None, 0.0077214, None)

reports.append(Report(604062880, ("CSC", 2, 4, 2, 20), "MEm42_20"))
reports[-1].posNum = 63184
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.012514, 0.0072606, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.481918, 0.229351, 0), \
                           ValErr(0.0011725, 0.00269056, 0), \
                           ValErr(0.00135125, 0.0120502, 0), \
                           ValErr(2.79434e-05, 5.79673e-05, 0), \
                           -96817.7, 63184, 63184, -nan)
reports[-1].sigmaresid = ValErr(1.12005, 0.00315079, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00679128, None, -6.75366e-06, None, -0.010992, None, -1.90889e-05, None, -0.010992, None, -1.90889e-05, None, -0.0128947, None, 1.10796e-05, None, -0.0128947, None, 1.10796e-05, None, 1.12009, None, 0.00740101, None, 1.12009, None, 0.00740101, None)

reports.append(Report(604062896, ("CSC", 2, 4, 2, 22), "MEm42_22"))
reports[-1].posNum = 59988
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0164439, 0.00740929, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.482674, 0.236916, 0), \
                           ValErr(0.000749157, 0.00279611, 0), \
                           ValErr(-0.00710822, 0.0124684, 0), \
                           ValErr(-0.000121991, 5.9112e-05, 0), \
                           -91329.5, 59988, 59988, -nan)
reports[-1].sigmaresid = ValErr(1.10907, 0.00320194, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.012921, None, 4.56995e-05, None, 0.00906618, None, 1.68404e-05, None, 0.00906618, None, 1.68404e-05, None, 0.0201937, None, 3.72165e-05, None, 0.0201937, None, 3.72165e-05, None, 1.10915, None, 0.00693605, None, 1.10915, None, 0.00693605, None)

reports.append(Report(604062912, ("CSC", 2, 4, 2, 24), "MEm42_24"))
reports[-1].posNum = 63631
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0115718, 0.00721261, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.260749, 0.125521, 0), \
                           ValErr(-0.00280651, 0.00138115, 0), \
                           ValErr(0.0133252, 0.0118825, 0), \
                           ValErr(1.53705e-05, 5.51042e-05, 0), \
                           -97449.9, 63631, 63631, -nan)
reports[-1].sigmaresid = ValErr(1.11913, 0.0030832, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00986163, None, 1.67324e-05, None, -0.00577448, None, -1.89041e-05, None, -0.00577448, None, -1.89041e-05, None, -0.00352177, None, 5.10843e-05, None, -0.00352177, None, 5.10843e-05, None, 1.11916, None, 0.00712363, None, 1.11916, None, 0.00712363, None)

reports.append(Report(604062928, ("CSC", 2, 4, 2, 26), "MEm42_26"))
reports[-1].posNum = 60438
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00144485, 0.00745534, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.374873, 0.23189, 0), \
                           ValErr(0.00122858, 0.00272445, 0), \
                           ValErr(0.000968643, 0.0122853, 0), \
                           ValErr(2.51562e-05, 5.95242e-05, 0), \
                           -91093.9, 60438, 60438, -nan)
reports[-1].sigmaresid = ValErr(1.09231, 0.00314178, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000499031, None, 3.10041e-05, None, 0.00287371, None, -1.04069e-06, None, 0.00287371, None, -1.04069e-06, None, -0.000959383, None, -1.09607e-05, None, -0.000959383, None, -1.09607e-05, None, 1.09233, None, 0.00698408, None, 1.09233, None, 0.00698408, None)

reports.append(Report(604062944, ("CSC", 2, 4, 2, 28), "MEm42_28"))
reports[-1].posNum = 64519
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0102877, 0.00720232, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.566721, 0.227741, 0), \
                           ValErr(-0.00329245, 0.0026567, 0), \
                           ValErr(-0.00741014, 0.0119439, 0), \
                           ValErr(2.95281e-06, 5.73735e-05, 0), \
                           -99679.8, 64519, 64519, -nan)
reports[-1].sigmaresid = ValErr(1.13432, 0.00315775, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00781969, None, -2.12154e-05, None, 0.00745043, None, -1.377e-08, None, 0.00745043, None, -1.377e-08, None, 0.0083755, None, -1.23684e-05, None, 0.0083755, None, -1.23684e-05, None, 1.13439, None, 0.00770108, None, 1.13439, None, 0.00770108, None)

reports.append(Report(604062960, ("CSC", 2, 4, 2, 30), "MEm42_30"))
reports[-1].posNum = 59764
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00626228, 0.00744717, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.203032, 0.234827, 0), \
                           ValErr(-0.00707574, 0.0027524, 0), \
                           ValErr(0.00768295, 0.0123807, 0), \
                           ValErr(-1.62534e-05, 5.9275e-05, 0), \
                           -90225, 59764, 59764, -nan)
reports[-1].sigmaresid = ValErr(1.09499, 0.00316721, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000460283, None, -6.50477e-06, None, -0.00400665, None, -8.92076e-07, None, -0.00400665, None, -8.92076e-07, None, -0.0104388, None, -2.32801e-05, None, -0.0104388, None, -2.32801e-05, None, 1.09507, None, 0.00734991, None, 1.09507, None, 0.00734991, None)

reports.append(Report(604062976, ("CSC", 2, 4, 2, 32), "MEm42_32"))
reports[-1].posNum = 63876
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00179934, 0.00703244, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.113731, 0.208316, 0), \
                           ValErr(-0.0011495, 0.00163764, 0), \
                           ValErr(0.0078836, 0.0113776, 0), \
                           ValErr(2.28636e-05, 4.0676e-05, 0), \
                           -97951.1, 63876, 63876, -nan)
reports[-1].sigmaresid = ValErr(1.12133, 0.00312831, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00204189, None, -6.17365e-05, None, 0.00203326, None, -5.28907e-05, None, 0.00203326, None, -5.28907e-05, None, 0.00339572, None, -5.10227e-05, None, 0.00339572, None, -5.10227e-05, None, 1.12134, None, 0.00765159, None, 1.12134, None, 0.00765159, None)

reports.append(Report(604062992, ("CSC", 2, 4, 2, 34), "MEm42_34"))
reports[-1].posNum = 61817
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.010624, 0.00729475, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.327155, 0.234553, 0), \
                           ValErr(0.000462819, 0.00274969, 0), \
                           ValErr(0.0144352, 0.0122545, 0), \
                           ValErr(7.79638e-05, 5.83534e-05, 0), \
                           -94697.7, 61817, 61817, -nan)
reports[-1].sigmaresid = ValErr(1.11959, 0.00318414, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00534641, None, -1.71612e-05, None, -0.00232979, None, -1.69567e-05, None, -0.00232979, None, -1.69567e-05, None, -0.000654847, None, -2.7143e-06, None, -0.000654847, None, -2.7143e-06, None, 1.11963, None, 0.00717427, None, 1.11963, None, 0.00717427, None)

reports.append(Report(604063008, ("CSC", 2, 4, 2, 36), "MEm42_36"))
reports[-1].posNum = 63107
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00175631, 0.00715638, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.439466, 0.228844, 0), \
                           ValErr(-0.00317511, 0.00266412, 0), \
                           ValErr(0.0187565, 0.0119589, 0), \
                           ValErr(2.93831e-05, 5.69456e-05, 0), \
                           -96510.3, 63107, 63107, -nan)
reports[-1].sigmaresid = ValErr(1.11669, 0.00314326, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0065783, None, 8.04001e-06, None, 0.0100784, None, 4.89258e-05, None, 0.0100784, None, 4.89258e-05, None, 0.0136222, None, 8.1019e-05, None, 0.0136222, None, 8.1019e-05, None, 1.11677, None, 0.0072394, None, 1.11677, None, 0.0072394, None)

