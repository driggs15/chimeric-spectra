class scan:
    def __init__(self):
        self.title = ""
        self.scan_num = -1
        self.rt = -1.0
        self.precursor_mass = -1.0
        self.precursor_intensity = -1.0
        self.charge = -1
        self.charge_state = None
        self.m_z = []
        self.intensity = []
        self.add = -1.0

    def __str__(self) -> str:
        peaks = []
        for i, m_z in enumerate(self.m_z):
            peaks.append(m_z + " " + self.intensity[i])
        peaks = "\n".join(peaks)
        return f"TITLE={self.title}\nRTINSECONDS={self.rt}\nPEPMASS={self.precursor_mass} {self.precursor_intensity}\nCHARGE={self.charge}{self.charge_state}\n{peaks}"
    
    def __eq__(self, other) -> bool:
        return self.title == other.title

    def parse_scan(self, lines):
        ## Assume list of file lines have been stripped of EOL characters
        for line in lines:
            if line.startswith("TITLE="):
                line = line.replace("TITLE=", "").split()[0]
                self.title = line

                line = line.split(".")
                self.scan_num = line[-2]
                self.add = int(self.scan_num)
            elif line.startswith("RTINSECONDS="):
                line = line.replace("RTINSECONDS=", "")
                self.rt = line
            elif line.startswith("PEPMASS="):
                line = line.replace("PEPMASS=", "")
                line = line.split()
                self.precursor_mass = line[0]
                self.precursor_intensity = line[1]
            elif line.startswith("CHARGE="):
                line = line.replace("CHARGE=", "")
                self.charge_state = line[-1]

                line = line[:-1]
                self.charge = line
            else:
                line = line.split()
                self.m_z.append(line[0])
                self.intensity.append(line[1])


                