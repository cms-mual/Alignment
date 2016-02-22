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
reports[-1].posNum = 138884
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00100564, 0.000714747, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.136021, 0.0413057, 0), \
                           ValErr(0.000716258, 0.00109434, 0), \
                           ValErr(0.00426206, 0.00544969, 0), \
                           ValErr(1.37624e-05, 1.46867e-05, 0), \
                           33303.1, 138884, 138884, -nan)
reports[-1].sigmaresid = ValErr(0.190381, 0.000361228, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000938679, None, -7.03828e-06, None, -0.00123703, None, 2.76193e-06, None, -0.00123703, None, 2.76193e-06, None, -0.000610749, None, 2.16473e-06, None, -0.000610749, None, 2.16473e-06, None, 0.190392, None, 0.00422924, None, 0.190392, None, 0.00422924, None)

reports.append(Report(604017688, ("CSC", 1, 1, 1, 3), "MEp11_03"))
reports[-1].posNum = 139490
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00238751, 0.000713484, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0895415, 0.0409953, 0), \
                           ValErr(-2.41661e-05, 0.00108497, 0), \
                           ValErr(-0.00630985, 0.00545302, 0), \
                           ValErr(1.45184e-05, 1.45197e-05, 0), \
                           34061.3, 139490, 139490, -nan)
reports[-1].sigmaresid = ValErr(0.189546, 0.000358862, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00138054, None, 9.24261e-07, None, -0.00174383, None, -2.89499e-06, None, -0.00174383, None, -2.89499e-06, None, -0.00177538, None, 1.26128e-05, None, -0.00177538, None, 1.26128e-05, None, 0.189551, None, 0.0043013, None, 0.189551, None, 0.0043013, None)

reports.append(Report(604017704, ("CSC", 1, 1, 1, 5), "MEp11_05"))
reports[-1].posNum = 139156
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000912597, 0.000714683, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.105502, 0.04135, 0), \
                           ValErr(-0.000816756, 0.0010902, 0), \
                           ValErr(0.00818595, 0.00544377, 0), \
                           ValErr(1.9713e-05, 1.46248e-05, 0), \
                           33160.9, 139156, 139156, -nan)
reports[-1].sigmaresid = ValErr(0.190665, 0.000361414, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0015147, None, -5.63596e-06, None, -0.00140513, None, 3.04246e-06, None, -0.00140513, None, 3.04246e-06, None, -0.00171008, None, -3.2201e-06, None, -0.00171008, None, -3.2201e-06, None, 0.190674, None, 0.00414925, None, 0.190674, None, 0.00414925, None)

reports.append(Report(604017720, ("CSC", 1, 1, 1, 7), "MEp11_07"))
reports[-1].posNum = 139378
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00146198, 0.000715299, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.145518, 0.0412789, 0), \
                           ValErr(-0.00134256, 0.00109292, 0), \
                           ValErr(-0.00270466, 0.00544919, 0), \
                           ValErr(-3.67e-05, 1.46339e-05, 0), \
                           33113.5, 139378, 139378, -nan)
reports[-1].sigmaresid = ValErr(0.190802, 0.000361386, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000891205, None, -4.28966e-06, None, -0.00154883, None, -2.09359e-06, None, -0.00154883, None, -2.09359e-06, None, -0.0020146, None, 1.70307e-05, None, -0.0020146, None, 1.70307e-05, None, 0.190816, None, 0.00419928, None, 0.190816, None, 0.00419928, None)

reports.append(Report(604017736, ("CSC", 1, 1, 1, 9), "MEp11_09"))
reports[-1].posNum = 138855
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00254735, 0.000714469, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.074378, 0.0411879, 0), \
                           ValErr(-0.00052773, 0.00108935, 0), \
                           ValErr(-0.00958045, 0.00544424, 0), \
                           ValErr(4.73321e-05, 1.46485e-05, 0), \
                           33741.6, 138855, 138855, -nan)
reports[-1].sigmaresid = ValErr(0.189771, 0.000362769, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000776008, None, 4.89995e-06, None, -0.00135629, None, 4.50027e-06, None, -0.00135629, None, 4.50027e-06, None, -0.000362622, None, -3.19272e-05, None, -0.000362622, None, -3.19272e-05, None, 0.189781, None, 0.00436526, None, 0.189781, None, 0.00436526, None)

reports.append(Report(604017752, ("CSC", 1, 1, 1, 11), "MEp11_11"))
reports[-1].posNum = 138257
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000831451, 0.000718982, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.185423, 0.0414816, 0), \
                           ValErr(-0.00196656, 0.0010966, 0), \
                           ValErr(0.00922222, 0.00547106, 0), \
                           ValErr(1.23314e-06, 1.47444e-05, 0), \
                           32545.7, 138257, 138257, -nan)
reports[-1].sigmaresid = ValErr(0.191218, 0.00036364, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00207658, None, -6.21503e-06, None, -0.00156067, None, -2.82844e-05, None, -0.00156067, None, -2.82844e-05, None, -0.00169476, None, -1.38291e-05, None, -0.00169476, None, -1.38291e-05, None, 0.191235, None, 0.00455632, None, 0.191235, None, 0.00455632, None)

reports.append(Report(604017768, ("CSC", 1, 1, 1, 13), "MEp11_13"))
reports[-1].posNum = 139768
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00295452, 0.000713481, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.105666, 0.0410422, 0), \
                           ValErr(-0.00062681, 0.00108974, 0), \
                           ValErr(0.00122709, 0.00543, 0), \
                           ValErr(5.1668e-06, 1.45898e-05, 0), \
                           33736.5, 139768, 139768, -nan)
reports[-1].sigmaresid = ValErr(0.190079, 0.000359515, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00282231, None, 3.67413e-07, None, -0.00301402, None, -6.96107e-07, None, -0.00301402, None, -6.96107e-07, None, -0.00285554, None, -4.48345e-06, None, -0.00285554, None, -4.48345e-06, None, 0.190084, None, 0.00416052, None, 0.190084, None, 0.00416052, None)

reports.append(Report(604017784, ("CSC", 1, 1, 1, 15), "MEp11_15"))
reports[-1].posNum = 138348
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0018088, 0.000714232, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0895986, 0.0411479, 0), \
                           ValErr(-0.00130607, 0.0010913, 0), \
                           ValErr(-0.00561005, 0.00543469, 0), \
                           ValErr(1.54866e-05, 1.51913e-05, 0), \
                           33514.6, 138348, 138348, -nan)
reports[-1].sigmaresid = ValErr(0.189913, 0.000361069, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00120239, None, -9.57428e-07, None, -0.00121873, None, -8.77054e-06, None, -0.00121873, None, -8.77054e-06, None, -0.000952917, None, -1.62304e-05, None, -0.000952917, None, -1.62304e-05, None, 0.189918, None, 0.00438629, None, 0.189918, None, 0.00438629, None)

reports.append(Report(604017800, ("CSC", 1, 1, 1, 17), "MEp11_17"))
reports[-1].posNum = 140088
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00109051, 0.000708962, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0553144, 0.0407598, 0), \
                           ValErr(-0.000536281, 0.00107833, 0), \
                           ValErr(0.00436992, 0.005426, 0), \
                           ValErr(1.92435e-06, 1.44257e-05, 0), \
                           34930, 140088, 140088, -nan)
reports[-1].sigmaresid = ValErr(0.18857, 0.000356251, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00192716, None, 6.47383e-06, None, -0.00142335, None, -4.0212e-06, None, -0.00142335, None, -4.0212e-06, None, -0.000985259, None, -1.28187e-05, None, -0.000985259, None, -1.28187e-05, None, 0.188573, None, 0.00418342, None, 0.188573, None, 0.00418342, None)

reports.append(Report(604017816, ("CSC", 1, 1, 1, 19), "MEp11_19"))
reports[-1].posNum = 138873
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00110726, 0.000715404, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0931945, 0.0411603, 0), \
                           ValErr(-0.00132769, 0.00108848, 0), \
                           ValErr(-0.00219269, 0.00545031, 0), \
                           ValErr(-7.52289e-06, 1.46872e-05, 0), \
                           33400.7, 138873, 138873, -nan)
reports[-1].sigmaresid = ValErr(0.190243, 0.000360982, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0010376, None, 2.32311e-06, None, -0.000994262, None, -7.7388e-06, None, -0.000994262, None, -7.7388e-06, None, -0.000230959, None, -3.09566e-05, None, -0.000230959, None, -3.09566e-05, None, 0.190248, None, 0.00431309, None, 0.190248, None, 0.00431309, None)

reports.append(Report(604017832, ("CSC", 1, 1, 1, 21), "MEp11_21"))
reports[-1].posNum = 139103
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00216522, 0.000709105, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0573837, 0.0409825, 0), \
                           ValErr(3.22772e-05, 0.00108164, 0), \
                           ValErr(0.000270921, 0.00542092, 0), \
                           ValErr(1.88198e-05, 1.44593e-05, 0), \
                           34587.4, 139103, 139103, -nan)
reports[-1].sigmaresid = ValErr(0.188702, 0.000357762, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00179156, None, 1.8255e-06, None, -0.00201582, None, -1.53645e-05, None, -0.00201582, None, -1.53645e-05, None, -0.00359913, None, -1.32416e-05, None, -0.00359913, None, -1.32416e-05, None, 0.188705, None, 0.00427251, None, 0.188705, None, 0.00427251, None)

reports.append(Report(604017848, ("CSC", 1, 1, 1, 23), "MEp11_23"))
reports[-1].posNum = 138580
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00217676, 0.000717161, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0619837, 0.0414509, 0), \
                           ValErr(9.53083e-05, 0.00109573, 0), \
                           ValErr(0.00454866, 0.00547142, 0), \
                           ValErr(2.49287e-05, 1.47068e-05, 0), \
                           32725.7, 138580, 138580, -nan)
reports[-1].sigmaresid = ValErr(0.191075, 0.000362943, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0017078, None, 1.35845e-06, None, -0.00233335, None, 2.77786e-06, None, -0.00233335, None, 2.77786e-06, None, -0.00205359, None, -1.24655e-05, None, -0.00205359, None, -1.24655e-05, None, 0.19108, None, 0.00475761, None, 0.19108, None, 0.00475761, None)

reports.append(Report(604017864, ("CSC", 1, 1, 1, 25), "MEp11_25"))
reports[-1].posNum = 139088
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00166755, 0.000715489, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0730236, 0.0411069, 0), \
                           ValErr(-0.00258049, 0.00108897, 0), \
                           ValErr(0.00347248, 0.00545937, 0), \
                           ValErr(2.35977e-05, 1.46199e-05, 0), \
                           33608.7, 139088, 139088, -nan)
reports[-1].sigmaresid = ValErr(0.19003, 0.000360298, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0011455, None, 9.1347e-06, None, -0.00174192, None, 3.42948e-07, None, -0.00174192, None, 3.42948e-07, None, 0.000200836, None, -1.15376e-05, None, 0.000200836, None, -1.15376e-05, None, 0.190037, None, 0.00458187, None, 0.190037, None, 0.00458187, None)

reports.append(Report(604017880, ("CSC", 1, 1, 1, 27), "MEp11_27"))
reports[-1].posNum = 138675
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00202654, 0.000713281, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0839467, 0.0411893, 0), \
                           ValErr(-0.00270067, 0.00109193, 0), \
                           ValErr(-0.0041133, 0.00544692, 0), \
                           ValErr(1.06051e-05, 1.46183e-05, 0), \
                           33655.4, 138675, 138675, -nan)
reports[-1].sigmaresid = ValErr(0.189829, 0.000360453, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00168449, None, 5.80301e-06, None, -0.00161058, None, -1.09511e-05, None, -0.00161058, None, -1.09511e-05, None, -0.00142794, None, -2.44097e-05, None, -0.00142794, None, -2.44097e-05, None, 0.189835, None, 0.00418351, None, 0.189835, None, 0.00418351, None)

reports.append(Report(604017896, ("CSC", 1, 1, 1, 29), "MEp11_29"))
reports[-1].posNum = 138134
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00387309, 0.000717752, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.124205, 0.0414481, 0), \
                           ValErr(-0.000939291, 0.00110351, 0), \
                           ValErr(-0.00119693, 0.00548322, 0), \
                           ValErr(2.74455e-05, 1.47192e-05, 0), \
                           32901.6, 138134, 138134, -nan)
reports[-1].sigmaresid = ValErr(0.190687, 0.00036279, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00364881, None, 1.61258e-05, None, -0.00354443, None, 1.87152e-05, None, -0.00354443, None, 1.87152e-05, None, -0.00222755, None, 7.91153e-06, None, -0.00222755, None, 7.91153e-06, None, 0.190695, None, 0.00413851, None, 0.190695, None, 0.00413851, None)

reports.append(Report(604017912, ("CSC", 1, 1, 1, 31), "MEp11_31"))
reports[-1].posNum = 139030
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00243394, 0.000712924, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0873818, 0.0413227, 0), \
                           ValErr(-0.00211869, 0.00109231, 0), \
                           ValErr(-0.00900692, 0.00546076, 0), \
                           ValErr(-9.08955e-06, 1.45563e-05, 0), \
                           33389.5, 139030, 139030, -nan)
reports[-1].sigmaresid = ValErr(0.19031, 0.000360905, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00179817, None, -9.54318e-07, None, -0.00180179, None, -1.53549e-06, None, -0.00180179, None, -1.53549e-06, None, -0.00145595, None, -1.35444e-05, None, -0.00145595, None, -1.35444e-05, None, 0.190318, None, 0.00416378, None, 0.190318, None, 0.00416378, None)

reports.append(Report(604017928, ("CSC", 1, 1, 1, 33), "MEp11_33"))
reports[-1].posNum = 138333
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00118067, 0.000721647, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.133674, 0.0415469, 0), \
                           ValErr(-0.00137522, 0.00110512, 0), \
                           ValErr(0.00124592, 0.00549694, 0), \
                           ValErr(-1.10928e-05, 1.48312e-05, 0), \
                           32159.6, 138333, 138333, -nan)
reports[-1].sigmaresid = ValErr(0.191778, 0.000364603, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00174476, None, -5.71768e-06, None, -0.00138829, None, -1.02815e-05, None, -0.00138829, None, -1.02815e-05, None, 0.00063659, None, -1.3814e-05, None, 0.00063659, None, -1.3814e-05, None, 0.191785, None, 0.00484283, None, 0.191785, None, 0.00484283, None)

reports.append(Report(604017944, ("CSC", 1, 1, 1, 35), "MEp11_35"))
reports[-1].posNum = 140048
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00187641, 0.000710273, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0411995, 0.0408116, 0), \
                           ValErr(-0.000660235, 0.00107729, 0), \
                           ValErr(-0.000917588, 0.00537333, 0), \
                           ValErr(4.3598e-06, 1.45211e-05, 0), \
                           34349.8, 140048, 140048, -nan)
reports[-1].sigmaresid = ValErr(0.18934, 0.000357758, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00123343, None, 2.49975e-06, None, -0.00176655, None, 3.18072e-06, None, -0.00176655, None, 3.18072e-06, None, -0.00143788, None, -4.69896e-06, None, -0.00143788, None, -4.69896e-06, None, 0.189341, None, 0.00415982, None, 0.189341, None, 0.00415982, None)

reports.append(Report(604017680, ("CSC", 1, 1, 1, 2), "MEp11_02"))
reports[-1].posNum = 138704
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00141452, 0.000641901, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0716196, 0.0348486, 0), \
                           ValErr(-0.000420212, 0.000923806, 0), \
                           ValErr(-0.000689824, 0.00463041, 0), \
                           ValErr(-1.06259e-05, 1.30305e-05, 0), \
                           48932.7, 138704, 138704, -nan)
reports[-1].sigmaresid = ValErr(0.17004, 0.000322842, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00155534, None, 7.83989e-06, None, -0.00145239, None, 3.37346e-05, None, -0.00145239, None, 3.37346e-05, None, -0.00105302, None, 3.58284e-05, None, -0.00105302, None, 3.58284e-05, None, 0.170043, None, 0.00446, None, 0.170043, None, 0.00446, None)

reports.append(Report(604017696, ("CSC", 1, 1, 1, 4), "MEp11_04"))
reports[-1].posNum = 138471
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00161749, 0.00063815, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.105553, 0.0364382, 0), \
                           ValErr(-0.000184518, 0.000955467, 0), \
                           ValErr(-0.00719011, 0.00465031, 0), \
                           ValErr(-1.43401e-06, 1.404e-05, 0), \
                           49299.3, 138471, 138471, -nan)
reports[-1].sigmaresid = ValErr(0.169489, 0.000320925, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000784349, None, -1.26461e-06, None, -0.00102612, None, -4.7278e-06, None, -0.00102612, None, -4.7278e-06, None, 0.000215076, None, -7.66958e-06, None, 0.000215076, None, -7.66958e-06, None, 0.169497, None, 0.00509413, None, 0.169497, None, 0.00509413, None)

reports.append(Report(604017712, ("CSC", 1, 1, 1, 6), "MEp11_06"))
reports[-1].posNum = 139204
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00146055, 0.000639416, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.03315, 0.0348754, 0), \
                           ValErr(0.000469439, 0.000923256, 0), \
                           ValErr(0.0014579, 0.00460785, 0), \
                           ValErr(-3.54402e-06, 1.30388e-05, 0), \
                           48872.9, 139204, 139204, -nan)
reports[-1].sigmaresid = ValErr(0.170328, 0.00032281, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00135668, None, 6.51474e-06, None, -0.00161814, None, 2.25595e-05, None, -0.00161814, None, 2.25595e-05, None, -0.00156078, None, 2.44083e-05, None, -0.00156078, None, 2.44083e-05, None, 0.170329, None, 0.00438026, None, 0.170329, None, 0.00438026, None)

reports.append(Report(604017728, ("CSC", 1, 1, 1, 8), "MEp11_08"))
reports[-1].posNum = 138052
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00117097, 0.000641304, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0825275, 0.0349086, 0), \
                           ValErr(-0.00165058, 0.000924449, 0), \
                           ValErr(-0.000192475, 0.00464381, 0), \
                           ValErr(-2.56164e-06, 1.30157e-05, 0), \
                           49064.4, 138052, 138052, -nan)
reports[-1].sigmaresid = ValErr(0.169595, 0.000322757, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000678981, None, 8.32166e-06, None, -0.00117587, None, 6.55083e-07, None, -0.00117587, None, 6.55083e-07, None, 0.000241782, None, 2.09377e-06, None, 0.000241782, None, 2.09377e-06, None, 0.169599, None, 0.00439385, None, 0.169599, None, 0.00439385, None)

reports.append(Report(604017744, ("CSC", 1, 1, 1, 10), "MEp11_10"))
reports[-1].posNum = 138732
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00025241, 0.000643786, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0752704, 0.0349146, 0), \
                           ValErr(-0.000136737, 0.000925515, 0), \
                           ValErr(0.00345989, 0.0046233, 0), \
                           ValErr(-5.1001e-06, 1.30831e-05, 0), \
                           48581, 138732, 138732, -nan)
reports[-1].sigmaresid = ValErr(0.170483, 0.000323652, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00082322, None, -9.4542e-07, None, -0.000594369, None, 2.39589e-05, None, -0.000594369, None, 2.39589e-05, None, -0.000217591, None, -1.72508e-06, None, -0.000217591, None, -1.72508e-06, None, 0.170487, None, 0.00450801, None, 0.170487, None, 0.00450801, None)

reports.append(Report(604017760, ("CSC", 1, 1, 1, 12), "MEp11_12"))
reports[-1].posNum = 138939
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00140063, 0.000636861, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0542025, 0.0348536, 0), \
                           ValErr(-0.000438622, 0.000919534, 0), \
                           ValErr(0.00219055, 0.0046329, 0), \
                           ValErr(-8.19892e-06, 1.2946e-05, 0), \
                           49455.4, 138939, 138939, -nan)
reports[-1].sigmaresid = ValErr(0.169502, 0.00032155, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00169794, None, 1.55718e-05, None, -0.00165933, None, 3.04139e-05, None, -0.00165933, None, 3.04139e-05, None, -0.00113512, None, 1.77965e-06, None, -0.00113512, None, 1.77965e-06, None, 0.169504, None, 0.00445683, None, 0.169504, None, 0.00445683, None)

reports.append(Report(604017776, ("CSC", 1, 1, 1, 14), "MEp11_14"))
reports[-1].posNum = 138803
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000243235, 0.000641261, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.105941, 0.0349691, 0), \
                           ValErr(0.000976182, 0.000926435, 0), \
                           ValErr(0.0036903, 0.0046368, 0), \
                           ValErr(-9.12983e-07, 1.30471e-05, 0), \
                           48781.8, 138803, 138803, -nan)
reports[-1].sigmaresid = ValErr(0.170267, 0.00032316, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00064532, None, 2.14843e-06, None, -0.000571514, None, 1.11131e-05, None, -0.000571514, None, 1.11131e-05, None, -4.793e-06, None, 7.90058e-06, None, -4.793e-06, None, 7.90058e-06, None, 0.170276, None, 0.00504517, None, 0.170276, None, 0.00504517, None)

reports.append(Report(604017792, ("CSC", 1, 1, 1, 16), "MEp11_16"))
reports[-1].posNum = 137660
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00266911, 0.000642349, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.128792, 0.0351798, 0), \
                           ValErr(-0.00255558, 0.000931571, 0), \
                           ValErr(0.00438033, 0.00466016, 0), \
                           ValErr(9.52997e-06, 1.30909e-05, 0), \
                           48465.4, 137660, 137660, -nan)
reports[-1].sigmaresid = ValErr(0.170162, 0.000324297, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00244959, None, 1.64264e-05, None, -0.00295277, None, 2.92156e-05, None, -0.00295277, None, 2.92156e-05, None, -0.00375706, None, 2.82962e-05, None, -0.00375706, None, 2.82962e-05, None, 0.170174, None, 0.00459658, None, 0.170174, None, 0.00459658, None)

reports.append(Report(604017808, ("CSC", 1, 1, 1, 18), "MEp11_18"))
reports[-1].posNum = 138630
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00143584, 0.000640588, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0998533, 0.0350051, 0), \
                           ValErr(-0.000335299, 0.00092412, 0), \
                           ValErr(0.000829005, 0.00463918, 0), \
                           ValErr(1.04893e-05, 1.30409e-05, 0), \
                           48829.1, 138630, 138630, -nan)
reports[-1].sigmaresid = ValErr(0.170135, 0.000323109, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0010042, None, 1.98199e-05, None, -0.00141193, None, 3.76241e-05, None, -0.00141193, None, 3.76241e-05, None, -0.000864532, None, 3.68135e-05, None, -0.000864532, None, 3.68135e-05, None, 0.17014, None, 0.00492538, None, 0.17014, None, 0.00492538, None)

reports.append(Report(604017824, ("CSC", 1, 1, 1, 20), "MEp11_20"))
reports[-1].posNum = 138600
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000775373, 0.000641437, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0577192, 0.0349242, 0), \
                           ValErr(-0.00110019, 0.000923706, 0), \
                           ValErr(0.00880475, 0.00463999, 0), \
                           ValErr(1.95632e-05, 1.30725e-05, 0), \
                           48940.7, 138600, 138600, -nan)
reports[-1].sigmaresid = ValErr(0.169985, 0.000322859, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00125468, None, 1.4293e-05, None, -0.00134231, None, 3.29132e-05, None, -0.00134231, None, 3.29132e-05, None, -0.00148336, None, 2.15638e-05, None, -0.00148336, None, 2.15638e-05, None, 0.169992, None, 0.00480318, None, 0.169992, None, 0.00480318, None)

reports.append(Report(604017840, ("CSC", 1, 1, 1, 22), "MEp11_22"))
reports[-1].posNum = 138069
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0020496, 0.00064123, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0934292, 0.034823, 0), \
                           ValErr(-0.000957739, 0.000922676, 0), \
                           ValErr(-0.00316592, 0.00464261, 0), \
                           ValErr(-1.59361e-05, 1.30106e-05, 0), \
                           49192.6, 138069, 138069, -nan)
reports[-1].sigmaresid = ValErr(0.169445, 0.000322452, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00203273, None, 4.38637e-06, None, -0.00193919, None, -1.65231e-05, None, -0.00193919, None, -1.65231e-05, None, -0.00178734, None, 3.32821e-06, None, -0.00178734, None, 3.32821e-06, None, 0.169451, None, 0.0046988, None, 0.169451, None, 0.0046988, None)

reports.append(Report(604017856, ("CSC", 1, 1, 1, 24), "MEp11_24"))
reports[-1].posNum = 138042
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00287301, 0.000641407, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0560433, 0.0351004, 0), \
                           ValErr(-0.00153009, 0.000923255, 0), \
                           ValErr(-0.00470127, 0.00462893, 0), \
                           ValErr(-1.27329e-05, 1.3078e-05, 0), \
                           48628.3, 138042, 138042, -nan)
reports[-1].sigmaresid = ValErr(0.170127, 0.000323782, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00202377, None, 1.80972e-05, None, -0.00259375, None, 3.24187e-05, None, -0.00259375, None, 3.24187e-05, None, -0.00131471, None, 2.25398e-05, None, -0.00131471, None, 2.25398e-05, None, 0.170131, None, 0.00452062, None, 0.170131, None, 0.00452062, None)

reports.append(Report(604017872, ("CSC", 1, 1, 1, 26), "MEp11_26"))
reports[-1].posNum = 138749
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000277724, 0.000639334, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0750062, 0.0350392, 0), \
                           ValErr(0.0024212, 0.000925759, 0), \
                           ValErr(0.00627216, 0.00463848, 0), \
                           ValErr(-1.43076e-05, 1.30298e-05, 0), \
                           48814.9, 138749, 138749, -nan)
reports[-1].sigmaresid = ValErr(0.170204, 0.000323101, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000733668, None, 8.13465e-07, None, -0.000941626, None, 3.22875e-05, None, -0.000941626, None, 3.22875e-05, None, -0.00078907, None, 1.11962e-05, None, -0.00078907, None, 1.11962e-05, None, 0.170215, None, 0.00489382, None, 0.170215, None, 0.00489382, None)

reports.append(Report(604017888, ("CSC", 1, 1, 1, 28), "MEp11_28"))
reports[-1].posNum = 137844
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000753923, 0.000647088, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.106318, 0.0352806, 0), \
                           ValErr(-0.00162637, 0.000933167, 0), \
                           ValErr(0.000162502, 0.00467555, 0), \
                           ValErr(-1.10569e-05, 1.31518e-05, 0), \
                           47713.7, 137844, 137844, -nan)
reports[-1].sigmaresid = ValErr(0.171173, 0.000326006, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000738678, None, 3.06366e-06, None, -0.000877885, None, 2.44924e-05, None, -0.000877885, None, 2.44924e-05, None, -0.00164477, None, 1.2728e-05, None, -0.00164477, None, 1.2728e-05, None, 0.17118, None, 0.00429567, None, 0.17118, None, 0.00429567, None)

reports.append(Report(604017904, ("CSC", 1, 1, 1, 30), "MEp11_30"))
reports[-1].posNum = 137481
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00157962, 0.000638118, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.120435, 0.0349834, 0), \
                           ValErr(-3.4201e-05, 0.000927085, 0), \
                           ValErr(-0.00420417, 0.00463648, 0), \
                           ValErr(3.89606e-06, 1.30127e-05, 0), \
                           49409.9, 137481, 137481, -nan)
reports[-1].sigmaresid = ValErr(0.16892, 0.000322139, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000898209, None, 6.12591e-06, None, -0.00120406, None, 2.72755e-05, None, -0.00120406, None, 2.72755e-05, None, -0.000718734, None, 1.48253e-05, None, -0.000718734, None, 1.48253e-05, None, 0.168928, None, 0.00461617, None, 0.168928, None, 0.00461617, None)

reports.append(Report(604017920, ("CSC", 1, 1, 1, 32), "MEp11_32"))
reports[-1].posNum = 138711
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00339383, 0.000641252, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0890779, 0.0350664, 0), \
                           ValErr(-0.00025686, 0.000923949, 0), \
                           ValErr(-0.013475, 0.00462776, 0), \
                           ValErr(2.57968e-05, 1.3054e-05, 0), \
                           48524.3, 138711, 138711, -nan)
reports[-1].sigmaresid = ValErr(0.170544, 0.000323792, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00172317, None, 7.05024e-06, None, -0.00202515, None, 2.42545e-05, None, -0.00202515, None, 2.42545e-05, None, -0.00100466, None, 2.55491e-05, None, -0.00100466, None, 2.55491e-05, None, 0.170554, None, 0.0044059, None, 0.170554, None, 0.0044059, None)

reports.append(Report(604017936, ("CSC", 1, 1, 1, 34), "MEp11_34"))
reports[-1].posNum = 129715
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00193002, 0.000675943, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0657787, 0.0375387, 0), \
                           ValErr(-0.000395434, 0.00105234, 0), \
                           ValErr(-0.00367714, 0.00477878, 0), \
                           ValErr(2.02114e-05, 1.41647e-05, 0), \
                           46611.9, 129715, 129715, -nan)
reports[-1].sigmaresid = ValErr(0.168928, 0.000330844, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00155399, None, -3.2499e-05, None, -0.00142152, None, -8.70145e-05, None, -0.00142152, None, -8.70145e-05, None, -0.000694473, None, -5.47698e-05, None, -0.000694473, None, -5.47698e-05, None, 0.168932, None, 0.00547895, None, 0.168932, None, 0.00547895, None)

reports.append(Report(604017952, ("CSC", 1, 1, 1, 36), "MEp11_36"))
reports[-1].posNum = 139067
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00197685, 0.00063948, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.114927, 0.0347955, 0), \
                           ValErr(-0.000115158, 0.000921496, 0), \
                           ValErr(0.00896758, 0.0046188, 0), \
                           ValErr(2.01855e-05, 1.30108e-05, 0), \
                           49221, 139067, 139067, -nan)
reports[-1].sigmaresid = ValErr(0.169844, 0.000322049, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00240905, None, 1.20468e-05, None, -0.00255343, None, 5.24895e-05, None, -0.00255343, None, 5.24895e-05, None, -0.002312, None, 3.17298e-05, None, -0.002312, None, 3.17298e-05, None, 0.169857, None, 0.00503976, None, 0.169857, None, 0.00503976, None)

reports.append(Report(604018184, ("CSC", 1, 1, 2, 1), "MEp12_01"))
reports[-1].posNum = 65104
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00401602, 0.00323047, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.207537, 0.0935177, 0), \
                           ValErr(0.00173501, 0.00201235, 0), \
                           ValErr(-0.0103956, 0.00685251, 0), \
                           ValErr(-2.13202e-07, 5.06738e-05, 0), \
                           -54728.6, 65104, 65104, -nan)
reports[-1].sigmaresid = ValErr(0.560847, 0.00155426, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00101254, None, -2.36826e-06, None, -0.000976509, None, 2.23601e-06, None, -0.000976509, None, 2.23601e-06, None, -0.00125555, None, -1.52788e-06, None, -0.00125555, None, -1.52788e-06, None, 0.560885, None, 0.00426154, None, 0.560885, None, 0.00426154, None)

reports.append(Report(604018200, ("CSC", 1, 1, 2, 3), "MEp12_03"))
reports[-1].posNum = 58077
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00752816, 0.00334921, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0707187, 0.0983472, 0), \
                           ValErr(-0.00414922, 0.00204908, 0), \
                           ValErr(0.00986439, 0.00717315, 0), \
                           ValErr(-6.90913e-05, 5.13636e-05, 0), \
                           -46147.4, 58077, 58077, -nan)
reports[-1].sigmaresid = ValErr(0.53561, 0.00157156, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00141923, None, -1.08929e-05, None, 0.00331825, None, -7.16549e-06, None, 0.00331825, None, -7.16549e-06, None, 0.00981888, None, -2.62116e-05, None, 0.00981888, None, -2.62116e-05, None, 0.535643, None, 0.00426611, None, 0.535643, None, 0.00426611, None)

reports.append(Report(604018216, ("CSC", 1, 1, 2, 5), "MEp12_05"))
reports[-1].posNum = 64638
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00326874, 0.00311588, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.147365, 0.0933794, 0), \
                           ValErr(-0.00221191, 0.00199906, 0), \
                           ValErr(-0.000287541, 0.00676205, 0), \
                           ValErr(-4.27344e-05, 4.87957e-05, 0), \
                           -53035.4, 64638, 64638, -nan)
reports[-1].sigmaresid = ValErr(0.549668, 0.00152877, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00400879, None, -2.89881e-06, None, 0.00271713, None, 3.33014e-07, None, 0.00271713, None, 3.33014e-07, None, 0.00909849, None, -4.21773e-05, None, 0.00909849, None, -4.21773e-05, None, 0.54969, None, 0.00400528, None, 0.54969, None, 0.00400528, None)

reports.append(Report(604018232, ("CSC", 1, 1, 2, 7), "MEp12_07"))
reports[-1].posNum = 58252
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0065495, 0.00343969, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.158993, 0.0974656, 0), \
                           ValErr(-0.00322783, 0.00207355, 0), \
                           ValErr(-0.00321766, 0.00720999, 0), \
                           ValErr(8.38337e-05, 5.27611e-05, 0), \
                           -47360.5, 58252, 58252, -nan)
reports[-1].sigmaresid = ValErr(0.545576, 0.0015984, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00263259, None, -1.69807e-05, None, -0.00386542, None, -1.74551e-05, None, -0.00386542, None, -1.74551e-05, None, -0.00206934, None, -6.1065e-06, None, -0.00206934, None, -6.1065e-06, None, 0.545609, None, 0.00436472, None, 0.545609, None, 0.00436472, None)

reports.append(Report(604018248, ("CSC", 1, 1, 2, 9), "MEp12_09"))
reports[-1].posNum = 59387
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000301376, 0.0032729, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.204562, 0.0993682, 0), \
                           ValErr(-0.00229809, 0.00208355, 0), \
                           ValErr(-0.000552989, 0.00710831, 0), \
                           ValErr(-4.78633e-05, 5.07659e-05, 0), \
                           -48466.2, 59387, 59387, -nan)
reports[-1].sigmaresid = ValErr(0.547259, 0.00158793, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000441389, None, 1.08026e-06, None, -0.000491567, None, 2.94707e-06, None, -0.000491567, None, 2.94707e-06, None, -0.000161297, None, 6.52998e-06, None, -0.000161297, None, 6.52998e-06, None, 0.547287, None, 0.00413504, None, 0.547287, None, 0.00413504, None)

reports.append(Report(604018264, ("CSC", 1, 1, 2, 11), "MEp12_11"))
reports[-1].posNum = 59548
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00176453, 0.00321583, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0389226, 0.0998089, 0), \
                           ValErr(0.000110849, 0.00212958, 0), \
                           ValErr(-0.00655222, 0.00710255, 0), \
                           ValErr(-7.55584e-05, 5.022e-05, 0), \
                           -47830.4, 59548, 59548, -nan)
reports[-1].sigmaresid = ValErr(0.540255, 0.00156549, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00444375, None, -2.47262e-05, None, 0.00224141, None, -3.25449e-06, None, 0.00224141, None, -3.25449e-06, None, 0.00268988, None, 5.82903e-06, None, 0.00268988, None, 5.82903e-06, None, 0.540273, None, 0.00421096, None, 0.540273, None, 0.00421096, None)

reports.append(Report(604018280, ("CSC", 1, 1, 2, 13), "MEp12_13"))
reports[-1].posNum = 57585
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00269543, 0.00345351, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0570785, 0.0978183, 0), \
                           ValErr(-0.00174425, 0.00208246, 0), \
                           ValErr(0.00696953, 0.00719759, 0), \
                           ValErr(6.5582e-06, 5.30073e-05, 0), \
                           -46126.8, 57585, 57585, -nan)
reports[-1].sigmaresid = ValErr(0.539066, 0.00158845, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00288971, None, 4.15956e-05, None, -0.00466676, None, 2.89581e-05, None, -0.00466676, None, 2.89581e-05, None, -0.00373019, None, 3.69325e-05, None, -0.00373019, None, 3.69325e-05, None, 0.539077, None, 0.00420766, None, 0.539077, None, 0.00420766, None)

reports.append(Report(604018296, ("CSC", 1, 1, 2, 15), "MEp12_15"))
reports[-1].posNum = 64458
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00514307, 0.00313589, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00267026, 0.0930913, 0), \
                           ValErr(-0.00223374, 0.00199666, 0), \
                           ValErr(0.00700632, 0.00676615, 0), \
                           ValErr(-8.87416e-06, 4.91257e-05, 0), \
                           -53147.4, 64458, 64458, -nan)
reports[-1].sigmaresid = ValErr(0.551887, 0.00153708, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00103975, None, -2.11459e-05, None, 0.00295849, None, -1.49243e-05, None, 0.00295849, None, -1.49243e-05, None, 0.0028777, None, -2.06798e-05, None, 0.0028777, None, -2.06798e-05, None, 0.551897, None, 0.00445543, None, 0.551897, None, 0.00445543, None)

reports.append(Report(604018312, ("CSC", 1, 1, 2, 17), "MEp12_17"))
reports[-1].posNum = 58052
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00268204, 0.00333408, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.300875, 0.0982813, 0), \
                           ValErr(0.00568744, 0.00208402, 0), \
                           ValErr(0.00118961, 0.00714151, 0), \
                           ValErr(-3.11823e-05, 5.138e-05, 0), \
                           -45839.2, 58052, 58052, -nan)
reports[-1].sigmaresid = ValErr(0.532957, 0.00156411, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00206544, None, 1.68476e-05, None, -0.00372114, None, 2.16656e-05, None, -0.00372114, None, 2.16656e-05, None, -0.00440451, None, 3.68185e-05, None, -0.00440451, None, 3.68185e-05, None, 0.533022, None, 0.00429103, None, 0.533022, None, 0.00429103, None)

reports.append(Report(604018328, ("CSC", 1, 1, 2, 19), "MEp12_19"))
reports[-1].posNum = 65529
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0110456, 0.00319963, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0837748, 0.092405, 0), \
                           ValErr(-0.00191219, 0.00198082, 0), \
                           ValErr(-0.0164935, 0.00678666, 0), \
                           ValErr(9.02205e-05, 4.98814e-05, 0), \
                           -54564.3, 65529, 65529, -nan)
reports[-1].sigmaresid = ValErr(0.556401, 0.00153694, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00327467, None, 5.97687e-06, None, -0.00471122, None, -1.34676e-05, None, -0.00471122, None, -1.34676e-05, None, -0.00407984, None, -1.48757e-05, None, -0.00407984, None, -1.48757e-05, None, 0.55644, None, 0.00427437, None, 0.55644, None, 0.00427437, None)

reports.append(Report(604018344, ("CSC", 1, 1, 2, 21), "MEp12_21"))
reports[-1].posNum = 57336
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00222064, 0.00333653, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.106626, 0.0993089, 0), \
                           ValErr(0.000634431, 0.00205782, 0), \
                           ValErr(0.0161851, 0.00719522, 0), \
                           ValErr(8.04316e-06, 5.10765e-05, 0), \
                           -44666.3, 57336, 57336, -nan)
reports[-1].sigmaresid = ValErr(0.527339, 0.00155726, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00146779, None, 4.55341e-07, None, -0.00215315, None, -2.10914e-06, None, -0.00215315, None, -2.10914e-06, None, -0.000633029, None, 1.12946e-05, None, -0.000633029, None, 1.12946e-05, None, 0.527371, None, 0.0040601, None, 0.527371, None, 0.0040601, None)

reports.append(Report(604018360, ("CSC", 1, 1, 2, 23), "MEp12_23"))
reports[-1].posNum = 64539
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00459322, 0.00314309, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.171207, 0.0935912, 0), \
                           ValErr(-0.00393954, 0.00200288, 0), \
                           ValErr(0.00452245, 0.00681344, 0), \
                           ValErr(3.45698e-05, 4.91218e-05, 0), \
                           -52913.7, 64539, 64539, -nan)
reports[-1].sigmaresid = ValErr(0.549324, 0.00152898, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0080041, None, 6.28946e-06, None, -0.00537074, None, -5.24299e-07, None, -0.00537074, None, -5.24299e-07, None, -0.00584331, None, 1.21239e-05, None, -0.00584331, None, 1.21239e-05, None, 0.549357, None, 0.00423487, None, 0.549357, None, 0.00423487, None)

reports.append(Report(604018376, ("CSC", 1, 1, 2, 25), "MEp12_25"))
reports[-1].posNum = 58386
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00144778, 0.00340966, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.128472, 0.0969004, 0), \
                           ValErr(0.00141252, 0.00206794, 0), \
                           ValErr(0.00339436, 0.0071182, 0), \
                           ValErr(-5.59857e-05, 5.24355e-05, 0), \
                           -46980.5, 58386, 58386, -nan)
reports[-1].sigmaresid = ValErr(0.541027, 0.00158325, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00329264, None, 1.3817e-05, None, -0.00349888, None, 9.03512e-06, None, -0.00349888, None, 9.03512e-06, None, -0.00458869, None, 2.94169e-05, None, -0.00458869, None, 2.94169e-05, None, 0.541045, None, 0.00429371, None, 0.541045, None, 0.00429371, None)

reports.append(Report(604018392, ("CSC", 1, 1, 2, 27), "MEp12_27"))
reports[-1].posNum = 59747
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00294068, 0.00329186, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0024084, 0.0976469, 0), \
                           ValErr(0.000157257, 0.00206475, 0), \
                           ValErr(-0.00621067, 0.00709061, 0), \
                           ValErr(7.09521e-06, 5.09118e-05, 0), \
                           -48641.9, 59747, 59747, -nan)
reports[-1].sigmaresid = ValErr(0.54618, 0.00158002, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00121287, None, -2.37701e-06, None, -0.00102118, None, -8.49831e-06, None, -0.00102118, None, -8.49831e-06, None, 0.000222383, None, -1.3552e-05, None, 0.000222383, None, -1.3552e-05, None, 0.546184, None, 0.00412175, None, 0.546184, None, 0.00412175, None)

reports.append(Report(604018408, ("CSC", 1, 1, 2, 29), "MEp12_29"))
reports[-1].posNum = 61191
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00563142, 0.00321614, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0674307, 0.0964687, 0), \
                           ValErr(-0.00189136, 0.00206572, 0), \
                           ValErr(0.0146854, 0.00692286, 0), \
                           ValErr(-5.12604e-05, 5.02737e-05, 0), \
                           -49653.1, 61191, 61191, -nan)
reports[-1].sigmaresid = ValErr(0.544713, 0.00155707, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000151553, None, 2.59666e-06, None, 0.000618592, None, 6.05019e-06, None, 0.000618592, None, 6.05019e-06, None, -0.000285788, None, -7.40451e-06, None, -0.000285788, None, -7.40451e-06, None, 0.54474, None, 0.00444984, None, 0.54474, None, 0.00444984, None)

reports.append(Report(604018424, ("CSC", 1, 1, 2, 31), "MEp12_31"))
reports[-1].posNum = 59647
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00372578, 0.00343692, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0255524, 0.0953733, 0), \
                           ValErr(-0.00165676, 0.00204012, 0), \
                           ValErr(-0.0042483, 0.00708989, 0), \
                           ValErr(4.48926e-05, 5.25981e-05, 0), \
                           -48736.6, 59647, 59647, -nan)
reports[-1].sigmaresid = ValErr(0.547795, 0.00158602, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00064343, None, -8.37543e-06, None, -0.00159949, None, 1.52435e-05, None, -0.00159949, None, 1.52435e-05, None, -0.0041923, None, 1.44509e-05, None, -0.0041923, None, 1.44509e-05, None, 0.547803, None, 0.00410057, None, 0.547803, None, 0.00410057, None)

reports.append(Report(604018440, ("CSC", 1, 1, 2, 33), "MEp12_33"))
reports[-1].posNum = 64035
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00325209, 0.00312324, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0828242, 0.0919799, 0), \
                           ValErr(-0.00304197, 0.00197177, 0), \
                           ValErr(-0.00535039, 0.00665729, 0), \
                           ValErr(9.44311e-05, 4.87122e-05, 0), \
                           -51939.9, 64035, 64035, -nan)
reports[-1].sigmaresid = ValErr(0.544534, 0.0015216, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00100637, None, -1.48736e-05, None, -0.000205747, None, -1.58861e-05, None, -0.000205747, None, -1.58861e-05, None, -0.00432583, None, 5.91724e-06, None, -0.00432583, None, 5.91724e-06, None, 0.544565, None, 0.00428261, None, 0.544565, None, 0.00428261, None)

reports.append(Report(604018456, ("CSC", 1, 1, 2, 35), "MEp12_35"))
reports[-1].posNum = 57078
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00495126, 0.00337538, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.080278, 0.0996073, 0), \
                           ValErr(0.000453787, 0.00211061, 0), \
                           ValErr(0.0038985, 0.00725198, 0), \
                           ValErr(-4.92858e-05, 5.1648e-05, 0), \
                           -44356.6, 57078, 57078, -nan)
reports[-1].sigmaresid = ValErr(0.526335, 0.0015578, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00397152, None, -1.56219e-05, None, 0.00276724, None, -1.81307e-05, None, 0.00276724, None, -1.81307e-05, None, -5.29128e-05, None, -1.38609e-05, None, -5.29128e-05, None, -1.38609e-05, None, 0.526343, None, 0.00414201, None, 0.526343, None, 0.00414201, None)

reports.append(Report(604018192, ("CSC", 1, 1, 2, 2), "MEp12_02"))
reports[-1].posNum = 58131
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0020201, 0.00315956, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0310975, 0.0916755, 0), \
                           ValErr(-0.00168404, 0.00190456, 0), \
                           ValErr(-0.0181021, 0.00656266, 0), \
                           ValErr(-4.3601e-05, 4.87281e-05, 0), \
                           -44558.6, 58131, 58131, -nan)
reports[-1].sigmaresid = ValErr(0.520784, 0.00152735, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00441829, None, -3.13585e-05, None, 0.00248627, None, -9.48178e-06, None, 0.00248627, None, -9.48178e-06, None, -0.00250488, None, -9.18892e-06, None, -0.00250488, None, -9.18892e-06, None, 0.520834, None, 0.00387067, None, 0.520834, None, 0.00387067, None)

reports.append(Report(604018208, ("CSC", 1, 1, 2, 4), "MEp12_04"))
reports[-1].posNum = 56393
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000995587, 0.00325681, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0330092, 0.0954887, 0), \
                           ValErr(-0.00053362, 0.00193745, 0), \
                           ValErr(0.0050521, 0.00686377, 0), \
                           ValErr(5.42221e-05, 4.94299e-05, 0), \
                           -43488.3, 56393, 56393, -nan)
reports[-1].sigmaresid = ValErr(0.523209, 0.00155793, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00162539, None, -2.93208e-06, None, 0.000597941, None, -2.42037e-05, None, 0.000597941, None, -2.42037e-05, None, -0.000127081, None, -7.29385e-06, None, -0.000127081, None, -7.29385e-06, None, 0.52322, None, 0.00393836, None, 0.52322, None, 0.00393836, None)

reports.append(Report(604018224, ("CSC", 1, 1, 2, 6), "MEp12_06"))
reports[-1].posNum = 61506
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00269839, 0.00307016, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00128294, 0.0868151, 0), \
                           ValErr(-0.00300708, 0.00183056, 0), \
                           ValErr(-0.010435, 0.00630912, 0), \
                           ValErr(-1.98566e-05, 4.74536e-05, 0), \
                           -47360.7, 61506, 61506, -nan)
reports[-1].sigmaresid = ValErr(0.522609, 0.00149006, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00223032, None, -1.39559e-05, None, 0.000107335, None, -1.85851e-05, None, 0.000107335, None, -1.85851e-05, None, -0.0034566, None, 9.23625e-07, None, -0.0034566, None, 9.23625e-07, None, 0.522636, None, 0.00407328, None, 0.522636, None, 0.00407328, None)

reports.append(Report(604018240, ("CSC", 1, 1, 2, 8), "MEp12_08"))
reports[-1].posNum = 54514
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000273591, 0.00331572, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0672059, 0.0921463, 0), \
                           ValErr(-0.00268511, 0.00190315, 0), \
                           ValErr(0.00194142, 0.00674213, 0), \
                           ValErr(-1.01569e-05, 4.98673e-05, 0), \
                           -40097.5, 54514, 54514, -nan)
reports[-1].sigmaresid = ValErr(0.504899, 0.00152909, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00149611, None, 3.80349e-06, None, -0.000507713, None, -1.23169e-05, None, -0.000507713, None, -1.23169e-05, None, -0.0028318, None, 2.59028e-05, None, -0.0028318, None, 2.59028e-05, None, 0.504916, None, 0.00666535, None, 0.504916, None, 0.00666535, None)

reports.append(Report(604018256, ("CSC", 1, 1, 2, 10), "MEp12_10"))
reports[-1].posNum = 64259
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00436279, 0.00305986, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0237729, 0.0873133, 0), \
                           ValErr(-0.00194573, 0.00185342, 0), \
                           ValErr(0.00274319, 0.00638489, 0), \
                           ValErr(-4.64719e-06, 4.7412e-05, 0), \
                           -50790.1, 64259, 64259, -nan)
reports[-1].sigmaresid = ValErr(0.533369, 0.00148781, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00374682, None, -1.59567e-05, None, 0.00345936, None, -2.58814e-05, None, 0.00345936, None, -2.58814e-05, None, 0.00666002, None, -2.84144e-05, None, 0.00666002, None, -2.84144e-05, None, 0.533375, None, 0.00400182, None, 0.533375, None, 0.00400182, None)

reports.append(Report(604018272, ("CSC", 1, 1, 2, 12), "MEp12_12"))
reports[-1].posNum = 54620
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00311074, 0.00324791, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.296037, 0.0906702, 0), \
                           ValErr(0.00051586, 0.00187077, 0), \
                           ValErr(-0.00173059, 0.00662427, 0), \
                           ValErr(-1.55151e-05, 4.89452e-05, 0), \
                           -40344.2, 54620, 54620, -nan)
reports[-1].sigmaresid = ValErr(0.506461, 0.00153233, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00276557, None, -1.53696e-05, None, 0.00313722, None, -1.75224e-05, None, 0.00313722, None, -1.75224e-05, None, 0.00177683, None, -5.25613e-06, None, 0.00177683, None, -5.25613e-06, None, 0.506514, None, 0.00423599, None, 0.506514, None, 0.00423599, None)

reports.append(Report(604018288, ("CSC", 1, 1, 2, 14), "MEp12_14"))
reports[-1].posNum = 62533
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00557392, 0.00308178, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0650321, 0.0859975, 0), \
                           ValErr(0.000246388, 0.00183412, 0), \
                           ValErr(0.00422179, 0.00630323, 0), \
                           ValErr(3.95384e-05, 4.75051e-05, 0), \
                           -48445.6, 62533, 62533, -nan)
reports[-1].sigmaresid = ValErr(0.525073, 0.00148474, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00746045, None, 1.88884e-05, None, -0.00619568, None, 2.53818e-05, None, -0.00619568, None, 2.53818e-05, None, -0.00702193, None, 1.06951e-05, None, -0.00702193, None, 1.06951e-05, None, 0.525082, None, 0.00414382, None, 0.525082, None, 0.00414382, None)

reports.append(Report(604018304, ("CSC", 1, 1, 2, 16), "MEp12_16"))
reports[-1].posNum = 56109
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(1.73844e-05, 0.00322641, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0736974, 0.0954594, 0), \
                           ValErr(-0.00191939, 0.00195151, 0), \
                           ValErr(0.00266965, 0.00682606, 0), \
                           ValErr(4.52602e-05, 4.8862e-05, 0), \
                           -42553.1, 56109, 56109, -nan)
reports[-1].sigmaresid = ValErr(0.516573, 0.00154206, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(8.48e-05, None, -5.6222e-06, None, 0.000174188, None, -2.64253e-05, None, 0.000174188, None, -2.64253e-05, None, 0.00152436, None, 2.73402e-06, None, 0.00152436, None, 2.73402e-06, None, 0.516589, None, 0.00432452, None, 0.516589, None, 0.00432452, None)

reports.append(Report(604018320, ("CSC", 1, 1, 2, 18), "MEp12_18"))
reports[-1].posNum = 58397
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00661272, 0.00319239, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0369875, 0.0901071, 0), \
                           ValErr(-0.00205452, 0.00185594, 0), \
                           ValErr(0.0138748, 0.00652525, 0), \
                           ValErr(3.37483e-05, 4.86262e-05, 0), \
                           -45483.3, 58397, 58397, -nan)
reports[-1].sigmaresid = ValErr(0.527253, 0.0015428, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00425762, None, -6.45589e-06, None, 0.00307026, None, 9.37836e-06, None, 0.00307026, None, 9.37836e-06, None, 0.00216492, None, 9.29197e-06, None, 0.00216492, None, 9.29197e-06, None, 0.527287, None, 0.00456573, None, 0.527287, None, 0.00456573, None)

reports.append(Report(604018336, ("CSC", 1, 1, 2, 20), "MEp12_20"))
reports[-1].posNum = 58848
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000338383, 0.00318306, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0564322, 0.0905808, 0), \
                           ValErr(-0.00186582, 0.00190376, 0), \
                           ValErr(-0.00562599, 0.00653554, 0), \
                           ValErr(-3.89449e-05, 4.90973e-05, 0), \
                           -45510.7, 58848, 58848, -nan)
reports[-1].sigmaresid = ValErr(0.52436, 0.00152844, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00173134, None, 1.34519e-05, None, 0.00125098, None, -5.08999e-06, None, 0.00125098, None, -5.08999e-06, None, 0.00298219, None, 1.25373e-05, None, 0.00298219, None, 1.25373e-05, None, 0.524374, None, 0.00422353, None, 0.524374, None, 0.00422353, None)

reports.append(Report(604018352, ("CSC", 1, 1, 2, 22), "MEp12_22"))
reports[-1].posNum = 57026
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00223898, 0.00324182, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.16105, 0.0929258, 0), \
                           ValErr(-0.00173826, 0.00192202, 0), \
                           ValErr(-0.00375457, 0.00672713, 0), \
                           ValErr(-1.43172e-05, 4.94223e-05, 0), \
                           -43598.1, 57026, 57026, -nan)
reports[-1].sigmaresid = ValErr(0.519749, 0.00153901, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.002576, None, -1.90627e-05, None, 0.00297563, None, 2.63326e-08, None, 0.00297563, None, 2.63326e-08, None, 0.00208348, None, -8.37108e-06, None, 0.00208348, None, -8.37108e-06, None, 0.519767, None, 0.00413827, None, 0.519767, None, 0.00413827, None)

reports.append(Report(604018368, ("CSC", 1, 1, 2, 24), "MEp12_24"))
reports[-1].posNum = 62313
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00113427, 0.00303031, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0842457, 0.0858694, 0), \
                           ValErr(0.000479978, 0.00182862, 0), \
                           ValErr(-0.00739126, 0.00623559, 0), \
                           ValErr(2.18224e-05, 4.72392e-05, 0), \
                           -47950.3, 62313, 62313, -nan)
reports[-1].sigmaresid = ValErr(0.522343, 0.00147962, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00241652, None, -2.00934e-06, None, 0.00140177, None, -3.76129e-06, None, 0.00140177, None, -3.76129e-06, None, 0.00231533, None, 4.83567e-06, None, 0.00231533, None, 4.83567e-06, None, 0.522353, None, 0.00396491, None, 0.522353, None, 0.00396491, None)

reports.append(Report(604018384, ("CSC", 1, 1, 2, 26), "MEp12_26"))
reports[-1].posNum = 55157
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00185734, 0.00327178, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0557436, 0.0903013, 0), \
                           ValErr(-0.00102296, 0.00185544, 0), \
                           ValErr(-0.00530284, 0.00664065, 0), \
                           ValErr(9.80347e-05, 4.90231e-05, 0), \
                           -40412.5, 55157, 55157, -nan)
reports[-1].sigmaresid = ValErr(0.503458, 0.00151582, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00323865, None, -1.28987e-05, None, 0.00184748, None, -2.04565e-05, None, 0.00184748, None, -2.04565e-05, None, 0.00329929, None, -1.95729e-05, None, 0.00329929, None, -1.95729e-05, None, 0.503478, None, 0.00403172, None, 0.503478, None, 0.00403172, None)

reports.append(Report(604018400, ("CSC", 1, 1, 2, 28), "MEp12_28"))
reports[-1].posNum = 63770
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00515564, 0.00306999, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.174448, 0.0874587, 0), \
                           ValErr(0.000182904, 0.00182638, 0), \
                           ValErr(-0.0106227, 0.00633513, 0), \
                           ValErr(6.21111e-05, 4.49049e-05, 0), \
                           -50289.1, 63770, 63770, -nan)
reports[-1].sigmaresid = ValErr(0.532412, 0.00147858, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000806527, None, -5.71158e-09, None, -0.000933121, None, 8.94277e-06, None, -0.000933121, None, 8.94277e-06, None, -0.00421758, None, 3.72659e-05, None, -0.00421758, None, 3.72659e-05, None, 0.532445, None, 0.00395271, None, 0.532445, None, 0.00395271, None)

reports.append(Report(604018416, ("CSC", 1, 1, 2, 30), "MEp12_30"))
reports[-1].posNum = 54430
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000946382, 0.00325817, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0815331, 0.0900714, 0), \
                           ValErr(-0.00207222, 0.00182969, 0), \
                           ValErr(0.0129619, 0.0065672, 0), \
                           ValErr(-2.00552e-05, 4.86404e-05, 0), \
                           -39543.5, 54430, 54430, -nan)
reports[-1].sigmaresid = ValErr(0.500357, 0.00151652, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00254463, None, -4.21948e-06, None, -0.00338767, None, -1.13619e-05, None, -0.00338767, None, -1.13619e-05, None, -0.00462872, None, 4.75409e-06, None, -0.00462872, None, 4.75409e-06, None, 0.500385, None, 0.00401548, None, 0.500385, None, 0.00401548, None)

reports.append(Report(604018432, ("CSC", 1, 1, 2, 32), "MEp12_32"))
reports[-1].posNum = 62275
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00157733, 0.00307578, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.105612, 0.0863053, 0), \
                           ValErr(-0.00319414, 0.00184708, 0), \
                           ValErr(-0.00423065, 0.00629625, 0), \
                           ValErr(2.13459e-05, 4.76396e-05, 0), \
                           -48070, 62275, 62275, -nan)
reports[-1].sigmaresid = ValErr(0.523593, 0.00148362, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000511303, None, 5.76427e-06, None, 0.000133597, None, -9.23431e-06, None, 0.000133597, None, -9.23431e-06, None, -0.00197365, None, -2.40026e-06, None, -0.00197365, None, -2.40026e-06, None, 0.523618, None, 0.00412596, None, 0.523618, None, 0.00412596, None)

reports.append(Report(604018448, ("CSC", 1, 1, 2, 34), "MEp12_34"))
reports[-1].posNum = 57782
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00670208, 0.00319207, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0203967, 0.0933808, 0), \
                           ValErr(-0.000658185, 0.00194058, 0), \
                           ValErr(0.0103255, 0.00670376, 0), \
                           ValErr(-4.00818e-05, 4.88419e-05, 0), \
                           -44413.5, 57782, 57782, -nan)
reports[-1].sigmaresid = ValErr(0.521891, 0.00153522, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00416533, None, -9.63289e-06, None, 0.00292197, None, -2.31538e-05, None, 0.00292197, None, -2.31538e-05, None, 0.00347962, None, -1.25885e-05, None, 0.00347962, None, -1.25885e-05, None, 0.521903, None, 0.00405295, None, 0.521903, None, 0.00405295, None)

reports.append(Report(604018464, ("CSC", 1, 1, 2, 36), "MEp12_36"))
reports[-1].posNum = 60143
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00382244, 0.00314837, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.173913, 0.088085, 0), \
                           ValErr(-0.00350927, 0.00183738, 0), \
                           ValErr(-0.00778193, 0.00640883, 0), \
                           ValErr(8.09988e-06, 4.83444e-05, 0), \
                           -46838.5, 60143, 60143, -nan)
reports[-1].sigmaresid = ValErr(0.527212, 0.00152012, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0019993, None, 1.30805e-05, None, -0.00136861, None, 7.38115e-06, None, -0.00136861, None, 7.38115e-06, None, 0.00358079, None, -1.11755e-05, None, 0.00358079, None, -1.11755e-05, None, 0.527248, None, 0.00406881, None, 0.527248, None, 0.00406881, None)

reports.append(Report(604018696, ("CSC", 1, 1, 3, 1), "MEp13_01"))
reports[-1].posNum = 26676
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00169211, 0.0135684, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.77808, 0.266387, 0), \
                           ValErr(0.00333847, 0.00594, 0), \
                           ValErr(0.008899, 0.0129123, 0), \
                           ValErr(-6.99148e-05, 0.00010475, 0), \
                           -48927.5, 26676, 26676, -nan)
reports[-1].sigmaresid = ValErr(1.51468, 0.00644931, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0167272, None, -8.05289e-06, None, -0.0051628, None, -1.77951e-05, None, -0.0051628, None, -1.77951e-05, None, -0.0171232, None, 1.90096e-05, None, -0.0171232, None, 1.90096e-05, None, 1.51777, None, 0.00639602, None, 1.51777, None, 0.00639602, None)

reports.append(Report(604018704, ("CSC", 1, 1, 3, 2), "MEp13_02"))
reports[-1].posNum = 26318
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00245681, 0.0136606, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.40516, 0.271955, 0), \
                           ValErr(-0.00998245, 0.00613668, 0), \
                           ValErr(-0.00609395, 0.0134025, 0), \
                           ValErr(-0.000152091, 0.000214864, 0), \
                           -48092.5, 26318, 26318, -nan)
reports[-1].sigmaresid = ValErr(1.50444, 0.00656365, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00772009, None, -1.8124e-05, None, 0.00109762, None, -5.33313e-05, None, 0.00109762, None, -5.33313e-05, None, 0.000140253, None, 8.75223e-06, None, 0.000140253, None, 8.75223e-06, None, 1.50674, None, 0.00669657, None, 1.50674, None, 0.00669657, None)

reports.append(Report(604018712, ("CSC", 1, 1, 3, 3), "MEp13_03"))
reports[-1].posNum = 24371
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00920237, 0.0139605, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.45591, 0.284735, 0), \
                           ValErr(-0.00614996, 0.0066625, 0), \
                           ValErr(-0.0204986, 0.0136345, 0), \
                           ValErr(8.3358e-05, 0.000229001, 0), \
                           -44609.2, 24371, 24371, -nan)
reports[-1].sigmaresid = ValErr(1.50906, 0.00683531, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0139727, None, -8.39239e-05, None, 0.00619368, None, -0.000119575, None, 0.00619368, None, -0.000119575, None, -0.00396662, None, -4.5418e-05, None, -0.00396662, None, -4.5418e-05, None, 1.51142, None, 0.00659358, None, 1.51142, None, 0.00659358, None)

reports.append(Report(604018720, ("CSC", 1, 1, 3, 4), "MEp13_04"))
reports[-1].posNum = 24711
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.035652, 0.013954, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.01382, 0.297087, 0), \
                           ValErr(-0.0129346, 0.00690274, 0), \
                           ValErr(0.0113835, 0.0139826, 0), \
                           ValErr(0.000118934, 0.000169516, 0), \
                           -45884.5, 24711, 24711, -nan)
reports[-1].sigmaresid = ValErr(1.54948, 0.0059536, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0356919, None, -7.28698e-05, None, 0.0298352, None, -8.8219e-05, None, 0.0298352, None, -8.8219e-05, None, 0.0234554, None, -3.1952e-05, None, 0.0234554, None, -3.1952e-05, None, 1.5527, None, 0.0072679, None, 1.5527, None, 0.0072679, None)

reports.append(Report(604018728, ("CSC", 1, 1, 3, 5), "MEp13_05"))
reports[-1].posNum = 27236
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0109773, 0.0128144, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.77359, 0.258651, 0), \
                           ValErr(-0.0146432, 0.00333751, 0), \
                           ValErr(0.00930993, 0.0123121, 0), \
                           ValErr(0.000215443, 0.00011708, 0), \
                           -49389.5, 27236, 27236, -nan)
reports[-1].sigmaresid = ValErr(1.48356, 0.00587123, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00650029, None, -1.96755e-05, None, 0.00484299, None, -5.82392e-05, None, 0.00484299, None, -5.82392e-05, None, -0.00383312, None, 3.23215e-05, None, -0.00383312, None, 3.23215e-05, None, 1.48677, None, 0.00660184, None, 1.48677, None, 0.00660184, None)

reports.append(Report(604018736, ("CSC", 1, 1, 3, 6), "MEp13_06"))
reports[-1].posNum = 27192
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0278685, 0.0133911, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.90687, 0.262675, 0), \
                           ValErr(-0.00112332, 0.00579708, 0), \
                           ValErr(0.00612729, 0.0127594, 0), \
                           ValErr(8.12651e-05, 0.000103532, 0), \
                           -49551.6, 27192, 27192, -nan)
reports[-1].sigmaresid = ValErr(1.49683, 0.00641101, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0102169, None, -7.43912e-05, None, 0.0236921, None, -0.000101008, None, 0.0236921, None, -0.000101008, None, 0.0146566, None, -8.42508e-05, None, 0.0146566, None, -8.42508e-05, None, 1.50019, None, 0.00647185, None, 1.50019, None, 0.00647185, None)

reports.append(Report(604018744, ("CSC", 1, 1, 3, 7), "MEp13_07"))
reports[-1].posNum = 25303
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0130798, 0.013755, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.96052, 0.275757, 0), \
                           ValErr(-0.00335116, 0.00636115, 0), \
                           ValErr(0.0038724, 0.013186, 0), \
                           ValErr(1.36202e-05, 0.000222388, 0), \
                           -46273, 25303, 25303, -nan)
reports[-1].sigmaresid = ValErr(1.50654, 0.00669876, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0155714, None, 3.18852e-05, None, -0.0179043, None, -2.1138e-05, None, -0.0179043, None, -2.1138e-05, None, -0.0113801, None, -1.98773e-05, None, -0.0113801, None, -1.98773e-05, None, 1.50998, None, 0.00662708, None, 1.50998, None, 0.00662708, None)

reports.append(Report(604018752, ("CSC", 1, 1, 3, 8), "MEp13_08"))
reports[-1].posNum = 24798
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00494328, 0.0141137, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.35777, 0.283216, 0), \
                           ValErr(0.0135583, 0.00657856, 0), \
                           ValErr(0.00740701, 0.0137676, 0), \
                           ValErr(0.000124341, 0.000228412, 0), \
                           -45553.8, 24798, 24798, -nan)
reports[-1].sigmaresid = ValErr(1.51901, 0.00682214, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0145686, None, -2.61579e-05, None, -0.000797662, None, -8.91941e-05, None, -0.000797662, None, -8.91941e-05, None, 0.00159547, None, 3.62318e-06, None, 0.00159547, None, 3.62318e-06, None, 1.52144, None, 0.00678059, None, 1.52144, None, 0.00678059, None)

reports.append(Report(604018760, ("CSC", 1, 1, 3, 9), "MEp13_09"))
reports[-1].posNum = 25085
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00279663, 0.0138472, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.69628, 0.279445, 0), \
                           ValErr(-0.0108797, 0.0059935, 0), \
                           ValErr(-0.0127529, 0.0134977, 0), \
                           ValErr(0.000566336, 0.00017083, 0), \
                           -45876.7, 25085, 25085, -nan)
reports[-1].sigmaresid = ValErr(1.50669, 0.00542186, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0192119, None, -4.53403e-05, None, 0.00942999, None, -0.000134746, None, 0.00942999, None, -0.000134746, None, 0.00972489, None, -0.000110186, None, 0.00972489, None, -0.000110186, None, 1.50974, None, 0.00651229, None, 1.50974, None, 0.00651229, None)

reports.append(Report(604018768, ("CSC", 1, 1, 3, 10), "MEp13_10"))
reports[-1].posNum = 27559
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00222979, 0.0131802, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.90877, 0.267744, 0), \
                           ValErr(-0.00255414, 0.00600349, 0), \
                           ValErr(-0.0190049, 0.01296, 0), \
                           ValErr(0.000268622, 9.88208e-05, 0), \
                           -50299.5, 27559, 27559, -nan)
reports[-1].sigmaresid = ValErr(1.50113, 0.00638992, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00869362, None, -5.21574e-05, None, 0.0134661, None, -0.000140763, None, 0.0134661, None, -0.000140763, None, 0.0219016, None, -0.000148491, None, 0.0219016, None, -0.000148491, None, 1.5044, None, 0.00656075, None, 1.5044, None, 0.00656075, None)

reports.append(Report(604018776, ("CSC", 1, 1, 3, 11), "MEp13_11"))
reports[-1].posNum = 25395
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0275964, 0.0140983, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.41673, 0.281837, 0), \
                           ValErr(-0.00647749, 0.00641319, 0), \
                           ValErr(-0.0202961, 0.0137566, 0), \
                           ValErr(0.000109526, 0.000223789, 0), \
                           -46888.8, 25395, 25395, -nan)
reports[-1].sigmaresid = ValErr(1.53333, 0.00680371, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00523248, None, 1.01789e-05, None, -0.0143944, None, -2.7688e-05, None, -0.0143944, None, -2.7688e-05, None, -0.0117853, None, 7.83841e-05, None, -0.0117853, None, 7.83841e-05, None, 1.53558, None, 0.00668848, None, 1.53558, None, 0.00668848, None)

reports.append(Report(604018784, ("CSC", 1, 1, 3, 12), "MEp13_12"))
reports[-1].posNum = 24643
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00608362, 0.0142041, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.64565, 0.280893, 0), \
                           ValErr(-0.00109009, 0.00652075, 0), \
                           ValErr(0.000808749, 0.0136227, 0), \
                           ValErr(-0.000162002, 0.000230966, 0), \
                           -45401, 24643, 24643, -nan)
reports[-1].sigmaresid = ValErr(1.52716, 0.00688019, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(7.77403e-05, None, -3.67539e-06, None, 0.00490324, None, -7.36404e-05, None, 0.00490324, None, -7.36404e-05, None, 0.000847453, None, -3.82319e-05, None, 0.000847453, None, -3.82319e-05, None, 1.52996, None, 0.0067656, None, 1.52996, None, 0.0067656, None)

reports.append(Report(604018792, ("CSC", 1, 1, 3, 13), "MEp13_13"))
reports[-1].posNum = 24146
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00879044, 0.0141852, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.84792, 0.281513, 0), \
                           ValErr(-0.00235587, 0.00651375, 0), \
                           ValErr(0.0175956, 0.013588, 0), \
                           ValErr(-2.79586e-05, 0.000229693, 0), \
                           -44213.2, 24146, 24146, -nan)
reports[-1].sigmaresid = ValErr(1.51005, 0.00687161, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0175967, None, -3.16366e-05, None, -0.00212346, None, -1.04303e-05, None, -0.00212346, None, -1.04303e-05, None, -0.00194636, None, 2.43721e-05, None, -0.00194636, None, 2.43721e-05, None, 1.5133, None, 0.00716082, None, 1.5133, None, 0.00716082, None)

reports.append(Report(604018800, ("CSC", 1, 1, 3, 14), "MEp13_14"))
reports[-1].posNum = 26994
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0226759, 0.013642, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.51689, 0.269515, 0), \
                           ValErr(0.000654638, 0.0059634, 0), \
                           ValErr(0.0195559, 0.0133569, 0), \
                           ValErr(-0.00027479, 0.000107381, 0), \
                           -49502.8, 26994, 26994, -nan)
reports[-1].sigmaresid = ValErr(1.51423, 0.00649513, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00848092, None, -7.48921e-06, None, 0.00734489, None, -3.57699e-05, None, 0.00734489, None, -3.57699e-05, None, -0.0141359, None, 3.88418e-05, None, -0.0141359, None, 3.88418e-05, None, 1.51675, None, 0.00675084, None, 1.51675, None, 0.00675084, None)

reports.append(Report(604018808, ("CSC", 1, 1, 3, 15), "MEp13_15"))
reports[-1].posNum = 26651
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0112832, 0.0135121, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.45867, 0.269129, 0), \
                           ValErr(-0.0112527, 0.00607643, 0), \
                           ValErr(-0.00887428, 0.0131897, 0), \
                           ValErr(-8.23695e-05, 0.000210873, 0), \
                           -48599.2, 26651, 26651, -nan)
reports[-1].sigmaresid = ValErr(1.49872, 0.0064916, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00792584, None, -5.3792e-05, None, 0.0166441, None, -9.84931e-05, None, 0.0166441, None, -9.84931e-05, None, 0.00944073, None, 7.17308e-07, None, 0.00944073, None, 7.17308e-07, None, 1.50115, None, 0.00632169, None, 1.50115, None, 0.00632169, None)

reports.append(Report(604018816, ("CSC", 1, 1, 3, 16), "MEp13_16"))
reports[-1].posNum = 24442
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.010161, 0.0141098, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.77014, 0.291308, 0), \
                           ValErr(-0.0063983, 0.00672984, 0), \
                           ValErr(-0.0313374, 0.0137745, 0), \
                           ValErr(0.000502232, 0.000138676, 0), \
                           -45023.9, 24442, 24442, -nan)
reports[-1].sigmaresid = ValErr(1.52675, 0.00621238, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00774339, None, 1.21006e-06, None, 0.0136805, None, -7.51574e-05, None, 0.0136805, None, -7.51574e-05, None, 0.00749675, None, -4.42819e-05, None, 0.00749675, None, -4.42819e-05, None, 1.52984, None, 0.00639462, None, 1.52984, None, 0.00639462, None)

reports.append(Report(604018824, ("CSC", 1, 1, 3, 17), "MEp13_17"))
reports[-1].posNum = 24176
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00565294, 0.0141717, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.88658, 0.289057, 0), \
                           ValErr(-0.00384907, 0.006775, 0), \
                           ValErr(0.0051676, 0.0139263, 0), \
                           ValErr(-0.000169116, 0.000233353, 0), \
                           -44425.1, 24176, 24176, -nan)
reports[-1].sigmaresid = ValErr(1.51988, 0.00691197, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00961202, None, 3.15605e-05, None, -0.0103834, None, -7.2702e-05, None, -0.0103834, None, -7.2702e-05, None, 0.0073838, None, -8.29029e-05, None, 0.0073838, None, -8.29029e-05, None, 1.52305, None, 0.00740864, None, 1.52305, None, 0.00740864, None)

reports.append(Report(604018832, ("CSC", 1, 1, 3, 18), "MEp13_18"))
reports[-1].posNum = 25620
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0159196, 0.0136871, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.41367, 0.26735, 0), \
                           ValErr(-0.0129213, 0.00569352, 0), \
                           ValErr(0.01007, 0.0131306, 0), \
                           ValErr(-7.12531e-05, 0.000140221, 0), \
                           -46642.7, 25620, 25620, -nan)
reports[-1].sigmaresid = ValErr(1.49425, 0.00613733, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00949194, None, -2.31349e-05, None, 0.00881346, None, -5.69374e-05, None, 0.00881346, None, -5.69374e-05, None, -0.00225531, None, -1.29895e-05, None, -0.00225531, None, -1.29895e-05, None, 1.49672, None, 0.00668588, None, 1.49672, None, 0.00668588, None)

reports.append(Report(604018840, ("CSC", 1, 1, 3, 19), "MEp13_19"))
reports[-1].posNum = 27227
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00303241, 0.0134432, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.90966, 0.266967, 0), \
                           ValErr(-0.00739442, 0.0060492, 0), \
                           ValErr(-0.00478185, 0.0129924, 0), \
                           ValErr(0.000162565, 0.00021091, 0), \
                           -49906.7, 27227, 27227, -nan)
reports[-1].sigmaresid = ValErr(1.51294, 0.00648356, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00678005, None, -2.39565e-05, None, 0.00712917, None, -0.000114609, None, 0.00712917, None, -0.000114609, None, 0.0172199, None, -0.000142492, None, 0.0172199, None, -0.000142492, None, 1.51627, None, 0.00666973, None, 1.51627, None, 0.00666973, None)

reports.append(Report(604018848, ("CSC", 1, 1, 3, 20), "MEp13_20"))
reports[-1].posNum = 26170
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00297513, 0.0137545, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.60872, 0.270676, 0), \
                           ValErr(0.00223441, 0.00617408, 0), \
                           ValErr(-0.00592187, 0.0133888, 0), \
                           ValErr(-0.000339187, 0.000216553, 0), \
                           -47752.5, 26170, 26170, -nan)
reports[-1].sigmaresid = ValErr(1.50045, 0.00655849, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.009474, None, -4.05589e-05, None, 0.00559795, None, -2.17031e-05, None, 0.00559795, None, -2.17031e-05, None, 0.018589, None, -1.62418e-05, None, 0.018589, None, -1.62418e-05, None, 1.50321, None, 0.00647685, None, 1.50321, None, 0.00647685, None)

reports.append(Report(604018856, ("CSC", 1, 1, 3, 21), "MEp13_21"))
reports[-1].posNum = 24096
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00354531, 0.0141734, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.21455, 0.289999, 0), \
                           ValErr(0.000149584, 0.00681745, 0), \
                           ValErr(0.0040834, 0.0138401, 0), \
                           ValErr(-0.000211597, 0.000233792, 0), \
                           -44311, 24096, 24096, -nan)
reports[-1].sigmaresid = ValErr(1.52196, 0.00693291, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00511165, None, 4.01938e-05, None, -0.0068018, None, -2.18958e-05, None, -0.0068018, None, -2.18958e-05, None, 0.00731114, None, -4.75075e-05, None, 0.00731114, None, -4.75075e-05, None, 1.52387, None, 0.00663067, None, 1.52387, None, 0.00663067, None)

reports.append(Report(604018864, ("CSC", 1, 1, 3, 22), "MEp13_22"))
reports[-1].posNum = 24907
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0125421, 0.0140557, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.68316, 0.290671, 0), \
                           ValErr(-0.00502861, 0.00664747, 0), \
                           ValErr(-0.00230008, 0.0139914, 0), \
                           ValErr(6.80443e-05, 0.000138712, 0), \
                           -46051.8, 24907, 24907, -nan)
reports[-1].sigmaresid = ValErr(1.53728, 0.00643739, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00532324, None, 1.00883e-05, None, -0.0087456, None, -5.30699e-05, None, -0.0087456, None, -5.30699e-05, None, -0.00801309, None, -9.62672e-06, None, -0.00801309, None, -9.62672e-06, None, 1.53989, None, 0.00672631, None, 1.53989, None, 0.00672631, None)

reports.append(Report(604018872, ("CSC", 1, 1, 3, 23), "MEp13_23"))
reports[-1].posNum = 27291
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0124664, 0.0133126, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.50727, 0.258072, 0), \
                           ValErr(-0.0106458, 0.00572216, 0), \
                           ValErr(-0.0072197, 0.013074, 0), \
                           ValErr(0.000314528, 0.000138384, 0), \
                           -49898.1, 27291, 27291, -nan)
reports[-1].sigmaresid = ValErr(1.50597, 0.00622947, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00039075, None, -3.68239e-05, None, -0.00623326, None, -7.50541e-05, None, -0.00623326, None, -7.50541e-05, None, -0.0255734, None, 5.02509e-06, None, -0.0255734, None, 5.02509e-06, None, 1.50849, None, 0.0068075, None, 1.50849, None, 0.0068075, None)

reports.append(Report(604018880, ("CSC", 1, 1, 3, 24), "MEp13_24"))
reports[-1].posNum = 26692
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0111704, 0.013268, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.93326, 0.263315, 0), \
                           ValErr(0.0033038, 0.00596771, 0), \
                           ValErr(0.0142711, 0.012774, 0), \
                           ValErr(6.04441e-05, 9.73885e-05, 0), \
                           -48361.6, 26692, 26692, -nan)
reports[-1].sigmaresid = ValErr(1.48128, 0.00638226, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0029694, None, -4.00106e-05, None, 0.000150643, None, -6.62834e-05, None, 0.000150643, None, -6.62834e-05, None, 0.0101017, None, -7.55507e-05, None, 0.0101017, None, -7.55507e-05, None, 1.48475, None, 0.00663461, None, 1.48475, None, 0.00663461, None)

reports.append(Report(604018888, ("CSC", 1, 1, 3, 25), "MEp13_25"))
reports[-1].posNum = 24737
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00239437, 0.01389, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.48019, 0.275211, 0), \
                           ValErr(0.00108685, 0.00633988, 0), \
                           ValErr(0.0197072, 0.0132443, 0), \
                           ValErr(-0.000467966, 0.000145578, 0), \
                           -45171.9, 24737, 24737, -nan)
reports[-1].sigmaresid = ValErr(1.50253, 0.00579733, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0187786, None, 5.59258e-07, None, -0.0138992, None, -5.87078e-05, None, -0.0138992, None, -5.87078e-05, None, -0.0185942, None, 3.44413e-05, None, -0.0185942, None, 3.44413e-05, None, 1.5052, None, 0.00672772, None, 1.5052, None, 0.00672772, None)

reports.append(Report(604018896, ("CSC", 1, 1, 3, 26), "MEp13_26"))
reports[-1].posNum = 24629
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00715423, 0.014286, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.2835, 0.283828, 0), \
                           ValErr(-0.0140976, 0.0066295, 0), \
                           ValErr(0.0103666, 0.0138605, 0), \
                           ValErr(-0.00027437, 0.000230553, 0), \
                           -45342.1, 24629, 24629, -nan)
reports[-1].sigmaresid = ValErr(1.52511, 0.00687171, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000424718, None, -2.24853e-05, None, -0.000563578, None, -0.000127381, None, -0.000563578, None, -0.000127381, None, 0.0116481, None, -0.000155515, None, 0.0116481, None, -0.000155515, None, 1.52721, None, 0.00691938, None, 1.52721, None, 0.00691938, None)

reports.append(Report(604018904, ("CSC", 1, 1, 3, 27), "MEp13_27"))
reports[-1].posNum = 25147
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.015567, 0.0138252, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.54357, 0.275234, 0), \
                           ValErr(0.000698918, 0.00625058, 0), \
                           ValErr(0.0144855, 0.0133195, 0), \
                           ValErr(6.20223e-05, 0.000220347, 0), \
                           -45865.1, 25147, 25147, -nan)
reports[-1].sigmaresid = ValErr(1.49922, 0.00668511, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00182016, None, -4.79804e-05, None, 0.00421663, None, -0.000168794, None, 0.00421663, None, -0.000168794, None, 0.00687209, None, -6.22743e-05, None, 0.00687209, None, -6.22743e-05, None, 1.50183, None, 0.00672378, None, 1.50183, None, 0.00672378, None)

reports.append(Report(604018912, ("CSC", 1, 1, 3, 28), "MEp13_28"))
reports[-1].posNum = 26302
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00120257, 0.0135701, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.95791, 0.275205, 0), \
                           ValErr(-0.000982035, 0.00607544, 0), \
                           ValErr(0.0258973, 0.0132921, 0), \
                           ValErr(-7.44027e-05, 0.00010876, 0), \
                           -48148.8, 26302, 26302, -nan)
reports[-1].sigmaresid = ValErr(1.50934, 0.00657735, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0218387, None, 2.25327e-05, None, -0.0178579, None, -2.40403e-05, None, -0.0178579, None, -2.40403e-05, None, -0.00706264, None, -1.57549e-05, None, -0.00706264, None, -1.57549e-05, None, 1.5128, None, 0.00665393, None, 1.5128, None, 0.00665393, None)

reports.append(Report(604018920, ("CSC", 1, 1, 3, 29), "MEp13_29"))
reports[-1].posNum = 24930
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0504067, 0.0138826, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.24106, 0.274214, 0), \
                           ValErr(-0.0147283, 0.00539542, 0), \
                           ValErr(0.0278692, 0.0134658, 0), \
                           ValErr(-0.000383738, 0.00018162, 0), \
                           -45328.6, 24930, 24930, -nan)
reports[-1].sigmaresid = ValErr(1.49077, 0.00566652, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0308467, None, -7.37943e-05, None, 0.0257481, None, -0.000132068, None, 0.0257481, None, -0.000132068, None, 0.0384902, None, -0.000170659, None, 0.0384902, None, -0.000170659, None, 1.49316, None, 0.00677172, None, 1.49316, None, 0.00677172, None)

reports.append(Report(604018928, ("CSC", 1, 1, 3, 30), "MEp13_30"))
reports[-1].posNum = 24574
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00781001, 0.0139804, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.35402, 0.274445, 0), \
                           ValErr(-0.0126181, 0.00633289, 0), \
                           ValErr(-0.0226811, 0.0133486, 0), \
                           ValErr(7.18104e-05, 0.000107713, 0), \
                           -44891.8, 24574, 24574, -nan)
reports[-1].sigmaresid = ValErr(1.5036, 0.00658325, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0104252, None, -4.78909e-06, None, 0.0101468, None, -5.29223e-05, None, 0.0101468, None, -5.29223e-05, None, 0.0144717, None, -4.55606e-05, None, 0.0144717, None, -4.55606e-05, None, 1.50598, None, 0.00713663, None, 1.50598, None, 0.00713663, None)

reports.append(Report(604018936, ("CSC", 1, 1, 3, 31), "MEp13_31"))
reports[-1].posNum = 24842
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.018478, 0.0140561, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.14558, 0.275657, 0), \
                           ValErr(0.000175903, 0.0061442, 0), \
                           ValErr(-0.0319721, 0.0133943, 0), \
                           ValErr(0.000172563, 0.000156643, 0), \
                           -45707.8, 24842, 24842, -nan)
reports[-1].sigmaresid = ValErr(1.52349, 0.00612196, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00532191, None, -5.45433e-05, None, 0.00899033, None, -4.42315e-05, None, 0.00899033, None, -4.42315e-05, None, 0.00451357, None, -6.2003e-05, None, 0.00451357, None, -6.2003e-05, None, 1.52762, None, 0.00803763, None, 1.52762, None, 0.00803763, None)

reports.append(Report(604018944, ("CSC", 1, 1, 3, 32), "MEp13_32"))
reports[-1].posNum = 26783
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0236816, 0.0134355, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.83577, 0.267219, 0), \
                           ValErr(-0.0170326, 0.0056899, 0), \
                           ValErr(0.0122753, 0.0131235, 0), \
                           ValErr(0.000136984, 0.000121344, 0), \
                           -48699.3, 26783, 26783, -nan)
reports[-1].sigmaresid = ValErr(1.49086, 0.00637777, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0255161, None, -8.62312e-05, None, 0.0137881, None, -0.000149513, None, 0.0137881, None, -0.000149513, None, 0.02716, None, -0.000118731, None, 0.02716, None, -0.000118731, None, 1.49422, None, 0.00645479, None, 1.49422, None, 0.00645479, None)

reports.append(Report(604018952, ("CSC", 1, 1, 3, 33), "MEp13_33"))
reports[-1].posNum = 26667
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00360234, 0.0134604, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.42163, 0.266513, 0), \
                           ValErr(-0.00532804, 0.00604406, 0), \
                           ValErr(-0.00620437, 0.0129834, 0), \
                           ValErr(-7.15144e-05, 0.000211682, 0), \
                           -48543, 26667, 26667, -nan)
reports[-1].sigmaresid = ValErr(1.49389, 0.00646859, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0107336, None, -3.43701e-05, None, 0.00118933, None, -8.5451e-05, None, 0.00118933, None, -8.5451e-05, None, -0.000288332, None, -2.93889e-06, None, -0.000288332, None, -2.93889e-06, None, 1.49626, None, 0.00686066, None, 1.49626, None, 0.00686066, None)

reports.append(Report(604018960, ("CSC", 1, 1, 3, 34), "MEp13_34"))
reports[-1].posNum = 25465
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0130823, 0.0138429, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.46224, 0.286597, 0), \
                           ValErr(-0.0117199, 0.00663019, 0), \
                           ValErr(0.00968462, 0.0136567, 0), \
                           ValErr(-0.000330751, 0.000225761, 0), \
                           -46937.9, 25465, 25465, -nan)
reports[-1].sigmaresid = ValErr(1.52851, 0.00677307, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0193501, None, -3.69448e-05, None, 0.00491522, None, -9.95995e-05, None, 0.00491522, None, -9.95995e-05, None, -0.00252651, None, -1.68761e-05, None, -0.00252651, None, -1.68761e-05, None, 1.53081, None, 0.00634374, None, 1.53081, None, 0.00634374, None)

reports.append(Report(604018968, ("CSC", 1, 1, 3, 35), "MEp13_35"))
reports[-1].posNum = 24510
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00200827, 0.0139887, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.98834, 0.288242, 0), \
                           ValErr(-0.0106359, 0.00674742, 0), \
                           ValErr(0.012022, 0.0135826, 0), \
                           ValErr(-0.000581665, 0.000119763, 0), \
                           -44986.4, 24510, 24510, -nan)
reports[-1].sigmaresid = ValErr(1.51664, 0.00636954, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00325938, None, -2.11654e-05, None, -0.00657687, None, -0.000110349, None, -0.00657687, None, -0.000110349, None, -0.0174341, None, -6.44347e-05, None, -0.0174341, None, -6.44347e-05, None, 1.52014, None, 0.0071045, None, 1.52014, None, 0.0071045, None)

reports.append(Report(604018976, ("CSC", 1, 1, 3, 36), "MEp13_36"))
reports[-1].posNum = 25580
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00390536, 0.013813, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.21259, 0.269413, 0), \
                           ValErr(0.00324118, 0.00612382, 0), \
                           ValErr(-0.0110785, 0.0131968, 0), \
                           ValErr(0.000119447, 0.000218037, 0), \
                           -46735.9, 25580, 25580, -nan)
reports[-1].sigmaresid = ValErr(1.50397, 0.00665943, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0129278, None, -6.80817e-05, None, 0.0125581, None, -9.81131e-05, None, 0.0125581, None, -9.81131e-05, None, 0.00730042, None, -2.04406e-05, None, 0.00730042, None, -2.04406e-05, None, 1.506, None, 0.00665164, None, 1.506, None, 0.00665164, None)

reports.append(Report(604017160, ("CSC", 1, 1, 4, 1), "MEp14_01"))
reports[-1].posNum = 138884
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00100564, 0.000714747, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.136021, 0.0413057, 0), \
                           ValErr(0.000716258, 0.00109434, 0), \
                           ValErr(0.00426206, 0.00544969, 0), \
                           ValErr(1.37624e-05, 1.46867e-05, 0), \
                           33303.1, 138884, 138884, -nan)
reports[-1].sigmaresid = ValErr(0.190381, 0.000361228, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000938679, None, -7.03828e-06, None, -0.00123703, None, 2.76193e-06, None, -0.00123703, None, 2.76193e-06, None, -0.000610749, None, 2.16473e-06, None, -0.000610749, None, 2.16473e-06, None, 0.190392, None, 0.00422924, None, 0.190392, None, 0.00422924, None)

reports.append(Report(604017176, ("CSC", 1, 1, 4, 3), "MEp14_03"))
reports[-1].posNum = 139490
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00238751, 0.000713484, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0895415, 0.0409953, 0), \
                           ValErr(-2.41661e-05, 0.00108497, 0), \
                           ValErr(-0.00630985, 0.00545302, 0), \
                           ValErr(1.45184e-05, 1.45197e-05, 0), \
                           34061.3, 139490, 139490, -nan)
reports[-1].sigmaresid = ValErr(0.189546, 0.000358862, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00138054, None, 9.24261e-07, None, -0.00174383, None, -2.89499e-06, None, -0.00174383, None, -2.89499e-06, None, -0.00177538, None, 1.26128e-05, None, -0.00177538, None, 1.26128e-05, None, 0.189551, None, 0.0043013, None, 0.189551, None, 0.0043013, None)

reports.append(Report(604017192, ("CSC", 1, 1, 4, 5), "MEp14_05"))
reports[-1].posNum = 139156
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000912597, 0.000714683, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.105502, 0.04135, 0), \
                           ValErr(-0.000816756, 0.0010902, 0), \
                           ValErr(0.00818595, 0.00544377, 0), \
                           ValErr(1.9713e-05, 1.46248e-05, 0), \
                           33160.9, 139156, 139156, -nan)
reports[-1].sigmaresid = ValErr(0.190665, 0.000361414, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0015147, None, -5.63596e-06, None, -0.00140513, None, 3.04246e-06, None, -0.00140513, None, 3.04246e-06, None, -0.00171008, None, -3.2201e-06, None, -0.00171008, None, -3.2201e-06, None, 0.190674, None, 0.00414925, None, 0.190674, None, 0.00414925, None)

reports.append(Report(604017208, ("CSC", 1, 1, 4, 7), "MEp14_07"))
reports[-1].posNum = 139378
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00146198, 0.000715299, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.145518, 0.0412789, 0), \
                           ValErr(-0.00134256, 0.00109292, 0), \
                           ValErr(-0.00270466, 0.00544919, 0), \
                           ValErr(-3.67e-05, 1.46339e-05, 0), \
                           33113.5, 139378, 139378, -nan)
reports[-1].sigmaresid = ValErr(0.190802, 0.000361386, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000891205, None, -4.28966e-06, None, -0.00154883, None, -2.09359e-06, None, -0.00154883, None, -2.09359e-06, None, -0.0020146, None, 1.70307e-05, None, -0.0020146, None, 1.70307e-05, None, 0.190816, None, 0.00419928, None, 0.190816, None, 0.00419928, None)

reports.append(Report(604017224, ("CSC", 1, 1, 4, 9), "MEp14_09"))
reports[-1].posNum = 138855
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00254735, 0.000714469, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.074378, 0.0411879, 0), \
                           ValErr(-0.00052773, 0.00108935, 0), \
                           ValErr(-0.00958045, 0.00544424, 0), \
                           ValErr(4.73321e-05, 1.46485e-05, 0), \
                           33741.6, 138855, 138855, -nan)
reports[-1].sigmaresid = ValErr(0.189771, 0.000362769, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000776008, None, 4.89995e-06, None, -0.00135629, None, 4.50027e-06, None, -0.00135629, None, 4.50027e-06, None, -0.000362622, None, -3.19272e-05, None, -0.000362622, None, -3.19272e-05, None, 0.189781, None, 0.00436526, None, 0.189781, None, 0.00436526, None)

reports.append(Report(604017240, ("CSC", 1, 1, 4, 11), "MEp14_11"))
reports[-1].posNum = 138257
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000831451, 0.000718982, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.185423, 0.0414816, 0), \
                           ValErr(-0.00196656, 0.0010966, 0), \
                           ValErr(0.00922222, 0.00547106, 0), \
                           ValErr(1.23314e-06, 1.47444e-05, 0), \
                           32545.7, 138257, 138257, -nan)
reports[-1].sigmaresid = ValErr(0.191218, 0.00036364, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00207658, None, -6.21503e-06, None, -0.00156067, None, -2.82844e-05, None, -0.00156067, None, -2.82844e-05, None, -0.00169476, None, -1.38291e-05, None, -0.00169476, None, -1.38291e-05, None, 0.191235, None, 0.00455632, None, 0.191235, None, 0.00455632, None)

reports.append(Report(604017256, ("CSC", 1, 1, 4, 13), "MEp14_13"))
reports[-1].posNum = 139768
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00295452, 0.000713481, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.105666, 0.0410422, 0), \
                           ValErr(-0.00062681, 0.00108974, 0), \
                           ValErr(0.00122709, 0.00543, 0), \
                           ValErr(5.1668e-06, 1.45898e-05, 0), \
                           33736.5, 139768, 139768, -nan)
reports[-1].sigmaresid = ValErr(0.190079, 0.000359515, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00282231, None, 3.67413e-07, None, -0.00301402, None, -6.96107e-07, None, -0.00301402, None, -6.96107e-07, None, -0.00285554, None, -4.48345e-06, None, -0.00285554, None, -4.48345e-06, None, 0.190084, None, 0.00416052, None, 0.190084, None, 0.00416052, None)

reports.append(Report(604017272, ("CSC", 1, 1, 4, 15), "MEp14_15"))
reports[-1].posNum = 138348
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0018088, 0.000714232, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0895986, 0.0411479, 0), \
                           ValErr(-0.00130607, 0.0010913, 0), \
                           ValErr(-0.00561005, 0.00543469, 0), \
                           ValErr(1.54866e-05, 1.51913e-05, 0), \
                           33514.6, 138348, 138348, -nan)
reports[-1].sigmaresid = ValErr(0.189913, 0.000361069, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00120239, None, -9.57428e-07, None, -0.00121873, None, -8.77054e-06, None, -0.00121873, None, -8.77054e-06, None, -0.000952917, None, -1.62304e-05, None, -0.000952917, None, -1.62304e-05, None, 0.189918, None, 0.00438629, None, 0.189918, None, 0.00438629, None)

reports.append(Report(604017288, ("CSC", 1, 1, 4, 17), "MEp14_17"))
reports[-1].posNum = 140088
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00109051, 0.000708962, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0553144, 0.0407598, 0), \
                           ValErr(-0.000536281, 0.00107833, 0), \
                           ValErr(0.00436992, 0.005426, 0), \
                           ValErr(1.92435e-06, 1.44257e-05, 0), \
                           34930, 140088, 140088, -nan)
reports[-1].sigmaresid = ValErr(0.18857, 0.000356251, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00192716, None, 6.47383e-06, None, -0.00142335, None, -4.0212e-06, None, -0.00142335, None, -4.0212e-06, None, -0.000985259, None, -1.28187e-05, None, -0.000985259, None, -1.28187e-05, None, 0.188573, None, 0.00418342, None, 0.188573, None, 0.00418342, None)

reports.append(Report(604017304, ("CSC", 1, 1, 4, 19), "MEp14_19"))
reports[-1].posNum = 138873
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00110726, 0.000715404, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0931945, 0.0411603, 0), \
                           ValErr(-0.00132769, 0.00108848, 0), \
                           ValErr(-0.00219269, 0.00545031, 0), \
                           ValErr(-7.52289e-06, 1.46872e-05, 0), \
                           33400.7, 138873, 138873, -nan)
reports[-1].sigmaresid = ValErr(0.190243, 0.000360982, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0010376, None, 2.32311e-06, None, -0.000994262, None, -7.7388e-06, None, -0.000994262, None, -7.7388e-06, None, -0.000230959, None, -3.09566e-05, None, -0.000230959, None, -3.09566e-05, None, 0.190248, None, 0.00431309, None, 0.190248, None, 0.00431309, None)

reports.append(Report(604017320, ("CSC", 1, 1, 4, 21), "MEp14_21"))
reports[-1].posNum = 139103
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00216522, 0.000709105, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0573837, 0.0409825, 0), \
                           ValErr(3.22772e-05, 0.00108164, 0), \
                           ValErr(0.000270921, 0.00542092, 0), \
                           ValErr(1.88198e-05, 1.44593e-05, 0), \
                           34587.4, 139103, 139103, -nan)
reports[-1].sigmaresid = ValErr(0.188702, 0.000357762, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00179156, None, 1.8255e-06, None, -0.00201582, None, -1.53645e-05, None, -0.00201582, None, -1.53645e-05, None, -0.00359913, None, -1.32416e-05, None, -0.00359913, None, -1.32416e-05, None, 0.188705, None, 0.00427251, None, 0.188705, None, 0.00427251, None)

reports.append(Report(604017336, ("CSC", 1, 1, 4, 23), "MEp14_23"))
reports[-1].posNum = 138580
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00217676, 0.000717161, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0619837, 0.0414509, 0), \
                           ValErr(9.53083e-05, 0.00109573, 0), \
                           ValErr(0.00454866, 0.00547142, 0), \
                           ValErr(2.49287e-05, 1.47068e-05, 0), \
                           32725.7, 138580, 138580, -nan)
reports[-1].sigmaresid = ValErr(0.191075, 0.000362943, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0017078, None, 1.35845e-06, None, -0.00233335, None, 2.77786e-06, None, -0.00233335, None, 2.77786e-06, None, -0.00205359, None, -1.24655e-05, None, -0.00205359, None, -1.24655e-05, None, 0.19108, None, 0.00475761, None, 0.19108, None, 0.00475761, None)

reports.append(Report(604017352, ("CSC", 1, 1, 4, 25), "MEp14_25"))
reports[-1].posNum = 139088
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00166755, 0.000715489, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0730236, 0.0411069, 0), \
                           ValErr(-0.00258049, 0.00108897, 0), \
                           ValErr(0.00347248, 0.00545937, 0), \
                           ValErr(2.35977e-05, 1.46199e-05, 0), \
                           33608.7, 139088, 139088, -nan)
reports[-1].sigmaresid = ValErr(0.19003, 0.000360298, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0011455, None, 9.1347e-06, None, -0.00174192, None, 3.42948e-07, None, -0.00174192, None, 3.42948e-07, None, 0.000200836, None, -1.15376e-05, None, 0.000200836, None, -1.15376e-05, None, 0.190037, None, 0.00458187, None, 0.190037, None, 0.00458187, None)

reports.append(Report(604017368, ("CSC", 1, 1, 4, 27), "MEp14_27"))
reports[-1].posNum = 138675
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00202654, 0.000713281, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0839467, 0.0411893, 0), \
                           ValErr(-0.00270067, 0.00109193, 0), \
                           ValErr(-0.0041133, 0.00544692, 0), \
                           ValErr(1.06051e-05, 1.46183e-05, 0), \
                           33655.4, 138675, 138675, -nan)
reports[-1].sigmaresid = ValErr(0.189829, 0.000360453, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00168449, None, 5.80301e-06, None, -0.00161058, None, -1.09511e-05, None, -0.00161058, None, -1.09511e-05, None, -0.00142794, None, -2.44097e-05, None, -0.00142794, None, -2.44097e-05, None, 0.189835, None, 0.00418351, None, 0.189835, None, 0.00418351, None)

reports.append(Report(604017384, ("CSC", 1, 1, 4, 29), "MEp14_29"))
reports[-1].posNum = 138134
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00387309, 0.000717752, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.124205, 0.0414481, 0), \
                           ValErr(-0.000939291, 0.00110351, 0), \
                           ValErr(-0.00119693, 0.00548322, 0), \
                           ValErr(2.74455e-05, 1.47192e-05, 0), \
                           32901.6, 138134, 138134, -nan)
reports[-1].sigmaresid = ValErr(0.190687, 0.00036279, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00364881, None, 1.61258e-05, None, -0.00354443, None, 1.87152e-05, None, -0.00354443, None, 1.87152e-05, None, -0.00222755, None, 7.91153e-06, None, -0.00222755, None, 7.91153e-06, None, 0.190695, None, 0.00413851, None, 0.190695, None, 0.00413851, None)

reports.append(Report(604017400, ("CSC", 1, 1, 4, 31), "MEp14_31"))
reports[-1].posNum = 139030
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00243394, 0.000712924, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0873818, 0.0413227, 0), \
                           ValErr(-0.00211869, 0.00109231, 0), \
                           ValErr(-0.00900692, 0.00546076, 0), \
                           ValErr(-9.08955e-06, 1.45563e-05, 0), \
                           33389.5, 139030, 139030, -nan)
reports[-1].sigmaresid = ValErr(0.19031, 0.000360905, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00179817, None, -9.54318e-07, None, -0.00180179, None, -1.53549e-06, None, -0.00180179, None, -1.53549e-06, None, -0.00145595, None, -1.35444e-05, None, -0.00145595, None, -1.35444e-05, None, 0.190318, None, 0.00416378, None, 0.190318, None, 0.00416378, None)

reports.append(Report(604017416, ("CSC", 1, 1, 4, 33), "MEp14_33"))
reports[-1].posNum = 138333
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00118067, 0.000721647, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.133674, 0.0415469, 0), \
                           ValErr(-0.00137522, 0.00110512, 0), \
                           ValErr(0.00124592, 0.00549694, 0), \
                           ValErr(-1.10928e-05, 1.48312e-05, 0), \
                           32159.6, 138333, 138333, -nan)
reports[-1].sigmaresid = ValErr(0.191778, 0.000364603, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00174476, None, -5.71768e-06, None, -0.00138829, None, -1.02815e-05, None, -0.00138829, None, -1.02815e-05, None, 0.00063659, None, -1.3814e-05, None, 0.00063659, None, -1.3814e-05, None, 0.191785, None, 0.00484283, None, 0.191785, None, 0.00484283, None)

reports.append(Report(604017432, ("CSC", 1, 1, 4, 35), "MEp14_35"))
reports[-1].posNum = 140048
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00187641, 0.000710273, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0411995, 0.0408116, 0), \
                           ValErr(-0.000660235, 0.00107729, 0), \
                           ValErr(-0.000917588, 0.00537333, 0), \
                           ValErr(4.3598e-06, 1.45211e-05, 0), \
                           34349.8, 140048, 140048, -nan)
reports[-1].sigmaresid = ValErr(0.18934, 0.000357758, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00123343, None, 2.49975e-06, None, -0.00176655, None, 3.18072e-06, None, -0.00176655, None, 3.18072e-06, None, -0.00143788, None, -4.69896e-06, None, -0.00143788, None, -4.69896e-06, None, 0.189341, None, 0.00415982, None, 0.189341, None, 0.00415982, None)

reports.append(Report(604017168, ("CSC", 1, 1, 4, 2), "MEp14_02"))
reports[-1].posNum = 138704
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00141452, 0.000641901, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0716196, 0.0348486, 0), \
                           ValErr(-0.000420212, 0.000923806, 0), \
                           ValErr(-0.000689824, 0.00463041, 0), \
                           ValErr(-1.06259e-05, 1.30305e-05, 0), \
                           48932.7, 138704, 138704, -nan)
reports[-1].sigmaresid = ValErr(0.17004, 0.000322842, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00155534, None, 7.83989e-06, None, -0.00145239, None, 3.37346e-05, None, -0.00145239, None, 3.37346e-05, None, -0.00105302, None, 3.58284e-05, None, -0.00105302, None, 3.58284e-05, None, 0.170043, None, 0.00446, None, 0.170043, None, 0.00446, None)

reports.append(Report(604017184, ("CSC", 1, 1, 4, 4), "MEp14_04"))
reports[-1].posNum = 138471
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00161749, 0.00063815, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.105553, 0.0364382, 0), \
                           ValErr(-0.000184518, 0.000955467, 0), \
                           ValErr(-0.00719011, 0.00465031, 0), \
                           ValErr(-1.43401e-06, 1.404e-05, 0), \
                           49299.3, 138471, 138471, -nan)
reports[-1].sigmaresid = ValErr(0.169489, 0.000320925, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000784349, None, -1.26461e-06, None, -0.00102612, None, -4.7278e-06, None, -0.00102612, None, -4.7278e-06, None, 0.000215076, None, -7.66958e-06, None, 0.000215076, None, -7.66958e-06, None, 0.169497, None, 0.00509413, None, 0.169497, None, 0.00509413, None)

reports.append(Report(604017200, ("CSC", 1, 1, 4, 6), "MEp14_06"))
reports[-1].posNum = 139204
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00146055, 0.000639416, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.03315, 0.0348754, 0), \
                           ValErr(0.000469439, 0.000923256, 0), \
                           ValErr(0.0014579, 0.00460785, 0), \
                           ValErr(-3.54402e-06, 1.30388e-05, 0), \
                           48872.9, 139204, 139204, -nan)
reports[-1].sigmaresid = ValErr(0.170328, 0.00032281, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00135668, None, 6.51474e-06, None, -0.00161814, None, 2.25595e-05, None, -0.00161814, None, 2.25595e-05, None, -0.00156078, None, 2.44083e-05, None, -0.00156078, None, 2.44083e-05, None, 0.170329, None, 0.00438026, None, 0.170329, None, 0.00438026, None)

reports.append(Report(604017216, ("CSC", 1, 1, 4, 8), "MEp14_08"))
reports[-1].posNum = 138052
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00117097, 0.000641304, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0825275, 0.0349086, 0), \
                           ValErr(-0.00165058, 0.000924449, 0), \
                           ValErr(-0.000192475, 0.00464381, 0), \
                           ValErr(-2.56164e-06, 1.30157e-05, 0), \
                           49064.4, 138052, 138052, -nan)
reports[-1].sigmaresid = ValErr(0.169595, 0.000322757, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000678981, None, 8.32166e-06, None, -0.00117587, None, 6.55083e-07, None, -0.00117587, None, 6.55083e-07, None, 0.000241782, None, 2.09377e-06, None, 0.000241782, None, 2.09377e-06, None, 0.169599, None, 0.00439385, None, 0.169599, None, 0.00439385, None)

reports.append(Report(604017232, ("CSC", 1, 1, 4, 10), "MEp14_10"))
reports[-1].posNum = 138732
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00025241, 0.000643786, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0752704, 0.0349146, 0), \
                           ValErr(-0.000136737, 0.000925515, 0), \
                           ValErr(0.00345989, 0.0046233, 0), \
                           ValErr(-5.1001e-06, 1.30831e-05, 0), \
                           48581, 138732, 138732, -nan)
reports[-1].sigmaresid = ValErr(0.170483, 0.000323652, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00082322, None, -9.4542e-07, None, -0.000594369, None, 2.39589e-05, None, -0.000594369, None, 2.39589e-05, None, -0.000217591, None, -1.72508e-06, None, -0.000217591, None, -1.72508e-06, None, 0.170487, None, 0.00450801, None, 0.170487, None, 0.00450801, None)

reports.append(Report(604017248, ("CSC", 1, 1, 4, 12), "MEp14_12"))
reports[-1].posNum = 138939
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00140063, 0.000636861, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0542025, 0.0348536, 0), \
                           ValErr(-0.000438622, 0.000919534, 0), \
                           ValErr(0.00219055, 0.0046329, 0), \
                           ValErr(-8.19892e-06, 1.2946e-05, 0), \
                           49455.4, 138939, 138939, -nan)
reports[-1].sigmaresid = ValErr(0.169502, 0.00032155, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00169794, None, 1.55718e-05, None, -0.00165933, None, 3.04139e-05, None, -0.00165933, None, 3.04139e-05, None, -0.00113512, None, 1.77965e-06, None, -0.00113512, None, 1.77965e-06, None, 0.169504, None, 0.00445683, None, 0.169504, None, 0.00445683, None)

reports.append(Report(604017264, ("CSC", 1, 1, 4, 14), "MEp14_14"))
reports[-1].posNum = 138803
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000243235, 0.000641261, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.105941, 0.0349691, 0), \
                           ValErr(0.000976182, 0.000926435, 0), \
                           ValErr(0.0036903, 0.0046368, 0), \
                           ValErr(-9.12983e-07, 1.30471e-05, 0), \
                           48781.8, 138803, 138803, -nan)
reports[-1].sigmaresid = ValErr(0.170267, 0.00032316, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00064532, None, 2.14843e-06, None, -0.000571514, None, 1.11131e-05, None, -0.000571514, None, 1.11131e-05, None, -4.793e-06, None, 7.90058e-06, None, -4.793e-06, None, 7.90058e-06, None, 0.170276, None, 0.00504517, None, 0.170276, None, 0.00504517, None)

reports.append(Report(604017280, ("CSC", 1, 1, 4, 16), "MEp14_16"))
reports[-1].posNum = 137660
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00266911, 0.000642349, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.128792, 0.0351798, 0), \
                           ValErr(-0.00255558, 0.000931571, 0), \
                           ValErr(0.00438033, 0.00466016, 0), \
                           ValErr(9.52997e-06, 1.30909e-05, 0), \
                           48465.4, 137660, 137660, -nan)
reports[-1].sigmaresid = ValErr(0.170162, 0.000324297, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00244959, None, 1.64264e-05, None, -0.00295277, None, 2.92156e-05, None, -0.00295277, None, 2.92156e-05, None, -0.00375706, None, 2.82962e-05, None, -0.00375706, None, 2.82962e-05, None, 0.170174, None, 0.00459658, None, 0.170174, None, 0.00459658, None)

reports.append(Report(604017296, ("CSC", 1, 1, 4, 18), "MEp14_18"))
reports[-1].posNum = 138630
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00143584, 0.000640588, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0998533, 0.0350051, 0), \
                           ValErr(-0.000335299, 0.00092412, 0), \
                           ValErr(0.000829005, 0.00463918, 0), \
                           ValErr(1.04893e-05, 1.30409e-05, 0), \
                           48829.1, 138630, 138630, -nan)
reports[-1].sigmaresid = ValErr(0.170135, 0.000323109, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0010042, None, 1.98199e-05, None, -0.00141193, None, 3.76241e-05, None, -0.00141193, None, 3.76241e-05, None, -0.000864532, None, 3.68135e-05, None, -0.000864532, None, 3.68135e-05, None, 0.17014, None, 0.00492538, None, 0.17014, None, 0.00492538, None)

reports.append(Report(604017312, ("CSC", 1, 1, 4, 20), "MEp14_20"))
reports[-1].posNum = 138600
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000775373, 0.000641437, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0577192, 0.0349242, 0), \
                           ValErr(-0.00110019, 0.000923706, 0), \
                           ValErr(0.00880475, 0.00463999, 0), \
                           ValErr(1.95632e-05, 1.30725e-05, 0), \
                           48940.7, 138600, 138600, -nan)
reports[-1].sigmaresid = ValErr(0.169985, 0.000322859, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00125468, None, 1.4293e-05, None, -0.00134231, None, 3.29132e-05, None, -0.00134231, None, 3.29132e-05, None, -0.00148336, None, 2.15638e-05, None, -0.00148336, None, 2.15638e-05, None, 0.169992, None, 0.00480318, None, 0.169992, None, 0.00480318, None)

reports.append(Report(604017328, ("CSC", 1, 1, 4, 22), "MEp14_22"))
reports[-1].posNum = 138069
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0020496, 0.00064123, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0934292, 0.034823, 0), \
                           ValErr(-0.000957739, 0.000922676, 0), \
                           ValErr(-0.00316592, 0.00464261, 0), \
                           ValErr(-1.59361e-05, 1.30106e-05, 0), \
                           49192.6, 138069, 138069, -nan)
reports[-1].sigmaresid = ValErr(0.169445, 0.000322452, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00203273, None, 4.38637e-06, None, -0.00193919, None, -1.65231e-05, None, -0.00193919, None, -1.65231e-05, None, -0.00178734, None, 3.32821e-06, None, -0.00178734, None, 3.32821e-06, None, 0.169451, None, 0.0046988, None, 0.169451, None, 0.0046988, None)

reports.append(Report(604017344, ("CSC", 1, 1, 4, 24), "MEp14_24"))
reports[-1].posNum = 138042
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00287301, 0.000641407, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0560433, 0.0351004, 0), \
                           ValErr(-0.00153009, 0.000923255, 0), \
                           ValErr(-0.00470127, 0.00462893, 0), \
                           ValErr(-1.27329e-05, 1.3078e-05, 0), \
                           48628.3, 138042, 138042, -nan)
reports[-1].sigmaresid = ValErr(0.170127, 0.000323782, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00202377, None, 1.80972e-05, None, -0.00259375, None, 3.24187e-05, None, -0.00259375, None, 3.24187e-05, None, -0.00131471, None, 2.25398e-05, None, -0.00131471, None, 2.25398e-05, None, 0.170131, None, 0.00452062, None, 0.170131, None, 0.00452062, None)

reports.append(Report(604017360, ("CSC", 1, 1, 4, 26), "MEp14_26"))
reports[-1].posNum = 138749
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000277724, 0.000639334, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0750062, 0.0350392, 0), \
                           ValErr(0.0024212, 0.000925759, 0), \
                           ValErr(0.00627216, 0.00463848, 0), \
                           ValErr(-1.43076e-05, 1.30298e-05, 0), \
                           48814.9, 138749, 138749, -nan)
reports[-1].sigmaresid = ValErr(0.170204, 0.000323101, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000733668, None, 8.13465e-07, None, -0.000941626, None, 3.22875e-05, None, -0.000941626, None, 3.22875e-05, None, -0.00078907, None, 1.11962e-05, None, -0.00078907, None, 1.11962e-05, None, 0.170215, None, 0.00489382, None, 0.170215, None, 0.00489382, None)

reports.append(Report(604017376, ("CSC", 1, 1, 4, 28), "MEp14_28"))
reports[-1].posNum = 137844
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000753923, 0.000647088, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.106318, 0.0352806, 0), \
                           ValErr(-0.00162637, 0.000933167, 0), \
                           ValErr(0.000162502, 0.00467555, 0), \
                           ValErr(-1.10569e-05, 1.31518e-05, 0), \
                           47713.7, 137844, 137844, -nan)
reports[-1].sigmaresid = ValErr(0.171173, 0.000326006, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000738678, None, 3.06366e-06, None, -0.000877885, None, 2.44924e-05, None, -0.000877885, None, 2.44924e-05, None, -0.00164477, None, 1.2728e-05, None, -0.00164477, None, 1.2728e-05, None, 0.17118, None, 0.00429567, None, 0.17118, None, 0.00429567, None)

reports.append(Report(604017392, ("CSC", 1, 1, 4, 30), "MEp14_30"))
reports[-1].posNum = 137481
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00157962, 0.000638118, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.120435, 0.0349834, 0), \
                           ValErr(-3.4201e-05, 0.000927085, 0), \
                           ValErr(-0.00420417, 0.00463648, 0), \
                           ValErr(3.89606e-06, 1.30127e-05, 0), \
                           49409.9, 137481, 137481, -nan)
reports[-1].sigmaresid = ValErr(0.16892, 0.000322139, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000898209, None, 6.12591e-06, None, -0.00120406, None, 2.72755e-05, None, -0.00120406, None, 2.72755e-05, None, -0.000718734, None, 1.48253e-05, None, -0.000718734, None, 1.48253e-05, None, 0.168928, None, 0.00461617, None, 0.168928, None, 0.00461617, None)

reports.append(Report(604017408, ("CSC", 1, 1, 4, 32), "MEp14_32"))
reports[-1].posNum = 138711
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00339383, 0.000641252, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0890779, 0.0350664, 0), \
                           ValErr(-0.00025686, 0.000923949, 0), \
                           ValErr(-0.013475, 0.00462776, 0), \
                           ValErr(2.57968e-05, 1.3054e-05, 0), \
                           48524.3, 138711, 138711, -nan)
reports[-1].sigmaresid = ValErr(0.170544, 0.000323792, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00172317, None, 7.05024e-06, None, -0.00202515, None, 2.42545e-05, None, -0.00202515, None, 2.42545e-05, None, -0.00100466, None, 2.55491e-05, None, -0.00100466, None, 2.55491e-05, None, 0.170554, None, 0.0044059, None, 0.170554, None, 0.0044059, None)

reports.append(Report(604017424, ("CSC", 1, 1, 4, 34), "MEp14_34"))
reports[-1].posNum = 129715
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00193002, 0.000675943, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0657787, 0.0375387, 0), \
                           ValErr(-0.000395434, 0.00105234, 0), \
                           ValErr(-0.00367714, 0.00477878, 0), \
                           ValErr(2.02114e-05, 1.41647e-05, 0), \
                           46611.9, 129715, 129715, -nan)
reports[-1].sigmaresid = ValErr(0.168928, 0.000330844, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00155399, None, -3.2499e-05, None, -0.00142152, None, -8.70145e-05, None, -0.00142152, None, -8.70145e-05, None, -0.000694473, None, -5.47698e-05, None, -0.000694473, None, -5.47698e-05, None, 0.168932, None, 0.00547895, None, 0.168932, None, 0.00547895, None)

reports.append(Report(604017440, ("CSC", 1, 1, 4, 36), "MEp14_36"))
reports[-1].posNum = 139067
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00197685, 0.00063948, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.114927, 0.0347955, 0), \
                           ValErr(-0.000115158, 0.000921496, 0), \
                           ValErr(0.00896758, 0.0046188, 0), \
                           ValErr(2.01855e-05, 1.30108e-05, 0), \
                           49221, 139067, 139067, -nan)
reports[-1].sigmaresid = ValErr(0.169844, 0.000322049, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00240905, None, 1.20468e-05, None, -0.00255343, None, 5.24895e-05, None, -0.00255343, None, 5.24895e-05, None, -0.002312, None, 3.17298e-05, None, -0.002312, None, 3.17298e-05, None, 0.169857, None, 0.00503976, None, 0.169857, None, 0.00503976, None)

reports.append(Report(604021256, ("CSC", 1, 2, 1, 1), "MEp21_01"))
reports[-1].posNum = 277901
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00124446, 0.00118769, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0095601, 0.0311205, 0), \
                           ValErr(0.0010779, 0.000614147, 0), \
                           ValErr(1.89426e-05, 0.00143036, 0), \
                           ValErr(1.21706e-05, 1.75306e-05, 0), \
                           -151657, 277901, 277901, -nan)
reports[-1].sigmaresid = ValErr(0.417607, 0.000560154, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00127315, None, 9.28257e-06, None, -0.00114486, None, 2.02218e-05, None, -0.00114486, None, 2.02218e-05, None, -0.000781472, None, 5.43355e-06, None, -0.000781472, None, 5.43355e-06, None, 0.41761, None, 0.00557563, None, 0.41761, None, 0.00557563, None)

reports.append(Report(604021272, ("CSC", 1, 2, 1, 3), "MEp21_03"))
reports[-1].posNum = 279044
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000758212, 0.00118473, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0365917, 0.0310636, 0), \
                           ValErr(0.000286766, 0.00061207, 0), \
                           ValErr(0.00108939, 0.00142851, 0), \
                           ValErr(1.05605e-05, 1.74477e-05, 0), \
                           -152244, 279044, 279044, -nan)
reports[-1].sigmaresid = ValErr(0.417551, 0.000558931, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00164457, None, 2.3594e-05, None, -0.0012786, None, 3.92775e-05, None, -0.0012786, None, 3.92775e-05, None, -0.000559204, None, 2.04662e-05, None, -0.000559204, None, 2.04662e-05, None, 0.417554, None, 0.00557079, None, 0.417554, None, 0.00557079, None)

reports.append(Report(604021288, ("CSC", 1, 2, 1, 5), "MEp21_05"))
reports[-1].posNum = 279026
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000780356, 0.00118538, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0729748, 0.0310518, 0), \
                           ValErr(0.00148262, 0.000612445, 0), \
                           ValErr(0.000949884, 0.0014278, 0), \
                           ValErr(4.26685e-06, 1.74921e-05, 0), \
                           -152191, 279026, 279026, -nan)
reports[-1].sigmaresid = ValErr(0.417487, 0.000558864, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000850924, None, -1.79136e-05, None, 0.000284995, None, 1.24534e-05, None, 0.000284995, None, 1.24534e-05, None, 0.0014852, None, -6.54037e-06, None, 0.0014852, None, -6.54037e-06, None, 0.417499, None, 0.00568243, None, 0.417499, None, 0.00568243, None)

reports.append(Report(604021304, ("CSC", 1, 2, 1, 7), "MEp21_07"))
reports[-1].posNum = 278455
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00305177, 0.00118916, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0390985, 0.0312641, 0), \
                           ValErr(3.13551e-05, 0.000671053, 0), \
                           ValErr(-0.00103524, 0.00143553, 0), \
                           ValErr(4.48942e-05, 1.90873e-05, 0), \
                           -151623, 278455, 278455, -nan)
reports[-1].sigmaresid = ValErr(0.417102, 0.000568833, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00119267, None, 1.76284e-05, None, -0.0020438, None, 3.79251e-05, None, -0.0020438, None, 3.79251e-05, None, -0.00174149, None, 2.16819e-05, None, -0.00174149, None, 2.16819e-05, None, 0.417109, None, 0.00573254, None, 0.417109, None, 0.00573254, None)

reports.append(Report(604021320, ("CSC", 1, 2, 1, 9), "MEp21_09"))
reports[-1].posNum = 278501
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00166846, 0.00117887, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00614549, 0.0308419, 0), \
                           ValErr(-0.000221458, 0.000607734, 0), \
                           ValErr(-3.67899e-05, 0.0014188, 0), \
                           ValErr(1.82633e-05, 1.73722e-05, 0), \
                           -149776, 278501, 278501, -nan)
reports[-1].sigmaresid = ValErr(0.414308, 0.00055513, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00241516, None, 1.2486e-05, None, -0.00147781, None, 1.35698e-05, None, -0.00147781, None, 1.35698e-05, None, -0.000370538, None, 4.7158e-06, None, -0.000370538, None, 4.7158e-06, None, 0.414309, None, 0.00561766, None, 0.414309, None, 0.00561766, None)

reports.append(Report(604021336, ("CSC", 1, 2, 1, 11), "MEp21_11"))
reports[-1].posNum = 278301
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00132188, 0.00117639, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0178394, 0.0309053, 0), \
                           ValErr(0.000947285, 0.000609332, 0), \
                           ValErr(-0.00100503, 0.00141955, 0), \
                           ValErr(-1.81296e-05, 1.7345e-05, 0), \
                           -149614, 278301, 278301, -nan)
reports[-1].sigmaresid = ValErr(0.414227, 0.00055522, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-9.02486e-05, None, 8.55824e-08, None, -0.000925668, None, 3.10549e-05, None, -0.000925668, None, 3.10549e-05, None, -0.00121193, None, -7.68211e-07, None, -0.00121193, None, -7.68211e-07, None, 0.414231, None, 0.00562001, None, 0.414231, None, 0.00562001, None)

reports.append(Report(604021352, ("CSC", 1, 2, 1, 13), "MEp21_13"))
reports[-1].posNum = 278351
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000246861, 0.00118242, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00287037, 0.0309584, 0), \
                           ValErr(1.2311e-07, 0.000612484, 0), \
                           ValErr(0.00154454, 0.00142795, 0), \
                           ValErr(-7.21947e-06, 1.74421e-05, 0), \
                           -150345, 278351, 278351, -nan)
reports[-1].sigmaresid = ValErr(0.415276, 0.000556578, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000980097, None, 4.44697e-07, None, -0.00118546, None, 1.33019e-05, None, -0.00118546, None, 1.33019e-05, None, -0.000498822, None, 8.97526e-07, None, -0.000498822, None, 8.97526e-07, None, 0.415277, None, 0.00561821, None, 0.415277, None, 0.00561821, None)

reports.append(Report(604021368, ("CSC", 1, 2, 1, 15), "MEp21_15"))
reports[-1].posNum = 277857
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00334161, 0.00117882, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0465183, 0.0309902, 0), \
                           ValErr(0.000705714, 0.000612029, 0), \
                           ValErr(-0.00126975, 0.00142522, 0), \
                           ValErr(-4.75374e-07, 1.7409e-05, 0), \
                           -149782, 277857, 277857, -nan)
reports[-1].sigmaresid = ValErr(0.414833, 0.000556478, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00310665, None, 1.78788e-05, None, -0.00262946, None, 3.92343e-05, None, -0.00262946, None, 3.92343e-05, None, -0.000814651, None, 7.37931e-06, None, -0.000814651, None, 7.37931e-06, None, 0.414838, None, 0.00572933, None, 0.414838, None, 0.00572933, None)

reports.append(Report(604021384, ("CSC", 1, 2, 1, 17), "MEp21_17"))
reports[-1].posNum = 278043
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00034574, 0.00119101, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0301724, 0.0311797, 0), \
                           ValErr(0.000375305, 0.000615466, 0), \
                           ValErr(-0.00103046, 0.00143676, 0), \
                           ValErr(7.14499e-06, 1.757e-05, 0), \
                           -152201, 278043, 278043, -nan)
reports[-1].sigmaresid = ValErr(0.418308, 0.000560951, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(2.27314e-05, None, 3.21416e-06, None, 0.000300324, None, 1.2586e-05, None, 0.000300324, None, 1.2586e-05, None, 0.00242111, None, 1.07896e-05, None, 0.00242111, None, 1.07896e-05, None, 0.418309, None, 0.00552049, None, 0.418309, None, 0.00552049, None)

reports.append(Report(604021264, ("CSC", 1, 2, 1, 2), "MEp21_02"))
reports[-1].posNum = 277421
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00136852, 0.0011293, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0163528, 0.0287796, 0), \
                           ValErr(-8.19893e-05, 0.000615967, 0), \
                           ValErr(-0.00243953, 0.00133115, 0), \
                           ValErr(2.30856e-05, 1.91766e-05, 0), \
                           -135261, 277421, 277421, -nan)
reports[-1].sigmaresid = ValErr(0.394012, 0.000538025, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000191806, None, -6.09793e-06, None, 0.000272769, None, 2.89435e-06, None, 0.000272769, None, 2.89435e-06, None, 0.00106039, None, -1.52251e-05, None, 0.00106039, None, -1.52251e-05, None, 0.394015, None, 0.00608297, None, 0.394015, None, 0.00608297, None)

reports.append(Report(604021280, ("CSC", 1, 2, 1, 4), "MEp21_04"))
reports[-1].posNum = 277337
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00313956, 0.00113255, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0106585, 0.0286552, 0), \
                           ValErr(-0.000669559, 0.000564106, 0), \
                           ValErr(0.002234, 0.00132248, 0), \
                           ValErr(-3.28343e-05, 1.66293e-05, 0), \
                           -136509, 277337, 277337, -nan)
reports[-1].sigmaresid = ValErr(0.395848, 0.000531507, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00202538, None, 5.97606e-06, None, 0.00151975, None, 9.26337e-07, None, 0.00151975, None, 9.26337e-07, None, 0.000811162, None, -1.56073e-05, None, 0.000811162, None, -1.56073e-05, None, 0.395852, None, 0.00601866, None, 0.395852, None, 0.00601866, None)

reports.append(Report(604021296, ("CSC", 1, 2, 1, 6), "MEp21_06"))
reports[-1].posNum = 276870
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00177304, 0.00113228, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00474173, 0.0286732, 0), \
                           ValErr(0.000681741, 0.000564728, 0), \
                           ValErr(0.00192891, 0.0013236, 0), \
                           ValErr(-2.28532e-05, 1.66251e-05, 0), \
                           -136304, 276870, 276870, -nan)
reports[-1].sigmaresid = ValErr(0.395883, 0.000532004, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000121231, None, 1.08209e-05, None, 0.0004279, None, 1.24968e-05, None, 0.0004279, None, 1.24968e-05, None, 0.00076243, None, 1.62649e-07, None, 0.00076243, None, 1.62649e-07, None, 0.395887, None, 0.00604933, None, 0.395887, None, 0.00604933, None)

reports.append(Report(604021312, ("CSC", 1, 2, 1, 8), "MEp21_08"))
reports[-1].posNum = 276949
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00258565, 0.00113152, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.015961, 0.0286765, 0), \
                           ValErr(0.000580611, 0.000564681, 0), \
                           ValErr(-0.00156266, 0.00132713, 0), \
                           ValErr(3.05393e-05, 1.6608e-05, 0), \
                           -136081, 276949, 276949, -nan)
reports[-1].sigmaresid = ValErr(0.39551, 0.000531425, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00182611, None, -9.19017e-06, None, -0.00138231, None, 4.76485e-06, None, -0.00138231, None, 4.76485e-06, None, 0.000252391, None, -1.94815e-05, None, 0.000252391, None, -1.94815e-05, None, 0.395513, None, 0.00601481, None, 0.395513, None, 0.00601481, None)

reports.append(Report(604021328, ("CSC", 1, 2, 1, 10), "MEp21_10"))
reports[-1].posNum = 278477
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0020679, 0.001134, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0141817, 0.028791, 0), \
                           ValErr(-0.00121801, 0.00056666, 0), \
                           ValErr(0.0016256, 0.00132794, 0), \
                           ValErr(-1.85311e-05, 1.66878e-05, 0), \
                           -138531, 278477, 278477, -nan)
reports[-1].sigmaresid = ValErr(0.39793, 0.000533208, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00153433, None, -7.35553e-06, None, 0.000944295, None, 3.6334e-06, None, 0.000944295, None, 3.6334e-06, None, 0.000887452, None, -3.24289e-06, None, 0.000887452, None, -3.24289e-06, None, 0.397935, None, 0.00605609, None, 0.397935, None, 0.00605609, None)

reports.append(Report(604021344, ("CSC", 1, 2, 1, 12), "MEp21_12"))
reports[-1].posNum = 277964
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00158982, 0.00113428, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0280072, 0.0286948, 0), \
                           ValErr(0.000135756, 0.000564414, 0), \
                           ValErr(0.00162424, 0.00132377, 0), \
                           ValErr(-5.12244e-07, 1.66566e-05, 0), \
                           -137694, 277964, 277964, -nan)
reports[-1].sigmaresid = ValErr(0.397098, 0.000532585, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00210767, None, 2.75424e-05, None, -0.0025381, None, 5.96706e-05, None, -0.0025381, None, 5.96706e-05, None, -0.000468278, None, 2.80692e-05, None, -0.000468278, None, 2.80692e-05, None, 0.3971, None, 0.00592266, None, 0.3971, None, 0.00592266, None)

reports.append(Report(604021360, ("CSC", 1, 2, 1, 14), "MEp21_14"))
reports[-1].posNum = 278196
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00061087, 0.00113379, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0131965, 0.0287063, 0), \
                           ValErr(-0.000586751, 0.000565175, 0), \
                           ValErr(-0.00218152, 0.00132588, 0), \
                           ValErr(-1.20694e-05, 1.66468e-05, 0), \
                           -137954, 278196, 278196, -nan)
reports[-1].sigmaresid = ValErr(0.397305, 0.000538486, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000223729, None, -4.61695e-06, None, 0.000535364, None, 3.35197e-05, None, 0.000535364, None, 3.35197e-05, None, 0.00106118, None, 2.64158e-05, None, 0.00106118, None, 2.64158e-05, None, 0.39731, None, 0.0059897, None, 0.39731, None, 0.0059897, None)

reports.append(Report(604021376, ("CSC", 1, 2, 1, 16), "MEp21_16"))
reports[-1].posNum = 278429
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00138223, 0.00114632, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0119047, 0.0295586, 0), \
                           ValErr(-0.00172116, 0.000565425, 0), \
                           ValErr(-0.000673555, 0.00132797, 0), \
                           ValErr(-1.86151e-06, 1.81623e-05, 0), \
                           -138618, 278429, 278429, -nan)
reports[-1].sigmaresid = ValErr(0.398089, 0.000538864, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000343224, None, -7.06478e-06, None, -0.00100657, None, 8.09862e-06, None, -0.00100657, None, 8.09862e-06, None, -0.00126396, None, -4.37228e-06, None, -0.00126396, None, -4.37228e-06, None, 0.398096, None, 0.00601415, None, 0.398096, None, 0.00601415, None)

reports.append(Report(604021392, ("CSC", 1, 2, 1, 18), "MEp21_18"))
reports[-1].posNum = 277971
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00136275, 0.00113286, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0410189, 0.0286241, 0), \
                           ValErr(0.000137544, 0.000563403, 0), \
                           ValErr(0.000294925, 0.00132319, 0), \
                           ValErr(4.90841e-07, 1.66169e-05, 0), \
                           -136999, 277971, 277971, -nan)
reports[-1].sigmaresid = ValErr(0.396101, 0.000531241, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00234332, None, 5.77999e-06, None, -0.00152878, None, -1.70305e-06, None, -0.00152878, None, -1.70305e-06, None, -0.000708819, None, -6.12037e-07, None, -0.000708819, None, -6.12037e-07, None, 0.396103, None, 0.00610485, None, 0.396103, None, 0.00610485, None)

reports.append(Report(604021768, ("CSC", 1, 2, 2, 1), "MEp22_01"))
reports[-1].posNum = 72491
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00340077, 0.00623079, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.175838, 0.154353, 0), \
                           ValErr(0.00268494, 0.00171982, 0), \
                           ValErr(0.00266314, 0.0081072, 0), \
                           ValErr(2.25534e-05, 4.78563e-05, 0), \
                           -104541, 72491, 72491, -nan)
reports[-1].sigmaresid = ValErr(1.02346, 0.00268789, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00160886, None, 2.51026e-05, None, 0.00288067, None, 4.38107e-06, None, 0.00288067, None, 4.38107e-06, None, 0.0079575, None, -6.04034e-06, None, 0.0079575, None, -6.04034e-06, None, 1.02349, None, 0.00684048, None, 1.02349, None, 0.00684048, None)

reports.append(Report(604021784, ("CSC", 1, 2, 2, 3), "MEp22_03"))
reports[-1].posNum = 62454
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0102423, 0.00665881, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.199576, 0.164795, 0), \
                           ValErr(-0.0018291, 0.0018071, 0), \
                           ValErr(0.00947564, 0.00873683, 0), \
                           ValErr(-2.37281e-05, 4.97743e-05, 0), \
                           -87613.3, 62454, 62454, -nan)
reports[-1].sigmaresid = ValErr(0.984035, 0.0027843, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00536825, None, -3.18687e-05, None, 0.00470394, None, -4.56791e-05, None, 0.00470394, None, -4.56791e-05, None, -0.00206808, None, -4.8942e-05, None, -0.00206808, None, -4.8942e-05, None, 0.98406, None, 0.00703366, None, 0.98406, None, 0.00703366, None)

reports.append(Report(604021800, ("CSC", 1, 2, 2, 5), "MEp22_05"))
reports[-1].posNum = 72523
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00139477, 0.00601669, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.432468, 0.156151, 0), \
                           ValErr(0.000558802, 0.00173995, 0), \
                           ValErr(-0.0131882, 0.00812056, 0), \
                           ValErr(-3.79985e-05, 4.66288e-05, 0), \
                           -103651, 72523, 72523, -nan)
reports[-1].sigmaresid = ValErr(1.01033, 0.00265284, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00312364, None, -2.18307e-06, None, 0.00609211, None, -3.95086e-05, None, 0.00609211, None, -3.95086e-05, None, 0.00535715, None, 2.73056e-06, None, 0.00535715, None, 2.73056e-06, None, 1.01042, None, 0.00667594, None, 1.01042, None, 0.00667594, None)

reports.append(Report(604021816, ("CSC", 1, 2, 2, 7), "MEp22_07"))
reports[-1].posNum = 62481
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00526286, 0.00674016, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0979154, 0.163988, 0), \
                           ValErr(-0.000933969, 0.00179911, 0), \
                           ValErr(0.00362982, 0.00872603, 0), \
                           ValErr(-5.20969e-05, 5.01659e-05, 0), \
                           -88445.5, 62481, 62481, -nan)
reports[-1].sigmaresid = ValErr(0.996625, 0.00281931, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00787746, None, 5.8838e-06, None, -0.00917972, None, 9.02051e-06, None, -0.00917972, None, 9.02051e-06, None, -0.00975849, None, 1.00692e-05, None, -0.00975849, None, 1.00692e-05, None, 0.996638, None, 0.00646084, None, 0.996638, None, 0.00646084, None)

reports.append(Report(604021832, ("CSC", 1, 2, 2, 9), "MEp22_09"))
reports[-1].posNum = 66095
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0100783, 0.00639921, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.244638, 0.164748, 0), \
                           ValErr(0.000994188, 0.00181189, 0), \
                           ValErr(-0.00719699, 0.00856087, 0), \
                           ValErr(-5.62104e-06, 4.88898e-05, 0), \
                           -95129.7, 66095, 66095, -nan)
reports[-1].sigmaresid = ValErr(1.02055, 0.00280696, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00527238, None, 3.81878e-05, None, -0.00705277, None, 4.59553e-05, None, -0.00705277, None, 4.59553e-05, None, -0.00812995, None, 3.96185e-05, None, -0.00812995, None, 3.96185e-05, None, 1.02058, None, 0.00803583, None, 1.02058, None, 0.00803583, None)

reports.append(Report(604021848, ("CSC", 1, 2, 2, 11), "MEp22_11"))
reports[-1].posNum = 65335
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0053336, 0.00639699, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.122191, 0.104918, 0), \
                           ValErr(-0.00124964, 0.00174183, 0), \
                           ValErr(-0.00595739, 0.00859064, 0), \
                           ValErr(9.17503e-05, 4.75427e-05, 0), \
                           -93149.1, 65335, 65335, -nan)
reports[-1].sigmaresid = ValErr(1.0068, 0.00272895, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00755651, None, -1.29563e-05, None, 0.00103981, None, 1.17417e-06, None, 0.00103981, None, 1.17417e-06, None, -0.00368352, None, -1.81585e-05, None, -0.00368352, None, -1.81585e-05, None, 1.00684, None, 0.0065124, None, 1.00684, None, 0.0065124, None)

reports.append(Report(604021864, ("CSC", 1, 2, 2, 13), "MEp22_13"))
reports[-1].posNum = 60849
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00379414, 0.00687796, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.108912, 0.166374, 0), \
                           ValErr(-0.00180974, 0.00181869, 0), \
                           ValErr(0.0192053, 0.00885532, 0), \
                           ValErr(3.94872e-06, 5.08669e-05, 0), \
                           -86179.6, 60849, 60849, -nan)
reports[-1].sigmaresid = ValErr(0.997356, 0.00285898, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0138038, None, 2.7265e-07, None, -0.0128581, None, -7.06084e-06, None, -0.0128581, None, -7.06084e-06, None, -0.0155417, None, 7.17293e-05, None, -0.0155417, None, 7.17293e-05, None, 0.99741, None, 0.00657981, None, 0.99741, None, 0.00657981, None)

reports.append(Report(604021880, ("CSC", 1, 2, 2, 15), "MEp22_15"))
reports[-1].posNum = 73737
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00516908, 0.00605078, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.25325, 0.153883, 0), \
                           ValErr(-0.00163173, 0.00171946, 0), \
                           ValErr(0.00166772, 0.00803336, 0), \
                           ValErr(1.90283e-05, 4.67955e-05, 0), \
                           -105994, 73737, 73737, -nan)
reports[-1].sigmaresid = ValErr(1.01869, 0.00265269, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000708339, None, 6.09639e-06, None, 0.00506539, None, 2.25499e-06, None, 0.00506539, None, 2.25499e-06, None, 0.0119701, None, -8.70718e-06, None, 0.0119701, None, -8.70718e-06, None, 1.01871, None, 0.00725029, None, 1.01871, None, 0.00725029, None)

reports.append(Report(604021896, ("CSC", 1, 2, 2, 17), "MEp22_17"))
reports[-1].posNum = 61630
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0161184, 0.00661318, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.478159, 0.167791, 0), \
                           ValErr(0.00190405, 0.00182126, 0), \
                           ValErr(-0.00575573, 0.00881182, 0), \
                           ValErr(0.000134606, 4.95779e-05, 0), \
                           -86593.2, 61630, 61630, -nan)
reports[-1].sigmaresid = ValErr(0.98621, 0.00280906, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0047319, None, 8.9301e-06, None, -0.0074914, None, -3.76204e-05, None, -0.0074914, None, -3.76204e-05, None, -0.00533525, None, 1.67463e-06, None, -0.00533525, None, 1.67463e-06, None, 0.986334, None, 0.00665632, None, 0.986334, None, 0.00665632, None)

reports.append(Report(604021912, ("CSC", 1, 2, 2, 19), "MEp22_19"))
reports[-1].posNum = 72902
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00626421, 0.00621376, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.051826, 0.153072, 0), \
                           ValErr(0.00143527, 0.00170334, 0), \
                           ValErr(0.0128045, 0.00807326, 0), \
                           ValErr(-7.94578e-05, 4.73557e-05, 0), \
                           -104890, 72902, 72902, -nan)
reports[-1].sigmaresid = ValErr(1.02004, 0.00267136, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00299316, None, -1.62666e-05, None, -0.00306593, None, -9.25405e-06, None, -0.00306593, None, -9.25405e-06, None, -0.00934359, None, 2.69593e-05, None, -0.00934359, None, 2.69593e-05, None, 1.02007, None, 0.00674289, None, 1.02007, None, 0.00674289, None)

reports.append(Report(604021928, ("CSC", 1, 2, 2, 21), "MEp22_21"))
reports[-1].posNum = 60883
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00720581, 0.00662805, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0852372, 0.167414, 0), \
                           ValErr(0.000844799, 0.00182184, 0), \
                           ValErr(0.00680628, 0.00878865, 0), \
                           ValErr(-4.0352e-05, 4.95426e-05, 0), \
                           -85176.9, 60883, 60883, -nan)
reports[-1].sigmaresid = ValErr(0.980285, 0.00280925, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00268622, None, -2.17199e-05, None, 0.00227434, None, -1.01751e-05, None, 0.00227434, None, -1.01751e-05, None, 0.00402531, None, 2.22472e-05, None, 0.00402531, None, 2.22472e-05, None, 0.980296, None, 0.00704406, None, 0.980296, None, 0.00704406, None)

reports.append(Report(604021944, ("CSC", 1, 2, 2, 23), "MEp22_23"))
reports[-1].posNum = 72796
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0109826, 0.00608452, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0374856, 0.0862961, 0), \
                           ValErr(-0.000133343, 0.00170322, 0), \
                           ValErr(-0.00168285, 0.0077694, 0), \
                           ValErr(3.3758e-06, 3.48187e-05, 0), \
                           -104361, 72796, 72796, -nan)
reports[-1].sigmaresid = ValErr(1.01477, 0.00265536, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0125444, None, 1.72609e-05, None, -0.0100505, None, 1.17305e-05, None, -0.0100505, None, 1.17305e-05, None, -0.0128959, None, 3.44518e-05, None, -0.0128959, None, 3.44518e-05, None, 1.01477, None, 0.00679838, None, 1.01477, None, 0.00679838, None)

reports.append(Report(604021960, ("CSC", 1, 2, 2, 25), "MEp22_25"))
reports[-1].posNum = 63503
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00398807, 0.00667373, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.369918, 0.161918, 0), \
                           ValErr(-0.00249743, 0.00177691, 0), \
                           ValErr(0.0061895, 0.00862777, 0), \
                           ValErr(-3.20432e-05, 4.97496e-05, 0), \
                           -89820, 63503, 63503, -nan)
reports[-1].sigmaresid = ValErr(0.995495, 0.00279337, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00558845, None, 2.71316e-05, None, -0.00819673, None, 9.1748e-06, None, -0.00819673, None, 9.1748e-06, None, -0.0116399, None, 3.1558e-05, None, -0.0116399, None, 3.1558e-05, None, 0.995549, None, 0.00646904, None, 0.995549, None, 0.00646904, None)

reports.append(Report(604021976, ("CSC", 1, 2, 2, 27), "MEp22_27"))
reports[-1].posNum = 66073
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00940782, 0.00644566, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.13173, 0.0905933, 0), \
                           ValErr(-0.000758103, 0.00106656, 0), \
                           ValErr(0.026062, 0.00848897, 0), \
                           ValErr(-1.83048e-05, 4.69307e-05, 0), \
                           -94745.7, 66073, 66073, -nan)
reports[-1].sigmaresid = ValErr(1.01513, 0.00278638, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00348754, None, 1.76275e-05, None, -0.00379459, None, -1.29851e-05, None, -0.00379459, None, -1.29851e-05, None, -0.00399695, None, 4.20699e-05, None, -0.00399695, None, 4.20699e-05, None, 1.01521, None, 0.00672453, None, 1.01521, None, 0.00672453, None)

reports.append(Report(604021992, ("CSC", 1, 2, 2, 29), "MEp22_29"))
reports[-1].posNum = 67007
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00866096, 0.00632477, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.2072, 0.161701, 0), \
                           ValErr(0.000783172, 0.00178722, 0), \
                           ValErr(0.0135891, 0.00841693, 0), \
                           ValErr(-3.47659e-05, 4.84633e-05, 0), \
                           -95462.4, 67007, 67007, -nan)
reports[-1].sigmaresid = ValErr(1.00574, 0.00274734, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00672224, None, 8.48285e-07, None, 0.00111906, None, -3.24919e-06, None, 0.00111906, None, -3.24919e-06, None, -0.00172502, None, 7.75387e-06, None, -0.00172502, None, 7.75387e-06, None, 1.00578, None, 0.00641134, None, 1.00578, None, 0.00641134, None)

reports.append(Report(604022008, ("CSC", 1, 2, 2, 31), "MEp22_31"))
reports[-1].posNum = 63410
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00410627, 0.00674691, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.134422, 0.162403, 0), \
                           ValErr(-0.00101012, 0.00179172, 0), \
                           ValErr(-0.000144558, 0.00870036, 0), \
                           ValErr(2.51069e-05, 4.99726e-05, 0), \
                           -89507.5, 63410, 63410, -nan)
reports[-1].sigmaresid = ValErr(0.992657, 0.00278744, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00602814, None, 1.717e-05, None, -0.00309302, None, 4.96281e-05, None, -0.00309302, None, 4.96281e-05, None, -0.00198365, None, 4.43696e-05, None, -0.00198365, None, 4.43696e-05, None, 0.992666, None, 0.00649592, None, 0.992666, None, 0.00649592, None)

reports.append(Report(604022024, ("CSC", 1, 2, 2, 33), "MEp22_33"))
reports[-1].posNum = 72398
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00753424, 0.00605743, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0255004, 0.154105, 0), \
                           ValErr(-0.00076461, 0.00171444, 0), \
                           ValErr(0.00114906, 0.00804889, 0), \
                           ValErr(6.29566e-05, 4.65922e-05, 0), \
                           -103611, 72398, 72398, -nan)
reports[-1].sigmaresid = ValErr(1.01227, 0.00266023, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00327721, None, 7.09214e-06, None, -0.00576925, None, -2.26115e-05, None, -0.00576925, None, -2.26115e-05, None, -0.00996192, None, 4.11983e-06, None, -0.00996192, None, 4.11983e-06, None, 1.01229, None, 0.0068707, None, 1.01229, None, 0.0068707, None)

reports.append(Report(604022040, ("CSC", 1, 2, 2, 35), "MEp22_35"))
reports[-1].posNum = 60125
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00717677, 0.00667723, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0890183, 0.169005, 0), \
                           ValErr(0.000591337, 0.00181876, 0), \
                           ValErr(0.000749546, 0.00890333, 0), \
                           ValErr(9.64613e-05, 4.93377e-05, 0), \
                           -83817.3, 60125, 60125, -nan)
reports[-1].sigmaresid = ValErr(0.97542, 0.00281287, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0017039, None, -5.09648e-06, None, -0.00313381, None, -4.56489e-06, None, -0.00313381, None, -4.56489e-06, None, -0.00221673, None, -3.78161e-05, None, -0.00221673, None, -3.78161e-05, None, 0.975458, None, 0.00647463, None, 0.975458, None, 0.00647463, None)

reports.append(Report(604021776, ("CSC", 1, 2, 2, 2), "MEp22_02"))
reports[-1].posNum = 64895
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00477828, 0.00637358, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0482055, 0.128679, 0), \
                           ValErr(0.000852646, 0.00141681, 0), \
                           ValErr(-0.017555, 0.00827356, 0), \
                           ValErr(3.16569e-06, 4.87191e-05, 0), \
                           -92347.4, 64895, 64895, -nan)
reports[-1].sigmaresid = ValErr(1.0041, 0.00278742, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00164277, None, 1.18589e-06, None, 0.00394749, None, -2.09865e-05, None, 0.00394749, None, -2.09865e-05, None, 0.00227648, None, -7.07655e-06, None, 0.00227648, None, -7.07655e-06, None, 1.00414, None, 0.00685054, None, 1.00414, None, 0.00685054, None)

reports.append(Report(604021792, ("CSC", 1, 2, 2, 4), "MEp22_04"))
reports[-1].posNum = 59802
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0112491, 0.00673708, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0216596, 0.10835, 0), \
                           ValErr(-9.72235e-05, 0.00176988, 0), \
                           ValErr(0.00391803, 0.00879861, 0), \
                           ValErr(-9.96068e-05, 5.01648e-05, 0), \
                           -84629.1, 59802, 59802, -nan)
reports[-1].sigmaresid = ValErr(0.996223, 0.00287466, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00395873, None, 7.34966e-06, None, 0.00507435, None, 6.5591e-08, None, 0.00507435, None, 6.5591e-08, None, 0.0124548, None, -1.9955e-05, None, 0.0124548, None, -1.9955e-05, None, 0.996257, None, 0.00642376, None, 0.996257, None, 0.00642376, None)

reports.append(Report(604021808, ("CSC", 1, 2, 2, 6), "MEp22_06"))
reports[-1].posNum = 70056
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00772558, 0.00618204, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.445293, 0.151146, 0), \
                           ValErr(0.00393119, 0.00168109, 0), \
                           ValErr(-0.0233462, 0.00792584, 0), \
                           ValErr(-3.72396e-05, 4.73933e-05, 0), \
                           -99922.7, 70056, 70056, -nan)
reports[-1].sigmaresid = ValErr(1.00741, 0.00269135, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000210732, None, 2.87073e-05, None, 0.00255334, None, 1.73994e-05, None, 0.00255334, None, 1.73994e-05, None, 0.0109324, None, -1.01247e-05, None, 0.0109324, None, -1.01247e-05, None, 1.0076, None, 0.00685751, None, 1.0076, None, 0.00685751, None)

reports.append(Report(604021824, ("CSC", 1, 2, 2, 8), "MEp22_08"))
reports[-1].posNum = 57725
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0103196, 0.0068518, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.1309, 0.156238, 0), \
                           ValErr(-0.00052191, 0.00140774, 0), \
                           ValErr(0.0132826, 0.00853874, 0), \
                           ValErr(-8.838e-05, 4.56449e-05, 0), \
                           -81165.2, 57725, 57725, -nan)
reports[-1].sigmaresid = ValErr(0.98721, 0.0028948, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000951896, None, 4.1658e-06, None, 5.03172e-06, None, 1.88378e-06, None, 5.03172e-06, None, 1.88378e-06, None, 0.00552002, None, 1.89238e-05, None, 0.00552002, None, 1.89238e-05, None, 0.987251, None, 0.00658428, None, 0.987251, None, 0.00658428, None)

reports.append(Report(604021840, ("CSC", 1, 2, 2, 10), "MEp22_10"))
reports[-1].posNum = 73269
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000302743, 0.00613156, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.139754, 0.149875, 0), \
                           ValErr(0.00215103, 0.00167071, 0), \
                           ValErr(-0.00213679, 0.00789953, 0), \
                           ValErr(-8.07393e-06, 4.69848e-05, 0), \
                           -104916, 73269, 73269, -nan)
reports[-1].sigmaresid = ValErr(1.01308, 0.00264648, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00177639, None, 2.30581e-05, None, 0.000427483, None, 8.55954e-06, None, 0.000427483, None, 8.55954e-06, None, 0.00313905, None, 1.05753e-05, None, 0.00313905, None, 1.05753e-05, None, 1.01309, None, 0.00681248, None, 1.01309, None, 0.00681248, None)

reports.append(Report(604021856, ("CSC", 1, 2, 2, 12), "MEp22_12"))
reports[-1].posNum = 58651
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00366108, 0.00670446, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0859233, 0.162728, 0), \
                           ValErr(-0.00412182, 0.00175071, 0), \
                           ValErr(0.00154195, 0.00860491, 0), \
                           ValErr(6.02016e-05, 4.9952e-05, 0), \
                           -82029.2, 58651, 58651, -nan)
reports[-1].sigmaresid = ValErr(0.979865, 0.00286097, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000723665, None, 1.24309e-06, None, -0.00176787, None, -7.52829e-06, None, -0.00176787, None, -7.52829e-06, None, -0.00880418, None, 2.38506e-05, None, -0.00880418, None, 2.38506e-05, None, 0.979926, None, 0.00665143, None, 0.979926, None, 0.00665143, None)

reports.append(Report(604021872, ("CSC", 1, 2, 2, 14), "MEp22_14"))
reports[-1].posNum = 70792
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00803285, 0.00620763, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0445402, 0.151771, 0), \
                           ValErr(-0.00131786, 0.00168288, 0), \
                           ValErr(-0.00443814, 0.00797932, 0), \
                           ValErr(3.38422e-05, 4.74541e-05, 0), \
                           -101475, 70792, 70792, -nan)
reports[-1].sigmaresid = ValErr(1.01459, 0.0026964, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0069717, None, 2.03373e-05, None, -0.00454248, None, -1.51551e-05, None, -0.00454248, None, -1.51551e-05, None, -0.00130312, None, -8.06886e-06, None, -0.00130312, None, -8.06886e-06, None, 1.0146, None, 0.0066025, None, 1.0146, None, 0.0066025, None)

reports.append(Report(604021888, ("CSC", 1, 2, 2, 16), "MEp22_16"))
reports[-1].posNum = 59835
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00193354, 0.00667981, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.00670643, 0.167982, 0), \
                           ValErr(-0.00142959, 0.0017881, 0), \
                           ValErr(-0.00922713, 0.00879445, 0), \
                           ValErr(-2.36666e-06, 4.97803e-05, 0), \
                           -84466.9, 59835, 59835, -nan)
reports[-1].sigmaresid = ValErr(0.992747, 0.00286975, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00877757, None, -1.63238e-05, None, 0.00620643, None, -2.52524e-05, None, 0.00620643, None, -2.52524e-05, None, -0.00216328, None, 8.90089e-06, None, -0.00216328, None, 8.90089e-06, None, 0.992768, None, 0.0065956, None, 0.992768, None, 0.0065956, None)

reports.append(Report(604021904, ("CSC", 1, 2, 2, 18), "MEp22_18"))
reports[-1].posNum = 64118
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00513936, 0.00652784, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0497736, 0.157472, 0), \
                           ValErr(-0.000999667, 0.00173164, 0), \
                           ValErr(0.00346399, 0.00828042, 0), \
                           ValErr(-5.33733e-05, 4.94739e-05, 0), \
                           -91798.2, 64118, 64118, -nan)
reports[-1].sigmaresid = ValErr(1.01285, 0.0028284, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00125172, None, 2.6082e-06, None, 0.00146705, None, -4.21624e-05, None, 0.00146705, None, -4.21624e-05, None, 0.00637671, None, 8.61729e-08, None, 0.00637671, None, 8.61729e-08, None, 1.01286, None, 0.0070446, None, 1.01286, None, 0.0070446, None)

reports.append(Report(604021920, ("CSC", 1, 2, 2, 20), "MEp22_20"))
reports[-1].posNum = 65559
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00699257, 0.00643628, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0549077, 0.157035, 0), \
                           ValErr(-0.00265282, 0.00171763, 0), \
                           ValErr(0.000560867, 0.00826968, 0), \
                           ValErr(-2.55244e-05, 4.86925e-05, 0), \
                           -93317.3, 65559, 65559, -nan)
reports[-1].sigmaresid = ValErr(1.00448, 0.00277403, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00790125, None, -5.02639e-05, None, 0.00574314, None, -8.397e-05, None, 0.00574314, None, -8.397e-05, None, 0.0116806, None, -4.1807e-05, None, 0.0116806, None, -4.1807e-05, None, 1.0045, None, 0.00655979, None, 1.0045, None, 0.00655979, None)

reports.append(Report(604021936, ("CSC", 1, 2, 2, 22), "MEp22_22"))
reports[-1].posNum = 60493
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00890847, 0.00664464, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.152316, 0.164658, 0), \
                           ValErr(-0.00209487, 0.00176953, 0), \
                           ValErr(0.00956641, 0.00863074, 0), \
                           ValErr(-5.50219e-05, 4.9613e-05, 0), \
                           -85269.4, 60493, 60493, -nan)
reports[-1].sigmaresid = ValErr(0.99068, 0.00284817, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00208983, None, 8.58739e-06, None, 0.00177839, None, 1.02836e-05, None, 0.00177839, None, 1.02836e-05, None, -0.0038278, None, 4.01246e-05, None, -0.0038278, None, 4.01246e-05, None, 0.990711, None, 0.00674311, None, 0.990711, None, 0.00674311, None)

reports.append(Report(604021952, ("CSC", 1, 2, 2, 24), "MEp22_24"))
reports[-1].posNum = 70345
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0083766, 0.00616595, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0425527, 0.130021, 0), \
                           ValErr(0.000161738, 0.0012969, 0), \
                           ValErr(-0.00369293, 0.00789791, 0), \
                           ValErr(-0.000110595, 4.7351e-05, 0), \
                           -100487, 70345, 70345, -nan)
reports[-1].sigmaresid = ValErr(1.0096, 0.00268712, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00256405, None, -2.87296e-05, None, 0.00600544, None, -4.62603e-05, None, 0.00600544, None, -4.62603e-05, None, 0.00955437, None, -1.02101e-05, None, 0.00955437, None, -1.02101e-05, None, 1.00965, None, 0.00704423, None, 1.00965, None, 0.00704423, None)

reports.append(Report(604021968, ("CSC", 1, 2, 2, 26), "MEp22_26"))
reports[-1].posNum = 58591
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0140579, 0.00683966, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.00422095, 0.163674, 0), \
                           ValErr(-0.00119666, 0.00175408, 0), \
                           ValErr(-0.0133685, 0.00875504, 0), \
                           ValErr(3.96738e-05, 4.98496e-05, 0), \
                           -82393.5, 58591, 58591, -nan)
reports[-1].sigmaresid = ValErr(0.987391, 0.00288442, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00190291, None, 1.08685e-05, None, -0.00578707, None, -1.2906e-05, None, -0.00578707, None, -1.2906e-05, None, -0.0105809, None, -2.89016e-05, None, -0.0105809, None, -2.89016e-05, None, 0.987415, None, 0.00670552, None, 0.987415, None, 0.00670552, None)

reports.append(Report(604021984, ("CSC", 1, 2, 2, 28), "MEp22_28"))
reports[-1].posNum = 72318
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00697475, 0.00619169, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.108493, 0.150461, 0), \
                           ValErr(0.00320483, 0.00168462, 0), \
                           ValErr(-0.000903937, 0.00794447, 0), \
                           ValErr(4.05845e-05, 4.74072e-05, 0), \
                           -103201, 72318, 72318, -nan)
reports[-1].sigmaresid = ValErr(1.00814, 0.00265084, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00196901, None, -2.97683e-05, None, -0.0049366, None, -5.94778e-05, None, -0.0049366, None, -5.94778e-05, None, -0.00303261, None, -7.00209e-05, None, -0.00303261, None, -7.00209e-05, None, 1.00817, None, 0.00703559, None, 1.00817, None, 0.00703559, None)

reports.append(Report(604022000, ("CSC", 1, 2, 2, 30), "MEp22_30"))
reports[-1].posNum = 57699
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0074996, 0.00679363, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.362428, 0.163379, 0), \
                           ValErr(0.00146167, 0.0017473, 0), \
                           ValErr(0.00918176, 0.0086416, 0), \
                           ValErr(3.94814e-05, 5.02489e-05, 0), \
                           -80917.7, 57699, 57699, -nan)
reports[-1].sigmaresid = ValErr(0.983609, 0.0028955, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0109858, None, 8.59748e-06, None, -0.0105158, None, -7.67534e-08, None, -0.0105158, None, -7.67534e-08, None, -0.0143067, None, 1.57334e-05, None, -0.0143067, None, 1.57334e-05, None, 0.983678, None, 0.00655138, None, 0.983678, None, 0.00655138, None)

reports.append(Report(604022016, ("CSC", 1, 2, 2, 32), "MEp22_32"))
reports[-1].posNum = 70411
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00299009, 0.00622117, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.309802, 0.152598, 0), \
                           ValErr(0.00050278, 0.00168516, 0), \
                           ValErr(-0.00908004, 0.00802219, 0), \
                           ValErr(6.04199e-05, 4.75638e-05, 0), \
                           -100859, 70411, 70411, -nan)
reports[-1].sigmaresid = ValErr(1.01358, 0.00270099, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00115973, None, 8.68801e-06, None, 0.00381891, None, 3.5975e-06, None, 0.00381891, None, 3.5975e-06, None, -0.00212595, None, 4.08952e-05, None, -0.00212595, None, 4.08952e-05, None, 1.01363, None, 0.00669659, None, 1.01363, None, 0.00669659, None)

reports.append(Report(604022032, ("CSC", 1, 2, 2, 34), "MEp22_34"))
reports[-1].posNum = 61857
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0168552, 0.006547, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.119733, 0.157818, 0), \
                           ValErr(0.000336285, 0.00143169, 0), \
                           ValErr(0.0109587, 0.00840068, 0), \
                           ValErr(-8.69637e-06, 4.38944e-05, 0), \
                           -87627.3, 61857, 61857, -nan)
reports[-1].sigmaresid = ValErr(0.997675, 0.00282825, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0132309, None, -3.49037e-05, None, 0.0113087, None, -4.46104e-06, None, 0.0113087, None, -4.46104e-06, None, 0.00808134, None, 8.52849e-06, None, 0.00808134, None, 8.52849e-06, None, 0.997693, None, 0.00942196, None, 0.997693, None, 0.00942196, None)

reports.append(Report(604022048, ("CSC", 1, 2, 2, 36), "MEp22_36"))
reports[-1].posNum = 66499
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0116224, 0.00639104, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0321258, 0.155729, 0), \
                           ValErr(0.00138048, 0.00171459, 0), \
                           ValErr(-0.0124079, 0.00813852, 0), \
                           ValErr(-3.27398e-05, 4.87498e-05, 0), \
                           -95140.9, 66499, 66499, -nan)
reports[-1].sigmaresid = ValErr(1.01184, 0.00277453, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00385345, None, 2.15142e-05, None, -0.00680005, None, 2.25666e-05, None, -0.00680005, None, 2.25666e-05, None, -0.00626547, None, 3.61542e-05, None, -0.00626547, None, 3.61542e-05, None, 1.01188, None, 0.00703271, None, 1.01188, None, 0.00703271, None)

reports.append(Report(604025352, ("CSC", 1, 3, 1, 1), "MEp31_01"))
reports[-1].posNum = 223356
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00276065, 0.00157457, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.00814522, 0.04346, 0), \
                           ValErr(-0.00086634, 0.000974292, 0), \
                           ValErr(-0.00138709, 0.00194623, 0), \
                           ValErr(-2.79906e-05, 2.58282e-05, 0), \
                           -161934, 223356, 223356, -nan)
reports[-1].sigmaresid = ValErr(0.499606, 0.000747506, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00115533, None, 1.96619e-05, None, 0.00183167, None, 4.91972e-05, None, 0.00183167, None, 4.91972e-05, None, -0.000870158, None, 2.78531e-05, None, -0.000870158, None, 2.78531e-05, None, 0.499608, None, 0.00623282, None, 0.499608, None, 0.00623282, None)

reports.append(Report(604025368, ("CSC", 1, 3, 1, 3), "MEp31_03"))
reports[-1].posNum = 223995
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000621773, 0.00157307, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.010473, 0.0434573, 0), \
                           ValErr(0.000312633, 0.000970173, 0), \
                           ValErr(0.00138754, 0.00194225, 0), \
                           ValErr(1.98313e-05, 2.57595e-05, 0), \
                           -162657, 223995, 223995, -nan)
reports[-1].sigmaresid = ValErr(0.500185, 0.000747303, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00127289, None, -1.10984e-05, None, 0.0015177, None, -1.04859e-06, None, 0.0015177, None, -1.04859e-06, None, -0.000443968, None, -1.08279e-05, None, -0.000443968, None, -1.08279e-05, None, 0.500186, None, 0.00644501, None, 0.500186, None, 0.00644501, None)

reports.append(Report(604025384, ("CSC", 1, 3, 1, 5), "MEp31_05"))
reports[-1].posNum = 223772
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00056739, 0.00157152, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0148405, 0.0432822, 0), \
                           ValErr(-0.00176098, 0.000967765, 0), \
                           ValErr(9.02604e-05, 0.00193746, 0), \
                           ValErr(-5.70356e-06, 2.61136e-05, 0), \
                           -161792, 223772, 223772, -nan)
reports[-1].sigmaresid = ValErr(0.498617, 0.000748307, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000209225, None, -1.62985e-05, None, -0.000542284, None, -2.17583e-06, None, -0.000542284, None, -2.17583e-06, None, 0.000263237, None, -9.42175e-06, None, 0.000263237, None, -9.42175e-06, None, 0.498621, None, 0.00596671, None, 0.498621, None, 0.00596671, None)

reports.append(Report(604025400, ("CSC", 1, 3, 1, 7), "MEp31_07"))
reports[-1].posNum = 223788
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00224513, 0.0015755, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0551066, 0.0436457, 0), \
                           ValErr(-0.00103134, 0.000974843, 0), \
                           ValErr(-0.00157765, 0.00194678, 0), \
                           ValErr(-2.20803e-05, 2.58346e-05, 0), \
                           -163061, 223788, 223788, -nan)
reports[-1].sigmaresid = ValErr(0.501426, 0.000749504, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000989028, None, -1.22774e-05, None, 0.0012346, None, -2.1114e-05, None, 0.0012346, None, -2.1114e-05, None, 0.000387168, None, -1.6347e-05, None, 0.000387168, None, -1.6347e-05, None, 0.501432, None, 0.00612145, None, 0.501432, None, 0.00612145, None)

reports.append(Report(604025416, ("CSC", 1, 3, 1, 9), "MEp31_09"))
reports[-1].posNum = 223240
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000637476, 0.00156755, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0458571, 0.0432509, 0), \
                           ValErr(-0.00197657, 0.000966186, 0), \
                           ValErr(0.00057891, 0.00193801, 0), \
                           ValErr(3.72649e-06, 2.5683e-05, 0), \
                           -160545, 223240, 223240, -nan)
reports[-1].sigmaresid = ValErr(0.496695, 0.00074334, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000300028, None, 1.0485e-05, None, -0.000287166, None, 1.23361e-05, None, -0.000287166, None, 1.23361e-05, None, -0.00227556, None, -2.35164e-05, None, -0.00227556, None, -2.35164e-05, None, 0.496703, None, 0.00604254, None, 0.496703, None, 0.00604254, None)

reports.append(Report(604025432, ("CSC", 1, 3, 1, 11), "MEp31_11"))
reports[-1].posNum = 222980
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(8.52718e-05, 0.00156468, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0510109, 0.0433556, 0), \
                           ValErr(-0.00209386, 0.000968269, 0), \
                           ValErr(-0.000947535, 0.0019359, 0), \
                           ValErr(-1.47177e-05, 2.56734e-05, 0), \
                           -160390, 222980, 222980, -nan)
reports[-1].sigmaresid = ValErr(0.496767, 0.000743885, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000422096, None, -5.72187e-06, None, -0.000520578, None, -1.15378e-05, None, -0.000520578, None, -1.15378e-05, None, 0.000862977, None, -2.38497e-06, None, 0.000862977, None, -2.38497e-06, None, 0.496772, None, 0.00603711, None, 0.496772, None, 0.00603711, None)

reports.append(Report(604025448, ("CSC", 1, 3, 1, 13), "MEp31_13"))
reports[-1].posNum = 222208
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00129821, 0.00157177, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00791725, 0.0434429, 0), \
                           ValErr(0.00183826, 0.000969748, 0), \
                           ValErr(0.00184112, 0.0019414, 0), \
                           ValErr(-9.47657e-07, 2.57957e-05, 0), \
                           -160105, 222208, 222208, -nan)
reports[-1].sigmaresid = ValErr(0.497371, 0.000746081, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000578204, None, -1.80262e-05, None, -0.000245529, None, -1.76422e-05, None, -0.000245529, None, -1.76422e-05, None, 0.00046169, None, -3.93038e-06, None, 0.00046169, None, -3.93038e-06, None, 0.497376, None, 0.00583854, None, 0.497376, None, 0.00583854, None)

reports.append(Report(604025464, ("CSC", 1, 3, 1, 15), "MEp31_15"))
reports[-1].posNum = 221975
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0037667, 0.00157043, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0368319, 0.0435193, 0), \
                           ValErr(0.000283417, 0.00097424, 0), \
                           ValErr(-0.00274236, 0.00194516, 0), \
                           ValErr(2.62777e-05, 2.57814e-05, 0), \
                           -160033, 221975, 221975, -nan)
reports[-1].sigmaresid = ValErr(0.497586, 0.000746795, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00292397, None, 1.62011e-05, None, 0.00231745, None, 6.07795e-06, None, 0.00231745, None, 6.07795e-06, None, 0.00333753, None, 1.00668e-05, None, 0.00333753, None, 1.00668e-05, None, 0.497592, None, 0.00596668, None, 0.497592, None, 0.00596668, None)

reports.append(Report(604025480, ("CSC", 1, 3, 1, 17), "MEp31_17"))
reports[-1].posNum = 222117
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00207757, 0.00158542, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0537435, 0.0437887, 0), \
                           ValErr(6.81146e-06, 0.000978768, 0), \
                           ValErr(0.00172213, 0.00195808, 0), \
                           ValErr(3.39078e-05, 2.60465e-05, 0), \
                           -161886, 222117, 222117, -nan)
reports[-1].sigmaresid = ValErr(0.501523, 0.000752461, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000575794, None, -1.08021e-05, None, -0.000926775, None, -1.98864e-05, None, -0.000926775, None, -1.98864e-05, None, -0.00147412, None, -2.23089e-05, None, -0.00147412, None, -2.23089e-05, None, 0.501528, None, 0.00598067, None, 0.501528, None, 0.00598067, None)

reports.append(Report(604025360, ("CSC", 1, 3, 1, 2), "MEp31_02"))
reports[-1].posNum = 229601
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00173235, 0.00159802, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0326035, 0.0453559, 0), \
                           ValErr(-0.000405542, 0.00101284, 0), \
                           ValErr(-0.00078588, 0.00203055, 0), \
                           ValErr(3.46799e-05, 2.62078e-05, 0), \
                           -172901, 229601, 229601, -nan)
reports[-1].sigmaresid = ValErr(0.513817, 0.00075824, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000877986, None, -8.48222e-06, None, -0.00200619, None, -5.50157e-06, None, -0.00200619, None, -5.50157e-06, None, -0.00358964, None, -2.20863e-06, None, -0.00358964, None, -2.20863e-06, None, 0.51382, None, 0.00582664, None, 0.51382, None, 0.00582664, None)

reports.append(Report(604025376, ("CSC", 1, 3, 1, 4), "MEp31_04"))
reports[-1].posNum = 229436
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000732428, 0.00160064, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0399602, 0.0455342, 0), \
                           ValErr(0.000487426, 0.00101559, 0), \
                           ValErr(-0.00179314, 0.00202761, 0), \
                           ValErr(5.81336e-06, 2.6333e-05, 0), \
                           -173517, 229436, 229436, -nan)
reports[-1].sigmaresid = ValErr(0.515477, 0.000760964, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000748988, None, -4.16501e-06, None, -0.000243539, None, 9.7161e-06, None, -0.000243539, None, 9.7161e-06, None, 0.00117139, None, 1.76243e-05, None, 0.00117139, None, 1.76243e-05, None, 0.51548, None, 0.00572163, None, 0.51548, None, 0.00572163, None)

reports.append(Report(604025392, ("CSC", 1, 3, 1, 6), "MEp31_06"))
reports[-1].posNum = 228586
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00213988, 0.00161138, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00355004, 0.0456311, 0), \
                           ValErr(-0.00110039, 0.00102027, 0), \
                           ValErr(0.00468712, 0.00204204, 0), \
                           ValErr(1.96522e-05, 2.64328e-05, 0), \
                           -173431, 228586, 228586, -nan)
reports[-1].sigmaresid = ValErr(0.516735, 0.000764237, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000997632, None, 6.78776e-06, None, 0.000587052, None, 1.04115e-05, None, 0.000587052, None, 1.04115e-05, None, 0.00239538, None, 1.34541e-05, None, 0.00239538, None, 1.34541e-05, None, 0.516742, None, 0.00575391, None, 0.516742, None, 0.00575391, None)

reports.append(Report(604025408, ("CSC", 1, 3, 1, 8), "MEp31_08"))
reports[-1].posNum = 227941
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00152104, 0.00160198, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0330482, 0.0431548, 0), \
                           ValErr(0.000163935, 0.00100734, 0), \
                           ValErr(-0.00110972, 0.00204155, 0), \
                           ValErr(-6.43901e-06, 2.62253e-05, 0), \
                           -172915, 227941, 227941, -nan)
reports[-1].sigmaresid = ValErr(0.516675, 0.000763268, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00209151, None, 7.53783e-06, None, 0.000871093, None, 1.4769e-05, None, 0.000871093, None, 1.4769e-05, None, 0.00129988, None, 5.38184e-06, None, 0.00129988, None, 5.38184e-06, None, 0.516676, None, 0.00589654, None, 0.516676, None, 0.00589654, None)

reports.append(Report(604025424, ("CSC", 1, 3, 1, 10), "MEp31_10"))
reports[-1].posNum = 228640
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00124708, 0.00161104, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0433633, 0.0459003, 0), \
                           ValErr(0.00147314, 0.0010272, 0), \
                           ValErr(0.000637216, 0.00204735, 0), \
                           ValErr(3.10576e-05, 2.65255e-05, 0), \
                           -174371, 228640, 228640, -nan)
reports[-1].sigmaresid = ValErr(0.518771, 0.000767158, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00126937, None, -1.06293e-05, None, -0.000750831, None, -1.03408e-05, None, -0.000750831, None, -1.03408e-05, None, -0.00149925, None, -1.70469e-05, None, -0.00149925, None, -1.70469e-05, None, 0.518777, None, 0.00585254, None, 0.518777, None, 0.00585254, None)

reports.append(Report(604025440, ("CSC", 1, 3, 1, 12), "MEp31_12"))
reports[-1].posNum = 228024
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000757302, 0.00161372, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0618252, 0.0449999, 0), \
                           ValErr(0.000969808, 0.00102061, 0), \
                           ValErr(0.000841772, 0.00204518, 0), \
                           ValErr(1.53243e-05, 2.62182e-05, 0), \
                           -173294, 228024, 228024, -nan)
reports[-1].sigmaresid = ValErr(0.51739, 0.000765094, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.002408, None, -6.85459e-06, None, 0.00130527, None, 5.86058e-06, None, 0.00130527, None, 5.86058e-06, None, -0.000339117, None, -4.35884e-06, None, -0.000339117, None, -4.35884e-06, None, 0.517395, None, 0.00579404, None, 0.517395, None, 0.00579404, None)

reports.append(Report(604025456, ("CSC", 1, 3, 1, 14), "MEp31_14"))
reports[-1].posNum = 229634
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000717044, 0.00161128, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0534023, 0.0456947, 0), \
                           ValErr(-0.000437225, 0.00102203, 0), \
                           ValErr(-0.00184963, 0.00203888, 0), \
                           ValErr(8.42218e-06, 2.6478e-05, 0), \
                           -175160, 229634, 229634, -nan)
reports[-1].sigmaresid = ValErr(0.518841, 0.000765601, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000373269, None, -9.35093e-06, None, -0.000282686, None, -8.92795e-06, None, -0.000282686, None, -8.92795e-06, None, 0.000300511, None, 1.97767e-06, None, 0.000300511, None, 1.97767e-06, None, 0.518844, None, 0.0058843, None, 0.518844, None, 0.0058843, None)

reports.append(Report(604025472, ("CSC", 1, 3, 1, 16), "MEp31_16"))
reports[-1].posNum = 228707
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000141135, 0.00161509, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0421483, 0.0457287, 0), \
                           ValErr(-3.12746e-05, 0.00102253, 0), \
                           ValErr(0.00147914, 0.0020443, 0), \
                           ValErr(4.45714e-06, 2.65193e-05, 0), \
                           -174119, 228707, 228707, -nan)
reports[-1].sigmaresid = ValErr(0.518084, 0.00076603, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(3.45802e-05, None, 3.80867e-06, None, 0.00099373, None, 8.3773e-06, None, 0.00099373, None, 8.3773e-06, None, 0.00287134, None, 2.19493e-05, None, 0.00287134, None, 2.19493e-05, None, 0.518086, None, 0.00582245, None, 0.518086, None, 0.00582245, None)

reports.append(Report(604025488, ("CSC", 1, 3, 1, 18), "MEp31_18"))
reports[-1].posNum = 229129
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0019431, 0.00161238, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0518518, 0.0455565, 0), \
                           ValErr(0.000706635, 0.00102096, 0), \
                           ValErr(0.000366665, 0.00203939, 0), \
                           ValErr(-3.65118e-05, 2.64588e-05, 0), \
                           -174082, 229129, 229129, -nan)
reports[-1].sigmaresid = ValErr(0.517274, 0.000764127, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00252253, None, 4.56418e-06, None, 0.00197056, None, 5.07237e-06, None, 0.00197056, None, 5.07237e-06, None, 0.00141328, None, 1.03869e-05, None, 0.00141328, None, 1.03869e-05, None, 0.517279, None, 0.00574339, None, 0.517279, None, 0.00574339, None)

reports.append(Report(604025864, ("CSC", 1, 3, 2, 1), "MEp32_01"))
reports[-1].posNum = 75880
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00364219, 0.00628105, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.14446, 0.174798, 0), \
                           ValErr(-0.0029208, 0.00198933, 0), \
                           ValErr(0.00896858, 0.00920627, 0), \
                           ValErr(-2.83719e-05, 4.89057e-05, 0), \
                           -111385, 75880, 75880, -nan)
reports[-1].sigmaresid = ValErr(1.0502, 0.00269582, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00109552, None, 2.72142e-05, None, -0.000714049, None, 1.66106e-05, None, -0.000714049, None, 1.66106e-05, None, -0.00185933, None, 2.2288e-05, None, -0.00185933, None, 2.2288e-05, None, 1.05023, None, 0.00723464, None, 1.05023, None, 0.00723464, None)

reports.append(Report(604025880, ("CSC", 1, 3, 2, 3), "MEp32_03"))
reports[-1].posNum = 66531
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0139186, 0.00669145, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0459818, 0.182881, 0), \
                           ValErr(0.00036175, 0.00202061, 0), \
                           ValErr(0.00830676, 0.00970514, 0), \
                           ValErr(8.86195e-05, 5.05468e-05, 0), \
                           -94879.9, 66531, 66531, -nan)
reports[-1].sigmaresid = ValErr(1.00719, 0.00276112, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00384478, None, -6.92404e-06, None, -0.00640204, None, -4.72981e-06, None, -0.00640204, None, -4.72981e-06, None, -0.00372512, None, -6.34669e-06, None, -0.00372512, None, -6.34669e-06, None, 1.00721, None, 0.00755151, None, 1.00721, None, 0.00755151, None)

reports.append(Report(604025896, ("CSC", 1, 3, 2, 5), "MEp32_05"))
reports[-1].posNum = 76266
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00450585, 0.00611992, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.142744, 0.175089, 0), \
                           ValErr(0.00291818, 0.00198117, 0), \
                           ValErr(-0.0034707, 0.00911205, 0), \
                           ValErr(-5.53891e-05, 4.78048e-05, 0), \
                           -111384, 76266, 76266, -nan)
reports[-1].sigmaresid = ValErr(1.04241, 0.00266905, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00289944, None, 2.63615e-05, None, 0.000933612, None, 2.81145e-05, None, 0.000933612, None, 2.81145e-05, None, 0.0012776, None, 1.31842e-05, None, 0.0012776, None, 1.31842e-05, None, 1.04243, None, 0.00765214, None, 1.04243, None, 0.00765214, None)

reports.append(Report(604025912, ("CSC", 1, 3, 2, 7), "MEp32_07"))
reports[-1].posNum = 67183
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00506971, 0.00679305, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.035684, 0.182519, 0), \
                           ValErr(0.00265223, 0.00203471, 0), \
                           ValErr(-0.0151073, 0.00978014, 0), \
                           ValErr(5.23996e-07, 5.12173e-05, 0), \
                           -96879.7, 67183, 67183, -nan)
reports[-1].sigmaresid = ValErr(1.02336, 0.00279179, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000162926, None, 1.87574e-05, None, -0.00157663, None, 2.46019e-05, None, -0.00157663, None, 2.46019e-05, None, -0.000859707, None, 8.02149e-06, None, -0.000859707, None, 8.02149e-06, None, 1.02339, None, 0.00727512, None, 1.02339, None, 0.00727512, None)

reports.append(Report(604025928, ("CSC", 1, 3, 2, 9), "MEp32_09"))
reports[-1].posNum = 70128
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0105178, 0.00636927, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.142308, 0.0913586, 0), \
                           ValErr(0.000331144, 0.00109053, 0), \
                           ValErr(0.00108489, 0.00939115, 0), \
                           ValErr(-8.11583e-05, 4.77372e-05, 0), \
                           -101958, 70128, 70128, -nan)
reports[-1].sigmaresid = ValErr(1.03557, 0.0027534, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00851681, None, 1.77489e-05, None, 0.00793442, None, -7.10599e-06, None, 0.00793442, None, -7.10599e-06, None, 0.0100161, None, 2.39496e-05, None, 0.0100161, None, 2.39496e-05, None, 1.0356, None, 0.00806428, None, 1.0356, None, 0.00806428, None)

reports.append(Report(604025944, ("CSC", 1, 3, 2, 11), "MEp32_11"))
reports[-1].posNum = 69535
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0101118, 0.00639192, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.240987, 0.183474, 0), \
                           ValErr(-0.000478601, 0.00202551, 0), \
                           ValErr(-0.00811425, 0.00954198, 0), \
                           ValErr(1.68303e-05, 4.90776e-05, 0), \
                           -100490, 69535, 69535, -nan)
reports[-1].sigmaresid = ValErr(1.02657, 0.00275279, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0161568, None, -5.17293e-05, None, -0.0126999, None, -4.70256e-05, None, -0.0126999, None, -4.70256e-05, None, -0.0125758, None, -3.15688e-05, None, -0.0125758, None, -3.15688e-05, None, 1.02659, None, 0.00794838, None, 1.02659, None, 0.00794838, None)

reports.append(Report(604025960, ("CSC", 1, 3, 2, 13), "MEp32_13"))
reports[-1].posNum = 66037
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000291668, 0.00677444, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0392159, 0.176635, 0), \
                           ValErr(0.00300284, 0.0020385, 0), \
                           ValErr(0.0137136, 0.00882043, 0), \
                           ValErr(3.16509e-05, 4.53948e-05, 0), \
                           -94639.3, 66037, 66037, -nan)
reports[-1].sigmaresid = ValErr(1.01429, 0.00272792, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00723945, None, -9.42865e-06, None, 0.00772977, None, 6.80088e-06, None, 0.00772977, None, 6.80088e-06, None, 0.0104787, None, -7.45124e-06, None, 0.0104787, None, -7.45124e-06, None, 1.01432, None, 0.0074515, None, 1.01432, None, 0.0074515, None)

reports.append(Report(604025976, ("CSC", 1, 3, 2, 15), "MEp32_15"))
reports[-1].posNum = 76351
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00247102, 0.00614136, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0551675, 0.17325, 0), \
                           ValErr(-0.00156935, 0.00195948, 0), \
                           ValErr(-0.00240999, 0.0091046, 0), \
                           ValErr(-1.89285e-06, 4.78407e-05, 0), \
                           -111335, 76351, 76351, -nan)
reports[-1].sigmaresid = ValErr(1.04004, 0.00266153, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00144681, None, 1.4531e-05, None, -0.00359144, None, 1.46482e-05, None, -0.00359144, None, 1.46482e-05, None, 0.00324037, None, -7.72123e-06, None, 0.00324037, None, -7.72123e-06, None, 1.04004, None, 0.00734792, None, 1.04004, None, 0.00734792, None)

reports.append(Report(604025992, ("CSC", 1, 3, 2, 17), "MEp32_17"))
reports[-1].posNum = 66710
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00255676, 0.00666888, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0738686, 0.121039, 0), \
                           ValErr(-0.00107087, 0.00201482, 0), \
                           ValErr(-0.00780185, 0.00979175, 0), \
                           ValErr(3.56478e-05, 4.91947e-05, 0), \
                           -95450.9, 66710, 66710, -nan)
reports[-1].sigmaresid = ValErr(1.01197, 0.00276851, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000385257, None, 1.4282e-05, None, 0.000897732, None, -3.20583e-06, None, 0.000897732, None, -3.20583e-06, None, 0.00373341, None, 1.1442e-06, None, 0.00373341, None, 1.1442e-06, None, 1.01198, None, 0.00756233, None, 1.01198, None, 0.00756233, None)

reports.append(Report(604026008, ("CSC", 1, 3, 2, 19), "MEp32_19"))
reports[-1].posNum = 76434
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0116575, 0.00628252, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0639037, 0.172109, 0), \
                           ValErr(-0.00166854, 0.00195594, 0), \
                           ValErr(-0.0184236, 0.0091312, 0), \
                           ValErr(-8.34994e-06, 4.85467e-05, 0), \
                           -111606, 76434, 76434, -nan)
reports[-1].sigmaresid = ValErr(1.04208, 0.00266529, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00449901, None, 1.73293e-05, None, 0.00316552, None, 1.9791e-05, None, 0.00316552, None, 1.9791e-05, None, -0.00165052, None, 4.24607e-05, None, -0.00165052, None, 4.24607e-05, None, 1.04212, None, 0.00823031, None, 1.04212, None, 0.00823031, None)

reports.append(Report(604026024, ("CSC", 1, 3, 2, 21), "MEp32_21"))
reports[-1].posNum = 66839
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00475225, 0.00663471, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0396668, 0.183206, 0), \
                           ValErr(0.000688965, 0.00200012, 0), \
                           ValErr(0.00252811, 0.0096681, 0), \
                           ValErr(2.74024e-05, 4.98576e-05, 0), \
                           -95418.7, 66839, 66839, -nan)
reports[-1].sigmaresid = ValErr(1.00869, 0.00275884, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00246476, None, -9.38512e-06, None, -0.00244314, None, -6.45722e-05, None, -0.00244314, None, -6.45722e-05, None, -0.00319807, None, -6.34051e-05, None, -0.00319807, None, -6.34051e-05, None, 1.00869, None, 0.0079658, None, 1.00869, None, 0.0079658, None)

reports.append(Report(604026040, ("CSC", 1, 3, 2, 23), "MEp32_23"))
reports[-1].posNum = 75654
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00666098, 0.00619131, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0411601, 0.174501, 0), \
                           ValErr(-0.00150422, 0.00197334, 0), \
                           ValErr(0.00700474, 0.00915132, 0), \
                           ValErr(-4.73715e-05, 4.80133e-05, 0), \
                           -110197, 75654, 75654, -nan)
reports[-1].sigmaresid = ValErr(1.03837, 0.00266944, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00790511, None, 1.40634e-05, None, 0.00793602, None, 3.48896e-06, None, 0.00793602, None, 3.48896e-06, None, 0.00698235, None, 1.8756e-06, None, 0.00698235, None, 1.8756e-06, None, 1.0384, None, 0.00718687, None, 1.0384, None, 0.00718687, None)

reports.append(Report(604026056, ("CSC", 1, 3, 2, 25), "MEp32_25"))
reports[-1].posNum = 67701
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00421472, 0.00673769, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.441232, 0.150737, 0), \
                           ValErr(0.0038476, 0.00182219, 0), \
                           ValErr(0.0142313, 0.00960248, 0), \
                           ValErr(5.04539e-05, 4.88767e-05, 0), \
                           -97907.8, 67701, 67701, -nan)
reports[-1].sigmaresid = ValErr(1.02762, 0.00276208, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00879997, None, 2.49314e-05, None, 0.0123635, None, 7.30194e-05, None, 0.0123635, None, 7.30194e-05, None, 0.0129256, None, 8.15324e-05, None, 0.0129256, None, 8.15324e-05, None, 1.0277, None, 0.00794664, None, 1.0277, None, 0.00794664, None)

reports.append(Report(604026072, ("CSC", 1, 3, 2, 27), "MEp32_27"))
reports[-1].posNum = 70449
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00444273, 0.00646136, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0856572, 0.182317, 0), \
                           ValErr(0.00249846, 0.00203689, 0), \
                           ValErr(0.0118205, 0.00955558, 0), \
                           ValErr(3.6211e-05, 4.96768e-05, 0), \
                           -102664, 70449, 70449, -nan)
reports[-1].sigmaresid = ValErr(1.03908, 0.00276819, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00261652, None, 5.76501e-05, None, 0.00200264, None, 3.88344e-05, None, 0.00200264, None, 3.88344e-05, None, -0.00311099, None, 2.96809e-05, None, -0.00311099, None, 2.96809e-05, None, 1.03911, None, 0.00816659, None, 1.03911, None, 0.00816659, None)

reports.append(Report(604026088, ("CSC", 1, 3, 2, 29), "MEp32_29"))
reports[-1].posNum = 71110
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0012057, 0.00638579, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.191749, 0.181285, 0), \
                           ValErr(-0.000850426, 0.00202546, 0), \
                           ValErr(0.00472705, 0.00945788, 0), \
                           ValErr(5.62306e-06, 4.91684e-05, 0), \
                           -103150, 71110, 71110, -nan)
reports[-1].sigmaresid = ValErr(1.03214, 0.0027369, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00237755, None, 7.51948e-06, None, 0.000873678, None, 1.86665e-05, None, 0.000873678, None, 1.86665e-05, None, 0.00206286, None, 4.70257e-05, None, 0.00206286, None, 4.70257e-05, None, 1.03215, None, 0.00806961, None, 1.03215, None, 0.00806961, None)

reports.append(Report(604026104, ("CSC", 1, 3, 2, 31), "MEp32_31"))
reports[-1].posNum = 68030
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00889026, 0.00677826, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.105751, 0.181764, 0), \
                           ValErr(0.00300066, 0.00203682, 0), \
                           ValErr(0.00635464, 0.00975867, 0), \
                           ValErr(7.54017e-05, 5.11502e-05, 0), \
                           -98131.6, 68030, 68030, -nan)
reports[-1].sigmaresid = ValErr(1.02381, 0.0027756, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00163158, None, 3.23547e-05, None, -0.00260909, None, 2.13412e-05, None, -0.00260909, None, 2.13412e-05, None, -0.00102432, None, 3.17316e-05, None, -0.00102432, None, 3.17316e-05, None, 1.02385, None, 0.00743936, None, 1.02385, None, 0.00743936, None)

reports.append(Report(604026120, ("CSC", 1, 3, 2, 33), "MEp32_33"))
reports[-1].posNum = 75624
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00713227, 0.00610088, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0293762, 0.172816, 0), \
                           ValErr(0.00289, 0.00196413, 0), \
                           ValErr(-0.00638315, 0.00899179, 0), \
                           ValErr(-2.52248e-05, 4.75183e-05, 0), \
                           -109745, 75624, 75624, -nan)
reports[-1].sigmaresid = ValErr(1.03278, 0.00265559, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000144071, None, 2.74659e-05, None, 0.00340468, None, 3.73969e-05, None, 0.00340468, None, 3.73969e-05, None, 0.000523571, None, 1.71095e-05, None, 0.000523571, None, 1.71095e-05, None, 1.0328, None, 0.00767815, None, 1.0328, None, 0.00767815, None)

reports.append(Report(604026136, ("CSC", 1, 3, 2, 35), "MEp32_35"))
reports[-1].posNum = 65360
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00678581, 0.0067227, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.130492, 0.184482, 0), \
                           ValErr(0.000792647, 0.00203132, 0), \
                           ValErr(0.0105355, 0.00981601, 0), \
                           ValErr(2.23024e-05, 5.04044e-05, 0), \
                           -92288.4, 65360, 65360, -nan)
reports[-1].sigmaresid = ValErr(0.993087, 0.00274673, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00534363, None, -1.09608e-05, None, -0.00126028, None, 8.46187e-07, None, -0.00126028, None, 8.46187e-07, None, 0.00350164, None, 1.33262e-05, None, 0.00350164, None, 1.33262e-05, None, 0.993101, None, 0.00711232, None, 0.993101, None, 0.00711232, None)

reports.append(Report(604025872, ("CSC", 1, 3, 2, 2), "MEp32_02"))
reports[-1].posNum = 72995
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00472965, 0.00637532, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.194498, 0.185382, 0), \
                           ValErr(-2.48724e-05, 0.00207102, 0), \
                           ValErr(-0.00918135, 0.0096742, 0), \
                           ValErr(6.78828e-05, 4.93005e-05, 0), \
                           -106370, 72995, 72995, -nan)
reports[-1].sigmaresid = ValErr(1.03903, 0.00271937, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00537634, None, -7.8228e-06, None, -0.0058264, None, -2.05008e-06, None, -0.0058264, None, -2.05008e-06, None, -0.00339655, None, -1.40128e-05, None, -0.00339655, None, -1.40128e-05, None, 1.03907, None, 0.00742091, None, 1.03907, None, 0.00742091, None)

reports.append(Report(604025888, ("CSC", 1, 3, 2, 4), "MEp32_04"))
reports[-1].posNum = 70186
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00528908, 0.00659717, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.188727, 0.191592, 0), \
                           ValErr(0.00198436, 0.00213305, 0), \
                           ValErr(-0.00208195, 0.0100787, 0), \
                           ValErr(-7.19391e-05, 5.04432e-05, 0), \
                           -102065, 70186, 70186, -nan)
reports[-1].sigmaresid = ValErr(1.03589, 0.00276487, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000635888, None, 3.02842e-05, None, 0.00140145, None, 3.81786e-05, None, 0.00140145, None, 3.81786e-05, None, 0.00266734, None, 2.37883e-05, None, 0.00266734, None, 2.37883e-05, None, 1.03592, None, 0.00699934, None, 1.03592, None, 0.00699934, None)

reports.append(Report(604025904, ("CSC", 1, 3, 2, 6), "MEp32_06"))
reports[-1].posNum = 76715
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0127933, 0.00618954, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00452596, 0.101378, 0), \
                           ValErr(0.00120724, 0.00105147, 0), \
                           ValErr(-0.0266137, 0.00933686, 0), \
                           ValErr(-3.69122e-05, 4.64999e-05, 0), \
                           -112710, 76715, 76715, -nan)
reports[-1].sigmaresid = ValErr(1.05155, 0.00267642, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000605236, None, -6.09535e-06, None, 0.000173121, None, -1.31651e-05, None, 0.000173121, None, -1.31651e-05, None, -0.00069699, None, -2.91942e-05, None, -0.00069699, None, -2.91942e-05, None, 1.05161, None, 0.00730356, None, 1.05161, None, 0.00730356, None)

reports.append(Report(604025920, ("CSC", 1, 3, 2, 8), "MEp32_08"))
reports[-1].posNum = 67743
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00538064, 0.00675293, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0786758, 0.191179, 0), \
                           ValErr(-0.00223341, 0.00212623, 0), \
                           ValErr(0.00262881, 0.010176, 0), \
                           ValErr(4.37709e-05, 5.14039e-05, 0), \
                           -97072.6, 67743, 67743, -nan)
reports[-1].sigmaresid = ValErr(1.01411, 0.00275512, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00172731, None, 2.25035e-05, None, -0.00225086, None, -2.20427e-05, None, -0.00225086, None, -2.20427e-05, None, 0.0017577, None, 2.92507e-05, None, 0.0017577, None, 2.92507e-05, None, 1.01413, None, 0.00782385, None, 1.01413, None, 0.00782385, None)

reports.append(Report(604025936, ("CSC", 1, 3, 2, 10), "MEp32_10"))
reports[-1].posNum = 79449
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00305462, 0.00616364, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.286663, 0.169759, 0), \
                           ValErr(0.00583333, 0.00168398, 0), \
                           ValErr(-0.00283725, 0.00919989, 0), \
                           ValErr(1.81954e-05, 4.30285e-05, 0), \
                           -117330, 79449, 79449, -nan)
reports[-1].sigmaresid = ValErr(1.05957, 0.00263252, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00366983, None, 1.78052e-05, None, 0.00261626, None, 3.88132e-05, None, 0.00261626, None, 3.88132e-05, None, 0.00453031, None, 4.0351e-05, None, 0.00453031, None, 4.0351e-05, None, 1.05964, None, 0.00958679, None, 1.05964, None, 0.00958679, None)

reports.append(Report(604025952, ("CSC", 1, 3, 2, 12), "MEp32_12"))
reports[-1].posNum = 68691
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0013305, 0.00664776, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0876014, 0.191963, 0), \
                           ValErr(0.00465046, 0.0021323, 0), \
                           ValErr(0.00405788, 0.0101251, 0), \
                           ValErr(-3.26139e-05, 5.08999e-05, 0), \
                           -99038.4, 68691, 68691, -nan)
reports[-1].sigmaresid = ValErr(1.02312, 0.00276036, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00358139, None, -2.40776e-05, None, -0.00131372, None, -2.08256e-05, None, -0.00131372, None, -2.08256e-05, None, 0.000576033, None, -1.6899e-05, None, 0.000576033, None, -1.6899e-05, None, 1.02317, None, 0.00764917, None, 1.02317, None, 0.00764917, None)

reports.append(Report(604025968, ("CSC", 1, 3, 2, 14), "MEp32_14"))
reports[-1].posNum = 77624
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0153858, 0.0062375, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0851748, 0.0897051, 0), \
                           ValErr(-0.000255384, 0.00102267, 0), \
                           ValErr(-0.00433141, 0.00939051, 0), \
                           ValErr(-9.6334e-05, 4.764e-05, 0), \
                           -114301, 77624, 77624, -nan)
reports[-1].sigmaresid = ValErr(1.05502, 0.00267543, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00872024, None, -2.26089e-06, None, 0.00995317, None, 1.57273e-05, None, 0.00995317, None, 1.57273e-05, None, 0.0083931, None, -1.51501e-05, None, 0.0083931, None, -1.51501e-05, None, 1.05505, None, 0.00734831, None, 1.05505, None, 0.00734831, None)

reports.append(Report(604025984, ("CSC", 1, 3, 2, 16), "MEp32_16"))
reports[-1].posNum = 69575
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000789304, 0.00657109, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.203763, 0.191626, 0), \
                           ValErr(0.000160899, 0.00214596, 0), \
                           ValErr(-0.00101166, 0.0100722, 0), \
                           ValErr(-4.34549e-05, 5.02641e-05, 0), \
                           -100411, 69575, 69575, -nan)
reports[-1].sigmaresid = ValErr(1.02456, 0.0027466, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00492691, None, 4.32519e-06, None, -0.00310003, None, 3.84111e-05, None, -0.00310003, None, 3.84111e-05, None, -0.00709987, None, 2.23653e-05, None, -0.00709987, None, 2.23653e-05, None, 1.02457, None, 0.00706387, None, 1.02457, None, 0.00706387, None)

reports.append(Report(604026000, ("CSC", 1, 3, 2, 18), "MEp32_18"))
reports[-1].posNum = 72641
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0112116, 0.00640303, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0941904, 0.184613, 0), \
                           ValErr(0.00157114, 0.00205097, 0), \
                           ValErr(0.0149345, 0.00965579, 0), \
                           ValErr(3.69649e-05, 4.92041e-05, 0), \
                           -106147, 72641, 72641, -nan)
reports[-1].sigmaresid = ValErr(1.04322, 0.00273697, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00515406, None, 2.10335e-05, None, -0.00352261, None, -4.20253e-06, None, -0.00352261, None, -4.20253e-06, None, -0.00469264, None, 2.35869e-05, None, -0.00469264, None, 2.35869e-05, None, 1.04324, None, 0.00802372, None, 1.04324, None, 0.00802372, None)

reports.append(Report(604026016, ("CSC", 1, 3, 2, 20), "MEp32_20"))
reports[-1].posNum = 74294
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00470425, 0.00630908, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.136848, 0.183759, 0), \
                           ValErr(-0.000385918, 0.0020612, 0), \
                           ValErr(-0.0139499, 0.00959512, 0), \
                           ValErr(7.78045e-05, 4.88531e-05, 0), \
                           -108566, 74294, 74294, -nan)
reports[-1].sigmaresid = ValErr(1.04328, 0.0027065, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00938921, None, 7.39159e-06, None, -0.0073307, None, -1.38318e-05, None, -0.0073307, None, -1.38318e-05, None, -0.00584501, None, 1.04732e-05, None, -0.00584501, None, 1.04732e-05, None, 1.04333, None, 0.00716605, None, 1.04333, None, 0.00716605, None)

reports.append(Report(604026032, ("CSC", 1, 3, 2, 22), "MEp32_22"))
reports[-1].posNum = 70046
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00157014, 0.00656232, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0209048, 0.173212, 0), \
                           ValErr(-0.0014734, 0.00191749, 0), \
                           ValErr(0.00772611, 0.0099516, 0), \
                           ValErr(-7.97629e-05, 4.91312e-05, 0), \
                           -101266, 70046, 70046, -nan)
reports[-1].sigmaresid = ValErr(1.02713, 0.00273046, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00127682, None, 6.52478e-06, None, 0.00118741, None, 1.01272e-05, None, 0.00118741, None, 1.01272e-05, None, 0.000681777, None, -2.03147e-05, None, 0.000681777, None, -2.03147e-05, None, 1.02717, None, 0.00717346, None, 1.02717, None, 0.00717346, None)

reports.append(Report(604026048, ("CSC", 1, 3, 2, 24), "MEp32_24"))
reports[-1].posNum = 76491
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00320024, 0.0061352, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0363308, 0.179694, 0), \
                           ValErr(0.000836743, 0.00204065, 0), \
                           ValErr(-0.0130703, 0.00936304, 0), \
                           ValErr(9.93092e-06, 4.80538e-05, 0), \
                           -111833, 76491, 76491, -nan)
reports[-1].sigmaresid = ValErr(1.04405, 0.00266932, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0070238, None, 4.10508e-06, None, -0.00831955, None, 3.35891e-05, None, -0.00831955, None, 3.35891e-05, None, -0.00524487, None, 1.89939e-05, None, -0.00524487, None, 1.89939e-05, None, 1.04407, None, 0.00728486, None, 1.04407, None, 0.00728486, None)

reports.append(Report(604026064, ("CSC", 1, 3, 2, 26), "MEp32_26"))
reports[-1].posNum = 68648
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0006555, 0.00676938, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.422057, 0.189303, 0), \
                           ValErr(-0.0036955, 0.00211177, 0), \
                           ValErr(0.00204962, 0.0101282, 0), \
                           ValErr(-6.38323e-05, 5.14257e-05, 0), \
                           -98609.9, 68648, 68648, -nan)
reports[-1].sigmaresid = ValErr(1.01767, 0.0027465, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00509794, None, 3.82442e-06, None, -0.00292581, None, -1.2405e-05, None, -0.00292581, None, -1.2405e-05, None, -0.00297145, None, -3.50722e-05, None, -0.00297145, None, -3.50722e-05, None, 1.01774, None, 0.00728755, None, 1.01774, None, 0.00728755, None)

reports.append(Report(604026080, ("CSC", 1, 3, 2, 28), "MEp32_28"))
reports[-1].posNum = 79308
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00298889, 0.00618694, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.29147, 0.177485, 0), \
                           ValErr(0.000463866, 0.00201252, 0), \
                           ValErr(0.00212195, 0.0093466, 0), \
                           ValErr(-2.65584e-05, 4.80537e-05, 0), \
                           -117275, 79308, 79308, -nan)
reports[-1].sigmaresid = ValErr(1.06161, 0.0026656, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0044602, None, -1.15016e-05, None, -0.00305032, None, -1.32464e-05, None, -0.00305032, None, -1.32464e-05, None, 0.00135305, None, -9.47737e-06, None, 0.00135305, None, -9.47737e-06, None, 1.06163, None, 0.00820092, None, 1.06163, None, 0.00820092, None)

reports.append(Report(604026096, ("CSC", 1, 3, 2, 30), "MEp32_30"))
reports[-1].posNum = 68150
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00824968, 0.00660567, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.124606, 0.189642, 0), \
                           ValErr(0.000466447, 0.00209642, 0), \
                           ValErr(0.0117374, 0.0100035, 0), \
                           ValErr(6.34696e-05, 5.01331e-05, 0), \
                           -97332, 68150, 68150, -nan)
reports[-1].sigmaresid = ValErr(1.00931, 0.00273385, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00229877, None, -6.55841e-06, None, -0.000492801, None, 3.51186e-05, None, -0.000492801, None, 3.51186e-05, None, -0.006436, None, -1.1954e-05, None, -0.006436, None, -1.1954e-05, None, 1.00933, None, 0.00747674, None, 1.00933, None, 0.00747674, None)

reports.append(Report(604026112, ("CSC", 1, 3, 2, 32), "MEp32_32"))
reports[-1].posNum = 77058
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00069255, 0.00620622, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.100187, 0.16865, 0), \
                           ValErr(0.00206295, 0.00200758, 0), \
                           ValErr(0.00351795, 0.0090823, 0), \
                           ValErr(7.18784e-06, 3.81005e-05, 0), \
                           -113055, 77058, 77058, -nan)
reports[-1].sigmaresid = ValErr(1.04939, 0.002672, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00551244, None, 2.00802e-05, None, 0.00240655, None, 1.01885e-05, None, 0.00240655, None, 1.01885e-05, None, 0.000970439, None, -2.4883e-06, None, 0.000970439, None, -2.4883e-06, None, 1.0494, None, 0.00736578, None, 1.0494, None, 0.00736578, None)

reports.append(Report(604026128, ("CSC", 1, 3, 2, 34), "MEp32_34"))
reports[-1].posNum = 71273
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0140517, 0.00655273, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.345049, 0.191491, 0), \
                           ValErr(0.00664144, 0.00215891, 0), \
                           ValErr(0.00801467, 0.0100556, 0), \
                           ValErr(3.33008e-05, 5.03889e-05, 0), \
                           -103835, 71273, 71273, -nan)
reports[-1].sigmaresid = ValErr(1.03866, 0.00275124, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0119417, None, -7.81738e-05, None, -0.00946378, None, -4.68175e-05, None, -0.00946378, None, -4.68175e-05, None, -0.0102342, None, -5.98135e-05, None, -0.0102342, None, -5.98135e-05, None, 1.03875, None, 0.00706391, None, 1.03875, None, 0.00706391, None)

reports.append(Report(604026144, ("CSC", 1, 3, 2, 36), "MEp32_36"))
reports[-1].posNum = 74573
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00763747, 0.00626433, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0800323, 0.182302, 0), \
                           ValErr(0.00180017, 0.00205605, 0), \
                           ValErr(-0.0111338, 0.00954629, 0), \
                           ValErr(-4.97108e-06, 4.85523e-05, 0), \
                           -108617, 74573, 74573, -nan)
reports[-1].sigmaresid = ValErr(1.03829, 0.00268852, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00286497, None, -2.43319e-05, None, 0.00279513, None, -6.10299e-05, None, 0.00279513, None, -6.10299e-05, None, -9.31933e-05, None, -8.52946e-05, None, -9.31933e-05, None, -8.52946e-05, None, 1.03831, None, 0.00736421, None, 1.03831, None, 0.00736421, None)

reports.append(Report(604029448, ("CSC", 1, 4, 1, 1), "MEp41_01"))
reports[-1].posNum = 179770
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00209623, 0.00204307, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.129672, 0.0591174, 0), \
                           ValErr(-0.000633564, 0.0015134, 0), \
                           ValErr(-0.000303692, 0.00258283, 0), \
                           ValErr(4.00631e-06, 3.77866e-05, 0), \
                           -157878, 179770, 179770, -nan)
reports[-1].sigmaresid = ValErr(0.58233, 0.000971171, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000783362, None, 2.72894e-06, None, 0.00193624, None, 7.70535e-06, None, 0.00193624, None, 7.70535e-06, None, 0.000678084, None, 3.92683e-05, None, 0.000678084, None, 3.92683e-05, None, 0.582338, None, 0.00590236, None, 0.582338, None, 0.00590236, None)

reports.append(Report(604029464, ("CSC", 1, 4, 1, 3), "MEp41_03"))
reports[-1].posNum = 179579
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00335611, 0.0020421, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0337578, 0.0508811, 0), \
                           ValErr(0.000516422, 0.00130681, 0), \
                           ValErr(-0.00217458, 0.00258726, 0), \
                           ValErr(-3.97153e-06, 3.35819e-05, 0), \
                           -158543, 179579, 179579, -nan)
reports[-1].sigmaresid = ValErr(0.585038, 0.000973245, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00219443, None, -2.87882e-06, None, 0.00210229, None, 2.86464e-05, None, 0.00210229, None, 2.86464e-05, None, 0.00286521, None, 1.22441e-05, None, 0.00286521, None, 1.22441e-05, None, 0.58504, None, 0.0058692, None, 0.58504, None, 0.0058692, None)

reports.append(Report(604029480, ("CSC", 1, 4, 1, 5), "MEp41_05"))
reports[-1].posNum = 180567
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000286857, 0.00204235, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0380553, 0.0592343, 0), \
                           ValErr(-0.00361223, 0.00151754, 0), \
                           ValErr(-0.00130902, 0.00258313, 0), \
                           ValErr(-4.18396e-06, 3.78082e-05, 0), \
                           -159278, 180567, 180567, -nan)
reports[-1].sigmaresid = ValErr(0.584592, 0.000972786, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000419905, None, -6.92492e-06, None, -0.000465092, None, 4.32896e-06, None, -0.000465092, None, 4.32896e-06, None, -0.00291952, None, -3.80137e-06, None, -0.00291952, None, -3.80137e-06, None, 0.584602, None, 0.00572592, None, 0.584602, None, 0.00572592, None)

reports.append(Report(604029496, ("CSC", 1, 4, 1, 7), "MEp41_07"))
reports[-1].posNum = 180518
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00145162, 0.00204506, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0245561, 0.0593582, 0), \
                           ValErr(0.000455919, 0.00151518, 0), \
                           ValErr(0.000552489, 0.00258501, 0), \
                           ValErr(5.27535e-05, 3.78017e-05, 0), \
                           -159349, 180518, 180518, -nan)
reports[-1].sigmaresid = ValErr(0.584964, 0.000973539, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000438825, None, 2.50776e-07, None, -0.00101348, None, 3.42321e-06, None, -0.00101348, None, 3.42321e-06, None, -0.00162828, None, 8.28204e-06, None, -0.00162828, None, 8.28204e-06, None, 0.584968, None, 0.0059091, None, 0.584968, None, 0.0059091, None)

reports.append(Report(604029512, ("CSC", 1, 4, 1, 9), "MEp41_09"))
reports[-1].posNum = 180396
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000645529, 0.00203824, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0257586, 0.0590838, 0), \
                           ValErr(-0.00184997, 0.00151231, 0), \
                           ValErr(0.00128267, 0.00257766, 0), \
                           ValErr(3.62782e-06, 3.76508e-05, 0), \
                           -158504, 180396, 180396, -nan)
reports[-1].sigmaresid = ValErr(0.582577, 0.000969894, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000947206, None, 9.88261e-06, None, 0.000107511, None, 7.38271e-05, None, 0.000107511, None, 7.38271e-05, None, -0.0016156, None, 4.19196e-05, None, -0.0016156, None, 4.19196e-05, None, 0.582582, None, 0.0129552, None, 0.582582, None, 0.0129552, None)

reports.append(Report(604029528, ("CSC", 1, 4, 1, 11), "MEp41_11"))
reports[-1].posNum = 180555
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0014162, 0.00202869, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0583511, 0.0590114, 0), \
                           ValErr(-0.00111823, 0.00150598, 0), \
                           ValErr(-0.00267037, 0.00257177, 0), \
                           ValErr(3.10347e-05, 3.74733e-05, 0), \
                           -158186, 180555, 180555, -nan)
reports[-1].sigmaresid = ValErr(0.5811, 0.000967011, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000510039, None, 2.41466e-06, None, -3.66984e-05, None, -1.37948e-07, None, -3.66984e-05, None, -1.37948e-07, None, -0.00077884, None, -7.81695e-06, None, -0.00077884, None, -7.81695e-06, None, 0.581107, None, 0.00580711, None, 0.581107, None, 0.00580711, None)

reports.append(Report(604029544, ("CSC", 1, 4, 1, 13), "MEp41_13"))
reports[-1].posNum = 180448
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00220129, 0.00203528, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0027853, 0.0592114, 0), \
                           ValErr(0.00143916, 0.00151547, 0), \
                           ValErr(0.00486099, 0.00258452, 0), \
                           ValErr(2.78034e-05, 3.7659e-05, 0), \
                           -158407, 180448, 180448, -nan)
reports[-1].sigmaresid = ValErr(0.582114, 0.000968984, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000101775, None, 5.38059e-08, None, 0.000639608, None, 1.48578e-05, None, 0.000639608, None, 1.48578e-05, None, -0.000347148, None, 2.88255e-06, None, -0.000347148, None, 2.88255e-06, None, 0.582122, None, 0.00590346, None, 0.582122, None, 0.00590346, None)

reports.append(Report(604029560, ("CSC", 1, 4, 1, 15), "MEp41_15"))
reports[-1].posNum = 152424
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00652001, 0.00222164, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.045262, 0.0635714, 0), \
                           ValErr(-0.0014123, 0.00163115, 0), \
                           ValErr(0.00820672, 0.00265917, 0), \
                           ValErr(0.000114178, 4.14035e-05, 0), \
                           -133947, 152424, 152424, -nan)
reports[-1].sigmaresid = ValErr(0.582654, 0.00105529, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0016466, None, -2.17739e-05, None, -0.00141277, None, -8.56723e-05, None, -0.00141277, None, -8.56723e-05, None, 0.000559398, None, 5.76007e-05, None, 0.000559398, None, 5.76007e-05, None, 0.582681, None, 0.00820292, None, 0.582681, None, 0.00820292, None)

reports.append(Report(604029576, ("CSC", 1, 4, 1, 17), "MEp41_17"))
reports[-1].posNum = 180506
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000322844, 0.00205153, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0115639, 0.0596298, 0), \
                           ValErr(-0.000988459, 0.00152698, 0), \
                           ValErr(-0.00155196, 0.00260036, 0), \
                           ValErr(1.78081e-05, 3.79461e-05, 0), \
                           -160108, 180506, 180506, -nan)
reports[-1].sigmaresid = ValErr(0.587463, 0.000977729, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000459611, None, -1.37432e-05, None, -0.0011666, None, 3.91254e-05, None, -0.0011666, None, 3.91254e-05, None, -0.000939476, None, 4.29796e-05, None, -0.000939476, None, 4.29796e-05, None, 0.587465, None, 0.00587528, None, 0.587465, None, 0.00587528, None)

reports.append(Report(604029456, ("CSC", 1, 4, 1, 2), "MEp41_02"))
reports[-1].posNum = 183181
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00259278, 0.00206563, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0194577, 0.0504415, 0), \
                           ValErr(1.14976e-05, 0.0013966, 0), \
                           ValErr(-0.00446383, 0.00268678, 0), \
                           ValErr(3.61614e-05, 3.37217e-05, 0), \
                           -165172, 183181, 183181, -nan)
reports[-1].sigmaresid = ValErr(0.596157, 0.000979491, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00241904, None, -4.41358e-06, None, 0.000184542, None, -2.05664e-06, None, 0.000184542, None, -2.05664e-06, None, -0.000391822, None, 1.08301e-06, None, -0.000391822, None, 1.08301e-06, None, 0.596166, None, 0.00563738, None, 0.596166, None, 0.00563738, None)

reports.append(Report(604029472, ("CSC", 1, 4, 1, 4), "MEp41_04"))
reports[-1].posNum = 183760
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00117267, 0.00207148, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.010942, 0.0616743, 0), \
                           ValErr(0.000677296, 0.00157694, 0), \
                           ValErr(-0.00185707, 0.00268538, 0), \
                           ValErr(2.63156e-05, 3.83973e-05, 0), \
                           -166399, 183760, 183760, -nan)
reports[-1].sigmaresid = ValErr(0.598447, 0.000987155, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0017622, None, -1.45381e-05, None, -0.00215192, None, -1.10568e-05, None, -0.00215192, None, -1.10568e-05, None, -0.00219941, None, -1.63517e-05, None, -0.00219941, None, -1.63517e-05, None, 0.59845, None, 0.00542198, None, 0.59845, None, 0.00542198, None)

reports.append(Report(604029488, ("CSC", 1, 4, 1, 6), "MEp41_06"))
reports[-1].posNum = 183070
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-8.24084e-05, 0.0020824, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00852104, 0.0617589, 0), \
                           ValErr(-0.000617729, 0.00158091, 0), \
                           ValErr(0.00247461, 0.00269334, 0), \
                           ValErr(5.07912e-05, 3.85448e-05, 0), \
                           -166083, 183070, 183070, -nan)
reports[-1].sigmaresid = ValErr(0.59946, 0.000990688, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000360375, None, -8.22197e-06, None, 0.00141898, None, 3.48228e-05, None, 0.00141898, None, 3.48228e-05, None, -0.00127787, None, 4.28723e-06, None, -0.00127787, None, 4.28723e-06, None, 0.599464, None, 0.00584938, None, 0.599464, None, 0.00584938, None)

reports.append(Report(604029504, ("CSC", 1, 4, 1, 8), "MEp41_08"))
reports[-1].posNum = 183035
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000196704, 0.00208056, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0124826, 0.0618422, 0), \
                           ValErr(-0.00231348, 0.00158183, 0), \
                           ValErr(-0.00140182, 0.0026997, 0), \
                           ValErr(-5.3211e-05, 3.85132e-05, 0), \
                           -165982, 183035, 183035, -nan)
reports[-1].sigmaresid = ValErr(0.599234, 0.00099041, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00144138, None, -8.61719e-06, None, -0.00109582, None, -6.61293e-06, None, -0.00109582, None, -6.61293e-06, None, -0.000870149, None, 4.54492e-06, None, -0.000870149, None, 4.54492e-06, None, 0.599239, None, 0.00539916, None, 0.599239, None, 0.00539916, None)

reports.append(Report(604029520, ("CSC", 1, 4, 1, 10), "MEp41_10"))
reports[-1].posNum = 183889
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00418082, 0.00207162, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.00424052, 0.0546165, 0), \
                           ValErr(0.00119548, 0.00129595, 0), \
                           ValErr(0.00219532, 0.00269626, 0), \
                           ValErr(2.44473e-06, 3.35279e-05, 0), \
                           -167341, 183889, 183889, -nan)
reports[-1].sigmaresid = ValErr(0.601139, 0.000986753, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00339611, None, -3.422e-08, None, -0.00294694, None, -1.99231e-07, None, -0.00294694, None, -1.99231e-07, None, -0.00310169, None, -2.81035e-05, None, -0.00310169, None, -2.81035e-05, None, 0.601142, None, 0.00548524, None, 0.601142, None, 0.00548524, None)

reports.append(Report(604029536, ("CSC", 1, 4, 1, 12), "MEp41_12"))
reports[-1].posNum = 183276
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0022201, 0.00207772, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.122031, 0.0506022, 0), \
                           ValErr(0.000370352, 0.00140828, 0), \
                           ValErr(0.00106264, 0.00270093, 0), \
                           ValErr(-2.10277e-06, 3.35907e-05, 0), \
                           -166659, 183276, 183276, -nan)
reports[-1].sigmaresid = ValErr(0.600731, 0.000988458, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0023856, None, -1.85731e-06, None, 0.00280518, None, -5.92949e-07, None, 0.00280518, None, -5.92949e-07, None, -0.000512396, None, -2.09902e-05, None, -0.000512396, None, -2.09902e-05, None, 0.600739, None, 0.00562251, None, 0.600739, None, 0.00562251, None)

reports.append(Report(604029552, ("CSC", 1, 4, 1, 14), "MEp41_14"))
reports[-1].posNum = 184424
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00159105, 0.00208504, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0323484, 0.0618012, 0), \
                           ValErr(0.000740425, 0.00158342, 0), \
                           ValErr(0.00124112, 0.00269818, 0), \
                           ValErr(7.62319e-05, 3.85375e-05, 0), \
                           -168191, 184424, 184424, -nan)
reports[-1].sigmaresid = ValErr(0.602325, 0.000991762, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00145018, None, -1.80832e-05, None, -0.000720037, None, 1.44539e-06, None, -0.000720037, None, 1.44539e-06, None, -0.00121191, None, -2.4483e-05, None, -0.00121191, None, -2.4483e-05, None, 0.602333, None, 0.0056923, None, 0.602333, None, 0.0056923, None)

reports.append(Report(604029568, ("CSC", 1, 4, 1, 16), "MEp41_16"))
reports[-1].posNum = 183719
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00168458, 0.00207716, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0336227, 0.0617257, 0), \
                           ValErr(0.00142483, 0.00157666, 0), \
                           ValErr(0.00177079, 0.00269393, 0), \
                           ValErr(4.3305e-06, 3.84453e-05, 0), \
                           -166528, 183719, 183719, -nan)
reports[-1].sigmaresid = ValErr(0.598991, 0.000988164, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00227617, None, -2.08651e-06, None, -0.000682934, None, 6.95341e-06, None, -0.000682934, None, 6.95341e-06, None, 0.000733431, None, 2.04749e-05, None, 0.000733431, None, 2.04749e-05, None, 0.598993, None, 0.00552075, None, 0.598993, None, 0.00552075, None)

reports.append(Report(604029584, ("CSC", 1, 4, 1, 18), "MEp41_18"))
reports[-1].posNum = 183519
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00392547, 0.00207853, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0232728, 0.0529005, 0), \
                           ValErr(0.000945672, 0.00132566, 0), \
                           ValErr(-0.00224314, 0.00269266, 0), \
                           ValErr(-3.50228e-05, 3.36276e-05, 0), \
                           -166776, 183519, 183519, -nan)
reports[-1].sigmaresid = ValErr(0.600391, 0.000986886, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00311619, None, -1.20402e-07, None, 0.00258449, None, -1.12226e-05, None, 0.00258449, None, -1.12226e-05, None, 0.003407, None, -9.55264e-06, None, 0.003407, None, -9.55264e-06, None, 0.600394, None, 0.00572243, None, 0.600394, None, 0.00572243, None)

reports.append(Report(604029960, ("CSC", 1, 4, 2, 1), "MEp42_01"))
reports[-1].posNum = 80216
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0159683, 0.00640491, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.392226, 0.196111, 0), \
                           ValErr(-0.000317279, 0.00227966, 0), \
                           ValErr(0.0250492, 0.010334, 0), \
                           ValErr(0.000107323, 5.07905e-05, 0), \
                           -121855, 80216, 80216, -nan)
reports[-1].sigmaresid = ValErr(1.10534, 0.00275963, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0027985, None, -3.05864e-05, None, -0.00199833, None, -1.44651e-07, None, -0.00199833, None, -1.44651e-07, None, 0.00566714, None, -3.58141e-05, None, 0.00566714, None, -3.58141e-05, None, 1.10542, None, 0.00759291, None, 1.10542, None, 0.00759291, None)

reports.append(Report(604029976, ("CSC", 1, 4, 2, 3), "MEp42_03"))
reports[-1].posNum = 73171
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0078794, 0.00671409, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.425272, 0.202659, 0), \
                           ValErr(0.00168386, 0.00231277, 0), \
                           ValErr(0.00608486, 0.0107655, 0), \
                           ValErr(8.30498e-05, 5.22927e-05, 0), \
                           -108169, 73171, 73171, -nan)
reports[-1].sigmaresid = ValErr(1.06116, 0.00277392, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00229756, None, 1.92375e-05, None, -0.00182333, None, 7.27353e-05, None, -0.00182333, None, 7.27353e-05, None, -0.00416734, None, 3.96716e-05, None, -0.00416734, None, 3.96716e-05, None, 1.06121, None, 0.00735838, None, 1.06121, None, 0.00735838, None)

reports.append(Report(604029992, ("CSC", 1, 4, 2, 5), "MEp42_05"))
reports[-1].posNum = 80786
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00169927, 0.00623952, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0587913, 0.195548, 0), \
                           ValErr(-0.00170972, 0.00225437, 0), \
                           ValErr(0.0100029, 0.0102126, 0), \
                           ValErr(2.6278e-07, 4.94297e-05, 0), \
                           -121979, 80786, 80786, -nan)
reports[-1].sigmaresid = ValErr(1.09523, 0.0027247, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00471245, None, 1.0851e-05, None, 0.00225552, None, 1.91268e-05, None, 0.00225552, None, 1.91268e-05, None, -0.00155757, None, 8.16602e-06, None, -0.00155757, None, 8.16602e-06, None, 1.09524, None, 0.00743203, None, 1.09524, None, 0.00743203, None)

reports.append(Report(604030008, ("CSC", 1, 4, 2, 7), "MEp42_07"))
reports[-1].posNum = 73303
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00316043, 0.00684929, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.211016, 0.20367, 0), \
                           ValErr(-0.00154453, 0.00234059, 0), \
                           ValErr(0.0028908, 0.0108763, 0), \
                           ValErr(2.0338e-05, 5.3246e-05, 0), \
                           -109542, 73303, 73303, -nan)
reports[-1].sigmaresid = ValErr(1.07836, 0.00281636, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00197704, None, -1.71203e-05, None, -0.00118861, None, -6.46781e-07, None, -0.00118861, None, -6.46781e-07, None, 0.000488242, None, -1.99854e-05, None, 0.000488242, None, -1.99854e-05, None, 1.07837, None, 0.00730419, None, 1.07837, None, 0.00730419, None)

reports.append(Report(604030024, ("CSC", 1, 4, 2, 9), "MEp42_09"))
reports[-1].posNum = 75133
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00109792, 0.00649004, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.602143, 0.20412, 0), \
                           ValErr(-0.000535189, 0.00232571, 0), \
                           ValErr(0.0150742, 0.0106156, 0), \
                           ValErr(6.39784e-05, 5.11194e-05, 0), \
                           -112849, 75133, 75133, -nan)
reports[-1].sigmaresid = ValErr(1.0866, 0.00280312, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00405662, None, -2.58965e-06, None, 0.00750405, None, 2.82653e-05, None, 0.00750405, None, 2.82653e-05, None, 0.013561, None, 1.47498e-05, None, 0.013561, None, 1.47498e-05, None, 1.08669, None, 0.00714807, None, 1.08669, None, 0.00714807, None)

reports.append(Report(604030040, ("CSC", 1, 4, 2, 11), "MEp42_11"))
reports[-1].posNum = 74265
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0133446, 0.00648719, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.104312, 0.189153, 0), \
                           ValErr(-0.00604911, 0.00220205, 0), \
                           ValErr(0.00326584, 0.0103139, 0), \
                           ValErr(7.41585e-05, 4.24558e-05, 0), \
                           -110756, 74265, 74265, -nan)
reports[-1].sigmaresid = ValErr(1.07511, 0.00278277, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00718319, None, -2.48075e-05, None, -0.00903313, None, 8.71563e-06, None, -0.00903313, None, 8.71563e-06, None, -0.00880676, None, 2.34043e-05, None, -0.00880676, None, 2.34043e-05, None, 1.07518, None, 0.00707489, None, 1.07518, None, 0.00707489, None)

reports.append(Report(604030056, ("CSC", 1, 4, 2, 13), "MEp42_13"))
reports[-1].posNum = 72271
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00271451, 0.00690758, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0418927, 0.204464, 0), \
                           ValErr(-0.000566092, 0.00234229, 0), \
                           ValErr(0.0135997, 0.0109252, 0), \
                           ValErr(5.22733e-05, 5.38667e-05, 0), \
                           -107835, 72271, 72271, -nan)
reports[-1].sigmaresid = ValErr(1.0759, 0.00282993, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00498016, None, 1.83599e-05, None, 0.00491495, None, 5.08249e-05, None, 0.00491495, None, 5.08249e-05, None, 0.0057367, None, 2.53138e-05, None, 0.0057367, None, 2.53138e-05, None, 1.07592, None, 0.00727631, None, 1.07592, None, 0.00727631, None)

reports.append(Report(604030072, ("CSC", 1, 4, 2, 15), "MEp42_15"))
reports[-1].posNum = 80837
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00461736, 0.00620057, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.559678, 0.193794, 0), \
                           ValErr(-0.000716474, 0.0022325, 0), \
                           ValErr(0.00417228, 0.0101505, 0), \
                           ValErr(6.73167e-06, 4.91388e-05, 0), \
                           -121577, 80837, 80837, -nan)
reports[-1].sigmaresid = ValErr(1.08876, 0.00270777, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-4.31836e-05, None, -1.48552e-05, None, -0.0027524, None, -1.09099e-05, None, -0.0027524, None, -1.09099e-05, None, -0.00481818, None, -3.03527e-05, None, -0.00481818, None, -3.03527e-05, None, 1.08882, None, 0.00746897, None, 1.08882, None, 0.00746897, None)

reports.append(Report(604030088, ("CSC", 1, 4, 2, 17), "MEp42_17"))
reports[-1].posNum = 72895
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00152722, 0.00680049, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.122785, 0.20722, 0), \
                           ValErr(-0.00466335, 0.00237845, 0), \
                           ValErr(-0.0128117, 0.011001, 0), \
                           ValErr(-2.99291e-05, 5.31756e-05, 0), \
                           -108566, 72895, 72895, -nan)
reports[-1].sigmaresid = ValErr(1.07295, 0.00281006, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00489253, None, -4.27073e-05, None, -0.00473551, None, -8.83563e-06, None, -0.00473551, None, -8.83563e-06, None, -0.000808146, None, -4.92885e-05, None, -0.000808146, None, -4.92885e-05, None, 1.07299, None, 0.00738681, None, 1.07299, None, 0.00738681, None)

reports.append(Report(604030104, ("CSC", 1, 4, 2, 19), "MEp42_19"))
reports[-1].posNum = 81000
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00215246, 0.00637238, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.505014, 0.194381, 0), \
                           ValErr(-0.00422888, 0.00226784, 0), \
                           ValErr(-0.0132001, 0.0103054, 0), \
                           ValErr(-0.000100078, 5.03733e-05, 0), \
                           -122626, 81000, 81000, -nan)
reports[-1].sigmaresid = ValErr(1.09962, 0.00273204, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0108284, None, 1.38366e-05, None, -0.00673794, None, 1.59838e-05, None, -0.00673794, None, 1.59838e-05, None, -0.00216853, None, 1.02903e-06, None, -0.00216853, None, 1.02903e-06, None, 1.09973, None, 0.00723851, None, 1.09973, None, 0.00723851, None)

reports.append(Report(604030120, ("CSC", 1, 4, 2, 21), "MEp42_21"))
reports[-1].posNum = 73437
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00094772, 0.00667158, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.190727, 0.167487, 0), \
                           ValErr(-0.00542213, 0.00194606, 0), \
                           ValErr(0.0115471, 0.0106547, 0), \
                           ValErr(-3.48932e-05, 4.6817e-05, 0), \
                           -108694, 73437, 73437, -nan)
reports[-1].sigmaresid = ValErr(1.06306, 0.00277073, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00137199, None, 6.84371e-06, None, 0.00390595, None, 3.27036e-05, None, 0.00390595, None, 3.27036e-05, None, 0.00342802, None, 2.21046e-05, None, 0.00342802, None, 2.21046e-05, None, 1.06313, None, 0.00721565, None, 1.06313, None, 0.00721565, None)

reports.append(Report(604030136, ("CSC", 1, 4, 2, 23), "MEp42_23"))
reports[-1].posNum = 80277
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00478425, 0.00630401, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0997174, 0.194614, 0), \
                           ValErr(-0.00365224, 0.00225098, 0), \
                           ValErr(0.00594952, 0.0102448, 0), \
                           ValErr(-2.85309e-06, 4.98956e-05, 0), \
                           -120925, 80277, 80277, -nan)
reports[-1].sigmaresid = ValErr(1.09134, 0.00272364, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00499146, None, -2.55773e-05, None, 0.00704617, None, -1.34499e-05, None, 0.00704617, None, -1.34499e-05, None, 0.0081039, None, 8.05322e-07, None, 0.0081039, None, 8.05322e-07, None, 1.09136, None, 0.00810114, None, 1.09136, None, 0.00810114, None)

reports.append(Report(604030152, ("CSC", 1, 4, 2, 25), "MEp42_25"))
reports[-1].posNum = 74836
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00303371, 0.00244284, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.278709, 0.186125, 0), \
                           ValErr(-0.00151636, 0.00159503, 0), \
                           ValErr(0.0122439, 0.00498832, 0), \
                           ValErr(-5.94187e-05, 3.82419e-05, 0), \
                           -112032, 74836, 74836, -nan)
reports[-1].sigmaresid = ValErr(1.08123, 0.00276917, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00487805, None, 5.3028e-05, None, 0.00540752, None, 8.87949e-05, None, 0.00540752, None, 8.87949e-05, None, 0.00138313, None, 5.82773e-05, None, 0.00138313, None, 5.82773e-05, None, 1.08128, None, 0.00729943, None, 1.08128, None, 0.00729943, None)

reports.append(Report(604030168, ("CSC", 1, 4, 2, 27), "MEp42_27"))
reports[-1].posNum = 76300
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00407195, 0.00645281, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.326, 0.201435, 0), \
                           ValErr(0.00361025, 0.00230132, 0), \
                           ValErr(-0.0112722, 0.0105718, 0), \
                           ValErr(-6.47148e-05, 5.05699e-05, 0), \
                           -114374, 76300, 76300, -nan)
reports[-1].sigmaresid = ValErr(1.08335, 0.00277327, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00324671, None, 1.36476e-05, None, -0.00246026, None, 1.13425e-05, None, -0.00246026, None, 1.13425e-05, None, -0.00744507, None, -1.75034e-05, None, -0.00744507, None, -1.75034e-05, None, 1.0834, None, 0.0071848, None, 1.0834, None, 0.0071848, None)

reports.append(Report(604030184, ("CSC", 1, 4, 2, 29), "MEp42_29"))
reports[-1].posNum = 77059
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0152161, 0.00644307, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.476148, 0.200443, 0), \
                           ValErr(0.000419353, 0.00229996, 0), \
                           ValErr(0.0246499, 0.010486, 0), \
                           ValErr(9.16168e-05, 5.08817e-05, 0), \
                           -115465, 77059, 77059, -nan)
reports[-1].sigmaresid = ValErr(1.08271, 0.00275795, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00047919, None, 1.9373e-05, None, -0.00242012, None, 3.58178e-05, None, -0.00242012, None, 3.58178e-05, None, -0.00288145, None, 1.79404e-05, None, -0.00288145, None, 1.79404e-05, None, 1.08279, None, 0.00715629, None, 1.08279, None, 0.00715629, None)

reports.append(Report(604030200, ("CSC", 1, 4, 2, 31), "MEp42_31"))
reports[-1].posNum = 74179
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000461995, 0.0067816, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.73316, 0.201033, 0), \
                           ValErr(-0.00148903, 0.00232403, 0), \
                           ValErr(-0.00310589, 0.0107657, 0), \
                           ValErr(-4.76836e-05, 5.28478e-05, 0), \
                           -110451, 74179, 74179, -nan)
reports[-1].sigmaresid = ValErr(1.07255, 0.00278462, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0078669, None, -2.08831e-06, None, -0.00360938, None, 8.74513e-05, None, -0.00360938, None, 8.74513e-05, None, -0.00407209, None, 4.31708e-05, None, -0.00407209, None, 4.31708e-05, None, 1.07266, None, 0.00872025, None, 1.07266, None, 0.00872025, None)

reports.append(Report(604030216, ("CSC", 1, 4, 2, 33), "MEp42_33"))
reports[-1].posNum = 80315
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0173642, 0.00625374, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.173554, 0.19418, 0), \
                           ValErr(-0.0021366, 0.00224072, 0), \
                           ValErr(-0.0243725, 0.0101674, 0), \
                           ValErr(-0.000109161, 4.94782e-05, 0), \
                           -120728, 80315, 80315, -nan)
reports[-1].sigmaresid = ValErr(1.08789, 0.00271437, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00849303, None, 6.21312e-05, None, 0.00376062, None, 0.000122376, None, 0.00376062, None, 0.000122376, None, 0.00303154, None, 5.89893e-05, None, 0.00303154, None, 5.89893e-05, None, 1.08795, None, 0.00730801, None, 1.08795, None, 0.00730801, None)

reports.append(Report(604030232, ("CSC", 1, 4, 2, 35), "MEp42_35"))
reports[-1].posNum = 72093
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00748217, 0.00680717, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.326914, 0.204944, 0), \
                           ValErr(-0.00243302, 0.00236162, 0), \
                           ValErr(0.0054681, 0.0109149, 0), \
                           ValErr(3.62573e-05, 5.30721e-05, 0), \
                           -106090, 72093, 72093, -nan)
reports[-1].sigmaresid = ValErr(1.05404, 0.00277584, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0101427, None, 5.71319e-05, None, -0.00372037, None, 6.98317e-05, None, -0.00372037, None, 6.98317e-05, None, -0.00415205, None, 6.30697e-05, None, -0.00415205, None, 6.30697e-05, None, 1.05408, None, 0.00744938, None, 1.05408, None, 0.00744938, None)

reports.append(Report(604029968, ("CSC", 1, 4, 2, 2), "MEp42_02"))
reports[-1].posNum = 78156
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00808358, 0.00652238, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.652264, 0.209543, 0), \
                           ValErr(0.00115483, 0.0024324, 0), \
                           ValErr(-0.00108391, 0.01094, 0), \
                           ValErr(8.59091e-05, 5.18456e-05, 0), \
                           -118692, 78156, 78156, -nan)
reports[-1].sigmaresid = ValErr(1.10487, 0.00279456, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0038685, None, -6.30885e-05, None, -0.00549231, None, -8.70088e-05, None, -0.00549231, None, -8.70088e-05, None, -0.011438, None, -0.000117922, None, -0.011438, None, -0.000117922, None, 1.10496, None, 0.00783378, None, 1.10496, None, 0.00783378, None)

reports.append(Report(604029984, ("CSC", 1, 4, 2, 4), "MEp42_04"))
reports[-1].posNum = 76460
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00324641, 0.0067173, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.418555, 0.213048, 0), \
                           ValErr(-0.00154942, 0.00247652, 0), \
                           ValErr(0.00161749, 0.011213, 0), \
                           ValErr(-4.93959e-05, 5.31264e-05, 0), \
                           -115839, 76460, 76460, -nan)
reports[-1].sigmaresid = ValErr(1.10086, 0.00281514, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00337537, None, -3.03753e-05, None, 0.00187448, None, -5.25104e-06, None, 0.00187448, None, -5.25104e-06, None, 0.0044186, None, -1.29897e-05, None, 0.0044186, None, -1.29897e-05, None, 1.1009, None, 0.00686102, None, 1.1009, None, 0.00686102, None)

reports.append(Report(604030000, ("CSC", 1, 4, 2, 6), "MEp42_06"))
reports[-1].posNum = 80936
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00768364, 0.00632723, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.264009, 0.202003, 0), \
                           ValErr(-0.000189456, 0.00235701, 0), \
                           ValErr(-0.0114268, 0.0105563, 0), \
                           ValErr(3.91569e-06, 5.04198e-05, 0), \
                           -122917, 80936, 80936, -nan)
reports[-1].sigmaresid = ValErr(1.10491, 0.00274625, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00524792, None, 1.01347e-05, None, 0.00338943, None, -8.28416e-06, None, 0.00338943, None, -8.28416e-06, None, 0.000435137, None, 1.29269e-05, None, 0.000435137, None, 1.29269e-05, None, 1.10493, None, 0.00736142, None, 1.10493, None, 0.00736142, None)

reports.append(Report(604030016, ("CSC", 1, 4, 2, 8), "MEp42_08"))
reports[-1].posNum = 73673
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00625485, 0.0068769, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.151717, 0.212378, 0), \
                           ValErr(-0.00219561, 0.00246046, 0), \
                           ValErr(0.00640207, 0.0112893, 0), \
                           ValErr(2.38536e-05, 5.43213e-05, 0), \
                           -110075, 73673, 73673, -nan)
reports[-1].sigmaresid = ValErr(1.07807, 0.00280851, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00623687, None, -4.62268e-05, None, -0.00273722, None, -3.88704e-05, None, -0.00273722, None, -3.88704e-05, None, -0.00206341, None, -4.61913e-05, None, -0.00206341, None, -4.61913e-05, None, 1.07808, None, 0.00710413, None, 1.07808, None, 0.00710413, None)

reports.append(Report(604030032, ("CSC", 1, 4, 2, 10), "MEp42_10"))
reports[-1].posNum = 83718
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00793797, 0.00631582, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.110688, 0.0905668, 0), \
                           ValErr(-0.00126065, 0.00109393, 0), \
                           ValErr(-0.00549492, 0.0105141, 0), \
                           ValErr(-4.28559e-05, 5.00355e-05, 0), \
                           -128701, 83718, 83718, -nan)
reports[-1].sigmaresid = ValErr(1.12567, 0.00274392, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00521614, None, -1.54443e-05, None, 0.00437515, None, -2.79315e-05, None, 0.00437515, None, -2.79315e-05, None, 0.00445235, None, -1.95361e-05, None, 0.00445235, None, -1.95361e-05, None, 1.12567, None, 0.00694785, None, 1.12567, None, 0.00694785, None)

reports.append(Report(604030048, ("CSC", 1, 4, 2, 12), "MEp42_12"))
reports[-1].posNum = 73928
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000258352, 0.00666955, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.109257, 0.212716, 0), \
                           ValErr(0.000297059, 0.00247783, 0), \
                           ValErr(-0.000325033, 0.0111936, 0), \
                           ValErr(-3.05682e-05, 5.27805e-05, 0), \
                           -110533, 73928, 73928, -nan)
reports[-1].sigmaresid = ValErr(1.07918, 0.00280656, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00402385, None, -7.68113e-06, None, -0.00112717, None, -3.25139e-05, None, -0.00112717, None, -3.25139e-05, None, 0.00432366, None, -4.49131e-05, None, 0.00432366, None, -4.49131e-05, None, 1.07918, None, 0.00710844, None, 1.07918, None, 0.00710844, None)

reports.append(Report(604030064, ("CSC", 1, 4, 2, 14), "MEp42_14"))
reports[-1].posNum = 81679
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00348422, 0.00634676, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.218195, 0.200895, 0), \
                           ValErr(-0.00294271, 0.00234858, 0), \
                           ValErr(0.0069452, 0.0105681, 0), \
                           ValErr(-6.74187e-06, 5.05609e-05, 0), \
                           -124304, 81679, 81679, -nan)
reports[-1].sigmaresid = ValErr(1.10841, 0.00274179, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00471403, None, 1.15392e-05, None, 0.00593484, None, 5.17726e-05, None, 0.00593484, None, 5.17726e-05, None, 0.00936247, None, 3.95327e-05, None, 0.00936247, None, 3.95327e-05, None, 1.10843, None, 0.00728316, None, 1.10843, None, 0.00728316, None)

reports.append(Report(604030080, ("CSC", 1, 4, 2, 16), "MEp42_16"))
reports[-1].posNum = 75854
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00401663, 0.00670197, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0231056, 0.212247, 0), \
                           ValErr(-0.000773111, 0.00247451, 0), \
                           ValErr(0.00707846, 0.0111823, 0), \
                           ValErr(6.62551e-06, 5.28557e-05, 0), \
                           -114291, 75854, 75854, -nan)
reports[-1].sigmaresid = ValErr(1.09176, 0.002803, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00121416, None, -2.13275e-05, None, -0.00105272, None, -2.52656e-05, None, -0.00105272, None, -2.52656e-05, None, 0.00329836, None, -2.50815e-05, None, 0.00329836, None, -2.50815e-05, None, 1.09176, None, 0.007192, None, 1.09176, None, 0.007192, None)

reports.append(Report(604030096, ("CSC", 1, 4, 2, 18), "MEp42_18"))
reports[-1].posNum = 77364
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0041197, 0.00656048, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0415648, 0.205313, 0), \
                           ValErr(-0.00475136, 0.00234218, 0), \
                           ValErr(0.0139592, 0.010432, 0), \
                           ValErr(1.73313e-05, 3.97108e-05, 0), \
                           -117510, 77364, 77364, -nan)
reports[-1].sigmaresid = ValErr(1.10515, 0.00280966, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00297187, None, -1.94735e-05, None, 0.00182303, None, -7.11908e-06, None, 0.00182303, None, -7.11908e-06, None, 0.00116485, None, -8.52241e-06, None, 0.00116485, None, -8.52241e-06, None, 1.10519, None, 0.00796821, None, 1.10519, None, 0.00796821, None)

reports.append(Report(604030112, ("CSC", 1, 4, 2, 20), "MEp42_20"))
reports[-1].posNum = 79298
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00344447, 0.00648748, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.343092, 0.148836, 0), \
                           ValErr(-0.00351445, 0.00178192, 0), \
                           ValErr(-0.0146183, 0.0107648, 0), \
                           ValErr(-1.78562e-05, 5.13749e-05, 0), \
                           -120434, 79298, 79298, -nan)
reports[-1].sigmaresid = ValErr(1.10496, 0.00277414, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00227209, None, 5.73798e-06, None, -0.00291614, None, -1.76277e-07, None, -0.00291614, None, -1.76277e-07, None, -0.00751262, None, -3.20468e-05, None, -0.00751262, None, -3.20468e-05, None, 1.10501, None, 0.00705522, None, 1.10501, None, 0.00705522, None)

reports.append(Report(604030128, ("CSC", 1, 4, 2, 22), "MEp42_22"))
reports[-1].posNum = 76171
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0142365, 0.00664181, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.61155, 0.208861, 0), \
                           ValErr(7.70672e-05, 0.00244129, 0), \
                           ValErr(-0.0194931, 0.0110222, 0), \
                           ValErr(-0.000101491, 5.25542e-05, 0), \
                           -114531, 76171, 76171, -nan)
reports[-1].sigmaresid = ValErr(1.08835, 0.00278843, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00481831, None, 1.44815e-05, None, 0.00274448, None, -1.07314e-05, None, 0.00274448, None, -1.07314e-05, None, 0.00827014, None, 1.99551e-05, None, 0.00827014, None, 1.99551e-05, None, 1.08845, None, 0.00717084, None, 1.08845, None, 0.00717084, None)

reports.append(Report(604030144, ("CSC", 1, 4, 2, 24), "MEp42_24"))
reports[-1].posNum = 81515
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00225076, 0.00621807, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.372957, 0.200344, 0), \
                           ValErr(-0.00435033, 0.0023497, 0), \
                           ValErr(-0.0216685, 0.0104507, 0), \
                           ValErr(-1.59091e-05, 4.95846e-05, 0), \
                           -123329, 81515, 81515, -nan)
reports[-1].sigmaresid = ValErr(1.09859, 0.00272083, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00812173, None, -2.83294e-05, None, -0.00673758, None, -3.11991e-05, None, -0.00673758, None, -3.11991e-05, None, -0.005071, None, -2.08583e-05, None, -0.005071, None, -2.08583e-05, None, 1.09867, None, 0.00713722, None, 1.09867, None, 0.00713722, None)

reports.append(Report(604030160, ("CSC", 1, 4, 2, 26), "MEp42_26"))
reports[-1].posNum = 74997
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0109049, 0.00680883, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.454491, 0.210613, 0), \
                           ValErr(-0.000303221, 0.00244316, 0), \
                           ValErr(0.0106568, 0.0112392, 0), \
                           ValErr(-6.70533e-05, 5.36024e-05, 0), \
                           -112315, 74997, 74997, -nan)
reports[-1].sigmaresid = ValErr(1.08183, 0.00279334, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00937751, None, -6.35823e-06, None, -0.00986458, None, -1.52789e-05, None, -0.00986458, None, -1.52789e-05, None, -0.00623337, None, -1.58712e-05, None, -0.00623337, None, -1.58712e-05, None, 1.08189, None, 0.00733641, None, 1.08189, None, 0.00733641, None)

reports.append(Report(604030176, ("CSC", 1, 4, 2, 28), "MEp42_28"))
reports[-1].posNum = 82783
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000744328, 0.00635491, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.733468, 0.199915, 0), \
                           ValErr(-0.00114529, 0.00234701, 0), \
                           ValErr(-0.00848228, 0.0105098, 0), \
                           ValErr(-5.48632e-05, 5.08103e-05, 0), \
                           -126887, 82783, 82783, -nan)
reports[-1].sigmaresid = ValErr(1.12056, 0.00275391, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0108035, None, -4.88496e-05, None, -0.00601498, None, -6.97757e-05, None, -0.00601498, None, -6.97757e-05, None, -0.00438823, None, -6.53895e-05, None, -0.00438823, None, -6.53895e-05, None, 1.12066, None, 0.00703167, None, 1.12066, None, 0.00703167, None)

reports.append(Report(604030192, ("CSC", 1, 4, 2, 30), "MEp42_30"))
reports[-1].posNum = 73520
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00131861, 0.00675724, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.157095, 0.211926, 0), \
                           ValErr(-0.00330236, 0.00244306, 0), \
                           ValErr(0.00946378, 0.0111523, 0), \
                           ValErr(6.24099e-06, 5.32857e-05, 0), \
                           -109362, 73520, 73520, -nan)
reports[-1].sigmaresid = ValErr(1.07098, 0.00279296, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00736651, None, 2.7875e-05, None, 0.00255255, None, 5.53758e-05, None, 0.00255255, None, 5.53758e-05, None, 0.00402468, None, 6.47882e-05, None, 0.00402468, None, 6.47882e-05, None, 1.07101, None, 0.00723232, None, 1.07101, None, 0.00723232, None)

reports.append(Report(604030208, ("CSC", 1, 4, 2, 32), "MEp42_32"))
reports[-1].posNum = 81262
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.016098, 0.00635715, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00943987, 0.202353, 0), \
                           ValErr(-0.000436972, 0.00236102, 0), \
                           ValErr(0.00376053, 0.0106421, 0), \
                           ValErr(0.000112955, 5.0704e-05, 0), \
                           -123583, 81262, 81262, -nan)
reports[-1].sigmaresid = ValErr(1.10723, 0.0027465, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00941956, None, 9.4079e-06, None, -0.0105803, None, -1.50861e-05, None, -0.0105803, None, -1.50861e-05, None, -0.0126974, None, 3.72702e-06, None, -0.0126974, None, 3.72702e-06, None, 1.10727, None, 0.00711031, None, 1.10727, None, 0.00711031, None)

reports.append(Report(604030224, ("CSC", 1, 4, 2, 34), "MEp42_34"))
reports[-1].posNum = 77119
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0166036, 0.00667771, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0517382, 0.211785, 0), \
                           ValErr(-0.00117321, 0.00247581, 0), \
                           ValErr(0.0163747, 0.0111597, 0), \
                           ValErr(5.97345e-05, 5.29324e-05, 0), \
                           -117318, 77119, 77119, -nan)
reports[-1].sigmaresid = ValErr(1.10774, 0.00282061, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00964079, None, -6.62145e-05, None, -0.00796244, None, -8.65365e-05, None, -0.00796244, None, -8.65365e-05, None, -0.0124105, None, -8.66092e-05, None, -0.0124105, None, -8.66092e-05, None, 1.10776, None, 0.00752736, None, 1.10776, None, 0.00752736, None)

reports.append(Report(604030240, ("CSC", 1, 4, 2, 36), "MEp42_36"))
reports[-1].posNum = 79593
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0100901, 0.00641719, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.7454, 0.205116, 0), \
                           ValErr(0.00428546, 0.0023906, 0), \
                           ValErr(-0.00394869, 0.0107346, 0), \
                           ValErr(3.8771e-05, 5.09704e-05, 0), \
                           -120788, 79593, 79593, -nan)
reports[-1].sigmaresid = ValErr(1.10366, 0.0027662, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00641363, None, 1.43729e-05, None, 0.0102796, None, 4.6762e-05, None, 0.0102796, None, 4.6762e-05, None, 0.0113814, None, 5.79939e-05, None, 0.0113814, None, 5.79939e-05, None, 1.10377, None, 0.00713536, None, 1.10377, None, 0.00713536, None)

reports.append(Report(604050440, ("CSC", 2, 1, 1, 1), "MEm11_01"))
reports[-1].posNum = 214554
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00257566, 0.000574416, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0869217, 0.0331047, 0), \
                           ValErr(-0.00222018, 0.000875954, 0), \
                           ValErr(-0.00534632, 0.00435769, 0), \
                           ValErr(-3.42199e-06, 1.17869e-05, 0), \
                           51651.2, 214554, 214554, -nan)
reports[-1].sigmaresid = ValErr(0.190201, 0.000290354, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00264322, None, -4.67067e-06, None, 0.00298377, None, -3.33059e-06, None, 0.00298377, None, -3.33059e-06, None, 0.00255314, None, -4.11003e-06, None, 0.00255314, None, -4.11003e-06, None, 0.190206, None, 0.00424221, None, 0.190206, None, 0.00424221, None)

reports.append(Report(604050456, ("CSC", 2, 1, 1, 3), "MEm11_03"))
reports[-1].posNum = 217389
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00242848, 0.00056909, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.120498, 0.0326986, 0), \
                           ValErr(-0.00221287, 0.000865955, 0), \
                           ValErr(-0.00330843, 0.00433382, 0), \
                           ValErr(-4.5235e-06, 1.1604e-05, 0), \
                           53751.1, 217389, 217389, -nan)
reports[-1].sigmaresid = ValErr(0.188964, 0.00028658, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00252795, None, -5.70436e-06, None, 0.00265084, None, -1.13643e-05, None, 0.00265084, None, -1.13643e-05, None, 0.00288481, None, -1.11035e-05, None, 0.00288481, None, -1.11035e-05, None, 0.188972, None, 0.0043208, None, 0.188972, None, 0.0043208, None)

reports.append(Report(604050472, ("CSC", 2, 1, 1, 5), "MEm11_05"))
reports[-1].posNum = 214754
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00207912, 0.000577175, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0636451, 0.0332434, 0), \
                           ValErr(-3.08207e-05, 0.000885061, 0), \
                           ValErr(-0.00162473, 0.00440362, 0), \
                           ValErr(-2.75558e-05, 1.18669e-05, 0), \
                           50883.1, 214754, 214754, -nan)
reports[-1].sigmaresid = ValErr(0.190925, 0.000291324, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00176546, None, -1.86749e-07, None, 0.00197875, None, -2.25835e-05, None, 0.00197875, None, -2.25835e-05, None, 0.000851869, None, -6.0641e-06, None, 0.000851869, None, -6.0641e-06, None, 0.19093, None, 0.00453646, None, 0.19093, None, 0.00453646, None)

reports.append(Report(604050488, ("CSC", 2, 1, 1, 7), "MEm11_07"))
reports[-1].posNum = 215894
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00129002, 0.000572435, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0597524, 0.0330436, 0), \
                           ValErr(-4.93808e-05, 0.000871302, 0), \
                           ValErr(-0.00724779, 0.00436596, 0), \
                           ValErr(-4.14713e-07, 1.169e-05, 0), \
                           52355.2, 215894, 215894, -nan)
reports[-1].sigmaresid = ValErr(0.189865, 0.000288941, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00175777, None, 4.08982e-06, None, 0.00187035, None, 1.6209e-05, None, 0.00187035, None, 1.6209e-05, None, 0.00130327, None, 2.46517e-05, None, 0.00130327, None, 2.46517e-05, None, 0.189868, None, 0.00415557, None, 0.189868, None, 0.00415557, None)

reports.append(Report(604050504, ("CSC", 2, 1, 1, 9), "MEm11_09"))
reports[-1].posNum = 215114
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000681234, 0.000577742, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0806157, 0.0332406, 0), \
                           ValErr(-0.00124459, 0.000881552, 0), \
                           ValErr(-0.00632429, 0.0044011, 0), \
                           ValErr(-7.42931e-07, 1.1843e-05, 0), \
                           50544.5, 215114, 215114, -nan)
reports[-1].sigmaresid = ValErr(0.191301, 0.000291655, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000902574, None, -4.56685e-06, None, 0.00118727, None, -1.57289e-05, None, 0.00118727, None, -1.57289e-05, None, 0.000419407, None, 1.38344e-05, None, 0.000419407, None, 1.38344e-05, None, 0.191305, None, 0.00447135, None, 0.191305, None, 0.00447135, None)

reports.append(Report(604050520, ("CSC", 2, 1, 1, 11), "MEm11_11"))
reports[-1].posNum = 215396
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00128842, 0.00057711, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.139283, 0.0332205, 0), \
                           ValErr(-0.000394752, 0.000880774, 0), \
                           ValErr(0.00334747, 0.00437934, 0), \
                           ValErr(1.45227e-05, 1.18394e-05, 0), \
                           50592.3, 215396, 215396, -nan)
reports[-1].sigmaresid = ValErr(0.191318, 0.000291489, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00129928, None, 9.37475e-06, None, 0.00113787, None, 2.1893e-05, None, 0.00113787, None, 2.1893e-05, None, -0.000458334, None, 2.42901e-05, None, -0.000458334, None, 2.42901e-05, None, 0.191327, None, 0.00425986, None, 0.191327, None, 0.00425986, None)

reports.append(Report(604050536, ("CSC", 2, 1, 1, 13), "MEm11_13"))
reports[-1].posNum = 214874
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00149547, 0.00057583, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.136184, 0.0331677, 0), \
                           ValErr(-0.000980657, 0.000878343, 0), \
                           ValErr(-0.000342693, 0.00439398, 0), \
                           ValErr(2.09411e-05, 1.17584e-05, 0), \
                           51485.9, 214874, 214874, -nan)
reports[-1].sigmaresid = ValErr(0.190415, 0.000290466, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00168217, None, 3.54693e-06, None, 0.00171877, None, 3.63714e-06, None, 0.00171877, None, 3.63714e-06, None, 0.00126964, None, 6.9538e-06, None, 0.00126964, None, 6.9538e-06, None, 0.190424, None, 0.00417729, None, 0.190424, None, 0.00417729, None)

reports.append(Report(604050552, ("CSC", 2, 1, 1, 15), "MEm11_15"))
reports[-1].posNum = 215553
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00249758, 0.00057671, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.140701, 0.0331814, 0), \
                           ValErr(-0.000933362, 0.000878795, 0), \
                           ValErr(-0.00626494, 0.00437205, 0), \
                           ValErr(-1.425e-05, 1.18197e-05, 0), \
                           50652.4, 215553, 215553, -nan)
reports[-1].sigmaresid = ValErr(0.191297, 0.000291351, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00278883, None, 1.67087e-06, None, 0.00288558, None, 6.66598e-07, None, 0.00288558, None, 6.66598e-07, None, 0.00200016, None, 6.50713e-06, None, 0.00200016, None, 6.50713e-06, None, 0.191308, None, 0.00454323, None, 0.191308, None, 0.00454323, None)

reports.append(Report(604050568, ("CSC", 2, 1, 1, 17), "MEm11_17"))
reports[-1].posNum = 215095
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.002167, 0.000572911, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0799678, 0.0328818, 0), \
                           ValErr(-0.000590092, 0.000869083, 0), \
                           ValErr(-0.00359437, 0.0043722, 0), \
                           ValErr(-2.09187e-05, 1.16559e-05, 0), \
                           53190, 215095, 215095, -nan)
reports[-1].sigmaresid = ValErr(0.188959, 0.000288097, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00224095, None, 7.91887e-07, None, 0.00226287, None, 1.40151e-05, None, 0.00226287, None, 1.40151e-05, None, 0.00183008, None, 1.97828e-05, None, 0.00183008, None, 1.97828e-05, None, 0.188964, None, 0.00424529, None, 0.188964, None, 0.00424529, None)

reports.append(Report(604050584, ("CSC", 2, 1, 1, 19), "MEm11_19"))
reports[-1].posNum = 215612
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00275699, 0.000575016, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.133876, 0.0332446, 0), \
                           ValErr(-0.00108721, 0.000878875, 0), \
                           ValErr(0.000386196, 0.00439087, 0), \
                           ValErr(-2.84399e-05, 1.17973e-05, 0), \
                           50886.2, 215612, 215612, -nan)
reports[-1].sigmaresid = ValErr(0.191102, 0.000291014, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00244297, None, -1.04747e-06, None, 0.00249574, None, -1.05135e-05, None, 0.00249574, None, -1.05135e-05, None, 0.00130221, None, 1.56246e-05, None, 0.00130221, None, 1.56246e-05, None, 0.191112, None, 0.00422632, None, 0.191112, None, 0.00422632, None)

reports.append(Report(604050600, ("CSC", 2, 1, 1, 21), "MEm11_21"))
reports[-1].posNum = 215744
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00145903, 0.000572196, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0106302, 0.032987, 0), \
                           ValErr(-0.00210554, 0.000871951, 0), \
                           ValErr(-0.00932941, 0.0043577, 0), \
                           ValErr(-4.77455e-06, 1.16546e-05, 0), \
                           52757.1, 215744, 215744, -nan)
reports[-1].sigmaresid = ValErr(0.18948, 0.000288455, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00217409, None, 1.85677e-06, None, 0.00216742, None, 1.99415e-05, None, 0.00216742, None, 1.99415e-05, None, 0.000491713, None, 3.25757e-05, None, 0.000491713, None, 3.25757e-05, None, 0.189485, None, 0.00422093, None, 0.189485, None, 0.00422093, None)

reports.append(Report(604050616, ("CSC", 2, 1, 1, 23), "MEm11_23"))
reports[-1].posNum = 214580
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00213086, 0.000576123, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.136698, 0.0332357, 0), \
                           ValErr(-0.000526634, 0.000882248, 0), \
                           ValErr(-0.00150406, 0.00438035, 0), \
                           ValErr(-1.41763e-05, 1.1836e-05, 0), \
                           50730.2, 214580, 214580, -nan)
reports[-1].sigmaresid = ValErr(0.191024, 0.000291594, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00122199, None, 3.28895e-06, None, 0.00214804, None, 1.5793e-05, None, 0.00214804, None, 1.5793e-05, None, 0.00135517, None, 5.73613e-07, None, 0.00135517, None, 5.73613e-07, None, 0.191033, None, 0.00474056, None, 0.191033, None, 0.00474056, None)

reports.append(Report(604050632, ("CSC", 2, 1, 1, 25), "MEm11_25"))
reports[-1].posNum = 216232
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00247701, 0.000570041, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0489926, 0.0328779, 0), \
                           ValErr(-0.000355549, 0.000868405, 0), \
                           ValErr(-0.00519464, 0.00433156, 0), \
                           ValErr(-1.86482e-05, 1.16424e-05, 0), \
                           53158.4, 216232, 216232, -nan)
reports[-1].sigmaresid = ValErr(0.189233, 0.000287754, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00235543, None, -1.41638e-06, None, 0.00273861, None, -4.55724e-06, None, 0.00273861, None, -4.55724e-06, None, 0.00184879, None, 1.51268e-05, None, 0.00184879, None, 1.51268e-05, None, 0.189236, None, 0.00462513, None, 0.189236, None, 0.00462513, None)

reports.append(Report(604050648, ("CSC", 2, 1, 1, 27), "MEm11_27"))
reports[-1].posNum = 214285
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00130848, 0.000578322, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0996193, 0.0333432, 0), \
                           ValErr(-0.00336104, 0.000883733, 0), \
                           ValErr(-0.00663747, 0.00439558, 0), \
                           ValErr(2.44761e-06, 1.18682e-05, 0), \
                           50312.3, 214285, 214285, -nan)
reports[-1].sigmaresid = ValErr(0.191335, 0.000292269, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00144377, None, 5.79048e-06, None, 0.00188272, None, -1.99386e-05, None, 0.00188272, None, -1.99386e-05, None, 0.00120334, None, -4.08724e-06, None, 0.00120334, None, -4.08724e-06, None, 0.191344, None, 0.00547244, None, 0.191344, None, 0.00547244, None)

reports.append(Report(604050664, ("CSC", 2, 1, 1, 29), "MEm11_29"))
reports[-1].posNum = 214340
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00177268, 0.000575435, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.100315, 0.0331657, 0), \
                           ValErr(-0.00254361, 0.00087905, 0), \
                           ValErr(0.00384414, 0.00438062, 0), \
                           ValErr(-6.86011e-07, 1.17944e-05, 0), \
                           51432.5, 214340, 214340, -nan)
reports[-1].sigmaresid = ValErr(0.190349, 0.000290725, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00169166, None, 4.47048e-06, None, 0.00146485, None, 7.12212e-06, None, 0.00146485, None, 7.12212e-06, None, 0.000520956, None, 2.19948e-05, None, 0.000520956, None, 2.19948e-05, None, 0.190355, None, 0.00418764, None, 0.190355, None, 0.00418764, None)

reports.append(Report(604050680, ("CSC", 2, 1, 1, 31), "MEm11_31"))
reports[-1].posNum = 216127
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00229993, 0.000572675, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0517692, 0.0329164, 0), \
                           ValErr(-0.000939811, 0.000870857, 0), \
                           ValErr(-0.00629285, 0.00436076, 0), \
                           ValErr(-1.75141e-05, 1.16794e-05, 0), \
                           52651.7, 216127, 216127, -nan)
reports[-1].sigmaresid = ValErr(0.189654, 0.000288465, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00237737, None, 3.37312e-07, None, 0.00266214, None, 7.82149e-06, None, 0.00266214, None, 7.82149e-06, None, 0.00176368, None, 2.975e-05, None, 0.00176368, None, 2.975e-05, None, 0.189658, None, 0.0044606, None, 0.189658, None, 0.0044606, None)

reports.append(Report(604050696, ("CSC", 2, 1, 1, 33), "MEm11_33"))
reports[-1].posNum = 216206
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00292946, 0.000574599, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0872603, 0.0331373, 0), \
                           ValErr(0.000239618, 0.000875916, 0), \
                           ValErr(-0.000861725, 0.00436582, 0), \
                           ValErr(-1.91075e-05, 1.17648e-05, 0), \
                           51201.9, 216206, 216206, -nan)
reports[-1].sigmaresid = ValErr(0.190947, 0.000290379, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00260735, None, -9.92248e-06, None, 0.00284074, None, -7.98469e-06, None, 0.00284074, None, -7.98469e-06, None, 0.00219427, None, 6.5066e-06, None, 0.00219427, None, 6.5066e-06, None, 0.190952, None, 0.0042797, None, 0.190952, None, 0.0042797, None)

reports.append(Report(604050712, ("CSC", 2, 1, 1, 35), "MEm11_35"))
reports[-1].posNum = 217102
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00221252, 0.000568279, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0408963, 0.0326533, 0), \
                           ValErr(-0.000763807, 0.000865446, 0), \
                           ValErr(-0.000880693, 0.00434832, 0), \
                           ValErr(8.97218e-06, 1.15582e-05, 0), \
                           54439, 217102, 217102, -nan)
reports[-1].sigmaresid = ValErr(0.188305, 0.000285768, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00186539, None, -7.59353e-06, None, 0.00236837, None, -1.23761e-05, None, 0.00236837, None, -1.23761e-05, None, 0.00195399, None, 1.17636e-05, None, 0.00195399, None, 1.17636e-05, None, 0.188306, None, 0.00465053, None, 0.188306, None, 0.00465053, None)

reports.append(Report(604050448, ("CSC", 2, 1, 1, 2), "MEm11_02"))
reports[-1].posNum = 215436
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00201101, 0.000514754, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.024168, 0.0280293, 0), \
                           ValErr(-0.000667441, 0.000742498, 0), \
                           ValErr(0.00124666, 0.0037205, 0), \
                           ValErr(-3.94989e-06, 1.04683e-05, 0), \
                           75810.9, 215436, 215436, -nan)
reports[-1].sigmaresid = ValErr(0.170191, 0.000259276, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00158478, None, -1.1126e-05, None, 0.00186899, None, -2.47337e-06, None, 0.00186899, None, -2.47337e-06, None, 0.00195532, None, -5.13907e-06, None, 0.00195532, None, -5.13907e-06, None, 0.170192, None, 0.00461149, None, 0.170192, None, 0.00461149, None)

reports.append(Report(604050464, ("CSC", 2, 1, 1, 4), "MEm11_04"))
reports[-1].posNum = 214645
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00172393, 0.00051381, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.126635, 0.0279865, 0), \
                           ValErr(-0.00123392, 0.000740309, 0), \
                           ValErr(0.00109153, 0.00371074, 0), \
                           ValErr(2.64579e-06, 1.04589e-05, 0), \
                           76339.7, 214645, 214645, -nan)
reports[-1].sigmaresid = ValErr(0.169552, 0.000258779, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00111887, None, -5.42068e-06, None, 0.00165641, None, -2.03062e-05, None, 0.00165641, None, -2.03062e-05, None, 0.0017975, None, -1.02421e-05, None, 0.0017975, None, -1.02421e-05, None, 0.169561, None, 0.00433306, None, 0.169561, None, 0.00433306, None)

reports.append(Report(604050480, ("CSC", 2, 1, 1, 6), "MEm11_06"))
reports[-1].posNum = 214654
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00151437, 0.000518705, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.100394, 0.0282002, 0), \
                           ValErr(-0.00028789, 0.000746067, 0), \
                           ValErr(0.00205497, 0.00373192, 0), \
                           ValErr(-1.35627e-05, 1.05535e-05, 0), \
                           74406, 214654, 214654, -nan)
reports[-1].sigmaresid = ValErr(0.171089, 0.000261119, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00160502, None, 8.07403e-07, None, 0.00120992, None, -2.74554e-05, None, 0.00120992, None, -2.74554e-05, None, 0.000770547, None, 2.77314e-06, None, 0.000770547, None, 2.77314e-06, None, 0.171095, None, 0.00454133, None, 0.171095, None, 0.00454133, None)

reports.append(Report(604050496, ("CSC", 2, 1, 1, 8), "MEm11_08"))
reports[-1].posNum = 214186
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00243864, 0.00051377, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0669558, 0.0291405, 0), \
                           ValErr(0.000181057, 0.000765234, 0), \
                           ValErr(-0.00015983, 0.00374299, 0), \
                           ValErr(-1.31977e-05, 1.13241e-05, 0), \
                           76541.6, 214186, 214186, -nan)
reports[-1].sigmaresid = ValErr(0.169263, 0.000257965, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00204946, None, -6.83569e-06, None, 0.00232812, None, -2.01654e-05, None, 0.00232812, None, -2.01654e-05, None, 0.00189021, None, -1.49116e-05, None, 0.00189021, None, -1.49116e-05, None, 0.169267, None, 0.00466234, None, 0.169267, None, 0.00466234, None)

reports.append(Report(604050512, ("CSC", 2, 1, 1, 10), "MEm11_10"))
reports[-1].posNum = 214140
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00272208, 0.000518465, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.115235, 0.0281802, 0), \
                           ValErr(-0.000628049, 0.000744639, 0), \
                           ValErr(0.00266019, 0.00374867, 0), \
                           ValErr(-1.81104e-05, 1.05448e-05, 0), \
                           74855.5, 214140, 214140, -nan)
reports[-1].sigmaresid = ValErr(0.170588, 0.000260667, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00183206, None, -8.5882e-06, None, 0.00232665, None, -2.63835e-05, None, 0.00232665, None, -2.63835e-05, None, 0.00200006, None, -2.27814e-05, None, 0.00200006, None, -2.27814e-05, None, 0.170596, None, 0.00476792, None, 0.170596, None, 0.00476792, None)

reports.append(Report(604050528, ("CSC", 2, 1, 1, 12), "MEm11_12"))
reports[-1].posNum = 214260
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0023496, 0.000512877, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0521106, 0.030686, 0), \
                           ValErr(-0.00076814, 0.000804355, 0), \
                           ValErr(0.00102435, 0.00371193, 0), \
                           ValErr(-1.55004e-05, 1.06327e-05, 0), \
                           76645.4, 214260, 214260, -nan)
reports[-1].sigmaresid = ValErr(0.169202, 0.000257777, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00228771, None, -8.0479e-06, None, 0.00211412, None, -2.64163e-05, None, 0.00211412, None, -2.64163e-05, None, 0.00158867, None, -1.1628e-05, None, 0.00158867, None, -1.1628e-05, None, 0.169205, None, 0.00479577, None, 0.169205, None, 0.00479577, None)

reports.append(Report(604050544, ("CSC", 2, 1, 1, 14), "MEm11_14"))
reports[-1].posNum = 214028
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00188431, 0.000515108, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.142836, 0.0281342, 0), \
                           ValErr(-0.00119048, 0.000742464, 0), \
                           ValErr(-0.00166754, 0.00373086, 0), \
                           ValErr(1.07453e-06, 1.04776e-05, 0), \
                           75675.1, 214028, 214028, -nan)
reports[-1].sigmaresid = ValErr(0.169905, 0.000259691, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00131536, None, -1.64619e-06, None, 0.00202821, None, -2.7501e-05, None, 0.00202821, None, -2.7501e-05, None, 0.00215564, None, -2.07367e-05, None, 0.00215564, None, -2.07367e-05, None, 0.169916, None, 0.00462607, None, 0.169916, None, 0.00462607, None)

reports.append(Report(604050560, ("CSC", 2, 1, 1, 16), "MEm11_16"))
reports[-1].posNum = 213359
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00106163, 0.000515711, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0689802, 0.0281657, 0), \
                           ValErr(-0.000859304, 0.000743644, 0), \
                           ValErr(0.00170676, 0.00373423, 0), \
                           ValErr(-7.95802e-06, 1.04858e-05, 0), \
                           75523.4, 213359, 213359, -nan)
reports[-1].sigmaresid = ValErr(0.169838, 0.000259994, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000561402, None, -5.40581e-06, None, 0.000840712, None, -1.22418e-05, None, 0.000840712, None, -1.22418e-05, None, 3.58233e-05, None, -1.77121e-05, None, 3.58233e-05, None, -1.77121e-05, None, 0.16984, None, 0.00439479, None, 0.16984, None, 0.00439479, None)

reports.append(Report(604050576, ("CSC", 2, 1, 1, 18), "MEm11_18"))
reports[-1].posNum = 215087
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00155978, 0.00051388, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0645153, 0.0279661, 0), \
                           ValErr(-0.000221898, 0.000738103, 0), \
                           ValErr(0.0017516, 0.00373249, 0), \
                           ValErr(-9.00099e-06, 1.16396e-05, 0), \
                           76245.6, 215087, 215087, -nan)
reports[-1].sigmaresid = ValErr(0.16975, 0.00025799, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00107323, None, 2.31446e-07, None, 0.00132664, None, -2.19824e-05, None, 0.00132664, None, -2.19824e-05, None, 0.000982089, None, 1.20904e-06, None, 0.000982089, None, 1.20904e-06, None, 0.169753, None, 0.0045181, None, 0.169753, None, 0.0045181, None)

reports.append(Report(604050592, ("CSC", 2, 1, 1, 20), "MEm11_20"))
reports[-1].posNum = 214492
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00183541, 0.000514815, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0760554, 0.0280473, 0), \
                           ValErr(-0.000868042, 0.000741459, 0), \
                           ValErr(-0.000696554, 0.00371482, 0), \
                           ValErr(6.14081e-06, 1.04633e-05, 0), \
                           75682.2, 214492, 214492, -nan)
reports[-1].sigmaresid = ValErr(0.17003, 0.0002596, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00224057, None, -9.13527e-06, None, 0.00195641, None, -2.5308e-05, None, 0.00195641, None, -2.5308e-05, None, 0.00135444, None, -1.06822e-05, None, 0.00135444, None, -1.06822e-05, None, 0.170033, None, 0.00439689, None, 0.170033, None, 0.00439689, None)

reports.append(Report(604050608, ("CSC", 2, 1, 1, 22), "MEm11_22"))
reports[-1].posNum = 213501
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0021611, 0.000514814, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.127801, 0.0280116, 0), \
                           ValErr(-0.000550038, 0.000742664, 0), \
                           ValErr(-0.00373135, 0.00371619, 0), \
                           ValErr(1.58516e-05, 1.04951e-05, 0), \
                           75984.9, 213501, 213501, -nan)
reports[-1].sigmaresid = ValErr(0.169511, 0.000259408, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00263143, None, -1.44144e-05, None, 0.0026373, None, -2.22053e-05, None, 0.0026373, None, -2.22053e-05, None, 0.00183393, None, -2.64073e-05, None, 0.00183393, None, -2.64073e-05, None, 0.16952, None, 0.00458232, None, 0.16952, None, 0.00458232, None)

reports.append(Report(604050624, ("CSC", 2, 1, 1, 24), "MEm11_24"))
reports[-1].posNum = 213720
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.003731, 0.000518213, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0945605, 0.0281509, 0), \
                           ValErr(-0.000956772, 0.000743057, 0), \
                           ValErr(0.00849562, 0.00376175, 0), \
                           ValErr(-2.5004e-05, 1.15897e-05, 0), \
                           74806.7, 213720, 213720, -nan)
reports[-1].sigmaresid = ValErr(0.17051, 0.000260578, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0030183, None, -1.73918e-05, None, 0.00278714, None, -2.27472e-05, None, 0.00278714, None, -2.27472e-05, None, 0.00179378, None, -1.55494e-05, None, 0.00179378, None, -1.55494e-05, None, 0.170518, None, 0.00538343, None, 0.170518, None, 0.00538343, None)

reports.append(Report(604050640, ("CSC", 2, 1, 1, 26), "MEm11_26"))
reports[-1].posNum = 215005
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00286343, 0.000513262, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.137237, 0.0279204, 0), \
                           ValErr(-0.000773295, 0.0007397, 0), \
                           ValErr(0.00381198, 0.00374875, 0), \
                           ValErr(-1.55638e-05, 1.16561e-05, 0), \
                           76772.6, 215005, 215005, -nan)
reports[-1].sigmaresid = ValErr(0.169312, 0.000257621, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0023359, None, -5.13759e-06, None, 0.00240694, None, -3.18945e-05, None, 0.00240694, None, -3.18945e-05, None, 0.00131378, None, -9.4685e-06, None, 0.00131378, None, -9.4685e-06, None, 0.169322, None, 0.0044851, None, 0.169322, None, 0.0044851, None)

reports.append(Report(604050656, ("CSC", 2, 1, 1, 28), "MEm11_28"))
reports[-1].posNum = 215181
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00277595, 0.000516728, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0871936, 0.0281339, 0), \
                           ValErr(-0.000640817, 0.000742158, 0), \
                           ValErr(0.00220844, 0.00375494, 0), \
                           ValErr(-1.57351e-05, 1.15813e-05, 0), \
                           75210.8, 215181, 215181, -nan)
reports[-1].sigmaresid = ValErr(0.170595, 0.000259683, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00249057, None, -1.15049e-05, None, 0.00245157, None, -1.84266e-05, None, 0.00245157, None, -1.84266e-05, None, 0.0023097, None, -1.34117e-05, None, 0.0023097, None, -1.34117e-05, None, 0.1706, None, 0.00426456, None, 0.1706, None, 0.00426456, None)

reports.append(Report(604050672, ("CSC", 2, 1, 1, 30), "MEm11_30"))
reports[-1].posNum = 214224
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000859557, 0.000515022, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0917153, 0.0307988, 0), \
                           ValErr(-0.00181919, 0.000808573, 0), \
                           ValErr(-0.00523152, 0.00370598, 0), \
                           ValErr(2.34744e-05, 1.05549e-05, 0), \
                           76142.9, 214224, 214224, -nan)
reports[-1].sigmaresid = ValErr(0.169589, 0.000258359, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00171082, None, -7.13172e-06, None, 0.00152671, None, -2.29091e-05, None, 0.00152671, None, -2.29091e-05, None, 0.00121329, None, -6.94265e-06, None, 0.00121329, None, -6.94265e-06, None, 0.169597, None, 0.00446254, None, 0.169597, None, 0.00446254, None)

reports.append(Report(604050688, ("CSC", 2, 1, 1, 32), "MEm11_32"))
reports[-1].posNum = 214361
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00172306, 0.000517457, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.134535, 0.0282347, 0), \
                           ValErr(-0.00074014, 0.000744547, 0), \
                           ValErr(-0.00192221, 0.00373614, 0), \
                           ValErr(1.37444e-05, 1.05204e-05, 0), \
                           74703.1, 214361, 214361, -nan)
reports[-1].sigmaresid = ValErr(0.170771, 0.000260811, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00201225, None, -1.52149e-05, None, 0.0020223, None, -3.89432e-05, None, 0.0020223, None, -3.89432e-05, None, 0.00216417, None, -3.2094e-05, None, 0.00216417, None, -3.2094e-05, None, 0.170781, None, 0.00440846, None, 0.170781, None, 0.00440846, None)

reports.append(Report(604050704, ("CSC", 2, 1, 1, 34), "MEm11_34"))
reports[-1].posNum = 214726
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000968537, 0.000512971, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.14751, 0.0278456, 0), \
                           ValErr(-0.00206098, 0.000736969, 0), \
                           ValErr(-0.0055292, 0.00369347, 0), \
                           ValErr(4.80156e-06, 1.04443e-05, 0), \
                           76827.5, 214726, 214726, -nan)
reports[-1].sigmaresid = ValErr(0.16919, 0.000258178, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00126996, None, 5.52824e-06, None, 0.00149977, None, -1.24765e-05, None, 0.00149977, None, -1.24765e-05, None, 0.00182995, None, -1.00239e-05, None, 0.00182995, None, -1.00239e-05, None, 0.169203, None, 0.00467209, None, 0.169203, None, 0.00467209, None)

reports.append(Report(604050720, ("CSC", 2, 1, 1, 36), "MEm11_36"))
reports[-1].posNum = 214908
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00308455, 0.000515631, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0924134, 0.0280998, 0), \
                           ValErr(-0.000998969, 0.000741501, 0), \
                           ValErr(0.00499639, 0.00375253, 0), \
                           ValErr(-1.73437e-05, 1.15816e-05, 0), \
                           75610, 214908, 214908, -nan)
reports[-1].sigmaresid = ValErr(0.170203, 0.000259213, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00257576, None, -9.1122e-06, None, 0.00250668, None, -2.66839e-05, None, 0.00250668, None, -2.66839e-05, None, 0.00119249, None, -1.32514e-05, None, 0.00119249, None, -1.32514e-05, None, 0.170209, None, 0.00445184, None, 0.170209, None, 0.00445184, None)

reports.append(Report(604050952, ("CSC", 2, 1, 2, 1), "MEm12_01"))
reports[-1].posNum = 104147
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00149472, 0.00251949, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.066628, 0.0736145, 0), \
                           ValErr(0.000722024, 0.00157958, 0), \
                           ValErr(0.00130879, 0.00538064, 0), \
                           ValErr(3.72109e-05, 3.95567e-05, 0), \
                           -87389.5, 104147, 104147, -nan)
reports[-1].sigmaresid = ValErr(0.559987, 0.00122699, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000798243, None, 4.17606e-06, None, -0.00134979, None, -2.31979e-06, None, -0.00134979, None, -2.31979e-06, None, 0.000704061, None, -2.17156e-08, None, 0.000704061, None, -2.17156e-08, None, 0.559994, None, 0.0042302, None, 0.559994, None, 0.0042302, None)

reports.append(Report(604050968, ("CSC", 2, 1, 2, 3), "MEm12_03"))
reports[-1].posNum = 98051
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0011164, 0.00255665, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0349973, 0.0741984, 0), \
                           ValErr(-9.86904e-05, 0.00159742, 0), \
                           ValErr(-0.0113026, 0.00546776, 0), \
                           ValErr(-6.6708e-06, 4.00175e-05, 0), \
                           -78507.7, 98051, 98051, -nan)
reports[-1].sigmaresid = ValErr(0.538883, 0.0012169, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00326115, None, -6.8399e-06, None, 0.00430915, None, -2.13613e-05, None, 0.00430915, None, -2.13613e-05, None, 0.00640556, None, -2.42874e-05, None, 0.00640556, None, -2.42874e-05, None, 0.538897, None, 0.00439432, None, 0.538897, None, 0.00439432, None)

reports.append(Report(604050984, ("CSC", 2, 1, 2, 5), "MEm12_05"))
reports[-1].posNum = 103359
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00457085, 0.00247326, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000160444, 0.0743227, 0), \
                           ValErr(-0.0029939, 0.00162303, 0), \
                           ValErr(0.00639723, 0.00538128, 0), \
                           ValErr(-5.30094e-05, 3.90963e-05, 0), \
                           -85445.4, 103359, 103359, -nan)
reports[-1].sigmaresid = ValErr(0.553079, 0.00121646, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00272881, None, -1.6816e-05, None, 0.00196026, None, -8.74556e-06, None, 0.00196026, None, -8.74556e-06, None, 0.00506869, None, -3.11076e-05, None, 0.00506869, None, -3.11076e-05, None, 0.553096, None, 0.00434435, None, 0.553096, None, 0.00434435, None)

reports.append(Report(604051000, ("CSC", 2, 1, 2, 7), "MEm12_07"))
reports[-1].posNum = 98544
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00365362, 0.00261321, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0345657, 0.0752644, 0), \
                           ValErr(-0.0028687, 0.00162238, 0), \
                           ValErr(-0.0108231, 0.00552184, 0), \
                           ValErr(0.000114245, 4.09331e-05, 0), \
                           -81226.8, 98544, 98544, -nan)
reports[-1].sigmaresid = ValErr(0.551744, 0.00124281, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00328721, None, 1.14177e-06, None, 0.00143935, None, 5.06823e-06, None, 0.00143935, None, 5.06823e-06, None, 0.000267769, None, -1.13709e-06, None, 0.000267769, None, -1.13709e-06, None, 0.55178, None, 0.00426782, None, 0.55178, None, 0.00426782, None)

reports.append(Report(604051016, ("CSC", 2, 1, 2, 9), "MEm12_09"))
reports[-1].posNum = 100715
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000318153, 0.00252192, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.141267, 0.0765934, 0), \
                           ValErr(-0.00349042, 0.00165656, 0), \
                           ValErr(-0.00444164, 0.00550688, 0), \
                           ValErr(-4.48548e-05, 3.9793e-05, 0), \
                           -83745.9, 100715, 100715, -nan)
reports[-1].sigmaresid = ValErr(0.555756, 0.00123829, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000889478, None, 5.32343e-06, None, 0.000331355, None, 1.52406e-05, None, 0.000331355, None, 1.52406e-05, None, 0.000671526, None, 1.43652e-06, None, 0.000671526, None, 1.43652e-06, None, 0.555783, None, 0.00428575, None, 0.555783, None, 0.00428575, None)

reports.append(Report(604051032, ("CSC", 2, 1, 2, 11), "MEm12_11"))
reports[-1].posNum = 99845
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000353159, 0.00253768, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0539054, 0.0767923, 0), \
                           ValErr(-0.00111437, 0.00167111, 0), \
                           ValErr(0.00165592, 0.00552095, 0), \
                           ValErr(-5.93793e-06, 4.00451e-05, 0), \
                           -82447.3, 99845, 99845, -nan)
reports[-1].sigmaresid = ValErr(0.552566, 0.00123654, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00237761, None, 8.91971e-06, None, -0.000952752, None, 1.87488e-06, None, -0.000952752, None, 1.87488e-06, None, 0.000525403, None, -1.39427e-06, None, 0.000525403, None, -1.39427e-06, None, 0.552567, None, 0.00447316, None, 0.552567, None, 0.00447316, None)

reports.append(Report(604051048, ("CSC", 2, 1, 2, 13), "MEm12_13"))
reports[-1].posNum = 96968
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000445822, 0.00263415, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.212402, 0.0757825, 0), \
                           ValErr(-0.00197036, 0.00163617, 0), \
                           ValErr(-3.65302e-05, 0.00556848, 0), \
                           ValErr(-3.97132e-06, 4.1208e-05, 0), \
                           -79040.6, 96968, 96968, -nan)
reports[-1].sigmaresid = ValErr(0.54672, 0.00124147, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00204126, None, 4.32027e-06, None, 0.000552342, None, -9.14901e-06, None, 0.000552342, None, -9.14901e-06, None, -0.000566016, None, -2.01114e-05, None, -0.000566016, None, -2.01114e-05, None, 0.546744, None, 0.00413003, None, 0.546744, None, 0.00413003, None)

reports.append(Report(604051064, ("CSC", 2, 1, 2, 15), "MEm12_15"))
reports[-1].posNum = 103701
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00416776, 0.00248486, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0157698, 0.0732893, 0), \
                           ValErr(-0.00079334, 0.00157552, 0), \
                           ValErr(0.00739734, 0.00534685, 0), \
                           ValErr(8.30396e-05, 3.89528e-05, 0), \
                           -85896.1, 103701, 103701, -nan)
reports[-1].sigmaresid = ValErr(0.553976, 0.00121642, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00452138, None, 1.16857e-05, None, -0.00518308, None, 1.44495e-06, None, -0.00518308, None, 1.44495e-06, None, -0.00723935, None, 2.36929e-05, None, -0.00723935, None, 2.36929e-05, None, 0.554, None, 0.00420551, None, 0.554, None, 0.00420551, None)

reports.append(Report(604051080, ("CSC", 2, 1, 2, 17), "MEm12_17"))
reports[-1].posNum = 98108
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000950851, 0.00256593, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0619612, 0.0754846, 0), \
                           ValErr(0.00229129, 0.00164726, 0), \
                           ValErr(0.00128239, 0.00551764, 0), \
                           ValErr(4.71265e-05, 4.04992e-05, 0), \
                           -79024.2, 98108, 98108, -nan)
reports[-1].sigmaresid = ValErr(0.541476, 0.0012224, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00182834, None, 1.52176e-05, None, -0.000481557, None, 2.08563e-05, None, -0.000481557, None, 2.08563e-05, None, -0.00536591, None, 1.40297e-05, None, -0.00536591, None, 1.40297e-05, None, 0.541487, None, 0.00413061, None, 0.541487, None, 0.00413061, None)

reports.append(Report(604051096, ("CSC", 2, 1, 2, 19), "MEm12_19"))
reports[-1].posNum = 104578
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00278267, 0.00250664, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0345217, 0.0734984, 0), \
                           ValErr(0.00218207, 0.0015774, 0), \
                           ValErr(0.0091193, 0.00536214, 0), \
                           ValErr(-5.09342e-05, 3.94609e-05, 0), \
                           -87755.3, 104578, 104578, -nan)
reports[-1].sigmaresid = ValErr(0.560009, 0.0012245, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00127377, None, 2.88326e-06, None, -0.000647834, None, -1.42764e-06, None, -0.000647834, None, -1.42764e-06, None, -0.000407759, None, -2.08969e-09, None, -0.000407759, None, -2.08969e-09, None, 0.560025, None, 0.00433762, None, 0.560025, None, 0.00433762, None)

reports.append(Report(604051112, ("CSC", 2, 1, 2, 21), "MEm12_21"))
reports[-1].posNum = 95832
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00363615, 0.0025763, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0350896, 0.0773861, 0), \
                           ValErr(-0.00177917, 0.00167787, 0), \
                           ValErr(0.00764154, 0.00560761, 0), \
                           ValErr(8.3944e-07, 4.07219e-05, 0), \
                           -76619.2, 95832, 95832, -nan)
reports[-1].sigmaresid = ValErr(0.538255, 0.00122947, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000351054, None, -4.45883e-06, None, 0.0014869, None, -1.08091e-06, None, 0.0014869, None, -1.08091e-06, None, 0.00118085, None, -1.49162e-05, None, 0.00118085, None, -1.49162e-05, None, 0.538265, None, 0.00422687, None, 0.538265, None, 0.00422687, None)

reports.append(Report(604051128, ("CSC", 2, 1, 2, 23), "MEm12_23"))
reports[-1].posNum = 104136
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00176044, 0.00247613, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0568368, 0.0741596, 0), \
                           ValErr(0.00193822, 0.00161319, 0), \
                           ValErr(-0.00214854, 0.00537522, 0), \
                           ValErr(6.38621e-05, 3.89577e-05, 0), \
                           -86376.7, 104136, 104136, -nan)
reports[-1].sigmaresid = ValErr(0.554616, 0.00121528, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00368093, None, -1.61586e-05, None, 0.00331318, None, -1.4162e-05, None, 0.00331318, None, -1.4162e-05, None, 0.004437, None, -7.0845e-06, None, 0.004437, None, -7.0845e-06, None, 0.554629, None, 0.00417621, None, 0.554629, None, 0.00417621, None)

reports.append(Report(604051144, ("CSC", 2, 1, 2, 25), "MEm12_25"))
reports[-1].posNum = 99581
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00086739, 0.00256809, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.19661, 0.0752311, 0), \
                           ValErr(-0.000543065, 0.00162211, 0), \
                           ValErr(-0.00809991, 0.00547242, 0), \
                           ValErr(9.30245e-06, 4.03938e-05, 0), \
                           -81595, 99581, 99581, -nan)
reports[-1].sigmaresid = ValErr(0.549055, 0.0012303, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00232411, None, -1.26663e-05, None, 0.00169182, None, -1.95368e-05, None, 0.00169182, None, -1.95368e-05, None, 0.0035213, None, -1.33638e-05, None, 0.0035213, None, -1.33638e-05, None, 0.549081, None, 0.00414032, None, 0.549081, None, 0.00414032, None)

reports.append(Report(604051160, ("CSC", 2, 1, 2, 27), "MEm12_27"))
reports[-1].posNum = 100756
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00652831, 0.0025413, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.151991, 0.0745021, 0), \
                           ValErr(-0.000861014, 0.00160586, 0), \
                           ValErr(-0.0103216, 0.00543187, 0), \
                           ValErr(1.62465e-05, 3.9757e-05, 0), \
                           -83208.5, 100756, 100756, -nan)
reports[-1].sigmaresid = ValErr(0.552612, 0.00123103, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00203133, None, 1.35692e-05, None, -0.00314759, None, 1.91651e-05, None, -0.00314759, None, 1.91651e-05, None, -0.00446076, None, 2.2552e-05, None, -0.00446076, None, 2.2552e-05, None, 0.552635, None, 0.00423323, None, 0.552635, None, 0.00423323, None)

reports.append(Report(604051176, ("CSC", 2, 1, 2, 29), "MEm12_29"))
reports[-1].posNum = 100757
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00117892, 0.00254271, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0782052, 0.0755371, 0), \
                           ValErr(0.00264204, 0.0016437, 0), \
                           ValErr(-0.00142258, 0.00548789, 0), \
                           ValErr(-1.29292e-05, 4.00962e-05, 0), \
                           -83798.5, 100757, 100757, -nan)
reports[-1].sigmaresid = ValErr(0.555853, 0.00123824, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000643071, None, -2.10563e-06, None, 0.00137234, None, -3.00007e-05, None, 0.00137234, None, -3.00007e-05, None, 0.00301033, None, -1.53551e-05, None, 0.00301033, None, -1.53551e-05, None, 0.555866, None, 0.00428249, None, 0.555866, None, 0.00428249, None)

reports.append(Report(604051192, ("CSC", 2, 1, 2, 31), "MEm12_31"))
reports[-1].posNum = 99345
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000152732, 0.00260354, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.104141, 0.0746275, 0), \
                           ValErr(-0.000675708, 0.00161303, 0), \
                           ValErr(-0.00811006, 0.00548779, 0), \
                           ValErr(-4.51814e-05, 4.08889e-05, 0), \
                           -81685.1, 99345, 99345, -nan)
reports[-1].sigmaresid = ValErr(0.550623, 0.00123528, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.002193, None, -4.89872e-06, None, 0.00183107, None, -1.50149e-05, None, 0.00183107, None, -1.50149e-05, None, 0.00306765, None, -5.07333e-06, None, 0.00306765, None, -5.07333e-06, None, 0.550643, None, 0.00416545, None, 0.550643, None, 0.00416545, None)

reports.append(Report(604051208, ("CSC", 2, 1, 2, 33), "MEm12_33"))
reports[-1].posNum = 103810
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00180652, 0.00248643, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0211755, 0.0733336, 0), \
                           ValErr(-0.00217491, 0.00157108, 0), \
                           ValErr(0.00497977, 0.00534156, 0), \
                           ValErr(-6.38027e-06, 3.89879e-05, 0), \
                           -86193.8, 103810, 103810, -nan)
reports[-1].sigmaresid = ValErr(0.555084, 0.00121822, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000565152, None, -5.03088e-06, None, 0.000238578, None, -2.63982e-06, None, 0.000238578, None, -2.63982e-06, None, -0.00251086, None, 6.47043e-06, None, -0.00251086, None, 6.47043e-06, None, 0.555092, None, 0.00427466, None, 0.555092, None, 0.00427466, None)

reports.append(Report(604051224, ("CSC", 2, 1, 2, 35), "MEm12_35"))
reports[-1].posNum = 95827
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0023942, 0.00262288, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0270781, 0.0682115, 0), \
                           ValErr(0.000376358, 0.00155556, 0), \
                           ValErr(0.00172344, 0.00559259, 0), \
                           ValErr(9.60511e-06, 3.79901e-05, 0), \
                           -76499.1, 95827, 95827, -nan)
reports[-1].sigmaresid = ValErr(0.537603, 0.00122633, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00278133, None, -5.05e-06, None, -0.0027057, None, -1.07802e-05, None, -0.0027057, None, -1.07802e-05, None, -0.00234009, None, 8.91042e-06, None, -0.00234009, None, 8.91042e-06, None, 0.537604, None, 0.00438663, None, 0.537604, None, 0.00438663, None)

reports.append(Report(604050960, ("CSC", 2, 1, 2, 2), "MEm12_02"))
reports[-1].posNum = 97171
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000454275, 0.00248537, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0379317, 0.0713782, 0), \
                           ValErr(-0.000630137, 0.00152486, 0), \
                           ValErr(-0.00622086, 0.00516877, 0), \
                           ValErr(6.36429e-05, 3.87423e-05, 0), \
                           -76803.2, 97171, 97171, -nan)
reports[-1].sigmaresid = ValErr(0.533367, 0.00120988, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00417896, None, -2.19664e-05, None, 0.00339725, None, -2.05398e-05, None, 0.00339725, None, -2.05398e-05, None, 0.00272055, None, -2.22838e-05, None, 0.00272055, None, -2.22838e-05, None, 0.533377, None, 0.00419109, None, 0.533377, None, 0.00419109, None)

reports.append(Report(604050976, ("CSC", 2, 1, 2, 4), "MEm12_04"))
reports[-1].posNum = 92348
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00173552, 0.0025454, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.058939, 0.0725774, 0), \
                           ValErr(-0.00265424, 0.0015199, 0), \
                           ValErr(0.00831655, 0.00520709, 0), \
                           ValErr(9.49886e-05, 3.95117e-05, 0), \
                           -71871.5, 92348, 92348, -nan)
reports[-1].sigmaresid = ValErr(0.526939, 0.00122612, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00137089, None, -7.40715e-05, None, 0.00103439, None, -6.49072e-05, None, 0.00103439, None, -6.49072e-05, None, -0.000784968, None, -8.26586e-06, None, -0.000784968, None, -8.26586e-06, None, 0.526977, None, 0.00531749, None, 0.526977, None, 0.00531749, None)

reports.append(Report(604050992, ("CSC", 2, 1, 2, 6), "MEm12_06"))
reports[-1].posNum = 102452
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00394988, 0.002422, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.160509, 0.0686204, 0), \
                           ValErr(0.000987472, 0.00145845, 0), \
                           ValErr(0.0123128, 0.00499966, 0), \
                           ValErr(-1.52373e-05, 3.78047e-05, 0), \
                           -81865.4, 102452, 102452, -nan)
reports[-1].sigmaresid = ValErr(0.53801, 0.00118854, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-3.54717e-05, None, 7.39373e-06, None, -4.81704e-06, None, 7.78344e-06, None, -4.81704e-06, None, 7.78344e-06, None, -0.00104683, None, 7.16024e-06, None, -0.00104683, None, 7.16024e-06, None, 0.538041, None, 0.00403121, None, 0.538041, None, 0.00403121, None)

reports.append(Report(604051008, ("CSC", 2, 1, 2, 8), "MEm12_08"))
reports[-1].posNum = 93774
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0032071, 0.00253075, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0964178, 0.0701941, 0), \
                           ValErr(-0.00610251, 0.00148126, 0), \
                           ValErr(0.00644324, 0.0051157, 0), \
                           ValErr(-2.11307e-05, 3.71157e-05, 0), \
                           -71211.9, 93774, 93774, -nan)
reports[-1].sigmaresid = ValErr(0.517089, 0.00119263, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00205627, None, -4.01294e-06, None, 0.00087312, None, -3.45278e-06, None, 0.00087312, None, -3.45278e-06, None, 0.00377607, None, -2.89591e-05, None, 0.00377607, None, -2.89591e-05, None, 0.517141, None, 0.00424787, None, 0.517141, None, 0.00424787, None)

reports.append(Report(604051024, ("CSC", 2, 1, 2, 10), "MEm12_10"))
reports[-1].posNum = 104830
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00560461, 0.00238938, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0030751, 0.068184, 0), \
                           ValErr(-0.00288341, 0.00145023, 0), \
                           ValErr(-0.0157057, 0.00494537, 0), \
                           ValErr(3.58575e-05, 3.73293e-05, 0), \
                           -84430.7, 104830, 104830, -nan)
reports[-1].sigmaresid = ValErr(0.541434, 0.00118246, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000778424, None, -8.57018e-06, None, -0.000301585, None, 3.8707e-06, None, -0.000301585, None, 3.8707e-06, None, 0.00415771, None, -1.12902e-05, None, 0.00415771, None, -1.12902e-05, None, 0.541471, None, 0.00396545, None, 0.541471, None, 0.00396545, None)

reports.append(Report(604051040, ("CSC", 2, 1, 2, 12), "MEm12_12"))
reports[-1].posNum = 95109
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00122846, 0.00248478, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0498589, 0.068774, 0), \
                           ValErr(-0.00136541, 0.00146074, 0), \
                           ValErr(0.00102554, 0.00505587, 0), \
                           ValErr(-6.80571e-06, 3.83606e-05, 0), \
                           -72255.2, 95109, 95109, -nan)
reports[-1].sigmaresid = ValErr(0.51725, 0.00118597, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00170883, None, -3.85588e-07, None, 0.00080676, None, 1.08886e-05, None, 0.00080676, None, 1.08886e-05, None, 0.00208806, None, -1.11292e-05, None, 0.00208806, None, -1.11292e-05, None, 0.517254, None, 0.00431012, None, 0.517254, None, 0.00431012, None)

reports.append(Report(604051056, ("CSC", 2, 1, 2, 14), "MEm12_14"))
reports[-1].posNum = 102177
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000311158, 0.00240454, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0858199, 0.0679788, 0), \
                           ValErr(0.00144984, 0.00145296, 0), \
                           ValErr(-0.00110863, 0.0049571, 0), \
                           ValErr(-6.53252e-05, 3.73928e-05, 0), \
                           -80425.5, 102177, 102177, -nan)
reports[-1].sigmaresid = ValErr(0.531624, 0.00117601, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0017985, None, 5.1827e-06, None, -0.00093196, None, 2.43572e-05, None, -0.00093196, None, 2.43572e-05, None, 0.00224502, None, -6.31151e-06, None, 0.00224502, None, -6.31151e-06, None, 0.531639, None, 0.00411768, None, 0.531639, None, 0.00411768, None)

reports.append(Report(604051072, ("CSC", 2, 1, 2, 16), "MEm12_16"))
reports[-1].posNum = 97047
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000756357, 0.00248834, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.06831, 0.0719072, 0), \
                           ValErr(0.00120784, 0.00150195, 0), \
                           ValErr(-0.00595883, 0.00521732, 0), \
                           ValErr(7.76422e-05, 3.83886e-05, 0), \
                           -76330, 97047, 97047, -nan)
reports[-1].sigmaresid = ValErr(0.531307, 0.00120598, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00410071, None, -1.99869e-05, None, 0.00236427, None, -9.88485e-06, None, 0.00236427, None, -9.88485e-06, None, 0.00150344, None, -8.71068e-06, None, 0.00150344, None, -8.71068e-06, None, 0.531324, None, 0.00419716, None, 0.531324, None, 0.00419716, None)

reports.append(Report(604051088, ("CSC", 2, 1, 2, 18), "MEm12_18"))
reports[-1].posNum = 98335
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000632155, 0.00245642, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00855644, 0.0696464, 0), \
                           ValErr(-0.00242151, 0.00146715, 0), \
                           ValErr(-0.000881532, 0.00504122, 0), \
                           ValErr(1.5077e-05, 3.81451e-05, 0), \
                           -77457, 98335, 98335, -nan)
reports[-1].sigmaresid = ValErr(0.531924, 0.00119945, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00017866, None, 1.4305e-05, None, -0.000106075, None, 7.73152e-06, None, -0.000106075, None, 7.73152e-06, None, -0.00106179, None, -1.18678e-05, None, -0.00106179, None, -1.18678e-05, None, 0.531932, None, 0.00410087, None, 0.531932, None, 0.00410087, None)

reports.append(Report(604051104, ("CSC", 2, 1, 2, 20), "MEm12_20"))
reports[-1].posNum = 101394
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00156893, 0.0024434, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0369467, 0.0692483, 0), \
                           ValErr(-0.000792789, 0.00148067, 0), \
                           ValErr(0.00154277, 0.00504437, 0), \
                           ValErr(3.53605e-05, 3.80778e-05, 0), \
                           -80755.4, 101394, 101394, -nan)
reports[-1].sigmaresid = ValErr(0.536608, 0.00119162, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(8.84523e-05, None, 2.04159e-05, None, -0.00148803, None, 3.45254e-05, None, -0.00148803, None, 3.45254e-05, None, -0.000496519, None, 1.78148e-05, None, -0.000496519, None, 1.78148e-05, None, 0.536613, None, 0.00410869, None, 0.536613, None, 0.00410869, None)

reports.append(Report(604051120, ("CSC", 2, 1, 2, 22), "MEm12_22"))
reports[-1].posNum = 96952
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000862472, 0.00249117, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0359569, 0.0701244, 0), \
                           ValErr(-0.000151226, 0.00149486, 0), \
                           ValErr(-0.00101077, 0.00509941, 0), \
                           ValErr(6.42911e-05, 3.87593e-05, 0), \
                           -76151.5, 96952, 96952, -nan)
reports[-1].sigmaresid = ValErr(0.53074, 0.00120528, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00154152, None, -2.41974e-05, None, 0.00222659, None, -1.05546e-05, None, 0.00222659, None, -1.05546e-05, None, 0.0008933, None, -2.64568e-05, None, 0.0008933, None, -2.64568e-05, None, 0.530749, None, 0.00404234, None, 0.530749, None, 0.00404234, None)

reports.append(Report(604051136, ("CSC", 2, 1, 2, 24), "MEm12_24"))
reports[-1].posNum = 101434
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0012357, 0.00240989, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0302379, 0.0674983, 0), \
                           ValErr(-0.00170289, 0.00144615, 0), \
                           ValErr(0.000125868, 0.00493502, 0), \
                           ValErr(4.50339e-05, 3.76306e-05, 0), \
                           -79123.3, 101434, 101434, -nan)
reports[-1].sigmaresid = ValErr(0.527877, 0.001172, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00303171, None, -8.63326e-06, None, 0.00186847, None, -5.03667e-06, None, 0.00186847, None, -5.03667e-06, None, 0.00225185, None, -1.78933e-05, None, 0.00225185, None, -1.78933e-05, None, 0.527885, None, 0.00399878, None, 0.527885, None, 0.00399878, None)

reports.append(Report(604051152, ("CSC", 2, 1, 2, 26), "MEm12_26"))
reports[-1].posNum = 93420
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00462841, 0.00250843, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.199862, 0.0702178, 0), \
                           ValErr(-0.000340457, 0.00149148, 0), \
                           ValErr(0.00803764, 0.00514089, 0), \
                           ValErr(-2.18425e-05, 3.8675e-05, 0), \
                           -70053.8, 93420, 93420, -nan)
reports[-1].sigmaresid = ValErr(0.51219, 0.00118494, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00345424, None, -2.53059e-05, None, 0.00183954, None, -8.52854e-06, None, 0.00183954, None, -8.52854e-06, None, 0.00278869, None, -1.82164e-05, None, 0.00278869, None, -1.82164e-05, None, 0.512221, None, 0.00398739, None, 0.512221, None, 0.00398739, None)

reports.append(Report(604051168, ("CSC", 2, 1, 2, 28), "MEm12_28"))
reports[-1].posNum = 104453
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00254208, 0.0024167, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0303414, 0.0684418, 0), \
                           ValErr(0.00119092, 0.00146153, 0), \
                           ValErr(-0.00380543, 0.00499284, 0), \
                           ValErr(-3.37369e-06, 3.76305e-05, 0), \
                           -84272.9, 104453, 104453, -nan)
reports[-1].sigmaresid = ValErr(0.542192, 0.00118625, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00256225, None, -8.00602e-06, None, 0.0036576, None, -8.7086e-06, None, 0.0036576, None, -8.7086e-06, None, 0.00476819, None, -4.82146e-06, None, 0.00476819, None, -4.82146e-06, None, 0.542196, None, 0.00393418, None, 0.542196, None, 0.00393418, None)

reports.append(Report(604051184, ("CSC", 2, 1, 2, 30), "MEm12_30"))
reports[-1].posNum = 93776
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00655731, 0.00248677, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.00326432, 0.0699887, 0), \
                           ValErr(-0.00233368, 0.00145959, 0), \
                           ValErr(-0.00119113, 0.00513008, 0), \
                           ValErr(-2.69593e-05, 3.8158e-05, 0), \
                           -70537.6, 93776, 93776, -nan)
reports[-1].sigmaresid = ValErr(0.513377, 0.00118543, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00477273, None, -2.9896e-05, None, 0.00637925, None, -3.97584e-05, None, 0.00637925, None, -3.97584e-05, None, 0.00767224, None, -4.97845e-05, None, 0.00767224, None, -4.97845e-05, None, 0.513386, None, 0.00415723, None, 0.513386, None, 0.00415723, None)

reports.append(Report(604051200, ("CSC", 2, 1, 2, 32), "MEm12_32"))
reports[-1].posNum = 103260
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000348856, 0.00239859, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.141724, 0.0677213, 0), \
                           ValErr(0.000931856, 0.00145029, 0), \
                           ValErr(0.00782095, 0.0049445, 0), \
                           ValErr(9.92663e-06, 3.73846e-05, 0), \
                           -81768.6, 103260, 103260, -nan)
reports[-1].sigmaresid = ValErr(0.534156, 0.0011754, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00176914, None, 2.09034e-05, None, -0.00192592, None, 2.26844e-05, None, -0.00192592, None, 2.26844e-05, None, 0.00130005, None, 2.57746e-06, None, 0.00130005, None, 2.57746e-06, None, 0.534175, None, 0.00428111, None, 0.534175, None, 0.00428111, None)

reports.append(Report(604051216, ("CSC", 2, 1, 2, 34), "MEm12_34"))
reports[-1].posNum = 99555
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00413657, 0.00245244, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.128286, 0.0702581, 0), \
                           ValErr(-0.00111205, 0.00149017, 0), \
                           ValErr(0.000794212, 0.00508052, 0), \
                           ValErr(-7.50834e-05, 3.82545e-05, 0), \
                           -79211, 99555, 99555, -nan)
reports[-1].sigmaresid = ValErr(0.536179, 0.00120161, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00017498, None, -1.67931e-05, None, 0.0026856, None, -4.4428e-06, None, 0.0026856, None, -4.4428e-06, None, 0.00206331, None, -1.27749e-05, None, 0.00206331, None, -1.27749e-05, None, 0.536201, None, 0.00429898, None, 0.536201, None, 0.00429898, None)

reports.append(Report(604051232, ("CSC", 2, 1, 2, 36), "MEm12_36"))
reports[-1].posNum = 101328
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00545809, 0.0024319, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0264344, 0.0681154, 0), \
                           ValErr(0.00135956, 0.00144945, 0), \
                           ValErr(-0.00437003, 0.00495481, 0), \
                           ValErr(4.59378e-05, 3.79306e-05, 0), \
                           -80544.4, 101328, 101328, -nan)
reports[-1].sigmaresid = ValErr(0.53577, 0.00119014, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00199344, None, 2.89066e-05, None, -0.00340636, None, 4.77759e-05, None, -0.00340636, None, 4.77759e-05, None, -0.00359352, None, 3.76675e-05, None, -0.00359352, None, 3.76675e-05, None, 0.535778, None, 0.00416333, None, 0.535778, None, 0.00416333, None)

reports.append(Report(604051464, ("CSC", 2, 1, 3, 1), "MEm13_01"))
reports[-1].posNum = 40964
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00356434, 0.00785235, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.17571, 0.206631, 0), \
                           ValErr(-0.0019479, 0.00346704, 0), \
                           ValErr(0.0110429, 0.00749499, 0), \
                           ValErr(0.000168728, 0.000129024, 0), \
                           -74890.7, 40964, 40964, -nan)
reports[-1].sigmaresid = ValErr(1.50569, 0.00454812, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0118313, None, 5.9218e-05, None, -0.0111645, None, 0.000109299, None, -0.0111645, None, 0.000109299, None, -0.0151954, None, 3.72774e-05, None, -0.0151954, None, 3.72774e-05, None, 1.50767, None, 0.00639503, None, 1.50767, None, 0.00639503, None)

reports.append(Report(604051472, ("CSC", 2, 1, 3, 2), "MEm13_02"))
reports[-1].posNum = 40291
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00540842, 0.0109967, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.40894, 0.214368, 0), \
                           ValErr(-0.00408233, 0.00464346, 0), \
                           ValErr(0.0109352, 0.0107337, 0), \
                           ValErr(-0.000222991, 0.00012238, 0), \
                           -73551.7, 40291, 40291, -nan)
reports[-1].sigmaresid = ValErr(1.50167, 0.00483823, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0115612, None, -1.02557e-05, None, -0.00297352, None, 4.45112e-05, None, -0.00297352, None, 4.45112e-05, None, 0.000203569, None, 1.12858e-05, None, 0.000203569, None, 1.12858e-05, None, 1.50396, None, 0.00674634, None, 1.50396, None, 0.00674634, None)

reports.append(Report(604051480, ("CSC", 2, 1, 3, 3), "MEm13_03"))
reports[-1].posNum = 37875
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00191334, 0.0113351, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.5044, 0.232204, 0), \
                           ValErr(-0.000380704, 0.00536281, 0), \
                           ValErr(-0.00065237, 0.0109982, 0), \
                           ValErr(5.17555e-05, 0.000184932, 0), \
                           -69749.8, 37875, 37875, -nan)
reports[-1].sigmaresid = ValErr(1.52599, 0.00554446, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000965593, None, 1.92892e-05, None, -0.00276764, None, 4.71187e-05, None, -0.00276764, None, 4.71187e-05, None, 0.0111541, None, 5.2352e-07, None, 0.0111541, None, 5.2352e-07, None, 1.52838, None, 0.006876, None, 1.52838, None, 0.006876, None)

reports.append(Report(604051488, ("CSC", 2, 1, 3, 4), "MEm13_04"))
reports[-1].posNum = 38129
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0176214, 0.0111792, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.85241, 0.234993, 0), \
                           ValErr(-0.0207521, 0.00544573, 0), \
                           ValErr(-0.00324038, 0.0111241, 0), \
                           ValErr(0.000406651, 8.66997e-05, 0), \
                           -70122.7, 38129, 38129, -nan)
reports[-1].sigmaresid = ValErr(1.52219, 0.0055126, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0268114, None, 2.14374e-05, None, -0.016228, None, 8.02418e-05, None, -0.016228, None, 8.02418e-05, None, -0.0257517, None, 0.000112406, None, -0.0257517, None, 0.000112406, None, 1.52523, None, 0.00652821, None, 1.52523, None, 0.00652821, None)

reports.append(Report(604051496, ("CSC", 2, 1, 3, 5), "MEm13_05"))
reports[-1].posNum = 40008
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00417662, 0.010996, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.65107, 0.218649, 0), \
                           ValErr(0.0031409, 0.00489759, 0), \
                           ValErr(-0.00240606, 0.0107464, 0), \
                           ValErr(-1.52593e-05, 0.000171451, 0), \
                           -72872.4, 40008, 40008, -nan)
reports[-1].sigmaresid = ValErr(1.49557, 0.00527846, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000493884, None, 2.26871e-05, None, -0.00129504, None, 7.71021e-05, None, -0.00129504, None, 7.71021e-05, None, 0.00103359, None, 6.27713e-05, None, 0.00103359, None, 6.27713e-05, None, 1.49833, None, 0.00665314, None, 1.49833, None, 0.00665314, None)

reports.append(Report(604051504, ("CSC", 2, 1, 3, 6), "MEm13_06"))
reports[-1].posNum = 40108
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0290345, 0.0108783, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.85549, 0.212624, 0), \
                           ValErr(0.00564229, 0.00418699, 0), \
                           ValErr(-0.0117039, 0.0103744, 0), \
                           ValErr(0.000136655, 0.000111306, 0), \
                           -72617.3, 40108, 40108, -nan)
reports[-1].sigmaresid = ValErr(1.47935, 0.00521964, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.02001, None, 0.000120464, None, -0.0208193, None, 0.000128719, None, -0.0208193, None, 0.000128719, None, -0.0189668, None, 7.14644e-05, None, -0.0189668, None, 7.14644e-05, None, 1.48272, None, 0.00700682, None, 1.48272, None, 0.00700682, None)

reports.append(Report(604051512, ("CSC", 2, 1, 3, 7), "MEm13_07"))
reports[-1].posNum = 38270
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00285485, 0.01114, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.61072, 0.219943, 0), \
                           ValErr(0.00214013, 0.0050447, 0), \
                           ValErr(0.000252419, 0.0106156, 0), \
                           ValErr(9.10527e-05, 0.000177781, 0), \
                           -69632.7, 38270, 38270, -nan)
reports[-1].sigmaresid = ValErr(1.49268, 0.00539539, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00543603, None, 2.81425e-05, None, 0.00528352, None, 5.33093e-05, None, 0.00528352, None, 5.33093e-05, None, -0.00970152, None, 5.58713e-05, None, -0.00970152, None, 5.58713e-05, None, 1.49547, None, 0.00630466, None, 1.49547, None, 0.00630466, None)

reports.append(Report(604051520, ("CSC", 2, 1, 3, 8), "MEm13_08"))
reports[-1].posNum = 36591
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0196185, 0.011409, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.18425, 0.231396, 0), \
                           ValErr(0.000578698, 0.00532599, 0), \
                           ValErr(-0.0202109, 0.0112557, 0), \
                           ValErr(-0.000133648, 9.22866e-05, 0), \
                           -66854, 36591, 36591, -nan)
reports[-1].sigmaresid = ValErr(1.504, 0.00533958, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00718984, None, 8.1782e-05, None, -0.00615111, None, 0.00012619, None, -0.00615111, None, 0.00012619, None, 0.00831592, None, 6.79283e-05, None, 0.00831592, None, 6.79283e-05, None, 1.50801, None, 0.0065381, None, 1.50801, None, 0.0065381, None)

reports.append(Report(604051528, ("CSC", 2, 1, 3, 9), "MEm13_09"))
reports[-1].posNum = 38388
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000324977, 0.0112511, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.61573, 0.227394, 0), \
                           ValErr(-0.00423173, 0.00511668, 0), \
                           ValErr(-0.00162585, 0.0110476, 0), \
                           ValErr(0.000244378, 0.000178029, 0), \
                           -70342, 38388, 38388, -nan)
reports[-1].sigmaresid = ValErr(1.51204, 0.00546367, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0056824, None, -3.00542e-05, None, 0.000638513, None, -1.10946e-06, None, 0.000638513, None, -1.10946e-06, None, 0.00817337, None, -2.57934e-05, None, 0.00817337, None, -2.57934e-05, None, 1.51468, None, 0.0065459, None, 1.51468, None, 0.0065459, None)

reports.append(Report(604051536, ("CSC", 2, 1, 3, 10), "MEm13_10"))
reports[-1].posNum = 40452
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0109358, 0.0108, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.1198, 0.219459, 0), \
                           ValErr(-0.00244372, 0.00483227, 0), \
                           ValErr(0.0102791, 0.0105828, 0), \
                           ValErr(-0.000124233, 9.96528e-05, 0), \
                           -73431.2, 40452, 40452, -nan)
reports[-1].sigmaresid = ValErr(1.48636, 0.00500429, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00861035, None, 8.97343e-05, None, 0.00216464, None, 0.000114702, None, 0.00216464, None, 0.000114702, None, 0.00779477, None, 4.82327e-05, None, 0.00779477, None, 4.82327e-05, None, 1.49007, None, 0.00654038, None, 1.49007, None, 0.00654038, None)

reports.append(Report(604051544, ("CSC", 2, 1, 3, 11), "MEm13_11"))
reports[-1].posNum = 38639
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00235098, 0.0112445, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.23364, 0.228152, 0), \
                           ValErr(-0.00199625, 0.00514802, 0), \
                           ValErr(-0.00378677, 0.0111413, 0), \
                           ValErr(0.000375755, 0.000178182, 0), \
                           -70822.5, 38639, 38639, -nan)
reports[-1].sigmaresid = ValErr(1.51284, 0.00544194, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00996053, None, 4.94554e-05, None, 0.00449845, None, 5.47741e-05, None, 0.00449845, None, 5.47741e-05, None, 0.0208377, None, -2.50238e-05, None, 0.0208377, None, -2.50238e-05, None, 1.51483, None, 0.00706618, None, 1.51483, None, 0.00706618, None)

reports.append(Report(604051552, ("CSC", 2, 1, 3, 12), "MEm13_12"))
reports[-1].posNum = 36201
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00824172, 0.0117106, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.68255, 0.230536, 0), \
                           ValErr(-0.00508027, 0.00533534, 0), \
                           ValErr(-0.00100307, 0.0111665, 0), \
                           ValErr(0.000177163, 0.000189291, 0), \
                           -66726.1, 36201, 36201, -nan)
reports[-1].sigmaresid = ValErr(1.52848, 0.00568049, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00107173, None, 0.000103857, None, -0.00631553, None, 9.97457e-05, None, -0.00631553, None, 9.97457e-05, None, 0.00375186, None, 2.12023e-05, None, 0.00375186, None, 2.12023e-05, None, 1.53136, None, 0.00665235, None, 1.53136, None, 0.00665235, None)

reports.append(Report(604051560, ("CSC", 2, 1, 3, 13), "MEm13_13"))
reports[-1].posNum = 37077
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0100864, 0.0114618, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.78855, 0.224987, 0), \
                           ValErr(-0.00100228, 0.00508188, 0), \
                           ValErr(-0.0135918, 0.0108857, 0), \
                           ValErr(3.27025e-05, 0.000180646, 0), \
                           -67924.9, 37077, 37077, -nan)
reports[-1].sigmaresid = ValErr(1.51143, 0.00555039, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00156065, None, 3.83341e-05, None, -0.00230961, None, 0.000128259, None, -0.00230961, None, 0.000128259, None, 0.0147426, None, 1.05204e-06, None, 0.0147426, None, 1.05204e-06, None, 1.51459, None, 0.00671715, None, 1.51459, None, 0.00671715, None)

reports.append(Report(604051568, ("CSC", 2, 1, 3, 14), "MEm13_14"))
reports[-1].posNum = 40269
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00919389, 0.0109496, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.57763, 0.21983, 0), \
                           ValErr(-0.00357381, 0.00494901, 0), \
                           ValErr(0.00199403, 0.010834, 0), \
                           ValErr(-3.25795e-05, 0.000170601, 0), \
                           -73210.3, 40269, 40269, -nan)
reports[-1].sigmaresid = ValErr(1.49047, 0.00526349, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00658105, None, 3.50967e-05, None, -0.0116089, None, 7.75549e-05, None, -0.0116089, None, 7.75549e-05, None, -0.00235453, None, 7.49315e-05, None, -0.00235453, None, 7.49315e-05, None, 1.49302, None, 0.00670796, None, 1.49302, None, 0.00670796, None)

reports.append(Report(604051576, ("CSC", 2, 1, 3, 15), "MEm13_15"))
reports[-1].posNum = 40536
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00298343, 0.0108793, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.81738, 0.221433, 0), \
                           ValErr(-0.0047403, 0.00492813, 0), \
                           ValErr(-0.0127731, 0.0106414, 0), \
                           ValErr(0.000175498, 8.40865e-05, 0), \
                           -74010.6, 40536, 40536, -nan)
reports[-1].sigmaresid = ValErr(1.50209, 0.00526707, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00847353, None, 6.29611e-06, None, 0.00715226, None, 0.00010576, None, 0.00715226, None, 0.00010576, None, 0.0273835, None, -2.28407e-05, None, 0.0273835, None, -2.28407e-05, None, 1.50512, None, 0.00672522, None, 1.50512, None, 0.00672522, None)

reports.append(Report(604051584, ("CSC", 2, 1, 3, 16), "MEm13_16"))
reports[-1].posNum = 37043
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00383053, 0.011415, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.81, 0.239047, 0), \
                           ValErr(0.000455947, 0.00554837, 0), \
                           ValErr(-0.00226949, 0.0112873, 0), \
                           ValErr(6.57324e-06, 0.000186278, 0), \
                           -68131.5, 37043, 37043, -nan)
reports[-1].sigmaresid = ValErr(1.52244, 0.00559331, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00766321, None, 6.32098e-06, None, -0.00175778, None, 0.000111152, None, -0.00175778, None, 0.000111152, None, -0.010905, None, 9.89805e-05, None, -0.010905, None, 9.89805e-05, None, 1.52538, None, 0.00644105, None, 1.52538, None, 0.00644105, None)

reports.append(Report(604051592, ("CSC", 2, 1, 3, 17), "MEm13_17"))
reports[-1].posNum = 37751
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.019124, 0.0112837, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.64036, 0.229509, 0), \
                           ValErr(-0.00488682, 0.00532412, 0), \
                           ValErr(-0.0167683, 0.0110586, 0), \
                           ValErr(0.000280048, 0.000182905, 0), \
                           -69161.3, 37751, 37751, -nan)
reports[-1].sigmaresid = ValErr(1.5115, 0.00550088, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00460667, None, 2.72646e-05, None, -0.00534313, None, 8.3502e-05, None, -0.00534313, None, 8.3502e-05, None, -0.00914414, None, 4.66543e-05, None, -0.00914414, None, 4.66543e-05, None, 1.51427, None, 0.00706447, None, 1.51427, None, 0.00706447, None)

reports.append(Report(604051600, ("CSC", 2, 1, 3, 18), "MEm13_18"))
reports[-1].posNum = 38173
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00594238, 0.00573973, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.64151, 0.21867, 0), \
                           ValErr(-0.00482467, 0.00472417, 0), \
                           ValErr(0.00100499, 0.00546356, 0), \
                           ValErr(-3.87773e-07, 7.9738e-05, 0), \
                           -69671.4, 38173, 38173, -nan)
reports[-1].sigmaresid = ValErr(1.50111, 0.00523423, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00210913, None, 4.32586e-05, None, -0.0074414, None, 5.70453e-05, None, -0.0074414, None, 5.70453e-05, None, -0.00296041, None, 3.02275e-05, None, -0.00296041, None, 3.02275e-05, None, 1.50397, None, 0.00647097, None, 1.50397, None, 0.00647097, None)

reports.append(Report(604051608, ("CSC", 2, 1, 3, 19), "MEm13_19"))
reports[-1].posNum = 39988
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0135893, 0.0108195, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.25253, 0.212574, 0), \
                           ValErr(-0.0138346, 0.00240045, 0), \
                           ValErr(-0.00288464, 0.0102564, 0), \
                           ValErr(1.26942e-05, 7.48338e-05, 0), \
                           -72635.4, 39988, 39988, -nan)
reports[-1].sigmaresid = ValErr(1.48808, 0.00500398, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0055666, None, 4.42198e-05, None, -0.0117327, None, 0.00012796, None, -0.0117327, None, 0.00012796, None, 0.00187911, None, 3.4377e-05, None, 0.00187911, None, 3.4377e-05, None, 1.49029, None, 0.00655111, None, 1.49029, None, 0.00655111, None)

reports.append(Report(604051616, ("CSC", 2, 1, 3, 20), "MEm13_20"))
reports[-1].posNum = 40290
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0049742, 0.0109819, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.7573, 0.218784, 0), \
                           ValErr(-0.00428663, 0.00451926, 0), \
                           ValErr(0.00682688, 0.0107897, 0), \
                           ValErr(-4.27793e-05, 0.000115404, 0), \
                           -73506.8, 40290, 40290, -nan)
reports[-1].sigmaresid = ValErr(1.50007, 0.00498583, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00334281, None, 2.94156e-05, None, 0.000973817, None, 3.83254e-05, None, 0.000973817, None, 3.83254e-05, None, -0.0163999, None, 2.21387e-05, None, -0.0163999, None, 2.21387e-05, None, 1.50299, None, 0.00638153, None, 1.50299, None, 0.00638153, None)

reports.append(Report(604051624, ("CSC", 2, 1, 3, 21), "MEm13_21"))
reports[-1].posNum = 38142
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0109507, 0.0110929, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.45428, 0.223128, 0), \
                           ValErr(-0.00417633, 0.00525187, 0), \
                           ValErr(0.0268978, 0.0108117, 0), \
                           ValErr(4.18277e-05, 0.000114111, 0), \
                           -69729.8, 38142, 38142, -nan)
reports[-1].sigmaresid = ValErr(1.50565, 0.00497691, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000885217, None, 4.13447e-05, None, -0.01102, None, 9.56126e-05, None, -0.01102, None, 9.56126e-05, None, -0.0113117, None, 9.85772e-05, None, -0.0113117, None, 9.85772e-05, None, 1.50811, None, 0.00670891, None, 1.50811, None, 0.00670891, None)

reports.append(Report(604051632, ("CSC", 2, 1, 3, 22), "MEm13_22"))
reports[-1].posNum = 37907
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.016089, 0.011171, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.00538, 0.234794, 0), \
                           ValErr(-0.0175406, 0.00543248, 0), \
                           ValErr(0.00621183, 0.0111825, 0), \
                           ValErr(0.000114509, 8.74214e-05, 0), \
                           -69472.5, 37907, 37907, -nan)
reports[-1].sigmaresid = ValErr(1.51251, 0.00545474, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0108528, None, -1.23363e-05, None, 0.0103507, None, 5.71863e-05, None, 0.0103507, None, 5.71863e-05, None, 0.0263359, None, -4.04413e-05, None, 0.0263359, None, -4.04413e-05, None, 1.51577, None, 0.00643977, None, 1.51577, None, 0.00643977, None)

reports.append(Report(604051640, ("CSC", 2, 1, 3, 23), "MEm13_23"))
reports[-1].posNum = 39981
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0239879, 0.0108467, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.66557, 0.216959, 0), \
                           ValErr(-0.00144813, 0.0042853, 0), \
                           ValErr(0.00475198, 0.0105734, 0), \
                           ValErr(-2.47454e-05, 0.000112642, 0), \
                           -72425.8, 39981, 39981, -nan)
reports[-1].sigmaresid = ValErr(1.48078, 0.00520828, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0229721, None, 8.06458e-05, None, -0.0257554, None, 0.000131109, None, -0.0257554, None, 0.000131109, None, -0.0238445, None, 0.000111218, None, -0.0238445, None, 0.000111218, None, 1.48356, None, 0.0064889, None, 1.48356, None, 0.0064889, None)

reports.append(Report(604051648, ("CSC", 2, 1, 3, 24), "MEm13_24"))
reports[-1].posNum = 40059
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00624424, 0.0109014, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.36227, 0.213274, 0), \
                           ValErr(0.00352851, 0.00481378, 0), \
                           ValErr(0.00866344, 0.0104638, 0), \
                           ValErr(2.40319e-05, 0.000169521, 0), \
                           -72574.7, 40059, 40059, -nan)
reports[-1].sigmaresid = ValErr(1.48106, 0.00520759, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00681757, None, -1.11763e-05, None, -0.0124754, None, 8.51101e-05, None, -0.0124754, None, 8.51101e-05, None, -0.00182725, None, 2.56576e-05, None, -0.00182725, None, 2.56576e-05, None, 1.48335, None, 0.00652134, None, 1.48335, None, 0.00652134, None)

reports.append(Report(604051656, ("CSC", 2, 1, 3, 25), "MEm13_25"))
reports[-1].posNum = 38527
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0153991, 0.0112859, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.55074, 0.220248, 0), \
                           ValErr(-0.0063635, 0.00500403, 0), \
                           ValErr(0.0145243, 0.0106974, 0), \
                           ValErr(-6.99738e-05, 0.000178734, 0), \
                           -70649.3, 38527, 38527, -nan)
reports[-1].sigmaresid = ValErr(1.5141, 0.00545455, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00473527, None, 2.93463e-05, None, 0.00540545, None, 1.53649e-05, None, 0.00540545, None, 1.53649e-05, None, 0.0131963, None, 1.17269e-05, None, 0.0131963, None, 1.17269e-05, None, 1.51678, None, 0.00642835, None, 1.51678, None, 0.00642835, None)

reports.append(Report(604051664, ("CSC", 2, 1, 3, 26), "MEm13_26"))
reports[-1].posNum = 36427
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00822251, 0.0116872, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.6214, 0.232254, 0), \
                           ValErr(-0.0145129, 0.0054097, 0), \
                           ValErr(-0.000847038, 0.0113408, 0), \
                           ValErr(-2.44604e-05, 0.000187443, 0), \
                           -66878.8, 36427, 36427, -nan)
reports[-1].sigmaresid = ValErr(1.51745, 0.00562151, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00643641, None, 4.25894e-05, None, -0.00798503, None, 7.74646e-05, None, -0.00798503, None, 7.74646e-05, None, -0.00634857, None, 3.61208e-05, None, -0.00634857, None, 3.61208e-05, None, 1.52014, None, 0.00649466, None, 1.52014, None, 0.00649466, None)

reports.append(Report(604051672, ("CSC", 2, 1, 3, 27), "MEm13_27"))
reports[-1].posNum = 38067
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0138729, 0.011271, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.70804, 0.227461, 0), \
                           ValErr(-0.000503621, 0.00516438, 0), \
                           ValErr(-0.00863806, 0.0109614, 0), \
                           ValErr(-3.49127e-05, 0.000104292, 0), \
                           -69865.6, 38067, 38067, -nan)
reports[-1].sigmaresid = ValErr(1.51648, 0.00513032, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0156278, None, 5.76487e-05, None, -0.00838529, None, 0.000117804, None, -0.00838529, None, 0.000117804, None, -0.023925, None, 0.000111057, None, -0.023925, None, 0.000111057, None, 1.51929, None, 0.00659139, None, 1.51929, None, 0.00659139, None)

reports.append(Report(604051680, ("CSC", 2, 1, 3, 28), "MEm13_28"))
reports[-1].posNum = 39633
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0125433, 0.0109828, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.08943, 0.224572, 0), \
                           ValErr(-0.0137378, 0.00510879, 0), \
                           ValErr(0.0061093, 0.0107643, 0), \
                           ValErr(8.24979e-05, 0.000174275, 0), \
                           -72367, 39633, 39633, -nan)
reports[-1].sigmaresid = ValErr(1.50229, 0.00533594, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0047474, None, 2.67027e-05, None, 0.00664095, None, 5.13088e-05, None, 0.00664095, None, 5.13088e-05, None, 0.00339148, None, 4.8379e-05, None, 0.00339148, None, 4.8379e-05, None, 1.50592, None, 0.00668519, None, 1.50592, None, 0.00668519, None)

reports.append(Report(604051688, ("CSC", 2, 1, 3, 29), "MEm13_29"))
reports[-1].posNum = 38305
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0114221, 0.0113293, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.50657, 0.218058, 0), \
                           ValErr(-0.000391578, 0.00505425, 0), \
                           ValErr(-0.0150426, 0.011013, 0), \
                           ValErr(-0.000267275, 0.000101133, 0), \
                           -70205.9, 38305, 38305, -nan)
reports[-1].sigmaresid = ValErr(1.51267, 0.00525696, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00298219, None, 1.72316e-05, None, -3.13766e-05, None, 5.50552e-05, None, -3.13766e-05, None, 5.50552e-05, None, 0.00841154, None, -3.39686e-06, None, 0.00841154, None, -3.39686e-06, None, 1.51524, None, 0.00664476, None, 1.51524, None, 0.00664476, None)

reports.append(Report(604051696, ("CSC", 2, 1, 3, 30), "MEm13_30"))
reports[-1].posNum = 36866
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0142727, 0.0115046, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.68064, 0.226842, 0), \
                           ValErr(-0.000281306, 0.00522678, 0), \
                           ValErr(-0.0106775, 0.0110584, 0), \
                           ValErr(0.00027782, 9.33174e-05, 0), \
                           -67650, 36866, 36866, -nan)
reports[-1].sigmaresid = ValErr(1.51602, 0.00525636, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00681368, None, 2.45085e-05, None, -0.00504775, None, -4.20568e-06, None, -0.00504775, None, -4.20568e-06, None, -0.00497946, None, -0.000105758, None, -0.00497946, None, -0.000105758, None, 1.51896, None, 0.00667281, None, 1.51896, None, 0.00667281, None)

reports.append(Report(604051704, ("CSC", 2, 1, 3, 31), "MEm13_31"))
reports[-1].posNum = 37657
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0162657, 0.0113856, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.21798, 0.220113, 0), \
                           ValErr(-0.00833317, 0.00473482, 0), \
                           ValErr(0.00192769, 0.0108164, 0), \
                           ValErr(-0.000109098, 0.000145712, 0), \
                           -68878.3, 37657, 37657, -nan)
reports[-1].sigmaresid = ValErr(1.50706, 0.00440602, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00939521, None, 5.52662e-05, None, -0.0205312, None, 0.000116975, None, -0.0205312, None, 0.000116975, None, -0.0139176, None, 6.79571e-05, None, -0.0139176, None, 6.79571e-05, None, 1.50908, None, 0.00650325, None, 1.50908, None, 0.00650325, None)

reports.append(Report(604051712, ("CSC", 2, 1, 3, 32), "MEm13_32"))
reports[-1].posNum = 41365
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00895598, 0.0109447, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.41945, 0.220224, 0), \
                           ValErr(0.0106849, 0.00438073, 0), \
                           ValErr(-0.00925467, 0.010811, 0), \
                           ValErr(4.62359e-05, 0.000110817, 0), \
                           -75812.7, 41365, 41365, -nan)
reports[-1].sigmaresid = ValErr(1.51261, 0.00517746, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000506047, None, 3.16262e-05, None, -0.0012567, None, 4.91187e-05, None, -0.0012567, None, 4.91187e-05, None, -0.00433629, None, 5.8175e-05, None, -0.00433629, None, 5.8175e-05, None, 1.51491, None, 0.00693036, None, 1.51491, None, 0.00693036, None)

reports.append(Report(604051720, ("CSC", 2, 1, 3, 33), "MEm13_33"))
reports[-1].posNum = 41011
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00615079, 0.0108365, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(3.02859, 0.21849, 0), \
                           ValErr(-0.00606481, 0.00489705, 0), \
                           ValErr(0.00129396, 0.010618, 0), \
                           ValErr(0.000422913, 0.000170196, 0), \
                           -74802.6, 41011, 41011, -nan)
reports[-1].sigmaresid = ValErr(1.49933, 0.00523518, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0131696, None, -1.35408e-05, None, 0.00681978, None, 5.17259e-05, None, 0.00681978, None, 5.17259e-05, None, 0.00310273, None, 2.12869e-05, None, 0.00310273, None, 2.12869e-05, None, 1.50297, None, 0.00669033, None, 1.50297, None, 0.00669033, None)

reports.append(Report(604051728, ("CSC", 2, 1, 3, 34), "MEm13_34"))
reports[-1].posNum = 37470
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00141374, 0.0114816, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.39946, 0.239486, 0), \
                           ValErr(0.00193662, 0.00555744, 0), \
                           ValErr(0.000355472, 0.011364, 0), \
                           ValErr(-0.000322007, 0.000186462, 0), \
                           -69240.3, 37470, 37470, -nan)
reports[-1].sigmaresid = ValErr(1.53564, 0.00561025, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000858695, None, 4.3618e-05, None, 0.00113296, None, 9.40925e-05, None, 0.00113296, None, 9.40925e-05, None, 0.00638185, None, 2.81967e-05, None, 0.00638185, None, 2.81967e-05, None, 1.53785, None, 0.00663395, None, 1.53785, None, 0.00663395, None)

reports.append(Report(604051736, ("CSC", 2, 1, 3, 35), "MEm13_35"))
reports[-1].posNum = 37269
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0219601, 0.0113875, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.66175, 0.234089, 0), \
                           ValErr(-0.00882112, 0.00543968, 0), \
                           ValErr(-0.0191253, 0.0111712, 0), \
                           ValErr(0.000121482, 0.000186345, 0), \
                           -68503.1, 37269, 37269, -nan)
reports[-1].sigmaresid = ValErr(1.52064, 0.00556981, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00171898, None, 3.36032e-05, None, -0.00716283, None, 5.60891e-05, None, -0.00716283, None, 5.60891e-05, None, -0.0110126, None, 9.70646e-05, None, -0.0110126, None, 9.70646e-05, None, 1.52337, None, 0.00667282, None, 1.52337, None, 0.00667282, None)

reports.append(Report(604051744, ("CSC", 2, 1, 3, 36), "MEm13_36"))
reports[-1].posNum = 38936
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0308785, 0.0110991, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(2.52284, 0.21129, 0), \
                           ValErr(-0.0113972, 0.00487309, 0), \
                           ValErr(-0.033588, 0.0106073, 0), \
                           ValErr(-0.000153364, 8.74811e-05, 0), \
                           -70819.6, 38936, 38936, -nan)
reports[-1].sigmaresid = ValErr(1.49173, 0.00523448, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0046602, None, 1.59878e-05, None, -0.00623692, None, 9.12419e-05, None, -0.00623692, None, 9.12419e-05, None, -0.0139055, None, 9.79589e-05, None, -0.0139055, None, 9.79589e-05, None, 1.49462, None, 0.00712609, None, 1.49462, None, 0.00712609, None)

reports.append(Report(604049928, ("CSC", 2, 1, 4, 1), "MEm14_01"))
reports[-1].posNum = 214554
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00257566, 0.000574416, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0869217, 0.0331047, 0), \
                           ValErr(-0.00222018, 0.000875954, 0), \
                           ValErr(-0.00534632, 0.00435769, 0), \
                           ValErr(-3.42199e-06, 1.17869e-05, 0), \
                           51651.2, 214554, 214554, -nan)
reports[-1].sigmaresid = ValErr(0.190201, 0.000290354, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00264322, None, -4.67067e-06, None, 0.00298377, None, -3.33059e-06, None, 0.00298377, None, -3.33059e-06, None, 0.00255314, None, -4.11003e-06, None, 0.00255314, None, -4.11003e-06, None, 0.190206, None, 0.00424221, None, 0.190206, None, 0.00424221, None)

reports.append(Report(604049944, ("CSC", 2, 1, 4, 3), "MEm14_03"))
reports[-1].posNum = 217389
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00242848, 0.00056909, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.120498, 0.0326986, 0), \
                           ValErr(-0.00221287, 0.000865955, 0), \
                           ValErr(-0.00330843, 0.00433382, 0), \
                           ValErr(-4.5235e-06, 1.1604e-05, 0), \
                           53751.1, 217389, 217389, -nan)
reports[-1].sigmaresid = ValErr(0.188964, 0.00028658, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00252795, None, -5.70436e-06, None, 0.00265084, None, -1.13643e-05, None, 0.00265084, None, -1.13643e-05, None, 0.00288481, None, -1.11035e-05, None, 0.00288481, None, -1.11035e-05, None, 0.188972, None, 0.0043208, None, 0.188972, None, 0.0043208, None)

reports.append(Report(604049960, ("CSC", 2, 1, 4, 5), "MEm14_05"))
reports[-1].posNum = 214754
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00207912, 0.000577175, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0636451, 0.0332434, 0), \
                           ValErr(-3.08207e-05, 0.000885061, 0), \
                           ValErr(-0.00162473, 0.00440362, 0), \
                           ValErr(-2.75558e-05, 1.18669e-05, 0), \
                           50883.1, 214754, 214754, -nan)
reports[-1].sigmaresid = ValErr(0.190925, 0.000291324, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00176546, None, -1.86749e-07, None, 0.00197875, None, -2.25835e-05, None, 0.00197875, None, -2.25835e-05, None, 0.000851869, None, -6.0641e-06, None, 0.000851869, None, -6.0641e-06, None, 0.19093, None, 0.00453646, None, 0.19093, None, 0.00453646, None)

reports.append(Report(604049976, ("CSC", 2, 1, 4, 7), "MEm14_07"))
reports[-1].posNum = 215894
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00129002, 0.000572435, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0597524, 0.0330436, 0), \
                           ValErr(-4.93808e-05, 0.000871302, 0), \
                           ValErr(-0.00724779, 0.00436596, 0), \
                           ValErr(-4.14713e-07, 1.169e-05, 0), \
                           52355.2, 215894, 215894, -nan)
reports[-1].sigmaresid = ValErr(0.189865, 0.000288941, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00175777, None, 4.08982e-06, None, 0.00187035, None, 1.6209e-05, None, 0.00187035, None, 1.6209e-05, None, 0.00130327, None, 2.46517e-05, None, 0.00130327, None, 2.46517e-05, None, 0.189868, None, 0.00415557, None, 0.189868, None, 0.00415557, None)

reports.append(Report(604049992, ("CSC", 2, 1, 4, 9), "MEm14_09"))
reports[-1].posNum = 215114
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000681234, 0.000577742, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0806157, 0.0332406, 0), \
                           ValErr(-0.00124459, 0.000881552, 0), \
                           ValErr(-0.00632429, 0.0044011, 0), \
                           ValErr(-7.42931e-07, 1.1843e-05, 0), \
                           50544.5, 215114, 215114, -nan)
reports[-1].sigmaresid = ValErr(0.191301, 0.000291655, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000902574, None, -4.56685e-06, None, 0.00118727, None, -1.57289e-05, None, 0.00118727, None, -1.57289e-05, None, 0.000419407, None, 1.38344e-05, None, 0.000419407, None, 1.38344e-05, None, 0.191305, None, 0.00447135, None, 0.191305, None, 0.00447135, None)

reports.append(Report(604050008, ("CSC", 2, 1, 4, 11), "MEm14_11"))
reports[-1].posNum = 215396
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00128842, 0.00057711, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.139283, 0.0332205, 0), \
                           ValErr(-0.000394752, 0.000880774, 0), \
                           ValErr(0.00334747, 0.00437934, 0), \
                           ValErr(1.45227e-05, 1.18394e-05, 0), \
                           50592.3, 215396, 215396, -nan)
reports[-1].sigmaresid = ValErr(0.191318, 0.000291489, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00129928, None, 9.37475e-06, None, 0.00113787, None, 2.1893e-05, None, 0.00113787, None, 2.1893e-05, None, -0.000458334, None, 2.42901e-05, None, -0.000458334, None, 2.42901e-05, None, 0.191327, None, 0.00425986, None, 0.191327, None, 0.00425986, None)

reports.append(Report(604050024, ("CSC", 2, 1, 4, 13), "MEm14_13"))
reports[-1].posNum = 214874
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00149547, 0.00057583, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.136184, 0.0331677, 0), \
                           ValErr(-0.000980657, 0.000878343, 0), \
                           ValErr(-0.000342693, 0.00439398, 0), \
                           ValErr(2.09411e-05, 1.17584e-05, 0), \
                           51485.9, 214874, 214874, -nan)
reports[-1].sigmaresid = ValErr(0.190415, 0.000290466, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00168217, None, 3.54693e-06, None, 0.00171877, None, 3.63714e-06, None, 0.00171877, None, 3.63714e-06, None, 0.00126964, None, 6.9538e-06, None, 0.00126964, None, 6.9538e-06, None, 0.190424, None, 0.00417729, None, 0.190424, None, 0.00417729, None)

reports.append(Report(604050040, ("CSC", 2, 1, 4, 15), "MEm14_15"))
reports[-1].posNum = 215553
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00249758, 0.00057671, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.140701, 0.0331814, 0), \
                           ValErr(-0.000933362, 0.000878795, 0), \
                           ValErr(-0.00626494, 0.00437205, 0), \
                           ValErr(-1.425e-05, 1.18197e-05, 0), \
                           50652.4, 215553, 215553, -nan)
reports[-1].sigmaresid = ValErr(0.191297, 0.000291351, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00278883, None, 1.67087e-06, None, 0.00288558, None, 6.66598e-07, None, 0.00288558, None, 6.66598e-07, None, 0.00200016, None, 6.50713e-06, None, 0.00200016, None, 6.50713e-06, None, 0.191308, None, 0.00454323, None, 0.191308, None, 0.00454323, None)

reports.append(Report(604050056, ("CSC", 2, 1, 4, 17), "MEm14_17"))
reports[-1].posNum = 215095
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.002167, 0.000572911, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0799678, 0.0328818, 0), \
                           ValErr(-0.000590092, 0.000869083, 0), \
                           ValErr(-0.00359437, 0.0043722, 0), \
                           ValErr(-2.09187e-05, 1.16559e-05, 0), \
                           53190, 215095, 215095, -nan)
reports[-1].sigmaresid = ValErr(0.188959, 0.000288097, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00224095, None, 7.91887e-07, None, 0.00226287, None, 1.40151e-05, None, 0.00226287, None, 1.40151e-05, None, 0.00183008, None, 1.97828e-05, None, 0.00183008, None, 1.97828e-05, None, 0.188964, None, 0.00424529, None, 0.188964, None, 0.00424529, None)

reports.append(Report(604050072, ("CSC", 2, 1, 4, 19), "MEm14_19"))
reports[-1].posNum = 215612
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00275699, 0.000575016, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.133876, 0.0332446, 0), \
                           ValErr(-0.00108721, 0.000878875, 0), \
                           ValErr(0.000386196, 0.00439087, 0), \
                           ValErr(-2.84399e-05, 1.17973e-05, 0), \
                           50886.2, 215612, 215612, -nan)
reports[-1].sigmaresid = ValErr(0.191102, 0.000291014, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00244297, None, -1.04747e-06, None, 0.00249574, None, -1.05135e-05, None, 0.00249574, None, -1.05135e-05, None, 0.00130221, None, 1.56246e-05, None, 0.00130221, None, 1.56246e-05, None, 0.191112, None, 0.00422632, None, 0.191112, None, 0.00422632, None)

reports.append(Report(604050088, ("CSC", 2, 1, 4, 21), "MEm14_21"))
reports[-1].posNum = 215744
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00145903, 0.000572196, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0106302, 0.032987, 0), \
                           ValErr(-0.00210554, 0.000871951, 0), \
                           ValErr(-0.00932941, 0.0043577, 0), \
                           ValErr(-4.77455e-06, 1.16546e-05, 0), \
                           52757.1, 215744, 215744, -nan)
reports[-1].sigmaresid = ValErr(0.18948, 0.000288455, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00217409, None, 1.85677e-06, None, 0.00216742, None, 1.99415e-05, None, 0.00216742, None, 1.99415e-05, None, 0.000491713, None, 3.25757e-05, None, 0.000491713, None, 3.25757e-05, None, 0.189485, None, 0.00422093, None, 0.189485, None, 0.00422093, None)

reports.append(Report(604050104, ("CSC", 2, 1, 4, 23), "MEm14_23"))
reports[-1].posNum = 214580
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00213086, 0.000576123, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.136698, 0.0332357, 0), \
                           ValErr(-0.000526634, 0.000882248, 0), \
                           ValErr(-0.00150406, 0.00438035, 0), \
                           ValErr(-1.41763e-05, 1.1836e-05, 0), \
                           50730.2, 214580, 214580, -nan)
reports[-1].sigmaresid = ValErr(0.191024, 0.000291594, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00122199, None, 3.28895e-06, None, 0.00214804, None, 1.5793e-05, None, 0.00214804, None, 1.5793e-05, None, 0.00135517, None, 5.73613e-07, None, 0.00135517, None, 5.73613e-07, None, 0.191033, None, 0.00474056, None, 0.191033, None, 0.00474056, None)

reports.append(Report(604050120, ("CSC", 2, 1, 4, 25), "MEm14_25"))
reports[-1].posNum = 216232
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00247701, 0.000570041, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0489926, 0.0328779, 0), \
                           ValErr(-0.000355549, 0.000868405, 0), \
                           ValErr(-0.00519464, 0.00433156, 0), \
                           ValErr(-1.86482e-05, 1.16424e-05, 0), \
                           53158.4, 216232, 216232, -nan)
reports[-1].sigmaresid = ValErr(0.189233, 0.000287754, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00235543, None, -1.41638e-06, None, 0.00273861, None, -4.55724e-06, None, 0.00273861, None, -4.55724e-06, None, 0.00184879, None, 1.51268e-05, None, 0.00184879, None, 1.51268e-05, None, 0.189236, None, 0.00462513, None, 0.189236, None, 0.00462513, None)

reports.append(Report(604050136, ("CSC", 2, 1, 4, 27), "MEm14_27"))
reports[-1].posNum = 214285
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00130848, 0.000578322, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0996193, 0.0333432, 0), \
                           ValErr(-0.00336104, 0.000883733, 0), \
                           ValErr(-0.00663747, 0.00439558, 0), \
                           ValErr(2.44761e-06, 1.18682e-05, 0), \
                           50312.3, 214285, 214285, -nan)
reports[-1].sigmaresid = ValErr(0.191335, 0.000292269, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00144377, None, 5.79048e-06, None, 0.00188272, None, -1.99386e-05, None, 0.00188272, None, -1.99386e-05, None, 0.00120334, None, -4.08724e-06, None, 0.00120334, None, -4.08724e-06, None, 0.191344, None, 0.00547244, None, 0.191344, None, 0.00547244, None)

reports.append(Report(604050152, ("CSC", 2, 1, 4, 29), "MEm14_29"))
reports[-1].posNum = 214340
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00177268, 0.000575435, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.100315, 0.0331657, 0), \
                           ValErr(-0.00254361, 0.00087905, 0), \
                           ValErr(0.00384414, 0.00438062, 0), \
                           ValErr(-6.86011e-07, 1.17944e-05, 0), \
                           51432.5, 214340, 214340, -nan)
reports[-1].sigmaresid = ValErr(0.190349, 0.000290725, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00169166, None, 4.47048e-06, None, 0.00146485, None, 7.12212e-06, None, 0.00146485, None, 7.12212e-06, None, 0.000520956, None, 2.19948e-05, None, 0.000520956, None, 2.19948e-05, None, 0.190355, None, 0.00418764, None, 0.190355, None, 0.00418764, None)

reports.append(Report(604050168, ("CSC", 2, 1, 4, 31), "MEm14_31"))
reports[-1].posNum = 216127
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00229993, 0.000572675, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0517692, 0.0329164, 0), \
                           ValErr(-0.000939811, 0.000870857, 0), \
                           ValErr(-0.00629285, 0.00436076, 0), \
                           ValErr(-1.75141e-05, 1.16794e-05, 0), \
                           52651.7, 216127, 216127, -nan)
reports[-1].sigmaresid = ValErr(0.189654, 0.000288465, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00237737, None, 3.37312e-07, None, 0.00266214, None, 7.82149e-06, None, 0.00266214, None, 7.82149e-06, None, 0.00176368, None, 2.975e-05, None, 0.00176368, None, 2.975e-05, None, 0.189658, None, 0.0044606, None, 0.189658, None, 0.0044606, None)

reports.append(Report(604050184, ("CSC", 2, 1, 4, 33), "MEm14_33"))
reports[-1].posNum = 216206
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00292946, 0.000574599, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0872603, 0.0331373, 0), \
                           ValErr(0.000239618, 0.000875916, 0), \
                           ValErr(-0.000861725, 0.00436582, 0), \
                           ValErr(-1.91075e-05, 1.17648e-05, 0), \
                           51201.9, 216206, 216206, -nan)
reports[-1].sigmaresid = ValErr(0.190947, 0.000290379, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00260735, None, -9.92248e-06, None, 0.00284074, None, -7.98469e-06, None, 0.00284074, None, -7.98469e-06, None, 0.00219427, None, 6.5066e-06, None, 0.00219427, None, 6.5066e-06, None, 0.190952, None, 0.0042797, None, 0.190952, None, 0.0042797, None)

reports.append(Report(604050200, ("CSC", 2, 1, 4, 35), "MEm14_35"))
reports[-1].posNum = 217102
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00221252, 0.000568279, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0408963, 0.0326533, 0), \
                           ValErr(-0.000763807, 0.000865446, 0), \
                           ValErr(-0.000880693, 0.00434832, 0), \
                           ValErr(8.97218e-06, 1.15582e-05, 0), \
                           54439, 217102, 217102, -nan)
reports[-1].sigmaresid = ValErr(0.188305, 0.000285768, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00186539, None, -7.59353e-06, None, 0.00236837, None, -1.23761e-05, None, 0.00236837, None, -1.23761e-05, None, 0.00195399, None, 1.17636e-05, None, 0.00195399, None, 1.17636e-05, None, 0.188306, None, 0.00465053, None, 0.188306, None, 0.00465053, None)

reports.append(Report(604049936, ("CSC", 2, 1, 4, 2), "MEm14_02"))
reports[-1].posNum = 215436
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00201101, 0.000514754, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.024168, 0.0280293, 0), \
                           ValErr(-0.000667441, 0.000742498, 0), \
                           ValErr(0.00124666, 0.0037205, 0), \
                           ValErr(-3.94989e-06, 1.04683e-05, 0), \
                           75810.9, 215436, 215436, -nan)
reports[-1].sigmaresid = ValErr(0.170191, 0.000259276, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00158478, None, -1.1126e-05, None, 0.00186899, None, -2.47337e-06, None, 0.00186899, None, -2.47337e-06, None, 0.00195532, None, -5.13907e-06, None, 0.00195532, None, -5.13907e-06, None, 0.170192, None, 0.00461149, None, 0.170192, None, 0.00461149, None)

reports.append(Report(604049952, ("CSC", 2, 1, 4, 4), "MEm14_04"))
reports[-1].posNum = 214645
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00172393, 0.00051381, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.126635, 0.0279865, 0), \
                           ValErr(-0.00123392, 0.000740309, 0), \
                           ValErr(0.00109153, 0.00371074, 0), \
                           ValErr(2.64579e-06, 1.04589e-05, 0), \
                           76339.7, 214645, 214645, -nan)
reports[-1].sigmaresid = ValErr(0.169552, 0.000258779, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00111887, None, -5.42068e-06, None, 0.00165641, None, -2.03062e-05, None, 0.00165641, None, -2.03062e-05, None, 0.0017975, None, -1.02421e-05, None, 0.0017975, None, -1.02421e-05, None, 0.169561, None, 0.00433306, None, 0.169561, None, 0.00433306, None)

reports.append(Report(604049968, ("CSC", 2, 1, 4, 6), "MEm14_06"))
reports[-1].posNum = 214654
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00151437, 0.000518705, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.100394, 0.0282002, 0), \
                           ValErr(-0.00028789, 0.000746067, 0), \
                           ValErr(0.00205497, 0.00373192, 0), \
                           ValErr(-1.35627e-05, 1.05535e-05, 0), \
                           74406, 214654, 214654, -nan)
reports[-1].sigmaresid = ValErr(0.171089, 0.000261119, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00160502, None, 8.07403e-07, None, 0.00120992, None, -2.74554e-05, None, 0.00120992, None, -2.74554e-05, None, 0.000770547, None, 2.77314e-06, None, 0.000770547, None, 2.77314e-06, None, 0.171095, None, 0.00454133, None, 0.171095, None, 0.00454133, None)

reports.append(Report(604049984, ("CSC", 2, 1, 4, 8), "MEm14_08"))
reports[-1].posNum = 214186
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00243864, 0.00051377, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0669558, 0.0291405, 0), \
                           ValErr(0.000181057, 0.000765234, 0), \
                           ValErr(-0.00015983, 0.00374299, 0), \
                           ValErr(-1.31977e-05, 1.13241e-05, 0), \
                           76541.6, 214186, 214186, -nan)
reports[-1].sigmaresid = ValErr(0.169263, 0.000257965, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00204946, None, -6.83569e-06, None, 0.00232812, None, -2.01654e-05, None, 0.00232812, None, -2.01654e-05, None, 0.00189021, None, -1.49116e-05, None, 0.00189021, None, -1.49116e-05, None, 0.169267, None, 0.00466234, None, 0.169267, None, 0.00466234, None)

reports.append(Report(604050000, ("CSC", 2, 1, 4, 10), "MEm14_10"))
reports[-1].posNum = 214140
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00272208, 0.000518465, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.115235, 0.0281802, 0), \
                           ValErr(-0.000628049, 0.000744639, 0), \
                           ValErr(0.00266019, 0.00374867, 0), \
                           ValErr(-1.81104e-05, 1.05448e-05, 0), \
                           74855.5, 214140, 214140, -nan)
reports[-1].sigmaresid = ValErr(0.170588, 0.000260667, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00183206, None, -8.5882e-06, None, 0.00232665, None, -2.63835e-05, None, 0.00232665, None, -2.63835e-05, None, 0.00200006, None, -2.27814e-05, None, 0.00200006, None, -2.27814e-05, None, 0.170596, None, 0.00476792, None, 0.170596, None, 0.00476792, None)

reports.append(Report(604050016, ("CSC", 2, 1, 4, 12), "MEm14_12"))
reports[-1].posNum = 214260
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0023496, 0.000512877, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0521106, 0.030686, 0), \
                           ValErr(-0.00076814, 0.000804355, 0), \
                           ValErr(0.00102435, 0.00371193, 0), \
                           ValErr(-1.55004e-05, 1.06327e-05, 0), \
                           76645.4, 214260, 214260, -nan)
reports[-1].sigmaresid = ValErr(0.169202, 0.000257777, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00228771, None, -8.0479e-06, None, 0.00211412, None, -2.64163e-05, None, 0.00211412, None, -2.64163e-05, None, 0.00158867, None, -1.1628e-05, None, 0.00158867, None, -1.1628e-05, None, 0.169205, None, 0.00479577, None, 0.169205, None, 0.00479577, None)

reports.append(Report(604050032, ("CSC", 2, 1, 4, 14), "MEm14_14"))
reports[-1].posNum = 214028
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00188431, 0.000515108, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.142836, 0.0281342, 0), \
                           ValErr(-0.00119048, 0.000742464, 0), \
                           ValErr(-0.00166754, 0.00373086, 0), \
                           ValErr(1.07453e-06, 1.04776e-05, 0), \
                           75675.1, 214028, 214028, -nan)
reports[-1].sigmaresid = ValErr(0.169905, 0.000259691, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00131536, None, -1.64619e-06, None, 0.00202821, None, -2.7501e-05, None, 0.00202821, None, -2.7501e-05, None, 0.00215564, None, -2.07367e-05, None, 0.00215564, None, -2.07367e-05, None, 0.169916, None, 0.00462607, None, 0.169916, None, 0.00462607, None)

reports.append(Report(604050048, ("CSC", 2, 1, 4, 16), "MEm14_16"))
reports[-1].posNum = 213359
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00106163, 0.000515711, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0689802, 0.0281657, 0), \
                           ValErr(-0.000859304, 0.000743644, 0), \
                           ValErr(0.00170676, 0.00373423, 0), \
                           ValErr(-7.95802e-06, 1.04858e-05, 0), \
                           75523.4, 213359, 213359, -nan)
reports[-1].sigmaresid = ValErr(0.169838, 0.000259994, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000561402, None, -5.40581e-06, None, 0.000840712, None, -1.22418e-05, None, 0.000840712, None, -1.22418e-05, None, 3.58233e-05, None, -1.77121e-05, None, 3.58233e-05, None, -1.77121e-05, None, 0.16984, None, 0.00439479, None, 0.16984, None, 0.00439479, None)

reports.append(Report(604050064, ("CSC", 2, 1, 4, 18), "MEm14_18"))
reports[-1].posNum = 215087
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00155978, 0.00051388, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0645153, 0.0279661, 0), \
                           ValErr(-0.000221898, 0.000738103, 0), \
                           ValErr(0.0017516, 0.00373249, 0), \
                           ValErr(-9.00099e-06, 1.16396e-05, 0), \
                           76245.6, 215087, 215087, -nan)
reports[-1].sigmaresid = ValErr(0.16975, 0.00025799, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00107323, None, 2.31446e-07, None, 0.00132664, None, -2.19824e-05, None, 0.00132664, None, -2.19824e-05, None, 0.000982089, None, 1.20904e-06, None, 0.000982089, None, 1.20904e-06, None, 0.169753, None, 0.0045181, None, 0.169753, None, 0.0045181, None)

reports.append(Report(604050080, ("CSC", 2, 1, 4, 20), "MEm14_20"))
reports[-1].posNum = 214492
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00183541, 0.000514815, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0760554, 0.0280473, 0), \
                           ValErr(-0.000868042, 0.000741459, 0), \
                           ValErr(-0.000696554, 0.00371482, 0), \
                           ValErr(6.14081e-06, 1.04633e-05, 0), \
                           75682.2, 214492, 214492, -nan)
reports[-1].sigmaresid = ValErr(0.17003, 0.0002596, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00224057, None, -9.13527e-06, None, 0.00195641, None, -2.5308e-05, None, 0.00195641, None, -2.5308e-05, None, 0.00135444, None, -1.06822e-05, None, 0.00135444, None, -1.06822e-05, None, 0.170033, None, 0.00439689, None, 0.170033, None, 0.00439689, None)

reports.append(Report(604050096, ("CSC", 2, 1, 4, 22), "MEm14_22"))
reports[-1].posNum = 213501
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0021611, 0.000514814, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.127801, 0.0280116, 0), \
                           ValErr(-0.000550038, 0.000742664, 0), \
                           ValErr(-0.00373135, 0.00371619, 0), \
                           ValErr(1.58516e-05, 1.04951e-05, 0), \
                           75984.9, 213501, 213501, -nan)
reports[-1].sigmaresid = ValErr(0.169511, 0.000259408, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00263143, None, -1.44144e-05, None, 0.0026373, None, -2.22053e-05, None, 0.0026373, None, -2.22053e-05, None, 0.00183393, None, -2.64073e-05, None, 0.00183393, None, -2.64073e-05, None, 0.16952, None, 0.00458232, None, 0.16952, None, 0.00458232, None)

reports.append(Report(604050112, ("CSC", 2, 1, 4, 24), "MEm14_24"))
reports[-1].posNum = 213720
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.003731, 0.000518213, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0945605, 0.0281509, 0), \
                           ValErr(-0.000956772, 0.000743057, 0), \
                           ValErr(0.00849562, 0.00376175, 0), \
                           ValErr(-2.5004e-05, 1.15897e-05, 0), \
                           74806.7, 213720, 213720, -nan)
reports[-1].sigmaresid = ValErr(0.17051, 0.000260578, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0030183, None, -1.73918e-05, None, 0.00278714, None, -2.27472e-05, None, 0.00278714, None, -2.27472e-05, None, 0.00179378, None, -1.55494e-05, None, 0.00179378, None, -1.55494e-05, None, 0.170518, None, 0.00538343, None, 0.170518, None, 0.00538343, None)

reports.append(Report(604050128, ("CSC", 2, 1, 4, 26), "MEm14_26"))
reports[-1].posNum = 215005
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00286343, 0.000513262, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.137237, 0.0279204, 0), \
                           ValErr(-0.000773295, 0.0007397, 0), \
                           ValErr(0.00381198, 0.00374875, 0), \
                           ValErr(-1.55638e-05, 1.16561e-05, 0), \
                           76772.6, 215005, 215005, -nan)
reports[-1].sigmaresid = ValErr(0.169312, 0.000257621, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0023359, None, -5.13759e-06, None, 0.00240694, None, -3.18945e-05, None, 0.00240694, None, -3.18945e-05, None, 0.00131378, None, -9.4685e-06, None, 0.00131378, None, -9.4685e-06, None, 0.169322, None, 0.0044851, None, 0.169322, None, 0.0044851, None)

reports.append(Report(604050144, ("CSC", 2, 1, 4, 28), "MEm14_28"))
reports[-1].posNum = 215181
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00277595, 0.000516728, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0871936, 0.0281339, 0), \
                           ValErr(-0.000640817, 0.000742158, 0), \
                           ValErr(0.00220844, 0.00375494, 0), \
                           ValErr(-1.57351e-05, 1.15813e-05, 0), \
                           75210.8, 215181, 215181, -nan)
reports[-1].sigmaresid = ValErr(0.170595, 0.000259683, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00249057, None, -1.15049e-05, None, 0.00245157, None, -1.84266e-05, None, 0.00245157, None, -1.84266e-05, None, 0.0023097, None, -1.34117e-05, None, 0.0023097, None, -1.34117e-05, None, 0.1706, None, 0.00426456, None, 0.1706, None, 0.00426456, None)

reports.append(Report(604050160, ("CSC", 2, 1, 4, 30), "MEm14_30"))
reports[-1].posNum = 214224
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000859557, 0.000515022, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0917153, 0.0307988, 0), \
                           ValErr(-0.00181919, 0.000808573, 0), \
                           ValErr(-0.00523152, 0.00370598, 0), \
                           ValErr(2.34744e-05, 1.05549e-05, 0), \
                           76142.9, 214224, 214224, -nan)
reports[-1].sigmaresid = ValErr(0.169589, 0.000258359, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00171082, None, -7.13172e-06, None, 0.00152671, None, -2.29091e-05, None, 0.00152671, None, -2.29091e-05, None, 0.00121329, None, -6.94265e-06, None, 0.00121329, None, -6.94265e-06, None, 0.169597, None, 0.00446254, None, 0.169597, None, 0.00446254, None)

reports.append(Report(604050176, ("CSC", 2, 1, 4, 32), "MEm14_32"))
reports[-1].posNum = 214361
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00172306, 0.000517457, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.134535, 0.0282347, 0), \
                           ValErr(-0.00074014, 0.000744547, 0), \
                           ValErr(-0.00192221, 0.00373614, 0), \
                           ValErr(1.37444e-05, 1.05204e-05, 0), \
                           74703.1, 214361, 214361, -nan)
reports[-1].sigmaresid = ValErr(0.170771, 0.000260811, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00201225, None, -1.52149e-05, None, 0.0020223, None, -3.89432e-05, None, 0.0020223, None, -3.89432e-05, None, 0.00216417, None, -3.2094e-05, None, 0.00216417, None, -3.2094e-05, None, 0.170781, None, 0.00440846, None, 0.170781, None, 0.00440846, None)

reports.append(Report(604050192, ("CSC", 2, 1, 4, 34), "MEm14_34"))
reports[-1].posNum = 214726
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000968537, 0.000512971, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.14751, 0.0278456, 0), \
                           ValErr(-0.00206098, 0.000736969, 0), \
                           ValErr(-0.0055292, 0.00369347, 0), \
                           ValErr(4.80156e-06, 1.04443e-05, 0), \
                           76827.5, 214726, 214726, -nan)
reports[-1].sigmaresid = ValErr(0.16919, 0.000258178, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00126996, None, 5.52824e-06, None, 0.00149977, None, -1.24765e-05, None, 0.00149977, None, -1.24765e-05, None, 0.00182995, None, -1.00239e-05, None, 0.00182995, None, -1.00239e-05, None, 0.169203, None, 0.00467209, None, 0.169203, None, 0.00467209, None)

reports.append(Report(604050208, ("CSC", 2, 1, 4, 36), "MEm14_36"))
reports[-1].posNum = 214908
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00308455, 0.000515631, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0924134, 0.0280998, 0), \
                           ValErr(-0.000998969, 0.000741501, 0), \
                           ValErr(0.00499639, 0.00375253, 0), \
                           ValErr(-1.73437e-05, 1.15816e-05, 0), \
                           75610, 214908, 214908, -nan)
reports[-1].sigmaresid = ValErr(0.170203, 0.000259213, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00257576, None, -9.1122e-06, None, 0.00250668, None, -2.66839e-05, None, 0.00250668, None, -2.66839e-05, None, 0.00119249, None, -1.32514e-05, None, 0.00119249, None, -1.32514e-05, None, 0.170209, None, 0.00445184, None, 0.170209, None, 0.00445184, None)

reports.append(Report(604054024, ("CSC", 2, 2, 1, 1), "MEm21_01"))
reports[-1].posNum = 431960
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(3.8247e-05, 0.000953081, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0219577, 0.0250301, 0), \
                           ValErr(-0.000649717, 0.000493496, 0), \
                           ValErr(-0.00172674, 0.00114826, 0), \
                           ValErr(1.64991e-05, 1.40804e-05, 0), \
                           -236534, 431960, 431960, -nan)
reports[-1].sigmaresid = ValErr(0.418385, 0.000450131, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000115157, None, -3.78502e-06, None, 0.00116327, None, -1.95209e-05, None, 0.00116327, None, -1.95209e-05, None, 0.000407641, None, 2.82673e-06, None, 0.000407641, None, 2.82673e-06, None, 0.418387, None, 0.00583402, None, 0.418387, None, 0.00583402, None)

reports.append(Report(604054040, ("CSC", 2, 2, 1, 3), "MEm21_03"))
reports[-1].posNum = 431159
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000135277, 0.000956259, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.00788553, 0.0250151, 0), \
                           ValErr(-0.000305616, 0.000494576, 0), \
                           ValErr(-0.000319431, 0.00115154, 0), \
                           ValErr(5.00834e-06, 1.41131e-05, 0), \
                           -235972, 431159, 431159, -nan)
reports[-1].sigmaresid = ValErr(0.418265, 0.00045042, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000292243, None, -4.02479e-07, None, 9.16936e-05, None, -1.42062e-05, None, 9.16936e-05, None, -1.42062e-05, None, 0.000209853, None, 3.95801e-07, None, 0.000209853, None, 3.95801e-07, None, 0.418265, None, 0.00580929, None, 0.418265, None, 0.00580929, None)

reports.append(Report(604054056, ("CSC", 2, 2, 1, 5), "MEm21_05"))
reports[-1].posNum = 430039
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00227801, 0.000954196, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0473393, 0.0250178, 0), \
                           ValErr(-0.000381819, 0.000494331, 0), \
                           ValErr(0.00164444, 0.00115001, 0), \
                           ValErr(-2.30321e-05, 1.41048e-05, 0), \
                           -234383, 430039, 430039, -nan)
reports[-1].sigmaresid = ValErr(0.417316, 0.000449983, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00160678, None, -3.90214e-06, None, 0.00113879, None, -8.5068e-06, None, 0.00113879, None, -8.5068e-06, None, -0.000235231, None, 8.56804e-06, None, -0.000235231, None, 8.56804e-06, None, 0.41732, None, 0.00569961, None, 0.41732, None, 0.00569961, None)

reports.append(Report(604054072, ("CSC", 2, 2, 1, 7), "MEm21_07"))
reports[-1].posNum = 429771
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0020503, 0.000952226, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0166479, 0.0274736, 0), \
                           ValErr(-0.000252722, 0.000562054, 0), \
                           ValErr(0.000893962, 0.00114552, 0), \
                           ValErr(1.96626e-06, 1.42818e-05, 0), \
                           -232448, 429771, 429771, -nan)
reports[-1].sigmaresid = ValErr(0.415583, 0.000449168, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000751942, None, 2.649e-06, None, 0.00156097, None, -1.05752e-05, None, 0.00156097, None, -1.05752e-05, None, 0.000858034, None, 1.77679e-05, None, 0.000858034, None, 1.77679e-05, None, 0.415583, None, 0.00560608, None, 0.415583, None, 0.00560608, None)

reports.append(Report(604054088, ("CSC", 2, 2, 1, 9), "MEm21_09"))
reports[-1].posNum = 430829
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000205959, 0.000951821, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0115325, 0.0248457, 0), \
                           ValErr(0.000774702, 0.000491446, 0), \
                           ValErr(-0.000871831, 0.00114631, 0), \
                           ValErr(3.92064e-06, 1.40332e-05, 0), \
                           -232787, 430829, 430829, -nan)
reports[-1].sigmaresid = ValErr(0.415358, 0.000447461, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000870364, None, 2.78236e-06, None, 0.000734093, None, -1.58665e-05, None, 0.000734093, None, -1.58665e-05, None, 0.000504227, None, -7.19605e-06, None, 0.000504227, None, -7.19605e-06, None, 0.41536, None, 0.00567743, None, 0.41536, None, 0.00567743, None)

reports.append(Report(604054104, ("CSC", 2, 2, 1, 11), "MEm21_11"))
reports[-1].posNum = 430263
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.003683, 0.000954001, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.035366, 0.0249105, 0), \
                           ValErr(-0.000142881, 0.000498801, 0), \
                           ValErr(0.00212649, 0.00115202, 0), \
                           ValErr(-1.5402e-05, 1.6236e-05, 0), \
                           -232421, 430263, 430263, -nan)
reports[-1].sigmaresid = ValErr(0.4153, 0.00045152, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00154617, None, -9.70987e-06, None, 0.00233868, None, -3.17375e-05, None, 0.00233868, None, -3.17375e-05, None, 0.00166716, None, -2.07844e-05, None, 0.00166716, None, -2.07844e-05, None, 0.415303, None, 0.00558866, None, 0.415303, None, 0.00558866, None)

reports.append(Report(604054120, ("CSC", 2, 2, 1, 13), "MEm21_13"))
reports[-1].posNum = 431333
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000375767, 0.000948324, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0189534, 0.0248195, 0), \
                           ValErr(-7.91417e-05, 0.000489407, 0), \
                           ValErr(-0.00206675, 0.0011417, 0), \
                           ValErr(4.00367e-06, 1.39601e-05, 0), \
                           -232679, 431333, 431333, -nan)
reports[-1].sigmaresid = ValErr(0.414991, 0.000446805, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00167844, None, 4.29962e-06, None, 0.00158235, None, -1.58054e-05, None, 0.00158235, None, -1.58054e-05, None, -0.000197959, None, 1.59633e-06, None, -0.000197959, None, 1.59633e-06, None, 0.414993, None, 0.00562837, None, 0.414993, None, 0.00562837, None)

reports.append(Report(604054136, ("CSC", 2, 2, 1, 15), "MEm21_15"))
reports[-1].posNum = 431659
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000156272, 0.000946822, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.00703055, 0.0248508, 0), \
                           ValErr(0.00031218, 0.000490015, 0), \
                           ValErr(-0.00080671, 0.00114106, 0), \
                           ValErr(3.91682e-06, 1.39559e-05, 0), \
                           -233105, 431659, 431659, -nan)
reports[-1].sigmaresid = ValErr(0.415233, 0.000446896, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00142607, None, -1.44086e-06, None, 0.000649072, None, -1.24211e-05, None, 0.000649072, None, -1.24211e-05, None, -9.47416e-05, None, 1.36028e-06, None, -9.47416e-05, None, 1.36028e-06, None, 0.415233, None, 0.00559593, None, 0.415233, None, 0.00559593, None)

reports.append(Report(604054152, ("CSC", 2, 2, 1, 17), "MEm21_17"))
reports[-1].posNum = 431962
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000729927, 0.000951669, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0373015, 0.0249052, 0), \
                           ValErr(0.000282672, 0.000491269, 0), \
                           ValErr(-0.000290016, 0.00114758, 0), \
                           ValErr(-8.73042e-06, 1.40298e-05, 0), \
                           -234570, 431962, 431962, -nan)
reports[-1].sigmaresid = ValErr(0.416485, 0.000448087, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000708344, None, -8.0439e-07, None, 0.000815209, None, -1.40369e-05, None, 0.000815209, None, -1.40369e-05, None, -8.44229e-05, None, -7.46824e-06, None, -8.44229e-05, None, -7.46824e-06, None, 0.416487, None, 0.00576772, None, 0.416487, None, 0.00576772, None)

reports.append(Report(604054032, ("CSC", 2, 2, 1, 2), "MEm21_02"))
reports[-1].posNum = 430836
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00136447, 0.000907339, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0430432, 0.0229467, 0), \
                           ValErr(-0.000470713, 0.000451205, 0), \
                           ValErr(0.00136039, 0.00105983, 0), \
                           ValErr(1.30761e-05, 1.33213e-05, 0), \
                           -211325, 430836, 430836, -nan)
reports[-1].sigmaresid = ValErr(0.39517, 0.00042571, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00079196, None, -2.39967e-05, None, 0.000701897, None, -3.09356e-05, None, 0.000701897, None, -3.09356e-05, None, 4.35649e-06, None, -1.8582e-05, None, 4.35649e-06, None, -1.8582e-05, None, 0.395174, None, 0.00608437, None, 0.395174, None, 0.00608437, None)

reports.append(Report(604054048, ("CSC", 2, 2, 1, 4), "MEm21_04"))
reports[-1].posNum = 430463
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0023308, 0.000909526, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0182891, 0.0229955, 0), \
                           ValErr(0.000376877, 0.000452477, 0), \
                           ValErr(0.000993638, 0.00106229, 0), \
                           ValErr(-1.84488e-05, 1.33524e-05, 0), \
                           -211683, 430463, 430463, -nan)
reports[-1].sigmaresid = ValErr(0.395667, 0.000426429, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00125036, None, -2.31945e-05, None, 0.00157367, None, -3.58867e-05, None, 0.00157367, None, -3.58867e-05, None, 0.00176839, None, -2.19987e-05, None, 0.00176839, None, -2.19987e-05, None, 0.395669, None, 0.00616293, None, 0.395669, None, 0.00616293, None)

reports.append(Report(604054064, ("CSC", 2, 2, 1, 6), "MEm21_06"))
reports[-1].posNum = 430211
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00130301, 0.000912288, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.00967859, 0.0230498, 0), \
                           ValErr(-0.000715677, 0.000453594, 0), \
                           ValErr(0.000483673, 0.00106387, 0), \
                           ValErr(-1.39551e-05, 1.33842e-05, 0), \
                           -212789, 430211, 430211, -nan)
reports[-1].sigmaresid = ValErr(0.3968, 0.000427775, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000563838, None, -1.0014e-05, None, 0.000882727, None, -4.17403e-05, None, 0.000882727, None, -4.17403e-05, None, 0.00102036, None, -3.49202e-05, None, 0.00102036, None, -3.49202e-05, None, 0.396801, None, 0.00588474, None, 0.396801, None, 0.00588474, None)

reports.append(Report(604054080, ("CSC", 2, 2, 1, 8), "MEm21_08"))
reports[-1].posNum = 431070
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00119493, 0.000918186, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0497424, 0.0231002, 0), \
                           ValErr(-0.000117188, 0.000453989, 0), \
                           ValErr(0.000525327, 0.00107539, 0), \
                           ValErr(-7.5948e-06, 1.62773e-05, 0), \
                           -214516, 431070, 431070, -nan)
reports[-1].sigmaresid = ValErr(0.398, 0.000433043, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000362102, None, -9.52594e-06, None, 0.000811691, None, -1.48085e-05, None, 0.000811691, None, -1.48085e-05, None, 0.000797802, None, 1.82559e-06, None, 0.000797802, None, 1.82559e-06, None, 0.398002, None, 0.00622924, None, 0.398002, None, 0.00622924, None)

reports.append(Report(604054096, ("CSC", 2, 2, 1, 10), "MEm21_10"))
reports[-1].posNum = 430907
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00147446, 0.000914288, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.00987033, 0.023108, 0), \
                           ValErr(-0.000565654, 0.000453929, 0), \
                           ValErr(-0.000267071, 0.00106638, 0), \
                           ValErr(-1.70282e-06, 1.34159e-05, 0), \
                           -214692, 430907, 430907, -nan)
reports[-1].sigmaresid = ValErr(0.398238, 0.00042898, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00191519, None, -1.15151e-05, None, 0.00161366, None, -3.47794e-05, None, 0.00161366, None, -3.47794e-05, None, 0.00129543, None, -1.23258e-05, None, 0.00129543, None, -1.23258e-05, None, 0.398239, None, 0.006167, None, 0.398239, None, 0.006167, None)

reports.append(Report(604054112, ("CSC", 2, 2, 1, 12), "MEm21_12"))
reports[-1].posNum = 430464
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00122958, 0.000911216, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00642524, 0.0263013, 0), \
                           ValErr(-0.000247224, 0.000467435, 0), \
                           ValErr(-0.000687983, 0.0010624, 0), \
                           ValErr(-2.73827e-05, 1.35018e-05, 0), \
                           -213379, 430464, 430464, -nan)
reports[-1].sigmaresid = ValErr(0.397229, 0.000432874, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000623404, None, -3.02176e-07, None, 0.00136189, None, -1.75142e-05, None, 0.00136189, None, -1.75142e-05, None, 0.000805509, None, -1.19462e-06, None, 0.000805509, None, -1.19462e-06, None, 0.397232, None, 0.00606187, None, 0.397232, None, 0.00606187, None)

reports.append(Report(604054128, ("CSC", 2, 2, 1, 14), "MEm21_14"))
reports[-1].posNum = 430795
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000289873, 0.000912113, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0161422, 0.0230807, 0), \
                           ValErr(-0.000345614, 0.000453913, 0), \
                           ValErr(-0.000111606, 0.00106451, 0), \
                           ValErr(1.69183e-05, 1.33977e-05, 0), \
                           -213999, 430795, 430795, -nan)
reports[-1].sigmaresid = ValErr(0.397649, 0.0004284, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000790746, None, -6.40914e-06, None, 0.000519844, None, -1.55399e-05, None, 0.000519844, None, -1.55399e-05, None, 0.000179049, None, 1.69418e-06, None, 0.000179049, None, 1.69418e-06, None, 0.397651, None, 0.00611946, None, 0.397651, None, 0.00611946, None)

reports.append(Report(604054144, ("CSC", 2, 2, 1, 16), "MEm21_16"))
reports[-1].posNum = 430131
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00143623, 0.00091167, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0376983, 0.0230182, 0), \
                           ValErr(0.000611919, 0.000453276, 0), \
                           ValErr(-0.00103792, 0.00106055, 0), \
                           ValErr(-5.39781e-07, 1.33981e-05, 0), \
                           -212684, 430131, 430131, -nan)
reports[-1].sigmaresid = ValErr(0.39674, 0.00042775, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.001933, None, -1.03516e-05, None, 0.00204214, None, -3.29598e-05, None, 0.00204214, None, -3.29598e-05, None, 0.000881348, None, -2.69658e-05, None, 0.000881348, None, -2.69658e-05, None, 0.396743, None, 0.00613186, None, 0.396743, None, 0.00613186, None)

reports.append(Report(604054160, ("CSC", 2, 2, 1, 18), "MEm21_18"))
reports[-1].posNum = 431238
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00133297, 0.000907626, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0163506, 0.0229375, 0), \
                           ValErr(-0.00092874, 0.000451176, 0), \
                           ValErr(0.000339976, 0.00105968, 0), \
                           ValErr(-4.0141e-06, 1.33317e-05, 0), \
                           -211608, 431238, 431238, -nan)
reports[-1].sigmaresid = ValErr(0.395249, 0.000425596, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00098428, None, -1.02953e-05, None, 0.0010946, None, -4.03682e-05, None, 0.0010946, None, -4.03682e-05, None, 0.00017229, None, -1.94019e-05, None, 0.00017229, None, -1.94019e-05, None, 0.395251, None, 0.00606883, None, 0.395251, None, 0.00606883, None)

reports.append(Report(604054536, ("CSC", 2, 2, 2, 1), "MEm22_01"))
reports[-1].posNum = 118552
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00114959, 0.00486341, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0659132, 0.121329, 0), \
                           ValErr(-0.00250252, 0.00137226, 0), \
                           ValErr(0.00593655, 0.00640106, 0), \
                           ValErr(-4.88291e-05, 3.7751e-05, 0), \
                           -170790, 118552, 118552, -nan)
reports[-1].sigmaresid = ValErr(1.02193, 0.00209871, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00782394, None, 1.9965e-05, None, -0.00358242, None, 1.84583e-05, None, -0.00358242, None, 1.84583e-05, None, -0.00703628, None, 2.70191e-06, None, -0.00703628, None, 2.70191e-06, None, 1.02195, None, 0.00672356, None, 1.02195, None, 0.00672356, None)

reports.append(Report(604054552, ("CSC", 2, 2, 2, 3), "MEm22_03"))
reports[-1].posNum = 106468
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00984971, 0.00504404, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.00575417, 0.0816869, 0), \
                           ValErr(-0.000842229, 0.00123409, 0), \
                           ValErr(-0.00676598, 0.00659809, 0), \
                           ValErr(8.85496e-05, 3.80304e-05, 0), \
                           -149204, 106468, 106468, -nan)
reports[-1].sigmaresid = ValErr(0.982611, 0.00212673, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000133189, None, 1.02775e-05, None, -0.00281913, None, 1.42535e-05, None, -0.00281913, None, 1.42535e-05, None, -0.00378884, None, 2.79839e-05, None, -0.00378884, None, 2.79839e-05, None, 0.982637, None, 0.00735373, None, 0.982637, None, 0.00735373, None)

reports.append(Report(604054568, ("CSC", 2, 2, 2, 5), "MEm22_05"))
reports[-1].posNum = 118121
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00318261, 0.00472584, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.116974, 0.12193, 0), \
                           ValErr(-0.00317101, 0.0013667, 0), \
                           ValErr(-0.00465472, 0.00634603, 0), \
                           ValErr(5.2273e-06, 3.68194e-05, 0), \
                           -168896, 118121, 118121, -nan)
reports[-1].sigmaresid = ValErr(1.01098, 0.00208, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00520659, None, -1.49023e-05, None, 0.00551613, None, 8.99651e-06, None, 0.00551613, None, 8.99651e-06, None, 0.0111063, None, -2.98913e-06, None, 0.0111063, None, -2.98913e-06, None, 1.01101, None, 0.0066128, None, 1.01101, None, 0.0066128, None)

reports.append(Report(604054584, ("CSC", 2, 2, 2, 7), "MEm22_07"))
reports[-1].posNum = 106477
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0019678, 0.0051883, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0378339, 0.12599, 0), \
                           ValErr(-6.16227e-05, 0.0014064, 0), \
                           ValErr(-0.00521386, 0.00669699, 0), \
                           ValErr(-2.19777e-05, 3.94622e-05, 0), \
                           -150784, 106477, 106477, -nan)
reports[-1].sigmaresid = ValErr(0.997188, 0.00216091, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00257005, None, -2.26278e-05, None, 0.00351039, None, -3.08854e-05, None, 0.00351039, None, -3.08854e-05, None, 0.00609471, None, -3.65501e-05, None, 0.00609471, None, -3.65501e-05, None, 0.997194, None, 0.00675382, None, 0.997194, None, 0.00675382, None)

reports.append(Report(604054600, ("CSC", 2, 2, 2, 9), "MEm22_09"))
reports[-1].posNum = 112353
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00518267, 0.00494203, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.198118, 0.126567, 0), \
                           ValErr(-0.00221334, 0.00141205, 0), \
                           ValErr(0.00367001, 0.0066185, 0), \
                           ValErr(-3.87069e-05, 3.83428e-05, 0), \
                           -161364, 112353, 112353, -nan)
reports[-1].sigmaresid = ValErr(1.01743, 0.00214634, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00148083, None, -5.44569e-06, None, 0.0021234, None, -1.66227e-05, None, 0.0021234, None, -1.66227e-05, None, 0.00316424, None, -3.39747e-05, None, 0.00316424, None, -3.39747e-05, None, 1.01746, None, 0.00702317, None, 1.01746, None, 0.00702317, None)

reports.append(Report(604054616, ("CSC", 2, 2, 2, 11), "MEm22_11"))
reports[-1].posNum = 111341
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00113098, 0.00495184, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.243601, 0.127778, 0), \
                           ValErr(0.000167777, 0.00142015, 0), \
                           ValErr(-0.0125732, 0.00664568, 0), \
                           ValErr(1.51669e-05, 3.82339e-05, 0), \
                           -160415, 111341, 111341, -nan)
reports[-1].sigmaresid = ValErr(1.02206, 0.00216588, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0066562, None, -9.31652e-06, None, 0.00751371, None, 1.16789e-08, None, 0.00751371, None, 1.16789e-08, None, 0.00682834, None, -5.0455e-06, None, 0.00682834, None, -5.0455e-06, None, 1.02209, None, 0.00684034, None, 1.02209, None, 0.00684034, None)

reports.append(Report(604054632, ("CSC", 2, 2, 2, 13), "MEm22_13"))
reports[-1].posNum = 104461
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00140753, 0.00523016, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.00689701, 0.127627, 0), \
                           ValErr(0.0013491, 0.00141826, 0), \
                           ValErr(-0.00297264, 0.00678389, 0), \
                           ValErr(-4.02847e-05, 3.97173e-05, 0), \
                           -148453, 104461, 104461, -nan)
reports[-1].sigmaresid = ValErr(1.0022, 0.00219261, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00373498, None, 2.43236e-05, None, 0.00112563, None, 9.58407e-06, None, 0.00112563, None, 9.58407e-06, None, -9.57323e-05, None, 2.45421e-05, None, -9.57323e-05, None, 2.45421e-05, None, 1.00221, None, 0.0065029, None, 1.00221, None, 0.0065029, None)

reports.append(Report(604054648, ("CSC", 2, 2, 2, 15), "MEm22_15"))
reports[-1].posNum = 117764
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00544988, 0.00471042, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0020902, 0.0710849, 0), \
                           ValErr(0.000540253, 0.00110102, 0), \
                           ValErr(0.00610344, 0.00625242, 0), \
                           ValErr(1.41223e-05, 3.6484e-05, 0), \
                           -169609, 117764, 117764, -nan)
reports[-1].sigmaresid = ValErr(1.02153, 0.00199253, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.010399, None, 4.4636e-06, None, -0.00782914, None, 5.16741e-06, None, -0.00782914, None, 5.16741e-06, None, -0.00902802, None, 3.00383e-05, None, -0.00902802, None, 3.00383e-05, None, 1.02155, None, 0.00696908, None, 1.02155, None, 0.00696908, None)

reports.append(Report(604054664, ("CSC", 2, 2, 2, 17), "MEm22_17"))
reports[-1].posNum = 106057
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0108639, 0.00501978, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.210805, 0.127727, 0), \
                           ValErr(-0.0013594, 0.00142698, 0), \
                           ValErr(-0.00627615, 0.00670594, 0), \
                           ValErr(6.67916e-05, 3.84371e-05, 0), \
                           -148808, 106057, 106057, -nan)
reports[-1].sigmaresid = ValErr(0.984285, 0.00213716, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00367886, None, 1.68033e-05, None, -0.00503637, None, 3.08859e-05, None, -0.00503637, None, 3.08859e-05, None, -0.0027016, None, 3.17311e-06, None, -0.0027016, None, 3.17311e-06, None, 0.984314, None, 0.0067246, None, 0.984314, None, 0.0067246, None)

reports.append(Report(604054680, ("CSC", 2, 2, 2, 19), "MEm22_19"))
reports[-1].posNum = 118356
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0107253, 0.00487762, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.15613, 0.121177, 0), \
                           ValErr(-0.00157635, 0.0013677, 0), \
                           ValErr(-0.00886142, 0.00638852, 0), \
                           ValErr(7.45734e-05, 3.78151e-05, 0), \
                           -170626, 118356, 118356, -nan)
reports[-1].sigmaresid = ValErr(1.02295, 0.00210254, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000772475, None, 5.86539e-06, None, -0.00357947, None, 4.43641e-05, None, -0.00357947, None, 4.43641e-05, None, -0.00427393, None, 2.34964e-05, None, -0.00427393, None, 2.34964e-05, None, 1.02298, None, 0.00655896, None, 1.02298, None, 0.00655896, None)

reports.append(Report(604054696, ("CSC", 2, 2, 2, 21), "MEm22_21"))
reports[-1].posNum = 104358
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00432217, 0.00505963, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0921336, 0.128256, 0), \
                           ValErr(-0.00183479, 0.00141792, 0), \
                           ValErr(0.00698555, 0.00672744, 0), \
                           ValErr(-6.11019e-05, 3.86431e-05, 0), \
                           -146892, 104358, 104358, -nan)
reports[-1].sigmaresid = ValErr(0.988707, 0.00216416, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000771906, None, -6.28984e-07, None, -0.00147983, None, -5.14228e-06, None, -0.00147983, None, -5.14228e-06, None, -0.00331828, None, 9.94036e-06, None, -0.00331828, None, 9.94036e-06, None, 0.988731, None, 0.00680893, None, 0.988731, None, 0.00680893, None)

reports.append(Report(604054712, ("CSC", 2, 2, 2, 23), "MEm22_23"))
reports[-1].posNum = 118167
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00191309, 0.00480618, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.179464, 0.122858, 0), \
                           ValErr(0.000141844, 0.00138443, 0), \
                           ValErr(-0.00271316, 0.00642047, 0), \
                           ValErr(-7.82889e-07, 3.74186e-05, 0), \
                           -170118, 118167, 118167, -nan)
reports[-1].sigmaresid = ValErr(1.02092, 0.00210004, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00113736, None, 9.50575e-06, None, -0.000623137, None, 3.8569e-05, None, -0.000623137, None, 3.8569e-05, None, 0.000786237, None, 3.42235e-05, None, 0.000786237, None, 3.42235e-05, None, 1.02092, None, 0.00695312, None, 1.02092, None, 0.00695312, None)

reports.append(Report(604054728, ("CSC", 2, 2, 2, 25), "MEm22_25"))
reports[-1].posNum = 107338
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00193849, 0.00512777, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0284098, 0.125185, 0), \
                           ValErr(0.000131391, 0.00139221, 0), \
                           ValErr(0.00387952, 0.00664746, 0), \
                           ValErr(3.87556e-05, 3.91198e-05, 0), \
                           -151898, 107338, 107338, -nan)
reports[-1].sigmaresid = ValErr(0.996205, 0.00215009, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00130692, None, 2.17922e-05, None, -0.00214918, None, 1.94606e-05, None, -0.00214918, None, 1.94606e-05, None, -0.0016098, None, 2.65369e-05, None, -0.0016098, None, 2.65369e-05, None, 0.996214, None, 0.00646692, None, 0.996214, None, 0.00646692, None)

reports.append(Report(604054744, ("CSC", 2, 2, 2, 27), "MEm22_27"))
reports[-1].posNum = 112275
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00137731, 0.00495973, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.124893, 0.125613, 0), \
                           ValErr(-0.00126635, 0.00141334, 0), \
                           ValErr(0.0012422, 0.00656943, 0), \
                           ValErr(-3.19241e-05, 3.84276e-05, 0), \
                           -161356, 112275, 112275, -nan)
reports[-1].sigmaresid = ValErr(1.01838, 0.00214909, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000235298, None, 3.85773e-06, None, -0.000370321, None, 5.4163e-06, None, -0.000370321, None, 5.4163e-06, None, 0.00127008, None, -1.92735e-05, None, 0.00127008, None, -1.92735e-05, None, 1.01839, None, 0.00683454, None, 1.01839, None, 0.00683454, None)

reports.append(Report(604054760, ("CSC", 2, 2, 2, 29), "MEm22_29"))
reports[-1].posNum = 113359
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0129157, 0.00492805, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0927611, 0.121781, 0), \
                           ValErr(0.000245132, 0.00104993, 0), \
                           ValErr(0.00872884, 0.00643948, 0), \
                           ValErr(-6.88689e-05, 3.50067e-05, 0), \
                           -162901, 113359, 113359, -nan)
reports[-1].sigmaresid = ValErr(1.01826, 0.00212827, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00292335, None, -7.86936e-06, None, 0.00603618, None, -2.13198e-05, None, 0.00603618, None, -2.13198e-05, None, 0.0048244, None, -2.53502e-05, None, 0.0048244, None, -2.53502e-05, None, 1.01828, None, 0.00685818, None, 1.01828, None, 0.00685818, None)

reports.append(Report(604054776, ("CSC", 2, 2, 2, 31), "MEm22_31"))
reports[-1].posNum = 106937
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00602856, 0.00524475, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.12966, 0.123965, 0), \
                           ValErr(-0.000652918, 0.00105217, 0), \
                           ValErr(-0.00118962, 0.00654223, 0), \
                           ValErr(-4.99324e-05, 3.65158e-05, 0), \
                           -152651, 106937, 106937, -nan)
reports[-1].sigmaresid = ValErr(1.00859, 0.00217493, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00344604, None, -2.68832e-05, None, 0.00457285, None, -6.97207e-05, None, 0.00457285, None, -6.97207e-05, None, 0.00130292, None, -4.75211e-05, None, 0.00130292, None, -4.75211e-05, None, 1.0086, None, 0.00677297, None, 1.0086, None, 0.00677297, None)

reports.append(Report(604054792, ("CSC", 2, 2, 2, 33), "MEm22_33"))
reports[-1].posNum = 118610
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00266265, 0.00476473, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0261831, 0.121292, 0), \
                           ValErr(-0.00214159, 0.00137536, 0), \
                           ValErr(0.00475193, 0.0063197, 0), \
                           ValErr(-3.61706e-05, 3.72416e-05, 0), \
                           -170595, 118610, 118610, -nan)
reports[-1].sigmaresid = ValErr(1.01953, 0.00209328, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0012196, None, 1.04403e-05, None, -0.000908964, None, -1.16248e-05, None, -0.000908964, None, -1.16248e-05, None, 0.000112444, None, -1.89816e-05, None, 0.000112444, None, -1.89816e-05, None, 1.01955, None, 0.00690262, None, 1.01955, None, 0.00690262, None)

reports.append(Report(604054808, ("CSC", 2, 2, 2, 35), "MEm22_35"))
reports[-1].posNum = 103784
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00807728, 0.00510054, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0584382, 0.130017, 0), \
                           ValErr(-0.000590761, 0.00144055, 0), \
                           ValErr(-0.00999437, 0.00683789, 0), \
                           ValErr(1.20985e-05, 3.84942e-05, 0), \
                           -145844, 103784, 103784, -nan)
reports[-1].sigmaresid = ValErr(0.986419, 0.00216512, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00649262, None, 7.61834e-06, None, -0.00286893, None, 6.61771e-06, None, -0.00286893, None, 6.61771e-06, None, -0.00570997, None, -8.86695e-06, None, -0.00570997, None, -8.86695e-06, None, 0.986431, None, 0.00676952, None, 0.986431, None, 0.00676952, None)

reports.append(Report(604054544, ("CSC", 2, 2, 2, 2), "MEm22_02"))
reports[-1].posNum = 109754
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0160312, 0.00498799, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.098481, 0.122357, 0), \
                           ValErr(-0.000221298, 0.00134977, 0), \
                           ValErr(-0.0140275, 0.00641996, 0), \
                           ValErr(9.13655e-05, 3.80752e-05, 0), \
                           -157133, 109754, 109754, -nan)
reports[-1].sigmaresid = ValErr(1.01283, 0.00216177, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00371254, None, 1.45735e-05, None, -0.00560965, None, 5.57474e-05, None, -0.00560965, None, 5.57474e-05, None, -0.0073891, None, 6.40687e-05, None, -0.0073891, None, 6.40687e-05, None, 1.01287, None, 0.00693737, None, 1.01287, None, 0.00693737, None)

reports.append(Report(604054560, ("CSC", 2, 2, 2, 4), "MEm22_04"))
reports[-1].posNum = 103663
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00453329, 0.00509412, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0118599, 0.0775588, 0), \
                           ValErr(-9.61664e-05, 0.00119606, 0), \
                           ValErr(-0.00247843, 0.00664487, 0), \
                           ValErr(3.26117e-05, 3.85498e-05, 0), \
                           -146218, 103663, 103663, -nan)
reports[-1].sigmaresid = ValErr(0.991612, 0.00217746, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000589115, None, -8.88266e-06, None, -0.00196596, None, 7.42226e-07, None, -0.00196596, None, 7.42226e-07, None, -0.000700558, None, -5.64144e-06, None, -0.000700558, None, -5.64144e-06, None, 0.991616, None, 0.00675701, None, 0.991616, None, 0.00675701, None)

reports.append(Report(604054576, ("CSC", 2, 2, 2, 6), "MEm22_06"))
reports[-1].posNum = 115556
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00913192, 0.00482306, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.144453, 0.113112, 0), \
                           ValErr(-0.000376699, 0.000883469, 0), \
                           ValErr(0.0244469, 0.00613692, 0), \
                           ValErr(-3.88779e-05, 3.61048e-05, 0), \
                           -165282, 115556, 115556, -nan)
reports[-1].sigmaresid = ValErr(1.01145, 0.0020919, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00577858, None, -8.72251e-06, None, -0.00444377, None, 4.0372e-06, None, -0.00444377, None, 4.0372e-06, None, 0.000836, None, -8.1743e-06, None, 0.000836, None, -8.1743e-06, None, 1.01152, None, 0.00696649, None, 1.01152, None, 0.00696649, None)

reports.append(Report(604054592, ("CSC", 2, 2, 2, 8), "MEm22_08"))
reports[-1].posNum = 100479
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000865706, 0.00522384, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.131569, 0.125539, 0), \
                           ValErr(-0.00136706, 0.00137367, 0), \
                           ValErr(0.00360201, 0.00667039, 0), \
                           ValErr(4.55942e-05, 3.89946e-05, 0), \
                           -140738, 100479, 100479, -nan)
reports[-1].sigmaresid = ValErr(0.981896, 0.00219035, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00126854, None, 6.36798e-08, None, 0.00112706, None, 2.44239e-05, None, 0.00112706, None, 2.44239e-05, None, 0.00561304, None, -8.53629e-06, None, 0.00561304, None, -8.53629e-06, None, 0.981918, None, 0.00660506, None, 0.981918, None, 0.00660506, None)

reports.append(Report(604054608, ("CSC", 2, 2, 2, 10), "MEm22_10"))
reports[-1].posNum = 118173
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0075126, 0.00482248, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0599431, 0.119212, 0), \
                           ValErr(-0.00154898, 0.0013451, 0), \
                           ValErr(-5.47215e-05, 0.00624624, 0), \
                           ValErr(-5.18232e-05, 3.75037e-05, 0), \
                           -169569, 118173, 118173, -nan)
reports[-1].sigmaresid = ValErr(1.01611, 0.0020901, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00501951, None, -1.63684e-05, None, 0.00557455, None, -2.99117e-05, None, 0.00557455, None, -2.99117e-05, None, 0.00491377, None, -3.98834e-05, None, 0.00491377, None, -3.98834e-05, None, 1.01613, None, 0.00664813, None, 1.01613, None, 0.00664813, None)

reports.append(Report(604054624, ("CSC", 2, 2, 2, 12), "MEm22_12"))
reports[-1].posNum = 101303
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00212259, 0.00513788, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.107198, 0.0864679, 0), \
                           ValErr(-0.00126829, 0.00116455, 0), \
                           ValErr(-0.00885576, 0.00656207, 0), \
                           ValErr(-1.48786e-05, 3.78511e-05, 0), \
                           -141390, 101303, 101303, -nan)
reports[-1].sigmaresid = ValErr(0.977048, 0.00215414, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00175672, None, 9.12941e-06, None, 0.00587896, None, 1.88089e-05, None, 0.00587896, None, 1.88089e-05, None, 0.00929139, None, -1.22449e-07, None, 0.00929139, None, -1.22449e-07, None, 0.977067, None, 0.00686823, None, 0.977067, None, 0.00686823, None)

reports.append(Report(604054640, ("CSC", 2, 2, 2, 14), "MEm22_14"))
reports[-1].posNum = 115477
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00459469, 0.00483636, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.195209, 0.119249, 0), \
                           ValErr(-0.00260406, 0.00134003, 0), \
                           ValErr(-0.0071225, 0.00627501, 0), \
                           ValErr(-1.02819e-05, 3.7332e-05, 0), \
                           -164656, 115477, 115477, -nan)
reports[-1].sigmaresid = ValErr(1.00696, 0.00209532, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000886973, None, 1.7805e-05, None, -0.00143341, None, -2.36193e-06, None, -0.00143341, None, -2.36193e-06, None, 0.00109084, None, 5.2951e-06, None, 0.00109084, None, 5.2951e-06, None, 1.00699, None, 0.00677565, None, 1.00699, None, 0.00677565, None)

reports.append(Report(604054656, ("CSC", 2, 2, 2, 16), "MEm22_16"))
reports[-1].posNum = 103277
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00863305, 0.00515214, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0977536, 0.12825, 0), \
                           ValErr(-0.000501769, 0.00140264, 0), \
                           ValErr(-0.0141628, 0.00674897, 0), \
                           ValErr(4.02311e-05, 3.89434e-05, 0), \
                           -146539, 103277, 103277, -nan)
reports[-1].sigmaresid = ValErr(0.999949, 0.00220019, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00598635, None, 1.39639e-05, None, -0.000186299, None, 1.58662e-05, None, -0.000186299, None, 1.58662e-05, None, -0.00463286, None, 1.35115e-05, None, -0.00463286, None, 1.35115e-05, None, 0.999975, None, 0.00643474, None, 0.999975, None, 0.00643474, None)

reports.append(Report(604054672, ("CSC", 2, 2, 2, 18), "MEm22_18"))
reports[-1].posNum = 108986
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000866087, 0.00500063, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0744952, 0.12165, 0), \
                           ValErr(0.00200216, 0.00134983, 0), \
                           ValErr(0.0060402, 0.00638617, 0), \
                           ValErr(2.05673e-05, 3.82951e-05, 0), \
                           -155441, 108986, 108986, -nan)
reports[-1].sigmaresid = ValErr(1.00734, 0.00215762, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00359932, None, -2.93686e-05, None, -0.00131927, None, -5.73928e-06, None, -0.00131927, None, -5.73928e-06, None, -0.00207055, None, -1.78253e-05, None, -0.00207055, None, -1.78253e-05, None, 1.00736, None, 0.00692345, None, 1.00736, None, 0.00692345, None)

reports.append(Report(604054688, ("CSC", 2, 2, 2, 20), "MEm22_20"))
reports[-1].posNum = 111794
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00461963, 0.00496025, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0418213, 0.121455, 0), \
                           ValErr(0.000448015, 0.00135564, 0), \
                           ValErr(-0.00280185, 0.00640063, 0), \
                           ValErr(-1.38335e-06, 3.79914e-05, 0), \
                           -159592, 111794, 111794, -nan)
reports[-1].sigmaresid = ValErr(1.00865, 0.00213313, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000790966, None, 1.71019e-05, None, -0.00326642, None, 3.49223e-05, None, -0.00326642, None, 3.49223e-05, None, 0.000630817, None, -9.70862e-06, None, 0.000630817, None, -9.70862e-06, None, 1.00865, None, 0.00670418, None, 1.00865, None, 0.00670418, None)

reports.append(Report(604054704, ("CSC", 2, 2, 2, 22), "MEm22_22"))
reports[-1].posNum = 103662
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000624976, 0.00513168, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0949092, 0.127319, 0), \
                           ValErr(-0.00143506, 0.00140408, 0), \
                           ValErr(0.0060461, 0.00668699, 0), \
                           ValErr(2.63703e-05, 3.89006e-05, 0), \
                           -146499, 103662, 103662, -nan)
reports[-1].sigmaresid = ValErr(0.994319, 0.00218375, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.003049, None, 1.02957e-06, None, -0.00108526, None, 6.20869e-06, None, -0.00108526, None, 6.20869e-06, None, 0.00540684, None, 4.9308e-06, None, 0.00540684, None, 4.9308e-06, None, 0.994335, None, 0.00670237, None, 0.994335, None, 0.00670237, None)

reports.append(Report(604054720, ("CSC", 2, 2, 2, 24), "MEm22_24"))
reports[-1].posNum = 113924
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00102625, 0.00484033, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0551276, 0.0663905, 0), \
                           ValErr(-0.000180198, 0.000856618, 0), \
                           ValErr(0.00365032, 0.00616909, 0), \
                           ValErr(1.80061e-05, 3.50648e-05, 0), \
                           -161870, 113924, 113924, -nan)
reports[-1].sigmaresid = ValErr(1.00192, 0.00208884, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00107106, None, 9.64175e-07, None, -9.05978e-05, None, -2.31145e-06, None, -9.05978e-05, None, -2.31145e-06, None, 0.00416835, None, -5.60166e-05, None, 0.00416835, None, -5.60166e-05, None, 1.00193, None, 0.00677203, None, 1.00193, None, 0.00677203, None)

reports.append(Report(604054736, ("CSC", 2, 2, 2, 26), "MEm22_26"))
reports[-1].posNum = 101132
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-3.63776e-05, 0.00524824, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.157873, 0.125651, 0), \
                           ValErr(0.000234521, 0.00137351, 0), \
                           ValErr(-0.00218222, 0.00671462, 0), \
                           ValErr(3.04393e-05, 3.9129e-05, 0), \
                           -142139, 101132, 101132, -nan)
reports[-1].sigmaresid = ValErr(0.986637, 0.00219381, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00387708, None, -1.37191e-05, None, 0.00235652, None, 1.64744e-05, None, 0.00235652, None, 1.64744e-05, None, 0.00177837, None, 6.95381e-06, None, 0.00177837, None, 6.95381e-06, None, 0.986647, None, 0.00661957, None, 0.986647, None, 0.00661957, None)

reports.append(Report(604054752, ("CSC", 2, 2, 2, 28), "MEm22_28"))
reports[-1].posNum = 118207
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00415443, 0.00482932, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0377065, 0.118375, 0), \
                           ValErr(0.000561524, 0.00134111, 0), \
                           ValErr(-0.00607165, 0.0062304, 0), \
                           ValErr(4.93843e-06, 3.73455e-05, 0), \
                           -169174, 118207, 118207, -nan)
reports[-1].sigmaresid = ValErr(1.0123, 0.00208197, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0010418, None, 5.13958e-06, None, -0.000958026, None, 4.63234e-05, None, -0.000958026, None, 4.63234e-05, None, 0.00209809, None, 1.12612e-05, None, 0.00209809, None, 1.12612e-05, None, 1.01231, None, 0.0065709, None, 1.01231, None, 0.0065709, None)

reports.append(Report(604054768, ("CSC", 2, 2, 2, 30), "MEm22_30"))
reports[-1].posNum = 100746
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00222007, 0.00517571, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.049545, 0.0962366, 0), \
                           ValErr(-0.000641276, 0.00122171, 0), \
                           ValErr(-0.0141887, 0.00660204, 0), \
                           ValErr(7.83181e-06, 3.86221e-05, 0), \
                           -141422, 100746, 100746, -nan)
reports[-1].sigmaresid = ValErr(0.98493, 0.00219219, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00556996, None, -2.5213e-05, None, 0.0094681, None, -2.42315e-05, None, 0.0094681, None, -2.42315e-05, None, 0.00564233, None, -3.91294e-05, None, 0.00564233, None, -3.91294e-05, None, 0.984954, None, 0.00694462, None, 0.984954, None, 0.00694462, None)

reports.append(Report(604054784, ("CSC", 2, 2, 2, 32), "MEm22_32"))
reports[-1].posNum = 116337
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00157557, 0.0048472, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.168045, 0.119298, 0), \
                           ValErr(-0.00183227, 0.00134229, 0), \
                           ValErr(-0.00248922, 0.00626902, 0), \
                           ValErr(-3.46207e-06, 3.74927e-05, 0), \
                           -166883, 116337, 116337, -nan)
reports[-1].sigmaresid = ValErr(1.01566, 0.0021056, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00042342, None, 3.08506e-05, None, 0.00260632, None, 3.07259e-05, None, 0.00260632, None, 3.07259e-05, None, 0.00556108, None, 1.82732e-06, None, 0.00556108, None, 1.82732e-06, None, 1.01568, None, 0.00680577, None, 1.01568, None, 0.00680577, None)

reports.append(Report(604054800, ("CSC", 2, 2, 2, 34), "MEm22_34"))
reports[-1].posNum = 105523
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00720179, 0.00504485, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.256442, 0.107592, 0), \
                           ValErr(-0.00273508, 0.001194, 0), \
                           ValErr(-0.00395345, 0.00654241, 0), \
                           ValErr(1.97815e-05, 3.76473e-05, 0), \
                           -148569, 105523, 105523, -nan)
reports[-1].sigmaresid = ValErr(0.989052, 0.00215034, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00823377, None, -3.28396e-06, None, 0.00987081, None, 1.68277e-05, None, 0.00987081, None, 1.68277e-05, None, 0.0068346, None, 1.26592e-06, None, 0.0068346, None, 1.26592e-06, None, 0.989086, None, 0.00671893, None, 0.989086, None, 0.00671893, None)

reports.append(Report(604054816, ("CSC", 2, 2, 2, 36), "MEm22_36"))
reports[-1].posNum = 112575
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00127734, 0.00497269, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.11461, 0.119639, 0), \
                           ValErr(0.00173621, 0.00133921, 0), \
                           ValErr(-0.00157026, 0.00632407, 0), \
                           ValErr(-4.52039e-05, 3.82698e-05, 0), \
                           -160404, 112575, 112575, -nan)
reports[-1].sigmaresid = ValErr(1.00595, 0.00212002, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000269392, None, 7.55057e-06, None, -0.00232845, None, -3.11527e-05, None, -0.00232845, None, -3.11527e-05, None, -0.000980197, None, -2.43029e-05, None, -0.000980197, None, -2.43029e-05, None, 1.00596, None, 0.00690009, None, 1.00596, None, 0.00690009, None)

reports.append(Report(604058120, ("CSC", 2, 3, 1, 1), "MEm31_01"))
reports[-1].posNum = 344897
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0011708, 0.00126324, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00653924, 0.0349505, 0), \
                           ValErr(0.000415467, 0.000781857, 0), \
                           ValErr(-0.00132403, 0.00156107, 0), \
                           ValErr(2.19012e-05, 2.0746e-05, 0), \
                           -249370, 344897, 344897, -nan)
reports[-1].sigmaresid = ValErr(0.49862, 0.000600358, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.001242, None, -2.50096e-07, None, -0.00182542, None, -8.43316e-06, None, -0.00182542, None, -8.43316e-06, None, -0.00262655, None, -1.78959e-06, None, -0.00262655, None, -1.78959e-06, None, 0.498622, None, 0.00597079, None, 0.498622, None, 0.00597079, None)

reports.append(Report(604058136, ("CSC", 2, 3, 1, 3), "MEm31_03"))
reports[-1].posNum = 346275
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00131029, 0.00126668, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0120657, 0.0349222, 0), \
                           ValErr(-0.000878806, 0.00078261, 0), \
                           ValErr(-0.00108324, 0.00156095, 0), \
                           ValErr(-6.57315e-06, 2.0793e-05, 0), \
                           -251443, 346275, 346275, -nan)
reports[-1].sigmaresid = ValErr(0.500172, 0.000601026, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00132306, None, 4.04196e-06, None, 0.000653968, None, 3.59093e-06, None, 0.000653968, None, 3.59093e-06, None, 0.001992, None, -1.42379e-06, None, 0.001992, None, -1.42379e-06, None, 0.500174, None, 0.00599528, None, 0.500174, None, 0.00599528, None)

reports.append(Report(604058152, ("CSC", 2, 3, 1, 5), "MEm31_05"))
reports[-1].posNum = 346174
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00146964, 0.0012673, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0327319, 0.0350174, 0), \
                           ValErr(0.00109011, 0.000782731, 0), \
                           ValErr(0.00291922, 0.00156469, 0), \
                           ValErr(3.09727e-05, 2.08368e-05, 0), \
                           -251566, 346174, 346174, -nan)
reports[-1].sigmaresid = ValErr(0.500456, 0.000601454, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000592588, None, -1.31961e-05, None, 0.000353196, None, -3.44943e-05, None, 0.000353196, None, -3.44943e-05, None, 0.000272124, None, -3.05809e-05, None, 0.000272124, None, -3.05809e-05, None, 0.500463, None, 0.00596134, None, 0.500463, None, 0.00596134, None)

reports.append(Report(604058168, ("CSC", 2, 3, 1, 7), "MEm31_07"))
reports[-1].posNum = 343890
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(3.30069e-06, 0.00126713, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00202019, 0.0348616, 0), \
                           ValErr(0.00110254, 0.000779009, 0), \
                           ValErr(0.000109928, 0.00156084, 0), \
                           ValErr(-6.54684e-06, 2.07795e-05, 0), \
                           -247914, 343890, 343890, -nan)
reports[-1].sigmaresid = ValErr(0.497567, 0.000599968, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00151364, None, 3.85296e-06, None, 3.62783e-05, None, 9.92992e-06, None, 3.62783e-05, None, 9.92992e-06, None, 0.00139652, None, 5.16529e-06, None, 0.00139652, None, 5.16529e-06, None, 0.497568, None, 0.00588159, None, 0.497568, None, 0.00588159, None)

reports.append(Report(604058184, ("CSC", 2, 3, 1, 9), "MEm31_09"))
reports[-1].posNum = 344011
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000235893, 0.00126461, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.014471, 0.0349467, 0), \
                           ValErr(-0.00130267, 0.000781128, 0), \
                           ValErr(-0.000209783, 0.00156398, 0), \
                           ValErr(2.66857e-05, 2.07696e-05, 0), \
                           -248036, 344011, 344011, -nan)
reports[-1].sigmaresid = ValErr(0.497615, 0.000599918, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000476395, None, -1.86579e-05, None, 0.000239931, None, -2.01194e-05, None, 0.000239931, None, -2.01194e-05, None, 7.78871e-05, None, -1.16929e-05, None, 7.78871e-05, None, -1.16929e-05, None, 0.497619, None, 0.00616895, None, 0.497619, None, 0.00616895, None)

reports.append(Report(604058200, ("CSC", 2, 3, 1, 11), "MEm31_11"))
reports[-1].posNum = 344330
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00376498, 0.00126127, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0578492, 0.0349449, 0), \
                           ValErr(-0.000249046, 0.000779549, 0), \
                           ValErr(0.00302902, 0.00155783, 0), \
                           ValErr(4.15033e-05, 2.07167e-05, 0), \
                           -248294, 344330, 344330, -nan)
reports[-1].sigmaresid = ValErr(0.497657, 0.000599691, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00117259, None, -1.93661e-05, None, -0.00182974, None, -3.75129e-05, None, -0.00182974, None, -3.75129e-05, None, -0.00194093, None, -3.4504e-05, None, -0.00194093, None, -3.4504e-05, None, 0.497663, None, 0.00589689, None, 0.497663, None, 0.00589689, None)

reports.append(Report(604058216, ("CSC", 2, 3, 1, 13), "MEm31_13"))
reports[-1].posNum = 345447
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000182478, 0.00126048, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0688917, 0.0347399, 0), \
                           ValErr(0.000368976, 0.000775956, 0), \
                           ValErr(-8.55501e-05, 0.00155542, 0), \
                           ValErr(4.07296e-06, 2.06534e-05, 0), \
                           -248378, 345447, 345447, -nan)
reports[-1].sigmaresid = ValErr(0.496618, 0.000597471, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000538189, None, -5.54029e-07, None, -0.000214407, None, 7.47567e-07, None, -0.000214407, None, 7.47567e-07, None, -0.000362825, None, 3.39144e-06, None, -0.000362825, None, 3.39144e-06, None, 0.496622, None, 0.0059288, None, 0.496622, None, 0.0059288, None)

reports.append(Report(604058232, ("CSC", 2, 3, 1, 15), "MEm31_15"))
reports[-1].posNum = 344263
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000876926, 0.00126005, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0373928, 0.0348466, 0), \
                           ValErr(0.000288118, 0.000776387, 0), \
                           ValErr(0.000980706, 0.00155343, 0), \
                           ValErr(-1.48559e-05, 2.06731e-05, 0), \
                           -247761, 344263, 344263, -nan)
reports[-1].sigmaresid = ValErr(0.496957, 0.000598905, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000954659, None, 8.0081e-06, None, 0.00137842, None, -1.47525e-05, None, 0.00137842, None, -1.47525e-05, None, -0.000722687, None, -1.29721e-05, None, -0.000722687, None, -1.29721e-05, None, 0.496959, None, 0.005929, None, 0.496959, None, 0.005929, None)

reports.append(Report(604058248, ("CSC", 2, 3, 1, 17), "MEm31_17"))
reports[-1].posNum = 345596
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00191027, 0.0012604, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0529454, 0.0348436, 0), \
                           ValErr(-0.000636763, 0.000778156, 0), \
                           ValErr(0.00324729, 0.00155659, 0), \
                           ValErr(3.69675e-05, 2.0667e-05, 0), \
                           -249275, 345596, 345596, -nan)
reports[-1].sigmaresid = ValErr(0.497754, 0.000598708, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(7.36978e-06, None, -4.90383e-06, None, 0.000132534, None, -5.86348e-06, None, 0.000132534, None, -5.86348e-06, None, 2.37572e-05, None, -9.44155e-06, None, 2.37572e-05, None, -9.44155e-06, None, 0.497761, None, 0.00595928, None, 0.497761, None, 0.00595928, None)

reports.append(Report(604058128, ("CSC", 2, 3, 1, 2), "MEm31_02"))
reports[-1].posNum = 355531
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0014551, 0.00129127, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0108292, 0.0365254, 0), \
                           ValErr(-0.00100949, 0.000817557, 0), \
                           ValErr(-0.000374415, 0.00163584, 0), \
                           ValErr(6.1142e-06, 2.11781e-05, 0), \
                           -269274, 355531, 355531, -nan)
reports[-1].sigmaresid = ValErr(0.516049, 0.000611979, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00227135, None, -1.54383e-05, None, -0.00163585, None, -1.4238e-05, None, -0.00163585, None, -1.4238e-05, None, -0.00261133, None, -2.64646e-05, None, -0.00261133, None, -2.64646e-05, None, 0.516051, None, 0.00587442, None, 0.516051, None, 0.00587442, None)

reports.append(Report(604058144, ("CSC", 2, 3, 1, 4), "MEm31_04"))
reports[-1].posNum = 354188
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00034127, 0.00128805, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0760391, 0.0364792, 0), \
                           ValErr(-0.000169169, 0.000813539, 0), \
                           ValErr(-0.000786713, 0.00162865, 0), \
                           ValErr(-1.80352e-05, 2.11185e-05, 0), \
                           -266962, 354188, 354188, -nan)
reports[-1].sigmaresid = ValErr(0.514165, 0.0006109, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00115662, None, 1.3872e-06, None, -0.00019602, None, 1.0932e-07, None, -0.00019602, None, 1.0932e-07, None, -0.000666823, None, -1.82472e-05, None, -0.000666823, None, -1.82472e-05, None, 0.514169, None, 0.00584967, None, 0.514169, None, 0.00584967, None)

reports.append(Report(604058160, ("CSC", 2, 3, 1, 6), "MEm31_06"))
reports[-1].posNum = 353548
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00107541, 0.00128007, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0266189, 0.0363087, 0), \
                           ValErr(0.000182423, 0.00081765, 0), \
                           ValErr(-0.00146956, 0.00163583, 0), \
                           ValErr(-1.31182e-05, 2.10349e-05, 0), \
                           -267876, 353548, 353548, -nan)
reports[-1].sigmaresid = ValErr(0.516202, 0.000612931, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000551485, None, -6.83597e-06, None, 0.000185042, None, -2.58936e-06, None, 0.000185042, None, -2.58936e-06, None, -0.00144183, None, -1.0007e-05, None, -0.00144183, None, -1.0007e-05, None, 0.516203, None, 0.00574927, None, 0.516203, None, 0.00574927, None)

reports.append(Report(604058176, ("CSC", 2, 3, 1, 8), "MEm31_08"))
reports[-1].posNum = 353490
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000129586, 0.00129809, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0728784, 0.036229, 0), \
                           ValErr(-0.000750589, 0.000809441, 0), \
                           ValErr(-0.000818248, 0.0016385, 0), \
                           ValErr(2.18988e-05, 2.11137e-05, 0), \
                           -269106, 353490, 353490, -nan)
reports[-1].sigmaresid = ValErr(0.518065, 0.000600163, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000276511, None, 8.62167e-07, None, -0.000225467, None, -1.61437e-06, None, -0.000225467, None, -1.61437e-06, None, -0.000358974, None, 2.14151e-06, None, -0.000358974, None, 2.14151e-06, None, 0.51807, None, 0.00590148, None, 0.51807, None, 0.00590148, None)

reports.append(Report(604058192, ("CSC", 2, 3, 1, 10), "MEm31_10"))
reports[-1].posNum = 353409
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(3.66318e-05, 0.00130322, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0163302, 0.0369714, 0), \
                           ValErr(0.000522286, 0.000825251, 0), \
                           ValErr(-0.000165891, 0.00165042, 0), \
                           ValErr(2.96816e-06, 2.13899e-05, 0), \
                           -270617, 353409, 353409, -nan)
reports[-1].sigmaresid = ValErr(0.520376, 0.000618961, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000174685, None, 7.34561e-06, None, -4.23183e-05, None, -4.74026e-06, None, -4.23183e-05, None, -4.74026e-06, None, 0.000220896, None, -9.42004e-06, None, 0.000220896, None, -9.42004e-06, None, 0.520376, None, 0.00578433, None, 0.520376, None, 0.00578433, None)

reports.append(Report(604058208, ("CSC", 2, 3, 1, 12), "MEm31_12"))
reports[-1].posNum = 353787
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00184886, 0.00129498, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0231856, 0.0338593, 0), \
                           ValErr(0.000114542, 0.000806809, 0), \
                           ValErr(-0.00111241, 0.00163926, 0), \
                           ValErr(8.55336e-06, 2.11237e-05, 0), \
                           -269674, 353787, 353787, -nan)
reports[-1].sigmaresid = ValErr(0.518566, 0.000613796, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00172648, None, -5.16647e-06, None, 0.00126163, None, -1.44174e-05, None, 0.00126163, None, -1.44174e-05, None, 0.00183436, None, -4.75645e-06, None, 0.00183436, None, -4.75645e-06, None, 0.518567, None, 0.00581824, None, 0.518567, None, 0.00581824, None)

reports.append(Report(604058224, ("CSC", 2, 3, 1, 14), "MEm31_14"))
reports[-1].posNum = 354169
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000947864, 0.00129973, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0308528, 0.0368232, 0), \
                           ValErr(-0.000789798, 0.000824016, 0), \
                           ValErr(0.00098794, 0.00164424, 0), \
                           ValErr(2.08005e-05, 2.13807e-05, 0), \
                           -270592, 354169, 354169, -nan)
reports[-1].sigmaresid = ValErr(0.519484, 0.000617237, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000245839, None, -3.90652e-06, None, -0.000299977, None, -5.14408e-06, None, -0.000299977, None, -5.14408e-06, None, -0.000761533, None, 4.26125e-06, None, -0.000761533, None, 4.26125e-06, None, 0.519486, None, 0.00583297, None, 0.519486, None, 0.00583297, None)

reports.append(Report(604058240, ("CSC", 2, 3, 1, 16), "MEm31_16"))
reports[-1].posNum = 354518
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00119746, 0.00129261, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0426857, 0.0366622, 0), \
                           ValErr(0.000405769, 0.000820842, 0), \
                           ValErr(-0.000290333, 0.00163409, 0), \
                           ValErr(1.37559e-05, 2.12449e-05, 0), \
                           -269260, 354518, 354518, -nan)
reports[-1].sigmaresid = ValErr(0.517147, 0.000614159, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000704239, None, -3.79947e-06, None, -0.00129637, None, -7.32248e-06, None, -0.00129637, None, -7.32248e-06, None, -0.000136342, None, -7.33738e-06, None, -0.000136342, None, -7.33738e-06, None, 0.517149, None, 0.00582899, None, 0.517149, None, 0.00582899, None)

reports.append(Report(604058256, ("CSC", 2, 3, 1, 18), "MEm31_18"))
reports[-1].posNum = 355685
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00104844, 0.00128706, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0450274, 0.0365298, 0), \
                           ValErr(-0.000523752, 0.000815453, 0), \
                           ValErr(0.00132264, 0.0016268, 0), \
                           ValErr(-2.42155e-06, 2.11704e-05, 0), \
                           -269223, 355685, 355685, -nan)
reports[-1].sigmaresid = ValErr(0.515807, 0.00061156, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000405267, None, 7.31197e-06, None, -0.00031849, None, -5.99482e-06, None, -0.00031849, None, -5.99482e-06, None, -0.00102375, None, -2.32454e-05, None, -0.00102375, None, -2.32454e-05, None, 0.515809, None, 0.0057832, None, 0.515809, None, 0.0057832, None)

reports.append(Report(604058632, ("CSC", 2, 3, 2, 1), "MEm32_01"))
reports[-1].posNum = 123444
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000311457, 0.00493088, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0119456, 0.138088, 0), \
                           ValErr(0.00361644, 0.00157679, 0), \
                           ValErr(0.00719949, 0.00727034, 0), \
                           ValErr(4.18523e-05, 3.85216e-05, 0), \
                           -182737, 123444, 123444, -nan)
reports[-1].sigmaresid = ValErr(1.06331, 0.00213998, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00701404, None, 3.08299e-06, None, 0.00431828, None, 2.1756e-05, None, 0.00431828, None, 2.1756e-05, None, 0.00462665, None, 1.61964e-06, None, 0.00462665, None, 1.61964e-06, None, 1.06334, None, 0.0076416, None, 1.06334, None, 0.0076416, None)

reports.append(Report(604058648, ("CSC", 2, 3, 2, 3), "MEm32_03"))
reports[-1].posNum = 113633
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00581358, 0.00497859, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0460976, 0.0730606, 0), \
                           ValErr(0.000506927, 0.00155329, 0), \
                           ValErr(-0.019562, 0.00730113, 0), \
                           ValErr(-2.95966e-05, 3.86751e-05, 0), \
                           -163640, 113633, 113633, -nan)
reports[-1].sigmaresid = ValErr(1.02136, 0.00211604, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00312455, None, -3.76668e-05, None, -0.00389933, None, -1.68407e-05, None, -0.00389933, None, -1.68407e-05, None, -0.00488293, None, 4.60371e-06, None, -0.00488293, None, 4.60371e-06, None, 1.02139, None, 0.00760346, None, 1.02139, None, 0.00760346, None)

reports.append(Report(604058664, ("CSC", 2, 3, 2, 5), "MEm32_05"))
reports[-1].posNum = 122007
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00652194, 0.00483275, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.138466, 0.101857, 0), \
                           ValErr(0.00226998, 0.00117017, 0), \
                           ValErr(-0.00851548, 0.00690025, 0), \
                           ValErr(3.30919e-05, 3.20338e-05, 0), \
                           -178955, 122007, 122007, -nan)
reports[-1].sigmaresid = ValErr(1.04898, 0.00210572, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00618607, None, 3.62338e-06, None, -0.0091075, None, -1.70601e-05, None, -0.0091075, None, -1.70601e-05, None, -0.00531238, None, 5.97015e-06, None, -0.00531238, None, 5.97015e-06, None, 1.04901, None, 0.00756467, None, 1.04901, None, 0.00756467, None)

reports.append(Report(604058680, ("CSC", 2, 3, 2, 7), "MEm32_07"))
reports[-1].posNum = 113529
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00421956, 0.00516114, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0213223, 0.141507, 0), \
                           ValErr(0.00324965, 0.00159593, 0), \
                           ValErr(0.00747513, 0.00749751, 0), \
                           ValErr(1.78457e-05, 3.97377e-05, 0), \
                           -165236, 113529, 113529, -nan)
reports[-1].sigmaresid = ValErr(1.03719, 0.00217666, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00227239, None, 7.93669e-07, None, -0.00016006, None, -1.57506e-05, None, -0.00016006, None, -1.57506e-05, None, 0.00346498, None, -1.33031e-05, None, 0.00346498, None, -1.33031e-05, None, 1.03722, None, 0.00826281, None, 1.03722, None, 0.00826281, None)

reports.append(Report(604058696, ("CSC", 2, 3, 2, 9), "MEm32_09"))
reports[-1].posNum = 118205
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00725872, 0.00492828, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.124381, 0.132778, 0), \
                           ValErr(0.000734788, 0.00142227, 0), \
                           ValErr(0.0106183, 0.00713191, 0), \
                           ValErr(4.66306e-05, 3.18314e-05, 0), \
                           -173425, 118205, 118205, -nan)
reports[-1].sigmaresid = ValErr(1.0494, 0.00215245, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00191577, None, -1.37281e-06, None, -0.000915825, None, -2.69741e-05, None, -0.000915825, None, -2.69741e-05, None, 0.000353591, None, 3.89193e-05, None, 0.000353591, None, 3.89193e-05, None, 1.04941, None, 0.00796699, None, 1.04941, None, 0.00796699, None)

reports.append(Report(604058712, ("CSC", 2, 3, 2, 11), "MEm32_11"))
reports[-1].posNum = 116870
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00204216, 0.00498254, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.107353, 0.10306, 0), \
                           ValErr(0.00187704, 0.00151592, 0), \
                           ValErr(-0.0127444, 0.00736005, 0), \
                           ValErr(1.073e-05, 3.70252e-05, 0), \
                           -171483, 116870, 116870, -nan)
reports[-1].sigmaresid = ValErr(1.04955, 0.00216623, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00302232, None, 1.92653e-06, None, -0.00298149, None, -3.54081e-05, None, -0.00298149, None, -3.54081e-05, None, -0.00608897, None, -2.38009e-05, None, -0.00608897, None, -2.38009e-05, None, 1.04957, None, 0.00774759, None, 1.04957, None, 0.00774759, None)

reports.append(Report(604058728, ("CSC", 2, 3, 2, 13), "MEm32_13"))
reports[-1].posNum = 111751
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000667841, 0.00519993, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.120043, 0.142658, 0), \
                           ValErr(-0.000438363, 0.00159963, 0), \
                           ValErr(0.0050504, 0.00755596, 0), \
                           ValErr(1.59122e-05, 3.97057e-05, 0), \
                           -162556, 111751, 111751, -nan)
reports[-1].sigmaresid = ValErr(1.03633, 0.00219209, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00570972, None, -1.31038e-05, None, 0.00343502, None, -2.90527e-05, None, 0.00343502, None, -2.90527e-05, None, -0.00489022, None, -3.02631e-05, None, -0.00489022, None, -3.02631e-05, None, 1.03634, None, 0.00772774, None, 1.03634, None, 0.00772774, None)

reports.append(Report(604058744, ("CSC", 2, 3, 2, 15), "MEm32_15"))
reports[-1].posNum = 119987
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0176613, 0.00484462, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0817131, 0.139831, 0), \
                           ValErr(-0.00193503, 0.00160113, 0), \
                           ValErr(-0.00695483, 0.00725319, 0), \
                           ValErr(-8.90776e-05, 3.81911e-05, 0), \
                           -175759, 119987, 119987, -nan)
reports[-1].sigmaresid = ValErr(1.04695, 0.00213719, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0133276, None, 5.05027e-05, None, 0.0115308, None, 1.69342e-05, None, 0.0115308, None, 1.69342e-05, None, 0.0141691, None, 4.74194e-05, None, 0.0141691, None, 4.74194e-05, None, 1.04698, None, 0.00825596, None, 1.04698, None, 0.00825596, None)

reports.append(Report(604058760, ("CSC", 2, 3, 2, 17), "MEm32_17"))
reports[-1].posNum = 113150
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00282988, 0.0050799, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.259107, 0.141006, 0), \
                           ValErr(0.00175508, 0.00158534, 0), \
                           ValErr(-0.00107177, 0.00746491, 0), \
                           ValErr(-8.73449e-05, 3.90698e-05, 0), \
                           -162916, 113150, 113150, -nan)
reports[-1].sigmaresid = ValErr(1.0211, 0.00214648, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000950737, None, -2.22957e-05, None, -0.00119331, None, -2.95812e-05, None, -0.00119331, None, -2.95812e-05, None, 0.00144407, None, 1.11676e-05, None, 0.00144407, None, 1.11676e-05, None, 1.02115, None, 0.00732013, None, 1.02115, None, 0.00732013, None)

reports.append(Report(604058776, ("CSC", 2, 3, 2, 19), "MEm32_19"))
reports[-1].posNum = 122929
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00493379, 0.00493226, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0447399, 0.137398, 0), \
                           ValErr(0.00260038, 0.00156565, 0), \
                           ValErr(-0.000914055, 0.00723626, 0), \
                           ValErr(-7.26196e-06, 3.85608e-05, 0), \
                           -181486, 122929, 122929, -nan)
reports[-1].sigmaresid = ValErr(1.05909, 0.00213597, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00174588, None, 1.83944e-05, None, 0.00424572, None, -1.12079e-06, None, 0.00424572, None, -1.12079e-06, None, 0.007378, None, -1.07806e-05, None, 0.007378, None, -1.07806e-05, None, 1.0591, None, 0.00761058, None, 1.0591, None, 0.00761058, None)

reports.append(Report(604058792, ("CSC", 2, 3, 2, 21), "MEm32_21"))
reports[-1].posNum = 111566
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00812374, 0.00506834, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.13553, 0.142818, 0), \
                           ValErr(0.00415631, 0.00158146, 0), \
                           ValErr(-0.00310403, 0.00751425, 0), \
                           ValErr(-3.64816e-05, 3.87872e-05, 0), \
                           -160697, 111566, 111566, -nan)
reports[-1].sigmaresid = ValErr(1.02167, 0.00216286, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00637641, None, 6.41217e-06, None, 0.00537798, None, -6.87174e-05, None, 0.00537798, None, -6.87174e-05, None, 0.00302054, None, -4.31804e-05, None, 0.00302054, None, -4.31804e-05, None, 1.02171, None, 0.00845791, None, 1.02171, None, 0.00845791, None)

reports.append(Report(604058808, ("CSC", 2, 3, 2, 23), "MEm32_23"))
reports[-1].posNum = 122979
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00478752, 0.00485264, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.170108, 0.137166, 0), \
                           ValErr(0.000204757, 0.00155767, 0), \
                           ValErr(-0.0064841, 0.0071666, 0), \
                           ValErr(-9.27016e-05, 3.79341e-05, 0), \
                           -180556, 122979, 122979, -nan)
reports[-1].sigmaresid = ValErr(1.05048, 0.00211816, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-3.96287e-05, None, -1.09716e-05, None, -0.00128155, None, -1.63264e-06, None, -0.00128155, None, -1.63264e-06, None, -0.00312189, None, 3.54349e-07, None, -0.00312189, None, 3.54349e-07, None, 1.05051, None, 0.00751145, None, 1.05051, None, 0.00751145, None)

reports.append(Report(604058824, ("CSC", 2, 3, 2, 25), "MEm32_25"))
reports[-1].posNum = 114725
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00184983, 0.00509467, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0691518, 0.140552, 0), \
                           ValErr(-9.68923e-05, 0.00158212, 0), \
                           ValErr(0.00171449, 0.00743313, 0), \
                           ValErr(1.62491e-05, 3.92612e-05, 0), \
                           -166492, 114725, 114725, -nan)
reports[-1].sigmaresid = ValErr(1.03281, 0.00215614, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000492566, None, -5.58868e-06, None, -0.000467733, None, -1.53909e-05, None, -0.000467733, None, -1.53909e-05, None, 0.00855813, None, 4.61197e-05, None, 0.00855813, None, 4.61197e-05, None, 1.03282, None, 0.00732577, None, 1.03282, None, 0.00732577, None)

reports.append(Report(604058840, ("CSC", 2, 3, 2, 27), "MEm32_27"))
reports[-1].posNum = 117609
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00185834, 0.00498379, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.250157, 0.140632, 0), \
                           ValErr(-4.15688e-05, 0.0015792, 0), \
                           ValErr(-0.0032297, 0.0073614, 0), \
                           ValErr(1.16679e-05, 3.85498e-05, 0), \
                           -172507, 117609, 117609, -nan)
reports[-1].sigmaresid = ValErr(1.049, 0.00216292, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00150177, None, -7.94728e-06, None, -0.00295318, None, -2.70238e-05, None, -0.00295318, None, -2.70238e-05, None, 0.00174314, None, -8.18022e-06, None, 0.00174314, None, -8.18022e-06, None, 1.04902, None, 0.00797154, None, 1.04902, None, 0.00797154, None)

reports.append(Report(604058856, ("CSC", 2, 3, 2, 29), "MEm32_29"))
reports[-1].posNum = 118583
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0103547, 0.00495883, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0424751, 0.140287, 0), \
                           ValErr(0.000197872, 0.0015844, 0), \
                           ValErr(0.000359415, 0.00734427, 0), \
                           ValErr(6.60885e-05, 3.86125e-05, 0), \
                           -173695, 118583, 118583, -nan)
reports[-1].sigmaresid = ValErr(1.04688, 0.00214967, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00977658, None, -2.52343e-05, None, -0.00777734, None, -3.40382e-05, None, -0.00777734, None, -3.40382e-05, None, -0.00848068, None, -4.7168e-05, None, -0.00848068, None, -4.7168e-05, None, 1.0469, None, 0.00754897, None, 1.0469, None, 0.00754897, None)

reports.append(Report(604058872, ("CSC", 2, 3, 2, 31), "MEm32_31"))
reports[-1].posNum = 114681
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00102989, 0.00518604, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.211392, 0.140631, 0), \
                           ValErr(0.000585847, 0.00158497, 0), \
                           ValErr(-0.00305025, 0.00749487, 0), \
                           ValErr(5.37798e-05, 3.97309e-05, 0), \
                           -167387, 114681, 114681, -nan)
reports[-1].sigmaresid = ValErr(1.04149, 0.00217445, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00332743, None, -1.77308e-06, None, 0.00167754, None, -1.36182e-05, None, 0.00167754, None, -1.36182e-05, None, -0.00173093, None, 4.41253e-06, None, -0.00173093, None, 4.41253e-06, None, 1.04151, None, 0.00753688, None, 1.04151, None, 0.00753688, None)

reports.append(Report(604058888, ("CSC", 2, 3, 2, 33), "MEm32_33"))
reports[-1].posNum = 123162
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00490637, 0.00478786, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.264027, 0.136307, 0), \
                           ValErr(-0.000738708, 0.00154601, 0), \
                           ValErr(0.000960986, 0.00708322, 0), \
                           ValErr(8.8642e-06, 3.75475e-05, 0), \
                           -180265, 123162, 123162, -nan)
reports[-1].sigmaresid = ValErr(1.04572, 0.00210698, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00521356, None, 1.50619e-05, None, 0.00556372, None, -9.02839e-07, None, 0.00556372, None, -9.02839e-07, None, 0.00647369, None, 2.17795e-06, None, 0.00647369, None, 2.17795e-06, None, 1.04573, None, 0.00773258, None, 1.04573, None, 0.00773258, None)

reports.append(Report(604058904, ("CSC", 2, 3, 2, 35), "MEm32_35"))
reports[-1].posNum = 111958
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0185336, 0.00515609, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.10228, 0.141807, 0), \
                           ValErr(-0.00128907, 0.00158399, 0), \
                           ValErr(-0.0220537, 0.00754184, 0), \
                           ValErr(-6.89903e-05, 3.90291e-05, 0), \
                           -161501, 111958, 111958, -nan)
reports[-1].sigmaresid = ValErr(1.02385, 0.00216369, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0111786, None, 3.64289e-05, None, 0.00605609, None, 1.66883e-05, None, 0.00605609, None, 1.66883e-05, None, 0.0149384, None, 3.5099e-05, None, 0.0149384, None, 3.5099e-05, None, 1.0239, None, 0.00767912, None, 1.0239, None, 0.00767912, None)

reports.append(Report(604058640, ("CSC", 2, 3, 2, 2), "MEm32_02"))
reports[-1].posNum = 121360
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00796295, 0.00496866, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.000896797, 0.144231, 0), \
                           ValErr(0.00203015, 0.00162068, 0), \
                           ValErr(-0.0135002, 0.00753896, 0), \
                           ValErr(-4.69504e-05, 3.86271e-05, 0), \
                           -179456, 121360, 121360, -nan)
reports[-1].sigmaresid = ValErr(1.06159, 0.00215477, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00164655, None, -2.01289e-05, None, 0.000524076, None, -3.25372e-05, None, 0.000524076, None, -3.25372e-05, None, 0.000101342, None, -2.28042e-05, None, 0.000101342, None, -2.28042e-05, None, 1.06161, None, 0.0073632, None, 1.06161, None, 0.0073632, None)

reports.append(Report(604058656, ("CSC", 2, 3, 2, 4), "MEm32_04"))
reports[-1].posNum = 118425
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00359033, 0.0050528, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.252524, 0.145579, 0), \
                           ValErr(0.000174942, 0.00164264, 0), \
                           ValErr(-0.00154963, 0.0076644, 0), \
                           ValErr(-9.2576e-06, 3.91099e-05, 0), \
                           -173809, 118425, 118425, -nan)
reports[-1].sigmaresid = ValErr(1.04994, 0.00215738, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00372403, None, 1.03779e-05, None, 0.00263755, None, -3.4884e-06, None, 0.00263755, None, -3.4884e-06, None, 0.000482716, None, -1.03612e-05, None, 0.000482716, None, -1.03612e-05, None, 1.04995, None, 0.0071889, None, 1.04995, None, 0.0071889, None)

reports.append(Report(604058672, ("CSC", 2, 3, 2, 6), "MEm32_06"))
reports[-1].posNum = 126747
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00733176, 0.00484973, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.241049, 0.141327, 0), \
                           ValErr(-0.00228647, 0.00160898, 0), \
                           ValErr(0.0190916, 0.00738365, 0), \
                           ValErr(-1.99196e-05, 3.80448e-05, 0), \
                           -188508, 126747, 126747, -nan)
reports[-1].sigmaresid = ValErr(1.07073, 0.00212665, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00329177, None, 5.98638e-06, None, 0.000138723, None, 3.47165e-05, None, 0.000138723, None, 3.47165e-05, None, 0.00396, None, 1.03153e-05, None, 0.00396, None, 1.03153e-05, None, 1.07078, None, 0.00741653, None, 1.07078, None, 0.00741653, None)

reports.append(Report(604058688, ("CSC", 2, 3, 2, 8), "MEm32_08"))
reports[-1].posNum = 115888
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00498556, 0.00513012, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.264792, 0.145127, 0), \
                           ValErr(0.00589678, 0.00164759, 0), \
                           ValErr(0.0170759, 0.00772173, 0), \
                           ValErr(-8.0734e-06, 3.95755e-05, 0), \
                           -168548, 115888, 115888, -nan)
reports[-1].sigmaresid = ValErr(1.0361, 0.00215213, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00237511, None, 2.94399e-06, None, 0.00182364, None, 2.65655e-06, None, 0.00182364, None, 2.65655e-06, None, -0.000606142, None, 1.05149e-05, None, -0.000606142, None, 1.05149e-05, None, 1.03619, None, 0.0071682, None, 1.03619, None, 0.0071682, None)

reports.append(Report(604058704, ("CSC", 2, 3, 2, 10), "MEm32_10"))
reports[-1].posNum = 128374
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0048513, 0.00482846, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0284071, 0.140348, 0), \
                           ValErr(0.00269787, 0.00160537, 0), \
                           ValErr(-0.00537869, 0.00733186, 0), \
                           ValErr(3.11058e-05, 3.78871e-05, 0), \
                           -191635, 128374, 128374, -nan)
reports[-1].sigmaresid = ValErr(1.07664, 0.0021248, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00146141, None, -1.04372e-05, None, -0.00618312, None, -5.23119e-05, None, -0.00618312, None, -5.23119e-05, None, -0.00448819, None, -3.14732e-05, None, -0.00448819, None, -3.14732e-05, None, 1.07666, None, 0.00739371, None, 1.07666, None, 0.00739371, None)

reports.append(Report(604058720, ("CSC", 2, 3, 2, 12), "MEm32_12"))
reports[-1].posNum = 117053
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0071376, 0.00503154, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.313494, 0.145808, 0), \
                           ValErr(0.00354292, 0.00165557, 0), \
                           ValErr(-0.00671527, 0.00768906, 0), \
                           ValErr(3.5301e-05, 3.9226e-05, 0), \
                           -170372, 117053, 117053, -nan)
reports[-1].sigmaresid = ValErr(1.03725, 0.00214376, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00681068, None, 7.07627e-06, None, -0.00823019, None, -3.73353e-05, None, -0.00823019, None, -3.73353e-05, None, -0.0123064, None, -4.70594e-05, None, -0.0123064, None, -4.70594e-05, None, 1.0373, None, 0.00752022, None, 1.0373, None, 0.00752022, None)

reports.append(Report(604058736, ("CSC", 2, 3, 2, 14), "MEm32_14"))
reports[-1].posNum = 126033
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00686892, 0.00484023, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.133721, 0.0733909, 0), \
                           ValErr(9.23555e-05, 0.00089698, 0), \
                           ValErr(0.0060838, 0.00729041, 0), \
                           ValErr(9.81406e-05, 3.65009e-05, 0), \
                           -186170, 126033, 126033, -nan)
reports[-1].sigmaresid = ValErr(1.05994, 0.00210219, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00110926, None, 2.3632e-05, None, -0.000897224, None, -3.6818e-06, None, -0.000897224, None, -3.6818e-06, None, -0.00545733, None, 1.25463e-05, None, -0.00545733, None, 1.25463e-05, None, 1.05997, None, 0.00721654, None, 1.05997, None, 0.00721654, None)

reports.append(Report(604058752, ("CSC", 2, 3, 2, 16), "MEm32_16"))
reports[-1].posNum = 118713
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00466373, 0.005035, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0750275, 0.146191, 0), \
                           ValErr(-0.000933097, 0.00165022, 0), \
                           ValErr(-0.00358506, 0.00768907, 0), \
                           ValErr(-3.52022e-05, 3.90335e-05, 0), \
                           -174443, 118713, 118713, -nan)
reports[-1].sigmaresid = ValErr(1.05181, 0.00215861, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00136937, None, 3.71865e-05, None, 0.00176784, None, 1.58342e-05, None, 0.00176784, None, 1.58342e-05, None, 0.00370269, None, 1.1668e-05, None, 0.00370269, None, 1.1668e-05, None, 1.05182, None, 0.00708433, None, 1.05182, None, 0.00708433, None)

reports.append(Report(604058768, ("CSC", 2, 3, 2, 18), "MEm32_18"))
reports[-1].posNum = 121046
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0154757, 0.00495656, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.00973606, 0.10023, 0), \
                           ValErr(0.00127147, 0.00112337, 0), \
                           ValErr(0.0118326, 0.00727552, 0), \
                           ValErr(5.79992e-05, 3.25187e-05, 0), \
                           -178517, 121046, 121046, -nan)
reports[-1].sigmaresid = ValErr(1.05744, 0.00214579, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00514843, None, -2.02363e-05, None, -0.00835167, None, -4.25261e-05, None, -0.00835167, None, -4.25261e-05, None, -0.00854091, None, -5.17286e-05, None, -0.00854091, None, -5.17286e-05, None, 1.05746, None, 0.00754988, None, 1.05746, None, 0.00754988, None)

reports.append(Report(604058784, ("CSC", 2, 3, 2, 20), "MEm32_20"))
reports[-1].posNum = 124114
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000858606, 0.0049331, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0697697, 0.098627, 0), \
                           ValErr(-0.00122675, 0.0014831, 0), \
                           ValErr(0.00977186, 0.00746072, 0), \
                           ValErr(-6.23866e-05, 3.85777e-05, 0), \
                           -183666, 124114, 124114, -nan)
reports[-1].sigmaresid = ValErr(1.06277, 0.00211539, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00243262, None, -1.18102e-05, None, 0.0010666, None, -9.69216e-06, None, 0.0010666, None, -9.69216e-06, None, 0.00128152, None, -6.37724e-06, None, 0.00128152, None, -6.37724e-06, None, 1.0628, None, 0.00755168, None, 1.0628, None, 0.00755168, None)

reports.append(Report(604058800, ("CSC", 2, 3, 2, 22), "MEm32_22"))
reports[-1].posNum = 117447
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.009023, 0.00508451, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0961764, 0.100732, 0), \
                           ValErr(0.00113836, 0.00158545, 0), \
                           ValErr(-0.00322895, 0.00772233, 0), \
                           ValErr(-8.42276e-05, 3.82568e-05, 0), \
                           -172591, 117447, 117447, -nan)
reports[-1].sigmaresid = ValErr(1.05188, 0.00210591, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000771082, None, 8.22338e-06, None, 0.0043783, None, 2.59201e-05, None, 0.0043783, None, 2.59201e-05, None, 0.00206786, None, -5.44746e-06, None, 0.00206786, None, -5.44746e-06, None, 1.05191, None, 0.00735266, None, 1.05191, None, 0.00735266, None)

reports.append(Report(604058816, ("CSC", 2, 3, 2, 24), "MEm32_24"))
reports[-1].posNum = 125647
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00958008, 0.00484102, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.188591, 0.140229, 0), \
                           ValErr(0.00108698, 0.00160054, 0), \
                           ValErr(0.0244354, 0.00733473, 0), \
                           ValErr(1.17231e-05, 3.79881e-05, 0), \
                           -185462, 125647, 125647, -nan)
reports[-1].sigmaresid = ValErr(1.05878, 0.0021121, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00439317, None, -2.52298e-05, None, 0.00125944, None, -3.08733e-07, None, 0.00125944, None, -3.08733e-07, None, -0.000621087, None, 3.37727e-06, None, -0.000621087, None, 3.37727e-06, None, 1.05884, None, 0.00732142, None, 1.05884, None, 0.00732142, None)

reports.append(Report(604058832, ("CSC", 2, 3, 2, 26), "MEm32_26"))
reports[-1].posNum = 116625
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000707742, 0.00512872, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.191506, 0.144688, 0), \
                           ValErr(-0.000494525, 0.00163714, 0), \
                           ValErr(-0.000219845, 0.00772084, 0), \
                           ValErr(-1.03212e-05, 3.95614e-05, 0), \
                           -169519, 116625, 116625, -nan)
reports[-1].sigmaresid = ValErr(1.03521, 0.00214346, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00229312, None, 2.81088e-05, None, 0.000197291, None, 2.26709e-05, None, 0.000197291, None, 2.26709e-05, None, 0.00182868, None, 1.85402e-05, None, 0.00182868, None, 1.85402e-05, None, 1.03521, None, 0.00712511, None, 1.03521, None, 0.00712511, None)

reports.append(Report(604058848, ("CSC", 2, 3, 2, 28), "MEm32_28"))
reports[-1].posNum = 128405
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00287801, 0.00486965, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0362084, 0.140623, 0), \
                           ValErr(-0.000540685, 0.0016067, 0), \
                           ValErr(-0.00733269, 0.00738376, 0), \
                           ValErr(-1.71289e-06, 3.80608e-05, 0), \
                           -191806, 128405, 128405, -nan)
reports[-1].sigmaresid = ValErr(1.07769, 0.00212661, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00322575, None, -2.0414e-05, None, -0.00611045, None, -3.16999e-06, None, -0.00611045, None, -3.16999e-06, None, -0.00105801, None, 7.73813e-06, None, -0.00105801, None, 7.73813e-06, None, 1.07769, None, 0.0073848, None, 1.07769, None, 0.0073848, None)

reports.append(Report(604058864, ("CSC", 2, 3, 2, 30), "MEm32_30"))
reports[-1].posNum = 116498
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00162783, 0.00507253, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.136183, 0.145586, 0), \
                           ValErr(0.000530223, 0.00163403, 0), \
                           ValErr(-0.00469321, 0.00769714, 0), \
                           ValErr(-5.5181e-05, 3.90709e-05, 0), \
                           -169496, 116498, 116498, -nan)
reports[-1].sigmaresid = ValErr(1.03665, 0.00214762, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00375063, None, 2.38924e-06, None, -0.0057915, None, -3.59867e-05, None, -0.0057915, None, -3.59867e-05, None, -0.0032236, None, -1.12705e-05, None, -0.0032236, None, -1.12705e-05, None, 1.03666, None, 0.00723364, None, 1.03666, None, 0.00723364, None)

reports.append(Report(604058880, ("CSC", 2, 3, 2, 32), "MEm32_32"))
reports[-1].posNum = 127445
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00412087, 0.0048202, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.32101, 0.140002, 0), \
                           ValErr(-0.00242703, 0.00159344, 0), \
                           ValErr(0.000334444, 0.00732339, 0), \
                           ValErr(2.13376e-05, 3.78193e-05, 0), \
                           -188759, 127445, 127445, -nan)
reports[-1].sigmaresid = ValErr(1.06414, 0.00210776, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00435281, None, 2.38862e-05, None, 0.00503854, None, 1.25004e-05, None, 0.00503854, None, 1.25004e-05, None, 0.00563204, None, 5.08338e-06, None, 0.00563204, None, 5.08338e-06, None, 1.06417, None, 0.00730863, None, 1.06417, None, 0.00730863, None)

reports.append(Report(604058896, ("CSC", 2, 3, 2, 34), "MEm32_34"))
reports[-1].posNum = 120085
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00332622, 0.00500779, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.125768, 0.146376, 0), \
                           ValErr(0.00477505, 0.00167744, 0), \
                           ValErr(0.00607049, 0.0076727, 0), \
                           ValErr(1.48105e-05, 3.93018e-05, 0), \
                           -177012, 120085, 120085, -nan)
reports[-1].sigmaresid = ValErr(1.05666, 0.00215615, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00490056, None, -9.73645e-06, None, -0.00020012, None, -3.45762e-05, None, -0.00020012, None, -3.45762e-05, None, 0.00088142, None, -2.75193e-05, None, 0.00088142, None, -2.75193e-05, None, 1.0567, None, 0.00743659, None, 1.0567, None, 0.00743659, None)

reports.append(Report(604058912, ("CSC", 2, 3, 2, 36), "MEm32_36"))
reports[-1].posNum = 124546
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00759393, 0.0048836, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.134165, 0.14165, 0), \
                           ValErr(0.000381057, 0.001612, 0), \
                           ValErr(-0.00642188, 0.00743095, 0), \
                           ValErr(-1.90863e-06, 3.82411e-05, 0), \
                           -183997, 124546, 124546, -nan)
reports[-1].sigmaresid = ValErr(1.06014, 0.00212416, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0036396, None, 2.57731e-06, None, 0.00476108, None, -1.45621e-05, None, 0.00476108, None, -1.45621e-05, None, 0.00937995, None, 3.6646e-05, None, 0.00937995, None, 3.6646e-05, None, 1.06015, None, 0.00728033, None, 1.06015, None, 0.00728033, None)

reports.append(Report(604062216, ("CSC", 2, 4, 1, 1), "MEm41_01"))
reports[-1].posNum = 281707
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(4.6186e-05, 0.00163725, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0375273, 0.0475078, 0), \
                           ValErr(0.00113375, 0.00121489, 0), \
                           ValErr(-0.00420671, 0.00207117, 0), \
                           ValErr(-2.59763e-06, 3.02831e-05, 0), \
                           -248706, 281707, 281707, -nan)
reports[-1].sigmaresid = ValErr(0.585033, 0.00077941, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0023581, None, -2.89094e-06, None, -0.00237265, None, -1.27838e-05, None, -0.00237265, None, -1.27838e-05, None, -0.000891851, None, -2.45784e-05, None, -0.000891851, None, -2.45784e-05, None, 0.585041, None, 0.00577578, None, 0.585041, None, 0.00577578, None)

reports.append(Report(604062232, ("CSC", 2, 4, 1, 3), "MEm41_03"))
reports[-1].posNum = 282887
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000398292, 0.00163835, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0216396, 0.0474219, 0), \
                           ValErr(2.12392e-05, 0.00121256, 0), \
                           ValErr(0.000935003, 0.00206448, 0), \
                           ValErr(3.84264e-05, 3.03232e-05, 0), \
                           -250312, 282887, 282887, -nan)
reports[-1].sigmaresid = ValErr(0.5862, 0.000779334, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000366512, None, -2.50857e-06, None, 0.000224951, None, -2.34561e-05, None, 0.000224951, None, -2.34561e-05, None, -0.0021492, None, -4.31898e-05, None, -0.0021492, None, -4.31898e-05, None, 0.586203, None, 0.00580743, None, 0.586203, None, 0.00580743, None)

reports.append(Report(604062248, ("CSC", 2, 4, 1, 5), "MEm41_05"))
reports[-1].posNum = 281114
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000266019, 0.00163689, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.000827403, 0.0476107, 0), \
                           ValErr(0.000287756, 0.00121807, 0), \
                           ValErr(0.00199381, 0.00207543, 0), \
                           ValErr(1.77669e-05, 3.03268e-05, 0), \
                           -248123, 281114, 281114, -nan)
reports[-1].sigmaresid = ValErr(0.584912, 0.000780071, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000247922, None, -1.55548e-07, None, 0.00144661, None, -3.0173e-05, None, 0.00144661, None, -3.0173e-05, None, -0.00149103, None, -4.42678e-05, None, -0.00149103, None, -4.42678e-05, None, 0.584912, None, 0.00580925, None, 0.584912, None, 0.00580925, None)

reports.append(Report(604062264, ("CSC", 2, 4, 1, 7), "MEm41_07"))
reports[-1].posNum = 280032
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00028687, 0.00163895, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0147503, 0.0474063, 0), \
                           ValErr(-0.00109728, 0.00121309, 0), \
                           ValErr(0.00098184, 0.00207338, 0), \
                           ValErr(-3.01765e-05, 3.0304e-05, 0), \
                           -246134, 280032, 280032, -nan)
reports[-1].sigmaresid = ValErr(0.582754, 0.000778692, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00207507, None, -9.5231e-06, None, 0.000775129, None, -2.48251e-05, None, 0.000775129, None, -2.48251e-05, None, -0.000692529, None, -7.96289e-06, None, -0.000692529, None, -7.96289e-06, None, 0.582757, None, 0.00578988, None, 0.582757, None, 0.00578988, None)

reports.append(Report(604062280, ("CSC", 2, 4, 1, 9), "MEm41_09"))
reports[-1].posNum = 282385
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00129017, 0.00162962, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00894123, 0.0472612, 0), \
                           ValErr(-0.00160911, 0.00120969, 0), \
                           ValErr(-0.000381166, 0.00206327, 0), \
                           ValErr(2.19724e-05, 3.01636e-05, 0), \
                           -248089, 282385, 282385, -nan)
reports[-1].sigmaresid = ValErr(0.58252, 0.00077513, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00234435, None, 1.27285e-05, None, 0.00112701, None, -2.57406e-07, None, 0.00112701, None, -2.57406e-07, None, -0.000785743, None, -7.27155e-06, None, -0.000785743, None, -7.27155e-06, None, 0.582523, None, 0.00573725, None, 0.582523, None, 0.00573725, None)

reports.append(Report(604062296, ("CSC", 2, 4, 1, 11), "MEm41_11"))
reports[-1].posNum = 282319
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00252974, 0.00162309, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.029763, 0.0473207, 0), \
                           ValErr(0.000226546, 0.00120917, 0), \
                           ValErr(0.000991077, 0.00205478, 0), \
                           ValErr(6.46354e-05, 3.00884e-05, 0), \
                           -247850, 282319, 282319, -nan)
reports[-1].sigmaresid = ValErr(0.582148, 0.000774727, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0025276, None, -4.33479e-07, None, -0.00182775, None, -2.09335e-05, None, -0.00182775, None, -2.09335e-05, None, -0.00132038, None, -1.64101e-05, None, -0.00132038, None, -1.64101e-05, None, 0.582152, None, 0.0056716, None, 0.582152, None, 0.0056716, None)

reports.append(Report(604062312, ("CSC", 2, 4, 1, 13), "MEm41_13"))
reports[-1].posNum = 284491
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00289894, 0.00162009, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0167816, 0.0469286, 0), \
                           ValErr(0.000170707, 0.00120182, 0), \
                           ValErr(-0.00300542, 0.00204588, 0), \
                           ValErr(-3.15449e-05, 2.99614e-05, 0), \
                           -249467, 284491, 284491, -nan)
reports[-1].sigmaresid = ValErr(0.581555, 0.000770976, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000792103, None, -1.8315e-08, None, 0.00109774, None, -1.4834e-05, None, 0.00109774, None, -1.4834e-05, None, 0.00086469, None, -7.66095e-06, None, 0.00086469, None, -7.66095e-06, None, 0.581558, None, 0.0059068, None, 0.581558, None, 0.0059068, None)

reports.append(Report(604062328, ("CSC", 2, 4, 1, 15), "MEm41_15"))
reports[-1].posNum = 284558
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000641128, 0.00162157, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0316584, 0.0470591, 0), \
                           ValErr(-0.000304752, 0.00120364, 0), \
                           ValErr(0.000871183, 0.00205049, 0), \
                           ValErr(1.3407e-05, 3.00276e-05, 0), \
                           -250029, 284558, 284558, -nan)
reports[-1].sigmaresid = ValErr(0.582583, 0.000772248, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00085047, None, -3.28299e-06, None, 0.00117379, None, -1.43939e-05, None, 0.00117379, None, -1.43939e-05, None, -0.000252829, None, -3.62803e-05, None, -0.000252829, None, -3.62803e-05, None, 0.582584, None, 0.00561865, None, 0.582584, None, 0.00561865, None)

reports.append(Report(604062344, ("CSC", 2, 4, 1, 17), "MEm41_17"))
reports[-1].posNum = 283113
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00264126, 0.00162469, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00101701, 0.0471186, 0), \
                           ValErr(0.000806702, 0.0012054, 0), \
                           ValErr(0.00499661, 0.0020563, 0), \
                           ValErr(4.58006e-05, 3.00292e-05, 0), \
                           -248340, 283113, 283113, -nan)
reports[-1].sigmaresid = ValErr(0.581722, 0.000773072, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000268739, None, 7.63895e-07, None, 0.00033097, None, -1.58722e-05, None, 0.00033097, None, -1.58722e-05, None, 0.000329722, None, -1.92912e-05, None, 0.000329722, None, -1.92912e-05, None, 0.58173, None, 0.00550916, None, 0.58173, None, 0.00550916, None)

reports.append(Report(604062224, ("CSC", 2, 4, 1, 2), "MEm41_02"))
reports[-1].posNum = 285761
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00264776, 0.00167069, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0512958, 0.0495186, 0), \
                           ValErr(-0.00137057, 0.00127078, 0), \
                           ValErr(0.000540176, 0.0021619, 0), \
                           ValErr(2.23401e-05, 3.09606e-05, 0), \
                           -259683, 285761, 285761, -nan)
reports[-1].sigmaresid = ValErr(0.600377, 0.00079416, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00340958, None, -7.43211e-06, None, -0.00229014, None, 6.72753e-06, None, -0.00229014, None, 6.72753e-06, None, -0.00423524, None, 4.92578e-06, None, -0.00423524, None, 4.92578e-06, None, 0.600381, None, 0.00554392, None, 0.600381, None, 0.00554392, None)

reports.append(Report(604062240, ("CSC", 2, 4, 1, 4), "MEm41_04"))
reports[-1].posNum = 284696
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000883793, 0.00166432, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.107807, 0.0493961, 0), \
                           ValErr(-0.00144848, 0.00126463, 0), \
                           ValErr(-0.0019108, 0.00215428, 0), \
                           ValErr(-4.15477e-05, 3.08166e-05, 0), \
                           -257303, 284696, 284696, -nan)
reports[-1].sigmaresid = ValErr(0.597408, 0.00079171, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000717042, None, -1.34294e-05, None, -0.000296977, None, -1.5213e-05, None, -0.000296977, None, -1.5213e-05, None, -0.00131122, None, -3.38174e-05, None, -0.00131122, None, -3.38174e-05, None, 0.597415, None, 0.00566532, None, 0.597415, None, 0.00566532, None)

reports.append(Report(604062256, ("CSC", 2, 4, 1, 6), "MEm41_06"))
reports[-1].posNum = 283926
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000482109, 0.00167119, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.0247126, 0.0496114, 0), \
                           ValErr(0.00114025, 0.00126659, 0), \
                           ValErr(0.00147714, 0.00216283, 0), \
                           ValErr(-3.28588e-05, 3.09272e-05, 0), \
                           -257344, 283926, 283926, -nan)
reports[-1].sigmaresid = ValErr(0.598961, 0.000794843, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000228015, None, -5.27898e-06, None, 0.000270956, None, -3.30675e-06, None, 0.000270956, None, -3.30675e-06, None, 0.000641215, None, 3.87777e-06, None, 0.000641215, None, 3.87777e-06, None, 0.598964, None, 0.0056113, None, 0.598964, None, 0.0056113, None)

reports.append(Report(604062272, ("CSC", 2, 4, 1, 8), "MEm41_08"))
reports[-1].posNum = 284043
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00177587, 0.00167271, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.05158, 0.043717, 0), \
                           ValErr(-0.00201531, 0.00106681, 0), \
                           ValErr(0.00267623, 0.00217306, 0), \
                           ValErr(6.0771e-05, 2.70489e-05, 0), \
                           -259013, 284043, 284043, -nan)
reports[-1].sigmaresid = ValErr(0.602263, 0.000794278, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000317661, None, -8.52381e-06, None, -0.000135948, None, -2.73115e-06, None, -0.000135948, None, -2.73115e-06, None, 0.00036541, None, -1.30681e-05, None, 0.00036541, None, -1.30681e-05, None, 0.602273, None, 0.00558746, None, 0.602273, None, 0.00558746, None)

reports.append(Report(604062288, ("CSC", 2, 4, 1, 10), "MEm41_10"))
reports[-1].posNum = 283900
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000535347, 0.00168692, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0441585, 0.0500161, 0), \
                           ValErr(-4.63269e-05, 0.00128047, 0), \
                           ValErr(0.000117573, 0.00218459, 0), \
                           ValErr(3.41973e-05, 3.11624e-05, 0), \
                           -259928, 283900, 283900, -nan)
reports[-1].sigmaresid = ValErr(0.604486, 0.000802212, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000240544, None, 6.84493e-06, None, -0.000387514, None, -3.09661e-06, None, -0.000387514, None, -3.09661e-06, None, -0.00106978, None, -1.37559e-05, None, -0.00106978, None, -1.37559e-05, None, 0.604488, None, 0.00631793, None, 0.604488, None, 0.00631793, None)

reports.append(Report(604062304, ("CSC", 2, 4, 1, 12), "MEm41_12"))
reports[-1].posNum = 284371
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00122412, 0.00167294, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.00765469, 0.0496873, 0), \
                           ValErr(-0.000823448, 0.00127285, 0), \
                           ValErr(-0.00138806, 0.00216469, 0), \
                           ValErr(1.42571e-05, 3.09811e-05, 0), \
                           -258583, 284371, 284371, -nan)
reports[-1].sigmaresid = ValErr(0.600721, 0.000796555, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000449424, None, -1.62614e-06, None, 0.000477902, None, -8.0511e-06, None, 0.000477902, None, -8.0511e-06, None, 0.00201464, None, 7.9992e-06, None, 0.00201464, None, 7.9992e-06, None, 0.600723, None, 0.00555575, None, 0.600723, None, 0.00555575, None)

reports.append(Report(604062320, ("CSC", 2, 4, 1, 14), "MEm41_14"))
reports[-1].posNum = 285631
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00229635, 0.0016731, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.066806, 0.0496852, 0), \
                           ValErr(0.00143873, 0.00127264, 0), \
                           ValErr(0.000367009, 0.00216208, 0), \
                           ValErr(-2.13684e-05, 3.10184e-05, 0), \
                           -260396, 285631, 285631, -nan)
reports[-1].sigmaresid = ValErr(0.602128, 0.000796656, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00241762, None, -6.76833e-06, None, 0.00245545, None, -1.69043e-05, None, 0.00245545, None, -1.69043e-05, None, 0.00303728, None, -2.48833e-05, None, 0.00303728, None, -2.48833e-05, None, 0.602132, None, 0.00556787, None, 0.602132, None, 0.00556787, None)

reports.append(Report(604062336, ("CSC", 2, 4, 1, 16), "MEm41_16"))
reports[-1].posNum = 284957
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00204035, 0.00162978, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0943134, 0.0430093, 0), \
                           ValErr(-0.00133598, 0.0012456, 0), \
                           ValErr(-0.00323045, 0.00212502, 0), \
                           ValErr(4.3499e-06, 2.68697e-05, 0), \
                           -258832, 284957, 284957, -nan)
reports[-1].sigmaresid = ValErr(0.600125, 0.000782249, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000264153, None, 1.04981e-05, None, 0.000241212, None, 8.80897e-06, None, 0.000241212, None, 8.80897e-06, None, -0.0015629, None, 1.82747e-05, None, -0.0015629, None, 1.82747e-05, None, 0.600131, None, 0.00576103, None, 0.600131, None, 0.00576103, None)

reports.append(Report(604062352, ("CSC", 2, 4, 1, 18), "MEm41_18"))
reports[-1].posNum = 285596
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00167371, 0.00166861, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(-0.00109621, 0.0495888, 0), \
                           ValErr(0.00130063, 0.00126979, 0), \
                           ValErr(0.000467875, 0.00216025, 0), \
                           ValErr(-5.82209e-06, 3.09159e-05, 0), \
                           -259551, 285596, 285596, -nan)
reports[-1].sigmaresid = ValErr(0.600416, 0.000794442, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000937058, None, -1.87143e-05, None, -0.00142589, None, -1.82046e-05, None, -0.00142589, None, -1.82046e-05, None, 0.000253096, None, -1.69781e-05, None, 0.000253096, None, -1.69781e-05, None, 0.600417, None, 0.00560514, None, 0.600417, None, 0.00560514, None)

reports.append(Report(604062728, ("CSC", 2, 4, 2, 1), "MEm42_01"))
reports[-1].posNum = 129917
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00732075, 0.005002, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.277895, 0.133129, 0), \
                           ValErr(-0.00229779, 0.00130662, 0), \
                           ValErr(-0.00667185, 0.00779947, 0), \
                           ValErr(-2.26113e-05, 2.83431e-05, 0), \
                           -198155, 129917, 129917, -nan)
reports[-1].sigmaresid = ValErr(1.11216, 0.00214778, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00584222, None, -1.78431e-05, None, 0.00387256, None, -3.86914e-05, None, 0.00387256, None, -3.86914e-05, None, 0.00702678, None, -4.41578e-05, None, 0.00702678, None, -4.41578e-05, None, 1.11219, None, 0.00752463, None, 1.11219, None, 0.00752463, None)

reports.append(Report(604062744, ("CSC", 2, 4, 2, 3), "MEm42_03"))
reports[-1].posNum = 122873
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00546871, 0.00510746, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.404103, 0.156084, 0), \
                           ValErr(-0.00428691, 0.00180911, 0), \
                           ValErr(-0.00476985, 0.00827829, 0), \
                           ValErr(8.43901e-05, 4.02558e-05, 0), \
                           -183687, 122873, 122873, -nan)
reports[-1].sigmaresid = ValErr(1.07896, 0.00217652, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000796928, None, -6.43075e-05, None, -0.00422002, None, -7.73289e-05, None, -0.00422002, None, -7.73289e-05, None, -0.00341925, None, -7.63749e-05, None, -0.00341925, None, -7.63749e-05, None, 1.07904, None, 0.00784535, None, 1.07904, None, 0.00784535, None)

reports.append(Report(604062760, ("CSC", 2, 4, 2, 5), "MEm42_05"))
reports[-1].posNum = 128882
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00654615, 0.00494006, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.367359, 0.154268, 0), \
                           ValErr(-0.000216817, 0.00178872, 0), \
                           ValErr(0.00515755, 0.00805242, 0), \
                           ValErr(8.38857e-05, 3.93024e-05, 0), \
                           -195303, 128882, 128882, -nan)
reports[-1].sigmaresid = ValErr(1.10122, 0.00216901, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0010603, None, -1.67772e-05, None, -0.00170162, None, -2.98849e-05, None, -0.00170162, None, -2.98849e-05, None, -0.00189153, None, -1.90757e-05, None, -0.00189153, None, -1.90757e-05, None, 1.10127, None, 0.00760018, None, 1.10127, None, 0.00760018, None)

reports.append(Report(604062776, ("CSC", 2, 4, 2, 7), "MEm42_07"))
reports[-1].posNum = 122538
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00944607, 0.00519843, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.168352, 0.157743, 0), \
                           ValErr(0.000442328, 0.00182582, 0), \
                           ValErr(-0.00797252, 0.00836481, 0), \
                           ValErr(-1.55611e-05, 4.09246e-05, 0), \
                           -184821, 122538, 122538, -nan)
reports[-1].sigmaresid = ValErr(1.09344, 0.00220875, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00675758, None, 1.9061e-05, None, 0.00572583, None, 2.07536e-05, None, 0.00572583, None, 2.07536e-05, None, 0.00622198, None, 2.91658e-05, None, 0.00622198, None, 2.91658e-05, None, 1.09345, None, 0.00753913, None, 1.09345, None, 0.00753913, None)

reports.append(Report(604062792, ("CSC", 2, 4, 2, 9), "MEm42_09"))
reports[-1].posNum = 126030
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.000833132, 0.00504358, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.219559, 0.157774, 0), \
                           ValErr(-0.00155955, 0.00181927, 0), \
                           ValErr(-0.00336713, 0.00823481, 0), \
                           ValErr(5.09147e-05, 3.99256e-05, 0), \
                           -191659, 126030, 126030, -nan)
reports[-1].sigmaresid = ValErr(1.10717, 0.00220491, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000705693, None, -3.76669e-05, None, 0.00121885, None, -5.14616e-05, None, 0.00121885, None, -5.14616e-05, None, -0.00359505, None, -6.10745e-05, None, -0.00359505, None, -6.10745e-05, None, 1.10719, None, 0.00766012, None, 1.10719, None, 0.00766012, None)

reports.append(Report(604062808, ("CSC", 2, 4, 2, 11), "MEm42_11"))
reports[-1].posNum = 124196
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00124495, 0.00508522, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.435565, 0.15844, 0), \
                           ValErr(0.000486467, 0.00183302, 0), \
                           ValErr(-0.00824018, 0.00826354, 0), \
                           ValErr(5.36229e-05, 4.03307e-05, 0), \
                           -188333, 124196, 124196, -nan)
reports[-1].sigmaresid = ValErr(1.10238, 0.00221246, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000209307, None, -2.03615e-05, None, -0.00247899, None, -6.01468e-05, None, -0.00247899, None, -6.01468e-05, None, -0.0019121, None, -4.4682e-05, None, -0.0019121, None, -4.4682e-05, None, 1.10244, None, 0.0073399, None, 1.10244, None, 0.0073399, None)

reports.append(Report(604062824, ("CSC", 2, 4, 2, 13), "MEm42_13"))
reports[-1].posNum = 121479
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00962303, 0.00525502, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.673368, 0.158889, 0), \
                           ValErr(-0.00121232, 0.00183362, 0), \
                           ValErr(0.0082679, 0.0084283, 0), \
                           ValErr(5.81155e-05, 4.1286e-05, 0), \
                           -183117, 121479, 121479, -nan)
reports[-1].sigmaresid = ValErr(1.09249, 0.00221643, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00852921, None, -7.66511e-05, None, -0.00437427, None, -0.000139101, None, -0.00437427, None, -0.000139101, None, -0.00865992, None, -0.000119886, None, -0.00865992, None, -0.000119886, None, 1.09259, None, 0.00737914, None, 1.09259, None, 0.00737914, None)

reports.append(Report(604062840, ("CSC", 2, 4, 2, 15), "MEm42_15"))
reports[-1].posNum = 129090
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00940395, 0.00492712, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.572766, 0.121854, 0), \
                           ValErr(0.00286171, 0.00154324, 0), \
                           ValErr(0.00773217, 0.00798583, 0), \
                           ValErr(-3.7767e-05, 3.74715e-05, 0), \
                           -195227, 129090, 129090, -nan)
reports[-1].sigmaresid = ValErr(1.0979, 0.00215266, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.0149042, None, 4.42069e-06, None, 0.0112873, None, -2.18768e-05, None, 0.0112873, None, -2.18768e-05, None, 0.0139991, None, 9.34516e-06, None, 0.0139991, None, 9.34516e-06, None, 1.09798, None, 0.00758957, None, 1.09798, None, 0.00758957, None)

reports.append(Report(604062856, ("CSC", 2, 4, 2, 17), "MEm42_17"))
reports[-1].posNum = 122641
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00235462, 0.00514092, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.596476, 0.156724, 0), \
                           ValErr(0.00183582, 0.00181426, 0), \
                           ValErr(-0.00433683, 0.00831756, 0), \
                           ValErr(-7.59413e-05, 4.06286e-05, 0), \
                           -183317, 122641, 122641, -nan)
reports[-1].sigmaresid = ValErr(1.07875, 0.00217816, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0028707, None, -4.83238e-05, None, -0.00224278, None, -4.98848e-05, None, -0.00224278, None, -4.98848e-05, None, -0.00213331, None, -6.63523e-05, None, -0.00213331, None, -6.63523e-05, None, 1.07883, None, 0.00745327, None, 1.07883, None, 0.00745327, None)

reports.append(Report(604062872, ("CSC", 2, 4, 2, 19), "MEm42_19"))
reports[-1].posNum = 130050
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00039891, 0.00498162, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.328084, 0.153927, 0), \
                           ValErr(-0.00187058, 0.00178182, 0), \
                           ValErr(0.000251283, 0.00809545, 0), \
                           ValErr(2.44328e-05, 3.95028e-05, 0), \
                           -198081, 130050, 130050, -nan)
reports[-1].sigmaresid = ValErr(1.10979, 0.00217607, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.000392667, None, 7.24468e-06, None, 0.00129228, None, 8.51255e-08, None, 0.00129228, None, 8.51255e-08, None, -0.00294512, None, -6.13621e-06, None, -0.00294512, None, -6.13621e-06, None, 1.10982, None, 0.00759258, None, 1.10982, None, 0.00759258, None)

reports.append(Report(604062888, ("CSC", 2, 4, 2, 21), "MEm42_21"))
reports[-1].posNum = 120936
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00432541, 0.00512802, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.274873, 0.11321, 0), \
                           ValErr(-0.00258909, 0.0015241, 0), \
                           ValErr(0.00515818, 0.00834632, 0), \
                           ValErr(-2.28421e-05, 4.02038e-05, 0), \
                           -180249, 120936, 120936, -nan)
reports[-1].sigmaresid = ValErr(1.07413, 0.00216894, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00308066, None, 7.13604e-05, None, 0.00544068, None, 4.49045e-05, None, 0.00544068, None, 4.49045e-05, None, 0.00462002, None, 5.35886e-05, None, 0.00462002, None, 5.35886e-05, None, 1.07416, None, 0.00739904, None, 1.07416, None, 0.00739904, None)

reports.append(Report(604062904, ("CSC", 2, 4, 2, 23), "MEm42_23"))
reports[-1].posNum = 130307
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000744388, 0.0049451, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.047486, 0.153207, 0), \
                           ValErr(-0.00135168, 0.00178084, 0), \
                           ValErr(-0.000786501, 0.00803191, 0), \
                           ValErr(-2.74528e-05, 3.9261e-05, 0), \
                           -197516, 130307, 130307, -nan)
reports[-1].sigmaresid = ValErr(1.10168, 0.00215802, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00319647, None, -6.15087e-05, None, -0.00197129, None, -7.96777e-05, None, -0.00197129, None, -7.96777e-05, None, 0.000700383, None, -6.0575e-05, None, 0.000700383, None, -6.0575e-05, None, 1.10168, None, 0.00717117, None, 1.10168, None, 0.00717117, None)

reports.append(Report(604062920, ("CSC", 2, 4, 2, 25), "MEm42_25"))
reports[-1].posNum = 125926
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00282522, 0.00506673, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.540441, 0.155014, 0), \
                           ValErr(-0.00139606, 0.00179764, 0), \
                           ValErr(-0.00914284, 0.0081772, 0), \
                           ValErr(-3.47975e-05, 3.99651e-05, 0), \
                           -189343, 125926, 125926, -nan)
reports[-1].sigmaresid = ValErr(1.08835, 0.00216869, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0048098, None, 1.97664e-05, None, -0.00213805, None, -8.29322e-06, None, -0.00213805, None, -8.29322e-06, None, -0.000130317, None, 2.13092e-05, None, -0.000130317, None, 2.13092e-05, None, 1.08842, None, 0.00715419, None, 1.08842, None, 0.00715419, None)

reports.append(Report(604062936, ("CSC", 2, 4, 2, 27), "MEm42_27"))
reports[-1].posNum = 128278
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00248894, 0.00498788, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.505252, 0.154893, 0), \
                           ValErr(-0.00329124, 0.00178182, 0), \
                           ValErr(-0.000730375, 0.00812462, 0), \
                           ValErr(8.55392e-06, 3.92601e-05, 0), \
                           -194338, 128278, 128278, -nan)
reports[-1].sigmaresid = ValErr(1.1008, 0.00217329, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00338464, None, -5.60917e-05, None, 0.00237043, None, -9.30953e-05, None, 0.00237043, None, -9.30953e-05, None, 0.000580756, None, -8.40329e-05, None, 0.000580756, None, -8.40329e-05, None, 1.10087, None, 0.00699924, None, 1.10087, None, 0.00699924, None)

reports.append(Report(604062952, ("CSC", 2, 4, 2, 29), "MEm42_29"))
reports[-1].posNum = 127930
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00375135, 0.00499143, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.312841, 0.154812, 0), \
                           ValErr(-0.00419748, 0.0017848, 0), \
                           ValErr(-0.0162038, 0.00810844, 0), \
                           ValErr(4.14804e-05, 3.9546e-05, 0), \
                           -193486, 127930, 127930, -nan)
reports[-1].sigmaresid = ValErr(1.09801, 0.00217072, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000802681, None, 3.79603e-05, None, -0.00121375, None, -4.118e-05, None, -0.00121375, None, -4.118e-05, None, -0.00163095, None, -2.7569e-05, None, -0.00163095, None, -2.7569e-05, None, 1.09808, None, 0.00728741, None, 1.09808, None, 0.00728741, None)

reports.append(Report(604062968, ("CSC", 2, 4, 2, 31), "MEm42_31"))
reports[-1].posNum = 125191
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000483799, 0.00516909, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.273792, 0.156527, 0), \
                           ValErr(-0.0014238, 0.00181914, 0), \
                           ValErr(-0.00762666, 0.00830547, 0), \
                           ValErr(3.73452e-05, 4.0829e-05, 0), \
                           -189326, 125191, 125191, -nan)
reports[-1].sigmaresid = ValErr(1.09786, 0.00219404, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00115931, None, -1.66044e-06, None, -0.00216271, None, -3.01782e-05, None, -0.00216271, None, -3.01782e-05, None, -0.00476012, None, -1.98131e-05, None, -0.00476012, None, -1.98131e-05, None, 1.09788, None, 0.00720781, None, 1.09788, None, 0.00720781, None)

reports.append(Report(604062984, ("CSC", 2, 4, 2, 33), "MEm42_33"))
reports[-1].posNum = 129872
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00617697, 0.0048952, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.331515, 0.152915, 0), \
                           ValErr(-0.00214997, 0.00176145, 0), \
                           ValErr(-0.00295816, 0.00797202, 0), \
                           ValErr(1.27124e-06, 3.88612e-05, 0), \
                           -196219, 129872, 129872, -nan)
reports[-1].sigmaresid = ValErr(1.09628, 0.00215105, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00475807, None, -3.08583e-05, None, 0.00507118, None, -3.88345e-05, None, 0.00507118, None, -3.88345e-05, None, 0.0058332, None, -2.08201e-05, None, 0.0058332, None, -2.08201e-05, None, 1.09631, None, 0.00760772, None, 1.09631, None, 0.00760772, None)

reports.append(Report(604063000, ("CSC", 2, 4, 2, 35), "MEm42_35"))
reports[-1].posNum = 121042
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00714817, 0.00526516, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0988476, 0.157211, 0), \
                           ValErr(-0.00266371, 0.00181447, 0), \
                           ValErr(-0.00466356, 0.00842006, 0), \
                           ValErr(-4.3791e-05, 4.11934e-05, 0), \
                           -180498, 121042, 121042, -nan)
reports[-1].sigmaresid = ValErr(1.07494, 0.00218474, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00848611, None, -6.67935e-05, None, 0.0035408, None, -6.28094e-05, None, 0.0035408, None, -6.28094e-05, None, 0.0065806, None, -4.15114e-05, None, 0.0065806, None, -4.15114e-05, None, 1.07495, None, 0.00724905, None, 1.07495, None, 0.00724905, None)

reports.append(Report(604062736, ("CSC", 2, 4, 2, 2), "MEm42_02"))
reports[-1].posNum = 126448
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00692214, 0.00514421, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.405986, 0.163852, 0), \
                           ValErr(0.000252003, 0.00192105, 0), \
                           ValErr(-0.0153048, 0.00858586, 0), \
                           ValErr(-2.32506e-05, 4.10785e-05, 0), \
                           -193561, 126448, 126448, -nan)
reports[-1].sigmaresid = ValErr(1.11831, 0.00222377, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00321523, None, 8.22696e-06, None, 0.00030534, None, 9.5971e-06, None, 0.00030534, None, 9.5971e-06, None, 0.00137483, None, 3.71521e-05, None, 0.00137483, None, 3.71521e-05, None, 1.11835, None, 0.00722235, None, 1.11835, None, 0.00722235, None)

reports.append(Report(604062752, ("CSC", 2, 4, 2, 4), "MEm42_04"))
reports[-1].posNum = 125771
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00289484, 0.00518966, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0333779, 0.162884, 0), \
                           ValErr(-0.00150877, 0.00190472, 0), \
                           ValErr(-0.0103306, 0.00859862, 0), \
                           ValErr(-5.78848e-05, 4.13237e-05, 0), \
                           -191729, 125771, 125771, -nan)
reports[-1].sigmaresid = ValErr(1.11125, 0.00221569, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00297852, None, -1.35933e-05, None, -0.00324584, None, 5.91156e-06, None, -0.00324584, None, 5.91156e-06, None, -0.00142875, None, 3.95686e-05, None, -0.00142875, None, 3.95686e-05, None, 1.11127, None, 0.00717242, None, 1.11127, None, 0.00717242, None)

reports.append(Report(604062768, ("CSC", 2, 4, 2, 6), "MEm42_06"))
reports[-1].posNum = 131320
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00792078, 0.00499, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.290295, 0.0764177, 0), \
                           ValErr(-0.00339609, 0.000974625, 0), \
                           ValErr(0.0174102, 0.00830561, 0), \
                           ValErr(4.08713e-05, 3.91834e-05, 0), \
                           -201973, 131320, 131320, -nan)
reports[-1].sigmaresid = ValErr(1.12646, 0.00215406, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0016919, None, 5.60852e-05, None, 0.000220141, None, 4.32289e-05, None, 0.000220141, None, 4.32289e-05, None, 0.00566418, None, 5.97601e-05, None, 0.00566418, None, 5.97601e-05, None, 1.12651, None, 0.00725279, None, 1.12651, None, 0.00725279, None)

reports.append(Report(604062784, ("CSC", 2, 4, 2, 8), "MEm42_08"))
reports[-1].posNum = 123345
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00953188, 0.00526405, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.388073, 0.163531, 0), \
                           ValErr(0.00134121, 0.00191427, 0), \
                           ValErr(0.0184702, 0.00869425, 0), \
                           ValErr(5.3816e-05, 4.19304e-05, 0), \
                           -186733, 123345, 123345, -nan)
reports[-1].sigmaresid = ValErr(1.09962, 0.00221395, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00152333, None, 2.78869e-07, None, -0.000393448, None, -1.00919e-05, None, -0.000393448, None, -1.00919e-05, None, -0.00151099, None, -2.5748e-06, None, -0.00151099, None, -2.5748e-06, None, 1.09967, None, 0.00714624, None, 1.09967, None, 0.00714624, None)

reports.append(Report(604062800, ("CSC", 2, 4, 2, 10), "MEm42_10"))
reports[-1].posNum = 132622
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00251159, 0.00498443, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.290833, 0.158598, 0), \
                           ValErr(-0.00154348, 0.00184711, 0), \
                           ValErr(-0.0132349, 0.0082828, 0), \
                           ValErr(1.32888e-05, 3.9617e-05, 0), \
                           -204841, 132622, 132622, -nan)
reports[-1].sigmaresid = ValErr(1.13384, 0.00220155, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(1.63689e-05, None, -7.01399e-05, None, -0.00240991, None, -9.28908e-05, None, -0.00240991, None, -9.28908e-05, None, -0.00165545, None, -7.02091e-05, None, -0.00165545, None, -7.02091e-05, None, 1.13387, None, 0.00727733, None, 1.13387, None, 0.00727733, None)

reports.append(Report(604062816, ("CSC", 2, 4, 2, 12), "MEm42_12"))
reports[-1].posNum = 124058
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00361597, 0.00515403, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.383279, 0.163503, 0), \
                           ValErr(-0.00218596, 0.00192043, 0), \
                           ValErr(0.0026734, 0.00862693, 0), \
                           ValErr(-6.97548e-05, 4.11129e-05, 0), \
                           -187634, 124058, 124058, -nan)
reports[-1].sigmaresid = ValErr(1.09805, 0.00220442, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00551548, None, -4.38773e-05, None, -0.0051889, None, -5.43171e-05, None, -0.0051889, None, -5.43171e-05, None, -0.00626678, None, -1.99107e-05, None, -0.00626678, None, -1.99107e-05, None, 1.0981, None, 0.00705533, None, 1.0981, None, 0.00705533, None)

reports.append(Report(604062832, ("CSC", 2, 4, 2, 14), "MEm42_14"))
reports[-1].posNum = 130911
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00306237, 0.00497151, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.38726, 0.158802, 0), \
                           ValErr(-0.0012044, 0.00185721, 0), \
                           ValErr(-0.00378531, 0.00831183, 0), \
                           ValErr(6.3699e-05, 3.96835e-05, 0), \
                           -200137, 130911, 130911, -nan)
reports[-1].sigmaresid = ValErr(1.11612, 0.00218126, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00481508, None, -1.24827e-05, None, 0.00370056, None, 4.92554e-06, None, 0.00370056, None, 4.92554e-06, None, 0.00563389, None, 1.89461e-05, None, 0.00563389, None, 1.89461e-05, None, 1.11617, None, 0.00725987, None, 1.11617, None, 0.00725987, None)

reports.append(Report(604062848, ("CSC", 2, 4, 2, 16), "MEm42_16"))
reports[-1].posNum = 125239
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00567322, 0.00517956, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.704178, 0.164442, 0), \
                           ValErr(0.00358233, 0.00192208, 0), \
                           ValErr(0.00715933, 0.00865931, 0), \
                           ValErr(-6.57232e-06, 4.12467e-05, 0), \
                           -191267, 125239, 125239, -nan)
reports[-1].sigmaresid = ValErr(1.11436, 0.0022266, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00472754, None, -5.68366e-05, None, -0.00305336, None, -5.13282e-05, None, -0.00305336, None, -5.13282e-05, None, -0.0039222, None, -5.92943e-05, None, -0.0039222, None, -5.92943e-05, None, 1.11445, None, 0.00692412, None, 1.11445, None, 0.00692412, None)

reports.append(Report(604062864, ("CSC", 2, 4, 2, 18), "MEm42_18"))
reports[-1].posNum = 126854
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00976834, 0.00508896, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0975059, 0.162602, 0), \
                           ValErr(-0.00152746, 0.00189776, 0), \
                           ValErr(0.00865455, 0.00848165, 0), \
                           ValErr(-5.69544e-06, 4.06309e-05, 0), \
                           -193899, 126854, 126854, -nan)
reports[-1].sigmaresid = ValErr(1.11581, 0.00221525, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00524669, None, -2.17376e-05, None, -0.00661769, None, 1.98873e-07, None, -0.00661769, None, 1.98873e-07, None, -0.00489458, None, 1.62205e-05, None, -0.00489458, None, 1.62205e-05, None, 1.11582, None, 0.00741255, None, 1.11582, None, 0.00741255, None)

reports.append(Report(604062880, ("CSC", 2, 4, 2, 20), "MEm42_20"))
reports[-1].posNum = 130345
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00442139, 0.00504323, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.240149, 0.16, 0), \
                           ValErr(-0.000526359, 0.00187319, 0), \
                           ValErr(-0.00469656, 0.00839145, 0), \
                           ValErr(3.08854e-05, 4.02544e-05, 0), \
                           -199904, 130345, 130345, -nan)
reports[-1].sigmaresid = ValErr(1.12156, 0.00219664, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00248092, None, -1.03133e-05, None, -0.00522088, None, -2.39029e-06, None, -0.00522088, None, -2.39029e-06, None, -0.0110743, None, -1.16527e-06, None, -0.0110743, None, -1.16527e-06, None, 1.12157, None, 0.00757611, None, 1.12157, None, 0.00757611, None)

reports.append(Report(604062896, ("CSC", 2, 4, 2, 22), "MEm42_22"))
reports[-1].posNum = 124572
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.0119687, 0.00515561, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.357917, 0.163937, 0), \
                           ValErr(0.00122044, 0.00193016, 0), \
                           ValErr(-0.00357248, 0.00861372, 0), \
                           ValErr(-5.46078e-05, 4.1227e-05, 0), \
                           -189833, 124572, 124572, -nan)
reports[-1].sigmaresid = ValErr(1.11065, 0.00222511, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00931408, None, 3.31461e-05, None, 0.00841351, None, 2.10498e-05, None, 0.00841351, None, 2.10498e-05, None, 0.0161397, None, 3.72878e-05, None, 0.0161397, None, 3.72878e-05, None, 1.11068, None, 0.00700744, None, 1.11068, None, 0.00700744, None)

reports.append(Report(604062912, ("CSC", 2, 4, 2, 24), "MEm42_24"))
reports[-1].posNum = 130326
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.0143094, 0.00501085, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.198622, 0.0858783, 0), \
                           ValErr(-0.000278313, 0.00105075, 0), \
                           ValErr(0.0221498, 0.00824015, 0), \
                           ValErr(2.06291e-05, 3.73086e-05, 0), \
                           -199348, 130326, 130326, -nan)
reports[-1].sigmaresid = ValErr(1.11703, 0.00217953, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00913541, None, 2.27182e-05, None, -0.00486249, None, 5.11128e-06, None, -0.00486249, None, 5.11128e-06, None, -0.00383966, None, 3.44267e-05, None, -0.00383966, None, 3.44267e-05, None, 1.11706, None, 0.00706549, None, 1.11706, None, 0.00706549, None)

reports.append(Report(604062928, ("CSC", 2, 4, 2, 26), "MEm42_26"))
reports[-1].posNum = 124167
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00148542, 0.00522591, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.298066, 0.162222, 0), \
                           ValErr(-0.00252048, 0.00190346, 0), \
                           ValErr(-0.00936178, 0.00862443, 0), \
                           ValErr(2.23583e-05, 4.16287e-05, 0), \
                           -187304, 124167, 124167, -nan)
reports[-1].sigmaresid = ValErr(1.09368, 0.00219469, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.00695475, None, 1.74951e-05, None, -0.00415742, None, 1.18498e-05, None, -0.00415742, None, 1.18498e-05, None, -0.00356091, None, 6.97551e-06, None, -0.00356091, None, 6.97551e-06, None, 1.09372, None, 0.00700631, None, 1.09372, None, 0.00700631, None)

reports.append(Report(604062944, ("CSC", 2, 4, 2, 28), "MEm42_28"))
reports[-1].posNum = 132977
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.000431737, 0.00502115, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.354081, 0.158978, 0), \
                           ValErr(-0.00190665, 0.00185557, 0), \
                           ValErr(0.00371729, 0.00833785, 0), \
                           ValErr(1.737e-05, 3.99881e-05, 0), \
                           -205727, 132977, 132977, -nan)
reports[-1].sigmaresid = ValErr(1.13672, 0.0022042, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.000793422, None, -2.87534e-05, None, 0.0016172, None, -3.15858e-05, None, 0.0016172, None, -3.15858e-05, None, -0.000790224, None, -3.28488e-05, None, -0.000790224, None, -3.28488e-05, None, 1.13675, None, 0.0072294, None, 1.13675, None, 0.0072294, None)

reports.append(Report(604062960, ("CSC", 2, 4, 2, 30), "MEm42_30"))
reports[-1].posNum = 123243
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00913358, 0.00520562, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.274448, 0.164058, 0), \
                           ValErr(-0.0035949, 0.00192544, 0), \
                           ValErr(0.0106593, 0.00866665, 0), \
                           ValErr(5.00142e-05, 4.14114e-05, 0), \
                           -186196, 123243, 123243, -nan)
reports[-1].sigmaresid = ValErr(1.09622, 0.00220802, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(-0.0025853, None, 7.04938e-06, None, -0.00312476, None, 1.78522e-05, None, -0.00312476, None, 1.78522e-05, None, -0.00345956, None, -5.5327e-06, None, -0.00345956, None, -5.5327e-06, None, 1.09626, None, 0.00738184, None, 1.09626, None, 0.00738184, None)

reports.append(Report(604062976, ("CSC", 2, 4, 2, 32), "MEm42_32"))
reports[-1].posNum = 131449
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00135083, 0.00498698, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.0122492, 0.159103, 0), \
                           ValErr(-0.00212942, 0.00185761, 0), \
                           ValErr(0.00261549, 0.0083303, 0), \
                           ValErr(1.49647e-05, 3.97489e-05, 0), \
                           -201672, 131449, 131449, -nan)
reports[-1].sigmaresid = ValErr(1.12219, 0.00218848, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00373277, None, -5.06e-05, None, 0.00287546, None, -5.77955e-05, None, 0.00287546, None, -5.77955e-05, None, 0.00126039, None, -5.1908e-05, None, 0.00126039, None, -5.1908e-05, None, 1.1222, None, 0.00758049, None, 1.1222, None, 0.00758049, None)

reports.append(Report(604062992, ("CSC", 2, 4, 2, 34), "MEm42_34"))
reports[-1].posNum = 127321
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(-0.00911862, 0.00508478, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.299741, 0.163122, 0), \
                           ValErr(-0.000882982, 0.00191185, 0), \
                           ValErr(0.0146415, 0.00853, 0), \
                           ValErr(8.17926e-05, 4.06213e-05, 0), \
                           -195112, 127321, 127321, -nan)
reports[-1].sigmaresid = ValErr(1.12019, 0.00221987, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00459036, None, -2.03981e-05, None, -0.000597935, None, -1.61967e-05, None, -0.000597935, None, -1.61967e-05, None, 0.00295576, None, -8.68305e-06, None, 0.00295576, None, -8.68305e-06, None, 1.12023, None, 0.00713148, None, 1.12023, None, 0.00713148, None)

reports.append(Report(604063008, ("CSC", 2, 4, 2, 36), "MEm42_36"))
reports[-1].posNum = 129983
reports[-1].negNum = 0
reports[-1].fittype = "6DOFrphi"
reports[-1].add_parameters(ValErr(0.00617963, 0.00498708, 0), \
                           ValErr(0, 0, 0), \
                           ValErr(0.476951, 0.159418, 0), \
                           ValErr(-0.00256105, 0.00185693, 0), \
                           ValErr(0.00579524, 0.00835182, 0), \
                           ValErr(-2.1376e-05, 3.96794e-05, 0), \
                           -198626, 129983, 129983, -nan)
reports[-1].sigmaresid = ValErr(1.11534, 0.0021875, 0)
reports[-1].sigmaresslope = ValErr(0, 0, 0)
reports[-1].add_stats(0.00665382, None, 3.78959e-06, None, 0.00770012, None, 3.78326e-05, None, 0.00770012, None, 3.78326e-05, None, 0.00843104, None, 3.95384e-05, None, 0.00843104, None, 3.95384e-05, None, 1.11539, None, 0.00715637, None, 1.11539, None, 0.00715637, None)

