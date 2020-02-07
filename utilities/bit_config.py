import utilities.custom_logger as cl
import logging


class Config:
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, suiteFlagNumber=0):

        self.suiteFlagNumber = suiteFlagNumber

        ################
        # Config Flags #
        ################

        self.FLAG_Prod = 1          # Binary 00001
        self.FLAG_Staging = 2       # Binary 00010
        self.FLAG_Email = 4         # Binary 00100
        self.FLAG_Chrome = 8        # Binary 01000
        self.FLAG_Firefox = 16      # Binary 010000
        self.FLAG_Edge = 32         # Binary 0100000
        self.FLAG_Safari = 64       # Binary 01000000
        self.FLAG_Android = 128     # Binary 010000000
        self.FLAG_Ios = 256         # Binary 0100000000
        self.FLAG_Suite = 512       # Binary 01000000000
        self.FLAG_MobileApp = 1024  # Binary 010000000000
        self.FLAG_Cloud = 2048      # Binary 0100000000000
        self.FLAG_Grid = 4096       # Binary 01000000000000
        self.FLAG_Local = 8192      # Binary 010000000000000

    def display_suite_bits(self):
        """
        display suite bits
        """
        self.log.info("display_suite_bits")
        bits = ""

        if self.check_suite_prod():
            bits = "1" + bits
        else:
            bits = "0" + bits

        if self.check_suite_staging():
            bits = "1" + bits
        else:
            bits = "0" + bits

        if self.check_suite_email():
            bits = "1" + bits
        else:
            bits = "0" + bits

        if self.check_suite_chrome():
            bits = "1" + bits
        else:
            bits = "0" + bits

        if self.check_suite_firefox():
            bits = "1" + bits
        else:
            bits = "0" + bits

        if self.check_suite_edge():
            bits = "1" + bits
        else:
            bits = "0" + bits

        if self.check_suite_safari():
            bits = "1" + bits
        else:
            bits = "0" + bits

        if self.check_suite_android():
            bits = "1" + bits
        else:
            bits = "0" + bits

        if self.check_suite_ios():
            bits = "1" + bits
        else:
            bits = "0" + bits

        if self.check_suite_suite():
            bits = "1" + bits
        else:
            bits = "0" + bits

        if self.check_suite_mobileapp():
            bits = "1" + bits
        else:
            bits = "0" + bits

        if self.check_suite_cloud():
            bits = "1" + bits
        else:
            bits = "0" + bits

        if self.check_suite_grid():
            bits = "1" + bits
        else:
            bits = "0" + bits

        if self.check_suite_local():
            bits = "1" + bits
        else:
            bits = "0" + bits

        return bits

    def get_bits(self, _num):
        """
        git bits
        """
        self.log.info("get_bits - number = " + str(_num))
        bits = ""

        if self.prod(_num):
            bits = "1" + bits
        else:
            bits = "0" + bits

        if self.staging(_num):
            bits = "1" + bits
        else:
            bits = "0" + bits

        if self.email(_num):
            bits = "1" + bits
        else:
            bits = "0" + bits

        if self.chrome(_num):
            bits = "1" + bits
        else:
            bits = "0" + bits

        if self.firefox(_num):
            bits = "1" + bits
        else:
            bits = "0" + bits

        if self.edge(_num):
            bits = "1" + bits
        else:
            bits = "0" + bits

        if self.safari(_num):
            bits = "1" + bits
        else:
            bits = "0" + bits

        if self.android(_num):
            bits = "1" + bits
        else:
            bits = "0" + bits

        if self.ios(_num):
            bits = "1" + bits
        else:
            bits = "0" + bits

        if self.suite(_num):
            bits = "1" + bits
        else:
            bits = "0" + bits

        if self.mobileapp(_num):
            bits = "1" + bits
        else:
            bits = "0" + bits

        if self.cloud(_num):
            bits = "1" + bits
        else:
            bits = "0" + bits

        if self.grid(_num):
            bits = "1" + bits
        else:
            bits = "0" + bits

        if self.local(_num):
            bits = "1" + bits
        else:
            bits = "0" + bits

        return bits

    def display_config(self, _num):
        """
        display config
        """
        self.log.info("display_config - number = " + str(_num))
        bits = ""

        if self.prod(_num):
            print("Suite Prod : 1")
            self.log.info("Suite Prod : 1")
            bits = "1" + bits
        else:
            print("Suite Prod : 0")
            self.log.info("Suite Prod : 0")
            bits = "0" + bits

        if self.staging(_num):
            print("Suite Staging : 1")
            self.log.info("Suite Staging : 1")
            bits = "1" + bits
        else:
            print("Suite Staging : 0")
            self.log.info("Suite Staging : 0")
            bits = "0" + bits

        if self.email(_num):
            print("Suite Email : 1")
            self.log.info("Suite Email : 1")
            bits = "1" + bits
        else:
            print("Suite Email : 0")
            self.log.info("Suite Email : 0")
            bits = "0" + bits

        if self.chrome(_num):
            print("Suite Chrome : 1")
            self.log.info("Suite Chrome : 1")
            bits = "1" + bits
        else:
            print("Suite Chrome : 0")
            self.log.info("Suite Chrome : 0")
            bits = "0" + bits

        if self.firefox(_num):
            print("Suite Firefox : 1")
            self.log.info("Suite Firefox : 1")
            bits = "1" + bits
        else:
            print("Suite Firefox : 0")
            self.log.info("Suite Firefox : 0")
            bits = "0" + bits

        if self.edge(_num):
            print("Suite Edge : 1")
            self.log.info("Suite Edge : 1")
            bits = "1" + bits
        else:
            print("Suite Edge : 0")
            self.log.info("Suite Edge : 0")
            bits = "0" + bits

        if self.safari(_num):
            print("Suite Safari : 1")
            self.log.info("Suite Safari : 1")
            bits = "1" + bits
        else:
            print("Suite Safari : 0")
            self.log.info("Suite Safari : 0")
            bits = "0" + bits

        if self.android(_num):
            print("Suite Android : 1")
            self.log.info("Suite Android : 1")
            bits = "1" + bits
        else:
            print("Suite Android : 0")
            self.log.info("Suite Android : 0")
            bits = "0" + bits

        if self.ios(_num):
            print("Suite IOS : 1")
            self.log.info("Suite IOS : 1")
            bits = "1" + bits
        else:
            print("Suite IOS : 0")
            self.log.info("Suite IOS: 0")
            bits = "0" + bits

        if self.suite(_num):
            print("Suite Suite : 1")
            self.log.info("Suite Suite : 1")
            bits = "1" + bits
        else:
            print("Suite Suite : 0")
            self.log.info("Suite Suite : 0")
            bits = "0" + bits

        if self.mobileapp(_num):
            print("Suite MobileApp : 1")
            self.log.info("Suite MobileApp : 1")
            bits = "1" + bits
        else:
            print("Suite MobileApp : 0")
            self.log.info("Suite MobileApp : 0")
            bits = "0" + bits

        if self.cloud(_num):
            self.log.info("Suite Cloud : 1")
            print("Suite Cloud : 1")
            bits = "1" + bits
        else:
            self.log.info("Suite Cloud : 0")
            print("Suite Cloud : 0")
            bits = "0" + bits

        if self.grid(_num):
            self.log.info("Suite Grid : 1")
            print("Suite Grid : 1")
            bits = "1" + bits
        else:
            self.log.info("Suite Grid : 0")
            print("Suite Grid : 0")
            bits = "0" + bits

        if self.local(_num):
            self.log.info("Suite Local : 1")
            print("Suite Local : 1")
            bits = "1" + bits
        else:
            self.log.info("Suite Local : 0")
            print("Suite Local : 0")
            bits = "0" + bits

        self.log.info("Value of suite is " + str(_num) + " Binary " + str(bits))
        print("Value of suite is " + str(_num) + " Binary " + str(bits))

    def display_suite_config(self):
        """
        display suite config
        """
        self.log.info("display_suite_config")
        bits = ""

        if self.check_suite_prod():
            self.log.info("Suite Prod : 1")
            print("Suite Prod : 1")
            bits = "1" + bits
        else:
            self.log.info("Suite Prod : 0")
            print("Suite Prod : 0")
            bits = "0" + bits

        if self.check_suite_staging():
            self.log.info("Suite Staging : 1")
            print("Suite Staging : 1")
            bits = "1" + bits
        else:
            self.log.info("Suite Staging : 0")
            print("Suite Staging : 0")
            bits = "0" + bits

        if self.check_suite_email():
            self.log.info("Suite Email : 1")
            print("Suite Email : 1")
            bits = "1" + bits
        else:
            self.log.info("Suite Email : 0")
            print("Suite Email : 0")
            bits = "0" + bits

        if self.check_suite_chrome():
            self.log.info("Suite Chrome : 1")
            print("Suite Chrome : 1")
            bits = "1" + bits
        else:
            self.log.info("Suite Chrome : 0")
            print("Suite Chrome : 0")
            bits = "0" + bits

        if self.check_suite_firefox():
            self.log.info("Suite Firefox : 1")
            print("Suite Firefox : 1")
            bits = "1" + bits
        else:
            self.log.info("Suite Firefox : 0")
            print("Suite Firefox : 0")
            bits = "0" + bits

        if self.check_suite_edge():
            self.log.info("Suite Edge : 1")
            print("Suite Edge : 1")
            bits = "1" + bits
        else:
            self.log.info("Suite Edge : 0")
            print("Suite Edge : 0")
            bits = "0" + bits

        if self.check_suite_safari():
            self.log.info("Suite Safari : 1")
            print("Suite Safari : 1")
            bits = "1" + bits
        else:
            print("Suite Safari : 0")
            self.log.info("Suite Safari : 0")
            bits = "0" + bits

        if self.check_suite_android():
            self.log.info("Suite Android : 1")
            print("Suite Android : 1")
            bits = "1" + bits
        else:
            self.log.info("Suite Android : 0")
            print("Suite Android : 0")
            bits = "0" + bits

        if self.check_suite_ios():
            self.log.info("Suite IOS : 1")
            print("Suite IOS : 1")
            bits = "1" + bits
        else:
            self.log.info("Suite IOS : 0")
            print("Suite IOS : 0")
            bits = "0" + bits

        if self.check_suite_suite():
            self.log.info("Suite Suite : 1")
            print("Suite Suite : 1")
            bits = "1" + bits
        else:
            self.log.info("Suite Suite : 0")
            print("Suite Suite : 0")
            bits = "0" + bits

        if self.check_suite_mobileapp():
            self.log.info("Suite MobileApp : 1")
            print("Suite MobileApp : 1")
            bits = "1" + bits
        else:
            self.log.info("Suite MobileApp : 0")
            print("Suite MobileApp : 0")
            bits = "0" + bits

        if self.check_suite_cloud():
            self.log.info("Suite Cloud : 1")
            print("Suite Cloud : 1")
            bits = "1" + bits
        else:
            self.log.info("Suite Cloud : 0")
            print("Suite Cloud : 0")
            bits = "0" + bits

        if self.check_suite_grid():
            self.log.info("Suite Grid : 1")
            print("Suite Grid : 1")
            bits = "1" + bits
        else:
            self.log.info("Suite Grid : 0")
            print("Suite Grid : 0")
            bits = "0" + bits

        if self.check_suite_local():
            self.log.info("Suite Local : 1")
            print("Suite Local : 1")
            bits = "1" + bits
        else:
            self.log.info("Suite Local : 0")
            print("Suite Local : 0")
            bits = "0" + bits

        self.log.info("Value of suite is " + str(self.suiteFlagNumber) + " Binary " + str(bits))
        print("Value of suite is " + str(self.suiteFlagNumber) + " Binary " + str(bits))

    def set_suite_prod(self):
        """
        set suite prod
        Operator: | Binary OR
        """
        self.suiteFlagNumber = self.suiteFlagNumber | self.FLAG_Prod

        self.log.info("set_suite_prod - Value of suite is " + str(self.suiteFlagNumber) + " Decimal " +
                      str(self.FLAG_Prod) + " (Prod Binary 00001)")

        print("set_suite_prod - Value of suite is " + str(self.suiteFlagNumber) + " Decimal " +
              str(self.FLAG_Prod) + " (Prod Binary 00001)")

    def set_suite_staging(self):
        """
        set suite staging
        Operator: | Binary OR
        """
        self.suiteFlagNumber = self.suiteFlagNumber | self.FLAG_Staging

        self.log.info("set_suite_staging - Value of suite is " + str(self.suiteFlagNumber) + " Decimal " + str(self.FLAG_Staging) + " (Prod Binary 00010)")

        print("set_suite_staging - Value of suite is " + str(self.suiteFlagNumber) + " Decimal " + str(self.FLAG_Staging) + " (Prod Binary 00010)")

    def set_suite_email(self):
        """
        set suite email
        Operator: | Binary OR
        """
        self.suiteFlagNumber = self.suiteFlagNumber | self.FLAG_Email

        self.log.info("set_suite_email - Value of suite is " +  str(self.suiteFlagNumber) + " Decimal" + str(self.FLAG_Email) + " (Email Binary 00100")

        print("set_suite_email - Value of suite is " + str(self.suiteFlagNumber) + " Decimal" + str(self.FLAG_Email) + " (Email Binary 00100")

    def set_suite_chrome(self):
        """
        set suite chrome
        Operator: | Binary OR
        """
        self.suiteFlagNumber = self.suiteFlagNumber | self.FLAG_Chrome

        self.log.info("set_suite_chrome - Value of suite is " + str(self.suiteFlagNumber) + " Decimal" + str(self.FLAG_Chrome) + " (Chrome Binary 01000")

        print("set_suite_chrome - Value of suite is " +  str(self.suiteFlagNumber) + " Decimal" + str(self.FLAG_Chrome) + " (Chrome Binary 01000")

    def set_suite_firefox(self):
        """
        set suite firefox
        Operator: | Binary OR
        """

        self.suiteFlagNumber = self.suiteFlagNumber | self.FLAG_Firefox

        self.log.info("set_suite_firefox - Value of suite is " + str(self.suiteFlagNumber) + " Decimal" + str(self.FLAG_Firefox) + " (Firefox Binary 010000")

        print("set_suite_firefox - Value of suite is " + str(self.suiteFlagNumber) + " Decimal" + str(self.FLAG_Firefox) + " (Firefox Binary 010000")

    def set_suite_edge(self):
        """
        set suite edge
        Operator: | Binary OR
        """

        self.suiteFlagNumber = self.suiteFlagNumber | self.FLAG_Edge

        self.log.info("set_suite_edge - Value of suite is " + str(self.suiteFlagNumber) + " Decimal" + str(self.FLAG_Edge) + " (Edge Binary 0100000")

        print("set_suite_edge - Value of suite is " + str(self.suiteFlagNumber) + " Decimal" + str(self.FLAG_Edge) + " (Edge Binary 0100000")

    def set_suite_safari(self):
        """
        set suite safari
        Operator: | Binary OR
        """

        self.suiteFlagNumber = self.suiteFlagNumber | self.FLAG_Safari

        self.log.info("set_suite_edge - Value of suite is " +  str(self.suiteFlagNumber) + " Decimal" + str(self.FLAG_Safari) + " (Safari Binary 01000000")

        print("set_suite_edge - Value of suite is " + str(self.suiteFlagNumber) + " Decimal" + str(self.FLAG_Safari) + " (Safari Binary 01000000")

    def set_suite_android(self):
        """
        set suite android
        Operator: | Binary OR
        """
        self.suiteFlagNumber = self.suiteFlagNumber | self.FLAG_Android

        self.log.info("set_suite_android - Value of suite is " + str(self.suiteFlagNumber) + " Decimal" + str(self.FLAG_Android) + " (Android Binary 010000000")

        print("set_suite_android - Value of suite is " + str(self.suiteFlagNumber) + " Decimal" + str(self.FLAG_Android) + " (Android Binary 010000000")

    def set_suite_ios(self):
        """
        set suite ios
        Operator: | Binary OR
        """
        self.suiteFlagNumber = self.suiteFlagNumber | self.FLAG_Ios

        self.log.info("set_suite_android - Value of suite is " + str(self.suiteFlagNumber) + " Decimal" + str(self.FLAG_Ios) + " (Android IOS 0100000000")

        print("set_suite_android - Value of suite is " +  str(self.suiteFlagNumber) + " Decimal" + str(self.FLAG_Ios) + " (Android IOS 0100000000")

    def set_suite_suite(self):
        """
        set suite suite
        Operator: | Binary OR
        """
        self.suiteFlagNumber = self.suiteFlagNumber | self.FLAG_Suite

        self.log.info("set_suite_android - Value of suite is " + str(self.suiteFlagNumber) + " Decimal" + str(self.FLAG_Suite) + " (Android Suite 01000000000")

        print("set_suite_android - Value of suite is " + str(self.suiteFlagNumber) + " Decimal" + str(self.FLAG_Suite) + " (Android Suite 01000000000")

    def set_suite_mobileapp(self):
        """
        set suite mobileapp
        Operator: | Binary OR
        """
        self.suiteFlagNumber = self.suiteFlagNumber | self.FLAG_MobileApp

        self.log.info("set_suite_mobileapp - Value of suite is " + str(self.suiteFlagNumber) + " Decimal" + str(self.FLAG_MobileApp) + " (Android Suite 010000000000")

        print("set_suite_mobileapp - Value of suite is " +  str(self.suiteFlagNumber) + " Decimal" + str(self.FLAG_MobileApp) + " (Android Suite 010000000000")

    def set_suite_cloud(self):
        """
        set suite cloud
        Operator: | Binary OR
        """
        self.suiteFlagNumber = self.suiteFlagNumber | self.FLAG_Cloud

        self.log.info("set_suite_cloud - Value of suite is " + str(self.suiteFlagNumber) + " Decimal" + str(self.FLAG_Cloud) + " (Android Suite 0100000000000")

        print("set_suite_cloud - Value of suite is " + str(self.suiteFlagNumber) + " Decimal" + str(self.FLAG_Cloud) + " (Android Suite 0100000000000")

    def set_suite_grid(self):
        """
        set suite grid
        Operator: | Binary OR
        """
        self.suiteFlagNumber = self.suiteFlagNumber | self.FLAG_Grid

        self.log.info("set_suite_grid - Value of suite is " + str(self.suiteFlagNumber) + " Decimal" + str(self.FLAG_Grid) + " (Android Suite 01000000000000")

        print("set_suite_grid - Value of suite is " + str(self.suiteFlagNumber) + " Decimal" + str(self.FLAG_Grid) + " (Android Suite 01000000000000")

    def set_suite_local(self):
        """
        set suite local
        Operator: | Binary OR
        """
        self.suiteFlagNumber = self.suiteFlagNumber | self.FLAG_Local

        self.log.info("set_suite_grid - Value of suite is " + str(self.suiteFlagNumber) + " Decimal" + str(self.FLAG_Local) + " (Android Suite 010000000000000")

        print("set_suite_grid - Value of suite is " + str(self.suiteFlagNumber) + " Decimal" + str(self.FLAG_Local) + " (Android Suite 010000000000000")

    def get_suite_flag_number(self):
        """
        get suite flag number
        """
        self.log.info("get_suite_flag_number = " + str(self.suiteFlagNumber))
        return self.suiteFlagNumber

    # Checking the flag - To test the value of a flag, use bitwise AND:
    def prod(self, _flagNumber):
        """
        prod
        Check flag - bitwise AND
        """
        return _flagNumber & self.FLAG_Prod == self.FLAG_Prod

    def staging(self, _flagNumber):
        """
        staging
        Check flag - bitwise AND
        """
        return _flagNumber & self.FLAG_Staging == self.FLAG_Staging

    def email(self, _flagNumber):
        """
        email
        Check flag - bitwise AND
        """
        return _flagNumber & self.FLAG_Email == self.FLAG_Email

    def chrome(self, _flagNumber):
        """
        chrome
        Check flag - bitwise AND
        """
        return _flagNumber & self.FLAG_Chrome == self.FLAG_Chrome

    def firefox(self, _flagNumber):
        """
        firefox
        Check flag - bitwise AND
        """
        return _flagNumber & self.FLAG_Firefox == self.FLAG_Firefox

    def edge(self, _flagNumber):
        """
        edge
        Check flag - bitwise AND
        """
        return _flagNumber & self.FLAG_Edge == self.FLAG_Edge

    def safari(self, _flagNumber):
        """
        safari
        Check flag - bitwise AND
        """
        return _flagNumber & self.FLAG_Safari == self.FLAG_Safari

    def android(self, _flagNumber):
        """
        android
        Check flag - bitwise AND
        """
        return _flagNumber & self.FLAG_Android == self.FLAG_Android

    def ios(self, _flagNumber):
        """
        ios
        Check flag - bitwise AND
        """
        return _flagNumber & self.FLAG_Ios == self.FLAG_Ios

    def suite(self, _flagNumber):
        """
        suite
        Check flag - bitwise AND
        """
        return _flagNumber & self.FLAG_Suite == self.FLAG_Suite

    def mobileapp(self, _flagNumber):
        """
        mobileapp
        Check flag - bitwise AND
        """
        return _flagNumber & self.FLAG_MobileApp == self.FLAG_MobileApp

    def cloud(self, _flagNumber):
        """
        cloud
        Check flag - bitwise AND
        """
        return _flagNumber & self.FLAG_Cloud == self.FLAG_Cloud

    def grid(self, _flagNumber):
        """
        grid
        Check flag - bitwise AND
        """
        return _flagNumber & self.FLAG_Grid == self.FLAG_Grid

    def local(self, _flagNumber):
        """
        local
        Check flag - bitwise AND
        """
        return _flagNumber & self.FLAG_Local == self.FLAG_Local

    def check_suite_prod(self):
        """
        check suite prod
        Check flag - bitwise AND
        """
        return self.suiteFlagNumber & self.FLAG_Prod == self.FLAG_Prod

    def check_suite_staging(self):
        """
        check suite staging
        Check flag - bitwise AND
        """
        return self.suiteFlagNumber & self.FLAG_Staging == self.FLAG_Staging

    def check_suite_email(self):
        """
        check suite email
        Check flag - bitwise AND
        """
        return self.suiteFlagNumber & self.FLAG_Email == self.FLAG_Email

    def check_suite_chrome(self):
        """
        check suite chrome
        Check flag - bitwise AND
        """
        return self.suiteFlagNumber & self.FLAG_Chrome == self.FLAG_Chrome

    def check_suite_firefox(self):
        """
        check suite firefox
        Check flag - bitwise AND
        """
        return self.suiteFlagNumber & self.FLAG_Firefox == self.FLAG_Firefox

    def check_suite_edge(self):
        """
        check suite edge
        Check flag - bitwise AND
        """
        return self.suiteFlagNumber & self.FLAG_Edge == self.FLAG_Edge

    def check_suite_safari(self):
        """
        check suite safari
        Check flag - bitwise AND
        """
        return self.suiteFlagNumber & self.FLAG_Safari == self.FLAG_Safari

    def check_suite_android(self):
        """
        check suite android
        Check flag - bitwise AND
        """
        return self.suiteFlagNumber & self.FLAG_Android == self.FLAG_Android

    def check_suite_ios(self):
        """
        check suite ios
        Check flag - bitwise AND
        """
        return self.suiteFlagNumber & self.FLAG_Ios == self.FLAG_Ios

    def check_suite_suite(self):
        """
        check suite suite
        Check flag - bitwise AND
        """
        return self.suiteFlagNumber & self.FLAG_Suite == self.FLAG_Suite

    def check_suite_mobileapp(self):
        """
        check suite mobileapp
        Check flag - bitwise AND
        """
        return self.suiteFlagNumber & self.FLAG_MobileApp == self.FLAG_MobileApp

    def check_suite_cloud(self):
        """
        check suite cloud
        Check flag - bitwise AND
        """
        return self.suiteFlagNumber & self.FLAG_Cloud == self.FLAG_Cloud

    def check_suite_grid(self):
        """
        check suite grid
        Check flag - bitwise AND
        """
        return self.suiteFlagNumber & self.FLAG_Grid == self.FLAG_Grid

    def check_suite_local(self):
        """
        check suite local
        Check flag - bitwise AND
        """
        return self.suiteFlagNumber & self.FLAG_Local == self.FLAG_Local

    #################
    # Flipping Bits #
    #################

    def flip_suite_prod(self):
        """
        flip suite prod
        Flipping Bits  - bitwise AND
        """
        self.suiteFlagNumber = self.suiteFlagNumber & ~ self.FLAG_Prod
        self.log.info("flip_suite_prod")
        print("flip_suite_prod")

    def flip_suite_staging(self):
        """
        flip suite staging
        Flipping Bits  - bitwise AND
        """
        self.suiteFlagNumber = self.suiteFlagNumber & ~ self.FLAG_Staging
        self.log.info("flip_suite_staging")
        print("flip_suite_staging")

    def flip_suite_email(self):
        """
        flip suite email
        Flipping Bits  - bitwise AND
        """
        self.suiteFlagNumber = self.suiteFlagNumber & ~ self.FLAG_Email
        self.log.info("flip_suite_email")
        print("flip_suite_email")

    def flip_suite_chrome(self):
        """
        flip suite chrome
        Flipping Bits  - bitwise AND
        """
        self.suiteFlagNumber = self.suiteFlagNumber & ~ self.FLAG_Chrome
        self.log.info("flip_suite_chrome")
        print("flip_suite_chrome")

    def flip_suite_firefox(self):
        """
        flip suite firefox
        Flipping Bits  - bitwise AND
        """
        self.suiteFlagNumber = self.suiteFlagNumber & ~ self.FLAG_Firefox
        self.log.info("flip_suite_firefox")
        print("flip_suite_firefox")

    def flip_suite_edge(self):
        """
        flip suite edge
        Flipping Bits  - bitwise AND
        """
        self.suiteFlagNumber = self.suiteFlagNumber & ~ self.FLAG_Edge
        self.log.info("flip_suite_edge")
        print("flip_suite_edge")

    def flip_suite_safari(self):
        """
        flip suite safari
        Flipping Bits  - bitwise AND
        """
        self.suiteFlagNumber = self.suiteFlagNumber & ~ self.FLAG_Safari
        self.log.info("flip_suite_safari")
        print("flip_suite_safari")

    def flip_suite_android(self):
        """
        flip suite android
        Flipping Bits  - bitwise AND
        """
        self.suiteFlagNumber = self.suiteFlagNumber & ~ self.FLAG_Android
        self.log.info("flip_suite_android")
        print("flip_suite_android")

    def flip_suite_ios(self):
        """
        flip suite ios
        Flipping Bits  - bitwise AND
        """
        self.suiteFlagNumber = self.suiteFlagNumber & ~ self.FLAG_Ios
        self.log.info("flip_suite_ios")
        print("flip_suite_ios")

    def flip_suite_suite(self):
        """
        flip suite suite
        Flipping Bits  - bitwise AND
        """
        self.suiteFlagNumber = self.suiteFlagNumber & ~ self.FLAG_Suite
        self.log.info("flip_suite_suite")
        print("flip_suite_suite")

    def flip_suite_mobileapp(self):
        """
        flip suite mobileapp
        Flipping Bits  - bitwise AND
        """
        self.suiteFlagNumber = self.suiteFlagNumber & ~ self.FLAG_MobileApp
        self.log.info("flip_suite_mobileapp")
        print("flip_suite_mobileapp")

    def flip_suite_cloud(self):
        """
        flip suite cloud
        Flipping Bits  - bitwise AND
        """
        self.suiteFlagNumber = self.suiteFlagNumber & ~ self.FLAG_Cloud
        self.log.info("flip_suite_cloud")
        print("flip_suite_cloud")

    def flip_suite_grid(self):
        """
        flip suite grid
        Flipping Bits  - bitwise AND
        """
        self.suiteFlagNumber = self.suiteFlagNumber & ~ self.FLAG_Grid
        self.log.info("flip_suite_grid")
        print("flip_suite_grid")

    def flip_suite_local(self):
        """
        flip suite local
        Flipping Bits  - bitwise AND
        """
        self.suiteFlagNumber = self.suiteFlagNumber & ~ self.FLAG_Local
        self.log.info("flip_suite_local")
        print("flip_suite_local")

    def flip_all_suite_bits(self):
        """
        flip all suite bits
        Flipping Bits  - bitwise AND
        """
        self.suiteFlagNumber = ~ self.suiteFlagNumber
        self.log.info("flip_suite_suite")
        print("flip_suite_suite")

    def clear_all_suite_bits(self):
        """
        clear all suite bits
        """
        self.suiteFlagNumber = 0
        self.log.info("clear_all_suite_bits")
        print("clear_all_suite_bits")

    def configBuilder(self):
        """
        config builder
        """
        config = Config()
        print("Configuration Builder")
        while True:
            action = input("Select to build a config? \n[P]roduction, [S]taging, [E]mail, \n[C]hrome, [F]irefox, "
                           "[V] IE Edge, \n[M] Safari, [A]ndroid, [I]os, [U] Suite, \n[B] MobileApp, [D] Cloud, "
                           "[G]rid  [L]ocal \n[Y] Clear Bits or \n[Z] Flip Bits \n [R]un Test ? " + "\n").upper()
            if action not in "PSECFVMAIUBDGLYZR" or len(action) != 1:
                print("I don't know how to do that")
                continue
            beforeBits = config.display_suite_bits()

            if action == 'P':
                # Prod
                if config.check_suite_staging():
                    config.flip_suite_staging()
                config.set_suite_prod()

            elif action == 'S':
                # Staging
                if config.check_suite_prod():
                    config.flip_suite_prod()

                config.set_suite_staging()

            elif action == 'E':
                # Email
                config.set_suite_email()

            elif action == 'C':

                # Chrome
                if config.check_suite_firefox():
                    config.flip_suite_firefox()

                if config.check_suite_edge():
                    config.flip_suite_edge()

                if config.check_suite_safari():
                    config.flip_suite_safari()

                if config.check_suite_ios():
                    config.flip_suite_ios()

                config.set_suite_chrome()

            elif action == 'F':
                # firefox
                if config.check_suite_chrome():
                    config.flip_suite_chrome()

                if config.check_suite_edge():
                    config.flip_suite_edge()

                if config.check_suite_safari():
                    config.flip_suite_safari()

                if config.check_suite_ios():
                    config.flip_suite_ios()

                config.set_suite_firefox()

            elif action == 'V':
                # Edge
                if config.check_suite_chrome():
                    config.flip_suite_chrome()

                if config.check_suite_firefox():
                    config.flip_suite_firefox()

                if config.check_suite_safari():
                    config.flip_suite_safari()

                if config.check_suite_ios():
                    config.flip_suite_ios()

                config.set_suite_edge()

            elif action == 'M':
                # Safari
                if config.check_suite_chrome():
                    config.flip_suite_chrome()

                if config.check_suite_firefox():
                    config.flip_suite_firefox()

                if config.check_suite_edge():
                    config.flip_suite_edge()

                if config.check_suite_android():
                    config.flip_suite_android()

                if not config.check_suite_ios():
                    config.flip_suite_ios()

                config.set_suite_safari()

            elif action == 'A':
                # Android Device

                if config.check_suite_safari():
                    config.flip_suite_safari()

                if config.check_suite_ios():
                    config.flip_suite_ios()

                if not config.check_suite_grid():
                    config.flip_suite_grid()

                config.set_suite_android()

            elif action == 'I':
                # Ios Device
                if config.check_suite_android():
                    config.flip_suite_android()

                if config.check_suite_chrome():
                    config.flip_suite_chrome()

                if config.check_suite_edge():
                    config.flip_suite_edge()

                if config.check_suite_chrome():
                    config.flip_suite_chrome()

                config.set_suite_ios()

            elif action == 'U':
                config.set_suite_suite()

            elif action == 'B':
                # Mobile Application
                # If it's a hybrid app it may have a browser defined to is.
                config.set_suite_mobileapp()

            elif action == 'D':
                # Cloud - Sauce Labs
                if config.check_suite_local():
                    config.flip_suite_local()

                if config.check_suite_grid():
                    config.flip_suite_grid()

                config.set_suite_cloud()

            elif action == 'G':
                # Grid
                if config.check_suite_local():
                    config.flip_suite_local()

                if config.check_suite_cloud():
                    config.flip_suite_cloud()

                config.set_suite_grid()

            elif action == 'L':
                # Local - Same computer as Jenkins
                if config.check_suite_grid():
                    config.flip_suite_grid()

                if config.check_suite_cloud():
                    config.flip_suite_cloud()

                config.set_suite_local()

            elif action == 'Y':
                config.clear_all_suite_bits()

            elif action == 'Z':
                config.flip_all_suite_bits()
            elif action == 'R':
                return config.suiteFlagNumber

            config.display_suite_config()

            self.log.info("Before : " + str(beforeBits))
            print("Before : " + str(beforeBits))
            b = config.display_suite_bits()
            self.log.info("After  : " + str(b))
            print("After  : " + str(b))
