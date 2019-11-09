
# -*- coding=UTF-8 -*-
# author: cody.guo

import sys
sys.path.append(sys.path[0] + r"\\home")
sys.path.append(sys.path[0] + r"\\login")
sys.path.append(sys.path[0] + r"\\user")
sys.path.append(sys.path[0] + r"\\network")
sys.path.append(sys.path[0] + r"\\policy")
sys.path.append(sys.path[0] + r"\\policy\\strategyBased")
sys.path.append(sys.path[0]+ r"\\policy\\controllerConfiguration")
from home import *
from login import *
from user import *
from network import *
from policy import *
from controllerConfiguration import *
from strategyBased import *


# 用例文件列表
def caselist():
    alltestnames = [
                    iman_login_control.TestContrologin,
                    iman_login_server.TestServerLogin,
                    iman_login_cloud.TestCloudlogin,
                    iman_Device_fingerprint.TestDevFinger,
                    iman_Mac_manager.TestMacManager,
                    iman_Device_type.TestDevice_type,
                    iman_ip_manager.TestIpManager,
                    iman_Port_manager.TestPortManager,
                    iman_Station_manager.TestStationManager,
                    iman_nat_manager.TestNatManager,
                    iman_application_exception.TestApplicationException,
                    iman_dhcp_configuration.TestDHCPConfiguration,
                    iman_exceptional_IP_section.TestExceptionIPSection,
                    iman_exceptional_domain_name.TestException_domain_name,
                    iman_ip_exception.TestIPException,
                    iman_mac_exception.TestMACException,
                    iman_isolation_ip.TestIsolationIP,
                    iman_isolation_url.Testisolationurl,
                    iman_ip_mapping.TestIpMapping,
                    iman_control_ip.TestControlIP,
                    iman_application_certification.TestApplication,
                    iman_download_program_manager.TestDownloadProgram,              
                    iman_registration_form.TestRegistration_form,
                    iman_time_quantum.TestTimequantum,
                    iman_warn_level_management.TestWarnLevelManager,
                    iman_warning_information.TestWarnInformation,
                    iman_welcome_temple.TestWelcome,
                    iman_WebAppStyle.Testwebappstyle,
                    iman_dept_manager.TestDeptManager,  
                    iman_guest_class.TestGuestManager,
                    iman_user_manager.TestUserManager,
                    iman_adRegion_manager.TestADRegionUserManager,
                    iman_guest_manager.TestGuestManager,
                    iman_radius_manager.TestRadiusUserManager,                    
                    iman_license.Test_license,
                    iman_systemPatch_management.TestSystemPatchManager,
                    ]

    print("success read case list!!")
    return alltestnames