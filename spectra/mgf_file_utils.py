import scan
import numpy

def parse_mgf(mgf_file):
    scans = []
    with open(mgf_file, encoding = "utf-8") as inFile:
        lines = []
        for line in inFile:
            line = line.strip()

            if line == "BEGIN IONS":
                continue
            if line == "END IONS":
                new_scan = scan.scan()
                new_scan.parse_scan(lines)

                scans.append(new_scan)
                lines = []
            else:
                lines.append(line)

    return scans

def write_mgf(scans, output_file):
    with open(output_file, "w", encoding = "utf-8") as outFile:
        for mgf in scans:
            num_m_z = list(map(numpy.longdouble, mgf.m_z.copy()))
            intensity = mgf.intensity.copy()

            intensity_sorted = [num for _, num in sorted(zip(num_m_z, intensity))]
            num_m_z = list(map(str, sorted(num_m_z)))

            mgf.m_z = num_m_z
            mgf.intensity = intensity_sorted

            outFile.write("BEGIN IONS\n")
            outFile.write(str(mgf) + "\n")
            outFile.write("END IONS\n")


