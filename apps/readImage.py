# # -*- coding: utf-8 -*-
#
# import os
# import sys
# import urllib
# # from models import Actor
# # list = [ 'ABP-053', 'ABP-100', 'ABP-108', 'ABP-119', 'ABP-138', 'ABP-145', 'ABP-159', 'ABP-164', 'ABP-171', 'ABP-172', 'ABP-180', 'ABP-204', 'ABP-205', 'ABP-210', 'ABP-211', 'ABP-212', 'ABP-213', 'ABP-214', 'ABP-219', 'ABP-224', 'ABP-225', 'ABP-226', 'ABP-227', 'ABP-228', 'ABP-229', 'ABP-230', 'ABP-231', 'ABP-232', 'ABP-233', 'ABP-234', 'ABP-235', 'ABP-236', 'ABP-251', 'ABS-082', 'ABS-086', 'ABS-100', 'ABS-137', 'ABS-139', 'ABS-147', 'ABS-178', 'ABS-210', 'ABS-231', 'ADN-008', 'ATFB-110', 'ATFB-155', 'ATKD-196', 'AVGL-109', 'AVKH-002', 'AVOP-004', 'AVOP-069', 'BBI-136', 'BBI-142', 'BBI-146', 'BBI-148', 'BBI-151', 'BBI-154', 'BBI-160', 'BBI-165', 'BBI-174', 'BBI-177', 'BBI-179', 'BBI-180', 'BEB-005', 'BEB-076', 'BEB-084', 'BEB-111', 'BF-266', 'BF-342', 'BF-352', 'BF-353', 'BF-354', 'BGN-013', 'BGN-014', 'BGN-015', 'BID-052', 'BIST-008', 'BLK-137', 'BMW-046', 'CHN-025', 'CHN-057', 'DCBS-011', 'DCOL-034', 'DFE-008', 'DIGI-170', 'DJE-048', 'DOM-043', 'DPMI-008', 'DPMI-011', 'DPMI-013', 'DSE-1225', 'DV-1583', 'DV-1666', 'DV-1677', 'DV-1679', 'DV-1681', 'DV-1682', 'DV-1683', 'DV-1684', 'DV-1688', 'DV-1689', 'DVAJ-0002', 'DVAJ-0003', 'DVAJ-0004', 'DVAJ-0005', 'DVAJ-0006', 'DVAJ-0007', 'DVDES-769', 'EBL-006', 'EBOD-163', 'EBOD-249', 'EBOD-285', 'EBOD-355', 'EBOD-401', 'EBOD-405', 'EBOD-417', 'EBOD-420', 'EBOD-421', 'ECB-086', 'EYAN-001', 'EYAN-003', 'EYAN-004', 'FNK-018', 'GAR-236', 'GAR-280', 'HXAF-002', 'HXAK-008', 'IDBD-446', 'IDBD-505', 'IDBD-586', 'IDBD-589', 'IDBD-593', 'INU-006', 'INU-047', 'IPSD-041', 'IPSD-045', 'IPTD-694', 'IPTD-711', 'IPTD-757', 'IPTD-799', 'IPTD-811', 'IPTD-909', 'IPTD-927', 'IPTD-938', 'IPTD-950', 'IPTD-959', 'IPTD-999', 'IPZ-039', 'IPZ-046', 'IPZ-059', 'IPZ-068', 'IPZ-071', 'IPZ-126', 'IPZ-127', 'IPZ-139', 'IPZ-144', 'IPZ-174', 'IPZ-181', 'IPZ-196', 'IPZ-251', 'IPZ-253', 'IPZ-266', 'IPZ-275', 'IPZ-339', 'IPZ-370', 'IPZ-420', 'IPZ-433', 'IPZ-440', 'IPZ-462', 'IPZ-472', 'IPZ-473', 'IPZ-475', 'IPZ-476', 'IPZ-477', 'IPZ-478', 'IPZ-479', 'IPZ-480', 'IPZ-481', 'IPZ-482', 'IPZ-483', 'IPZ-485', 'IPZ-486', 'IPZ-487', 'IPZ-488', 'IPZ-489', 'IPZ-490', 'IPZ-491', 'IPZ-492', 'IPZ-493', 'IPZ-494', 'IPZ-495', 'IPZ-497', 'IPZ-498', 'IPZ-499', 'IPZ-500', 'IPZ-501', 'IPZ-502', 'IPZ-503', 'IPZ-504', 'IPZ-505', 'IPZ-506', 'IPZ-507', 'IPZ-508', 'IPZ-509', 'IPZ-510', 'IPZ-511', 'IPZ-512', 'IPZ-513', 'IPZ-514', 'IPZ-515', 'JBS-011', 'JBS-022', 'JUC-369', 'JUFD-100', 'JUFD-305', 'JUFD-369', 'KAWD-596', 'KAWD-597', 'KAWD-599', 'KAWD-600', 'KAWD-601', 'KAWD-602', 'KAWD-604', 'KAWD-605', 'KAWD-606', 'MDB-557', 'MDYD-759', 'MDYD-778', 'MDYD-810', 'MDYD-894', 'MEK-008', 'MIAD-524', 'MIAD-632', 'MIAD-657', 'MIAD-663', 'MIAD-711', 'MIAD-719', 'MIAD-720', 'MIAD-721', 'MIAD-723', 'MIAD-725', 'MIAD-727', 'MIBD-706', 'MIBD-854', 'MIDD-735', 'MIDD-747', 'MIDD-791', 'MIDD-832', 'MIDD-876', 'MIDD-885', 'MIDD-893', 'MIDD-910', 'MIDD-922', 'MIDD-944', 'MIDD-972', 'MIDD-992', 'MIDE-007', 'MIDE-008', 'MIDE-020', 'MIDE-022', 'MIDE-051', 'MIDE-058', 'MIDE-072', 'MIDE-075', 'MIDE-109', 'MIDE-128', 'MIDE-130', 'MIDE-138', 'MIDE-139', 'MIDE-162', 'MIDE-163', 'MIDE-164', 'MIDE-165', 'MIDE-166', 'MIDE-167', 'MIDE-168', 'MIDE-169', 'MIDE-170', 'MIDE-175', 'MIDE-191', 'MIGD-488', 'MIGD-604', 'MIGD-618', 'MIGD-619', 'MIGD-620', 'MIGD-621', 'MIGD-634', 'MILD-941', 'MILD-942', 'MILD-943', 'MILD-944', 'MILD-945', 'MILD-946', 'MILD-947', 'MILD-948', 'MILD-949', 'MIMK-011', 'MIMK-015', 'MIMK-020', 'MIMK-025', 'MIMK-026', 'MIMK-027', 'MIMK-028', 'MIMK-029', 'MIRD-081', 'MIRD-117', 'MIRD-119', 'MIRD-133', 'MIRD-134', 'MIRD-136', 'MIRD-144', 'MIRD-145', 'MXGS-582', 'MXGS-600', 'MXGS-693', 'MXGS-706', 'MXGS-707', 'MXGS-708', 'MXGS-709', 'MXGS-711', 'MXGS-712', 'MXGS-713', 'MXGS-714', 'MXGS-715', 'MXGS-716', 'MXGS-722', 'NAMA-004', 'NHDTA-480', 'ODFM-022', 'ODFW-006', 'OKAD-508', 'OKAX-014', 'ONSD-879', 'OVG-010', 'PBD-252', 'PGD-481', 'PGD-574', 'PGD-585', 'PGD-606', 'PGD-627', 'PGD-635', 'PGD-677', 'PGD-683', 'PGD-685', 'PGD-718', 'PGD-720', 'PGD-728', 'PGD-729', 'PGD-730', 'PGD-731', 'PGD-732', 'PGD-733', 'PGD-734', 'PGD-735', 'PGD-739', 'PGD-742', 'PPB-015', 'PPFT-004', 'PPPD-248', 'PPPD-267', 'PPPD-286', 'PPPD-288', 'PPPD-320', 'PPPD-328', 'PPPD-329', 'PPPD-330', 'PPPD-331', 'PPPD-332', 'PPPD-341', 'PPS-227', 'PPSD-047', 'PSD-408', 'PZ-104', 'RAW-012', 'RBD-228', 'RBD-582', 'RCT-472', 'RCT-587', 'RCT-644', 'RKI-111', 'RKI-365', 'SAMA-385', 'SDDE-318', 'SDDE-355', 'SDMU-130', 'SERO-0263', 'SERO-0264', 'SERO-0266', 'SERO-0267', 'SGA-018', 'SHKD-491', 'SHKD-546', 'SNIS-027', 'SNIS-070', 'SNIS-091', 'SNIS-136', 'SNIS-147', 'SNIS-166', 'SNIS-205', 'SNIS-212', 'SNIS-264', 'SNIS-265', 'SNIS-266', 'SNIS-267', 'SNIS-269', 'SNIS-270', 'SNIS-271', 'SNIS-272', 'SNIS-273', 'SNIS-274', 'SNIS-275', 'SNIS-277', 'SNIS-278', 'SNIS-279', 'SNIS-280', 'SNIS-281', 'SNIS-282', 'SNIS-283', 'SNIS-284', 'SNIS-286', 'SNIS-287', 'SNIS-288', 'SNIS-290', 'SNIS-291', 'SNIS-293', 'SNIS-294', 'SNIS-295', 'SNIS-296', 'SNIS-297', 'SNIS-299', 'SNIS-300', 'SNIS-301', 'SNIS-302', 'SNIS-303', 'SNIS-304', 'SNIS-305', 'SNIS-306', 'SNIS-307', 'SNIS-308', 'SNIS-309', 'SNIS-310', 'SNIS-312', 'SNIS-313', 'SNIS-314', 'SNIS-315', 'SNIS-316', 'SNIS-317', 'SNIS-318', 'SNIS-319', 'SNIS-321', 'SNIS-322', 'SNIS-323', 'SNIS-324', 'SNIS-325', 'SNIS-326', 'SNTM-002', 'SOE-289', 'SOE-883', 'SOE-992', 'SON-503', 'SRS-022', 'STAR-369', 'STAR-395', 'STAR-413', 'STAR-458', 'STAR-471', 'STAR-497', 'STAR-560', 'STAR-561', 'STAR-562', 'STAR-563', 'STAR-564', 'STAR-565', 'STAR-567', 'STAR-568', 'STAR-569', 'STAR-570', 'SUPD-122', 'SUPD-123', 'SUPD-124', 'SW-258', 'TDT-018', 'TEAM-055', 'URDT-012', 'VGQ-014', 'WANZ-055', 'WANZ-064', 'WANZ-085', 'WANZ-105', 'WANZ-110', 'WANZ-162', 'WANZ-178', 'WANZ-225', 'WANZ-263', 'WANZ-264', 'WANZ-265', 'WANZ-266', 'WANZ-268', 'WANZ-269', 'WANZ-270', 'WANZ-271', 'WANZ-272', 'WWW-016', 'WWW-017', 'XVSR-016', 'XVSR-017', 'XVSR-019', 'XVSR-020', 'XVSR-021', 'XVSR-022', 'XVSR-023', 'ZIZG-001', 'ZIZG-003', 'ZUKO-046']
# list2 = ['고토 리사','고토 에미','구루루기 미칸', '기타노 하루카', '나가사와 에리나 ', '나가사와 츠구미', '나가사와 카나', '나가사쿠 유미', '나가사키 후미', '나가세 료코', '나가세 마미', '나가세 사토미', '나가세 아오이', '나가츠키 람 ', '나기노 미유', '나기사 카자미', '나기사 코토미', '나나사와 루리', '나나사키 후우카', '나나세 유리', '나나우미 나나', '나다사카 마이', '나루미 레이', '나루미 우루미', '나루세 코코미', '나리미야 카나', '나리타 아이', '나미키 안리', '나미키 유', '나오시마 아이', '나이토 카나', '나츠메 나나', '나츠메 유키', '나츠메 이로하', '나츠미 이쿠', '나츠카제 마린', '나츠키 미나미', '나츠키 유노', '나카가와 미레이', '나카가와 미카', '나카노 노조미 ', '나카노 에리카', '나카모리 레이코', '나카무라 치카', '나카야마 리리', '나카야마 에리스', '나카자토 유나', '나카지마 쿄코', '노노카 하나', '노노하라 미키', '노조미 마유', '니노미야 나나', '니노미야 사키', '니노미야 아키', '니시나 모모카', '니시노 세이나', '니시노 쇼우', '니시다 카리나', '니시야마 노조미', '니시야마 마리', '니시카와 유이', '니이야마 란', '니이야마 사야', '니이야마 카에데', '다카츠키 와카', '루카와 리나', '리오', '마나베 사치카', '마노 유리아 ', '마리나 오다', '마리카 미쿠', '마미야 준', '마시로 노조미', '마시로 미나', '마시로 안', '마에다 사오리 ', '마에다 카오리', '마에시마 미호', '마에하라 유키', '마이사키 미쿠니', '마이카 나츠', '마츠다 치사토', '마츠모토 메이', '마츠시마 아오이', '마츠시마 카에데', '마츠시타 나오', '마츠시타 레이', '마츠시타 아카네', '마츠시타 히카리', '마츠오카 세리아', '마츠오카 치나', '마키 아즈사', '마키 쿄우코', '마키세 미사', '메구 에리카', '메구리', '메모리 시즈쿠', '모로호시 세이라', '모리 나나코', '모리 하루라', '모리나가 쿠루미', '모리모토 아스카', '모리무라 나츠미', '모리시타 아야노', '모리시타 쿠루미', '모리카와 스즈카', '모모노 나고미', '모모세 레몬', '모모이로 사쿠라', '모모카 린', '모모카 마리에', '모모카 에미리', '모모타 유키나', '모모타 히비키', '모모타니 에리카 ', '모치즈키 치히로', '모치즈키 케이', '무라카미 료코', '무라카미 리사', '무토 츠구미', '미나모토 미이나', '미나미 나미', '미나미 네이', '미나미 리오나 ', '미나미 사아야', '미나미 사야', '미나미 사호', '미나미 아이루', '미나미 아이리', '미나미 츠카사', '미나미 카요', '미나미 토토카', '미나미노 아야카', '미나미노 유키나', '미나토 리쿠', '미네 나유카', '미사키 린', '미사키 미유', '미사키 안', '미사키 칸나', '미사키 히나', '미사토 아리사', '미야노 히토미', '미야마 시호', '미야마 아오이', '미야모토 사오리', '미야비 사야카', '미야세 리코', '미야시타 리카', '미야시타 츠바사', '미야자키 아야', '미야자키 아이리 ', '미야자키 치이로', '미야자키 카호', '미야지 아이', '미야지 유리카', '미오리', '미우라 카나데', '미유 치나', '미유키 아리스', '미즈나 레이', '미즈나 유이', '미즈노 미도리', '미즈노 아사히', '미즈모토 에리카', '미즈모토 유우나', '미즈미 사키', '미즈사와 노노', '미즈사와 마오', '미즈사와 마키', '미즈사키 카렌', '미즈시로 세이라', '미즈키 나오', '미즈키 리사', '미즈키 유메', '미즈키 카난', '미즈키 코하루', '미즈타니 코코네', '미즈타마 레몬', '미즈하라 사나', '미즈호시 유키', '미츠미 아이', '미츠이 유카리', '미츠키 시노부', '미츠하시 히요리', '미카미 세리', '미쿠리 유네', '미쿠리야 아오이', '미키 이토우', '사나', '사나다 하루카', '사노 마유', '사라', '사라다 마키', '사사키 레미', '사사키 에미', '사사키 유이', '사사키 하루카', '사사하라 리무', '사야 이츠카', '사야마 아이', '사에구사 치토세', '사에지마 카오리 ', '사에키 나나', '사에키 사키', '사오토메 러브', '사오토메 루이', '사오토메 린', '사와 아리사 ', '사와무라 레이코', '사와이 메이', '사와지리 마미', '사이온지 레오', '사이조 루리', '사이조우 카렌', '사자나미 후', '사츠키 마이 ', '사카구치 미호노', '사카우에 모카', '사카이 모모카', '사카키 나치 ', '사쿠라 나나미', '사쿠라 리오', '사쿠라 마나', '사쿠라 아이', '사쿠라 에나 ', '사쿠라 유라', '사쿠라 치즈루', '사쿠라 코코미', '사쿠라 키즈나 ', '사쿠라기 린', '사쿠라기 에미카', '사쿠라기 유키네', '사쿠라이 리아', '사쿠라이 아야 ', '사쿠라이 아유', '사쿠라이 유코', '사쿠라이 토모카', '사쿠라자키 마이카', '사쿠야 유아 ', '사키 하츠미', '사키타 아리나', '사키타 우라라', '사토 아이리', '사토 유리', '사토 하루키', '사토 히마리', '사토미 유리아', '사토사키 시오리', '사토우 마유', '사토우 에리카', '사토우 히로미', '산카 레나', '세나 마오', '세나 미즈키', '세나 아유무', '쇼다 치사토', '스기사키 리카', '스기사키 안리 ', '스나카와 아이코', '스노하라 미키', '스에키 유리하', '스오 유키코', '스즈네 리오나', '스즈네 린', '스즈네 사유키', '스즈모리 로사', '스즈무라 미유우', '스즈무라 아이리', '스즈카 린', '스즈카와 아야네', '스즈카제 코토노', '스즈키 린', '스즈키 마나미', '스즈키 미라이', '스즈키 민트 ', '스즈키 사토미 ', '스즈키 안리 ', '스즈키 코나츠', '스즈키 코코', '스즈키 코하루', '스즈하 미우', '스즈하라 에미리 ', '시노 메구미', '시노다 아유미', '시노자키 미사', '시노하라 나미', '시노하라 안 ', '시라사키 모모', '시라세 에리나', '시라유리 노조미', '시라이시 나츠미', '시라이시 마리나', '시라이시 마리에', '시라이시 마유', '시라이시 미사키', '시라이시 유우', '시라이시 유키나', '시라이시 히요리', '시라자키 아이', '시라키 유우코', '시라토리 스미레', '시로사키 마이', '시로사키 아즈아', '시마자키 리카', '시마자키 마유', '시마타미 아이', '시바사키 에리카', '시부야 미키', '시부야 아리스', '시부야 카호', '시이나 마리나', '시이나 마유', '시이나 미유', '시이나 미쿠루', '시이나 유나', '시이나 히카루', '시즈쿠 파인', '아노아 루루', '아다치 아미', '아다치 유즈나', '아라가키 토와', '아라카와 미요', '아라키 리나', '아라키 마이', '아라키 아리사', '아리무라 치카', '아리사와 리사', '아리사와 미사', '아마네 에미루', '아마미 츠바사', '아마미야 마키', '아마미야 코토네', '아마이 미츠', '아마츠카 모에', '아베 미카코 ', '아베노 미쿠', '아사기리 메이사', '아사기리 아카리', '아사노 미나미', '아사노 에미', '아사노 하루미', '아사미 유마', '아사미야 마도카', '아사카와 미카', '아사쿠라 료우카', '아사쿠라 민트', '아사쿠라 아스카', '아사쿠라 아야네', '아사쿠라 유우', '아사토 유카', '아사히 마나', '아사히나 아카리', '아소 노조미', '아소우 메이', '아소우 유우', '아소우 카즈키', '아스카 미츠키', '아스카 이오', '아스카 키라라', '아시나 미호', '아시나 유리아', '아야나미 세나', '아야네 유리아', '아야네 하루나', '아야노 나나', '아야노 사키', '아야메 미오', '아야미 슌카', '아야세 나루미 ', '아야세 렌', '아야세 미나미', '아야세 시오리', '아야세 치즈루', '아야시로 유리나', '아오노 마린', '아오노 카나', '아오바 유나', '아오바 유이', '아오야마 나나', '아오야마 라우라', '아오야마 미쿠', '아오야마 아오이', '아오이', '아오이 레이', '아오이 부루마', '아오이 소라', '아오이 에리', '아오이 츠카사', '아오이 치히로', '아오이 카에데', '아오키 레이', '아오키 린', '아오키 미쿠 ', '아오키 카렌', '아유카와 나오', '아유카와 치사토', '아유하라 히카루', '아이나 리나', '아이네 마히로', '아이노 나미', '아이노 라라', '아이다 나나', '아이다 미나미', '아이다 사야카', '아이다 유아', '아이리 미쿠', '아이미 레이', '아이바 레이카', '아이사카 하루나', '아이세 리리코', '아이스 코코아', '아이시로 사야카', '아이자와 렌', '아이자와 렌2', '아이자와 리나', '아이자와 아리사', '아이자와 준', '아이자와 츠바사', '아이자와 카린', '아이카 린', '아이카 사야', '아이카와 린', '아이카와 세이라', '아이카와 유이', '아이카와 카오리', '아이쿠 유우', '아이토 유우키', '아이하라 사에', '아이하라 에레나', '아이하라 유아', '아이하라 히토미', '아즈마 린', '아즈미', '아즈미 렌', '아즈사 나가사와', '아즈사 유이', '아즈치 유이', '아카네 레이라', '아카네 리노', '아카네 아즈사', '아카네 유이', '아카이 미즈키', '아키 레이코', '아키나', '아키나 카에데', '아키모토 마유카', '아키모토 미유', '아키야마 쇼코', '아키요시 히나', '아키즈키 레이나', '아키츠키 메이', '안 미츠키', '안나 리카', '안노 루리', '안노 안', '안노 유미', '안죠 안나', '안주 사나', '야구치 미리', '야노 사키', '야마구치 리쿠', '야마다 마리코', '야마카와 세이라', '야부키 안', '야타베 카즈사', '에비하라 사쿠라', '오가와 리오', '오가와 아사미', '오구라 나나', '오노 마리아', '오노 마치코', '오노 사리나', '오노 아유미', '오노우에 와카바', '오니시 린카', '오다 마코', '오바 유이', '오사와 미카', '오시마 리나', '오시마 미나미', '오시마 아이루', '오시오 유리', '오시카와 유우리', '오오바 유이', '오오바유이', '오오사와 유카', '오오사키 미카', '오오시 노조미', '오오에 유키', '오오이시 모에', '오오츠카 히나', '오오쿠라 아야네', '오오타 히로미', '오오호리 카나', '오우카 리리', '오우카 에나', '오우카 에리', '오이시 미사키', '오이치 미오', '오이카와 하루나', '오자와 미리나', '오자와 아리스', '오츠키 히비키', '오카다 리카', '오카모토 나기사', '오카자키 에미리', '오쿠 유미코', '오쿠다 사키', '오키 히토미', '오키타 안리', '오키타 유이카', '오토와 레온', '오토이 나즈나', '오토하 나나세', '오하시 미쿠', '요시자와 아키호', '요시자키 나오', '요시카와 아이미', '요츠하 메구루', '요코야마 미유키', '우노 츠구미', '우라야 마호', '우루미 유우', '우메미야 아야노', '우사기 란', '우사미 나나', '우사미 마이', '우사키 모모', '우에무라 아즈사', '우에하라 아이', '우에하라 유우미', '우에하라 유이', '우에하라 카렌', '우에하라 호나미', '우츠노미야 시온', '우치다 미나코', '유리카와 사라', '유메 카나', '유메노 아이카 ', '유우키 마이코', '유우키 마코토', '유우키 카나', '유이노', '유이카와 루리', '유즈키 아이', '유즈키 티나', '유키 마오', '유키 마유', '유키 사야카', '유키 유리카', '유키 치세', '이가와 유이', '이나가와 나츠메', '이노우에 유나', '이노우에 히토미', '이마무라 미호', '이마무라 카에데', '이마이 카논', '이마이 히로노', '이부키 린', '이시카와 루카', '이시하라 리나', '이시하라 미키', '이시하라 아유무', '이시하라 아즈사', '이이오카 카나코', '이즈미 마나', '이치노세 스즈', '이치노세 아메리', '이치조 키미카', '이치카 노아', '이치카와 마호', '이치키 미호', '이카와 스즈노', '이케가미 사쿠라코', '이쿠이나 사유리', '이타가키 아즈사', '이타노 유키', '이토 레이', '이토 베니', '이토 에리', '이토 하루카', '이하라 시오리', '준나 츠라라', '줄리아', '진 유키', '츠루타 카나', '츠바사 미사키', '츠바키 에리', '츠바키 유이', '츠바키 쿠루미', '츠보미', '츠지 사키', '츠지모토 안', '츠카다 시오리', '츠카사 미코토', '츠쿠요미 히마리', '츠키미 시오리', '츠키시로 루네', '츠키시마 아이', '치노 아즈미 ', '치아키 하나', '카가미 유이', '카나 유메', '카나사키 유메', '카나에 루카', '카라사와 미키', '카미노 하즈키', '카미사키 시오리', '카미야 마유', '카미오 마이 ', '카미조 리오나', '카미카와 미온', '카미카와 히나', '카미하타 이치카', '카스가 모나', '카스가 유이', '카스가 쿠루미', '카스가노 유이', '카스미 노아', '카스미 리사 ', '카스미 카호', '카시와기 노조미', '카시와기 미레이', '카시와기 미아', '카시와기 유리', '카야마 나츠코', '카야마 미레이', '카에데 마오', '카에데 히메키', '카와고에 유이', '카와나 미스즈', '카와나미 마이카', '카와모토 아이', '카와무라 마야', '카와세 사야카', '카와세 토모카', '카와이 안리', '카와이 유이 ', '카와이 유키노', '카와이 코코로', '카와카미 나나미', '카와카미 유', '카자마 메이', '카자마 유미', '카츠라기 나오', '카츠키 유우리', '카타히라 미우', '카토우 나오', '카토우 리나', '카호', '칸나 리사', '칸노 미이나', '칸노 시즈카', '칸노 아리사', '코가와 이오리', '코구레 카렌', '코니시 유우', '코다 리사', '코다 미라이', '코모리 리코', '코모리 아이', '코무카이 미나코', '코미네 히나타', '코미야마 유키', '코바시 에미', '코바야시 리호', '코바야시 메이 ', '코바야카와 레이코', '코사카 레이라', '코사카 메구루 ', '코사카 유리', '코우자이 사키', '코이 사야', '코이노 렌 ', '코이데 하루카', '코이즈미 노조미', '코이즈미 마유', '코이즈미 마키', '코이즈미 아리사', '코이즈미 아야 ', '코지마 미나미', '코지마 유이나', '코지마 준나', '코코로 유우카', '코토 히카루 ', '코토네 리아', '코토네 사라 ', '코토하라 미유', '코하루 아오이', '코하쿠 우타', '콘노 리노', '콘노 히카루', '쿄노 나나카', '쿄노 유이 ', '쿠라키 미오', '쿠라타 마오', '쿠로사와 아이 ', '쿠로카와 키라라', '쿠루미 히나', '크리스틴 키타지마', '키나미 히나', '키노시타 아즈미', '키노시타 와카나', '키노시타 유즈카', '키류 사쿠라', '키리시마 리온', '키리시마 사쿠라', '키리시마 체리', '키리오카 사츠키', '키리타니 유리아', '키무라 마리에', '키무라 츠나', '키무라 카나코', '키미노 미키', '키미노 아유미', '키미노 유나', '키미아미 히나', '키사키 에마', '키시 아이노', '키요미 레이', '키우치 안나', '키자키 리오나', '키자키 제시카 ', '키지마 아이리', '키타가와 나츠키', '키타가와 안주', '키타가와 에리카', '키타가와 유리', '키타가와 히토미', '키타노 노조미 ', '키타노 하루카', '타나베 리코', '타니하라 유키', '타마나 미라', '타마루 미쿠', '타마모리 유키', '타마키 마이', '타사키 유카', '타츠미 유이', '타치바나 나오 ', '타치바나 리사', '타치바나 리코', '타치바나 미스즈', '타치바나 사야', '타치바나 이즈미', '타치바나 케이코', '타치바나 쿠라라', '타치바나 쿠루미', '타치바나 하루미', '타치바나 히나타', '타카나시 아유미', '타카세 나나미', '타카시로 레이나', '타카자와 사야', '타카하시 미오', '타카하시 에밀리', '타카히데 아카리', '타케시타 사에코 ', '타케우치 마코토', '타케우치 아이 ', '타케우치 유우', '타케이 모나 ', '타키가와 레미', '타키가와 소피아 ', '타키모토아리사', '타키자와 로라', '타키자와 유나', '타키자와 히카루', '텐바 마유', '토도 마리에', '토모다 아야카', '토미나가 히로미', '토키와 린', '티아', '하나노 마리아', '하나미야 아미', '하네다 모모코', '하네다 아이', '하라 사라사', '하라 사오리', '하라 아키나', '하라 치구사', '하라다 아키에', '하라사와 유아', '하루나 마이', '하루나 하나', '하루노 리카', '하루노 아즈미', '하루사키 아즈미', '하루사키 카자리', '하루카 루리', '하루카 마나', '하루카 메구미', '하루카제 에미', '하루키 유키노', '하마사키 리오', '하마사키 마오', '하세가와 리호', '하세가와 미쿠', '하세가와 세나', '하세가와 시오리', '하세가와 시즈쿠', '하세가와 유나', '하스미 쿠레아', '하시모토 마야', '하시모토 스미레', '하야마 메이', '하야미 루리', '하야사카 히토미', '하야세 앨리스', '하야시 유나', '하야카와 린', '하야카와 세리나', '하즈키 노조미', '하즈키 카렌', '하츠네 미노리', '하츠메 리나', '하츠미 리온', '하츠미 사키', '하츠카와 미나미', '하타노 유이', '헤이와지마 유우키', '호노카', '호리구치 나츠미', '호리사키 리아', '호리우치 아케미', '호리키타 나나미', '호사카 에리', '호소카와 마리', '호시 아스카', '호시 안제', '호시나 마미', '호시노 나미', '호시노 라무', '호시노 미유', '호시노 아카리', '호시노 유이', '호시노 치사', '호시노 하루카', '호시노 히비키', '호시미 레이카', '호시미 리카', '호시미야 아이', '호시아이 히카루', '호시이 아이', '호시자와 나나', '호시조라 모아', '호시즈키 아즈', '호시카와 나츠', '호우즈키 히카루', '호조 마키', '혼다 나나미', '혼다 나미', '혼다 리코', '혼마 유리', '혼조 사유리', '후와리 유우키', '후유츠키 카에데', '후지모리 아야코', '후지사키 리오', '후지시마 유이', '후지와라 히토미', '후지이 레이나', '후지키타 아야카', '후쿠다 사야', '후쿠야마 사야카', '후타바 코노미', '히나모리 미코', '히나미 루카', '히나미 마도카', '히나타 리사', '히노 히카리', '히라기 토모미', '히라세 미쿠루', '히라야마 카오루', '히라코 에미리', '히로세 나나미', '히로세 나오미', '히로세 유나', '히메노 유우리', '히메노 코코아', '히메사키 리리아', '히메카와 리나', '히토미 린', '히토미 타나카', '히토세 아미']
# import unicodedata
#
# def download_photo(img_url, filename):
#     file_path = "%s%s" % ("/Users/hongsasung/Desktop/actor/", '%s.jpg'%filename)
#     downloaded_image = file(file_path, "wb")
#     image_on_web = urllib.urlopen(img_url)
#     while True:
#         buf = image_on_web.read(100000000)
#         if len(buf) == 0:
#             break
#         downloaded_image.write(buf)
#     downloaded_image.close()
#     image_on_web.close()
#     return file_path
# #
# list3 = []
#
# for each in list2:
#     # new = each.decode('utf-8').encode('utf-8')
#     url = 'http://www.jikbakguri.com/show2/'+each
#     download_photo(url,each)
#
#
