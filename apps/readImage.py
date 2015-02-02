# -*- coding: utf-8 -*-

import os
import sys
import urllib
from models import Actor
# list = [ 'ABP-053', 'ABP-100', 'ABP-108', 'ABP-119', 'ABP-138', 'ABP-145', 'ABP-159', 'ABP-164', 'ABP-171', 'ABP-172', 'ABP-180', 'ABP-204', 'ABP-205', 'ABP-210', 'ABP-211', 'ABP-212', 'ABP-213', 'ABP-214', 'ABP-219', 'ABP-224', 'ABP-225', 'ABP-226', 'ABP-227', 'ABP-228', 'ABP-229', 'ABP-230', 'ABP-231', 'ABP-232', 'ABP-233', 'ABP-234', 'ABP-235', 'ABP-236', 'ABP-251', 'ABS-082', 'ABS-086', 'ABS-100', 'ABS-137', 'ABS-139', 'ABS-147', 'ABS-178', 'ABS-210', 'ABS-231', 'ADN-008', 'ATFB-110', 'ATFB-155', 'ATKD-196', 'AVGL-109', 'AVKH-002', 'AVOP-004', 'AVOP-069', 'BBI-136', 'BBI-142', 'BBI-146', 'BBI-148', 'BBI-151', 'BBI-154', 'BBI-160', 'BBI-165', 'BBI-174', 'BBI-177', 'BBI-179', 'BBI-180', 'BEB-005', 'BEB-076', 'BEB-084', 'BEB-111', 'BF-266', 'BF-342', 'BF-352', 'BF-353', 'BF-354', 'BGN-013', 'BGN-014', 'BGN-015', 'BID-052', 'BIST-008', 'BLK-137', 'BMW-046', 'CHN-025', 'CHN-057', 'DCBS-011', 'DCOL-034', 'DFE-008', 'DIGI-170', 'DJE-048', 'DOM-043', 'DPMI-008', 'DPMI-011', 'DPMI-013', 'DSE-1225', 'DV-1583', 'DV-1666', 'DV-1677', 'DV-1679', 'DV-1681', 'DV-1682', 'DV-1683', 'DV-1684', 'DV-1688', 'DV-1689', 'DVAJ-0002', 'DVAJ-0003', 'DVAJ-0004', 'DVAJ-0005', 'DVAJ-0006', 'DVAJ-0007', 'DVDES-769', 'EBL-006', 'EBOD-163', 'EBOD-249', 'EBOD-285', 'EBOD-355', 'EBOD-401', 'EBOD-405', 'EBOD-417', 'EBOD-420', 'EBOD-421', 'ECB-086', 'EYAN-001', 'EYAN-003', 'EYAN-004', 'FNK-018', 'GAR-236', 'GAR-280', 'HXAF-002', 'HXAK-008', 'IDBD-446', 'IDBD-505', 'IDBD-586', 'IDBD-589', 'IDBD-593', 'INU-006', 'INU-047', 'IPSD-041', 'IPSD-045', 'IPTD-694', 'IPTD-711', 'IPTD-757', 'IPTD-799', 'IPTD-811', 'IPTD-909', 'IPTD-927', 'IPTD-938', 'IPTD-950', 'IPTD-959', 'IPTD-999', 'IPZ-039', 'IPZ-046', 'IPZ-059', 'IPZ-068', 'IPZ-071', 'IPZ-126', 'IPZ-127', 'IPZ-139', 'IPZ-144', 'IPZ-174', 'IPZ-181', 'IPZ-196', 'IPZ-251', 'IPZ-253', 'IPZ-266', 'IPZ-275', 'IPZ-339', 'IPZ-370', 'IPZ-420', 'IPZ-433', 'IPZ-440', 'IPZ-462', 'IPZ-472', 'IPZ-473', 'IPZ-475', 'IPZ-476', 'IPZ-477', 'IPZ-478', 'IPZ-479', 'IPZ-480', 'IPZ-481', 'IPZ-482', 'IPZ-483', 'IPZ-485', 'IPZ-486', 'IPZ-487', 'IPZ-488', 'IPZ-489', 'IPZ-490', 'IPZ-491', 'IPZ-492', 'IPZ-493', 'IPZ-494', 'IPZ-495', 'IPZ-497', 'IPZ-498', 'IPZ-499', 'IPZ-500', 'IPZ-501', 'IPZ-502', 'IPZ-503', 'IPZ-504', 'IPZ-505', 'IPZ-506', 'IPZ-507', 'IPZ-508', 'IPZ-509', 'IPZ-510', 'IPZ-511', 'IPZ-512', 'IPZ-513', 'IPZ-514', 'IPZ-515', 'JBS-011', 'JBS-022', 'JUC-369', 'JUFD-100', 'JUFD-305', 'JUFD-369', 'KAWD-596', 'KAWD-597', 'KAWD-599', 'KAWD-600', 'KAWD-601', 'KAWD-602', 'KAWD-604', 'KAWD-605', 'KAWD-606', 'MDB-557', 'MDYD-759', 'MDYD-778', 'MDYD-810', 'MDYD-894', 'MEK-008', 'MIAD-524', 'MIAD-632', 'MIAD-657', 'MIAD-663', 'MIAD-711', 'MIAD-719', 'MIAD-720', 'MIAD-721', 'MIAD-723', 'MIAD-725', 'MIAD-727', 'MIBD-706', 'MIBD-854', 'MIDD-735', 'MIDD-747', 'MIDD-791', 'MIDD-832', 'MIDD-876', 'MIDD-885', 'MIDD-893', 'MIDD-910', 'MIDD-922', 'MIDD-944', 'MIDD-972', 'MIDD-992', 'MIDE-007', 'MIDE-008', 'MIDE-020', 'MIDE-022', 'MIDE-051', 'MIDE-058', 'MIDE-072', 'MIDE-075', 'MIDE-109', 'MIDE-128', 'MIDE-130', 'MIDE-138', 'MIDE-139', 'MIDE-162', 'MIDE-163', 'MIDE-164', 'MIDE-165', 'MIDE-166', 'MIDE-167', 'MIDE-168', 'MIDE-169', 'MIDE-170', 'MIDE-175', 'MIDE-191', 'MIGD-488', 'MIGD-604', 'MIGD-618', 'MIGD-619', 'MIGD-620', 'MIGD-621', 'MIGD-634', 'MILD-941', 'MILD-942', 'MILD-943', 'MILD-944', 'MILD-945', 'MILD-946', 'MILD-947', 'MILD-948', 'MILD-949', 'MIMK-011', 'MIMK-015', 'MIMK-020', 'MIMK-025', 'MIMK-026', 'MIMK-027', 'MIMK-028', 'MIMK-029', 'MIRD-081', 'MIRD-117', 'MIRD-119', 'MIRD-133', 'MIRD-134', 'MIRD-136', 'MIRD-144', 'MIRD-145', 'MXGS-582', 'MXGS-600', 'MXGS-693', 'MXGS-706', 'MXGS-707', 'MXGS-708', 'MXGS-709', 'MXGS-711', 'MXGS-712', 'MXGS-713', 'MXGS-714', 'MXGS-715', 'MXGS-716', 'MXGS-722', 'NAMA-004', 'NHDTA-480', 'ODFM-022', 'ODFW-006', 'OKAD-508', 'OKAX-014', 'ONSD-879', 'OVG-010', 'PBD-252', 'PGD-481', 'PGD-574', 'PGD-585', 'PGD-606', 'PGD-627', 'PGD-635', 'PGD-677', 'PGD-683', 'PGD-685', 'PGD-718', 'PGD-720', 'PGD-728', 'PGD-729', 'PGD-730', 'PGD-731', 'PGD-732', 'PGD-733', 'PGD-734', 'PGD-735', 'PGD-739', 'PGD-742', 'PPB-015', 'PPFT-004', 'PPPD-248', 'PPPD-267', 'PPPD-286', 'PPPD-288', 'PPPD-320', 'PPPD-328', 'PPPD-329', 'PPPD-330', 'PPPD-331', 'PPPD-332', 'PPPD-341', 'PPS-227', 'PPSD-047', 'PSD-408', 'PZ-104', 'RAW-012', 'RBD-228', 'RBD-582', 'RCT-472', 'RCT-587', 'RCT-644', 'RKI-111', 'RKI-365', 'SAMA-385', 'SDDE-318', 'SDDE-355', 'SDMU-130', 'SERO-0263', 'SERO-0264', 'SERO-0266', 'SERO-0267', 'SGA-018', 'SHKD-491', 'SHKD-546', 'SNIS-027', 'SNIS-070', 'SNIS-091', 'SNIS-136', 'SNIS-147', 'SNIS-166', 'SNIS-205', 'SNIS-212', 'SNIS-264', 'SNIS-265', 'SNIS-266', 'SNIS-267', 'SNIS-269', 'SNIS-270', 'SNIS-271', 'SNIS-272', 'SNIS-273', 'SNIS-274', 'SNIS-275', 'SNIS-277', 'SNIS-278', 'SNIS-279', 'SNIS-280', 'SNIS-281', 'SNIS-282', 'SNIS-283', 'SNIS-284', 'SNIS-286', 'SNIS-287', 'SNIS-288', 'SNIS-290', 'SNIS-291', 'SNIS-293', 'SNIS-294', 'SNIS-295', 'SNIS-296', 'SNIS-297', 'SNIS-299', 'SNIS-300', 'SNIS-301', 'SNIS-302', 'SNIS-303', 'SNIS-304', 'SNIS-305', 'SNIS-306', 'SNIS-307', 'SNIS-308', 'SNIS-309', 'SNIS-310', 'SNIS-312', 'SNIS-313', 'SNIS-314', 'SNIS-315', 'SNIS-316', 'SNIS-317', 'SNIS-318', 'SNIS-319', 'SNIS-321', 'SNIS-322', 'SNIS-323', 'SNIS-324', 'SNIS-325', 'SNIS-326', 'SNTM-002', 'SOE-289', 'SOE-883', 'SOE-992', 'SON-503', 'SRS-022', 'STAR-369', 'STAR-395', 'STAR-413', 'STAR-458', 'STAR-471', 'STAR-497', 'STAR-560', 'STAR-561', 'STAR-562', 'STAR-563', 'STAR-564', 'STAR-565', 'STAR-567', 'STAR-568', 'STAR-569', 'STAR-570', 'SUPD-122', 'SUPD-123', 'SUPD-124', 'SW-258', 'TDT-018', 'TEAM-055', 'URDT-012', 'VGQ-014', 'WANZ-055', 'WANZ-064', 'WANZ-085', 'WANZ-105', 'WANZ-110', 'WANZ-162', 'WANZ-178', 'WANZ-225', 'WANZ-263', 'WANZ-264', 'WANZ-265', 'WANZ-266', 'WANZ-268', 'WANZ-269', 'WANZ-270', 'WANZ-271', 'WANZ-272', 'WWW-016', 'WWW-017', 'XVSR-016', 'XVSR-017', 'XVSR-019', 'XVSR-020', 'XVSR-021', 'XVSR-022', 'XVSR-023', 'ZIZG-001', 'ZIZG-003', 'ZUKO-046']

# def getVideoName():
#     list = []
#     oVideo = Video.query.all()
#     for each in oVideo:
#         list.append(each.name)
#     return list
#
def getActorName():
    list = []
    oActor = Actor.query.all()
    for each in oActor:
        list.append(each.name)
    return list

def download_photo(img_url, filename):
    file_path = "%s%s" % ("C:/pythonTest/", '%s.jpg'%filename)
    downloaded_image = file(file_path, "wb")
    image_on_web = urllib.urlopen(img_url)
    while True:
        buf = image_on_web.read(100000000)
        if len(buf) == 0:
            break
        downloaded_image.write(buf)
    downloaded_image.close()
    image_on_web.close()
    return file_path
#
# for each in list:
#     url = 'http://www.jikbakguri.com/show2/'+each
#     download_photo(url,each)

